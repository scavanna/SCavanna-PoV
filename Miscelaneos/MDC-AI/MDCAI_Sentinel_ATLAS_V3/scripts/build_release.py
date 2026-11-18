from __future__ import annotations

import csv
import io
import json
import re
from collections import Counter
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo

import azure_artifacts

ROOT = Path(__file__).resolve().parents[1]
PROFILE_ALIAS = "MDCAI_V3_Profiles"
RELATION_ALIAS = "MDCAI_V3_Relations"
SCENARIO_ALIAS = "MDCAI_V3_CAAT"
ATLAS_ALIAS = "MDCAI_V3_ATLAS"
RELATIONS = {"direct", "conditional", "context"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def csv_content(rows: list[dict]) -> str:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, list(rows[0]), lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def unique_index(rows: list[dict], key: str) -> dict:
    result = {row[key]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError(f"{key}: hay claves duplicadas")
    return result


def build_model(ref: dict, policy: dict) -> dict:
    release = policy["release"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", release):
        raise ValueError(f"Versión de mapeo inválida: {release}")
    if any(not re.fullmatch(r"[\w .()-]+", name) for name in policy["product_names"]):
        raise ValueError("Nombre de producto no válido para el filtro desplegable")
    cat = unique_index(ref["catalog"], "alert_type")
    scenarios = unique_index(ref["caat"], "id")
    assessment = {r[0]: r[1:] for r in policy["scenario_assessment"]}
    if len(scenarios) != 14 or set(assessment) != set(scenarios) or len(assessment) != len(policy["scenario_assessment"]):
        raise ValueError("Comprobar el catálogo CAAT: faltantes, duplicados o escenarios sin disposición")
    if set(cat) != set(policy["rules"]):
        raise ValueError(f"Alertas sin política: {sorted(cat.keys() - policy['rules'].keys())}; fuera de catálogo: {sorted(policy['rules'].keys() - cat.keys())}")
    atlas = ref["atlas"]
    vocab = atlas["techniques"]
    tactics = atlas["tactics"]
    if len(ref["owasp"]) != 2 or any(len(risks) != 10 for risks in ref["owasp"].values()):
        raise ValueError("El diccionario OWASP debe incluir las diez categorías de cada edición")
    for old, new in atlas["migrations"].items():
        if old in vocab or new not in vocab:
            raise ValueError(f"Migración incoherente con la versión ATLAS: {old} → {new}")
    atlas_rows = []
    for tid, technique in sorted(vocab.items()):
        ids = sorted(set(technique["tactics"]))
        atlas_rows.append(dict(
            TechniqueId=tid, TechniqueName=technique["name"], TacticIds=";".join(ids),
            TacticNames=";".join(tactics[i] for i in ids), ATLASVersion=atlas["version"], TechniqueUrl=technique["url"],
        ))
    profiles, full_links, caat_rows, caat_links = [], [], [], []
    candidates = {}
    for alert_type, alert in cat.items():
        rule = policy["rules"][alert_type]
        links = []
        seen = set()
        for fw, tid, level, evidence in rule["links"]:
            if level not in RELATIONS or not evidence.strip() or (fw, tid) in seen:
                raise ValueError(f"Relación duplicada, vacía o de tipo inválido: {alert_type}/{fw}/{tid}")
            seen.add((fw, tid))
            if fw == "CAAT":
                target = scenarios[tid]
                framework, version, name, url = fw, target["source_date"], target["label"], target["url"]
            elif fw == "ATLAS":
                target = vocab[tid]
                framework, version, name, url = fw, atlas["version"], target["name"], target["url"]
            elif fw in {"OWASP-2025", "OWASP-2026"}:
                framework, version = "OWASP-LLM", fw.rsplit("-", 1)[1]
                target = ref["owasp"][version][tid]
                name, url = target["name"], target["url"]
            else:
                raise ValueError(f"Framework desconocido: {fw}")
            links.append(dict(
                AlertType=alert_type, Framework=framework, FrameworkVersion=version, TargetId=tid, TargetName=name,
                Relation=level, EvidenceNeeded=evidence, AlertEvidenceUrl=alert["anchor"], TargetUrl=url, MappingVersion=release,
            ))
        full_links.extend(links)
        candidates[alert_type] = links
        levels = {link["Relation"] for link in links}

        def direct_ids(framework, edition=None):
            return ";".join(link["TargetId"] for link in links if link["Relation"] == "direct"
                            and link["Framework"] == framework
                            and (edition is None or link["FrameworkVersion"] == edition))

        profiles.append(dict(
            AlertType=alert_type, OfficialName=alert["label"], DocumentedSeverity=alert["severity"],
            DocumentedAttack=";".join(alert["attack_tactics"]), ReleaseStatus=alert["status"], SignalScope=alert["scope"],
            Signal=rule["signal"], Disposition=next((x for x in ("direct", "conditional", "context") if x in levels), "no_attribution"),
            AutoCAAT=direct_ids("CAAT"), AutoATLAS=direct_ids("ATLAS"), AutoOWASP2025=direct_ids("OWASP-LLM", "2025"),
            AutoOWASP2026=direct_ids("OWASP-LLM", "2026"),
            Meaning=rule["meaning"], Triage=rule["triage"], EvidenceBoundary=rule["boundary"], LearnUrl=alert["anchor"], MappingVersion=release,
        ))
    for sid, scenario in sorted(scenarios.items()):
        family, documented, gap = assessment[sid]
        caat_rows.append(dict(
            CAAT_Id=sid, Scenario=scenario["label"], Family_Proposed=family, DocumentedLink=documented, Qualification=gap,
            OWASP_Edition=scenario["owasp_edition"], Learn_OWASP=";".join(scenario["owasp_ids"]),
            Learn_ATLAS=";".join(scenario["atlas_ids"]), Learn_Mitigations=";".join(scenario["mitigation_ids"]),
            LearnUrl=scenario["url"], LearnDate=scenario["source_date"], LearnAuthor=scenario["author"], MappingVersion=release,
        ))
        for tid in scenario["atlas_ids"]:
            canonical = tid if tid in vocab else atlas["migrations"].get(tid, "")
            state = "vigente" if canonical == tid else "migración MITRE; revisar semántica" if canonical else "no resuelto"
            caat_links.append(dict(
                CAAT_Id=sid, Framework="ATLAS", VersionInSource="sin edición indicada", SourceId=tid,
                CanonicalId=canonical, CanonicalVersion=atlas["version"], State=state, LearnUrl=scenario["url"],
                ReferenceUrl=vocab[canonical]["url"] if canonical else "",
            ))
        for oid in scenario["owasp_ids"]:
            edition = scenario["owasp_edition"]
            caat_links.append(dict(
                CAAT_Id=sid, Framework="OWASP-LLM", VersionInSource=edition, SourceId=oid,
                CanonicalId=oid, CanonicalVersion=edition, State="cita de Learn; no es una señal de producto",
                LearnUrl=scenario["url"], ReferenceUrl=ref["owasp"][edition][oid]["url"],
            ))
    return dict(profiles=profiles, relations=full_links, caat=caat_rows, caat_links=caat_links,
                atlas=atlas_rows, candidates=candidates)


def make_worksheet(book, name, rows: list[dict], table_index: int):
    ws = book.create_sheet(name)
    headers = list(rows[0])
    ws.append(headers)
    long_fields = {"OfficialName", "Meaning", "Triage", "EvidenceBoundary", "Qualification", "EvidenceNeeded",
                   "Scenario", "Acción / evidencia", "DocumentedLink", "TacticNames", "Learn_ATLAS", "Learn_OWASP"}
    for row in rows:
        ws.append([row[k] for k in headers])
        for cell, key in zip(ws[ws.max_row], headers, strict=True):
            if isinstance(cell.value, str):
                cell.data_type = "s"
                if key.lower().endswith(("url", "enlace")) and cell.value.startswith("https://"):
                    cell.hyperlink = cell.value
                    cell.font = Font(color="12649D", underline="single")
            cell.alignment = Alignment(vertical="center", wrap_text=key in long_fields)
            if str(cell.value) in RELATIONS:
                fill = {"direct": "DAF1E5", "conditional": "FFF0CC", "context": "E8EEF7"}[cell.value]
                cell.fill = PatternFill(fill_type="solid", fgColor=fill)
        ws.row_dimensions[ws.max_row].height = 42 if any(k in long_fields for k in headers) else 19
    for col, key in enumerate(headers, 1):
        width = 60 if key in long_fields else 46 if key.lower().endswith(("url", "enlace")) else 42 if key in {"AlertType", "Signal", "Etiqueta", "Name", "TacticNames", "Mitigación"} else 23
        ws.column_dimensions[get_column_letter(col)].width = width
    table = Table(displayName=f"MDCAI{table_index}", ref=ws.dimensions)
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(table)
    ws.freeze_panes = "B2"
    ws.sheet_view.showGridLines = False
    return ws


def make_excel(ref, policy, model):
    book = Workbook()
    book.remove(book.active)
    readme = book.create_sheet("Inicio")
    rows = [
        ("DEFENDER FOR CLOUD AI SERVICES × SENTINEL", "MITRE ATLAS / OWASP LLM"),
        ("Paquete", f"V{policy['release']} · corte {ref['as_of']} · base de propuesta sin validación en tenant"),
        ("Catálogo", "Severidad y tácticas publicadas en Learn. Significado y guía de triage son síntesis del paquete."),
        ("Alerta x marco", "Una fila por propuesta. Directa = relación que describe la señal, no éxito. Condicional = falta evidencia. Contexto = pivote."),
        ("CAAT x marcos", "Lo que Learn cita a nivel escenario, separado de los enlaces por alerta. Se mantiene la edición OWASP 2025 de Learn."),
        ("ATLAS", "Técnicas oficiales y sus tácticas. El diccionario no implica cobertura."),
        ("Piloto", "Completá resultados y evidencia en tu tenant. Ausencia de actividad no demuestra cobertura ni ausencia de riesgo."),
        ("Fuente operativa", "La matriz es una vista generada. Para cambios persistentes, editá data\\policy.json y regenerá los artefactos."),
        ("Infraestructura", "Defender for Containers y otras fuentes no se registran como alertas runtime de este plan."),
    ]
    for data in rows:
        readme.append(data)
    readme.column_dimensions["A"].width = 56
    readme.column_dimensions["B"].width = 102
    for row in readme.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        readme.row_dimensions[row[0].row].height = 36
    for cell in readme[1]:
        cell.fill = PatternFill(fill_type="solid", fgColor="17365D")
        cell.font = Font(color="FFFFFF", bold=True, size=13)
    readme.sheet_view.showGridLines = False

    def add(name, rows):
        return make_worksheet(book, name, rows, len(book.sheetnames))

    add("Catálogo alertas", model["profiles"])
    add("Alerta x marco", model["relations"])
    add("Escenarios CAAT", model["caat"])
    add("CAAT x marcos", model["caat_links"])
    add("Diccionario ATLAS", model["atlas"])
    add("OWASP 2025 y 2026", [
        dict(Edition=edition, RiskId=oid, Name=risk["name"], ReferenceUrl=risk["url"])
        for edition, risks in sorted(ref["owasp"].items()) for oid, risk in sorted(risks.items())
    ])
    if ref["atlas"]["migrations"]:
        add("Migraciones ATLAS", [
            dict(SourceId=old, CanonicalId=new, Name=ref["atlas"]["techniques"][new]["name"], ReferenceUrl=ref["atlas"]["techniques"][new]["url"])
            for old, new in sorted(ref["atlas"]["migrations"].items())
        ])
    if ref["infrastructure"]:
        add("Fuentes adyacentes", [
            dict(Etiqueta=x["label"], DocumentedSeverity=x["severity"], Scope=x["scope"], LearnUrl=x["anchor"])
            for x in ref["infrastructure"]
        ])
    ws = add("Piloto", [
        dict(AlertType=x["AlertType"], Signal=x["Signal"], **{"Estado piloto": "Pendiente", "Acción / evidencia": "", "Fecha UTC": ""}, LearnUrl=x["LearnUrl"])
        for x in model["profiles"]
    ])
    dv = DataValidation(type="list", formula1='"Pendiente,Ingesta confirmada,Validado,No disponible,No aplica"')
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    dv.add(f"C2:C{ws.max_row}")
    add("Fuentes", [dict(Fuente=k, ReferenceUrl=v) for k, v in sorted(ref["sources"].items())])
    book.save(ROOT / "MDC_AI_ATLAS_OWASP_Mapping_v3.xlsx")


def main():
    ref = load_json(ROOT / "data" / "reference.json")
    policy = load_json(ROOT / "data" / "policy.json")
    model = build_model(ref, policy)
    values = {
        "RELEASE": policy["release"], "ATLAS_VERSION": ref["atlas"]["version"],
        "PRODUCT_NAMES": ", ".join(json.dumps(x, ensure_ascii=False) for x in policy["product_names"]),
        "PROFILE_COUNT": str(len(model["profiles"])), "RELATION_COUNT": str(len(model["relations"])),
        "CAAT_COUNT": str(len(model["caat"])), "ATLAS_COUNT": str(len(model["atlas"])),
    }
    for src in sorted((ROOT / "src").glob("*.kql.in")):
        query = src.read_text(encoding="utf-8")
        for key, substitution in values.items():
            query = query.replace(f"__{key}__", substitution)
        if re.search(r"__[A-Z_]+__", query):
            raise ValueError(f"Quedó un marcador sin resolver en {src.name}")
        (ROOT / "kql" / src.stem).write_text(query, encoding="utf-8")
    files = {}
    (ROOT / "watchlists").mkdir(exist_ok=True)
    for alias, key, modelkey in [(PROFILE_ALIAS, "AlertType", "profiles"), (RELATION_ALIAS, "AlertType", "relations"),
                                 (SCENARIO_ALIAS, "CAAT_Id", "caat"), (ATLAS_ALIAS, "TechniqueId", "atlas")]:
        raw = csv_content(model[modelkey])
        (ROOT / "watchlists" / f"{alias}.csv").write_bytes(raw.encode("utf-8-sig"))
        files[alias] = (key, raw)
    (ROOT / "data" / "CAAT_publicado_relaciones.csv").write_bytes(csv_content(model["caat_links"]).encode("utf-8-sig"))
    make_excel(ref, policy, model)
    azure_artifacts.build(ROOT, ref, policy, model, files)
    print(json.dumps({
        "version": policy["release"], "alert_types": len(model["profiles"]), "caat": len(model["caat"]),
        "atlas_elements": len(model["atlas"]), "local_relations": dict(Counter(x["Relation"] for x in model["relations"])),
        "caat_reference_rows": len(model["caat_links"]),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

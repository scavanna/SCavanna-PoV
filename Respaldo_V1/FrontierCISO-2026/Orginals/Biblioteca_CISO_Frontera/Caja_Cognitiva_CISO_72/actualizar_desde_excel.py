#!/usr/bin/env python3
"""Rebuild generated concept notes and the standalone HTML from the editable workbook."""

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from openpyxl import load_workbook


ROOT = Path(__file__).resolve().parent
WORKBOOK = ROOT / "Catalogo_CISO_Editable.xlsx"
HTML_NAME = "ciso-caja-cognitiva-excel.html"
GROUPS = {
    "modelos": ("Modelos mentales", "01_modelos_mentales"),
    "sesgos": ("Sesgos cognitivos", "02_sesgos_cognitivos"),
    "mindsets": ("Mindsets", "03_mindsets"),
    "ejecutivas": ("Funciones ejecutivas", "04_funciones_ejecutivas"),
    "otras": ("Otras capacidades y prácticas", "05_otras_capacidades"),
}
CONCEPT_COLUMNS = (
    "id", "categoria", "orden", "nombre", "definicion", "base_definicion",
    "limites", "justificacion_ciso", "caso_ciso", "pregunta_guia", "dominios",
    "casos_ciso_adicionales", "aplicaciones_arquitectura",
    "relevancia_soc", "motivo_soc", "relevancia_trust", "motivo_trust",
    "ejercicios", "evaluaciones", "controles", "cantidad_fuentes",
)
AUXILIARY_COLUMNS = {
    "Alias": ("id", "alias"),
    "Pensadores": ("id", "persona", "vinculo"),
    "Referencias": ("id", "referencia"),
    "Fuentes": ("id", "documento", "localizador", "tipo_evidencia"),
}
DEFINITION_BASES = {"source_supported", "conservative_derived", "pending"}
LEVELS = {"high", "medium", "low", "pending"}
ID_PATTERN = re.compile(r"[A-Z][A-Z0-9_-]{1,39}\Z")
GENERATED_MARKER = re.compile(r"<!-- generado-ciso-excel sha256:([a-f0-9]{64}) -->\n")
JSON_PATTERN = {
    name: re.compile(
        rf'(<script id="{name}" type="application/json">)(.*?)(</script>)',
        flags=re.DOTALL,
    )
    for name in ("conceptData", "metaData")
}


def default_html():
    for parent in ROOT.parents:
        if parent.name == "OneDrive - Microsoft":
            return parent / "Documents" / "Microsoft Scout" / HTML_NAME
    return ROOT / HTML_NAME


def value(cell):
    return str(cell).strip() if cell is not None else ""


def lines(cell):
    return [entry.strip() for entry in value(cell).splitlines() if entry.strip()]


def records(sheet, expected):
    raw_headers = [value(cell.value) for cell in sheet[1]]
    if len(raw_headers) != len(set(raw_headers)) or not all(raw_headers):
        raise ValueError(f"{sheet.title}: cabeceras vacías o duplicadas")
    missing = set(expected) - set(raw_headers)
    extra = set(raw_headers) - set(expected)
    if missing or extra:
        raise ValueError(
            f"{sheet.title}: cabeceras inválidas (faltan {sorted(missing)}, sobran {sorted(extra)})"
        )
    for row_number, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 2):
        if not any(cell is not None and value(cell) for cell in row):
            continue
        yield row_number, dict(zip(raw_headers, row))


def parse_positive_integer(raw, where):
    if raw in (None, ""):
        return None
    if isinstance(raw, bool):
        raise ValueError(f"{where}: debe ser un entero positivo")
    try:
        number = int(raw)
    except (ValueError, TypeError, OverflowError) as error:
        raise ValueError(f"{where}: debe ser un entero positivo") from error
    if number < 1 or str(raw).strip() not in (str(number), str(float(number))):
        raise ValueError(f"{where}: debe ser un entero positivo")
    return number


def parse_nonnegative_integer(raw, where):
    if raw in (None, ""):
        return None
    number = parse_positive_integer(raw, where) if raw not in (0, 0.0, "0") else 0
    return number


def read_catalog(path):
    workbook = load_workbook(path, read_only=True, data_only=True)
    try:
        expected = {"Conceptos", *AUXILIARY_COLUMNS}
        missing_sheets = expected - set(workbook.sheetnames)
        if missing_sheets:
            raise ValueError(f"Faltan hojas del Excel: {', '.join(sorted(missing_sheets))}")
        items = []
        index = {}
        used_ranks = {}
        for row_number, record in records(workbook["Conceptos"], CONCEPT_COLUMNS):
            concept_id = value(record["id"]).upper()
            group = value(record["categoria"]).lower()
            name = value(record["nombre"])
            where = f"Conceptos, fila {row_number}"
            if not ID_PATTERN.fullmatch(concept_id):
                raise ValueError(f"{where}: ID inválido ({concept_id!r}); use p. ej. NEW-0001")
            if concept_id in index:
                raise ValueError(f"{where}: ID duplicado {concept_id}")
            if group not in GROUPS:
                raise ValueError(f"{where}: categoría desconocida {group!r}")
            if not name:
                raise ValueError(f"{where}: falta el nombre de {concept_id}")
            rank = parse_positive_integer(record["orden"], f"{where}, orden")
            if rank is not None and (group, rank) in used_ranks:
                raise ValueError(
                    f"{where}: orden {rank} duplicado en {group} "
                    f"(fila {used_ranks[(group, rank)]})"
                )
            if rank is not None:
                used_ranks[(group, rank)] = row_number
            basis = value(record["base_definicion"]) or "pending"
            if basis not in DEFINITION_BASES:
                raise ValueError(f"{where}: base_definicion desconocida {basis!r}")
            soc_level = value(record["relevancia_soc"]) or "pending"
            trust_level = value(record["relevancia_trust"]) or "pending"
            if soc_level not in LEVELS or trust_level not in LEVELS:
                raise ValueError(f"{where}: relevancia debe ser high, medium, low o pending")
            count = parse_nonnegative_integer(
                record["cantidad_fuentes"], f"{where}, cantidad_fuentes"
            )
            item = {
                "id": concept_id, "group": group, "rank": rank, "name": name,
                "canonicalName": name,
                "definition": value(record["definicion"]),
                "definitionBasis": basis,
                "limits": value(record["limites"]),
                "why": value(record["justificacion_ciso"]),
                "scenario": value(record["caso_ciso"]),
                "question": value(record["pregunta_guia"]),
                "domains": lines(record["dominios"]),
                "cisoUses": lines(record["casos_ciso_adicionales"]),
                "architectUses": lines(record["aplicaciones_arquitectura"]),
                "exercises": lines(record["ejercicios"]),
                "evaluations": lines(record["evaluaciones"]),
                "controls": lines(record["controles"]),
                "soc": {"level": soc_level, "reason": value(record["motivo_soc"])},
                "trust": {"level": trust_level, "reason": value(record["motivo_trust"])},
                "aliases": [], "authors": [], "references": [], "sources": [],
                "sourceCount": count, "excelRow": row_number,
            }
            index[concept_id] = item
            items.append(item)

        if not items:
            raise ValueError("Conceptos: no se encontraron entradas")
        for item in items:
            if item["rank"] is None:
                group = item["group"]
                rank = max(
                    (rank for key, rank in used_ranks if key == group), default=0
                ) + 1
                item["rank"] = rank
                used_ranks[(group, rank)] = item["excelRow"]

        for sheet_name, columns in AUXILIARY_COLUMNS.items():
            for row_number, record in records(workbook[sheet_name], columns):
                concept_id = value(record["id"]).upper()
                if concept_id not in index:
                    raise ValueError(f"{sheet_name}, fila {row_number}: ID desconocido {concept_id!r}")
                item = index[concept_id]
                if sheet_name == "Alias":
                    alias = value(record["alias"])
                    if not alias:
                        raise ValueError(f"Alias, fila {row_number}: alias vacío")
                    item["aliases"].append(alias)
                elif sheet_name == "Pensadores":
                    person = value(record["persona"])
                    if not person:
                        raise ValueError(f"Pensadores, fila {row_number}: nombre vacío")
                    item["authors"].append({"name": person, "basis": value(record["vinculo"])})
                elif sheet_name == "Referencias":
                    reference = value(record["referencia"])
                    if not reference:
                        raise ValueError(f"Referencias, fila {row_number}: referencia vacía")
                    item["references"].append(reference)
                else:
                    document = value(record["documento"])
                    locator = value(record["localizador"])
                    if not document or not locator:
                        raise ValueError(
                            f"Fuentes, fila {row_number}: documento y localizador obligatorios"
                        )
                    item["sources"].append({
                        "document": document, "locator": locator,
                        "provenance": value(record["tipo_evidencia"]) or "Sin clasificar",
                    })
    finally:
        workbook.close()

    for item in items:
        if item["sourceCount"] is None:
            item["sourceCount"] = len(item["sources"])
        if item["sourceCount"] < len(item["sources"]):
            raise ValueError(
                f"{item['id']}: cantidad_fuentes menor que las referencias en Fuentes"
            )
        if item["definitionBasis"] == "source_supported" and not item["sources"]:
            raise ValueError(
                f"{item['id']}: definición declarada apoyada sin localizador en Fuentes"
            )
        item["incomplete"] = [
            label for key, label in (
                ("definition", "definición"), ("limits", "límites"),
                ("why", "justificación"), ("scenario", "caso CISO"),
                ("question", "pregunta guía"), ("domains", "dominios"),
                ("exercises", "ejercicios"), ("evaluations", "evaluación"),
                ("controls", "controles"),
            )
            if not item[key]
        ]
        if not item["sources"]:
            item["incomplete"].append("fuentes/localizadores")
        del item["excelRow"]
    items.sort(key=lambda item: (list(GROUPS).index(item["group"]), item["rank"]))
    return items


def markdown_lines(entries, empty="No consta en los documentos analizados."):
    if not entries:
        return f"- {empty}\n"
    return "".join("- " + str(entry).replace("\n", "\n  ") + "\n" for entry in entries)


def markdown(item):
    group = GROUPS[item["group"]][0]
    label = {
        "source_supported": "Apoyada por fuentes del catálogo",
        "conservative_derived": "Síntesis conservadora derivada",
        "pending": "Pendiente de contrastar con fuentes",
    }[item["definitionBasis"]]
    relevance = {"high": "Alta", "medium": "Media", "low": "Indirecta", "pending": "Por evaluar"}
    authors = [
        author["name"] + (f" — {author['basis']}" if author["basis"] else "")
        for author in item["authors"]
    ]
    sources = [
        f"{source['document']} — {source['locator']} "
        f"({source['provenance']})"
        for source in item["sources"]
    ]
    def field(name):
        return item[name] or "**Pendiente de documentar en Excel.**"
    sections = [
        f"# {item['name']}\n",
        f"**ID:** `{item['id']}` · **Categoría:** {group} · "
        f"**Prioridad editorial:** {item['rank']} · "
        f"**Base de definición:** {label}\n",
        "## Definición y alcance\n",
        f"{field('definition')}\n",
        f"**Límites:** {field('limits')}\n",
        "## Alias\n", markdown_lines(item["aliases"]),
        "## Relevancia para el CISO\n",
        f"**Por qué:** {field('why')}\n",
        f"**Caso específico:** {field('scenario')}\n",
        f"**Pregunta guía:** {field('question')}\n",
        "**Dominios:** " + (", ".join(item["domains"]) or "**Pendiente de documentar.**") + "\n",
        "**Casos CISO adicionales:**\n", markdown_lines(item["cisoUses"]),
        "## Aplicación para arquitectura, SOC agéntico y Trust Framework\n",
        "**Arquitectura:**\n", markdown_lines(item["architectUses"]),
        f"**SOC agéntico — {relevance[item['soc']['level']]}:** "
        f"{item['soc']['reason'] or '**Pendiente de documentar.**'}\n",
        f"**Trust Framework — {relevance[item['trust']['level']]}:** "
        f"{item['trust']['reason'] or '**Pendiente de documentar.**'}\n",
        "## Práctica y evaluación\n",
        "**Ejercicios:**\n", markdown_lines(item["exercises"], "Pendiente de documentar en Excel."),
        "**Métodos de evaluación:**\n",
        markdown_lines(item["evaluations"], "Pendiente de documentar en Excel."),
        "**Controles o compensaciones:**\n",
        markdown_lines(item["controls"], "Pendiente de documentar en Excel."),
        "## Pensadores y bibliografía identificados\n",
        "**Personas y atribución documentada:**\n", markdown_lines(authors),
        "**Referencias bibliográficas mencionadas en el corpus:**\n",
        markdown_lines(item["references"]),
        "## Trazabilidad documental\n",
        f"**Documentos contabilizados en el catálogo:** {item['sourceCount']}. "
        f"**Localizadores representativos listados:** {len(sources)}.\n",
        markdown_lines(sources, "Sin documento ni localizador; pendiente de evidencia."),
        "## Nota metodológica\n",
        "La definición y las referencias se registran desde el catálogo; "
        "la prioridad, el caso concreto y la pregunta son adaptación editorial "
        "para el CISO, no evidencia experimental de eficacia. "
        + ("Un sesgo se gestiona con controles compensatorios y revisión independiente, "
           "no se promete eliminarlo mediante entrenamiento.\n"
           if item["group"] == "sesgos"
           else "Aplicar como herramienta situada, no como explicación universal.\n"),
    ]
    if item["incomplete"]:
        sections.extend([
            "## Campos por completar\n",
            markdown_lines(item["incomplete"]),
        ])
    return "\n".join(sections).rstrip() + "\n"


def markdown_path(item):
    slug = unicodedata.normalize("NFKD", item["name"])
    slug = slug.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")[:70].rstrip("-")
    return ROOT / GROUPS[item["group"]][1] / f"{item['id']}-{slug or 'concepto'}.md"


def generated_text(body):
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return f"<!-- generado-ciso-excel sha256:{digest} -->\n{body}"


def preflight_generated_file(path):
    if not path.exists():
        return
    existing = path.read_text(encoding="utf-8")
    match = GENERATED_MARKER.match(existing)
    if not match:
        raise FileExistsError(f"No se sobrescribe un archivo sin marcador de generación: {path}")
    body = existing[match.end():]
    if hashlib.sha256(body.encode("utf-8")).hexdigest() != match.group(1):
        raise ValueError(f"Hay cambios manuales en {path}; guárdelos antes de regenerar")


def index_markdown(items):
    lines_out = [
        "# Índice de la caja cognitiva del CISO\n",
        "Índice generado desde `Catalogo_CISO_Editable.xlsx`. "
        "El Excel es la fuente editable; estas fichas son vistas derivadas.\n",
    ]
    for group, (title, _) in GROUPS.items():
        subset = [item for item in items if item["group"] == group]
        lines_out.extend([f"## {title} ({len(subset)})\n"])
        for item in subset:
            path = markdown_path(item).relative_to(ROOT).as_posix()
            lines_out.append(f"- {item['rank']}. [{item['name']}]({path}) (`{item['id']}`)")
        lines_out.append("")
    return "\n".join(lines_out).rstrip() + "\n"


def safe_json(value):
    return (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )


def updated_html(path, items):
    page = path.read_text(encoding="utf-8")
    groups = {
        key: {"label": title, "count": sum(item["group"] == key for item in items)}
        for key, (title, _) in GROUPS.items()
    }
    for name, data in (
        ("conceptData", items),
        ("metaData", {"edition": "Excel editable", "groups": groups}),
    ):
        pattern = JSON_PATTERN[name]
        if len(pattern.findall(page)) != 1:
            raise ValueError(f"{path}: se esperaba un único bloque {name}")
        page = pattern.sub(
            lambda match: match.group(1) + safe_json(data) + match.group(3), page, count=1
        )
    return page


def rebuild(workbook_path, html_path):
    items = read_catalog(workbook_path)
    writes = {markdown_path(item): generated_text(markdown(item)) for item in items}
    writes[ROOT / "00_Indice.md"] = generated_text(index_markdown(items))
    for path in writes:
        preflight_generated_file(path)
    if not html_path.is_file():
        raise FileNotFoundError(f"No se encontró el HTML editable: {html_path}")
    page = updated_html(html_path, items)
    for path, content in writes.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    html_path.write_text(page, encoding="utf-8")
    incomplete = [item["id"] for item in items if item["incomplete"]]
    print(
        f"Excel: {workbook_path}\n"
        f"Fichas: {len(items)} · Pendientes: {len(incomplete)}"
        f"{' (' + ', '.join(incomplete[:12]) + ')' if incomplete else ''}\n"
        f"HTML actualizado: {html_path}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--excel", type=Path, default=WORKBOOK)
    parser.add_argument("--html", type=Path, default=default_html())
    arguments = parser.parse_args()
    rebuild(arguments.excel, arguments.html)

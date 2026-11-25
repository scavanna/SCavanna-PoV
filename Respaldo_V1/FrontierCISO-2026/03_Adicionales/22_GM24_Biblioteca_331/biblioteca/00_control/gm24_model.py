#!/usr/bin/env python3
"""Reconcile curated GM24, Atlas, HC and maieutic evidence without inventing approvals."""

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(r"C:\Users\scavanna\OneDrive - Microsoft\AI-CISOMindSet")
LIBRARY = ROOT / "Biblioteca_GM24"
CONTROL = LIBRARY / "00_control"
CURATED = ROOT / "Curado02"
BASE_CODE = re.compile(r"[GM][1-6]\.[12]-K(?:0[1-9]|10)\Z")
CORE_HEADING = re.compile(
    r"(?m)^#{2,3}\s+(\d{1,3})\.\s+([GM]\d\.\d-K\d{2})\s+[—–-]\s+(.+?)\s*$"
)
UNIT_HEADING = re.compile(r"(?m)^### ([GM]\d\.\d)\s+[—–-]\s+(.+?)\s*$")
HC_HEADING = re.compile(r"(?m)^#### (HC-\d{3})\s+[—–-]\s+(.+?)\s*$")


def load_json(path):
    with path.open(encoding="utf-8-sig") as source:
        return json.load(source)


def clean_title(title):
    return title.strip().rstrip(".:").strip()


def compare_title(title):
    plain = unicodedata.normalize("NFKD", clean_title(title).lower())
    return re.sub(r"\W+", " ", plain.encode("ascii", "ignore").decode("ascii")).strip()


def heading_line(text, offset):
    return text.count("\n", 0, offset) + 1


def excerpt_first_sentence(text):
    plain = re.sub(r"(?m)^\s*#{2,5}\s+.*$", "", text)
    plain = re.sub(r"(?m)^\*\*(?:Unidad|Palabras|Estado):\*\*.*$", "", plain)
    plain = re.sub(r"^\*\*[^*]{3,100}[\.:]\*\*\s*", "", plain.strip())
    plain = re.sub(r"\*\*", "", plain)
    first = re.split(r"(?<=\.)\s+(?=[A-ZÁÉÍÓÚÑ])", plain, maxsplit=1)[0].strip()
    return first if len(first) <= 500 else first[:497].rsplit(" ", 1)[0] + "..."


def trimmed_block(block):
    return re.split(r"(?m)^---\s*$", block, maxsplit=1)[0].strip()


def find_curated(manifest, suffix):
    found = [
        item for item in manifest["items"]
        if item["canonical_source"].endswith("/" + suffix)
        or any(alias.endswith("/" + suffix) for alias in item["other_identical_origins"])
    ]
    if len(found) != 1:
        raise ValueError(f"Expected one curated origin {suffix}: found {len(found)}")
    path = ROOT / found[0]["curated_path"]
    if not path.is_file():
        raise FileNotFoundError(path)
    return path, found[0]


def curated_lots(manifest):
    files = [
        ROOT / item["curated_path"]
        for item in manifest["items"]
        if item["canonical_source"].startswith("thenextciso_2026/")
        and (
            "Ensayos base " in item["canonical_source"]
            or "Ensayos_Bases_" in item["canonical_source"]
        )
    ]
    if len(files) != 8:
        raise ValueError(f"Expected eight 30-concept Markdown lots, found {len(files)}")
    return files


def parse_master(path):
    text = path.read_text(encoding="utf-8-sig")
    heads = list(UNIT_HEADING.finditer(text))
    result = {}
    master_cores = {}
    expansions = []
    for index, match in enumerate(heads):
        body = text[
            match.end(): heads[index + 1].start() if index + 1 < len(heads) else len(text)
        ]
        if "**Desarrollo conceptual original (10 conceptos):**" not in body:
            continue
        code = match.group(1)
        core = body.split("**Desarrollo conceptual original (10 conceptos):**", 1)[1]
        core = core.split("**Ampliaciones derivadas", 1)[0]
        numbers = [
            (int(number), clean_title(name))
            for number, name in re.findall(
                r"(?m)^(\d+)\.\s+\*\*(.+?)\*\*", core
            )
        ]
        if [number for number, _ in numbers] != list(range(1, 11)):
            raise ValueError(f"{code}: base concepts are not K01-K10")
        for number, name in numbers:
            master_cores[f"{code}-K{number:02}"] = name
        extension_section = body.split("**Ampliaciones derivadas", 1)
        if len(extension_section) != 2:
            raise ValueError(f"{code}: missing Atlas extensions section")
        extension_section = extension_section[1].split(
            "**Objetivo de aprendizaje", 1
        )[0]
        extension_names = [
            clean_title(name)
            for name in re.findall(r"(?m)^-\s+\*\*(.+?)\*\*", extension_section)
        ]
        if not 2 <= len(extension_names) <= 3:
            raise ValueError(f"{code}: unexpected extension count {len(extension_names)}")
        for name in extension_names:
            expansions.append({"id": f"AMP-{len(expansions)+1:02}", "unit": code, "name": name})

        def metadata(key):
            found = re.search(r"\*\*" + re.escape(key) + r":\*\*\s*([^\n]+)", body)
            return found.group(1).strip() if found else ""

        result[code] = {
            "id": code, "title": match.group(2).strip(),
            "pillar": metadata("Pilar").split(".")[0],
            "axis": metadata("Eje").split("**")[0].strip().rstrip("."),
            "atlas": metadata("Ubicación en el Atlas").split(".")[0].strip(),
            "guiding_question": metadata("Pregunta rectora"),
            "alignment": metadata("Alineaciones propuestas"),
            "source_path": str(path),
            "source_line": heading_line(text, match.start()),
            "base_ids": [f"{code}-K{i:02}" for i in range(1, 11)],
            "amp_ids": [],
        }
    if len(result) != 24 or len(master_cores) != 240 or len(expansions) != 51:
        raise ValueError(
            f"Master corpus mismatch: units={len(result)} base={len(master_cores)} AMP={len(expansions)}"
        )
    for expansion in expansions:
        result[expansion["unit"]]["amp_ids"].append(expansion["id"])
    return result, master_cores, expansions


def parse_lots(paths, names, ideas):
    base = {}
    observed_numbers = {}
    for path in paths:
        text = path.read_text(encoding="utf-8-sig")
        matches = list(CORE_HEADING.finditer(text))
        if len(matches) != 30:
            raise ValueError(f"{path}: expected exactly 30 essay ideas, got {len(matches)}")
        for index, match in enumerate(matches):
            number, concept_id, title = match.groups()
            number = int(number)
            if concept_id in base or number in observed_numbers:
                raise ValueError(f"Duplicate concept code or ordinal: {concept_id}/{number}")
            observed_numbers[number] = concept_id
            if concept_id not in names or compare_title(names[concept_id]) != compare_title(title):
                raise ValueError(f"{concept_id}: title differs between master and essay: {title}")
            block = trimmed_block(
                text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)]
            )
            question = re.search(r"\*\*Pregunta generadora:\*\*\s*(.+)", block)
            words = len(re.findall(r"\b\w+\b", block))
            if not 240 <= words <= 1000:
                raise ValueError(
                    f"{concept_id}: essay block unexpectedly short/long ({words} words)"
                )
            idea = ideas.get(concept_id)
            if not idea or compare_title(idea["titulo"]) != compare_title(title):
                raise ValueError(f"{concept_id}: missing or mismatched structured central idea")
            source_paragraphs = idea.get("parrafos", [])
            if len(source_paragraphs) < 4:
                raise ValueError(f"{concept_id}: incomplete structured essay idea")
            base[concept_id] = {
                "id": concept_id, "title": names[concept_id],
                "type": "base", "status": "idea central propuesta; concepto base GM-24",
                "unit": concept_id.split("-K")[0],
                "related_units": [concept_id.split("-K")[0]],
                "definition": excerpt_first_sentence(source_paragraphs[0]["texto"]),
                "source_tension": excerpt_first_sentence(source_paragraphs[1]["texto"]),
                "source_application": excerpt_first_sentence(source_paragraphs[2]["texto"]),
                "source_result": excerpt_first_sentence(source_paragraphs[3]["texto"]),
                "text": block,
                "question": question.group(1).strip() if question else idea["pregunta_generadora"],
                "source_path": str(path),
                "source_start": heading_line(text, match.start()),
                "source_end": heading_line(text, match.end()) + block.count("\n"),
                "word_count": words, "ordinal": number,
                "structured_labels": [
                    paragraph.get("etiqueta", "") for paragraph in idea.get("parrafos", [])
                ],
            }
    if sorted(observed_numbers) != list(range(1, 241)) or len(base) != 240:
        raise ValueError("The essay lots do not cover 001-240 exactly once")
    return base


def parse_hybrids(path, ideas, core_ids):
    text = path.read_text(encoding="utf-8-sig")
    matches = list(HC_HEADING.finditer(text))
    if len(matches) != 40:
        raise ValueError(f"Expected 40 HC sections, found {len(matches)}")
    hybrids = {}
    for index, match in enumerate(matches):
        concept_id, title = match.groups()
        if concept_id != f"HC-{index+1:03}":
            raise ValueError(f"HC IDs out of order: {concept_id}")
        idea = ideas.get(concept_id)
        if not idea or compare_title(title) != compare_title(idea["titulo"]):
            raise ValueError(f"{concept_id}: structured hybrid title mismatch")
        relations = idea.get("relaciones", [])
        linked = [relation["preensayo"] for relation in relations]
        if len(linked) < 4 or any(link not in core_ids for link in linked):
            raise ValueError(f"{concept_id}: missing links to original GM24 concepts")
        segment = trimmed_block(
            text[match.end():matches[index+1].start() if index+1<len(matches) else len(text)]
        )
        if not idea.get("actividad") or not idea.get("criterio"):
            raise ValueError(f"{concept_id}: no integrative exercise or evaluation")
        hybrids[concept_id] = {
            "id": concept_id, "title": clean_title(title),
            "type": "hybrid", "status": "candidato integrador HC; incluido por decisión del usuario",
            "unit": None,
            "related_units": sorted({key.split("-K")[0] for key in linked}),
            "definition": excerpt_first_sentence(idea["idea_integradora"]),
            "text": segment,
            "question": "", "links": relations,
            "activity": idea["actividad"], "outcome": idea["resultado"],
            "evaluation": idea["criterio"], "duplication_risk": idea["riesgo_duplicacion"],
            "group": idea["grupo"],
            "source_path": str(path), "source_start": heading_line(text, match.start()),
            "source_end": heading_line(text, match.end()) + segment.count("\n"),
            "word_count": len(re.findall(r"\b\w+\b", segment)),
        }
    return hybrids


def parse_amp(expansions, data, expected_ids):
    proposals = data.get("ideas", [])
    if len(proposals) != 51:
        raise ValueError(f"Expected 51 WorkIQ-grounded proposals, found {len(proposals)}")
    indexed = {proposal["id"]: proposal for proposal in proposals}
    if len(indexed) != 51:
        raise ValueError("Repeated AMP proposal ID")
    result = {}
    for index, item in enumerate(expansions, 1):
        proposal = indexed.get(item["id"])
        if not proposal or proposal["unidad"] != item["unit"] or proposal["fila"] != index + 284:
            raise ValueError(f"{item['id']}: proposed idea does not match master sequence")
        if not proposal["idea"] or proposal["vinculo"] not in expected_ids:
            raise ValueError(f"{item['id']}: missing proposed thesis or invalid linked ID")
        result[item["id"]] = {
            "id": item["id"], "title": item["name"],
            "type": "atlas", "status": "ampliación Atlas: título original; tesis propuesta [P], no aprobada",
            "unit": item["unit"], "related_units": [item["unit"]],
            "definition": proposal["idea"],
            "text": "",
            "question": "", "links": [{"preensayo": proposal["vinculo"],
                                       "relacion": "VÍNCULO EDITORIAL PROPUESTO"}],
            "workbook_source": data["fuente"],
            "workbook_locator": f"06Ensayos!A{proposal['fila']}:T{proposal['fila']}",
            "workbook_idea_cell": f"06Ensayos!I{proposal['fila']}",
            "verification_note": proposal.get("nota_verificacion", ""),
        }
    return result


def parse_question_corpus(preessays, question_rows, taxonomy, existing):
    index = {item["id"]: item for item in preessays}
    if len(index) != 639 or len(preessays) != 639:
        raise ValueError(f"Expected 639 distinct pre-essays, found {len(index)}")
    by_type = Counter(item["tipo"] for item in preessays)
    if sorted(by_type.values()) != [40, 51, 240, 308]:
        raise ValueError(f"Unexpected pre-essay distribution: {by_type}")
    if set(existing) != {
        item["id"] for item in preessays if item["tipo"] != "Ampliación por pregunta"
    }:
        raise ValueError("The 331 current GM24 IDs differ from the 639-source set")
    for item in preessays:
        if item["id"] in existing and compare_title(item["titulo"]) != compare_title(
            existing[item["id"]]["title"]
        ):
            raise ValueError(f"{item['id']}: source title mismatch in pre-essay corpus")
    if len(question_rows) != 543:
        raise ValueError(f"Expected 543 consolidated questions, found {len(question_rows)}")
    questions = {}
    for row in question_rows:
        if row["id"] in questions or row["preensayo_directo"] not in index:
            raise ValueError(f"Question {row['id']}: repeated or broken direct link")
        if row["preensayo_331"] and row["preensayo_331"] not in existing:
            raise ValueError(f"{row['id']}: broken 331-concept link")
        questions[row["id"]] = {
            "id": row["id"], "text": row["pregunta"],
            "form": "interrogativa" if "?" in row["pregunta"] else "petición imperativa",
            "direct_id": row["preensayo_directo"], "gm24_id": row["preensayo_331"],
            "bank_id": row["pregunta_banco_directa"],
            "type": row["tipo_mayeutico_directo"],
            "origin": row["origen"], "origin_id": row["id_origen"],
            "source_locator": f"preguntas[id={row['id']}]",
        }

    derived = {}
    for row in preessays:
        if row["tipo"] != "Ampliación por pregunta":
            continue
        if not row["tesis"] or not row["tension"] or not row["desarrollo"] or not row["producto"]:
            raise ValueError(f"{row['id']}: incomplete source-derived thesis")
        origin = row["pregunta_origen"]
        if origin not in questions:
            raise ValueError(f"{row['id']}: missing originating question {origin}")
        special = row["especializa"]
        if special and special not in existing:
            raise ValueError(f"{row['id']}: unknown specialization {special}")
        primary_unit = existing[special]["unit"] if special else None
        linked_units = (
            existing[special]["related_units"] if special else sorted({
                unit
                for link in row.get("vinculos", [])
                if link.get("preensayo") in existing
                for unit in existing[link["preensayo"]]["related_units"]
            })
        )
        derived[row["id"]] = {
            "id": row["id"], "title": row["titulo"], "type": "question_derived",
            "status": "tesis propuesta en corpus mayéutico; no concepto base aprobado",
            "unit": primary_unit, "related_units": linked_units,
            "definition": row["tesis"], "tension": row["tension"],
            "development": row["desarrollo"], "mistake": row["error"],
            "product": row["producto"], "origin_question": origin,
            "specializes": special, "links": row.get("vinculos", []),
            "mirrors": row.get("espejos", []),
            "source_locator": f"preensayos[id={row['id']}]",
        }
    if len(derived) != 308:
        raise ValueError(f"Expected 308 question-derived propositions, found {len(derived)}")
    for question in questions.values():
        direct = question["direct_id"]
        if direct not in derived and direct not in existing:
            raise ValueError(f"Question direct target {direct} is not in known objects")
        question["related_thesis"] = (
            derived[direct]["definition"] if direct in derived else ""
        )
        question["related_thesis_status"] = (
            "tesis derivada [P] del pre-ensayo AP, no afirmación literal de la pregunta"
            if direct in derived else "sin enunciado derivado unívoco en este corpus"
        )

    templates = {row["codigo"]: row for row in taxonomy["tipos_mayeuticos"]}
    if len(templates) != 8:
        raise ValueError("Expected eight documented maieutic types")
    bm = []
    for row in preessays:
        if not re.fullmatch(r"BM-\d{4}", row["bm_inicio"]):
            raise ValueError(f"{row['id']}: invalid starting BM ID")
        start = int(row["bm_inicio"][3:])
        for offset, type_id in enumerate(row["serie"]):
            if type_id not in templates:
                raise ValueError(f"{row['id']}: unknown maieutic template {type_id}")
            bm.append({
                "id": f"BM-{start+offset:04}", "concept_id": row["id"],
                "type": type_id, "type_name": templates[type_id]["nombre"],
                "text": templates[type_id]["plantilla"].format(t=row["titulo"]),
                "provenance": "pregunta generada mediante plantilla; no cita textual de entrevista",
            })
    if len(bm) != 2395 or sorted(int(x["id"][3:]) for x in bm) != list(range(1, 2396)):
        raise ValueError("BM sequence is not exactly 0001..2395")
    bm.sort(key=lambda question: int(question["id"][3:]))
    return derived, questions, bm, templates


def build_model():
    manifest = load_json(CURATED / "00_control" / "Manifiesto_Curado02.json")
    path, _ = find_curated(manifest, "TheNextCISO_GM-24_Documento_Maestro.md")
    units, master_names, expansions = parse_master(path)
    source_ideas, _ = find_curated(manifest, "corpus_ideas_centrales.json")
    ideas = load_json(source_ideas)["ideas"]
    lots = parse_lots(curated_lots(manifest), master_names, ideas)
    hybrid_source, _ = find_curated(
        manifest, "TheNextCISO GM-24 — 40 conceptos híbridos y vinculantes (1).md"
    )
    hybrids = parse_hybrids(hybrid_source, ideas, set(lots))
    proposal_data = load_json(CONTROL / "AMP_ideas_propuestas_2026-11.json")
    amp = parse_amp(expansions, proposal_data, set(lots) | set(hybrids))
    concepts = {**lots, **amp, **hybrids}
    if len(concepts) != 331:
        raise ValueError("240 + 51 + 40 must equal 331 unique IDs")
    for item in concepts.values():
        item["linked_questions"] = []
        item["bm_ids"] = []

    question_source, _ = find_curated(manifest, "preguntas_consolidadas.json")
    preessay_source, _ = find_curated(manifest, "corpus_preensayos.json")
    taxonomy_source, _ = find_curated(manifest, "taxonomia.json")
    derived, questions, bank, templates = parse_question_corpus(
        load_json(preessay_source)["preensayos"],
        load_json(question_source)["preguntas"],
        load_json(taxonomy_source),
        concepts,
    )
    for question in questions.values():
        ids = {question["gm24_id"], question["direct_id"]}
        for linked in ids:
            if linked in concepts:
                concepts[linked]["linked_questions"].append(question["id"])
            if linked in derived:
                derived[linked].setdefault("linked_questions", []).append(question["id"])
    for question in bank:
        concept_id = question["concept_id"]
        entry = concepts.get(concept_id) or derived.get(concept_id)
        if entry is None:
            raise ValueError(f"{question['id']}: unknown BM target")
        entry.setdefault("bm_ids", []).append(question["id"])

    contexts = load_json(CONTROL / "Casos_y_Rubricas_por_Unidad.json")["casos"]
    if len(contexts) != 24 or {case["unidad"] for case in contexts} != set(units):
        raise ValueError("24 unique contextual scenarios are required")
    scenarios = {case["unidad"]: case for case in contexts}
    for code, case in scenarios.items():
        if any(link not in concepts for link in (*case["par"], case["amp"])):
            raise ValueError(f"{code}: invalid concept link in learning case")
        if any(concepts[link]["unit"] != code for link in (*case["par"], case["amp"])):
            raise ValueError(f"{code}: learning case primary concepts not in unit")
        if case["hc"] and (
            case["hc"] not in hybrids
            or (code not in hybrids[case["hc"]]["related_units"] and code != "G2.1")
        ):
            raise ValueError(f"{code}: learning case HC link not supported by source")
        if not all(case[field] for field in (
            "escenario", "decision", "alternativas", "insumos", "entregable",
            "criterio_critico", "investigacion", "contraparte", "cognitivo"
        )):
            raise ValueError(f"{code}: incomplete learning scenario")
    for code, unit in units.items():
        unit["hc_ids"] = [
            item["id"] for item in hybrids.values() if code in item["related_units"]
        ]
        unit["ap_ids"] = [
            item["id"] for item in derived.values() if item["unit"] == code
        ]
        unit["case"] = scenarios[code]

    assert len(units) == 24 and len(concepts) == 331
    assert len(derived) == 308 and len(questions) == 543 and len(bank) == 2395
    return {
        "units": units, "concepts": concepts, "derived": derived,
        "questions": questions, "bank": bank, "templates": templates,
        "manifest": manifest,
        "curated_question_sources": {
            "questions": str(question_source),
            "preessays": str(preessay_source), "taxonomy": str(taxonomy_source),
            "ideas": str(source_ideas),
        },
    }


if __name__ == "__main__":
    model = build_model()
    print(json.dumps({
        "units": len(model["units"]),
        "core": Counter(item["type"] for item in model["concepts"].values()),
        "derived": len(model["derived"]),
        "questions": len(model["questions"]),
        "maieutic_templates": len(model["templates"]),
        "generated_bank": len(model["bank"]),
        "selected_documents": model["manifest"]["unique_copies"],
    }, ensure_ascii=False, default=dict))

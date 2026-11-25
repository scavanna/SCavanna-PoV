#!/usr/bin/env python3
"""Independently audit published GM24 files, relationships, provenance and hours."""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

from jsonschema import Draft202012Validator
from openpyxl import load_workbook


ROOT = Path(r"C:\Users\scavanna\OneDrive - Microsoft\AI-CISOMindSet")
LIBRARY = ROOT / "Biblioteca_GM24"
CONTROL = LIBRARY / "00_control"
CURATED = ROOT / "Curado02"
MASTER = LIBRARY / "Mapa_GM24_331_y_Metodo.xlsx"
SCHEMA = json.loads((CONTROL / "Esquemas_GM24.json").read_text(encoding="utf-8"))
EXPECTED = {
    "Unidades_24": 24, "Conceptos_331": 331, "AMP_51": 51, "HC_40": 40,
    "Tesis_AP_308": 308, "Preguntas_543": 543, "Banco_BM_2395": 2395,
    "Ejercicios_192": 192, "Plan_800h": 25, "Fuentes_31": 31,
}


def hash_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path, count, kind):
    validator = Draft202012Validator({
        "$schema": SCHEMA["$schema"], "$defs": SCHEMA["$defs"],
        "$ref": f"#/$defs/{kind}",
    })
    records = []
    with path.open(encoding="utf-8") as source:
        for number, line in enumerate(source, 1):
            entry = json.loads(line)
            errors = sorted(validator.iter_errors(entry), key=lambda issue: str(issue.path))
            if errors:
                raise ValueError(f"{path}:{number}: {errors[0].message}")
            records.append(entry)
    if len(records) != count or len({row["id"] for row in records}) != count:
        raise ValueError(f"{path}: expected {count} unique rows, found {len(records)}")
    return records


def audit():
    manifest = json.loads((CURATED / "00_control" / "Manifiesto_Curado02.json").read_text(encoding="utf-8"))
    if manifest["unique_copies"] != 31 or manifest["selection_inputs"] != 32:
        raise ValueError("Selected-source manifest changed unexpectedly")
    for row in manifest["items"]:
        origin = ROOT / row["canonical_source"]
        copy = ROOT / row["curated_path"]
        if not origin.is_file() or not copy.is_file():
            raise FileNotFoundError(f"Original or curated copy missing: {row['canonical_source']}")
        if (hash_file(origin) != row["sha256"]
                or hash_file(copy) != row["sha256"]
                or copy.stat().st_size != row["bytes"]):
            raise ValueError(f"Source bytes changed: {row['curated_path']}")
    for row in manifest.get("archived_versions", []):
        copy = ROOT / row["curated_path"]
        if not copy.is_file() or hash_file(copy) != row["sha256"]:
            raise ValueError(f"Historical curated version changed: {row['curated_path']}")

    catalog = load_jsonl(CONTROL / "Catalogo_GM24_639.jsonl", 639, "catalog")
    questions = load_jsonl(
        LIBRARY / "03_metodo_mayeutico" / "Preguntas_Originales_543.jsonl",
        543, "question",
    )
    bm = load_jsonl(
        LIBRARY / "03_metodo_mayeutico" / "Banco_Mayeutico_BM_2395.jsonl",
        2395, "bank",
    )
    counts = Counter(item["type"] for item in catalog)
    if counts != {"base": 240, "atlas": 51, "hybrid": 40, "question_derived": 308}:
        raise ValueError(f"Wrong corpus distribution: {counts}")
    by_id = {row["id"]: row for row in catalog}
    original_ids = {row["id"] for row in questions}
    for row in catalog:
        if row["type"] == "question_derived":
            if row["origin_question"] not in original_ids:
                raise ValueError(f"{row['id']}: missing original question")
            if row["specializes"] and row["specializes"] not in by_id:
                raise ValueError(f"{row['id']}: broken specialization")
        else:
            if any(question_id not in original_ids for question_id in row["questions"]):
                raise ValueError(f"{row['id']}: invalid linked original question")
    for row in questions:
        if row["direct_id"] not in by_id:
            raise ValueError(f"{row['id']}: broken direct concept")
        if row["gm24_id"] and (
            row["gm24_id"] not in by_id
            or by_id[row["gm24_id"]]["type"] == "question_derived"
        ):
            raise ValueError(f"{row['id']}: broken base-corpus link")
    if Counter(row["form"] for row in questions) != {
        "interrogativa": 539, "petición imperativa": 4
    }:
        raise ValueError("Questions' source modality changed")
    if any(row["concept_id"] not in by_id for row in bm):
        raise ValueError("A generated maieutic question has no concept")
    if sorted(int(row["id"][3:]) for row in bm) != list(range(1, 2396)):
        raise ValueError("BM sequence is incomplete")

    word_limits = {
        "01_base_gm24": (240, 600),
        "02_ampliaciones_atlas": (51, 550),
        "03_hibridos_candidatos": (40, 550),
    }
    md_by_type = {}
    for folder, (expected, minimum) in word_limits.items():
        files = list((LIBRARY / "02_conceptos" / folder).glob("*.md"))
        if len(files) != expected:
            raise ValueError(f"{folder}: expected {expected} concept notes, found {len(files)}")
        if any(len(re.findall(r"\b\w+\b", file.read_text(encoding="utf-8"))) < minimum for file in files):
            raise ValueError(f"{folder}: a concept note is under {minimum} words")
        md_by_type[folder] = len(files)
    derived_files = list(
        (LIBRARY / "03_metodo_mayeutico" / "01_tesis_derivadas").glob("*.md")
    )
    if len(derived_files) != 308 or any(
        len(re.findall(r"\b\w+\b", file.read_text(encoding="utf-8"))) < 350
        for file in derived_files
    ):
        raise ValueError("Derived propositions are incomplete")
    units = list((LIBRARY / "01_unidades").glob("*/Unidad_*.md"))
    if len(units) != 24:
        raise ValueError(f"Expected 24 unit guides, found {len(units)}")
    for path in units:
        content = path.read_text(encoding="utf-8")
        if any(f"### {number}. " not in content for number in range(1, 9)):
            raise ValueError(f"{path}: unit lacks an exercise modality")
        if "Rúbrica formativa" not in content:
            raise ValueError(f"{path}: unit lacks an evaluation rubric")

    marker = re.compile(r"<!-- generado-gm24 sha256:([a-f0-9]{64}) -->\n")
    bad_links = []
    generated = 0
    links = 0
    for path in LIBRARY.rglob("*.md"):
        content = path.read_text(encoding="utf-8")
        match = marker.match(content)
        if match:
            generated += 1
            if hashlib.sha256(content[match.end():].encode("utf-8")).hexdigest() != match.group(1):
                raise ValueError(f"Generated Markdown edited after publication: {path}")
        for ref in re.findall(r"(?<!\!)\[[^\]]+\]\(([^)]+)\)", content):
            if ref.startswith(("https://", "http://", "mailto:", "#")):
                continue
            links += 1
            target = (path.parent / unquote(ref.split("#")[0].split("?")[0])).resolve()
            if not target.exists():
                bad_links.append((str(path), ref))
    if generated != 670 or bad_links:
        raise ValueError(f"Generated MD={generated}; broken links={bad_links[:3]}")

    workbook = load_workbook(MASTER, read_only=True, data_only=False)
    try:
        actual = {name: workbook[name].max_row - 1 for name in EXPECTED}
        if actual != EXPECTED:
            raise ValueError(f"Wrong master Excel sheet sizes: {actual}")
        total_hours = sum(row[6] for row in workbook["Plan_800h"].iter_rows(
            min_row=2, values_only=True
        ))
        if total_hours != 800:
            raise ValueError(f"Program sums to {total_hours}, not 800 hours")
        if any(row[1] == "hybrid" and row[3] != "Transversal"
               for row in workbook["Conceptos_331"].iter_rows(min_row=2, values_only=True)):
            raise ValueError("A hybrid has been assigned exclusively to a unit")
    finally:
        workbook.close()
    unit_workbooks = list((LIBRARY / "01_unidades").glob("*/Unidad_*.xlsx"))
    if len(unit_workbooks) != 24:
        raise ValueError(f"Expected 24 unit workbooks, found {len(unit_workbooks)}")
    for path in unit_workbooks:
        unit = path.parent.name
        book = load_workbook(path, read_only=True, data_only=False)
        try:
            if book["Conceptos"].max_row - 1 not in (12, 13):
                raise ValueError(f"{unit}: wrong 10+2/3 concept count")
            if book["Ejercicios_8"].max_row - 1 != 8:
                raise ValueError(f"{unit}: eight modalities not represented in Excel")
        finally:
            book.close()
    checks = {
        "status": "ready_as_working_library",
        "scanned_files": manifest["root_screened_files"],
        "curated_sources": manifest["unique_copies"],
        "curated_duplicates": manifest["identical_duplicates"],
        "units": len(units),
        "main_corpus": dict(counts),
        "derived_notes": len(derived_files),
        "original_questions": len(questions),
        "templated_questions": len(bm),
        "unit_exercises": len(units) * 8,
        "design_hours_not_accredited": total_hours,
        "generated_markdown": generated,
        "excel_workbooks": 1 + len(unit_workbooks),
        "internal_links_resolved": links,
        "schema_validated": "Esquemas_GM24.json (Draft 2020-12)",
        "reservations": [
            "The original matrix without suffix returned Result is protected through WorkIQ.",
            "The exact 20250604 historical workbook was not found through WorkIQ.",
            "51 AMP ideas are [P], 40 HC are candidates; neither group is formally approved.",
            "800 hours and exercise rubrics are proposals requiring academic approval.",
            "No unit video was verified; the other library has only candidate links.",
        ],
    }
    result = LIBRARY / "05_calidad" / "Resultados_Auditoria.json"
    result.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checks, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    audit()

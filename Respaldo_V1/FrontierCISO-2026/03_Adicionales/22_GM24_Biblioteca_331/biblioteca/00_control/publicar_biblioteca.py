#!/usr/bin/env python3
"""Publish the traceable 24-unit GM24 library and accompanying Excel snapshots."""

import hashlib
import json
import re
from pathlib import Path

from gm24_excel import (
    master_counts, unit_counts, validate_workbook, workbook_master, workbook_unit,
)
from gm24_model import LIBRARY, ROOT, build_model
from gm24_render import (
    concept_markdown, concept_path, derived_index_markdown,
    index_markdown, method_markdown, program_markdown, proposition_markdown,
    quality_markdown, questions_markdown, source_contract_markdown,
    unit_markdown, unit_path,
)


GENERATOR = re.compile(r"<!-- generado-gm24 sha256:([a-f0-9]{64}) -->\n")
STATE = LIBRARY / "00_control" / "Estado_Publicacion.json"


def sha256(content):
    return hashlib.sha256(content).hexdigest()


def tagged(body):
    return f"<!-- generado-gm24 sha256:{sha256(body.encode('utf-8'))} -->\n{body}"


def preflight(path, content):
    if not path.exists():
        return
    before = path.read_text(encoding="utf-8")
    match = GENERATOR.match(before)
    if not match:
        raise FileExistsError(f"No se sobrescribe un documento no generado: {path}")
    remainder = before[match.end():]
    if sha256(remainder.encode("utf-8")) != match.group(1):
        raise ValueError(f"Hay cambios manuales en {path}; no se sobrescriben")
    if before != content:
        raise ValueError(
            f"La fuente cambió desde la publicación de {path}; "
            "publique una edición nueva en lugar de reemplazar silenciosamente"
        )


def build_text_files(model):
    result = {}
    for item in model["concepts"].values():
        path = concept_path(item)
        result[path] = tagged(concept_markdown(item, model))
    for item in model["derived"].values():
        path = concept_path(item)
        result[path] = tagged(proposition_markdown(item, model))
    for unit in model["units"].values():
        result[unit_path(unit["id"])] = tagged(unit_markdown(unit, model))
    extras = {
        LIBRARY / "Indice_Biblioteca_GM24.md": index_markdown(model),
        LIBRARY / "03_metodo_mayeutico" / "Metodo_Preguntas_y_Enunciados.md": method_markdown(model),
        LIBRARY / "03_metodo_mayeutico" / "Indice_Tesis_308.md": derived_index_markdown(model),
        LIBRARY / "03_metodo_mayeutico" / "Banco_Preguntas_543.md": questions_markdown(model),
        LIBRARY / "04_programa" / "Programa_GM24_y_Integracion.md": program_markdown(model),
        LIBRARY / "05_calidad" / "Control_Final_GM24.md": quality_markdown(model),
        LIBRARY / "00_control" / "Contrato_Analisis_Fuentes.md": source_contract_markdown(model),
    }
    for path, body in extras.items():
        result[path] = tagged(body)
    return result


def json_records(model):
    catalog = []
    for item in model["concepts"].values():
        catalog.append({
            "id": item["id"], "name": item["title"], "type": item["type"],
            "status": item["status"], "unit": item["unit"],
            "related_units": item["related_units"],
            "statement": item["definition"],
            "questions": item["linked_questions"],
            "generated_bm_count": len(item["bm_ids"]),
            "source": (
                item["workbook_source"] + "#" + item["workbook_idea_cell"]
                if item["type"] == "atlas"
                else Path(item["source_path"]).relative_to(ROOT).as_posix()
                + "#L" + str(item["source_start"])
            ),
        })
    for item in model["derived"].values():
        catalog.append({
            "id": item["id"], "name": item["title"], "type": item["type"],
            "status": item["status"], "unit": item["unit"],
            "related_units": item["related_units"],
            "statement": item["definition"],
            "origin_question": item["origin_question"],
            "specializes": item["specializes"],
            "source": Path(model["curated_question_sources"]["preessays"])
            .relative_to(ROOT).as_posix()
            + "#" + item["source_locator"],
        })
    if len(catalog) != 639:
        raise ValueError(f"Expected 639 classified catalog entries, found {len(catalog)}")
    return {
        LIBRARY / "00_control" / "Catalogo_GM24_639.jsonl": catalog,
        LIBRARY / "03_metodo_mayeutico" / "Preguntas_Originales_543.jsonl":
            list(model["questions"].values()),
        LIBRARY / "03_metodo_mayeutico" / "Banco_Mayeutico_BM_2395.jsonl":
            model["bank"],
    }


def publish():
    model = build_model()
    content = build_text_files(model)
    data = {
        path: "\n".join(
            json.dumps(row, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
            for row in rows
        ) + "\n"
        for path, rows in json_records(model).items()
    }
    workbooks = {
        LIBRARY / "Mapa_GM24_331_y_Metodo.xlsx":
            (workbook_master(model), master_counts(model))
    }
    for unit in model["units"].values():
        path = unit_path(unit["id"]).with_suffix(".xlsx")
        workbooks[path] = (workbook_unit(unit, model), unit_counts(unit, model))
    if len(content) != 670 or len(workbooks) != 25 or len(data) != 3:
        raise ValueError(
            f"Unexpected shape: md={len(content)}, Excel={len(workbooks)}, data={len(data)}"
        )
    for path, text in content.items():
        preflight(path, text)
    for path, text in data.items():
        if path.exists() and path.read_text(encoding="utf-8") != text:
            raise ValueError(f"Hay cambios en el JSONL generado; no se sobrescribe: {path}")
    for path in workbooks:
        if path.exists():
            raise FileExistsError(f"Libro ya existente, no sobrescribir: {path}")
    if STATE.exists():
        raise FileExistsError(
            f"Existe una edición previa: {STATE}. "
            "Cree una nueva edición versionada para cambiar fuentes."
        )
    for path, text in content.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"Markdown: {len(content)} fichas, unidades e índices", flush=True)
    for path, text in data.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print("JSONL: 639 conceptos, 543 formulaciones, 2.395 preguntas BM", flush=True)
    for position, (path, (book, counts)) in enumerate(workbooks.items(), 1):
        path.parent.mkdir(parents=True, exist_ok=True)
        book.save(path)
        validate_workbook(path, counts)
        book.close()
        if position == 1 or position % 6 == 0 or position == len(workbooks):
            print(f"Excel verificables: {position}/{len(workbooks)}", flush=True)
    STATE.write_text(
        json.dumps({
            "edition": "2026-11",
            "manifest": "Curado02/00_control/Manifiesto_Curado02.json",
            "root_screened": model["manifest"]["root_screened_files"],
            "units": len(model["units"]),
            "main_corpus": len(model["concepts"]),
            "derived_propositions": len(model["derived"]),
            "original_questions": len(model["questions"]),
            "templated_questions": len(model["bank"]),
            "exercises": 8 * len(model["units"]),
            "published_markdown": len(content),
            "published_excel": len(workbooks),
            "published_jsonl": len(data),
            "root_index": str(LIBRARY / "Indice_Biblioteca_GM24.md"),
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Publicado y verificado: {LIBRARY}", flush=True)


if __name__ == "__main__":
    publish()

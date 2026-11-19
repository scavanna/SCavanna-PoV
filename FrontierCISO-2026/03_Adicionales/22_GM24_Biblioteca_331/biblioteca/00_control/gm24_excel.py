#!/usr/bin/env python3
"""Publish read-only Excel snapshots of the reconciled GM24 learning library."""

import re
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

from gm24_model import LIBRARY, ROOT
from gm24_render import learning_exercises


HEADER_FILL = PatternFill("solid", fgColor="B11F4B")
PALE_FILL = PatternFill("solid", fgColor="F7F4EF")
PLAIN_FILL = PatternFill("solid", fgColor="FFFFFF")


def safe(value):
    if value is None:
        return ""
    if isinstance(value, (int, float)):
        return value
    result = str(value)
    if len(result) > 32767:
        raise ValueError(f"Excel cell exceeds 32767 characters ({len(result)})")
    if re.match(r"^\s*[=+\-@]", result):
        return "'" + result
    return result


def add_rows(book, name, headers, rows, widths=None):
    sheet = book.create_sheet(name)
    sheet.append(headers)
    for row in rows:
        if len(row) != len(headers):
            raise ValueError(f"{name}: row has {len(row)} values, expected {len(headers)}")
        sheet.append([safe(value) for value in row])
    sheet.freeze_panes = "D2" if len(headers) > 5 else "A2"
    sheet.sheet_view.showGridLines = False
    sheet.row_dimensions[1].height = 40
    for cell in sheet[1]:
        cell.fill = HEADER_FILL
        cell.font = Font(name="Aptos", size=11, bold=True, color="FFFFFF")
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for index, row in enumerate(sheet.iter_rows(min_row=2), 2):
        fill = PALE_FILL if index % 2 == 0 else PLAIN_FILL
        for cell in row:
            cell.fill = fill
            cell.font = Font(name="Aptos", size=10, color="242424")
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        if sheet.max_row <= 800:
            sheet.row_dimensions[index].height = 42
    if sheet.max_row > 1:
        sheet.auto_filter.ref = sheet.dimensions
    for index, header in enumerate(headers, 1):
        width = widths[index - 1] if widths else (
            22 if header.lower() in ("id", "unidad", "tipo") else 55
        )
        sheet.column_dimensions[sheet.cell(1, index).column_letter].width = width
    sheet.print_title_rows = "1:1"
    return sheet


def guide(book, description):
    sheet = book.active
    sheet.title = "Guia"
    rows = [
        ("Biblioteca GM-24", description),
        ("Versión", "Fuente curricular noviembre 2026; informe y Excel son vistas derivadas reproducibles desde Curado02."),
        ("331 = 240 + 51 + 40", "240 conceptos base con idea central; 51 ampliaciones Atlas [P]; 40 híbridos HC candidatos incluidos por decisión del propietario."),
        ("Banco AP", "308 tesis derivadas de preguntas se presentan aparte del núcleo de 331. El corpus mayéutico ampliado contiene 639 pre-ensayos."),
        ("Preguntas", "543 formulaciones originales (539 interrogativas y 4 peticiones), y 2.395 textos BM construidos con ocho plantillas."),
        ("Fuentes", "Véase el manifiesto SHA-256 de Curado02 y las celdas 06Ensayos!I285:I335 para las 51 AMP."),
        ("Carga de aprendizaje", "24×31 h + capstone 56 h = escenario de 800 h. Solo 24×3 h corresponden a clases directas; no hay acreditación institucional demostrada."),
        ("Relaciones", "Una conexión HC–unidad es muchos-a-muchos. Una correspondencia Atlas/NIST/ISACA es temática, no homologación ni certificación."),
        ("Uso responsable", "Este libro no conserva etiquetas MIP de las fuentes. Verifique derechos y clasificación antes de redistribuir."),
    ]
    for row in rows:
        sheet.append(row)
    sheet.column_dimensions["A"].width = 28
    sheet.column_dimensions["B"].width = 118
    sheet.freeze_panes = "A2"
    sheet.sheet_view.showGridLines = False
    for row in sheet:
        sheet.row_dimensions[row[0].row].height = 66 if row[0].row > 1 else 44
        for cell in row:
            cell.fill = HEADER_FILL if cell.row == 1 else (
                PALE_FILL if cell.row % 2 == 0 else PLAIN_FILL
            )
            cell.font = Font(
                name="Aptos", size=10, bold=cell.column == 1,
                color="FFFFFF" if cell.row == 1 else "242424",
            )
            cell.alignment = Alignment(wrap_text=True, vertical="center")


def base_rows(model, selected_ids=None):
    for item in model["concepts"].values():
        if selected_ids is not None and item["id"] not in selected_ids:
            continue
        source = (
            f"{item['workbook_source']}#{item['workbook_idea_cell']}"
            if item["type"] == "atlas"
            else (
                f"{Path(item['source_path']).relative_to(ROOT).as_posix()}:"
                f"{item['source_start']}-{item['source_end']}"
            )
        )
        yield (
            item["id"], item["type"], item["status"],
            item["unit"] or "Transversal",
            ", ".join(item["related_units"]), item["title"],
            item["definition"], item["text"], source,
            item.get("question", ""),
            ", ".join(item.get("linked_questions", [])),
            ", ".join(item.get("bm_ids", [])),
            item.get("verification_note", ""),
        )


def derived_rows(model, unit_code=None):
    for item in model["derived"].values():
        if unit_code and item["unit"] != unit_code:
            continue
        yield (
            item["id"], item["title"], item["unit"] or "Sin unidad exclusiva",
            ", ".join(item["related_units"]), item["origin_question"],
            item["specializes"], item["definition"], item["tension"],
            item["development"], item["mistake"], item["product"],
            "; ".join(
                f"{link['preensayo']}:{link['relacion']}" for link in item["links"]
            ),
            item["source_locator"], item["status"],
        )


def exercise_rows(model, unit_code=None):
    for unit in model["units"].values():
        if unit_code and unit["id"] != unit_code:
            continue
        for number, exercise in enumerate(learning_exercises(unit, model), 1):
            yield (
                unit["id"], number, exercise["type"],
                exercise["prompt"], exercise["product"],
                exercise["check"], unit["case"]["cognitivo"],
                "Propuesta docente, validación pendiente",
            )


def question_rows(model, unit_code=None):
    for row in model["questions"].values():
        if unit_code:
            linked = model["concepts"].get(row["gm24_id"])
            derived = model["derived"].get(row["direct_id"])
            if not (linked and linked["unit"] == unit_code) and not (
                derived and derived["unit"] == unit_code
            ):
                continue
        yield (
            row["id"], row["form"], row["text"],
            row["gm24_id"], row["direct_id"], row["bank_id"],
            row["related_thesis"], row["related_thesis_status"],
            row["source_locator"],
        )


def workbook_master(model):
    book = Workbook()
    book.properties.title = "TheNextCISO GM-24 — 331 conceptos y método"
    book.properties.subject = "Noviembre 2026; 24 unidades y 308 tesis mayéuticas separadas"
    guide(book, "Catálogo maestro y recursos de formación basados en fuentes curadas.")
    add_rows(
        book, "Unidades_24",
        ("Unidad", "Pilar", "Eje", "Título", "Dominios Atlas propuestos",
         "Conceptos base", "AMP propuestas", "HC vinculados",
         "AP asignados", "Lente cognitiva", "Horas propuestas"),
        [
            (
                unit["id"], unit["pillar"], unit["axis"], unit["title"],
                unit["atlas"], 10, len(unit["amp_ids"]),
                ", ".join(unit["hc_ids"]), len(unit["ap_ids"]),
                unit["case"]["cognitivo"], 31,
            )
            for unit in model["units"].values()
        ],
    )
    add_rows(
        book, "Conceptos_331",
        ("ID", "Tipo", "Estado", "Unidad principal", "Unidades relacionadas",
         "Nombre", "Tesis o enunciado", "Idea central/documento fuente",
         "Archivo o celda de origen", "Pregunta generadora",
         "Preguntas originales relacionadas", "Banco BM", "Nota de verificación"),
        list(base_rows(model)),
    )
    add_rows(
        book, "AMP_51",
        ("ID", "Unidad", "Nombre", "Tesis [P]", "Celda Excel",
         "Vínculo candidato", "Estado"),
        [
            (
                item["id"], item["unit"], item["title"], item["definition"],
                item["workbook_idea_cell"], item["links"][0]["preensayo"],
                item["status"],
            )
            for item in model["concepts"].values() if item["type"] == "atlas"
        ],
    )
    add_rows(
        book, "HC_40",
        ("ID", "Nombre", "Unidades vinculadas", "Relaciones del borrador",
         "Actividad", "Producto", "Criterio", "Estado"),
        [
            (
                item["id"], item["title"], ", ".join(item["related_units"]),
                "; ".join(
                    f"{row['preensayo']}:{row['relacion']} — {row.get('motivo', '')}"
                    for row in item["links"]
                ),
                item["activity"], item["outcome"], item["evaluation"],
                item["status"],
            )
            for item in model["concepts"].values() if item["type"] == "hybrid"
        ],
    )
    add_rows(
        book, "Tesis_AP_308",
        ("ID", "Nombre", "Unidad principal", "Unidades relacionadas",
         "Pregunta origen", "Especializa", "Tesis propuesta", "Tensión",
         "Desarrollo/investigación", "Error", "Producto",
         "Relaciones candidatas", "Localizador JSON", "Estado"),
        list(derived_rows(model)),
    )
    add_rows(
        book, "Preguntas_543",
        ("ID", "Forma", "Texto original", "Vínculo 331",
         "Pre-ensayo directo", "Banco BM", "Tesis AP relacionada",
         "Estado de tesis", "Localizador JSON"),
        list(question_rows(model)),
    )
    add_rows(
        book, "Banco_BM_2395",
        ("ID", "Concepto", "Tipo", "Texto generado por plantilla", "Procedencia"),
        [
            (
                row["id"], row["concept_id"], row["type_name"],
                row["text"], row["provenance"],
            )
            for row in model["bank"]
        ],
    )
    add_rows(
        book, "Ejercicios_192",
        ("Unidad", "Número", "Modalidad", "Consigna",
         "Producto", "Comprobación", "Lente cognitiva", "Estado"),
        list(exercise_rows(model)),
    )
    add_rows(
        book, "Plan_800h",
        ("Unidad", "Título", "Horas clase", "Horas lectura/investigación",
         "Horas laboratorio", "Horas aplicación", "Total propuesto",
         "Estado"),
        [
            (
                unit["id"], unit["title"], 3, 8, 12, 8, 31,
                "Escenario no acreditado",
            )
            for unit in model["units"].values()
        ] + [
            ("Capstone", "Proyecto y defensa integradores", 0, 8, 16, 32, 56,
             "Escenario no acreditado")
        ],
    )
    add_rows(
        book, "Fuentes_31",
        ("Copia curada", "Original", "SHA-256", "Bytes",
         "Uso", "Orígenes idénticos", "Nota sobre acceso y estado"),
        [
            (
                source["curated_path"], source["canonical_source"],
                source["sha256"], source["bytes"], source["purpose"],
                "; ".join(source["other_identical_origins"]),
                source["interpretation_note"],
            )
            for source in model["manifest"]["items"]
        ],
    )
    return book


def workbook_unit(unit, model):
    book = Workbook()
    book.properties.title = f"Unidad {unit['id']} — TheNextCISO GM-24"
    guide(book, f"{unit['id']}: {unit['title']}. Las diez ideas base y "
          f"{len(unit['amp_ids'])} propuestas Atlas se sitúan en 24 unidades.")
    wanted = set(unit["base_ids"] + unit["amp_ids"])
    add_rows(
        book, "Conceptos",
        ("ID", "Tipo", "Estado", "Unidad principal", "Unidades relacionadas",
         "Nombre", "Tesis o enunciado", "Idea central/documento fuente",
         "Archivo o celda de origen", "Pregunta generadora",
         "Preguntas originales relacionadas", "Banco BM", "Nota de verificación"),
        list(base_rows(model, wanted)),
    )
    add_rows(
        book, "Puentes_HC",
        ("ID", "Nombre", "Unidades", "Actividad", "Evaluación", "Estado"),
        [
            (
                item["id"], item["title"], ", ".join(item["related_units"]),
                item["activity"], item["evaluation"], item["status"],
            )
            for item in (
                model["concepts"][code] for code in unit["hc_ids"]
            )
        ],
    )
    add_rows(
        book, "Ejercicios_8",
        ("Unidad", "Número", "Modalidad", "Consigna",
         "Producto", "Comprobación", "Lente cognitiva", "Estado"),
        list(exercise_rows(model, unit["id"])),
    )
    add_rows(
        book, "Tesis_AP",
        ("ID", "Nombre", "Unidad principal", "Unidades relacionadas",
         "Pregunta origen", "Especializa", "Tesis propuesta", "Tensión",
         "Desarrollo/investigación", "Error", "Producto",
         "Relaciones candidatas", "Localizador JSON", "Estado"),
        list(derived_rows(model, unit["id"])),
    )
    add_rows(
        book, "Preguntas",
        ("ID", "Forma", "Texto original", "Vínculo 331",
         "Pre-ensayo directo", "Banco BM", "Tesis AP relacionada",
         "Estado de tesis", "Localizador JSON"),
        list(question_rows(model, unit["id"])),
    )
    add_rows(
        book, "Banco_BM",
        ("ID", "Concepto", "Tipo", "Texto generado por plantilla", "Procedencia"),
        [
            (
                row["id"], row["concept_id"], row["type_name"],
                row["text"], row["provenance"],
            )
            for row in model["bank"] if row["concept_id"] in wanted
        ],
    )
    return book


def validate_workbook(path, expected_counts):
    book = load_workbook(path, read_only=True, data_only=False)
    try:
        for sheet_name, expected in expected_counts.items():
            if sheet_name not in book.sheetnames:
                raise ValueError(f"{path}: missing sheet {sheet_name}")
            actual = book[sheet_name].max_row - 1
            if actual != expected:
                raise ValueError(
                    f"{path} / {sheet_name}: {actual} rows, expected {expected}"
                )
        for name in book.sheetnames:
            sheet = book[name]
            for row in sheet.iter_rows(values_only=False):
                if any(cell.data_type == "f" for cell in row):
                    raise ValueError(f"{path}/{name}: unintended Excel formula")
    finally:
        book.close()


def master_counts(model):
    return {
        "Unidades_24": 24, "Conceptos_331": 331, "AMP_51": 51, "HC_40": 40,
        "Tesis_AP_308": 308, "Preguntas_543": 543, "Banco_BM_2395": 2395,
        "Ejercicios_192": 192, "Plan_800h": 25, "Fuentes_31": 31,
    }


def unit_counts(unit, model):
    wanted = set(unit["base_ids"] + unit["amp_ids"])
    linked_questions = list(question_rows(model, unit["id"]))
    return {
        "Conceptos": len(wanted),
        "Puentes_HC": len(unit["hc_ids"]),
        "Ejercicios_8": 8,
        "Tesis_AP": len(unit["ap_ids"]),
        "Preguntas": len(linked_questions),
        "Banco_BM": sum(row["concept_id"] in wanted for row in model["bank"]),
    }

#!/usr/bin/env python3
"""Write navigable, source-qualified learning material from the reconciled model."""

import os
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

from gm24_model import LIBRARY, ROOT


KIND = {
    "base": "Concepto curricular base",
    "atlas": "Ampliación Atlas propuesta",
    "hybrid": "Puente híbrido candidato",
    "question_derived": "Tesis derivada de una pregunta mayéutica",
}
BASE_DIR = LIBRARY / "02_conceptos" / "01_base_gm24"
AMP_DIR = LIBRARY / "02_conceptos" / "02_ampliaciones_atlas"
HC_DIR = LIBRARY / "02_conceptos" / "03_hibridos_candidatos"
AP_DIR = LIBRARY / "03_metodo_mayeutico" / "01_tesis_derivadas"


def link_to(path, from_file, title=None):
    dest = Path(path)
    relative = os.path.relpath(dest, from_file.parent).replace("\\", "/")
    return f"[{title or dest.name}]({quote(relative, safe='/-_.')})"


def concept_path(concept):
    directory = {
        "base": BASE_DIR, "atlas": AMP_DIR, "hybrid": HC_DIR,
        "question_derived": AP_DIR,
    }[concept["type"]]
    return directory / f"{concept['id']}.md"


def unit_path(code):
    return LIBRARY / "01_unidades" / code / f"Unidad_{code}.md"


def table_cell(text):
    return str(text or "").replace("|", "\\|").replace("\n", "<br>").strip()


def paragraphs(*parts):
    return "\n\n".join(str(part).strip() for part in parts if str(part).strip())


def render_list(items, empty="No documentado en las fuentes disponibles."):
    return "\n".join(f"- {item}" for item in items) if items else f"- {empty}"


def source_reference(concept, destination, model):
    if concept["type"] == "atlas":
        book = next(
            ROOT / item["curated_path"] for item in model["manifest"]["items"]
            if item["canonical_source"].endswith(
                "/AI_CISO_Atlas_Ensayos_TheNextCISO_x_Core_Accountabilities_FY27_2026-11-05.xlsx"
            )
        )
        register = LIBRARY / "00_control" / "AMP_ideas_propuestas_2026-11.json"
        return (
            f"{link_to(book, destination, 'Matriz de 331 pre-ensayos')}, "
            f"`{concept['workbook_locator']}` (idea `[P]`: `{concept['workbook_idea_cell']}`); "
            f"{link_to(register, destination, 'registro de consulta y estado [P]')}."
        )
    if concept["type"] == "question_derived":
        source = model["curated_question_sources"]["preessays"]
        return (
            f"{link_to(source, destination, 'corpus de pre-ensayos mayéuticos')}, "
            f"`{concept['source_locator']}`."
        )
    return (
        f"{link_to(concept['source_path'], destination, 'texto fuente en Curado02')}, "
        f"líneas {concept['source_start']}–{concept['source_end']}."
    )


def question_examples(concept, destination, model, limit=3):
    originals = [model["questions"][question_id] for question_id in concept.get("linked_questions", [])]
    samples = [
        f"`{row['id']}` ({row['form']}): {row['text']} "
        f"— vínculo `{row['gm24_id'] or row['direct_id']}`."
        for row in originals[:limit]
    ]
    templates = [
        f"`{entry['id']}` [{entry['type_name']}]: {entry['text']}"
        for entry in model["bank"]
        if entry["id"] in concept.get("bm_ids", [])[:3]
    ]
    source = model["curated_question_sources"]["questions"]
    return paragraphs(
        "**Preguntas originales consolidadas (si hay vínculo directo o de corpus):**\n"
        + render_list(samples, "Sin pregunta original vinculada explícitamente."),
        "**Ejemplos generados con plantillas mayéuticas documentadas:**\n"
        + render_list(templates, "Sin serie de banco asignada."),
        "Las preguntas de banco son construcciones mediante plantilla; no se presentan "
        "como citas de entrevistas. Fuente original: "
        + link_to(source, destination, "preguntas consolidadas") + ".",
    )


def exercise_for_concept(concept, unit, model):
    case = unit["case"]
    label = concept["title"]
    case_task = (
        f"Ante «{case['escenario'].rstrip('.')}», explica qué aporta «{label}» frente a "
        f"las opciones «{case['alternativas'].rstrip('.')}». Usa {case['insumos']} y entrega "
        f"{case['entregable']}. "
    )
    if concept["type"] == "atlas":
        case_task += "Distingue tesis [P] de evidencia obtenida y de supuestos de diseño."
    if concept["type"] == "hybrid":
        case_task += "Justifica cada relación interunidad y no la trates como causal sin prueba."
    review = (
        f"Se acepta para revisión si identifica autoridad y límites, documenta fuentes "
        f"y supuestos, compara al menos dos decisiones y demuestra «{case['criterio_critico'].rstrip('.')}». "
        "La rúbrica de la unidad es una propuesta docente, no un estándar aprobado."
    )
    return case_task, review


def concept_markdown(concept, model):
    destination = concept_path(concept)
    unit = model["units"].get(concept.get("unit"))
    if concept["type"] == "hybrid":
        related = concept["related_units"]
        unit = model["units"][related[0]]
    case = unit["case"] if unit else None
    places = (
        ", ".join(concept["related_units"]) if concept["related_units"] else "por asignar"
    )
    heading = [
        f"# {concept['id']} — {concept['title']}",
        f"**Clase:** {KIND[concept['type']]} · **Estado:** {concept['status']} · "
        f"**Unidades:** {places}.",
        "## Enunciado y fuerza de la evidencia",
        concept["definition"],
    ]
    if concept["type"] == "base":
        heading += [
            "La frase inicial es una síntesis del primer párrafo de la idea central. "
            "El desarrollo siguiente proviene del lote editorial de noviembre de 2026; "
            "no es un ensayo final ni una validación empírica.",
            "## Desarrollo extenso de la idea central (fuente)",
            concept["text"],
            "## Interpretación situada y ejercicio docente",
        ]
    elif concept["type"] == "atlas":
        related_id = concept["links"][0]["preensayo"]
        related = model["concepts"][related_id]
        heading += [
            "**Importante:** en el Documento Maestro se documentó el **título** de "
            f"`{concept['id']}`; la oración precedente es una **tesis propuesta [P]** "
            "en la matriz posterior, no una definición aprobada del programa.",
            "## Desarrollo para el aprendizaje (derivación editorial)",
            f"Esta ampliación examina «{concept['title']}» en la unidad "
            f"`{unit['id']}` ({unit['title']}). Su pregunta de diseño es qué "
            f"cambiaría en la decisión de {case['decision'].rstrip('.').lower()} "
            f"al tomar en serio la tesis [P]. "
            f"El vínculo `{related_id}` —{related['title']}— "
            f"aporta una lente vecina: «{related['definition'].rstrip('.')}». La relación "
            "no implica identidad de conceptos, aprobación del nuevo tema ni "
            "eficacia demostrada de una intervención.",
            f"En la organización ficticia del programa: {case['escenario']} "
            f"Una solución defendible debe contrastar estas alternativas: "
            f"{case['alternativas'].rstrip('.')}; "
            f"las observaciones iniciales serían {case['insumos']}. El estudiante "
            "separa lo observado, lo inferido y lo aún no verificable antes de "
            "sugerir cambios de arquitectura, gobierno u operación.",
            f"El producto de aprendizaje propuesto es «{case['entregable']}». "
            f"Debe poder explicar por qué su recomendación es revisable y "
            f"cómo verificaría que «{case['criterio_critico'].rstrip('.')}». "
            "La propuesta permanece abierta a revisión curricular y técnica.",
            "## Ejercicio y criterio de evaluación",
        ]
        if concept.get("verification_note"):
            heading.append(f"**Afirmación que exige verificación adicional:** {concept['verification_note']}")
    else:
        heading += [
            "**Importante:** se incorpora al **corpus de trabajo** por decisión "
            "del usuario, conservando explícitamente la condición de candidato "
            "a revisión editorial y ontológica. No crea una unidad adicional.",
            "## Desarrollo integrador del documento fuente",
            concept["text"],
            "## Lectura relacional guiada (derivación editorial)",
            f"El documento vincula `{concept['links'][0]['preensayo']}` "
            f"({model['concepts'][concept['links'][0]['preensayo']]['title']}) mediante "
            f"`{concept['links'][0]['relacion']}` y "
            f"`{concept['links'][1]['preensayo']}` "
            f"({model['concepts'][concept['links'][1]['preensayo']]['title']}) mediante "
            f"`{concept['links'][1]['relacion']}`. Contrasta qué prueba, orden "
            "o intercambio haría falta para justificar cada verbo; cuando "
            "no exista esa prueba, trátalo como asociación analítica y "
            "conserva sus alternativas. El puente debe explicar interacciones "
            "sin reemplazar la ficha de ninguno de sus componentes.",
            "## Transferencia al ejercicio de unidad",
        ]
    if case:
        task, review = exercise_for_concept(concept, unit, model)
        heading.extend([f"**Práctica:** {task}", f"**Validación:** {review}"])
    if concept.get("unit"):
        heading.append(
            "La guía de unidad desarrolla el escenario longitudinal, las ocho "
            f"modalidades de ejercicio y la rúbrica: {link_to(unit_path(concept['unit']), destination, 'abrir unidad')}."
        )
    else:
        heading.append(
            "Se estudia como puente transversal; sus relaciones con unidades "
            "no son una asignación exclusiva ni una dependencia automática."
        )
    heading.extend([
        "## Preguntas del método y comprobación",
        question_examples(concept, destination, model),
        "## Procedencia y límites",
        source_reference(concept, destination, model),
        "El nombre del marco, su aparición en el corpus y una alineación temática "
        "no acreditan dominio profesional, cumplimiento ni aprobación formal. "
        "Las referencias bibliográficas individuales solo se atribuyen si "
        "la fuente las identifica; véase el documento maestro para bibliografía "
        "general de NIST e ISACA y para la condición propuesta de sus mapeos.",
    ])
    if concept.get("unit"):
        heading.append(
            f"{link_to(unit['source_path'], destination, 'Documento Maestro')}, "
            f"sección `{unit['id']}` (línea {unit['source_line']})."
        )
    return paragraphs(*heading) + "\n"


def proposition_markdown(item, model):
    destination = concept_path(item)
    question = model["questions"][item["origin_question"]]
    status = (
        f"`{item['unit']}` (especialización explícita)"
        if item["unit"] else
        ("Vínculo transversal; sin asignación exclusiva a unidad" if item["specializes"]
         else "Unidad principal no asignada en la fuente; hay relaciones candidatas")
    )
    linked = [
        f"`{row['preensayo']}` — `{row['relacion']}`: {row.get('motivo', '')}"
        for row in item["links"]
    ]
    part = [
        f"# {item['id']} — {item['title']}",
        f"**Tipo:** tesis ampliada por pregunta · **Estado:** propuesta editorial "
        f"del corpus mayéutico, no concepto original GM-24 · **Ubicación:** {status}.",
        "## Pregunta original (sin sustituirla)",
        f"`{question['id']}` · {question['form']}: {question['text']}",
        "La formulación anterior es contenido de la fuente. La tesis siguiente "
        "no es una cita literal de esa pregunta: es el **enunciado declarativo "
        "ya registrado como propuesta** en el corpus de pre-ensayos.",
        "## Tesis propuesta",
        item["definition"],
        "## Tensión, prueba y limitación",
        f"**Tensión documentada:** {item['tension']}",
        f"**Desarrollo/investigación propuesto:** {item['development']}",
        f"**Error a evitar:** {item['mistake']}",
        f"**Producto observable:** {item['product']}",
        "## Relaciones candidatas",
        render_list(linked),
        f"**Especializa:** `{item['specializes']}`." if item["specializes"]
        else "**Especializa:** sin valor explícito en la fuente. No se asignó unidad "
             "por proximidad temática ni por la primera arista.",
        "## Ejercicio de método",
        "Conserva la pregunta inicial. En un caso real, identifica qué datos "
        "la harían relevante, prueba la tesis contra al menos una interpretación "
        "alternativa y explica cuál sería la decisión revisable. Entrega "
        f"{item['product']}. Se considera logrado solo si la evidencia documenta "
        "la tesis sin transformar la pregunta original en hecho establecido.",
        "## Procedencia",
        source_reference(item, destination, model),
        f"Pregunta original: {link_to(model['curated_question_sources']['questions'], destination)}"
        f", `{question['source_locator']}`. "
        "Toda relación marcada en la fuente sigue siendo candidata para "
        "revisión por expertos, no una arista aprobada de la ontología.",
    ]
    return paragraphs(*part) + "\n"


def learning_exercises(unit, model):
    case = unit["case"]
    a, b = case["par"]
    first, second = model["concepts"][a], model["concepts"][b]
    amp = model["concepts"][case["amp"]]
    hc = model["concepts"].get(case["hc"]) if case["hc"] else None
    cross = f"`{hc['id']}` — {hc['title']}" if hc else (
        "la unidad G3.1 como contraste normativo propuesto (no equivalencia)"
    )
    return [
        {
            "type": "Comprensión conceptual",
            "prompt": (
                f"Define `{a}` ({first['title']}) y `{b}` ({second['title']}) con "
                "tus palabras. Señala una frontera de responsabilidad, una "
                f"confusión habitual y cómo la ampliación `{amp['id']}` altera "
                f"la interpretación del caso «{case['escenario']}»."
            ),
            "product": "cuadro de contraste con dos decisiones distintas y citas a las fichas",
            "check": "No declara como sinónimos dos títulos vecinos ni toma la tesis [P] como definición aprobada.",
        },
        {
            "type": "Relaciones y contextualización",
            "prompt": (
                f"Dibuja la cadena de decisiones entre `{a}`, `{b}`, `{amp['id']}` "
                f"y {cross}. Anota en cada conexión dirección, evidencia textual, "
                "posible solapamiento y qué cambiaría al variar el contexto de negocio. "
                "Las aristas nuevas son hipótesis hasta que se validen."
            ),
            "product": "mapa de relaciones G–M y tabla de procedencia de cada enlace",
            "check": "No transforma cercanía temática en causalidad ni convierte HC en requisito aprobado.",
        },
        {
            "type": "Práctica aplicada",
            "prompt": (
                f"Trabaja en «{case['escenario']}». Con {case['insumos']}, "
                f"construye {case['entregable']}; incluye propietario, condiciones "
                "de entrada y salida, hipótesis adversa y prueba de funcionamiento."
            ),
            "product": case["entregable"],
            "check": case["criterio_critico"],
        },
        {
            "type": "Investigación y fuentes",
            "prompt": (
                f"Investiga esta pregunta acotada: {case['investigacion']} "
                "Localiza al menos dos fuentes primarias con fecha y versión; "
                "distingue obligación, recomendación, definición, ejemplo y opinión."
            ),
            "product": "ficha de fuentes con extractos breves, localizador y discrepancias",
            "check": "No cita un borrador editorial o mapeo informativo como norma obligatoria.",
        },
        {
            "type": "Orquestación de actores y agentes",
            "prompt": (
                f"Con {case['contraparte']}, construye un flujo de tres hitos "
                f"para «{case['decision']}». Define qué puede proponer un agente, "
                "qué requiere aprobación humana, quién responde y cómo detener, "
                "registrar y revertir una acción errónea."
            ),
            "product": "RACI/DACI, diagrama de traspasos y plan de supervisión",
            "check": "Hay autoridad, trazas y camino de escalamiento para cada acción de alto impacto.",
        },
        {
            "type": "Análisis y contrafactual",
            "prompt": (
                f"Compara «{case['alternativas']}» usando datos de {case['insumos']}. "
                f"Contrasta la primera impresión con la lente cognitiva "
                f"`{case['cognitivo']}` del programa metacognitivo; plantea qué "
                "evidencia falsaría cada hipótesis y un efecto de segundo orden."
            ),
            "product": "matriz de alternativas, incertidumbres y pruebas refutatorias",
            "check": "La comparación conserva supuestos, costos de reversión y consecuencias no observadas.",
        },
        {
            "type": "Toma de decisiones",
            "prompt": (
                f"Redacta para el responsable competente una recomendación "
                f"sobre «{case['decision']}», con dos opciones, beneficio, "
                "riesgo residual, autoridad de aceptación, indicador temprano "
                "y condición explícita de pausa o rollback."
            ),
            "product": "memorando ejecutivo de una página más expediente de evidencia",
            "check": case["criterio_critico"],
        },
        {
            "type": "Exposición y defensa",
            "prompt": (
                f"Defiende la decisión ante {case['contraparte']} en siete "
                "minutos; reserva tres para objeciones. Un par cambia un dato "
                "del escenario a mitad de la exposición: revisa la postura "
                "sin ocultar el supuesto que deja de sostenerse."
            ),
            "product": "presentación oral, preguntas difíciles y registro de revisiones",
            "check": "La defensa distingue certeza, incertidumbre, decisión y propiedad del riesgo.",
        },
    ]


def rubric_for_unit(unit):
    return (
        "| Criterio | 0 — insuficiente | 2 — parcial | 4 — sólido |\n"
        "|---|---|---|---|\n"
        "| Precisión | Confunde conceptos, categorías o estados editoriales | "
        "Explica definiciones sin límites | Distingue base, propuesta y candidato; "
        "explica límites y relaciones sin equivalencias ficticias |\n"
        "| Evidencia | Cita sin procedencia ni prueba | Traza fuentes pero no su calidad | "
        "Localiza fuente, versión, modalidad, incertidumbre y prueba de eficacia |\n"
        "| Decisión y autoridad | No compara opciones ni propietario | "
        "Compara pero sin residual o escalamiento | Justifica alternativas, "
        "derecho de decisión, residual, parada y revisión |\n"
        "| Transferencia | Entrega teórica sin caso | Caso parcial sin contraprueba | "
        "Artefacto operable, prueba adversa y defensa ajustada a la audiencia |\n\n"
        f"**Condición crítica de esta unidad:** {unit['case']['criterio_critico']} "
        "La práctica se devuelve para revisión si incumple este criterio, "
        "aunque el promedio sea alto. Para aprendizaje se propone al menos "
        "3/4 en cada dimensión; no es una acreditación aprobada."
    )


def unit_markdown(unit, model):
    destination = unit_path(unit["id"])
    case = unit["case"]
    items = model["concepts"]
    master = unit["source_path"]
    base = [items[concept_id] for concept_id in unit["base_ids"]]
    amp = [items[concept_id] for concept_id in unit["amp_ids"]]
    hybrids = [items[concept_id] for concept_id in unit["hc_ids"]]
    derived_here = [model["derived"][code] for code in unit["ap_ids"]]
    cross_derived = [
        row for row in model["derived"].values()
        if not row["unit"] and unit["id"] in row["related_units"]
    ]
    base_summaries = [
        f"### {entry['id']} — {entry['title']}\n\n"
        f"{entry['definition']} {entry['source_tension']} "
        f"El desarrollo completo y sus límites están en "
        f"{link_to(concept_path(entry), destination, 'la ficha de idea central')} "
        f"({entry['word_count']} palabras de borrador, no ensayo final)."
        for entry in base
    ]
    amp_summaries = [
        f"**{link_to(concept_path(entry), destination, entry['id'] + ' — ' + entry['title'])} "
        f"[P].** {entry['definition']} Vínculo propuesto: "
        f"`{entry['links'][0]['preensayo']}`; fuente `{entry['workbook_idea_cell']}`."
        for entry in amp
    ]
    hc_summaries = [
        f"{link_to(concept_path(entry), destination, entry['id'] + ' — ' + entry['title'])}: "
        f"conecta {', '.join('`'+r['preensayo']+'`' for r in entry['links'][:4])}. "
        f"**Candidato**, no unidad ni arista aprobada."
        for entry in hybrids
    ]
    exercises = learning_exercises(unit, model)
    tasks = [
        f"### {index}. {entry['type']}\n\n"
        f"**Consigna:** {entry['prompt']}\n\n"
        f"**Producto:** {entry['product']}.\n\n"
        f"**Comprobación:** {entry['check']}"
        for index, entry in enumerate(exercises, 1)
    ]
    questions = [
        question for question in model["questions"].values()
        if question["gm24_id"] in set(unit["base_ids"] + unit["amp_ids"])
    ]
    original_prompts = [
        f"`{row['id']}`: {row['text']} (vínculo `{row['gm24_id']}`)."
        for row in questions[:6]
    ]
    bm_index = {question["id"]: question for question in model["bank"]}
    selected_bm = [
        f"`{bm_index[code]['id']}` — {bm_index[code]['text']}"
        for concept in base[:2] + amp[:1]
        for code in concept["bm_ids"][:2]
    ]
    AP_sample = [
        f"{link_to(concept_path(row), destination, row['id'] + ' — ' + row['title'])} "
        f"← `{row['origin_question']}`"
        for row in derived_here[:8]
    ]
    AP_cross = [
        f"{link_to(concept_path(row), destination, row['id'])} "
        "(relación transversal, no asignación principal)"
        for row in cross_derived[:5]
    ]
    source_lots = sorted({entry["source_path"] for entry in base})
    sources = [
        f"{link_to(master, destination, 'Documento Maestro')}, "
        f"unidad `{unit['id']}` desde línea {unit['source_line']}.",
        *[link_to(path, destination, "lote de ideas base") for path in source_lots],
        "Las 51 tesis Atlas [P] proceden de `06Ensayos!I285:I335` en "
        + link_to(
            next(
                ROOT / item["curated_path"] for item in model["manifest"]["items"]
                if item["canonical_source"].endswith(
                    "/AI_CISO_Atlas_Ensayos_TheNextCISO_x_Core_Accountabilities_FY27_2026-11-05.xlsx"
                )
            ),
            destination,
            "matriz de pre-ensayos",
        ) + ".",
    ]
    result = [
        f"# {unit['id']} — {unit['title']}",
        f"**Pilar:** {unit['pillar']} · **Eje:** {unit['axis']} · "
        f"**Atlas:** `{unit['atlas']}` (alineación editorial, no identidad de dominio).",
        f"**Pregunta rectora de fuente:** {unit['guiding_question']}",
        "**Alcance:** diez conceptos base con idea central desarrollada; "
        f"{len(amp)} ampliaciones Atlas cuyo título pertenece al Documento Maestro "
        "y cuya tesis es propuesta [P]. Los puentes HC relacionados son candidatos "
        "transversales; ninguna extensión altera por sí sola el número de unidades.",
        "## Situación longitudinal y decisión",
        f"**Organización ficticia:** {case['escenario']}",
        f"**Decisión a sostener:** {case['decision']}",
        f"**Cursos de acción en tensión:** {case['alternativas']}",
        f"**Información inicial:** {case['insumos']}",
        f"**Interesados:** {case['contraparte']}",
        f"**Producto acumulativo:** {case['entregable']}",
        f"**Regla de seguridad y responsabilidad:** {case['criterio_critico']}",
        "## Desarrollo de los diez conceptos base",
        *base_summaries,
        "## Ampliaciones Atlas de esta unidad: tesis para discutir, no definiciones aprobadas",
        render_list(amp_summaries),
        "## Conceptos híbridos candidatos que conectan esta unidad",
        render_list(hc_summaries, "No hay HC con enlace explícito a esta unidad; "
                    "se pueden analizar conexiones como hipótesis editoriales."),
        "## Puente con TheMetaCognitiveCISO",
        f"Se propone entrenar la lente cognitiva `{case['cognitivo']}` junto a las "
        f"decisiones de `{unit['id']}`. Esta es una **relación pedagógica derivada**, "
        "no una equivalencia canónica con el GM-24. Consulte "
        + link_to(
            ROOT / "Biblioteca_CISO_Frontera" / "Caja_Cognitiva_CISO_72" / "00_Indice.md",
            destination,
            "la caja cognitiva del CISO",
        ) + " para la ficha y su evidencia.",
        "## Laboratorio: ocho modalidades de ejercicio",
        "Las tareas comparten el mismo caso; no son ocho horas añadidas por "
        "separado. Se practican en la asignación indicativa de 3 h de seminario, "
        "8 h de investigación y lectura, 12 h de laboratorio y 8 h de aplicación "
        "por unidad. Los tiempos requieren aprobación académica.",
        *tasks,
        "## Rúbrica formativa y evidencia de logro",
        rubric_for_unit(unit),
        "## Preguntas mayéuticas, sin confundirlas con afirmaciones",
        "**Pregunta original consolidada (muestras):**\n"
        + render_list(original_prompts, "Sin pregunta original asignada a esta unidad "
                      "en la matriz; usar las de plantilla como práctica."),
        "**Serie de banco construida desde plantillas documentadas (muestras):**\n"
        + render_list(selected_bm),
        f"**Tesis propuestas por pregunta asignadas explícitamente a esta unidad: "
        f"{len(derived_here)}.**\n"
        + render_list(AP_sample, "No se registraron tesis AP asignadas de forma exclusiva."),
        "**Tesis transversales relacionadas sin asignación principal (muestras):**\n"
        + render_list(AP_cross, "Sin vínculos transversales adicionales."),
        "El banco completo conserva 543 preguntas originales y 2.395 preguntas "
        "derivadas mecánicamente de plantillas; 308 tesis AP forman un **anexo "
        "provisional**, distinto de los 331 conceptos del corpus de trabajo.",
        "## Lecturas, investigación y modalidad",
        "**Lecturas internas verificables:**\n" + render_list(sources),
        "**Lecturas complementarias por cotejar:** NIST CSF 2.0, NIST RMF y "
        "dominios CISM/CRISC según la unidad y las fuentes listadas por el "
        "Documento Maestro. El mapeo de este documento es una propuesta "
        f"temática: `{unit['alignment']}`. La fuente oficial, edición y pertinencia "
        "deben comprobarse al preparar cada clase; no se presume cobertura "
        "íntegra de examen o norma.",
        "**Recursos audiovisuales:** no se identificó un video específico, "
        "vigente y verificable por unidad en los documentos base. Existe un "
        + link_to(
            ROOT / "Biblioteca_CISO_Frontera" / "Consolidado_2026_MM_2026-11-11"
            / "03_programa_1200h" / "Videos_Observados_en_Fuentes.md",
            destination,
            "inventario complementario de enlaces observados",
        )
        + ", aún sin comprobación de contenido, disponibilidad, duración "
        "ni correspondencia con esta unidad. El equipo docente deberá "
        "seleccionarlos, comprobar derechos y documentar el vínculo antes "
        "de asignarlos.",
        "**Carga de diseño:** 31 h por unidad; 24 unidades más capstone "
        "integrador de 56 h = escenario de 800 h. No es acreditación.",
    ]
    return paragraphs(*result) + "\n"


def method_markdown(model):
    examples = [
        question for question in model["questions"].values()
        if question["direct_id"] in model["derived"]
    ][:3]
    demonstration = [
        f"- `{row['id']}`: {row['text']}\n"
        f"  - Enunciado `[P]` relacionado: "
        f"{model['derived'][row['direct_id']]['definition']}\n"
        f"  - Relación: `preensayo_directo={row['direct_id']}`. "
        "El enunciado no sustituye ni prueba la pregunta."
        for row in examples
    ]
    return paragraphs(
        "# Método mayéutico: preguntar, contrastar y formular hipótesis",
        "## Cuatro conjuntos que no se deben confundir",
        "| Capa | Registros | Significado |\n"
        "|---|---:|---|\n"
        "| Núcleo TheNextCISO GM-24 | 331 | 240 conceptos base, "
        "51 ampliaciones Atlas propuestas [P], 40 HC candidatos incluidos |\n"
        "| Preguntas originales consolidadas | 543 | 539 interrogativas y "
        "4 peticiones en imperativo; conservar el texto y su procedencia |\n"
        "| Tesis ampliadas desde preguntas | 308 | Identificadores `APC/APA/APN`; "
        "contienen tesis, tensión, desarrollo y producto de una fuente editorial; "
        "separadas del núcleo 331 |\n"
        "| Preguntas BM generadas por plantilla | 2.395 | 639 series × 3–5 "
        "tipos; textos construidos a partir de título y plantilla, "
        "no citas de personas |\n\n"
        "El corpus de pre-ensayos ampliado tiene **639 registros (331 + 308)**; "
        "sus tipos no elevan silenciosamente la línea base de 24 unidades. "
        "Los HC son candidatos incluidos por decisión del propietario del "
        "programa; las ampliaciones siguen siendo propuestas hasta aprobación. "
        "De las 543 formulaciones, 308 enlazan directamente con una tesis AP "
        "declarativa. Las otras 235 enlazan con 111 ideas base, 85 AMP y 39 HC: "
        "el vínculo permite debatir un enunciado ya existente, **no autoriza "
        "inventar una tesis adicional** ni presentar una pregunta como hecho.",
        "## Procedimiento de enseñanza",
        "1. Formular la pregunta original con su ID y ámbito sin convertir una "
        "interrogación en un hecho.\n"
        "2. Identificar decisión, interesado, evidencia disponible, condición, "
        "negación y alternativa que podría refutar una respuesta.\n"
        "3. Contrastar la tesis editorial AP, si existe, con la pregunta. "
        "Es una interpretación candidata, no la única respuesta correcta.\n"
        "4. Producir un expediente de decisión y una prueba de resultado; "
        "clasificar observación, hipótesis, recomendación y laguna.\n"
        "5. Revisar la respuesta ante un par y registrar qué evidencia la "
        "haría cambiar. Mantener el ID `PC/PA/PN` y el enlace AP o base.",
        "## Ejemplos trazables de doble lectura",
        render_list(demonstration),
        "## Ocho modalidades del banco",
        render_list([
            f"`{type_id}` — **{template['nombre']}**: {template['descripcion']} "
            f"Plantilla: {template['plantilla']}"
            for type_id, template in model["templates"].items()
        ]),
        "## Controles de fidelidad",
        "- Las cuatro formulaciones en imperativo no se etiquetan como preguntas "
        "interrogativas; conservan tipo de petición.\n"
        "- Siete preguntas originales no poseen `preensayo_331`, aunque sí "
        "un vínculo `preensayo_directo`; no se asigna un ID faltante por proximidad.\n"
        "- Siete tesis AP no especifican `especializa`; se conservan sus "
        "vínculos candidatos sin inventar unidad primaria.\n"
        "- Un enlace `ESPECIALIZA`, `FUNDAMENTA` u otro predicado de la fuente "
        "no se convierte automáticamente en una arista aprobada del Atlas.\n"
        "- Ninguna tesis propuesta acredita dominio adquirido ni eficacia de "
        "un control; la evaluación exige evidencia observada.",
    ) + "\n"


def program_markdown(model):
    rows = [
        f"| {link_to(unit_path(unit['id']), LIBRARY / '04_programa' / 'Programa_GM24_y_Integracion.md', unit['id'])} "
        f"| {table_cell(unit['title'])} | 3 | 8 | 12 | 8 | **31** | "
        f"`{unit['case']['cognitivo']}` |"
        for unit in model["units"].values()
    ]
    return paragraphs(
        "# Programa GM-24 y articulación con TheMetaCognitiveCISO",
        "**Estado:** escenario de diseño curricular **no acreditado**. "
        "El Documento Maestro de noviembre mantiene una aspiración de 800 h; "
        "no afirma que exista aprobación institucional de las 728 h fuera de "
        "las 24 clases de tres horas. Los 331 conceptos incluyen 51 propuestas "
        "[P] y 40 puentes candidatos; se enseñan con ese estado visible.",
        "## Modelo de aprendizaje",
        "1. **TheNextCISO:** Gobierno decide mandato, apetito y supervisión "
        "(G1.1–G6.2); Gestión diseña, opera y comprueba resultados "
        "(M1.1–M6.2). Cada una de las 24 unidades usa 10 conceptos base "
        "y 2–3 ampliaciones propuestas sin confundirlas con definiciones "
        "originales. Los HC conectan varias unidades.\n"
        "2. **TheMetaCognitiveCISO:** la caja cognitiva complementa el método "
        "con reflexión sobre el propio juicio, sesgos, funciones ejecutivas "
        "y comunicación; el cruce cognitivo por unidad es una propuesta "
        "pedagógica, no contenido base obligatorio de GM-24.\n"
        "3. **AI CISO Atlas:** territorios y dominios ayudan a situar y "
        "contrastar decisiones. Los mapeos son correspondencias temáticas; "
        "la evolución H contextual no es una escalera universal de madurez.\n"
        "4. **Método mayéutico:** mantener las preguntas originales y "
        "formular tesis AP refutables, trazadas a su pregunta; practicar "
        "comparación, decisión, prueba y defensa.",
        "## Distribución propuesta: 24 × 31 + 56 = 800 h",
        "| Unidad | Foco | Clase | Lectura e investigación | Taller/laboratorio | Aplicación | Total propuesto | Lente cognitiva propuesta |\n"
        "|---|---|---:|---:|---:|---:|---:|---|\n"
        + "\n".join(rows)
        + "\n| **Capstone** | Integración G↔M, Atlas y método | 0 | 8 | 16 | 32 | **56** | Juicio y revisión cruzada |\n"
        "| **Total** | **24 unidades + capstone** | **72** | **200** | **304** | **224** | **800** | No sumar programas externos |",
        "La categoría de capstone comprende **8 h de investigación, 16 h de "
        "laboratorio y 32 h de aplicación, evaluación y defensa**; las 56 h "
        "no se reparten entre las 24 unidades. La distribución por unidad "
        "es 3+8+12+8 = 31 h. Las sumas: 72+200+304+224 = 800 h.",
        "## Capstone integrador y evaluación",
        "En la organización ficticia Faro Futura S.A. se despliega un SOC con "
        "agentes sobre datos sensibles, identidades no humanas, proveedores "
        "y dependencias de continuidad. El participante construye un "
        "expediente que parte de G1.1 (mandato), pasa por G4.2 (límites "
        "de autonomía), M2.2/M3.1 (identidad y arquitectura), M4.1 "
        "(operación supervisada) y M5.1/M6.1 (crisis y recuperación), "
        "regresa a G5.2/G6.1 (aceptación y comunicación), y documenta "
        "un HC como **candidato** y una AMP como **tesis [P]**. Debe "
        "defender dos alternativas, refutar una hipótesis inicial y "
        "mostrar criterios para detener o revertir la automatización.",
        "El panel evalúa precisión de conceptos y frontera G/M (25%), "
        "procedencia/calidad de evidencia (25%), autoridad y decisión "
        "proporcional (25%), y prueba/transferencia/comunicación (25%). "
        "El umbral de aprobación es **una propuesta**, sujeto a validación "
        "académica, no una certificación.",
        "## Frontera con el programa cognitivo de 1.200 h",
        "La edición de la Biblioteca CISO de frontera ya contiene un programa "
        "independiente de 1.200 h. Sus horas **no se suman automáticamente** "
        "a las 800 h de diseño GM-24 ni se reclasifican como acreditadas. "
        "Un reconocimiento de aprendizajes o equivalencia futura exige "
        "comparar objetivos, carga real, evaluación y autoridad curricular. "
        "Consulte "
        + link_to(
            ROOT / "Biblioteca_CISO_Frontera" / "Consolidado_2026_MM_2026-11-11"
            / "03_programa_1200h" / "Programa_CISO_Frontera_1200h.md",
            LIBRARY / "04_programa" / "Programa_GM24_y_Integracion.md",
            "programa metacognitivo de 1.200 h",
        ) + ".",
        "## Bibliografía y audiovisuales",
        "Las lecturas base son el Documento Maestro GM-24, sus ocho lotes "
        "de ideas centrales, los 40 HC y la matriz editorial de 331. "
        "Las fuentes oficiales NIST CSF 2.0, RMF e ISACA constan en la "
        "bibliografía del Documento Maestro, pero deben cotejarse "
        "por versión y unidad antes de asignarlas. No existe en esta "
        "base un video verificado para cada unidad; el "
        + link_to(
            ROOT / "Biblioteca_CISO_Frontera" / "Consolidado_2026_MM_2026-11-11"
            / "03_programa_1200h" / "Videos_Observados_en_Fuentes.md",
            LIBRARY / "04_programa" / "Programa_GM24_y_Integracion.md",
            "inventario observado del programa cognitivo",
        )
        + " contiene candidatos, no contenidos, duraciones ni "
        "correspondencias GM-24 ya comprobados. Su selección y accesibilidad "
        "permanecen pendientes.",
    ) + "\n"


def index_markdown(model):
    counts = Counter(entry["type"] for entry in model["concepts"].values())
    destination = LIBRARY / "Indice_Biblioteca_GM24.md"
    rows = [
        f"| {link_to(unit_path(unit['id']), destination, unit['id'])} "
        f"| {table_cell(unit['title'])} | {unit['pillar']} | 10 | {len(unit['amp_ids'])} "
        f"| {len(unit['hc_ids'])} | {len(unit['ap_ids'])} |"
        for unit in model["units"].values()
    ]
    return paragraphs(
        "# TheNextCISO GM-24 — Biblioteca de conocimiento accionable",
        "**Edición de trabajo:** noviembre de 2026. **Corpus principal:** "
        "**331 entradas** = 240 ideas base en 24 unidades + 51 ampliaciones "
        "Atlas propuestas + 40 conceptos híbridos candidatos. "
        "No se afirma que 330 sea el total: las fuentes consolidadas "
        "cuentan 331. El corpus mayéutico agrega 308 tesis AP provisionales "
        "vinculadas a 543 preguntas; no redefine la cifra base.",
        "**Estado de fuentes:** los 240 textos base son ideas centrales "
        "editoriales, no ensayos finales; las 51 AMP nacen como títulos "
        "y su tesis en matriz está marcada `[P]`; los 40 HC se incluyen "
        "por decisión del propietario conservando estado candidato. "
        "La organización en 24 unidades procede de GM-24 y no se "
        "equivale automáticamente a los 24 dominios del Atlas.",
        "## Accesos principales",
        render_list([
            link_to(LIBRARY / "04_programa" / "Programa_GM24_y_Integracion.md", destination,
                    "Escenario de desarrollo de 800 h y articulación con TheMetaCognitiveCISO"),
            link_to(LIBRARY / "03_metodo_mayeutico" / "Metodo_Preguntas_y_Enunciados.md",
                    destination, "Método: 543 preguntas y 308 tesis derivadas"),
            link_to(LIBRARY / "03_metodo_mayeutico" / "Banco_Preguntas_543.md",
                    destination, "Banco de preguntas originales"),
            link_to(LIBRARY / "Mapa_GM24_331_y_Metodo.xlsx", destination,
                    "Excel: conceptos, puentes, ejercicios, preguntas y trazabilidad"),
            link_to(LIBRARY / "00_control" / "Catalogo_GM24_639.jsonl", destination,
                    "Corpus estructurado: 331 entradas + 308 tesis derivadas"),
            link_to(ROOT / "Curado02" / "00_control" / "Manifiesto_Curado02.json",
                    destination, "Manifiesto de copias curadas con SHA-256"),
            link_to(LIBRARY / "05_calidad" / "Control_Final_GM24.md",
                    destination, "Control de calidad y pendientes"),
            link_to(LIBRARY / "05_calidad" / "Auditoria_Independiente_GM24.md",
                    destination, "Auditoría independiente y condiciones de uso docente"),
        ]),
        "## Unidades y cobertura (12 Gobierno + 12 Gestión)",
        "| Unidad | Enfoque | Pilar | Base | AMP [P] | HC asociados, no exclusivos | AP asignados |\n"
        "|---|---|---|---:|---:|---:|---:|\n"
        + "\n".join(rows)
        + f"\n| **Totales de clase** | **24 unidades** | — | **240** | **51** "
        f"| **40 únicos**, multiunidad | **{sum(len(u['ap_ids']) for u in model['units'].values())}** de 308 con asignación primaria |",
        "Las referencias a HC son **múltiples por unidad**; sumar la columna "
        "HC produciría doble conteo. Las AP transversales o sin unidad "
        "principal se encuentran en "
        + link_to(
            LIBRARY / "03_metodo_mayeutico" / "Indice_Tesis_308.md",
            destination,
            "el anexo de tesis mayéuticas",
        )
        + " y en el Excel maestro.",
        "## Criterio de selección y versiones",
        "Se criban los 1.705 archivos inventariados en la raíz y se copian "
        "31 archivos únicos desde 32 rutas seleccionadas a `Curado02`. "
        "Los informes CSU de contenido comercial no son fuentes "
        "curriculares. Dos versiones idénticas del documento HC se "
        "conservan como un solo contenido, con ambos orígenes en el "
        "manifiesto. El currículo `202506 v3` ya documentaba 24 "
        "unidades y 240 conceptos, aunque conserva secciones de una "
        "propuesta de 32 unidades. Es un antecedente para comprender "
        "la evolución; noviembre de 2026 integra 51 propuestas Atlas "
        "y 40 puentes candidatos sin sustituir el núcleo de 2025.",
        "## Relación con AI CISO Atlas y TheMetaCognitiveCISO",
        "El Atlas aporta localización y preguntas; TheNextCISO desarrolla "
        "gobierno y gestión; TheMetaCognitiveCISO aporta juicio, "
        "autorregulación, prácticas de decisión y control de sesgos. "
        "Se distinguen el corpus, los vínculos editoriales y las "
        "propuestas pedagógicas, con fuentes y límites por ficha.",
    ) + "\n"


def questions_markdown(model):
    destination = LIBRARY / "03_metodo_mayeutico" / "Banco_Preguntas_543.md"
    rows = [
        f"| `{row['id']}` | {table_cell(row['text'])} "
        f"| `{row['direct_id']}` | `{row['gm24_id'] or 'sin vínculo 331'}` "
        f"| {row['form']} |"
        for row in model["questions"].values()
    ]
    return paragraphs(
        "# Banco de 543 preguntas consolidadas",
        "Se conservan los enunciados originales sin convertirlos en hechos: "
        "539 interrogativas y cuatro peticiones en imperativo. "
        "`preensayo_directo` existe en las 543 filas; siete no "
        "tienen `preensayo_331` explícito. La tesis AP relacionada "
        "se consulta por el ID directo, cuando existe, y nunca "
        "se atribuye como cita textual de la pregunta.",
        "Fuente: "
        + link_to(model["curated_question_sources"]["questions"], destination,
                  "preguntas_consolidadas.json") + ", `preguntas[id=...]`.",
        "| ID | Texto original | Pre-ensayo directo | Vínculo con núcleo 331 | Tipo de formulación |\n"
        "|---|---|---|---|---|\n" + "\n".join(rows),
    ) + "\n"


def derived_index_markdown(model):
    destination = LIBRARY / "03_metodo_mayeutico" / "Indice_Tesis_308.md"
    groups = {
        "APC": "Ampliaciones derivadas de preguntas al CISO",
        "APA": "Ampliaciones derivadas del marco",
        "APN": "Ampliaciones derivadas de preguntas nuevas",
    }
    blocks = [
        "# Índice de las 308 tesis derivadas del método mayéutico",
        "No son 308 conceptos originales adicionales de GM-24. Su tesis, "
        "tensión, desarrollo, error y producto proceden del corpus mayéutico "
        "de noviembre de 2026; cada pregunta original se conserva por ID. "
        "La asignación principal se toma solo de `especializa` cuando "
        "esta apunta a un concepto base o AMP con unidad. Un HC puede "
        "relacionar varias unidades sin pertenencia exclusiva.",
    ]
    for prefix, label in groups.items():
        subset = [row for row in model["derived"].values() if row["id"].startswith(prefix)]
        blocks.extend([
            f"## {label} ({len(subset)})",
            render_list([
                f"{link_to(concept_path(row), destination, row['id'] + ' — ' + row['title'])} "
                f"← `{row['origin_question']}`; "
                f"{'unidad '+row['unit'] if row['unit'] else 'transversal/sin unidad primaria'}."
                for row in subset
            ]),
        ])
    return paragraphs(*blocks) + "\n"


def source_contract_markdown(model):
    m = model["manifest"]
    docs = [
        f"- `{entry['curated_path']}` ← `{entry['canonical_source']}`, "
        f"`sha256={entry['sha256']}`. {entry['purpose']}."
        for entry in m["items"]
        if entry["curated_path"].startswith("Curado02/01_noviembre_2026")
    ]
    return paragraphs(
        "# Contrato de análisis y procedencia GM-24",
        "**Pregunta primaria:** ¿cómo formar y evaluar decisiones "
        "del líder de ciberseguridad en 24 unidades de gobierno y "
        "gestión, preservando la frontera entre 240 bases, 51 "
        "ampliaciones propuestas, 40 puentes candidatos y "
        "308 tesis generadas desde preguntas?",
        "## Perfil de fuente",
        "Textos Markdown y JSON en español con terminología inglesa "
        "(formación/estrategia/técnica; alta densidad conceptual) "
        "y documentos Office de referencia en OneDrive. Los "
        "Markdown y JSON copiados son legibles y verificables por "
        "sección, ID y localizador; los Office alojados en OneDrive "
        "se consultaron mediante WorkIQ Ask, sin descomprimirlos. "
        "El Excel sin sufijo `Matrices_Curriculares.xlsx` devolvió "
        "`Result is protected`: se conserva la copia para trazabilidad, "
        "pero su contenido no se utilizó para inferir diferencias.",
        "## Afirmaciones de alcance (con modalidades)",
        "- **CLM-001, explícita:** la estructura GM-24 tiene 24 unidades "
        "en 12 ejes ya en `The Next CISO - Curricula 202506 v3.docx` "
        "(Partes 1 y 2 y tablas resumen) y en el Documento Maestro "
        "de noviembre §2. El v3 conserva además restos de un diseño "
        "previo de 32 unidades; no se los añade al programa.\n"
        "- **CLM-002, explícita/editorial:** existen 240 conceptos "
        "base K01–K10 en cada unidad y ocho lotes de idea central. "
        "Fuentes: Documento Maestro §3, ocho lotes, matriz "
        "`01Unidades24!J2:J25`.\n"
        "- **CLM-003, propuesta:** 51 AMP cuyo título está en "
        "Documento Maestro §3; sus ideas centrales son propuestas "
        "[P] de `06Ensayos!I285:I335`, con fuente por celda.\n"
        "- **CLM-004, candidato incluido:** 40 HC-001–HC-040 "
        "son puentes transversales y no aumentan el número de "
        "unidades. Fuente: `40 conceptos híbridos`, §1–§6.\n"
        "- **CLM-005, edición mayéutica:** 543 preguntas originales, "
        "308 tesis AP, 639 pre-ensayos y 2.395 posiciones BM "
        "templadas. Fuentes: JSON del paquete de preguntas y "
        "su LEEME.\n"
        "- **CLM-006, escenario y no acreditación:** 24×3 h "
        "de clases y aspiración a 800 h de aprendizaje integral. "
        "Fuente: Documento Maestro §1 y §7; carga adicional "
        "propuesta pendiente de aprobación institucional.",
        "## Contradicciones, ambigüedades y exclusiones",
        "- **CON-001:** se mencionaron 330 conceptos, pero "
        "la matriz vigente registra 331 (=240+51+40). "
        "El usuario confirmó la inclusión de los tres grupos; "
        "no se eliminó una entrada para ajustar una cifra.\n"
        "- **CON-002:** el currículo `202506 v3` ya expresa 24 unidades "
        "y 240 conceptos, **a la vez que conserva apartados de 32 "
        "unidades**. Se da precedencia a sus tablas revisadas de 24 "
        "y al documento integrado de noviembre; no se fecha en 2026 "
        "la primera aparición de GM-24.\n"
        "- **AMB-001:** que una tesis AP responda a una pregunta "
        "es una interpretación editorial, no un hecho constatado.\n"
        "- **GAP-001:** el libro protegido sin sufijo no permite "
        "comparación fila a fila con `(2).xlsx`; se usa la matriz "
        "legible sin declarar que el sufijo indica autoridad.\n"
        "- **GAP-002:** el Excel histórico `Estructura Academica color - "
        "20250604.xlsx` no fue localizable por WorkIQ; se copió sin "
        "interpretar sus celdas.\n"
        "- **GAP-003:** las 51 ideas AMP y 40 HC carecen aquí "
        "de constancia de aprobación formal; el programa 800 h "
        "también es escenario de diseño.\n"
        "- **EXCL-001:** informes CSU comerciales y salidas "
        "previas de otra biblioteca no se incorporan como "
        "definiciones GM-24; el catálogo cognitivo se cita "
        "como complemento. No se volvió a convertir el "
        "archivo histórico completo de 1,8 GB.",
        "## Relación estructural y prueba MECE",
        "La partición **base / AMP / HC** es exclusiva por ID para "
        "el corpus de 331 y exhaustiva dentro de ese alcance; "
        "AP es una cuarta capa separada. En cambio, la estructura "
        "de **unidades y HC no es MECE**: un puente puede conectar "
        "varias unidades; no se inventó un propietario exclusivo. "
        "Una arista curricular no prueba causalidad, dependencia "
        "ni aprobación ontológica.",
        "## Fuentes 2026 de mayor autoridad en este paquete",
        "\n".join(docs),
        "## Cambios de contenido",
        "No se modificaron las definiciones ni los documentos "
        "originales. El desarrollo nuevo está señalado como "
        "diseño instruccional o interpretación derivada; "
        "el registro AMP conserva la tesis [P] y su celda "
        "exacta. Las preguntas originales se conservan "
        "separadas de las tesis.",
    ) + "\n"


def quality_markdown(model):
    base = sum(item["type"] == "base" for item in model["concepts"].values())
    amp = sum(item["type"] == "atlas" for item in model["concepts"].values())
    hc = sum(item["type"] == "hybrid" for item in model["concepts"].values())
    assigned = sum(bool(item["unit"]) for item in model["derived"].values())
    unassigned = sum(not item["specializes"] for item in model["derived"].values())
    return paragraphs(
        "# Control de calidad de la biblioteca GM-24",
        "## Medidas comprobadas en el generador",
        "| Control | Resultado |\n|---|---:|\n"
        f"| Archivos de origen cribados | {model['manifest']['root_screened_files']} |\n"
        f"| Copias únicas en Curado02 | {model['manifest']['unique_copies']} |\n"
        f"| Unidades | {len(model['units'])} |\n"
        f"| Ideas base con texto fuente, ID y cita | {base} |\n"
        f"| Ampliaciones Atlas con propuesta [P] y celda | {amp} |\n"
        f"| Híbridos candidatos con cuatro vínculos mínimo | {hc} |\n"
        f"| Total corpus principal | {len(model['concepts'])} |\n"
        f"| Tesis AP derivadas y trazadas a pregunta | {len(model['derived'])} |\n"
        f"| AP con unidad principal explícita | {assigned} |\n"
        f"| AP sin `especializa` explícito | {unassigned} |\n"
        f"| Preguntas originales conservadas | {len(model['questions'])} |\n"
        f"| Preguntas BM generadas desde plantilla | {len(model['bank'])} |\n"
        f"| Ejercicios de unidad (8 × 24) | {8 * len(model['units'])} |\n"
        "| Horas de diseño (24 × 31 + 56) | 800, no acreditadas |",
        "## Reservas que limitan la conclusión",
        "1. Los textos base son **ideas centrales editoriales**, "
        "no ensayos aprobados ni resultados empíricos; los "
        "HC son candidatos y las AMP son tesis [P].\n"
        "2. La matriz curricular sin sufijo estaba protegida; "
        "se usó su variante legible `(2)`, sin asegurar "
        "equivalencia de contenidos ni fecha interna posterior.\n"
        "3. Los enlaces entre unidades, Atlas y 72 capacidades "
        "cognitivas son propuestas de enseñanza, no el "
        "grafo aprobado ni homologaciones de marcos.\n"
        "4. No se inventaron bibliografía individual ni videos "
        "para suplir vacíos documentales.\n"
        "5. No se analizaron de nuevo los 1.705 archivos completos: "
        "se hizo inventario y cribado, se estudiaron las "
        "fuentes GM-24 pertinentes y se aprovecharon las "
        "curaciones históricas. No se promete cobertura "
        "conceptual de todo archivo no seleccionado.\n"
        "6. Una pregunta original no acredita la tesis asociada; "
        "hay cuatro peticiones, siete preguntas sin "
        "`preensayo_331` y siete AP sin unidad primaria.",
        "## Validación adicional recomendada al responsable académico",
        "- Revisar 51 AMP y 40 HC para aprobar, rechazar o "
        "editar; registrar un ChangeSet por modificación.\n"
        "- Revisar con expertos escenarios, 192 consignas, "
        "rúbricas, carga horaria, materiales audiovisuales "
        "y bibliografía oficial por edición.\n"
        "- Conciliar por WorkIQ el Excel protegido cuando "
        "exista una copia accesible; no extraerlo desde "
        "paquetes Office locales para eludir derechos.\n"
        "- Probar los casos con participantes antes de "
        "atribuirles eficacia o acreditación.",
    ) + "\n"

# -*- coding: utf-8 -*-
"""Documentos GM-24: texto V4 íntegro (convertido con pandoc desde los DOCX V4) + bloques ◆ por unidad + Anexo PO-GAC al Documento Maestro."""
import os, re, subprocess
import data as D
from gen_md import table, write, PA_BY_UNIT, LENTE_BY_UNIT, H_PA, H_LENTE
ROOT = os.path.join(os.path.dirname(__file__), ".."); OUT = os.path.join(ROOT, "GM24_V6"); os.makedirs(OUT, exist_ok=True)
V4_DIR = os.environ.get("V4_DIR", "/mnt/data")
V4_FILES = {"base": "Formación CISO_ Gobierno y Gestión_ 4.docx", "act": "Formación CISO_ Gobierno y Gestión (Versión Actualizada) 4.docx", "c24": "Formación CISO_ Gobierno y Gestión (Estructura 24 Clases) 4.docx"}
MAP24 = {"G1":"G1.1","G2":"G1.1","G3":"G1.2","G4":"G1.2","G5":"G2.1","G6":"G2.2","G7":"G3.1","G8":"G4.1","G9":"G4.2","G10":"G5.1","G11":"G5.2","G12":"G3.2","G13":"G6.1","G14":"G6.1","G15":"G6.2","G16":"G6.2",
         "M1":"M1.1","M2":"M1.2","M3":"M2.1","M4":"M2.2","M5":"M3.1","M6":"M3.2","M7":"M4.1","M8":"M4.2","M9":"M5.1","M10":"M5.2","M11":"M6.1","M12":"M6.2","M13":"M6.2","M14":"M1.1","M15":"M1.2","M16":"M6.1"}
FRONT = f"""> **Trazabilidad de versiones.** V4 (abr-2025 / 4-nov-2026): texto original íntegro. **V5**: eje transversal PO-GAC (67 PA). **V6 ({D.FECHA})**: base 331 pre-ensayos; 42 PA con pre-ensayo; lente PO-GAC sobre 91 conceptos; tres rutas de construcción. Los bloques marcados **◆ V5/V6** se agregan sin alterar el contenido V4; `****` marca integraciones previas del propio V4."""
INTRO_BASE = "Este documento conserva íntegra la Propuesta de Estructura Académica V4 (32 unidades) y agrega, al final, los bloques ◆ V6 con la lectura PO-GAC por unidad de 24 (mapa de 32 → 24)."
INTRO_ACT = "Este documento conserva íntegra la Versión Actualizada V4 y agrega los bloques ◆ V6 por unidad."
V6_32 = {}

def md_from_docx(key):
    cached = os.path.join(os.path.dirname(__file__), "fuentes_V4", key + ".md")
    if os.path.exists(cached): return open(cached, encoding="utf-8").read()
    src = os.path.join(V4_DIR, V4_FILES[key])
    if not os.path.exists(src): return f"\n> **AVISO:** no se encontró `{V4_FILES[key]}` en `{V4_DIR}`; el texto V4 no pudo incluirse. Colocar los DOCX V4 y regenerar.\n"
    return subprocess.run(["pandoc", src, "-t", "gfm", "--wrap=none"], capture_output=True, text=True).stdout

def bloque_v6(u24):
    pas = PA_BY_UNIT.get(u24, []); lens = LENTE_BY_UNIT.get(u24, [])
    return (f"**◆ V5.** Eje PO-GAC: la unidad recibe conceptos del sub-plan (Product Owner de control y gerente de agentes). "
            f"**◆ V6.** Base 331 (K/AMP/HC) · {len(pas)} concepto(s) PA ({sum(p[10] for p in pas)} h): " + ("; ".join(f"**{p[0]}** {p[2]}" for p in pas) if pas else "—") +
            f". Lente PO-GAC sobre {len(lens)} concepto(s) existente(s) ({sum(l[2] for l in lens)} h): " + (", ".join(l[0] for l in lens) if lens else "—") + ".")

def seccion_unidades_24(): return "\n".join(f"\n### ◆ {u['id']} — {u['title']}\n\n{bloque_v6(u['id'])}\n" for u in D.UNITS)
def seccion_unidades_32(): return "\n".join(f"\n### ◆ {u32} → {u24} — {D.UNIT[u24]['title']}\n\n{bloque_v6(u24)} {V6_32.get(u32,'')}\n" for u32, u24 in MAP24.items())

def doc_32(fname, title, intro, strip=False):
    v4 = md_from_docx("act" if "Actualizada" in fname else "base")
    write(os.path.join(OUT, fname), f"# {title}\n\n{FRONT}\n\n{intro}\n\n---\n\n{v4}\n\n---\n\n## Anexo ◆ V5/V6/V7 — Lectura PO-GAC por unidad (mapa 32 → 24)\n{seccion_unidades_32()}")

def doc_24():
    v4 = md_from_docx("c24")
    write(os.path.join(OUT, f"Formación CISO_ Gobierno y Gestión (Estructura 24 Clases) {D.VERSION.replace('V','').replace('.0','')}.md"), f"# Gobierno y Gestión de la Ciberseguridad - The Next CISO: Propuesta de Estructura Académica (24 Clases / 12 Ejes) — {D.VERSION}\n\n{FRONT}\n\n---\n\n{v4}\n\n---\n\n## Anexo ◆ V5/V6/V7 — Lectura PO-GAC por unidad\n{seccion_unidades_24()}")

def anexo_maestro():
    rows = [(u["id"], u["title"], len(PA_BY_UNIT.get(u["id"], [])), sum(p[10] for p in PA_BY_UNIT.get(u["id"], [])), len(LENTE_BY_UNIT.get(u["id"], [])), sum(l[2] for l in LENTE_BY_UNIT.get(u["id"], []))) for u in D.UNITS]
    write(os.path.join(OUT, f"TheNextCISO_GM-24_Documento_Maestro_Anexo_PO-GAC_{D.VERSION.replace('.0','')}.md"), f"""# TheNextCISO GM-24 — Documento Maestro · Anexo PO-GAC ({D.VERSION})

{FRONT}

## 1. Objeto
Anexo al Documento Maestro (331 pre-ensayos) que incorpora el sub-plan PO-GAC sin modificar los conceptos existentes: {len(D.PA)} conceptos PA ({H_PA} h), lente sobre {len(D.LENTE)} conceptos ({H_LENTE} h), {len(D.COMPETENCIAS)} competencias, {len(D.TAREAS)} tareas del modelo operativo, {len(D.AGENTES)} agentes, {len(D.CONTROLES)} controles AGC, {len(D.KPIS)} KPIs.

## 2. Distribución por unidad
{table(["Unidad","Título","PA (n)","PA (h)","Lente (n)","Lente (h)"], rows)}

## 3. Conceptos PA por unidad
{table(["ID","Unidad","Concepto","Definición","h","Competencias"], [(p[0], p[1], p[2], p[3], p[10], ", ".join(p[11])) for p in D.PA])}

## 4. Lente PO-GAC
{table(["ID","Unidad","Lectura PO-GAC","Instrumento","h"], [(l[0], l[1], l[3], l[4], l[2]) for l in D.LENTE])}

## 5. Conciliación V5 → V6
{table(["PA V5","Tratamiento V6"], D.RETIRADOS)}
""")

if __name__ == "__main__":
    doc_32(f"Formación CISO_ Gobierno y Gestión_ {D.VERSION.replace('V','').replace('.0','')}.md", f"Gobierno y Gestión de la Ciberseguridad - The Next CISO: Propuesta de Estructura Académica — {D.VERSION}", INTRO_BASE, strip=True)
    doc_32(f"Formación CISO_ Gobierno y Gestión (Versión Actualizada) {D.VERSION.replace('V','').replace('.0','')}.md", f"Gobierno y Gestión de la Ciberseguridad - The Next CISO: Propuesta de Estructura Académica (Versión Actualizada) — {D.VERSION}", INTRO_ACT, strip=False)
    doc_24(); anexo_maestro(); print("DONE GM-24 docs")

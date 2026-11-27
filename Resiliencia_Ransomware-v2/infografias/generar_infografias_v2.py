"""
Generador reproducible de la serie de 8 infografias para Resiliencia_Ransomware-v2.
Produce SVG vectoriales nativos (1920x1200), PNG 4K Retina (3840x2400),
JPG de alta calidad (3840x2400) y galeria HTML portable sin rutas locales fijas.
"""

import argparse
import html
import pathlib
import shutil
from PIL import Image
from playwright.sync_api import sync_playwright

OUT_DIR = pathlib.Path(__file__).resolve().parent
SVG_DIR = OUT_DIR / "svg"
PNG_DIR = OUT_DIR / "png"
JPG_DIR = OUT_DIR / "jpg"

W, H = 1920, 1200
FONT = "Segoe UI, Inter, -apple-system, Arial, sans-serif"

TRUNCATION_WARNINGS = []


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def wrap_text(text: str, max_px: float, font_size: float, bold: bool = False, max_lines: int = 10) -> list[str]:
    char_w = font_size * (0.58 if bold else 0.53)
    max_chars = max(8, int(max_px / char_w))
    words = str(text).split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for w in words[1:]:
        if len(cur) + 1 + len(w) <= max_chars:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    if len(lines) > max_lines:
        TRUNCATION_WARNINGS.append((text[:60], len(lines), max_lines, max_px, font_size))
        kept = lines[:max_lines]
        if len(kept[-1]) > max_chars - 2:
            kept[-1] = kept[-1][: max_chars - 2].rstrip() + "…"
        else:
            kept[-1] = kept[-1].rstrip() + "…"
        return kept
    return lines


def svg_text_block(
    x: float,
    y: float,
    text: str,
    max_px: float,
    font_size: float = 13,
    fill: str = "#1E293B",
    bold: bool = False,
    line_height: float = 1.28,
    max_lines: int = 6,
    anchor: str = "start",
) -> str:
    lines = wrap_text(text, max_px, font_size, bold=bold, max_lines=max_lines)
    weight = "700" if bold else "400"
    out = [f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{font_size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">']
    for idx, ln in enumerate(lines):
        dy = "0" if idx == 0 else f"{font_size * line_height:.1f}"
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def badge(x: float, y: float, w: float, h: float, label: str, kind: str = "OK", font_size: float = 11.5) -> str:
    styles = {
        "OK": ("#DCFCE7", "#16A34A", "#14532D"),
        "GATE": ("#DBEAFE", "#2563EB", "#1E3A8A"),
        "WARN": ("#FEF9C3", "#CA8A04", "#713F12"),
        "ALERT": ("#FFEDD5", "#EA580C", "#7C2D12"),
        "CRIT": ("#FEE2E2", "#DC2626", "#7F1D1D"),
        "INFO": ("#E0F2FE", "#0284C7", "#0C4A6E"),
        "PURP": ("#EDE9FE", "#7C3AED", "#4C1D95"),
        "NEUTRAL": ("#F1F5F9", "#94A3B8", "#334155"),
    }
    bg, stroke, fg = styles.get(kind, styles["NEUTRAL"])
    dash = ' stroke-dasharray="4,2"' if kind in ("CRIT", "ALERT") else ""
    ty = y + h * 0.68
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2:.1f}" fill="{bg}" stroke="{stroke}" stroke-width="1.4"{dash}/>'
        f'<text x="{x + w/2:.1f}" y="{ty:.1f}" font-family="{FONT}" font-size="{font_size}" font-weight="700" fill="{fg}" text-anchor="middle">{esc(label)}</text>'
    )


def card(x: float, y: float, w: float, h: float, fill: str = "#FFFFFF", stroke: str = "#CBD5E1", rx: float = 12, shadow: bool = True, stroke_w: float = 1.5) -> str:
    flt = ' filter="url(#cardShadow)"' if shadow else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_w}"{flt}/>'


def arrow_h(x1: float, y: float, x2: float, color: str = "#0284C7") -> str:
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2-6}" y2="{y}" stroke="{color}" stroke-width="2.4"/>'
        f'<polygon points="{x2},{y} {x2-9},{y-5.5} {x2-9},{y+5.5}" fill="{color}"/>'
    )


def base_shell(piece_num: int, title: str, subtitle: str, archetype: str, scope_tag: str, body_svg: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <linearGradient id="hdrGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#091E3A"/>
      <stop offset="60%" stop-color="#0F2C59"/>
      <stop offset="100%" stop-color="#154360"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0284C7"/>
      <stop offset="50%" stop-color="#0EA5E9"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <rect x="0" y="0" width="{W}" height="{H}" fill="#F1F5F9"/>

  <!-- Header Banner -->
  <rect x="0" y="0" width="{W}" height="118" fill="url(#hdrGrad)"/>
  <rect x="0" y="118" width="{W}" height="4" fill="url(#accentGrad)"/>

  <rect x="48" y="16" width="356" height="24" rx="12" fill="#1E3A5F" stroke="#38BDF8" stroke-width="1"/>
  <text x="226" y="32.5" font-family="{FONT}" font-size="11.5" font-weight="700" fill="#7DD3FC" text-anchor="middle">KIT RESILIENCIA RANSOMWARE v2.0 · INFOGRAFÍA {piece_num:02d} DE 08</text>

  <text x="48" y="70" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFFFFF">{esc(title)}</text>
  <text x="48" y="99" font-family="{FONT}" font-size="14" font-weight="400" fill="#BAE6FD">{esc(subtitle)}</text>

  <rect x="1456" y="16" width="416" height="86" rx="10" fill="#0B2240" stroke="#334155" stroke-width="1.2"/>
  <text x="1474" y="38" font-family="{FONT}" font-size="11.5" font-weight="700" fill="#38BDF8">EDICIÓN CANÓNICA v2.0 (12 NOVIEMBRE 2026)</text>
  <text x="1474" y="59" font-family="{FONT}" font-size="12" font-weight="600" fill="#E2E8F0">Arquetipo: {esc(archetype)}</text>
  <text x="1474" y="80" font-family="{FONT}" font-size="11.5" font-weight="400" fill="#94A3B8">{esc(scope_tag)}</text>

  <!-- Main Content -->
  {body_svg}

  <!-- Footer Semiotic Bar -->
  <rect x="0" y="1144" width="{W}" height="56" fill="#E2E8F0"/>
  <line x1="0" y1="1144" x2="{W}" y2="1144" stroke="#CBD5E1" stroke-width="1.5"/>

  {badge(48, 1158, 168, 26, "[VERIFICADO / BASE]", "OK", 11)}
  {badge(228, 1158, 174, 26, "[DECISIÓN / GATE DD]", "GATE", 11)}
  {badge(414, 1158, 184, 26, "[CONDICIÓN / PARCIAL]", "WARN", 11)}
  {badge(610, 1158, 198, 26, "[LÍMITE / RIESGO CRÍTICO]", "CRIT", 11)}

  <text x="1872" y="1176" font-family="{FONT}" font-size="12" font-weight="600" fill="#334155" text-anchor="end">Seguridad humana prevalece · Ningún artefacto autoriza cambios por sí solo · Fuente: PKG-RANSOM v2.0 (Guías 01–15)</text>
</svg>'''


# ==============================================================================
# RR-01: MAPA MAESTRO DEL CICLO OPERATIVO, 3 OLAS Y 7 FASES CISO 365 (F0-F6)
# ==============================================================================
def build_rr01() -> str:
    parts = []

    # Top Card: 4 Operational Macro-Phases + 3 Execution Waves
    parts.append(card(48, 136, 1824, 236))
    parts.append(f'<text x="72" y="164" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">CICLO OPERATIVO EN 4 MACRO-FASES Y PRIORIDAD DE IMPLANTACIÓN EN 3 OLAS (SIN POSTERGAR COPIAS NI PRIVILEGIOS [MS-01])</text>')

    macro = [
        ("FASE I · PREPARAR Y EVALUAR", "Guías 01–03 · Libro 01", "#EFF6FF", "#2563EB",
         "Mandato escrito, canales fuera de banda, BIA con RTO/RPO firmados, línea base CT-01..21 y plan de brechas con dueño."),
        ("FASE II · DETECTAR Y CONTENER", "Guías 04–05, 10 · Libro 02", "#FEFCE8", "#CA8A04",
         "Vigilancia viva DE-01..13, triage UTC, activación CI y ejecución acotada PB-01..07 (F3) verificando efecto real."),
        ("FASE III · PRESERVAR Y RECUPERAR", "Guías 06–08 · Libro 02", "#F0FDF4", "#16A34A",
         "Custodia SHA-256 y holds, modo contingencia, restauración limpia <= RTO/RPO aceptada por negocio y avisos aprobados."),
        ("FASE IV · ENSAYAR Y SOSTENER", "Guías 09, 13–15 · Libro 03", "#EDE9FE", "#7C3AED",
         "Ensayos anuales E1–E3 sin pistas, métricas con denominador, operación en 12 capas Full MS y rutas Ninja titular+suplente."),
    ]
    mw = 423
    mgap = 28
    for i, (mh, msub, mbg, mst, mdesc) in enumerate(macro):
        mx = 72 + i * (mw + mgap)
        parts.append(f'<rect x="{mx}" y="176" width="{mw}" height="128" rx="10" fill="{mbg}" stroke="{mst}" stroke-width="1.6"/>')
        parts.append(f'<text x="{mx+14}" y="198" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#0F172A">{esc(mh)}</text>')
        parts.append(badge(mx + 14, 206, 162, 20, msub, "INFO", 10.2))
        parts.append(svg_text_block(mx + 14, 243, mdesc, mw - 28, 11.8, "#1E293B", False, 1.25, 3))
        if i < 3:
            parts.append(arrow_h(mx + mw + 4, 240, mx + mw + mgap - 4, "#0F2C59"))

    waves = [
        ("OLA 1 · Protección Inmediata (No SLA)", "Autoridad + BIA + aislar copias existentes + acceso emergencia + canal fuera de banda.", "OK"),
        ("OLA 2 · Reducción de Alcance", "Robustecer respaldos/identidad, cubrir EDR y logs, segmentar y ensayar revocación.", "GATE"),
        ("OLA 3 · Resistencia Continua", "Reducir superficie externa, integrar datos/terceros/IA y medir ejercicios anuales E1–E3.", "PURP"),
    ]
    for i, (wh, wd, wk) in enumerate(waves):
        wx = 72 + i * (580 + 18)
        parts.append(f'<rect x="{wx}" y="314" width="580" height="46" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(badge(wx + 10, 324, 224, 24, wh, wk, 10.5))
        parts.append(svg_text_block(wx + 244, 333, wd, 326, 11.2, "#334155", False, 1.2, 2))

    # Bottom Card: 7 Phases in First 365 Days (PKG-CISO365)
    parts.append(card(48, 386, 1824, 742))
    parts.append(f'<text x="72" y="414" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">SECUENCIA EN LOS PRIMEROS 365 DÍAS DEL CISO (PKG-CISO365: FASES F0 A F6, HITOS H0–H365 Y CONTROLES CT-*)</text>')

    cols = [
        ("Fase y Ventana Temporal", 216),
        ("Hito de Salida", 224),
        ("Qué Debe Lograr el CISO en Resiliencia Ransomware", 534),
        ("Controles CT-* Activados / Revisados", 376),
        ("Trampa Habitual a Evitar", 418),
    ]
    cx = 68
    hy = 426
    for ch_t, cw_t in cols:
        parts.append(f'<rect x="{cx}" y="{hy}" width="{cw_t}" height="38" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + cw_t/2:.1f}" y="{hy+24}" font-family="{FONT}" font-size="12.8" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(ch_t)}</text>')
        cx += cw_t + 4

    fases = [
        ("F0 · Antes del Día 1 (D-30 a D0)", "H0 · Mandato acordado (Día 0)",
         "Llegar con mandato explícito, derechos de decisión iniciales, hipótesis de trabajo y agenda de escucha preparada; no con un plan cerrado.",
         "Seguimiento transversal (ACT-002 mandato, ACT-009 diario R01)",
         "Aceptar el cargo con una solución decidida sin acordar alcance, línea de reporte ni acceso al Directorio."),
        ("F1 · Recepción (Días 1–30)", "H30 · Acta de recepción (Día 30)",
         "Saber qué se recibe (personas, riesgos abiertos, llaves), estabilizar copias e identidad urgente y verificar preparación mínima IR (ACT-011 / ACT-023).",
         "CT-01 · CT-02 · CT-03 · CT-04 · CT-08 · CT-13 · CT-18",
         "Confundir escucha con pasividad o intervenir sin registrar herencia recibida vs. gestión propia."),
        ("F2 · Diagnóstico (Días 31–60)", "H60 · Diagnóstico base (Día 60)",
         "Construir línea base objetiva y defendible con denominadores reales: BIA, escenarios de ataque, activos críticos, obligaciones, telemetría y terceros.",
         "CT-01 · CT-05..07 · CT-09..12 · CT-14..17 · CT-19..21",
         "El diagnóstico eterno: medir con todos los marcos sin decidir prioridades, o emitir opiniones sin evidencia."),
        ("F3 · Plan 100 Días (Días 61–100)", "H100 · Informe 100 días (Día 100)",
         "Convertir el diagnóstico en prioridades acotadas con propietario, mostrar victorias tempranas en copias/privilegios/IR y pedir apoyos explícitos.",
         "CT-02 · CT-04 · CT-13 · CT-16 · CT-20",
         "Prometer un plan ambicioso sin recursos aprobados, sin dueños de negocio y sin decisiones de la dirección."),
        ("F4 · Gobierno (Días 101–180)", "H180 · Gobierno operando (Día 180)",
         "Instalar comité de ciberriesgo (R12), apetito, políticas, dueños de riesgo, excepciones con vencimiento (R09) y operación regular de controles.",
         "CT-03..14 · CT-17 · CT-18 · CT-19 · CT-21",
         "Gobierno decorativo: comités puramente informativos, apetito sin umbrales y métricas sin meta ni uso."),
        ("F5 · Pruebas (Días 181–270)", "H270 · Capacidades probadas (Día 270)",
         "Someter a prueba real lo afirmado: ejercicio ejecutivo E1, restauración extremo a extremo E2, aislamiento/custodia E3 y modo sin IA (K56).",
         "CT-01 · CT-02 · CT-03 · CT-09 · CT-15..18 · CT-20 · CT-21",
         "Confundir actividad o licencias con efectividad: controles configurados que nunca se ensayaron."),
        ("F6 · Cierre Anual (Días 271–365)", "H365 · Rendición anual (Día 365)",
         "Rendir cuentas al Directorio (Q1–Q6) con evidencia medida, recalibrar riesgo/madurez y comprometer el plan calibrado del Año 2.",
         "CT-06 · CT-07 · CT-08 · CT-15 · CT-17 · CT-21",
         "Presentar un informe de logros ocultando brechas abiertas, o repetir el plan del Año 1 sin recalibrar."),
    ]

    for idx, (f_col, h_col, obj_col, ct_col, trap_col) in enumerate(fases):
        ry = 472 + idx * 91
        bg = "#F8FAFC" if idx % 2 == 1 else "#FFFFFF"
        parts.append(f'<rect x="68" y="{ry}" width="1784" height="83" rx="8" fill="{bg}" stroke="#CBD5E1" stroke-width="1.2"/>')
        cx = 68
        vals = [f_col, h_col, obj_col, ct_col, trap_col]
        for j, val in enumerate(vals):
            cw_t = cols[j][1]
            if j == 0:
                parts.append(badge(cx + 10, ry + 14, cw_t - 20, 24, val.split(" · ")[0], "GATE", 11))
                parts.append(svg_text_block(cx + 12, ry + 54, val.split(" · ")[1], cw_t - 24, 11.8, "#0F172A", True, 1.2, 2))
            elif j == 1:
                parts.append(badge(cx + 10, ry + 14, cw_t - 20, 24, val.split(" · ")[0], "OK", 11))
                parts.append(svg_text_block(cx + 12, ry + 54, val.split(" · ")[1], cw_t - 24, 11.8, "#14532D", True, 1.2, 2))
            elif j == 3:
                parts.append(svg_text_block(cx + 12, ry + 24, val, cw_t - 24, 12, "#1E3A8A", True, 1.3, 3))
            elif j == 4:
                parts.append(f'<rect x="{cx+6}" y="{ry+8}" width="{cw_t-12}" height="67" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1" stroke-dasharray="4,2"/>')
                parts.append(svg_text_block(cx + 14, ry + 25, val, cw_t - 28, 11.6, "#7F1D1D", False, 1.26, 3))
            else:
                parts.append(svg_text_block(cx + 12, ry + 24, val, cw_t - 24, 12, "#1E293B", False, 1.28, 3))
            cx += cw_t + 4

    return base_shell(
        1,
        "Fases del Programa: Ciclo Operativo, 3 Olas e Hitos de 365 Días",
        "Articulación completa entre las 4 macro-fases de resiliencia, la prioridad en 3 olas y las 7 fases del primer año del CISO (F0–F6)",
        "Flujo de Fases + Matriz Temporal F0–F6",
        "Guías 01, 03 y 13 · PKG-RANSOM + PKG-CISO365",
        "\n".join(parts),
    )


# ==============================================================================
# RR-02: GOBIERNO, RESPONSABLES, DERECHOS DE DECISIÓN (DD##) Y ACTIVACIÓN
# ==============================================================================
def build_rr02() -> str:
    parts = []

    # Top-Left: 3 Activation Levels
    parts.append(card(48, 136, 884, 184))
    parts.append(f'<text x="68" y="164" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">3 NIVELES DE ACTIVACIÓN PROVISIONAL (SIN ESPERAR ATRIBUCIÓN [MS-05])</text>')
    levels = [
        ("1 · SOSPECHA", "WARN", "Señal creíble de cifrado, borrado de copias, privilegio anómalo o defensa apagada.", "Abrir caso, preservar volátiles y activar SOC."),
        ("2 · INCIDENTE MAYOR", "ALERT", "Cifrado activo, propagación, copias/privilegios tomados o función esencial caída.", "CI abre sala fuera de banda + contención + Legal."),
        ("3 · CRISIS DE NEGOCIO", "CRIT", "Continuidad, seguridad física u obligaciones superan autoridad operativa normal.", "Patrocinador/Comité decide; CI coordina técnica."),
    ]
    for i, (lt, lk, lcond, lact) in enumerate(levels):
        lx = 68 + i * (274 + 11)
        parts.append(f'<rect x="{lx}" y="176" width="274" height="132" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(badge(lx + 10, 184, 178, 22, lt, lk, 10.5))
        parts.append(svg_text_block(lx + 10, 220, lcond, 254, 11.0, "#334155", False, 1.22, 3))
        parts.append(svg_text_block(lx + 10, 272, "Acción: " + lact, 254, 10.9, "#0F172A", True, 1.2, 2))

    # Top-Right: 6-Step Coordination Sequence
    parts.append(card(952, 136, 920, 184))
    parts.append(f'<text x="972" y="164" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">SECUENCIA DE COORDINACIÓN EN CRISIS (6 PASOS · PISTAS SIMULTÁNEAS)</text>')
    seq6 = [
        ("1. Apertura UTC", "Primer indicio, fuente, activos y canal seguro."),
        ("2. Sala Fuera de Banda", "Confirmar CI, suplentes, escribiente y mandatos."),
        ("3. Dos Pistas Paralelas", "SOC delimita alcance || Operadores contienen."),
        ("4. Ritmo de Informes", "Separar Confirmado, Probable y Desconocido."),
        ("5. Negocio y Legal", "Modo alternativo + matriz comunicaciones (08)."),
        ("6. Salida Verificada", "Sin acceso activo + claves sanas + aval negocio."),
    ]
    for i, (sh, sd) in enumerate(seq6):
        col_i = i % 3
        row_i = i // 3
        sx = 972 + col_i * (286 + 11)
        sy = 176 + row_i * 68
        parts.append(f'<rect x="{sx}" y="{sy}" width="286" height="62" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2"/>')
        parts.append(f'<text x="{sx+12}" y="{sy+20}" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#1E3A8A">{esc(sh)}</text>')
        parts.append(svg_text_block(sx + 12, sy + 37, sd, 262, 10.8, "#334155", False, 1.18, 2))

    # Bottom-Left: 7 Governance Roles Matrix
    parts.append(card(48, 336, 1064, 792))
    parts.append(f'<text x="68" y="364" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">RESPONSABLES EN CRISIS: ROLES DESIGNADOS, AUTORIDAD Y REGISTRO MÍNIMO (GUÍA 01 + TARJETAS 10)</text>')

    rcols = [
        ("Rol (Titular + Suplente)", 206),
        ("Disponible Para", 262),
        ("Qué Autoriza o Valida", 292),
        ("Registro Mínimo Obligatorio", 252),
    ]
    cx = 68
    for rt, rw in rcols:
        parts.append(f'<rect x="{cx}" y="376" width="{rw}" height="34" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + rw/2:.1f}" y="398" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(rt)}</text>')
        cx += rw + 4

    roles = [
        ("Comandante (CI) y Suplente", "Declaración, coordinación fuera de banda, cadencia y cierre.", "Alcance de contención, reversión y contingencia dentro del mandato.", "ID, hora UTC, razón, alternativas y aprobador."),
        ("SOC / Respuesta (IR)", "Triage, correlación, hunting y doble verificación de cese.", "Recomendación técnica fundada (nunca mensaje externo).", "Indicadores, fuentes vivas, confianza y acciones."),
        ("Identidad / Plataformas / Backup", "Aislamiento acotado, revocación, protección WORM y restauración.", "Ejecución en perímetro autorizado con criterio de reversión.", "Sistema, operador, tarea, resultado y evidencia."),
        ("Forense / Custodio", "Preservación por volatilidad, hashes SHA-256 y transferencias.", "Método, integridad, control de acceso y retención junto a Legal.", "Cadena de custodia EV-ID, hashes y limitaciones."),
        ("Negocio / Continuidad (BCP)", "BIA, activación de modo degradado y pruebas funcionales.", "Prioridad de procesos, RTO/RPO tolerables y aceptación de retorno.", "Función, dependencia, tiempos medidos y excepción."),
        ("Legal / Privacidad", "Jurisdicciones, contratos, holds legales y hechos notificables.", "Avisos regulatorios, reservas legales, divulgación y contacto policial.", "Fundamento legal, jurisdicción y reloj confirmado."),
        ("Comunicaciones / Portavoz", "Redacción adaptada por audiencia y canales alternativos seguros.", "Publicación manual tras aprobación de Legal y autoridad ejecutiva.", "Versión exacta, audiencia, remitente, UTC y acuse."),
    ]
    for idx, rvals in enumerate(roles):
        ry = 418 + idx * 91
        bg = "#F8FAFC" if idx % 2 == 1 else "#FFFFFF"
        parts.append(f'<rect x="68" y="{ry}" width="1024" height="83" rx="7" fill="{bg}" stroke="#CBD5E1" stroke-width="1.1"/>')
        cx = 68
        for j, val in enumerate(rvals):
            rw = rcols[j][1]
            parts.append(svg_text_block(cx + 10, ry + 24, val, rw - 20, 11.8, "#0F172A" if j == 0 else "#334155", j == 0, 1.26, 3))
            cx += rw + 4

    parts.append('<rect x="68" y="1062" width="1024" height="52" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.3"/>')
    parts.append(svg_text_block(82, 1083, "Regla de suplencia y fuera de banda (CT-01, CT-16, K16): Cada suplente debe operar sin correo corporativo ni directorio principal. Nunca guardar contactos personales ni secretos en HTML/Git.", 996, 11.6, "#78350F", True, 1.25, 2))

    # Bottom-Right: Decision Rights DD##
    rx = 1132
    parts.append(card(rx, 336, 740, 792))
    parts.append(f'<text x="{rx+20}" y="364" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">DERECHOS DE DECISIÓN CANÓNICOS (DD## · QUIÉN APRUEBA VS. EJECUTA)</text>')

    dds = [
        ("DD01 / DD03", "Mandato, Carta y Apetito de Riesgo", "A: Directorio / CEO · R: CISO y Comité Ciberriesgo", "Fija umbrales preautorizados antes de cualquier crisis.", "INFO"),
        ("DD10", "Declarar Incidente Mayor", "A: CISO (indelegable en terceros)", "Un proveedor puede recomendar, nunca declarar por la organización.", "GATE"),
        ("DD11", "Aislar o Desconectar Servicio Crítico", "A: CEO / Comité Ejecutivo · R: CISO + CIO/CTO", "Con consulta a Negocio y Legal; exige plan formal de reversión.", "CRIT"),
        ("DD12", "Notificar a Reguladores o Afectados", "A: Legal, Cumplimiento y Privacidad · R: CISO", "Legal fija obligación y reloj aplicable; CISO aporta hechos probados.", "WARN"),
        ("DD13", "Autorizar Comunicación Pública", "A: CEO · R: Comunicaciones · C: Legal + CISO", "Portavoz único; prohibido especular o prometer 'cero exfiltración'.", "WARN"),
        ("DD14", "Activar Continuidad (BCP) o DR", "A: CEO · R: CIO/CTO · C: CISO + Dueño Negocio", "Cuando el daño conectado crece o restauración supera RTO.", "GATE"),
        ("DD18", "Suspender Agente IA / Autoridad Delegada", "A: Dueño de Negocio · R: CIO/CTO · C: CISO + Legal", "Activa PB-07 y modo sin IA (K56); no autoriza por sí solo DD11.", "PURP"),
    ]
    for idx, (dc, dt, draci, dnote, dk) in enumerate(dds):
        dy = 380 + idx * 88
        parts.append(f'<rect x="{rx+18}" y="{dy}" width="704" height="80" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(badge(rx + 28, dy + 10, 118, 24, dc, dk, 11))
        parts.append(f'<text x="{rx+158}" y="{dy+27}" font-family="{FONT}" font-size="13.2" font-weight="700" fill="#0F172A">{esc(dt)}</text>')
        parts.append(f'<text x="{rx+28}" y="{dy+50}" font-family="{FONT}" font-size="11.8" font-weight="700" fill="#1E3A8A">{esc(draci)}</text>')
        parts.append(svg_text_block(rx + 28, dy + 68, dnote, 680, 11.3, "#475569", False, 1.2, 1))

    parts.append(f'<rect x="{rx+18}" y="1002" width="704" height="112" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.4"/>')
    parts.append(f'<text x="{rx+32}" y="1026" font-family="{FONT}" font-size="13" font-weight="700" fill="#1E3A8A">TRES MODALIDADES EXPLÍCITAS DE DECISIÓN EN CRISIS (HOJA DECISIONES · LIBRO 02)</text>')
    parts.append(svg_text_block(rx + 32, 1048, "1) ACTUAR en perímetro autorizado · 2) ESPERAR con mitigación temporal · 3) RECHAZAR con aceptación formal del riesgo residual. Separar siempre cualquier evaluación sobre rescate/extorsión en vía ejecutiva/legal independiente [MS-02].", 676, 11.6, "#1E293B", False, 1.3, 3))

    return base_shell(
        2,
        "Gobierno, Responsables y Derechos de Decisión en Crisis (DD##)",
        "Quién activa, quién autoriza (A), quién ejecuta (R) y cómo opera el mando dual fuera de banda sin improvisar autoridad",
        "Matriz de Roles + Derechos de Decisión",
        "Guías 01 y 10 · Libro 02 (Hoja Decisiones)",
        "\n".join(parts),
    )


# ==============================================================================
# RR-03: TAREAS DE PREPARACIÓN — CATÁLOGO CT-01..21 Y ESCALA DE EVIDENCIA
# ==============================================================================
def build_rr03() -> str:
    parts = []

    # Top Strip: 5 Evidence States
    parts.append(card(48, 136, 1824, 144))
    parts.append(f'<text x="72" y="162" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">ESCALA DE MADUREZ DEMOSTRADA: IMPLEMENTADO NO SIGNIFICA PROBADO (EQUIVALENCIA CISO 365 EV01–51 Y KPI E1–E5)</text>')

    states = [
        ("0 · NO EVALUADO", "NEUTRAL", "Sin evidencia ni denominadores (KSG04 pendiente). Estado inicial obligatorio antes de H30/H60."),
        ("1 · NO IMPLEMENTADO", "CRIT", "EV=0 Inexistente · Estadio KPI E1 (ad hoc). Ausencia confirmada en el alcance evaluado (F1/H30)."),
        ("2 · PARCIAL", "WARN", "EV=1 Inicial · Estadio KPI E2. Cobertura incompleta, sin denominador contra universo o sin operación regular."),
        ("3 · IMPLEMENTADO", "INFO", "EV=2 Definido · Elegible E3 solo en despliegue. Configuración y operador activos, pero SIN ensayo funcional."),
        ("4 · PROBADO", "OK", "EV=3/4 Con Evidencia · Habilita E3/E4 en resiliencia (H270). Ensayo autorizado con fecha, denominador y acta."),
    ]
    sw = 336
    sgap = 24
    for i, (st_h, st_k, st_d) in enumerate(states):
        sx = 72 + i * (sw + sgap)
        parts.append(f'<rect x="{sx}" y="174" width="{sw}" height="94" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(badge(sx + 10, 182, 186, 22, st_h, st_k, 10.5))
        parts.append(svg_text_block(sx + 10, 218, st_d, sw - 20, 11.2, "#334155", False, 1.24, 3))
        if i < 4:
            parts.append(arrow_h(sx + sw + 3, 221, sx + sw + sgap - 3, "#64748B"))

    # 4 Columns of Controls CT-01..21 (Non-MECE functional reinforcement explicitly noted)
    pillars = [
        ("A · RECUPERACIÓN Y CONTINUIDAD (1º)", "#14532D", "#DCFCE7", "#16A34A", [
            ("CT-01", "BIA, Dueños y Dependencias", "Procesos críticos con dueño, RTO/RPO firmados y mapa de identidad/red/datos/3P.", "Negocio / BCP · F1–F2"),
            ("CT-02", "Copias Inmutables y Restaurables", "Respaldos WORM fuera del plano admin productivo; probar restauración vs RTO/RPO.", "Backup / Negocio · F1–F5"),
            ("CT-03", "Recuperación Limpia de Identidad", "Ruta aislada AD Forest Recovery + break-glass FIDO2 sin dependencia circular.", "Identidad / IR · F1–F5"),
            ("CT-15", "Modo Degradado / Contingencia", "Operación manual segura con umbral de activación, numeración y reconciliación.", "Continuidad · F2–F5"),
            ("CT-20", "Recuperación Masiva M365", "M365 Backup y Files Restore ensayados en su alcance (no sustituyen AD ni apps).", "M365 / Backup · F2–F5"),
        ]),
        ("B · IDENTIDAD, PRIVILEGIOS Y SUPERFICIE", "#1E3A8A", "#DBEAFE", "#2563EB", [
            ("CT-04", "Mínimo Privilegio, PIM y MFA Fuerte", "Elevación JIT sin admin permanente, MFA resistente a phishing, LAPS y estaciones PAW.", "Identidad · F1–F4"),
            ("CT-05", "EDR y Tamper Protection Medible", "Agente sano/universo inventariado; exclusiones justificadas y con vencimiento.", "Endpoints · F2–F4"),
            ("CT-06", "Exposición Externa y Parcheo", "Accesos remotos y servicios publicados priorizados por explotabilidad real e impacto.", "Plataforma · F2–F6"),
            ("CT-07", "Segmentación TI/OT/Backup", "Frena movimiento lateral hacia copias y activos críticos; restringe egress en zona limpia.", "Red / OT · F2–F6"),
            ("CT-08", "Identidades de Carga y Secretos", "Service principals, OAuth, certificados y claves con dueño, expiración y rotación dual.", "Identidad / Apps · F1–F6"),
        ]),
        ("C · ENTRADA, DETECCIÓN SOC Y CONTENCIÓN", "#0C4A6E", "#E0F2FE", "#0284C7", [
            ("CT-09", "Defensa de Correo, Web y Ejecución", "MDO Safe Links/Attachments, reglas ASR y bloqueo temprano integrado al SOC.", "Correo / Endpoint · F2–F5"),
            ("CT-10", "Control de Escritura y Retención", "Mínimo permiso de borrado, Controlled Folder Access y Preservation Lock.", "Datos / M365 · F2–F4"),
            ("CT-11", "Telemetría UTC y Salud de Sensor", "Cobertura identidad/host/red/backup/datos; caída de sensor dispara alerta propia.", "Ingeniería SOC · F2–F4"),
            ("CT-12", "Casos de Uso DE-01 a DE-13 Vivos", "Cada detección tiene regla, guardia, criterio de escalamiento y simulación trimestral.", "SOC · F2–F4"),
            ("CT-13", "Aislamiento y Repudio Comprobados", "Ejecución autorizada de corte en host/cuenta/sesión/app verificando cese efectivo.", "IR / IdP / Red · F1–F4"),
        ]),
        ("D · FORENSE, CRISIS, TERCEROS E IA", "#4C1D95", "#EDE9FE", "#7C3AED", [
            ("CT-14", "Preservación Forense y Custodia", "Audit Premium >=1 año, Legal Hold, hash SHA-256 y transferencias trazables.", "Forense / Legal · F2–F4"),
            ("CT-16", "Comunicaciones y Fuera de Banda", "Matriz legal por jurisdicción, borradores por audiencia y simulacro sin envío real.", "Legal / Comms · F2–F5"),
            ("CT-17", "Revisiones Trimestrales y E1–E3", "Control de deriva cada trimestre + ejercicio anual medido con retest de fallos.", "Programa / CI · F2–F6"),
            ("CT-18", "Accesos e Integraciones Terceros", "Inventario B2B/OAuth/EDI, SLAs de aviso y ruta probada de desconexión/reingreso.", "Compras / IR · F1–F5"),
            ("CT-19", "Visibilidad y Freno de Exfiltración", "Detección DLP/IRM de robo de datos separada de la hipótesis de cifrado.", "Datos / SOC · F2–F4"),
            ("CT-21", "Gobierno de IA y Modo Sin IA", "Inventario de agentes, dueño humano, Entra Agent ID, DLP prompts y apagado PB-07.", "IA / IdP / Negocio · F2–F6"),
        ]),
    ]

    pw = 441
    pgap = 20
    for col_i, (ptitle, pfg, pbg, pst, items) in enumerate(pillars):
        px = 48 + col_i * (pw + pgap)
        parts.append(card(px, 294, pw, 834))
        parts.append(f'<rect x="{px}" y="294" width="{pw}" height="42" rx="10" fill="{pbg}" stroke="{pst}" stroke-width="1.5"/>')
        parts.append(f'<text x="{px + pw/2:.1f}" y="320" font-family="{FONT}" font-size="13.2" font-weight="700" fill="{pfg}" text-anchor="middle">{esc(ptitle)}</text>')

        n_items = len(items)
        step_h = 152 if n_items == 5 else 127
        box_h = 140 if n_items == 5 else 117
        for idx, (cid, cname, cdesc, cowner) in enumerate(items):
            cy = 348 + idx * step_h
            parts.append(f'<rect x="{px+12}" y="{cy}" width="{pw-24}" height="{box_h}" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.1"/>')
            parts.append(badge(px + 20, cy + 10, 68, 22, cid, "GATE" if col_i < 3 else "PURP", 11))
            parts.append(f'<text x="{px+98}" y="{cy+26}" font-family="{FONT}" font-size="12.6" font-weight="700" fill="#0F172A">{esc(cname)}</text>')
            parts.append(svg_text_block(px + 20, cy + 48, cdesc, pw - 40, 11.4, "#334155", False, 1.22, 3 if n_items == 5 else 2))
            parts.append(f'<text x="{px+20}" y="{cy + box_h - 11}" font-family="{FONT}" font-size="10.8" font-weight="700" fill="{pfg}">Dueño y ventana: {esc(cowner)}</text>')

    return base_shell(
        3,
        "Tareas de Preparación: Los 21 Controles (CT-01..21) y su Evidencia",
        "Agrupación funcional (no-MECE) por prioridad de ejecución [MS-01]: cada control exige alcance, denominador contra universo y acta de prueba",
        "Progresión de Evidencia + Grilla 21 Controles",
        "Guías 02 y 03 · Libro 01 (Evaluación y Controles)",
        "\n".join(parts),
    )


# ==============================================================================
# RR-04: PROCESO CRÍTICO 1 — MONITOREO, DETECCIONES DE-01..13 Y TRIAGE
# ==============================================================================
def build_rr04() -> str:
    parts = []

    # Top: 6-Step Reproducible Triage Flow
    parts.append(card(48, 136, 1824, 202))
    parts.append(f'<text x="72" y="163" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">PROCESO DE TRIAGE REPRODUCIBLE EN 6 PASOS: ABRIR, VERIFICAR Y DECIDIR CON HILO AUDITABLE UTC (GUÍA 04 · FORMULARIO F1)</text>')

    tsteps = [
        ("1. ABRIR Y SALUD", "Asignar INC-ID, guardar alerta original + UTC (evento, ingesta, recepción) y comprobar que el sensor esté vivo."),
        ("2. CONTEXTO BIA", "Contrastar ventana de cambio aprobada, criticidad y dueño; buscar 2ª evidencia independiente cuando haya margen."),
        ("3. HIPÓTESIS CLARA", "Separar activos Confirmados, Posibles y No revisados; nunca clasificar como 'limpio' lo aún desconocido."),
        ("4. ESCALAR AL CI", "Cifrado, copias tocadas, privilegio alto, exfiltración o RTO amenazado activan al CI sin esperar vector inicial."),
        ("5. PEDIR CONTENCIÓN", "Proponer PB-01..07 indicando radio de impacto, autorizador DD##, reversión y preservación forense paralela."),
        ("6. DOBLE CHEQUEO", "Confirmar acción ejecutada en plataforma Y ausencia de propagación en telemetría durante ventana aprobada."),
    ]
    tw = 276
    tgap = 24
    for i, (th, td) in enumerate(tsteps):
        tx = 72 + i * (tw + tgap)
        parts.append(f'<rect x="{tx}" y="176" width="{tw}" height="148" rx="10" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>')
        parts.append(f'<text x="{tx+14}" y="201" font-family="{FONT}" font-size="13" font-weight="700" fill="#1E3A8A">{esc(th)}</text>')
        parts.append(svg_text_block(tx + 14, 225, td, tw - 28, 11.6, "#1E293B", False, 1.26, 5))
        if i < 5:
            parts.append(arrow_h(tx + tw + 3, 250, tx + tw + tgap - 3, "#1D4ED8"))

    # Bottom-Left: 13 Detection Use Cases Table (DE-01..DE-13)
    parts.append(card(48, 352, 1368, 776))
    parts.append(f'<text x="68" y="380" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">CATÁLOGO DE LOS 13 CASOS DE USO DE DETECCIÓN (DE-01 A DE-13) Y ESCALAMIENTO A PLAYBOOKS</text>')

    dcols = [
        ("Código y Fase", 210),
        ("Señal que Inicia Revisión", 456),
        ("Tablas / Motor Referencia Full Microsoft", 452),
        ("Escalamiento", 198),
    ]
    cx = 68
    for dt, dw in dcols:
        parts.append(f'<rect x="{cx}" y="392" width="{dw}" height="34" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + dw/2:.1f}" y="414" font-family="{FONT}" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(dt)}</text>')
        cx += dw + 4

    des = [
        ("DE-01 · Acceso inicial", "Autenticación de riesgo, repetición anómala o acceso remoto fuera de patrón.", "SigninLogs, IdentityLogonEvents · Entra ID Prot. + MDI + UEBA", "PB-02 (IR/IdP)"),
        ("DE-02 · Toma de control", "Alta de privilegios, cambio MFA/CA, consentimiento OAuth o cuenta emergencia.", "AuditLogs, CloudAppEvents · Entra PIM + Defender XDR + NRT", "PB-02 / PB-05"),
        ("DE-03 · Supresión defensa", "EDR/AV deshabilitado, nueva exclusión, borrado de logs (1102) o host offline.", "DeviceEvents, SecurityEvent, Heartbeat · MDE Tamper + Sentinel", "PB-01 Urgente"),
        ("DE-04 · Mov. lateral", "Inicio remoto administrativo o ejecución/propagación entre múltiples hosts.", "DeviceLogonEvents, DeviceProcessEvents · MDI + Attack Disruption", "PB-01 / PB-02"),
        ("DE-05 · Ataque a copias", "Desactivación, borrado, cambio de retención/WORM o fallos en respaldos.", "AddonAzureBackupAlerts, vssadmin/wbadmin · Resource Guard + NRT", "PB-03 Crítico"),
        ("DE-06 · Cifrado activo", "Cambios masivos de archivos, notas de rescate, procesos cifradores o I/O pico.", "DeviceFileEvents, StorageBlobLogs · Attack Disruption + CFA", "PB-01 Inmediato"),
        ("DE-07 · Sincr. / borrado", "Borrado masivo, versionado alterado o sincronización inusual (sin cifrado).", "OfficeActivity, CloudAppEvents · MDA + SharePoint/OneDrive + Audit", "PB-04 Datos"),
        ("DE-08 · Exfiltración", "Transferencia o compartición externa masiva de datos sensibles fuera de base.", "Purview DLP/IRM Alerts, DeviceNetworkEvents · DLP + Adaptive Prot.", "PB-04 + Legal"),
        ("DE-09 · Control remoto", "Tráfico saliente, C2 o dominio/IP sospechoso correlacionado con otra señal.", "DeviceNetworkEvents, CommonSecurityLog, DnsEvents · MDE Net + TI", "PB-01 / PB-05"),
        ("DE-10 · Disponibilidad", "Caída de servicio crítico, fallo de identidad o degradación que amenaza RTO.", "AzureActivity, Heartbeat, Azure Monitor · Tablero SOC/Plataforma", "PB-03 + CI/BCP"),
        ("DE-11 · Ceguera sensor", "Falta de logs/heartbeats, caída de agente o desfase horario en activo crítico.", "Heartbeat, SentinelHealth, Usage · Salud SOC y MDE Sensor Health", "PB-01 Incidente"),
        ("DE-12 · Aviso humano", "Usuario, socio o proveedor reporta rescate, indisponibilidad o extorsión.", "Canal fuera de banda + Tickets SOC + Purview eDiscovery Hold", "PB-01 / PB-04"),
        ("DE-13 · IA y Agentes", "Prompt injection indirecto, abuso de herramienta MCP o acceso masivo por agente.", "CopilotInteraction, Defender for AI, SigninLogs (Agent) · DSPM AI", "PB-07 + K56"),
    ]
    for idx, (dc, dsig, dtab, desc_pb) in enumerate(des):
        ry = 432 + idx * 52.5
        is_ai_or_bkp = idx in (4, 5, 10, 12)
        bg = "#FEFCE8" if is_ai_or_bkp else ("#F8FAFC" if idx % 2 == 1 else "#FFFFFF")
        parts.append(f'<rect x="68" y="{ry:.1f}" width="1328" height="47.5" rx="6" fill="{bg}" stroke="#CBD5E1" stroke-width="1"/>')
        cx = 68
        for j, val in enumerate((dc, dsig, dtab, desc_pb)):
            dw = dcols[j][1]
            if j == 3:
                b_kind = "CRIT" if ("Inmediato" in val or "Crítico" in val) else ("PURP" if "PB-07" in val else "GATE")
                parts.append(badge(cx + 10, ry + 11.5, dw - 20, 24, val, b_kind, 10.8))
            else:
                parts.append(svg_text_block(cx + 10, ry + 19, val, dw - 20, 11.2, "#0F172A" if j == 0 else "#334155", j == 0, 1.2, 2))
            cx += dw + 4

    # Bottom-Right: Cadence + Guardrails
    rx = 1436
    parts.append(card(rx, 352, 436, 422))
    parts.append(f'<text x="{rx+20}" y="382" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">CADENCIA OPERATIVA DEL SOC</text>')
    cads = [
        ("Por Turno / Diaria (R04)", "Salud de fuentes críticas, cola alta severidad, canal fuera de banda y suplentes."),
        ("Semanal (R03)", "Cambios en reglas, falsos positivos/negativos, altas privilegiadas y fallos de backup."),
        ("Trimestral", "Simulaciones benignas de DE-*, denominadores de cobertura, latencia y escalamiento."),
        ("Posincidente / Ejercicio", "Cronología detección->triage->contención, huecos de logs y lecciones con dueño."),
    ]
    for i, (ch, cd) in enumerate(cads):
        cy = 400 + i * 90
        parts.append(f'<rect x="{rx+18}" y="{cy}" width="400" height="80" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.1"/>')
        parts.append(f'<text x="{rx+30}" y="{cy+24}" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#0284C7">{esc(ch)}</text>')
        parts.append(svg_text_block(rx + 30, cy + 43, cd, 376, 11.4, "#334155", False, 1.22, 2))

    parts.append(card(rx, 790, 436, 338, fill="#FEF2F2", stroke="#EF4444", stroke_w=1.5))
    parts.append(f'<text x="{rx+20}" y="820" font-family="{FONT}" font-size="14.5" font-weight="700" fill="#991B1B">REGLAS ANTI-SILENCIO Y MEDICIÓN</text>')
    rules = [
        "• Doble extorsión sin cifrado: DE-07 y DE-08 operan independientes de DE-06.",
        "• Prohibido desactivar una regla permanente para cerrar un falso positivo.",
        "• Reportar mediana, p90 y peor caso (la media esconde demoras fatales).",
        "• Sin medición verificada mostrar 'Sin datos', nunca '0 min' ni '100%'.",
    ]
    for i, rl in enumerate(rules):
        parts.append(svg_text_block(rx + 20, 848 + i * 66, rl, 396, 11.8, "#7F1D1D", i in (0, 3), 1.25, 3))

    return base_shell(
        4,
        "Proceso de Monitoreo, 13 Detecciones (DE-01..13) y Triage SOC",
        "Flujo reproducible desde la alerta o caída de sensor hasta la solicitud de contención y verificación en dos vías",
        "Flujo 6 Pasos + Matriz de 13 Detecciones",
        "Guía 04 · Libro 02 (Detecciones) · F1",
        "\n".join(parts),
    )


# ==============================================================================
# RR-05: PROCESO CRÍTICO 2 — CONTENCIÓN, PLAYBOOKS PB-01..07 Y REVOCACIÓN
# ==============================================================================
def build_rr05() -> str:
    parts = []

    # Top-Left: 5 Invariants
    parts.append(card(48, 136, 884, 186, fill="#FFFBEB", stroke="#F59E0B", stroke_w=1.6))
    parts.append(f'<text x="68" y="163" font-family="{FONT}" font-size="15" font-weight="700" fill="#92400E">5 INVARIANTES DE INTERVENCIÓN EN RESPUESTA TEMPRANA (GUÍA 05)</text>')
    invs = [
        ("1. Personas primero:", "Identificar sistemas clínicos, industriales o físicos esenciales antes de aislar."),
        ("2. Acción en paralelo:", "Ante propagación activa, aislar sin esperar imagen forense completa [MS-05]."),
        ("3. No apagar por rutina:", "Apagar destruye memoria volátil y claves; preferir aislamiento de red/EDR [MS-06]."),
        ("4. Perímetro preciso:", "Acotar host, cuenta, segmento o app; evitar tumbar todo el tenant sin evaluar BCP."),
        ("5. Efecto comprobado:", "'Comando aceptado' != 'acceso terminado'; verificar cese real en telemetría."),
    ]
    for i, (ik, iv) in enumerate(invs):
        iy = 185 + i * 26
        parts.append(f'<text x="68" y="{iy}" font-family="{FONT}" font-size="11.8" font-weight="700" fill="#78350F">{esc(ik)}</text>')
        parts.append(f'<text x="234" y="{iy}" font-family="{FONT}" font-size="11.6" font-weight="400" fill="#1E293B">{esc(iv)}</text>')

    # Top-Right: 6-Step Common Playbook Loop (Form F3)
    parts.append(card(952, 136, 920, 186))
    parts.append(f'<text x="972" y="163" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">BUCLE COMÚN DE EJECUCIÓN DE CADA PLAYBOOK (6 PASOS · ORDEN F3)</text>')
    ploop = [
        ("1. Abrir y Avisar", "INC-ID, UTC, afectados y aviso a CI/custodio."),
        ("2. Acción Mínima", "Elegir perímetro autorizado y medir colateral."),
        ("3. Preservar Previo", "Guardar logs/estado seguro sin frenar urgencia."),
        ("4. Consola Oficial", "Ejecutar con permisos reales y guardar Task ID."),
        ("5. Verificar Cese", "Validar en telemetría + negocio nuevas sesiones."),
        ("6. Plan Reversión", "Documentar orden limpio y aval CI/negocio."),
    ]
    for i, (ph, pd) in enumerate(ploop):
        col_i = i % 3
        row_i = i // 3
        px = 972 + col_i * (286 + 11)
        py = 175 + row_i * 68
        parts.append(f'<rect x="{px}" y="{py}" width="286" height="62" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>')
        parts.append(f'<text x="{px+12}" y="{py+20}" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#14532D">{esc(ph)}</text>')
        parts.append(svg_text_block(px + 12, py + 37, pd, 262, 10.8, "#334155", False, 1.18, 2))

    # Middle: 7 Playbooks Table (PB-01..PB-07)
    parts.append(card(48, 336, 1824, 496))
    parts.append(f'<text x="72" y="364" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">TARJETAS DE CONTENCIÓN E INVALIDACIÓN DEL ACCESO ADVERSARIO ("REPUDIO" OPERATIVO: PB-01 A PB-07)</text>')

    pcols = [
        ("Playbook y Disparador", 284),
        ("Decisión DD", 122),
        ("Acción Inicial Autorizada (Stack Referencia)", 684),
        ("Verificación Independiente y Límite Crítico", 682),
    ]
    cx = 68
    for pt, pw in pcols:
        parts.append(f'<rect x="{cx}" y="376" width="{pw}" height="34" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + pw/2:.1f}" y="398" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(pt)}</text>')
        cx += pw + 4

    pbs = [
        ("PB-01 · Host con cifrado o propagación (DE-03/04/06)", "DD10 · DD11",
         "Aislar origen/propagación vía MDE Device Isolation, red o Attack Disruption; recoger paquete Live Response sin apagar por defecto.",
         "Confirmar aislamiento efectivo y cero tráfico lateral nuevo; no aislar servicios físicos esenciales sin ruta de continuidad."),
        ("PB-02 · Identidad privilegiada o sesión (DE-01/02)", "DD10 · DD11",
         "Asegurar canal break-glass limpio; deshabilitar cuenta AD/Entra, revocar refresh tokens, CAE, doble reset KRBTGT según alcance y revisar MFA/PIM.",
         "Probar que nuevos accesos fallan; recordar que access tokens vigentes o cookies propias de apps SaaS pueden seguir activas [MS-10]."),
        ("PB-03 · Repositorio de respaldos atacado (DE-05/10)", "DD11 · DD14",
         "Bloquear borrado/cambios con Multi-User Authorization (Resource Guard), inmovilizar copias WORM sanas y proteger inventario de claves.",
         "Validar puntos limpios previos al compromiso; nunca borrar logs de backup ni cortar replicación sin medir impacto en RTO."),
        ("PB-04 · Exfiltración o borrado/sync (DE-07/08)", "DD11 · DD12",
         "Pausar sincronización OneDrive afectada, cortar descargas en Defender for Cloud Apps, aplicar bloqueo DLP y activar Legal Hold en Purview.",
         "Delimitar archivos/enlaces/destinos y confirmar fin de salida; Legal evalúa notificación sin prometer 'ausencia de robo'."),
        ("PB-05 · Claves, apps OAuth o terceros (DE-02/09)", "DD11 · DD15/16",
         "Suspender Service Principal/Enterprise App, revocar consentimientos OAuth, rotar secretos/certificados en Key Vault bajo control dual y cortar B2B.",
         "Verificar que servicios esenciales operan con credenciales nuevas y que tokens antiguos fallan junto al proveedor."),
        ("PB-06 · Alcance erróneo o falso positivo", "DD11 · DD14",
         "Conservar evidencia del estado previo, obtener aval de CI y dueño de negocio y revertir gradualmente por tramos controlados.",
         "Volver a medir salud operativa y ausencia de amenaza; no cerrar incidente si subsiste hipótesis plausible."),
        ("PB-07 · Agente IA, Copilot o MCP comprometido (DE-13)", "DD11 · DD17/18",
         "Bloquear identidad en Entra Agent ID / Agent 365, desactivar agente/MCP en Copilot Studio o Foundry, cortar RAG contaminado y pasar a modo sin IA.",
         "Preservar CopilotInteraction en Purview Audit, revocar credenciales OBO/SPN subyacentes y confirmar continuidad manual (K56)."),
    ]
    for idx, (p_id, p_dd, p_act, p_lim) in enumerate(pbs):
        ry = 416 + idx * 58
        bg = "#EDE9FE" if idx == 6 else ("#F8FAFC" if idx % 2 == 1 else "#FFFFFF")
        parts.append(f'<rect x="68" y="{ry}" width="1784" height="53" rx="6" fill="{bg}" stroke="#CBD5E1" stroke-width="1.1"/>')
        cx = 68
        parts.append(svg_text_block(cx + 10, ry + 20, p_id, pcols[0][1] - 20, 11.4, "#0F172A", True, 1.2, 2))
        cx += pcols[0][1] + 4
        parts.append(badge(cx + 8, ry + 14, pcols[1][1] - 16, 24, p_dd, "PURP" if idx == 6 else "GATE", 10.5))
        cx += pcols[1][1] + 4
        parts.append(svg_text_block(cx + 10, ry + 20, p_act, pcols[2][1] - 20, 11.3, "#1E293B", False, 1.22, 2))
        cx += pcols[2][1] + 4
        parts.append(svg_text_block(cx + 10, ry + 20, p_lim, pcols[3][1] - 20, 11.3, "#7F1D1D" if idx in (1, 2, 6) else "#334155", False, 1.22, 2))

    # Bottom: 6 Revocation Surfaces & Residual Risk
    parts.append(card(48, 846, 1824, 282))
    parts.append(f'<text x="72" y="874" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">MATRIZ DE LAS 6 SUPERFICIES DE REVOCACIÓN: POR QUÉ "CUENTA BLOQUEADA" NO EQUIVALE A CIERRE [MS-10]</text>')

    surfs = [
        ("1. AD Híbrido", "Verificar replicación DCs, sesiones remotas y roles.", "Riesgo: equipos no sincronizados y tickets Kerberos ya emitidos."),
        ("2. Microsoft Entra", "Bloqueo, revocación refresh tokens y roles PIM.", "Riesgo: access tokens siguen vivos hasta expirar salvo CAE."),
        ("3. SaaS / Aplicación", "Sesiones propias, cuentas locales sin SSO y soporte.", "Riesgo: Entra NO revoca cookies emitidas por otra app."),
        ("4. Servicio / API", "Secretos, certificados, Managed IDs y permisos OAuth.", "Riesgo: rotación incompleta deja puertas abiertas o cae prod."),
        ("5. Dispositivo Host", "Caché local, aislamiento EDR y carpetas sincronizadas.", "Riesgo: offline conserva datos; wipe borra evidencia forense."),
        ("6. Agente IA / MCP", "Entra Agent ID, permisos Graph, conectores y tokens OBO.", "Riesgo: apagar UI del chat no revoca SPN ni limpia RAG."),
    ]
    sw = 282
    sgap = 18
    for i, (sh, sver, srisk) in enumerate(surfs):
        sx = 72 + i * (sw + sgap)
        parts.append(f'<rect x="{sx}" y="890" width="{sw}" height="222" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(f'<rect x="{sx}" y="890" width="{sw}" height="32" rx="8" fill="#0F2C59"/>')
        parts.append(f'<text x="{sx + sw/2:.1f}" y="911" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(sh)}</text>')
        parts.append(svg_text_block(sx + 12, 942, "Verificar: " + sver, sw - 24, 11.4, "#1E293B", False, 1.24, 3))
        parts.append(f'<rect x="{sx+10}" y="1008" width="{sw-20}" height="94" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1" stroke-dasharray="4,2"/>')
        parts.append(svg_text_block(sx + 18, 1028, srisk, sw - 36, 11.2, "#7F1D1D", True, 1.24, 4))

    return base_shell(
        5,
        "Proceso de Contención, Playbooks (PB-01..07) y Superficies de Revocación",
        "Invariantes de seguridad, bucle operativo F3, tarjetas de respuesta (incluida IA PB-07) y límites técnicos de revocación",
        "Bucle Operativo + 7 Playbooks + 6 Superficies",
        "Guía 05 · Libro 02 (Decisiones e Incidentes) · F3",
        "\n".join(parts),
    )


# ==============================================================================
# RR-06: PROCESO CRÍTICO 3 — FORENSE (SHA-256) Y RECUPERACIÓN LIMPIA (RTO/RPO)
# ==============================================================================
def build_rr06() -> str:
    parts = []

    # Top-Left: Forensic Chain of Custody (6 Steps + F4)
    parts.append(card(48, 136, 650, 618))
    parts.append(f'<text x="68" y="164" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">PISTA A · EVIDENCIA Y CADENA DE CUSTODIA (GUÍA 06 · F4)</text>')

    fsteps = [
        ("1. Priorizar por volatilidad y Legal Hold", "Memoria, árbol EDR, logs identidad/nube/DNS, copias y notas; activar Purview Legal Hold sin avisar al atacante."),
        ("2. Capturar con ventana UTC y silencios", "Registrar EV-ID, filtros exactos y también qué fuentes NO entregaron eventos y por qué."),
        ("3. Integridad SHA-256 en depósito WORM", "Calcular hash por copia/exportación y alojar en repositorio cifrado inmutable (nunca adjuntar binarios al Excel)."),
        ("4. Transferencias verificadas con acuse", "Registrar emisor, receptor, UTC y hash comprobado; si falla integridad, frenar uso probatorio y recapturar."),
        ("5. Análisis sobre copias segregadas", "Nunca alterar el original ni abrir muestras en equipos operativos; correlación temporal != causalidad."),
        ("6. Retención y disposición por Legal", "Conservar bajo hold regulatorio/penal; prohibido borrar logs en retención por falta de espacio."),
    ]
    for i, (fh, fd) in enumerate(fsteps):
        fy = 180 + i * 76
        parts.append(f'<rect x="68" y="{fy}" width="610" height="68" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.1"/>')
        parts.append(f'<text x="82" y="{fy+22}" font-family="{FONT}" font-size="12.3" font-weight="700" fill="#4C1D95">{esc(fh)}</text>')
        parts.append(svg_text_block(82, fy + 41, fd, 582, 11.2, "#334155", False, 1.2, 2))

    parts.append('<rect x="68" y="642" width="610" height="98" rx="8" fill="#EDE9FE" stroke="#7C3AED" stroke-width="1.3"/>')
    parts.append(f'<text x="82" y="665" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#4C1D95">ESTRUCTURA OBLIGATORIA DEL INFORME FORENSE</text>')
    parts.append(svg_text_block(82, 686, "Separar estrictamente: (a) Hechos observados con EV-ID y UTC · (b) Inferencias con soporte · (c) Hipótesis abiertas · (d) Lagunas de telemetría. Nunca declarar 'ausencia de exfiltración' solo por falta de alertas.", 582, 11.3, "#1E293B", False, 1.25, 3))

    # Top-Right: Clean-Room Recovery Process (7 Steps + Contingency)
    rx = 718
    rw = 1154
    parts.append(card(rx, 136, rw, 618))
    parts.append(f'<text x="{rx+22}" y="164" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">PISTA B · CONTINGENCIA Y RECUPERACIÓN CONFIABLE EN ZONA LIMPIA (GUÍA 07 · DD14 · F2)</text>')

    parts.append(f'<rect x="{rx+22}" y="178" width="{rw-44}" height="68" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.4"/>')
    parts.append(badge(rx + 34, 190, 214, 24, "[GATE DD14] Modo Contingencia", "WARN", 11))
    parts.append(svg_text_block(rx + 262, 198, "CI + Dueño de Negocio activan operación degradada/manual cuando seguir conectado amplifica daño o la restauración superará el RTO. Numerar transacciones manuales para reconciliación posterior y validar privacidad/seguridad con Legal.", rw - 298, 11.5, "#78350F", False, 1.25, 2))

    rsteps = [
        ("1. Fijar Límite de Confianza", "IR delimita planos sospechosos y valida que el atacante NO controla la consola de backup ni la zona limpia."),
        ("2. Elegir Punto de Restauración", "Comparar hora del compromiso vs última copia íntegra y RPO; si excede RPO, negocio decide reconciliación."),
        ("3. Restituir Cimientos en Orden", "Break-glass verificado -> Identidad (AD/Entra) -> DNS -> Red segmentada -> Telemetría/EDR -> Secretos -> Base."),
        ("4. Reconstruir Servicios Aislados", "Imágenes limpias, parches, EDR activo y rotación de credenciales ANTES de abrir tráfico productivo."),
        ("5. Prueba Funcional y Medición", "Negocio ejecuta transacciones reales, concilia datos manuales y mide RTO y RPO efectivos frente al BIA."),
        ("6. Reconexión Gradual Vigilada", "CI autoriza por segmento; IR vigila cero reaparición adversaria y el Dueño de Negocio firma aceptación."),
        ("7. Cierre, Evidencia y Mejora", "Conciliar pendientes manuales, entregar evidencia a Legal y actualizar BIA, arquitectura y plan de pruebas."),
    ]
    for i, (rh, rd) in enumerate(rsteps):
        col_i = i % 2
        row_i = i // 2
        bx = rx + 22 + col_i * (546 + 18) if i < 6 else rx + 22
        bw_c = 546 if i < 6 else rw - 44
        by = 260 + row_i * 120
        bh_c = 108 if i < 6 else 104
        parts.append(f'<rect x="{bx}" y="{by}" width="{bw_c}" height="{bh_c}" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.3"/>')
        parts.append(f'<text x="{bx+14}" y="{by+25}" font-family="{FONT}" font-size="13" font-weight="700" fill="#14532D">{esc(rh)}</text>')
        parts.append(svg_text_block(bx + 14, by + 47, rd, bw_c - 28, 11.6, "#1E293B", False, 1.26, 3))

    # Bottom: 4 Full Microsoft Recovery Scopes
    parts.append(card(48, 770, 1824, 358))
    parts.append(f'<text x="72" y="798" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">ARQUITECTURA DE RECUPERACIÓN FULL MICROSOFT EN 4 ÁMBITOS Y CONDICIONES DE NO-REINTRODUCCIÓN</text>')

    scols = [
        ("1. Infraestructura, VMs, SQL y Archivos", "Azure Backup inmutable + Multi-User Authorization (Resource Guard en suscripción/tenant separado) + Azure Site Recovery hacia Landing Zone limpia.", "PROHIBIDO reconectar redes restauradas al dominio comprometido antes de contener y rotar secretos (CT-02, CT-07 · K28, K30, K47)."),
        ("2. Colaboración Masiva (M365)", "Microsoft 365 Backup para restauración rápida a gran escala de SharePoint, OneDrive y Exchange; Files Restore (30d) para casos acotados.", "Ni OneDrive Sync ni Files Restore reconstruyen Active Directory, bases de datos LOB ni configuraciones SaaS (CT-20 · K28, K30)."),
        ("3. Plano de Identidad (AD DS y Entra)", "Procedimiento aislado de AD Forest Recovery, cuentas break-glass en Entra con FIDO2 y políticas de Acceso Condicional exportadas como código.", "PROHIBIDO restaurar controladores desde imágenes con persistencia previa o reutilizar KRBTGT comprometido (CT-03 · K33, K34)."),
        ("4. Procesos Asistidos por IA y Agentes", "Desacople selectivo en Entra Agent ID / Agent 365 / Copilot Studio / Foundry (PB-07) y transición inmediata a flujo determinista o manual.", "PROHIBIDO depender de un agente de IA en un proceso crítico sin ruta degradada sin IA probada anualmente (CT-21 · K29, K56)."),
    ]
    sw = 432
    sgap = 16
    for i, (st, scap, slim) in enumerate(scols):
        sx = 72 + i * (sw + sgap)
        parts.append(f'<rect x="{sx}" y="814" width="{sw}" height="298" rx="9" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(f'<rect x="{sx}" y="814" width="{sw}" height="36" rx="9" fill="#1E3A5F"/>')
        parts.append(f'<text x="{sx + sw/2:.1f}" y="837" font-family="{FONT}" font-size="12.4" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(st)}</text>')
        parts.append(svg_text_block(sx + 14, 870, scap, sw - 28, 11.6, "#1E293B", False, 1.26, 5))
        parts.append(f'<rect x="{sx+12}" y="990" width="{sw-24}" height="110" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1" stroke-dasharray="4,2"/>')
        parts.append(svg_text_block(sx + 20, 1012, slim, sw - 40, 11.2, "#7F1D1D", True, 1.24, 4))

    return base_shell(
        6,
        "Procesos de Custodia Forense (SHA-256) y Recuperación en Zona Limpia",
        "Coordinación simultánea entre preservación probatoria admisible (Pista A) y restitución confiable dentro de RTO/RPO (Pista B)",
        "Doble Pista Secuencial + 4 Ámbitos MS",
        "Guías 06 y 07 · Libro 02 · F2 y F4",
        "\n".join(parts),
    )


# ==============================================================================
# RR-07: COMUNICACIONES DE CRISIS, PRUEBAS ANUALES (E1-E3) Y FORMULARIOS F1-F8
# ==============================================================================
def build_rr07() -> str:
    parts = []

    # Top-Left: Crisis Communications (5 Steps + 8 Audiences)
    parts.append(card(48, 136, 900, 518))
    parts.append(f'<text x="68" y="164" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">PROCESO DE COMUNICACIONES DE CRISIS (GUÍA 08 · DD12/DD13 · F5)</text>')
    parts.append(f'<text x="68" y="185" font-family="{FONT}" font-size="11.8" fill="#991B1B" font-weight="700">Regla crítica: No existen plazos universales ("72h") sin ley/contrato confirmado por Legal; prohibido reenviar la misma nota a todos.</text>')

    csteps = [
        ("1. Ficha CI", "Hechos UTC vs hipótesis."),
        ("2. Matriz Legal", "Jurisdicción y reloj real."),
        ("3. Versión Exacta", "Adaptada por audiencia."),
        ("4. Canal Seguro", "Doble chequeo y envío manual."),
        ("5. Corrección", "Nueva versión sin borrar."),
    ]
    for i, (ch, cd) in enumerate(csteps):
        cx = 68 + i * (158 + 17)
        parts.append(f'<rect x="{cx}" y="198" width="158" height="64" rx="7" fill="#EFF6FF" stroke="#60A5FA" stroke-width="1.2"/>')
        parts.append(f'<text x="{cx+10}" y="220" font-family="{FONT}" font-size="11.6" font-weight="700" fill="#1E3A8A">{esc(ch)}</text>')
        parts.append(svg_text_block(cx + 10, 239, cd, 138, 10.6, "#334155", False, 1.18, 2))
        if i < 4:
            parts.append(arrow_h(cx + 160, 230, cx + 173, "#2563EB"))

    auds = [
        ("Empleados y Respuesta", "Rutas seguras y canal alternativo (sin IOCs sensibles).", "Gate: CI + Seguridad + RR. HH."),
        ("Dirección y Directorio", "Impacto en funciones, RTO/RPO y decisiones requeridas.", "Gate: CI + Negocio + Legal + Gob."),
        ("Inversionistas y Mercado", "Solo hechos materiales exigibles según jurisdicción.", "Gate: Legal + Rel. Inversores + CEO"),
        ("Prensa y Público", "Portavoz único; hechos confirmados sin especular rescate.", "Gate: CEO (DD13) + Legal + Comms"),
        ("Fuerzas de la Ley / CERT", "Canal oficial, evidencia autorizada y número de caso.", "Gate: Legal + Custodio Forense + CI"),
        ("Reguladores / Privacidad", "Categorías afectadas y medidas; etiquetar lo desconocido.", "Gate: Legal/Privacidad (DD12)"),
        ("Socios y Proveedores", "Suspensión/reingreso de integraciones y contratos.", "Gate: CI + Dueño del Tercero + Legal"),
        ("Clientes y Titulares", "Servicios/datos afectados, acciones de protección y soporte.", "Gate: Negocio + Legal + Comms"),
    ]
    for idx, (aname, aneed, agate) in enumerate(auds):
        col_i = idx % 2
        row_i = idx // 2
        ax = 68 + col_i * (422 + 16)
        ay = 274 + row_i * 92
        parts.append(f'<rect x="{ax}" y="{ay}" width="422" height="84" rx="7" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.1"/>')
        parts.append(f'<text x="{ax+12}" y="{ay+22}" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#0F172A">{esc(aname)}</text>')
        parts.append(svg_text_block(ax + 12, ay + 41, aneed, 398, 11.1, "#334155", False, 1.2, 2))
        parts.append(f'<text x="{ax+12}" y="{ay+74}" font-family="{FONT}" font-size="10.8" font-weight="700" fill="#0284C7">{esc(agate)}</text>')

    # Top-Right: Annual Execution Tests E1, E2, E3 (Guide 09)
    rx = 968
    parts.append(card(rx, 136, 904, 518))
    parts.append(f'<text x="{rx+22}" y="164" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">PROGRAMA MÍNIMO DE ENSAYOS ANUALES Y EVALUACIÓN SIN PISTAS (GUÍA 09 · F6)</text>')

    tests = [
        ("E1 · EJERCICIO INTEGRADO MULTI-ROL (>= 1 VEZ / AÑO)", "GATE",
         "Participan CI, SOC, Identidad, Plataforma, Backup, Negocio, Forense, Legal y Comunicaciones con 6 inyecciones en orden variable: cuenta privilegiada + ceguera parcial, ataque a copias, posible exfiltración, cifrado + caída de correo, presión de prensa/regulador y restauración con identidad original sospechosa."),
        ("E2 · RESTAURACIÓN TÉCNICA EXTREMO A EXTREMO POR FUNCIÓN CRÍTICA", "OK",
         "Obligatoria cada 12 meses para cada servicio crítico/Tier-0 del BIA: reconstruye identidad/red, configuración, aplicación, datos y transacción real de negocio en zona autorizada, demostrando tiempo real <= RTO y pérdida <= RPO. Un 'backup job exitoso' NO acredita E2."),
        ("E3 · AISLAMIENTO, REPUDIO, CUSTODIA SHA-256 Y COMUNICACIÓN SIMULADA", "PURP",
         "Aísla objetivo benigno, revoca sesión en laboratorio, comprueba cese efectivo y reversión, adquiere evidencia con hash y transferencia a otro operador, y aprueba borradores para audiencias distintas con reloj legal simulado (cero envíos reales a terceros)."),
    ]
    for i, (th, tk, td) in enumerate(tests):
        ty = 180 + i * 118
        parts.append(f'<rect x="{rx+22}" y="{ty}" width="860" height="108" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(badge(rx + 34, ty + 10, 460, 24, th, tk, 10.8))
        parts.append(svg_text_block(rx + 34, ty + 48, td, 836, 11.4, "#1E293B", False, 1.24, 4))

    parts.append(f'<rect x="{rx+22}" y="538" width="860" height="102" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.4" stroke-dasharray="4,2"/>')
    parts.append(f'<text x="{rx+36}" y="562" font-family="{FONT}" font-size="12.8" font-weight="700" fill="#991B1B">RÚBRICA ESTRICTA DE APROBACIÓN INDIVIDUAL (HOJA COMPETENCIAS · K12, K16)</text>')
    parts.append(svg_text_block(rx + 36, 584, "Cada titular Y suplente crítico debe demostrar su tarjeta de rol SIN indicaciones del facilitador. No existe 'aprobada con reservas': si falla un criterio esencial o falta el suplente, se registra Fallida / Incompleta con responsable y fecha obligatoria de retest.", 832, 11.4, "#7F1D1D", False, 1.26, 3))

    # Bottom: Out-of-Band Forms F1-F8 + 3 Workbooks & 3 HTML Viewers
    parts.append(card(48, 670, 1824, 458))
    parts.append(f'<text x="72" y="698" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59">HERRAMIENTAS OPERATIVAS FUERA DE BANDA: FORMULARIOS F1–F8, 3 LIBROS EXCEL Y 3 VISORES LOCALES</text>')

    forms = [
        ("F1 · Apertura y Triage", "INC-ID, UTC triple, hechos EV-ID, señales DE-* y aviso CI."),
        ("F2 · BIA y Contingencia", "RTO/RPO, punto degradado, numeración manual y retorno."),
        ("F3 · Orden Contención", "PB-ID, DD10..18, impacto, autorizador, reversión y efecto."),
        ("F4 · Cadena de Custodia", "EV-ID, SHA-256, depósito restringido, hold y transferencias."),
        ("F5 · Mensaje y Aprobación", "Audiencia, reloj legal validado, texto exacto y acuse."),
        ("F6 · Evaluación / Ejercicio", "Alcance E1–E3, cronología UTC, brechas y fecha de retest."),
        ("F7 · Relevo de Turno", "Sale/entra UTC, contenciones activas, RTO restante y pendientes."),
        ("F8 · Práctica Segura Ninja", "Etiqueta [LAB]/[SOLO-PROD], report-only, PIM y tope SCU."),
    ]
    for i, (fh, fd) in enumerate(forms):
        col_i = i % 4
        row_i = i // 4
        fx = 72 + col_i * (274 + 14)
        fy = 716 + row_i * 102
        parts.append(f'<rect x="{fx}" y="{fy}" width="274" height="90" rx="8" fill="#F8FAFC" stroke="#94A3B8" stroke-width="1.2"/>')
        parts.append(f'<text x="{fx+12}" y="{fy+25}" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#0F2C59">{esc(fh)}</text>')
        parts.append(svg_text_block(fx + 12, fy + 46, fd, 250, 11.2, "#334155", False, 1.22, 3))

    parts.append('<rect x="72" y="924" width="1138" height="186" rx="8" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1.2"/>')
    parts.append(f'<text x="90" y="950" font-family="{FONT}" font-size="13.2" font-weight="700" fill="#1E3A8A">LOS 3 LIBROS EXCEL OPERATIVOS DEL PAQUETE (FUENTE DE REGISTRO ESTRUCTURADO)</text>')
    wbs_txt = [
        "• Libro 01 (01-Evaluacion-y-controles.xlsx): Hojas BIA, Controles (CT-01..21), Evaluaciones trimestrales y Plan de brechas.",
        "• Libro 02 (02-Operacion-y-pruebas.xlsx): Hojas Detecciones, Incidentes, Decisiones (DD##), Evidencia, Comunicaciones, Pruebas y Competencias.",
        "• Libro 03 (03-Correlacion-Prioridades-FullMS-Ninja.xlsx): Hojas Prioridades_Sector_365, Matriz_Controles_360, Matriz_SOC_IR_360 y Rutas_Ninja_Roles.",
    ]
    for i, wt in enumerate(wbs_txt):
        parts.append(svg_text_block(90, 976 + i * 42, wt, 1102, 11.8, "#1E293B", False, 1.22, 2))

    parts.append('<rect x="1228" y="716" width="620" height="394" rx="8" fill="#FFFBEB" stroke="#F59E0B" stroke-width="1.4"/>')
    parts.append(f'<text x="1248" y="744" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#92400E">3 VISORES HTML Y LÍMITES DE SEGURIDAD DEL KIT</text>')
    html_items = [
        ("Panel-de-resiliencia.html", "Consulta filtrable de controles CT-01..21 y BIA por fase CISO 365, pregunta del Directorio (Q1–Q6) y capa Microsoft."),
        ("Consola-de-incidente.html", "Bitácora local fuera de banda durante ejercicios o incidentes para estructurar DD##, PB-01..07 y notas exportables."),
        ("Mapa-de-correlacion-y-prioridades.html", "Cruza sector industrial, horizonte 365, arquitectura Full Microsoft y calculadora de horas Ninja por rol."),
        ("Límite estricto de operación:", "Los HTML NO ejecutan aislamientos ni envían avisos. Prohibido guardar incidentes reales, contactos o secretos en Git."),
    ]
    for i, (hh, hd) in enumerate(html_items):
        hy = 766 + i * 84
        parts.append(f'<text x="1248" y="{hy}" font-family="{FONT}" font-size="12.2" font-weight="700" fill="#78350F">{esc(hh)}</text>')
        parts.append(svg_text_block(1248, hy + 20, hd, 580, 11.3, "#451A03", i == 3, 1.22, 3))

    return base_shell(
        7,
        "Comunicaciones de Crisis, Ensayos Anuales (E1–E3) y Formularios F1–F8",
        "Control de mensajes por audiencia sin plazos supuestos, validación práctica sin pistas y artefactos listos para operar fuera de banda",
        "Flujo de Aprobación + Ensayos + Kit Operativo",
        "Guías 08, 09 y 12 · README · Libros 01–03",
        "\n".join(parts),
    )


# ==============================================================================
# RR-08: ARQUITECTURA 12 CAPAS FULL MICROSOFT, 9 ROLES NINJA Y SECTORES
# ==============================================================================
def build_rr08() -> str:
    parts = []

    # Left: 12 Operational Layers Full Microsoft (MS-CAP-01..12)
    parts.append(card(48, 136, 1044, 992))
    parts.append(f'<text x="68" y="164" font-family="{FONT}" font-size="15.2" font-weight="700" fill="#0F2C59">ARQUITECTURA OPERATIVA FULL MICROSOFT EN 12 CAPAS (MS-CAP-01 A MS-CAP-12 · GUÍA 14)</text>')

    mcols = [
        ("Capa y Productos Clave", 344),
        ("Dueño y Controles", 232),
        ("Límite Operativo Crítico a Gobernar", 418),
    ]
    cx = 68
    for mt, mw in mcols:
        parts.append(f'<rect x="{cx}" y="176" width="{mw}" height="32" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + mw/2:.1f}" y="197" font-family="{FONT}" font-size="11.8" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(mt)}</text>')
        cx += mw + 4

    caps = [
        ("MS-CAP-01 · Identidad Zero Trust (Entra P2 + GSA)", "Identidad · PB-02/05 · CT-03/04/07", "CAE no revoca cookies propias de apps 3P sin proxy o baja."),
        ("MS-CAP-02 · Gobierno Privilegiado, Workload ID y LAPS", "Identidad/GRC · CT-04/08/17/18", "Workload ID Premium se licencia aparte; priorizar críticas."),
        ("MS-CAP-03 · Endpoints, DVM, Exposure Mgmt e Intune", "Endpoints/SOC · PB-01 · CT-01/05/06", "Host desconectado no aísla hasta reconectar; wipe borra evidencia."),
        ("MS-CAP-04 · Seguridad AD Híbrido (MDI v3.x)", "IdP Híbrida/SOC · PB-02 · CT-03/04", "Exige sensores sanos en todos los DCs/ADFS/ADCS y Forest Recovery."),
        ("MS-CAP-05 · Correo y Colaboración (MDO P2)", "Colaboración · PB-01/04 · CT-09/12", "Medir reporte temprano K11 sin castigos que oculten clics."),
        ("MS-CAP-06 · Nube Híbrida, Servers P2, Storage y OT", "Cloud/OT · PB-01/03/05 · CT-05..08", "Facturación por consumo Azure; verificar cobertura real en Arc."),
        ("MS-CAP-07 · Defender XDR + Attack Disruption + MDA", "SOC/IR · PB-01/02/04/05 · CT-11..13", "Attack Disruption frena avance, pero no sustituye erradicar raíz."),
        ("MS-CAP-08 · Microsoft Sentinel + Azure Logic Apps SOAR", "Ing. SOC · PB-01..07 · CT-11..14", "Aislamientos críticos exigen aprobación humana DD11; cuidar ingesta."),
        ("MS-CAP-09 · Security Copilot (SOC Asistido/Agéntico)", "Líder SOC · PB-01/02/07 · CT-12/21", "Gobernar costo por hora de SCU y validar todo borrador ejecutivo."),
        ("MS-CAP-10 · Purview MIP + DLP + Insider Risk + SAM", "Datos/SOC · PB-04/07 · CT-10/19/21", "MD/HTML/CSV locales no heredan RMS; calibrar DLP en simulación."),
        ("MS-CAP-11 · Purview Audit Premium + eDiscovery + GRC", "Legal/Forense · PB-04 · CT-14/16/17", "Activar Audit Premium antes del ataque (no es retroactivo)."),
        ("MS-CAP-12 · Azure Backup MUA + M365 Backup + Agent 365", "Infra/BCP/IA · PB-03/07 · CT-02/15/21", "Resource Guard en otra suscripción y modo sin IA probado (K56)."),
    ]
    for idx, (c_name, c_own, c_lim) in enumerate(caps):
        ry = 214 + idx * 75
        bg = "#EFF6FF" if idx in (0, 6, 7, 11) else ("#F8FAFC" if idx % 2 == 1 else "#FFFFFF")
        parts.append(f'<rect x="68" y="{ry}" width="1002" height="69" rx="6" fill="{bg}" stroke="#CBD5E1" stroke-width="1"/>')
        parts.append(svg_text_block(78, ry + 23, c_name, 324, 11.4, "#0F172A", True, 1.22, 2))
        parts.append(svg_text_block(424, ry + 23, c_own, 214, 11.1, "#1E3A8A", False, 1.22, 2))
        parts.append(svg_text_block(660, ry + 23, c_lim, 398, 11.2, "#7F1D1D", False, 1.22, 2))

    # Right-Top: 9 Operational Roles & Ninja Training Sizing (Guide 15)
    rx = 1112
    parts.append(card(rx, 136, 760, 608))
    parts.append(f'<text x="{rx+20}" y="164" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">RESPONSABLES TÉCNICOS Y DOTACIÓN NINJA (ROL-01..09 · K16)</text>')
    parts.append(badge(rx + 20, 174, 720, 24, "1.572 h (1 Titular/Rol) · 3.144 h (Dupla Titular + Suplente en 12 meses · 15 Programas NT-01..15)", "INFO", 10.8))

    r9 = [
        ("ROL-01 · SOC y Detección", "81h / 90h / 72h", "243h (486h par)", "NT-01, NT-02, NT-04 · DE-01..13"),
        ("ROL-02 · Comandante (CI) / CISO", "42h / 43h / 45h", "130h (260h par)", "NT-02, NT-03, NT-11, NT-13 · DD10..14"),
        ("ROL-03 · Identidad y Acceso No Humano", "58h / 116h / 47h", "221h (442h par)", "NT-03, NT-02 · PB-02/05/07"),
        ("ROL-04 · Endpoints, Red y Exposición", "52h / 91h / 32h", "175h (350h par)", "NT-02, NT-14, NT-03 · PB-01"),
        ("ROL-05 · Respaldos y Recuperación", "40h / 49h / 41h", "130h (260h par)", "NT-14, NT-09, NT-15 · PB-03 / E2"),
        ("ROL-06 · Negocio, BCP y Dueños Riesgo", "18h / 20h / 27h", "65h (130h par)", "NT-11, NT-05, NT-13 · BIA / RTO"),
        ("ROL-07 · Datos, DLP y Forense", "58h / 87h / 63h", "208h (416h par)", "NT-05..07, NT-10, NT-12 · PB-04"),
        ("ROL-08 · Legal, GRC y Comunicaciones", "30h / 53h / 22h", "105h (210h par)", "NT-08, NT-10, NT-11 · DD12/13"),
        ("ROL-09 · Arquitectura y Gobierno IA", "70h / 134h / 91h", "295h (590h par)", "NT-13, NT-15, NT-12, NT-03 · PB-07"),
    ]
    for idx, (rn, rolas, rtot, rprog) in enumerate(r9):
        ry = 208 + idx * 58
        bg = "#F8FAFC" if idx % 2 == 1 else "#FFFFFF"
        parts.append(f'<rect x="{rx+18}" y="{ry}" width="724" height="52" rx="6" fill="{bg}" stroke="#CBD5E1" stroke-width="1"/>')
        parts.append(f'<text x="{rx+28}" y="{ry+20}" font-family="{FONT}" font-size="11.8" font-weight="700" fill="#0F172A">{esc(rn)}</text>')
        parts.append(f'<text x="{rx+28}" y="{ry+39}" font-family="{FONT}" font-size="10.8" fill="#475569">Olas 1/2/3: {esc(rolas)} · {esc(rprog)}</text>')
        parts.append(badge(rx + 566, ry + 13, 166, 24, rtot, "OK" if idx in (0, 2, 8) else "NEUTRAL", 10.6))

    # Right-Bottom: 6 Sectors + 6 Board Questions (Q1-Q6)
    parts.append(card(rx, 760, 760, 368))
    parts.append(f'<text x="{rx+20}" y="788" font-family="{FONT}" font-size="14.8" font-weight="700" fill="#0F2C59">PRIORIZACIÓN SECTORIAL Y LAS 6 PREGUNTAS DEL DIRECTORIO (Q1–Q6)</text>')

    sects = [
        ("LOG · Logística:", "Corte EDI/API socios (K31), modo manual numerado (K29) y sin IA (K56)."),
        ("OYG · Oil & Gas:", "Segmentación TI/OT (K36/K40), accesos remotos y seguridad física."),
        ("IND · Industrial:", "Continuidad planta OEE + resguardo IP/diseños (K37) y MES/ERP WORM."),
        ("FIN · Financiero:", "Doble extorsión 24x7, MTTC horas, aviso supervisor (K61) y agentes IA."),
        ("GOB · Gobierno:", "MFA fuerte (K33), copias aisladas (K28/30) y evidencia auditable (K57)."),
        ("ELE · Eléctrico:", "Aislar DCS/SCADA de TI/OEM (K36/40), cero admin fijo y modo sin IA."),
    ]
    for i, (sk, sv) in enumerate(sects):
        sy = 808 + i * 51
        parts.append(f'<rect x="{rx+18}" y="{sy}" width="424" height="45" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>')
        parts.append(f'<text x="{rx+28}" y="{sy+18}" font-family="{FONT}" font-size="11.2" font-weight="700" fill="#0F2C59">{esc(sk)}</text>')
        parts.append(svg_text_block(rx + 28, sy + 34, sv, 404, 10.6, "#334155", False, 1.15, 1))

    qs = [
        ("Q1 · ¿Nivel real de riesgo?", "K25, K26, K46, K33, K39"),
        ("Q2 · ¿Estamos mejorando?", "K22, K18, K60, K42, K45"),
        ("Q3 · ¿Invertimos bien?", "K17, K19, K20, K12"),
        ("Q4 · ¿Listos ante crisis?", "K30, K28, K15, K32, K31"),
        ("Q5 · ¿Riesgo con evidencia?", "K09, K14, K58, K57, K50"),
        ("Q6 · ¿Cumplimos promesa?", "KSG01..06, K02, K01"),
    ]
    for i, (qk, qv) in enumerate(qs):
        qy = 808 + i * 51
        parts.append(f'<rect x="{rx+452}" y="{qy}" width="290" height="45" rx="6" fill="#EFF6FF" stroke="#93C5FD" stroke-width="1"/>')
        parts.append(f'<text x="{rx+462}" y="{qy+18}" font-family="{FONT}" font-size="11.2" font-weight="700" fill="#1E3A8A">{esc(qk)}</text>')
        parts.append(f'<text x="{rx+462}" y="{qy+35}" font-family="{FONT}" font-size="10.6" font-weight="600" fill="#334155">{esc(qv)}</text>')

    return base_shell(
        8,
        "Operación Full Microsoft (12 Capas), Dotación de 9 Roles y Sectores",
        "Traducción tecnológica diaria y trimestral, dimensionamiento formativo titular+suplente (3.144 h) y foco por industria",
        "Arquitectura 12 Capas + Roles + Sectores",
        "Guías 13, 14 y 15 · Libro 03 (Correlación 360)",
        "\n".join(parts),
    )


SERIES_SPECS = [
    ("RR-01_Mapa_Maestro_Ciclo_y_Fases_365", "Fases del Programa: Ciclo Operativo, 3 Olas e Hitos de 365 Días", build_rr01),
    ("RR-02_Gobierno_Roles_Autoridad_y_Activacion", "Gobierno, Responsables y Derechos de Decisión en Crisis (DD##)", build_rr02),
    ("RR-03_Catalogo_21_Controles_y_Escala_Evidencia", "Tareas de Preparación: Los 21 Controles (CT-01..21) y su Evidencia", build_rr03),
    ("RR-04_Proceso_Monitoreo_13_Detecciones_y_Triage", "Proceso de Monitoreo, 13 Detecciones (DE-01..13) y Triage SOC", build_rr04),
    ("RR-05_Proceso_Contencion_Playbooks_y_Revocacion", "Proceso de Contención, Playbooks (PB-01..07) y Superficies de Revocación", build_rr05),
    ("RR-06_Proceso_Forense_Continuidad_y_Recuperacion", "Procesos de Custodia Forense (SHA-256) y Recuperación en Zona Limpia", build_rr06),
    ("RR-07_Proceso_Comunicaciones_Pruebas_y_Formularios", "Comunicaciones de Crisis, Ensayos Anuales (E1–E3) y Formularios F1–F8", build_rr07),
    ("RR-08_Arquitectura_Full_Microsoft_y_Dotacion_Roles", "Operación Full Microsoft (12 Capas), Dotación de 9 Roles y Sectores", build_rr08),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mirror-dir", type=str, default="", help="Optional preview mirror directory")
    args = parser.parse_args()
    mirror_dir = pathlib.Path(args.mirror_dir) if args.mirror_dir else None

    for d in (SVG_DIR, PNG_DIR, JPG_DIR):
        d.mkdir(parents=True, exist_ok=True)
    if mirror_dir:
        mirror_dir.mkdir(parents=True, exist_ok=True)

    svg_paths = []
    for slug, title, builder in SERIES_SPECS:
        svg_content = builder()
        svg_path = SVG_DIR / f"{slug}.svg"
        svg_path.write_text(svg_content, encoding="utf-8")
        if mirror_dir:
            shutil.copy2(svg_path, mirror_dir / f"{slug}.svg")
        svg_paths.append((slug, title, svg_path))
        print(f"Wrote SVG: {svg_path.name} ({len(svg_content)} chars)")

    if TRUNCATION_WARNINGS:
        print(f"TRUNCATION WARNINGS ({len(TRUNCATION_WARNINGS)}):")
        for w in TRUNCATION_WARNINGS:
            print(" ", w)
    else:
        print("ZERO text truncations across all 8 infographics!")

    edge_candidates = [
        pathlib.Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        pathlib.Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    edge_path = next((str(p) for p in edge_candidates if p.exists()), None)

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=edge_path, headless=True) if edge_path else p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=2)
        page = context.new_page()

        for slug, title, svg_path in svg_paths:
            page.goto(svg_path.as_uri(), wait_until="load")
            page.wait_for_timeout(150)
            png_path = PNG_DIR / f"{slug}.png"
            jpg_path = JPG_DIR / f"{slug}.jpg"
            page.screenshot(path=str(png_path), type="png", full_page=False)

            with Image.open(png_path) as im:
                rgb = im.convert("RGB")
                rgb.save(jpg_path, format="JPEG", quality=95, subsampling=0, optimize=True)

            if mirror_dir:
                shutil.copy2(png_path, mirror_dir / f"{slug}.png")
                shutil.copy2(jpg_path, mirror_dir / f"{slug}.jpg")
            print(f"Rendered 4K PNG & JPG: {slug} ({png_path.stat().st_size // 1024} KB PNG / {jpg_path.stat().st_size // 1024} KB JPG)")

        browser.close()

    cards_html = []
    for slug, title, _ in svg_paths:
        cards_html.append(f"""
        <section style="background:#fff;border:1px solid #cbd5e1;border-radius:12px;padding:20px;margin-bottom:28px;box-shadow:0 2px 8px rgba(15,23,42,0.06)">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
            <h2 style="margin:0;font-size:18px;color:#0f2c59">{esc(slug.replace('_', ' '))} — {esc(title)}</h2>
            <div style="display:flex;gap:10px;font-size:13px;font-weight:600">
              <a href="svg/{slug}.svg" target="_blank" style="color:#0284c7;text-decoration:none;padding:5px 12px;border:1px solid #0284c7;border-radius:6px">Abrir SVG Vectorial</a>
              <a href="png/{slug}.png" target="_blank" style="color:#166534;text-decoration:none;padding:5px 12px;border:1px solid #16a34a;border-radius:6px">Abrir PNG 4K (3840×2400)</a>
              <a href="jpg/{slug}.jpg" target="_blank" style="color:#7c2d12;text-decoration:none;padding:5px 12px;border:1px solid #ea580c;border-radius:6px">Abrir JPG Alta Calidad</a>
            </div>
          </div>
          <img src="svg/{slug}.svg" alt="{esc(title)}" style="width:100%;height:auto;border-radius:8px;border:1px solid #e2e8f0"/>
        </section>""")

    gallery_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8"/>
  <title>Serie de Infografías: Resiliencia ante Ransomware v2.0</title>
</head>
<body style="font-family:'Segoe UI',Inter,Arial,sans-serif;background:#f1f5f9;color:#0f172a;margin:0;padding:32px">
  <div style="max-width:1440px;margin:0 auto">
    <header style="background:#091e3a;color:#fff;padding:28px 32px;border-radius:14px;margin-bottom:28px">
      <h1 style="margin:0 0 8px 0;font-size:26px">Serie de 8 Infografías: Programa Operativo de Resiliencia ante Ransomware (v2.0)</h1>
      <p style="margin:0;color:#bae6fd;font-size:15px">24 archivos generados (8 SVG vectoriales 1920×1200 + 8 PNG Retina 3840×2400 + 8 JPG 3840×2400) — Fases, Tareas, Responsables, Procesos Críticos y Arquitectura Full Microsoft.</p>
    </header>
    {''.join(cards_html)}
  </div>
</body>
</html>"""
    (OUT_DIR / "Galeria_Serie_Infografias_Resiliencia_Ransomware_v2.html").write_text(gallery_html, encoding="utf-8")
    print("Portable HTML gallery written successfully.")


if __name__ == "__main__":
    main()

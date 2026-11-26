import html
import json
import pathlib
import shutil
from PIL import Image
from playwright.sync_api import sync_playwright

BASE_DIR = pathlib.Path(r"C:\Users\scavanna\OneDrive - Microsoft\AB - SOAR LogicApps\Analisis_Competitivo_Agentic_SOC_Nov2026")
PERSIST_DIR = BASE_DIR / "persistencia"
INFOG_DIR = BASE_DIR / "infografias"
SVG_DIR = INFOG_DIR / "svg"
PNG_DIR = INFOG_DIR / "png"
JPG_DIR = INFOG_DIR / "jpg"
SCOUT_PREVIEW_DIR = pathlib.Path(r"C:\Users\scavanna\OneDrive - Microsoft\Documents\Microsoft Scout\infografias_agentic_soc_nov2026")
SESSION_FILES = pathlib.Path(r"C:\Users\scavanna\.scout\copilot\session-state\df4febd6-1b1d-4459-95e6-ab0898615c9a\files\infografias")

for d in (SVG_DIR, PNG_DIR, JPG_DIR, SCOUT_PREVIEW_DIR, SESSION_FILES):
    d.mkdir(parents=True, exist_ok=True)

comp_data = json.loads((PERSIST_DIR / "03_competidores_12_enterprise_nov2026.json").read_text(encoding="utf-8"))

W, H = 1920, 1200
FONT = "Segoe UI, Inter, -apple-system, Arial, sans-serif"


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def wrap_text(text: str, max_px: float, font_size: float, bold: bool = False, max_lines: int = 10) -> list[str]:
    char_w = font_size * (0.57 if bold else 0.52)
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
    font_size: float = 14,
    fill: str = "#1E293B",
    bold: bool = False,
    line_height: float = 1.32,
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


def badge(x: float, y: float, w: float, h: float, label: str, kind: str = "GA", font_size: float = 12) -> str:
    styles = {
        "GA": ("#DCFCE7", "#16A34A", "#14532D"),
        "PREV": ("#FEF9C3", "#CA8A04", "#713F12"),
        "EA": ("#FFEDD5", "#EA580C", "#7C2D12"),
        "ROAD": ("#FEE2E2", "#DC2626", "#7F1D1D"),
        "INFO": ("#E0F2FE", "#0284C7", "#0C4A6E"),
        "MS": ("#DBEAFE", "#2563EB", "#1E3A8A"),
        "NEUTRAL": ("#F1F5F9", "#94A3B8", "#334155"),
    }
    bg, stroke, fg = styles.get(kind, styles["NEUTRAL"])
    dash = ' stroke-dasharray="4,2"' if kind in ("ROAD", "EA") else ""
    ty = y + h * 0.68
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2:.1f}" fill="{bg}" stroke="{stroke}" stroke-width="1.4"{dash}/>'
        f'<text x="{x + w/2:.1f}" y="{ty:.1f}" font-family="{FONT}" font-size="{font_size}" font-weight="700" fill="{fg}" text-anchor="middle">{esc(label)}</text>'
    )


def card(x: float, y: float, w: float, h: float, fill: str = "#FFFFFF", stroke: str = "#CBD5E1", rx: float = 12, shadow: bool = True, stroke_w: float = 1.5) -> str:
    flt = ' filter="url(#cardShadow)"' if shadow else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_w}"{flt}/>'


def base_shell(series_num: int, title: str, subtitle: str, archetype: str, body_svg: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="hdrGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0B1F3A"/>
      <stop offset="60%" stop-color="#12345E"/>
      <stop offset="100%" stop-color="#1B4965"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0EA5E9"/>
      <stop offset="50%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#14B8A6"/>
    </linearGradient>
    <linearGradient id="msBarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1D4ED8"/>
      <stop offset="100%" stop-color="#0EA5E9"/>
    </linearGradient>
    <linearGradient id="peerBarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0284C7"/>
    </linearGradient>
    <linearGradient id="tier2BarGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#64748B"/>
    </linearGradient>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect x="0" y="0" width="{W}" height="{H}" fill="#F8FAFC"/>

  <!-- Header -->
  <rect x="0" y="0" width="{W}" height="118" fill="url(#hdrGrad)"/>
  <rect x="0" y="115" width="{W}" height="5" fill="url(#accentGrad)"/>

  <rect x="48" y="18" width="276" height="24" rx="12" fill="#0EA5E9" fill-opacity="0.22" stroke="#38BDF8" stroke-width="1"/>
  <text x="186" y="34" font-family="{FONT}" font-size="12" font-weight="700" fill="#E0F2FE" text-anchor="middle">SERIE AGENTIC SOC · INFOGRAFÍA 0{series_num} DE 07</text>

  <text x="48" y="72" font-family="{FONT}" font-size="27" font-weight="700" fill="#FFFFFF">{esc(title)}</text>
  <text x="48" y="100" font-family="{FONT}" font-size="14.5" font-weight="400" fill="#BAE6FD">{esc(subtitle)}</text>

  <!-- Top-Right Metadata Box -->
  <rect x="1512" y="20" width="360" height="78" rx="10" fill="#0F294A" stroke="#38BDF8" stroke-width="1.2"/>
  <text x="1530" y="46" font-family="{FONT}" font-size="12" font-weight="700" fill="#7DD3FC">CORTE VERIFICADO: 25 NOVIEMBRE 2026</text>
  <text x="1530" y="68" font-family="{FONT}" font-size="12.5" font-weight="600" fill="#FFFFFF">Arquetipo: {esc(archetype)}</text>
  <text x="1530" y="87" font-family="{FONT}" font-size="11.5" font-weight="400" fill="#CBD5E1">12 Fabricantes Enterprise + 6 Especialistas</text>

  <!-- Body -->
  {body_svg}

  <!-- Footer -->
  <rect x="0" y="1144" width="{W}" height="56" fill="#E2E8F0"/>
  <line x1="0" y1="1144" x2="{W}" y2="1144" stroke="#CBD5E1" stroke-width="1.5"/>
  {badge(48, 1158, 118, 26, "[GA] Producción", "GA", 11.5)}
  {badge(176, 1158, 146, 26, "[PREV] Vista Previa", "PREV", 11.5)}
  {badge(332, 1158, 168, 26, "[EA/GATED] Restringido", "EA", 11.5)}
  {badge(510, 1158, 178, 26, "[ACOTADO/ROAD] Límite", "ROAD", 11.5)}
  <text x="1872" y="1176" font-family="{FONT}" font-size="12" font-weight="600" fill="#334155" text-anchor="end">Fuentes: Microsoft Ignite Nov 2026, Microsoft Learn, GitHub Docs y portales técnicos/release notes oficiales de los 12 fabricantes</text>
</svg>"""


# ==============================================================================
# IG-01: RANKING GLOBAL 12 FABRICANTES ENTERPRISE
# ==============================================================================
def build_ig01() -> str:
    parts = []
    kpis = [
        ("12 Fabricantes Enterprise", "Evaluados en 10 dimensiones + 6 especialistas pure-play", "#0284C7"),
        ("97.6 / 100 · Microsoft #1", "+11.2 pts sobre el #2 (PANW 86.5) y +19.8 vs media (77.8)", "#1D4ED8"),
        ("57.1% en GA Productivo", "32 de 56 capacidades auditadas en GA; 42.9% en Preview/EA", "#16A34A"),
        ("40 Fuentes Verificadas", "Navegación directa de docs, changelogs y anuncios a nov-2026", "#0F766E"),
    ]
    for i, (big, sub, col) in enumerate(kpis):
        kx = 48 + i * (438 + 24)
        parts.append(card(kx, 138, 438, 92))
        parts.append(f'<rect x="{kx}" y="138" width="8" height="92" rx="4" fill="{col}"/>')
        parts.append(f'<text x="{kx+24}" y="174" font-family="{FONT}" font-size="22" font-weight="700" fill="#0F172A">{esc(big)}</text>')
        parts.append(svg_text_block(kx + 24, 198, sub, 398, 13, "#475569", False, 1.25, 2))

    # Left Ranking Card
    parts.append(card(48, 248, 1264, 876))
    parts.append(f'<text x="72" y="280" font-family="{FONT}" font-size="17" font-weight="700" fill="#0F2C59">ÍNDICE COMPETITIVO PONDERADO (0–100) Y OFERTA INSIGNIA VERIFICADA A NOVIEMBRE 2026</text>')
    parts.append('<line x1="72" y1="294" x2="1288" y2="294" stroke="#E2E8F0" stroke-width="1.5"/>')

    ranked = [
        ("#1", "Microsoft", "Referencia Full-Stack", 97.6, "0.0", "ISOC + Perception (GA) + Sec. Copilot (+18) + MDASH + GHAS", "ms"),
        ("#2", "Palo Alto Networks", "SOC / SOAR / Red", 86.5, "-11.2", "Cortex XSIAM 3.6 + AgentiX 1.4 (FedRAMP High) + XSOAR 8.15", "p1"),
        ("#3", "Google Cloud + Wiz", "Cloud / SIEM / AppSec", 85.0, "-12.7", "AI Threat Defense + SecOps + CodeMender (Prev) + Wiz Agents", "p1"),
        ("#4", "CrowdStrike", "EDR / Next-Gen SIEM", 81.7, "-15.9", "Falcon SIEM + Fusion SOAR + Charlotte AI + SafeMind", "p1"),
        ("#5", "AWS", "Hyperscaler Cloud / AppSec", 76.0, "-21.6", "AWS Continuum (GA 2 reg. US) + Security Incident Response AI", "p2"),
        ("#5", "SentinelOne", "EDR / Autonomous SOC", 76.0, "-21.6", "Singularity ASOC + Purple AI Investigation + Hyperautomation", "p2"),
        ("#7", "Fortinet", "Red + SOAR Unificado", 75.1, "-22.6", "FortiSOAR 8.0 (>19 agentes + MCP GA) + FortiSOC (Prev)", "p2"),
        ("#8", "Cisco / Splunk", "SIEM Instalado / Red", 74.6, "-23.0", "Splunk ES 8.8 (GA 4-nov) + SOAR HA + Cisco XDR Instant Verif.", "p2"),
        ("#9", "IBM Security", "Híbrido / Riesgo & IA", 74.3, "-23.4", "Autonomous Security (ATOM/ARGO) + watsonx Discover & Contain", "p2"),
        ("#10", "Elastic", "Search SIEM & Workflows", 73.4, "-24.2", "Elastic 9.5 Attack Discovery + Workflows GA + 9.6 AlertZero", "p2"),
        ("#11", "Zscaler", "Zero Trust / Inline SOC", 67.0, "-30.6", "Zscaler Agentic SOC (GA sep-26) + Decoy Mesh + Risk360", "p2"),
        ("#12", "ServiceNow", "Workflow ITSM / Gobierno IA", 65.9, "-31.7", "SecOps SIR + Now Assist + Arc Agent + AI Control Tower", "p2"),
    ]

    bar_x = 344
    bar_max_w = 430.0
    avg_x = bar_x + (77.8 / 100.0) * bar_max_w

    for idx, (rk, name, sub, sc, gap, suite, grp) in enumerate(ranked):
        ry = 304 + idx * 65
        row_bg = "#EFF6FF" if grp == "ms" else ("#F8FAFC" if idx % 2 == 1 else "#FFFFFF")
        row_stroke = "#93C5FD" if grp == "ms" else "#E2E8F0"
        parts.append(f'<rect x="68" y="{ry}" width="1224" height="55" rx="8" fill="{row_bg}" stroke="{row_stroke}" stroke-width="1"/>')

        rk_bg = "#1D4ED8" if grp == "ms" else ("#0284C7" if grp == "p1" else "#64748B")
        parts.append(f'<rect x="80" y="{ry+11}" width="44" height="32" rx="8" fill="{rk_bg}"/>')
        parts.append(f'<text x="102" y="{ry+32}" font-family="{FONT}" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">{rk}</text>')

        parts.append(f'<text x="138" y="{ry+24}" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F172A">{esc(name)}</text>')
        parts.append(f'<text x="138" y="{ry+43}" font-family="{FONT}" font-size="12" font-weight="400" fill="#64748B">{esc(sub)}</text>')

        bw = (sc / 100.0) * bar_max_w
        grad = "url(#msBarGrad)" if grp == "ms" else ("url(#peerBarGrad)" if grp == "p1" else "url(#tier2BarGrad)")
        parts.append(f'<rect x="{bar_x}" y="{ry+14}" width="{bar_max_w}" height="26" rx="6" fill="#E2E8F0"/>')
        parts.append(f'<rect x="{bar_x}" y="{ry+14}" width="{bw:.1f}" height="26" rx="6" fill="{grad}"/>')
        parts.append(f'<text x="{bar_x + bw - 10:.1f}" y="{ry+32}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#FFFFFF" text-anchor="end">{sc:.1f}</text>')

        gap_kind = "MS" if grp == "ms" else ("INFO" if grp == "p1" else "NEUTRAL")
        gap_lbl = "BASE" if grp == "ms" else f"{gap} pts"
        parts.append(badge(788, ry + 14, 84, 26, gap_lbl, gap_kind, 11.5))

        parts.append(svg_text_block(888, ry + 23, suite, 392, 12.5, "#1E293B", grp == "ms", 1.25, 2))

    # Market average dashed line + bottom pill (zero overlap with row #1 or row #12)
    parts.append(f'<line x1="{avg_x:.1f}" y1="299" x2="{avg_x:.1f}" y2="1088" stroke="#DC2626" stroke-width="1.8" stroke-dasharray="5,4"/>')
    parts.append(f'<rect x="{avg_x - 72:.1f}" y="1088" width="144" height="22" rx="11" fill="#FEE2E2" stroke="#DC2626" stroke-width="1.1"/>')
    parts.append(f'<text x="{avg_x:.1f}" y="1103" font-family="{FONT}" font-size="11.5" font-weight="700" fill="#991B1B" text-anchor="middle">Media Mercado: 77.8</text>')

    # Right Synthesis Cards (x=1334, w=538)
    rx = 1334
    # Card 1: 3 Escalones del Mercado
    parts.append(card(rx, 248, 538, 276))
    parts.append(f'<text x="{rx+24}" y="282" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59">ESTRUCTURA EN 3 ESCALONES DEL MERCADO</text>')
    tiers_txt = [
        ("1. Plataforma Integral (>95 pts): Microsoft (97.6)", "Único proveedor con sensores y actuadores nativos en Identidad, Endpoint, Email, Datos, SIEM/Data Lake, Código y SOAR."),
        ("2. Perseguidores Tier-1 (81–87 pts): PANW, Google+Wiz, CS", "Muy fuertes en SOC/Cloud, pero carecen de IdP corporativo propio, suite de productividad/correo o DLP integral."),
        ("3. Especialistas Cloud/SIEM/ITSM (65–76 pts)", "Lideran nichos concretos (AWS Continuum en código, FortiSOAR 8.0 en MCP, ServiceNow en CMDB) pero con puntos ciegos amplios."),
    ]
    for idx_t, (th, td) in enumerate(tiers_txt):
        ty = 312 + idx_t * 68
        parts.append(f'<text x="{rx+24}" y="{ty}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#0F172A">{esc(th)}</text>')
        parts.append(svg_text_block(rx + 24, ty + 19, td, 490, 12.2, "#475569", False, 1.25, 2))

    # Card 2: Señales Competitivas FY27
    parts.append(card(rx, 544, 538, 280))
    parts.append(f'<text x="{rx+24}" y="578" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59">DINÁMICA COMPETITIVA VERIFICADA (OCT–NOV 2026)</text>')
    win_items = [
        ("Tener 'agentes' dejó de ser diferenciador", "En sep–nov 2026 los 12 fabricantes lanzaron ofertas Agentic SOC; el comprador ahora audita qué ven y qué pueden frenar."),
        ("Presión de costos SIEM y 'Platformization'", "CrowdStrike + Dynatrace atacan el costo de Sentinel; Palo Alto empuja migración total hacia XSIAM 3.6 + AgentiX 1.4."),
        ("Convergencia Código-a-SOC", "Microsoft (MDASH+GHAS), Google (CodeMender+Wiz) y AWS (Continuum) llevan la validación con PoC antes del despliegue."),
    ]
    for idx_w, (wh, wd) in enumerate(win_items):
        wy = 608 + idx_w * 70
        parts.append(f'<circle cx="{rx+31}" cy="{wy-5}" r="4.5" fill="#0284C7"/>')
        parts.append(f'<text x="{rx+44}" y="{wy}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#0F172A">{esc(wh)}</text>')
        parts.append(svg_text_block(rx + 44, wy + 19, wd, 470, 12.2, "#475569", False, 1.25, 2))

    # Card 3: Ecosistema Pure-Play Anexo
    parts.append(card(rx, 844, 538, 280, fill="#F0F9FF", stroke="#7DD3FC"))
    parts.append(f'<text x="{rx+24}" y="878" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0C4A6E">6 ESPECIALISTAS PURE-PLAY TAMBIÉN AUDITADOS</text>')
    sp_lines = [
        "• Torq (Socrates + Agentic Builder): HyperSOC no-code ($1.2B val).",
        "• Swimlane Turbine: MCP bidireccional GA (28-oct-2026) + Hero AI.",
        "• Snyk Evo (ADS + COS): gobierna MCPs/skills y valida código IA.",
        "• Okta Blueprint Alliance: Agent SSO; kill switch aún planeado.",
        "• SailPoint Agentic Fabric: identidad máquina; kill switch en Preview.",
        "• OpenAI GPT-6 Cyber & Anthropic Cyber Mission: modelos gated.",
    ]
    for idx_s, sl in enumerate(sp_lines):
        parts.append(f'<text x="{rx+24}" y="{910 + idx_s*34}" font-family="{FONT}" font-size="11.8" font-weight="600" fill="#0F172A">{esc(sl)}</text>')

    return base_shell(
        1,
        "Microsoft Lidera el Benchmark Agentic SOC Enterprise (97.6 vs. 77.8 Media)",
        "Evaluación cuantitativa ponderada en 10 dimensiones técnicas y operativas sobre los 12 fabricantes líderes al 25 de noviembre de 2026",
        "Ranking Cuantitativo + Grupos",
        "\n".join(parts),
    )


# ==============================================================================
# IG-02: ARQUITECTURA MICROSOFT 6 PLANOS SIN SOLAPAMIENTOS
# ==============================================================================
def build_ig02() -> str:
    parts = []
    lx = 48
    lw = 1310

    # Layer 1: Perception (y=142, h=208)
    parts.append(card(lx, 142, lw, 208, fill="#FFFFFF", stroke="#2563EB", stroke_w=2))
    parts.append(f'<rect x="{lx}" y="142" width="{lw}" height="40" rx="10" fill="#1E3A8A"/>')
    parts.append(f'<text x="{lx+20}" y="168" font-family="{FONT}" font-size="16" font-weight="700" fill="#FFFFFF">PLANO 2 · ORQUESTACIÓN MULTI-AGENTE POR OUTCOMES: MICROSOFT PERCEPTION</text>')
    parts.append(badge(lx + lw - 200, 149, 182, 26, "[GA] Plataforma 17-Nov", "GA", 11.5))

    teams = [
        ("RED TEAM · Simular y Exponer", "#FEF2F2", "#EF4444", "#991B1B", [
            ("Recon Agent", "GA", "Mapea rutas de ataque, activos críticos y permisos excesivos."),
            ("Web App Pen Test", "PREV", "Pentest dinámico web (31% Incalmo); consume hallazgos MDASH."),
        ]),
        ("BLUE TEAM · Detectar e Investigar", "#EFF6FF", "#3B82F6", "#1E3A8A", [
            ("Alert Triage & Attack Inv.", "GA", "Cubre ~80% de cola Defender; reconstruye ataque + AWS/Okta."),
            ("Detection Authoring & TI", "GA", "Traduce inteligencia externa en KQL probado contra histórico."),
        ]),
        ("GREEN TEAM · Priorizar y Remediar", "#F0FDF4", "#22C55E", "#14532D", [
            ("Posture Prioritization", "GA", "Prioriza riesgo explotable real en Microsoft, AWS y GCP."),
            ("Risk Reduction & Identity", "PREV", "Coordina parches Intune, WAF Front Door y Vuln. Shielding."),
        ]),
    ]
    for i, (t_title, t_bg, t_st, t_fg, items) in enumerate(teams):
        tx = lx + 18 + i * (418 + 10)
        parts.append(f'<rect x="{tx}" y="192" width="418" height="146" rx="8" fill="{t_bg}" stroke="{t_st}" stroke-width="1.3"/>')
        parts.append(f'<text x="{tx+14}" y="214" font-family="{FONT}" font-size="13.5" font-weight="700" fill="{t_fg}">{esc(t_title)}</text>')
        for j, (aname, ast, adesc) in enumerate(items):
            ay = 234 + j * 50
            parts.append(f'<text x="{tx+14}" y="{ay}" font-family="{FONT}" font-size="13" font-weight="700" fill="#0F172A">{esc(aname)}</text>')
            parts.append(badge(tx + 324, ay - 14, 80, 20, f"[{ast}]", "GA" if ast == "GA" else "PREV", 10.5))
            parts.append(svg_text_block(tx + 14, ay + 16, adesc, 390, 11.5, "#334155", False, 1.2, 2))

    # Layer 2: Security Copilot +18 Agents (y=366, h=156)
    parts.append(card(lx, 366, lw, 156))
    parts.append(f'<rect x="{lx}" y="366" width="10" height="156" rx="4" fill="#0284C7"/>')
    parts.append(f'<text x="{lx+26}" y="396" font-family="{FONT}" font-size="16" font-weight="700" fill="#0F2C59">PLANO 3 · ASISTENCIA INTERACTIVA Y AGENTES POR DOMINIO: MICROSOFT SECURITY COPILOT (+18 AGENTES)</text>')
    parts.append(badge(lx + lw - 246, 376, 228, 26, "[GA] Incluido en M365 E5 / E7", "GA", 11.5))
    doms = [
        ("Defender (6)", "Phishing GA, Alert Triage Prev, TI Briefing GA, Hunting GA, Analyst, Dynamic Detection"),
        ("Entra (4)", "Conditional Access Opt. GA, Identity Risk Prev, Access Review Prev, Lifecycle Prev"),
        ("Intune (4)", "Vuln. Remediation, Policy Config, Change Review, Device Offboarding"),
        ("Purview (2)", "DLP Alert Triage [PREV], Insider Risk Triage [PREV]"),
        ("Sentinel + Store", "Sentinel MCP Server, Agent Builder no-code + >30 agentes partners"),
    ]
    for i, (dh, dd) in enumerate(doms):
        dx = lx + 24 + i * (248 + 8)
        parts.append(f'<rect x="{dx}" y="412" width="248" height="96" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(f'<text x="{dx+12}" y="434" font-family="{FONT}" font-size="13" font-weight="700" fill="#0284C7">{esc(dh)}</text>')
        parts.append(svg_text_block(dx + 12, 454, dd, 224, 11.5, "#334155", False, 1.25, 3))

    # Layer 3: AppSec MDASH + GHAS (y=538, h=176)
    parts.append(card(lx, 538, 646, 176, fill="#FFFFFF", stroke="#7C3AED", stroke_w=1.6))
    parts.append(f'<text x="{lx+20}" y="568" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#4C1D95">PLANO 5A · CODENAME MDASH (CÓDIGO UPSTREAM)</text>')
    parts.append(badge(lx + 474, 548, 156, 24, "[PREV] Repos 5 GB", "PREV", 11))
    parts.append(svg_text_block(lx + 20, 594, "Harness multi-modelo read-only de 5 etapas: Prepare -> Scan (>100 subagentes) -> Validate (LSP + debate) -> Dedupe -> Prove (PoC dinámico). 14 lenguajes (5 esp. + 9 gen.). Usa tokens Microsoft Foundry y alimenta a Perception Web Pen Test.", 606, 12.3, "#334155", False, 1.3, 4))

    parts.append(card(lx + 664, 538, 646, 176, fill="#FFFFFF", stroke="#16A34A", stroke_w=1.6))
    parts.append(f'<text x="{lx+684}" y="568" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#14532D">PLANO 5B · GITHUB ADVANCED SECURITY AUTOFIX</text>')
    parts.append(badge(lx + 1126, 548, 168, 24, "[GA] GHEC / [PREV] ADO", "GA", 11))
    parts.append(svg_text_block(lx + 684, 594, "Remediación agéntica en el flujo dev: copilot-swe-agent explora contexto multi-archivo, propone fix, re-ejecuta CodeQL para verificar cierre y abre PR (hasta 25 alertas por PR en Security Campaigns; $0.01 USD/crédito IA).", 606, 12.3, "#334155", False, 1.3, 4))

    # Layer 4: Azure Logic Apps SOAR (y=730, h=168)
    parts.append(card(lx, 730, lw, 168))
    parts.append(f'<rect x="{lx}" y="730" width="10" height="168" rx="4" fill="#0F766E"/>')
    parts.append(f'<text x="{lx+26}" y="762" font-family="{FONT}" font-size="16" font-weight="700" fill="#0F2C59">PLANO 4 · SOAR DETERMINÍSTICO Y PUENTE MULTI-SIEM: AZURE LOGIC APPS + PERCEPTION MCP</text>')
    parts.append(badge(lx + lw - 216, 742, 198, 26, "[GA] Producción Híbrida", "GA", 11.5))
    parts.append(svg_text_block(lx + 26, 792, "• >1.400 conectores empresariales/ITSM/red + On-Premises Data Gateway para coexistencia plurianual con Splunk/QRadar on-prem sin forzar migración masiva de logs.", 1260, 13, "#1E293B", False, 1.3, 2))
    parts.append(svg_text_block(lx + 26, 836, "• Ejecución determinística con estado, RBAC Managed Identity y bajo TCO por acción, combinada con APIs y servidor/cliente MCP (Preview) para invocar playbooks de Perception desde cualquier flujo.", 1260, 13, "#1E293B", False, 1.3, 2))

    # Layer 5: ISOC Foundation (y=914, h=210)
    parts.append(card(lx, 914, lw, 210, fill="#EFF6FF", stroke="#1D4ED8", stroke_w=2))
    parts.append(f'<text x="{lx+24}" y="948" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#1E3A8A">PLANO 1 (BASE) · DATOS, CONTEXTO Y ACTUADORES: ISOC IN MICROSOFT DEFENDER + SENTINEL + XDR</text>')
    parts.append(badge(lx + lw - 252, 926, 234, 26, "[GA Core] + [PREV] 90d/Norm.", "INFO", 11.5))
    isoc_boxes = [
        ("SIEM + XDR Unificados [GA]", "Casos, playbooks, workbooks, UEBA, workspaces e ingesta 3P (>500 conectores) en el portal Defender."),
        ("Economía y Data Lake [GA]", "Opt-in desde 17-nov-2026 para clientes Sentinel con E5/E7/Defender Suite; ingesta $2.40/GB y Data Lake integrado."),
        ("Capacidades en Preview [PREV]", "90 días de retención Defender incluida, normalización en tiempo de ingesta, Detections-as-Code y Vuln. Shielding."),
    ]
    for i, (ih, idesc) in enumerate(isoc_boxes):
        ix = lx + 24 + i * (412 + 14)
        parts.append(f'<rect x="{ix}" y="968" width="412" height="138" rx="8" fill="#FFFFFF" stroke="#93C5FD" stroke-width="1.2"/>')
        parts.append(f'<text x="{ix+14}" y="994" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#0F2C59">{esc(ih)}</text>')
        parts.append(svg_text_block(ix + 14, 1018, idesc, 384, 12.2, "#334155", False, 1.3, 4))

    # Right Cross-Cutting Pillar: Governance & Separation Guide (x=1382, w=490)
    rx = 1382
    parts.append(card(rx, 142, 490, 572, fill="#F8FAFC", stroke="#0F2C59", stroke_w=2))
    parts.append(f'<rect x="{rx}" y="142" width="490" height="44" rx="10" fill="#0F2C59"/>')
    parts.append(f'<text x="{rx+245}" y="170" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">PLANO 6 TRANSVERSAL · GOBIERNO AGENTES IA</text>')

    gov_pillars = [
        ("Microsoft Agent 365", "PREV / GA", "Inventario central y Cost Management; conecta agentes Foundry, Copilot Studio, Bedrock, Vertex y Claude."),
        ("Microsoft Entra Agent ID", "GA / PREV", "Identidad dedicada por agente, Conditional Access dinámico y permisos temporales acotados a la tarea."),
        ("Defender Local Agent Prot.", "GA Windows", "Descubre 60 tipos locales (Claude Code, Codex, Copilot CLI, OpenClaw) y bloquea instrucciones maliciosas en el loop."),
        ("Microsoft Purview para IA", "PREV Ene-27", "DSPM for AI, protección de grounding sin etiquetado previo y DLP para prompts y agentes locales."),
    ]
    for i, (gh, gst, gd) in enumerate(gov_pillars):
        gy = 204 + i * 124
        parts.append(f'<rect x="{rx+18}" y="{gy}" width="454" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(f'<text x="{rx+32}" y="{gy+26}" font-family="{FONT}" font-size="14" font-weight="700" fill="#0F172A">{esc(gh)}</text>')
        parts.append(badge(rx + 338, gy + 10, 120, 22, f"[{gst}]", "GA" if "GA Windows" in gst else "PREV", 10.5))
        parts.append(svg_text_block(rx + 32, gy + 48, gd, 424, 12, "#475569", False, 1.28, 3))

    # Bottom-Right Clarity Key Card
    parts.append(card(rx, 730, 490, 394, fill="#FFFBEB", stroke="#F59E0B", stroke_w=1.6))
    parts.append(f'<text x="{rx+22}" y="764" font-family="{FONT}" font-size="16" font-weight="700" fill="#92400E">GUÍA RÁPIDA: QUÉ HACE CADA PIEZA</text>')
    rules = [
        ("Security Copilot =", "Asiste al humano y ejecuta agentes acotados dentro de cada consola."),
        ("Perception =", "Orquesta equipos Red/Blue/Green de punta a punta hacia un outcome."),
        ("Codename MDASH =", "Descubre y prueba vulnerabilidades profundas en código (read-only)."),
        ("GHAS Autofix =", "Genera el parche multi-archivo, valida con CodeQL y abre el PR."),
        ("Azure Logic Apps =", "Ejecuta el SOAR determinístico e integra SIEMs híbridos (Splunk)."),
        ("ISOC / Defender =", "Provee el plano compartido de datos, contexto y actuadores."),
    ]
    for i, (rk_k, rk_v) in enumerate(rules):
        ry_r = 796 + i * 52
        parts.append(f'<text x="{rx+22}" y="{ry_r}" font-family="{FONT}" font-size="13" font-weight="700" fill="#78350F">{esc(rk_k)}</text>')
        parts.append(svg_text_block(rx + 22, ry_r + 18, rk_v, 446, 12, "#451A03", False, 1.2, 2))

    return base_shell(
        2,
        "Arquitectura Microsoft Agentic Security: 6 Planos Sin Solapamientos",
        "Separación funcional verificada tras Microsoft Ignite (17–20 nov 2026) entre datos, orquestación, copilotos, código, SOAR y gobierno",
        "Arquitectura en Capas + Pilar Transversal",
        "\n".join(parts),
    )


# ==============================================================================
# IG-03: MAPA DE CALOR 12 FABRICANTES x 10 DIMENSIONES
# ==============================================================================
def build_ig03() -> str:
    parts = []
    parts.append(card(48, 138, 1824, 756))

    short_dims = [
        ("D01", "SIEM+XDR", "14%"),
        ("D02", "Orq. R/B/G", "14%"),
        ("D03", "SOAR/Híbr.", "12%"),
        ("D04", "Triage/Inv.", "12%"),
        ("D05", "Hunt/Det.", "8%"),
        ("D06", "Código PoC", "10%"),
        ("D07", "Autofix PR", "6%"),
        ("D08", "Gob. Agent", "10%"),
        ("D09", "Mod./MCP", "6%"),
        ("D10", "TCO/Coex.", "8%"),
    ]

    x0 = 68
    w_vendor = 224
    w_cell = 132
    w_total = 136
    w_rank = 92

    # Header row
    hy = 154
    parts.append(f'<rect x="{x0}" y="{hy}" width="{w_vendor}" height="58" rx="6" fill="#0F2C59"/>')
    parts.append(f'<text x="{x0+16}" y="{hy+26}" font-family="{FONT}" font-size="14" font-weight="700" fill="#FFFFFF">Fabricante Enterprise</text>')
    parts.append(f'<text x="{x0+16}" y="{hy+45}" font-family="{FONT}" font-size="11.5" fill="#BAE6FD">(Peso de dimensión -&gt;)</text>')

    for j, (dc, dn, dw) in enumerate(short_dims):
        cx = x0 + w_vendor + 4 + j * (w_cell + 4)
        parts.append(f'<rect x="{cx}" y="{hy}" width="{w_cell}" height="58" rx="6" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + w_cell/2:.1f}" y="{hy+20}" font-family="{FONT}" font-size="12" font-weight="700" fill="#7DD3FC" text-anchor="middle">{dc} · {dw}</text>')
        parts.append(f'<text x="{cx + w_cell/2:.1f}" y="{hy+42}" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(dn)}</text>')

    tx = x0 + w_vendor + 4 + 10 * (w_cell + 4)
    parts.append(f'<rect x="{tx}" y="{hy}" width="{w_total}" height="58" rx="6" fill="#0F2C59"/>')
    parts.append(f'<text x="{tx + w_total/2:.1f}" y="{hy+25}" font-family="{FONT}" font-size="12.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Índice</text>')
    parts.append(f'<text x="{tx + w_total/2:.1f}" y="{hy+44}" font-family="{FONT}" font-size="12" fill="#BAE6FD" text-anchor="middle">(0–100)</text>')

    rkx = tx + w_total + 4
    parts.append(f'<rect x="{rkx}" y="{hy}" width="{w_rank}" height="58" rx="6" fill="#0F2C59"/>')
    parts.append(f'<text x="{rkx + w_rank/2:.1f}" y="{hy+35}" font-family="{FONT}" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">Rank</text>')

    weights = [d["weight"] for d in comp_data["scoring_dimensions"]]
    vendors_sorted = sorted(
        comp_data["vendors_12"],
        key=lambda v: sum(w * s for w, s in zip(weights, v["scores"])),
        reverse=True,
    )

    def score_style(val: float):
        if val >= 4.5:
            return ("#0F766E", "#FFFFFF", "#0D9488", "ALTO+")
        if val >= 3.8:
            return ("#DCFCE7", "#14532D", "#86EFAC", "FUERTE")
        if val >= 3.0:
            return ("#FEF9C3", "#713F12", "#FDE047", "MEDIO")
        return ("#FEE2E2", "#7F1D1D", "#FCA5A5", "BRECHA")

    for i, v in enumerate(vendors_sorted):
        ry = 220 + i * 50
        idx100 = sum(w * s for w, s in zip(weights, v["scores"])) * 20.0
        rk_num = 1 if i == 0 else (5 if v["vendor"].startswith(("AWS", "SentinelOne")) else i + 1)

        v_bg = "#EFF6FF" if i == 0 else ("#F8FAFC" if i % 2 == 1 else "#FFFFFF")
        parts.append(f'<rect x="{x0}" y="{ry}" width="{w_vendor}" height="44" rx="6" fill="{v_bg}" stroke="#CBD5E1" stroke-width="1"/>')
        v_short = "AWS" if v["vendor"].startswith("AWS") else v["vendor"]
        parts.append(f'<text x="{x0+14}" y="{ry+28}" font-family="{FONT}" font-size="14.5" font-weight="700" fill="#0F172A">{esc(v_short)}</text>')

        for j, sc in enumerate(v["scores"]):
            cx = x0 + w_vendor + 4 + j * (w_cell + 4)
            bg, fg, st, tag = score_style(sc)
            dash = ' stroke-dasharray="3,2"' if sc < 3.0 else ""
            parts.append(f'<rect x="{cx}" y="{ry}" width="{w_cell}" height="44" rx="6" fill="{bg}" stroke="{st}" stroke-width="1.2"{dash}/>')
            parts.append(f'<text x="{cx + 38}" y="{ry+28}" font-family="{FONT}" font-size="15" font-weight="700" fill="{fg}" text-anchor="middle">{sc:.1f}</text>')
            parts.append(f'<text x="{cx + 92}" y="{ry+27}" font-family="{FONT}" font-size="10.5" font-weight="700" fill="{fg}" text-anchor="middle">{tag}</text>')

        parts.append(f'<rect x="{tx}" y="{ry}" width="{w_total}" height="44" rx="6" fill="{v_bg}" stroke="#94A3B8" stroke-width="1.2"/>')
        parts.append(f'<text x="{tx + w_total/2:.1f}" y="{ry+28}" font-family="{FONT}" font-size="15.5" font-weight="700" fill="#0F2C59" text-anchor="middle">{idx100:.1f}</text>')

        parts.append(f'<rect x="{rkx}" y="{ry}" width="{w_rank}" height="44" rx="6" fill="#1E293B"/>')
        parts.append(f'<text x="{rkx + w_rank/2:.1f}" y="{ry+28}" font-family="{FONT}" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">#{rk_num}</text>')

    # Market average row
    ary = 220 + 12 * 50 + 6
    parts.append(f'<rect x="{x0}" y="{ary}" width="{w_vendor}" height="44" rx="6" fill="#E2E8F0" stroke="#64748B" stroke-width="1.4"/>')
    parts.append(f'<text x="{x0+14}" y="{ary+28}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#0F172A">PROMEDIO MERCADO</text>')
    for j in range(10):
        avg_d = sum(v["scores"][j] for v in vendors_sorted) / 12.0
        cx = x0 + w_vendor + 4 + j * (w_cell + 4)
        parts.append(f'<rect x="{cx}" y="{ary}" width="{w_cell}" height="44" rx="6" fill="#E2E8F0" stroke="#64748B" stroke-width="1.4"/>')
        parts.append(f'<text x="{cx + w_cell/2:.1f}" y="{ary+28}" font-family="{FONT}" font-size="14.5" font-weight="700" fill="#0F172A" text-anchor="middle">{avg_d:.2f}</text>')
    parts.append(f'<rect x="{tx}" y="{ary}" width="{w_total}" height="44" rx="6" fill="#0F2C59"/>')
    parts.append(f'<text x="{tx + w_total/2:.1f}" y="{ary+28}" font-family="{FONT}" font-size="15" font-weight="700" fill="#FFFFFF" text-anchor="middle">77.8</text>')

    # Bottom 3 analytical insight cards (y=912, h=212)
    insights = [
        ("1. La Mayor Fractura del Mercado: AppSec Agéntico (D06–D07)",
         "Promedio de mercado más bajo (3.22 y 2.88). Solo Microsoft (MDASH+GHAS: 4.9/5.0), Google+Wiz (CodeMender: 4.7/4.4) y AWS (Continuum: 4.6/4.5) conectan vulnerabilidades de código probadas con el SOC; los pure-plays EDR/SIEM quedan bajo 3.4."),
        ("2. Potencia SOAR vs. Ceguera de Sensores (D01 vs D03)",
         "Palo Alto lidera D03 (4.9 con XSOAR 8.15 + AgentiX 1.4), seguido por Microsoft (4.8 con Logic Apps), ServiceNow (4.6) y Fortinet (4.5 con FortiSOAR 8.0). Pero ServiceNow marca 2.0 en D01 por carecer de SIEM y telemetría primaria propia."),
        ("3. Adopción Rápida de MCP y Ruteo Multi-Modelo (D09)",
         "La industria convergió en 2026 hacia soporte MCP y selección multi-modelo (media 4.24): Microsoft Perception, Google SecOps DEA, FortiSOAR 8.0, Splunk 8.8 y Swimlane ya exponen o consumen herramientas MCP."),
    ]
    for i, (ih, itxt) in enumerate(insights):
        ix = 48 + i * (592 + 24)
        parts.append(card(ix, 912, 592, 212))
        parts.append(f'<rect x="{ix}" y="912" width="592" height="8" rx="4" fill="#0284C7"/>')
        parts.append(f'<text x="{ix+22}" y="948" font-family="{FONT}" font-size="15" font-weight="700" fill="#0F2C59">{esc(ih)}</text>')
        parts.append(svg_text_block(ix + 22, 976, itxt, 548, 12.8, "#334155", False, 1.35, 5))

    return base_shell(
        3,
        "Mapa de Calor Técnico: 12 Fabricantes × 10 Dimensiones Ponderadas",
        "Cada celda combina puntaje numérico exacto (1.0–5.0) y categoría semántica accesible (ALTO+ >=4.5 | FUERTE 3.8–4.4 | MEDIO 3.0–3.7 | BRECHA <3.0)",
        "Matriz Cuantitativa Multidimensional",
        "\n".join(parts),
    )


# ==============================================================================
# IG-04: AUDITORÍA DE MADUREZ REAL GA vs PREVIEW / EA / ROADMAP
# ==============================================================================
def build_ig04() -> str:
    parts = []
    # Top Distribution Strip (y=138, h=114)
    parts.append(card(48, 138, 1824, 114))
    parts.append(f'<text x="72" y="168" font-family="{FONT}" font-size="16" font-weight="700" fill="#0F2C59">DISTRIBUCIÓN REAL DE LAS 56 CAPACIDADES AGÉNTICAS AUDITADAS AL 25 DE NOVIEMBRE DE 2026</text>')

    buckets = [
        ("GA Productivo: 31 (55.4%)", 31, "#16A34A", "#FFFFFF"),
        ("GA Acotado: 1 (1.8%)", 1, "#22C55E", "#FFFFFF"),
        ("Public Preview: 14 (25.0%)", 14, "#FACC15", "#713F12"),
        ("Gated: 3 (5.4%)", 3, "#FB923C", "#FFFFFF"),
        ("EA: 3 (5.4%)", 3, "#F97316", "#FFFFFF"),
        ("Roadmap: 4 (7.1%)", 4, "#EF4444", "#FFFFFF"),
    ]
    bx = 72.0
    total_w = 1776.0
    for label, cnt, bg, fg in buckets:
        seg_w = (cnt / 56.0) * total_w
        parts.append(f'<rect x="{bx:.1f}" y="182" width="{seg_w:.1f}" height="34" fill="{bg}" stroke="#FFFFFF" stroke-width="1.5"/>')
        if seg_w > 110:
            parts.append(f'<text x="{bx + seg_w/2:.1f}" y="204" font-family="{FONT}" font-size="12.5" font-weight="700" fill="{fg}" text-anchor="middle">{esc(label)}</text>')
        bx += seg_w
    parts.append(f'<text x="72" y="238" font-family="{FONT}" font-size="12.5" fill="#475569">Lectura ejecutiva: Casi la mitad (42.9% = 24 de 56) de los anuncios de seguridad agéntica del mercado siguen en Preview, Early Access, acceso restringido o Roadmap 2027.</text>')

    # 8 Vendor Audit Cards (4x2 grid, y=268..1124)
    cards_data = [
        ("Microsoft (Ignite Nov 2026)", "MS",
         "Perception plataforma + 4 agentes Blue + Recon + Posture Prioritization; ISOC core + 3P ingestion; GHAS Autofix (GHEC); Defender Local Agent Protection Windows.",
         "Codename MDASH (Preview 5GB, sin fecha GA pública); Web App Pen Test y Risk Reduction (Preview); ISOC 90d retention y normalización (Preview); Purview Agent DLP (ene-2027)."),
        ("Palo Alto Networks", "INFO",
         "Cortex XSIAM 3.6 y Cortex AgentiX 1.4 (autorizado FedRAMP Moderate & High); Cortex XDR 5.2 AES y XDR One (oct-2026); XSOAR 8.15; PAN-OS 12.2 Virtual Patching.",
         "Creación de workflows multi-paso por lenguaje natural (adquisición de Console sep-2026) aún en integración gradual; fuerte dependencia de migración completa a XSIAM."),
        ("Google Cloud + Wiz", "INFO",
         "Google SecOps SIEM/SOAR (RN nov-2026); Alert Triage Agent (>5M alertas); Wiz Red/Blue/Green Agents por tokens; Wiz Sensor Forensics y Wiz AI SAST (oct-2026).",
         "CodeMender sigue en Public Preview (invocación desde Wiz marcada 'coming soon'); Threat Hunt Agent en Preview (solo Enterprise+); Gemini 4 Carbon acotado; consolas aún separadas."),
        ("CrowdStrike", "INFO",
         "Charlotte AI investigaciones multi-agente coordinadas (oct-2026); Falcon Next-Gen SIEM + Fusion SOAR; SafeMind (sep-2026); Agent Graph score 0-100.",
         "AI Kill Switch corta solo vía Falcon AI Gateway (sin revocar identidad ni cubrir modelos locales); Adversary Emulation en Early Access (4-nov); Fiddler y Dreadnode cierran Q4 FY27."),
        ("AWS (Amazon Web Services)", "NEUTRAL",
         "AWS Security Incident Response con agente IA investigativo (actualizado 18-nov-2026); AWS Continuum for Code Vulnerabilities GA el 22-oct-2026.",
         "AWS Continuum GA restringido inicialmente a solo 2 regiones de EE. UU.; Continuum Penetration Testing y STRIDE Threat Modeling siguen en Preview; sin cobertura fuera de AWS."),
        ("SentinelOne", "NEUTRAL",
         "Suite Singularity ASOC (21-oct-2026); Purple AI Agentic Investigation (>400k alertas críticas desde jun-2026); Hyperautomation Closed-Loop gobernado (ago-2026).",
         "Singularity Agentic Detection & Response (para descubrir/frenar agentes IA) recién en Early Access (21-oct-2026); sensor en VM Claude Cowork solo planeado (2-nov)."),
        ("Cisco / Splunk", "NEUTRAL",
         "Splunk Enterprise Security 8.8.0 (GA 4-nov-2026); Cisco Data Fabric sobre Splunk (GA ago-2026); Cisco XDR Instant Attack Verification; SOAR Automation Broker HA.",
         "Agentic SOC en ES 8.8 enfocado en despliegues Cloud-Connected; upgrade a ES 8.x es irreversible respecto a investigaciones previas sin backup; usa Azure OpenAI externo."),
        ("ServiceNow · IBM · Elastic · Fortinet", "NEUTRAL",
         "FortiSOAR 8.0 (>19 agentes + MCP GA oct-26); Elastic Workflows 9.4 y Attack Discovery 9.5 GA; Zscaler Agentic SOC GA (sep-26); ServiceNow Arc Agent GA (21-oct).",
         "Elastic 9.6 AlertZero en Tech Preview (23-nov); FortiSOC cloud en Preview; IBM watsonx Discover & Contain en Tech Preview; ServiceNow AI Passport OpenShell en release futuro."),
    ]

    cw = 438
    ch = 414
    for idx, (vtitle, kind, ga_txt, prev_txt) in enumerate(cards_data):
        col_i = idx % 4
        row_i = idx // 4
        cx = 48 + col_i * (cw + 24)
        cy = 268 + row_i * (ch + 22)
        stroke = "#2563EB" if kind == "MS" else "#CBD5E1"
        parts.append(card(cx, cy, cw, ch, stroke=stroke, stroke_w=2 if kind == "MS" else 1.4))
        hdr_bg = "#1E3A8A" if kind == "MS" else "#1E293B"
        parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="38" rx="10" fill="{hdr_bg}"/>')
        parts.append(f'<text x="{cx+18}" y="{cy+25}" font-family="{FONT}" font-size="14.5" font-weight="700" fill="#FFFFFF">{esc(vtitle)}</text>')

        # GA Box
        parts.append(f'<rect x="{cx+14}" y="{cy+50}" width="{cw-28}" height="164" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>')
        parts.append(badge(cx + 24, cy + 60, 146, 22, "[GA] Disponible Hoy", "GA", 11))
        parts.append(svg_text_block(cx + 24, cy + 100, ga_txt, cw - 48, 12.2, "#14532D", False, 1.3, 6))

        # Preview / Watchout Box
        parts.append(f'<rect x="{cx+14}" y="{cy+226}" width="{cw-28}" height="174" rx="8" fill="#FFFBEB" stroke="#FCD34D" stroke-width="1.2"/>')
        parts.append(badge(cx + 24, cy + 236, 232, 22, "[PREV / EA / LÍMITE] Atención", "PREV", 11))
        parts.append(svg_text_block(cx + 24, cy + 276, prev_txt, cw - 48, 12.2, "#713F12", False, 1.3, 6))

    return base_shell(
        4,
        "Auditoría GA vs. Preview: Qué Está en Producción Real a Noviembre 2026",
        "Contraste verificable por fabricante entre capacidades listas para producción hoy y anuncios sujetos a Preview, regiones limitadas o cierres futuros",
        "Grilla Modular de Madurez",
        "\n".join(parts),
    )


# ==============================================================================
# IG-05: SOAR, LOGIC APPS Y COEXISTENCIA MULTI-SIEM (SPLUNK ON-PREM)
# ==============================================================================
def build_ig05() -> str:
    parts = []

    # Top Conceptual Contrast: Path A vs Path B (y=138, h=336)
    # Left Card: Rip-and-Replace
    parts.append(card(48, 138, 896, 336, fill="#FEF2F2", stroke="#EF4444", stroke_w=1.8))
    parts.append(badge(68, 154, 240, 26, "RUTA A · ALTO RIESGO Y COSTO", "ROAD", 11.5))
    parts.append(f'<text x="322" y="173" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#7F1D1D">Modelo "Rip-and-Replace" (XSIAM / Falcon Next-Gen SIEM)</text>')

    ra_boxes = [
        ("1. Migración Forzada de Ingesta", "Exige mover terabytes de logs, parsers y detecciones desde Splunk/QRadar hacia el nuevo SIEM antes de capturar valor agéntico completo."),
        ("2. Fricción Operativa Plurianual", "12–24 meses de doble pago de licencias, reentrenamiento total del SOC y pérdida de contexto histórico durante la transición."),
        ("3. Lock-In Post-Promoción", "Descuentos agresivos de entrada ('Platformization' / bundles) seguidos de altos costos recurrentes de ingesta propietaria y servicios."),
    ]
    for i, (bh, bd) in enumerate(ra_boxes):
        by = 196 + i * 88
        parts.append(f'<rect x="68" y="{by}" width="856" height="76" rx="8" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="1.2"/>')
        parts.append(f'<text x="86" y="{by+25}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#991B1B">{esc(bh)}</text>')
        parts.append(svg_text_block(86, by + 45, bd, 820, 12.2, "#334155", False, 1.25, 2))

    # Right Card: Microsoft Governed Hybrid Coexistence
    rx = 976
    parts.append(card(rx, 138, 896, 336, fill="#F0FDF4", stroke="#16A34A", stroke_w=2))
    parts.append(badge(rx + 20, 154, 266, 26, "RUTA B · ARQUITECTURA RECOMENDADA", "GA", 11.5))
    parts.append(f'<text x="{rx+300}" y="173" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#14532D">Coexistencia Híbrida Gobernada (Logic Apps + ISOC + Splunk)</text>')

    rb_boxes = [
        ("1. Convivencia Plurianual con Splunk On-Prem", "Azure Logic Apps (+1.400 conectores y On-Prem Data Gateway) orquesta consultas y acciones sobre Splunk sin mover logs masivamente."),
        ("2. Costo Marginal Óptimo en Nube Microsoft", "Activa Sentinel / ISOC aprovechando los datos ya bonificados por Microsoft 365 E5 y Defender for Servers Plan 2 + 90d Defender (Preview)."),
        ("3. Plano Único de Casos y Agentes (Perception MCP)", "Case management unificado y disparo bidireccional de playbooks Perception y Security Copilot vía APIs/MCP sobre todo el entorno."),
    ]
    for i, (bh, bd) in enumerate(rb_boxes):
        by = 196 + i * 88
        parts.append(f'<rect x="{rx+20}" y="{by}" width="856" height="76" rx="8" fill="#FFFFFF" stroke="#86EFAC" stroke-width="1.2"/>')
        parts.append(f'<text x="{rx+38}" y="{by+25}" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#14532D">{esc(bh)}</text>')
        parts.append(svg_text_block(rx + 38, by + 45, bd, 820, 12.2, "#334155", False, 1.25, 2))

    # Bottom Comparative Table of 8 SOAR Platforms (y=492..1124, h=632)
    parts.append(card(48, 492, 1824, 632))
    parts.append(f'<text x="72" y="524" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59">COMPARATIVA TÉCNICA DE LOS 8 MOTORES LÍDERES DE SOAR E HIPERAUTOMATIZACIÓN (NOVIEMBRE 2026)</text>')

    cols = [
        ("Plataforma SOAR / Automatización", 290),
        ("Conectores e Hibridez", 270),
        ("Determinístico + Agéntico", 330),
        ("Soporte MCP", 230),
        ("Coexistencia SIEM 3P", 320),
        ("Modelo TCO / Costo", 324),
    ]
    cx = 68
    hy = 540
    for ch_t, cw_t in cols:
        parts.append(f'<rect x="{cx}" y="{hy}" width="{cw_t}" height="38" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + cw_t/2:.1f}" y="{hy+24}" font-family="{FONT}" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(ch_t)}</text>')
        cx += cw_t + 4

    soar_data = [
        ("Microsoft Logic Apps + Perception", ">1.400 enterprise + On-Prem Gateway + >500 ISOC", "Playbooks PaaS con estado + equipos Red/Blue/Green", "[PREV/GA] MCP en Perception y Sentinel", "ALTA: ideal sobre Splunk on-prem sin migrar todo", "Muy bajo por ejecución / Standard predecible", True),
        ("Palo Alto XSOAR 8.15 + AgentiX 1.4", ">1.000 packs + conectores unificados con Vault", "War Room maduro + planes AgentiX JSON Schema", "[ENDPOINT] Descubre riesgos MCP en XDR", "MEDIA: XSOAR sí, pero empuja XSIAM", "Alto (licencia + servicios Unit 42)", False),
        ("Fortinet FortiSOAR 8.0 + FortiAI 6.0", ">500 conectores + caza en FortiSIEM y Splunk", "Playbooks completos + >19 agentes IA por hipótesis", "[GA] Servidor y cliente MCP nativo en 8.0", "ALTA: appliance/VM opera sobre SIEM 3P", "Competitivo por asiento/nodo", False),
        ("Cisco / Splunk SOAR + ES 8.8", ">350 apps + Automation Broker HA en 8.8", "Playbooks Python/visual + respuesta guiada humana", "[DOCS] MCP Server for Splunk Platform", "ALTA con Splunk; menor agilidad multi-cloud", "Costoso (requiere edición Premier/add-on)", False),
        ("ServiceNow SIR + Now Assist", "IntegrationHub + CMDB empresarial completa", "Flow Designer ITSM + Agentic Workflows (oct-26)", "[PREV/Q4] AI Passport valida alcances MCP", "ALTA en tickets, pero sin detección propia", "Muy alto (SIR + uplift Pro/Enterprise Plus)", False),
        ("CrowdStrike Falcon Fusion + Charlotte", "Falcon Store + integraciones API/Dynatrace", "Workflows nativos Falcon + agentes en paralelo", "Ecosistema propio AgentWorks", "BAJA: diseñado para mover hacia Falcon SIEM", "Escala con módulos e ingesta Falcon SIEM", False),
        ("Elastic Workflows 9.4+ + AlertZero", "Conectores nativos sobre Elasticsearch", "Scripts + 5 skills de Elastic AI Agent sobre datos", "Conector abierto multi-LLM / Agent Builder", "BAJA fuera del clúster Elasticsearch", "Incluido en suscripción Elastic Enterprise", False),
        ("Torq Socrates / Swimlane Turbine", "Centenares de APIs rest/webhook no-code", "Agentic Builder ('Cursor SecOps') / Hero AI", "[GA] Swimlane MCP bidireccional (oct-26)", "ALTA neutralidad, pero suma otro silo/contrato", "Suscripción anual dedicada ($150k+)", False),
    ]

    for idx_r, row_vals in enumerate(soar_data):
        is_ms = row_vals[-1]
        ry = 584 + idx_r * 66
        bg = "#EFF6FF" if is_ms else ("#F8FAFC" if idx_r % 2 == 1 else "#FFFFFF")
        st = "#60A5FA" if is_ms else "#E2E8F0"
        parts.append(f'<rect x="68" y="{ry}" width="1784" height="60" rx="6" fill="{bg}" stroke="{st}" stroke-width="1.2"/>')
        cx = 68
        for col_j, val in enumerate(row_vals[:-1]):
            cw_t = cols[col_j][1]
            parts.append(svg_text_block(cx + 10, ry + 23, val, cw_t - 20, 12.2, "#0F172A" if col_j == 0 else "#334155", col_j == 0 or is_ms and col_j == 4, 1.25, 2))
            cx += cw_t + 4

    return base_shell(
        5,
        "SOAR y Coexistencia SIEM: Orquestación Híbrida vs. Rip-and-Replace",
        "Por qué Azure Logic Apps + ISOC + Perception MCP maximizan retorno sobre Splunk on-prem frente al reemplazo traumático o silos SOAR adicionales",
        "Contraste Arquitectónico + Matriz SOAR",
        "\n".join(parts),
    )


# ==============================================================================
# IG-06: APPSEC AGÉNTICO (MDASH + GHAS vs CODEMENDER+WIZ vs AWS CONTINUUM)
# ==============================================================================
def build_ig06() -> str:
    parts = []

    # Top Pipeline Card: Microsoft Upstream Loop (y=138, h=300)
    parts.append(card(48, 138, 1824, 300))
    parts.append(f'<text x="72" y="170" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59"> FLUJO CERRADO MICROSOFT: DEL DESCUBRIMIENTO PROFUNDO EN CÓDIGO (MDASH) AL PR VERIFICADO (GHAS)</text>')
    parts.append(f'<text x="72" y="192" font-family="{FONT}" font-size="12.5" fill="#475569">Principio arquitectónico de MDASH: "El modelo es solo un insumo; el harness multi-modelo de validación y prueba dinámica es el producto".</text>')

    stages = [
        ("1. PREPARE", "MDASH [PREV]", "Call-graph, historial Git, modelo de amenazas y ranking de riesgo.", "#EDE9FE", "#7C3AED"),
        ("2. SCAN", "MDASH [PREV]", ">100 subagentes; elige 3–5 auditores expertos por función.", "#EDE9FE", "#7C3AED"),
        ("3. VALIDATE", "MDASH [PREV]", "Taint/tipos vía LSP + debate cruzado multi-modelo contra FPs.", "#EDE9FE", "#7C3AED"),
        ("4. DEDUPE", "MDASH [PREV]", "Agrupa hallazgos equivalentes y calcula score de confianza.", "#EDE9FE", "#7C3AED"),
        ("5. PROVE", "MDASH [PREV]", "Genera inputs/PoC y fuzzing para demostrar explotabilidad.", "#EDE9FE", "#7C3AED"),
        ("6. WEB PENTEST", "Perception [PREV]", "Valida en app viva (31% Incalmo) y sugiere WAF/Shielding.", "#DBEAFE", "#2563EB"),
        ("7. AUTOFIX PR", "GHAS [GA GHEC]", "copilot-swe-agent edita multi-archivo, re-corre CodeQL y abre PR.", "#DCFCE7", "#16A34A"),
    ]
    sw = 236
    gap = 18
    for i, (st_t, prod_t, desc_t, bg, stroke) in enumerate(stages):
        sx = 72 + i * (sw + gap)
        sy = 212
        parts.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="204" rx="10" fill="{bg}" stroke="{stroke}" stroke-width="1.6"/>')
        parts.append(f'<text x="{sx+14}" y="{sy+28}" font-family="{FONT}" font-size="14" font-weight="700" fill="#0F172A">{esc(st_t)}</text>')
        parts.append(badge(sx + 14, sy + 38, 138, 22, prod_t, "GA" if "GA" in prod_t else "PREV", 10.5))
        parts.append(svg_text_block(sx + 14, sy + 82, desc_t, sw - 28, 12.2, "#1E293B", False, 1.32, 5))
        if i < len(stages) - 1:
            ax = sx + sw + 2
            parts.append(f'<line x1="{ax}" y1="{sy+102}" x2="{ax+14}" y2="{sy+102}" stroke="#475569" stroke-width="2.2"/>')
            parts.append(f'<polygon points="{ax+14},{sy+102} {ax+8},{sy+97} {ax+8},{sy+107}" fill="#475569"/>')

    # Bottom Matrix: 6 AppSec Agentic Offerings (y=456..1124, h=668)
    parts.append(card(48, 456, 1824, 668))
    parts.append(f'<text x="72" y="490" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59">BENCHMARK HEAD-TO-HEAD: PLATAFORMAS DE VULNERABILIDADES AGÉNTICAS Y AUTOFIX DE CÓDIGO (NOV 2026)</text>')

    acols = [
        ("Fabricante y Solución", 280),
        ("Estado Real (Nov 2026)", 230),
        ("Arquitectura / Modelos", 330),
        ("¿Valida con Exploit / PoC?", 290),
        ("¿Autofix Verificado en PR?", 320),
        ("Límite o Ventaja Clave", 314),
    ]
    cx = 68
    hy = 508
    for ch_t, cw_t in acols:
        parts.append(f'<rect x="{cx}" y="{hy}" width="{cw_t}" height="38" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + cw_t/2:.1f}" y="{hy+24}" font-family="{FONT}" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(ch_t)}</text>')
        cx += cw_t + 4

    arows = [
        ("Microsoft (Codename MDASH + GHAS Autofix + Perception)", "[GA] GHAS GHEC | [PREV] MDASH (5GB) & ADO", "Ensemble Foundry + MAI-Cyber-1.1/2 + copilot-swe-agent", "SÍ: PoC dinámico en MDASH + Web Pen Test Agent en app viva", "SÍ (GA): PR multi-archivo verificado con CodeQL (hasta 25 alertas)", "Único puente nativo GitHub + Código + Exposición Defender + SOC", True),
        ("Google Cloud + Wiz (CodeMender + Wiz AI SAST + Red Agent)", "[PREV] CodeMender | [GA] Wiz AI SAST", "DeepMind Gemini / Gemini 4 Carbon + grafo cloud Wiz", "SÍ: exploits PoC en sandbox aislado + Wiz Red Agent", "SÍ (Preview): parches evaluados con LLM-as-a-judge y migración segura", "Integración Wiz->CodeMender figura aún 'coming soon' en docs", False),
        ("AWS (AWS Continuum + Security Agent + Kiro/Claude)", "[GA] Code Vulns (2 reg. US) | [PREV] Pentest", "Grafo AWS + Amazon Bedrock + plugins IDE Kiro y Claude Code", "SÍ: prueba reproducible en sandbox (33/37 CVEs reales explotados)", "SÍ: mitigación reversible rápida + PRs duraderos en Git", "GA restringido hoy a 2 regiones US y acotado a cargas AWS", False),
        ("Snyk (Evo Agentic Dev Security + Continuous Offensive)", "[GA / Rollout] Lanzado jun-2026", "AI Security Fabric: Evo ADS (guardrails) + Evo COS (ofensivo)", "SÍ: Evo COS simula ataques continuos para hallar fallas reales", "SÍ: DeepCode AI corrige al momento de escribir código en el IDE", "Fuerte en DevSecOps y MCPs, pero aislado del SIEM/XDR/IdP del SOC", False),
        ("Palo Alto Networks (Unit 42 Frontier AI + PAN-OS 12.2)", "[GA/Servicio] Unit 42 + Virtual Patching", "Modelos OpenAI y Anthropic operados con Cortex y expertos Unit 42", "SÍ: validación de exploits asistida por modelos en entornos Unit 42", "Foco en Virtual Patching de red (PAN-OS 12.2) más que PR nativo", "Alta dependencia de servicios gestionados Unit 42 y firewalls PANW", False),
        ("CrowdStrike (SafeMind + Adquisición Dreadnode)", "[SEP-26] SafeMind | [Q4 FY27] Dreadnode", "SafeMind sobre NVIDIA Nemotron + razonamiento GPT-5.6 Cyber", "Emulación adversaria en SOC (EA nov-26), no SAST de código fuente", "NO posee motor propio de SAST ni generación de PRs en repositorios", "Requiere socios externos (ej. GitHub/Snyk/Wiz) para cubrir código", False),
    ]

    for idx_r, rvals in enumerate(arows):
        is_ms = rvals[-1]
        ry = 554 + idx_r * 90
        bg = "#EFF6FF" if is_ms else ("#F8FAFC" if idx_r % 2 == 1 else "#FFFFFF")
        st = "#60A5FA" if is_ms else "#E2E8F0"
        parts.append(f'<rect x="68" y="{ry}" width="1784" height="82" rx="8" fill="{bg}" stroke="{st}" stroke-width="1.2"/>')
        cx = 68
        for col_j, val in enumerate(rvals[:-1]):
            cw_t = acols[col_j][1]
            parts.append(svg_text_block(cx + 12, ry + 24, val, cw_t - 24, 12.4, "#0F172A" if col_j == 0 else "#334155", col_j in (0, 1), 1.3, 3))
            cx += cw_t + 4

    return base_shell(
        6,
        "AppSec Agéntico: Descubrimiento Profundo, PoC Exploit y Autofix en PR",
        "Comparación técnica del ciclo Codename MDASH + Perception + GitHub Advanced Security frente a Google CodeMender, AWS Continuum y Snyk Evo",
        "Pipeline Secuencial + Matriz AppSec",
        "\n".join(parts),
    )


# ==============================================================================
# IG-07: GOBIERNO Y CONTENCIÓN DE AGENTES IA ("AGENTIC INSIDERS")
# ==============================================================================
def build_ig07() -> str:
    parts = []

    # Top 5 Control Points Strip (y=138, h=174)
    cps = [
        ("CP-1 · DESCUBRIMIENTO", "Agentes locales en OS, agentes cloud 1P/3P, extensiones IDE y servidores MCP.", "#0284C7"),
        ("CP-2 · IDENTIDAD AGENTE", "Credencial propia (Agent ID), mínimo privilegio, delegación acotada y acceso condicional.", "#2563EB"),
        ("CP-3 · LOOP OS / ENDPOINT", "Inspección en tiempo real del agent loop local para frenar prompt injection o comandos dañinos.", "#0F766E"),
        ("CP-4 · DATOS Y DLP", "Clasificación y bloqueo de exfiltración sobre archivos sensibles y prompts con o sin etiqueta.", "#7C3AED"),
        ("CP-5 · KILL SWITCH REAL", "Capacidad hoy en GA de revocar identidad + frenar proceso en host + cortar acceso a datos.", "#DC2626"),
    ]
    cw_cp = 346
    for i, (ct, cd, col) in enumerate(cps):
        cx = 48 + i * (cw_cp + 23.5)
        parts.append(card(cx, 138, cw_cp, 174))
        parts.append(f'<rect x="{cx}" y="138" width="{cw_cp}" height="34" rx="8" fill="{col}"/>')
        parts.append(f'<text x="{cx + cw_cp/2:.1f}" y="160" font-family="{FONT}" font-size="13" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(ct)}</text>')
        parts.append(svg_text_block(cx + 16, 196, cd, cw_cp - 32, 12.8, "#334155", False, 1.34, 4))

    # Center Control-Point Matrix (y=328..942, h=614)
    parts.append(card(48, 328, 1824, 614))
    parts.append(f'<text x="72" y="360" font-family="{FONT}" font-size="16.5" font-weight="700" fill="#0F2C59">¿QUIÉN PUEDE DESCUBRIR, GOBERNAR Y DETENER UN AGENTE COMPROMETIDO HOY? (AUDITORÍA NOVIEMBRE 2026)</text>')

    gcols = [
        ("Fabricante / Plano de Control", 290),
        ("CP-1: Descubrimiento", 284),
        ("CP-2: Identidad Nativa", 284),
        ("CP-3: Runtime Endpoint/OS", 300),
        ("CP-4: Datos y DLP", 284),
        ("CP-5: Realidad Kill Switch", 322),
    ]
    cx = 68
    hy = 376
    for ch_t, cw_t in gcols:
        parts.append(f'<rect x="{cx}" y="{hy}" width="{cw_t}" height="36" rx="5" fill="#1E3A5F"/>')
        parts.append(f'<text x="{cx + cw_t/2:.1f}" y="{hy+23}" font-family="{FONT}" font-size="12.8" font-weight="700" fill="#FFFFFF" text-anchor="middle">{esc(ch_t)}</text>')
        cx += cw_t + 4

    grows = [
        ("Microsoft (Agent 365 + Entra Agent ID + Defender + Purview)",
         ("GA", "[GA] 60 locales + [PREV] Bedrock/Vertex"),
         ("GA", "[GA/PREV] Entra Agent ID + CA dinámico"),
         ("GA", "[GA Windows] Bloquea instrucciones en loop"),
         ("PREV", "[GA] DSPM AI + [PREV Ene-27] Agent DLP"),
         ("GA", "[COMPLETO] Revoca ID + frena host + DLP")),
        ("Palo Alto Networks (Cortex XDR 5.2 AES + XDR One)",
         ("GA", "[GA] Agentes, IDEs, MCPs y Shadow AI"),
         ("INFO", "[INDIRECTO] Vía Okta / Entra / AD CAP"),
         ("GA", "[GA] SLMs en endpoint bloquean comandos"),
         ("INFO", "[PARCIAL] Prisma Browser + archivo 300MB"),
         ("INFO", "[FUERTE EN HOST] Sin propiedad de IdP/M365")),
        ("CrowdStrike (Falcon Guardian + Agent Graph)",
         ("GA", "[GA] Endpoints + hooks Copilot/Claude/Codex"),
         ("ROAD", "[SIN IdP] Depende de identidad externa"),
         ("PREV", "[PARCIAL] Hooks prompt; host kill sin fecha"),
         ("ROAD", "[LIMITADO] Sin gobierno integral tipo Purview"),
         ("EA", "[SOLO GATEWAY] No frena modelos locales")),
        ("ServiceNow (AI Control Tower + AI Passport)",
         ("GA", "[GA] Inventario CMDB + Shadow AI red"),
         ("PREV", "[Q4 2026] AI Passport firmado en runtime"),
         ("ROAD", "[CERO OS] Sin sensor ni agente endpoint"),
         ("ROAD", "[CERO DLP] Flujos GRC sin inspección datos"),
         ("ROAD", "[DELEGA] Necesita que 3P ejecute el corte")),
        ("IBM (watsonx Orchestrate Gateway + Agent Identity)",
         ("EA", "[TECH PREV] Bedrock, Foundry y Gemini"),
         ("GA", "[GA] IBM Agent Identity + HashiCorp Vault"),
         ("INFO", "[RUNTIME PROPIO] Contenedor aislado IBM"),
         ("GA", "[GA] Guardium AI + catálogo EU AI Act"),
         ("EA", "[TECH PREV] Contención multi-cloud en prueba")),
        ("Okta Blueprint / SailPoint Agentic Fabric",
         ("PREV", "[PARCIAL] Tokens OAuth e IDs máquina"),
         ("GA", "[FUERTE] Agent SSO, IGA y certificaciones"),
         ("ROAD", "[CERO OS] Sin visibilidad en el dispositivo"),
         ("ROAD", "[CERO DLP] Depende de socios externos"),
         ("PREV", "[PREVIEW/ROAD] Kill switch sin fecha GA")),
    ]

    for idx_r, (vname, c1, c2, c3, c4, c5) in enumerate(grows):
        ry = 418 + idx_r * 84
        is_ms = idx_r == 0
        bg = "#EFF6FF" if is_ms else ("#F8FAFC" if idx_r % 2 == 1 else "#FFFFFF")
        parts.append(f'<rect x="68" y="{ry}" width="1784" height="76" rx="8" fill="{bg}" stroke="#CBD5E1" stroke-width="1.2"/>')
        parts.append(svg_text_block(80, ry + 26, vname, 266, 13, "#0F172A", True, 1.28, 3))

        cx = 68 + 290 + 4
        for j, (bkind, btxt) in enumerate((c1, c2, c3, c4, c5)):
            cw_t = gcols[j + 1][1]
            cell_bg = {"GA": "#F0FDF4", "INFO": "#F0F9FF", "PREV": "#FEFCE8", "EA": "#FFF7ED", "ROAD": "#FEF2F2"}[bkind]
            cell_st = {"GA": "#86EFAC", "INFO": "#7DD3FC", "PREV": "#FDE047", "EA": "#FDBA74", "ROAD": "#FCA5A5"}[bkind]
            parts.append(f'<rect x="{cx+4}" y="{ry+8}" width="{cw_t-8}" height="60" rx="6" fill="{cell_bg}" stroke="{cell_st}" stroke-width="1.2"/>')
            parts.append(svg_text_block(cx + 14, ry + 30, btxt, cw_t - 28, 12, "#0F172A", j == 4 or is_ms, 1.25, 2))
            cx += cw_t + 4

    # Bottom Strip: 3 CISO Deal Questions (y=958..1124, h=166)
    parts.append(card(48, 958, 1824, 166, fill="#0F2C59", stroke="#0EA5E9", stroke_w=1.8))
    parts.append(f'<text x="72" y="990" font-family="{FONT}" font-size="16" font-weight="700" fill="#7DD3FC">3 PREGUNTAS DE AUDITORÍA PARA EL CISO ANTE PROMESAS DE "CONTROL NEUTRAL DE AGENTES"</text>')
    qs = [
        ("1. ¿Revoca identidad o solo corta un Gateway?", "Si un desarrollador usa un agente local o credenciales robadas (device-code phishing), cortar el AI Gateway no detiene el acceso al repo o datos."),
        ("2. ¿Viaja la política de datos (DLP) con el agente?", "Un inventario en CMDB no impide que un agente lea y filtre un documento confidencial no etiquetado en Windows o SharePoint."),
        ("3. ¿Está en GA hoy o en Preview sin fecha?", "Exija demostración en vivo sobre endpoints reales hoy: varios 'Kill Switches' anunciados en oct-nov 2026 siguen en Preview o dependen de terceros."),
    ]
    for i, (qh, qd) in enumerate(qs):
        qx = 72 + i * (584 + 20)
        parts.append(f'<rect x="{qx}" y="1006" width="584" height="102" rx="8" fill="#1E3A5F" stroke="#38BDF8" stroke-width="1"/>')
        parts.append(f'<text x="{qx+16}" y="1032" font-family="{FONT}" font-size="13.5" font-weight="700" fill="#FFFFFF">{esc(qh)}</text>')
        parts.append(svg_text_block(qx + 16, 1054, qd, 552, 12, "#E2E8F0", False, 1.28, 3))

    return base_shell(
        7,
        "Gobierno de 'Agentic Insiders': Control Full-Stack vs. Promesas Parciales",
        "Evaluación en los 5 puntos de control requeridos para descubrir, autenticar y contener agentes IA locales, cloud y MCP a noviembre de 2026",
        "Matriz de Puntos de Control (5 Capas)",
        "\n".join(parts),
    )


SERIES_SPECS = [
    ("IG-01_Ranking_Global_12_Fabricantes", "Panorama y Ranking Ponderado de los 12 Fabricantes Enterprise", build_ig01),
    ("IG-02_Arquitectura_Microsoft_6_Planos", "Arquitectura Microsoft Agentic Security: 6 Planos Sin Solapamientos", build_ig02),
    ("IG-03_Mapa_Calor_10_Dimensiones", "Mapa de Calor Técnico: 12 Fabricantes x 10 Dimensiones", build_ig03),
    ("IG-04_Realidad_GA_vs_Preview_Nov2026", "Auditoría de Madurez Real: GA vs. Preview, EA y Roadmap", build_ig04),
    ("IG-05_SOAR_LogicApps_y_Coexistencia_SIEM", "SOAR, Logic Apps y Coexistencia Híbrida Multi-SIEM", build_ig05),
    ("IG-06_AppSec_Agentico_MDASH_CodeMender_Continuum", "AppSec Agéntico: Descubrimiento, PoC Exploit y Autofix en PR", build_ig06),
    ("IG-07_Gobierno_y_Contencion_Agentes_IA", "Gobierno y Contención Runtime de Agentes IA ('Agentic Insiders')", build_ig07),
]


def main():
    svg_paths = []
    for slug, title, builder in SERIES_SPECS:
        svg_content = builder()
        svg_path = SVG_DIR / f"{slug}.svg"
        svg_path.write_text(svg_content, encoding="utf-8")
        shutil.copy2(svg_path, SCOUT_PREVIEW_DIR / f"{slug}.svg")
        shutil.copy2(svg_path, SESSION_FILES / f"{slug}.svg")
        svg_paths.append((slug, title, svg_path))
        print(f"Wrote SVG: {svg_path.name} ({len(svg_content)} chars)")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=edge_path, headless=True)
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

            shutil.copy2(png_path, SCOUT_PREVIEW_DIR / f"{slug}.png")
            shutil.copy2(jpg_path, SCOUT_PREVIEW_DIR / f"{slug}.jpg")
            shutil.copy2(png_path, SESSION_FILES / f"{slug}.png")
            shutil.copy2(jpg_path, SESSION_FILES / f"{slug}.jpg")
            print(f"Rendered 2x Retina PNG & JPG: {slug} ({png_path.stat().st_size // 1024} KB PNG / {jpg_path.stat().st_size // 1024} KB JPG)")

        browser.close()

    # Build HTML Visual Gallery Index inside infografias/
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
  <title>Serie de Infografías: Benchmark Agentic SOC, SOAR &amp; AppSec (Noviembre 2026)</title>
</head>
<body style="font-family:'Segoe UI',Inter,Arial,sans-serif;background:#f1f5f9;color:#0f172a;margin:0;padding:32px">
  <div style="max-width:1440px;margin:0 auto">
    <header style="background:#0b1f3a;color:#fff;padding:28px 32px;border-radius:14px;margin-bottom:28px">
      <h1 style="margin:0 0 8px 0;font-size:26px">Serie de 7 Infografías Ejecutivas y Técnicas: Agentic SOC, SOAR &amp; AppSec (Nov 2026)</h1>
      <p style="margin:0;color:#bae6fd;font-size:15px">21 archivos generados (7 SVG vectoriales 1920×1200 + 7 PNG Retina 3840×2400 + 7 JPG 3840×2400) con densidad cognitiva controlada y trazabilidad completa.</p>
    </header>
    {''.join(cards_html)}
  </div>
</body>
</html>"""
    (INFOG_DIR / "Galeria_Serie_7_Infografias_Nov2026.html").write_text(gallery_html, encoding="utf-8")
    print("Gallery HTML written successfully.")


if __name__ == "__main__":
    main()

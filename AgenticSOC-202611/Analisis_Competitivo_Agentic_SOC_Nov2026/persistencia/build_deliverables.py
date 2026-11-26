import json
import pathlib
import shutil
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference

BASE_DIR = pathlib.Path(r"C:\Users\scavanna\OneDrive - Microsoft\AB - SOAR LogicApps\Analisis_Competitivo_Agentic_SOC_Nov2026")
PERSIST_DIR = BASE_DIR / "persistencia"
ROOT_SOAR_DIR = pathlib.Path(r"C:\Users\scavanna\OneDrive - Microsoft\AB - SOAR LogicApps")
SESSION_FILES = pathlib.Path(r"C:\Users\scavanna\.scout\copilot\session-state\df4febd6-1b1d-4459-95e6-ab0898615c9a\files")

ms_data = json.loads((PERSIST_DIR / "02_microsoft_baseline_ignite2026.json").read_text(encoding="utf-8"))
comp_data = json.loads((PERSIST_DIR / "03_competidores_12_enterprise_nov2026.json").read_text(encoding="utf-8"))

# Styling palette (Corporate Navy / Slate / Semantic Status)
FONT_FAMILY = "Segoe UI"
TITLE_FILL = PatternFill("solid", fgColor="0F2C59")
SUBTITLE_FILL = PatternFill("solid", fgColor="1B4965")
HEADER_FILL = PatternFill("solid", fgColor="1E3A5F")
SECTION_FILL = PatternFill("solid", fgColor="D9E6F2")
ZEBRA_FILL = PatternFill("solid", fgColor="F7FAFC")
WHITE_FILL = PatternFill("solid", fgColor="FFFFFF")
MS_HIGHLIGHT_FILL = PatternFill("solid", fgColor="EBF5FF")
TOTAL_FILL = PatternFill("solid", fgColor="E2E8F0")

GA_FILL = PatternFill("solid", fgColor="DCFCE7")
GA_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="166534")
PREV_FILL = PatternFill("solid", fgColor="FEF9C3")
PREV_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="854D0E")
EA_FILL = PatternFill("solid", fgColor="FFEDD5")
EA_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="9A3412")
ROAD_FILL = PatternFill("solid", fgColor="FEE2E2")
ROAD_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="991B1B")

TITLE_FONT = Font(name=FONT_FAMILY, size=15, bold=True, color="FFFFFF")
SUBTITLE_FONT = Font(name=FONT_FAMILY, size=10, italic=True, color="E2E8F0")
HEADER_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="FFFFFF")
SECTION_FONT = Font(name=FONT_FAMILY, size=11, bold=True, color="0F2C59")
BODY_FONT = Font(name=FONT_FAMILY, size=10, color="1E293B")
BOLD_FONT = Font(name=FONT_FAMILY, size=10, bold=True, color="0F172A")
LINK_FONT = Font(name=FONT_FAMILY, size=10, color="0369A1", underline="single")

THIN_SIDE = Side(border_style="thin", color="CBD5E1")
MED_NAVY = Side(border_style="medium", color="0F2C59")
GRID_BORDER = Border(left=THIN_SIDE, right=THIN_SIDE, top=THIN_SIDE, bottom=THIN_SIDE)
TOTAL_BORDER = Border(top=MED_NAVY, bottom=MED_NAVY, left=THIN_SIDE, right=THIN_SIDE)

WRAP_TOP = Alignment(wrap_text=True, vertical="top", horizontal="left")
WRAP_CENTER = Alignment(wrap_text=True, vertical="center", horizontal="center")
NUM_CENTER = Alignment(vertical="center", horizontal="center")
NUM_RIGHT = Alignment(vertical="center", horizontal="right")


def add_banner(ws, title, subtitle, max_col):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max_col)
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max_col)
    c1 = ws.cell(1, 1, title)
    c1.font = TITLE_FONT
    c1.fill = TITLE_FILL
    c1.alignment = Alignment(vertical="center", horizontal="left", indent=1)
    ws.row_dimensions[1].height = 30

    c2 = ws.cell(2, 1, subtitle)
    c2.font = SUBTITLE_FONT
    c2.fill = SUBTITLE_FILL
    c2.alignment = Alignment(vertical="center", horizontal="left", indent=1)
    ws.row_dimensions[2].height = 20


def style_headers(ws, row_idx, headers, widths=None):
    ws.row_dimensions[row_idx].height = 28
    for idx, text in enumerate(headers, start=1):
        cell = ws.cell(row_idx, idx, text)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = WRAP_CENTER
        cell.border = GRID_BORDER
        if widths and idx <= len(widths):
            ws.column_dimensions[get_column_letter(idx)].width = widths[idx - 1]


def style_status_cell(cell):
    val = str(cell.value or "")
    u = val.upper()
    if u.startswith("GA") or u == "GA":
        cell.fill = GA_FILL
        cell.font = GA_FONT
    elif "PUBLIC PREVIEW" in u or u == "PREVIEW":
        cell.fill = PREV_FILL
        cell.font = PREV_FONT
    elif "PRIVATE" in u or "GATED" in u or "EARLY ACCESS" in u or "TECH PREVIEW" in u:
        cell.fill = EA_FILL
        cell.font = EA_FONT
    elif "ROADMAP" in u or "PLANEADO" in u or "SIN FECHA" in u:
        cell.fill = ROAD_FILL
        cell.font = ROAD_FONT


def auto_row_height(ws, row_idx, max_col, min_h=22, chars_per_line=52):
    max_lines = 1
    for col_idx in range(1, max_col + 1):
        val = str(ws.cell(row_idx, col_idx).value or "")
        if val.startswith("="):
            continue
        col_w = ws.column_dimensions[get_column_letter(col_idx)].width or 20
        cpl = max(14, int(col_w * 0.9))
        lines = sum(max(1, (len(part) // cpl) + 1) for part in val.split("\n"))
        if lines > max_lines:
            max_lines = lines
    ws.row_dimensions[row_idx].height = min(195, max(min_h, max_lines * 14 + 6))


# ==============================================================================
# WORKBOOK 1: MATRIZ COMPETITIVA 12 FABRICANTES ENTERPRISE (NOV 2026)
# ==============================================================================
def build_workbook_1():
    wb = Workbook()

    # --- TAB 00: RESUMEN EJECUTIVO ---
    ws0 = wb.active
    ws0.title = "00_Resumen_Ejecutivo"
    ws0.views.sheetView[0].showGridLines = True
    add_banner(
        ws0,
        "BENCHMARK COMPETITIVO ENTERPRISE: AGENTIC SOC, SOAR & APPSEC (NOVIEMBRE 2026)",
        "Corte verificado al 25-nov-2026 | Microsoft Ignite 2026 + Navegación en vivo de sitios, documentación técnica y release notes de los 12 fabricantes",
        8,
    )

    # KPI Summary Cards block (rows 4-6)
    kpi_headers = [
        "Fabricantes Enterprise Evaluados",
        "Especialistas Pure-Play Anexos",
        "Hitos / Capacidades Auditadas",
        "% Capacidades en GA Real (Mercado)",
        "Capacidades en Preview / EA / Gated",
        "Fuentes Oficiales Verificadas",
        "Puntaje #1 Ponderado (0-100)",
        "Puntaje Promedio Mercado (0-100)",
    ]
    style_headers(ws0, 4, kpi_headers, [22, 22, 22, 22, 24, 22, 24, 24])
    kpi_formulas = [
        "=COUNTA('01_Matriz_12_Fabricantes'!B5:B16)",
        "=COUNTA('07_Especialistas_y_Playbook'!A5:A10)",
        "=COUNTA('03_Estado_GA_vs_Preview_2026'!D13:D68)",
        "=COUNTIF('03_Estado_GA_vs_Preview_2026'!D13:D68,\"GA*\")/COUNTA('03_Estado_GA_vs_Preview_2026'!D13:D68)",
        "=COUNTA('03_Estado_GA_vs_Preview_2026'!D13:D68)-COUNTIF('03_Estado_GA_vs_Preview_2026'!D13:D68,\"GA*\")",
        "=COUNTA('08_Fuentes_y_Evidencia_Web'!A5:A44)",
        "=MAX('02_Scoring_Ponderado_10Dim'!N6:N17)",
        "=AVERAGE('02_Scoring_Ponderado_10Dim'!N6:N17)",
    ]
    ws0.row_dimensions[5].height = 28
    for idx, f in enumerate(kpi_formulas, start=1):
        c = ws0.cell(5, idx, f)
        c.font = Font(name=FONT_FAMILY, size=13, bold=True, color="0F2C59")
        c.fill = MS_HIGHLIGHT_FILL
        c.alignment = NUM_CENTER
        c.border = GRID_BORDER
        if idx == 4:
            c.number_format = "0.0%"
        elif idx in (7, 8):
            c.number_format = "0.0"

    # Ranking Table linked dynamically to 02_Scoring_Ponderado_10Dim
    ws0.merge_cells("A7:H7")
    sec1 = ws0.cell(7, 1, "RANKING CONSOLIDADO DE LOS 12 FABRICANTES ENTERPRISE (VINCULADO DINÁMICAMENTE AL MODELO DE SCORING)")
    sec1.font = SECTION_FONT
    sec1.fill = SECTION_FILL
    ws0.row_dimensions[7].height = 24

    rank_headers = [
        "Ranking",
        "Fabricante",
        "Categoría Estratégica",
        "Score (0-5)",
        "Índice (0-100)",
        "Brecha vs Microsoft",
        "Oferta Insignia Agentic SOC / AppSec (Nov 2026)",
        "Señal Competitiva / Posicionamiento FY27",
    ]
    style_headers(ws0, 8, rank_headers)

    for i, v in enumerate(comp_data["vendors_12"]):
        r = 9 + i
        s_row = 6 + i  # row in 02_Scoring_Ponderado_10Dim
        row_vals = [
            f"='02_Scoring_Ponderado_10Dim'!O{s_row}",
            f"='02_Scoring_Ponderado_10Dim'!B{s_row}",
            v["tier"],
            f"='02_Scoring_Ponderado_10Dim'!M{s_row}",
            f"='02_Scoring_Ponderado_10Dim'!N{s_row}",
            f"='02_Scoring_Ponderado_10Dim'!P{s_row}",
            v["agentic_soc_offering"],
            v["win_loss_fy27"],
        ]
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        for col_idx, val in enumerate(row_vals, start=1):
            c = ws0.cell(r, col_idx, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_idx in (1, 2, 5) else BODY_FONT
            if col_idx == 1:
                c.alignment = NUM_CENTER
            elif col_idx in (4, 5, 6):
                c.alignment = NUM_RIGHT
                c.number_format = "0.00" if col_idx == 4 else "0.0"
            else:
                c.alignment = WRAP_TOP
        auto_row_height(ws0, r, 8, min_h=28)

    # Architectural Synthesis Table below Ranking
    ws0.merge_cells("A23:H23")
    sec2 = ws0.cell(23, 1, "CONCLUSIONES ARQUITECTÓNICAS CLAVE AL CORTE DE NOVIEMBRE 2026")
    sec2.font = SECTION_FONT
    sec2.fill = SECTION_FILL
    ws0.row_dimensions[23].height = 24

    takeaways = [
        ("1. Tener agentes ya es comodity; el diferenciador es el plano de contexto y actuadores",
         "En sep-nov 2026 los 12 fabricantes anuncian 'Agentic SOC'. La ventaja real de Microsoft reside en unir ISOC en Defender (SIEM+XDR+Data Lake) con actuadores nativos en Entra (identidad), Defender (endpoint/email/cloud), Intune (parcheo/contención) y Purview (datos/DLP)."),
        ("2. Separación limpia de planos en Microsoft (Ignite nov-2026)",
         "Security Copilot asiste al humano e impulsa +18 agentes por dominio; Perception (GA 17-nov-2026) orquesta equipos Red/Blue/Green hacia outcomes; Codename MDASH descubre/prueba vulnerabilidades profundas en código; GHAS Autofix corrige en PRs; Logic Apps ejecuta el SOAR determinístico e híbrido."),
        ("3. Brecha entre titulares de marketing y realidad GA vs Preview en todo el mercado",
         "AWS Continuum es GA solo en 2 regiones US (pentesting en Preview); Google CodeMender e integración con Wiz siguen en Preview/'coming soon'; el AI Kill Switch de CrowdStrike corta solo vía Gateway; ServiceNow AI Passport e IBM Discover & Contain están en Preview/Q4."),
        ("4. Coexistencia híbrida (Logic Apps + ISOC + Perception MCP) frente al 'Rip-and-Replace'",
         "Mientras Palo Alto (XSIAM) y CrowdStrike (Next-Gen SIEM) fuerzan desplazamiento completo de SIEM, Microsoft permite coexistir años con Splunk/QRadar on-prem usando Azure Logic Apps + conectores MCP de Perception y activando ISOC sobre el beneficio E5/E7/Defender Suite.")
    ]
    style_headers(ws0, 24, ["Hallazgo Estratégico", "Evidencia Verificada en Documentación y Sitios Oficiales (Nov 2026)", "", "", "", "", "", ""])
    for idx, (k, desc) in enumerate(takeaways):
        r = 25 + idx
        ws0.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
        ws0.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
        c_k = ws0.cell(r, 1, k)
        c_d = ws0.cell(r, 3, desc)
        c_k.font = BOLD_FONT
        c_d.font = BODY_FONT
        c_k.alignment = WRAP_TOP
        c_d.alignment = WRAP_TOP
        for col_i in range(1, 9):
            ws0.cell(r, col_i).fill = ZEBRA_FILL if idx % 2 == 1 else WHITE_FILL
            ws0.cell(r, col_i).border = GRID_BORDER
        ws0.row_dimensions[r].height = 42

    # Add BarChart to the right of table (Col J)
    chart = BarChart()
    chart.type = "bar"
    chart.style = 10
    chart.title = "Índice Competitivo Ponderado (0-100) - Nov 2026"
    chart.y_axis.title = "Fabricante"
    chart.x_axis.title = "Puntaje Ponderado (0-100)"
    data_ref = Reference(ws0, min_col=5, min_row=8, max_row=20)
    cats_ref = Reference(ws0, min_col=2, min_row=9, max_row=20)
    chart.add_data(data_ref, titles_from_data=True)
    chart.set_categories(cats_ref)
    chart.legend = None
    chart.width = 18
    chart.height = 14
    ws0.add_chart(chart, "J4")
    ws0.freeze_panes = "A9"

    # --- TAB 01: MATRIZ 12 FABRICANTES ---
    ws1 = wb.create_sheet("01_Matriz_12_Fabricantes")
    add_banner(
        ws1,
        "MATRIZ INTEGRAL DE CAPACIDADES: 12 FABRICANTES ENTERPRISE DE SEGURIDAD AGÉNTICA",
        "Comparativa extremo a extremo: SIEM/XDR, SOAR, Agentic SOC, AppSec Agéntico, Gobierno de Agentes IA, Modelos/MCP, Estado GA/Preview y Licenciamiento",
        13,
    )
    h1 = [
        "#", "Fabricante", "Tier / Categoría", "Base SIEM / XDR / Data Lake",
        "SOAR y Automatización", "Oferta Agentic SOC (2026)",
        "AppSec y Vulnerabilidades Agénticas", "Gobierno y Contención de Agentes IA",
        "Estrategia de Modelos y MCP", "Estado Real GA vs Preview (Nov 2026)",
        "Licenciamiento y Modelo Comercial", "Fortalezas Diferenciadoras", "Brechas y Puntos Débiles"
    ]
    w1 = [5, 18, 22, 34, 32, 36, 34, 34, 30, 36, 30, 32, 34]
    style_headers(ws1, 4, h1, w1)
    for i, v in enumerate(comp_data["vendors_12"]):
        r = 5 + i
        vals = [
            v["rank_id"], v["vendor"], v["tier"], v["siem_xdr_foundation"],
            v["soar_automation"], v["agentic_soc_offering"], v["appsec_vuln_agentic"],
            v["agent_governance_insiders"], v["models_and_mcp"], v["ga_vs_preview_nov2026"],
            v["licensing_commercial"], v["key_strengths"], v["key_gaps_watchouts"]
        ]
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        for col_idx, val in enumerate(vals, start=1):
            c = ws1.cell(r, col_idx, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_idx in (1, 2) else BODY_FONT
            c.alignment = NUM_CENTER if col_idx == 1 else WRAP_TOP
        auto_row_height(ws1, r, 13, min_h=55)
    ws1.freeze_panes = "C5"

    # --- TAB 02: SCORING PONDERADO 10 DIMENSIONES ---
    ws2 = wb.create_sheet("02_Scoring_Ponderado_10Dim")
    add_banner(
        ws2,
        "MODELO CUANTITATIVO PONDERADO (10 DIMENSIONES TÉCNICAS Y OPERATIVAS — ESCALA 1 A 5)",
        "Pesos editables en la fila 4 | Fórmulas dinámicas SUMPRODUCT, RANK, AVERAGE, MAX, MIN y Brecha vs Microsoft",
        16,
    )
    dims = comp_data["scoring_dimensions"]
    ws2.cell(4, 1, "PESO").font = BOLD_FONT
    ws2.cell(4, 1).fill = SECTION_FILL
    ws2.cell(4, 1).alignment = NUM_CENTER
    ws2.cell(4, 1).border = GRID_BORDER
    ws2.cell(4, 2, "Ponderación por Dimensión ->").font = BOLD_FONT
    ws2.cell(4, 2).fill = SECTION_FILL
    ws2.cell(4, 2).alignment = WRAP_TOP
    ws2.cell(4, 2).border = GRID_BORDER

    for idx, d in enumerate(dims, start=3):
        c = ws2.cell(4, idx, d["weight"])
        c.font = BOLD_FONT
        c.fill = SECTION_FILL
        c.alignment = NUM_CENTER
        c.number_format = "0%"
        c.border = GRID_BORDER

    c_sum_w = ws2.cell(4, 13, "=SUM(C4:L4)")
    c_sum_w.font = BOLD_FONT
    c_sum_w.fill = GA_FILL
    c_sum_w.alignment = NUM_CENTER
    c_sum_w.number_format = "0%"
    c_sum_w.border = GRID_BORDER
    for extra_col in (14, 15, 16):
        ec = ws2.cell(4, extra_col, "")
        ec.fill = SECTION_FILL
        ec.border = GRID_BORDER

    h2 = ["ID", "Fabricante"] + [f"{d['code']}: {d['name']}" for d in dims] + [
        "Score Ponderado (0-5)", "Índice (0-100)", "Ranking", "Brecha vs MS (pts)"
    ]
    w2 = [6, 22] + [16] * 10 + [16, 15, 11, 16]
    style_headers(ws2, 5, h2, w2)
    ws2.row_dimensions[5].height = 42

    for i, v in enumerate(comp_data["vendors_12"]):
        r = 6 + i
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        c_id = ws2.cell(r, 1, i + 1)
        c_id.alignment = NUM_CENTER
        c_v = ws2.cell(r, 2, v["vendor"])
        c_v.alignment = WRAP_TOP
        for col_i in (1, 2):
            ws2.cell(r, col_i).font = BOLD_FONT
            ws2.cell(r, col_i).fill = fill
            ws2.cell(r, col_i).border = GRID_BORDER

        for j, sc in enumerate(v["scores"], start=3):
            cs = ws2.cell(r, j, sc)
            cs.font = BODY_FONT
            cs.fill = fill
            cs.alignment = NUM_CENTER
            cs.number_format = "0.0"
            cs.border = GRID_BORDER

        c_w5 = ws2.cell(r, 13, f"=SUMPRODUCT($C$4:$L$4,C{r}:L{r})")
        c_w100 = ws2.cell(r, 14, f"=M{r}*20")
        c_rk = ws2.cell(r, 15, f"=RANK(N{r},$N$6:$N$17)")
        c_gap = ws2.cell(r, 16, f"=N{r}-$N$6")
        for col_m, fmt in ((c_w5, "0.00"), (c_w100, "0.0"), (c_rk, "0"), (c_gap, "+0.0;-0.0;0.0")):
            col_m.font = BOLD_FONT
            col_m.fill = fill
            col_m.alignment = NUM_CENTER
            col_m.number_format = fmt
            col_m.border = GRID_BORDER
        ws2.row_dimensions[r].height = 24

    # Summary statistics rows (rows 18-20)
    stats = [
        (18, "PROMEDIO MERCADO (12 FABRICANTES)", "AVERAGE"),
        (19, "MÁXIMO POR DIMENSIÓN", "MAX"),
        (20, "MÍNIMO POR DIMENSIÓN", "MIN"),
    ]
    for r_stat, label, fn in stats:
        ws2.cell(r_stat, 1, "").fill = TOTAL_FILL
        ws2.cell(r_stat, 1).border = TOTAL_BORDER
        cl = ws2.cell(r_stat, 2, label)
        cl.font = BOLD_FONT
        cl.fill = TOTAL_FILL
        cl.border = TOTAL_BORDER
        for col_idx in range(3, 15):
            col_let = get_column_letter(col_idx)
            cf = ws2.cell(r_stat, col_idx, f"={fn}({col_let}6:{col_let}17)")
            cf.font = BOLD_FONT
            cf.fill = TOTAL_FILL
            cf.alignment = NUM_CENTER
            cf.number_format = "0.00" if col_idx == 13 else "0.0"
            cf.border = TOTAL_BORDER
        for extra_col in (15, 16):
            ce = ws2.cell(r_stat, extra_col, "")
            ce.fill = TOTAL_FILL
            ce.border = TOTAL_BORDER
        ws2.row_dimensions[r_stat].height = 22
    ws2.freeze_panes = "C6"

    # --- TAB 03: ESTADO REAL GA VS PREVIEW (NOV 2026) ---
    ws3 = wb.create_sheet("03_Estado_GA_vs_Preview_2026")
    add_banner(
        ws3,
        "AUDITORÍA DE MADUREZ REAL: GA vs. PREVIEW / EARLY ACCESS / ROADMAP (CORTE 25-NOV-2026)",
        "Verificación directa en portales de documentación, changelogs y anuncios oficiales para separar marketing de disponibilidad productiva",
        7,
    )

    cap_items = [
        ("Microsoft", "SOC / Plataforma Agéntica", "Microsoft Perception (Plataforma y Orquestador)", "GA", "2026-11-17", "GA en Ignite 2026; orquesta agentes Red, Blue y Green mediante playbooks y chat.", "SRC-01 / SRC-02"),
        ("Microsoft", "Perception Blue Team", "Alert Triage, Attack Investigation, Detection Authoring y TI Agents (x4)", "GA", "2026-11-17", "4 agentes Blue en GA; razonan también sobre señales 3P (AWS, Okta, Salesforce).", "SRC-01 / SRC-02"),
        ("Microsoft", "Perception Red/Green Team", "Recon Agent (Red) y Posture Prioritization Agent (Green)", "GA", "2026-11-17", "GA en Ignite 2026; cobertura multi-nube Microsoft, AWS y Google Cloud.", "SRC-01 / SRC-04"),
        ("Microsoft", "Perception Red/Green Team", "Web App Pen Test Agent (Red) y Risk Reduction Agent (Green)", "Public Preview", "2026-11-17", "En Public Preview en Ignite 2026; Web Pen Test logró 31.0% en benchmark Incalmo.", "SRC-01 / SRC-02"),
        ("Microsoft", "Perception Ecosistema", "Integraciones MCP / API con SIEM, SOAR e ITSM externos", "Public Preview", "2026-11-17", "Permite disparar playbooks Perception desde herramientas externas y devolver artefactos.", "SRC-01 / SRC-02"),
        ("Microsoft", "SIEM + XDR Unificado", "ISOC in Microsoft Defender (Core: casos, playbooks, UEBA, ingesta 3P)", "GA", "2026-11-17", "GA core + opt-in para clientes Sentinel con E5/E7/Defender Suite ($2.40/GB + Data Lake).", "SRC-01 / SRC-03"),
        ("Microsoft", "SIEM + XDR Unificado", "ISOC: Retención 90 días Defender, Normalización en ingesta y Detections-as-Code", "Public Preview", "2026-11-17", "Capacidades ampliadas de SIEM y Content Hub en Preview durante Ignite 2026.", "SRC-03"),
        ("Microsoft", "Defensa Proactiva", "Vulnerability Shielding en Microsoft Defender", "Public Preview", "2026-11-17", "Protección temporal autónoma entre divulgación de CVE y parche permanente.", "SRC-01 / SRC-03"),
        ("Microsoft", "AppSec Agéntico", "Codename MDASH (repos hasta 5 GB, nubes reguladas, MAI-Cyber-2)", "Private/Gated Preview", "2026-11-17", "Preview expandido por nominación; sin fecha GA pública confirmada; consume tokens Foundry.", "SRC-01 / SRC-05"),
        ("Microsoft", "AppSec / DevSecOps", "GitHub Advanced Security (GHAS) Agentic Autofix en GitHub Enterprise Cloud", "GA", "2026-10-15", "GA en GHEC (rama default, hasta 25 alertas por PR con copilot-swe-agent, $0.01/crédito).", "SRC-07"),
        ("Microsoft", "AppSec / DevSecOps", "GHAS Agentic Autofix para Azure DevOps", "Public Preview", "2026-11-23", "Anunciado en Public Preview el 23-nov-2026 ejecutando jobs en Azure Pipelines.", "SRC-08"),
        ("Microsoft", "Copilot & Agentes", "Microsoft Security Copilot + inclusión en M365 E5/E7 (+18 agentes ecosistema)", "GA", "2025-11-18", "Plataforma GA; agentes individuales combinan GA (Phishing, CA Opt, TI) y Preview (DLP/IRM).", "SRC-06"),
        ("Microsoft", "Gobierno Agentes IA", "Defender Local AI Agent Discovery & Runtime Protection en Windows (60 agentes)", "GA", "2026-11-17", "GA en Windows: inspecciona el agent loop y bloquea instrucciones maliciosas (Claude Code, Copilot CLI, OpenClaw).", "SRC-03"),
        ("Microsoft", "Gobierno Agentes IA", "Postura para agentes cloud 3P (Bedrock, Vertex, Gemini, Claude) vía Agent 365", "Public Preview", "2026-11-17", "Inventario unificado y evaluación de riesgo junto a agentes Foundry y Copilot Studio.", "SRC-03"),
        ("Microsoft", "Datos & IA", "Purview DLP para agentes locales y Grounding Protection sin etiquetado previo", "Roadmap / Ene-2027", "2026-11-17", "Anunciado en Ignite 2026 para entrar en Public Preview en enero de 2027.", "SRC-01"),
        ("Microsoft", "SOAR Empresarial", "Azure Logic Apps (Playbooks Sentinel/Defender + >1.400 conectores + On-Prem Gateway)", "GA", "Producción", "Madurez total en producción para orquestación determinística y coexistencia con Splunk.", "SRC-03"),
        ("CrowdStrike", "Agentic SOC", "Charlotte AI — Investigaciones paralelas multi-agente coordinadas", "GA", "2026-10-06", "GA en octubre 2026 sobre telemetría Falcon; GovCloud aún marcado 'próximamente'.", "SRC-09 / SRC-11"),
        ("CrowdStrike", "Modelos / Harness Cyber", "CrowdStrike SafeMind (con NVIDIA Nemotron + GPT-5.6 Cyber)", "GA / Rollout", "2026-09-01", "Anunciado en Fal.Con Las Vegas sep-2026 combinando agentes ofensivos y defensivos.", "SRC-10 / SRC-40"),
        ("CrowdStrike", "Red Teaming Agéntico", "Charlotte AI Agentic Adversary Emulation", "Early Access", "2026-11-04", "Puesto en Early Access el 4-nov-2026; adquisición de Dreadnode aún no cerrada (Q4 FY27).", "SRC-40"),
        ("CrowdStrike", "Gobierno Agentes IA", "Falcon Guardian + Agent Graph (score 0-100) + AI Kill Switch", "GA Parcial / Limitado", "2026-11-03", "Kill Switch solo corta acceso al modelo vía Falcon AI Gateway; terminación en host/SaaS sin fecha.", "SRC-10 / SRC-40"),
        ("CrowdStrike", "Observabilidad & Red Team IA", "Adquisiciones de Fiddler AI y Dreadnode", "Roadmap / En Cierre", "2026-11-04", "Acuerdos firmados; cierre estimado para Q4 FY27 (no integrados nativamente hoy).", "SRC-40"),
        ("Palo Alto Networks", "SIEM + Agentic SOC", "Cortex XSIAM 3.6 + Cortex AgentiX 1.4 (con JSON Schema & FedRAMP High)", "GA", "2026-07-30", "En producción comercial y autorizado FedRAMP Moderate & High.", "SRC-12 / SRC-13 / SRC-14"),
        ("Palo Alto Networks", "SOAR Dedicado", "Cortex XSOAR 8.15", "GA", "2026-07-30", "GA con exportación nativa a Azure Blob y autenticación continua Strata Logging.", "SRC-14"),
        ("Palo Alto Networks", "Endpoint & Agentes IA", "Cortex XDR 5.2 Agentic Endpoint Security (AES) + Cortex XDR One", "GA", "2026-10-19", "Visibilidad AIDR por sesión, descubrimiento MCP/extensiones y SLMs residentes en endpoint.", "SRC-14 / SRC-40"),
        ("Palo Alto Networks", "Red & Virtual Patching", "PAN-OS 12.2 con Frontier Virtual Patching y Network Security Agents", "GA / Reciente", "2026-10-08", "Presentado en InterSECt oct-2026 para clientes de firewalls Palo Alto.", "SRC-40"),
        ("Palo Alto Networks", "Workflows Lenguaje Natural", "Integración de la adquisición de Console en Cortex workflows", "Public Preview", "2026-09-15", "Adquisición cerrada en sep-2026; controles de rollback y permisos en evolución.", "SRC-40"),
        ("Google Cloud + Wiz", "SIEM + SOAR Unificado", "Google Security Operations (Basic Mode Search, Unified Playbooks, GTI_IOC)", "GA", "2026-11-19", "Actualizaciones continuas en GA; menú unificado SIEM/SOAR en Public Preview (4-nov-2026).", "SRC-15"),
        ("Google Cloud + Wiz", "SOC Triage", "Google SecOps Alert Triage & Investigation Agent", "GA", "2026-04-22", "GA; >5M de alertas analizadas con Gemini.", "SRC-18"),
        ("Google Cloud + Wiz", "Threat Hunting & Detección", "Google SecOps Threat Hunt Agent y Detection Engineering Agent (MCP)", "Public Preview", "2026-10-15", "Threat Hunt Agent en Public Preview solo para clientes Google SecOps Enterprise Plus.", "SRC-15 / SRC-18"),
        ("Google Cloud + Wiz", "AppSec Agéntico", "Google DeepMind CodeMender (escaneo, exploit PoC y parches)", "Public Preview", "2026-07-21", "En Preview sobre Gemini Enterprise Agent Platform; aislamiento actualizado 4-nov-2026; conexión desde Wiz 'coming soon'.", "SRC-17 / SRC-40"),
        ("Google Cloud + Wiz", "Modelos Cyber", "Gemini 4 Carbon para ciberdefensa", "Private/Gated Preview", "2026-10-28", "Acceso inicial restringido a un subconjunto de ciberdefensores.", "SRC-40"),
        ("Google Cloud + Wiz", "Cloud & Agentes", "Wiz Red, Blue & Green Agents + Wiz Defend Sensor Forensics + Wiz AI SAST", "GA", "2026-10-06", "Disponibles con consumo por tokens; Sensor Runtime nativo para GKE en Preview (20-oct-2026).", "SRC-19 / SRC-40"),
        ("Google Cloud + Wiz", "Gobierno Agentes Cloud", "Google SCC descubrimiento automático de agentes/MCP no gestionados en GKE/Cloud Run", "Roadmap / Coming Soon", "2026-04-22", "Documentado como 'coming soon in preview' en Google Cloud Security.", "SRC-18"),
        ("Cisco / Splunk", "SIEM + Agentic SOC", "Splunk Enterprise Security 8.8.0 (Agentic SOC Agents, Detection Builder, Exposure Analytics)", "GA", "2026-11-04", "GA el 4-nov-2026; Agentic SOC orientado a despliegues Cloud / Cloud-Connected.", "SRC-20 / SRC-21"),
        ("Cisco / Splunk", "SOAR", "Splunk SOAR con Automation Broker High Availability y ES-SOAR Cert Mgmt", "GA", "2026-11-04", "Disponible para edición Premier en ES 8.8.", "SRC-20"),
        ("Cisco / Splunk", "XDR & Federación", "Cisco XDR Instant Attack Verification y Cisco Data Fabric (sobre Splunk)", "GA", "2026-08-17", "GA desde agosto 2026; operación deliberadamente human-in-the-loop (no respuesta autónoma).", "SRC-22"),
        ("SentinelOne", "Autonomous SOC", "Singularity ASOC + Purple AI Agentic Investigation + Hyperautomation Closed-Loop", "GA", "2026-10-21", "Purple Agentic Investigation activo desde jun-2026; suite ASOC anunciada 21-oct-2026.", "SRC-23 / SRC-24"),
        ("SentinelOne", "Gobierno Agentes IA", "Singularity Agentic Detection and Response (ADR)", "Early Access", "2026-10-21", "En Early Access desde 21-oct-2026; sensor runtime para VM Claude Cowork solo planeado (2-nov).", "SRC-40"),
        ("AWS", "AppSec Agéntico", "AWS Continuum for Code Vulnerabilities", "GA", "2026-10-22", "GA el 22-oct-2026 pero inicialmente restringido a solo 2 regiones de EE. UU.", "SRC-25 / SRC-40"),
        ("AWS", "Pentesting & Threat Model", "AWS Continuum Penetration Testing y STRIDE Threat Modeling", "Public Preview", "2026-06-17", "En Preview como evolución de AWS Security Agent.", "SRC-25"),
        ("AWS", "Respuesta a Incidentes", "AWS Security Incident Response (con agente IA investigativo + ingenieros 24/7)", "GA", "2026-11-18", "GA para cuentas AWS Organizations sobre hallazgos de GuardDuty y Security Hub.", "SRC-26"),
        ("ServiceNow", "SecOps Workflows", "Now Assist for Security Operations (SIR) + Agente Empresarial Arc", "GA", "2026-10-21", "Arc GA el 21-oct-2026; Now Assist actualizado oct-2026 por niveles de producto.", "SRC-27 / SRC-40"),
        ("ServiceNow", "Gobierno Agentes IA", "AI Control Tower + AI Passport (credencial runtime firmada)", "Public Preview", "2026-10-15", "AI Passport planeado Q4 2026; enforcement en NVIDIA OpenShell pospuesto a release futuro.", "SRC-28 / SRC-40"),
        ("ServiceNow", "Exposición / Ataque", "Alianza ServiceNow + OpenAI para validación y mitigación de rutas de ataque", "Roadmap / Ene-2027", "2026-10-28", "Early Access anunciado recién para enero de 2027.", "SRC-40"),
        ("IBM Security", "Operaciones Autónomas", "IBM Autonomous Security (ATOM + ARGO + ADA) + QRadar SOAR", "GA", "2026-04-08", "Modelo operativo multi-agente desplegado en servicios y suite IBM.", "SRC-29"),
        ("IBM Security", "Gobierno Agentes Multi-Cloud", "watsonx Orchestrate AI Gateway — Discover and Contain (Bedrock, Foundry, Gemini)", "Private/Gated Preview", "2026-10-27", "En Tech Preview tras TechXchange oct-2026.", "SRC-30 / SRC-40"),
        ("Zscaler", "Agentic SOC", "Zscaler Agentic SOC + Risk360 Exposure Management", "GA", "2026-09-09", "Disponible globalmente desde 9-sep-2026 sobre telemetría Zero Trust y Decoy Mesh.", "SRC-31"),
        ("Zscaler", "Protección Apps / DLP", "Autonomous Application Shield (con IBM/Red Hat) y mejoras GovCloud DLP", "Early Access", "2026-10-05", "Anunciado oct-2026; múltiples funciones DLP en disponibilidad limitada.", "SRC-40"),
        ("Elastic", "SOAR Nativo & Triage", "Elastic Workflows (9.4) + Attack Discovery autónomo + 5 Skills AI Agent (9.5)", "GA", "2026-08-04", "GA para clientes Enterprise en Elastic 9.4 / 9.5.", "SRC-32 / SRC-33"),
        ("Elastic", "Capa Agéntica SOC", "Elastic Security 9.6 AlertZero + Elastic nightshift AI SRE", "Public Preview", "2026-11-23", "AlertZero en Technical Preview en serverless (23-nov-2026); ECH/Self-Managed inicios dic-2026.", "SRC-34"),
        ("Fortinet", "SOAR Agéntico + MCP", "FortiSOAR 8.0.0 con FortiAI v6.0.0 (>19 agentes IA) y servidor/cliente MCP", "GA", "2026-10-29", "GA en versión 8.0.0 con servicios fsr-ai y mcp-server nativos.", "SRC-35"),
        ("Fortinet", "Plataforma SOC Cloud", "FortiSOC (consola cloud unificando FortiSIEM, FortiSOAR, FortiAnalyzer y FortiTIP)", "Public Preview", "2026-03-10", "Presentado en Preview en Fortinet Accelerate 2026.", "SRC-36"),
        ("Torq (Especialista)", "HyperSOC / SOAR", "Torq AI SOC Platform + Torq Socrates + Agentic Builder", "GA", "2026-03-18", "En producción en SOCs Fortune 500.", "SRC-37"),
        ("Swimlane (Especialista)", "AI SOC / SOAR", "Swimlane Turbine + Hero AI App Builder + Two-Way MCP + Detecciones propias", "GA", "2026-10-28", "GA el 28-oct-2026.", "SRC-38"),
        ("Snyk (Especialista)", "AppSec & Gobierno Dev IA", "Snyk Evo Agentic Development Security (ADS) + Continuous Offensive Security", "GA", "2026-06-23", "Lanzado en junio 2026 para asegurar agentes de código y servidores MCP.", "SRC-39"),
        ("SailPoint / Okta (Esp.)", "Identidad de Agentes", "SailPoint Agentic Fabric Kill Switch / Okta Runtime Gateway & Kill Switch", "Public Preview", "2026-10-08", "En Preview / Roadmap sin fecha GA confirmada.", "SRC-40"),
    ]

    # Top Summary Table with COUNTIF formulas (rows 4-9)
    style_headers(ws3, 4, ["Estado de Disponibilidad", "Cantidad de Capacidades", "% del Total Auditado", "Interpretación para el CISO / Comprador", "", "", ""], [26, 22, 18, 52, 18, 42, 16])
    statuses_summary = [
        ("GA", "Disponible comercialmente hoy (validar siempre alcance regional y SKU exacto)."),
        ("GA / Rollout", "Anunciado como GA con despliegue gradual o cobertura parcial."),
        ("GA Parcial / Limitado", "Disponible pero con limitaciones arquitectónicas relevantes (ej. solo gateway o pocas regiones)."),
        ("Public Preview", "Prueba pública activa; sujeto a cambios de precio, SLA y alcance antes de GA."),
        ("Private/Gated Preview", "Acceso restringido por nominación o validación previa del fabricante."),
        ("Early Access", "Adopción temprana controlada con cobertura funcional inicial."),
        ("Roadmap / Ene-2027", "Compromiso futuro anunciado oficialmente pero no desplegable en producción hoy."),
    ]
    last_cap_row = 13 + len(cap_items) - 1
    # Wait: let's normalize status labels in cap_items to 5 clean buckets so COUNTIF is 100% exact!
    norm_map = {
        "GA / Rollout": "GA",
        "GA / Reciente": "GA",
        "GA Parcial / Limitado": "GA (Alcance Acotado)",
        "Roadmap / En Cierre": "Roadmap / Futuro",
        "Roadmap / Coming Soon": "Roadmap / Futuro",
        "Roadmap / Ene-2027": "Roadmap / Futuro",
    }
    clean_buckets = [
        ("GA", "Disponibilidad general en producción verificada en documentación/release notes."),
        ("GA (Alcance Acotado)", "GA con restricciones fuertes (ej. corte solo por gateway)."),
        ("Public Preview", "Vista previa pública disponible para evaluación sin SLA productivo completo."),
        ("Private/Gated Preview", "Vista previa privada/restringida por nominación o tech preview."),
        ("Early Access", "Acceso temprano limitado a clientes seleccionados."),
        ("Roadmap / Futuro", "Anunciado para ene-2027, Q4 FY27 o adquisiciones pendientes de cierre."),
    ]
    start_data_row = 13
    end_data_row = start_data_row + len(cap_items) - 1
    for idx_b, (b_name, b_desc) in enumerate(clean_buckets):
        r_b = 5 + idx_b
        ws3.merge_cells(start_row=r_b, start_column=4, end_row=r_b, end_column=7)
        c1 = ws3.cell(r_b, 1, b_name)
        c2 = ws3.cell(r_b, 2, f'=COUNTIF($D${start_data_row}:$D${end_data_row},A{r_b})')
        c3 = ws3.cell(r_b, 3, f"=B{r_b}/$B$11")
        c4 = ws3.cell(r_b, 4, b_desc)
        style_status_cell(c1)
        c1.alignment = NUM_CENTER
        c2.font = BOLD_FONT
        c2.alignment = NUM_CENTER
        c3.font = BOLD_FONT
        c3.alignment = NUM_CENTER
        c3.number_format = "0.0%"
        c4.font = BODY_FONT
        c4.alignment = WRAP_TOP
        for col_i in range(1, 8):
            ws3.cell(r_b, col_i).border = GRID_BORDER
            if col_i > 1:
                ws3.cell(r_b, col_i).fill = WHITE_FILL
        ws3.row_dimensions[r_b].height = 21

    # Total row 11
    ws3.merge_cells("D11:G11")
    ws3.cell(11, 1, "TOTAL CAPACIDADES AUDITADAS").font = BOLD_FONT
    ws3.cell(11, 2, "=SUM(B5:B10)").font = BOLD_FONT
    ws3.cell(11, 2).alignment = NUM_CENTER
    ws3.cell(11, 3, "=SUM(C5:C10)").font = BOLD_FONT
    ws3.cell(11, 3).alignment = NUM_CENTER
    ws3.cell(11, 3).number_format = "0.0%"
    ws3.cell(11, 4, "Cobertura completa de los 12 fabricantes enterprise + especialistas clave.").font = BOLD_FONT
    for col_i in range(1, 8):
        ws3.cell(11, col_i).fill = TOTAL_FILL
        ws3.cell(11, col_i).border = TOTAL_BORDER
    ws3.row_dimensions[11].height = 23

    style_headers(
        ws3, 12,
        ["Fabricante", "Dominio", "Capacidad / Producto Específico", "Estado Real (Nov 2026)", "Fecha Anuncio / Release", "Evidencia Técnica, Alcance y Limitaciones", "Fuente ID"],
        [22, 24, 40, 24, 18, 54, 16]
    )
    for idx_c, (vend, dom, cap, st, dt, notes, src) in enumerate(cap_items):
        r = start_data_row + idx_c
        st_clean = norm_map.get(st, st)
        row_v = [vend, dom, cap, st_clean, dt, notes, src]
        fill = MS_HIGHLIGHT_FILL if vend == "Microsoft" else (ZEBRA_FILL if idx_c % 2 == 1 else WHITE_FILL)
        for col_i, val in enumerate(row_v, start=1):
            c = ws3.cell(r, col_i, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i in (1, 3) else BODY_FONT
            c.alignment = NUM_CENTER if col_i in (4, 5, 7) else WRAP_TOP
            if col_i == 4:
                style_status_cell(c)
        auto_row_height(ws3, r, 7, min_h=26)
    ws3.freeze_panes = "A13"

    # --- TAB 04: SOAR Y COEXISTENCIA MULTI-SIEM ---
    ws4 = wb.create_sheet("04_SOAR_y_Coexistencia_SIEM")
    add_banner(
        ws4,
        "COMPARATIVA PROFUNDA SOAR, HIPERAUTOMATIZACIÓN Y COEXISTENCIA MULTI-SIEM (FOCO LOGIC APPS + ISOC + PERCEPTION)",
        "Evaluación para arquitecturas SOC híbridas (ej. coexistencia plurianual con Splunk/QRadar on-prem + plano único de casos y agentes)",
        9,
    )
    soar_rows = [
        ("Microsoft (Azure Logic Apps + ISOC Playbooks + Perception)", "Nativo PaaS Empresarial + Agéntico Integrado", ">1.400 conectores enterprise + On-Premises Data Gateway + >500 conectores Sentinel/ISOC", "Dual: Playbooks determinísticos auditables (Logic Apps) + Orquestación agéntica por objetivos (Perception)", "Bidireccional (Perception MCP Preview + Logic Apps Custom/MCP Connectors + Sentinel MCP)", "Excelente: convive años con Splunk/QRadar on-prem vía Data Gateway/REST sin forzar ingesta total en Sentinel (aprovecha beneficio E5 + MDC P2).", "Consumo por ejecución centavos USD / Standard plan predecible (TCO muy inferior a SOAR por analista/evento).", "Altísima escalabilidad cloud, RBAC Entra Managed Identity, CI/CD ARM/Bicep.", "Líder para arquitectura híbrida y consolidación progresiva."),
        ("Palo Alto Networks (Cortex XSOAR 8.15 + AgentiX 1.4)", "SOAR Dedicado Líder + Capa Agéntica", ">1.000 packs Marketplace + conectores unificados por fabricante con Vault central en AgentiX 1.4", "Playbooks determinísticos War Room + planes de agentes AgentiX con JSON Schema estricto + Console NL", "Visibilidad de riesgos MCP en endpoint; ejecución centrada en librería de acciones Cortex", "Media: XSOAR standalone convive bien con SIEM 3P, pero la estrategia comercial empuja migración completa hacia Cortex XSIAM.", "Alto costo de licenciamiento enterprise y servicios profesionales/Unit 42.", "Muy maduro, FedRAMP High en AgentiX 1.4, exportación nativa a Azure Blob en 8.15.", "Principal rival técnico en madurez pura de playbooks SecOps."),
        ("CrowdStrike (Falcon Fusion SOAR + Charlotte AI Workflows)", "SOAR Embebido en XDR/Next-Gen SIEM", "Ecosistema Falcon Store + integraciones API/alianza Dynatrace", "Workflows nativos sobre eventos Falcon + ejecución paralela de agentes Charlotte AI / AgentWorks", "Ecosistema cerrado/gobernado AgentWorks sobre plataforma Falcon", "Baja-Media: optimizado para desplazar el SIEM existente hacia Falcon Next-Gen SIEM más que para operar sobre Splunk/QRadar.", "Incluido base en módulos Falcon pero escala en costo con ingesta Next-Gen SIEM y Charlotte AI.", "Muy rápido para acciones de contención en endpoint/identidad conectada.", "Menor amplitud de conectores IT/ERP/on-prem frente a Logic Apps o XSOAR."),
        ("Google Cloud (Google SecOps SOAR - ex Siemplify)", "SOAR Integrado en SIEM Cloud", "~300+ integraciones Marketplace + Publisher Agent 2.7.2 para ejecución remota on-prem", "Playbooks de casos/alertas con post-ingestion triggers, Case Wall colaborativo y Data RBAC", "Detection Engineering Agent opera vía cliente MCP (Antigravity / Claude Code)", "Media: SOAR muy acoplado a Google SecOps SIEM; menos común hoy como capa SOAR neutral sobre SIEMs on-prem externos.", "Empaquetado en Google SecOps Enterprise / Enterprise Plus.", "Buena ergonomía de Case Wall y agrupación de alertas.", "Rollback reciente en GitSync v53->v54 (oct-2026); sin actuadores nativos de endpoint/correo corporativo."),
        ("Cisco / Splunk (Splunk SOAR + ES 8.8 Guided Response)", "SOAR Acoplado a SIEM Híbrido", ">350 apps en Splunkbase + Automation Broker con Alta Disponibilidad (HA) en ES 8.8", "Playbooks Python/visuales en Splunk SOAR + respuesta guiada human-in-the-loop en ES 8.8 / Cisco XDR", "MCP Server for Splunk Platform incorporado en documentación ES 8.8", "Alta con Splunk on-prem (gestión self-service de certificados ES-SOAR en 8.8), pero menor agilidad multi-nube fuera del stack Splunk/Cisco.", "Licenciamiento Premier / add-on costoso sumado al costo de ingesta Splunk.", "Fuerte gobernanza y trazabilidad forense para auditoría.", "Complejidad operativa de mantener infraestructura dual ES + SOAR + brokers."),
        ("SentinelOne (Singularity Hyperautomation + Purple AI)", "No-Code Hyperautomation Embebido", "Catálogo Singularity Marketplace + webhooks/APIs", "Workflows gráficos no-code capaces de invocar investigaciones autónomas de Purple AI en cualquier paso (ago-2026)", "Integración centrada en APIs Singularity", "Baja-Media: diseñado como suite cerrada Singularity ASOC (oct-2026) más que como orquestador empresarial multi-SIEM.", "Bundled en Singularity ASOC / módulos Hyperautomation.", "Tiempo de implementación muy corto y límites claros de autonomía/aprobación humana.", "Ecosistema enterprise/ITSM/legacy más acotado que Logic Apps, ServiceNow o XSOAR."),
        ("ServiceNow (SecOps SIR + Flow Designer + Now Assist)", "Plano Enterprise ITSM/SOAR", " Amplio ecosistema IntegrationHub + CMDB empresarial + AI Control Tower", "Workflows estructurados ITSM/SIR + Agentic Workflows en Now Assist (oct-2026) + agente Arc", "Gobierno runtime de alcances MCP mediante credenciales firmadas AI Passport (Q4 2026)", "Alta como plano superior de tickets/casos sobre cualquier SIEM (Splunk, Sentinel), pero requiere otro motor para detección y contención técnica.", "Muy alto (licencias SIR/VR + uplift Pro Plus / Enterprise Plus).", "Estándar de facto en flujos de aprobación inter-áreas, CMDB y GRC.", "No reemplaza la automatización técnica de baja latencia en el SOC; alto costo y fricción."),
        ("Fortinet (FortiSOAR 8.0.0 + FortiAI v6.0.0)", "SOAR Dedicado Full-Featured + Agéntico", ">500 conectores + Content Hub autenticado + caza conectable a FortiSIEM y Splunk", "Playbooks robustos + motor agéntico de hipótesis múltiples + >19 agentes IA preconstruidos", "Soporte MCP bidireccional GA en 8.0.0 (consume MCP externos y expone conectores como MCP server)", "Alta: FortiSOAR 8.0 puede operar standalone sobre Splunk o FortiSIEM e incluye módulo de identidades y TIM.", "Competitivo por asiento/nodo frente a XSOAR y ServiceNow.", "Arquitectura técnica muy completa en v8.0 (servicios fsr-ai y mcp-server).", "Requiere gestión de appliance/infraestructura FortiSOAR y re-licenciamiento en upgrade 8.0."),
        ("Elastic (Elastic Workflows 9.4+ + AlertZero 9.6)", "Automatización Nativa en Motor de Datos", "Conectores Elasticsearch / webhooks / sistemas de tickets", "Combina automatización determinística por scripts y razonamiento de Elastic AI Agent sobre los datos", "Conector multi-LLM abierto y Agent Builder", "Baja fuera de Elastic: vive dentro del clúster Elasticsearch para evitar un SOAR externo, no para orquestar SIEMs terceros.", "Incluido en suscripción Elastic Enterprise.", "Cero latencia de movimiento de datos entre búsqueda ES|QL y acción.", "Madurez reciente (GA may-2026; authoring agéntico aún experimental)."),
        ("Torq / Swimlane (Pure-Play HyperSOC)", "Orquestadores Agénticos Cloud-Native Agnósticos", "Centenares de integraciones API/webhook sin código", "Torq Socrates + Agentic Builder / Swimlane Turbine + Hero AI App Builder", "Swimlane ofrece MCP bidireccional GA (28-oct-2026)", "Alta neutralidad multi-vendor, pero introducen otro silo de datos/credenciales y costo anual significativo ($150k-$500k+).", "Suscripción anual dedicada de plataforma AI SOC/SOAR.", "UX moderna tipo 'Cursor para SecOps' y rápida creación de flujos por prompts.", "Sin telemetría propia, sin Data Lake nativo y duplican capacidades ya incluidas en Azure Logic Apps + Perception.")
    ]
    h4 = [
        "Fabricante y Solución SOAR", "Arquitectura", "Ecosistema de Conectores",
        "Modelo Determinístico vs Agéntico", "Soporte MCP (Nov 2026)",
        "Coexistencia con SIEM On-Prem (ej. Splunk)", "Modelo de Costos / TCO",
        "Fortaleza Operativa", "Limitación Principal"
    ]
    w4 = [26, 22, 30, 34, 28, 36, 26, 30, 30]
    style_headers(ws4, 4, h4, w4)
    for i, row_v in enumerate(soar_rows):
        r = 5 + i
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        for col_i, val in enumerate(row_v, start=1):
            c = ws4.cell(r, col_i, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i == 1 else BODY_FONT
            c.alignment = WRAP_TOP
        auto_row_height(ws4, r, 9, min_h=48)
    ws4.freeze_panes = "B5"

    # --- TAB 05: APPSEC Y VULNERABILIDADES AGÉNTICAS ---
    ws5 = wb.create_sheet("05_AppSec_y_Vuln_Agentica")
    add_banner(
        ws5,
        "BENCHMARK DE SEGURIDAD DE APLICACIONES Y DESCUBRIMIENTO/REMEDIACIÓN AGÉNTICA DE VULNERABILIDADES",
        "Comparativa de Codename MDASH + Perception Web Pen Test + GitHub Copilot/GHAS Autofix frente a Google CodeMender, AWS Continuum, Wiz y Snyk",
        8,
    )
    appsec_rows = [
        ("Microsoft (Codename MDASH + GHAS Agentic Autofix + Perception Web Pen Test)", "MDASH: Expanded Preview (nov-2026) | GHAS Autofix: GA GHEC (15-oct-2026) y Preview ADO (23-nov-2026) | Web Pen Test: Preview", "Pipeline de 5 etapas (Prepare -> Scan [>100 subagentes] -> Validate [LSP + debate multi-modelo] -> Dedupe -> Prove [PoC/fuzzing]) + validación dinámica web en Perception.", "Sí: MDASH construye inputs desencadenantes/PoC y alimenta al Web App Pen Test Agent (31.0% solve rate en Incalmo, 2x Codex).", "Sí (GA en GHEC): copilot-swe-agent explora múltiples archivos, propone fix, re-ejecuta CodeQL para confirmar cierre y abre PR (hasta 25 alertas juntas).", "5 especialistas (Java, C/C++, C#, JS/TS, Python) + 9 generalistas (Go, Rust, Kotlin, PHP, Ruby, Swift, Obj-C/C++, Zig); repos hasta 5 GB.", "Tokens Microsoft Foundry para MDASH + $0.01 USD por GitHub AI Credit en GHAS Autofix.", "Único flujo completo: Código profundo (MDASH) -> Explotabilidad web (Perception) -> Exposición en Defender -> PR verificado (GHAS)."),
        ("Google Cloud + Wiz (CodeMender + Wiz AI SAST + Wiz Red/Green Agents)", "CodeMender: Public Preview (jul/nov-2026) | Wiz AI SAST: GA (6-oct-2026) | Invocación Wiz->CodeMender: 'Coming Soon'", "Agente nacido en Google DeepMind sobre Gemini Enterprise Agent Platform con aislamiento VPC, cero retención y grafo cloud Wiz.", "Sí: ejecuta exploits de prueba de concepto en sandbox para confirmar explotabilidad real y priorizar con Wiz Red Agent.", "Sí (Preview en CodeMender): genera parches probados usando LLM-as-a-judge para no romper funcionalidad y soporta migración a lenguajes memory-safe.", "Código 1P, open-source y 3P vía CLI, CI/CD, VS Code y Google Antigravity.", "Consumo Gemini Enterprise Agent Platform + tokens flexibles de Wiz Agents.", "Muy potente en investigación IA, pero CodeMender sigue en Preview y el puente completo con Wiz aún figura 'coming soon'."),
        ("AWS (AWS Continuum + Security Agent + Kiro/Claude Plugins)", "Continuum Code Vulns: GA en 2 regiones US (22-oct-2026) | Pentesting y STRIDE Threat Modeling: Preview", "Grafo de contexto de negocio/entorno AWS + validación aislada en sandbox + mitigaciones rápidas reversibles + fix duradero.", "Sí: construye prueba reproducible en sandbox aislado (AWS reportó explotación de 33 de 37 CVEs reales en pruebas internas).", "Sí: escaneo de PRs y remediación en plataformas Git principales + integración IDE con Kiro power, plugin Claude Code y MCP.", "Amplio soporte de lenguajes modernos y documentos de diseño para modelado STRIDE.", "Facturación por consumo regional AWS (disponible inicialmente solo en 2 regiones de EE. UU.).", "Competidor directo más cercano a MDASH+GHAS en nube, pero limitado geográficamente hoy (2 regiones US) y acotado al ecosistema AWS."),
        ("Palo Alto Networks (Unit 42 Continuous Frontier AI Defense + Prisma/Cortex Cloud)", "Disponible vía servicios Unit 42 / Cortex Cloud + PAN-OS 12.2 Virtual Patching (oct-2026)", "Combina modelos frontera de OpenAI y Anthropic con telemetría Cortex y expertos Unit 42 para descubrir y validar exploits.", "Sí (asistido por modelos y Unit 42 en entornos controlados).", "Orientado a virtual patching en red (PAN-OS 12.2) y guías de remediación; menor natividad en PRs de desarrollador frente a GitHub.", "Multi-lenguaje vía Cortex Cloud AppSec.", "Servicios Unit 42 + suscripción Cortex Cloud / NGFW.", "Fuerte en mitigación perimetral inmediata (Virtual Patching), pero dependiente de servicios gestionados y sin control nativo de GitHub."),
        ("CrowdStrike (SafeMind Offensive Agents + Adquisición Dreadnode)", "SafeMind: anunciado sep-2026 | Agentic Adversary Emulation: EA (4-nov-2026) | Dreadnode: cierre Q4 FY27", "Agentes ofensivos validan hipótesis de ataque frente a agentes defensivos sobre telemetría Falcon e infraestructura NVIDIA Nemotron.", "Validación de rutas de ataque a nivel endpoint/identidad/cloud, no análisis profundo de código fuente tipo SAST/MDASH.", "No posee motor nativo de autofix de código fuente ni generación de PRs en repositorios.", "N/A para SAST profundo propio (depende de socios).", "Módulos Falcon / servicios.", "Excelente para emulación adversaria SOC, pero no compite nativamente en seguridad de código fuente."),
        ("Snyk (Evo Agentic Development Security + Continuous Offensive Security)", "GA / Rollout desde 23-jun-2026", "AI Security Fabric: Evo COS simula ataques ofensivos y Evo ADS gobierna en tiempo real lo que usan y generan los agentes de código.", "Sí: Evo COS prueba vulnerabilidades explotables de forma continua.", "Sí: DeepCode AI / Evo corrige vulnerabilidades en el momento de creación del código dentro del IDE/agente.", "Amplia matriz de lenguajes, dependencias open-source, contenedores e IaC; gobierna servidores MCP y skills.", "Suscripción por desarrollador AppSec enterprise.", "Especialista muy sólido en DevSecOps y cadena de suministro MCP, pero desconectado de la operación nativa XDR/SIEM/Identidad del SOC.")
    ]
    h5 = [
        "Fabricante / Solución AppSec Agéntica", "Estado Real (Nov 2026)",
        "Arquitectura del Harness Agéntico", "¿Prueba Explotabilidad Real (PoC / Sandbox)?",
        "¿Genera Autofix Verificado en Código / PR?", "Cobertura de Lenguajes y Escala",
        "Modelo de Consumo / Costo", "Diferenciación / Brecha frente a Microsoft"
    ]
    w5 = [28, 26, 34, 30, 32, 28, 26, 34]
    style_headers(ws5, 4, h5, w5)
    for i, row_v in enumerate(appsec_rows):
        r = 5 + i
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        for col_i, val in enumerate(row_v, start=1):
            c = ws5.cell(r, col_i, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i == 1 else BODY_FONT
            c.alignment = WRAP_TOP
        auto_row_height(ws5, r, 8, min_h=52)
    ws5.freeze_panes = "B5"

    # --- TAB 06: GOBIERNO DE AGENTES IA E INSIDERS AGÉNTICOS ---
    ws6 = wb.create_sheet("06_Gobierno_Agentes_Insiders")
    add_banner(
        ws6,
        "GOBIERNO, IDENTIDAD Y CONTENCIÓN RUNTIME DE AGENTES IA ('AGENTIC INSIDERS' — NOV 2026)",
        "Pregunta crítica en cuentas enterprise: ¿Quién puede descubrir agentes locales/cloud, revocar su identidad, aplicar políticas de datos y detenerlos hoy?",
        8,
    )
    gov_rows = [
        ("Microsoft (Agent 365 + Entra Agent ID + Defender + Purview + Intune)", "Local Discovery & Runtime Protection Windows: GA (nov-2026) | Cloud 3P Posture & Dynamic Risk: Preview | Purview Agent DLP: Preview ene-2027", "60 tipos de agentes locales (Claude Code, Codex, GitHub Copilot CLI, OpenClaw, ChatGPT Desktop) + agentes cloud en Foundry, Copilot Studio, Bedrock, Vertex y Gemini.", "Sí (Nativo): Microsoft Entra Agent ID dedicado con Conditional Access dinámico, ID Protection y permisos temporales por tarea.", "Sí (GA en Windows): inspecciona puntos críticos del agent loop en el SO y bloquea instrucciones maliciosas antes de actuar + contención Intune.", "Sí: Purview DSPM for AI, clasificación compartida y DLP sobre prompts, archivos y tráfico de agentes.", "Completa: bloquea el loop local en el endpoint, revoca la sesión/identidad en Entra/GitHub y corta acceso a datos sensibles.", "Único plano integral Identidad + OS Endpoint + Datos + Red."),
        ("CrowdStrike (Falcon Guardian + Agent Graph + AI Kill Switch)", "Falcon Guardian & Agent Graph: GA parcial (oct/nov-2026) | Adquisición Fiddler AI: Q4 FY27", "Agentes en endpoints gestionados + hooks de políticas en M365 Copilot, GitHub Copilot, Claude Code, Codex y Cursor.", "No posee IdP propio (depende de Okta/Entra para revocar credenciales reales).", "Parcial: Falcon Guardian inspecciona prompts/tool calls, pero la terminación completa en host y contención browser/SaaS no tienen fecha.", "Limitada a políticas de prompt/endpoint; sin plataforma integral de clasificación y gobierno de datos empresariales como Purview.", "Limitada a Gateway: el AI Kill Switch solo corta la conexión al modelo vía Falcon AI Gateway/3P gateway y bloquea relanzamiento; no cubre modelos locales.", "Fuerte visibilidad endpoint, pero su Kill Switch anunciado en nov-2026 es más estrecho que el titular."),
        ("Palo Alto Networks (Cortex XDR 5.2 AES + Cortex XDR One + Prisma Browser)", "GA (jul-2026 en XDR 5.2 / 19-oct-2026 en XDR One)", "Descubre agentes IA, plataformas dev, extensiones IDE, servidores MCP, skills, plugins, repos clonados y cuentas personales Shadow AI.", "Indirecta: dispara MFA o restricción vía integraciones con Microsoft Entra, Okta o AD on-prem (ITDR 2.0).", "Sí (Fuerte en Endpoint y Browser): guardrails en tiempo real en el agente XDR y SLMs locales bloquean comandos destructivos y fuga de API keys.", "DLP en Prisma Browser y escaneo de archivos en endpoint hasta 300 MB.", "Buena en endpoint/red/browser gestionado por Palo Alto; sin propiedad nativa del plano de identidad cloud ni datos M365.", "Uno de los competidores más sólidos en runtime endpoint para desarrolladores."),
        ("ServiceNow (Super Intelligence / AI Control Tower + AI Passport)", "Control Tower base: GA | AI Passport: Q4 2026 (enforcement OpenShell en release futuro)", "Inventaría agentes, modelos y servidores MCP en la CMDB empresarial (incluyendo conectores hacia Agent 365) y detecta Shadow AI en red.", "AI Passport (credencial firmada criptográficamente en runtime para verificar alcance y delegación acotada paso a paso).", "No posee agente de endpoint ni firewall propio: el bloqueo real requiere que plataformas de terceros respeten y ejecuten AI Passport.", "Gobierno basado en flujos GRC/aprobaciones, no inspección DLP profunda de archivos o memoria.", "Dependiente de terceros: 'encuentra y marca' en CMDB, pero necesita sistemas externos de identidad/seguridad para contener en la práctica.", "Excelente catálogo GRC/CMDB, pero no es un control de seguridad runtime autónomo por sí solo."),
        ("IBM (watsonx Orchestrate AI Gateway + Discover & Contain + Agent Identity)", "Discover & Contain: Tech Preview (27-oct-2026) | HashiCorp Vault / Guardium AI: GA", "Descubre agentes, modelos y servidores MCP terceros en Amazon Bedrock, Microsoft Foundry y Google Gemini.", "IBM Agent Identity complementado con HashiCorp Vault para acceso least-privilege a secretos y credenciales.", "Premium Runtime con aislamiento de contenedores virtualizado por hardware y cero movimiento lateral para agentes alojados allí.", "Guardium AI Security y catálogo gobernado alineado a EU AI Act, OWASP y CoSAI.", "En Tech Preview para agentes multi-nube externos; muy sólido para agentes que corren dentro de su propio Premium Runtime/Gateway.", "Atractivo en banca/sectores regulados por enfoque de cumplimiento EU AI Act y Vault."),
        ("Okta & SailPoint (Agent SSO / Blueprint Alliance / Agentic Fabric)", " Capacidades clave de runtime authorization y Kill Switch en Preview / Roadmap sin fecha GA", "Descubrimiento de identidades de máquina, OAuth tokens, conexiones agent-to-agent y propietarios de credenciales.", "Foco central: SSO de agentes, certificaciones de acceso, gobierno de ciclo de vida y delegación trazable.", "Sin sensor de endpoint ni control del sistema operativo donde corren agentes locales.", "Sin motor DLP nativo (dependen de socios como Zscaler, Proofpoint o Cyera).", "En construcción: los switches de corte anunciados en oct-2026 están en Preview (SailPoint) o planeados (Okta gateway).", "Cubren bien la capa OAuth/IGA, pero no ven ni frenan procesos locales ni prompts maliciosos en el dispositivo.")
    ]
    h6 = [
        "Fabricante / Solución", "Estado Real (Nov 2026)", "Descubrimiento (Local, Cloud, MCP)",
        "Identidad y Autorización del Agente", "Protección Runtime en Endpoint / OS",
        "Política de Datos y DLP sobre el Agente", "Realidad del 'Kill Switch' / Contención Hoy",
        "Conclusión Arquitectónica"
    ]
    w6 = [28, 26, 32, 30, 32, 30, 34, 30]
    style_headers(ws6, 4, h6, w6)
    for i, row_v in enumerate(gov_rows):
        r = 5 + i
        fill = MS_HIGHLIGHT_FILL if i == 0 else (ZEBRA_FILL if i % 2 == 1 else WHITE_FILL)
        for col_i, val in enumerate(row_v, start=1):
            c = ws6.cell(r, col_i, val)
            c.fill = fill
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i == 1 else BODY_FONT
            c.alignment = WRAP_TOP
        auto_row_height(ws6, r, 8, min_h=50)
    ws6.freeze_panes = "B5"

    # --- TAB 07: ESPECIALISTAS Y PLAYBOOK COMPETE ---
    ws7 = wb.create_sheet("07_Especialistas_y_Playbook")
    add_banner(
        ws7,
        "ECOSISTEMA DE ESPECIALISTAS PURE-PLAY Y PLAYBOOK DE POSICIONAMIENTO COMPETITIVO PARA EL CISO",
        "Sección A: Retadores especialistas (SOAR, AppSec, Identidad, Labs IA) | Sección B: Preguntas de contraste y manejo de objeciones en cuentas",
        6,
    )
    style_headers(ws7, 4, ["Fabricante Especialista", "Categoría", "Oferta y Anuncios Verificados 2026", "Estado (Nov 2026)", "Arquitectura y MCP", "Ángulo Competitivo frente a Microsoft"], [22, 26, 38, 20, 36, 42])
    for i, sp in enumerate(comp_data["specialists"]):
        r = 5 + i
        vals = [sp["vendor"], sp["category"], sp["flagship_2026"], sp["status"], sp["mcp_and_arch"], sp["compete_angle_vs_ms"]]
        for col_i, val in enumerate(vals, start=1):
            c = ws7.cell(r, col_i, val)
            c.fill = ZEBRA_FILL if i % 2 == 1 else WHITE_FILL
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i == 1 else BODY_FONT
            c.alignment = NUM_CENTER if col_i == 4 else WRAP_TOP
            if col_i == 4:
                style_status_cell(c)
        auto_row_height(ws7, r, 6, min_h=38)

    ws7.merge_cells("A12:F12")
    sec_pb = ws7.cell(12, 1, "PLAYBOOK DE ARQUITECTURA Y CONTRASTE EN REUNIONES EJECUTIVAS / TÉCNICAS")
    sec_pb.font = SECTION_FONT
    sec_pb.fill = SECTION_FILL
    ws7.row_dimensions[12].height = 24

    playbook_rows = [
        ("vs. CrowdStrike (Charlotte AI + SafeMind + Next-Gen SIEM)", "Presionan con costo de ingesta SIEM (alianza Dynatrace) y velocidad de agentes EDR.", "¿Cómo construye su IA contexto completo sobre correo, archivos sensibles, políticas Conditional Access y código fuente, y cómo revoca la identidad o frena un agente con modelo local fuera de su AI Gateway?", "Mostrar ISOC ($2.40/GB + 90d Defender + Data Lake) + Perception Red/Blue/Green + revocación completa Entra Agent ID + Purview DLP."),
        ("vs. Palo Alto Networks (Cortex XSIAM 3.6 + AgentiX 1.4)", "Empujan 'Platformization' (reemplazo total de SIEM+SOAR+EDR) apalancando su base de firewalls.", "¿Cuánto dura y cuesta migrar todo el SOC a XSIAM antes de que AgentiX entregue valor, y quién gobierna nativamente Entra ID, M365 e Intune cuando acaba el periodo promocional?", "Posicionar adopción sin rip-and-replace: activar ISOC y Perception sobre señales E5/E7 que el cliente ya genera y coexistir con terceros vía Logic Apps y MCP."),
        ("vs. Google Cloud + Wiz (AI Threat Defense + CodeMender)", " Combinan benchmarks de modelos Gemini, grafo cloud Wiz y visión autónoma código-a-nube.", "¿Cuántas consolas y contratos separados requiere hoy operar Google SecOps + Wiz + su EDR/IdP/Email externos, y qué partes de CodeMender<->Wiz están realmente en GA hoy versus 'coming soon'?", "Contrastar con integración nativa en un único portal Defender (ISOC + Perception + Exposure Management + MDASH + GitHub)."),
        ("vs. Cisco / Splunk (ES 8.8 + Splunk SOAR + Cisco XDR)", "Defienden la inercia del SIEM on-prem instalado y la auditoría human-in-the-loop.", "¿Por qué pagar doble ingesta y licencias Premier adicionales cuando el propio Splunk AI Assistant recurre a Azure OpenAI para mejorar calidad de respuesta?", "No pelear un reemplazo traumático día 1: posicionar coexistencia híbrida con Logic Apps + Perception MCP mientras se activa Sentinel/ISOC dentro del beneficio E5 y Defender for Servers P2."),
        ("vs. AWS (AWS Continuum + Security Incident Response)", "Entran por equipos cloud/DevOps con validación de vulnerabilidades en código y compromisos EDP.", "¿Cómo protege AWS Continuum o Security Incident Response sus laptops corporativas, correo, Active Directory, identidades Entra, SaaS o cargas fuera de las 2 regiones US donde Continuum es GA?", "Reconocer valor en cargas AWS puras, pero demostrar cobertura multi-nube real (Microsoft + AWS + GCP + Okta + GitHub) desde Perception, Defender for Cloud y GHAS."),
        ("vs. ServiceNow (Now Assist SecOps + AI Control Tower)", "Se posicionan ante CIO/CISO como la torre de control neutral de flujos y agentes IA.", "Cuando Control Tower detecta un agente comprometido en la CMDB, ¿puede bloquear el proceso en Windows, cortar el acceso al archivo confidencial o revocar el token sin llamar a Microsoft?", "Coexistencia clara: ServiceNow como sistema de tickets ITSM/CMDB corporativo; Microsoft (Agent 365 + Entra + Defender + Purview + Perception) como plano real de sensores y ejecución de seguridad.")
    ]
    style_headers(ws7, 13, ["Escenario Competitivo", "Táctica Habitual del Competidor", "Pregunta de Contraste Arquitectónico (Due Diligence)", "Respuesta y Arquitectura Recomendada Microsoft", "", ""])
    for idx_p, (sc, tac, q, ans) in enumerate(playbook_rows):
        r = 14 + idx_p
        ws7.merge_cells(start_row=r, start_column=4, end_row=r, end_column=6)
        ws7.cell(r, 1, sc).font = BOLD_FONT
        ws7.cell(r, 2, tac).font = BODY_FONT
        ws7.cell(r, 3, q).font = BODY_FONT
        ws7.cell(r, 4, ans).font = BODY_FONT
        for col_i in range(1, 7):
            ws7.cell(r, col_i).fill = ZEBRA_FILL if idx_p % 2 == 1 else WHITE_FILL
            ws7.cell(r, col_i).border = GRID_BORDER
            ws7.cell(r, col_i).alignment = WRAP_TOP
        ws7.row_dimensions[r].height = 48
    ws7.freeze_panes = "A5"

    # --- TAB 08: FUENTES Y EVIDENCIA WEB ---
    ws8 = wb.create_sheet("08_Fuentes_y_Evidencia_Web")
    add_banner(
        ws8,
        "REGISTRO DE TRAZABILIDAD Y FUENTES PRIMARIAS VERIFICADAS (NOVIEMBRE 2026)",
        "Portales de documentación, release notes, blogs de producto, changelogs y corpus autorizado consultados para esta matriz",
        6,
    )
    style_headers(ws8, 4, ["ID Fuente", "Fabricante", "Tipo de Fuente", "Fecha Publicación / Corte", "Título del Documento / Release Note", "URL Oficial / Ubicación Verificada"], [12, 20, 30, 20, 48, 65])
    for i, s in enumerate(comp_data["sources"]):
        r = 5 + i
        vals = [s["id"], s["vendor"], s["type"], s["date"], s["title"], s["url"]]
        for col_i, val in enumerate(vals, start=1):
            c = ws8.cell(r, col_i, val)
            c.fill = ZEBRA_FILL if i % 2 == 1 else WHITE_FILL
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i in (1, 2) else (LINK_FONT if col_i == 6 and str(val).startswith("http") else BODY_FONT)
            if col_i == 6 and str(val).startswith("http"):
                c.hyperlink = val
            c.alignment = NUM_CENTER if col_i in (1, 4) else WRAP_TOP
        ws8.row_dimensions[r].height = 24
    ws8.freeze_panes = "A5"

    out_path = BASE_DIR / "Matriz_Competitiva_Agentic_SOC_12_Fabricantes_Nov2026.xlsx"
    wb.save(str(out_path))
    shutil.copy2(out_path, ROOT_SOAR_DIR / "Matriz_Competitiva_Agentic_SOC_12_Fabricantes_Nov2026.xlsx")
    shutil.copy2(out_path, SESSION_FILES / "Matriz_Competitiva_Agentic_SOC_12_Fabricantes_Nov2026.xlsx")
    return out_path


# ==============================================================================
# WORKBOOK 2: CATÁLOGO TÉCNICO MICROSOFT AGENTIC SECURITY (IGNITE NOV 2026)
# ==============================================================================
def build_workbook_2():
    wb = Workbook()

    # --- TAB 00: ARQUITECTURA 6 PLANOS ---
    ws0 = wb.active
    ws0.title = "00_Arquitectura_6_Planos"
    add_banner(
        ws0,
        "CATÁLOGO TÉCNICO MICROSOFT AGENTIC SECURITY — IGNITE NOVIEMBRE 2026",
        "Arquitectura integrada sin solapamientos: ISOC in Defender + Perception + Security Copilot (+18 agentes) + Codename MDASH + GHAS + Logic Apps SOAR",
        6,
    )
    style_headers(
        ws0, 4,
        ["Agentes Perception Documentados", "Agentes Perception en GA", "Agentes Security Copilot Nativos", "Planos Arquitectónicos", "Lenguajes Soportados MDASH", "Corte Documental"],
        [24, 22, 26, 22, 24, 22]
    )
    kpis = [
        "=COUNTA('01_Perception_Red_Blue_Green'!B5:B13)",
        "=COUNTIF('01_Perception_Red_Blue_Green'!C5:C13,\"*GA*\")",
        "=COUNTA('02_Security_Copilot_Agentes'!B5:B22)",
        "=COUNTA(A8:A13)",
        "=COUNTA('03_MDASH_y_GHAS_Autofix'!A16:A29)",
        "2026-11-25",
    ]
    ws0.row_dimensions[5].height = 28
    for idx, f in enumerate(kpis, start=1):
        c = ws0.cell(5, idx, f)
        c.font = Font(name=FONT_FAMILY, size=13, bold=True, color="0F2C59")
        c.fill = MS_HIGHLIGHT_FILL
        c.alignment = NUM_CENTER
        c.border = GRID_BORDER

    style_headers(
        ws0, 7,
        ["Plano Arquitectónico", "Productos / Componentes Microsoft", "Estado Real (Nov 2026)", "Capacidades Técnicas Verificadas", "Rol Específico y Diferenciación Interna", ""],
        [28, 30, 26, 48, 38, 8]
    )
    for idx, pl in enumerate(ms_data["architectural_planes"]):
        r = 8 + idx
        ws0.merge_cells(start_row=r, start_column=5, end_row=r, end_column=6)
        vals = [pl["plane"], pl["products"], pl["status_nov_2026"], pl["key_capabilities"], pl["role_vs_others"]]
        for col_i, val in enumerate(vals, start=1):
            c = ws0.cell(r, col_i, val)
            c.font = BOLD_FONT if col_i in (1, 2) else BODY_FONT
            c.alignment = WRAP_TOP
        for col_i in range(1, 7):
            ws0.cell(r, col_i).fill = ZEBRA_FILL if idx % 2 == 1 else WHITE_FILL
            ws0.cell(r, col_i).border = GRID_BORDER
        auto_row_height(ws0, r, 5, min_h=54)
    ws0.freeze_panes = "A8"

    # --- TAB 01: PERCEPTION AGENTES Y PLAYBOOKS ---
    ws1 = wb.create_sheet("01_Perception_Red_Blue_Green")
    add_banner(
        ws1,
        "MICROSOFT PERCEPTION: CATÁLOGO DE AGENTES RED, BLUE & GREEN Y PLAYBOOKS (IGNITE NOV 2026)",
        "Sistema multi-agente coordinado en el portal Microsoft Defender con enrutamiento de modelos por tarea, contexto compartido y aprobación humana",
        5,
    )
    style_headers(ws1, 4, ["Equipo (Color)", "Nombre del Agente Perception", "Estado (Ignite Nov 2026)", "Señales 3P y Fuentes Soportadas", "Función Técnica y Evidencia Documentada"], [18, 30, 26, 34, 62])
    for i, ag in enumerate(ms_data["perception_agents"]):
        r = 5 + i
        vals = [ag["team"], ag["name"], ag["status"], ag["3p_signals"], ag["description"]]
        for col_i, val in enumerate(vals, start=1):
            c = ws1.cell(r, col_i, val)
            c.fill = ZEBRA_FILL if i % 2 == 1 else WHITE_FILL
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i in (1, 2) else BODY_FONT
            c.alignment = NUM_CENTER if col_i in (1, 3) else WRAP_TOP
            if col_i == 3:
                style_status_cell(c)
        auto_row_height(ws1, r, 5, min_h=34)

    ws1.merge_cells("A15:E15")
    spb = ws1.cell(15, 1, "PLAYBOOKS MULTI-AGENTE DESTACADOS EN MICROSOFT PERCEPTION (IGNITE NOV 2026)")
    spb.font = SECTION_FONT
    spb.fill = SECTION_FILL
    ws1.row_dimensions[15].height = 24
    playbooks = [
        ("Protect against a threat", "Blue + Red + Green", "GA / Core", "TI Agent analiza campaña -> Recon Agent mapea rutas de exposición -> Posture Prioritization prioriza fixes -> Detection Authoring crea reglas KQL e investiga incidentes.", "Ciclo cerrado completo con pausas de aprobación."),
        ("Detect emerging threats", "Blue Team (TI + Detection Authoring)", "GA (Nov 2026)", "Convierte artículos externos de inteligencia en hallazgos estructurados y genera reglas KQL adaptadas al tenant, probándolas contra datos históricos antes de activar.", "Evita falsos positivos estimando volumen previo."),
        ("Run web pen test", "Red Team (Web App Pen Test Agent)", "Public Preview", "Ejecuta pruebas de penetración autorizadas sobre autenticación, APIs, inyección y lógica de negocio; puede guiarse por hallazgos previos de código de Codename MDASH.", "31.0% solve rate y 91% respeto de límites en Incalmo."),
        ("Protect web app", "Red + Green (Web Pen Test + Risk Reduction)", "Public Preview", "Valida vulnerabilidades explotables en la aplicación web y coordina mitigaciones inmediatas como reglas WAF en Azure Front Door mientras se desarrolla el parche definitivo.", "Cierra la ventana entre hallazgo y remediación en código."),
        ("Reduce exposure risk", "Green Team (Posture + Risk Reduction)", "Public Preview", "Evalúa caminos de reducción de riesgo: coordina despliegue controlado de parches vía Microsoft Intune o aplica Vulnerability Shielding temporal cuando no se puede parchear ya.", "Integra SecOps e IT Operations sin perder control."),
    ]
    style_headers(ws1, 16, ["Playbook Perception", "Equipos Orquestados", "Estado", "Flujo Multi-Agente Extremo a Extremo", "Valor Operativo Clave"])
    for idx_p, row_v in enumerate(playbooks):
        r = 17 + idx_p
        for col_i, val in enumerate(row_v, start=1):
            c = ws1.cell(r, col_i, val)
            c.fill = ZEBRA_FILL if idx_p % 2 == 1 else WHITE_FILL
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i == 1 else BODY_FONT
            c.alignment = NUM_CENTER if col_i == 3 else WRAP_TOP
            if col_i == 3:
                style_status_cell(c)
        auto_row_height(ws1, r, 5, min_h=38)
    ws1.freeze_panes = "A5"

    # --- TAB 02: SECURITY COPILOT +18 AGENTES ---
    ws2 = wb.create_sheet("02_Security_Copilot_Agentes")
    add_banner(
        ws2,
        "MICROSOFT SECURITY COPILOT: INVENTARIO DE +18 AGENTES NATIVOS EN DEFENDER, ENTRA, INTUNE, PURVIEW Y SENTINEL",
        "Incluidos para clientes elegibles M365 E5 / E7 (despliegue iniciado nov-2025 y ampliado en 2026) + +30 agentes de partners en Microsoft Security Store",
        5,
    )
    style_headers(ws2, 4, ["Producto / Consola Embebida", "Nombre del Agente Security Copilot", "Estado Documentado", "Modelo de Identidad / Permisos", "Descripción Técnica y Disparadores (Triggers)"], [26, 34, 26, 28, 62])
    for i, ag in enumerate(ms_data["security_copilot_agents"]):
        r = 5 + i
        vals = [ag["workload"], ag["name"], ag["status"], ag["identity"], ag["description"]]
        for col_i, val in enumerate(vals, start=1):
            c = ws2.cell(r, col_i, val)
            c.fill = ZEBRA_FILL if i % 2 == 1 else WHITE_FILL
            c.border = GRID_BORDER
            c.font = BOLD_FONT if col_i in (1, 2) else BODY_FONT
            c.alignment = NUM_CENTER if col_i == 3 else WRAP_TOP
            if col_i == 3:
                style_status_cell(c)
        auto_row_height(ws2, r, 5, min_h=30)
    ws2.freeze_panes = "A5"

    # --- TAB 03: CODENAME MDASH Y GHAS AUTOFIX ---
    ws3 = wb.create_sheet("03_MDASH_y_GHAS_Autofix")
    add_banner(
        ws3,
        "SEGURIDAD AGÉNTICA DE CÓDIGO MICROSOFT: CODENAME MDASH + GITHUB ADVANCED SECURITY (GHAS) AGENTIC AUTOFIX",
        "Diferenciación arquitectónica, pipeline de 5 etapas de MDASH, matriz de 14 lenguajes y flujo de remediación verificada con GitHub Copilot",
        5,
    )
    comp_rows = [
        ("Rol en el Ciclo de Vida", "Descubrimiento profundo read-only, validación multi-modelo y prueba dinámica (PoC) en código fuente.", "Remediación agéntica multi-archivo en el repositorio, re-ejecución de CodeQL y apertura de Pull Request.", "MDASH descubre/prueba upstream; GHAS + Copilot reparan en el flujo dev."),
        ("Estado a Noviembre 2026", "Expanded Preview (anunciado 12-may-2026; ampliado en Ignite 17-nov-2026 a repos de 5 GB y nubes reguladas).", "GA en GitHub Enterprise Cloud (15-oct-2026) y Public Preview en GHAS for Azure DevOps (23-nov-2026).", "Separar claramente Preview (MDASH) de GA en producción (GHAS Autofix GHEC)."),
        ("Arquitectura Agéntica", "Harness de 5 etapas: Prepare -> Scan (>100 subagentes, 3-5 por función) -> Validate (LSP + debate) -> Dedupe -> Prove.", "Agente de ingeniería copilot-swe-agent explora contexto del repo, refina cambios en varios archivos y valida con CodeQL.", "En MDASH 'el sistema/harness es el producto, el modelo es un insumo'."),
        ("Estrategia de Modelos", "Ensemble multi-modelo vía Microsoft Foundry + soporte opcional para MAI-Cyber-1.1-Flash y MAI-Cyber-2 (Preview).", "Modelos de GitHub Copilot optimizados para ingeniería de software y seguridad.", "MDASH requiere región Foundry con soporte para Azure OpenAI Responses API."),
        ("Integración Operativa", "Portal Defender (Security Exposure Management), Defender CLI (defender scan ai-scan / defender fix), SARIF 2.1.0, GitHub Actions, Azure DevOps y Perception.", "Botón 'Assign to Copilot' en alertas Code Scanning, campañas de hasta 25 alertas por PR, REST API y Azure Pipelines.", "Flujo conjunto: MDASH -> SARIF -> Defender CLI / GitHub -> Copilot PR -> Revisión humana."),
        ("Modelo de Costos", "Sin licencia standalone en Preview; el cliente paga consumo de tokens en Microsoft Foundry (~50M small, ~200M medium, ~1.000M+ large repo, orientativo).", "Incluido en licencia GHAS / Code Security; el cómputo de cada fix se factura en GitHub AI Credits a $0.01 USD por crédito.", "Ninguno ejecuta merge automático sin revisión humana."),
    ]
    style_headers(ws3, 4, ["Dimensión Técnica", "Codename MDASH", "GitHub Advanced Security (GHAS) Agentic Autofix", "Guía de Arquitectura Conjunta", ""], [24, 42, 42, 38, 12])
    for idx_m, (dim, mdash_v, ghas_v, guide_v) in enumerate(comp_rows):
        r = 5 + idx_m
        ws3.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        ws3.cell(r, 1, dim).font = BOLD_FONT
        ws3.cell(r, 2, mdash_v).font = BODY_FONT
        ws3.cell(r, 3, ghas_v).font = BODY_FONT
        ws3.cell(r, 4, guide_v).font = BODY_FONT
        for col_i in range(1, 6):
            ws3.cell(r, col_i).fill = ZEBRA_FILL if idx_m % 2 == 1 else WHITE_FILL
            ws3.cell(r, col_i).border = GRID_BORDER
            ws3.cell(r, col_i).alignment = WRAP_TOP
        auto_row_height(ws3, r, 4, min_h=40)

    ws3.merge_cells("A14:E14")
    slang = ws3.cell(14, 1, "MATRIZ OFICIAL DE LENGUAJES SOPORTADOS EN CODENAME MDASH (MICROSOFT LEARN NOV 2026)")
    slang.font = SECTION_FONT
    slang.fill = SECTION_FILL
    ws3.row_dimensions[14].height = 24
    style_headers(ws3, 15, ["Lenguaje", "Extensiones Soportadas", "Tipo de Sub-Agentes MDASH", "Notas Oficiales Microsoft Learn", ""])
    langs = [
        ("Java", ".java", "Sub-agentes Especializados", "Cobertura profunda con resolución de tipos y call-graph."),
        ("C / C++", ".c, .h, .c.in, .cc, .cpp, .cxx, .hh, .hpp", "Sub-agentes Especializados", "Fuerte detección de memory-safety (use-after-free, double-free, buffer overflow)."),
        ("C#", ".cs", "Sub-agentes Especializados", "Cobertura profunda sobre ecosistema .NET."),
        ("JavaScript / TypeScript", ".js, .mjs, .cjs, .ts, .tsx, .mts", "Sub-agentes Especializados", "JavaScript minificado está excluido actualmente."),
        ("Python", ".py, .pyw", "Sub-agentes Especializados", "Análisis semántico y de flujo de datos cross-file."),
        ("Go", ".go", "Sub-agentes Generalistas", "Calidad de escaneo variable según complejidad."),
        ("Rust", ".rs", "Sub-agentes Generalistas", "Descubrimiento generalista sobre bloques unsafe y lógica."),
        ("Kotlin", ".kt, .k, .kts", "Sub-agentes Generalistas", "Soporte generalista documentado en Learn."),
        ("PHP", ".php, .phtml, .inc, .module, .install, .theme", "Sub-agentes Generalistas", "Soporte para aplicaciones web y módulos CMS."),
        ("Ruby", ".rb", "Sub-agentes Generalistas", "Soporte generalista."),
        ("Swift", ".swift", "Sub-agentes Generalistas", "Soporte generalista."),
        ("Objective-C", ".m", "Sub-agentes Generalistas", "Soporte generalista."),
        ("Objective-C++", ".mm", "Sub-agentes Generalistas", "Soporte generalista."),
        ("Zig", ".zig", "Sub-agentes Generalistas", "Soporte generalista."),
    ]
    for idx_l, (lg, ext, agt, note) in enumerate(langs):
        r = 16 + idx_l
        ws3.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        ws3.cell(r, 1, lg).font = BOLD_FONT
        ws3.cell(r, 2, ext).font = BODY_FONT
        ws3.cell(r, 3, agt).font = BOLD_FONT if "Especializados" in agt else BODY_FONT
        ws3.cell(r, 4, note).font = BODY_FONT
        for col_i in range(1, 6):
            ws3.cell(r, col_i).fill = MS_HIGHLIGHT_FILL if "Especializados" in agt else (ZEBRA_FILL if idx_l % 2 == 1 else WHITE_FILL)
            ws3.cell(r, col_i).border = GRID_BORDER
            ws3.cell(r, col_i).alignment = WRAP_TOP
        ws3.row_dimensions[r].height = 22
    ws3.freeze_panes = "A5"

    # --- TAB 04: ISOC Y ARQUITECTURA LOGIC APPS SOAR ---
    ws4 = wb.create_sheet("04_ISOC_y_LogicApps_SOAR")
    add_banner(
        ws4,
        "ISOC IN MICROSOFT DEFENDER + AZURE LOGIC APPS: PLANO FUNDACIONAL DEL SOC AGÉNTICO Y COEXISTENCIA SPLUNK",
        "Desglose exacto de disponibilidad Ignite Nov 2026 y patrón de arquitectura híbrida con Logic Apps como plano SOAR determinístico",
        5,
    )
    isoc_rows = [
        ("Case Management, Playbooks, Workbooks y UEBA en portal Defender", "GA (17-nov-2026)", "Unifica operación diaria de incidentes SIEM y XDR en una sola experiencia de analista."),
        ("Creación de Workspaces e Ingesta de Terceros (>500 conectores)", "GA (17-nov-2026)", "Disponible con tarifa reducida de ingesta ($2.40/GB referenciado en anuncios Ignite) y Data Lake integrado."),
        ("Opt-in a ISOC para clientes existentes de Microsoft Sentinel", "GA / Activo (17-nov-2026)", "Elegible para clientes con Microsoft 365 E5, M365 E7 o Defender Suite sin migración destructiva."),
        ("90 días de retención integrada para datos elegibles de Microsoft Defender", "Public Preview (nov-2026)", "Amplía ventana de investigación y hunting para humanos y agentes sin sobrecosto de ingesta base."),
        ("Normalización en tiempo de ingesta (Ingest-time normalization)", "Public Preview (nov-2026)", "Estandariza esquemas vía gestión de parsers al ingerir para acelerar KQL, analítica y agentes Perception."),
        ("Detections as Code, Content Hub, SOC Optimization y Logs de Auditoría de Automatización", "Public Preview (nov-2026)", "Gobernanza de ingeniería de detección moderna y auditoría de ejecuciones automatizadas."),
        ("Azure Logic Apps como Plano SOAR Empresarial e Híbrido (Coexistencia con Splunk On-Prem)", "GA (Producción)", "Conecta Splunk on-prem (vía Data Gateway / REST), ServiceNow, firewalls e identidad con Sentinel/ISOC (usando solo ingesta bonificada E5 y MDC Servers P2) y dispara/recibe sesiones de Perception vía MCP."),
    ]
    style_headers(ws4, 4, ["Capacidad / Componente ISOC & SOAR", "Estado Real (Nov 2026)", "Impacto Arquitectónico y Económico para el Cliente", "", ""], [38, 26, 68, 12, 12])
    for idx_i, (cap, st, imp) in enumerate(isoc_rows):
        r = 5 + idx_i
        ws4.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)
        ws4.cell(r, 1, cap).font = BOLD_FONT
        c_st = ws4.cell(r, 2, st)
        style_status_cell(c_st)
        c_st.alignment = NUM_CENTER
        ws4.cell(r, 3, imp).font = BODY_FONT
        for col_i in range(1, 6):
            if col_i != 2:
                ws4.cell(r, col_i).fill = ZEBRA_FILL if idx_i % 2 == 1 else WHITE_FILL
            ws4.cell(r, col_i).border = GRID_BORDER
            if col_i != 2:
                ws4.cell(r, col_i).alignment = WRAP_TOP
        auto_row_height(ws4, r, 3, min_h=34)
    ws4.freeze_panes = "A5"

    out_path = BASE_DIR / "Catalogo_Microsoft_Agentic_Security_Ignite2026.xlsx"
    wb.save(str(out_path))
    shutil.copy2(out_path, ROOT_SOAR_DIR / "Catalogo_Microsoft_Agentic_Security_Ignite2026.xlsx")
    shutil.copy2(out_path, SESSION_FILES / "Catalogo_Microsoft_Agentic_Security_Ignite2026.xlsx")
    return out_path


if __name__ == "__main__":
    p1 = build_workbook_1()
    p2 = build_workbook_2()
    print("Generated Workbook 1:", p1)
    print("Generated Workbook 2:", p2)

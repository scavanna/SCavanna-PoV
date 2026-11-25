# -*- coding: utf-8 -*-
"""Genera los documentos Markdown del Sub-plan PO-GAC (00–10) desde data.py."""
import os, json
import data as D
ROOT = os.path.join(os.path.dirname(__file__), ".."); OUT = os.path.join(ROOT, "docs"); PRE = os.path.join(ROOT, "pre_ensayos")
os.makedirs(OUT, exist_ok=True); os.makedirs(PRE, exist_ok=True)
HEADER = f"> **GM-24 {D.VERSION} · Sub-plan PO-GAC** · {D.FECHA}. Base: 331 pre-ensayos del GM-24 (240 K + 51 AMP + 40 HC). Lo específico de Microsoft es implementación; lo agnóstico, base. Referencias DD/K4x/R/eo:OP/COE: marco interno (CISO 365 / AI CISO Atlas)."
def esc(s): return str(s).replace("|", "\\|").replace("\n", " ")
def table(h, rows): return "\n".join(["| " + " | ".join(h) + " |", "|" + "|".join(["---"]*len(h)) + "|"] + ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows])
def write(path, txt): open(path, "w", encoding="utf-8").write(txt.strip() + "\n")
PA_BY_UNIT = {}
for p in D.PA: PA_BY_UNIT.setdefault(p[1], []).append(p)
LENTE_BY_UNIT = {}
for l in D.LENTE: LENTE_BY_UNIT.setdefault(l[1], []).append(l)
H_PA = sum(p[10] for p in D.PA); H_LENTE = sum(l[2] for l in D.LENTE)

def plan():
    rows = [(u["id"], u["title"], len(PA_BY_UNIT.get(u["id"], [])), sum(p[10] for p in PA_BY_UNIT.get(u["id"], [])), len(LENTE_BY_UNIT.get(u["id"], [])), sum(l[2] for l in LENTE_BY_UNIT.get(u["id"], []))) for u in D.UNITS]
    write(os.path.join(OUT, "00_Plan_de_Trabajo.md"), f"""# 00 · Plan de trabajo y decisiones — Sub-plan PO-GAC ({D.VERSION})

{HEADER}

## 1. Objetivo
Itinerario para que un analista de ciberseguridad evolucione a **Product Owner de un control de seguridad (PO)** y **gerente de agentes cognitivos (GAC)** integrados en un SOC, sin pilotear agentes, dentro de las 24 unidades del GM-24 y sobre su base de 331 pre-ensayos.

## 2. Horas
- {len(D.PA)} conceptos PA nuevos: **{H_PA} h**. Lente PO-GAC sobre {len(D.LENTE)} conceptos existentes: **{H_LENTE} h**. Práctica guiada y capstone: **91 h**. Total: **{H_PA + H_LENTE + 91} h**.
- Envolvente de referencia: {D.HORAS_UNIDAD} h/unidad ({D.HORAS_UNIDAD*24} h); reescalado a 800 h pendiente (D07).

## 3. Distribución por unidad
{table(["Unidad","Título","PA (n)","PA (h)","Lente (n)","Lente (h)"], rows)}

## 4. Decisiones
{table(["ID","Decisión","Detalle","Estado"], D.DECISIONES)}

## 5. Etapas
{table(["Etapa","Nombre","Calendario","Conceptos clave"], D.ETAPAS)}
""")

def competencias():
    write(os.path.join(OUT, "02_Marco_de_Competencias.md"), f"""# 02 · Marco de competencias PO-GAC ({len(D.COMPETENCIAS)} competencias en {len(D.DOMINIOS)} dominios)

{HEADER}

## Dominios
{table(["ID","Dominio"], D.DOMINIOS)}

## Competencias (N1 reconoce · N2 aplica con apoyo · N3 decide y defiende · N4 diseña y gobierna)
{table(["ID","Dominio","Competencia","Niveles","Conceptos que la sostienen"], [(c[0], c[1], c[2], c[3], ", ".join(c[4])) for c in D.COMPETENCIAS])}
""")

def mapeo():
    rows = [(p[0], p[1], p[2], p[3], p[4], "; ".join(f"{a} ({b})" for a, b in p[5]), p[10], ", ".join(p[11]), p[12]) for p in D.PA]
    write(os.path.join(OUT, "03_Mapeo_GM24_y_Gap.md"), f"""# 03 · Mapeo al GM-24 y análisis de brecha ({D.VERSION})

{HEADER}

## 1. Conceptos PA ({len(D.PA)})
{table(["ID","Unidad","Concepto","Definición","Brecha frente a los 331","Relaciones","h","Competencias","Origen"], rows)}

## 2. Lente PO-GAC sobre conceptos existentes ({len(D.LENTE)}, {H_LENTE} h)
{table(["ID","Unidad","Concepto","h","Lectura PO-GAC","Instrumento","Competencias"], [(l[0], l[1], D.CATX.get(l[0], {}).get("concepto", ""), l[2], l[3], l[4], ", ".join(l[5])) for l in D.LENTE])}

## 3. PA retirados o fusionados respecto de V5
{table(["PA V5","Tratamiento V6"], D.RETIRADOS)}
""")

def modelo_operativo():
    write(os.path.join(OUT, "04_Modelo_Operativo_MDO_XDR.md"), f"""# 04 · Modelo operativo del control de correo y colaboración (Defender for Office 365 en Defender XDR)

{HEADER}

{len(D.TAREAS)} tareas con cadencia, persona (según Microsoft Learn), función CSF, práctica agnóstica eo:OP, nivel de autonomía recomendado, agente y KPI.

{table(["ID","Tarea","Cadencia","Persona","CSF 2.0","SAF","eo:OP","Autonomía","Agente","KPI","Fuente"], D.TAREAS)}

## KPIs del control y de la flota
{table(["ID","KPI","Definición","Meta","Cadencia","Tipo"], D.KPIS)}
""")

def gobierno():
    write(os.path.join(OUT, "05_Gobierno_y_Gestion_de_Agentes.md"), f"""# 05 · Gobierno y gestión de agentes: catálogo AGC, RACI y escala de autonomía

{HEADER}

## 1. Catálogo de controles AGC ({len(D.CONTROLES)})
{table(["ID","Capa","Control","Objetivo","AI RMF","ISO 42001","OWASP ASI","Implementación Microsoft","Base agnóstica","Evidencia","Responsable"], D.CONTROLES)}

## 2. RACI ({len(D.RACI)} actividades)
{table(["Actividad"] + D.RACI_ROLES, D.RACI)}

## 3. Escala de autonomía L0–L4
| Nivel | Definición | Ejemplo |
|---|---|---|
| L0 | Solo informa | Reporte de tendencias |
| L1 | Propone; humano ejecuta | Hipótesis de hunting |
| L2 | Propone y ejecuta tras aprobación | Remediación de correo |
| L3 | Ejecuta acciones reversibles y de bajo impacto; auditoría posterior | Detección de deriva; tickets |
| L4 | Autónomo con límites estrictos (no previsto en este sub-plan) | — |
""")

def subplan():
    write(os.path.join(OUT, "06_Subplan_de_Desarrollo.md"), f"""# 06 · Sub-plan de desarrollo: etapas, evidencias y capstone

{HEADER}

{table(["Etapa","Nombre","Calendario","Conceptos clave"], D.ETAPAS)}

## Evidencias por etapa
- E0: ficha de rol, grilla de ownership, diagrama de arquitectura de correo, bitácora de 2 semanas del runbook.
- E1: 20 incidentes triados, 10 casos FP/FN, 5 consultas + 2 detecciones, procedimiento de excepciones, cadena objetivo→config→evidencia.
- E2: política de agentes, 3 fichas, declaración de apetito, matriz tarea→nivel→gate, evaluación AGC, matriz de permisos.
- E3: decisión de ruta, dataset dorado + evaluación, red teaming, matriz amenaza→agente, pipeline ALM.
- E4: organigrama híbrido + RACI, tablero de observabilidad, revisión de desempeño, KRIs, modelo FinOps.
- E5 (capstone): reporte ejecutivo trimestral, día en modo degradado, tabletop, post-mortem + ChangeSet.

## Autoevaluación
Instrumento de {len(D.COMPETENCIAS)} competencias × 4 niveles; línea base en E0, repetición en E3 y E5.
""")

def agentes():
    write(os.path.join(OUT, "08_Catalogo_Agentes.md"), f"""# 08 · Catálogo de agentes del control ({len(D.AGENTES)})

{HEADER}

{table(["ID","Agente","Propósito","Tareas","Entradas","Herramientas","Autonomía","Gates","KPIs","Costo","Riesgos ASI","Identidad","Owner","Ruta"], D.AGENTES)}

## Rutas de construcción
- **R1** Security Copilot (agente personalizado; SCU). **R2** Copilot Studio (entorno de desarrollo; conectores, MCP, Graph; créditos/capacidad). **R3** Foundry Agent Service (MCP; modelo elegible; tokens).
""")

def agnostico():
    rows = [("Modelo operativo por cadencias","MAEO eo:OP; ITIL","Security Operations Guide MDO; tareas SOC XDR","Alto"),("Identidad de agentes","OAuth2/OIDC; SPIFFE; workload identity","Entra Agent ID","Medio"),("Permisos de herramientas","Least privilege; allowlists","Políticas de datos PPAC; API permissions","Medio"),("Telemetría","OpenTelemetry","Foundry tracing; Sentinel; Agent 365 analytics","Alto"),("Herramientas/protocolos","MCP; OpenAPI","Sentinel MCP; MCP Server for Enterprise; conectores","Alto (MCP) / Bajo (conectores)"),("Evidencia","Esquema común; ISO 27001 A.8.15","SharePoint/Dataverse + Sentinel","Alto"),("Detección como código","Sigma","Custom detections; KQL en Git","Medio"),("Gobierno de IA","AI RMF; ISO 42001","AGC; Compliance Manager; Agent 365","Alto"),("Controles de agentes","OWASP ASI; CSA AICM","Prompt Shields; DLP; CA para agentes","Medio"),("Costos","FinOps Foundation","Cost Management; SCU; capacidad","Alto"),("Autorización","NIST RMF Authorize","Expediente ATO; Agent 365","Alto"),("Postura de IA","CSPM/AI-SPM; CIS Benchmarks","Defender for Cloud (IA)","Medio"),("Continuidad","ISO 22301","Soluciones versionadas; exportación de agentes","Medio"),("Datos","Gobierno de datos; DSPM","Purview DSPM for AI; DLP","Medio"),("Pruebas adversariales","Red teaming de IA; ATLAS","Foundry evaluations; PyRIT","Alto")]
    write(os.path.join(OUT, "09_Bases_Agnosticas_vs_Microsoft.md"), f"""# 09 · Bases agnósticas frente a implementación Microsoft

{HEADER}

{table(["Capacidad","Base agnóstica","Implementación Microsoft","Portabilidad"], rows)}
""")

def conciliacion():
    write(os.path.join(OUT, "10_Conciliacion_V5_a_V6.md"), f"""# 10 · Conciliación V5 → V6

{HEADER}

- V5: 67 PA (316 h) sobre 240 K. V6: base 331 (240 K + 51 AMP + 40 HC); **{len(D.PA)} PA** ({H_PA} h); {len(D.RETIRADOS)} PA de V5 retirados o fusionados; lente PO-GAC sobre {len(D.LENTE)} conceptos existentes ({H_LENTE} h).

{table(["PA V5","Tratamiento V6"], D.RETIRADOS)}
""")

if __name__ == "__main__":
    plan(); competencias(); mapeo(); modelo_operativo(); gobierno(); subplan(); agentes(); agnostico(); conciliacion(); print("DONE docs")

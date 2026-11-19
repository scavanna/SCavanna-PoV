# 01 · Ficha de producto-control: SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender) |
| Dominio Zero Trust | Visibilidad, automatización y orquestación (transversal); interfaz con XDR, owners de dominio y flotas de agentes (observabilidad, Sentinel MCP) |
| Tecnología | Microsoft Sentinel (incidentes, analytics rules, automation rules, playbooks, Content hub, workbooks, watchlists, TI STIX 2.1, UEBA, SOC optimization, data lake, MCP server preview), Azure Monitor; portal de Defender obligatorio desde el 31-mar-2027 |
| Funciones CSF 2.0 | GV.OV · ID.AM · ID.RA · PR.PS · DE.CM/DE.AE · RS.MA/RS.MI · ID.IM |
| Fuente oficial del modelo operativo | Microsoft Sentinel operational guide (diario/semanal/mensual) + deployment checklist post-despliegue + SOC optimization + health & audit |
| Objetivo del control | Fuentes con salud y costo gobernado; reglas con cobertura y bajo ruido; automatización sin fallos y con aprobación; incidentes en SLA en el portal unificado |
| SLO | Conectores en error = 0 (24 h); reglas fallidas = 0; playbooks fallidos ≤24 h; desvío de ingesta ≤10 %; cobertura MITRE ≥90 %; SOC optimization críticas ≤30 días |
| Owner | PO-GAC Siem (sponsor de los agentes SA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Dominio de la plataforma de datos y automatización: su riesgo principal es la pérdida de visibilidad y el costo. Comparte la cola con XDR; es dueño de fuentes, reglas, retención, costos y SOAR. Base de la observabilidad de todas las flotas y del Sentinel MCP. |
| Interfaz con otros owners | Owner XDR: cola y correlación. Owners de dominio: fuentes y reglas. FinOps: commitment tiers. Flotas: telemetría y Sentinel MCP (preview). |
| Personas (Learn) | SOC analysts (Tier 1-3) · Security engineers · Sentinel admins · FinOps |
| Permisos | Sentinel Reader / Responder / Contributor / Playbook Operator; Logic App Operator/Contributor; Log Analytics Reader/Contributor; Unified RBAC |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | SI-D01, SI-D03, SI-W01, SI-W03, SI-W05, SI-A02 |
| DE.CM | SI-D02, SI-D04 |
| GV.OV | SI-W02, SI-W04, SI-M03, SI-M05, SI-Q02, SI-A03 |
| GV.PO | SI-M02, SI-Q01 |
| GV.RM | SI-Q01 |
| GV.RR | SI-M01 |
| ID.AM | SI-D02, SI-W04, SI-M03, SI-M04, SI-A01 |
| ID.IM | SI-W01, SI-W05, SI-Q02, SI-Q04, SI-A04 |
| ID.RA | SI-W03, SI-W06 |
| PR.AA | SI-M01, SI-Q03 |
| PR.PS | SI-D03, SI-D05, SI-W02, SI-M02, SI-M04, SI-A01, SI-A03 |
| RS | SI-D01, SI-D05, SI-M05, SI-A02, SI-A04 |
| RS.CO | SI-M05 |
| RS.MA | SI-D01 |
| RS.MI | SI-D05, SI-A02 |

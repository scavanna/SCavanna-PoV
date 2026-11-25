# 01 · Ficha de producto-control: Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk) |
| Dominio Zero Trust | Datos (pilar Zero Trust); en reposo, en uso y en movimiento en M365, endpoints, SaaS, on-prem y en el uso por IA; interfaz con Productividad, Endpoints, Identidades y con las flotas de agentes (fuentes aprobadas) |
| Tecnología | Purview Information Protection (labels, auto-labeling, encriptación), DLP (Exchange, SharePoint/OneDrive, Teams, Endpoint, Copilot), DSPM y DSPM for AI, Insider Risk Management, Activity/Content explorer, Compliance Manager; Defender for Cloud Apps; scanner; Purview APIs para agentes |
| Funciones CSF 2.0 | GV.PO · ID.AM · ID.RA · PR.DS · PR.AA · DE.CM/DE.AE · RS.AN/RS.MI · ID.IM |
| Fuente oficial del modelo operativo | Deploy an information protection solution with Microsoft Purview (fases 1–3; roles); default labels & policies (DSPM setup tasks); plan for DLP; DLP alerts; Insider Risk Management; Defender for Cloud Apps information protection |
| Objetivo del control | Información sensible descubierta, clasificada y protegida; DLP en bloqueo para SITs críticos con FP controlados; sobrecompartición y uso por IA medidos y reducidos; alertas DLP/Insider triadas en SLA |
| SLO | Cobertura de etiquetado ≥90 %; DLP en bloqueo para SITs críticos en todas las ubicaciones; alertas DLP High ≤4 h; 'Anyone' en sitios sensibles = 0; recomendaciones DSPM críticas ≤30 días |
| Owner | PO-GAC Datos (sponsor de los agentes DA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Mayor dependencia de dueños de negocio y mayor costo de falso positivo en productividad. Ciclo iterativo (descubrir → etiquetar → proteger → medir). Provee las fuentes aprobadas y la DLP para IA a todas las flotas (AGC-07). |
| Interfaz con otros owners | Productividad: DLP de correo y Safe Attachments en la misma ruta. Endpoints: Endpoint DLP depende del onboarding de MDE. Identidades: encriptación depende de identidades y CA. Dueños de datos: taxonomía y excepciones. Privacidad/Legal: Insider Risk. |
| Personas (Learn) | Information Protection Admin · Analyst / Investigator · Reader · IRM Admin/Analysts/Investigators · Compliance Administrator · Data owners · Privacidad/Legal |
| Permisos | Purview: Information Protection Admin / Analyst / Investigator / Reader; IRM roles (solo humanos); MDA Security Operator; Graph: InformationProtectionPolicy.Read, SecurityAlert.Read.All, Sites.Read.All |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | DP-D01 |
| DE.CM | DP-D04, DP-D05, DP-W04 |
| GV.OV | DP-W05, DP-M04, DP-M05, DP-Q02 |
| GV.PO | DP-M01, DP-M02, DP-M03, DP-Q01, DP-A03 |
| GV.RM | DP-Q01 |
| ID.AM | DP-W02, DP-A02 |
| ID.IM | DP-D03, DP-W01, DP-W05, DP-M02, DP-M05, DP-Q02, DP-Q04, DP-A04 |
| ID.RA | DP-D04, DP-W03, DP-M03 |
| PR.AA | DP-W03, DP-M06, DP-Q03 |
| PR.DS | DP-D03, DP-W01, DP-W02, DP-W06, DP-M01, DP-M06, DP-A02, DP-A03 |
| PR.PS | DP-D05 |
| RS | DP-D01, DP-D02, DP-W06, DP-M04, DP-A01, DP-A04 |
| RS.AN | DP-D02 |
| RS.CO | DP-M04, DP-A01 |
| RS.MA | DP-D01 |
| RS.MI | DP-D02, DP-W06, DP-A01 |

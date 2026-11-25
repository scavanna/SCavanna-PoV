# 01 · Ficha de producto-control: Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services) |
| Dominio Zero Trust | Infraestructura y aplicaciones en la nube (multicloud Azure/AWS/GCP y on-prem vía Arc); interfaz con XDR, Identidades, Datos y flotas (postura de recursos de IA) |
| Tecnología | Defender for Cloud: CSPM (MCSB, secure score clásico y risk-based, governance rules, attack paths, regulatory compliance, exemptions), CWPP (Servers/Containers/Storage/SQL/APIs/AI Services), workflow automation, continuous export, DWU; portal de Defender |
| Funciones CSF 2.0 | GV.OV · ID.AM · ID.RA · PR.PS · PR.AA · DE.CM/DE.AE · RS.MI · ID.IM |
| Fuente oficial del modelo operativo | Defender for Cloud: secure score y MCSB; recommendations y governance rules; attack path analysis; regulatory compliance; workflow automation; release notes |
| Objetivo del control | Postura multicloud gobernada (recomendaciones con dueño y fecha, attack paths rotos, cumplimiento sostenido), cargas críticas y recursos de IA protegidos, alertas en SLA |
| SLO | Críticas/altas con dueño y fecha = 100 %; vencidas ≤5 %; attack paths críticos >30 días = 0; cumplimiento ≥90 %; planes en suscripciones críticas = 100 %; alertas High ≤30 min |
| Owner | PO-GAC Nube (sponsor de los agentes CA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Más dueños externos al SOC: el owner no remedia, asigna y hace seguimiento (governance rules). Costo por recurso (DWU) y dos modelos de secure score. Da postura a los recursos de IA que usan todas las flotas (AMP-51). |
| Interfaz con otros owners | XDR: alertas en la cola unificada. Identidades: permisos excesivos en attack paths. Datos: datos sensibles en almacenamiento. Plataforma/DevOps: remedian. Cumplimiento: estándares. |
| Personas (Learn) | Security Admin / Security Reader · dueños de suscripción · Plataforma/DevOps · Cumplimiento · FinOps |
| Permisos | Azure RBAC: Security Reader, Security Admin (humano), Owner/Contributor (plataforma); Logic App Contributor; Unified RBAC con cloud scopes |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | CL-D01 |
| DE.CM | CL-W05 |
| GV.OC | CL-W03 |
| GV.OV | CL-D03, CL-W01, CL-W02, CL-W03, CL-W07, CL-M02, CL-M05, CL-Q02 |
| GV.PO | CL-M01, CL-Q01, CL-A03 |
| GV.RM | CL-Q01 |
| GV.RR | CL-M01 |
| ID.AM | CL-W04, CL-M03, CL-A02 |
| ID.IM | CL-D03, CL-W01, CL-W02, CL-W07, CL-Q02, CL-Q04, CL-A04 |
| ID.RA | CL-D02 |
| PR.AA | CL-M04, CL-Q03 |
| PR.PS | CL-D02, CL-W04, CL-W05, CL-W06, CL-M04, CL-A02, CL-A03 |
| RS | CL-D01, CL-W06, CL-M05, CL-A01, CL-A04 |
| RS.CO | CL-M05 |
| RS.MA | CL-D01 |
| RS.MI | CL-W06, CL-A01 |

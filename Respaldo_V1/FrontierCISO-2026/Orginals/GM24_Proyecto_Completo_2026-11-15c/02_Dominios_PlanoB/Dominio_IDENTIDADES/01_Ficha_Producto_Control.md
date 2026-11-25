# 01 · Ficha de producto-control: Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance) |
| Dominio Zero Trust | Identidades (pilar Zero Trust); humanas y no humanas (incl. agentes), on-prem e híbridas; interfaz con Endpoints y XDR |
| Tecnología | Defender for Identity, Entra ID Protection (risky users/sign-ins, unified risk; Entra ID P2), Conditional Access (basadas en riesgo), Entra ID Governance (access reviews, PIM), Entra Agent ID, Defender XDR |
| Funciones CSF 2.0 | GV.RR · ID.AM · ID.RA · PR.AA · DE.CM/DE.AE · RS.AN/RS.MI · RC.RP |
| Fuente oficial del modelo operativo | Defender for Identity operational guide (daily/weekly/monthly/quarterly) + Microsoft Entra security operations guide + Entra ID Protection |
| Objetivo del control | Que toda identidad con riesgo medio/alto sea remediada en SLA, sensores saludables, postura en mejora y NHI (incl. agentes) con dueño y caducidad |
| SLO | Risky users High remediados ≤4 h; CA basadas en riesgo activas; sensores MDI sin issues; 100 % NHI con dueño; recertificaciones a tiempo |
| Owner | PO-GAC Identidades (sponsor de los agentes IA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Mayor proporción de remediación automática legítima (self-remediation vía CA) y mayor sensibilidad a bloquear personas. Incluye el gobierno de identidades de agentes (Entra Agent ID): sostiene AGC-05/06/18 de todas las flotas. |
| Interfaz con otros owners | Owner XDR: correlación. Owner Endpoints: cumplimiento de dispositivo como señal de CA. IAM/Entra admins: ejecutan cambios de CA y PIM; el owner Identidades propone y verifica. |
| Personas (Learn) | SOC analysts · Security administrators · IAM administrators |
| Permisos | Security Reader/Operator (Entra) · Conditional Access Administrator (solo humano) · Identity Governance Administrator · Unified RBAC · Graph: IdentityRiskyUser.*, Policy.Read.All, AuditLog.Read.All |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | ID-D02, ID-W02 |
| DE.CM | ID-D01, ID-D05, ID-D06 |
| GV.OV | ID-W01, ID-W05, ID-M03, ID-Q02 |
| GV.PO | ID-W03, ID-M04 |
| ID.AM | ID-M02, ID-A03 |
| ID.IM | ID-D04, ID-W01, ID-W05, ID-M01, ID-Q02, ID-Q04, ID-A04 |
| ID.RA | ID-D01, ID-W02, ID-W04 |
| PR.AA | ID-W03, ID-W04, ID-M02, ID-M04, ID-Q03, ID-A03 |
| PR.IR | ID-Q01 |
| PR.PS | ID-D05, ID-Q01 |
| RS | ID-D02, ID-D03, ID-M03, ID-A01, ID-A02, ID-A04 |
| RS.AN | ID-D03, ID-A02 |
| RS.CO | ID-M03 |
| RS.MA | ID-D02 |
| RS.MI | ID-D03, ID-A01 |

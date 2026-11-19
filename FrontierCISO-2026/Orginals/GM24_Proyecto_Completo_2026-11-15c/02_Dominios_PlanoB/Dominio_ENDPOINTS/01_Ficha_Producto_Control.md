# 01 · Ficha de producto-control: Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune) |
| Dominio Zero Trust | Endpoints / dispositivos (pilar Zero Trust); interfaz con Identidades (cumplimiento como señal de CA) y con XDR |
| Tecnología | Defender for Endpoint (EDR, next-gen protection, ASR, web/network protection, device control, attack disruption), Defender Vulnerability Management, Intune (baselines, cumplimiento), Defender XDR |
| Funciones CSF 2.0 | ID.AM · ID.RA · PR.PS · PR.AA · DE.CM/DE.AE · RS.AN/RS.MI · RC.RP |
| Fuente oficial del modelo operativo | Microsoft Defender for Endpoint Security Operations Guide (diario/semanal/mensual/ad hoc) + Defender Vulnerability Management + ASR + device groups; Intune security baselines |
| Objetivo del control | Que todo dispositivo del alcance esté onboarded, saludable, con ASR y baseline aplicados, con vulnerabilidades críticas remediadas en SLA y respuesta a incidentes de endpoint dentro del SLA |
| SLO | Onboarded ≥98 %; EDR/AV saludable ≥98 %; CVEs críticos en activos críticos ≤7 días; ASR en bloqueo ≥90 %; incidentes High triados ≤30 min |
| Owner | PO-GAC Endpoints (sponsor de los agentes EA-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Endpoints tiene más acciones irreversibles (aislar, restringir, offboard) y más dependencia de IT (Intune). Desde el 1-sep-2026 AIR ya no es una experiencia separada en MDE: la detección/respuesta automática queda embebida en el stack antivirus; el foco pasa a revisar el Action center y los niveles de automatización por grupo. |
| Interfaz con otros owners | Owner XDR: cola y automatización transversal. Owner Identidades: cumplimiento de dispositivo como condición de acceso. IT/Intune: ejecuta remediaciones; el owner Endpoints las prioriza y verifica. |
| Personas (Learn) | Security Operations Team · Security Administration Team · Engineering & SecOps · IT (Intune) |
| Permisos | Security data basics · Alerts (Manage) · Response (Manage) · Live response · Vulnerability management · Security settings (Manage) · Authorization (device groups) |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | EP-D02, EP-D04 |
| DE.CM | EP-D05, EP-W02, EP-W05, EP-W06 |
| GV.OV | EP-D01, EP-W01, EP-M04, EP-Q02 |
| GV.PO | EP-Q01 |
| GV.RM | EP-Q01 |
| ID.AM | EP-M03, EP-A03 |
| ID.IM | EP-D03, EP-W01, EP-W03, EP-M05, EP-Q02, EP-Q04, EP-A05 |
| ID.RA | EP-D04, EP-W02, EP-W03, EP-W06, EP-A04 |
| PR.AA | EP-M01, EP-M02, EP-Q03 |
| PR.PS | EP-D03, EP-D05, EP-W04, EP-W05, EP-M01, EP-M02, EP-M05, EP-Q04, EP-A03, EP-A04 |
| RS | EP-D01, EP-D02, EP-D06, EP-M04, EP-A01, EP-A02, EP-A05 |
| RS.AN | EP-D06, EP-A02 |
| RS.CO | EP-M04 |
| RS.MA | EP-D02 |
| RS.MI | EP-D01, EP-D06, EP-A01 |

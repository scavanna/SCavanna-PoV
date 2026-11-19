# 01 · Ficha de producto-control: Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Microsoft Defender XDR)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Microsoft Defender XDR)** · 2026-11-14 · v1.1 (re-emisión en formato uniforme de la instancia V5/V6). Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Campo | Contenido |
|---|---|
| Producto-control | Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Microsoft Defender XDR) |
| Dominio Zero Trust | Productividad y colaboración (Exchange, SharePoint, OneDrive, Teams); interfaz con XDR, Identidades y Datos |
| Tecnología | EOP + Defender for Office 365 Plan 2 (Safe Links, Safe Attachments, anti-phishing, ZAP, presets Standard/Strict, Campaign Views, Threat Explorer, AIR, Attack Simulation Training, Submissions, TABL), Defender XDR |
| Funciones CSF 2.0 | GV.PO/PR.PS · DE.AE/DE.CM · RS.AN/RS.MI · ID.IM · PR.AT |
| Fuente oficial del modelo operativo | Microsoft Defender for Office 365 Security Operations Guide + tareas de mantenimiento del SOC de Defender XDR |
| Objetivo del control | Ningún mensaje malicioso residente >24 h; FP/FN como calidad de producto; configuración en baseline; incidentes en SLA |
| SLO | Residentes >24 h = 0; FP <1 %; triaje M/H ≥95 %; desviaciones críticas = 0; cuentas prioritarias 100 % |
| Owner | PO-GAC Productividad (sponsor de los agentes AG-xx en Entra Agent ID) |
| Diferencia frente a otros dominios | Instancia de referencia del sub-plan (V5/V6). Protege un canal con un sensor; acción más sensible: hard delete y liberación de cuarentena. |
| Interfaz con otros owners | XDR: correlación y automatización. Datos: DLP de correo. Identidades: cuentas prioritarias. Mesa de mensajería: flujo de correo. |
| Personas (Learn) | Security Operations Team · Security Administration · Messaging Team · Threat hunting team · SOC Oversight |
| Permisos | Unified RBAC + roles de Exchange Online/MDO; Agent ID para agentes |

## Grilla de ownership CSF 2.0 × dominio

| Categoría CSF 2.0 | Tareas del modelo operativo |
|---|---|
| DE.AE | MDO-D01, MDO-D09, MDO-W04, MDO-M03, MDO-A04 |
| DE.CM | MDO-W01, MDO-A02, MDO-A03 |
| GV.OV | MDO-W06, MDO-Q02 |
| GV.PO | MDO-Q01 |
| ID.IM | MDO-D04, MDO-D05, MDO-D06, MDO-W05, MDO-M02, MDO-Q04, MDO-A07 |
| ID.RA | MDO-W02, MDO-W03 |
| PR.AA | MDO-W03, MDO-Q03, MDO-A05 |
| PR.AT | MDO-M04 |
| PR.PS | MDO-D07, MDO-W07, MDO-M01 |
| RS.AN | MDO-D02 |
| RS.MA | MDO-D01, MDO-D03, MDO-A06 |
| RS.MI | MDO-D02, MDO-D08, MDO-D09, MDO-A01 |

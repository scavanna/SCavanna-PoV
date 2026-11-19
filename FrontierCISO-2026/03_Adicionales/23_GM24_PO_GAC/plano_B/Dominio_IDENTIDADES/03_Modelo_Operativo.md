# 03 · Modelo operativo (23 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Defender for Identity operational guide (daily/weekly/monthly/quarterly) + Microsoft Entra security operations guide + Entra ID Protection.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| ID-D01 | Revisar el Identity Security dashboard | Diaria | SOC analysts + IAM admins | DE.CM, ID.RA | SOP | eo:OP-SOP-29 Revisar el tablero de postura y riesgo del dominio | L3 | IA-08 | Insights revisados | MDI ops-guide-daily |
| ID-D02 | Triar incidentes de identidad por prioridad y resolver remediados | Diaria | SOC analysts | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | IA-01 | % H/M en SLA | MDI ops-guide-daily |
| ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie | Diaria | SOC analysts | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | IA-02 | Risky users High ≤4 h | ID Protection investigate-risk |
| ID-D04 | Configurar reglas de tuning para benign true positives de MDI | Diaria | SOC analysts + Security admins | ID.IM | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L2 | IA-04 | Reglas con vencimiento | MDI ops-guide-daily |
| ID-D05 | Revisar salud de sensores MDI | Diaria | Security admins | PR.PS, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | IA-05 | Health issues = 0 | MDI ops-guide-daily |
| ID-D06 | Hunting proactivo sobre identidad | Diaria/Semanal | SOC analysts | DE.CM | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | IA-11 | Hunts | MDI ops-guide-daily/weekly |
| ID-W01 | Revisar Secure Score y posture assessments; alimentar backlog | Semanal | Security admins + SOC | ID.IM, GV.OV | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | IA-08 | Secure Score ↑ | MDI ops-guide-weekly |
| ID-W02 | Responder a amenazas emergentes con detecciones personalizadas | Semanal | Security admins + SOC | DE.AE, ID.RA | SOP | eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | L2 | IA-11 | Detecciones vigentes | MDI ops-guide-weekly |
| ID-W03 | Revisar efectos de Conditional Access (report-only) y proponer ajustes | Semanal | IAM admins + SOC | PR.AA, GV.PO | POS | eo:OP-POS-18 Evaluar el efecto de las políticas de acceso y ajustarlas | L2 | IA-07 | Report-only → on | Entra security-operations |
| ID-W04 | Revisar riesgo de identidades de carga de trabajo (SPs, agentes) | Semanal | IAM admins + PO-GAC | ID.RA, PR.AA | AYI | eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | L2 | IA-06 | NHI sin dueño = 0 | workload identity risk |
| ID-W05 | Revisar Message Center y novedades | Semanal | Security admins | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | IA-10 | Cambios evaluados ≤7 días | MDI ops-guide-monthly |
| ID-M01 | Revisar alertas tuned y retirar reglas sin coincidencias | Mensual | Security admins + SOC | ID.IM | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | IA-04 | Reglas obsoletas retiradas | MDI ops-guide-monthly |
| ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM | Mensual | IAM admins | PR.AA, ID.AM | AYI | eo:OP-AYI-03 Mantener el inventario y la higiene de identidades privilegiadas | L2 | IA-09 | Admins fuera de PIM = 0 | Entra security-operations |
| ID-M03 | Informe mensual de identidad para el CISO | Mensual | Security admins | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | IA-08 | Informe a tiempo | Propuesta |
| ID-M04 | Revisar baseline de CA y excepciones (break-glass) con vencimiento | Mensual | IAM admins + SOC Oversight | GV.PO, PR.AA | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | IA-07 | Exclusiones justificadas | risk-based policies |
| ID-Q01 | Revisar service health, setup de sensores y configuración de dominio | Trimestral | Security admins | PR.PS, PR.IR | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L1 | IA-05 | Hallazgos cerrados | MDI ops-guide-quarterly |
| ID-Q02 | Revisar desempeño y costo de la flota Identidades | Trimestral | PO-GAC Identidades | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | IA-13 | KPIs vs. meta | Propuesta |
| ID-Q03 | Recertificación de accesos (humanos, grupos privilegiados, agentes) | Trimestral | IAM + PO-GAC | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | IA-09 | % a tiempo | Entra ID Governance |
| ID-Q04 | Evaluaciones/regresión y red teaming; prueba de bloqueo indebido y rollback | Trimestral | PO-GAC + AppSec | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA | Por evento | SOC + IAM | RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | IA-02 | Tiempo a contención | investigate-risk |
| ID-A02 | Investigación de insider risk correlacionada con riesgo de identidad | Por evento | SOC + Privacidad | RS.AN | SOP | eo:OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | L1 | — | Casos autorizados | Insider Risk Management |
| ID-A03 | Alta/baja de identidades de agentes (Entra Agent ID), sponsors y permisos | Por evento | IAM + PO-GAC | PR.AA, ID.AM | AYI | eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | L2 | IA-06 | Agentes sin sponsor = 0 | agent-id-governance-overview |
| ID-A04 | Tabletop de compromiso de identidad privilegiada (incl. 'agente comprometido') | Según necesidad | SOC Oversight + IAM | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-D01 | Revisar el Identity Security dashboard | SOC analysts + IAM admins | IA-08 | L3 |
| ID-D02 | Triar incidentes de identidad por prioridad y resolver remediados | SOC analysts | IA-01 | L2 |
| ID-D03 | Investigar risky users / sign-ins; confirmar o descartar; remediar o dejar que CA auto-remedie | SOC analysts | IA-02 | L2 |
| ID-D04 | Configurar reglas de tuning para benign true positives de MDI | SOC analysts + Security admins | IA-04 | L2 |
| ID-D05 | Revisar salud de sensores MDI | Security admins | IA-05 | L3 |
| ID-D06 | Hunting proactivo sobre identidad | SOC analysts | IA-11 | L1 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-W01 | Revisar Secure Score y posture assessments; alimentar backlog | Security admins + SOC | IA-08 | L3 |
| ID-W02 | Responder a amenazas emergentes con detecciones personalizadas | Security admins + SOC | IA-11 | L2 |
| ID-W03 | Revisar efectos de Conditional Access (report-only) y proponer ajustes | IAM admins + SOC | IA-07 | L2 |
| ID-W04 | Revisar riesgo de identidades de carga de trabajo (SPs, agentes) | IAM admins + PO-GAC | IA-06 | L2 |
| ID-W05 | Revisar Message Center y novedades | Security admins | IA-10 | L3 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-M01 | Revisar alertas tuned y retirar reglas sin coincidencias | Security admins + SOC | IA-04 | L2 |
| ID-M02 | Revisar cuentas sensibles, inactivas, admins sin PIM | IAM admins | IA-09 | L2 |
| ID-M03 | Informe mensual de identidad para el CISO | Security admins | IA-08 | L3 |
| ID-M04 | Revisar baseline de CA y excepciones (break-glass) con vencimiento | IAM admins + SOC Oversight | IA-07 | L2 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-Q01 | Revisar service health, setup de sensores y configuración de dominio | Security admins | IA-05 | L1 |
| ID-Q02 | Revisar desempeño y costo de la flota Identidades | PO-GAC Identidades | IA-13 | L1 |
| ID-Q03 | Recertificación de accesos (humanos, grupos privilegiados, agentes) | IAM + PO-GAC | IA-09 | L2 |
| ID-Q04 | Evaluaciones/regresión y red teaming; prueba de bloqueo indebido y rollback | PO-GAC + AppSec | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-A01 | Respuesta a compromiso de identidad: revocar, reset, deshabilitar, bloquear por CA | SOC + IAM | IA-02 | L2 |
| ID-A02 | Investigación de insider risk correlacionada con riesgo de identidad | SOC + Privacidad | — | L1 |
| ID-A03 | Alta/baja de identidades de agentes (Entra Agent ID), sponsors y permisos | IAM + PO-GAC | IA-06 | L2 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| ID-A04 | Tabletop de compromiso de identidad privilegiada (incl. 'agente comprometido') | SOC Oversight + IAM | — | L1 |

## 3. Prácticas agnósticas eo:OP (20)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | ID-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | ID-W04, ID-A03 | Nueva (propuesta MAEO) |
| eo:OP-AYI-03 Mantener el inventario y la higiene de identidades privilegiadas | ID-M02 | Nueva (propuesta MAEO) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | ID-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | ID-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-11 Reportar la postura y su tendencia | ID-W01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | ID-M04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | ID-M01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | ID-D05, ID-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-18 Evaluar el efecto de las políticas de acceso y ajustarlas | ID-W03 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | ID-W05 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | ID-M03 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | ID-D06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | ID-D02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | ID-D03, ID-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | ID-D04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | ID-W02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | ID-A04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-29 Revisar el tablero de postura y riesgo del dominio | ID-D01 | Nueva (propuesta MAEO) |
| eo:OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | ID-A02 | Nueva (propuesta MAEO) |

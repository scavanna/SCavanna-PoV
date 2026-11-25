# 03 · Modelo operativo del control XDR (28 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Detección y respuesta unificada (Microsoft Defender XDR)** · 2026-11-14 · Dominio_XDR v1.0. Nivel de abstracción: *ProductPractice* / escenario (plano B). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuentes: Defender XDR SecOps guide (steps 4–6), MDE Security Operations Guide, MDI operational guide, MDA daily guide, AIR y Unified RBAC. XDR-Q02/Q03 son propuestas del sub-plan.

## 1. Tareas

| ID | Tarea | Cadencia | Persona (Learn) | CSF 2.0 | SAF | Práctica agnóstica eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) | Diaria | Monitoring (Tier 1-2) | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | XA-01 | % H/M triados en SLA | Learn: integrate-microsoft-365-defender-secops-tasks |
| XDR-D02 | Investigar incidentes correlacionados y ejecutar/aprobar acciones de respuesta | Diaria | Monitoring (Tier 2) + CSIRT | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | XA-02 | MTTR por severidad | Learn: manage-incidents; m365d-autoir |
| XDR-D03 | Revisar el Action center: acciones pendientes y ejecutadas (AIR) | Diaria | Monitoring + Engineering | RS.MI, GV.OV | SOP | eo:OP-SOP-27 Supervisar la remediación automatizada | L2 | XA-03 | Pendientes >4 h = 0 | Learn: m365d-autoir-actions |
| XDR-D04 | Clasificar incidentes y resolver los remediados | Diaria | Monitoring | RS.AN, ID.IM | SOP | eo:OP-SOP-13 Clasificar incidentes para aprender patrones | L2 | XA-01 | % clasificados | Learn: ops-guide-daily (MDA) |
| XDR-D05 | Gestionar FP/FN y tuning de alertas en todos los sensores | Diaria | Monitoring + Security Administration | ID.IM, PR.PS | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L2 | XA-04 | Alertas suprimidas con justificación | Learn: mde-sec-ops-guide |
| XDR-D06 | Revisar salud de sensores (EDR/AV, MDI, conectores de apps) | Diaria | Security Administration | PR.PS, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | XA-05 | % EDR saludable; MDI issues = 0 | Learn: mde-sec-ops-guide; ops-guide-daily (MDI) |
| XDR-D07 | Revisar Threat analytics de alto impacto y derivar acciones | Diaria/Semanal | Threat Intelligence & Analytics | ID.RA, DE.AE | SOP | eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | L2 | XA-06 | Acciones derivadas | Learn: mde-sec-ops-guide |
| XDR-D08 | Actualizar tickets de escalamiento (ITSM) y notificaciones | Diaria | Todos los equipos SOC | RS.MA, RS.CO | SOP | eo:OP-SOP-25 Mantener trazabilidad de escalamientos | L3 | XA-15 | Tickets sincronizados | Learn: secops-tasks |
| XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 | Semanal | Monitoring (Tier 2-3) + TI | DE.CM, ID.RA | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | XA-07 | Hunts/semana | Learn: advanced-hunting-overview |
| XDR-W02 | Crear/revisar detecciones personalizadas y automation rules | Semanal | Engineering & SecOps | DE.AE, PR.PS | SOP | eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | L2 | XA-07 | Detecciones vigentes; precisión | Learn: custom-detections-overview |
| XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog | Semanal | SOC Monitoring + Security Administration | ID.IM, GV.OV | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | XA-08 | Secure Score por producto | Learn: secops-tasks |
| XDR-W04 | Revisar informes de amenazas y protección | Semanal | Monitoring + Security Administration | DE.CM, ID.RA | POS | eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | L3 | XA-09 | Informe semanal | Learn: mde-sec-ops-guide |
| XDR-W05 | Revisar Message Center y novedades; evaluar impacto | Semanal | SOC Oversight | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | XA-10 | Cambios evaluados ≤7 días | Learn: mde-sec-ops-guide |
| XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM | Semanal | Engineering & SecOps | PR.PS, DE.CM | SOP | eo:OP-SOP-22 Mantener la automatización operativa | L1 | — | Automatizaciones probadas | Learn: configure-siem-defender |
| XDR-M01 | Revisar niveles de automatización por grupo de dispositivos y políticas de alertas | Mensual | Security Administration + SOC Oversight | PR.PS, GV.PO | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | XA-11 | Grupos fuera de baseline = 0 | Learn: m365d-configure-auto-investigation-response |
| XDR-M02 | Revisar Unified RBAC: roles, permisos y asignaciones de humanos y agentes | Mensual | SOC Oversight + IAM | PR.AA, GV.RR | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | XA-11 | Asignaciones sin justificación = 0 | Learn: custom-permissions-details |
| XDR-M03 | Revisar alertas tuned/suprimidas y reglas sin coincidencias | Mensual | Security Administration | ID.IM, DE.AE | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | XA-04 | Reglas obsoletas retiradas | Learn: ops-guide-monthly (MDI) |
| XDR-M04 | Informe mensual de seguridad para el CISO | Mensual | SOC Oversight | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | XA-09 | Informe a tiempo | Learn: threat-protection-reports |
| XDR-M05 | Actualizar entrenamiento del SOC con lecciones; ejercicios Blue/Red/Purple | Mensual | SOC Oversight | PR.AT, ID.IM | SIG | eo:OP-SIG-11 Convertir lecciones del SOC en concientización | L1 | XA-12 | Ejercicios realizados | Learn: secops-roles |
| XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor | Trimestral | SOC Oversight + CSIRT + TI | GV.PO, RS.MA | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Casos de uso vigentes | Learn: secops-use-cases |
| XDR-Q02 | Revisar desempeño y costo de la flota de agentes XDR | Trimestral | PO-GAC | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | XA-13 | KPIs vs. meta | Propuesta (sub-plan) |
| XDR-Q03 | Recertificar accesos de humanos y agentes (Unified RBAC + Entra Agent ID) | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | XA-13 | % recertificados | Propuesta (sub-plan) |
| XDR-Q04 | Evaluaciones/regresión y red teaming de agentes; service health; setup de sensores | Trimestral | PO-GAC + AppSec + Security Administration | ID.IM, PR.PS | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % agentes evaluados | Propuesta; ops-guide-quarterly (MDI) |
| XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) | Por evento | CSIRT + Monitoring | RS.MI, RS.CO | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | XA-02 | Tiempo a contención | Learn: secops-roles (CSIRT) |
| XDR-A02 | Live response / recolección de paquetes de investigación | Por evento | Tier 3 / CSIRT | RS.AN | SOP | eo:OP-SOP-28 Recolectar evidencia forense con autoridad y registro | L1 | — | Paquetes con registro | Learn: custom-permissions-details |
| XDR-A03 | Crear incidentes/alertas manuales; fusionar o dividir incidentes | Por evento | Monitoring | RS.MA | SOP | eo:OP-SOP-12 Cerrar incidentes con criterio documentado | L2 | XA-01 | Incidentes manuales trazados | Learn: manually-create-incident |
| XDR-A04 | Onboarding/offboarding de dispositivos y fuentes; device discovery | Por evento | Engineering & SecOps | ID.AM, PR.PS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | XA-05 | Dispositivos no onboarded | Learn: mde-sec-ops-guide |
| XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') | Según necesidad | SOC Oversight + CSIRT | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | Learn: secops-roles; AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-D01 | Triar la cola de incidentes unificada (todas las fuentes; High/Medium primero) | Monitoring (Tier 1-2) | XA-01 | L2 |
| XDR-D02 | Investigar incidentes correlacionados y ejecutar/aprobar acciones de respuesta | Monitoring (Tier 2) + CSIRT | XA-02 | L2 |
| XDR-D03 | Revisar el Action center: acciones pendientes y ejecutadas (AIR) | Monitoring + Engineering | XA-03 | L2 |
| XDR-D04 | Clasificar incidentes y resolver los remediados | Monitoring | XA-01 | L2 |
| XDR-D05 | Gestionar FP/FN y tuning de alertas en todos los sensores | Monitoring + Security Administration | XA-04 | L2 |
| XDR-D06 | Revisar salud de sensores (EDR/AV, MDI, conectores de apps) | Security Administration | XA-05 | L3 |
| XDR-D07 | Revisar Threat analytics de alto impacto y derivar acciones | Threat Intelligence & Analytics | XA-06 | L2 |
| XDR-D08 | Actualizar tickets de escalamiento (ITSM) y notificaciones | Todos los equipos SOC | XA-15 | L3 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-W01 | Hunting proactivo cross-domain y guided hunting para Tier 1 | Monitoring (Tier 2-3) + TI | XA-07 | L1 |
| XDR-W02 | Crear/revisar detecciones personalizadas y automation rules | Engineering & SecOps | XA-07 | L2 |
| XDR-W03 | Revisar Secure Score y Exposure Management; alimentar backlog | SOC Monitoring + Security Administration | XA-08 | L3 |
| XDR-W04 | Revisar informes de amenazas y protección | Monitoring + Security Administration | XA-09 | L3 |
| XDR-W05 | Revisar Message Center y novedades; evaluar impacto | SOC Oversight | XA-10 | L3 |
| XDR-W06 | Desplegar/probar automatizaciones aprobadas; verificar conectividad SIEM | Engineering & SecOps | — | L1 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-M01 | Revisar niveles de automatización por grupo de dispositivos y políticas de alertas | Security Administration + SOC Oversight | XA-11 | L2 |
| XDR-M02 | Revisar Unified RBAC: roles, permisos y asignaciones de humanos y agentes | SOC Oversight + IAM | XA-11 | L2 |
| XDR-M03 | Revisar alertas tuned/suprimidas y reglas sin coincidencias | Security Administration | XA-04 | L2 |
| XDR-M04 | Informe mensual de seguridad para el CISO | SOC Oversight | XA-09 | L3 |
| XDR-M05 | Actualizar entrenamiento del SOC con lecciones; ejercicios Blue/Red/Purple | SOC Oversight | XA-12 | L1 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-Q01 | Revisar casos de uso del SOC, playbooks del CSIRT y modelo de amenazas por sensor | SOC Oversight + CSIRT + TI | — | L1 |
| XDR-Q02 | Revisar desempeño y costo de la flota de agentes XDR | PO-GAC | XA-13 | L1 |
| XDR-Q03 | Recertificar accesos de humanos y agentes (Unified RBAC + Entra Agent ID) | PO-GAC + IAM | XA-13 | L2 |
| XDR-Q04 | Evaluaciones/regresión y red teaming de agentes; service health; setup de sensores | PO-GAC + AppSec + Security Administration | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-A01 | Responder a incidentes mayores con el CSIRT (aislar, revocar, deshabilitar, contener) | CSIRT + Monitoring | XA-02 | L2 |
| XDR-A02 | Live response / recolección de paquetes de investigación | Tier 3 / CSIRT | — | L1 |
| XDR-A03 | Crear incidentes/alertas manuales; fusionar o dividir incidentes | Monitoring | XA-01 | L2 |
| XDR-A04 | Onboarding/offboarding de dispositivos y fuentes; device discovery | Engineering & SecOps | XA-05 | L2 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| XDR-A05 | Tabletop / Purple team cross-domain (incl. 'agente comprometido') | SOC Oversight + CSIRT | — | L1 |

## 3. Prácticas agnósticas (26)

| Práctica eo:OP | Tareas XDR | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | XDR-M02, XDR-Q03 | Reutilizada (instancia productividad) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | XDR-Q02 | Reutilizada (instancia productividad) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | XDR-Q04 | Reutilizada (instancia productividad) |
| eo:OP-POS-11 Reportar la postura y su tendencia | XDR-W03 | Reutilizada (instancia productividad) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | XDR-M01 | Reutilizada (instancia productividad) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | XDR-M03 | Reutilizada (instancia productividad) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | XDR-D06 | Nueva (propuesta MAEO) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | XDR-A04 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | XDR-W05 | Reutilizada (instancia productividad) |
| eo:OP-SIG-11 Convertir lecciones del SOC en concientización | XDR-M05 | Reutilizada (instancia productividad) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | XDR-Q01 | Reutilizada (instancia productividad) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | XDR-M04 | Nueva (propuesta MAEO) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | XDR-W01 | Reutilizada (instancia productividad) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | XDR-D01 | Reutilizada (instancia productividad) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | XDR-D02, XDR-A01 | Reutilizada (instancia productividad) |
| eo:OP-SOP-12 Cerrar incidentes con criterio documentado | XDR-A03 | Reutilizada (instancia productividad) |
| eo:OP-SOP-13 Clasificar incidentes para aprender patrones | XDR-D04 | Reutilizada (instancia productividad) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | XDR-D05 | Reutilizada (instancia productividad) |
| eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | XDR-W04 | Reutilizada (instancia productividad) |
| eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | XDR-D07 | Reutilizada (instancia productividad) |
| eo:OP-SOP-22 Mantener la automatización operativa | XDR-W06 | Reutilizada (instancia productividad) |
| eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | XDR-W02 | Reutilizada (instancia productividad) |
| eo:OP-SOP-25 Mantener trazabilidad de escalamientos | XDR-D08 | Reutilizada (instancia productividad) |
| eo:OP-SOP-26 Probar los planes de respuesta | XDR-A05 | Reutilizada (instancia productividad) |
| eo:OP-SOP-27 Supervisar la remediación automatizada | XDR-D03 | Nueva (propuesta MAEO) |
| eo:OP-SOP-28 Recolectar evidencia forense con autoridad y registro | XDR-A02 | Nueva (propuesta MAEO) |

La reutilización de prácticas eo:OP entre dominios demuestra que el modelo es portable: la tarea de producto cambia, la práctica agnóstica no.

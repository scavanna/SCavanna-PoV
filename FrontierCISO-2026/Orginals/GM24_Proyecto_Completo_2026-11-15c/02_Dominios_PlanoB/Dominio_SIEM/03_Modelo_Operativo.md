# 03 · Modelo operativo (24 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Microsoft Sentinel operational guide (diario/semanal/mensual) + deployment checklist post-despliegue + SOC optimization + health & audit.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| SI-D01 | Triar e investigar incidentes de Sentinel en el portal unificado | Diaria | SOC analysts | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | SA-01 | % H/M en SLA | Sentinel ops guide (daily) |
| SI-D02 | Revisar salud de conectores y agentes AMA | Diaria | Sentinel admins | ID.AM, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | SA-05 | Conectores en error = 0 | Sentinel ops guide (daily) |
| SI-D03 | Revisar/habilitar reglas analíticas nuevas; monitorear salud de reglas | Diaria | Security engineers | DE.AE, PR.PS | SOP | eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | L2 | SA-07 | Reglas fallidas = 0 | Sentinel ops guide (daily) |
| SI-D04 | Explorar hunting queries y bookmarks | Diaria | SOC analysts (Tier 2-3) | DE.CM | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | SA-07 | Hunts | Sentinel ops guide (daily) |
| SI-D05 | Verificar ejecución de playbooks y automation rules | Diaria | Security engineers | RS.MI, PR.PS | SOP | eo:OP-SOP-22 Mantener la automatización operativa | L2 | SA-03 | Fallidos ≤24 h | monitor-automation-health |
| SI-W01 | Revisar Content hub (soluciones, reglas, workbooks, playbooks) | Semanal | Security engineers | ID.IM, DE.AE | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | SA-04 | Contenido evaluado | Sentinel ops guide (weekly) |
| SI-W02 | Auditar actividad de Sentinel (cambios de reglas, bookmarks, automatización) | Semanal | Sentinel admins | GV.OV, PR.PS | POS | eo:OP-POS-22 Auditar cambios de la plataforma de detección y automatización | L3 | SA-06 | Cambios no autorizados = 0 | audit-sentinel-data |
| SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas | Semanal | Security engineers + TI | ID.RA, DE.AE | POS | eo:OP-POS-23 Medir y cerrar la cobertura de detección por técnica | L3 | SA-04 | Cobertura ≥90 % | MITRE coverage |
| SI-W04 | Revisar ingesta y costo vs. commitment tier | Semanal | Sentinel admins + FinOps | GV.OV, ID.AM | POS | eo:OP-POS-24 Gobernar el costo de ingesta y retención | L3 | SA-08 | Desvío ≤10 % | billing-monitor-costs |
| SI-W05 | Revisar recomendaciones de SOC optimization | Semanal | Security engineers | ID.IM, DE.AE | POS | eo:OP-POS-23 Medir y cerrar la cobertura de detección por técnica | L2 | SA-04 | Recomendaciones tratadas | soc-optimization-access |
| SI-W06 | Revisar ingesta de TI y reglas de matching | Semanal | TI | ID.RA | SOP | eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | L2 | SA-02 | Indicadores vigentes | understand-threat-intelligence |
| SI-M01 | Revisar accesos a Sentinel y Log Analytics; inactivos | Mensual | Sentinel admins + IAM | PR.AA, GV.RR | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | SA-06 | Inactivos removidos | Sentinel ops guide (monthly) |
| SI-M02 | Revisar retención y almacenamiento a largo plazo | Mensual | Sentinel admins | PR.PS, GV.PO | POS | eo:OP-POS-24 Gobernar el costo de ingesta y retención | L2 | SA-08 | Retención alineada | Sentinel ops guide (monthly) |
| SI-M03 | Actualizar watchlists y revisar commitment tiers | Mensual | Security engineers + FinOps | ID.AM, GV.OV | POS | eo:OP-POS-24 Gobernar el costo de ingesta y retención | L2 | SA-08 | Watchlists al día | deploy-overview |
| SI-M04 | Afinar DCRs y transformaciones de ingesta | Mensual | Security engineers | PR.PS, ID.AM | POS | eo:OP-POS-24 Gobernar el costo de ingesta y retención | L1 | SA-05 | Datos sin valor filtrados | deploy-overview (DCRs) |
| SI-M05 | Informe mensual del SOC (eficiencia) para el CISO | Mensual | SOC Lead | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | SA-09 | Informe a tiempo | top-workbooks |
| SI-Q01 | Revisar casos de uso, supresión y apetito de automatización | Trimestral | SOC Lead + CISO | GV.PO, GV.RM | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Decisiones registradas | Propuesta |
| SI-Q02 | Revisar desempeño y costo de la flota SIEM | Trimestral | PO-GAC SIEM | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | SA-10 | KPIs vs. meta | Propuesta |
| SI-Q03 | Recertificar roles de Sentinel/Logic Apps (humanos y agentes, incl. Sentinel MCP) | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | SA-10 | % recertificados | Propuesta |
| SI-Q04 | Evaluaciones/regresión de agentes y pruebas de playbooks en escenarios de falla | Trimestral | PO-GAC + Security engineers | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| SI-A01 | Onboarding de una fuente de datos (conector, DCR, parser, reglas, costo) | Por evento | Security engineers | ID.AM, PR.PS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L1 | SA-05 | Fuentes onboarded | connect-data-sources |
| SI-A02 | Crear/modificar regla analítica o automation rule (prueba, versión, aprobación) | Por evento | Security engineers | DE.AE, RS.MI | SOP | eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | L2 | SA-07 | Reglas versionadas | create-analytics-rule |
| SI-A03 | Migración al portal de Defender (antes del 31-mar-2027) | Por evento | Sentinel admins | PR.PS, GV.OV | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L1 | — | Hito cumplido | move-to-defender |
| SI-A04 | Tabletop de pérdida de visibilidad | Según necesidad | SOC Lead | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-D01 | Triar e investigar incidentes de Sentinel en el portal unificado | SOC analysts | SA-01 | L2 |
| SI-D02 | Revisar salud de conectores y agentes AMA | Sentinel admins | SA-05 | L3 |
| SI-D03 | Revisar/habilitar reglas analíticas nuevas; monitorear salud de reglas | Security engineers | SA-07 | L2 |
| SI-D04 | Explorar hunting queries y bookmarks | SOC analysts (Tier 2-3) | SA-07 | L1 |
| SI-D05 | Verificar ejecución de playbooks y automation rules | Security engineers | SA-03 | L2 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-W01 | Revisar Content hub (soluciones, reglas, workbooks, playbooks) | Security engineers | SA-04 | L3 |
| SI-W02 | Auditar actividad de Sentinel (cambios de reglas, bookmarks, automatización) | Sentinel admins | SA-06 | L3 |
| SI-W03 | Revisar cobertura MITRE de reglas vs. técnicas priorizadas | Security engineers + TI | SA-04 | L3 |
| SI-W04 | Revisar ingesta y costo vs. commitment tier | Sentinel admins + FinOps | SA-08 | L3 |
| SI-W05 | Revisar recomendaciones de SOC optimization | Security engineers | SA-04 | L2 |
| SI-W06 | Revisar ingesta de TI y reglas de matching | TI | SA-02 | L2 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-M01 | Revisar accesos a Sentinel y Log Analytics; inactivos | Sentinel admins + IAM | SA-06 | L2 |
| SI-M02 | Revisar retención y almacenamiento a largo plazo | Sentinel admins | SA-08 | L2 |
| SI-M03 | Actualizar watchlists y revisar commitment tiers | Security engineers + FinOps | SA-08 | L2 |
| SI-M04 | Afinar DCRs y transformaciones de ingesta | Security engineers | SA-05 | L1 |
| SI-M05 | Informe mensual del SOC (eficiencia) para el CISO | SOC Lead | SA-09 | L3 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-Q01 | Revisar casos de uso, supresión y apetito de automatización | SOC Lead + CISO | — | L1 |
| SI-Q02 | Revisar desempeño y costo de la flota SIEM | PO-GAC SIEM | SA-10 | L1 |
| SI-Q03 | Recertificar roles de Sentinel/Logic Apps (humanos y agentes, incl. Sentinel MCP) | PO-GAC + IAM | SA-10 | L2 |
| SI-Q04 | Evaluaciones/regresión de agentes y pruebas de playbooks en escenarios de falla | PO-GAC + Security engineers | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-A01 | Onboarding de una fuente de datos (conector, DCR, parser, reglas, costo) | Security engineers | SA-05 | L1 |
| SI-A02 | Crear/modificar regla analítica o automation rule (prueba, versión, aprobación) | Security engineers | SA-07 | L2 |
| SI-A03 | Migración al portal de Defender (antes del 31-mar-2027) | Sentinel admins | — | L1 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| SI-A04 | Tabletop de pérdida de visibilidad | SOC Lead | — | L1 |

## 3. Prácticas agnósticas eo:OP (17)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | SI-M01, SI-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | SI-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | SI-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | SI-D02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | SI-A01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-22 Auditar cambios de la plataforma de detección y automatización | SI-W02 | Nueva (propuesta MAEO) |
| eo:OP-POS-23 Medir y cerrar la cobertura de detección por técnica | SI-W03, SI-W05 | Nueva (propuesta MAEO) |
| eo:OP-POS-24 Gobernar el costo de ingesta y retención | SI-W04, SI-M02, SI-M03, SI-M04 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | SI-W01, SI-A03 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | SI-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | SI-M05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | SI-D04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | SI-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | SI-W06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-22 Mantener la automatización operativa | SI-D05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-24 Convertir hunting en detecciones automatizadas | SI-D03, SI-A02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | SI-A04 | Reutilizada (productividad/XDR) |

# 03 · Modelo operativo (25 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Deploy an information protection solution with Microsoft Purview (fases 1–3; roles); default labels & policies (DSPM setup tasks); plan for DLP; DLP alerts; Insider Risk Management; Defender for Cloud Apps information protection.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver | Diaria | Information Protection Analyst | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | DA-01 | % High ≤4 h | Purview DLP alerts |
| DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción | Diaria | Information Protection Investigator | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | DA-02 | MTTR; revertidas <2 % | activity explorer |
| DP-D03 | Gestionar FP DLP: coincidencias de SIT, umbrales, excepciones con vencimiento; simulación antes de bloquear | Diaria | Information Protection Admin | ID.IM, PR.DS | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L2 | DA-03 | FP recurrentes ↓ | plan for DLP |
| DP-D04 | Revisar DSPM / DSPM for AI: uso de datos sensibles por Copilot y agentes, prompts riesgosos | Diaria | Data Security Management | ID.RA, DE.CM | POS | eo:OP-POS-19 Vigilar la postura de datos y su uso por IA | L3 | DA-04 | Recomendaciones críticas abiertas | DSPM for AI |
| DP-D05 | Revisar salud de la clasificación: auto-labeling, scanner, conectores MDA | Diaria | Information Protection Admin | PR.PS, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | DA-05 | Políticas en error = 0 | deploy-scanner |
| DP-W01 | Revisar simulación de auto-etiquetado y DLP en prueba; proponer producción | Semanal | Information Protection Admin + data owners | PR.DS, ID.IM | POS | eo:OP-POS-20 Promover políticas de protección de datos de simulación a producción con evidencia | L2 | DA-06 | Políticas promovidas | apply-sensitivity-label-automatically |
| DP-W02 | Revisar cobertura de etiquetado y tendencia | Semanal | Information Protection Analyst | ID.AM, PR.DS | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | DA-07 | Cobertura ≥90 % | data classification reports |
| DP-W03 | Revisar sobrecompartición: 'Anyone', externos, sitios sensibles | Semanal | Information Protection Analyst + SharePoint admin | ID.RA, PR.AA | POS | eo:OP-POS-21 Reducir la sobrecompartición de información sensible | L2 | DA-08 | 'Anyone' en sensibles = 0 | DSPM oversharing |
| DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas | Semanal | Investigator | DE.CM | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | DA-09 | Hunts | advanced hunting |
| DP-W05 | Revisar Message Center y novedades de Purview | Semanal | Information Protection Admin | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | DA-10 | Cambios evaluados ≤7 días | Message Center |
| DP-W06 | Revisar file policies de MDA (SaaS) y acciones de gobierno | Semanal | Information Protection Admin + SecOps | PR.DS, RS.MI | POS | eo:OP-POS-21 Reducir la sobrecompartición de información sensible | L2 | DA-08 | Archivos expuestos en SaaS ↓ | Defender for Cloud Apps |
| DP-M01 | Revisar taxonomía de etiquetas y políticas de publicación con dueños de negocio | Mensual | Information Protection Admin + data owners | GV.PO, PR.DS | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Taxonomía vigente | create-sensitivity-labels |
| DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento | Mensual | Information Protection Admin | GV.PO, ID.IM | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | DA-03 | Overrides sin justificación = 0 | DLP overrides |
| DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos | Mensual | IRM Admin + Privacidad | ID.RA, GV.PO | SIG | eo:OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | L1 | — | Casos en SLA | insider-risk-management |
| DP-M04 | Informe mensual de protección de datos para CISO y CDO | Mensual | Data Security Management | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | DA-07 | Informe a tiempo | purview-reports |
| DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias | Mensual | Compliance Administrator | GV.OV, ID.IM | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | DA-07 | Acciones cerradas | compliance-manager |
| DP-M06 | Revisar fuentes de conocimiento y DLP para IA de las flotas (todos los dominios) | Mensual | Information Protection Admin + PO-GAC de cada dominio | PR.DS, PR.AA | IA | eo:OP-IA-04 Gobernar los datos que alcanzan los agentes | L2 | DA-04 | Fuentes no aprobadas = 0 | Purview APIs for AI apps; AMP-32 |
| DP-Q01 | Revisar política de protección de datos, apetito y mapa de datos sensibles | Trimestral | PO-GAC Datos + CISO + CDO | GV.PO, GV.RM | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Decisiones registradas | Propuesta |
| DP-Q02 | Revisar desempeño y costo de la flota Datos | Trimestral | PO-GAC Datos | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | DA-11 | KPIs vs. meta | Propuesta |
| DP-Q03 | Recertificar roles de Purview y permisos de agentes | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | DA-11 | % recertificados | scc-permissions |
| DP-Q04 | Evaluaciones/regresión y red teaming (fuga de datos en salidas, evasión de DLP) | Trimestral | PO-GAC + AppSec | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) | Por evento | Investigator + SecOps + Legal | RS.MI, RS.CO | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | DA-02 | Tiempo a contención | DLP incident response |
| DP-A02 | Descubrimiento y etiquetado de un nuevo repositorio (on-prem, SaaS, Azure Storage) | Por evento | Information Protection Admin | ID.AM, PR.DS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | DA-05 | Repositorios sin descubrir ↓ | deploy-scanner |
| DP-A03 | Alta de etiqueta/SIT/clasificador y su política (simulación → producción) | Por evento | Information Protection Admin + data owners | GV.PO, PR.DS | POS | eo:OP-POS-20 Promover políticas de protección de datos de simulación a producción con evidencia | L2 | DA-06 | Políticas promovidas | trainable classifiers |
| DP-A04 | Tabletop de fuga de datos / insider (incl. 'agente filtra datos') | Según necesidad | PO-GAC Datos + Legal + CSIRT | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver | Information Protection Analyst | DA-01 | L2 |
| DP-D02 | Investigar alertas DLP (Activity/Content explorer); decidir acción | Information Protection Investigator | DA-02 | L2 |
| DP-D03 | Gestionar FP DLP: coincidencias de SIT, umbrales, excepciones con vencimiento; simulación antes de bloquear | Information Protection Admin | DA-03 | L2 |
| DP-D04 | Revisar DSPM / DSPM for AI: uso de datos sensibles por Copilot y agentes, prompts riesgosos | Data Security Management | DA-04 | L3 |
| DP-D05 | Revisar salud de la clasificación: auto-labeling, scanner, conectores MDA | Information Protection Admin | DA-05 | L3 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-W01 | Revisar simulación de auto-etiquetado y DLP en prueba; proponer producción | Information Protection Admin + data owners | DA-06 | L2 |
| DP-W02 | Revisar cobertura de etiquetado y tendencia | Information Protection Analyst | DA-07 | L3 |
| DP-W03 | Revisar sobrecompartición: 'Anyone', externos, sitios sensibles | Information Protection Analyst + SharePoint admin | DA-08 | L2 |
| DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas | Investigator | DA-09 | L1 |
| DP-W05 | Revisar Message Center y novedades de Purview | Information Protection Admin | DA-10 | L3 |
| DP-W06 | Revisar file policies de MDA (SaaS) y acciones de gobierno | Information Protection Admin + SecOps | DA-08 | L2 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-M01 | Revisar taxonomía de etiquetas y políticas de publicación con dueños de negocio | Information Protection Admin + data owners | — | L1 |
| DP-M02 | Revisar excepciones DLP y overrides de usuario con vencimiento | Information Protection Admin | DA-03 | L2 |
| DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos | IRM Admin + Privacidad | — | L1 |
| DP-M04 | Informe mensual de protección de datos para CISO y CDO | Data Security Management | DA-07 | L3 |
| DP-M05 | Revisar Compliance Manager: acciones de mejora y evidencias | Compliance Administrator | DA-07 | L3 |
| DP-M06 | Revisar fuentes de conocimiento y DLP para IA de las flotas (todos los dominios) | Information Protection Admin + PO-GAC de cada dominio | DA-04 | L2 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-Q01 | Revisar política de protección de datos, apetito y mapa de datos sensibles | PO-GAC Datos + CISO + CDO | — | L1 |
| DP-Q02 | Revisar desempeño y costo de la flota Datos | PO-GAC Datos | DA-11 | L1 |
| DP-Q03 | Recertificar roles de Purview y permisos de agentes | PO-GAC + IAM | DA-11 | L2 |
| DP-Q04 | Evaluaciones/regresión y red teaming (fuga de datos en salidas, evasión de DLP) | PO-GAC + AppSec | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-A01 | Respuesta a fuga de datos: alcance, quitar compartición, cuarentena, revocar, notificar (Legal) | Investigator + SecOps + Legal | DA-02 | L2 |
| DP-A02 | Descubrimiento y etiquetado de un nuevo repositorio (on-prem, SaaS, Azure Storage) | Information Protection Admin | DA-05 | L2 |
| DP-A03 | Alta de etiqueta/SIT/clasificador y su política (simulación → producción) | Information Protection Admin + data owners | DA-06 | L2 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| DP-A04 | Tabletop de fuga de datos / insider (incl. 'agente filtra datos') | PO-GAC Datos + Legal + CSIRT | — | L1 |

## 3. Prácticas agnósticas eo:OP (20)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | DP-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | DP-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | DP-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-IA-04 Gobernar los datos que alcanzan los agentes | DP-M06 | Nueva (propuesta MAEO) |
| eo:OP-POS-11 Reportar la postura y su tendencia | DP-W02, DP-M05 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | DP-M02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | DP-D05 | Reutilizada (productividad/XDR) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | DP-A02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-19 Vigilar la postura de datos y su uso por IA | DP-D04 | Nueva (propuesta MAEO) |
| eo:OP-POS-20 Promover políticas de protección de datos de simulación a producción con evidencia | DP-W01, DP-A03 | Nueva (propuesta MAEO) |
| eo:OP-POS-21 Reducir la sobrecompartición de información sensible | DP-W03, DP-W06 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | DP-W05 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | DP-M01, DP-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | DP-M04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | DP-W04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | DP-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | DP-D02, DP-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | DP-D03 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | DP-A04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-30 Investigar riesgo interno con proporcionalidad y privacidad | DP-M03 | Nueva (propuesta MAEO) |

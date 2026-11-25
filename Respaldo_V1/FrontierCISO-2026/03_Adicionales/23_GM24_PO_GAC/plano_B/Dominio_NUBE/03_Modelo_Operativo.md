# 03 · Modelo operativo (23 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Defender for Cloud: secure score y MCSB; recommendations y governance rules; attack path analysis; regulatory compliance; workflow automation; release notes.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| CL-D01 | Triar alertas de carga de trabajo en la cola unificada; correlar con XDR | Diaria | SOC analysts | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | CA-01 | % High ≤30 min | alerts-reference |
| CL-D02 | Revisar attack paths nuevos/críticos; asignar dueño | Diaria | Security Admin + Plataforma | ID.RA, PR.PS | POS | eo:OP-POS-25 Priorizar la reducción de exposición por rutas de ataque | L2 | CA-02 | Attack paths críticos >30 días = 0 | how-to-manage-attack-path |
| CL-D03 | Revisar recomendaciones nuevas de alto riesgo; asignar dueño/fecha (governance rules) | Diaria | Security Admin | ID.IM, GV.OV | POS | eo:OP-POS-26 Gobernar la remediación de recomendaciones con dueño y fecha | L2 | CA-03 | Críticas sin dueño = 0 | governance-rules |
| CL-W01 | Revisar secure score por suscripción/conector y tendencia | Semanal | Security Admin | ID.IM, GV.OV | POS | eo:OP-POS-11 Reportar la postura y su tendencia | L3 | CA-04 | Score ↑ | secure-score-security-controls |
| CL-W02 | Revisar recomendaciones vencidas y notificar a dueños | Semanal | Security Admin | GV.OV, ID.IM | POS | eo:OP-POS-26 Gobernar la remediación de recomendaciones con dueño y fecha | L3 | CA-03 | Vencidas ≤5 % | review-security-recommendations |
| CL-W03 | Revisar cumplimiento regulatorio y exenciones | Semanal | Cumplimiento + Security Admin | GV.OV, GV.OC | POS | eo:OP-POS-27 Sostener el cumplimiento regulatorio de la nube con evidencia | L3 | CA-05 | Cumplimiento ≥90 % | regulatory-compliance |
| CL-W04 | Revisar cobertura de planes Defender y recursos sin protección (incl. AI services) | Semanal | Security Admin + FinOps | PR.PS, ID.AM | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L3 | CA-06 | Críticas sin plan = 0 | manage-plans |
| CL-W05 | Revisar postura y alertas de recursos de IA (Defender for AI Services; AI-SPM) | Semanal | Security Admin + PO-GAC de dominios | PR.PS, DE.CM | IA | eo:OP-IA-05 Vigilar la postura y las amenazas de los recursos de IA | L3 | CA-07 | Recomendaciones de IA críticas abiertas | ai-threat-protection |
| CL-W06 | Verificar workflow automations y continuous export a Sentinel | Semanal | Security engineers | RS.MI, PR.PS | SOP | eo:OP-SOP-22 Mantener la automatización operativa | L2 | CA-08 | Fallidas = 0 | workflow-automations |
| CL-W07 | Revisar release notes / Message Center; evaluar impacto | Semanal | Security Admin | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | CA-09 | Cambios evaluados ≤7 días | release-notes |
| CL-M01 | Revisar governance rules y exenciones con vencimiento | Mensual | Security Admin + SOC Oversight | GV.PO, GV.RR | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | CA-03 | Exenciones sin vencimiento = 0 | governance-rules |
| CL-M02 | Revisar costo (DWU, planes) y optimizar | Mensual | FinOps + Security Admin | GV.OV | POS | eo:OP-POS-24 Gobernar el costo de ingesta y retención | L3 | CA-06 | Desvío ≤10 % | estimate-track-costs |
| CL-M03 | Revisar inventario cloud y conectores multicloud; recursos no evaluados | Mensual | Security Admin + Plataforma | ID.AM | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | CA-06 | No evaluados ↓ | asset-inventory |
| CL-M04 | Revisar hardening preventivo (deny/enforce, JIT) y su efecto | Mensual | Security Admin + Plataforma | PR.PS, PR.AA | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | CA-02 | No conformes creados = 0 | prevent-misconfigurations |
| CL-M05 | Informe mensual de postura cloud | Mensual | Security Admin | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | CA-04 | Informe a tiempo | Propuesta |
| CL-Q01 | Revisar estándares asignados, recomendaciones personalizadas y apetito (deny) | Trimestral | PO-GAC Nube + Cumplimiento + CISO | GV.PO, GV.RM | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Decisiones registradas | create-custom-recommendations |
| CL-Q02 | Revisar desempeño y costo de la flota Nube | Trimestral | PO-GAC Nube | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | CA-10 | KPIs vs. meta | Propuesta |
| CL-Q03 | Recertificar roles (Security Admin/Reader, Owner/Contributor, cloud scopes) | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | CA-10 | % recertificados | cloud-scopes |
| CL-Q04 | Evaluaciones/regresión de agentes; prueba de workflow automation en falla | Trimestral | PO-GAC + Security engineers | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| CL-A01 | Respuesta a alerta crítica de carga de trabajo; coordinar con XDR/Endpoints | Por evento | SOC + Plataforma | RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | CA-01 | Tiempo a contención | defender-for-servers |
| CL-A02 | Onboarding de suscripción / cuenta AWS / proyecto GCP / Arc; asignar estándar y planes | Por evento | Security Admin + Plataforma | ID.AM, PR.PS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | CA-06 | Onboarded con planes | connect-azure-environments |
| CL-A03 | Crear recomendación o estándar personalizado | Por evento | Security Admin | GV.PO, PR.PS | POS | eo:OP-POS-27 Sostener el cumplimiento regulatorio de la nube con evidencia | L1 | CA-05 | Custom vigentes | create-custom-recommendations |
| CL-A04 | Tabletop de ruta de ataque explotada (incl. agente de IA como objetivo) | Según necesidad | PO-GAC Nube + CSIRT | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-D01 | Triar alertas de carga de trabajo en la cola unificada; correlar con XDR | SOC analysts | CA-01 | L2 |
| CL-D02 | Revisar attack paths nuevos/críticos; asignar dueño | Security Admin + Plataforma | CA-02 | L2 |
| CL-D03 | Revisar recomendaciones nuevas de alto riesgo; asignar dueño/fecha (governance rules) | Security Admin | CA-03 | L2 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-W01 | Revisar secure score por suscripción/conector y tendencia | Security Admin | CA-04 | L3 |
| CL-W02 | Revisar recomendaciones vencidas y notificar a dueños | Security Admin | CA-03 | L3 |
| CL-W03 | Revisar cumplimiento regulatorio y exenciones | Cumplimiento + Security Admin | CA-05 | L3 |
| CL-W04 | Revisar cobertura de planes Defender y recursos sin protección (incl. AI services) | Security Admin + FinOps | CA-06 | L3 |
| CL-W05 | Revisar postura y alertas de recursos de IA (Defender for AI Services; AI-SPM) | Security Admin + PO-GAC de dominios | CA-07 | L3 |
| CL-W06 | Verificar workflow automations y continuous export a Sentinel | Security engineers | CA-08 | L2 |
| CL-W07 | Revisar release notes / Message Center; evaluar impacto | Security Admin | CA-09 | L3 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-M01 | Revisar governance rules y exenciones con vencimiento | Security Admin + SOC Oversight | CA-03 | L2 |
| CL-M02 | Revisar costo (DWU, planes) y optimizar | FinOps + Security Admin | CA-06 | L3 |
| CL-M03 | Revisar inventario cloud y conectores multicloud; recursos no evaluados | Security Admin + Plataforma | CA-06 | L2 |
| CL-M04 | Revisar hardening preventivo (deny/enforce, JIT) y su efecto | Security Admin + Plataforma | CA-02 | L2 |
| CL-M05 | Informe mensual de postura cloud | Security Admin | CA-04 | L3 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-Q01 | Revisar estándares asignados, recomendaciones personalizadas y apetito (deny) | PO-GAC Nube + Cumplimiento + CISO | — | L1 |
| CL-Q02 | Revisar desempeño y costo de la flota Nube | PO-GAC Nube | CA-10 | L1 |
| CL-Q03 | Recertificar roles (Security Admin/Reader, Owner/Contributor, cloud scopes) | PO-GAC + IAM | CA-10 | L2 |
| CL-Q04 | Evaluaciones/regresión de agentes; prueba de workflow automation en falla | PO-GAC + Security engineers | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-A01 | Respuesta a alerta crítica de carga de trabajo; coordinar con XDR/Endpoints | SOC + Plataforma | CA-01 | L2 |
| CL-A02 | Onboarding de suscripción / cuenta AWS / proyecto GCP / Arc; asignar estándar y planes | Security Admin + Plataforma | CA-06 | L2 |
| CL-A03 | Crear recomendación o estándar personalizado | Security Admin | CA-05 | L1 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| CL-A04 | Tabletop de ruta de ataque explotada (incl. agente de IA como objetivo) | PO-GAC Nube + CSIRT | — | L1 |

## 3. Prácticas agnósticas eo:OP (19)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | CL-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | CL-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | CL-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-IA-05 Vigilar la postura y las amenazas de los recursos de IA | CL-W05 | Nueva (propuesta MAEO) |
| eo:OP-POS-11 Reportar la postura y su tendencia | CL-W01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | CL-M04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | CL-M01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | CL-W04, CL-M03, CL-A02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-24 Gobernar el costo de ingesta y retención | CL-M02 | Nueva (propuesta MAEO) |
| eo:OP-POS-25 Priorizar la reducción de exposición por rutas de ataque | CL-D02 | Nueva (propuesta MAEO) |
| eo:OP-POS-26 Gobernar la remediación de recomendaciones con dueño y fecha | CL-D03, CL-W02 | Nueva (propuesta MAEO) |
| eo:OP-POS-27 Sostener el cumplimiento regulatorio de la nube con evidencia | CL-W03, CL-A03 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | CL-W07 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | CL-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | CL-M05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | CL-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | CL-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-22 Mantener la automatización operativa | CL-W06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | CL-A04 | Reutilizada (productividad/XDR) |

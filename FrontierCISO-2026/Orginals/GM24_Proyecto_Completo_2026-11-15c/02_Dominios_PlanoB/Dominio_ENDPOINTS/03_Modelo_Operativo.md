# 03 · Modelo operativo (26 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Microsoft Defender for Endpoint Security Operations Guide (diario/semanal/mensual/ad hoc) + Defender Vulnerability Management + ASR + device groups; Intune security baselines.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| EP-D01 | Revisar acciones automáticas y manuales en el Action center | Diaria | Security Operations Team | RS.MI, GV.OV | SOP | eo:OP-SOP-27 Supervisar la remediación automatizada | L2 | EA-03 | Pendientes >4 h = 0 | MDE SecOps guide |
| EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados | Diaria | Security Operations Team | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | EA-01 | % H/M en SLA | MDE SecOps guide |
| EP-D03 | Gestionar FP/FN: indicadores, exclusiones, envíos; causa (ASR, AV, EDR) | Diaria | Security Operations Team | ID.IM, PR.PS | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L2 | EA-04 | FP recurrentes ↓ | MDE SecOps guide |
| EP-D04 | Revisar Threat analytics de alto impacto y derivar acciones | Diaria | Security Operations Team | ID.RA, DE.AE | SOP | eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | L2 | EA-06 | Acciones derivadas | MDE SecOps guide |
| EP-D05 | Revisar salud de dispositivos (AV signature/platform/engine, EDR sensor) | Diaria | Security Administration Team | PR.PS, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | EA-05 | % saludables ≥98 % | MDE SecOps guide |
| EP-D06 | Investigar incidentes de endpoint y ejecutar/aprobar acciones (aislar, restringir, scan, paquete) | Diaria | Tier 2-3 + CSIRT | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | EA-02 | MTTR; aislamientos revertidos <2 % | MDE API machineaction |
| EP-W01 | Revisar Message Center (MDE/Intune) y evaluar impacto | Semanal | General | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | EA-10 | Cambios evaluados ≤7 días | MDE SecOps guide |
| EP-W02 | Revisar threat protection report y tendencias | Semanal | Security Operations Team | DE.CM, ID.RA | POS | eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | L3 | EA-09 | Informe semanal | MDE SecOps guide |
| EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune | Semanal | Security Administration Team + IT | ID.RA, ID.IM | POS | eo:OP-POS-17 Priorizar y seguir la remediación de vulnerabilidades por riesgo | L2 | EA-07 | CVEs críticos ≤7 días | MDE SecOps guide (TVM) |
| EP-W04 | Revisar ASR rules report y proponer paso de audit a block | Semanal | Security Administration Team | PR.PS | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | EA-08 | % reglas en block | attack-surface-reduction-rules-report |
| EP-W05 | Revisar web protection / network protection y custom indicators | Semanal | Security Administration Team | DE.CM, PR.PS | POS | eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | L3 | EA-09 | Bloqueos; indicadores vigentes | MDE SecOps guide |
| EP-W06 | Hunting proactivo sobre Device* y detecciones personalizadas | Semanal | Tier 2-3 | DE.CM, ID.RA | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | EA-11 | Hunts; hallazgos→detecciones | advanced-hunting-overview |
| EP-M01 | Revisar device groups, niveles de automatización y RBAC por grupo | Mensual | Security Administration + SOC Oversight | PR.PS, PR.AA | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | EA-08 | Grupos fuera de baseline = 0 | configure-automated-investigations-remediation |
| EP-M02 | Revisar baselines de Intune y su deriva | Mensual | Security Administration + IT | PR.PS, PR.AA | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | EA-08 | No conformes ↓ | Intune security baselines |
| EP-M03 | Revisar device discovery: no gestionados y de red; plan de onboarding | Mensual | Engineering & SecOps | ID.AM | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | EA-05 | No gestionados ↓ | device-discovery |
| EP-M04 | Informe mensual de seguridad de endpoints | Mensual | SOC Oversight | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | EA-09 | Informe a tiempo | threat-protection-reports |
| EP-M05 | Revisar indicadores y exclusiones con vencimiento; retirar obsoletos | Mensual | Security Administration | ID.IM, PR.PS | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | EA-04 | Sin vencimiento = 0 | MDE indicators |
| EP-Q01 | Revisar política de endpoints, excepciones y apetito de autonomía | Trimestral | PO-GAC Endpoints + CISO | GV.PO, GV.RM | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Decisiones registradas | Propuesta |
| EP-Q02 | Revisar desempeño y costo de la flota Endpoints | Trimestral | PO-GAC Endpoints | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | EA-13 | KPIs vs. meta | Propuesta |
| EP-Q03 | Recertificar accesos (Unified RBAC por device group; Agent ID) | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | EA-13 | % recertificados | Propuesta |
| EP-Q04 | Evaluaciones/regresión y red teaming de agentes; prueba de reversión de aislamiento | Trimestral | PO-GAC + AppSec | ID.IM, PR.PS | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| EP-A01 | Respuesta a incidente mayor: aislamiento masivo acotado, restricción, offboarding | Por evento | CSIRT | RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | EA-02 | Tiempo a contención | MDE machineaction |
| EP-A02 | Live response / recolección de paquetes | Por evento | Tier 3 / CSIRT | RS.AN | SOP | eo:OP-SOP-28 Recolectar evidencia forense con autoridad y registro | L1 | — | Paquetes con registro | custom-permissions-details |
| EP-A03 | Onboarding/offboarding de dispositivos; grupos y tags | Por evento | Engineering & SecOps | ID.AM, PR.PS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L2 | EA-05 | No onboarded | MDE onboarding |
| EP-A04 | Bloquear aplicación vulnerable (TVM) o mitigación alternativa | Por evento | Security Administration + IT | PR.PS, ID.RA | POS | eo:OP-POS-17 Priorizar y seguir la remediación de vulnerabilidades por riesgo | L2 | EA-07 | Apps bloqueadas | defender-vulnerability-management |
| EP-A05 | Tabletop ransomware/dispositivo comprometido (incl. 'agente comprometido') | Según necesidad | SOC Oversight + CSIRT | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-D01 | Revisar acciones automáticas y manuales en el Action center | Security Operations Team | EA-03 | L2 |
| EP-D02 | Triar incidentes de la cola con alertas de MDE y resolver remediados | Security Operations Team | EA-01 | L2 |
| EP-D03 | Gestionar FP/FN: indicadores, exclusiones, envíos; causa (ASR, AV, EDR) | Security Operations Team | EA-04 | L2 |
| EP-D04 | Revisar Threat analytics de alto impacto y derivar acciones | Security Operations Team | EA-06 | L2 |
| EP-D05 | Revisar salud de dispositivos (AV signature/platform/engine, EDR sensor) | Security Administration Team | EA-05 | L3 |
| EP-D06 | Investigar incidentes de endpoint y ejecutar/aprobar acciones (aislar, restringir, scan, paquete) | Tier 2-3 + CSIRT | EA-02 | L2 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-W01 | Revisar Message Center (MDE/Intune) y evaluar impacto | General | EA-10 | L3 |
| EP-W02 | Revisar threat protection report y tendencias | Security Operations Team | EA-09 | L3 |
| EP-W03 | Revisar Defender Vulnerability Management: nuevas vulnerabilidades, recomendaciones, exposure score; solicitudes a Intune | Security Administration Team + IT | EA-07 | L2 |
| EP-W04 | Revisar ASR rules report y proponer paso de audit a block | Security Administration Team | EA-08 | L2 |
| EP-W05 | Revisar web protection / network protection y custom indicators | Security Administration Team | EA-09 | L3 |
| EP-W06 | Hunting proactivo sobre Device* y detecciones personalizadas | Tier 2-3 | EA-11 | L1 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-M01 | Revisar device groups, niveles de automatización y RBAC por grupo | Security Administration + SOC Oversight | EA-08 | L2 |
| EP-M02 | Revisar baselines de Intune y su deriva | Security Administration + IT | EA-08 | L2 |
| EP-M03 | Revisar device discovery: no gestionados y de red; plan de onboarding | Engineering & SecOps | EA-05 | L2 |
| EP-M04 | Informe mensual de seguridad de endpoints | SOC Oversight | EA-09 | L3 |
| EP-M05 | Revisar indicadores y exclusiones con vencimiento; retirar obsoletos | Security Administration | EA-04 | L2 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-Q01 | Revisar política de endpoints, excepciones y apetito de autonomía | PO-GAC Endpoints + CISO | — | L1 |
| EP-Q02 | Revisar desempeño y costo de la flota Endpoints | PO-GAC Endpoints | EA-13 | L1 |
| EP-Q03 | Recertificar accesos (Unified RBAC por device group; Agent ID) | PO-GAC + IAM | EA-13 | L2 |
| EP-Q04 | Evaluaciones/regresión y red teaming de agentes; prueba de reversión de aislamiento | PO-GAC + AppSec | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-A01 | Respuesta a incidente mayor: aislamiento masivo acotado, restricción, offboarding | CSIRT | EA-02 | L2 |
| EP-A02 | Live response / recolección de paquetes | Tier 3 / CSIRT | — | L1 |
| EP-A03 | Onboarding/offboarding de dispositivos; grupos y tags | Engineering & SecOps | EA-05 | L2 |
| EP-A04 | Bloquear aplicación vulnerable (TVM) o mitigación alternativa | Security Administration + IT | EA-07 | L2 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| EP-A05 | Tabletop ransomware/dispositivo comprometido (incl. 'agente comprometido') | SOC Oversight + CSIRT | — | L1 |

## 3. Prácticas agnósticas eo:OP (20)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | EP-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | EP-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | EP-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | EP-W04, EP-M01, EP-M02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | EP-M05 | Reutilizada (productividad/XDR) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | EP-D05 | Reutilizada (productividad/XDR) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | EP-M03, EP-A03 | Reutilizada (productividad/XDR) |
| eo:OP-POS-17 Priorizar y seguir la remediación de vulnerabilidades por riesgo | EP-W03, EP-A04 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | EP-W01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | EP-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | EP-M04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | EP-W06 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | EP-D02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | EP-D06, EP-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | EP-D03 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-19 Revisar tendencias de detección y ajustar políticas | EP-W02, EP-W05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-20 Revisar inteligencia de amenazas y derivar acciones | EP-D04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | EP-A05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-27 Supervisar la remediación automatizada | EP-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-28 Recolectar evidencia forense con autoridad y registro | EP-A02 | Reutilizada (productividad/XDR) |

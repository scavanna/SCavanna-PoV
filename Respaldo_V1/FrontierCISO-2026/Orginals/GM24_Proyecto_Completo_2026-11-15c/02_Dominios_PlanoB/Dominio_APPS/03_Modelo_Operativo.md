# 03 · Modelo operativo (26 tareas)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

Fuente: Microsoft Defender for Cloud Apps operational guide (daily/weekly/monthly/ad hoc) + app governance (manage, policies, hygiene, alerts) + cloud discovery policies + CA app control + anomaly detection policies + roles admin.

## 1. Tareas

| ID | Tarea | Cadencia | Persona | CSF 2.0 | SAF | eo:OP | Autonomía | Agente | KPI | Fuente |
|---|---|---|---|---|---|---|---|---|---|---|
| AP-D01 | Triar alertas de Defender for Cloud Apps (anomalías, actividad, app governance) en la cola unificada; clasificar y resolver | Diaria | SOC analysts | DE.AE, RS.MA | SOP | eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | L2 | PA-01 | % High triadas ≤4 h | ops-guide-daily |
| AP-D02 | Investigar alertas de OAuth apps (app governance: permisos inusuales, consentimiento masivo, app maliciosa) y ejecutar/aprobar deshabilitar app o revocar consentimiento | Diaria | SOC analysts + Security admins | RS.AN, RS.MI | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | PA-02 | MTTR; acciones revertidas <2 % | app-governance-manage-alerts |
| AP-D03 | Revisar apps OAuth nuevas con permisos altos (incl. agentes de IA conectados) y alertas de políticas predefinidas; asignar dueño o bloquear | Diaria | Security admins | ID.AM, PR.AA | POS | eo:OP-POS-28 Gobernar el consentimiento y los permisos de aplicaciones OAuth | L2 | PA-03 | Alto privilegio sin dueño = 0 | app-governance-investigate-predefined-policies |
| AP-D04 | Revisar alertas de cloud discovery (shadow IT: apps nuevas de alto riesgo/volumen, apps de IA generativa) y proponer sanción/bloqueo/monitoreo | Diaria | Security admins | ID.RA, ID.AM | POS | eo:OP-POS-29 Descubrir y decidir sobre aplicaciones no sancionadas | L2 | PA-04 | Apps de alto riesgo con decisión ≤7 días | policies-cloud-discovery; manage-generative-ai-apps |
| AP-D05 | Revisar bloqueos y alertas de access/session policies (CA app control) y falsos positivos de sesión | Diaria | SOC analysts + IAM | PR.AA, DE.AE | SOP | eo:OP-SOP-15 Analizar causa raíz de errores de detección | L2 | PA-05 | Bloqueos indebidos ↓ | conditional-access-app-control-how-to-overview |
| AP-D06 | Revisar salud de app connectors y del agente de descubrimiento (logs de firewall/proxy, Defender for Endpoint como fuente) | Diaria | Security admins | PR.PS, DE.CM | POS | eo:OP-POS-15 Mantener la salud de la ingesta de señales | L3 | PA-06 | Conectores saludables 100 % | enable-instant-visibility-protection-and-governance-actions |
| AP-W01 | Revisar Message Center y novedades de MDA/app governance; evaluar impacto (p. ej., retiro de file policies 6-ene-2027) | Semanal | Security admins | GV.OV, ID.IM | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L3 | PA-07 | Cambios evaluados ≤7 días | ops-guide-weekly |
| AP-W02 | Revisar governance log: estado de acciones de gobierno (deshabilitar app, suspender usuario, requerir re-login) y fallos | Semanal | Security admins | RS.MI, GV.OV | SOP | eo:OP-SOP-22 Mantener la automatización operativa | L2 | PA-08 | Acciones fallidas = 0 | ops-guide-weekly; governance-actions |
| AP-W03 | Revisar app hygiene: apps no usadas, credenciales no usadas o por expirar; proponer deshabilitación automática | Semanal | Security admins | PR.AA, ID.AM | AYI | eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | L2 | PA-03 | Inactivas >90 días deshabilitadas ≤30 días | app-governance-secure-apps-app-hygiene-features |
| AP-W04 | Hunting sobre CloudAppEvents/OAuthAppInfo: consentimientos anómalos, descargas masivas, uso de apps de IA, actividad de apps OAuth de las flotas | Semanal | SOC analysts (Tier 2-3) | DE.CM | SOP | eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | L1 | PA-09 | Hunts; hallazgos→políticas | app-activity-threat-hunting |
| AP-W05 | Revisar reporte de cloud discovery: tendencia de apps, categorías (incl. Generative AI), usuarios, volumen; actualizar etiquetas sancionada/no sancionada | Semanal | Security admins + dueños de negocio | ID.AM, ID.RA | POS | eo:OP-POS-29 Descubrir y decidir sobre aplicaciones no sancionadas | L2 | PA-04 | Apps sin etiqueta ↓ | discovered-apps |
| AP-W06 | Verificar que las apps OAuth de los agentes de todas las flotas (AG/XA/EA/IA/DA/SA/CA) tengan dueño, permisos mínimos y uso coherente | Semanal | Security admins + PO-GAC de dominios | PR.AA, GV.RR | AYI | eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | L2 | PA-03 | Apps de agentes sin dueño = 0 | app-governance-visibility-insights-view-apps |
| AP-M01 | Revisar policy assessments y alertas FP/benign TP; ajustar alcance de políticas de anomalías e IPs corporativas (impossible travel) | Mensual | Security admins | ID.IM | POS | eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | L2 | PA-05 | FP recurrentes ↓ | ops-guide-monthly |
| AP-M02 | Revisar políticas de OAuth (predefinidas/personalizadas), umbrales de permisos y usuarios, y apps aprobadas/prohibidas | Mensual | Security admins + SOC Oversight | GV.PO, PR.AA | POS | eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | L2 | PA-03 | Políticas vigentes; prohibidas sin justificación = 0 | app-permission-policy |
| AP-M03 | Revisar access/session policies de CA app control con IAM (cobertura de apps críticas, efecto, excepciones) | Mensual | IAM + Security admins | PR.AA, GV.PO | POS | eo:OP-POS-18 Evaluar el efecto de las políticas de acceso y ajustarlas | L2 | PA-05 | Apps críticas con sesión controlada ≥90 % | session-policy-aad; access-policy-aad |
| AP-M04 | Informe mensual de aplicaciones (shadow IT, OAuth, anomalías, sesiones, IA generativa) para CISO y dueños de negocio | Mensual | Security admins | GV.OV, RS.CO | SIG | eo:OP-SIG-13 Reportar resultados del SOC a la dirección | L3 | PA-10 | Informe a tiempo | Propuesta |
| AP-M05 | Revisar roles de administración de MDA (Cloud App Security admin, Compliance admin) y auditoría de actividad de admins | Mensual | SOC Oversight + IAM | PR.AA, GV.RR | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | PA-11 | Admins sin justificación = 0 | manage-admins |
| AP-Q01 | Revisar política de aplicaciones (criterios de sanción/bloqueo, apetito para apps de IA, consentimiento de usuarios) con negocio y CISO | Trimestral | PO-GAC Apps + CISO + dueños de negocio | GV.PO, GV.RM | SIG | eo:OP-SIG-12 Revisar políticas y excepciones del control | L1 | — | Decisiones registradas | Propuesta |
| AP-Q02 | Revisar desempeño y costo de la flota de agentes Apps | Trimestral | PO-GAC Apps | GV.OV, ID.IM | IA | eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | L1 | PA-11 | KPIs vs. meta | Propuesta |
| AP-Q03 | Recertificar permisos de apps OAuth críticas (humanas y de agentes) y roles de MDA | Trimestral | PO-GAC + IAM | PR.AA | AYI | eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | L2 | PA-11 | % recertificados | Propuesta |
| AP-Q04 | Evaluaciones/regresión y red teaming de agentes (consentimiento inducido, app maliciosa simulada) | Trimestral | PO-GAC + AppSec | ID.IM | IA | eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | L2 | — | % evaluados | Propuesta |
| AP-A01 | Respuesta a app OAuth maliciosa o consentimiento ilícito: deshabilitar app, revocar consentimientos, suspender usuarios, revisar actividad; coordinar con Identidades/XDR | Por evento | SOC + Security admins + IAM | RS.MI, RS.CO | SOP | eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | L2 | PA-02 | Tiempo a contención | app-governance-detect-remediate-overview |
| AP-A02 | Onboarding de una app SaaS crítica: app connector, CA app control (access/session), políticas de actividad | Por evento | Security admins + IAM | PR.AA, PR.PS | POS | eo:OP-POS-16 Mantener el inventario de fuentes de señal | L1 | PA-06 | Apps críticas onboarded | conditional-access-app-control-how-to-overview |
| AP-A03 | Decisión sobre una app descubierta (sancionar / bloquear vía MDE-indicators o proxy / monitorear) con el dueño de negocio | Por evento | Security admins + dueños de negocio | ID.RA, PR.PS | POS | eo:OP-POS-29 Descubrir y decidir sobre aplicaciones no sancionadas | L2 | PA-04 | Decisiones ≤14 días | governance-discovery |
| AP-A04 | Migración de file policies de MDA a Purview DLP / auto-labeling antes del 6-ene-2027 (coordinado con Dominio_DATOS) | Por evento | Security & Compliance admins + PO-GAC Datos | PR.DS, GV.OV | SIG | eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | L1 | — | Hito cumplido | policies-information-protection |
| AP-A05 | Tabletop de consentimiento ilícito / app OAuth comprometida (incl. 'app de un agente de IA con permisos excesivos') | Según necesidad | PO-GAC Apps + CSIRT + IAM | ID.IM, RS | SOP | eo:OP-SOP-26 Probar los planes de respuesta | L1 | — | Ejercicios/año | AMP-43 |

## 2. Vista por cadencia

### Diaria

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-D01 | Triar alertas de Defender for Cloud Apps (anomalías, actividad, app governance) en la cola unificada; clasificar y resolver | SOC analysts | PA-01 | L2 |
| AP-D02 | Investigar alertas de OAuth apps (app governance: permisos inusuales, consentimiento masivo, app maliciosa) y ejecutar/aprobar deshabilitar app o revocar consentimiento | SOC analysts + Security admins | PA-02 | L2 |
| AP-D03 | Revisar apps OAuth nuevas con permisos altos (incl. agentes de IA conectados) y alertas de políticas predefinidas; asignar dueño o bloquear | Security admins | PA-03 | L2 |
| AP-D04 | Revisar alertas de cloud discovery (shadow IT: apps nuevas de alto riesgo/volumen, apps de IA generativa) y proponer sanción/bloqueo/monitoreo | Security admins | PA-04 | L2 |
| AP-D05 | Revisar bloqueos y alertas de access/session policies (CA app control) y falsos positivos de sesión | SOC analysts + IAM | PA-05 | L2 |
| AP-D06 | Revisar salud de app connectors y del agente de descubrimiento (logs de firewall/proxy, Defender for Endpoint como fuente) | Security admins | PA-06 | L3 |

### Semanal

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-W01 | Revisar Message Center y novedades de MDA/app governance; evaluar impacto (p. ej., retiro de file policies 6-ene-2027) | Security admins | PA-07 | L3 |
| AP-W02 | Revisar governance log: estado de acciones de gobierno (deshabilitar app, suspender usuario, requerir re-login) y fallos | Security admins | PA-08 | L2 |
| AP-W03 | Revisar app hygiene: apps no usadas, credenciales no usadas o por expirar; proponer deshabilitación automática | Security admins | PA-03 | L2 |
| AP-W04 | Hunting sobre CloudAppEvents/OAuthAppInfo: consentimientos anómalos, descargas masivas, uso de apps de IA, actividad de apps OAuth de las flotas | SOC analysts (Tier 2-3) | PA-09 | L1 |
| AP-W05 | Revisar reporte de cloud discovery: tendencia de apps, categorías (incl. Generative AI), usuarios, volumen; actualizar etiquetas sancionada/no sancionada | Security admins + dueños de negocio | PA-04 | L2 |
| AP-W06 | Verificar que las apps OAuth de los agentes de todas las flotas (AG/XA/EA/IA/DA/SA/CA) tengan dueño, permisos mínimos y uso coherente | Security admins + PO-GAC de dominios | PA-03 | L2 |

### Mensual

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-M01 | Revisar policy assessments y alertas FP/benign TP; ajustar alcance de políticas de anomalías e IPs corporativas (impossible travel) | Security admins | PA-05 | L2 |
| AP-M02 | Revisar políticas de OAuth (predefinidas/personalizadas), umbrales de permisos y usuarios, y apps aprobadas/prohibidas | Security admins + SOC Oversight | PA-03 | L2 |
| AP-M03 | Revisar access/session policies de CA app control con IAM (cobertura de apps críticas, efecto, excepciones) | IAM + Security admins | PA-05 | L2 |
| AP-M04 | Informe mensual de aplicaciones (shadow IT, OAuth, anomalías, sesiones, IA generativa) para CISO y dueños de negocio | Security admins | PA-10 | L3 |
| AP-M05 | Revisar roles de administración de MDA (Cloud App Security admin, Compliance admin) y auditoría de actividad de admins | SOC Oversight + IAM | PA-11 | L2 |

### Trimestral

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-Q01 | Revisar política de aplicaciones (criterios de sanción/bloqueo, apetito para apps de IA, consentimiento de usuarios) con negocio y CISO | PO-GAC Apps + CISO + dueños de negocio | — | L1 |
| AP-Q02 | Revisar desempeño y costo de la flota de agentes Apps | PO-GAC Apps | PA-11 | L1 |
| AP-Q03 | Recertificar permisos de apps OAuth críticas (humanas y de agentes) y roles de MDA | PO-GAC + IAM | PA-11 | L2 |
| AP-Q04 | Evaluaciones/regresión y red teaming de agentes (consentimiento inducido, app maliciosa simulada) | PO-GAC + AppSec | — | L2 |

### Por evento

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-A01 | Respuesta a app OAuth maliciosa o consentimiento ilícito: deshabilitar app, revocar consentimientos, suspender usuarios, revisar actividad; coordinar con Identidades/XDR | SOC + Security admins + IAM | PA-02 | L2 |
| AP-A02 | Onboarding de una app SaaS crítica: app connector, CA app control (access/session), políticas de actividad | Security admins + IAM | PA-06 | L1 |
| AP-A03 | Decisión sobre una app descubierta (sancionar / bloquear vía MDE-indicators o proxy / monitorear) con el dueño de negocio | Security admins + dueños de negocio | PA-04 | L2 |
| AP-A04 | Migración de file policies de MDA a Purview DLP / auto-labeling antes del 6-ene-2027 (coordinado con Dominio_DATOS) | Security & Compliance admins + PO-GAC Datos | — | L1 |

### Según necesidad

| ID | Tarea | Humano | Agente | Autonomía |
|---|---|---|---|---|
| AP-A05 | Tabletop de consentimiento ilícito / app OAuth comprometida (incl. 'app de un agente de IA con permisos excesivos') | PO-GAC Apps + CSIRT + IAM | — | L1 |

## 3. Prácticas agnósticas eo:OP (20)

| Práctica | Tareas | Origen |
|---|---|---|
| eo:OP-AYI-01 Recertificar accesos privilegiados, no humanos y de agentes | AP-M05, AP-Q03 | Reutilizada (productividad/XDR) |
| eo:OP-AYI-02 Vigilar el riesgo de identidades no humanas | AP-W03, AP-W06 | Nueva (propuesta MAEO) |
| eo:OP-IA-02 Revisar desempeño, costo y riesgo de los agentes | AP-Q02 | Reutilizada (productividad/XDR) |
| eo:OP-IA-03 Evaluar y probar adversarialmente a los agentes | AP-Q04 | Reutilizada (productividad/XDR) |
| eo:OP-POS-12 Detectar y corregir deriva de configuración frente al baseline | AP-M02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-13 Revisar y depurar excepciones que debilitan la detección | AP-M01 | Reutilizada (productividad/XDR) |
| eo:OP-POS-15 Mantener la salud de la ingesta de señales | AP-D06 | Reutilizada (productividad/XDR) |
| eo:OP-POS-16 Mantener el inventario de fuentes de señal | AP-A02 | Reutilizada (productividad/XDR) |
| eo:OP-POS-18 Evaluar el efecto de las políticas de acceso y ajustarlas | AP-M03 | Nueva (propuesta MAEO) |
| eo:OP-POS-28 Gobernar el consentimiento y los permisos de aplicaciones OAuth | AP-D03 | Nueva (propuesta MAEO) |
| eo:OP-POS-29 Descubrir y decidir sobre aplicaciones no sancionadas | AP-D04, AP-W05, AP-A03 | Nueva (propuesta MAEO) |
| eo:OP-SIG-10 Vigilar cambios de la plataforma y evaluar impacto | AP-W01, AP-A04 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-12 Revisar políticas y excepciones del control | AP-Q01 | Reutilizada (productividad/XDR) |
| eo:OP-SIG-13 Reportar resultados del SOC a la dirección | AP-M04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-02 Buscar amenazas por técnicas priorizadas y convertir hallazgos en detecciones | AP-W04 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-10 Triar incidentes por prioridad dentro del SLA | AP-D01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-11 Investigar y remediar incidentes con evidencia | AP-D02, AP-A01 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-15 Analizar causa raíz de errores de detección | AP-D05 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-22 Mantener la automatización operativa | AP-W02 | Reutilizada (productividad/XDR) |
| eo:OP-SOP-26 Probar los planes de respuesta | AP-A05 | Reutilizada (productividad/XDR) |

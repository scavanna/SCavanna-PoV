# 04 · Catálogo de agentes (11)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de aplicaciones SaaS y OAuth (Microsoft Defender for Cloud Apps + app governance + Conditional Access app control)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| PA-01 | Triage Copilot de alertas de apps | AP-D01 | L2 | R1 (alt. R2) |
| PA-02 | Asistente de investigación y remediación de OAuth | AP-D02, AP-A01 | L2 | R1 (alt. R2) |
| PA-03 | Steward de OAuth apps y permisos (incl. agentes de IA) | AP-D03, AP-W03, AP-W06, AP-M02 | L2 | R2 |
| PA-04 | Analista de shadow IT y apps de IA generativa | AP-D04, AP-W05, AP-A03 | L2 | R2 |
| PA-05 | Analista de sesiones y anomalías | AP-D05, AP-M01, AP-M03 | L1-L2 | R2 |
| PA-06 | Centinela de conectores y cobertura | AP-D06, AP-A02 | L3 (detección) / L2 (tickets) | R2 |
| PA-07 | Vigía de cambios de plataforma (MDA / app governance) | AP-W01 | L3 | R2 |
| PA-08 | Supervisor del governance log | AP-W02 | L2 | R2 |
| PA-09 | Bibliotecario de hunting de apps | AP-W04 | L2 | R3 (alt. R2) |
| PA-10 | Reportero de aplicaciones | AP-M04 | L3 | R2 |
| PA-11 | Analista de la flota Apps y recertificación | AP-M05, AP-Q02, AP-Q03 | L1-L2 | R2 |

## 2. Tools de la flota (28; nuevos del dominio: 10)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| AT-01 | Microsoft Graph / portal | App governance · OAuth apps (inventario, permisos, consentimiento, uso, agentes de IA conectados) | Leer apps OAuth registradas en Entra (y Google/Salesforce conectados), permisos, publisher, usuarios con consentimiento, agentes de IA asociados | Security Reader / Cloud App Security administrator (lectura) | GA (incluido en licencia MDA) | Compartido | PA-02, PA-03, PA-10, PA-11 | learn.microsoft.com/defender-cloud-apps/app-governance-visibility-insights-view-apps |
| AT-02 | Portal / API | App governance · políticas de OAuth (predefinidas y personalizadas) y acciones (deshabilitar app, revocar consentimiento) | Leer alertas de políticas; proponer deshabilitar/revocar; ejecutar tras aprobación | Cloud App Security administrator (acciones); agente: lectura + propuesta | GA | Compartido | PA-02, PA-03, PA-08 | learn.microsoft.com/defender-cloud-apps/app-governance-app-policies-create |
| AT-03 | Portal / API | App governance · hygiene (apps no usadas, credenciales no usadas/expirando, auto-deshabilitar) | Detectar apps y credenciales inactivas; proponer deshabilitación | Cloud App Security administrator; agente: lectura | GA | Propio | PA-03 | learn.microsoft.com/defender-cloud-apps/app-governance-secure-apps-app-hygiene-features |
| AT-04 | Defender for Cloud Apps API | Cloud discovery · reportes, apps descubiertas, riesgo (cloud app catalog, categoría Generative AI), etiquetas sancionada/no sancionada | Leer apps descubiertas, usuarios, volumen, puntuación de riesgo; proponer sancionar/bloquear | Cloud App Security administrator; agente: lectura; etiquetado con aprobación | GA | Compartido | PA-04, PA-06, PA-10 | learn.microsoft.com/defender-cloud-apps/policies-cloud-discovery |
| AT-05 | Microsoft Graph | Conditional Access · políticas con control de sesión (CA app control) y access policies de MDA | Leer políticas de acceso/sesión y su efecto; proponer ajustes (report-only) | Policy.Read.All; cambios solo humano (CA Administrator) | GA | Propio | PA-05 | learn.microsoft.com/defender-cloud-apps/conditional-access-app-control-how-to-overview |
| AT-06 | Advanced Hunting (KQL) | Tablas CloudAppEvents, OAuthAppInfo, IdentityLogonEvents (actividad de apps y consentimientos) | Hunting sobre actividad de apps, consentimientos, descargas masivas, uso de apps de IA | ThreatHunting.Read.All | GA | Compartido | PA-01, PA-02, PA-04, PA-09 | learn.microsoft.com/defender-cloud-apps/app-activity-threat-hunting |
| AT-07 | Portal / API | Anomaly detection policies (modelo dinámico) y activity policies | Leer alertas de anomalías (impossible travel, descargas masivas, ransomware activity); tuning de alcance y IPs corporativas | Cloud App Security administrator; agente: lectura + propuestas | GA (modelo dinámico desde jun-2025) | Compartido | PA-01, PA-05, PA-10 | learn.microsoft.com/defender-cloud-apps/anomaly-detection-policy |
| AT-08 | Portal | Governance log y acciones de gobierno sobre apps/actividades (suspender usuario, requerir re-inicio de sesión) | Verificar estado de acciones de gobierno; proponer acciones de usuario tras aprobación | Cloud App Security administrator; agente: lectura | GA | Compartido | PA-02, PA-08 | learn.microsoft.com/defender-cloud-apps/governance-actions |
| AT-09 | Conector / app connectors | App connectors (M365, Google Workspace, Salesforce, ServiceNow, GitHub, etc.) · estado y salud | Verificar conectores conectados y su salud; proponer nuevas conexiones | Cloud App Security administrator; agente: lectura | GA | Propio | PA-06 | learn.microsoft.com/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions |
| AT-10 | Portal / exportación | Policy assessments y recomendaciones de MDA (impacto de políticas, FP/benign TP) | Revisar evaluación de políticas y alertas FP | Cloud App Security administrator (lectura) | verificar (API) | Propio | PA-05 | learn.microsoft.com/defender-cloud-apps/ops-guide/ops-guide-monthly |
| IT-07 | REST API (OpenAPI) | Microsoft Graph · auditLogs/signIns y directoryAudits | Sign-in logs y auditoría de directorio | AuditLog.Read.All | GA | Propio | PA-05 | learn.microsoft.com/graph/api/resources/signin |
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Propio | PA-01 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-02 | MCP | Microsoft MCP Server for Enterprise (Graph) | Consultas de solo lectura sobre el tenant (usuarios, grupos, roles, dispositivos) | Custom connector; app registration con permisos MCP.*; solo lectura | GA (solo lectura) | Propio | PA-03 | learn.microsoft.com/graph/mcp-server/use-enterprise-mcp-server-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Propio | PA-07 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Compartido | PA-01, PA-02 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Propio | PA-09 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | PA-07 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | PA-11 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Propio | PA-11 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | PA-06 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | PA-04 | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | PA-09, PA-10 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Propio | PA-11 | microsoft.com/microsoft-agent-365 |
| XT-08 | REST API (OpenAPI) | Defender XDR · custom detection rules API / automation rules | Crear/actualizar detecciones personalizadas y reglas de automatización | Custom detections (Manage); Automation rules (Manage) | GA (detectionRules); automation rules a verificar | Propio | PA-09 | learn.microsoft.com/graph/api/resources/security-detectionrule |

## 3. Knowledge nuevos (6)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| AK-01 | Criterios de triaje de alertas de apps (anomalía, OAuth, sesión, discovery) por severidad, app, usuario y criticidad | Dataverse | PA-01, PA-04 | Interno (derivado de ops guide MDA) |
| AK-02 | Playbooks de app OAuth maliciosa / consentimiento ilícito con ejecutores humano/agente y coordinación IAM | SharePoint | PA-02, PA-08 | Interno (M5.1-PA01 instancia Apps) |
| AK-03 | Inventario de apps OAuth: dueño, privilegio, uso, publisher, agentes de IA conectados; lista de apps aprobadas/prohibidas | Dataverse | PA-03 | Interno (M2.1-PA01 instancia Apps; AMP-33) |
| AK-04 | Criterios de sanción/bloqueo de apps (riesgo, categoría, datos, cumplimiento) y apetito para apps de IA generativa | SharePoint | PA-04, PA-10 | Interno (G2.2-PA03 instancia Apps) |
| AK-05 | Baseline de access/session policies por app crítica; IPs corporativas; excepciones de anomalías con vencimiento | SharePoint / Git | PA-05 | Interno |
| AK-06 | Inventario de app connectors y fuentes de descubrimiento con umbrales de salud | Dataverse | PA-06 | Interno |

## 4. Skills nuevos (5)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| AS-01 | Triaje de alertas de apps por consentimiento y sesión | Distinguir anomalía de usuario, abuso de app OAuth y bloqueo de sesión legítimo; correlar con identidad; no cerrar por una sola señal. | PA-01 |
| AS-02 | Remediación proporcional de apps OAuth | Revocar consentimiento antes que deshabilitar la app; nunca tocar apps first-party ni de las flotas sin segunda aprobación; registrar. | PA-02 |
| AS-03 | Gobierno de consentimiento y permisos | Leer permisos delegados/aplicación, publisher verificado, uso real; detectar alto privilegio sin dueño; proponer mínimo privilegio. | PA-03 |
| AS-04 | Análisis de shadow IT y apps de IA | Ponderar riesgo del catálogo, volumen, usuarios y datos; preparar la decisión sancionar/bloquear/monitorear para negocio. | PA-04 |
| AS-05 | Tuning de anomalías y sesiones | Detectar FP por IPs corporativas y viajes legítimos; proponer alcance mínimo; solo proponer cambios de CA. | PA-05 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | PA-01 | PA-02 | PA-03 | PA-04 | PA-05 | PA-06 | PA-07 | PA-08 | PA-09 | PA-10 | PA-11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AT-01 |  | ● | ● |  |  |  |  |  |  | ● | ● |
| AT-02 |  | ● | ● |  |  |  |  | ● |  |  |  |
| AT-03 |  |  | ● |  |  |  |  |  |  |  |  |
| AT-04 |  |  |  | ● |  | ● |  |  |  | ● |  |
| AT-05 |  |  |  |  | ● |  |  |  |  |  |  |
| AT-06 | ● | ● |  | ● |  |  |  |  | ● |  |  |
| AT-07 | ● |  |  |  | ● |  |  |  |  | ● |  |
| AT-08 |  | ● |  |  |  |  |  | ● |  |  |  |
| AT-09 |  |  |  |  |  | ● |  |  |  |  |  |
| AT-10 |  |  |  |  | ● |  |  |  |  |  |  |
| IT-07 |  |  |  |  | ● |  |  |  |  |  |  |
| T-01 | ● |  |  |  |  |  |  |  |  |  |  |
| T-02 |  |  | ● |  |  |  |  |  |  |  |  |
| T-03 |  |  |  |  |  |  | ● |  |  |  |  |
| T-04 | ● | ● |  |  |  |  |  |  |  |  |  |
| T-05 |  |  |  |  |  |  |  |  | ● |  |  |
| T-09 |  |  |  |  |  |  | ● |  |  |  |  |
| T-13 |  |  |  |  |  |  |  |  |  |  | ● |
| T-14 |  |  |  |  |  |  |  |  |  |  | ● |
| T-15 |  |  |  |  |  | ● |  |  |  |  |  |
| T-16 | ◎ | ◎ | ◎ | ● | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 |  |  |  |  |  |  |  |  | ● | ● |  |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  |  |  |  |  | ● |
| XT-08 |  |  |  |  |  |  |  |  | ● |  |  |

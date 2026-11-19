# 04 · Catálogo de agentes (13)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección, detección y respuesta en endpoints (Microsoft Defender for Endpoint + Defender Vulnerability Management + Intune)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| EA-01 | Triage Copilot de incidentes de endpoint | EP-D02 | L2 | R1 (alt. R2) |
| EA-02 | Asistente de investigación y respuesta en dispositivos | EP-D06, EP-A01 | L2 | R1 (alt. R2) |
| EA-03 | Supervisor del Action center (endpoints) | EP-D01 | L2 | R2 |
| EA-04 | Analista de FP/FN, indicadores y exclusiones | EP-D03, EP-M05 | L2 | R2 |
| EA-05 | Centinela de salud y cobertura de dispositivos | EP-D05, EP-M03, EP-A03 | L3 (detección) / L2 (tickets) | R2 |
| EA-06 | Briefer de Threat analytics de endpoints | EP-D04 | L2 | R1 (alt. R2) |
| EA-07 | Analista de vulnerabilidades y remediación | EP-W03, EP-A04 | L2 | R2 |
| EA-08 | Auditor de ASR, baselines y grupos | EP-W04, EP-M01, EP-M02 | L2 | R2 |
| EA-09 | Reportero de protección y resumen mensual | EP-W02, EP-W05, EP-M04 | L3 | R2 |
| EA-10 | Vigía de cambios de plataforma (MDE/Intune) | EP-W01 | L3 | R2 |
| EA-11 | Bibliotecario de hunting de endpoints | EP-W06 | L2 | R3 (alt. R2) |
| EA-12 | Redactor de lecciones de endpoints | EP-A05 | L1 | R2 |
| EA-13 | Analista de la flota Endpoints | EP-Q02, EP-Q03 | L1-L2 | R2 |

## 2. Tools de la flota (30; nuevos del dominio: 8)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| ET-01 | REST API (OpenAPI) | Defender Vulnerability Management · recommendations / vulnerabilities / software inventory / exposure score | Recomendaciones priorizadas, CVEs, inventario de software, exposure score | Vulnerability.Read.All, Software.Read.All, Score.Read.All | GA | Propio | EA-07 | learn.microsoft.com/defender-endpoint/api/get-all-recommendations |
| ET-02 | REST API / Intune | Remediation request (TVM → Intune) y remediation activities | Crear y seguir solicitudes de remediación hacia IT | RemediationTasks.Read.All; permisos de Intune para crear | GA | Propio | EA-07 | learn.microsoft.com/defender-vulnerability-management/tvm-remediation |
| ET-03 | REST API (OpenAPI) | MDE · indicators (file, IP, URL, certificate) | Indicadores de bloqueo/permiso con vencimiento | Ti.ReadWrite | GA | Propio | EA-04 | learn.microsoft.com/defender-endpoint/api/ti-indicator |
| ET-04 | Advanced Hunting (KQL) | Tablas DeviceEvents (ASR), DeviceTvmSoftwareVulnerabilities, DeviceNetworkEvents, DeviceLogonEvents | Hunting y análisis de ASR, vulnerabilidades y comportamiento de dispositivos | ThreatHunting.Read.All | GA | Compartido | EA-01, EA-02, EA-04, EA-07, EA-08, EA-09, EA-11 | learn.microsoft.com/defender-xdr/advanced-hunting-schema-tables |
| ET-05 | Intune Graph API | Intune · device compliance, configuration profiles, security baselines, ASR policies | Leer cumplimiento y perfiles; proponer cambios | DeviceManagementConfiguration.Read.All; escritura con aprobación | GA | Propio | EA-08 | learn.microsoft.com/graph/api/resources/intune-graph-overview |
| ET-06 | REST API (OpenAPI) | MDE · device discovery (unmanaged, network devices) | Detectar dispositivos no gestionados y de red | Machine.Read.All | GA | Propio | EA-05 | learn.microsoft.com/defender-endpoint/device-discovery |
| ET-07 | REST API (OpenAPI) | MDE · machine actions (isolate, restrict app execution, run AV scan, offboard) | Acciones de respuesta sobre dispositivos | Machine.Isolate, Machine.RestrictExecution, Machine.Scan, Machine.Offboard | GA | Propio | EA-02 | learn.microsoft.com/defender-endpoint/api/machineaction |
| ET-08 | Conector / Hunting | Informes MDE: device health, ASR rules report, web protection, threat protection | Compilar informes de salud y protección | Security data basics | verificar (exportación vía API) | Compartido | EA-05, EA-09 | learn.microsoft.com/defender-endpoint/device-health-reports |
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Compartido | EA-01, EA-02, EA-06 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Compartido | EA-06, EA-10 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Compartido | EA-01, EA-02, EA-03, EA-06, EA-12 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Propio | EA-11 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-06 | REST API (OpenAPI) | Microsoft Graph · security/threatSubmission | Crear envíos de FP/FN a Microsoft y consultar estado | ThreatSubmission.ReadWrite.All | GA | Propio | EA-04 | learn.microsoft.com/graph/api/resources/security-threatsubmissionroot |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | EA-10 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | EA-13 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Propio | EA-13 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | EA-05 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | EA-12 | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | EA-09, EA-11, EA-13 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Propio | EA-13 | microsoft.com/microsoft-agent-365 |
| XT-03 | REST API (OpenAPI) | Defender XDR · Action center / pending actions | Leer acciones pendientes y ejecutadas; preparar aprobación | Security data basics; Response (Read) | verificar (cobertura API del Action center unificado) | Propio | EA-03 | learn.microsoft.com/defender-xdr/m365d-autoir-actions |
| XT-05 | REST API (OpenAPI) | Defender for Endpoint API · machines (healthStatus, onboardingStatus) | Detectar dispositivos no saludables / no onboarded | Machine.Read.All | GA | Propio | EA-05 | learn.microsoft.com/defender-endpoint/api/get-machines |
| XT-07 | Advanced Hunting (KQL) | Threat analytics vía ExposureGraph / tablas de TA | Exposición a amenazas activas | ThreatHunting.Read.All | verificar (tablas por licencia) | Propio | EA-06 | learn.microsoft.com/defender-xdr/advanced-hunting-schema-tables |
| XT-08 | REST API (OpenAPI) | Defender XDR · custom detection rules API / automation rules | Crear/actualizar detecciones personalizadas y reglas de automatización | Custom detections (Manage); Automation rules (Manage) | GA (detectionRules); automation rules a verificar | Propio | EA-11 | learn.microsoft.com/graph/api/resources/security-detectionrule |
| XT-11 | REST API (OpenAPI) | Defender for Endpoint API · machine groups / automation level | Leer niveles de automatización AIR por grupo | Machine.Read.All | verificar | Propio | EA-08 | learn.microsoft.com/defender-xdr/m365d-configure-auto-investigation-response |
| XT-12 | Microsoft Graph | Unified RBAC · roleManagement/defender (roleDefinitions, roleAssignments) | Leer roles y asignaciones de Unified RBAC (humanos y agentes) | RoleManagement.Read.Defender | GA | Propio | EA-08 | learn.microsoft.com/graph/api/resources/unifiedrbacapplication |

## 3. Knowledge nuevos (7)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| DK-E1 | Criterios de triaje de endpoint por grupo y criticidad | Dataverse | EA-01 | Interno |
| DK-E2 | Playbooks de respuesta en dispositivos con límites por grupo | SharePoint | EA-02 | Interno (M5.1-PA01 instancia Endpoints) |
| DK-E3 | Baseline de automatización por device group y acciones con aprobación | SharePoint | EA-03 | Interno |
| DK-E4 | Registro de indicadores y exclusiones (ASR, AV) con vencimiento | Dataverse | EA-04 | Interno |
| DK-E5 | Inventario de dispositivos, grupos, tags, umbrales de salud y plan de onboarding | Dataverse | EA-05 | Interno (M2.1-PA01 instancia Endpoints) |
| DK-E6 | Criterios de priorización de remediación y SLAs con IT | SharePoint | EA-07 | Interno |
| DK-E7 | Baseline de ASR, Intune security baselines y device groups/RBAC | SharePoint / Git | EA-08, EA-10 | Interno (G2.2-PA03 instancia Endpoints) |

## 4. Skills nuevos (3)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| DS-E1 | Triaje por grupo y criticidad de dispositivo | Ponderar severidad por grupo y criticidad del activo; reconocer attack disruption. | EA-01 |
| DS-E2 | Respuesta proporcional en dispositivos | Scan → restringir → aislar; nunca offboard; límite por grupo; verificar reversión. | EA-02 |
| DS-E3 | Priorización de vulnerabilidades por riesgo | Explotación activa, exposición, activos críticos; remediación o mitigación alternativa. | EA-07 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | EA-01 | EA-02 | EA-03 | EA-04 | EA-05 | EA-06 | EA-07 | EA-08 | EA-09 | EA-10 | EA-11 | EA-12 | EA-13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ET-01 |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| ET-02 |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| ET-03 |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| ET-04 | ● | ● |  | ● |  |  | ● | ● | ● |  | ● |  |  |
| ET-05 |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| ET-06 |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| ET-07 |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| ET-08 |  |  |  |  | ● |  |  |  | ● |  |  |  |  |
| T-01 | ● | ● |  |  |  | ● |  |  |  |  |  |  |  |
| T-03 |  |  |  |  |  | ● |  |  |  | ● |  |  |  |
| T-04 | ● | ● | ● |  |  | ● |  |  |  |  |  | ● |  |
| T-05 |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| T-06 |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| T-09 |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| T-13 |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| T-14 |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| T-15 |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ● | ◎ |
| T-19 |  |  |  |  |  |  |  |  | ● |  | ● |  | ● |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| XT-03 |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| XT-05 |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| XT-07 |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| XT-08 |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| XT-11 |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| XT-12 |  |  |  |  |  |  |  | ● |  |  |  |  |  |

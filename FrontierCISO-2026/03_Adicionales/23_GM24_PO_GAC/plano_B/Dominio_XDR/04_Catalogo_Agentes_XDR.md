# 04 · Catálogo de agentes XDR (15)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Detección y respuesta unificada (Microsoft Defender XDR)** · 2026-11-14 · Dominio_XDR v1.0. Nivel de abstracción: *ProductPractice* / escenario (plano B). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta | Equivalente productividad |
|---|---|---|---|---|---|
| XA-01 | Triage Copilot de incidentes unificados | XDR-D01, XDR-D04, XDR-A03 | L2 | R1 (alt. R2) | AG-01 |
| XA-02 | Asistente de investigación y respuesta cross-domain | XDR-D02, XDR-A01 | L2 | R1 (alt. R2) | AG-02 |
| XA-03 | Supervisor del Action center (AIR) | XDR-D03 | L2 | R2 | — |
| XA-04 | Analista de tuning y FP/FN multi-sensor | XDR-D05, XDR-M03 | L2 | R2 | AG-03/AG-11 |
| XA-05 | Centinela de salud de sensores | XDR-D06, XDR-A04 | L3 (detección) / L2 (tickets) | R2 | — |
| XA-06 | Briefer de Threat analytics cross-domain | XDR-D07 | L2 | R1 (alt. R2) | AG-06 |
| XA-07 | Bibliotecario de hunting y detecciones cross-domain | XDR-W01, XDR-W02 | L2 | R3 (alt. R2) | AG-14 |
| XA-08 | Reportero de postura y exposición | XDR-W03 | L3 | R2 | AG-08 |
| XA-09 | Reportero de amenazas y resumen mensual | XDR-W04, XDR-M04 | L3 | R2 | AG-05 |
| XA-10 | Vigía de cambios de plataforma XDR | XDR-W05 | L3 | R2 | AG-09 |
| XA-11 | Auditor de automatización y RBAC | XDR-M01, XDR-M02 | L2 | R2 | AG-10 |
| XA-12 | Redactor de lecciones y ejercicios | XDR-M05, XDR-A05 | L1 | R2 | AG-12 |
| XA-13 | Analista de la flota XDR | XDR-Q02, XDR-Q03 | L1-L2 | R2 | AG-13 |
| XA-14 | Correlador de incidentes y casos | XDR-A03, XDR-D01 | L2 | R2 | — |
| XA-15 | Sincronizador ITSM y notificaciones | XDR-D08 | L3 | R2 | AG-15 |

**Orden de construcción sugerido:** XA-05, XA-08/XA-09, XA-10, XA-03, XA-04, XA-01, XA-07, XA-14, XA-06, XA-11, XA-12, XA-13, XA-15, **XA-02 último**.

## 2. Tools de la flota XDR (30)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Compartido | XA-01, XA-02, XA-06, XA-07 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Compartido | XA-06, XA-10 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Compartido | XA-01, XA-02, XA-03, XA-04, XA-06, XA-12, XA-14, XA-15 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Compartido | XA-01, XA-02, XA-04, XA-07, XA-14 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-08 | REST API (OpenAPI) | Microsoft Graph · security/secureScores | Leer Secure Score y recomendaciones | SecurityEvents.Read.All | GA | Propio | XA-08 | learn.microsoft.com/graph/api/resources/securescore |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | XA-10 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | XA-13 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Compartido | XA-11, XA-13 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Compartido | XA-05, XA-15 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | XA-12 | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | XA-07, XA-09, XA-13 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-21 | Conector prebuilt | Defender for Cloud Apps / Defender ATP (conectores) | Correlación con alertas de apps y endpoints | Lectura de alertas | GA (conectores soportados) | Compartido | XA-01, XA-02 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-22 | REST API (OpenAPI) | Microsoft Graph · reports (informes de protección) | Informes de estado de protección y flujo de correo | Reports.Read.All | verificar (cobertura de informes MDO vía API) | Propio | XA-09 | learn.microsoft.com/graph/api/resources/report |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Propio | XA-13 | microsoft.com/microsoft-agent-365 |
| XT-01 | REST API (OpenAPI) | Defender for Endpoint API · machine actions (isolate, scan, collect investigation package, restrict app execution) | Acciones de respuesta sobre dispositivos | Machine.Isolate, Machine.Scan, Machine.CollectForensics; Response (Manage) | GA | Propio | XA-02 | learn.microsoft.com/defender-endpoint/api/machineaction |
| XT-02 | REST API (OpenAPI) | Microsoft Graph · identity (revokeSignInSessions, riskyUsers confirmCompromised) y users (accountEnabled) | Revocar sesiones, marcar comprometido, deshabilitar usuario | User.RevokeSessions.All, IdentityRiskyUser.ReadWrite.All, User.EnableDisableAccount.All | GA | Propio | XA-02 | learn.microsoft.com/graph/api/user-revokesigninsessions |
| XT-03 | REST API (OpenAPI) | Defender XDR · Action center / pending actions | Leer acciones pendientes y ejecutadas; preparar aprobación | Security data basics; Response (Read) | verificar (cobertura API del Action center unificado) | Propio | XA-03 | learn.microsoft.com/defender-xdr/m365d-autoir-actions |
| XT-04 | REST API (OpenAPI) | Defender XDR · alert tuning rules / MDE indicators | Proponer y crear reglas de tuning y supresión con vencimiento | Alerts (Manage) | GA (indicadores); tuning vía API a verificar | Propio | XA-04 | learn.microsoft.com/defender-xdr/investigate-alerts#tune-an-alert |
| XT-05 | REST API (OpenAPI) | Defender for Endpoint API · machines (healthStatus, onboardingStatus) | Detectar dispositivos no saludables / no onboarded | Machine.Read.All | GA | Propio | XA-05 | learn.microsoft.com/defender-endpoint/api/get-machines |
| XT-06 | REST API (OpenAPI) | Defender for Identity · health issues (Graph security/identities/healthIssues) | Problemas de salud de sensores MDI | SecurityIdentitiesHealth.Read.All | GA | Propio | XA-05 | learn.microsoft.com/graph/api/resources/security-healthissue |
| XT-07 | Advanced Hunting (KQL) | Threat analytics vía ExposureGraph / tablas de TA | Exposición a amenazas activas | ThreatHunting.Read.All | verificar (tablas por licencia) | Propio | XA-06 | learn.microsoft.com/defender-xdr/advanced-hunting-schema-tables |
| XT-08 | REST API (OpenAPI) | Defender XDR · custom detection rules API / automation rules | Crear/actualizar detecciones personalizadas y reglas de automatización | Custom detections (Manage); Automation rules (Manage) | GA (detectionRules); automation rules a verificar | Propio | XA-07 | learn.microsoft.com/graph/api/resources/security-detectionrule |
| XT-09 | REST API / Hunting | Exposure Management (ExposureGraphNodes/Edges; iniciativas) | Postura y activos críticos | SecurityEvents.Read.All; ThreatHunting.Read.All | GA (hunting); API de iniciativas a verificar | Propio | XA-08 | learn.microsoft.com/security-exposure-management |
| XT-10 | Conector / Hunting | Informes MDE (threat protection, ASR, web protection) y monthly security summary | Compilar informes | Security data basics | verificar (exportación vía API) | Propio | XA-09 | learn.microsoft.com/defender-endpoint/threat-protection-reports |
| XT-11 | REST API (OpenAPI) | Defender for Endpoint API · machine groups / automation level | Leer niveles de automatización AIR por grupo | Machine.Read.All | verificar | Propio | XA-11 | learn.microsoft.com/defender-xdr/m365d-configure-auto-investigation-response |
| XT-12 | Microsoft Graph | Unified RBAC · roleManagement/defender (roleDefinitions, roleAssignments) | Leer roles y asignaciones de Unified RBAC (humanos y agentes) | RoleManagement.Read.Defender | GA | Propio | XA-11 | learn.microsoft.com/graph/api/resources/unifiedrbacapplication |

## 3. Knowledge nuevos (9)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| XK-01 | Criterios de triaje unificado por carga de trabajo (MDE/MDI/MDO/MDA) y severidad | SharePoint / Dataverse | XA-01, XA-14 | Interno |
| XK-02 | Playbooks de respuesta del CSIRT con ejecutores humano/AIR/agente | SharePoint | XA-02 | Interno (M5.1-PA01 instancia XDR) |
| XK-03 | Baseline de automatización: niveles AIR por grupo, acciones que requieren aprobación | SharePoint | XA-03 | Interno (G2.2-PA03 instancia XDR) |
| XK-04 | Registro de reglas de tuning/supresión con vencimiento y justificación | Dataverse | XA-04 | Interno |
| XK-05 | Inventario de fuentes de señal (dispositivos, sensores MDI, conectores) y umbrales de salud | Dataverse | XA-05 | Interno (M2.1-PA01 instancia XDR) |
| XK-06 | Casos de uso del SOC (step 5) y biblioteca de hunting cross-domain | Git/SharePoint | XA-07 | Interno |
| XK-07 | Portafolio de productos-control y owners por dominio | Dataverse | XA-08 | Interno (M1.1-PA02) |
| XK-08 | Baseline de Unified RBAC: roles por persona SOC y por agente | SharePoint | XA-11 | Interno (M2.2-PA01 instancia XDR) |
| XK-09 | Lecciones aprendidas de incidentes y guiones de ejercicios | SharePoint | XA-12 | Interno |

## 4. Skills nuevos (7)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| XS-01 | Triaje unificado por fuente y correlación | Priorizar High/Medium, todas las fuentes; reconocer correlación multi-señal y no cerrar por una sola alerta. | XA-01, XA-14 |
| XS-02 | Respuesta proporcional cross-domain | Elegir la acción menos invasiva que contiene; límite por alcance; registrar. | XA-02 |
| XS-03 | Supervisión de remediación automatizada | Resumir qué hizo AIR y por qué, señalar acciones anómalas o masivas, preparar la decisión humana. | XA-03 |
| XS-04 | Tuning con vencimiento | Toda supresión lleva justificación, alcance mínimo y fecha; detectar reglas sin coincidencias. | XA-04 |
| XS-05 | Salud de ingesta | Interpretar health reports de EDR/AV, sensores MDI y conectores; abrir tickets con dueño. | XA-05 |
| XS-06 | Detection engineering cross-domain | Consultas multi-tabla; convertir hunts en detecciones con prueba y versión; evitar ruido. | XA-07 |
| XS-07 | Auditoría de automatización y RBAC | Comparar niveles AIR y asignaciones RBAC contra baseline; distinguir error de excepción. | XA-11 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | XA-01 | XA-02 | XA-03 | XA-04 | XA-05 | XA-06 | XA-07 | XA-08 | XA-09 | XA-10 | XA-11 | XA-12 | XA-13 | XA-14 | XA-15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-01 | ● | ● |  |  |  | ● | ● |  |  |  |  |  |  |  |  |
| T-03 |  |  |  |  |  | ● |  |  |  | ● |  |  |  |  |  |
| T-04 | ● | ● | ● | ● |  | ● |  |  |  |  |  | ● |  | ● | ● |
| T-05 | ● | ● |  | ● |  |  | ● |  |  |  |  |  |  | ● |  |
| T-08 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| T-09 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| T-13 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| T-14 |  |  |  |  |  |  |  |  |  |  | ● |  | ● |  |  |
| T-15 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  | ● |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ● | ◎ | ◎ | ◎ |
| T-19 |  |  |  |  |  |  | ● |  | ● |  |  |  | ● |  |  |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-21 | ● | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| T-22 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| XT-01 |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| XT-02 |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| XT-03 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| XT-04 |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |
| XT-05 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| XT-06 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| XT-07 |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |
| XT-08 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| XT-09 |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |
| XT-10 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| XT-11 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |
| XT-12 |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |

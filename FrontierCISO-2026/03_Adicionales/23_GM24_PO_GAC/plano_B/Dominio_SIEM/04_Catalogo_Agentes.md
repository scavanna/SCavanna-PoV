# 04 · Catálogo de agentes (10)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: SIEM/SOAR y data lake de seguridad (Microsoft Sentinel en el portal de Microsoft Defender)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| SA-01 | Triage Copilot de incidentes de Sentinel | SI-D01 | L2 | R1 (alt. R2) |
| SA-02 | Briefer de threat intelligence | SI-W06 | L2 | R1 (alt. R2) |
| SA-03 | Supervisor de automatización (playbooks y automation rules) | SI-D05 | L2 | R2 |
| SA-04 | Analista de cobertura y contenido | SI-W01, SI-W03, SI-W05 | L2 | R2 |
| SA-05 | Centinela de ingesta y fuentes | SI-D02, SI-M04, SI-A01 | L3 / L2 (tickets) | R2 |
| SA-06 | Auditor de cambios y accesos de Sentinel | SI-W02, SI-M01 | L2 | R2 |
| SA-07 | Bibliotecario de detecciones y hunting | SI-D03, SI-D04, SI-A02 | L2 | R3 (alt. R2) |
| SA-08 | Analista FinOps de ingesta | SI-W04, SI-M02, SI-M03 | L2 | R2 |
| SA-09 | Reportero de eficiencia del SOC | SI-M05 | L3 | R2 |
| SA-10 | Analista de la flota SIEM | SI-Q02, SI-Q03 | L1-L2 | R2 |

## 2. Tools de la flota (23; nuevos del dominio: 8)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| ST-01 | REST API (Security Insights) | Sentinel · incidents, alertRules, automationRules, bookmarks, entities | Leer/actualizar incidentes; leer y proponer reglas | Sentinel Reader; Responder para incidentes; Contributor con aprobación | GA | Compartido | SA-01, SA-03, SA-04, SA-07, SA-09 | learn.microsoft.com/rest/api/securityinsights/ |
| ST-02 | REST API / KQL | Sentinel · health & audit (SentinelHealth, SentinelAudit) | Salud de conectores, reglas y automatización; auditoría de cambios | Log Analytics Reader | GA | Compartido | SA-03, SA-05, SA-06 | learn.microsoft.com/azure/sentinel/health-audit |
| ST-03 | REST API (Security Insights) | Sentinel · recommendations (SOC optimization API) | Recomendaciones de cobertura y valor de datos | Sentinel Reader | preview (API) | Propio | SA-04 | learn.microsoft.com/azure/sentinel/soc-optimization/soc-optimization-api |
| ST-04 | REST API / Content hub | Sentinel · contentTemplates / contentPackages, MITRE coverage | Actualizaciones de soluciones y cobertura MITRE | Sentinel Reader; instalación humana | GA | Propio | SA-04 | learn.microsoft.com/azure/sentinel/sentinel-solutions-deploy |
| ST-05 | KQL (Usage, workbooks) | Workspace Usage Report / Sentinel Cost workbook; tabla Usage | Ingesta, costo, latencia | Log Analytics Reader | GA | Propio | SA-08 | learn.microsoft.com/azure/sentinel/billing-monitor-costs |
| ST-06 | REST API | Sentinel · watchlists; threat intelligence (STIX 2.1) | Mantener watchlists; revisar ingesta de TI | Contributor (watchlists) con aprobación; Reader para TI | GA | Compartido | SA-02, SA-08 | learn.microsoft.com/azure/sentinel/understand-threat-intelligence |
| ST-07 | Logic Apps / Defender SOC connector | Playbooks (Logic Apps) y generated playbooks; run history | Verificar ejecuciones fallidas; proponer correcciones | Logic App Operator; Contributor solo humano | GA | Propio | SA-03 | learn.microsoft.com/azure/sentinel/automation/run-playbooks |
| ST-08 | REST API / DCR | Azure Monitor · Data Collection Rules, AMA agents health | Verificar agentes y DCRs; proponer transformaciones | Monitoring Reader; cambios con aprobación | GA | Propio | SA-05 | learn.microsoft.com/azure/azure-monitor/agents/azure-monitor-agent-overview |
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Compartido | SA-01, SA-07 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Propio | SA-02 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Propio | SA-01 | learn.microsoft.com/graph/api/resources/security-incident |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Compartido | SA-08, SA-10 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Compartido | SA-06, SA-10 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | SA-05 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | SA-01, SA-02, SA-05, SA-07, SA-09, SA-10 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Propio | SA-10 | microsoft.com/microsoft-agent-365 |
| XT-08 | REST API (OpenAPI) | Defender XDR · custom detection rules API / automation rules | Crear/actualizar detecciones personalizadas y reglas de automatización | Custom detections (Manage); Automation rules (Manage) | GA (detectionRules); automation rules a verificar | Propio | SA-07 | learn.microsoft.com/graph/api/resources/security-detectionrule |
| XT-12 | Microsoft Graph | Unified RBAC · roleManagement/defender (roleDefinitions, roleAssignments) | Leer roles y asignaciones de Unified RBAC (humanos y agentes) | RoleManagement.Read.Defender | GA | Propio | SA-06 | learn.microsoft.com/graph/api/resources/unifiedrbacapplication |

## 3. Knowledge nuevos (5)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| SK-01-KB | Criterios de triaje de incidentes de Sentinel por regla, severidad, entidad y táctica | Dataverse | SA-01 | Interno |
| SK-02-KB | Apetito de automatización: qué automation rules/playbooks actúan sin aprobación | SharePoint / Git | SA-03, SA-06 | Interno (G2.2-PA03 instancia SIEM) |
| SK-03-KB | Técnicas MITRE priorizadas y mapa de cobertura objetivo | Dataverse | SA-04 | Interno |
| SK-04-KB | Inventario de fuentes, conectores, DCRs, parsers y umbrales de salud | Dataverse | SA-05 | Interno (M2.1-PA01 instancia SIEM) |
| SK-05-KB | Commitment tiers, presupuesto de ingesta, retención, tablas con valor | Dataverse | SA-08 | Interno |

## 4. Skills nuevos (4)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| DS-S1 | Triaje por regla y táctica | Ponderar severidad de regla, entidades, táctica y correlación con XDR; detectar reglas ruidosas. | SA-01 |
| DS-S2 | Supervisión de SOAR | Leer run history, distinguir fallo técnico de acción indebida; nunca ejecutar respuesta. | SA-03 |
| DS-S3 | Ingeniería de cobertura | Mapear reglas a técnicas, detectar huecos, proponer templates; medir ruido. | SA-04 |
| DS-S4 | FinOps de ingesta | Costo por tabla/fuente, valor de seguridad, basic logs, filtros DCR, retención. | SA-08 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | SA-01 | SA-02 | SA-03 | SA-04 | SA-05 | SA-06 | SA-07 | SA-08 | SA-09 | SA-10 |
|---|---|---|---|---|---|---|---|---|---|---|
| ST-01 | ● |  | ● | ● |  |  | ● |  | ● |  |
| ST-02 |  |  | ● |  | ● | ● |  |  |  |  |
| ST-03 |  |  |  | ● |  |  |  |  |  |  |
| ST-04 |  |  |  | ● |  |  |  |  |  |  |
| ST-05 |  |  |  |  |  |  |  | ● |  |  |
| ST-06 |  | ● |  |  |  |  |  | ● |  |  |
| ST-07 |  |  | ● |  |  |  |  |  |  |  |
| ST-08 |  |  |  |  | ● |  |  |  |  |  |
| T-01 | ● |  |  |  |  |  | ● |  |  |  |
| T-03 |  | ● |  |  |  |  |  |  |  |  |
| T-04 | ● |  |  |  |  |  |  |  |  |  |
| T-13 |  |  |  |  |  |  |  | ● |  | ● |
| T-14 |  |  |  |  |  | ● |  |  |  | ● |
| T-15 |  |  |  |  | ● |  |  |  |  |  |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 | ● | ● |  |  | ● |  | ● |  | ● | ● |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  |  |  |  | ● |
| XT-08 |  |  |  |  |  |  | ● |  |  |  |
| XT-12 |  |  |  |  |  | ● |  |  |  |  |

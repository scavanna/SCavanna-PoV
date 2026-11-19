# 04 · Catálogo de agentes (10)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Postura y protección de cargas de trabajo en la nube (Microsoft Defender for Cloud: CSPM, CWPP, Defender for AI Services)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| CA-01 | Triage Copilot de alertas de carga de trabajo | CL-D01, CL-A01 | L2 | R1 (alt. R2) |
| CA-02 | Analista de rutas de ataque y hardening | CL-D02, CL-M04 | L2 | R2 |
| CA-03 | Steward de governance rules y recomendaciones | CL-D03, CL-W02, CL-M01 | L2 | R2 |
| CA-04 | Reportero de postura cloud | CL-W01, CL-M05 | L3 | R2 |
| CA-05 | Analista de cumplimiento regulatorio | CL-W03, CL-A03 | L2 | R2 |
| CA-06 | Centinela de cobertura e inventario multicloud | CL-W04, CL-M02, CL-M03, CL-A02 | L3 / L2 (tickets) | R2 |
| CA-07 | Centinela de postura de recursos de IA | CL-W05 | L3 / L2 (propuestas) | R2 |
| CA-08 | Supervisor de workflow automation y export | CL-W06 | L2 | R2 |
| CA-09 | Vigía de cambios de plataforma (Defender for Cloud) | CL-W07 | L3 | R2 |
| CA-10 | Analista de la flota Nube | CL-Q02, CL-Q03 | L1-L2 | R2 |

## 2. Tools de la flota (24; nuevos del dominio: 9)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| CT-01 | REST API (Microsoft.Security) | Defender for Cloud · assessments, secureScores, secureScoreControls | Recomendaciones y secure score | Security Reader | GA | Compartido | CA-02, CA-03, CA-04, CA-05, CA-06, CA-07 | learn.microsoft.com/rest/api/defenderforcloud/ |
| CT-02 | REST API (Microsoft.Security) | Defender for Cloud · governanceRules / governanceAssignments | Asignar dueño y fecha a recomendaciones; seguir vencidas | Security Admin con aprobación; Reader para seguimiento | GA | Compartido | CA-02, CA-03 | learn.microsoft.com/azure/defender-for-cloud/governance-rules |
| CT-03 | REST API / Resource Graph | Defender for Cloud · attack paths y cloud security graph | Rutas de ataque y recomendaciones que las rompen | Security Reader | GA (Defender CSPM) | Compartido | CA-02, CA-04 | learn.microsoft.com/azure/defender-for-cloud/how-to-manage-attack-path |
| CT-04 | REST API (Microsoft.Security) | Defender for Cloud · regulatoryCompliance | Estado de cumplimiento por estándar y control | Security Reader | GA | Propio | CA-05 | learn.microsoft.com/azure/defender-for-cloud/concept-regulatory-compliance-standards |
| CT-05 | REST API (Microsoft.Security) | Defender for Cloud · alerts y continuous export | Alertas de carga de trabajo; correlación con XDR | Security Reader; Admin para dismiss con aprobación | GA | Propio | CA-01 | learn.microsoft.com/azure/defender-for-cloud/alerts-reference |
| CT-06 | Logic Apps | Defender for Cloud · workflow automation | Verificar automatizaciones y proponer nuevas | Security Admin + Logic App Contributor (humano) | GA | Propio | CA-08 | learn.microsoft.com/azure/defender-for-cloud/workflow-automations |
| CT-07 | REST API (Microsoft.Security) | Defender for Cloud · pricings y DWU cost tracking | Planes habilitados y costo | Security Reader | GA (DWU en portal Defender) | Propio | CA-06 | learn.microsoft.com/azure/defender-for-cloud/defender-portal/estimate-track-costs |
| CT-08 | REST API (Microsoft.Security) | Defender for Cloud · exemptions / posture policies (preview) | Exenciones y políticas de postura | Security Reader; exenciones solo humano | GA (exenciones); preview (posture policies) | Compartido | CA-03, CA-05 | learn.microsoft.com/azure/defender-for-cloud/exempt-resource |
| CT-09 | REST API / Defender XDR | Defender for AI Services + AI-SPM | Postura y amenazas de recursos de IA | Security Reader | GA (plan Defender for AI Services) | Propio | CA-07 | learn.microsoft.com/azure/defender-for-cloud/ai-threat-protection |
| ST-07 | Logic Apps / Defender SOC connector | Playbooks (Logic Apps) y generated playbooks; run history | Verificar ejecuciones fallidas; proponer correcciones | Logic App Operator; Contributor solo humano | GA | Propio | CA-08 | learn.microsoft.com/azure/sentinel/automation/run-playbooks |
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Propio | CA-01 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Propio | CA-09 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Propio | CA-01 | learn.microsoft.com/graph/api/resources/security-incident |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | CA-09 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Compartido | CA-06, CA-10 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Propio | CA-10 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | CA-06 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | CA-03 | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | CA-01, CA-04, CA-08, CA-10 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Compartido | CA-07, CA-10 | microsoft.com/microsoft-agent-365 |

## 3. Knowledge nuevos (6)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| CK-01 | Criticidad de suscripciones/recursos, criterios de triaje y dueños de suscripción | Dataverse | CA-01, CA-02, CA-04 | Interno |
| CK-02 | Attack paths vigentes, recomendaciones que los rompen y decisiones de deny/JIT | Dataverse | CA-02 | Interno |
| CK-03 | Governance rules (alcance, dueños, SLAs, gracia) y exenciones con vencimiento | SharePoint / Dataverse | CA-03, CA-08 | Interno (G2.2-PA03 instancia Nube) |
| CK-04 | Estándares regulatorios asignados, controles objetivo y evidencia | SharePoint | CA-05 | Interno |
| CK-05 | Inventario multicloud, planes habilitados y presupuesto DWU | Dataverse | CA-06 | Interno (M2.1-PA01 instancia Nube) |
| CK-06 | Inventario de recursos de IA por flota y postura objetivo | Dataverse | CA-07 | Interno (AMP-51) |

## 4. Skills nuevos (6)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| DS-C1 | Triaje de alertas cloud por criticidad de recurso | Ponderar plan, recurso, criticidad, exposición y correlación XDR. | CA-01 |
| DS-C2 | Lectura de rutas de ataque | Identificar entrada, movimiento y objetivo; proponer la recomendación que rompe la ruta. | CA-02 |
| DS-C3 | Gobierno de remediación delegada | Asignar dueño/fecha con governance rules, seguir vencidas, escalar; nunca remediar. | CA-03 |
| DS-C4 | Cumplimiento con evidencia | Leer estado por estándar/control, preparar evidencia, detectar exenciones débiles. | CA-05 |
| DS-C5 | Cobertura y costo multicloud | Planes por suscripción, recursos no evaluados, DWU; cobertura proporcional a criticidad. | CA-06 |
| DS-C6 | Postura de recursos de IA | Leer recomendaciones/alertas de AI Services y AI-SPM; vincular con la flota que usa el recurso. | CA-07 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | CA-01 | CA-02 | CA-03 | CA-04 | CA-05 | CA-06 | CA-07 | CA-08 | CA-09 | CA-10 |
|---|---|---|---|---|---|---|---|---|---|---|
| CT-01 |  | ● | ● | ● | ● | ● | ● |  |  |  |
| CT-02 |  | ● | ● |  |  |  |  |  |  |  |
| CT-03 |  | ● |  | ● |  |  |  |  |  |  |
| CT-04 |  |  |  |  | ● |  |  |  |  |  |
| CT-05 | ● |  |  |  |  |  |  |  |  |  |
| CT-06 |  |  |  |  |  |  |  | ● |  |  |
| CT-07 |  |  |  |  |  | ● |  |  |  |  |
| CT-08 |  |  | ● |  | ● |  |  |  |  |  |
| CT-09 |  |  |  |  |  |  | ● |  |  |  |
| ST-07 |  |  |  |  |  |  |  | ● |  |  |
| T-01 | ● |  |  |  |  |  |  |  |  |  |
| T-03 |  |  |  |  |  |  |  |  | ● |  |
| T-04 | ● |  |  |  |  |  |  |  |  |  |
| T-09 |  |  |  |  |  |  |  |  | ● |  |
| T-13 |  |  |  |  |  | ● |  |  |  | ● |
| T-14 |  |  |  |  |  |  |  |  |  | ● |
| T-15 |  |  |  |  |  | ● |  |  |  |  |
| T-16 | ◎ | ◎ | ● | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 | ● |  |  | ● |  |  |  | ● |  | ● |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  | ● |  |  | ● |

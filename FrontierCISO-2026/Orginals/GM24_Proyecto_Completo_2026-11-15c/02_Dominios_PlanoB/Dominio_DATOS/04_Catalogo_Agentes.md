# 04 · Catálogo de agentes (11)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de la información y de los datos (Microsoft Purview: clasificación, etiquetado, DLP, DSPM / DSPM for AI, Insider Risk)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| DA-01 | Triage Copilot de alertas DLP e Insider | DP-D01 | L2 | R2 |
| DA-02 | Asistente de investigación y remediación de datos | DP-D02, DP-A01 | L2 | R2 |
| DA-03 | Analista de falsos positivos y excepciones DLP | DP-D03, DP-M02 | L2 | R2 |
| DA-04 | Centinela de postura de datos e IA | DP-D04, DP-M06 | L3 / L2 (propuestas) | R2 |
| DA-05 | Centinela de salud de clasificación | DP-D05, DP-A02 | L3 / L2 (tickets) | R2 |
| DA-06 | Analista de simulación y promoción de políticas | DP-W01, DP-A03 | L2 | R2 |
| DA-07 | Reportero de cobertura y protección de datos | DP-W02, DP-M04, DP-M05 | L3 | R2 |
| DA-08 | Steward de compartición y archivos en SaaS | DP-W03, DP-W06 | L2 | R2 |
| DA-09 | Bibliotecario de hunting de datos | DP-W04 | L2 | R3 (alt. R2) |
| DA-10 | Vigía de cambios de plataforma (Purview) | DP-W05 | L3 | R2 |
| DA-11 | Analista de la flota Datos | DP-Q02, DP-Q03 | L1-L2 | R2 |

## 2. Tools de la flota (24; nuevos del dominio: 10)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| DT-02 | Security & Compliance PowerShell (runbook) | Purview PowerShell · Get-DlpCompliancePolicy/Rule, Get-Label/LabelPolicy, Get-AutoSensitivityLabelPolicy | Leer políticas DLP, etiquetas, auto-etiquetado; proponer cambios (simulación) | Information Protection Admin; el agente solo invoca el runbook | GA | Compartido | DA-03, DA-05, DA-06 | learn.microsoft.com/powershell/module/exchange/get-dlpcompliancepolicy |
| DT-03 | Microsoft Graph | Microsoft Graph · security/alerts_v2 (DLP) y auditLogs | Alertas DLP y auditoría de Purview | SecurityAlert.Read.All; AuditLog.Read.All | GA | Compartido | DA-01, DA-03 | learn.microsoft.com/graph/api/resources/security-alert |
| DT-04 | Advanced Hunting (KQL) | CloudAppEvents, EmailEvents (DLP), DataSecurityBehaviors/Events (preview) | Hunting sobre actividad de datos, etiquetado y egress | ThreatHunting.Read.All | GA (CloudAppEvents); verificar tablas IRM | Compartido | DA-01, DA-02, DA-08, DA-09 | learn.microsoft.com/defender-xdr/advanced-hunting-schema-tables |
| DT-05 | Portal / exportación | Activity explorer, Content explorer, DLP reports, Data classification | Actividad de etiquetas/DLP, contenido clasificado, informes | Information Protection Analyst/Investigator | verificar (API de exportación) | Compartido | DA-02, DA-03, DA-06, DA-07 | learn.microsoft.com/purview/data-classification-activity-explorer |
| DT-06 | Portal / exportación | DSPM y DSPM for AI (Purview) | Postura de datos, sobrecompartición, uso de IA sobre datos sensibles | Data Security Management / Compliance Administrator | verificar (API) | Compartido | DA-04, DA-07 | learn.microsoft.com/purview/data-security-posture-management-learn-about |
| DT-08 | Defender for Cloud Apps API | Defender for Cloud Apps · file policies, files API, governance actions | Descubrir y proteger archivos en SaaS; aplicar etiqueta / quitar compartición tras aprobación | API token acotado; governance con aprobación | GA | Compartido | DA-02, DA-05, DA-08 | learn.microsoft.com/defender-cloud-apps/api-files |
| DT-09 | Agent flow + scanner | Information protection scanner (on-prem) · informes | Descubrir y etiquetar repositorios on-prem | Cuenta del scanner; agente solo lectura | GA | Propio | DA-05 | learn.microsoft.com/purview/deploy-scanner |
| DT-10 | Microsoft Graph | Microsoft Graph · sites/drives (sharing links, permissions) | Detectar sobrecompartición y proponer corrección | Sites.Read.All; corrección con aprobación | GA | Compartido | DA-02, DA-08 | learn.microsoft.com/graph/api/resources/sharinglink |
| DT-11 | Microsoft Graph | Microsoft Graph · security/dataSecurityAndGovernance (processContent, protectionScopes) | Evaluar contenido de prompts/respuestas de agentes contra políticas de Purview (DLP para IA) | Content.Process.All / ProtectionScopes.Compute.All | GA (Purview APIs for AI apps) | Propio | DA-04 | learn.microsoft.com/purview/developer/ |
| DT-12 | Portal / PowerShell | Compliance Manager · evaluaciones, improvement actions | Evaluaciones y acciones de mejora de protección de datos | Compliance Manager Reader | verificar (API) | Propio | DA-07 | learn.microsoft.com/purview/compliance-manager |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Propio | DA-10 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Propio | DA-01 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Propio | DA-09 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | DA-10 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | DA-11 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Propio | DA-11 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | DA-05 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | DA-07, DA-09, DA-11 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Compartido | DA-04, DA-11 | microsoft.com/microsoft-agent-365 |

## 3. Knowledge nuevos (6)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| DK-D1 | Taxonomía de etiquetas, SITs críticos, ubicaciones y criterios de triaje DLP | SharePoint / Dataverse | DA-01, DA-06, DA-08 | Interno (G2.2-PA03 instancia Datos) |
| DK-D2 | Playbooks de fuga de datos con ejecutores y coordinación Legal | SharePoint | DA-02 | Interno (M5.1-PA01 instancia Datos) |
| DK-D3 | Registro de excepciones DLP, overrides y ajustes de SIT con vencimiento; simulaciones | Dataverse | DA-03, DA-06 | Interno |
| DK-D4 | Inventario de fuentes de conocimiento aprobadas por flota y protection scopes | Dataverse | DA-04, DA-07 | Interno (AMP-32, AGC-07) |
| DK-D5 | Inventario de repositorios, políticas de auto-etiquetado y estado del scanner | Dataverse | DA-05 | Interno (M2.1-PA01 instancia Datos) |
| DK-D6 | Sitios sensibles, reglas de compartición y excepciones | Dataverse | DA-08 | Interno |

## 4. Skills nuevos (4)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| DS-D1 | Triaje DLP por sensibilidad real | Ponderar SIT, confianza, cantidad, ubicación y usuario; distinguir error de exfiltración; correlar con IRM sin abrir casos. | DA-01 |
| DS-D2 | Remediación proporcional de datos | Educar → quitar compartición → cuarentena; nunca borrar; límite; coordinar notificación con Legal. | DA-02, DA-08 |
| DS-D3 | Tuning de clasificación con simulación | Analizar coincidencias y confianza; proponer ajuste con vencimiento; siempre simular antes de bloquear. | DA-03, DA-06 |
| DS-D4 | Postura de datos e IA | Leer DSPM/DSPM for AI; verificar fuentes aprobadas y protection scopes de agentes. | DA-04 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | DA-01 | DA-02 | DA-03 | DA-04 | DA-05 | DA-06 | DA-07 | DA-08 | DA-09 | DA-10 | DA-11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DT-02 |  |  | ● |  | ● | ● |  |  |  |  |  |
| DT-03 | ● |  | ● |  |  |  |  |  |  |  |  |
| DT-04 | ● | ● |  |  |  |  |  | ● | ● |  |  |
| DT-05 |  | ● | ● |  |  | ● | ● |  |  |  |  |
| DT-06 |  |  |  | ● |  |  | ● |  |  |  |  |
| DT-08 |  | ● |  |  | ● |  |  | ● |  |  |  |
| DT-09 |  |  |  |  | ● |  |  |  |  |  |  |
| DT-10 |  | ● |  |  |  |  |  | ● |  |  |  |
| DT-11 |  |  |  | ● |  |  |  |  |  |  |  |
| DT-12 |  |  |  |  |  |  | ● |  |  |  |  |
| T-03 |  |  |  |  |  |  |  |  |  | ● |  |
| T-04 | ● |  |  |  |  |  |  |  |  |  |  |
| T-05 |  |  |  |  |  |  |  |  | ● |  |  |
| T-09 |  |  |  |  |  |  |  |  |  | ● |  |
| T-13 |  |  |  |  |  |  |  |  |  |  | ● |
| T-14 |  |  |  |  |  |  |  |  |  |  | ● |
| T-15 |  |  |  |  | ● |  |  |  |  |  |  |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 |  |  |  |  |  |  | ● |  | ● |  | ● |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  | ● |  |  |  |  |  |  | ● |

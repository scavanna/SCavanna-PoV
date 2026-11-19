# 04 · Catálogo de agentes (11)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Protección de identidades y acceso (Microsoft Defender for Identity + Microsoft Entra ID Protection + Conditional Access + Entra ID Governance)** · 2026-11-14 · v1.0. Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| IA-01 | Triage Copilot de incidentes de identidad | ID-D02 | L2 | R1 (alt. R2) |
| IA-02 | Asistente de investigación y remediación de identidad | ID-D03, ID-A01 | L2 | R1 (alt. R2) |
| IA-04 | Analista de tuning de alertas de identidad | ID-D04, ID-M01 | L2 | R2 |
| IA-05 | Centinela de salud de sensores de identidad | ID-D05, ID-Q01 | L3 (detección) / L2 (tickets) | R2 |
| IA-06 | Steward de identidades no humanas y de agentes | ID-W04, ID-A03 | L2 | R2 |
| IA-07 | Analista de Conditional Access | ID-W03, ID-M04 | L1-L2 | R2 |
| IA-08 | Reportero de postura y riesgo de identidad | ID-D01, ID-W01, ID-M03 | L3 | R2 |
| IA-09 | Steward de identidades privilegiadas y recertificación | ID-M02, ID-Q03 | L2 | R2 |
| IA-10 | Vigía de cambios de plataforma (MDI/Entra) | ID-W05 | L3 | R2 |
| IA-11 | Bibliotecario de hunting de identidad | ID-D06, ID-W02 | L2 | R3 (alt. R2) |
| IA-13 | Analista de la flota Identidades | ID-Q02 | L1-L2 | R2 |

## 2. Tools de la flota (29; nuevos del dominio: 9)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| IT-01 | REST API (OpenAPI) | Microsoft Graph · identityProtection/riskyUsers, riskySignIns (riskDetections) | Usuarios e inicios de sesión riesgosos; confirmar comprometido / descartar | IdentityRiskyUser.Read.All / ReadWrite.All; IdentityRiskEvent.Read.All | GA (Entra ID P2) | Compartido | IA-01, IA-02 | learn.microsoft.com/graph/api/resources/riskyuser |
| IT-02 | REST API (OpenAPI) | Microsoft Graph · identity/conditionalAccess/policies (+ report-only insights) | Leer políticas de CA; proponer cambios en report-only | Policy.Read.All; escritura solo con aprobación | GA | Propio | IA-07 | learn.microsoft.com/graph/api/resources/conditionalaccesspolicy |
| IT-03 | REST API (OpenAPI) | Microsoft Graph · security/identities/healthIssues (MDI) e Identity Security dashboard | Salud de sensores MDI; insights de identidad | SecurityIdentitiesHealth.Read.All | GA | Compartido | IA-05, IA-08 | learn.microsoft.com/graph/api/resources/security-healthissue |
| IT-04 | Advanced Hunting (KQL) | Tablas IdentityLogonEvents, IdentityDirectoryEvents, IdentityQueryEvents, AADSignInEventsBeta, IdentityInfo | Hunting sobre autenticación y cambios de directorio | ThreatHunting.Read.All | GA | Compartido | IA-01, IA-02, IA-04, IA-11 | learn.microsoft.com/defender-xdr/advanced-hunting-schema-tables |
| IT-05 | REST API (OpenAPI) | Microsoft Graph · users (revokeSignInSessions, accountEnabled), authentication methods | Revocar sesiones, deshabilitar, forzar reset | User.RevokeSessions.All; User.EnableDisableAccount.All; UserAuthenticationMethod.ReadWrite.All | GA | Propio | IA-02 | learn.microsoft.com/graph/api/user-revokesigninsessions |
| IT-06 | REST API (OpenAPI) | Microsoft Graph · identityGovernance (access reviews, PIM, entitlement) | Recertificación, elegibilidad PIM, paquetes de acceso | AccessReview.ReadWrite.All; RoleManagement.Read.Directory | GA | Compartido | IA-06, IA-09 | learn.microsoft.com/graph/api/resources/identitygovernance-overview |
| IT-07 | REST API (OpenAPI) | Microsoft Graph · auditLogs/signIns y directoryAudits | Sign-in logs y auditoría de directorio | AuditLog.Read.All | GA | Compartido | IA-02, IA-07 | learn.microsoft.com/graph/api/resources/signin |
| IT-08 | REST API (OpenAPI) | Microsoft Graph · identityProtection/riskyServicePrincipals (workload identities) | Riesgo de identidades de carga de trabajo (incl. agentes) | IdentityRiskyServicePrincipal.Read.All | GA (Workload Identities Premium) | Propio | IA-06 | learn.microsoft.com/graph/api/resources/riskyserviceprincipal |
| IT-09 | REST API / Hunting | Secure Score (MDI / Entra) y posture assessments de MDI | Postura de identidad (on-prem e híbrida) | SecurityEvents.Read.All | GA | Propio | IA-08 | learn.microsoft.com/defender-for-identity/security-assessment |
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Propio | IA-01 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-02 | MCP | Microsoft MCP Server for Enterprise (Graph) | Consultas de solo lectura sobre el tenant (usuarios, grupos, roles, dispositivos) | Custom connector; app registration con permisos MCP.*; solo lectura | GA (solo lectura) | Propio | IA-06 | learn.microsoft.com/graph/mcp-server/use-enterprise-mcp-server-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Propio | IA-10 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Compartido | IA-01, IA-02, IA-04 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Propio | IA-11 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-08 | REST API (OpenAPI) | Microsoft Graph · security/secureScores | Leer Secure Score y recomendaciones | SecurityEvents.Read.All | GA | Propio | IA-08 | learn.microsoft.com/graph/api/resources/securescore |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Compartido | IA-05, IA-10 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-11 | Conector prebuilt | Microsoft Graph · users (Entra) | Atributos de usuarios y etiquetas para cuentas prioritarias | User.Read.All | GA | Propio | IA-09 | learn.microsoft.com/graph/api/resources/user |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | IA-13 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Compartido | IA-09, IA-13 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | IA-05 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | IA-07, IA-08, IA-11, IA-13 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Compartido | IA-06, IA-13 | microsoft.com/microsoft-agent-365 |
| XT-04 | REST API (OpenAPI) | Defender XDR · alert tuning rules / MDE indicators | Proponer y crear reglas de tuning y supresión con vencimiento | Alerts (Manage) | GA (indicadores); tuning vía API a verificar | Propio | IA-04 | learn.microsoft.com/defender-xdr/investigate-alerts#tune-an-alert |
| XT-08 | REST API (OpenAPI) | Defender XDR · custom detection rules API / automation rules | Crear/actualizar detecciones personalizadas y reglas de automatización | Custom detections (Manage); Automation rules (Manage) | GA (detectionRules); automation rules a verificar | Propio | IA-11 | learn.microsoft.com/graph/api/resources/security-detectionrule |

## 3. Knowledge nuevos (6)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|
| DK-I1 | Criterios de triaje de identidad: cuentas sensibles, riesgo compuesto, detecciones MDI | Dataverse | IA-01 | Interno |
| DK-I2 | Playbooks de compromiso de identidad con remediación automática vs. manual | SharePoint | IA-02 | Interno (M5.1-PA01 instancia Identidades) |
| DK-I3 | Registro de reglas de tuning de MDI con vencimiento | Dataverse | IA-04 | Interno |
| DK-I4 | Inventario de sensores MDI y umbrales de salud | Dataverse | IA-05 | Interno |
| DK-I5 | Inventario de identidades privilegiadas, NHI y agentes (sponsor, caducidad, PIM) | Dataverse | IA-06, IA-09 | Interno (AMP-33, M2.1-PA01) |
| DK-I6 | Baseline de Conditional Access (riesgo, break-glass, exclusiones con vencimiento) | SharePoint / Git | IA-07 | Interno (G2.2-PA03 instancia Identidades) |

## 4. Skills nuevos (4)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|
| DS-I1 | Triaje de identidad por sensibilidad y riesgo compuesto | Priorizar cuentas sensibles y riesgo High compuesto; distinguir benign true positives. | IA-01 |
| DS-I2 | Remediación proporcional de identidad | Dejar que CA auto-remedie cuando aplica; revocar antes que deshabilitar; nunca break-glass. | IA-02 |
| DS-I3 | Higiene de identidades privilegiadas y no humanas | PIM, caducidad, sponsors, migración a Agent ID; detectar huérfanas. | IA-06, IA-09 |
| DS-I4 | Análisis de efecto de Conditional Access | Leer insights/report-only, estimar impacto, detectar bloqueos indebidos; solo proponer. | IA-07 |

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | IA-01 | IA-02 | IA-04 | IA-05 | IA-06 | IA-07 | IA-08 | IA-09 | IA-10 | IA-11 | IA-13 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IT-01 | ● | ● |  |  |  |  |  |  |  |  |  |
| IT-02 |  |  |  |  |  | ● |  |  |  |  |  |
| IT-03 |  |  |  | ● |  |  | ● |  |  |  |  |
| IT-04 | ● | ● | ● |  |  |  |  |  |  | ● |  |
| IT-05 |  | ● |  |  |  |  |  |  |  |  |  |
| IT-06 |  |  |  |  | ● |  |  | ● |  |  |  |
| IT-07 |  | ● |  |  |  | ● |  |  |  |  |  |
| IT-08 |  |  |  |  | ● |  |  |  |  |  |  |
| IT-09 |  |  |  |  |  |  | ● |  |  |  |  |
| T-01 | ● |  |  |  |  |  |  |  |  |  |  |
| T-02 |  |  |  |  | ● |  |  |  |  |  |  |
| T-03 |  |  |  |  |  |  |  |  | ● |  |  |
| T-04 | ● | ● | ● |  |  |  |  |  |  |  |  |
| T-05 |  |  |  |  |  |  |  |  |  | ● |  |
| T-08 |  |  |  |  |  |  | ● |  |  |  |  |
| T-09 |  |  |  | ● |  |  |  |  | ● |  |  |
| T-11 |  |  |  |  |  |  |  | ● |  |  |  |
| T-13 |  |  |  |  |  |  |  |  |  |  | ● |
| T-14 |  |  |  |  |  |  |  | ● |  |  | ● |
| T-15 |  |  |  | ● |  |  |  |  |  |  |  |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 |  |  |  |  |  | ● | ● |  |  | ● | ● |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  | ● |  |  |  |  |  | ● |
| XT-04 |  |  | ● |  |  |  |  |  |  |  |  |
| XT-08 |  |  |  |  |  |  |  |  |  | ● |  |

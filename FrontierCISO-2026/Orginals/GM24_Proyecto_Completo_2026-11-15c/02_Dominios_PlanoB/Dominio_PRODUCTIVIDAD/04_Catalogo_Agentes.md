# 04 · Catálogo de agentes (15)

> **GM-24 V7.1 · Sub-plan PO-GAC · Instancia de dominio: Seguridad de correo y colaboración (Microsoft Defender for Office 365 sobre Exchange Online Protection, en Microsoft Defender XDR)** · 2026-11-14 · v1.1 (re-emisión en formato uniforme de la instancia V5/V6). Plano B (*ProductPractice* / escenario). No agrega ni modifica conceptos de la V7 (379): los instancia. Escenario 100 % Microsoft sobre bases agnósticas; estado GA/preview/verificar según Microsoft Learn. Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Resumen

| ID | Agente | Tareas | Autonomía | Ruta |
|---|---|---|---|---|
| AG-01 | Triage Copilot de incidentes de correo | MDO-D01, MDO-D03, MDO-D04 | L2 | R2 (alt. R1) |
| AG-02 | Asistente de investigación y remediación | MDO-D02, MDO-A01 | L2 | R2 (alt. R1) |
| AG-03 | Analista de FP/FN y listas | MDO-D05, MDO-D06, MDO-D07, MDO-D08 | L2 | R2 |
| AG-04 | Revisor de campañas | MDO-D09, MDO-W04 | L2 / L3 (informe) | R2 |
| AG-05 | Reportero de tendencias de detección | MDO-W01 | L3 | R2 |
| AG-06 | Briefer de inteligencia de amenazas | MDO-W02 | L2 | R2 (alt. R1) |
| AG-07 | Steward de cuentas prioritarias | MDO-W03, MDO-A05 | L2 | R2 |
| AG-08 | Reportero de postura (Secure Score) | MDO-W05 | L3 | R2 |
| AG-09 | Vigía de cambios de plataforma | MDO-W06 | L3 | R2 |
| AG-10 | Centinela de deriva de configuración | MDO-M01 | L3 (detección) / L2 (corrección) | R2 |
| AG-11 | Auditor de overrides y suplantación | MDO-M02, MDO-M03 | L2 | R2 |
| AG-12 | Redactor de concientización | MDO-M04 | L1 | R2 |
| AG-13 | Analista de la flota (desempeño, costo, accesos) | MDO-Q02, MDO-Q03 | L1-L2 | R2 |
| AG-14 | Bibliotecario de hunting y detecciones | MDO-A02, MDO-A03, MDO-A04 | L2 | R3 (alt. R2) |
| AG-15 | Sincronizador de tickets | MDO-A06 | L3 | R2 |

## 2. Tools de la flota (24; nuevos del dominio: 0)

| ID | Tipo | Tool | Operación | Permiso mínimo | Estado | Alcance | Agentes | Fuente |
|---|---|---|---|---|---|---|---|---|
| T-01 | MCP | Microsoft Sentinel MCP server | Consultas sobre el data lake de Sentinel (EmailEvents, EmailUrlInfo, AlertInfo, IdentityInfo); colecciones de triage/hunting | Entra ID integrated; RBAC de Sentinel (lectura) | preview | Compartido | AG-01, AG-02, AG-06, AG-14 | learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio |
| T-02 | MCP | Microsoft MCP Server for Enterprise (Graph) | Consultas de solo lectura sobre el tenant (usuarios, grupos, roles, dispositivos) | Custom connector; app registration con permisos MCP.*; solo lectura | GA (solo lectura) | Propio | AG-07 | learn.microsoft.com/graph/mcp-server/use-enterprise-mcp-server-copilot-studio |
| T-03 | MCP | Microsoft Learn Docs MCP | Documentación oficial (guías de operación, cambios) | Sin datos del tenant | GA | Compartido | AG-06, AG-09 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-04 | Conector prebuilt | Microsoft Graph · security/incidents y alerts_v2 | Leer incidentes/alertas de Defender XDR; actualizar clasificación, estado, comentarios | SecurityIncident.Read.All / ReadWrite.All; Unified RBAC | GA | Compartido | AG-01, AG-02, AG-04, AG-06, AG-15 | learn.microsoft.com/graph/api/resources/security-incident |
| T-05 | REST API (OpenAPI) | Microsoft Graph · security/runHuntingQuery | KQL sobre tablas de Defender XDR (EmailEvents, EmailPostDeliveryEvents, UrlClickEvents) | ThreatHunting.Read.All | GA | Compartido | AG-01, AG-02, AG-03, AG-04, AG-05, AG-07, AG-11, AG-14 | learn.microsoft.com/graph/api/security-security-runhuntingquery |
| T-06 | REST API (OpenAPI) | Microsoft Graph · security/threatSubmission | Crear envíos de FP/FN a Microsoft y consultar estado | ThreatSubmission.ReadWrite.All | GA | Propio | AG-03 | learn.microsoft.com/graph/api/resources/security-threatsubmissionroot |
| T-07 | Agent flow + Azure Automation | Exchange Online PowerShell vía runbook (TABL, cuarentena, políticas) | New/Get/Remove-TenantAllowBlockListItems; Get/Release-QuarantineMessage; Get-*Policy | Identidad administrada con rol Exchange acotado; el agente solo invoca el flujo | GA (patrón a validar) | Compartido | AG-02, AG-03, AG-04, AG-11 | learn.microsoft.com/powershell/module/exchange/new-tenantallowblocklistitems |
| T-08 | REST API (OpenAPI) | Microsoft Graph · security/secureScores | Leer Secure Score y recomendaciones | SecurityEvents.Read.All | GA | Compartido | AG-08, AG-10 | learn.microsoft.com/graph/api/resources/securescore |
| T-09 | Conector prebuilt | Microsoft 365 Message Center / serviceAnnouncement | Leer anuncios y cambios planificados | ServiceMessage.Read.All | GA | Propio | AG-09 | learn.microsoft.com/graph/api/resources/serviceannouncement |
| T-10 | Agent flow + PowerShell (ORCA) | ORCA / Configuration Analyzer | Comparar configuración de Defender for Office 365 frente a Standard/Strict | Lectura de configuración vía identidad administrada | GA (ORCA comunitario) | Propio | AG-10 | github.com/cammurray/orca |
| T-11 | Conector prebuilt | Microsoft Graph · users (Entra) | Atributos de usuarios y etiquetas para cuentas prioritarias | User.Read.All | GA | Propio | AG-07 | learn.microsoft.com/graph/api/resources/user |
| T-12 | REST API (OpenAPI) | Microsoft Graph · security/attackSimulation | Crear/consultar simulaciones | AttackSimulation.ReadWrite.All | GA | Propio | AG-12 | learn.microsoft.com/graph/api/resources/attacksimulationroot |
| T-13 | Conector prebuilt | Azure Cost Management | Consumo y presupuesto de Foundry y Copilot Studio | Cost Management Reader | GA | Propio | AG-13 | learn.microsoft.com/rest/api/cost-management |
| T-14 | REST API (OpenAPI) | Microsoft Graph · identityGovernance/accessReviews | Revisiones de acceso (recertificación) | AccessReview.ReadWrite.All | GA (Entra ID Governance) | Propio | AG-13 | learn.microsoft.com/graph/api/resources/accessreviewsv2-overview |
| T-15 | Conector prebuilt | ServiceNow / Jira (ITSM) | Crear, leer y actualizar tickets | Cuenta de servicio ITSM acotada | GA | Propio | AG-15 | learn.microsoft.com/connectors/service-now |
| T-16 | Conector prebuilt | Microsoft Teams (mensajes y tarjetas) | Notificar, pedir aprobación, entregar informes | Canales designados | GA | Común | flota | learn.microsoft.com/connectors/teams |
| T-17 | Conector prebuilt | Approvals | Aprobación humana (gate L2) con registro del aprobador | Aprobadores designados | GA | Común | flota | learn.microsoft.com/connectors/approvals |
| T-18 | Conector prebuilt | SharePoint / Dataverse | Evidencias, bitácoras, informes y registros | Escritura en sitios/tablas designados | GA | Común | flota | learn.microsoft.com/connectors/sharepointonline |
| T-19 | Conector prebuilt | Azure Monitor Logs (Sentinel) | KQL sobre workspace de Sentinel | Log Analytics Reader | GA | Compartido | AG-05, AG-13, AG-14 | learn.microsoft.com/connectors/azuremonitorlogs |
| T-20 | Prompt (AI Builder) | Prompt de resumen y clasificación | Resumir, clasificar, redactar en formato fijo | Sin datos externos | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/nlu-prompt-node |
| T-21 | Conector prebuilt | Defender for Cloud Apps / Defender ATP (conectores) | Correlación con alertas de apps y endpoints | Lectura de alertas | GA (conectores soportados) | Propio | AG-02 | learn.microsoft.com/power-platform/admin/security/secure-web-ai-gateway-agents |
| T-22 | REST API (OpenAPI) | Microsoft Graph · reports (informes de protección) | Informes de estado de protección y flujo de correo | Reports.Read.All | verificar (cobertura de informes MDO vía API) | Propio | AG-05 | learn.microsoft.com/graph/api/resources/report |
| T-23 | Agent flow (programado) | Trigger de cadencia | Disparar tareas diarias/semanales/mensuales | — | GA | Común | flota | learn.microsoft.com/microsoft-copilot-studio/advanced-flow |
| T-24 | Agent 365 / PPAC | APIs de Agent 365 | Inventario, estado y analítica de agentes | Administrador de agentes | verificar (API pública no confirmada) | Propio | AG-13 | microsoft.com/microsoft-agent-365 |

## 3. Knowledge nuevos (0)

| ID | Fuente | Tipo | Agentes | Origen |
|---|---|---|---|---|

## 4. Skills nuevos (0)

| ID | Skill | Descripción | Agentes |
|---|---|---|---|

## 5. Matriz tools × agentes (● propio · ◎ común)

| Tool | AG-01 | AG-02 | AG-03 | AG-04 | AG-05 | AG-06 | AG-07 | AG-08 | AG-09 | AG-10 | AG-11 | AG-12 | AG-13 | AG-14 | AG-15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T-01 | ● | ● |  |  |  | ● |  |  |  |  |  |  |  | ● |  |
| T-02 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| T-03 |  |  |  |  |  | ● |  |  | ● |  |  |  |  |  |  |
| T-04 | ● | ● |  | ● |  | ● |  |  |  |  |  |  |  |  | ● |
| T-05 | ● | ● | ● | ● | ● |  | ● |  |  |  | ● |  |  | ● |  |
| T-06 |  |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |
| T-07 |  | ● | ● | ● |  |  |  |  |  |  | ● |  |  |  |  |
| T-08 |  |  |  |  |  |  |  | ● |  | ● |  |  |  |  |  |
| T-09 |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |  |
| T-10 |  |  |  |  |  |  |  |  |  | ● |  |  |  |  |  |
| T-11 |  |  |  |  |  |  | ● |  |  |  |  |  |  |  |  |
| T-12 |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |  |
| T-13 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| T-14 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |
| T-15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ● |
| T-16 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-17 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-18 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-19 |  |  |  |  | ● |  |  |  |  |  |  |  | ● | ● |  |
| T-20 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-21 |  | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |
| T-22 |  |  |  |  | ● |  |  |  |  |  |  |  |  |  |  |
| T-23 | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ | ◎ |
| T-24 |  |  |  |  |  |  |  |  |  |  |  |  | ● |  |  |

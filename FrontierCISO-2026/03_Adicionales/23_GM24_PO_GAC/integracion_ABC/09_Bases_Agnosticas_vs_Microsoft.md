# 09 · Bases agnósticas frente a implementación Microsoft

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

| Capacidad | Base agnóstica | Implementación Microsoft | Portabilidad |
|---|---|---|---|
| Modelo operativo por cadencias | MAEO eo:OP; ITIL | Security Operations Guide MDO; tareas SOC XDR | Alto |
| Identidad de agentes | OAuth2/OIDC; SPIFFE; workload identity | Entra Agent ID | Medio |
| Permisos de herramientas | Least privilege; allowlists | Políticas de datos PPAC; API permissions | Medio |
| Telemetría | OpenTelemetry | Foundry tracing; Sentinel; Agent 365 analytics | Alto |
| Herramientas/protocolos | MCP; OpenAPI | Sentinel MCP; MCP Server for Enterprise; conectores | Alto (MCP) / Bajo (conectores) |
| Evidencia | Esquema común; ISO 27001 A.8.15 | SharePoint/Dataverse + Sentinel | Alto |
| Detección como código | Sigma | Custom detections; KQL en Git | Medio |
| Gobierno de IA | AI RMF; ISO 42001 | AGC; Compliance Manager; Agent 365 | Alto |
| Controles de agentes | OWASP ASI; CSA AICM | Prompt Shields; DLP; CA para agentes | Medio |
| Costos | FinOps Foundation | Cost Management; SCU; capacidad | Alto |
| Autorización | NIST RMF Authorize | Expediente ATO; Agent 365 | Alto |
| Postura de IA | CSPM/AI-SPM; CIS Benchmarks | Defender for Cloud (IA) | Medio |
| Continuidad | ISO 22301 | Soluciones versionadas; exportación de agentes | Medio |
| Datos | Gobierno de datos; DSPM | Purview DSPM for AI; DLP | Medio |
| Pruebas adversariales | Red teaming de IA; ATLAS | Foundry evaluations; PyRIT | Alto |

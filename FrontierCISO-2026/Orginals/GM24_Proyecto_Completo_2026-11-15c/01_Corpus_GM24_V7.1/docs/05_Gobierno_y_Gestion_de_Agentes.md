# 05 · Gobierno y gestión de agentes: catálogo AGC, RACI y escala de autonomía

> **GM-24 V7.1 · The Next CISO + Sub-plan PO-GAC** · 2026-11-14. Catálogo: 379 conceptos (245 K · 52 AMP · 40 HC · 42 PA), todos con pre-ensayo íntegro y mapeados a 17 marcos (NIST/ISACA/MITRE/OWASP/CIS/CSA). V7.1 = ChangeSet editorial CS-GM24-V7.1-001 (4 títulos generalizados; sin cambio de IDs, cantidad ni mapeo). Plano A (corpus académico). Referencias DD/K4x/R/eo:OP/COE: marco interno.

## 1. Catálogo de controles AGC (24)
| ID | Capa | Control | Objetivo | AI RMF | ISO 42001 | OWASP ASI | Implementación Microsoft | Base agnóstica | Evidencia | Responsable |
|---|---|---|---|---|---|---|---|---|---|---|
| AGC-01 | Dirección | Registro e inventario de agentes | Todo agente registrado con dueño, propósito, estado | GOVERN-1 | A.6 | ASI10 | Agent 365 registry; PPAC | Inventario de sistemas de IA | Inventario | PO-GAC |
| AGC-02 | Dirección | Dueño y sponsor | Cada agente tiene owner y sponsor con autoridad real | GOVERN-2 | A.3 | ASI10 | Entra Agent ID sponsor | Accountability | Declaración | PO-GAC |
| AGC-03 | Política | Ficha aprobada | Charter con propósito, límites, autonomía, KPIs | GOVERN-1 | A.6 | ASI01 | Plantilla ficha; descripción Copilot Studio | Documentación de sistemas | Ficha | PO-GAC |
| AGC-04 | Política | Clasificación de riesgo y autonomía | Nivel L0–L4 por tipo de acción aprobado por dueño del riesgo | MAP-2 | A.5 | ASI03 | Escala L0–L4; Approvals | Apetito de riesgo | Clasificación | Dueño del riesgo |
| AGC-05 | Identidad | Identidad propia | Agente con Entra Agent ID, no identidad del constructor | GOVERN-1 | A.9 | ASI03 | Entra Agent ID | Workload identity | Identidad | IAM |
| AGC-06 | Identidad | Mínimo privilegio y herramientas | Permisos por tool; allowlist de conectores | MANAGE-1 | A.9 | ASI02 | Políticas de datos PPAC; API permissions | Least privilege | Allowlist | PO-GAC |
| AGC-07 | Datos | Datos y fuentes aprobadas | Knowledge sources aprobadas, etiquetadas, con procedencia | MAP-4 | A.7 | ASI06 | Purview DLP; DSPM for AI | Gobierno de datos | Inventario de fuentes | Datos |
| AGC-08 | Datos | Guardrails | Contenido nunca es instrucción; filtros; content safety | MEASURE-2 | A.6 | ASI01 | Prompt Shields; Content Safety; SK-01 | Defensa en profundidad | Pruebas | PO-GAC |
| AGC-09 | Operación | HITL por acción | Aprobación previa / auditoría posterior / nunca por tarea | GOVERN-2 | A.9 | ASI09 | Approvals; matriz tarea→gate | Meaningful human control | Matriz | PO-GAC |
| AGC-10 | Operación | Límites y kill switch | Límites de lote; detención probada trimestralmente | MANAGE-1 | A.6 | ASI08 | PPAC/Agent 365 desactivación | Circuit breaker | Prueba | PO-GAC |
| AGC-11 | Evidencia | Trazabilidad | Esquema de evidencia común por decisión | MEASURE-3 | A.6 | ASI07 | Sentinel; SharePoint/Dataverse | Logging | Paquete de evidencia | PO-GAC |
| AGC-12 | Evidencia | Evaluación previa | Dataset dorado + red teaming antes de producción | MEASURE-2 | A.6 | ASI01 | Foundry evaluations; PyRIT | Testing | Informe | PO-GAC |
| AGC-13 | Dirección | ATO | Autorización formal con expediente y vigencia | MANAGE-1 | A.5 | ASI10 | Agent 365; comité | RMF Authorize | Expediente | Dueño del riesgo |
| AGC-14 | Operación | Monitoreo y deriva | KRIs y revisión trimestral de desempeño | MEASURE-3 | A.6 | ASI08 | Sentinel; Agent 365 analytics | Monitoreo | KRIs | PO-GAC |
| AGC-15 | Operación | Presupuesto y consumo | Costo por tarea; alertas de consumo | MAP-3 | A.6 | — | Cost Management | FinOps | Modelo de costos | PO-GAC |
| AGC-16 | Operación | Cambios y versionado | ChangeSets con regresión; ALM | MANAGE-4 | A.6 | ASI04 | Power Platform ALM; Git | Gestión de cambios | Pipeline | PO-GAC |
| AGC-17 | Operación | Incidentes de agentes | Playbook 'agente comprometido'; tabletop | MANAGE-4 | A.6 | ASI08 | Playbooks; Sentinel | IR | Playbook | CSIRT |
| AGC-18 | Identidad | Recertificación | Accesos de agentes recertificados trimestralmente | GOVERN-1 | A.9 | ASI03 | Entra access reviews | Recertificación | Evidencia | IAM |
| AGC-19 | Dirección | Retiro | Desactivación, revocación y archivo de evidencia | MANAGE-2 | A.6 | ASI10 | Agent 365; Entra | Ciclo de vida | Registro | PO-GAC |
| AGC-20 | Datos | Cadena de suministro de IA | AI BOM; conectores/MCP aprobados | GOVERN-6 | A.10 | ASI04 | Inventario MCP; PPAC | C-SCRM | AI BOM | PO-GAC |
| AGC-21 | Política | Transparencia | Disclosure a usuarios; derecho a revisión humana | GOVERN-4 | A.8 | ASI09 | Texto de disclosure | IA responsable | Disclosure | PO-GAC |
| AGC-22 | Evidencia | Aseguramiento independiente | Auditoría interna anual con acceso directo a evidencia | GOVERN-2 | A.6 | — | Plan de auditoría | Tres líneas | Informe | Auditoría |
| AGC-23 | Dirección | Competencia del owner | Itinerario acreditado antes de operar L2+ | GOVERN-3 | A.4 | — | Sub-plan PO-GAC | Competency-based | Autoevaluación | CISO |
| AGC-24 | Dirección | Métricas de gobierno | Cobertura de registro, sin dueño, recertificación a tiempo | MEASURE-1 | A.6 | ASI10 | Agent 365; Compliance Manager | Governance metrics | Tablero | PO-GAC |

## 2. RACI (16 actividades)
| Actividad | Analista/Constructor | PO-GAC | Dueño del riesgo / COE-IA | IAM / Datos | Auditoría |
|---|---|---|---|---|---|
| Registrar agente | R | A | C | I | I |
| Aprobar ficha | R | A | C | I | I |
| Clasificar autonomía | C | R | A | I | I |
| Asignar identidad y permisos | R | A | I | C | I |
| Aprobar fuentes de datos | C | A | I | R | I |
| Evaluar previo a producción | R | A | C | I | I |
| Autorizar (ATO) | C | R | A | I | I |
| Aprobar acciones L2 | R | A | I | I | I |
| Monitorear KRIs | R | A | I | I | C |
| Revisar desempeño trimestral | R | A | C | I | I |
| Recertificar accesos | R | A | I | C | I |
| Gestionar cambios (ChangeSet) | R | A | C | I | I |
| Gestionar incidentes de agentes | R | A | C | I | I |
| Retirar agente | R | A | I | C | I |
| Auditar flota | I | C | I | I | A/R |
| Reportar a dirección | R | A | C | I | I |

## 3. Escala de autonomía L0–L4
| Nivel | Definición | Ejemplo |
|---|---|---|
| L0 | Solo informa | Reporte de tendencias |
| L1 | Propone; humano ejecuta | Hipótesis de hunting |
| L2 | Propone y ejecuta tras aprobación | Remediación de correo |
| L3 | Ejecuta acciones reversibles y de bajo impacto; auditoría posterior | Detección de deriva; tickets |
| L4 | Autónomo con límites estrictos (no previsto en este sub-plan) | — |

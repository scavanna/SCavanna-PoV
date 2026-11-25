# Microsoft AI Security & Compliance Coverage — Versión 4
## Roadmap con dependencias, licenciamiento, riesgo Preview y auditabilidad

> **Conclusión.** La V4 no aumenta artificialmente el porcentaje de cobertura técnica. Ajusta la V3 a una cobertura **asegurada y defendible**, penalizando dependencias no implementadas, capacidades Preview y evidencia insuficiente. El resultado es más conservador, pero más útil para auditoría, decisiones de inversión y compromisos de cumplimiento.

## 1. Método V4

La V4 separa tres conceptos:

1. **Cobertura V3:** alcance potencial si todas las tecnologías propuestas están disponibles y correctamente configuradas.
2. **Cobertura V4 asegurada:** cobertura que puede sostenerse con dependencias explícitas, controles GA, fallback, ownership, operación y licenciamiento.
3. **Readiness de auditoría/evidencia:** capacidad de entregar artefactos suficientes, íntegros, trazables, vigentes y aprobados para demostrar diseño y efectividad.

Los porcentajes son estimaciones analíticas relativas, no certificaciones, opiniones legales ni scores emitidos por Microsoft, ISO, NIST, OWASP, MITRE o una autoridad de protección de datos.

## 2. Comparación V3, V4 y evidencia

| Framework | V3 potencial | V4 asegurada | Variación | Readiness evidencia | Gap V4-evidencia |
|---|---:|---:|---:|---:|---:|
| OWASP LLM06 + NIST AI RMF | 96% | 94% | -2 pp | 92% | 2 pp |
| MITRE ATLAS | 96% | 93% | -3 pp | 91% | 2 pp |
| ISO/IEC 42001 | 92% | 90% | -2 pp | 84% | 6 pp |
| NIST AI RMF | 97% | 95% | -2 pp | 88% | 7 pp |
| GDPR | 91% | 89% | -2 pp | 82% | 7 pp |

### Interpretación

La disminución de 2 a 3 puntos desde V3 no representa una pérdida tecnológica. Es un descuento de assurance por capacidades Preview, cobertura condicionada, licencias separadas, dependencia de onboarding y ausencia posible de evidencia primaria. La mayor distancia entre operación y evidencia aparece en GDPR y NIST AI RMF (7 pp), seguidos de ISO/IEC 42001 (6 pp), porque la tecnología no puede sustituir decisiones jurídicas, liderazgo, independencia de auditoría, revisión de dirección ni documentación controlada.

## 3. Roadmap V4

| Fase | Horizonte | Objetivo | Dependencias mínimas | Licenciamiento/costo | Tratamiento Preview | Gate |
|---|---|---|---|---|---|---|
| F0 | 0-15 días | Gobierno y arquitectura de evidencia | Inventario mínimo de agentes y AI workloads; RACI; Data Owner; CISO/SOC; DPO/Legal; Audit; Platform Engineering. | M365 E7 y Agent 365 habilitados; Azure subscription; roles administrativos; repositorio de evidencia; decisión de alcance AIMS/GDPR. | Incluido: E7/Agent 365 según contrato. Consumo adicional: Azure storage/monitoring. | Scope aprobado; 100% activos con owner/sponsor; repositorio y retención definidos. |
| F1 | 15-45 días | Fundación GA y baseline | F0; conectores y permisos; clasificación de datos; arquitectura de identidad; selección de workspaces y regiones. | E7 incluye Entra Suite y Purview elegible; Defender for Cloud/CSPM, Key Vault, Azure Monitor y Log Analytics son cargos Azure separados. | Usar MCSB v1 GA como baseline. MCSB v2 solo shadow mapping. | Gate 1: evidencia de inventario, identidad y datos; revisión de privacidad de telemetría. |
| F2 | 30-75 días | Observabilidad y detección | F1; esquema de eventos; IDs de correlación; DCR; clasificación/redacción; runbooks; SOC capacitado. | Sentinel y Log Analytics por ingestión/retención/queries; Application Insights por volumen; Security Copilot incluido para tenants E5/E7 elegibles, con SCUs y eventual overage. | Agent views y parte de tracing/continuous evaluation pueden ser Preview; mantener dashboards GA y exportación de logs como respaldo. | Gate 2: DLP/redacción validada; retención aprobada; detecciones probadas con eventos sintéticos. |
| F3 | 45-90 días | Frontera de ejecución GA | F1 identidad/red; F2 logging; catálogo de modelos/tools; owners de API; threat model. | APIM tier según requerimientos; Defender for APIs plan separado con cinco niveles y overage por tráfico; Private Link/DDoS/WAF según arquitectura. | No depender del AI Gateway dedicado Preview. Pilotearlo aislado; APIM GA permanece control productivo. | Gate 3: gateway GA, rollback, export de config, pruebas de autorización y resiliencia. |
| F4 | 60-120 días | Secure SDLC y assurance | F1 repos/inventario; F3 endpoints; criterios de severidad; ambientes test; datos sintéticos. | GHAS/ADO por active committer; pipelines/compute; Foundry/model/token consumption; Defender for Cloud DevOps/CSPM según plan. | Red teaming agent, algunas evaluaciones y continuous evaluation pueden estar Preview; nunca único gate de release. | Gate 4: evidencia reproducible; revisión humana; aprobación release; rollback probado. |
| F5 | 90-150 días | Auditoría y conformidad | F0-F4; control owners; muestreo; control de documentos; Legal/DPO; Internal Audit independiente. | Principalmente esfuerzo interno/partner; Compliance Manager según licencia; almacenamiento WORM/retención si requerido. | Evidencia Preview se acepta solo como secundaria, etiquetada y acompañada por control GA/manual. | Gate 5: auditoría interna cerrada o plan CAPA aprobado antes de claim externo/certificación. |
| F6 | Continuo | Operación, recertificación y cambio | F5 operativo; calendario de control; SLAs; CAB; vendor management; threat intel. | Costos recurrentes de Azure, Sentinel, API protection, SCUs/agents, repos y auditoría/certificación. | Promoción Preview→GA solo tras revalidación, update de arquitectura, DR, SLA y evidencias. | Gate continuo: revisión mensual operativa, trimestral riesgo/preview y anual AIMS/privacidad. |

### Secuencia crítica

- **F0 antes de tecnología:** sin alcance, owners, RACI y una taxonomía de evidencia, los dashboards no demuestran accountability.
- **F1 antes de observabilidad:** identidad administrada, clasificación y retención evitan que el logging se convierta en una nueva exposición.
- **F2 antes de automatización:** el SOC necesita data contracts, IDs de correlación y playbooks antes de incorporar agentes de respuesta.
- **F3 usa GA para producción:** APIM y sus capacidades de AI gateway son la frontera productiva; el AI Gateway dedicado Preview queda como piloto con fallback.
- **F4 separa test automatizado de aprobación:** red teaming y evaluadores Preview complementan, pero no reemplazan revisión humana ni criterios de release.
- **F5 convierte controles en evidencia:** cada control crítico requiere owner, período, población, fuente, muestreo y resultado.

## 4. Dependencias estructurales

| Dependencia | Capacidades afectadas | Entregable | Fase | Owner |
|---|---|---|---|---|
| Inventario y ownership | Todas | Agent Registry + AI BOM + CMDB reconciliados | F0-F1 | Agent Owner / Cloud Security |
| Identidad y secretos | Gateway, APIs, observabilidad, runtime | Managed identities, Entra CA, Key Vault, access reviews | F1 | IAM Owner |
| Clasificación y privacidad | Purview, tracing, Sentinel, GDPR | Data map, labels, DLP, redaction, retention, DPIA threshold | F0-F2 | DPO + Data Owner |
| Data contract de telemetría | Sentinel, App Insights, Foundry | Event schema, trace ID, time sync, source of truth, retention | F2 | Observability Lead |
| Gateway/egress enforzado | Defender for APIs, MCP/tool control | APIM GA, private paths, deny bypass, approved backends | F3 | Platform Owner |
| Secure SDLC | Runtime y auditoría | Repos, CI/CD, GHAS, SBOM/AI BOM, releases | F4 | DevSecOps |
| Gobierno documental | ISO/GDPR/NIST | Version control, approval, retention, immutability, access | F0-F5 | AIMS Manager / Records |
| Auditoría independiente | ISO/GDPR assurance | Plan, sampling, competence, independence and CAPA | F5-F6 | Internal Audit |

## 5. Licenciamiento y costos que condicionan la cobertura

| Tecnología | Modelo | Dependencias | Riesgo | Evidencia |
|---|---|---|---|---|
| Microsoft 365 E7 + Agent 365 | Licencia base por usuario/tenant según contrato | Asignación de licencias, roles y habilitación de servicios. | Tenant sin rollout, límites de servicio y diferencias regionales. | Contrato, service plan export, capturas de roles y configuración. |
| Microsoft Security Copilot | Incluido para clientes elegibles M365 E5/E7; capacidad medida en SCUs; overage/provisioning puede generar cargos | Tenant habilitado, workspace, roles y gobierno de capacidad. | Throttling/overage, costos de agentes, datos almacenados y roles por defecto. | Uso SCU, configuración workspace, roles, auditoría de prompts/actions. |
| Microsoft Sentinel | Azure consumption: Analytics/Data Lake, ingestión, retención y queries; compromiso/prepurchase opcional | Azure subscription, Log Analytics/Sentinel, DCR/conectores. | Costo por volumen, retención, queries y automatización. | Cost analysis, data collection rules, retention, connector health, analytics rules. |
| Azure Monitor / Application Insights | Azure consumption por ingestión, retención y consulta | Instrumentación, workspace, RBAC, redacción. | PII/secrets, alto volumen y vistas preview. | Sampling/redaction config, retention, trace IDs, cost reports. |
| Azure API Management | Tier APIM según escala/red/HA; AI gateway capabilities están en APIM | Networking, identity, policies, backends y certificados. | Tier insuficiente, costos de unidades/regiones y bypass. | Policies exportadas, diagnostics, deployment history, gateway logs. |
| AI Gateway dedicado | Preview; pricing/business model puede cambiar o no estar cerrado | Región soportada, feature flag, aislamiento y rollback a APIM. | Sin SLA de producción, regiones limitadas y migración/resource type. | Registro de aceptación Preview, test report, rollback y config export. |
| Defender for APIs | Plan separado a nivel suscripción; cinco planes por volumen y overage | APIM, Defender for Cloud y onboarding explícito. | Plan 1 por defecto puede causar overage; cobertura parcial. | Plan seleccionado, APIs onboarded, traffic entitlement, alerts y recommendations. |
| Defender for Cloud/CSPM/AI workloads | Planes Azure por recurso/suscripción; revisar pricing vigente | Conectores Azure/AWS/GCP, permissions y planes habilitados. | Activos no conectados y cargos por plan/recurso. | Pricing settings export, inventory, recommendations, attack paths y alerts. |
| GHAS / Advanced Security for Azure DevOps | Licencia por active committer; facturación mensual a Azure subscription | Azure Repos/GitHub, pipelines, permisos y repos in-scope. | Crecimiento de active committers, repos sin habilitar y Marketplace tasks. | License count, repo coverage, scan runs, alerts and waivers. |
| Microsoft Purview DSPM / AI interactions | M365 E5/Purview Suite para DSPM; algunas interacciones pueden requerir PAYG | Licencias, permissions, analytics opt-in y data connectors. | PAYG inesperado, soporte desigual por app/agente y privacidad. | License assignment, opt-in, support matrix, policy matches y cases. |
| WAF / Front Door / DDoS / Private Link / Key Vault | Azure consumption por recurso, SKU, tráfico y operaciones | Diseño de red, DNS, certificates y managed identities. | Complejidad, bloqueo legítimo, costos y dependencia regional. | Policies, access logs, attack simulations, secret rotation y DR tests. |

### Implicaciones principales

- Microsoft Sentinel no debe modelarse como capacidad incluida sin límites: la ingesta, retención, consultas, automatización y data lake condicionan costo y diseño.
- Security Copilot está incluido para tenants M365 E5/E7 elegibles, pero la capacidad se mide en SCUs y los agentes/overage pueden afectar presupuesto y disponibilidad.
- Defender for APIs requiere plan separado y onboarding. La selección incorrecta del plan puede producir overage y una API no onboarded no queda protegida.
- GHAS para Azure DevOps se factura por active committer, por lo que el alcance de repositorios debe definirse antes de habilitarlo masivamente.
- Purview DSPM requiere las licencias correspondientes y ciertas interacciones de IA pueden necesitar PAYG.

## 6. Registro de riesgos Preview

| Funcionalidad | Riesgo | Severidad | Control compensatorio | Regla de evidencia | Criterio de producción |
|---|---|---|---|---|---|
| AI Gateway dedicado / new resource type | Cambio de APIs, resource IDs/endpoints, regiones y pricing; sin garantía de producción. | Alta | Pilot aislado; APIM GA como fallback; IaC abstraído; feature flag; export config; prueba de rollback. | No evidencia primaria; solo soporte secundario etiquetado Preview. | No producción crítica hasta GA/SLA/región y pen test aprobados. |
| MCSB v2 y AI security domain | Controles/mappings pueden cambiar y recomputar resultados. | Media | Baseline productivo MCSB v1 + Azure Policy propias; versionar export v2. | Puede apoyar gap analysis, no claim de certificación. | Usar como shadow assessment; promover tras estabilización. |
| Foundry continuous evaluation / red teaming agent | Resultados/modelos pueden cambiar, sin SLA y con cobertura de ataques incompleta. | Alta | Combinar con pruebas manuales, datasets versionados y evaluadores GA; reproducibilidad y sign-off humano. | Evidencia secundaria; informe firmado y dataset/versiones como evidencia primaria. | No gate único de release. |
| Foundry tracing para workflow/external agents | Cambios de schema, gaps de telemetría y captura de datos sensibles. | Alta | OTel estándar, logs de aplicación, redacción, sampling y data contract propio. | Export OTel controlada es primaria; vista preview es visualización secundaria. | No depender del dashboard para retención o cadena de custodia. |
| Application Insights Agents view | La vista puede cambiar aunque los traces subyacentes permanezcan. | Media | Consultas KQL/workbooks versionados y exportables; acceso a raw telemetry. | KQL export + trace IDs, no screenshots solamente. | Admitida para operación, no como único artefacto de auditoría. |
| Copilot Studio environment-level telemetry | Solo managed environments y cobertura/schema limitados. | Alta | Agent-level telemetry GA cuando esté disponible; pruebas en non-prod; documentar gaps. | Evidence pack debe declarar población no cubierta. | No claim 100% hasta reconciliación de eventos. |
| Security Copilot agents con funciones Preview | Autonomía, consumo SCU y acciones automatizadas pueden variar. | Alta | Least privilege, human approval, budget caps, sandbox, kill switch y action logs. | Logs de decisión/acción + ticket humano; salida generativa no es evidencia concluyente. | Automatización de bajo impacto primero. |
| Sentinel MCP server/tools | Quotas, query costs, freshness y exposición de herramientas de seguridad. | Media-Alta | Read-only, roles mínimos, monitoring, quotas y separación de tenants/workspaces. | KQL/query logs y approvals; no usar respuestas generadas como prueba única. | Pilot SOC interno; no acciones destructivas. |

### Política V4 para Preview

1. Ninguna capacidad Preview es el único control que previene, detecta o prueba un riesgo crítico.
2. Toda Preview tiene owner, feature flag, entorno delimitado, presupuesto, monitoreo, kill switch y rollback probado.
3. La evidencia generada por Preview se clasifica como secundaria, salvo que los datos subyacentes se exporten a una fuente GA controlada e íntegra.
4. El paso a producción exige revisión de SLA, región, soporte, licenciamiento, data handling, API/resource type y pruebas de regresión.
5. Cada trimestre se revisa continuidad, promoción a GA, deprecación y necesidad de re-DPIA o actualización del AIMS.

## 7. Auditoría y evidencia por framework

### OWASP LLM06 + NIST AI RMF
**Cobertura V4 asegurada: 94%. Readiness de evidencia: 92%.**

**Brecha clave:** OWASP no es certificable; debe probarse la efectividad del least privilege y de los gates por caso de uso.

| Requisito | Artefacto | Fuente | Frecuencia | Owner | Preparación |
|---|---|---|---|---|---|
| Inventario de tools y funciones | Matriz agente-tool-function con necesidad y owner | Agent 365/APIM catalog | Mensual y por cambio | Agent Owner | Parcial |
| Least privilege | Scopes, access package, identity, access review y pruebas de denegación | Entra/Key Vault/APIM | Trimestral y por release | IAM Owner | Alta |
| Human approval | Reglas, tickets y logs de aprobación para acciones críticas | Aplicación/Agent 365/Sentinel | Cada acción crítica | Business Owner | Media |
| Prueba adversaria | Casos negativos, resultados y remediación | Foundry/GHAS/red team | Cada release mayor | AI Assurance | Alta |

### MITRE ATLAS
**Cobertura V4 asegurada: 93%. Readiness de evidencia: 91%.**

**Brecha clave:** ATLAS es una base viva, no certificación; hay que fijar versión y demostrar cobertura y prueba de detecciones.

| Requisito | Artefacto | Fuente | Frecuencia | Owner | Preparación |
|---|---|---|---|---|---|
| Scope y versión | Matriz ATLAS fijada por release, plataformas y técnicas relevantes | ATLAS Navigator/repo | Trimestral | Threat Modeling Lead | Media |
| Detecciones | Hipótesis, reglas, fuentes, test event y resultado | Sentinel/Defender XDR | Mensual | Detection Engineering | Alta |
| Red/purple team | Plan, ejecución, evidencias, hallazgos y CAPA | Foundry/manual/Sentinel | Semestral y release crítica | Red Team | Alta |

### ISO/IEC 42001
**Cobertura V4 asegurada: 90%. Readiness de evidencia: 84%.**

**Brecha clave:** Las herramientas generan evidencia técnica, pero no sustituyen liderazgo, auditoría independiente ni documentación controlada.

| Requisito | Artefacto | Fuente | Frecuencia | Owner | Preparación |
|---|---|---|---|---|---|
| Contexto y alcance | AIMS scope, partes interesadas, procesos y activos | Repositorio AIMS/Agent registry | Anual y por cambio material | AIMS Manager | Media |
| Liderazgo | AI policy, objetivos, RACI, recursos y management review | AIMS/Compliance Manager | Anual/trimestral | Top Management | Media |
| Riesgo e impacto | Metodología, assessments, SoA y treatment plan | AIMS/Purview/Defender | Por sistema y anual | Risk Owner | Media-Alta |
| Auditoría y mejora | Audit plan/report, nonconformities, CAPA y cierre | Audit/CAPA repository | Anual | Internal Audit | Media |

### NIST AI RMF
**Cobertura V4 asegurada: 95%. Readiness de evidencia: 88%.**

**Brecha clave:** Es voluntario y no certificable; la organización debe definir tolerancia, métodos de medida y aceptación de riesgo.

| Requisito | Artefacto | Fuente | Frecuencia | Owner | Preparación |
|---|---|---|---|---|---|
| GOVERN | Perfil, políticas, responsabilidades y tolerancia | AIMS/Agent 365 | Anual | AI Governance | Media-Alta |
| MAP | Context, purpose, actors, impacts, data and dependencies | Registry/AI BOM/DPIA | Por sistema | Product Owner | Alta |
| MEASURE | TEVV, metrics, datasets, uncertainty and monitoring | Foundry/App Insights | Release/continuo | AI Assurance | Alta |
| MANAGE | Risk decision, treatment, residual acceptance and monitoring | Risk register/CAPA | Trimestral | Risk Owner | Media-Alta |

### GDPR
**Cobertura V4 asegurada: 89%. Readiness de evidencia: 82%.**

**Brecha clave:** La plataforma no determina base legal, proporcionalidad, roles controller/processor ni suficiencia jurídica de transferencias.

| Requisito | Artefacto | Fuente | Frecuencia | Owner | Preparación |
|---|---|---|---|---|---|
| ROPA y base legal | Processing record, purpose, categories, recipients, retention, legal basis | Purview + privacy repository | Por proceso y anual | Controller/DPO | Media |
| DPIA | Descripción, necesidad, proporcionalidad, riesgos, medidas, residual y DPO advice | DPIA + evidence pack | Antes de high-risk processing | Controller/DPO | Media-Alta |
| Derechos y transparencia | Notices, DSAR cases, deletion/export evidence | Purview/eDiscovery/case mgmt | Por solicitud | Privacy Ops | Media-Alta |
| Seguridad e incidentes | Access logs, DLP, alerts, breach assessment/register and notifications | Purview/Defender/Sentinel | Continuo/por incidente | CISO + DPO | Alta |
| Transferencias y processors | DPA, subprocessors, locations, transfer mechanism and assessments | Contracts/service docs | Por proveedor/cambio | Legal/Procurement | Baja-Media |

## 8. Reglas de calidad de evidencia

Una captura de pantalla o un score no son suficientes por sí solos. Un artefacto defendible debe registrar:

- control y requisito al que responde;
- alcance, población y exclusiones;
- owner y aprobador;
- fuente y sistema de registro;
- fecha, período y zona horaria;
- versión de política, modelo, herramienta, framework y dataset;
- integridad, retención y acceso;
- resultado, excepción y riesgo residual;
- ticket, decisión o CAPA asociada;
- evidencia de efectividad, no solo de configuración.

## 9. Conclusión ejecutiva

La V4 desplaza el foco desde “qué productos tenemos” hacia “qué podemos demostrar”. La arquitectura Microsoft puede ofrecer cobertura muy alta, especialmente para identidad, datos, runtime, observabilidad y respuesta. La preparación de auditoría siempre será inferior a la cobertura técnica mientras falten decisiones humanas, documentos controlados, validación jurídica, revisión independiente y pruebas de efectividad. El objetivo del roadmap V4 no es recuperar el 100%, sino hacer que cada porcentaje declarado sea trazable, financiado, operable y defendible.
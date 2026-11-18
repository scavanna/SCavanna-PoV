# Qué reemplaza la V3

| Entregable anterior | Reemplazo dentro de la V3 |
|---|---|
| `MDC_AI_ATLAS_OWASP_Mapping_v1.xlsx` | `MDC_AI_ATLAS_OWASP_Mapping_v3.xlsx`: catálogo corroborado, vínculos y evidencia requerida, ATLAS pinneado, OWASP por edición, referencia CAAT y validación editable. |
| `Deep dive CAAT + crosswalk con alertas MDC-AI.md` | `docs\Investigacion_y_mapeo.md`, hojas CAAT y `data\CAAT_publicado_relaciones.csv`. |
| `Enriquecimiento_MDC-AI.md` | `docs\Investigacion_y_mapeo.md` + `README.md`. |
| `otro.md` | Roadmap público y proyectos: `docs\Investigacion_y_mapeo.md`. Contactos internos corroborados: `uso-interno\Conversaciones_y_contactos.md`. Las menciones no corroboradas de reuniones o compromisos no se conservaron como hechos. |
| `README – Estrategia y pasos de implementación.md` y `README v2 – estrategia e instrucciones de implementación.md` | `README.md` y `docs\Validacion.md`. |
| `Enriquecimiento_MDC-AI.zip` y `Enriquecimiento_MDC-AI v2.zip` | `MDCAI_Sentinel_ATLAS_V3.zip`. Incluye los archivos para instalar, verificar y reconstruir V3. |

La V3 no mantiene compatibilidad con los nombres de funciones, watchlists o tablas de las versiones anteriores. El ZIP permite revertir o volver a instalar **V3**; no borra ni migra recursos de Azure. Antes de retirar archivos antiguos, verificá el manifest y rescatá tus propias notas/resultados. Los artefactos de Azure pueden convivir mientras el playbook nuevo sigue en modo de solo lectura.

## Alertas que cambiaron

Los siguientes cruces son reconciliaciones por descripción con el catálogo Learn. **No son una tabla de alias retrocompatibles**: todavía hay que comprobar `AlertType` que llega a tu tenant.

| Clave local anterior | Decisión V3 |
|---|---|
| `AI.Azure_PhishingContentInModelResponse` | `AI.Azure_MaliciousUrl.ModelResponse` |
| `AI.Azure_PhishingContentInAIApplication` | `AI.Azure_MaliciousUrl.UnknownSource` |
| `AI.Azure_PhishingContentInUserPrompt` | `AI.Azure_MaliciousUrl.UserPrompt` |
| `AI.Azure_SuspiciousInitialAccessOperation` | `AI.Azure_AnomalousOperation.InitialAccess` |
| `AI.Azure_DataLeakInModelResponse.Sensitive`, `AI.Azure_Anomaly` | No aparecen como IDs en el catálogo contrastado. Si se observan, registrarlos como no clasificados; no asociar automáticamente a alertas con nombre parecido. |

Se agregan `AI.Azure_DOWVolumeAnomaly`, `AI.Azure_AnomalousToolInvocation`, `AI.Azure_LLMReconnaissance` (preview) y `AI.AIModelScan_MalwareDetected` (escaneo en preview, opt-in en playbook). `AI.Azure_ASCIISmuggling` se documenta como High; `AI.Azure_AccessAnomaly` incluye Execution, Reconnaissance e Initial access. `Exposed Kubernetes service` y protección de Agent 365 u otros planes son fuentes adyacentes, no tipos de alerta runtime de este inventario.

# Guía y assessment: Logic Apps como capa SOAR central en coexistencia Microsoft Sentinel y SIEM OnPrem

**Versión:** 3.0  
**Actualizado:** 2026-11-11  
**Alcance:** Cliente M365 E5, Microsoft Sentinel dentro del beneficio aplicable, Defender for Servers Plan 2 y un SIEM OnPrem coexistente.  

> Validar licenciamiento, disponibilidad regional, estado GA/preview, APIs, límites y costos en el tenant antes de producción.

## 1. Resumen ejecutivo

El cliente puede construir una capa SOAR centralizada con tecnologías Microsoft durante la convivencia de Microsoft Sentinel y SIEM OnPrem, pero debe distinguir tres funciones: sistema de registro del caso, plano de orquestación y fuentes de detección. La recomendación es usar el portal Microsoft Defender como experiencia operacional preferente para incidentes y casos Microsoft; Microsoft Sentinel como SIEM/XDR de referencia para las señales que se incorporen al ecosistema Microsoft; y Azure Logic Apps como plano reutilizable de orquestación e integración. SIEM OnPrem puede seguir siendo SIEM y fuente de incidentes durante la transición, enviando eventos o casos seleccionados a la capa Microsoft mediante APIs, webhooks, conectores o un broker de integración.

Logic Apps no debe convertirse en una base de datos de casos ni en un “meta-SIEM”. Debe ejecutar flujos idempotentes, auditables y desacoplados de cada SIEM. El case management de Defender puede ser el registro operativo central cuando se validen las licencias, APIs y funciones aplicables al tenant. Si no existe integración soportada suficiente para representar un incidente externo como caso nativo con toda la fidelidad requerida, se debe conservar el sistema de registro vigente y sincronizar contexto, estado y evidencias mediante un identificador de correlación común.

- Adoptar un modelo federado durante la coexistencia, no una migración big bang.
- Priorizar Microsoft Defender portal, Cases, Sentinel, Logic Apps y Security Copilot para las operaciones que ya están en Microsoft.
- Integrar SIEM OnPrem por contrato de eventos/casos estable, evitando playbooks duplicados por SIEM.
- Mantener humano en control para acciones destructivas, de alto impacto o de confianza insuficiente.

## 2. Respuesta directa a la pregunta arquitectónica

Sí, es viable crear un SOAR centralizado que priorice Logic Apps y tecnologías Microsoft aunque existan varias instancias de Sentinel y SIEM OnPrem. La forma robusta no consiste en obligar a que todos los SIEM compartan inmediatamente un único repositorio, sino en centralizar el catálogo de automatizaciones, las políticas de decisión, la observabilidad y los contratos de integración.

El portal Defender puede administrar una instancia primaria y varias secundarias de Sentinel dentro de un tenant, con alcances y limitaciones por experiencia. La cola unificada correlaciona Defender XDR con el workspace primario; los workspaces secundarios mantienen consideraciones específicas. Cases agrega gestión de trabajo, tareas, evidencia e historial dentro del portal Defender. Estas capacidades no significan automáticamente que cualquier incidente de SIEM OnPrem se convierta, sin diseño adicional, en un incidente o caso nativo equivalente. Esa integración debe validarse mediante APIs soportadas, pruebas de ciclo de vida y requisitos de auditoría.

Para la convivencia con SIEM OnPrem, Microsoft documenta como método side-by-side recomendado reenviar alertas desde el SIEM heredado hacia Microsoft Sentinel (por ejemplo, mediante Logstash, APIs o Syslog) para establecer una interfaz única, manteniendo el SIEM heredado para investigaciones profundas durante un período de transición extendido. Ese patrón es coherente con priorizar el portal Defender, Cases y Logic Apps como capa central.

- Patrón recomendado: Defender portal/Cases como plano de experiencia; Logic Apps como plano de ejecución; Sentinel y SIEM OnPrem como productores de señales e incidentes.
- Alternativa de transición: mantener ITSM o SIEM OnPrem como sistema de registro maestro y utilizar Microsoft como plano de enriquecimiento y respuesta.
- No crear dependencia directa de cada playbook con el esquema nativo de cada SIEM; usar un esquema canónico.

## 3. Principios de diseño

La arquitectura debe preservar autonomía entre detección, investigación, decisión y ejecución. Cada automatización debe poder invocarse desde Sentinel, Defender, SIEM OnPrem, ITSM o una operación manual autorizada, sin duplicar la lógica de remediación.

- Contrato canónico de incidente y entidad.
- Idempotencia y prevención de ejecuciones duplicadas.
- Mínimo privilegio con identidades administradas cuando sea posible.
- Separación entre enriquecimiento, recomendación, aprobación y remediación.
- Trazabilidad de entrada, decisión, acción, resultado, costo y actor.
- Infraestructura como código, control de versiones y promoción entre ambientes.
- Acciones reversibles primero; aislamiento y contención antes que eliminación.
- Degradación segura cuando Copilot, un conector o un SIEM no estén disponibles.
- Datos sensibles minimizados y secretos en Key Vault.
- Pruebas técnicas y operativas antes de habilitar automatización autónoma.

## 4. Arquitectura objetivo de coexistencia

La arquitectura propuesta utiliza cinco capas. La primera recibe alertas, incidentes y solicitudes desde Defender XDR, uno o más workspaces Sentinel, SIEM OnPrem, Defender for Cloud y canales ITSM. La segunda normaliza el contenido a un “Security Orchestration Envelope”. La tercera aplica políticas de priorización, confianza, criticidad del activo y aprobación. La cuarta ejecuta capacidades modulares en Logic Apps. La quinta registra el resultado en los sistemas pertinentes y en una bitácora de auditoría.

El sistema maestro del caso debe definirse explícitamente por escenario. Para incidentes nacidos y gestionados en el ecosistema Microsoft, la opción preferida es Defender portal/Cases. Para incidentes que permanezcan bajo responsabilidad de SIEM OnPrem o de un ITSM, el caso maestro puede continuar allí, mientras Logic Apps sincroniza resumen, evidencias, tareas y estado. El identificador global evita que un incidente replicado se procese dos veces.

Restricción de calendario: después del 31 de marzo de 2027, Microsoft Sentinel deja de estar soportado en Azure portal y queda disponible solo en el portal Microsoft Defender. Toda automatización, regla y procedimiento operativo debe diseñarse y probarse sobre el portal Defender.

- Fuentes: Defender XDR, Sentinel primario/secundarios, SIEM OnPrem, Defender for Cloud, ITSM.
- Ingreso: triggers nativos, webhook/API Management, Event Grid/Service Bus cuando se requiera desacoplamiento.
- Normalización: esquema canónico con sourceSystem, sourceTenant, sourceInstance, sourceCaseId y globalCorrelationId.
- Decisión: reglas, listas de activos críticos, severidad, confianza, riesgo y autorización.
- Ejecución: playbooks reutilizables de enriquecimiento, notificación, ticketing, contención, recuperación y cierre.
- Experiencia: Defender portal/Cases cuando sea aplicable; sincronización con SIEM OnPrem/ITSM durante coexistencia.
- Auditoría: Application Insights/Log Analytics, historial de ejecución, comentarios del caso y repositorio de evidencias.

## 5. Contrato canónico de orquestación

El Security Orchestration Envelope desacopla los productores de alertas de los playbooks. Los adaptadores de entrada traducen Sentinel, Defender o SIEM OnPrem al mismo contrato; los adaptadores de salida actualizan cada sistema con su API correspondiente.

- Identidad: globalCorrelationId, sourceSystem, sourceInstance, sourceCaseId, sourceAlertIds.
- Clasificación: title, description, severity, status, category, tactics, techniques, confidence.
- Contexto: entities, artifacts, assetCriticality, businessService, dataSensitivity.
- Gobierno: automationPolicy, approvalRequired, approvedBy, legalHold, dataResidency.
- Ejecución: requestedActions, completedActions, failedActions, retryCount.
- Auditoría: timestamps, initiatingIdentity, workflowVersion, decisionEvidence, costTags.

## 6. Buenas prácticas para Logic Apps como SOAR

Microsoft Sentinel usa playbooks basados en Azure Logic Apps y permite iniciarlos por incidente, alerta o entidad, automáticamente mediante reglas de automatización o manualmente. Para esta arquitectura, se recomienda un patrón de orquestador y capacidades: un flujo de entrada valida y normaliza; luego invoca flujos pequeños y reutilizables por función.

Consumption resulta apropiado para ejecuciones esporádicas y simples. Standard puede ser preferible cuando se requieren varios workflows por recurso, red privada, rendimiento más predecible, administración de conexiones y CI/CD más integrado. La selección debe basarse en volumen, conectividad, residencia, aislamiento y costo medido, no en una regla universal.

En el portal Defender coexisten tres familias de playbooks: Logic Apps con el conector Microsoft Defender SOC (triggers de alerta y de caso), playbooks generados con Playbook Generator (código Python, no son Logic Apps) y Logic Apps con el conector Microsoft Sentinel, que siguen soportados sobre casos e incidentes. Las reglas de automatización pueden ejecutar playbooks cuando un caso, incidente o alerta cumple su trigger y condiciones. En esta guía, Logic Apps es el estándar de orquestación; los playbooks generados se consideran un complemento sujeto a revisión de código y a sus límites documentados (hasta 100 por tenant, hasta 10 minutos por ejecución, sin librerías externas ni anidamiento).

- Separar triggers/adaptadores de las acciones de respuesta.
- Usar scopes TRY/CATCH/FINALLY y registrar errores funcionales y técnicos.
- Aplicar retry exponencial solo a operaciones seguras e idempotentes.
- Usar Service Bus para picos, reintentos durables y desacoplamiento cuando el caso lo justifique.
- Usar APIM para publicar una fachada estable a SIEM OnPrem y otros productores.
- Usar managed identity; almacenar secretos inevitables en Key Vault.
- Etiquetar recursos por caso de uso, dueño, criticidad, ambiente y centro de costo.
- Versionar workflows, parámetros, conexiones, esquemas y políticas.
- Implementar circuit breaker y cola de cuarentena para mensajes fallidos.
- Medir tasa de éxito, latencia, reintentos, costo, rollback y acciones evitadas por controles.
- Diseñar los nuevos playbooks con el conector Microsoft Defender SOC (trigger de alerta o de caso) y mantener los del conector Sentinel mientras se valida la transición a casos.
- Un playbook con entrada de alerta no es automáticamente compatible con entrada de caso: probar cada playbook con el tipo de entrada que usará.
- Permisos: rol Microsoft Sentinel Automation Contributor para la cuenta de servicio de Sentinel en el resource group de los playbooks y permisos RBAC unificados de Defender (Playbooks, Automation rules).
- Persistir estado de correlación e idempotencia en un almacén liviano (por ejemplo, Azure Table Storage) con managed identity y rol Storage Table Data Contributor.

## 7. Case management y consola unificada

Cases en el portal Defender puede administrar trabajo de respuesta, tareas, evidencia, comentarios e historial. La elegibilidad y el comportamiento dependen del escenario, licencia y configuración. La arquitectura debe validar el ciclo completo: creación, enlace de incidentes, asignación, SLA, tareas, evidencias, comentarios, búsqueda, cierre, reapertura, API y auditoría.

No se debe asumir que la vista multi-workspace transforma todos los workspaces en un único repositorio homogéneo. El diseño debe documentar qué funciones operan sobre el workspace primario, cuáles agregan información de secundarios y cuáles requieren seleccionar un workspace. Tampoco se debe asumir paridad entre un caso de Defender y un notable/evento o incidente de SIEM OnPrem.

Cases admite las tres familias de playbooks, con ejecución manual desde el caso y revisión de resultados en Artifacts > Activities. La experiencia de incidentes se está actualizando a la experiencia completa de casos. Con gestión multitenant, el portal Defender permite gestionar casos entre tenants; cada workspace debe incorporarse al portal Defender en su tenant.

- Definir el sistema maestro por tipo de incidente.
- Mantener tabla de estados y severidades entre Microsoft, SIEM OnPrem e ITSM.
- Conservar vínculos al registro original y evidencias, no copiar datos innecesarios.
- Probar conflictos de actualización, cierres simultáneos y reaperturas.
- Usar un journal de sincronización para reconciliación.

## 8. Security Copilot y evolución a SOC agéntico

Security Copilot debe incorporarse primero como capacidad de enriquecimiento, resumen y recomendación con evidencia. Logic Apps puede invocar capacidades de Security Copilot mediante conectores soportados y registrar la salida en incidentes o casos. El uso debe gobernarse por costo, permisos, exposición de datos, calidad del resultado y necesidad operacional.

La autonomía debe progresar por niveles: asistido, recomendado, aprobado y autónomo acotado. Un agente no debe recibir permisos amplios por conveniencia. Las acciones de identidad, aislamiento, bloqueo, borrado, cambios de firewall o recuperación deben tener criterios explícitos, límites, aprobación y rollback.

El conector de Security Copilot para Logic Apps ofrece las acciones Submit a Security Copilot prompt (con sesión, plugins y Direct Skill) y Submit a Security Copilot promptbook; una acción más reciente ejecuta agentes configurados en el workspace predeterminado. Combinar Logic Apps con Security Copilot puede elevar el consumo de SCU: usar Direct Skills, limitar llamadas y adjuntar el playbook solo a incidentes que lo justifiquen mediante condiciones en la regla de automatización. El método de autenticación del conector debe validarse en laboratorio. El conector MCP de Sentinel para Logic Apps está en preview y comienza con Entity Analyzer para usuarios y URLs; muchas herramientas MCP requieren onboarding al Data Lake.

- Nivel 0: manual documentado.
- Nivel 1: enriquecimiento y resumen automático, decisión humana.
- Nivel 2: recomendación y borrador de acciones, aprobación humana.
- Nivel 3: acciones de bajo riesgo autónomas; alto riesgo con aprobación.
- Nivel 4: autonomía acotada por política, confianza, activo, horario y blast radius.
- Registrar prompt/skill o agente, entradas, fuentes, resultado, confianza, versión y decisión humana.

## 9. Patrones de integración con el SIEM OnPrem

El SIEM OnPrem puede coexistir durante varios años con Microsoft Sentinel y con la capa SOAR basada en Logic Apps. La articulación no depende de una marca específica, sino de que el producto exponga mecanismos estables y gobernables para intercambiar alertas, casos, entidades, evidencias y cambios de estado.

El patrón preferido es desacoplar el SIEM OnPrem de los playbooks mediante un contrato canónico y, cuando el volumen o la criticidad lo justifique, una fachada de API o mensajería. Logic Apps recibe o consulta eventos, normaliza los datos, aplica correlación e idempotencia, ejecuta enriquecimientos o respuestas y devuelve al sistema maestro únicamente los cambios autorizados.

Si el SIEM OnPrem no cumple los requisitos obligatorios, no debe conectarse directamente a acciones de respuesta. Debe interponerse un adaptador, API Management, mensajería o un servicio de integración controlado.

- Patrón A: publicar alertas o casos seleccionados hacia la capa Microsoft.
- Patrón B: sincronización bidireccional de estado, propietario, severidad, comentarios, evidencias y vínculos.
- Patrón C: enriquecimiento bajo demanda, consultando detalles solo cuando un caso lo requiere.
- Patrón D: respuesta delegada con confirmación, auditoría, aprobación y rollback.
- Patrón E: broker desacoplado para autenticación, cuotas, transformación, reintentos y cola de errores.
- No replicar indiscriminadamente todos los eventos; priorizar contexto necesario para respuesta.

## 10. Requisitos del SIEM OnPrem para integrarse con la capa SOAR

La matriz siguiente define capacidades mínimas que el SIEM OnPrem debe ofrecer directamente o mediante un adaptador gobernado. Los requisitos obligatorios son condiciones de entrada para integración productiva. Los recomendados pueden aceptarse temporalmente solo con mitigación, responsable y fecha objetivo.

La aceptación debe basarse en evidencia y pruebas reproducibles. La ausencia de una API nativa no invalida el modelo, pero exige una capa de adaptación y aumenta costo, riesgo y responsabilidad operacional.

- Interoperabilidad | Obligatorio | API documentada para leer alertas/casos y detalles por identificador | Evidencia: Especificación y prueba de lectura
- Interoperabilidad | Obligatorio | Mecanismo push: webhook, cola, syslog estructurado o exportación equivalente | Evidencia: Prueba de publicación y recepción
- Interoperabilidad | Obligatorio | Actualización de estado, propietario, severidad y comentarios, nativa o mediante adaptador | Evidencia: Prueba de escritura y lectura posterior
- Modelo de datos | Obligatorio | Identificador único, estable e inmutable por alerta o caso | Evidencia: Muestra de identificadores y regla de persistencia
- Modelo de datos | Obligatorio | Timestamps en UTC para creación, modificación y eventos | Evidencia: Payload y prueba de sincronización horaria
- Modelo de datos | Obligatorio | Severidad, estado, tipo, origen, entidades y evidencias exportables | Evidencia: Diccionario de campos y payload
- Modelo de datos | Recomendado | Versionado de esquema o compatibilidad hacia atrás | Evidencia: Política y prueba de cambio
- Seguridad | Obligatorio | Autenticación de aplicación sin cuentas personales y credenciales rotables | Evidencia: Configuración y prueba de rotación
- Seguridad | Obligatorio | Autorización granular y mínimo privilegio | Evidencia: Matriz de permisos
- Seguridad | Obligatorio | TLS y validación de certificados | Evidencia: Prueba de conexión
- Seguridad | Obligatorio | Allowlist, proxy o gateway compatible con la conectividad híbrida | Evidencia: Diagrama y reglas de red
- Seguridad | Obligatorio | Auditoría de autenticación, cambios, acciones y actor técnico | Evidencia: Logs correlacionados
- Operación | Obligatorio | Cuotas, paginación, límites de API y códigos de error documentados | Evidencia: Documentación y prueba de rate limit
- Operación | Obligatorio | Disponibilidad, mantenimiento, soporte y escalamiento definidos | Evidencia: SLA/SLO y contactos
- Operación | Obligatorio | Reintento, cola o recuperación sin pérdida | Evidencia: Prueba de caída y recuperación
- Operación | Recomendado | Ambiente no productivo o simulación segura | Evidencia: Evidencia de sandbox
- Gobierno | Obligatorio | Propietario técnico y propietario del proceso | Evidencia: RACI aprobado
- Gobierno | Obligatorio | Sistema maestro definido por familia de incidente y campo | Evidencia: Matriz de autoridad
- Gobierno | Obligatorio | Política de retención, clasificación, residencia y minimización | Evidencia: Política aprobada
- Respuesta | Obligatorio | Confirmación de ejecución y resultado de acciones delegadas | Evidencia: Respuesta con estado y timestamp
- Respuesta | Obligatorio | Idempotencia o deduplicación de comandos repetidos | Evidencia: Prueba de replay
- Respuesta | Recomendado | Aprobación, cancelación o rollback en SIEM o capa SOAR | Evidencia: Prueba de control humano
- Observabilidad | Obligatorio | Métricas de latencia, error, volumen y backlog | Evidencia: Dashboard o exportación
- Observabilidad | Recomendado | Health endpoint o prueba sintética | Evidencia: Monitor activo
- Resiliencia | Obligatorio | Comportamiento documentado ante indisponibilidad y eventos fuera de orden | Evidencia: Prueba de resiliencia
- Resiliencia | Recomendado | Alta disponibilidad para componentes críticos | Evidencia: Arquitectura y prueba

## 11. Alcance de licencias y beneficios a validar

M365 E5 aporta capacidades Defender XDR y puede habilitar beneficios específicos de Sentinel y Security Copilot sujetos a elegibilidad y términos vigentes. Defender for Servers Plan 2 aporta protección de servidores y un beneficio documentado de ingestión de datos de seguridad elegibles. Estos beneficios no deben interpretarse como cobertura ilimitada de datos de SIEM OnPrem, de todos los tipos de log ni del costo de Logic Apps.

El assessment debe confirmar asignaciones, tenants, workspaces, medidores de Sentinel, retención, automatizaciones, conectores, consumo de Security Copilot y elegibilidad de cada fuente. Los costos de Logic Apps, conectores, red, APIM, Service Bus, almacenamiento, Log Analytics y retención deben modelarse por escenario.

- Confirmar beneficio de Sentinel asociado a productos Microsoft 365 contratados y su consumo real.
- Confirmar 500 MB/día por nodo de Defender for Servers Plan 2 para tipos de datos elegibles y workspace aplicable.
- Separar beneficio de ingestión, costo de análisis/retención y costo de automatización.
- Crear showback por workflow, sourceSystem y businessService.

## 12. Plan paso a paso para construir o validar

El programa se organiza en fases con entregables y puertas de salida. Si el cliente ya posee automatizaciones, las fases iniciales funcionan como descubrimiento y validación en lugar de despliegue desde cero.

- Fase 0, mandato y gobierno: sponsor, RACI, riesgos, sistemas maestros y criterios de autonomía.
- Fase 1, inventario: SIEM, workspaces, fuentes, casos, playbooks, conectores, identidades, costos y dependencias.
- Fase de entrada SIEM OnPrem: evaluar requisitos obligatorios, evidencias, brechas y decisión go/no-go antes de habilitar escritura o acciones.
- Fase 2, evaluación técnica: permisos, red, APIs, Cases, multi-workspace, SIEM OnPrem, beneficios, observabilidad y transición al portal Defender antes del 31/03/2027.
- Fase 3, contrato canónico: esquema, mapeos, correlación, estados, severidades y modelo de errores.
- Fase 4, plataforma mínima: APIM opcional, Logic Apps, Key Vault, monitoreo, repositorio e IaC.
- Fase 5, tres casos piloto: enriquecimiento no destructivo, sincronización de caso y contención con aprobación.
- Fase 6, validación: pruebas funcionales, seguridad, resiliencia, volumen, costo, rollback y auditoría.
- Fase 7, operación: SLO, runbooks, ownership, soporte, cambios, métricas y revisión mensual.
- Fase 8, agentificación: Copilot para resumen/recomendación y autonomía gradual basada en evidencia.
- Fase 9, racionalización SIEM: decidir qué señales migrar, federar, resumir o retirar sin condicionar el SOAR.

## 13. Casos de uso prioritarios

Los pilotos deben demostrar valor transversal y bajo riesgo antes de automatizar remediaciones irreversibles.

- Enriquecimiento de usuario, IP, URL, host y vulnerabilidad con comentario estructurado.
- Normalización y sincronización de severidad, propietario, estado y vínculos entre sistemas.
- Notificación y colaboración con Teams o ITSM, sin convertir chat en registro maestro.
- Aislamiento de dispositivo o bloqueo de identidad con aprobación y comprobación de criticidad.
- Respuesta a alertas de Defender for Servers P2 con validación de propietario y ventana.
- Resumen y recomendación de Security Copilot con fuentes y revisión humana.
- Reconciliación programada de casos divergentes y cola de fallos.

## 14. Modelo de madurez y assessment

Cada control se puntúa de 0 a 5: 0 inexistente; 1 ad hoc; 2 repetible parcialmente; 3 definido y medido; 4 automatizado y gobernado; 5 optimizado y adaptable. La meta inicial sugerida es alcanzar 3 en gobierno, identidad, auditoría y resiliencia antes de ampliar autonomía.

Los requisitos obligatorios del SIEM OnPrem sin evidencia o con score inferior a 3 bloquean la integración productiva bidireccional y las acciones de respuesta.

- Dominios: estrategia, arquitectura, casos, automatización, integración SIEM OnPrem, identidad, red, datos, IA, DevSecOps, operación, resiliencia, costo y métricas.
- Evidencias: configuración exportada, ejecución de prueba, logs, permisos, diagramas, repositorios, tickets y aprobaciones.
- Resultado: score actual, objetivo, brecha, riesgo, acción, dueño, dependencia, esfuerzo y fecha.

## 15. Controles mínimos de producción

Ningún playbook de alto impacto debe pasar a producción sin controles de autorización, validación, auditoría, rollback y operación.

- Mínimo privilegio y separación de funciones.
- Allowlist/denylist de acciones, activos y fuentes.
- Aprobación adaptativa por impacto, confianza y criticidad.
- Idempotency key y deduplicación.
- Timeout, retry, compensación y dead-letter queue.
- Logs sin secretos y con correlación extremo a extremo.
- Pruebas sintéticas y simulación de API indisponible.
- Rollback probado y contactos de escalamiento.
- Control de cambios, revisión por pares y despliegue automatizado.
- Revisión periódica de conectores, permisos, costos y funcionalidades preview.

## 16. KPIs, KRIs y SLOs

Las métricas deben demostrar reducción de esfuerzo y riesgo, no solo cantidad de automatizaciones.

- Porcentaje de incidentes elegibles procesados.
- Tasa de éxito y de rollback por playbook.
- Tiempo hasta enriquecimiento, decisión y contención.
- Minutos de analista ahorrados, validados por muestreo.
- Falsos positivos/negativos introducidos por automatización.
- Casos divergentes entre sistemas y tiempo de reconciliación.
- Acciones bloqueadas por política o falta de confianza.
- Costo por caso y por workflow.
- Cobertura de trazabilidad y evidencias.
- Incidentes causados o amplificados por automatización.

## 17. Decisiones arquitectónicas obligatorias

Antes del diseño detallado deben resolverse decisiones que cambian materialmente el patrón.

- ¿Cuál es el sistema maestro del caso para cada familia de incidentes?
- ¿Qué señales permanecen solo en SIEM OnPrem y cuáles se incorporan a Sentinel?
- ¿Qué automatizaciones necesitan latencia inmediata y cuáles admiten cola?
- ¿Consumption o Standard por dominio y por qué?
- ¿Se requiere APIM, Service Bus, conectividad privada o gateway on-premises?
- ¿Qué acciones puede ejecutar una identidad administrada y cuáles requieren otro patrón?
- ¿Qué campos y evidencias pueden cruzar fronteras de datos?
- ¿Cuándo Copilot recomienda, cuándo solicita aprobación y cuándo puede actuar?
- ¿Cómo se suspende globalmente la automatización?
- ¿Qué condiciones habilitan retirar un flujo legacy o una dependencia de SIEM OnPrem?

## 18. Blueprint lógico

Flujo de referencia: (1) un SIEM o producto Defender crea o actualiza una señal; (2) un adaptador invoca el endpoint o trigger autorizado; (3) el orquestador valida autenticidad, esquema y duplicados; (4) normaliza y recupera política; (5) realiza enriquecimientos en paralelo; (6) opcionalmente consulta Security Copilot; (7) calcula una recomendación; (8) solicita aprobación si corresponde; (9) ejecuta capacidades modulares; (10) verifica resultado y compensa si falla; (11) actualiza caso maestro y sistemas satélite; (12) registra telemetría, evidencia y costo.

## 19. Riesgos y mitigaciones

El principal riesgo no es técnico sino operativo: crear una nueva capa central que duplique estados y aumente la ambigüedad. La mitigación es definir propiedad, contrato, correlación y reconciliación antes de automatizar.

- Duplicación de casos: identificador global, deduplicación y sistema maestro.
- Bucles SIEM OnPrem–Microsoft: sourceOfTruth, hop count y supresión de eco.
- Permisos excesivos: identidades por capacidad y alcance mínimo.
- Dependencia de preview: aislamiento, feature flags y alternativa GA.
- Costo impredecible: cuotas, muestreo, tagging y presupuesto.
- Alucinación o recomendación incorrecta: fuentes, confianza, aprobación y acciones acotadas.
- Pérdida de evidencia: repositorio inmutable o controles de retención apropiados.
- Falla de conector: colas, reintentos, circuit breaker y operación manual documentada.
- Operación en Azure portal después del 31/03/2027: migrar procedimientos y automatizaciones al portal Defender con anticipación.

## 20. Matriz RACI para requisitos del SIEM OnPrem

La matriz RACI asigna una única responsabilidad de aprobación (A) y, cuando sea posible, una única responsabilidad de ejecución (R) para cada requisito. C identifica a quienes deben participar antes de cerrar la decisión; I identifica a quienes deben recibir el resultado. Los nombres concretos deben reemplazar los roles genéricos durante la fase de gobierno. La RACI no reemplaza los permisos técnicos ni la segregación de funciones.

- Roles considerados: Sponsor/CISO, SOC Manager, Arquitecto de Seguridad/SOAR, Propietario del SIEM OnPrem, Ingeniería del SIEM OnPrem, Ingeniería Sentinel/Defender, Plataforma Cloud/Integración, IAM/PAM, Redes, GRC/Privacidad, Incident Response y Service Management.
- Interoperabilidad y modelo de datos: A = Arquitecto de Seguridad/SOAR; R = Ingeniería del SIEM OnPrem y/o Plataforma de Integración; C = Sentinel/Defender y SOC; I = Sponsor/CISO y Service Management.
- Seguridad, identidad y red: A = Arquitecto de Seguridad/SOAR; R = IAM/PAM, Redes y Plataforma Cloud según el control; C = GRC y equipos SIEM; I = SOC Manager.
- Operación, observabilidad y resiliencia: A = SOC Manager; R = Propietario/Ingeniería del SIEM OnPrem y Plataforma; C = Incident Response y Service Management; I = Sponsor/CISO.
- Gobierno y datos: A = Sponsor/CISO o delegado de riesgo; R = GRC/Privacidad y SOC Manager; C = Arquitectura y propietarios técnicos; I = equipos operativos.
- Respuesta automatizada: A = SOC Manager; R = Incident Response y Plataforma SOAR; C = Arquitectura, IAM y propietario del SIEM OnPrem; I = Sponsor/CISO y Service Management.

## 21. Plan de remediación de requisitos no cumplidos

El plan de remediación se activa cuando Cumple es distinto de Sí o el score es menor que 3. Cada brecha debe conservar el ID del requisito, la evidencia faltante, la causa raíz, la solución objetivo, la mitigación temporal, el dueño, las dependencias, el esfuerzo, la fecha objetivo y el criterio de cierre. Los requisitos obligatorios bloquean el go-live mientras no estén cumplidos o exista una excepción de riesgo formalmente aprobada. Los requisitos recomendados pueden ingresar en backlog si existe mitigación, dueño y fecha.

- Paso 1, confirmar la brecha: reproducir la prueba y adjuntar evidencia; evitar convertir “sin evidencia” en “cumplido”.
- Paso 2, clasificar: Bloqueante si es obligatorio y afecta seguridad, integridad, identidades, auditoría, idempotencia o recuperación; Alta para otros obligatorios; Media o Baja para recomendados según riesgo.
- Paso 3, analizar causa raíz: capacidad inexistente, configuración, proceso, permisos, conectividad, contrato con proveedor, deuda técnica o falta de evidencia.
- Paso 4, seleccionar tratamiento: corregir en el SIEM OnPrem, implementar adaptador controlado, aplicar compensación temporal, aceptar formalmente el riesgo o retirar el patrón afectado.
- Paso 5, diseñar y probar: definir entregable, ambiente, casos positivos y negativos, seguridad, carga, fallo, rollback y criterio de aceptación.
- Paso 6, aprobar y desplegar: seguir control de cambios, actualizar documentación y RACI, habilitar monitoreo y conservar evidencia.
- Paso 7, validar cierre: Cumple = Sí, score mínimo 3, evidencia aceptada y prueba de regresión exitosa. El cierre debe aprobarlo el rol A de la RACI.
- Cadencia sugerida: revisión semanal de bloqueantes y altas; quincenal de medias y bajas; revisión mensual de excepciones de riesgo.
- Orden recomendado de remediación: identidad y seguridad; integridad e idempotencia; interoperabilidad mínima; auditoría y observabilidad; resiliencia; operación; optimizaciones.

## 22. Fuentes oficiales y notas de validación

La guía se basa en documentación oficial de Microsoft consultada para playbooks de Sentinel sobre Logic Apps, reglas de automatización, ejecución desde casos/incidentes/alertas, múltiples workspaces en Defender, case management, incorporación de Sentinel al portal Defender, Defender for Servers Plan 2 y su beneficio de ingestión, coexistencia side-by-side con SIEM heredados, migración desde SIEM OnPrem, playbooks generados y conectores de Security Copilot y Sentinel MCP para Logic Apps. Las capacidades, licencias, previews, APIs y límites deben revalidarse en el tenant y contra la documentación vigente antes de producción.

- Azure Logic Apps for Microsoft Sentinel playbooks: https://learn.microsoft.com/azure/sentinel/automation/logic-apps-playbooks
- Automation in Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/automation/automation
- Automate and run playbooks: https://learn.microsoft.com/azure/sentinel/automation/run-playbooks
- Multiple Sentinel workspaces in Defender portal: https://learn.microsoft.com/azure/sentinel/workspaces-defender-portal
- Case management in Defender portal: https://learn.microsoft.com/defender-xdr/siem-defender-case-management
- Connect Sentinel to Defender portal: https://learn.microsoft.com/azure/sentinel/microsoft-sentinel-onboard
- Defender for Servers data ingestion benefit: https://learn.microsoft.com/azure/defender-for-cloud/data-ingestion-benefit
- Defender for Servers overview: https://learn.microsoft.com/azure/defender-for-cloud/defender-for-servers-overview
- Generate playbooks using AI in Defender portal: https://learn.microsoft.com/defender-xdr/siem-defender-generate-playbooks
- Automation with ISOC in Microsoft Defender: https://learn.microsoft.com/defender-xdr/siem-defender-automation
- Microsoft Sentinel in the Defender portal: https://learn.microsoft.com/azure/sentinel/microsoft-sentinel-defender-portal
- Microsoft Defender multitenant management: https://learn.microsoft.com/defender-xdr/mto-overview
- Deploy Sentinel side-by-side with existing SIEM: https://learn.microsoft.com/azure/sentinel/deploy-side-by-side
- SIEM migration experience: https://learn.microsoft.com/azure/sentinel/siem-migration
- Plan migration to Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/migration
- Security Copilot connector for Logic Apps: https://learn.microsoft.com/copilot/security/connector-logicapp
- Sentinel MCP for Logic Apps: https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-logic-apps

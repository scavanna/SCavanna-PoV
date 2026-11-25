# Evaluaciones y respuestas

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿A partir de qué fecha Microsoft Sentinel deja de estar soportado en el portal de Azure?**

- a) 1 de julio de 2025
- b) 1 de julio de 2026
- c) 31 de marzo de 2027  ✅
- d) 31 de diciembre de 2027

*Respuesta: c).* El anuncio del 29 de enero de 2026 extendió la fecha original (1 de julio de 2026) al 31 de marzo de 2027. [Fuente](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué se requiere para usar Microsoft Sentinel en el portal de Defender?**

- a) Licencia Microsoft 365 E5 obligatoria
- b) Tener Defender XDR desplegado
- c) Un workspace con Sentinel habilitado y los roles adecuados  ✅
- d) Una licencia de Security Copilot

*Respuesta: c).* No se requiere Defender XDR ni E5 para usar Sentinel en el portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**3. ¿Qué incluye la prueba gratuita de Sentinel?**

- a) 5 GB/día durante 30 días
- b) 10 GB/día en el nivel de analítica durante 31 días  ✅
- c) 100 GB/día durante 14 días
- d) Ingesta ilimitada durante 90 días

*Respuesta: b).* La prueba cubre 10 GB/día en el nivel de analítica durante 31 días, con un límite de 20 workspaces por tenant. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/billing) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. ¿Cuál es el beneficio de ingesta para clientes de Microsoft 365 E5, E7, A5, F5 y G5?**

- a) 5 GB por usuario al mes
- b) Hasta 5 MB por usuario por día de datos de Microsoft 365 elegibles  ✅
- c) 10 GB por día por tenant
- d) No existe beneficio

*Respuesta: b).* La oferta otorga hasta 5 MB por usuario por día de ingesta de datos de Microsoft 365 elegibles. [Fuente](https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. Un analista debe asignarse incidentes y cambiar su estado, pero no crear reglas. ¿Qué rol mínimo necesita?**

- a) Microsoft Sentinel Reader
- b) Microsoft Sentinel Responder  ✅
- c) Microsoft Sentinel Contributor
- d) Owner

*Respuesta: b).* Responder suma a los permisos de Reader la gestión de incidentes. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/roles) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**6. ¿Qué rol se necesita para instalar o actualizar soluciones del Content hub?**

- a) Sentinel Reader en el workspace
- b) Sentinel Responder en la suscripción
- c) Sentinel Contributor en el grupo de recursos  ✅
- d) Logic App Contributor

*Respuesta: c).* Instalar soluciones requiere Microsoft Sentinel Contributor a nivel de grupo de recursos. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-deploy) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**7. Al incorporar un workspace de Sentinel al portal de Defender, el conector de Microsoft Defender XDR…**

- a) Debe configurarse siempre de forma manual
- b) Se habilita automáticamente  ✅
- c) No está soportado
- d) Requiere un playbook de Logic Apps

*Respuesta: b).* El conector se habilita automáticamente durante la incorporación al portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. ¿Qué operador de KQL filtra filas según una condición?**

- a) project
- b) summarize
- c) where  ✅
- d) extend

*Respuesta: c).* where filtra filas; project elige columnas; extend agrega columnas calculadas; summarize agrega. [Fuente](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference?view=microsoft-fabric) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**9. ¿Cuál es el equivalente en KQL de GROUP BY en SQL?**

- a) summarize … by  ✅
- b) join
- c) distinct
- d) top

*Respuesta: a).* summarize con la cláusula by agrupa y agrega, como GROUP BY. [Fuente](https://learn.microsoft.com/en-us/kusto/query/sql-cheat-sheet?view=microsoft-fabric) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**10. ¿Cuándo alcanzó disponibilidad general el data lake de Microsoft Sentinel?**

- a) 22 de julio de 2025
- b) 30 de septiembre de 2025  ✅
- c) 29 de enero de 2026
- d) 31 de marzo de 2027

*Respuesta: b).* Julio de 2025 fue la vista previa pública; la disponibilidad general llegó el 30 de septiembre de 2025. [Fuente](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**11. En las habilidades del SC-200 vigentes desde el 21 de octubre de 2026, ¿qué dominio tiene mayor peso?**

- a) Realizar búsqueda de amenazas
- b) Responder a incidentes de seguridad
- c) Gestionar un entorno de operaciones de seguridad  ✅
- d) Todos pesan igual

*Respuesta: c).* Gestionar el entorno de operaciones de seguridad pesa entre 40 y 45 %. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**12. ¿Qué requisito tiene el nuevo Microsoft Sentinel Training Lab?**

- a) Un clúster dedicado de 500 GB/día
- b) Un workspace incorporado al portal de Defender como principal  ✅
- c) Una licencia de Security Copilot
- d) Un tenant de proveedor CSP

*Respuesta: b).* El laboratorio requiere un workspace conectado al portal de Defender como workspace principal. [Fuente](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/README.md) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Arquitectura, datos, detección y operación

**1. En el portal de Defender, ¿cuál es el modelo de workspaces de Sentinel por tenant?**

- a) Hasta cinco principales
- b) Uno principal y secundarios ilimitados  ✅
- c) Un único workspace
- d) Uno principal y diez secundarios

*Respuesta: b).* Cada tenant tiene un workspace principal, que es el único correlacionado con Defender XDR, y secundarios ilimitados. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. Para un workspace en una región de Latinoamérica fuera de Brasil, ¿dónde procesa Sentinel los datos de cliente según la documentación de residencia?**

- a) En la misma región del workspace
- b) En Brasil
- c) En una región de EE. UU.  ✅
- d) En Europa

*Respuesta: c).* Los workspaces fuera de Europa e Israel procesan datos de cliente en una región de EE. UU. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/geographical-availability-data-residency) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. Los eventos recolectados con Windows Event Forwarding se escriben en la tabla…**

- a) SecurityEvent
- b) WindowsEvent  ✅
- c) Event
- d) CommonSecurityLog

*Respuesta: b).* WEF escribe en WindowsEvent, por lo que muchas reglas integradas basadas en SecurityEvent requieren adaptación. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-windows-based) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**4. ¿Cuál es la situación de la HTTP Data Collector API a noviembre de 2026?**

- a) Recomendada para conectores nuevos
- b) Fin de soporte el 14 de septiembre de 2026; migrar a Logs Ingestion API o CCF  ✅
- c) Retirada junto con MMA en 2024
- d) Reemplazada por Logstash

*Respuesta: b).* Su soporte terminó el 14 de septiembre de 2026; la ruta es la API de ingesta de logs o CCF. [Fuente](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**5. Una transformación split configurada en Table management…**

- a) Elimina los datos que no cumplen la condición
- b) Envía lo que cumple la condición a analítica y el resto solo al data lake  ✅
- c) Solo funciona en el portal de Azure
- d) Solo aplica a tablas Basic

*Respuesta: b).* Split divide el flujo entre el nivel de analítica y el data lake según una condición KQL. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/transformation-filter-split) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**6. ¿Qué tablas reemplazan a ThreatIntelligenceIndicator?**

- a) ThreatIntelIndicators y ThreatIntelObjects  ✅
- b) TIIndicators_CL
- c) SecurityIoC
- d) ThreatIntelligenceIndicatorV2

*Respuesta: a).* Las nuevas tablas almacenan indicadores y objetos STIX; la tabla heredada dejó de recibir datos en agosto de 2025. [Fuente](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/table-talk-sentinel%E2%80%99s-new-threatintel-tables-explained/4440273) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**7. ¿Qué prerrequisito tiene la experiencia de migración de SIEM del portal de Defender?**

- a) Licencia de Splunk Enterprise Security
- b) Security Copilot habilitado en el tenant, sin consumo de SCU  ✅
- c) Logic Apps Standard
- d) Un workspace en el portal de Azure

*Respuesta: b).* Requiere Security Copilot habilitado, pero la experiencia de migración no consume unidades de cómputo de seguridad. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**8. ¿Con qué frecuencia y con qué retraso se ejecutan las reglas NRT de analítica?**

- a) Cada 5 minutos, con 5 minutos de retraso
- b) Cada minuto, con 2 minutos de retraso  ✅
- c) Cada minuto, sin retraso
- d) Cada 15 minutos, con 2 minutos de retraso

*Respuesta: b).* Las reglas NRT de analítica se ejecutan cada minuto con un retraso de 2 minutos y tienen un máximo de 50 por cliente. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/near-real-time-rules) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**9. Al incorporar un workspace al portal de Defender, ¿qué ocurre con Fusion?**

- a) Sigue activo
- b) Pasa a vista previa
- c) Se deshabilita y lo reemplaza la correlación de Defender XDR  ✅
- d) Se convierte en una detección personalizada

*Respuesta: c).* En el portal de Defender, el motor de correlación de Defender XDR reemplaza a Fusion. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/fusion) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**10. ¿Qué tabla de supervisión NO se factura?**

- a) SentinelAudit
- b) SentinelHealth  ✅
- c) Ambas
- d) Ninguna

*Respuesta: b).* SentinelHealth no se factura; SentinelAudit sí. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/health-audit) · Repasa [M12](02_Nivel_2_Intermedio.md#m12)

**11. ¿Por qué se usa arg_max() al calcular métricas con la tabla SecurityIncident?**

- a) Para ordenar por severidad
- b) Porque cada actualización del incidente crea un registro nuevo  ✅
- c) Para unir con SecurityAlert
- d) Para reducir costos

*Respuesta: b).* Hay que quedarse con el último registro de cada incidente antes de calcular métricas. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Repasa [M9](02_Nivel_2_Intermedio.md#m9)

**12. ¿Dónde se pueden crear marcadores de hunting?**

- a) Solo en el portal de Defender
- b) En la búsqueda avanzada
- c) Solo en el portal de Azure  ✅
- d) En ambos portales

*Respuesta: c).* Defender muestra los marcadores, pero solo se crean en el portal de Azure; la búsqueda avanzada no tiene marcadores. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/bookmarks) · Repasa [M10](02_Nivel_2_Intermedio.md#m10)

**13. En 2026, ¿cuál es la experiencia recomendada para gestionar incidentes en el portal de Defender?**

- a) La integración con Teams
- b) Los incident cases (vista previa)  ✅
- c) Los libros
- d) Los hunts

*Respuesta: b).* Los incident cases agregan tareas, SLA, campos personalizados, adjuntos y auditoría. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management) · Repasa [M9](02_Nivel_2_Intermedio.md#m9)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Ingeniería de plataforma y contenido

**1. ¿Qué capacidad tienen las detecciones personalizadas y NO las reglas de analítica?**

- a) Supresión de alertas
- b) Acciones de respuesta nativas de Defender XDR  ✅
- c) Alertas sin incidente
- d) Agrupación personalizada de alertas

*Respuesta: b).* Las detecciones personalizadas incluyen acciones de remediación nativas de XDR; supresión, alertas sin incidente y agrupación personalizada siguen siendo exclusivas de las reglas de analítica. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/compare-analytics-rules-custom-detections) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**2. ¿Qué parámetro de un parser ASIM agrupa los campos no normalizados en AdditionalFields?**

- a) extra
- b) pack  ✅
- c) raw
- d) bag

*Respuesta: b).* El parámetro pack empaqueta los campos adicionales de la fuente. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-parsers) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. Según la guía actual para desarrollar parsers ASIM, ¿qué operador está prohibido?**

- a) where
- b) project-rename
- c) mv-expand  ✅
- d) extend

*Respuesta: c).* Los parsers deben limitarse a operaciones locales por registro: sin joins, watchlists, externaldata, mv-expand ni summarize. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/isv/normalization-develop-parsers) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. En series_decompose_anomalies, ¿cuáles son el umbral y la estacionalidad por defecto?**

- a) 3,0 y 0
- b) 1,5 y autodetección  ✅
- c) 2,5 y 24
- d) 1,0 y 168

*Respuesta: b).* El umbral por defecto es 1,5 y la estacionalidad se autodetecta (-1). [Fuente](https://learn.microsoft.com/en-us/kusto/query/series-decompose-anomalies-function?view=microsoft-fabric) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**5. ¿Qué recurso usa Sentinel Repositories para desplegar detecciones personalizadas como código?**

- a) Microsoft.SecurityInsights/alertRules con ARM
- b) Microsoft.Security/detectionRules con la extensión Bicep MicrosoftSecurity  ✅
- c) Microsoft.Insights/scheduledQueryRules con Terraform
- d) Microsoft.OperationalInsights/savedSearches

*Respuesta: b).* Las detecciones personalizadas se declaran como Microsoft.Security/detectionRules con la extensión Bicep MicrosoftSecurity. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**6. ¿Cuántas conexiones de repositorio admite un workspace de Sentinel?**

- a) 1
- b) 3
- c) 5  ✅
- d) 10

*Respuesta: c).* El límite actual es de cinco conexiones de repositorio por workspace. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**7. Un ISV quiere enviar eventos en tiempo casi real sin exponer una API para sondeo. ¿Qué modelo conviene?**

- a) CCF de sondeo
- b) CCF Push sobre la API de ingesta de logs  ✅
- c) HTTP Data Collector API desde una Azure Function
- d) Conector Logstash

*Respuesta: b).* CCF Push aprovisiona app de Entra, DCR, DCE y tabla para que la aplicación envíe eventos. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-push-codeless-connector) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**8. Una integración de tickets usa GET /security/alerts de Microsoft Graph. ¿Qué corresponde hacer?**

- a) Nada, la API es estable
- b) Migrar a /security/alerts_v2 e /security/incidents  ✅
- c) Migrar a la API de Defender for Endpoint
- d) Volver a Az.SecurityInsights 1.x

*Respuesta: b).* El endpoint heredado se retiró el 15 de octubre de 2026. [Fuente](https://learn.microsoft.com/en-us/graph/alertsv1-alertsv2-migration) · Repasa [A6](03_Nivel_3_Avanzado.md#a6)

**9. Un KQL job crea una tabla en el nivel de analítica. ¿Qué sufijo recibe y qué permiso adicional requiere?**

- a) _CL; Sentinel Contributor para el usuario
- b) _KQL_CL; Log Analytics Contributor para la identidad administrada del lago  ✅
- c) _SRCH; Owner de la suscripción
- d) _KQL; Monitoring Metrics Publisher

*Respuesta: b).* Las tablas de salida usan el sufijo _KQL_CL y la identidad administrada del lago necesita Log Analytics Contributor. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs) · Repasa [A8](03_Nivel_3_Avanzado.md#a8)

**10. Sobre los grafos personalizados de Sentinel, ¿qué afirmación es correcta?**

- a) Un graph job bajo demanda materializa el grafo 30 días y uno programado lo reconstruye  ✅
- b) Los grafos de una sesión interactiva se guardan solos
- c) Se consultan con SQL estándar
- d) No generan costos

*Respuesta: a).* Los graph jobs bajo demanda duran 30 días; los programados se reconstruyen según su calendario. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/custom-graphs-overview) · Repasa [A8](03_Nivel_3_Avanzado.md#a8)

**11. En la gestión multi-inquilino de Defender sin Azure Lighthouse, ¿qué workspaces se pueden consultar?**

- a) Todos los de todos los tenants
- b) Solo el workspace principal de cada tenant  ✅
- c) Ninguno
- d) Solo los de la suscripción del MSSP

*Respuesta: b).* Para workspaces secundarios de otros tenants se requiere Azure Lighthouse. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Repasa [A9](03_Nivel_3_Avanzado.md#a9)

**12. ¿En qué fechas se retiró el agente SAP en contenedor y se eliminaron sus imágenes?**

- a) 31 de marzo de 2027 y 30 de junio de 2027
- b) 14 de septiembre de 2026 y 14 de octubre de 2026  ✅
- c) 1 de julio de 2025 y 1 de julio de 2026
- d) 18 de agosto de 2026 y 31 de diciembre de 2026

*Respuesta: b).* La ruta vigente es el conector sin agente. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/sap/sap-agent-migrate) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

<a id="eval-experto"></a>

## Nivel 4 · Experto agéntico · SOAR avanzado, Security Copilot, agentes y MCP

**1. ¿Qué rol necesita la cuenta de servicio de Sentinel sobre el grupo de recursos del playbook para que una regla de automatización lo ejecute?**

- a) Logic App Contributor
- b) Microsoft Sentinel Automation Contributor  ✅
- c) Microsoft Sentinel Responder
- d) Reader

*Respuesta: b).* Sin ese permiso el playbook aparece deshabilitado en el selector de la regla. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**2. La regla 1 (incidente creado) baja la severidad de media a baja; la regla 2, posterior, solo aplica a severidad media o mayor. ¿Qué ocurre?**

- a) La regla 2 se ejecuta porque evalúa el estado original
- b) La regla 2 no se ejecuta porque evalúa el estado ya modificado  ✅
- c) Ambas corren en paralelo
- d) Se produce un error de conflicto

*Respuesta: b).* Las reglas corren en secuencia y cada una evalúa el incidente tal como lo dejaron las anteriores. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**3. ¿Qué disparador de playbook NO puede invocarse desde una regla de automatización?**

- a) Incidente
- b) Alerta
- c) Entidad  ✅
- d) Todos pueden invocarse

*Respuesta: c).* El disparador de entidad solo admite ejecución manual. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automation/playbook-triggers-actions) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**4. Un playbook en Logic Apps Standard con private endpoint falla cada vez que Sentinel intenta ejecutarlo. ¿Qué falta con mayor probabilidad?**

- a) Application Insights
- b) Una política de restricción de acceso que permita a Sentinel invocar el flujo  ✅
- c) Convertir el flujo a stateless
- d) Instalarlo desde el Content hub

*Respuesta: b).* Con private endpoint hay que permitir explícitamente que Sentinel invoque el flujo. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automation/logic-apps-playbooks) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**5. La identidad administrada de un playbook debe agregar comentarios y cambiar el estado de incidentes. ¿Qué rol mínimo necesita?**

- a) Microsoft Sentinel Reader
- b) Microsoft Sentinel Responder  ✅
- c) Owner
- d) Logic App Operator

*Respuesta: b).* Responder permite escribir en incidentes; Reader alcanza solo si el playbook lee. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**6. Con Sentinel en el portal de Defender, un incidente recibe cuatro cambios en seis minutos. ¿Qué recibe la automatización?**

- a) Cuatro actualizaciones
- b) Una sola actualización con el cambio más reciente  ✅
- c) Ninguna
- d) Dos actualizaciones agrupadas

*Respuesta: b).* Los cambios dentro de una ventana de 5 a 10 minutos se agrupan y los estados intermedios se pierden. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules) · Repasa [X1](04_Nivel_4_Experto_agentico.md#x1)

**7. ¿Qué método de autenticación documenta oficialmente el conector de Security Copilot para Logic Apps?**

- a) Identidad administrada
- b) OAuth delegado (Authorization Code) de un usuario con acceso a Security Copilot  ✅
- c) Clave de API
- d) Ninguno

*Respuesta: b).* El usuario de la conexión necesita acceso a Security Copilot y a los datos consultados. [Fuente](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Repasa [X3](04_Nivel_4_Experto_agentico.md#x3)

**8. En la acción Submit a Security Copilot prompt, ¿qué parámetro permite saltear el planificador e invocar una habilidad concreta?**

- a) Session ID
- b) Plugins
- c) Direct Skill Name  ✅
- d) Prompt Content

*Respuesta: c).* Las Direct Skills son más rápidas y suelen consumir menos SCU. [Fuente](https://learn.microsoft.com/en-us/copilot/security/connector-logicapp) · Repasa [X3](04_Nivel_4_Experto_agentico.md#x3)

**9. Una organización con 2.500 licencias elegibles de Microsoft 365 E5, ¿cuántas SCU mensuales recibe por la inclusión?**

- a) 400
- b) 1.000  ✅
- c) 2.500
- d) 10.000

*Respuesta: b).* Son 400 SCU por cada 1.000 licencias, de forma proporcional y con tope de 10.000. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [X2](04_Nivel_4_Experto_agentico.md#x2)

**10. ¿Qué colección del servidor MCP de Sentinel permite listar incidentes y ejecutar consultas de búsqueda avanzada?**

- a) Exploración de datos
- b) Triage  ✅
- c) Creación de agentes de Security Copilot
- d) Grafo

*Respuesta: b).* La colección de triage expone incidentes, alertas y consultas de búsqueda avanzada. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-triage-tool) · Repasa [X6](04_Nivel_4_Experto_agentico.md#x6)

**11. ¿Qué rol mínimo permite crear herramientas MCP personalizadas a partir de consultas guardadas?**

- a) Security Reader
- b) Global Reader
- c) Security Operator  ✅
- d) Microsoft Sentinel Reader

*Respuesta: c).* Crear requiere Security Operator, Security Administrator o Global Administrator; usar requiere Security Reader. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-create-custom-tool) · Repasa [X6](04_Nivel_4_Experto_agentico.md#x6)

**12. El Security Alert Triage Agent es…**

- a) Un agente de partner del Security Store
- b) El Phishing Triage Agent ampliado a más tipos de alerta  ✅
- c) Un plugin de Logic Apps
- d) Un agente de Purview

*Respuesta: b).* Es el mismo agente con capacidades extendidas: correo en GA y nube e identidad en vista previa. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/security-alert-triage-agent) · Repasa [X5](04_Nivel_4_Experto_agentico.md#x5)

**13. ¿Cuál de estos NO es un destino válido para un plugin KQL de Security Copilot?**

- a) Sentinel
- b) SentinelDataLake
- c) Kusto
- d) Purview  ✅

*Respuesta: d).* Los destinos admitidos son Sentinel, SentinelDataLake, LogAnalytics, Defender y Kusto. [Fuente](https://learn.microsoft.com/en-us/copilot/security/plugin-kql) · Repasa [X4](04_Nivel_4_Experto_agentico.md#x4)

**14. Al desarrollar un agente personalizado, ¿qué actividad consume SCU?**

- a) Crearlo con el agent builder
- b) Crearlo con NL2Agent vía MCP
- c) Probarlo  ✅
- d) Publicarlo

*Respuesta: c).* Crear y publicar no consumen SCU; probar siempre consume. [Fuente](https://learn.microsoft.com/en-us/copilot/security/developer/cost-considerations) · Repasa [X5](04_Nivel_4_Experto_agentico.md#x5)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Laboratorio y práctica en producción

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md) · [Índice del programa](README.md) · [Cierre, glosario y fuentes →](08_Cierre_glosario_y_fuentes.md)

Este archivo responde tres preguntas para este programa: qué puedes practicar en el entorno de laboratorio, qué requiere producción (y por qué), y cómo hacerlo con riesgo controlado. La guía para construir el entorno con los créditos de Azure de Visual Studio Enterprise y una prueba de Microsoft 365 E5 está en el [anexo común](../Anexo_Entorno_de_practica.md).

**Tenant y suscripción de laboratorio.** Nunca practiques con datos de producción ni de clientes sin autorización. Usa una suscripción propia con la cuenta gratuita de Azure o una suscripción de pruebas, y configura un presupuesto con alertas desde el primer día.

**Sentinel.** La prueba gratuita cubre 10 GB/día durante 31 días en el nivel de analítica. Conecta el workspace al portal de Defender como principal, porque el Training Lab y muchas funciones nuevas lo requieren.

**Datos de práctica.** El Microsoft Sentinel Training Lab carga datos pregrabados y 17 ejercicios; para KQL puro, el clúster gratuito de Azure Data Explorer y Kusto Detective Agency no requieren suscripción.

**Costos a vigilar.** Consultas y cómputo del data lake, ejecuciones de Logic Apps, el plan de Logic Apps Standard y las SCU de Security Copilot. Si tu tenant tiene Microsoft 365 E5, la inclusión de Security Copilot puede cubrir la práctica; si aprovisionas SCU, recuerda que se cobran por hora y desaprovisiona al terminar.

**Limpieza.** Al terminar cada nivel, elimina lo que no vayas a reutilizar. Un laboratorio barato y desechable es la mejor inversión de esta ruta.

<a id="matriz-laboratorio"></a>

## Matriz de laboratorio y producción

| Capacidad | ¿Laboratorio? | Requisito o limitación | Cómo practicar en producción | Riesgo | Mitigación | Fuente |
|---|---|---|---|---|---|---|
| Incorporar el workspace de Sentinel al portal de Defender | Sí | Suscripción de Azure en el mismo inquilino; la prueba de 31 días cubre 10 GB/día del nivel de análisis. | Incorporar en ventana de cambio tras inventariar reglas de automatización y conectores que dependen del portal de Azure. | Reglas de automatización o conectores que cambian de comportamiento al unificar. | Probar primero con un workspace secundario y documentar la reversión. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) |
| Reglas programadas y detecciones personalizadas desde plantillas | Sí | Con poca telemetría algunas reglas no disparan; usa simulaciones y datos del Training Lab. | Crear la regla deshabilitada o con severidad informativa y revisar resultados una semana. | Ruido o incidentes masivos. | Umbrales conservadores, agrupación de alertas y revisión por pares antes de activar. | [Fuente](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) |
| Hunting por hipótesis y cobertura MITRE | Parcial | Los datos del laboratorio son escasos; el Training Lab aporta registros pregrabados de terceros. | Ejecutar consultas de solo lectura sobre datos reales con rol de lector. | Consultas costosas o exposición de datos personales. | Rol Microsoft Sentinel Reader, ventanas de tiempo acotadas y registro de las búsquedas. | [Fuente](https://github.com/Azure/Azure-Sentinel/tree/master/Tools/Microsoft-Sentinel-Training-Lab) |
| Reenviador Syslog/CEF con el agente de Azure Monitor | Sí | VM Linux con créditos de Azure; enciéndela solo durante el ejercicio. | Desplegar un DCR piloto con filtros por facility y severidad para una sola fuente. | Ingesta excesiva y costo inesperado. | Límite diario, transformaciones de ingesta y revisión de la tabla Usage a las 48 h. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-cef-syslog-ama) |
| Niveles de datos, data lake y KQL jobs | Parcial | Los medidores del data lake se cobran incluso durante la prueba gratuita. | Mover al lake una tabla piloto de bajo valor y medir costo y uso durante un mes. | Perder capacidad de detección si se mueve una tabla usada por reglas. | Revisar dependencias de reglas antes de cambiar el nivel y conservar el análisis 90 días. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview) |
| Grafos personalizados y notebooks del data lake | Parcial | Se cobran por hora de cómputo; construir un grafo usa 49 vCores. | Prototipar en el laboratorio y llevar a producción solo el grafo aprobado. | Costo elevado por ejecuciones repetidas. | Presupuesto específico, ejecuciones bajo demanda y borrado de grafos de prueba. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/create-custom-graphs) |
| UEBA y capa de comportamientos | No | Necesita semanas de datos reales de usuarios y fuentes compatibles. | Activar en producción y usar los resultados solo para enriquecer, no para bloquear. | Falsos positivos que generan acciones injustas. | Periodo de observación, validación con el equipo de identidad y privacidad. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/entity-behaviors-layer) |
| SOC optimization y valor de los datos | No | Solo considera tablas facturables con ingesta en los últimos 30 días. | Revisar recomendaciones en producción y aplicar una por vez. | Desactivar datos necesarios para investigaciones. | Registro del cambio, validación con hunting y reversión de la configuración de la tabla. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference) |
| Niveles de compromiso y modelado de costos | No | Empiezan en 50 GB/día (promoción) o 100 GB/día y dependen del volumen real. | Modelar con la tabla Usage de producción antes de comprometerse. | Comprometer capacidad que no se usa durante 31 días. | Analizar tres meses de consumo y empezar por el nivel inferior. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/billing) |
| Multiinquilino para MSSP (GDAP, Lighthouse, perfiles de distribución) | No | Requiere dos o más inquilinos con relación delegada. | Piloto con un inquilino secundario y roles de solo lectura. | Permisos delegados excesivos. | URBAC de mínimo privilegio, revisión de acceso trimestral y registro de cambios. | [Fuente](https://learn.microsoft.com/en-us/defender-xdr/mto-distribution-profiles) |
| Detección como código con Repositories | Sí | La vista previa requiere workspace incorporado al portal de Defender y Owner del grupo de recursos. | Conectar el repositorio primero a un workspace no productivo y exigir pull requests. | El repositorio sobrescribe cambios hechos en el portal. | Rama protegida, revisión por pares y despliegue por etapas. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/ci-cd-custom-content) |
| Playbooks con identidad administrada | Sí | Logic Apps de Consumo con créditos; no habilites Application Insights (excluido del crédito). | Desplegar con permisos mínimos y aprobación humana para acciones destructivas. | Acciones automáticas sobre activos críticos. | Tarjeta de aprobación, exclusión de activos críticos y reversión probada. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel) |
| Servidor MCP de Sentinel y entity analyzer | Parcial | El servidor no tiene costo, pero las consultas al lake se cobran y el entity analyzer consume SCU. | Usar con incidentes reales en un grupo piloto de analistas. | Consumo de SCU y consultas costosas. | Roles de lectura, presupuesto del lake y revisión del panel de uso de SCU. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started) |
| Migración desde otro SIEM | No | Requiere reglas y playbooks reales del SIEM de origen. | Ejecutar la experiencia de migración con un subconjunto de reglas en paralelo. | Pérdida de cobertura durante la transición. | Operación en paralelo, comparación de alertas y criterios de salida. | [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration) |

## Principios para practicar en producción

1. **Primero observar, después actuar.** Usa los modos de solo informe, auditoría o simulación antes de cualquier bloqueo o acción automática.
2. **Alcance mínimo.** Grupos piloto, usuarios y dispositivos de prueba etiquetados, unidades administrativas y ámbitos adaptables pequeños.
3. **Privilegio justo a tiempo.** Roles de solo lectura para estudiar y activación con PIM, aprobación y justificación para cambiar.
4. **Cuentas de emergencia excluidas y monitoreadas.** Nunca practiques acceso condicional o protección de identidad sin cuentas de emergencia probadas.
5. **Cambio registrado y reversible.** Cada práctica tiene responsable, ventana, criterio de éxito, plan de reversión y limpieza al terminar.
6. **Privacidad y áreas de negocio.** Para riesgo interno, comunicaciones o eDiscovery, acuerda con RR. HH., Legal y privacidad antes de crear políticas, aunque sean de prueba.

<a id="ejercicios"></a>

## Índice de ejercicios

Resumen: Laboratorio: 105, Laboratorio parcial: 30, Solo producción: 4, Sin etiqueta: 6.

| Módulo | N.º | Entorno | Ejercicio |
|---|---|---|---|
| [P0](01_Nivel_1_Inicial.md#p0) | 1 | Laboratorio | Repasa la ruta de aprendizaje de SC-900 o, como mínimo, sus módulos sobre Sentinel y Defender XDR (certificación SC-900). |
| [P0](01_Nivel_1_Inicial.md#p0) | 2 | Laboratorio | Crea una suscripción de laboratorio con la cuenta gratuita de Azure y define de inmediato una alerta de presupuesto. |
| [P0](01_Nivel_1_Inicial.md#p0) | 3 | Laboratorio | Recorre el tutorial de Log Analytics: abre una tabla, filtra por tiempo y cambia entre el modo simple y el modo KQL. |
| [P0](01_Nivel_1_Inicial.md#p0) | 4 | Laboratorio | En tu tenant de prueba, identifica qué roles de Entra ID y de Azure tienes asignados y en qué ámbito. |
| [I0](01_Nivel_1_Inicial.md#i0) | 1 | Laboratorio | Lee la guía de estudio de SC-200 y marca, por cada habilidad medida, el módulo de esta guía que la cubre. |
| [I0](01_Nivel_1_Inicial.md#i0) | 2 | Laboratorio | Suscríbete a los eventos virtuales de la Security Community y al blog de Sentinel en Tech Community. |
| [I0](01_Nivel_1_Inicial.md#i0) | 3 | Laboratorio | Agenda el knowledge check del Ninja oficial para cuando termines el nivel intermedio. |
| [I1](01_Nivel_1_Inicial.md#i1) | 1 | Laboratorio | Lee Sentinel en el portal de Defender y anota cinco diferencias con la experiencia del portal de Azure. |
| [I1](01_Nivel_1_Inicial.md#i1) | 2 | Laboratorio | Con la página de precios y el artículo de facturación, estima el costo mensual de un escenario de 50 GB/día con el beneficio de Microsoft 365 E5 y las fuentes gratuitas. |
| [I1](01_Nivel_1_Inicial.md#i1) | 3 | Laboratorio | Explica en un párrafo, como si fuera para un CISO, qué aportan el data lake, el graph y el servidor MCP. |
| [I2](01_Nivel_1_Inicial.md#i2) | 1 | Laboratorio | Dibuja la arquitectura actual de tu organización o de un cliente y marca qué patrón aplica: SIEM principal, SIEM + XDR, multinube, lado a lado o MSSP. |
| [I2](01_Nivel_1_Inicial.md#i2) | 2 | Laboratorio | Si conviven dos SIEM, define el flujo de alertas recomendado y los criterios para dar por terminada la convivencia (lado a lado). |
| [I3](01_Nivel_1_Inicial.md#i3) | 1 | Laboratorio | Sigue el quickstart completo con la solución Azure Activity hasta ver tu primera consulta en la búsqueda avanzada. |
| [I3](01_Nivel_1_Inicial.md#i3) | 2 | Laboratorio | Conecta el workspace al portal de Defender como workspace principal (onboarding) y verifica que el conector de Defender XDR quedó activo. |
| [I3](01_Nivel_1_Inicial.md#i3) | 3 | Laboratorio | Instala la solución de Microsoft Entra ID desde el Content hub y habilita los registros de auditoría (y de inicio de sesión si tienes P1 o P2). |
| [I3](01_Nivel_1_Inicial.md#i3) | 4 | Laboratorio | Activa cinco reglas de plantilla relevantes para tus conectores y revisa cómo cambia la cobertura en la página de MITRE ATT&CK. |
| [I3](01_Nivel_1_Inicial.md#i3) | 5 | Laboratorio | Asigna roles por grupos: Responder para analistas y Contributor para ingenieros, siguiendo roles y permisos. |
| [I3](01_Nivel_1_Inicial.md#i3) | 6 | Laboratorio | Recorre la guía de despliegue y su lista de verificación posterior. |
| [I4](01_Nivel_1_Inicial.md#i4) | 1 | Laboratorio | Escribe cinco consultas sobre `SigninLogs` o `AzureActivity`: fallos por aplicación, IP distintas por usuario, operaciones por hora, top 10 de llamadores y una visualización con `render timechart`. |
| [I4](01_Nivel_1_Inicial.md#i4) | 2 | Laboratorio | Traduce tres consultas SQL que conozcas con la hoja de equivalencias SQL a KQL. |
| [I4](01_Nivel_1_Inicial.md#i4) | 3 | Laboratorio | Resuelve al menos un caso de Kusto Detective Agency. |
| [I4](01_Nivel_1_Inicial.md#i4) | 4 | Laboratorio | Toma una regla de plantilla, lee su consulta línea por línea y explica qué detecta. |
| [I5](01_Nivel_1_Inicial.md#i5) | 1 | Laboratorio | Despliega el Training Lab y completa los primeros cuatro ejercicios. |
| [I5](01_Nivel_1_Inicial.md#i5) | 2 | Laboratorio | Completa los laboratorios de SC-200 de KQL, despliegue, conectores, detecciones y hunting. |
| [I5](01_Nivel_1_Inicial.md#i5) | 3 | Laboratorio | Configura un presupuesto con alerta al 50 % y al 80 %, y al terminar elimina el grupo de recursos del laboratorio. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 1 | Laboratorio | Aplica el árbol de decisión de workspaces a un caso: un banco con operación en tres países y dos tenants de Entra. Documenta cada decisión y su justificación. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 2 | Laboratorio | En el laboratorio, conecta un workspace secundario y verifica qué funciones quedan limitadas al principal. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 3 | Laboratorio | Activa el RBAC unificado para Sentinel en un workspace de prueba y crea un rol personalizado para analistas. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 4 | Laboratorio parcial | Opcional: crea un Sentinel scope para un SOC regional y valida que sus analistas solo vean sus filas. |
| [M2](02_Nivel_2_Intermedio.md#m2) | 1 | Laboratorio | Clasifica diez conectores de tu entorno por método de ingesta usando la referencia de conectores. |
| [M2](02_Nivel_2_Intermedio.md#m2) | 2 | Laboratorio | Despliega un reenviador Linux con AMA (con Azure Arc si está fuera de Azure) y el conector Syslog/CEF vía AMA (configurar). |
| [M2](02_Nivel_2_Intermedio.md#m2) | 3 | Laboratorio | Habilita Windows Security Events vía AMA con el conjunto Common y compara el volumen con Minimal (conjuntos de eventos). |
| [M2](02_Nivel_2_Intermedio.md#m2) | 4 | Laboratorio | Envía un log personalizado con la API de ingesta de logs a una tabla propia. |
| [M2](02_Nivel_2_Intermedio.md#m2) | 5 | Laboratorio | Activa el libro de salud de recolección y una alerta para cuando un conector deje de enviar datos (salud de conectores). |
| [M3](02_Nivel_2_Intermedio.md#m3) | 1 | Laboratorio parcial | Con la tabla `Usage`, lista las diez tablas de mayor volumen y clasifícalas por valor de detección. |
| [M3](02_Nivel_2_Intermedio.md#m3) | 2 | Laboratorio | Mueve al nivel lake una tabla de alto volumen y bajo valor de detección, y define su retención. |
| [M3](02_Nivel_2_Intermedio.md#m3) | 3 | Laboratorio | Crea una summary rule que agregue por hora los registros de firewall en una tabla de analítica. |
| [M3](02_Nivel_2_Intermedio.md#m3) | 4 | Laboratorio | Ejecuta un KQL job sobre el lago y usa su resultado en una regla. |
| [M3](02_Nivel_2_Intermedio.md#m3) | 5 | Laboratorio | Arma una estimación mensual de costos con la página de precios y el beneficio de Microsoft 365 E5; compara dos escenarios. |
| [M4](02_Nivel_2_Intermedio.md#m4) | 1 | Laboratorio | Conecta el conector de inteligencia de amenazas de Microsoft y un feed TAXII público; verifica los datos en `ThreatIntelIndicators`. |
| [M4](02_Nivel_2_Intermedio.md#m4) | 2 | Laboratorio | Habilita una plantilla de regla de coincidencia de indicadores (TI map) contra registros de inicio de sesión y valida una alerta. |
| [M4](02_Nivel_2_Intermedio.md#m4) | 3 | Laboratorio | Crea las watchlists «Usuarios VIP» e «IP de escáneres autorizados» y úsalas en una regla para elevar la severidad o suprimir alertas (crear watchlists). |
| [M4](02_Nivel_2_Intermedio.md#m4) | 4 | Laboratorio | Enriquece inicios de sesión con `geo_info_from_ip_address()` y discute sus límites de precisión (función). |
| [M5](02_Nivel_2_Intermedio.md#m5) | 1 | Laboratorio | Configura una transformación split para una tabla de firewall: tráfico denegado al nivel de analítica y permitido solo al lago. |
| [M5](02_Nivel_2_Intermedio.md#m5) | 2 | Laboratorio | Escribe una DCR de transformación del workspace que elimine columnas ruidosas y pruébala con `datatable` (ejemplos). |
| [M5](02_Nivel_2_Intermedio.md#m5) | 3 | Laboratorio | Enmascara un campo de correo electrónico en la ingesta y compara el volumen antes y después con `Usage`. |
| [M6](02_Nivel_2_Intermedio.md#m6) | 1 | Laboratorio | Ejecuta la experiencia de migración de SIEM con una exportación de reglas de ejemplo y revisa sus recomendaciones. |
| [M6](02_Nivel_2_Intermedio.md#m6) | 2 | Laboratorio | Arma un plan por fases con criterios de éxito siguiendo la guía de migración. |
| [M6](02_Nivel_2_Intermedio.md#m6) | 3 | Laboratorio | Traduce tres búsquedas SPL a KQL con el mapeo SPL a KQL. |
| [M6](02_Nivel_2_Intermedio.md#m6) | 4 | Laboratorio | Define la estrategia de datos históricos y la de automatización (migrar automatización de Splunk). |
| [M7](02_Nivel_2_Intermedio.md#m7) | 1 | Laboratorio | Desde una plantilla del Content hub, crea una regla programada con mapeo de entidades y detalles personalizados. |
| [M7](02_Nivel_2_Intermedio.md#m7) | 2 | Laboratorio | Recrea la misma lógica como detección personalizada con una acción de respuesta y compárala con la tabla de paridad. |
| [M7](02_Nivel_2_Intermedio.md#m7) | 3 | Laboratorio | Escribe una regla NRT para un evento crítico, como el alta de un usuario en un grupo privilegiado. |
| [M7](02_Nivel_2_Intermedio.md#m7) | 4 | Laboratorio parcial | Revisa las recomendaciones de optimización del SOC e implementa una de cada tipo. |
| [M7](02_Nivel_2_Intermedio.md#m7) | 5 | Laboratorio parcial | Ajusta una regla ruidosa con una watchlist de excepciones y mide la reducción de falsos positivos. |
| [M8](02_Nivel_2_Intermedio.md#m8) | 1 | Laboratorio | Instala un libro del Content hub y personalízalo con parámetros y pestañas. |
| [M8](02_Nivel_2_Intermedio.md#m8) | 2 | Laboratorio | Construye un libro de eficiencia del SOC con métricas de `SecurityIncident`. |
| [M8](02_Nivel_2_Intermedio.md#m8) | 3 | Laboratorio | Exporta una consulta a Power BI y publícala para una audiencia ejecutiva. |
| [M9](02_Nivel_2_Intermedio.md#m9) | 1 | Laboratorio | Abre un incident case, agrega tareas mediante una regla de automatización, clasifica y cierra; luego verifica el evento en `SecurityCaseEvent` (gestión de casos). |
| [M9](02_Nivel_2_Intermedio.md#m9) | 2 | Laboratorio | Investiga un incidente del laboratorio con el gráfico y las páginas de entidad, y documenta la línea de tiempo. |
| [M9](02_Nivel_2_Intermedio.md#m9) | 3 | Laboratorio parcial | Calcula MTTT y MTTR por severidad con `SecurityIncident` y `arg_max()` (métricas). |
| [M10](02_Nivel_2_Intermedio.md#m10) | 1 | Laboratorio | Desde la página de MITRE, elige una técnica sin cobertura y crea un hunt con consultas del Content hub. |
| [M10](02_Nivel_2_Intermedio.md#m10) | 2 | Laboratorio | Documenta hallazgos y evidencia, y conviértelos en una regla y un incidente. |
| [M10](02_Nivel_2_Intermedio.md#m10) | 3 | Laboratorio | Repite una búsqueda en la búsqueda avanzada combinando una tabla de Sentinel con una de Defender XDR. |
| [M11](02_Nivel_2_Intermedio.md#m11) | 1 | Laboratorio parcial | Habilita UEBA y selecciona fuentes (habilitar UEBA); tras unos días, revisa `BehaviorAnalytics` y las páginas de entidad. |
| [M11](02_Nivel_2_Intermedio.md#m11) | 2 | Laboratorio parcial | Si tienes AWS CloudTrail o CEF compatibles, activa la capa de behaviors y consulta comportamientos por táctica y técnica. |
| [M11](02_Nivel_2_Intermedio.md#m11) | 3 | Laboratorio | Usa `IdentityInfo` en una regla para elevar la severidad cuando la cuenta afectada sea privilegiada. |
| [M12](02_Nivel_2_Intermedio.md#m12) | 1 | Laboratorio | Activa salud y auditoría, fuerza el fallo de una regla y consulta `_SentinelHealth()` y `_SentinelAudit()` (salud y auditoría). |
| [M12](02_Nivel_2_Intermedio.md#m12) | 2 | Laboratorio | Crea una regla que alerte cuando alguien elimine o deshabilite una regla de analítica. |
| [M12](02_Nivel_2_Intermedio.md#m12) | 3 | Laboratorio parcial | Revisa las recomendaciones de optimización del SOC y el indicador de cobertura por amenaza. |
| [M13](02_Nivel_2_Intermedio.md#m13) | 1 | Laboratorio | Crea una regla de automatización que asigne responsable y etiquete los incidentes de alta severidad. |
| [M13](02_Nivel_2_Intermedio.md#m13) | 2 | Laboratorio | Crea otra que cierre automáticamente un falso positivo conocido, con fecha de vencimiento. |
| [M13](02_Nivel_2_Intermedio.md#m13) | 3 | Laboratorio | Despliega un playbook desde plantilla y ejecútalo bajo demanda sobre un incidente. |
| [A1](03_Nivel_3_Avanzado.md#a1) | 1 | Laboratorio | Escribe una regla de fuerza bruta independiente de la fuente con `_Im_Authentication` y sus parámetros de filtrado. |
| [A1](03_Nivel_3_Avanzado.md#a1) | 2 | Laboratorio | Desarrolla un parser ASIM para una fuente Syslog de laboratorio, en versión filtrante y sin parámetros, y pruébalo con las herramientas de prueba de ASIM (desarrollar parsers). |
| [A1](03_Nivel_3_Avanzado.md#a1) | 3 | Laboratorio | Compara el rendimiento de una consulta con el parser unificador frente al parser específico de la fuente. |
| [A2](03_Nivel_3_Avanzado.md#a2) | 1 | Laboratorio | Optimiza una consulta lenta aplicando las buenas prácticas y mide el antes y el después con las estadísticas de consulta. |
| [A2](03_Nivel_3_Avanzado.md#a2) | 2 | Laboratorio | Construye una detección de anomalías por hora en fallos de inicio de sesión con `make-series` y `series_decompose_anomalies`. |
| [A2](03_Nivel_3_Avanzado.md#a2) | 3 | Laboratorio | Modela rutas de movimiento lateral con `make-graph` y `graph-match` sobre eventos de inicio de sesión en dispositivos. |
| [A2](03_Nivel_3_Avanzado.md#a2) | 4 | Laboratorio | Convierte una consulta repetida en una función reutilizable con parámetros. |
| [A3](03_Nivel_3_Avanzado.md#a3) | 1 | Laboratorio | Elige un riesgo de negocio de tu organización y diseña el caso de uso completo: fuentes, detecciones, respuesta, métricas y responsable. |
| [A3](03_Nivel_3_Avanzado.md#a3) | 2 | Laboratorio | Instala una solución de dominio del Content hub y documenta qué cubre y qué falta para tu caso. |
| [A3](03_Nivel_3_Avanzado.md#a3) | 3 | Solo producción | Si operas SAP, planifica la migración al conector sin agente (migración SAP). |
| [A4](03_Nivel_3_Avanzado.md#a4) | 1 | Laboratorio | Conecta un repositorio de GitHub a un workspace de laboratorio y despliega dos reglas en Bicep desde el repositorio de ejemplo. |
| [A4](03_Nivel_3_Avanzado.md#a4) | 2 | Laboratorio | Modifica una regla en el repositorio, observa el despliegue inteligente y verifica el historial. |
| [A4](03_Nivel_3_Avanzado.md#a4) | 3 | Laboratorio | Despliega una detección personalizada como código con `Microsoft.Security/detectionRules` (guía). |
| [A4](03_Nivel_3_Avanzado.md#a4) | 4 | Laboratorio | Agrega una prueba: ejecuta una simulación de ataque controlada en una VM de laboratorio y valida que la regla genere la alerta esperada. |
| [A5](03_Nivel_3_Avanzado.md#a5) | 1 | Laboratorio | Construye un conector CCF de sondeo para una API REST pública de prueba, con paginación y autenticación (crear conector). |
| [A5](03_Nivel_3_Avanzado.md#a5) | 2 | Laboratorio | Genera el mismo conector con el agente constructor desde Visual Studio Code y compara el resultado. |
| [A5](03_Nivel_3_Avanzado.md#a5) | 3 | Laboratorio | Empaqueta el conector, una regla y un libro como solución con la herramienta V3. |
| [A6](03_Nivel_3_Avanzado.md#a6) | 1 | Laboratorio | Lista incidentes y actualiza uno con la API de Graph (`/security/incidents`) usando una app con permisos mínimos. |
| [A6](03_Nivel_3_Avanzado.md#a6) | 2 | Laboratorio | Ejecuta una consulta de búsqueda avanzada por API con `runHuntingQuery` apuntando a tu workspace. |
| [A6](03_Nivel_3_Avanzado.md#a6) | 3 | Solo producción | Inventaría integraciones que todavía usen `/security/alerts` o las APIs antiguas de búsqueda avanzada y planifica su migración. |
| [A7](03_Nivel_3_Avanzado.md#a7) | 1 | Laboratorio | Instala la extensión de Microsoft Sentinel en Visual Studio Code y ejecuta un notebook PySpark sobre una tabla del lago (notebooks). |
| [A7](03_Nivel_3_Avanzado.md#a7) | 2 | Laboratorio | Programa el notebook como trabajo y escribe su resultado en una tabla consumible por una regla. |
| [A7](03_Nivel_3_Avanzado.md#a7) | 3 | Laboratorio | Ejecuta un notebook de investigación con MSTICPy para enriquecer IP con inteligencia de amenazas. |
| [A8](03_Nivel_3_Avanzado.md#a8) | 1 | Laboratorio parcial | Consulta 90 días de una tabla del lago desde la búsqueda avanzada y estima su costo con el medidor de consulta. |
| [A8](03_Nivel_3_Avanzado.md#a8) | 2 | Laboratorio | Crea un KQL job programado que resuma conexiones raras y alimente una regla de detección (KQL jobs). |
| [A8](03_Nivel_3_Avanzado.md#a8) | 3 | Laboratorio parcial | Explora el radio de impacto de un usuario comprometido en el gráfico de incidentes y en el hunting graph. |
| [A8](03_Nivel_3_Avanzado.md#a8) | 4 | Laboratorio parcial | Opcional: crea un grafo personalizado en un notebook y materialízalo con un graph job. |
| [A9](03_Nivel_3_Avanzado.md#a9) | 1 | Laboratorio parcial | Configura la gestión multi-inquilino de Defender con dos tenants de laboratorio y revisa la cola de incidentes unificada (MTO). |
| [A9](03_Nivel_3_Avanzado.md#a9) | 2 | Laboratorio parcial | Crea un perfil de distribución de contenido y publica dos reglas en ambos tenants. |
| [A9](03_Nivel_3_Avanzado.md#a9) | 3 | Laboratorio | Diseña la matriz de delegación (B2B, GDAP, Lighthouse) para un MSSP con tres clientes y justifica cada elección. |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 1 | Laboratorio | Orden de reglas: crea dos reglas de automatización (la primera baja la severidad y la segunda solo aplica a severidad media o mayor) y observa que la segunda evalúa el incidente ya modificado. |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 2 | Laboratorio | Aprobación humana: despliega la plantilla de tarjeta adaptable de Teams en la creación de incidentes y espera la respuesta del analista (conector de Teams). |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 3 | Laboratorio | Enriquecimiento con identidad administrada: sigue el tutorial de enriquecimiento de IP y asigna a la identidad solo el rol Responder. |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 4 | Laboratorio | Contención aprobada: combina la aprobación con Isolate-MDEMachine y Revoke-AADSignInSessions. |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 5 | Laboratorio parcial | Red privada: despliega un playbook en Logic Apps Standard con private endpoint y la política de restricción de acceso que permite a Sentinel invocarlo (playbooks en Logic Apps). |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 6 | Laboratorio | Como código y observable: exporta el playbook a ARM o Bicep, publícalo con un pipeline y correlaciona `SentinelHealth` con los diagnósticos de Logic Apps. |
| [X1](04_Nivel_4_Experto_agentico.md#x1) | 7 | Laboratorio parcial | Agéntico: crea un flujo de agente autónomo en Logic Apps Standard que reciba un incidente, consulte herramientas y proponga una acción para aprobación humana (agentes autónomos). |
| [X2](04_Nivel_4_Experto_agentico.md#x2) | 1 | Solo producción | Verifica si tu tenant tiene la inclusión de E5, revisa la capacidad y el workspace creados y explora el panel de uso. |
| [X2](04_Nivel_4_Experto_agentico.md#x2) | 2 | Laboratorio parcial | En un incidente de Sentinel, genera el resumen y las respuestas guiadas y compáralos con tu propio triage. |
| [X2](04_Nivel_4_Experto_agentico.md#x2) | 3 | Laboratorio parcial | En la búsqueda avanzada, genera tres consultas con el Threat Hunting Assistant en modo de solo consulta; revisa y corrige el KQL antes de ejecutarlo. |
| [X2](04_Nivel_4_Experto_agentico.md#x2) | 4 | Laboratorio parcial | Ejecuta un promptbook integrado de investigación sobre un incidente con el plugin de Sentinel (Security Copilot en Sentinel) y exporta el informe. |
| [X2](04_Nivel_4_Experto_agentico.md#x2) | 5 | Laboratorio | Redacta una guía de prompts para tu SOC: contexto, objetivo, fuentes y formato de salida esperados. |
| [X3](04_Nivel_4_Experto_agentico.md#x3) | 1 | Laboratorio parcial | Despliega el ejemplo oficial SecurityCopilot-Sentinel-Incident-Investigation y adjúntalo con una regla de automatización solo a incidentes de severidad alta. |
| [X3](04_Nivel_4_Experto_agentico.md#x3) | 2 | Laboratorio parcial | Modifícalo para usar una Direct Skill y compara el consumo de SCU en el panel de uso. |
| [X3](04_Nivel_4_Experto_agentico.md#x3) | 3 | Laboratorio parcial | Construye un playbook que ejecute un promptbook con parámetros del incidente y publique el resultado en Teams. |
| [X3](04_Nivel_4_Experto_agentico.md#x3) | 4 | Laboratorio parcial | Dispara un agente desde Logic Apps con la acción de ejecución de agentes (guía). |
| [X4](04_Nivel_4_Experto_agentico.md#x4) | 1 | Laboratorio parcial | Crea un plugin KQL con tres habilidades sobre tablas de Sentinel (por ejemplo, fallos de inicio de sesión de un usuario, dispositivos con un indicador y cambios recientes en reglas) (plugins KQL). |
| [X4](04_Nivel_4_Experto_agentico.md#x4) | 2 | Laboratorio parcial | Diseña un promptbook de triage de phishing con cinco prompts y parámetros de entrada, y compártelo con el equipo. |
| [X4](04_Nivel_4_Experto_agentico.md#x4) | 3 | Laboratorio parcial | Construye un plugin de API sobre un servicio de inteligencia con su especificación OpenAPI y versiona los manifiestos en Git. |
| [X5](04_Nivel_4_Experto_agentico.md#x5) | 1 | Solo producción | Habilita el Security Alert Triage Agent para alertas de correo en el laboratorio, revisa sus decisiones y dale retroalimentación en lenguaje natural. |
| [X5](04_Nivel_4_Experto_agentico.md#x5) | 2 | Laboratorio parcial | Ejecuta el Threat Intelligence Briefing Agent y compara su informe con tu proceso actual de inteligencia. |
| [X5](04_Nivel_4_Experto_agentico.md#x5) | 3 | Laboratorio parcial | Construye un agente propio para triage de inicios de sesión sospechosos con herramientas MCP de Sentinel y tu plugin KQL; define instrucciones, herramientas y permisos, y pruébalo (consume SCU). |
| [X5](04_Nivel_4_Experto_agentico.md#x5) | 4 | Laboratorio | Escribe la ficha de gobierno del agente: identidad, sponsor, owner, permisos, tope de costo y frecuencia de revisión. |
| [X6](04_Nivel_4_Experto_agentico.md#x6) | 1 | Laboratorio | Conecta Visual Studio Code con GitHub Copilot al servidor MCP de Sentinel (visión general) con las colecciones de exploración y triage. |
| [X6](04_Nivel_4_Experto_agentico.md#x6) | 2 | Laboratorio | Pide en lenguaje natural las tablas con datos de inicio de sesión y luego los fallos de los últimos siete días; revisa el KQL generado. |
| [X6](04_Nivel_4_Experto_agentico.md#x6) | 3 | Laboratorio | Lista los incidentes abiertos de severidad alta y pide un resumen con las herramientas de triage. |
| [X6](04_Nivel_4_Experto_agentico.md#x6) | 4 | Laboratorio | Crea una herramienta personalizada desde una consulta guardada de búsqueda avanzada y úsala desde Visual Studio Code. |
| [X6](04_Nivel_4_Experto_agentico.md#x6) | 5 | Laboratorio parcial | Conecta Copilot Studio o Microsoft Foundry con una app de Entra de acceso delegado y construye un agente simple (Copilot Studio). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 1 | Laboratorio | **Fase 1 · Plataforma:** workspace principal incorporado a Defender con data lake, RBAC unificado y presupuesto. Entregable: diagrama y registro de decisiones (M1, M3). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 2 | Laboratorio | **Fase 2 · Datos:** Entra ID, Defender XDR, actividad de Azure y una fuente Syslog/CEF vía AMA o un conector CCF; una tabla dividida entre analítica y lago. Entregable: inventario de tablas por nivel con costo… |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 3 | Laboratorio | **Fase 3 · Detección:** tres reglas (una NRT, una con ASIM y una con watchlist) y una detección personalizada con acción de respuesta, todas en un repositorio. Entregable: contenido como código con mapeo MITRE (M7,… |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 4 | Laboratorio | **Fase 4 · Validación:** simulación controlada con el Training Lab o una prueba en una VM de laboratorio; incidentes generados y métricas de detección (I5, M9). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 5 | Laboratorio | **Fase 5 · Automatización:** regla de automatización, playbook de enriquecimiento con identidad administrada, aprobación en Teams y contención (M13, X1). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 6 | Laboratorio parcial | **Fase 6 · IA:** playbook que invoca Security Copilot y comenta el incidente, un promptbook de triage y un plugin KQL propio (X2, X3, X4). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 7 | Laboratorio parcial | **Fase 7 · Agentes y MCP:** un agente de Microsoft habilitado y supervisado, un agente propio que usa herramientas MCP de Sentinel y consultas en lenguaje natural sobre el lago desde Visual Studio Code (X5, X6). |
| [X7](04_Nivel_4_Experto_agentico.md#x7) | 8 | Laboratorio | **Fase 8 · Operación y gobierno:** salud y auditoría, tablero de consumo (ingesta, lago y SCU), identidades de agentes y un informe ejecutivo de una página (M12, X5). |
| [C1](05_Comunidad.md#c1) | 1 | — | Elige cinco referentes de este directorio, uno por especialidad, y síguelos en su blog, GitHub o LinkedIn. |
| [C1](05_Comunidad.md#c1) | 2 | — | Marca con «Watch» los repositorios de consultas que más uses para recibir sus novedades. |
| [C5](05_Comunidad.md#c5) | 1 | — | **Cada semana (unos 30 minutos):** suscríbete por RSS al blog de Sentinel (feed), lee THE PROMPT y revisa lo nuevo en kqlsearch.com y en el Microsoft Security Blog. |
| [C5](05_Comunidad.md#c5) | 2 | — | **Cada mes:** revisa las novedades de Sentinel, Defender XDR y Security Copilot, el resumen mensual de Defender comentado por Jeffrey Appel y las notas de versión de las soluciones del Content hub que uses. |
| [C5](05_Comunidad.md#c5) | 3 | — | **Cada trimestre o evento:** arma tu agenda de Ignite (noviembre) y RSAC (marzo) por códigos de sesión, y revisa las fechas límite: portal de Azure (31 de marzo de 2027), retiros de APIs y cambios de conectores. |
| [C5](05_Comunidad.md#c5) | 4 | — | **Antes de recomendar algo a un cliente:** confirma el estado (vista previa o disponibilidad general) y la fecha en la fuente oficial. |

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

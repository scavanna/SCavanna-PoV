# Narrativa para el CIO y el CTO

**Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2** · documento 12 de 16 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base, sujeta a validación y a calibración en cada organización. La ejecución se puede contratar; la rendición de cuentas, no.

## Cómo usar este documento

Es una narrativa de base, no un texto para leer en voz alta. Antes de usarla, reemplace cada dato entre corchetes por el valor de su diagnóstico y quite lo que no aplique. Los indicadores y las decisiones provienen del modelo; el orden y el tono son una propuesta.

## 1. Qué le importa a esta audiencia

El CIO y el CTO operan las plataformas sobre las que se aplica la seguridad. Les importa la velocidad de entrega, la estabilidad, el costo, la carga de sus equipos y quién responde por qué. Llegan a esta conversación con una experiencia previa: la seguridad como una lista de pedidos que compite con sus proyectos.

## 2. El mensaje en un párrafo

*La seguridad deja de ser una lista de proyectos que compite con los suyos. Pasa a ser un conjunto de servicios con dueño, nivel de servicio y medición, sobre una arquitectura que definimos juntos. Les pido tres cosas: propiedad compartida de los controles que viven en sus plataformas, una misma línea base en todos los entornos y visibilidad sobre los contratos de tecnología que incluyen funciones de seguridad. A cambio ofrezco reglas estables, menos herramientas solapadas y un tiempo de habilitación que se mide y se publica.*

## 3. El hilo de la conversación

| Paso | Qué se dice | Dato que lo sostiene |
|---|---|---|
| 1. Qué encontramos | El diagnóstico calificó cada función con evidencia. No es una auditoría de tecnología: es una línea base común. | [Nivel promedio de evidencia de los servicios de operación]; [funciones sin dueño]; [paridad de control entre entornos, K123] |
| 2. Cada control tiene un dueño | Un control es un producto: tiene un objetivo, una configuración de referencia y una evidencia. Varios de esos dueños están en tecnología. | [Productos-control con dueño designado]; lista de dueños propuestos |
| 3. Una regla para todos los entornos | La política se define una vez y se aplica igual en cada nube, en el centro de datos y en lo que opera un tercero. La arquitectura de referencia es Zero Trust, en ocho dominios. | [Recursos conformes a la línea base en el entorno menos conforme, K141]; [cuentas y suscripciones bajo la línea base, K134] |
| 4. Habilitar más rápido | La revisión de seguridad ocurre antes de producción y tiene un plazo comprometido. | [Tiempo de habilitación segura de iniciativas, K20]; [iniciativas con revisión de arquitectura, K116] |
| 5. Detectar, contener y recuperar | Los tiempos se miden de punta a punta, también cuando un proveedor opera el servicio. | [Tiempo medio de detección, K42]; [de contención, K45]; [restauración frente al objetivo, K47] |
| 6. Menos herramientas, mejor integradas | El relevamiento de la pila muestra dónde hay solapamiento sin justificación y qué no llega a la telemetría central. | [Capacidades con herramientas solapadas, K122]; [cobertura de telemetría, K41] |
| 7. Agentes de IA | Un agente que ejecuta tareas es una identidad con dueño, límites y registro. Lo tratamos como a una cuenta privilegiada, no como a una función de una aplicación. | [Agentes inventariados]; [agentes con identidad propia]. Tema de base provisoria. |

## 4. Qué pedimos

| Dimensión | Qué cambia | Decisión que se pide | Etapa |
|---|---|---|---|
| Presupuesto | Racionalizar las herramientas solapadas libera gasto, pero la migración cuesta. | Aprobar el plan de consolidación con su costo de transición. | Ciclo 2 |
| Organigrama | Cada control pasa a tener un dueño de producto. | Designar dueños de producto-control por dominio. | Ciclo 1 |
| Organigrama | Seguridad y tecnología comparten la operación: hace falta una frontera clara. | Aprobar la matriz de responsabilidades entre seguridad y tecnología. | Ciclo 1 |
| Dotación | Los agentes ejecutan tareas: cambia el trabajo de los analistas. | Aprobar el itinerario de desarrollo del equipo y los niveles de autonomía de los agentes. | Ciclo 3 |
| Cultura | La seguridad entra antes del diseño, no al final. | Exigir la revisión de arquitectura antes de la puesta en producción. | Ciclo 2 |
| Socios | Las integraciones con socios abren accesos. | Exigir identidad propia, privilegio mínimo y registro en toda integración. | Ciclo 2 |
| Proveedores | Los contratos pasan a medirse por resultados. | Renegociar los contratos críticos con niveles de servicio por resultado y evidencia. | Ciclo 2 |
| Proveedores | Todo servicio crítico debe poder dejarse. | Ensayar la salida de los servicios críticos. | Ciclo 3 |

## 5. Qué comprometemos

16 indicadores principales para esta audiencia. Los umbrales son propuestas para calibrar con la línea base.

| ID | Indicador | Unidad | Mejor si es | Umbrales E2 · E3 · E4 · E5 |
|---|---|---|---|---|
| K20 | Tiempo de habilitación segura de iniciativas | días | Menor | 20 · 10 · 5 · 2 |
| K33 | Autenticación resistente al phishing | % | Mayor | 25 · 50 · 80 · 95 |
| K34 | Accesos privilegiados sin privilegios permanentes (JIT) | % | Mayor | 25 · 50 · 75 · 90 |
| K36 | Segmentación de activos críticos verificada | % | Mayor | 40 · 60 · 80 · 95 |
| K38 | Aplicaciones críticas con controles automatizados en el pipeline | % | Mayor | 30 · 50 · 75 · 90 |
| K41 | Cobertura de telemetría y protección de activos críticos | % | Mayor | 60 · 75 · 90 · 98 |
| K42 | Tiempo medio de detección (MTTD) | horas | Menor | 72 · 24 · 8 · 1 |
| K45 | Tiempo medio de contención (MTTC) | horas | Menor | 48 · 12 · 4 · 1 |
| K47 | Tiempo de restauración de servicios críticos frente al RTO | % del RTO | Menor | 200 · 150 · 100 · 75 |
| K116 | Iniciativas con revisión de arquitectura antes de producción | % | Mayor | 40 · 65 · 85 · 95 |
| K118 | Accesos evaluados por política con señales de contexto | % | Mayor | 40 · 65 · 85 · 95 |
| K120 | Desviaciones críticas de configuración abiertas | n.º | Menor | 20 · 10 · 3 · 0 |
| K123 | Paridad de control entre entornos | % | Mayor | 40 · 60 · 80 · 95 |
| K134 | Cuentas y suscripciones de nube bajo la línea base | % | Mayor | 50 · 75 · 90 · 98 |
| K138 | Tiempo de corrección de vulnerabilidades críticas | días | Menor | 60 · 30 · 15 · 7 |
| K141 | Recursos conformes a la línea base en el entorno menos conforme | % | Mayor | 50 · 70 · 85 · 95 |

## 6. Cuándo y cómo informamos

| Cadencia | Rito | Qué se trata |
|---|---|---|
| Semanal | Revisión operativa de los controles | Revisar alertas, incidentes, cambios y tareas de cadencia de cada producto-control. |
| Mensual | Comité de seguridad y riesgo | Decidir sobre riesgos, excepciones y cambios de prioridad. |
| Por ciclo · cierre | Informe al CIO y al CTO | Rendir el avance técnico y acordar la cartera del ciclo siguiente. |

El informe de cierre de ciclo usa la hoja «Tablero tecnología» del libro `Frontier_CISO_Atlas_CISO365_KPIs_y_Tablero_v2.0.xlsx`.

## 7. Objeciones previsibles

| Objeción | Respuesta |
|---|---|
| «Esto va a frenar los proyectos.» | El plan mide el tiempo de habilitación segura (K20) y lo publica. Si la revisión demora, el indicador lo muestra y la corrección es nuestra. |
| «Ya tenemos herramientas para eso.» | El diagnóstico no agrega herramientas: registra cuáles hay, quién las opera y dónde se solapan (K122). El resultado habitual es usar mejor las que existen. |
| «Mi equipo no tiene capacidad.» | Por eso cada función tiene un modelo de provisión. Ser dueño de un control no obliga a operarlo: obliga a responder por su objetivo y por su evidencia. |
| «El proveedor de nube ya lo cubre.» | Cubre su parte. La configuración, las identidades y los datos son responsabilidad nuestra, y la paridad entre entornos (K123) muestra dónde no se aplica la misma regla. |
| «Los agentes son un tema de datos, no de seguridad.» | Son las dos cosas. Un agente con permisos permanentes y sin registro es una cuenta privilegiada sin control. |
| «¿Quién decide si hay conflicto?» | Las decisiones reservadas y su dueño quedan escritas en el ciclo 1. Lo que excede el apetito de riesgo se escala al comité. |

## 8. Guion breve (cinco minutos)

1. «Medimos antes de proponer. Este es el estado de las funciones que dependen de sus plataformas: [dos o tres datos].»
2. «Propongo que cada control tenga un dueño. Estos son los que, a mi juicio, deberían estar en tecnología: [lista].»
3. «Una sola línea base para todos los entornos. Hoy la paridad es de [K123].»
4. «Me comprometo a un tiempo de habilitación de [K20] y a publicarlo en cada ciclo.»
5. «Necesito de ustedes estas decisiones: [las de la sección 4 que correspondan al ciclo].»
6. «Nos vemos al cierre de cada ciclo con este mismo tablero.»

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · versión 2.0, revisión 2 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

# Logic Apps como SOAR central hacia un SOC agéntico

Guía, mejor práctica y base de assessment para M365 E5, Sentinel, Defender for Cloud Servers Plan 2 y Splunk on-prem

- Versión: 1.0.0
- Fecha de verificación: 2026-11-11
- Hash de contenido: `b9074bd5994b9d57622999814d31ff868be4f7282fc4c2083bcdf3b6e9093443`
- Estado: Guía de arquitectura. No es una declaración de cumplimiento ni un diseño aprobado del cliente.
- Audiencia: CISO, responsable de SOC, arquitecto de seguridad, ingeniería de detección, ingeniería de automatización

Este archivo contiene el mismo modelo que el JSON y que el HTML. El Excel es el assessment, el plan y la base que actualiza el estado del HTML.

## 1. Respuesta directa

Sí. Se puede construir un plano de trabajo y respuesta que priorice Logic Apps, Security Copilot y la gestión de casos del portal de Microsoft Defender, aunque la detección siga repartida durante años entre Sentinel, Defender XDR y uno o varios Splunk on-prem. No existe un interruptor que convierta a Splunk, o a varias instancias de Sentinel, en un único SIEM dentro de la consola. Lo que sí existe es una arquitectura de federación: cada SIEM detecta en su dominio, y un contrato común de señal entra a Logic Apps, que crea o actualiza un único objeto de trabajo en el plano Microsoft.

Ese objeto de trabajo, para una señal que merece respuesta, es un incidente de Microsoft Sentinel conectado al portal de Defender. Al estar el workspace conectado, el incidente se gestiona como incident case. El analista no debería tener una cola en Splunk y otra en Defender para el mismo ataque. Splunk conserva la detección y el notable; el case es la cola. Logic Apps es la tela que cruza los dos mundos. Security Copilot razona sobre el case y llama a Logic Apps. No sustituye al playbook cuando la acción cambia identidad, dispositivo o un control de producción.

> **Decisión de arquitectura.** Muchos planos de detección. Un solo plano de trabajo. Una sola tela de automatización. Las acciones de contención pasan por un playbook con aprobación, no por el SIEM que originó la alerta ni por un agente con permiso de escritura amplio.

Esta guía sirve para diseñar esa convivencia y para evaluar lo que el cliente ya tiene. El Excel es el assessment y el plan vivo. El HTML puede recibir el estado copiado desde la hoja Estado_HTML sin reescribir la guía. Markdown, JSON y HTML contienen el mismo modelo.

## 2. Qué problema resuelve y qué no

El cliente tiene Microsoft 365 E5, Microsoft Sentinel dentro del alcance del beneficio de ingesta, Defender for Cloud Servers Plan 2, y un Splunk on-prem que no va a desaparecer en un proyecto. El objetivo no es migrar Splunk en un big-bang. El objetivo es que el SOC avance hacia un modelo agéntico apoyado en tecnologías Microsoft sin abrir una segunda, tercera o cuarta cola de respuesta cada vez que aparece otro SIEM.

### Qué sí resuelve

- Una cola de trabajo en el portal de Defender para incidentes Microsoft y para detecciones externas que se promueven a incidente.
- Un contrato único para conectar otra instancia de Sentinel o de Splunk sin rediseñar el SOAR.
- Respuesta determinista, auditable y con aprobación, aunque el razonamiento lo haga Security Copilot.
- Un uso consciente del beneficio E5 y del allowance de Servers Plan 2, sin duplicar logs para 'tenerlos en los dos SIEM'.
- Un camino por fases desde playbooks deterministas hasta agentes con alcance escrito.

### Qué no resuelve

- No convierte a Splunk en un data connector nativo de case management. La federación se construye.
- No incluye en E5 el producto Sentinel completo, UEBA, Logic Apps, ni la capacidad de Security Copilot.
- No justifica copiar el volumen histórico de Splunk a Sentinel para poder automatizar.
- No autoriza a un agente a aislar dispositivos o deshabilitar cuentas sin un playbook y una aprobación.
- No reemplaza las acciones nativas de Defender XDR. Si Defender ya puede interrumpir el ataque, el playbook no debe reinventarlo.

## 3. Alcance de licenciamiento y de beneficio

Hay que separar cuatro cosas que el cliente suele oír como si fueran una sola: el derecho de uso de Defender XDR que trae Microsoft 365 E5, el beneficio de ingesta de Sentinel, el allowance de Defender for Servers Plan 2, y los productos que se pagan aparte. Diseñar el SOAR sin esta separación produce dos errores: prometer agentes o UEBA como si vinieran en E5, o ingerir en Sentinel datos que el beneficio no cubre.

### Beneficio de Sentinel para Microsoft 365 E5, A5, F5, G5 y variantes Security

La oferta publicada por Microsoft, verificada el 11 de noviembre de 2026, concede un data grant de hasta 5 MB por usuario por día para ingerir datos de Microsoft 365 en Sentinel. El grant se calcula y se aplica en la factura. Cubre, según la página de la oferta, estas fuentes: registros de inicio de sesión y de auditoría de Microsoft Entra ID; registros de detección de shadow IT de Microsoft Defender for Cloud Apps; registros de Microsoft Purview Information Protection; y datos de advanced hunting de Microsoft 365. El medidor asociado en exportaciones de uso de Azure Monitor es Free Benefit - M365 Defender Data Ingestion.

> **Límite del grant.** 5 MB por usuario por día no es un derecho a ingerir cualquier log en Sentinel. Firewalls, aplicaciones on-prem, syslog general, canales de eventos que no estén en la lista y telemetría cruda que exceda el grant se facturan, salvo que otro beneficio los cubra. El volumen exacto por tabla se confirma en el usage export del workspace, no en esta guía.

### Fuentes sin cargo de ingesta para cualquier cliente de Sentinel

Además del grant, el artículo de facturación de Sentinel lista fuentes que no se cobran. No dependen de E5. Son: Azure Activity Logs; Microsoft Sentinel Health; Office 365 Audit Logs, incluidos SharePoint, actividad de administración de Exchange y Teams; y alertas de seguridad de Microsoft Defender XDR, Defender for Cloud, Defender for Office 365, Defender for Identity, Defender for Endpoint y Defender for Cloud Apps. Las alertas son gratuitas. Varios logs crudos de esos mismos productos son de pago. No se ingieren logs crudos solo porque las alertas no cuesten.

### Defender for Servers Plan 2

Al habilitar Defender for Servers Plan 2, Microsoft documenta 500 MB de ingesta gratuita por nodo y por día. El allowance diario es el número de máquinas por 500 MB. Se calcula para todas las máquinas de la suscripción y no se exige máquina por máquina: una máquina puede pasar de 500 MB si el total de la suscripción cabe en el allowance. Aplica al workspace de Log Analytics mientras el plan está activo en ese workspace. Con medidores clásicos de Sentinel aplica a la ingesta de Log Analytics. Con medidores simplificados o unificados aplica a la ingesta de Sentinel. Hay que identificar qué modelo factura el workspace del cliente antes de estimar ahorro.

El allowance cubre datos de seguridad elegibles ingeridos por Azure Monitor Agent, por el sensor de Microsoft Defender for Endpoint, o por file integrity monitoring sin agente. La lista documentada incluye SecurityAlert, SecurityBaseline, SecurityBaselineSummary, SecurityDetection, SecurityEvent, WindowsFirewall, ProtectionStatus, Update y UpdateSummary en las condiciones indicadas, MDCFileIntegrityMonitoringEvents, WindowsEvent, DeviceCustomFileEvents y DeviceCustomRegistryEvents. Aunque WindowsEvent aparece en la lista, solo califican los eventos de seguridad del stream Microsoft-SecurityEvent que van a SecurityEvent. Application, System y otros canales se facturan como ingesta normal.

Para ver el allowance hace falta que el plan esté habilitado en el workspace. La documentación de costos de Azure Monitor indica, además, que la solución Security debe haber sido creada en el workspace para recibir el allowance de Defender for Servers. Se valida en la página Usage and estimated costs y en el usage export, medidor Standard Data Included per Node.

### Qué no entra en estos beneficios

| Capacidad | ¿La cubre E5 o el allowance? | Implicación para el SOAR |
| --- | --- | --- |
| Detección y respuesta de Defender XDR (Endpoint, Identity, Office 365, Cloud Apps) y Entra ID P2 | Sí, como productos de E5. No es ingesta de Sentinel. | La primera respuesta de identidad, endpoint y correo debe ser nativa. Logic Apps orquesta lo que cruza sistemas. |
| Microsoft Sentinel como SIEM completo | No. Solo el grant de hasta 5 MB/usuario/día y las fuentes siempre gratuitas. | Sentinel se usa para correlación, hunting y casos dentro de ese alcance. El resto se justifica con un caso de costo. |
| UEBA de Sentinel | No. Es una capacidad de pago. E5 permite conectar ciertas fuentes XDR a UEBA sin reingestarlas, pero UEBA no está incluido y sus salidas generan cargo de Log Analytics. | No diseñar el SOC agéntico sobre UEBA hasta tener presupuesto y un caso de uso. |
| Security Copilot y agentes | No. Operan con SCU. No hay una licencia de agente aparte, pero la capacidad no viene por tener E5. | El camino crítico de respuesta no puede depender de SCU. Copilot acelera; el playbook responde. |
| Azure Logic Apps | No. Consumption o Standard se facturan aparte. | Presupuestar el bus de federación. Standard se justifica por red privada hacia Splunk, no por moda. |
| Sesiones agénticas sobre incident cases | No como derecho de E5. La documentación las limita a clientes con acceso a Project Perception. | No bloquear el programa si el tenant no tiene ese acceso. El camino general es agente de Security Copilot más Logic Apps. |
| Splunk on-prem | Fuera de Microsoft. | Sigue siendo el plano de detección de lo que no tiene dueño Microsoft ni caso de migración. |

> **Verificar en el tenant.** Confirmar elegibilidad E5, E7, A5, F5 o G5 y el acuerdo Enterprise; el modelo de medidor del workspace; que Plan 2 está activo en el workspace de los servidores; el consumo real de ambos beneficios en los últimos 31 días; y si hay SCU de Security Copilot contratadas. Esta guía no sustituye el cost estimator ni una cotización.

## 4. Principio: muchos SIEM, un plano de trabajo

Un SIEM es un plano de detección y retención. Un SOAR es un plano de decisión y acción. Mezclarlos es la razón por la que cada SIEM nuevo crea otro SOC. La consola unificada, los cases y Logic Apps permiten separar esas funciones.

| Plano | Dueño en esta arquitectura | Puede haber varios | No debe hacer |
| --- | --- | --- | --- |
| Detección Microsoft de identidad, endpoint, correo y SaaS | Defender XDR, con E5 | No como cola. Sí como productos. | Exportar sus alertas a Splunk para que otro equipo las trabaje otra vez. |
| Detección y hunting dentro del beneficio | Sentinel en el portal de Defender | Solo si residencia, soberanía o radio de impacto lo exigen. Un workspace primario. | Ingerir el archivo histórico de Splunk. |
| Detección on-prem y fuentes aún sin caso de migración | Splunk | Sí, varias instancias, si el contrato de señal es el mismo. | Ser la cola de trabajo de incidentes que Defender ya correlacionó. |
| Trabajo del analista | Cases del portal de Defender | No. Una cola. | Depender de un notable o de un ticket como único registro de la investigación. |
| Automatización y cruce entre sistemas | Azure Logic Apps | Varios flujos, una tela y un estándar. | Contener en producción sin identidad, sin idempotencia y sin aprobación. |
| Razonamiento y asistencia | Security Copilot | Varios agentes, un alcance escrito por agente. | Ejecutar contención por su cuenta o guardar el secreto de Splunk. |

Si mañana aparece una segunda instancia de Sentinel o un segundo Splunk, no se crea otro SOAR. Se le exige el mismo contrato de señal y se registra la instancia en el inventario. El case sigue siendo uno. Esa es la prueba de que el diseño está bien: el número de SIEM deja de ser el número de colas.

## 5. Arquitectura objetivo

La arquitectura tiene cinco anillos. El analista y el agente viven en el anillo de trabajo. Logic Apps es el único componente autorizado a cruzar anillos para actuar. Los SIEM no se llaman entre sí para contener.

1. Experiencia: portal de Microsoft Defender en security.microsoft.com. Cases, incidentes, hunting de Defender y Sentinel conectado. El portal de Azure de Sentinel deja de ser la consola operativa. Microsoft retirará Sentinel del portal de Azure el 31 de marzo de 2027.
2. Trabajo: incident cases para señales que son o se promueven a incidente. Generic cases para trabajo de SecOps que no es un incidente, como una caza, un seguimiento de control o una mejora. Un generic case puede enlazar incidentes, indicadores y recomendaciones. No es un SIEM.
3. Razonamiento: Security Copilot embebido y, cuando haya SCU, promptbooks y agentes. Los agentes llaman skills. El skill que toca Splunk es un flujo de Logic Apps, para que el secreto no viva en el agente.
4. Tela: Logic Apps. Playbooks de Sentinel para señales que ya son incidente o alerta. Flujos Standard, en red virtual, para hablar con Splunk on-prem. Un almacén de idempotencia. Key Vault. Identidad administrada.
5. Detección: Defender XDR, Sentinel dentro del beneficio y del allowance, y Splunk para el resto. Cada fuente tiene un dueño de detección. La duplicación, si existe, tiene fecha de salida.

### Flujo de una señal externa

1. Splunk, u otro SIEM, emite solo notables o alertas de la severidad acordada. No emite el log crudo.
2. La llamada sale de Splunk hacia Logic Apps, por HTTPS, autenticada. No se abre el puerto de gestión de Splunk a Internet.
3. Logic Apps normaliza la señal al contrato, busca la clave de idempotencia y busca un incidente Microsoft abierto con las mismas entidades dentro de la ventana acordada.
4. Si ya existe incidente, no crea otro. Comenta, etiqueta y actualiza el notable como enlazado.
5. Si no existe y la severidad está en el umbral, crea un incidente de Sentinel con entidades, enlace al notable y la clave de origen. El incident case aparece en el portal.
6. Una automation rule dispara enriquecimiento y, si aplica, un promptbook. La contención queda en un playbook con aprobación.
7. Al cerrar el case, Logic Apps actualiza el notable por un camino privado y escribe el resultado. El analista no cierra en dos consolas a mano.

### Flujo de una señal Microsoft

Defender XDR correlaciona y, si corresponde, interrumpe. Sentinel aporta correlación e hunting dentro de su alcance. El incident case es el trabajo. Logic Apps enriquece, notifica y ejecuta solo los pasos que salen del plano Microsoft o que la operación quiere dejar deterministas. Si Splunk tiene un notable del mismo ataque, se enlaza. No se copia la alerta de Defender a Splunk para abrir otro notable.

> **Límite de producto.** La creación de generic cases está documentada como acción del portal. No se encontró, en la documentación verificada, un conector soportado para crear generic cases desde Logic Apps. No se diseña el bus sobre una API no publicada. El on-ramp de automatización es el incidente de Sentinel, que el portal gestiona como incident case. Los generic cases los abre el analista para trabajo que no debe fingir ser un incidente. Antes de construir una dependencia de escritura sobre cases, se verifica en el tenant si apareció un conector soportado.

## 6. Qué hace cada tecnología y qué no debe hacer

### Portal de Defender y case management

Es la consola del SOC. Case management está solo en el portal de Defender, no en la experiencia de Sentinel del portal de Azure. Hay dos tipos relevantes. Incident cases, en versión preliminar a la fecha de esta guía, son la experiencia recomendada para investigar y cerrar incidentes: historia de ataque, alertas, activos, evidencia, tareas, comentarios, clasificación y, si el tenant tiene Project Perception, sesiones agénticas. Generic cases sirven para trabajo de SecOps no atado a un incidente: dueño, prioridad, estado, tareas, comentarios, adjuntos, campos personalizados y objetos enlazados.

Las plantillas permiten campos personalizados y directivas de SLA. Esos campos son el lugar del contrato de procedencia: sistema de origen, instancia y identificador. La actividad de cases se puede auditar en Log Analytics en la tabla SecurityCaseEvent. Los permisos de incident cases siguen el modelo de incidentes. Los generic cases usan Security data basics para leer, Alerts (manage) para crear y gestionar, y Core security settings para plantillas. También aplican roles de Sentinel: Reader, Responder y Contributor, según la acción.

Para un cliente ISOC, la documentación indica que incident cases y generic cases no exigen un workspace. Este cliente usa Sentinel, así que el workspace sí debe estar conectado. Sin esa conexión no hay incident case a partir del incidente de Sentinel ni benefit operativo de la consola unificada.

### Logic Apps

Es el SOAR. En Sentinel, un playbook es un flujo de Logic Apps. Las automation rules pueden ejecutarlo cuando un case, un incidente o una alerta cumple condiciones. También se puede ejecutar a mano sobre un incidente, una alerta o una entidad. El cargo de Logic Apps es adicional.

Consumption sirve para playbooks de Sentinel de volumen irregular, si no necesitan red virtual. Standard sirve para el bus con Splunk: red virtual, puntos de conexión privados, más control de ejecución y un lugar donde vivir el flujo que consulta o actualiza notables. No se exponen conexiones con la cuenta personal de un ingeniero. La identidad es administrada. El secreto de Splunk está en Key Vault.

Microsoft Sentinel ejecuta playbooks de incidente con una cuenta de servicio. Esa cuenta necesita el rol Microsoft Sentinel Automation Contributor sobre el grupo de recursos del playbook. Quien otorga ese rol necesita Owner o User Access Administrator. Sin ese rol, la automation rule no corre el playbook aunque el flujo esté bien.

### Security Copilot

Es el plano de razonamiento. Puede investigar, resumir, cazar y, con agentes, ejecutar tareas dentro de permisos, disparadores y una identidad que configura el administrador. Los agentes consumen SCU. Un agente se despliega desde el portal de Security Copilot o el Security Store. El administrador define identidad y RBAC. El usuario puede revisar disparadores, acceso a datos y si el permiso es de lectura o de escritura.

Hay dos sentidos de integración con Logic Apps, ambos documentados. De fuera hacia dentro: un conector de Logic Apps puede disparar un agente ya creado, si el plugin del agente está publicado para Anyone in this Workspace. De dentro hacia fuera: un flujo de Logic Apps puede publicarse como skill e invocarse desde un prompt, un promptbook o un agente. Ese segundo sentido es el que debe usar cualquier lectura o actualización de Splunk.

Las sesiones agénticas lanzadas desde un incident case, con Run agentic playbook, están documentadas solo para clientes con acceso a Project Perception. Si el cliente no lo tiene, no se promete. El programa sigue con promptbooks y agentes de Security Copilot que llaman playbooks.

### Sentinel, dentro del alcance

Sentinel no es el SOAR de esta arquitectura, aunque históricamente se haya vendido como SIEM y SOAR. Aquí es el plano de detección, hunting y retención de lo que el beneficio y el allowance cubren, y el sistema que materializa un incidente cuando una señal externa merece un case. También es el lugar de las automation rules. No es el lugar donde se pega el log de Splunk para poder orquestar.

Conviene un workspace primario conectado al portal. Otros workspaces solo si hay una razón de residencia, soberanía, blast radius o facturación. Las automation rules son del workspace. Si hay más de uno, cada workspace llama a la misma tela de Logic Apps. No se clona el estándar.

### Splunk on-prem

Durante la convivencia, Splunk sigue detectando sobre las fuentes que no tienen dueño Microsoft o cuyo volumen no cabe en un caso de costo. Conserva notables, contenido y retención que el negocio todavía exige. Pierde el derecho a ser la cola principal del SOC para ataques que el plano Microsoft ya ve. Gana un contrato claro: emite señales, recibe estado, no ejecuta contención de Entra o de Defender por su cuenta.

## 7. Contrato de señal y reglas de federación

Toda fuente que quiera entrar al plano de trabajo emite el mismo objeto. Si una fuente no puede llenar los campos obligatorios, no se federa: se corrige el notable o se deja en su SIEM. El contrato es la condición para que el número de SIEM no importe.

| Campo | Obligatorio | Uso |
| --- | --- | --- |
| sourceSystem | Sí | sentinel, defender-xdr, splunk u otro valor controlado. |
| sourceInstance | Sí | Nombre estable de la instancia o del workspace. No el nombre del analista. |
| sourceEventId | Sí | Identificador estable del notable, la alerta o el incidente de origen. |
| idempotencyKey | Sí | sourceSystem + sourceInstance + sourceEventId. La guarda Logic Apps, no el analista. |
| title | Sí | Una línea. Sin volcar el log. |
| severity | Sí | Valor ya mapeado a Informational, Low, Medium o High. |
| eventTime | Sí | Hora del evento en UTC. |
| entities | Sí, si existen | Cuenta, dispositivo, IP, URL o archivo. Sin entidades, no hay deduplicación seria. |
| sourceUrl | Sí | Enlace para el analista que necesite el contexto crudo. |
| recommendedAction | No | Pista. No es una orden de contención. |
| rawRef | No | Puntero a un evento, no el evento completo. |

### Mapa de severidad inicial

Es una propuesta para acordar, no un valor de producto. Por defecto solo se federan High y, si el cliente lo firma, Medium de reglas ya afinadas. Informational no entra a la cola.

| Origen típico | Valor de origen | Severidad del incidente | ¿Se federa por defecto? |
| --- | --- | --- | --- |
| Splunk | critical | High | Sí |
| Splunk | high | High | Sí |
| Splunk | medium | Medium | Solo si la regla está en la lista blanca |
| Splunk | low o info | Low o Informational | No |
| Sentinel o Defender | High, Medium, Low, Informational | Se conserva | Ya está en el plano. No se recrea. |

### Reglas de deduplicación

1. Misma idempotencyKey: no se crea otro incidente. Se actualiza el existente si cambió el estado de origen.
2. Misma cuenta, mismo dispositivo o misma IP, con un incidente Microsoft abierto dentro de la ventana: no se crea otro. Se enlaza. La ventana inicial propuesta es de 6 horas. Es una decisión del cliente, no un valor de producto.
3. Dos notables de dos Splunk sobre las mismas entidades y la misma ventana: un solo incidente, dos enlaces.
4. Un incidente Defender y un notable Splunk del mismo usuario: un incident case. El notable se marca como enlazado.
5. Señal sin entidades y sin identificador estable: se rechaza y se cuenta como error de contrato. No se inventa un incidente para no perderla.

El almacén de idempotencia recomendado es Azure Table Storage, con la clave y una vigencia de 30 días. Un watchlist de Sentinel puede servir en un piloto de bajo volumen, pero no es el candado de concurrencia. Dos ejecuciones simultáneas del mismo notable deben producir un solo incidente. Eso se prueba, no se supone.

## 8. Patrones de integración con Splunk on-prem

El patrón correcto mueve señales y estado. El patrón incorrecto mueve terabytes. CEF o syslog vía Azure Monitor Agent sirve para dispositivos que deban detectar en Sentinel. No sirve para volcar Splunk dentro de Sentinel y llamar a eso integración SOAR.

### Patrón preferido: Splunk llama, Logic Apps responde por camino privado

1. Una alert action o un webhook de Splunk, solo para notables de la lista blanca, hace HTTPS de salida hacia el trigger del flujo. Splunk ya suele poder salir. No hace falta publicar Splunk.
2. El trigger exige un secreto rotado o una firma. La URL no es la autenticación.
3. Logic Apps crea o enlaza el incidente y guarda la idempotencyKey.
4. El camino de vuelta, para actualizar el notable por la REST API de Splunk, sale de un Logic App Standard unido a la red del cliente por VPN, ExpressRoute o un equivalente privado. El token está en Key Vault y lo lee una identidad administrada.
5. Si el camino de vuelta no está listo, se puede federar de ida y dejar el notable en un estado 'enviado al SOC Microsoft'. No se abre Splunk a Internet para completar el piloto.

### Patrón alternativo: Logic Apps consulta

Si Splunk no puede iniciar la salida, un flujo Standard en red virtual consulta la API de notables en un intervalo corto. Es menos inmediato y más frágil si la consulta es amplia. Solo se usa si el patrón preferido es imposible. La consulta filtra por severidad y por tiempo. No hace un search libre cada minuto.

### Lo que no se hace

- Reenviar todos los logs de Microsoft 365 a Splunk y también al grant de Sentinel.
- Reenviar todas las alertas de Defender a Splunk para que el SOC legado no pierda visibilidad. La visibilidad se gana con acceso al portal, no con una segunda cola.
- Usar el notable como sistema de registro de la investigación. El registro es el case, su actividad y SecurityCaseEvent.
- Dejar que una búsqueda de Splunk deshabilite una cuenta de Entra. Esa acción vive en un playbook con aprobación.
- Guardar el token de Splunk en el plugin de Security Copilot, en el código del flujo o en un correo.

Más adelante, cuando una detección de Splunk tenga equivalente en Defender o en Sentinel y la fuente ya tenga dueño Microsoft, se apaga la regla de Splunk. La experiencia de migración de SIEM de Sentinel, que analiza detecciones de Splunk y recomienda contenido, es una herramienta de esa fase de reducción. No es el bus de respuesta.

## 9. Estándares de Logic Apps para este SOAR

Un playbook de producción cumple el estándar o no se conecta a una automation rule. El estándar es corto a propósito.

| Estándar | Regla |
| --- | --- |
| Nombre | soarr-<dominio>-<accion>-<entorno>. Ejemplo: soar-splunk-promote-notable-prod. |
| Entornos | Desarrollo y producción separados. Un flujo no se prueba contra el tenant productivo de identidad. |
| Identidad | Identidad administrada. Sin conexiones de usuario. |
| Secretos | Key Vault. Rotación acordada con quien administra Splunk. |
| Permiso de Sentinel | Microsoft Sentinel Automation Contributor en el grupo de recursos, otorgado a la cuenta de servicio de automatización. |
| Entrada | Solo el contrato de señal o el identificador del incidente. No un log completo. |
| Idempotencia | Toda creación de incidente comprueba la clave antes de crear. |
| Aprobación | Contención de identidad, aislamiento de dispositivo y cualquier cambio en un control de producción esperan aprobación. El timeout tiene un resultado explícito: no actuar. |
| Fallo | Si Splunk no responde, el case sigue. Se registra el fallo. No se revierte una contención ya hecha solo porque el notable no se actualizó. |
| Salida | El flujo escribe en el incidente qué hizo, qué no pudo hacer y el enlace de origen. |
| Cambio | El flujo se exporta y se versiona. No hay ediciones de producción sin registro. |
| Observabilidad | Run history, SentinelHealth para la automatización de Sentinel, y una métrica de fallos del bus. |

### Consumption o Standard

No es una elección religiosa. Un playbook que solo enriquece un incidente de Sentinel con conectores de Microsoft puede vivir en Consumption. El flujo que debe alcanzar Splunk por red privada vive en Standard. Mezclar el token de Splunk dentro de decenas de playbooks Consumption es un error. Hay un flujo de ida, un flujo de vuelta y playbooks de acción. Los demás llaman a esos, no reimplementan el cliente HTTP de Splunk.

### Acciones que el playbook puede ejecutar

Dentro de Microsoft, se prefieren conectores soportados: Microsoft Sentinel, Microsoft Defender for Endpoint, Microsoft Entra ID, Microsoft Teams, Key Vault y el conector de Security Copilot para disparar un agente ya publicado. Aislar un dispositivo o revocar sesiones son acciones nativas. El playbook las llama. No se sustituyen por scripts propios si el conector cubre el caso. Fuera de Microsoft, el único cliente HTTP de producción en la primera etapa es Splunk, más el sistema de tickets si el cliente decide que existe y que no será una tercera cola.

> **Tickets.** Si hay ServiceNow u otro ITSM, se elige una regla y se escribe en el registro de decisiones. O el case es la cola del SOC y el ticket es el registro de negocio, sincronizado por un solo playbook, o no se sincroniza. Dos colas con sincronización parcial son peores que una.

## 10. Case management como cola única

El case no reemplaza al SIEM. Reemplaza a la costumbre de investigar en la herramienta que disparó la alerta. Esa costumbre no sobrevive a dos SIEM.

### Cuándo se usa cada tipo

| Situación | Objeto | Quién lo crea |
| --- | --- | --- |
| Incidente de Defender o de Sentinel | Incident case | El producto, al existir el incidente y estar el workspace conectado. |
| Notable de Splunk prioritario, sin incidente equivalente | Incidente de Sentinel y, por tanto, incident case | Logic Apps, vía el conector o la API de incidentes de Sentinel. |
| Notable que coincide con un incidente abierto | El incident case ya existente, más un comentario y un tag de enlace | Logic Apps. No crea otro. |
| Caza, mejora de detección, seguimiento de un control, trabajo entre equipos | Generic case | Un analista, en el portal. Puede enlazar el incidente si después aparece. |
| Pregunta de un agente o un resumen | No es un case. Es una sesión o un comentario | No se abre un case por cada prompt. |

### Mínimo que debe tener la plantilla

- Tag o campo sourceSystem.
- Tag o campo sourceInstance.
- Campo sourceEventId, para soporte y para la idempotencia humana.
- SLA por severidad, aunque al principio sea único.
- Estado de federación: nuevo, enlazado, actualizado en origen, error de origen.
- Dueño. Un case sin dueño no está en operación.

Cerrar el incident case sincroniza el estado con el incidente. Las alertas relacionadas no se cierran solas. La clasificación y las notas de cierre quedan en el case y en el incidente. El playbook de cierre debe esperar a esa clasificación antes de decirle a Splunk que el notable está resuelto. Si se cierra el notable primero, el SOC legado cree que el trabajo terminó cuando el analista todavía no clasificó.

Las automation rules documentadas pueden disparar playbooks ante un case, un incidente o una alerta. En el tenant hay que confirmar que el disparador de case está disponible en la experiencia del portal, porque la superficie se está moviendo desde Azure. Hasta confirmarlo, el disparador seguro es el incidente.

El portal multitenant de Defender es el lugar documentado para ver y gestionar cases entre tenants. No se construye un Logic App que fusione tenants de clientes distintos en un solo case. Si el cliente tiene más de un tenant, cada tenant tiene su plano de trabajo y, si hace falta una vista de grupo, se usa la capacidad multitenant, no una base de datos paralela.

## 11. Security Copilot y el camino a un SOC agéntico

Un SOC agéntico no es un SOC sin personas ni un conjunto de flujos con un modelo de lenguaje pegado encima. Es un SOC donde el trabajo repetido de contexto, clasificación y preparación lo hace un agente con identidad, alcance y memoria de retroalimentación, y donde la acción que cambia el entorno sigue siendo determinista. Microsoft documenta agentes que razonan, planifican según disparadores, recuerdan según su diseño y actúan solo dentro de los permisos concedidos. También documenta que el cliente conserva el control.

### Orden correcto de autonomía

1. Consola única y case con dueño. Sin esto, el agente no tiene un lugar donde dejar el trabajo.
2. Playbooks deterministas de enriquecimiento, notificación, federación y contención con aprobación. Sin esto, el agente inventa el camino de acción.
3. Security Copilot asistido: el analista pide un resumen del incident case, una hipótesis o una consulta. El promptbook de triaje estandariza esa petición.
4. Skill de solo lectura hacia Splunk, implementada como Logic App. El agente puede pedir contexto que solo está on-prem. No puede cambiar el notable por este skill.
5. Agente de triaje con identidad propia, permiso de lectura y permiso para escribir un comentario o una tarea, no para contener.
6. El agente recomienda una acción. El playbook la ejecuta después de aprobación humana.
7. Solo para acciones reversibles y de bajo impacto, y solo después de meses de medición, se evalúa quitar la aprobación. Esa decisión se escribe. No se hereda de un piloto.
8. Sesiones agénticas nativas del incident case, si Project Perception está disponible en el tenant. Si no lo está, el paso anterior ya es un SOC agéntico defendible.

### Alcance escrito de un agente

Cada agente que se encienda tiene cuatro líneas visibles para el CISO: qué lo dispara, qué datos puede leer, qué acciones puede ejecutar solo, y qué acciones le están prohibidas aunque el modelo las proponga. La prohibición inicial incluye deshabilitar cuentas, revocar sesiones, aislar dispositivos, borrar evidencias, cerrar incidentes como falso positivo sin una persona, y modificar reglas de detección. Si el alcance no cabe en una página, el agente está mal recortado.

> **El camino crítico no depende del modelo.** Si Security Copilot no tiene SCU, si el agente falla o si el analista no está de acuerdo con el resumen, el notable sigue pudiendo convertirse en incident case y la contención sigue pudiendo aprobarse en el playbook. Un SOC agéntico que se cae cuando se cae el modelo no es más maduro. Es más frágil.

La retroalimentación importa. Los agentes documentados aprenden de la corrección del analista. Eso solo funciona si el analista corrige en el producto, no en un chat paralelo. El case es donde queda la corrección: clasificación, notas y, cuando exista, la evaluación de la sesión.

## 12. Modelo operativo

| Rol | Responsabilidad en esta arquitectura | No hace |
| --- | --- | --- |
| CISO o responsable de SOC | Firma la cola única, el umbral de federación y el alcance de autonomía. | No pide una copia de todos los logs 'por si el otro SIEM falla'. |
| Arquitectura | Mantiene el contrato, la landing zone y la matriz de propiedad de datos. | No abre conectores nuevos sin dueño de la fuente. |
| Ingeniería de detección Microsoft | Reglas y hunting dentro del beneficio y de Defender XDR. | No reimplementa en Sentinel lo que Defender ya detecta, sin un hueco demostrado. |
| Ingeniería de Splunk | Calidad del notable, lista blanca y camino de salida HTTPS. | No contiene identidades de Entra desde una búsqueda. |
| Ingeniería de automatización | Playbooks, idempotencia, secretos, pruebas de fallo. | No edita producción para un incidente en curso. |
| Analista de turno | Trabaja el case, aprueba contenciones, clasifica al cerrar. | No cierra el notable a mano si el playbook de vuelta existe. |
| Responsable de Security Copilot | SCU, plugins, identidad del agente y revisión del alcance. | No concede al agente el rol que usaría un respondedor humano. |

### Métricas mínimas

- Tiempo desde el notable hasta el incident case, para señales federadas.
- Porcentaje de notables federados que crearon un duplicado. El objetivo inicial es cero duplicados en la prueba, y luego una tasa revisada cada mes.
- Porcentaje de incident cases con playbook de enriquecimiento ejecutado.
- Porcentaje de contenciones con aprobación registrada.
- Fallos del camino de vuelta a Splunk.
- Consumo del grant de 5 MB/usuario/día y del allowance de 500 MB/nodo/día, contra el desborde facturado.
- Número de fuentes en estado 'ambos temporal' sin fecha de salida. Debe tender a cero.

No se exige, en la primera fase, un MTTR de industria. Se exige que el SOC pueda explicar, con evidencia, cuánto tardó la federación y si el analista trabajó una cola o dos.

## 13. Seguridad de la automatización

Un SOAR mal aislado es un camino de movimiento lateral con logo de automatización. El diseño asume que un playbook será un objetivo.

- Identidad administrada por flujo o por grupo de flujos del mismo dominio. No una identidad única que pueda contener, leer Splunk y cambiar reglas.
- El rol Automation Contributor permite a Sentinel ejecutar playbooks del grupo de recursos. Por eso los playbooks de producción viven en un grupo dedicado, no junto a flujos de negocio.
- Key Vault con firewall. El token de Splunk no se registra en el run history. Las entradas del flujo se redactan si pueden contener secreto o dato de más.
- La URL del trigger no basta. Hay autenticación y, si el origen es estable, restricción de red.
- Aprobación de dos personas para contención de cuentas privilegiadas. Una persona basta, al principio, para una cuenta estándar, si el cliente lo escribe así.
- El timeout de la aprobación no contiene. Contener por silencio es inaceptable.
- Separación de entornos. El flujo de desarrollo no tiene el conector de Entra de producción.
- Prueba de restauración: se puede deshabilitar el bus de federación sin deshabilitar Defender. Si el bus se apaga, las detecciones Microsoft siguen en el portal.
- Registro: run history, cambios de flujo versionados, SecurityCaseEvent, y la traza de quién aprobó.
- El agente de Security Copilot tiene una identidad distinta de la identidad del playbook de contención. Que el agente pueda llamar al playbook no significa que pueda saltarse la aprobación.

## 14. Costos, beneficios y anti-patrones

### Dónde está el valor

- Dejar de pagar dos veces la investigación del mismo ataque Microsoft.
- Usar el grant de hasta 5 MB/usuario/día y el allowance de 500 MB/nodo/día para lo que sí cubren, y ver el desborde.
- No migrar a Sentinel el volumen on-prem que Splunk ya retiene, hasta que una detección concreta lo merezca.
- Reducir trabajo manual de contexto con Copilot, sin pagar SCU para acciones que un playbook ya hace mejor.

### Anti-patrones

| Anti-patrón | Por qué falla | En su lugar |
| --- | --- | --- |
| Copiar Splunk a Sentinel para poder usar playbooks | Paga ingesta, duplica detección y no mejora la cola. | Federar notables y consultar bajo demanda. |
| Exportar alertas de Defender a Splunk | Crea la segunda cola que esta arquitectura quiere cerrar. | Dar acceso al portal y enlazar notables solo cuando Splunk vio algo que Defender no vio. |
| Un playbook por cada regla de Splunk | No se puede operar ni revisar. | Un flujo de promoción y playbooks por tipo de acción. |
| Contención automática el primer mes | Un falso positivo privilegiado es un incidente de disponibilidad. | Aprobación humana hasta tener tasa de error medida. |
| Agente con rol de respondedor | El modelo no es un control de cambio. | Identidad de lectura y playbook con aprobación. |
| Generic case como incidente falso | Pierde correlación, entidades y acciones nativas. | Crear incidente de Sentinel si merece respuesta. |
| Seguir operando Sentinel solo en el portal de Azure | Esa experiencia se retira el 31 de marzo de 2027 y no tiene cases. | Conectar el workspace y mover el trabajo diario. |
| Prometer UEBA o SCU dentro de E5 | No están en el beneficio de ingesta. | Presupuestar aparte o no diseñar sobre ellos. |
| Dos Logic Apps que deshabilitan al mismo usuario | Carrera y doble acción. | Una acción de identidad, con candado por objeto. |
| Medir madurez por número de playbooks | Se pueden tener cincuenta flujos inútiles. | Medir duplicados, tiempo de federación y acciones auditadas. |

## 15. Plan por fases

El plan detallado, con pasos para construir o para validar lo que ya existe, está en el Excel y en las secciones de plan de este mismo modelo. Aquí está la lógica de las fases. No se salta de fase porque un fabricante lo enseñe en una diapositiva. Se salta cuando los controles de la fase anterior tienen evidencia.

| Fase | Resultado | No empezar la siguiente si |
| --- | --- | --- |
| F0 Descubrimiento | Inventario de SIEM, beneficios, playbooks, red de Splunk y cola real del analista. | No se sabe qué workspace factura ni quién trabaja las alertas hoy. |
| F1 Consola y beneficio | Sentinel en el portal de Defender, Plan 2 confirmado, consumo de beneficios medido, matriz de datos firmada. | El trabajo diario sigue en el portal de Azure o no hay cifra de desborde. |
| F2 Landing zone | Logic Apps con identidad, Key Vault, entorno y camino de red decidido. | El secreto de Splunk estaría en un flujo personal. |
| F3 Cases | Plantillas, SLA, RBAC y prueba de que un incidente aparece como incident case. | No hay campos de procedencia. |
| F4 Federación | Notables prioritarios crean o enlazan un incidente, con idempotencia probada. | Una prueba genera dos cases. |
| F5 Playbooks de acción | Enriquecer, notificar, contener con aprobación, cerrar y actualizar el notable. | La contención no tiene timeout explícito. |
| F6 Copilot asistido | SCU, promptbook de triaje y skill de lectura a Splunk. | El camino crítico se diseñó dentro del prompt. |
| F7 Medición | Métricas de la sección operativa, revisión mensual de duplicados y de datos. | No hay evidencia de un mes de operación. |
| F8 Agentes | Un agente de triaje con alcance de una página. Project Perception solo si el tenant lo tiene. | El agente puede contener. |
| F9 Reducción de Splunk | Se apagan detecciones duplicadas con fecha. El SIEM on-prem se queda con lo que aún no tiene dueño. | Se apaga Splunk por calendario, no por evidencia. |

Un cliente puede estar en F5 para identidad Microsoft y en F0 para Splunk. El Excel permite ese desnivel. La guía no obliga a un programa de nueve trimestres si la federación todavía no tiene caso. Obligatorio desde el primer día, si Sentinel ya está en uso, es F1: consola unificada y verdad sobre el beneficio. El resto se prioriza por dónde está el dolor del turno.

## 16. Cómo validar lo que ya funciona

Antes de construir, se recorre el plan en modo validación. Un paso puede cerrarse como 'ya existe' solo con evidencia, no con una demo antigua. La evidencia mínima es una captura, un identificador de incidente, un run id de Logic Apps o una fila del usage export. El Excel tiene la columna para pegarla.

- Portal: abrir un incidente reciente y comprobar si el trabajo se hace en security.microsoft.com como case, o todavía en el portal de Azure.
- Beneficio E5: en el usage export, filtrar el workspace y el medidor Free Benefit - M365 Defender Data Ingestion. Anotar gigabytes de los últimos 31 días y compararlos con usuarios E5 por 5 MB.
- Servers Plan 2: confirmar el plan en el workspace, no solo en la suscripción, y el medidor Standard Data Included per Node. Revisar si se están ingeriendo canales no cubiertos.
- Playbooks: inventario de flujos, tipo Consumption o Standard, identidad de cada conexión y si Automation Contributor está asignado.
- Splunk: una prueba controlada de un notable de laboratorio. Contar cuántos incidentes aparecen. El resultado válido es uno, o cero si la prueba debía enlazarse a uno existente.
- Aprobación: ejecutar el playbook de contención en un entorno de prueba y no aprobar. Confirmar que no hubo cambio en Entra ni en el dispositivo.
- Copilot: confirmar SCU y que un promptbook no es el único camino para enriquecer.
- Duplicados: tomar cinco incidentes High de la última semana y buscar el mismo usuario en Splunk. Anotar si hubo dos trabajos humanos.

Si la prueba de Splunk no se puede hacer todavía porque la red no está decidida, el control queda en No evaluado. No se marca Cumple por diseño. El HTML y el Excel distinguen Cumple, Parcial, No cumple y No evaluado.

## 17. Criterios de assessment

El assessment usa una escala de 0 a 4. El Excel calcula el nivel ponderado solo con las preguntas respondidas. Una pregunta en blanco no suma como cero: significa que todavía no se evaluó. El peso 3 está reservado a lo que, si falla, rompe la cola única o la seguridad de la acción.

Las preguntas, los pesos y la guía de qué es bueno están en el modelo, en el HTML interactivo y en la hoja Assessment del Excel. No se mantiene una cuarta redacción. Si se cambia un criterio, se cambia aquí y se regeneran los archivos, o se versiona el cambio en el registro de decisiones del Excel.

## 18. Catálogo inicial de playbooks

Ocho flujos cubren la primera operación. No se construyen ocho el mismo mes. El orden de la tabla es el orden recomendado. El estado vivo se lleva en el Excel.

| Orden | Playbook | Disparador | Acción | Aprobación |
| --- | --- | --- | --- | --- |
| 1 | Promover o enlazar notable | HTTP desde Splunk o consulta acotada | Normalizar, deduplicar, crear incidente o enlazar | No |
| 2 | Enriquecer incidente | Automation rule al crear incidente | Identidad, dispositivo, alertas relacionadas, enlace de origen | No |
| 3 | Notificar al turno | Después del enriquecimiento, solo High | Mensaje a Teams con enlace al case, no un volcado | No |
| 4 | Actualizar notable | Cambio de estado del incidente | Escribir estado y enlace del case en Splunk | No |
| 5 | Contener identidad | Manual desde el case, o recomendación del agente | Revocar sesiones o deshabilitar cuenta por conector de Entra | Sí |
| 6 | Aislar dispositivo | Manual desde el case | Aislar con el conector de Defender for Endpoint | Sí |
| 7 | Cerrar de forma coordinada | Clasificación completada | Cerrar notable y registrar clasificación. No cerrar alertas a ciegas. | No, si la clasificación ya es humana |
| 8 | Pedir triaje al agente | Automation rule o acción del analista | Disparar el agente o el promptbook. El agente no contiene. | No para pedir triaje. Sí para cualquier acción que el triaje recomiende. |

## 19. Límites de esta guía

- Verificada contra documentación pública de Microsoft el 11 de noviembre de 2026. Los productos en preliminar, en especial incident cases y agentes, pueden cambiar.
- No se inspeccionó el tenant del cliente. Todo control nace en No evaluado.
- No se afirma un conector oficial de escritura de generic cases. No se afirma un conector oficial de Splunk sin revisarlo en el catálogo el día de la implementación.
- Las cifras de 5 MB por usuario por día y 500 MB por nodo por día son las publicadas. El ahorro en dinero depende del precio efectivo, la región y el modelo de medidor.
- Project Perception se menciona solo como condición documentada para sesiones agénticas dentro del incident case. No se describe su funcionamiento interno.
- Esta guía no es asesoramiento legal, no clasifica datos del cliente y no autoriza a conectar Splunk ni a crear incidentes en su nombre.
- La lista de tablas del grant E5 se cita como categorías de la oferta. El mapeo fino a tablas del workspace se confirma en el usage export antes de apagar una fuente en Splunk.

## 20. Fuentes verificadas

Fecha de verificación: 11 de noviembre de 2026. Si una página cambia, manda la página, no este archivo.

- Oferta de beneficio de Microsoft Sentinel para Microsoft 365 E5, A5, F5 y G5: https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/
- Facturación y fuentes gratuitas de Microsoft Sentinel: https://learn.microsoft.com/azure/sentinel/billing
- Beneficio de ingesta de Defender for Cloud: https://learn.microsoft.com/azure/defender-for-cloud/data-ingestion-benefit
- Cómo ver los beneficios en Azure Monitor: https://learn.microsoft.com/azure/azure-monitor/fundamentals/cost-usage
- Case management en el portal de Defender: https://learn.microsoft.com/defender-xdr/siem-defender-case-management
- Gestionar incident cases: https://learn.microsoft.com/defender-xdr/manage-incident-cases
- Gestionar generic cases: https://learn.microsoft.com/defender-xdr/manage-cases
- Playbooks y automation rules: https://learn.microsoft.com/azure/sentinel/automate-responses-with-playbooks
- Disparar agentes de Security Copilot desde Logic Apps: https://learn.microsoft.com/copilot/security/connector-logicapp-agent-trigger
- Plugin de Logic Apps en Security Copilot: https://learn.microsoft.com/copilot/security/developer/plugin-logic-apps
- Información general de agentes: https://learn.microsoft.com/copilot/security/agents-overview
- Tarjeta de aplicación de agentes de Security Copilot: https://learn.microsoft.com/copilot/security/security-copilot-application-card-agents
- UEBA no incluido en E5: https://learn.microsoft.com/defender-xdr/extend-ueba
- Qué es Microsoft Sentinel, incluida la retirada del portal de Azure: https://learn.microsoft.com/azure/sentinel/sentinel-overview

## 21. Cómo usar los cuatro archivos

El JSON es el modelo canónico. El Markdown es la misma guía para lectura y diff. El HTML renderiza el mismo modelo y añade assessment, plan y controles interactivos. El Excel es la guía de trabajo: se completa en el cliente, calcula madurez y avance, y es la base que actualiza el estado del HTML.

1. Leer la respuesta directa y la arquitectura antes de abrir el assessment. Sin esa decisión, las puntuaciones no significan nada.
2. Completar en el Excel las hojas Assessment, Plan, Controles, Inventario, Propiedad de datos y Playbooks. Las celdas de entrada están marcadas. No se escriben encima de las fórmulas.
3. Copiar la hoja Estado_HTML, incluidos los encabezados, y pegarla en el HTML en Actualizar desde Excel. El HTML reemplaza niveles, estados y resultados. No reescribe la guía.
4. Exportar desde el HTML el estado JSON si se quiere guardar una foto sin volver a copiar. Esa foto no sustituye al Excel: el Excel sigue siendo la base editable.
5. Cuando cambie un criterio de la guía, se versiona el modelo y se regeneran Markdown, JSON y HTML. Las evidencias del cliente viven en el Excel, no dentro de la prosa.

> **Contrato de actualización.** La hoja Estado_HTML tiene las columnas Tipo, Clave, Campo y Valor. El HTML reconoce assessment/nivel, plan/estado, control/resultado y meta/fecha_estado. Si se agregan filas al Excel a mano, el HTML las ignora hasta que existan en el modelo. Así la guía y el assessment no se desfasan en silencio.

## Assessment

Escala: 0 no existe, 1 ad hoc, 2 definido, 3 operado, 4 optimizado. Una pregunta sin responder no cuenta como cero.

| ID | Dominio | Peso | Pregunta | Qué es bueno |
| --- | --- | --- | --- | --- |
| A01 | Consola unificada | 2 | El trabajo diario de incidentes de Sentinel se hace en el portal de Defender, no en el portal de Azure. | Un incidente reciente se abre como incident case en security.microsoft.com y el equipo de turno no necesita el portal de Azure para asignarlo o cerrarlo. |
| A02 | Consola unificada | 2 | Hay un workspace primario acordado para el beneficio, la correlación y la conexión al portal. | El inventario nombra un workspace primario. Cualquier otro tiene una razón escrita de residencia, soberanía o blast radius. |
| A03 | Beneficio E5 | 2 | Se conoce el consumo del grant de hasta 5 MB por usuario por día y qué fuentes lo están usando. | Hay una cifra de los últimos 31 días del medidor Free Benefit - M365 Defender Data Ingestion y una lista de conectores asociados. |
| A04 | Beneficio E5 | 3 | No se ingieren en Sentinel datos fuera del grant sin una decisión de costo y un dueño. | Cada conector de pago tiene una fila en la matriz de propiedad con decisión y, si sigue, un motivo. |
| A05 | Defender for Servers P2 | 2 | Plan 2 está habilitado en el workspace al que reportan los servidores y el allowance se ve en uso o en el export. | No basta con el plan en la suscripción. El medidor Standard Data Included per Node aparece para ese workspace. |
| A06 | Defender for Servers P2 | 2 | Los canales de eventos no cubiertos no se confunden con el allowance de 500 MB. | Application, System y otros canales están identificados como ingesta facturable o están apagados. |
| A07 | Propiedad de la detección | 3 | Cada fuente tiene un solo sistema de detección dueño, o una duplicación con fecha de salida. | La hoja de propiedad no tiene filas 'ambos' sin fecha. El analista sabe dónde nace la detección. |
| A08 | Propiedad de la detección | 3 | Las alertas de Defender no se reexportan a Splunk para formar una segunda cola. | No hay un reenvío general de alertas XDR hacia notables. Las excepciones están nombradas. |
| A09 | Case management | 2 | Las plantillas tienen campos o tags de procedencia, SLA y un RBAC que separa ver, gestionar y configurar. | sourceSystem, sourceInstance y sourceEventId caben en el case. Quien configura plantillas no es todo el turno. |
| A10 | Case management | 3 | El analista trabaja el incident case. Splunk no es la cola principal de los ataques que Microsoft ya correlacionó. | En una muestra de incidentes High, el registro de la investigación está en el case, no solo en el notable. |
| A11 | Logic Apps | 3 | Los playbooks de producción usan identidad administrada y no conexiones de una persona. | El inventario de conexiones no muestra cuentas nominativas en flujos productivos. |
| A12 | Logic Apps | 2 | Hay separación de entornos, flujos versionados y Automation Contributor en el grupo de recursos correcto. | Un cambio de producción tiene historia. La cuenta de servicio de Sentinel puede ejecutar el playbook. |
| A13 | Federación Splunk | 3 | Los notables prioritarios entran por un contrato único, con idempotencia probada. | Reenviar el mismo notable de laboratorio no crea un segundo incidente. |
| A14 | Federación Splunk | 3 | El camino de vuelta a Splunk no exige publicar el puerto de gestión en Internet. | La actualización del notable sale por red privada, o está explícitamente pendiente y la ida no depende de abrir Splunk. |
| A15 | Security Copilot | 1 | Hay capacidad SCU, un responsable y un promptbook de triaje usado por el turno. | Si no hay SCU, la puntuación puede ser 0 sin bloquear el resto. No se simula Copilot con un prompt suelto. |
| A16 | Security Copilot | 3 | Ningún agente tiene permiso directo de contención. La acción pasa por un playbook con aprobación. | La identidad del agente no puede deshabilitar cuentas ni aislar dispositivos por sí misma. |
| A17 | Aprobación y auditoría | 3 | Contener una identidad o aislar un dispositivo exige aprobación, y el silencio no contiene. | Una prueba sin aprobar no produce cambios. El timeout está documentado. |
| A18 | Aprobación y auditoría | 2 | Se puede reconstruir quién aprobó, qué flujo corrió y qué se escribió en Splunk y en el case. | Para un incidente de prueba existen run id, comentario en el case y resultado del notable. |
| A19 | Medición | 2 | Se miden duplicados, tiempo de federación y porcentaje de incidentes con playbook. | Hay una cifra del último periodo, aunque sea manual. No un objetivo de industria sin dato propio. |
| A20 | Preparación agéntica | 2 | El alcance de autonomía está escrito: qué puede hacer solo un agente y qué tiene prohibido. | Cabe en una página y nombra las prohibiciones de contención, cierre y cambio de reglas. |
| A21 | Multi-SIEM | 2 | Otra instancia de Sentinel o de Splunk se conectaría al mismo contrato, sin un SOAR nuevo. | El inventario tiene un lugar para la instancia y el flujo de promoción no está hardcodeado a un solo Splunk sin configuración. |
| A22 | Retiro del portal de Azure | 2 | Hay un plan fechado para operar Sentinel solo en el portal de Defender antes del 31 de marzo de 2027. | El plan tiene dueño. No depende de que el portal de Azure siga disponible. |

## Plan paso a paso

| ID | Fase | Paso | Objetivo | Construir | Validar si ya existe | Depende de | Rol |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P01 | F0 Descubrimiento | Inventariar workspaces de Sentinel | Saber cuántos planos de detección Microsoft existen antes de unir la cola. | Listar suscripción, workspace, región, workspace primario propuesto y si está conectado al portal de Defender. | Contrastar el inventario con el portal y con Azure Resource Graph o el listado de Sentinel. Un workspace no inventariado invalida el paso. |  | Arquitectura |
| P02 | F0 Descubrimiento | Identificar el modelo de facturación | Saber si el allowance de Plan 2 aplica a Log Analytics o a Sentinel. | Revisar si el workspace usa medidores clásicos o simplificados y anotarlo en el inventario. | Señalar la página de precios o el export que lo demuestra. Si no se puede distinguir, el paso queda abierto. | P01 | Arquitectura |
| P03 | F0 Descubrimiento | Inventariar Splunk | Conocer instancias, quién administra notables y si Splunk puede salir por HTTPS. | Registrar instancia, versión de la interfaz de notables, red de salida y responsable. No hace falta el token en esta fase. | El responsable de Splunk confirma por escrito la salida HTTPS o su imposibilidad. |  | Ingeniería de Splunk |
| P04 | F0 Descubrimiento | Inventariar playbooks y conexiones | No construir encima de flujos con cuentas personales. | Listar Logic Apps usadas por Sentinel, tipo, grupo de recursos e identidad de cada conexión. | Abrir cada flujo productivo y comprobar la conexión. El inventario sin abrir el flujo no valida. | P01 | Ingeniería de automatización |
| P05 | F0 Descubrimiento | Fotografiar la cola real | Saber dónde trabaja el analista hoy: portal, Azure, Splunk o un ticket. | Revisar cinco incidentes o notables High de las últimas dos semanas y anotar dónde quedó la investigación. | La muestra tiene identificadores. Una opinión del turno, sin identificadores, no cierra el paso. |  | Responsable de SOC |
| P06 | F0 Descubrimiento | Medir beneficios ya activos | Tener la línea base de 5 MB/usuario/día y de 500 MB/nodo/día. | Extraer del usage export los medidores Free Benefit - M365 Defender Data Ingestion y Standard Data Included per Node. | El archivo de export o la cifra de la página de uso está referenciada. Cero también es un dato, si el medidor existe. | P01 | Arquitectura |
| P07 | F1 Consola y beneficio | Conectar Sentinel al portal de Defender | Habilitar la consola unificada y los incident cases. | Conectar el workspace primario al portal y mover el trabajo diario. Planificar el abandono operativo del portal de Azure. | Un incidente nuevo se gestiona en security.microsoft.com. El equipo sabe que el portal de Azure se retira el 31 de marzo de 2027. | P01 | Arquitectura |
| P08 | F1 Consola y beneficio | Confirmar qué fuentes del grant ya ingresan | No activar conectores duplicados. | Mapear Entra sign-in y audit, shadow IT de Defender for Cloud Apps, Purview Information Protection y advanced hunting de Microsoft 365 contra lo que ya está conectado. | Cada categoría de la oferta tiene un estado: conectada, no aplica o pendiente de decisión. | P06 | Ingeniería de detección |
| P09 | F1 Consola y beneficio | Confirmar Plan 2 en el workspace de servidores | Activar el allowance donde realmente llegan los eventos. | Habilitar o verificar Defender for Servers Plan 2 en el workspace, y la solución Security si el allowance no aparece. | El allowance se ve en Usage and estimated costs o en el export después del cambio. | P02 | Arquitectura |
| P10 | F1 Consola y beneficio | Separar el desborde facturable | Que el beneficio no oculte ingesta de pago. | Listar tablas o conectores fuera del grant y fuera del allowance, con volumen de 31 días. | La lista alimenta la hoja de propiedad. Un conector de pago sin fila es un hallazgo, no un paso cerrado. | P06,P08,P09 | Arquitectura |
| P11 | F1 Consola y beneficio | Firmar la matriz de propiedad de datos | Decidir el dueño de cada fuente antes de federar. | Completar la hoja Propiedad_datos con decisión y, si hay duplicado temporal, fecha de salida. | El responsable de SOC y el de Splunk aceptan la matriz. Sin esa aceptación no hay F4. | P10,P03 | Responsable de SOC |
| P12 | F1 Consola y beneficio | Cerrar reexportaciones que crean segunda cola | Dejar de fabricar notables a partir de alertas que Defender ya correlaciona. | Identificar reenvíos de alertas XDR a Splunk y apagar los generales. Dejar solo excepciones con fecha. | Una alerta de prueba de Defender no abre un notable nuevo, salvo la excepción nombrada. | P11 | Ingeniería de Splunk |
| P13 | F2 Landing zone | Elegir el tipo de Logic App del bus | Poner el secreto y la red en el lugar correcto. | Crear Logic Apps Standard para ida y vuelta con Splunk si hace falta red privada. Dejar Consumption solo para playbooks Microsoft simples ya existentes. | El diseño de red está dibujado: quién inicia la conexión y qué puerto no se publica. | P03,P04 | Ingeniería de automatización |
| P14 | F2 Landing zone | Identidad, Key Vault y RBAC | Que el bus no dependa de una persona. | Asignar identidad administrada, guardar el token de Splunk en Key Vault y otorgar Automation Contributor a la cuenta de servicio de Sentinel en el grupo de recursos de playbooks. | Un playbook de prueba corre desde una automation rule sin conexión nominativa. | P13 | Ingeniería de automatización |
| P15 | F2 Landing zone | Separar entornos y versionar | Poder cambiar el bus sin editar en caliente. | Crear recurso de desarrollo sin conectores de identidad productivos. Exportar los flujos a un repositorio. | El flujo de desarrollo no puede deshabilitar un usuario real. El de producción tiene historia de versiones. | P14 | Ingeniería de automatización |
| P16 | F3 Cases | Definir plantillas y SLA | Que la procedencia quepa en el case. | Configurar campos o tags sourceSystem, sourceInstance, sourceEventId, estado de federación y un SLA inicial por severidad. | Un case de prueba muestra los campos. Quien no tiene permiso de configuración no puede cambiar la plantilla. | P07 | Responsable de SOC |
| P17 | F3 Cases | Acordar incident case frente a generic case | Evitar incidentes falsos y cases genéricos usados como SIEM. | Publicar la tabla de esta guía, ajustada al cliente, como criterio del turno. | El turno clasifica tres ejemplos reales con el mismo criterio. Los desacuerdos se escriben en Decisiones. | P16 | Responsable de SOC |
| P18 | F3 Cases | Probar el incident case extremo a extremo | Confirmar que el on-ramp de automatización existe en este tenant. | Crear o usar un incidente de laboratorio y gestionarlo como incident case: asignar, comentar, clasificar, cerrar. | El cierre del case se refleja en el incidente. Se anota si el disparador de automation rule sobre case está disponible. Si no, se usa el disparador de incidente. | P07,P16 | Arquitectura |
| P19 | F3 Cases | Confirmar auditoría de cases | Tener un registro fuera de la memoria del analista. | Consultar SecurityCaseEvent para el case de prueba y fijar retención. | La consulta devuelve la creación y el cambio de estado del case de prueba. | P18 | Ingeniería de detección |
| P20 | F4 Federación | Firmar contrato y mapa de severidad | Que Splunk y Microsoft emitan el mismo objeto. | Acordar campos obligatorios, umbral y ventana de deduplicación. La propuesta inicial es federar High y una ventana de 6 horas. | La decisión está en la hoja Decisiones, con nombres. Un contrato solo en un chat no cierra el paso. | P11,P17 | Responsable de SOC |
| P21 | F4 Federación | Implementar la idempotencia | Impedir el doble incidente. | Tabla de Azure con la clave sourceSystem, sourceInstance y sourceEventId, vigencia de 30 días, y una prueba de dos ejecuciones simultáneas. | Dos entregas del mismo notable de laboratorio producen un incidente. | P14,P20 | Ingeniería de automatización |
| P22 | F4 Federación | Promover un notable a incidente | Entrar al plano de trabajo sin copiar logs. | Webhook autenticado desde Splunk, o consulta acotada si la salida es imposible. Crear incidente de Sentinel con entidades, enlace y clave. | El notable de laboratorio aparece como un incident case. El log crudo no aparece como ingesta nueva. | P21,P18 | Ingeniería de automatización |
| P23 | F4 Federación | Enlazar cuando el incidente ya existe | No duplicar un ataque que Defender ya abrió. | Buscar entidades en incidentes abiertos dentro de la ventana. Si hay coincidencia, comentar y etiquetar, no crear. | Un notable de laboratorio sobre un usuario que ya tiene incidente High no crea un segundo case. | P22 | Ingeniería de automatización |
| P24 | F4 Federación | Rechazar señales sin contrato | Que el volumen mal formado no ensucie la cola. | Si faltan identificador o severidad mapeada, no crear incidente. Contar el rechazo. | Un notable de prueba incompleto no crea case y sí deja un rastro de error. | P22 | Ingeniería de automatización |
| P25 | F5 Playbooks | Enriquecer y notificar | Dar contexto antes de pedir una decisión humana. | Playbook de enriquecimiento con conectores Microsoft y notificación a Teams solo para High, con enlace al case. | El incidente de laboratorio recibe un comentario de enriquecimiento y, si es High, un mensaje. El mensaje no contiene el log crudo. | P18,P14 | Ingeniería de automatización |
| P26 | F5 Playbooks | Contener identidad con aprobación | Tener una acción seria, reversible en el procedimiento, y nunca silenciosa. | Playbook manual que revoca sesiones o deshabilita la cuenta por el conector de Entra, con aprobación y timeout que no actúa. | Sin aprobar, la cuenta de prueba no cambia. Con aprobar, el cambio ocurre y queda el run id en el case. | P25 | Ingeniería de automatización |
| P27 | F5 Playbooks | Aislar dispositivo con aprobación | Usar la acción nativa, no un script paralelo. | Playbook manual con el conector de Defender for Endpoint y la misma regla de aprobación. | La prueba en un dispositivo de laboratorio no aísla si nadie aprueba. | P26 | Ingeniería de automatización |
| P28 | F5 Playbooks | Actualizar Splunk al cambiar el estado | Cerrar la segunda consola sin que el analista la opere. | Flujo de vuelta por camino privado. No marcar resuelto en Splunk hasta que el case esté clasificado. | El notable de laboratorio recibe el enlace del case y el estado. Si Splunk está caído, el case igual se puede cerrar y el fallo queda registrado. | P22,P13 | Ingeniería de automatización |
| P29 | F5 Playbooks | Probar el fallo y el candado de identidad | Saber cómo se comporta el bus cuando el entorno no coopera. | Simular token vencido, Splunk inalcanzable y dos aprobaciones de la misma cuenta. Confirmar un solo cambio de identidad. | El informe de prueba está referenciado. Un fallo no contiene por error y no duplica la acción. | P26,P28 | Ingeniería de automatización |
| P30 | F6 Copilot asistido | Confirmar SCU y responsable | No diseñar agentes sobre una capacidad inexistente. | Verificar capacidad, propietarios y que el camino de F4 y F5 funciona con Copilot apagado. | Si no hay SCU, este paso se marca No aplica y F6 se pospone. F5 no se deshace. | P25 | Responsable de Security Copilot |
| P31 | F6 Copilot asistido | Publicar un promptbook de triaje | Estandarizar la ayuda, no la acción. | Promptbook que resume el incident case, propone hipótesis y lista datos que faltan. No contiene acciones de escritura. | Dos analistas obtienen una estructura usable sobre el mismo incidente de laboratorio. La contención sigue en el playbook. | P30,P18 | Responsable de Security Copilot |
| P32 | F6 Copilot asistido | Exponer Splunk como skill de lectura | Dar contexto on-prem sin mover el secreto al agente. | Publicar el flujo de consulta como skill de Logic Apps. El flujo solo busca. Otro flujo, distinto, actualiza notables. | Un prompt recupera contexto del notable de laboratorio. El mismo skill no puede cambiar el notable. | P28,P31 | Ingeniería de automatización |
| P33 | F7 Medición | Operar un periodo y publicar cifras | Decidir con datos si se amplía la lista blanca. | Durante al menos cuatro semanas, registrar tiempo de federación, duplicados, fallos de vuelta, contenciones aprobadas y desborde de beneficio. | Las seis métricas de la guía tienen valor o una razón de no aplica. Se revisa la matriz de datos. | P23,P28,P29 | Responsable de SOC |
| P34 | F8 Agentes | Escribir el alcance de un agente de triaje | Poder explicarle a un CISO qué no puede hacer el agente. | Una página: disparador, datos, acciones permitidas y prohibiciones. Identidad distinta de la del playbook de contención. | La identidad del agente no tiene rol para deshabilitar cuentas ni aislar dispositivos. | P33,P32 | Responsable de Security Copilot |
| P35 | F8 Agentes | Encender el agente en laboratorio y luego en High | Automatizar contexto, no el juicio de cierre. | El agente comenta el case o completa una tarea de triaje. Recomendar contención dispara el playbook con aprobación, no la acción. | En laboratorio, una recomendación incorrecta no cambia Entra. El analista puede corregir la salida. | P34,P26 | Responsable de Security Copilot |
| P36 | F8 Agentes | Probar sesiones agénticas solo si hay acceso | Usar la capacidad nativa del incident case sin volverla dependencia. | Si el tenant tiene Project Perception, ejecutar un agentic playbook sobre un incident case de laboratorio y revisar la sesión desde el case. | Si no hay acceso, el paso se marca No aplica. El SOC agéntico de P35 no queda bloqueado. | P35,P18 | Arquitectura |
| P37 | F9 Reducción de Splunk | Elegir detecciones duplicadas con equivalente Microsoft | Reducir Splunk por evidencia, no por eslogan. | Listar reglas de Splunk cuya fuente ya tiene dueño en Defender o Sentinel y cuyo notable no aportó casos únicos en el periodo medido. | Cada regla candidata tiene equivalente, volumen y una fecha propuesta. No hay una lista vacía presentada como migración completa. | P33,P11 | Ingeniería de detección |
| P38 | F9 Reducción de Splunk | Apagar solo lo firmado y conservar el resto | Dejar Splunk como plano de lo que aún no tiene dueño Microsoft. | Apagar las reglas firmadas, mantener el contrato de señal para el resto y revisar a los 30 días si reapareció el hueco. | El inventario de Splunk distingue retirado, federado y pendiente. Ninguna fuente queda sin dueño. | P37 | Responsable de SOC |

## Controles

| ID | Fase | Control | Evidencia esperada |
| --- | --- | --- | --- |
| C01 | F1 | El workspace primario está conectado al portal de Defender. | Incidente abierto en security.microsoft.com. |
| C02 | F1 | El medidor Free Benefit - M365 Defender Data Ingestion se revisó para el workspace. | Export o captura de los últimos 31 días. |
| C03 | F1 | Defender for Servers Plan 2 está habilitado en el workspace de los servidores. | Configuración del workspace, no solo de la suscripción. |
| C04 | F1 | El allowance de 500 MB se distingue de los canales no cubiertos. | Nota de canales Application o System, o constancia de que no se ingieren. |
| C05 | F1 | La matriz de propiedad tiene dueño y no tiene duplicados sin fecha. | Hoja Propiedad_datos firmada en Decisiones. |
| C06 | F2 | Los flujos productivos no usan conexiones de una persona. | Inventario de conexiones. |
| C07 | F2 | Automation Contributor está asignado en el grupo de recursos de los playbooks. | Asignación de rol. |
| C08 | F2 | El secreto de Splunk, si ya existe, está en Key Vault. | Referencia del secreto, no el secreto. |
| C09 | F3 | La plantilla puede guardar sistema, instancia e identificador de origen. | Case de prueba. |
| C10 | F3 | Un incidente de Sentinel se gestiona como incident case. | Identificador de incidente y de case. |
| C11 | F3 | SecurityCaseEvent registra el case de prueba. | Consulta. |
| C12 | F4 | El mismo notable no crea dos incidentes. | Prueba de idempotencia con identificadores. |
| C13 | F4 | Un notable de una entidad que ya tiene incidente no crea otro case. | Prueba de enlace. |
| C14 | F4 | La promoción no ingiere el log crudo de Splunk. | Ausencia de conector de volcado y volumen sin cambio atribuible a la prueba. |
| C15 | F5 | No aprobar la contención equivale a no actuar. | Prueba de timeout o rechazo en laboratorio. |
| C16 | F5 | El notable recibe estado por un camino que no publica Splunk en Internet. | Diseño de red o resultado de la actualización. |
| C17 | F6 | El triaje de Copilot no es el único camino de enriquecimiento. | Playbook de enriquecimiento ejecutable con Copilot deshabilitado. |
| C18 | F6 | El skill de Splunk usado por Copilot es de solo lectura. | Prueba de que no actualiza el notable. |
| C19 | F8 | La identidad del agente no puede contener. | Roles de la identidad del agente. |
| C20 | F1 | Hay fecha y dueño para dejar de operar Sentinel en el portal de Azure antes del 31 de marzo de 2027. | Fila en Decisiones o en el plan. |

## Catálogo de playbooks

| ID | Orden | Nombre | Disparador | Acción | Aprobación | Fase |
| --- | --- | --- | --- | --- | --- | --- |
| PB01 | 1 | Promover o enlazar notable | HTTP desde Splunk o consulta acotada | Normalizar, deduplicar, crear incidente o enlazar | No | F4 |
| PB02 | 2 | Enriquecer incidente | Automation rule al crear el incidente | Añadir identidad, dispositivo, alertas relacionadas y enlace de origen | No | F5 |
| PB03 | 3 | Notificar al turno | Tras el enriquecimiento, solo High | Mensaje a Teams con enlace al case | No | F5 |
| PB04 | 4 | Actualizar notable | Cambio de estado del incidente | Escribir estado y enlace en Splunk por camino privado | No | F5 |
| PB05 | 5 | Contener identidad | Manual desde el case | Revocar sesiones o deshabilitar cuenta con el conector de Entra | Sí | F5 |
| PB06 | 6 | Aislar dispositivo | Manual desde el case | Aislar con el conector de Defender for Endpoint | Sí | F5 |
| PB07 | 7 | Cierre coordinado | Clasificación humana completada | Actualizar notable con la clasificación. No cerrar alertas relacionadas a ciegas. | No | F5 |
| PB08 | 8 | Pedir triaje | Analista o automation rule | Disparar promptbook o agente. Cualquier contención vuelve a PB05 o PB06. | No para pedir. Sí para actuar. | F6 |

## Matriz inicial de propiedad de datos

| ID | Fuente | Beneficio | Recomendación | Riesgo si se duplica |
| --- | --- | --- | --- | --- |
| D01 | Inicios de sesión y auditoría de Entra ID | Grant E5, hasta 5 MB/usuario/día | Sentinel, si cabe en el grant. Detección de identidad en Defender e Entra ID Protection. | Doble ingesta y dos colas para el mismo riesgo de identidad. |
| D02 | Shadow IT de Defender for Cloud Apps | Grant E5 | Sentinel solo si se usa para hunting o correlación. La detección de SaaS sigue en Defender. | Volumen de discovery copiado a Splunk sin un analista que lo trabaje. |
| D03 | Registros de Purview Information Protection | Grant E5 | Sentinel si el caso de uso es seguridad. No moverlos a Splunk por completitud. | Datos de clasificación fuera del plano de gobierno, sin mejora de respuesta. |
| D04 | Advanced hunting de Microsoft 365 | Grant E5, dentro del tope | Confirmar tablas en el usage export antes de depender de ellas. No asumir que todo Defender XDR entra en los 5 MB. | Desborde facturable y una copia más en Splunk. |
| D05 | Alertas de Defender XDR, Defender for Cloud y productos Defender asociados | Gratuitas en Sentinel para cualquier cliente | Dejar la alerta en el plano Microsoft. No reexportarla a Splunk. | Segunda cola. Es el anti-patrón principal de esta guía. |
| D06 | Azure Activity y auditoría de Office 365 incluida en la lista gratuita | Gratuita en Sentinel | Sentinel. Revisar si Splunk aún la necesita para un control que Defender no cubre. | Retención doble. Aceptable solo con fecha de salida. |
| D07 | Eventos de seguridad de servidores | Allowance de Plan 2, 500 MB/nodo/día, agregado por suscripción | Workspace con Plan 2, vía AMA o sensor de MDE. No contar Application ni System como beneficio. | Pagar en Sentinel el canal no cubierto y seguir detectando en Splunk. |
| D08 | Telemetría cruda de endpoint más allá de alertas y del grant | No asumir cobertura | Hunting en Defender. Ingerir en Sentinel solo con caso y cifra. | El costo más fácil de disparar por imitación de un SIEM legado. |
| D09 | Aplicaciones on-prem, OT y fuentes sin conector Microsoft | Ninguno | Splunk sigue como dueño. Se federa el notable, no el log. | Proyecto de migración disfrazado de SOAR. |
| D10 | Firewall, proxy y DNS de alto volumen | Ninguno por defecto | Decisión por volumen y por detección. Mientras no haya caso, Splunk detecta y Logic Apps promueve. | Ingesta de pago en Sentinel que no cambia la cola. |
| D11 | Logs crudos que solo hacen falta en una investigación puntual | No ingerir por anticipado | Consulta bajo demanda al sistema que ya los tiene, vía Logic App de lectura. | Retener dos veces un dato que se usa pocas veces al mes. |
| D12 | UEBA y otros análisis de pago de Sentinel | No incluido en E5 | No activar hasta tener presupuesto y un hueco que Defender no cubre. | Costo recurrente y una expectativa falsa de que E5 ya lo pagaba. |

## Decisiones que el cliente debe confirmar

| ID | Decisión | Estado | Nota |
| --- | --- | --- | --- |
| R01 | La cola del SOC es el case del portal de Defender. | Propuesta de esta guía | El cliente debe firmarla antes de federar. |
| R02 | Solo se federan notables High, más Medium de una lista blanca. | Propuesta inicial | Ventana de deduplicación propuesta: 6 horas. |
| R03 | No se copia el log crudo de Splunk a Sentinel para poder orquestar. | Regla de la guía | Una excepción exige fila en Propiedad_datos y cifra de costo. |
| R04 | La contención de identidad y dispositivo exige aprobación. El timeout no actúa. | Regla de la guía | Cuentas privilegiadas: evaluar doble aprobación. |
| R05 | Security Copilot no está en el camino crítico. | Regla de la guía | Si no hay SCU, F6 y F8 se posponen. |
| R06 | El secreto de Splunk vive en Key Vault y lo usa Logic Apps, no el agente. | Regla de la guía | Revisar el catálogo de conectores el día de la implementación. |
| R07 | Sentinel deja de operarse en el portal de Azure antes del 31 de marzo de 2027. | Fecha de producto | El trabajo en cases ya exige el portal de Defender. |
| R08 | Un segundo SIEM se conecta al mismo contrato. No crea otro SOAR. | Regla de la guía | Registrar la instancia antes de abrir el flujo. |

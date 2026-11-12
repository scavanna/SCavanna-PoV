# Evaluaciones y respuestas

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Cuánto tiempo retiene Audit (Standard) los registros generados desde el 17 de octubre de 2023?**

- a) 90 días
- b) 180 días  ✅
- c) Un año
- d) Diez años

*Respuesta: b).* La retención de Audit (Standard) pasó de 90 a 180 días para los registros generados desde esa fecha. Un año es la política predeterminada de Audit (Premium) y diez años requiere un complemento. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**2. ¿Cuándo retiró Microsoft todas las experiencias clásicas de eDiscovery (Content Search, Standard y Premium), salvo en los tenants operados por 21Vianet?**

- a) 26 de mayo de 2025
- b) 16 de febrero de 2026
- c) 31 de agosto de 2025  ✅
- d) 15 de octubre de 2027

*Respuesta: c).* El retiro completo fue el 31 de agosto de 2025. El 26 de mayo de 2025 se retiraron Content Search clásica y los casos Standard; el 16 de febrero de 2026 se limitaron las content searches, y el 15 de octubre de 2027 se retira Search-UnifiedAuditLog. [Fuente](https://learn.microsoft.com/en-us/purview/ediscovery) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Quién puede quitar miembros de un caso de eDiscovery?**

- a) La persona que creó el caso
- b) Cualquier eDiscovery Manager que sea miembro del caso
- c) Un integrante de Organization Management
- d) Un eDiscovery Administrator  ✅

*Respuesta: d).* eDiscovery Administrator ve todos los casos, configura la solución y es el único que puede quitar miembros. eDiscovery Manager solo trabaja en los casos donde es miembro. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. Un custodio tiene Microsoft 365 E3 sin complementos. ¿Qué hace falta para analizar sus datos con funciones premium?**

- a) Nada: basta con que quien revisa tenga E5
- b) Que el custodio tenga Purview Suite o el complemento «eDiscovery and Audit»  ✅
- c) Una licencia de Security Copilot para el custodio
- d) Que el caso lo cree un eDiscovery Administrator

*Respuesta: b).* La licencia premium la necesita el custodio cuyos datos se analizan: E5, o E1/E3 con Purview Suite o «eDiscovery and Audit». Los miembros del caso que recolectan y revisan no necesitan E5. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. En una búsqueda de eDiscovery, ¿qué significa un espacio entre dos términos?**

- a) AND
- b) NEAR
- c) Frase exacta
- d) OR  ✅

*Respuesta: d).* Un espacio equivale a OR. Para exigir ambos términos usa AND en mayúsculas y, para una frase exacta, comillas. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**6. ¿Qué devuelve una condición vacía en una búsqueda de eDiscovery?**

- a) Ningún resultado
- b) Todo el contenido del alcance de la búsqueda  ✅
- c) Solo los ítems parcialmente indexados
- d) Un error de sintaxis

*Respuesta: b).* Una condición vacía no filtra nada: devuelve todo el alcance, con el riesgo de exponer contenido y de exportar de más. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**7. ¿Qué necesitas para que las estadísticas de una búsqueda muestren el keyword report?**

- a) Al menos dos cuadrículas de palabras clave  ✅
- b) Una licencia de Security Copilot
- c) Agregar los resultados a un review set
- d) Escribir la consulta en KQL

*Respuesta: a).* El keyword report aparece cuando la consulta tiene al menos dos cuadrículas de palabras clave; al convertirla a KeyQL, las cuadrículas se separan con c:s. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-condition-builder) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. ¿Cuántos trabajos de búsqueda de auditoría simultáneos puede tener un usuario?**

- a) Tres
- b) Cinco
- c) Diez  ✅
- d) Cincuenta

*Respuesta: c).* Hasta diez trabajos simultáneos por usuario, solo uno de ellos sin filtros; los resultados se conservan 30 días y los trabajos siguen corriendo aunque cierres el navegador. [Fuente](https://learn.microsoft.com/en-us/purview/audit-search) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. Hoy creas una política de retención de auditoría de un año. ¿Qué pasa con los registros que ya vencieron?**

- a) Se recuperan los de los últimos doce meses
- b) Nada: los cambios no son retroactivos  ✅
- c) Se recuperan solo los de usuarios con E5
- d) Se recuperan si agregas el complemento de 10 años

*Respuesta: b).* Los cambios en las políticas de retención de auditoría no son retroactivos. Por eso la retención se decide antes del incidente o del requerimiento. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**10. ¿Qué hace falta para usar funciones de pago por uso de Purview, como Data Security Investigations?**

- a) Tener Microsoft 365 E7
- b) Activar Audit (Premium)
- c) Comprar SCU de Security Copilot
- d) Asociar el tenant a una suscripción de Azure activa  ✅

*Respuesta: d).* El pago por uso se factura en Azure y exige asociar el tenant a una suscripción activa. No depende de E7, de Audit (Premium) ni de Security Copilot. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**11. ¿Qué es Microsoft Purview Suite?**

- a) El nuevo nombre de Microsoft 365 E5 Compliance: un complemento sobre E3 que incluye Audit y eDiscovery  ✅
- b) Un plan de pago por uso para Data Security Investigations
- c) Una edición gratuita de Purview para tenants E3
- d) El paquete de Security Copilot para Purview

*Respuesta: a).* Microsoft 365 E5 Compliance pasó a llamarse Microsoft Purview Suite, sin cambio funcional. Se agrega a Microsoft 365 E3 y ya viene incluido en Microsoft 365 E5. [Fuente](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**12. Para usuarios con licencias E3 y E5, ¿en qué nivel de auditoría está el evento MailItemsAccessed?**

- a) Solo en Audit (Premium)
- b) Solo con el complemento de 10 años
- c) En Audit (Standard)  ✅
- d) Solo con pago por uso

*Respuesta: c).* MailItemsAccessed forma parte de Audit (Standard) para usuarios E3 y E5; Audit (Premium) le agrega propiedades como SensitivityLabel y una retención más larga. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**13. No existe un «Audit Ninja» oficial. ¿Qué recurso oficial es lo más cercano?**

- a) La ruta de Learn «Audit and search activity in Microsoft Purview», alineada con SC-401  ✅
- b) Los escenarios Ninja de Information Protection y DLP en Learn
- c) El módulo de MS-101 sobre Audit (Premium)
- d) El Ninja de Communication Compliance

*Respuesta: a).* La ruta «Audit and search activity in Microsoft Purview» (cerca de 1 h 31 min) cubre investigaciones con Audit y búsquedas con eDiscovery. El módulo de MS-101 es heredado y los otros Ninja tratan otras soluciones. [Fuente](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**14. ¿Dónde se usa un subconjunto de KQL (Kusto) dentro de eDiscovery?**

- a) En el editor de búsquedas del caso
- b) En el generador de condiciones de los holds
- c) En la configuración de la exportación
- d) En el explorador avanzado de review sets (vista previa)  ✅

*Respuesta: d).* Las búsquedas del caso usan KeyQL. El explorador avanzado de review sets, en vista previa, ejecuta un subconjunto de Kusto sobre ReviewSetTable. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**15. ¿Qué grupo de roles permite buscar en la auditoría sin poder cambiar su configuración?**

- a) Audit Manager
- b) Audit Reader  ✅
- c) eDiscovery Administrator
- d) Organization Configuration

*Respuesta: b).* Audit Reader tiene el rol View-Only Audit Logs. Audit Manager tiene Audit Logs, que también permite administrar la configuración, y Organization Configuration se usa para las políticas de retención de auditoría. [Fuente](https://learn.microsoft.com/en-us/purview/audit-get-started) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Preservar, revisar, investigar y producir

**1. ¿Cuánto puede tardar una política de hold de eDiscovery en aplicarse?**

- a) Hasta una hora
- b) Hasta 24 horas  ✅
- c) Hasta siete días
- d) Se aplica al instante

*Respuesta: b).* Un hold puede tardar hasta 24 horas en aplicarse: créalo antes de anunciar el asunto y verifica su estado antes de dar por preservado a un custodio. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. Creas un hold sobre un grupo de Microsoft 365 y al día siguiente se suma una persona al grupo. ¿Qué ocurre?**

- a) Queda retenida automáticamente
- b) Queda retenida solo si tiene E5
- c) No queda retenida: la membresía se tomó como instantánea al crear la política  ✅
- d) El hold se suspende hasta volver a aplicarlo

*Respuesta: c).* La membresía del grupo se captura al crear la política; las altas posteriores no quedan retenidas hasta que actualices el hold. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. Con funciones premium, ¿cuántos buzones admite como máximo una política de hold de caso?**

- a) 100
- b) 1.000
- c) 10.000
- d) 2.000  ✅

*Respuesta: d).* Con funciones premium, 2.000 buzones y 2.000 sitios por hold de caso; con funciones estándar, 1.000 de cada uno. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. Un hold de eDiscovery es lo único que mantiene un buzón inactivo. ¿Qué pasa si liberas el hold o cierras el caso?**

- a) El buzón inactivo se elimina  ✅
- b) El buzón vuelve a estar activo
- c) El buzón queda retenido 180 días más
- d) Nada cambia

*Respuesta: a).* Si ningún otro hold o retención lo mantiene, el buzón inactivo se elimina. Por eso la liberación se verifica antes en el procedimiento. [Fuente](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿Qué ocurre al agregar los resultados de una búsqueda a un review set?**

- a) Los ítems se mueven fuera del buzón original
- b) La búsqueda se vuelve a ejecutar y los ítems se copian a almacenamiento de Azure gestionado por Microsoft, donde se reindexan  ✅
- c) Se crea un vínculo a los ítems sin copiarlos
- d) Se exportan automáticamente a PST

*Respuesta: b).* Al agregar, la búsqueda se vuelve a ejecutar y los ítems se copian al almacenamiento del caso y se reindexan; los originales no se mueven. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Cómo eliminas ítems o un review set completo?**

- a) Desde el menú del review set
- b) Con el rol Search And Purge
- c) Esperando 30 días a que expire
- d) Solo eliminando el caso completo  ✅

*Respuesta: d).* No se pueden borrar ítems ni review sets; solo desaparecen al eliminar el caso. Ese carácter estático favorece la cadena de custodia. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-manage) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué rol necesitas para procesar adjuntos cifrados al agregarlos a un review set?**

- a) Reviewer
- b) Search And Purge
- c) Audit Reader
- d) RMS Decrypt  ✅

*Respuesta: d).* RMS Decrypt permite descifrar el contenido protegido al agregarlo a un review set o al exportarlo. Asígnalo solo a quien lo necesite en cada asunto. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Cada cuánto se agregan los accesos bind de MailItemsAccessed?**

- a) Cada minuto
- b) Cada cinco minutos
- c) Cada dos minutos  ✅
- d) Cada hora

*Respuesta: c).* Los accesos bind se agregan en ventanas de dos minutos e incluyen el InternetMessageId de cada mensaje; los sync se registran por carpeta. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. Según Microsoft, ¿cuánto puede crecer el volumen del registro de auditoría hacia el SIEM con los registros ampliados?**

- a) Hasta 10 veces  ✅
- b) Hasta 2 veces
- c) Hasta 100 veces
- d) No cambia

*Respuesta: a).* Microsoft advierte que los registros ampliados pueden multiplicar hasta 10 veces el volumen hacia el SIEM: estima el costo antes de habilitar la ingesta completa. [Fuente](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué evento de búsqueda de Exchange no viene habilitado por defecto y se activa buzón por buzón?**

- a) MailItemsAccessed
- b) SearchQueryInitiatedExchange  ✅
- c) Send
- d) FileAccessed

*Respuesta: b).* SearchQueryInitiatedExchange se habilita por buzón; el de SharePoint viene habilitado. Decide con privacidad sobre quién se activa. [Fuente](https://learn.microsoft.com/en-us/purview/audit-get-started) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. En un compromiso de correo, ¿qué conviene hacer antes de eliminar las reglas de reenvío creadas por el atacante?**

- a) Preservar la evidencia: hold sobre el buzón y exportación de la auditoría con hash  ✅
- b) Desactivar la auditoría del buzón para no generar ruido
- c) Purgar los mensajes que envió el atacante
- d) Esperar a que la auditoría cumpla 180 días

*Respuesta: a).* La contención no espera, pero la erradicación sí: preservar primero conserva la prueba del alcance que Legal necesitará para decidir notificaciones. [Fuente](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. Desde el 16 de febrero de 2026, ¿cuándo expiran los paquetes de exportación de búsquedas?**

- a) A los 7 días
- b) A los 30 días
- c) Nunca
- d) A los 14 días  ✅

*Respuesta: d).* Expiran 14 días después de su creación. El cambio no afecta a las exportaciones de review sets. [Fuente](https://mc.merill.net/message/MC1217141) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. Exportas un review set con redacciones confirmadas. ¿Qué recibe el destinatario por cada documento redactado?**

- a) El nativo y el PDF
- b) El PDF redactado (_burn.pdf) en lugar del nativo  ✅
- c) Nada: los ítems redactados no se exportan
- d) Solo el informe de ítems

*Respuesta: b).* Con redacciones confirmadas, la exportación reemplaza el nativo por el PDF redactado _burn.pdf. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. ¿Qué pasa con una exportación que dura más de siete días?**

- a) Se pausa hasta que la reanudes
- b) Se divide en paquetes de 40 GB
- c) Se cancela  ✅
- d) Se completa en archivos PST de 10 GB

*Respuesta: c).* Una exportación que supera siete días se cancela; planifica lotes que terminen antes. Los paquetes de 40 GB y los PST de 10 GB son límites de formato, no una salida al plazo. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. ¿Dentro de qué plazo hay que descargar una exportación de review set?**

- a) 14 días
- b) 7 días
- c) 30 días  ✅
- d) 90 días

*Respuesta: c).* Las exportaciones de review set se retienen durante la vida del caso, pero hay que descargarlas dentro de 30 días; los 14 días aplican a las exportaciones de búsquedas. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, automatización y SOC

**1. ¿Dónde se guardan los prompts y respuestas de Copilot que eDiscovery puede buscar, retener y exportar?**

- a) En el OneDrive del usuario
- b) En el workspace de Sentinel
- c) En el buzón del usuario  ✅
- d) En el review set del caso

*Respuesta: c).* Prompts y respuestas de Copilot y de otras apps de IA se guardan en el buzón del usuario, identificados por clase de ítem; por eso eDiscovery los trata como cualquier otro contenido. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Qué rol se requiere para eliminar datos de IA con el flujo de búsqueda y eliminación de eDiscovery?**

- a) eDiscovery Manager
- b) Audit Reader
- c) Reviewer
- d) Search And Purge  ✅

*Respuesta: d).* Search And Purge permite eliminar el contenido que coincide con la búsqueda, hasta 10 ítems por buzón por vez y retirando antes holds y retención. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. La auditoría de interacciones con apps de IA no Microsoft (AIAppInteraction)…**

- a) …está incluida en E5 sin costo adicional
- b) …requiere pago por uso y se retiene 180 días  ✅
- c) …requiere Audit (Premium) y se retiene un año
- d) …no se audita

*Respuesta: b).* Las apps de IA de Microsoft se auditan en Audit (Standard); las no Microsoft se facturan por uso y se retienen 180 días. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. En un registro de auditoría de Copilot, ¿qué propiedad de los recursos consultados señala una posible inyección de instrucciones?**

- a) AgentId
- b) AppAccessContext
- c) XPIADetected  ✅
- d) InternetMessageId

*Respuesta: c).* AccessedResources incluye SensitivityLabelId y XPIADetected. AgentId identifica a un agente, AppAccessContext es una propiedad de Teams y InternetMessageId identifica mensajes en MailItemsAccessed. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Qué reemplaza a Search-UnifiedAuditLog, que se retira el 15 de octubre de 2027?**

- a) La API AuditLogQuery de Microsoft Graph  ✅
- b) La Management Activity API
- c) Get-AdminAuditLogConfig
- d) Content Search

*Respuesta: a).* AuditLogQuery llegó a disponibilidad general en octubre de 2026. La Management Activity API sigue existiendo, pero para suscripciones hacia un SIEM. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. ¿Cuál de estos es un límite documentado de AuditLogQuery por tenant?**

- a) Diez consultas por día
- b) Mil registros por consulta
- c) Una consulta en cola por usuario
- d) 200 envíos cada 24 horas  ✅

*Respuesta: d).* Cada tenant admite 200 envíos cada 24 horas y 50 consultas en cola o en ejecución (HTTP 429 al exceder); cada consulta devuelve hasta un millón de registros. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. Con E3 y permisos delegados, ¿qué automatizas con la API de eDiscovery de Graph sin pago adicional?**

- a) Casos, búsquedas y holds  ✅
- b) Review sets y analítica
- c) Autenticación solo aplicación
- d) Descargas masivas

*Respuesta: a).* Con E3 delegado: casos, búsquedas y holds. Exportar con E3 requiere pago por uso; review sets, analítica y solo aplicación requieren E5, y la API no está pensada para descargas masivas. [Fuente](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. Desde agosto de 2026, ¿qué no admiten los cmdlets de eDiscovery de Security & Compliance PowerShell?**

- a) La creación de holds
- b) La autenticación solo aplicación  ✅
- c) Las búsquedas
- d) La purga

*Respuesta: b).* La autenticación solo aplicación dejó de estar soportada en esos cmdlets: los procesos desatendidos deben migrar a Microsoft Graph. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. En la Management Activity API, ¿cuánto puede tardar el primer blob después de crear una suscripción?**

- a) Cinco minutos
- b) Una hora
- c) Hasta 12 horas  ✅
- d) Siete días

*Respuesta: c).* El primer blob puede tardar hasta 12 horas y los eventos no llegan en orden: el SIEM debe ordenar por marca de tiempo. [Fuente](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**10. ¿Qué tabla de Sentinel contiene la auditoría de Exchange, SharePoint y Teams?**

- a) SigninLogs
- b) AzureActivity
- c) CloudAppEvents
- d) OfficeActivity  ✅

*Respuesta: d).* OfficeActivity reúne la auditoría de Exchange, SharePoint y Teams. CloudAppEvents es una tabla de la búsqueda avanzada de Defender XDR. [Fuente](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. ¿Qué advierte el conector de Purview Information Protection para Sentinel (vista previa)?**

- a) Que solo funciona con Audit (Premium)
- b) Que, si el workspace está en otra región que Office 365, los datos pueden transmitirse entre regiones  ✅
- c) Que no admite el nivel data lake
- d) Que requiere Security Copilot

*Respuesta: b).* La advertencia de transmisión entre regiones convierte la ubicación del workspace en una decisión de privacidad. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Cómo se licencia Data Security Investigations?**

- a) Incluida en Microsoft 365 E5
- b) Complemento por usuario
- c) Pago por uso de almacenamiento y Compute Units  ✅
- d) Solo con capacidad aprovisionada de Security Copilot

*Respuesta: c).* DSI no requiere licencia dedicada: se factura por almacenamiento (GB al mes) y por Data Security Investigations Compute Units. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. ¿Dónde puede ejecutarse el cómputo de IA de Data Security Investigations?**

- a) Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»  ✅
- b) En la región del tenant, incluida Latinoamérica
- c) Solo en EE. UU.
- d) En el workspace de Sentinel

*Respuesta: a).* No hay opción en Latinoamérica: la elección de ubicación es una decisión para Legal y privacidad en cada país. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Qué afirmación sobre Security Copilot en eDiscovery es correcta?**

- a) Puede ver todos los casos aunque el usuario no sea miembro
- b) Requiere el rol eDiscovery Administrator
- c) Ejecuta exportaciones automáticamente
- d) Actúa en nombre del usuario y nunca excede sus permisos  ✅

*Respuesta: d).* Security Copilot usa autenticación en nombre del usuario: solo ve lo que el usuario puede ver en Purview. Sus roles owner y contributor no son roles de Entra. [Fuente](https://learn.microsoft.com/en-us/copilot/security/authentication) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué etapas agrupa EDRM 2.0 bajo «Data Acquisition»?**

- a) Revisión, análisis y producción
- b) Identificación, preservación, recolección y procesamiento  ✅
- c) Disposición y gobierno de la información
- d) Presentación y producción

*Respuesta: b).* EDRM 2.0 (1 de septiembre de 2026) agrupa identificación, preservación, recolección y procesamiento en «Data Acquisition», agrega la disposición y se apoya en el IGRM. [Fuente](https://edrm.net/edrm-model/current/) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué publicación de NIST reemplazó en abril de 2025 a la SP 800-61 Rev. 2?**

- a) SP 800-53 Rev. 5
- b) CSF 2.0
- c) SP 800-61 Rev. 3  ✅
- d) SP 800-86

*Respuesta: c).* SP 800-61 Rev. 3 reemplazó a la Rev. 2 y alinea la respuesta a incidentes con CSF 2.0. [Fuente](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten fecha de expiración. ¿Cuáles quedan excluidas?**

- a) Audit Reader y Audit Manager
- b) eDiscovery Administrator y eDiscovery Manager  ✅
- c) Organization Configuration
- d) Reviewer

*Respuesta: b).* eDiscovery Administrator y eDiscovery Manager no admiten fecha de expiración: contrólalos con PIM para grupos y revisiones de acceso. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Por qué conviene mantener pequeño el grupo eDiscovery Administrator?**

- a) Porque consume licencias E5 adicionales
- b) Porque solo admite cinco miembros
- c) Porque su actividad no se audita
- d) Porque accede a todos los casos y a sus datos  ✅

*Respuesta: d).* eDiscovery Administrator ve todos los casos y sus datos sensibles. Su actividad sí se audita y no tiene un límite de cinco miembros. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Qué dato registran en Audit las actividades de la experiencia unificada de eDiscovery y faltaba en las heredadas?**

- a) La dirección IP del cliente  ✅
- b) El hash del paquete exportado
- c) El nombre del abogado responsable
- d) El consumo de SCU

*Respuesta: a).* Las actividades de la experiencia unificada incluyen la IP del cliente; un IP vacío indica la experiencia heredada. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué anunció MC1473155 para fines de septiembre y octubre de 2026?**

- a) El retiro de Audit (Standard)
- b) Nuevas operaciones de auditoría de RBAC en Purview  ✅
- c) La expiración de exportaciones a 14 días
- d) La disponibilidad general de AuditLogQuery

*Respuesta: b).* MC1473155 agrega operaciones como CheckUsersInRoles y CheckUserInRolesWithScopes, útiles para vigilar quién obtiene permisos; no son retroactivas. [Fuente](https://mc.merill.net/message/MC1473155) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Dónde ves el consumo de pago por uso de Purview por función?**

- a) En el Usage center de Purview (vista previa)  ✅
- b) En el panel de SCU de Security Copilot
- c) En la tabla OfficeActivity
- d) En el review set del caso

*Respuesta: a).* El Usage center muestra el consumo de pago por uso por función; el panel de Security Copilot muestra SCU, que es otra capacidad. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Dónde se aprovisiona el almacenamiento de un review set?**

- a) En la región del workspace de Sentinel
- b) En una cuenta de Azure Storage del cliente
- c) En la geografía del caso, con soporte de Customer Key  ✅
- d) En el OneDrive del eDiscovery Manager

*Respuesta: c).* El almacenamiento del review set lo gestiona Microsoft, se aprovisiona en la geografía del caso, admite Customer Key y no ofrece acceso directo por SAS. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**9. ¿Cuándo entra en vigencia la Ley 21.719 de protección de datos personales de Chile?**

- a) 13 de diciembre de 2024
- b) 20 de marzo de 2025
- c) 1 de diciembre de 2026  ✅
- d) 15 de octubre de 2027

*Respuesta: c).* Se publicó en diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026, con reglas de transferencia internacional. El 20 de marzo de 2025 corresponde a la nueva LFPDPPP de México. [Fuente](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. Legal duda si entregar una exportación a un estudio jurídico de otro país es una transferencia internacional. ¿Qué corresponde según esta guía?**

- a) Decidirlo según la región del tenant
- b) Llevar la pregunta a Legal y privacidad con la evidencia técnica y las fuentes oficiales  ✅
- c) Exportar primero y notificar después
- d) Procesarla en DSI con ubicación «en cualquier lugar»

*Respuesta: b).* La guía no interpreta la ley: aporta el dato técnico (qué sale, adónde y cuándo vence) y la pregunta va a Legal y privacidad, con la norma oficial de cada país. [Fuente](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. ¿Qué permite restringir las búsquedas de un equipo de eDiscovery a un país o a una empresa del grupo?**

- a) Las Compute Units de DSI
- b) Las etiquetas de retención
- c) El rol Reviewer
- d) Los límites de cumplimiento (filtros de permisos de búsqueda)  ✅

*Respuesta: d).* Los límites de cumplimiento usan filtros de permisos de búsqueda por atributo (país, subsidiaria) y aplican también a Data Security Investigations. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Qué consecuencia tiene la limpieza prioritaria (vista previa) para eDiscovery?**

- a) El contenido eliminado deja de ser descubrible  ✅
- b) El contenido pasa a un review set
- c) Se crea un hold automático
- d) Solo afecta a registros regulatorios

*Respuesta: a).* La limpieza prioritaria puede eliminar contenido aunque esté retenido, y lo eliminado deja de ser descubrible. No aplica a registros ni a registros regulatorios. [Fuente](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. Desde julio de 2026, ¿qué aprobaciones exige la limpieza prioritaria?**

- a) Una, del Global Administrator
- b) Dos, de cualquier administrador de Purview
- c) Tres: limpieza prioritaria, retención y eDiscovery  ✅
- d) Ninguna si antes se ejecutó la simulación

*Respuesta: c).* Las novedades de julio de 2026 exigen tres aprobaciones separadas; avisos anteriores hablaban de dos administradores. Inclúyelo en el procedimiento y en el registro de decisiones. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

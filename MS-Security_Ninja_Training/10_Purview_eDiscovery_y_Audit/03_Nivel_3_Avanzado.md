# Nivel 3 · Avanzado · IA, automatización y SOC

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Copilot, agentes y apps de IA como evidencia, automatización con Microsoft Graph y PowerShell, integración con respuesta a incidentes, Sentinel y Defender XDR, e investigaciones asistidas por IA con Security Copilot y Data Security Investigations.

*L400 · 4 módulos · ~20 horas · 22 recursos*

**Módulos de este nivel:** [A1 IA y agentes como evidencia](#a1) · [A2 Graph y PowerShell](#a2) · [A3 IR, Sentinel y Defender XDR](#a3) · [A4 Security Copilot y DSI](#a4)

<a id="a1"></a>

## A1 · eDiscovery y Audit para Copilot, agentes y apps de IA

*L400 · ~4 h · Origen: Nuevo en esta edición (el Ninja oficial de 2026 incluye la búsqueda de contenido de Copilot)*

Con Copilot y los agentes, la evidencia incluye conversaciones con máquinas. Los prompts y respuestas de Copilot y de otras apps de IA se guardan en una carpeta oculta del buzón del usuario, identificados por clase de ítem, y por eso eDiscovery puede buscarlos, retenerlos, revisarlos y exportarlos como cualquier otro contenido. En Audit, los registros de interacción se generan automáticamente en Audit (Standard) e incluyen los recursos consultados (`AccessedResources`, con la etiqueta de confidencialidad y la señal `XPIADetected` de inyección de instrucciones) y, para agentes, `AgentId` y `AgentName`.

El alcance crece rápido: Security Copilot, Copilot en Fabric, Copilot Studio y Microsoft Foundry se auditan sin costo adicional; las apps de IA no Microsoft (registro `AIAppInteraction`) requieren pago por uso y se retienen 180 días. En 2026 eDiscovery sumó contenedores de SharePoint Embedded (Loop, Copilot Pages y Copilot Notebooks) y Claude Enterprise, mientras Priority Cleanup (vista previa) permite borrar contenido retenido de forma que deja de ser descubrible. Y desde el 1 de mayo de 2026, Purview para agentes gestionados con Agent 365 se licencia con Microsoft 365 E7 o el complemento Agent 365. Este módulo te enseña a tratar la IA como fuente de evidencia y como riesgo de gobierno.

**Por qué importa**

Los reguladores, los tribunales y las investigaciones internas ya preguntan qué se le pidió a la IA y qué respondió, qué documentos consultó un agente y si alguien llevó datos sensibles a una app externa. Poder responder con evidencia preservada, y eliminar con control cuando corresponde, reduce el riesgo legal de adoptar IA y acelera su aprobación por parte de Legal y privacidad.

**Qué vas a lograr**

- Buscar, retener y exportar interacciones de Copilot y otras apps de IA con eDiscovery.
- Interpretar registros de auditoría de Copilot y agentes (AccessedResources, XPIADetected, AgentId).
- Distinguir qué auditoría de IA está incluida y cuál requiere pago por uso.
- Aplicar el flujo de búsqueda y eliminación de datos de IA con controles de preservación.
- Evaluar el impacto de Priority Cleanup y de SharePoint Embedded en el proceso de eDiscovery.

> **Novedad.** 24 de septiembre de 2026: eDiscovery busca, retiene, revisa y exporta contenedores de SharePoint Embedded de usuario (Loop, Copilot Pages y Copilot Notebooks), con conversión HTML opcional ([Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)). Learn todavía lo marca en vista previa ([componentes de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-features-components)).

> **Atención.** La limpieza prioritaria (Priority Cleanup, vista previa) puede eliminar contenido de buzones aunque tenga retención, holds o Preservation Lock, con simulación y aprobaciones; no aplica a registros y puede desactivarse a nivel de tenant ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)). Desde julio de 2026 exige tres aprobaciones —limpieza prioritaria, retención y eDiscovery—, aunque avisos anteriores hablaban de dos ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Lo eliminado deja de ser descubrible.

> **Consejo Ninja.** Prompts y respuestas viven en el buzón del usuario, identificados por clase de ítem. Para eliminarlos necesitas el rol Search And Purge, se borran hasta 10 ítems por buzón por vez y hay que retirar y volver a aplicar holds o retención ([datos de IA en eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data)). Nunca purgues sin la confirmación escrita de Legal.

> **Qué cambió.** Las apps de IA de Microsoft (Security Copilot, Copilot en Fabric, Copilot Studio y Microsoft Foundry) se auditan en Audit (Standard); las no Microsoft (`AIAppInteraction`) requieren pago por uso y se retienen 180 días. Los registros incluyen `AccessedResources` con `SensitivityLabelId` y `XPIADetected`, y `AgentId` y `AgentName` para agentes ([auditoría de Copilot e IA](https://learn.microsoft.com/en-us/purview/audit-copilot)). Para agentes gestionados con Agent 365, la descripción de servicio ubica la auditoría y el eDiscovery de Purview entre las capacidades de Microsoft 365 E7 o Agent 365, disponibles en general desde el 1 de mayo de 2026 ([Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)).

**¿Tienes poco tiempo?**

- [Search for and delete AI application data in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Documentación
- [Audit logs for Copilot and AI applications](https://learn.microsoft.com/en-us/purview/audit-copilot) · Documentación
- [What’s new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial

### Documentación, cursos y credenciales

- [Search for and delete AI application data in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Documentación · Oficial · Microsoft Learn. Flujo para buscar y eliminar prompts/respuestas de Copilot y otras apps de IA (almacenados en el buzón del usuario) con eDiscovery y Graph Explorer, incluyendo la tabla de clases de ítem.
- [Audit logs for Copilot and AI applications](https://learn.microsoft.com/en-us/purview/audit-copilot) · Documentación · Oficial · Microsoft Learn. Describe los registros de interacción con Copilot, Cowork, agentes y apps de IA (AccessedResources, AgentId, AppHost) y la facturación por uso para apps de IA no-Microsoft.

### Anuncios y blogs oficiales

- [What’s new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Anuncia que eDiscovery ya permite buscar, retener, revisar y exportar contenedores de SharePoint Embedded de usuario (Loop, Copilot Pages, Copilot Notebooks) con conversión HTML opcional.

### Comunidad: blogs, libros, newsletters y eventos

- [Things to Know About Microsoft Purview – October 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/) · Blog · MVP · Nuevo · Albert Hoitingh · Albert Hoitingh (blog) · 7 oct 2026. Resumen mensual de un MVP: eDiscovery sobre SharePoint Embedded, Priority Cleanup (preview) capaz de anular holds tras simulación y doble aprobación, soporte de Claude Enterprise y fin del app-only en cmdlets de eDiscovery.

**Manos a la obra**

1. `Laboratorio parcial` Busca en un caso las interacciones de Copilot de una cuenta de prueba usando las clases de ítem de IA, agrégalas a un review set y revísalas con el visor de actividad de Copilot. Limitación: las licencias de Microsoft 365 Copilot no vienen en la prueba E5 (se pueden comprar en el sandbox de desarrollador); sin ellas no hay interacciones que buscar ([datos de IA en eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data)). Evidencia: consulta, conteo y captura del visor.
2. `Laboratorio parcial` Busca en Audit los registros de interacción con Copilot o con un agente y anota, para uno de ellos, `AccessedResources` (con `SensitivityLabelId` y `XPIADetected`), `AgentId` y `AgentName`. Limitación: necesitas actividad real de Copilot o de un agente en el tenant, y la cobertura de Purview para agentes gestionados con Agent 365 requiere E7 o Agent 365 ([auditoría de Copilot e IA](https://learn.microsoft.com/en-us/purview/audit-copilot)). Evidencia: registro JSON anotado con lo que prueba y lo que no.
3. `Laboratorio parcial` Practica el flujo de búsqueda y eliminación de datos de IA sobre una cuenta de prueba: verifica holds y retención, retíralos de forma controlada, purga hasta 10 ítems por buzón, confirma con una nueva búsqueda y vuelve a aplicar la preservación. Limitación: requiere interacciones reales de Copilot; en producción, practica solo con una cuenta de prueba y el rol Search And Purge asignado de forma temporal con PIM. Evidencia: lista de verificación con doble aprobación y registros de auditoría de la purga.
4. `Laboratorio parcial` Si tu tenant de prueba tiene Loop, crea un espacio de trabajo con contenido sintético y búscalo en eDiscovery; al exportar, prueba la conversión HTML. Limitación: Learn marca en vista previa el soporte de SharePoint Embedded, y Copilot Pages y Copilot Notebooks necesitan licencias de Copilot ([Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)). Evidencia: resultado de la búsqueda y del paquete exportado.
5. `Laboratorio` Calcula cuánto costaría auditar apps de IA no Microsoft (`AIAppInteraction`, pago por uso, 180 días de retención) para tu organización y quién debe aprobarlo. Evidencia: nota de decisión con supuestos, costo estimado y aprobadores ([auditoría de Copilot e IA](https://learn.microsoft.com/en-us/purview/audit-copilot)).
6. `Solo producción` Gobierna la limpieza prioritaria antes de que alguien la use: con Legal, retención y eDiscovery define si se habilita o se desactiva a nivel de tenant, quién da cada una de las tres aprobaciones y cómo se verifica que no hay holds de asuntos activos. Cómo hacerlo seguro: no se ejecuta en producción como práctica; ejercicio de mesa y decisión registrada en el registro de [O3](04_Nivel_4_Operacion.md#o3) ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)). Evidencia: procedimiento aprobado o decisión de desactivar.

**¿Quieres profundizar?**

- [Things to Know About Microsoft Purview – October 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/) · Blog

<a id="a2"></a>

## A2 · Automatización con Microsoft Graph y PowerShell

*L400 · ~6 h · Origen: Ninja de Advanced eDiscovery (2021): sección Advanced, actualizada a Microsoft Graph y AuditLogQuery*

Automatizar eDiscovery y Audit tiene sentido cuando los asuntos se repiten: abrir casos con una plantilla, aplicar holds a una lista de custodios, extraer auditoría para un incidente o alimentar un SIEM. La **API de eDiscovery de Microsoft Graph** (espacio de nombres `microsoft.graph.security`) expone casos, custodios, búsquedas, políticas de hold, review sets y etiquetas. Con E3 y permisos delegados automatizas casos, búsquedas y holds; exportar con E3 requiere pago por uso; review sets, analítica y la autenticación solo aplicación requieren E5. No está pensada para descargas masivas.

En auditoría conviven tres caminos. `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027; su reemplazo es la API **AuditLogQuery** de Graph, disponible en general desde octubre de 2026, con consultas asíncronas de hasta un millón de registros y límites por tenant. La **Management Activity API** sigue siendo el canal de suscripción para el SIEM. Y desde agosto de 2026 los cmdlets de eDiscovery de Security & Compliance PowerShell no admiten autenticación solo aplicación: los procesos desatendidos deben migrar a Graph.

**Por qué importa**

Los scripts heredados son deuda técnica con fecha de vencimiento: dejarán de funcionar en 2027 o ya fallan si usan autenticación solo aplicación en cmdlets de eDiscovery. Automatizar sobre Graph reduce errores manuales en asuntos repetitivos, deja trazabilidad completa en la auditoría y libera horas del equipo para el análisis en lugar de los clics.

**Qué vas a lograr**

- Crear casos, búsquedas y holds con la API de eDiscovery de Graph y una app registrada con mínimo privilegio.
- Consultar la auditoría con AuditLogQuery respetando sus límites y manejar respuestas HTTP 429.
- Migrar un script de Search-UnifiedAuditLog a AuditLogQuery.
- Elegir entre AuditLogQuery y la Management Activity API según el caso de uso.
- Identificar qué operaciones requieren E5 o pago por uso.

> **Novedad.** Octubre de 2026: la API AuditLogQuery de Graph llegó a disponibilidad general, con hasta un millón de registros por consulta, 200 envíos cada 24 horas y 50 consultas en cola o en ejecución por tenant (HTTP 429 al exceder). `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027 ([MC1505599](https://mc.merill.net/message/MC1505599), [referencia](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0)).

> **Qué cambió.** Desde agosto de 2026, los cmdlets de eDiscovery de Security & Compliance PowerShell no admiten autenticación solo aplicación ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)), y desde el 26 de mayo de 2025 ya no exportan ([MC1055528](https://mc.merill.net/message/MC1055528)). Todo proceso desatendido debe ir por Microsoft Graph.

> **Atención.** La API de eDiscovery de Graph no está pensada para descargas masivas. Con E3 y permisos delegados automatizas casos, búsquedas y holds; exportar con E3 requiere pago por uso; review sets, analítica y la autenticación solo aplicación requieren E5 ([API de eDiscovery](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)). El aviso MC1055528 de abril de 2025 asociaba la exportación a E5: confírmalo en tu tenant.

> **Consejo Ninja.** Para alimentar un SIEM, la Management Activity API sigue siendo el canal: tipos de contenido Audit.AzureActiveDirectory, Audit.Exchange, Audit.SharePoint, Audit.General y DLP.All. El primer blob puede tardar hasta 12 horas y los eventos no llegan en orden ([referencia](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference)).

**¿Tienes poco tiempo?**

- [Use the Microsoft Purview eDiscovery API in Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) · Documentación
- [MC1505599 - Microsoft Purview Audit: AuditLogQuery API generally available and Search-UnifiedAuditLog retiring](https://mc.merill.net/message/MC1505599) · Documentación
- [Get auditLogQuery - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0) · Documentación

**Interfaces programáticas de eDiscovery y Audit (noviembre de 2026)**

| Interfaz | Para qué sirve | Estado | Licencia y límites | Fuente |
|---|---|---|---|---|
| API de eDiscovery de Microsoft Graph (`microsoft.graph.security`) | Casos, custodios, búsquedas, holds, review sets y etiquetas | Disponible en general; camino recomendado para automatizar | E3 delegado: casos, búsquedas y holds; exportar con E3 requiere pago por uso; review sets, analítica y solo aplicación requieren E5; no apta para descargas masivas | [Learn](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) |
| API AuditLogQuery de Microsoft Graph | Búsquedas asíncronas del registro de auditoría | Disponible en general desde octubre de 2026 | Hasta un millón de registros por consulta; 200 envíos cada 24 horas y 50 consultas en cola por tenant (HTTP 429) | [MC1505599](https://mc.merill.net/message/MC1505599) |
| Management Activity API | Suscripción y descarga continua hacia un SIEM | Vigente | Base de 2.000 solicitudes por minuto por tenant, cerca del doble con E5; primer blob hasta 12 horas | [Learn](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) |
| `Search-UnifiedAuditLog` (Exchange Online PowerShell) | Búsqueda de auditoría por cmdlet | Se retira el 15 de octubre de 2027 | Migrar a AuditLogQuery | [MC1505599](https://mc.merill.net/message/MC1505599) |
| Cmdlets de eDiscovery de Security & Compliance PowerShell | Casos, holds, búsquedas y purga en forma interactiva | Vigentes, sin parámetros de exportación desde el 26 de mayo de 2025 y sin autenticación solo aplicación desde agosto de 2026 | Lo desatendido va por Graph | [MC1055528](https://mc.merill.net/message/MC1055528), [novedades](https://learn.microsoft.com/en-us/purview/whats-new) |
| Tabla `OfficeActivity` de Sentinel | Auditoría de Exchange, SharePoint y Teams para correlación y búsqueda | Vigente | Fuente gratuita; admite los niveles Auxiliary y data lake | [Learn](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity) |

Antes de registrar una app, revisa los permisos que lista cada página de referencia y concede el mínimo necesario.

### Documentación, cursos y credenciales

- [MC1505599 - Microsoft Purview Audit: AuditLogQuery API generally available and Search-UnifiedAuditLog retiring](https://mc.merill.net/message/MC1505599) · Documentación · Oficial · Nuevo · Message Center (archivo mc.merill.net) · 12 oct 2026. La API AuditLogQuery de Graph es GA desde octubre de 2026 (hasta 1 millón de registros por consulta) y Search-UnifiedAuditLog se retira el 15-oct-2027.
- [Use the Microsoft Purview eDiscovery API in Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) · Documentación · Oficial · Nuevo · Microsoft Learn (Graph) · 7 may 2026. Visión general de la API eDiscovery de Graph (microsoft.graph.security: ediscoveryCase, custodian, search, holdPolicy, reviewSet, tags) y matriz de licencias por tipo de autenticación.
- [Get auditLogQuery - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Graph). Referencia de la operación GET /security/auditLog/queries/{id} con filtros por fecha, recordType, operación, UPN, IP y unidades administrativas, y ejemplos en SDKs y PowerShell.
- [Office 365 Management Activity API reference](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) · Documentación · Oficial · Microsoft Learn. Referencia de la API de suscripción/blobs (Audit.AzureActiveDirectory, Audit.Exchange, Audit.SharePoint, Audit.General, DLP.All) para exportar auditoría a un SIEM.

**Manos a la obra**

1. `Laboratorio` Registra una app en Entra ID con el permiso mínimo de eDiscovery que indica la [API de eDiscovery](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0), guarda el secreto en Key Vault y, con Microsoft Graph PowerShell, crea un caso, una búsqueda y un hold; repite con autenticación solo aplicación (requiere E5, incluida en la prueba). Evidencia: script, caso creado y sus registros en la auditoría.
2. `Laboratorio` Crea una consulta AuditLogQuery filtrada por fechas, tipo de registro, operación y usuario; consulta su estado hasta que termine, descarga los registros y agrega reintentos con espera ante HTTP 429. Compara el conteo con la misma búsqueda en el portal. Evidencia: script y tabla de comparación ([AuditLogQuery](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0)).
3. `Laboratorio` Migra un script: toma una búsqueda de `MailItemsAccessed` de siete días hecha con `Search-UnifiedAuditLog` y reescríbela con AuditLogQuery. Documenta las diferencias: asincronía, límites de 200 envíos al día y 50 consultas en cola, y campos devueltos ([MC1505599](https://mc.merill.net/message/MC1505599)). Evidencia: ambos scripts y la nota de migración.
4. `Laboratorio parcial` Crea suscripciones de la Management Activity API a Audit.Exchange y Audit.General con tu app, espera el primer blob (puede tardar hasta 12 horas) y verifica que los eventos no llegan en orden comparando sus marcas de tiempo. Limitación: el volumen del laboratorio no permite ver la limitación de solicitudes ([referencia](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference)). Evidencia: suscripción activa y análisis del orden.
5. `Solo producción` Inventaria los scripts y procesos de tu organización que usan `Search-UnifiedAuditLog`, `-Export` en `New-ComplianceSearchAction` o cmdlets de eDiscovery con autenticación solo aplicación, y fija su fecha de migración a Graph. Cómo hacerlo seguro: revisión de código en el repositorio sin ejecutar nada contra producción, migración probada primero en el laboratorio y cambio con aprobación. Evidencia: inventario con dueño y fecha por script.

<a id="a3"></a>

## A3 · Integración con respuesta a incidentes, Sentinel y Defender XDR

*L400 · ~6 h · Origen: Nuevo en esta edición*

En un incidente, eDiscovery y Audit trabajan para el SOC: la auditoría aporta la línea de tiempo y la preservación asegura que la evidencia sobreviva a la remediación. En Sentinel, la tabla **OfficeActivity** contiene la auditoría de Exchange, SharePoint y Teams, admite los niveles Auxiliary y data lake y figura entre las fuentes sin costo de ingesta; en Defender XDR, la búsqueda avanzada consulta **CloudAppEvents**. Para otros SIEM, la Management Activity API entrega los mismos registros.

La integración también va en sentido contrario: las alertas de Insider Risk Management y DLP llegan a la cola de incidentes de Defender XDR, los casos de riesgo interno y las alertas de Communication Compliance pueden escalarse a una investigación de eDiscovery, y Data Security Investigations recibe incidentes de Defender XDR o casos de riesgo interno. Este módulo diseña ese circuito con NIST SP 800-61 Rev. 3 como marco, para que el SOC, Legal y RR. HH. sepan quién decide preservar, quién investiga y quién notifica.

**Por qué importa**

Muchos incidentes graves terminan en un asunto legal o regulatorio. Si el SOC remedia antes de preservar, o si la auditoría no llega al SIEM, la organización pierde la capacidad de probar el alcance. Un circuito integrado reduce el tiempo de investigación, evita perder evidencia durante la contención y da a Legal información confiable para decidir notificaciones.

**Qué vas a lograr**

- Consultar la auditoría de Microsoft 365 en Sentinel (OfficeActivity) y en Defender XDR (CloudAppEvents).
- Integrar la preservación con holds en los playbooks de respuesta a incidentes.
- Describir cómo se escalan a eDiscovery los casos de Insider Risk Management y las alertas de Communication Compliance.
- Diseñar un procedimiento de adquisición forense de la auditoría con su registro de custodia.

> **Consejo Ninja.** En Sentinel, OfficeActivity (Exchange, SharePoint y Teams) es una fuente de datos gratuita y admite los niveles Auxiliary y data lake ([OfficeActivity](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity), [facturación de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/billing)). En Defender XDR, la búsqueda avanzada consulta `CloudAppEvents` ([esquema de búsqueda avanzada](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)).

> **Atención.** El conector de Purview Information Protection para Sentinel (vista previa) advierte que, si el workspace está en otra región que Office 365, los datos pueden transmitirse entre regiones. Es una decisión que debe aprobar privacidad ([conector](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview)).

> **Novedad.** NIST SP 800-61 Rev. 3 (abril de 2025) reemplazó a la Rev. 2 y alinea la respuesta a incidentes con CSF 2.0 ([NIST](https://csrc.nist.gov/pubs/sp/800/61/r3/final)). Úsala para fijar en el playbook que la preservación con holds ocurre antes de la erradicación.

> **Consejo Ninja.** Los casos de Insider Risk Management y las alertas de Communication Compliance se pueden escalar a una investigación de eDiscovery; desde Communication Compliance se escalan hasta 100 mensajes por vez ([casos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases), [alertas de Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate)). La herramienta comunitaria [Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite) (GPL-2.0) adquiere UAL y MailItemsAccessed: valídala en laboratorio y úsala con cuentas de solo lectura.

**¿Tienes poco tiempo?**

- [Respond to a compromised email account in Microsoft 365](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Documentación
- [Azure Monitor Logs reference - OfficeActivity](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity) · Documentación
- [GitHub - invictus-ir/Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite) · GitHub

### Documentación, cursos y credenciales

- [Respond to a compromised email account in Microsoft 365](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Documentación · Oficial · Microsoft Learn (Defender for Office 365). Procedimiento de respuesta ante BEC: síntomas, contención (deshabilitar cuenta, reglas de bandeja, reenvíos) e investigación de la cuenta comprometida.
- [Azure Monitor Logs reference - OfficeActivity](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity) · Documentación · Oficial · Microsoft Learn. Esquema de la tabla OfficeActivity que Sentinel usa para los registros de auditoría de Exchange, SharePoint y Teams.
- [Stream data from Microsoft Purview Information Protection to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Documentación · Oficial · Vista previa · Microsoft Learn. Conector (preview) que envía eventos de etiquetado del registro de auditoría a la tabla MicrosoftPurviewInformationProtection de Sentinel. *Nota:* Advierte que si el workspace está en otra región que Office 365 los datos pueden transmitirse entre regiones (O3)

### Laboratorios, GitHub y herramientas

- [GitHub - invictus-ir/Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite) · GitHub · Comunidad · Invictus IR (Joey Rentenaar, Korstiaan Stam) · GitHub. Módulo PowerShell de código abierto para adquisición forense de UAL, auditoría de buzones, reglas, message trace, sesiones de MailItemsAccessed y registros de Entra.

### Comunidad: blogs, libros, newsletters y eventos

- [From Authorization to Action: Operationalizing CISA's Microsoft Cloud Logs Playbook in Sentinel](https://nineliveszerotrust.com/blog/cisa-microsoft-cloud-logs-sentinel/) · Blog · Comunidad · Nuevo · Jerrad Dahlager · Nine Lives Zero Trust · 10 may 2026. Mapa práctico de cobertura en Sentinel del playbook de CISA con consultas y validación de tablas (OfficeActivity, SigninLogs, AzureActivity).

**Manos a la obra**

1. `Laboratorio parcial` En un workspace de Sentinel pagado con los créditos de Visual Studio, conecta la auditoría de Microsoft 365 y verifica que llegan filas a `OfficeActivity`. Escribe una consulta KQL que reconstruya el BEC de [M3](02_Nivel_2_Intermedio.md#m3): creación de la regla y `MailItemsAccessed` de la cuenta. Limitación: volumen bajo y sin tráfico real ([OfficeActivity](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity)). Evidencia: consulta y resultado.
2. `Laboratorio parcial` Repite la reconstrucción en la búsqueda avanzada de Defender XDR con `CloudAppEvents` y compara con `OfficeActivity`: campos, latencia y cobertura. Limitación: necesitas datos de aplicaciones en la nube en el tenant y unas horas de actividad ([esquema de búsqueda avanzada](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables)). Evidencia: ambas consultas y tabla de diferencias.
3. `Laboratorio` Escribe el playbook de BEC con las fases de [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) y un paso explícito de preservación (hold y exportación de la auditoría con hash) antes de la erradicación, con los puntos de decisión de Legal y RR. HH. Pruébalo en una mesa de trabajo con tu simulación de [M3](02_Nivel_2_Intermedio.md#m3). Evidencia: playbook versionado y minuta de la prueba.
4. `Laboratorio parcial` Escala a eDiscovery: desde una alerta de Communication Compliance usa «Escalate for investigation», o desde un caso de Insider Risk Management usa el escalamiento a eDiscovery, y verifica el caso creado y su contenido. Limitación: requiere políticas configuradas (se ven en sus programas) y coincidencias del laboratorio, que pueden tardar ([alertas de Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate), [casos de IRM](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases)). Evidencia: caso escalado con su origen.
5. `Laboratorio` Adquiere la auditoría de la cuenta del BEC con [Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite) usando una cuenta de solo lectura, calcula el hash de lo adquirido, completa el formulario de custodia de [M4](02_Nivel_2_Intermedio.md#m4) y compara con tu extracción por AuditLogQuery. Evidencia: archivos con hash, formulario y diferencias.
6. `Solo producción` Lleva el circuito al SOC real: agrega al runbook de incidentes el paso «preservar antes de erradicar» y una consulta de búsqueda proactiva sobre reglas de reenvío sospechosas y picos de `MailItemsAccessed`. Cómo hacerlo seguro: primero como consulta de búsqueda sin acciones automáticas, dos semanas de revisión de falsos positivos con la jefatura del SOC y aprobación antes de convertirla en regla. Evidencia: runbook actualizado e informe de falsos positivos.

<a id="a4"></a>

## A4 · Investigaciones asistidas por IA: Security Copilot y Data Security Investigations

*L400 · ~4 h · Origen: Nuevo en esta edición*

**Security Copilot** está integrado en eDiscovery de dos formas: redacta consultas KeyQL a partir de lenguaje natural (vista previa) y genera resúmenes contextuales de ítems del review set y de casos. Trabaja con los permisos del usuario y consume unidades de cómputo de seguridad (SCU); Microsoft 365 E5 y E7 incluyen 400 SCU al mes por cada 1.000 licencias pagadas, con un tope de 10.000. Su acceso a datos de Microsoft 365 se limita a lo que procesa Purview, como los review sets.

**Data Security Investigations** (DSI), disponible en general desde enero de 2026, lleva la investigación de incidentes de datos a otra escala: búsqueda vectorial, categorización y examen con IA generativa sobre Exchange, Teams, SharePoint, OneDrive, Copilot y evidencias de Endpoint DLP, con integración con Defender XDR, Insider Risk Management, DSPM y la auditoría, y acciones de purga suave o dura. No requiere licencia: se factura por almacenamiento y por unidades de cómputo de DSI, y su cómputo de IA se ubica en Australia y Nueva Zelanda, la UE, el Reino Unido o EE. UU., u opcionalmente «en cualquier lugar». No hay opción en Latinoamérica.

**Por qué importa**

Después de una filtración la pregunta es qué datos sensibles quedaron expuestos y a quiénes afecta, y responderla a mano sobre miles de documentos lleva semanas. La IA acorta ese tiempo, pero introduce costos por uso y decisiones de ubicación del procesamiento que Legal y privacidad deben aprobar. Este módulo enseña a usarla con control de costos, de calidad y de jurisdicción.

**Qué vas a lograr**

- Usar Security Copilot en eDiscovery para redactar KeyQL y resumir ítems, validando siempre sus resultados.
- Describir el flujo de Data Security Investigations y sus integraciones con Defender XDR, Insider Risk Management, DSPM y Audit.
- Estimar el costo de una investigación de DSI y configurar alertas de presupuesto.
- Evaluar con Legal la ubicación del cómputo de IA y la retención de los datos de la investigación.

> **Novedad.** Data Security Investigations llegó a disponibilidad general a fines de enero de 2026 ([AMA oficial](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393)). En 2026 sumó insights proactivas en DSPM, en disponibilidad general desde junio ([MC1317196](https://mc.merill.net/message/MC1317196)), y OCR, en vista previa en mayo y disponible en general en julio ([roadmap](https://www.microsoft.com/releasecommunications/api/v2/m365/561489)).

> **Atención.** DSI no requiere licencia dedicada: se factura por almacenamiento (GB al mes) y por Data Security Investigations Compute Units, y las insights proactivas consumen ambos de forma continua. El cómputo de IA se ubica en Australia y Nueva Zelanda, la UE, el Reino Unido o EE. UU., o «en cualquier lugar»: no hay opción en Latinoamérica ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).

> **Consejo Ninja.** Security Copilot actúa en nombre del usuario y nunca excede sus permisos; sus roles owner y contributor no son roles de Entra ([autenticación](https://learn.microsoft.com/en-us/copilot/security/authentication)). Para usarlo en Purview hay que habilitar el origen de Purview ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)), y el consumo de SCU se revisa en un panel de 90 días exportable a Excel ([uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)).

> **Novedad.** El Posture Agent de DSI (vista previa) busca credenciales expuestas en SharePoint, OneDrive, Exchange y Teams, con tablero Kanban y puntajes de riesgo; consume SCU y no requiere configurar la facturación de DSI ([Posture Agent](https://learn.microsoft.com/en-us/purview/data-security-investigations-posture-agent)).

**¿Tienes poco tiempo?**

- [Learn about Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations) · Documentación
- [Billing in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Documentación
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación

### Documentación, cursos y credenciales

- [Learn about Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jun 2026. Describe DSI: búsqueda vectorial, categorización y examen con IA generativa, purga suave/dura e integración con Defender XDR, Insider Risk, DSPM, UAL y evidencias de Endpoint DLP.
- [Billing in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Documentación · Oficial · Microsoft Learn. Detalla el medidor de almacenamiento (GB/mes) y las Data Security Investigations Compute Units, ubicaciones de cómputo (ANZ, EU, UK, US u opción global) y buenas prácticas de costos.
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn. Resume las experiencias integradas y standalone de Security Copilot en Purview, incluido el resumen contextual de casos de eDiscovery.
- [MC1317196 - Data Security Investigations: Proactive AI insights in DSPM](https://mc.merill.net/message/MC1317196) · Documentación · Oficial · Nuevo · Message Center (archivo mc.merill.net) · 20 may 2026. Insights proactivas de DSI dentro de DSPM para posibles exfiltraciones, con despliegue GA a inicios de junio de 2026.
- [Search, review, and refine results in Data Security Investigations](https://learn.microsoft.com/en-us/purview/data-security-investigations-search) · Documentación · Oficial · Microsoft Learn. Búsqueda en DSI sobre Exchange, Teams, SharePoint, OneDrive, Copilot y evidencias de Endpoint DLP, con búsqueda por auditoría y estadísticas antes de agregar al alcance.
- [Pricing - Microsoft Purview | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/purview/) · Documentación · Oficial · Microsoft Azure. Página de precios de consumo de Purview que describe los dos medidores de DSI (almacenamiento por GB y Compute Units) y otros medidores de seguridad de datos.
- [Microsoft Purview: Data Security Investigations – Introducing OCR support (Roadmap 561489)](https://www.microsoft.com/releasecommunications/api/v2/m365/561489) · Documentación · Oficial · Nuevo · Microsoft 365 Roadmap · jul 2026. Entrada de roadmap: DSI agrega OCR para analizar texto en imágenes, en preview desde mayo y GA en julio de 2026.

### Comunidad: blogs, libros, newsletters y eventos

- [Ask Microsoft Anything: Purview Data Security Investigations Part 2](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393) · Evento · Empleado de Microsoft · Trevor_Rusher · Microsoft Tech Community · 5 feb 2026. AMA oficial que anuncia la disponibilidad general de DSI y repasa nuevas funciones y el modelo de negocio refinado.
- [Microsoft brings AI-powered investigations to security teams (Help Net Security)](https://www.helpnetsecurity.com/2026/01/27/microsoft-purview-data-security-investigations/) · Blog · Comunidad · Sinisa Markovic · Help Net Security · 27 ene 2026. Nota de prensa sobre la GA de DSI con casos de uso (filtraciones, credenciales expuestas, fraude), acción de purga y precios por uso.

**Manos a la obra**

1. `Laboratorio parcial` En un caso piloto con datos sintéticos, usa Security Copilot para redactar una consulta KeyQL, resumir tres ítems del review set y resumir el caso; valida cada salida contra tu lectura y anota el consumo en el panel de uso. Limitación: la inclusión de SCU aplica a licencias E5 pagadas; en producción, solo un caso piloto con datos de prueba ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview), [uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)). Evidencia: tabla de validación y consumo.
2. `Laboratorio parcial` Con el pago por uso asociado en [P0](01_Nivel_1_Inicial.md#p0), configura Data Security Investigations y crea una investigación sobre uno o dos buzones de prueba con datos sensibles sintéticos; ejecuta la categorización y el examen con IA, anota GB y unidades de cómputo consumidas y elimina la investigación al terminar. Limitación: tiene costo por uso y los datos sintéticos no representan un incidente real ([empezar con DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started), [facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)). Evidencia: consumo registrado y captura de la eliminación.
3. `Laboratorio` Prepara la decisión de ubicación del cómputo de IA de DSI para cada país donde operas (Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar») con las preguntas que debe responder Legal, sin interpretar la ley. Evidencia: entrada en el registro de decisiones de [O3](04_Nivel_4_Operacion.md#o3) ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).
4. `Laboratorio parcial` Crea una investigación de DSI desde un caso de Insider Risk Management de prueba, con el contexto en lenguaje natural, y revisa la búsqueda por auditoría antes de agregar datos al alcance. Limitación: necesitas un caso de IRM en el laboratorio ([crear una investigación](https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation), [buscar en DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-search)). Evidencia: investigación con su origen y alcance.
5. `Solo producción` Usa DSI en un incidente de datos real. Cómo hacerlo seguro: alcance mínimo, estimación de costo previa, presupuesto y alertas de Azure al 50, 75 y 90 %, ubicación del cómputo aprobada por Legal y privacidad, ninguna purga sin aprobación escrita y revisión de holds, y eliminación de la investigación al cerrar ([DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations)). Evidencia: aprobaciones, consumo y acta de cierre.

**¿Quieres profundizar?**

- [Ask Microsoft Anything: Purview Data Security Investigations Part 2](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393) · Evento

<a id="reto-avanzado"></a>

## Reto del nivel

**Incidente con IA, automatización y SOC.** Un agente o Copilot consultó un documento etiquetado como confidencial y el SOC pide reconstruir qué pasó. Entrega: un script sobre Microsoft Graph que abre el caso, aplica el hold y extrae la auditoría con AuditLogQuery (con manejo de HTTP 429); el registro de auditoría de la interacción interpretado (`AccessedResources`, `SensitivityLabelId`, `XPIADetected`, `AgentId`); la misma reconstrucción en `OfficeActivity` de Sentinel o en `CloudAppEvents` de Defender XDR; la estimación de costo y la propuesta de ubicación del cómputo si se escalara a Data Security Investigations; y, si tienes capacidad de Security Copilot, un resumen del caso validado frente a tu lectura. Sin licencias de Copilot, documenta el diseño con datos sintéticos y marca qué quedó sin probar.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Dónde se guardan los prompts y respuestas de Copilot que eDiscovery puede buscar, retener y exportar?
   - a) En el OneDrive del usuario
   - b) En el workspace de Sentinel
   - c) En el buzón del usuario
   - d) En el review set del caso

2. ¿Qué rol se requiere para eliminar datos de IA con el flujo de búsqueda y eliminación de eDiscovery?
   - a) eDiscovery Manager
   - b) Audit Reader
   - c) Reviewer
   - d) Search And Purge

3. La auditoría de interacciones con apps de IA no Microsoft (AIAppInteraction)…
   - a) …está incluida en E5 sin costo adicional
   - b) …requiere pago por uso y se retiene 180 días
   - c) …requiere Audit (Premium) y se retiene un año
   - d) …no se audita

4. En un registro de auditoría de Copilot, ¿qué propiedad de los recursos consultados señala una posible inyección de instrucciones?
   - a) AgentId
   - b) AppAccessContext
   - c) XPIADetected
   - d) InternetMessageId

5. ¿Qué reemplaza a Search-UnifiedAuditLog, que se retira el 15 de octubre de 2027?
   - a) La API AuditLogQuery de Microsoft Graph
   - b) La Management Activity API
   - c) Get-AdminAuditLogConfig
   - d) Content Search

6. ¿Cuál de estos es un límite documentado de AuditLogQuery por tenant?
   - a) Diez consultas por día
   - b) Mil registros por consulta
   - c) Una consulta en cola por usuario
   - d) 200 envíos cada 24 horas

7. Con E3 y permisos delegados, ¿qué automatizas con la API de eDiscovery de Graph sin pago adicional?
   - a) Casos, búsquedas y holds
   - b) Review sets y analítica
   - c) Autenticación solo aplicación
   - d) Descargas masivas

8. Desde agosto de 2026, ¿qué no admiten los cmdlets de eDiscovery de Security & Compliance PowerShell?
   - a) La creación de holds
   - b) La autenticación solo aplicación
   - c) Las búsquedas
   - d) La purga

9. En la Management Activity API, ¿cuánto puede tardar el primer blob después de crear una suscripción?
   - a) Cinco minutos
   - b) Una hora
   - c) Hasta 12 horas
   - d) Siete días

10. ¿Qué tabla de Sentinel contiene la auditoría de Exchange, SharePoint y Teams?
   - a) SigninLogs
   - b) AzureActivity
   - c) CloudAppEvents
   - d) OfficeActivity

11. ¿Qué advierte el conector de Purview Information Protection para Sentinel (vista previa)?
   - a) Que solo funciona con Audit (Premium)
   - b) Que, si el workspace está en otra región que Office 365, los datos pueden transmitirse entre regiones
   - c) Que no admite el nivel data lake
   - d) Que requiere Security Copilot

12. ¿Cómo se licencia Data Security Investigations?
   - a) Incluida en Microsoft 365 E5
   - b) Complemento por usuario
   - c) Pago por uso de almacenamiento y Compute Units
   - d) Solo con capacidad aprovisionada de Security Copilot

13. ¿Dónde puede ejecutarse el cómputo de IA de Data Security Investigations?
   - a) Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»
   - b) En la región del tenant, incluida Latinoamérica
   - c) Solo en EE. UU.
   - d) En el workspace de Sentinel

14. ¿Qué afirmación sobre Security Copilot en eDiscovery es correcta?
   - a) Puede ver todos los casos aunque el usuario no sea miembro
   - b) Requiere el rol eDiscovery Administrator
   - c) Ejecuta exportaciones automáticamente
   - d) Actúa en nombre del usuario y nunca excede sus permisos

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

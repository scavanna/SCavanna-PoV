# Nivel 3 · Avanzado · Evidencia, conectores y supervisión regulada

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Conectores de terceros, reportes y evidencia de auditoría (con la migración a la API de Microsoft Graph), automatización con Power Automate y APIs, y supervisión regulada del sector financiero. Terminas con un paquete de evidencia de supervisión reproducible.

*L400 · 4 módulos · ~14 horas · 16 recursos*

**Módulos de este nivel:** [A1 Conectores de terceros](#a1) · [A2 Reportes y auditoría](#a2) · [A3 Power Automate y APIs](#a3) · [A4 Supervisión financiera](#a4)

<a id="a1"></a>

## A1 · Conectores de datos de terceros

*L400 · ~3 h · Origen: Ninja oficial de CC · comunicaciones que no son de Microsoft*

Muchas comunicaciones reguladas no ocurren en Microsoft 365: mesas de negociación en Instant Bloomberg o ICE Chat, mensajería móvil de asesores, redes sociales corporativas o asistentes de IA de terceros. Los **conectores de datos** de Purview importan esos mensajes a buzones de Microsoft 365 para aplicarles Communication Compliance, retención y eDiscovery. Hay conectores nativos —Instant Bloomberg, Bloomberg Message, ICE Chat, LinkedIn, ChatGPT Enterprise y Anthropic Claude, entre otros— y conectores de partners (TeleMessage, 17a-4 LLC y CellTrust); los de Veritas se retiraron el 30 de junio de 2024.

Cada conector tiene requisitos propios. Instant Bloomberg se conecta a diario al sitio SFTP de Bloomberg con claves PGP y SSH, requiere una suscripción Bloomberg Anywhere y mapea usuarios por CorporateEmailAddress o con un CSV; los mensajes sin un usuario válido no se importan. Los conectores de partners requieren una entidad de servicio aprovisionada, el rol Data Connector Admin y una relación comercial con el partner, y los datos que procesa el tercero quedan fuera de los compromisos de Purview. El contenido de terceros llega a CC con una latencia de 24 a 48 horas, y la retención de lo importado se profundiza en el programa de Data Lifecycle y Records Management.

**Por qué importa**

Si la supervisión regulada se limita a correo y Teams, el regulador encontrará el punto ciego en el canal que no conectaste. Los conectores llevan esas comunicaciones al mismo flujo de revisión, retención y evidencia, con un costo y un riesgo contractual que Legal y compras deben evaluar antes de firmar.

**Qué vas a lograr**

- Elegir entre un conector nativo y uno de partner según el canal y el contrato.
- Describir los prerrequisitos de Instant Bloomberg y de un conector de partner.
- Diseñar el mapeo de usuarios y el monitoreo del estado del conector.
- Evaluar con Legal los riesgos contractuales y de residencia de datos del partner.

> **Qué cambió.** Los conectores de Veritas se retiraron el 30 de junio de 2024; hoy los partners son TeleMessage, 17a-4 LLC y CellTrust, y sus conectores requieren una entidad de servicio aprovisionada ([conectores de datos](https://learn.microsoft.com/en-us/purview/archive-third-party-data)).

> **Atención.** Licencias: cada usuario beneficiado necesita E5, E5 IP&G, Purview Suite, E5 IRM, E5 eDiscovery and Audit u Office 365 E5, y los conectores de partners exigen además una relación comercial con el partner ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

> **Consejo Ninja.** Instant Bloomberg requiere una suscripción Bloomberg Anywhere y un sitio BB-SFTP, y los elementos sin un usuario válido no se importan: valida el CSV de mapeo antes de la primera importación ([Instant Bloomberg](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data)). En los conectores de partners, los datos que procesa el tercero quedan fuera de los compromisos de Purview: revisa contrato y residencia con Legal ([conector de 17a-4](https://learn.microsoft.com/en-us/purview/archive-17a-4-bloomberg-data)).

**¿Tienes poco tiempo?**

- [Use data connectors to import and archive third-party data in Microsoft 365](https://learn.microsoft.com/en-us/purview/archive-third-party-data) · Documentación
- [Set up a connector to archive Instant Bloomberg data](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data) · Documentación
- [Set up a connector to archive Bloomberg data in Microsoft 365 (17a-4 DataParser)](https://learn.microsoft.com/en-us/purview/archive-17a-4-bloomberg-data) · Documentación

### Documentación, cursos y credenciales

- [Use data connectors to import and archive third-party data in Microsoft 365](https://learn.microsoft.com/en-us/purview/archive-third-party-data) · Documentación · Oficial · Microsoft Learn. Catálogo de conectores nativos (Instant Bloomberg, Bloomberg Message, ICE Chat, ChatGPT Enterprise, Anthropic Claude, etc.) y de socios TeleMessage, 17a-4 LLC y CellTrust, con soluciones de Purview aplicables (incluida Communication Compliance).
- [Set up a connector to archive Instant Bloomberg data](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data) · Documentación · Oficial · Microsoft Learn. Conector nativo que se conecta diariamente al SFTP de Bloomberg (claves PGP/SSH), convierte los chats a formato de correo y los importa a buzones para aplicar CC, retención y eDiscovery.
- [Set up a connector to archive Bloomberg data in Microsoft 365 (17a-4 DataParser)](https://learn.microsoft.com/en-us/purview/archive-17a-4-bloomberg-data) · Documentación · Oficial · Microsoft Learn. Ejemplo de conector de partner (17a-4 LLC): requiere cuenta DataParser, rol Data Connector Admin y una entidad de servicio aprovisionada; importa a buzones para aplicar CC y retención.

**Manos a la obra**

1. `Laboratorio` Revisa el catálogo de conectores y elabora la matriz de tus canales de terceros: conector nativo o de partner, contrato requerido, licencias y soluciones de Purview compatibles con cada uno ([conectores de datos](https://learn.microsoft.com/en-us/purview/archive-third-party-data)).
2. `Laboratorio` Diseña el CSV de mapeo de usuarios de Instant Bloomberg con cuentas de prueba y define cómo detectarás los elementos que no se importan por falta de un usuario válido ([Instant Bloomberg](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data)).
3. `Solo producción` Configura un conector Instant Bloomberg o de un partner (17a-4, TeleMessage). Por qué: requiere contrato con Bloomberg o con el partner, BB-SFTP y una entidad de servicio. Práctica segura: piloto con 1 o 2 buzones mapeados por CSV, política de CC solo de revisión con muestreo, monitoreo del estado del conector y de la auditoría `ComplianceConnector`, y contrato y acuerdo de tratamiento revisados por Legal ([Instant Bloomberg](https://learn.microsoft.com/en-us/purview/archive-instant-bloomberg-data), [conector de 17a-4](https://learn.microsoft.com/en-us/purview/archive-17a-4-bloomberg-data)).
4. `Solo producción` Aplica una política de CC sobre el contenido importado por el conector y mide la latencia real frente a las 24 a 48 horas documentadas. Por qué: requiere datos reales del canal. Práctica segura: población acotada, revisores seudonimizados y desactivación de la política como reversión ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).

<a id="a2"></a>

## A2 · Reportes, auditoría y evidencia de supervisión

*L400 · ~4 h · Origen: Ninja oficial de CC · reportes y auditoría*

Communication Compliance ofrece widgets y reportes detallados —por política, ubicación, usuario, tipos de información confidencial por ubicación y remitentes de envíos masivos— y el reporte **Message details**, del que puedes programar hasta 5 por política. Las unidades administrativas no aplican a los reportes, así que cuida quién los recibe. Para la evidencia de supervisión, el registro de auditoría guarda operaciones como `SupervisionRuleMatch`, `SupervisionPolicyCreated`, `SupervisionPolicyUpdated`, `SupervisionPolicyDeleted` y `SupervisoryReviewTag` (tipo de registro `ComplianceSupervisionExchange`); Information Barriers usa `InformationBarrierPolicyApplication` y los conectores, `ComplianceConnector`.

Aquí está el cambio más urgente del programa: la documentación indica que las actividades de CC solo se consultan con `Search-UnifiedAuditLog`, y ese cmdlet **se retira el 15 de octubre de 2027**. La API **AuditLogQuery** de Microsoft Graph está en disponibilidad general desde octubre de 2026, con hasta 1 millón de registros por consulta, 200 búsquedas cada 24 horas y 50 en cola por tenant. La retención depende de la licencia: 180 días con Audit (Standard), hasta 1 año con Audit (Premium) y 10 años con un complemento por usuario. La auditoría como disciplina se profundiza en el programa de eDiscovery y Audit (módulos I2 y M3).

**Por qué importa**

La supervisión que no deja evidencia no existe para un auditor. Reportes programados y consultas de auditoría reproducibles demuestran qué se revisó, quién lo hizo y cuándo; migrar a tiempo a la API de Microsoft Graph evita que los scripts de evidencia dejen de funcionar en octubre de 2027, justo cuando un regulador podría pedirlos.

**Qué vas a lograr**

- Generar y programar los reportes de Communication Compliance y controlar su distribución.
- Consultar las operaciones de auditoría de CC, IB y conectores por tipo de registro.
- Migrar una consulta de evidencia de Search-UnifiedAuditLog a la API AuditLogQuery.
- Alinear la retención de auditoría con los plazos de evidencia que exige tu organización.

> **Atención.** Las actividades de CC (`SupervisionRuleMatch`, `SupervisionPolicyCreated`, `SupervisionPolicyUpdated`, `SupervisionPolicyDeleted` y `SupervisoryReviewTag`) solo se consultan con `Search-UnifiedAuditLog`; no aparecen en la lista de actividades del portal de auditoría ([actividades de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-activities)).

> **Novedad.** Octubre de 2026: la API AuditLogQuery de Microsoft Graph es GA (hasta 1 millón de registros por consulta, 200 búsquedas cada 24 horas y 50 en cola por tenant) y `Search-UnifiedAuditLog` se retira el 15 de octubre de 2027, sin opción de excepción ([MC1505599](https://mc.merill.net/message/MC1505599)). Prueba en tu tenant que las operaciones de CC salgan por la API antes de migrar los scripts de evidencia.

> **Consejo Ninja.** Filtra por tipo de registro en scripts y en el SIEM: `ComplianceSupervisionExchange` (CC), `InformationBarrierPolicyApplication` (IB) y `ComplianceConnector` (conectores) ([tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services)). Retención: 180 días con Audit (Standard), hasta 1 año con Premium y 10 años con un complemento por usuario ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).

> **Atención.** Las unidades administrativas no aplican a los reportes de CC y el buzón de cada política está limitado a 100 GB o 1 millón de mensajes; el reporte Message details admite hasta 5 reportes programados por política ([reportes y auditoría](https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits)).

**¿Tienes poco tiempo?**

- [Use Communication Compliance reports and audits](https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits) · Documentación
- [Audit log activities (Communication compliance and Information barriers activities)](https://learn.microsoft.com/en-us/purview/audit-log-activities) · Documentación
- [MC1505599 - Microsoft Purview Audit: AuditLogQuery API generally available and Search-UnifiedAuditLog retiring](https://mc.merill.net/message/MC1505599) · Herramienta
- [Microsoft services that support auditing (record types)](https://learn.microsoft.com/en-us/purview/audit-supported-services) · Documentación

**Evidencia de auditoría de Communication Compliance, Information Barriers y conectores**

| Operación o tipo de registro | Qué registra | Cómo se consulta hoy | Antes del 15 de octubre de 2027 | Fuente |
|---|---|---|---|---|
| SupervisionRuleMatch | Un mensaje coincidió con una política de CC | Search-UnifiedAuditLog (no figura en la lista de actividades del portal) | Migrar a la API AuditLogQuery y verificar que la operación aparece | [Actividades](https://learn.microsoft.com/en-us/purview/audit-log-activities) |
| SupervisionPolicyCreated, SupervisionPolicyUpdated y SupervisionPolicyDeleted | Creación, cambio o eliminación de políticas de CC | Search-UnifiedAuditLog | Migrar a la API y alertar sobre cambios en el SIEM | [Actividades](https://learn.microsoft.com/en-us/purview/audit-log-activities) |
| SupervisoryReviewTag | Etiqueta aplicada por un revisor | Search-UnifiedAuditLog | Migrar a la API e incluirla en el informe mensual para privacidad | [Actividades](https://learn.microsoft.com/en-us/purview/audit-log-activities) |
| ComplianceSupervisionExchange | Tipo de registro de Communication Compliance | Filtro RecordType en el cmdlet | Filtro por tipo de registro en la API | [Tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services) |
| InformationBarrierPolicyApplication | Aplicación de políticas de Information Barriers | Búsqueda de auditoría o cmdlet | Filtro por tipo de registro en la API | [Tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services) |
| ComplianceConnector | Actividad de los conectores de datos | Búsqueda de auditoría o cmdlet | Filtro por tipo de registro en la API | [Tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services) |

Fuentes: [actividades de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-activities), [tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services) y [MC1505599](https://mc.merill.net/message/MC1505599).

### Documentación, cursos y credenciales

- [Use Communication Compliance reports and audits](https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jun 2026. Widgets y reportes detallados (por política, ubicación, usuario, SIT por ubicación, remitentes de email blast), reporte Message details programable y auditoría con Search-UnifiedAuditLog.
- [Audit log activities (Communication compliance and Information barriers activities)](https://learn.microsoft.com/en-us/purview/audit-log-activities) · Documentación · Oficial · Microsoft Learn. Catálogo de operaciones del registro unificado: para CC registra SupervisionRuleMatch, SupervisionPolicyCreated/Updated/Deleted y SupervisoryReviewTag, además de una tabla específica de actividades de Information Barriers.
- [Learn about auditing solutions in Microsoft Purview](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) · Documentación · Oficial · Microsoft Learn. Compara Audit (Standard) y Audit (Premium): búsqueda en portal, Audit Search Graph API, Search-UnifiedAuditLog, exportación CSV, Management Activity API, retención de 180 días, 1 año y 10 años (complemento).
- [Microsoft services that support auditing (record types)](https://learn.microsoft.com/en-us/purview/audit-supported-services) · Documentación · Oficial · Microsoft Learn · 18 feb 2026. Tabla de tipos de registro por servicio: Communication compliance usa ComplianceSupervisionExchange, Information barriers usa InformationBarrierPolicyApplication y los conectores de datos ComplianceConnector.

### Laboratorios, GitHub y herramientas

- [MC1505599 - Microsoft Purview Audit: AuditLogQuery API generally available and Search-UnifiedAuditLog retiring](https://mc.merill.net/message/MC1505599) · Herramienta · Oficial · Nuevo · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 12 oct 2026. Anuncio oficial: la API AuditLogQuery de Microsoft Graph es GA desde inicios de octubre de 2026 (hasta 1 millón de registros por consulta) y el cmdlet Search-UnifiedAuditLog se retira el 15-oct-2027 sin opción de excepción.

**Manos a la obra**

1. `Laboratorio` Programa el reporte Message details de tu política piloto y verifica quién lo recibe; documenta que las unidades administrativas no filtran los reportes y cómo controlarás su distribución ([reportes y auditoría](https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits)).
2. `Laboratorio` Consulta eventos `SupervisionRuleMatch` y `SupervisionPolicyUpdated` con `Search-UnifiedAuditLog`, filtrando por el tipo de registro `ComplianceSupervisionExchange`, y guarda la salida ([actividades](https://learn.microsoft.com/en-us/purview/audit-log-activities), [tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services)).
3. `Laboratorio` Repite la consulta con la API AuditLogQuery de Microsoft Graph, compara resultados y documenta el plan de migración antes del 15 de octubre de 2027 ([auditLogQuery](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0), [MC1505599](https://mc.merill.net/message/MC1505599)).
4. `Laboratorio` Aplica una política de IB de prueba, consulta los eventos `InformationBarrierPolicyApplication` y anota el tiempo entre el cambio y el evento ([tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services)).
5. `Laboratorio` Compara la retención de auditoría de tu tenant con el plazo de evidencia que necesita tu área de cumplimiento y documenta la brecha y la licencia que la cerraría ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).

<a id="a3"></a>

## A3 · Automatización con Power Automate, PowerShell y APIs

*L400 · ~3 h · Origen: Ninja oficial de CC · integración con Power Automate y SIEM, ampliado a Microsoft Graph*

Power Automate se integra con las alertas de Communication Compliance: desde una alerta puedes crear, compartir, editar o eliminar flujos, y la plantilla «Notify manager when a user has a Communication Compliance alert» resuelve el caso más común. La plantilla por defecto no requiere licencias adicionales de Power Automate, aunque las funciones premium o el conector de Purview pueden requerirlas. En el plano programático, la API AuditLogQuery de Microsoft Graph (v1.0) permite extraer eventos de CC e IB hacia informes, expedientes de evidencia o un SIEM como Microsoft Sentinel.

Ojo con PowerShell. La página de políticas afirma que no es compatible para crear o administrar políticas de CC, pero los cmdlets heredados `*-SupervisoryReviewPolicyV2` siguen documentados en Security & Compliance PowerShell e incluso mencionan el portal retirado. La recomendación prudente es usarlos solo para inventario o lectura, en el laboratorio. Para Information Barriers, en cambio, PowerShell es la vía principal: segmentos, políticas, aplicación de políticas y reportes de SharePoint. La automatización con Microsoft Graph y PowerShell a escala se profundiza en el programa de eDiscovery y Audit (módulo A2).

**Por qué importa**

Automatizar las tareas repetitivas —avisos a gerentes o a RR. HH., extracción de evidencia, alimentación del SIEM— libera tiempo de revisión y reduce errores manuales. Hacerlo con las APIs vigentes, y no con cmdlets en retiro o sin soporte, evita que el proceso se rompa justo cuando el regulador pide evidencia.

**Qué vas a lograr**

- Crear un flujo de Power Automate desde una alerta de CC con la plantilla de aviso.
- Consultar eventos de CC e IB con la API AuditLogQuery de Microsoft Graph.
- Decidir qué automatizar con PowerShell (Information Barriers) y qué no (políticas de CC).
- Documentar licencias, permisos, propietario y reversión de cada automatización.

> **Atención.** PowerShell y CC: la página de políticas dice que no es compatible para crear o administrar políticas, pero los cmdlets `*-SupervisoryReviewPolicyV2` siguen documentados y mencionan el portal retirado ([New-SupervisoryReviewPolicyV2](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-supervisoryreviewpolicyv2?view=exchange-ps)). Úsalos solo para inventario, en el laboratorio.

> **Consejo Ninja.** La plantilla «Notify manager when a user has a Communication Compliance alert» no requiere licencias adicionales de Power Automate; las funciones premium o el conector de Purview pueden requerirlas ([Power Automate](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate)). Define un propietario y una cuenta de servicio para cada flujo.

> **Novedad.** La API AuditLogQuery (v1.0) crea consultas asíncronas del registro de auditoría filtrables por tipo de registro, operación, usuario y fechas, con ejemplos en varios SDK y PowerShell; la página indica disponibilidad solo en la nube global ([auditLogQuery](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0)).

**¿Tienes poco tiempo?**

- [Use Microsoft Power Automate with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate) · Documentación
- [Get auditLogQuery - Microsoft Graph v1.0 (Audit Search API)](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0) · Documentación
- [New-SupervisoryReviewPolicyV2 (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-supervisoryreviewpolicyv2?view=exchange-ps) · Documentación

### Documentación, cursos y credenciales

- [Use Microsoft Power Automate with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate) · Documentación · Oficial · Microsoft Learn. Cómo crear, compartir, editar y borrar flujos de Power Automate desde una alerta; incluye la plantilla 'Notify manager when a user has a Communication Compliance alert'.
- [Get auditLogQuery - Microsoft Graph v1.0 (Audit Search API)](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn (Microsoft Graph). API de Microsoft Graph (v1.0) para crear y leer consultas asíncronas del registro de auditoría de Purview, filtrables por tipo de registro, operación, usuario y fechas, con ejemplos en varios SDK y PowerShell.
- [New-SupervisoryReviewPolicyV2 (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-supervisoryreviewpolicyv2?view=exchange-ps) · Documentación · Oficial · Legado aún útil · Microsoft Learn (PowerShell reference). Referencia del cmdlet de Security & Compliance PowerShell heredado de Supervision para crear políticas de revisión supervisora (nombre, revisores, preservación, cargas de trabajo de reportes de usuario). *Nota:* Contradicción: la página 'Create and manage Communication Compliance policies' afirma que PowerShell no es compatible para crear/gestionar políticas de CC; usar estos cmdlets solo para inventario/lectura y bajo pruebas. El texto aún menciona el portal de cumplimiento retirado

**Manos a la obra**

1. `Laboratorio` Crea un flujo de Power Automate desde una alerta de CC con la plantilla «Notify manager when a user has a Communication Compliance alert» que avise a una cuenta de prueba de RR. HH.; documenta licencias, propietario y cómo desactivarlo ([Power Automate](https://learn.microsoft.com/en-us/purview/communication-compliance-power-automate)).
2. `Laboratorio` Escribe un script con la API AuditLogQuery que extraiga cada semana los eventos de CC e IB a un CSV con hash de integridad para el expediente de evidencia ([auditLogQuery](https://learn.microsoft.com/en-us/graph/api/security-auditlogquery-get?view=graph-rest-1.0)).
3. `Laboratorio` En el laboratorio, lista tus políticas con la familia de cmdlets SupervisoryReviewPolicyV2 solo como inventario de lectura, compara la salida con el portal y documenta por qué no los usarás para crear políticas ([cmdlet](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/new-supervisoryreviewpolicyv2?view=exchange-ps), [políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
4. `Laboratorio parcial` Envía los eventos de auditoría de CC e IB a Microsoft Sentinel o a tu SIEM y crea una alerta por cambios en políticas (`SupervisionPolicyUpdated` y `SupervisionPolicyDeleted`). Limitación: requiere un workspace con ingesta, que tiene costo; usa la suscripción de laboratorio con presupuesto (la ingesta se profundiza en el programa de Sentinel) ([tipos de registro](https://learn.microsoft.com/en-us/purview/audit-supported-services)).

<a id="a4"></a>

## A4 · Escenarios regulatorios del sector financiero

*L400 · ~4 h · Origen: Nuevo en esta edición (amplía el escenario regulatorio del Ninja oficial)*

La supervisión de comunicaciones nació en el sector financiero. La plantilla de cumplimiento normativo financiero aplica seis clasificadores —Customer complaints, Gifts & entertainment, Money laundering, Regulatory collusion, Stock manipulation y Unauthorized disclosure— que la documentación asocia a obligaciones de EE. UU. como FINRA 4530, 4513 y 2111 (quejas), FCPA y FINRA 2320 (regalos), BSA y FINRA 3310 (lavado), FINRA 2372 y 5270 (manipulación) y FINRA 2010 y SEC 10b-5 (divulgación), con una revisión del 10 %. Todos funcionan **solo en inglés**, así que en MCSA necesitas diccionarios en español.

Dos lecciones atraviesan el módulo. Primera: supervisar no es conservar. Las reglas de conservación (SEC 17a-4, FINRA 4511, CFTC 1.31) se cubren con la retención de Purview, que el programa de Data Lifecycle y Records Management profundiza en su módulo A4; la revisión (FINRA 3110) exige que un principal registrado revise y deje evidencia escrita, y CC la apoya, pero no reemplaza los procedimientos de supervisión escritos. Segunda: en MCSA los reguladores son locales; las reglas de EE. UU. sirven como referencia de diseño, nunca como interpretación de tu obligación, que corresponde a Cumplimiento y Legal.

Verás también cómo combinar CC con barreras éticas (Information Barriers), conectores de mensajería financiera y la integración con Insider Risk en una arquitectura de supervisión para una mesa de negociación.

**Por qué importa**

Para un banco, una casa de bolsa o una aseguradora, la supervisión de comunicaciones es una obligación, no una buena práctica. Un diseño que combina plantillas, diccionarios en español, conectores, barreras éticas y evidencia de revisión reduce el riesgo de sanciones y acorta las respuestas a los requerimientos del regulador.

**Qué vas a lograr**

- Mapear los seis clasificadores financieros a los riesgos de conducta que detectan y a sus límites de idioma.
- Distinguir las obligaciones de conservación y de revisión, y qué solución de Purview cubre cada una.
- Diseñar una supervisión por muestreo con diccionarios en español y revisores designados.
- Combinar CC, Information Barriers y conectores en una arquitectura para una mesa de negociación.

> **Atención.** Los seis clasificadores financieros funcionan solo en inglés (mínimo 6 palabras), Customer complaints solo evalúa archivos .msg y .eml en CC y Regulatory collusion genera ruido con boletines, que se reduce con Filter email blasts ([definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)).

> **Consejo Ninja.** Supervisar no es conservar: FINRA 3110 exige que un principal registrado revise y deje evidencia escrita; CC apoya esa revisión, pero no reemplaza los procedimientos de supervisión escritos ([guía de un partner](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/)). La conservación (SEC 17a-4, FINRA 4511, CFTC 1.31) se cubre con retención; la opción de registro de auditoría o WORM rige desde el 3 de enero de 2023 ([oferta SEC 17a-4](https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs)).

> **Novedad.** La evaluación de Cohasset (julio de 2022) concluye que Exchange, Teams, SharePoint, OneDrive y Viva Engage, bien configurados, cumplen SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31; la página de requisitos regulatorios se actualizó el 26 de septiembre de 2025 ([requisitos regulatorios](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements)).

> **Atención.** Usa con cautela las fuentes comunitarias: el marco FSI Copilot Governance (control 3.4, septiembre de 2026) mapea FINRA 3110, FINRA 2210 y Reg BI a políticas de CC sobre comunicaciones asistidas por Copilot, pero repite una licencia antigua («Office 365 E3 + Advanced Compliance») ([control 3.4](https://judeper.github.io/FSI-CopilotGov/controls/pillar-3-compliance/3.4-communication-compliance/)). Las reglas de EE. UU. son referencia de diseño; tu obligación la define el regulador local con Legal.

**¿Tienes poco tiempo?**

- [Securities and Exchange Commission (SEC) Rule 17a-4, SEC Rule 18a-6, FINRA 4511, & CFTC 1.31 United States](https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs) · Documentación
- [FINRA and SEC Recordkeeping in Microsoft 365: An IT Guide](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/) · Blog
- [Resources to help you meet regulatory requirements for data lifecycle management and records management](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Documentación
- [FSI Copilot Governance Framework - Control 3.4: Communication Compliance Monitoring](https://judeper.github.io/FSI-CopilotGov/controls/pillar-3-compliance/3.4-communication-compliance/) · GitHub

### Documentación, cursos y credenciales

- [Securities and Exchange Commission (SEC) Rule 17a-4, SEC Rule 18a-6, FINRA 4511, & CFTC 1.31 United States](https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs) · Documentación · Oficial · Microsoft Learn (Microsoft Compliance). Oferta de cumplimiento: requisitos de registros electrónicos (opción de audit trail o WORM vigente desde el 3-ene-2023), servicios en alcance (incluye Copilot, Exchange, Teams y Viva Engage) y evaluaciones independientes de Cohasset.
- [Resources to help you meet regulatory requirements for data lifecycle management and records management](https://learn.microsoft.com/en-us/purview/retention-regulatory-requirements) · Documentación · Oficial · Microsoft Learn · 26 sep 2025. Enlaza la evaluación de Cohasset (julio 2022) que concluye que SharePoint, OneDrive, Exchange, Teams y Viva Engage, bien configurados, cumplen SEC 17a-4(f), FINRA 4511(c) y CFTC 1.31.
- [Key compliance and security considerations for US banking and capital markets (archived)](https://learn.microsoft.com/th-th/previous-versions/microsoft-365/solutions/financial-services-secure-collaboration) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Guía (con aportes de Protiviti) para banca y mercados de capitales de EE. UU. que cubre barreras éticas con Information Barriers, control de supervisión (Communication Compliance), insider risk e ingesta de datos de terceros. *Nota:* Artículo archivado (previous-versions) con ilustraciones de noviembre de 2020; la URL visible tiene locale th-th pero el contenido está en inglés; nombres antiguos (Supervision, Advanced Compliance)

### Laboratorios, GitHub y herramientas

- [FSI Copilot Governance Framework - Control 3.4: Communication Compliance Monitoring](https://judeper.github.io/FSI-CopilotGov/controls/pillar-3-compliance/3.4-communication-compliance/) · GitHub · Comunidad · Nuevo · judeper · FSI-CopilotGov (GitHub Pages) · 22 sep 2026. Control comunitario para servicios financieros que mapea FINRA 3110, FINRA 2210 y Reg BI a políticas de CC sobre comunicaciones asistidas por Copilot, con niveles base, recomendado y regulado e integración con IRM.

### Comunidad: blogs, libros, newsletters y eventos

- [FINRA and SEC Recordkeeping in Microsoft 365: An IT Guide](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/) · Blog · Comunidad · Nuevo · Michael Branson · i3solutions · 21 sep 2026. Distingue las reglas de conservación (FINRA 4511, SEC 17a-4) de la regla de revisión (FINRA 3110) y las mapea a retención de Purview y a Communication Compliance, incluido Teams.

**Manos a la obra**

1. `Laboratorio parcial` Crea una política desde «Detect financial regulatory compliance» con revisión del 10 % para cuentas de prueba de una mesa simulada y envía un mensaje sintético en inglés por cada riesgo. Limitación: el laboratorio no reproduce volumen ni la estructura de supervisores, y los clasificadores no detectan español ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)).
2. `Laboratorio` Complementa la plantilla con un diccionario en español de términos financieros locales (por ejemplo, «información privilegiada», «rendimiento garantizado» o «regalo») y valídalo con «Probar condiciones» ([condiciones en español](https://learn.microsoft.com/es-es/purview/communication-compliance-conditions-scenarios)).
3. `Laboratorio` Elabora una matriz que separe las obligaciones de conservación (retención y registros) de las de revisión (CC) para tu entidad, con el regulador local y la evidencia de cada una, y revísala con Cumplimiento ([oferta SEC 17a-4](https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs), [guía de un partner](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/)).
4. `Laboratorio` Diseña la arquitectura de supervisión de una mesa de negociación: CC con plantilla financiera y diccionario, IB entre Investigación y Ventas, conector de Bloomberg y retención; dibújala y anota licencias y aprobaciones ([guía archivada para banca y mercados de capitales](https://learn.microsoft.com/th-th/previous-versions/microsoft-365/solutions/financial-services-secure-collaboration)).
5. `Solo producción` Aplica la supervisión financiera sobre mesas de negociación reales. Por qué: requiere datos y usuarios reales, procedimientos de supervisión escritos y revisión por un principal registrado o el supervisor que designe tu regulador. Práctica segura: aprobación de Cumplimiento y Legal, población acotada, revisores seudonimizados, porcentaje de revisión bajo al inicio, pausa de la política como reversión y evidencia documentada de cada revisión ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies), [guía de un partner](https://i3solutions.com/answers/finra-sec-microsoft-365-recordkeeping-supervision/)).

<a id="reto-avanzado"></a>

## Reto del nivel

**Paquete de evidencia de supervisión.** Construye un paquete reproducible para una mesa de negociación simulada: política financiera con diccionario en español, diseño del conector de Bloomberg (con su plan de piloto en producción), flujo de Power Automate que avise a RR. HH., script con la API AuditLogQuery que exporte cada semana los eventos de CC e IB con hash de integridad y la matriz de conservación frente a revisión. Cierra explicando cómo responderías a un requerimiento del regulador en 48 horas.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué debes planificar para la evidencia de auditoría de Communication Compliance (por ejemplo, SupervisionRuleMatch)?
   - a) Nada: la lista de actividades del portal ya muestra estas operaciones
   - b) Migrar de Search-UnifiedAuditLog a la API AuditLogQuery antes del 15 de octubre de 2027
   - c) Exportar las coincidencias desde eDiscovery (Premium) en lugar de usar la auditoría
   - d) Activar Audit (Premium), que mantiene Search-UnifiedAuditLog después de 2027

2. ¿Qué tipo de registro de auditoría corresponde a Communication Compliance?
   - a) InformationBarrierPolicyApplication
   - b) ComplianceConnector
   - c) ComplianceSupervisionExchange
   - d) SharePointFileOperation

3. ¿Cuál es la retención por defecto del registro de auditoría con Audit (Standard)?
   - a) 90 días
   - b) 180 días
   - c) 1 año
   - d) 10 años

4. ¿Qué límites tiene la API AuditLogQuery según el aviso MC1505599?
   - a) Hasta 1 millón de registros por consulta, 200 búsquedas cada 24 horas y 50 en cola por tenant
   - b) Hasta 50.000 registros por consulta y 10 búsquedas simultáneas por usuario
   - c) Sin límites mientras exista una licencia de Audit (Premium)
   - d) Hasta 100.000 registros por consulta y 20 búsquedas cada 24 horas

5. ¿Qué requiere un conector de un partner, como 17a-4 o TeleMessage?
   - a) Nada adicional a la licencia E5 de los usuarios
   - b) Audit (Premium) y una licencia de Copilot para el administrador
   - c) Un servidor local de Veritas como intermediario
   - d) Una entidad de servicio aprovisionada y una relación comercial con el partner

6. ¿Cómo mapea usuarios el conector de Instant Bloomberg?
   - a) Por CorporateEmailAddress o con un archivo CSV
   - b) Por el número de teléfono registrado en Bloomberg
   - c) Por la dirección IP del terminal de Bloomberg
   - d) No mapea usuarios: importa todo a un buzón común

7. ¿Qué ocurrió con los conectores de Veritas?
   - a) Siguen disponibles
   - b) Pasaron a vista previa
   - c) Se retiraron el 30 de junio de 2024
   - d) Se integraron a Information Barriers

8. ¿Qué dice la documentación sobre PowerShell para las políticas de Communication Compliance?
   - a) Es la vía recomendada y la única que admite plantillas
   - b) La página de políticas dice que no es compatible, aunque los cmdlets SupervisoryReviewPolicyV2 siguen documentados
   - c) Solo funciona en las nubes GCC y GCC High
   - d) Es obligatorio para crear la plantilla financiera

9. ¿Qué licencia necesita la plantilla de Power Automate «Notify manager when a user has a Communication Compliance alert»?
   - a) Power Automate Premium para cada revisor que reciba avisos
   - b) Una licencia de Copilot Studio para el flujo
   - c) No requiere licencias adicionales de Power Automate; las funciones premium sí pueden requerirlas
   - d) Pago por uso de Purview por cada ejecución del flujo

10. ¿Qué afirmación sobre la plantilla de cumplimiento normativo financiero es correcta?
   - a) Usa seis clasificadores que funcionan en español y portugués
   - b) Revisa el 100 % de los mensajes y no admite conectores
   - c) Usa seis clasificadores solo en inglés y una revisión del 10 %
   - d) Bloquea los mensajes antes de enviarse si detecta manipulación

11. Según una guía de un partner sobre FINRA 3110, ¿qué papel cumple Communication Compliance?
   - a) Reemplaza los procedimientos de supervisión escritos si la política está documentada
   - b) Cubre la conservación WORM que exigen SEC 17a-4 y FINRA 4511
   - c) Elimina la necesidad de un principal registrado gracias a los clasificadores
   - d) Apoya la revisión, pero no reemplaza los procedimientos escritos ni la revisión por un principal registrado

12. ¿Qué capacidad de Purview cubre la conservación exigida por SEC 17a-4, FINRA 4511 y CFTC 1.31?
   - a) La retención y la gestión de registros, según la evaluación de Cohasset
   - b) Communication Compliance, que conserva las coincidencias hasta 7 años
   - c) Information Barriers, que congela los chats entre segmentos
   - d) Power Automate, que copia los mensajes a un repositorio WORM

13. ¿Qué clasificador financiero genera ruido con boletines y se beneficia de Filter email blasts?
   - a) Customer complaints
   - b) Money laundering
   - c) Gifts & entertainment
   - d) Regulatory collusion

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

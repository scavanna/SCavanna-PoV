# Programa: cómo usar, justificación, rutas y plan

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[Índice del programa](README.md) · [Nivel 1 · Inicial →](01_Nivel_1_Inicial.md)

<a id="como-usar"></a>

## Cómo usar esta guía

¿Quieres convertirte en Ninja de eDiscovery y Audit? Esta guía reúne, ordenados como un curso, los mejores recursos públicos para preservar, encontrar, revisar y producir información de Microsoft 365 con criterio legal y técnico, y para reconstruir con el registro de auditoría quién hizo qué, cuándo y desde dónde. Documentación de Microsoft Learn, avisos del Message Center, webinars de la Microsoft Security Community, el Ninja oficial de eDiscovery y el trabajo de MVPs y empleados de Microsoft, todo verificado al 6 de noviembre de 2026.

Está pensada para quienes operan estas capacidades por razones distintas: Legal y litigios, investigaciones internas, cumplimiento y registros, auditoría interna, privacidad y el SOC, que usa la auditoría como fuente de investigación. Puedes seguirla completa o por tu rol. Cada nivel cierra con una evaluación y un reto; con 80 % o más generas tu certificado de finalización, como en el Ninja original. Y como la evidencia ya no es solo correo y documentos, el recorrido llega a Copilot, los agentes, Data Security Investigations y Security Copilot.

**Estructura.** Tres niveles técnicos —Inicial (L100–L200), Intermedio (L300) y Avanzado (L400)—, un track de operación (L300–L400) para el modelo operativo, las métricas y el gobierno, y una sección transversal de comunidad. El orden sigue la vida de un asunto: preparar la plataforma, buscar, preservar, revisar, producir, investigar y operar.

**Cada módulo** sigue la forma Ninja: una introducción con el porqué, la justificación de negocio (*Por qué importa*), lo que vas a lograr, novedades y advertencias con fecha y fuente, una ruta rápida (*¿Tienes poco tiempo?*), los recursos agrupados por tipo, la práctica guiada (*Manos a la obra*) y lecturas para profundizar.

**Evaluación y certificado.** Cada nivel técnico y el track de operación cierran con una evaluación de opción múltiple, con la explicación y la fuente de cada respuesta, y un reto integrador. Con 80 % o más puedes generar el certificado de finalización. Es una autoevaluación de esta guía, no una certificación de Microsoft: para eso están el examen SC-401, la credencial Applied Skills de retención, eDiscovery y Communication Compliance, y el knowledge check del Ninja oficial.

**Laboratorio.** Cada ejercicio indica dónde se puede hacer: `[LAB]` completo en una prueba de Microsoft 365 E5 con una suscripción de Azure; `[LAB-PARCIAL]` con las limitaciones que se explican; `[SOLO-PRODUCCION]` cuando hacen falta licencias pagas, volumen o datos reales, con la forma segura de practicar. En eDiscovery, «seguro» incluye acordar con Legal, RR. HH. y privacidad antes de tocar datos de personas reales.

**Fechas y estados.** Cada dato tiene fuente y fecha. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa; la documentación en español suele actualizarse después que la versión en inglés. Ante una diferencia, manda la documentación oficial en inglés vigente. Esta guía no interpreta leyes: en temas regulatorios y laborales remite a fuentes oficiales y a tus áreas de Legal y privacidad.

**Leyenda de etiquetas**

| Etiqueta | Significado |
|---|---|
| Microsoft oficial | Documentación, blogs y videos publicados por Microsoft. |
| Empleado de Microsoft | Material de ingenieros, gerentes de producto o arquitectos de Microsoft en canales propios o comunitarios. |
| MVP de Microsoft | Material de Most Valuable Professionals, con estado verificado en fuentes públicas. |
| Comunidad o partner | Autores de la comunidad o de partners; útil, pero contrástalo con la documentación oficial. |
| Vista previa | Funcionalidad en preview: puede cambiar y no siempre tiene soporte de producción. |
| Legado aún útil | Recurso anterior a los cambios de 2025–2026 que sigue explicando bien el concepto; lee la nota de qué cambió. |
| Ninja original | Recurso que formaba parte del Ninja oficial del producto. |
| Nuevo | Recurso publicado o actualizado desde mayo de 2026. |
| ES | Recurso disponible en español. |
| Laboratorio | Ejercicio que puedes hacer completo en el entorno de práctica (prueba de Microsoft 365 E5 o sandbox y suscripción de Azure). |
| Laboratorio parcial | Ejercicio posible en el entorno de práctica con limitaciones que se indican. |
| Solo producción | Requiere licencias pagas, datos o usuarios reales, o varios inquilinos: síguelo con la estrategia de práctica segura en producción. |

<a id="por-que"></a>

## Por qué este programa

**Por qué ahora.** eDiscovery y Audit cambiaron más entre 2024 y 2026 que en la década anterior: Microsoft retiró el eDiscovery clásico (Content Search, Standard y Premium) el 31 de agosto de 2025, limitó las búsquedas de contenido a buscar y exportar y fijó en 14 días la vida de sus exportaciones desde el 16 de febrero de 2026, publicó la API AuditLogQuery en disponibilidad general (octubre de 2026) y anunció el retiro de `Search-UnifiedAuditLog` para el 15 de octubre de 2027. Además, los prompts de Copilot, las acciones de los agentes y las interacciones con apps de IA de terceros ya son evidencia. Un equipo formado con material de 2021 a 2023 busca menús que no existen, pierde exportaciones vencidas y mantiene scripts que dejarán de funcionar.

**Qué gana la organización.** Resultados medibles: tiempo desde la solicitud de Legal hasta el hold efectivo, porcentaje de custodios preservados en 24 horas, exportaciones descargadas y conciliadas dentro de la ventana de 14 días, tiempo para responder «¿qué mensajes leyó el atacante?», cobertura de la retención de auditoría frente a la política interna y cero accesos sin justificar a casos. Cada nivel deja entregables reutilizables: plantillas de caso, consultas KeyQL documentadas, un formulario de cadena de custodia, scripts sobre Microsoft Graph, un registro de decisiones de privacidad y un procedimiento con RACI.

**Para quién.** Gestores de eDiscovery y asesoría legal, investigadores internos, equipos de registros y cumplimiento, auditoría interna, analistas del SOC y oficiales de privacidad. Cada equipo opera la capacidad por una razón distinta —litigio, investigación laboral, requerimiento regulatorio, auditoría o incidente— y las rutas por rol permiten recorrer solo lo necesario, con un tronco común en el nivel inicial.

**Cómo se conecta con el resto de la serie.** Es uno de los ocho programas de Purview, porque cada capacidad la operan equipos distintos por razones distintas. Las retenciones de Purview se profundizan en el programa de ciclo de vida de los datos y registros; los casos que se escalan desde riesgo interno y cumplimiento de comunicaciones nacen en sus propios programas; las etiquetas y el cifrado que eDiscovery debe descifrar se ven en Information Protection, y la seguridad de datos para IA en DSPM. Del lado del SOC, la auditoría alimenta a **Sentinel** y **Defender XDR**; **Entra** aporta las identidades y PIM para los roles privilegiados; y **Security Copilot** asiste dentro de eDiscovery y de Data Security Investigations.

<a id="licencias"></a>

## Licencias: qué incluye cada plan

Purview combina licencias por usuario y pago por uso facturado en Azure, que exige asociar el tenant a una suscripción activa ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)). Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama **Microsoft Purview Suite**, sin cambio funcional; se agrega a Microsoft 365 E3 (u Office 365 E3 con EMS E3) y Microsoft 365 E5 ya lo incluye ([cambio de nombre](https://samexpert.com/microsoft-365-defender-purview-renames/), [precios](https://www.microsoft.com/en-us/security/microsoft-purview-pricing)). La fuente de verdad para asignar licencias es la [descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

Dos reglas prácticas: en eDiscovery, la licencia premium la necesita el **custodio** cuyos datos se analizan, no quien busca o revisa; en Audit, la retención depende de la licencia del **usuario** que generó el registro y de las políticas que lo alcanzan.

**Licencias de eDiscovery y Audit (noviembre de 2026)**

| Capacidad | Microsoft 365 E3 | Microsoft 365 E5 / E5 Compliance (Purview Suite) | Complemento o pago por uso | Fuente |
|---|---|---|---|---|
| Audit (Standard): habilitado por defecto, búsqueda en portal, PowerShell y API, 180 días de retención | Incluido | Incluido | — | [Learn: auditing solutions](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) |
| Eventos de investigación: MailItemsAccessed, envíos y SearchQueryInitiated | Incluido en Audit (Standard); SearchQueryInitiated de Exchange se habilita por buzón | Incluido; Premium agrega propiedades como SensitivityLabel en MailItemsAccessed | — | [Learn: MailItemsAccessed](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) |
| Audit (Premium): un año por defecto para Exchange, SharePoint, OneDrive y Entra ID, y hasta 50 políticas personalizadas | No (180 días) | Incluido | E1 o E3 con Purview Suite o con el complemento «eDiscovery and Audit» | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Retención de auditoría de 10 años | No | Requiere complemento | Complemento de retención de registros de auditoría de 10 años | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Ancho de banda de la Management Activity API | Base de 2.000 solicitudes por minuto por tenant, que crece con los asientos | Aproximadamente el doble | — | [Learn: auditing solutions](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) |
| Auditoría de Copilot, agentes y apps de IA de Microsoft (Security Copilot, Copilot en Fabric, Copilot Studio, Microsoft Foundry) | Incluida en Audit (Standard) | Incluida | Apps de IA no Microsoft (AIAppInteraction): pago por uso, 180 días | [Learn: audit logs for Copilot and AI](https://learn.microsoft.com/en-us/purview/audit-copilot) |
| eDiscovery estándar: casos, búsquedas, estadísticas, holds de caso y exportación | Incluido | Incluido | F1 y F3 no incluyen derechos para ser objeto de hold | [Learn: create holds](https://learn.microsoft.com/en-us/purview/edisc-hold-create) |
| Holds por consulta, por rango de fechas o por custodio | No | Incluido | Purview Suite o «eDiscovery and Audit» | [Learn: create holds](https://learn.microsoft.com/en-us/purview/edisc-hold-create) |
| Funciones premium: review sets, analítica, OCR, importación de datos externos, Security Copilot y Graph solo aplicación | No | Incluido para custodios con E5 | E1 o E3 con Purview Suite o «eDiscovery and Audit» por custodio; quien busca y revisa no necesita E5 | [Learn: eDiscovery permissions](https://learn.microsoft.com/en-us/purview/edisc-permissions) |
| Escala de eDiscovery | Estándar: 10.000 casos, 1.000 buzones por hold de caso, 2 TB por búsqueda y por día | Premium: 50.000 casos, 2.000 buzones por hold de caso, 5 TB por búsqueda y por día | — | [Learn: eDiscovery limits](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) |
| Quién exporta resultados de búsqueda | Necesita E3 o E5 (y la licencia de SharePoint del nivel E3 para contenido de SharePoint) | Incluido | — | [Learn: export search results](https://learn.microsoft.com/en-us/purview/edisc-search-export) |
| API de eDiscovery de Microsoft Graph | Delegada: casos, búsquedas y holds; exportar requiere pago por uso | Además: review sets, analítica y autenticación solo aplicación | Pago por uso para exportar con E3 | [Learn: eDiscovery API](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) |
| Security Copilot en eDiscovery (KeyQL desde lenguaje natural, resúmenes) | No (función premium) | Con la inclusión de Security Copilot: 400 SCU al mes por cada 1.000 licencias pagadas, hasta 10.000 | Capacidad aprovisionada o uso excedente en SCU | [Learn: Security Copilot inclusion](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) |
| Data Security Investigations | No incluido | No incluido: no requiere licencia dedicada | Pago por uso: almacenamiento (GB al mes) y unidades de cómputo; suscripción de Azure en el mismo tenant | [Learn: DSI billing](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) |
| Escalamiento a eDiscovery desde Insider Risk Management y Communication Compliance | No (requiere esas soluciones) | Incluido | Purview Suite o complementos de esas soluciones | [Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |
| Interacciones de Microsoft 365 Copilot como evidencia (búsqueda, retención y auditoría) | Requiere licencias de Microsoft 365 Copilot (complemento) | Requiere licencias de Microsoft 365 Copilot (complemento) | Microsoft 365 E7 incluye Microsoft 365 Copilot (disponible en general desde el 1 de mayo de 2026) | [Tech Community: E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) |
| Purview para agentes gestionados con Agent 365 (auditoría y eDiscovery, DSPM con observabilidad de IA, DLP e Insider Risk Management) | No | No incluido para esos agentes | Microsoft 365 E7 (E5 + Microsoft 365 Copilot + Agent 365 + Entra Suite) o Agent 365 como complemento | [Agent 365 service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365) |
| Prueba para practicar | Prueba de Purview Suite: 25 licencias durante 90 días | Prueba de Microsoft 365 E5: 25 licencias durante un mes | — | [Learn: Purview Suite trial](https://learn.microsoft.com/en-us/purview/purview-trial) |

Verifica siempre la [descripción del servicio de Purview](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) y la [guía de licenciamiento](https://www.microsoft.com/licensing/guidance/Microsoft-Purview) antes de comprar o asignar: los planes A5, G5 y F5 tienen matices propios.

<a id="cambios-retiros"></a>

## Cambios y retiros 2024–2027

Cronología de los cambios con impacto en procedimientos, scripts y licencias, incluidos dos antecedentes de 2023 que todavía explican diferencias entre documentos. La última columna remite al módulo donde se trata cada cambio; la tabla [Qué cambió](#cambios) resume el antes y el después.

**Cambios y retiros de eDiscovery y Audit (estado al 6 de noviembre de 2026)**

| Fecha | Cambio | Estado al 6 de noviembre de 2026 | Fuente | Módulo |
|---|---|---|---|---|
| 2023-10-17 (antecedente) | Audit (Standard): la retención pasa de 90 a 180 días | Vigente | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) | [I2](01_Nivel_1_Inicial.md#i2) |
| 2023-11-30 (antecedente) | Retiro de la búsqueda clásica de auditoría | Retirado | [Learn: auditing solutions](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) | [I2](01_Nivel_1_Inicial.md#i2) |
| 2024-07 | Disponibilidad general del portal de Microsoft Purview | Vigente | [MC807798](https://mc.merill.net/message/MC807798) | [P0](01_Nivel_1_Inicial.md#p0) |
| 2024-08-12 | Vista previa de la experiencia unificada de eDiscovery | Disponible en general; única experiencia | [Tech Community: anuncio](https://techcommunity.microsoft.com/blog/microsoft-security-blog/ediscovery-launches-a-modern-intuitive-user-experience/4215184) | [I1](01_Nivel_1_Inicial.md#i1) |
| 2024-11-14 a 2024-12-14 | Retiro del portal clásico de cumplimiento | Retirado | [MC939918](https://mc.merill.net/message/MC939918) | [P0](01_Nivel_1_Inicial.md#p0) |
| 2025-01-15 | La CISA publica el Microsoft Expanded Cloud Logs Implementation Playbook | Vigente | [CISA](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook) | [M3](02_Nivel_2_Intermedio.md#m3) |
| 2025-02-11 | MC1002399 anuncia el retiro del eDiscovery clásico entre el 1 de agosto y el 1 de septiembre de 2025 | Ejecutado | [MC1002399](https://mc.merill.net/message/MC1002399) | [I1](01_Nivel_1_Inicial.md#i1) |
| 2025-05-26 | Retiro de Content Search clásica, casos clásicos Standard y parámetros de exportación de PowerShell | Retirado | [MC1055528](https://mc.merill.net/message/MC1055528) | [I1](01_Nivel_1_Inicial.md#i1), [M4](02_Nivel_2_Intermedio.md#m4) |
| 2025-08-31 | Retiro de todas las experiencias clásicas de eDiscovery (salvo 21Vianet) | Retirado | [Learn: legacy solutions](https://learn.microsoft.com/en-us/purview/ediscovery) | [I1](01_Nivel_1_Inicial.md#i1) |
| 2025-10-01 | Microsoft 365 E5 Compliance pasa a llamarse Microsoft Purview Suite | Vigente | [SAMexpert](https://samexpert.com/microsoft-365-defender-purview-renames/) | [P0](01_Nivel_1_Inicial.md#p0) |
| 2025-11-18 | Security Copilot incluido en Microsoft 365 E5 y E7: 400 SCU al mes por cada 1.000 licencias pagadas | Despliegue por fases | [Learn: Security Copilot inclusion](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) | [A4](03_Nivel_3_Avanzado.md#a4) |
| 2026-01 (fin de mes) | Data Security Investigations en disponibilidad general, con pago por uso | GA | [Tech Community: AMA](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393) | [A4](03_Nivel_3_Avanzado.md#a4) |
| 2026-02-16 | Las exportaciones de búsquedas expiran a los 14 días | Vigente | [MC1217141](https://mc.merill.net/message/MC1217141) | [M4](02_Nivel_2_Intermedio.md#m4) |
| 2026-02-16 | Content searches limitadas a buscar y exportar (MC1216266) | Vigente | [Office 365 for IT Pros](https://office365itpros.com/2026/01/15/content-searches-change/) | [I1](01_Nivel_1_Inicial.md#i1), [M4](02_Nivel_2_Intermedio.md#m4) |
| 2026-05-01 | Disponibilidad general de Microsoft 365 E7 y Agent 365; Purview para agentes de Agent 365 requiere E7 o Agent 365 | GA | [Tech Community](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) | [A1](03_Nivel_3_Avanzado.md#a1) |
| 2026-06 | DSI: insights proactivas en DSPM | GA | [MC1317196](https://mc.merill.net/message/MC1317196) | [A4](03_Nivel_3_Avanzado.md#a4) |
| 2026-07 | DSI: reconocimiento óptico de caracteres (OCR) | GA (vista previa desde mayo) | [Roadmap 561489](https://www.microsoft.com/releasecommunications/api/v2/m365/561489) | [A4](03_Nivel_3_Avanzado.md#a4) |
| 2026-07 | Fecha de expiración en asignaciones de roles de Purview (salvo eDiscovery Administrator y Manager); Priority Cleanup exige tres aprobaciones | Vigente | [Learn: What’s new in Purview](https://learn.microsoft.com/en-us/purview/whats-new) | [O1](04_Nivel_4_Operacion.md#o1), [A1](03_Nivel_3_Avanzado.md#a1) |
| 2026-08 | Sin soporte de autenticación solo aplicación en cmdlets de eDiscovery de Security & Compliance PowerShell | Vigente | [Learn: What’s new in Purview](https://learn.microsoft.com/en-us/purview/whats-new) | [A2](03_Nivel_3_Avanzado.md#a2) |
| 2026-08 | Priority Cleanup puede borrar contenido que deja de ser descubrible; Claude Enterprise llega a eDiscovery | Vista previa | [Learn: What’s new in Purview](https://learn.microsoft.com/en-us/purview/whats-new) | [A1](03_Nivel_3_Avanzado.md#a1) |
| 2026-09-01 | Publicación de EDRM 2.0 | Vigente | [EDRM](https://edrm.net/edrm-model/current/) | [O1](04_Nivel_4_Operacion.md#o1) |
| 2026-09-24 | eDiscovery sobre contenedores de SharePoint Embedded (Loop, Copilot Pages y Copilot Notebooks) | Anunciado; Learn lo marca en vista previa | [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) | [A1](03_Nivel_3_Avanzado.md#a1) |
| 2026-09 a 2026-10 | Nuevas operaciones de auditoría de RBAC de Purview | GA | [MC1473155](https://mc.merill.net/message/MC1473155) | [O2](04_Nivel_4_Operacion.md#o2) |
| 2026-10 | API AuditLogQuery de Microsoft Graph en disponibilidad general | GA | [MC1505599](https://mc.merill.net/message/MC1505599) | [A2](03_Nivel_3_Avanzado.md#a2) |
| 2026-10-28 | Actualización de las habilidades medidas del examen SC-401 | Vigente | [Learn: SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) | [I0](01_Nivel_1_Inicial.md#i0) |
| 2026-12-01 | Entra en vigencia la Ley 21.719 de protección de datos personales de Chile | Próximo | [BCN](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) | [O3](04_Nivel_4_Operacion.md#o3) |
| 2027-10-15 | Retiro de Search-UnifiedAuditLog | Planificado | [MC1505599](https://mc.merill.net/message/MC1505599) | [A2](03_Nivel_3_Avanzado.md#a2) |

Fuente principal: sección de cambios y retiros de la investigación de este programa, ampliada con avisos del Message Center y de la página [What’s new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new).

<a id="roles-permisos"></a>

## Roles y permisos de eDiscovery y Audit

Separa funciones: quien autoriza un asunto (Legal) no debería ser quien exporta, y quien administra la auditoría no debería poder borrar evidencia. Mantén mínimo el grupo eDiscovery Administrator, porque accede a todos los casos ([permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions)). Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten fecha de expiración, **salvo** eDiscovery Administrator y eDiscovery Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)): para esos roles usa PIM para grupos y revisiones de acceso ([permisos del portal](https://learn.microsoft.com/en-us/purview/purview-permissions)).

Vigila los cambios: desde septiembre y octubre de 2026 el portal registra nuevas operaciones de auditoría de RBAC ([MC1473155](https://mc.merill.net/message/MC1473155)) y todas las actividades de eDiscovery quedan en Audit con la IP del cliente ([actividades de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)). La tabla completa de grupos de roles predeterminados está en [roles y grupos de roles](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions).

**Roles y permisos de eDiscovery y Audit**

| Grupo de roles o rol | Qué permite | Quién debería tenerlo | Riesgo | Fuente |
|---|---|---|---|---|
| eDiscovery Manager (subgrupo) | Crear casos y trabajar en los casos donde es miembro: búsquedas, holds, review sets y exportaciones | Gestores de eDiscovery, Legal e investigadores designados; admite usuarios y grupos de seguridad habilitados para correo | Acceso a contenido sensible y a exportaciones; la asignación no admite fecha de expiración | [Learn: eDiscovery permissions](https://learn.microsoft.com/en-us/purview/edisc-permissions) |
| eDiscovery Administrator (subgrupo) | Ver y acceder a todos los casos, configurar la solución y quitar miembros de los casos | Dos o tres personas del liderazgo de eDiscovery; solo usuarios individuales | Muy alto: acceso a todos los asuntos; mantenlo mínimo, con PIM y monitoreo | [Learn: eDiscovery permissions](https://learn.microsoft.com/en-us/purview/edisc-permissions) |
| Reviewer (rol Review) | Revisar, etiquetar y anotar en review sets de los casos donde fue agregado, sin crear casos ni búsquedas | Abogados y revisores internos o externos | Exposición al contenido de un asunto; limítalo por caso y por tiempo | [Learn: roles and role groups](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions) |
| RMS Decrypt | Descifrar contenido protegido al agregarlo a review sets o exportarlo | Solo quienes deban procesar contenido cifrado de un asunto | Contenido cifrado en claro fuera de su protección original | [Learn: add to review set](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) |
| Search And Purge | Eliminar en bloque contenido que coincide con una búsqueda, incluidos prompts y respuestas de IA (hasta 10 ítems por buzón por vez) | Uno o dos operadores, con asignación justo a tiempo y aprobación de Legal | Destrucción de evidencia o de datos bajo obligación de preservación | [Learn: AI data in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) |
| Audit Manager (rol Audit Logs) | Buscar en la auditoría y administrar su configuración | Responsable de la plataforma de auditoría | Desactivar o alterar la auditoría; alerta ante cambios de configuración | [Learn: get started with auditing](https://learn.microsoft.com/en-us/purview/audit-get-started) |
| Audit Reader (rol View-Only Audit Logs) | Buscar y exportar registros de auditoría sin cambiar la configuración | SOC, auditoría interna e investigadores | Visibilidad de la actividad de todas las personas: es tratamiento de datos personales | [Learn: search the audit log](https://learn.microsoft.com/en-us/purview/audit-search) |
| Organization Configuration | Crear y modificar políticas de retención de auditoría (hasta 50; los cambios no son retroactivos) | Administración de cumplimiento | Reducir la retención por error; un cambio no recupera registros vencidos | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Límites de cumplimiento y unidades administrativas | Restringir qué contenido puede buscar cada grupo (país, subsidiaria) en eDiscovery y DSI | Configurados por eDiscovery Administrator con aprobación de Legal | Filtros mal definidos: sobreacceso o búsquedas incompletas | [Learn: compliance boundaries](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) |
| Grupos de roles de Insider Risk Management y Communication Compliance | Escalar casos o alertas a una investigación de eDiscovery | Investigadores de esas soluciones; el caso escalado se trabaja con roles de eDiscovery | Pasar de una señal de riesgo a evidencia sin el control de Legal y RR. HH. | [Learn: IRM permissions](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) |
| Roles de Data Security Investigations | Crear investigaciones, agregar datos y analizarlos con IA | Equipo de investigaciones de seguridad de datos, con separación entre quien crea y quien revisa | Costo por uso y procesamiento con IA de contenido sensible | [Learn: get started with DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-get-started) |
| Security Copilot (owner y contributor) | Usar Security Copilot, que actúa en nombre del usuario y nunca excede sus permisos de Purview | Usuarios de eDiscovery e investigación habilitados | Consumo de SCU; los roles de Security Copilot no son roles de Entra | [Learn: Security Copilot authentication](https://learn.microsoft.com/en-us/copilot/security/authentication) |

Antes de asignar, compara con la tabla oficial de [roles y grupos de roles](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions) y con los [permisos del portal de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions); los nombres de roles pueden cambiar.

<a id="retencion-auditoria"></a>

## Retención de auditoría

La retención la deciden la licencia del usuario que generó el registro y las políticas que lo alcanzan. Audit (Standard) retiene 180 días desde el 17 de octubre de 2023 (antes, 90). Audit (Premium) agrega una política predeterminada de un año para Exchange, SharePoint, OneDrive y Entra ID, hasta 50 políticas personalizadas con el rol Organization Configuration y la opción de 10 años con el complemento ([políticas de retención de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)).

Para investigaciones, la regla es simple: si tu política interna o tu regulador exige más de 180 días, configura Premium o envía la auditoría a un SIEM **antes** del incidente, porque una política nueva no recupera registros vencidos.

**Retención de auditoría por actividad o carga (noviembre de 2026)**

| Actividad o carga | Audit (Standard) | Audit (Premium) | Complemento de 10 años | Fuente |
|---|---|---|---|---|
| Exchange, SharePoint, OneDrive y Entra ID de usuarios con licencia Premium | 180 días | Un año por defecto (política predeterminada) | Hasta 10 años con política personalizada y complemento | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Otras cargas y tipos de registro de usuarios con licencia Premium (por ejemplo, Teams o Copilot) | 180 días | 180 días, salvo política personalizada | Hasta 10 años con política personalizada y complemento | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Usuarios sin licencia Premium | 180 días | No aplica: la retención extendida depende de la licencia del usuario | No aplica | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Entidades no usuario (service principals, sistema y apps) | Un año fijo | Un año fijo; no admite políticas personalizadas | No aplica | [Learn: auditing solutions](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) |
| Interacciones con apps de IA no Microsoft (AIAppInteraction) | 180 días, con pago por uso | 180 días, con pago por uso | No documentado | [Learn: audit logs for Copilot and AI](https://learn.microsoft.com/en-us/purview/audit-copilot) |
| Security Copilot (eventos de administración y metadatos de actividad) | 180 días por defecto | Ampliable con política personalizada | Con política personalizada y complemento | [Learn: Security Copilot audit log](https://learn.microsoft.com/en-us/copilot/security/audit-log) |
| Registros generados antes del 17 de octubre de 2023 | 90 días (antecedente; ya vencidos) | — | — | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Trabajos de búsqueda en el portal de auditoría | Se conservan 30 días; hasta 10 simultáneos por usuario | Igual | No aplica | [Learn: search the audit log](https://learn.microsoft.com/en-us/purview/audit-search) |
| Cambios en políticas de retención de auditoría | No aplica | No son retroactivos; máximo de 50 políticas | Igual | [Learn: audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |

Las filas de entidades no usuario y de Security Copilot tienen puntos por confirmar: revisa la sección de limitaciones al final de la guía.

<a id="formato"></a>

## El formato Ninja: historia y familia

El Ninja de eDiscovery nació como **Become a Microsoft 365 Advanced eDiscovery Ninja**, anunciado en Tech Community el 4 de octubre de 2021 ([anuncio](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog-post--become-a-microsoft-365-advanced-ediscovery-ninja/2810216)). Seguía las etapas del Electronic Discovery Reference Model (EDRM) en ocho secciones —Overview, Getting Started, Identification, Preservation, Collection & Processing, Review & Analysis, Production y Advanced— con un knowledge check al terminar cada nivel. Como el resto de la familia de cumplimiento, entregaba un certificado de participación por medio de un portal de atestación, en tres a cinco días hábiles y con la aclaración de que no era una certificación oficial ([ejemplo del mecanismo](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322)).

El producto cambió de nombre dos veces —Advanced eDiscovery, luego eDiscovery (Premium) y hoy funciones premium dentro del eDiscovery unificado— y el Ninja lo acompañó. La versión vigente, **Become a Microsoft Purview eDiscovery Ninja** ([post](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108)), de Stefanie Bier, muestra el 5 de mayo de 2026 como última actualización y unas 226.000 vistas en el [índice de Ninja Training](https://techcommunity.microsoft.com/tag/ninja%20training). Según su descripción pública, cubre la experiencia unificada, permisos, retenciones, búsqueda en Microsoft 365 (incluidos Teams y Copilot), conjuntos de revisión, analítica, exportaciones, guías interactivas y la transición del clásico al moderno ([índice comunitario](https://mscloudexplorers.com/learn/)). Para Audit no existe un Ninja oficial: lo más cercano es la ruta de Learn [Audit and search activity in Microsoft Purview](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/), alineada con SC-401.

Esta edición respeta la forma Ninja —módulos con introducción, recursos curados, práctica y evaluación— y agrega lo que el original no tenía: Audit como mitad del programa, la evidencia de Copilot y agentes, Data Security Investigations, la integración con el SOC y un track de operación. También actualiza el marco de referencia: EDRM 2.0, publicado el 1 de septiembre de 2026, agrupa identificación, preservación, recolección y procesamiento en «Data Acquisition», agrega la disposición y se apoya en el modelo de gobierno de la información (IGRM) ([EDRM 2.0](https://edrm.net/edrm-model/current/)). La familia de Purview, además, migra hacia rutas de Learn con insignia, como los [escenarios Ninja de Information Protection y DLP](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/).

**La familia Ninja relacionada**

| Ninja | Qué cubre | Estado y última actualización |
|---|---|---|
| [Become a Microsoft Purview eDiscovery Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108) | eDiscovery unificado de fundamentos a flujos avanzados: permisos, holds, búsqueda (incluidos Teams y Copilot), review sets, analítica y exportación | Vigente; 5 de mayo de 2026 en el índice de Tech Community |
| [Advanced eDiscovery Ninja (anuncio de 2021)](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog-post--become-a-microsoft-365-advanced-ediscovery-ninja/2810216) | Ocho secciones alineadas al EDRM, con knowledge check por nivel | Histórico (4 de octubre de 2021); útil para entender el formato original |
| [Audit and search activity in Microsoft Purview (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) | Ruta de Learn de 1 h 31 min: investigaciones con Audit (incluidos Copilot e IA) y búsqueda con eDiscovery | Vigente; no existe un «Audit Ninja» oficial |
| [Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283) | Políticas, revisión, integraciones y escalamiento de comunicaciones | Legado aún útil (abril de 2022) |
| [Become an Insider Risk Management Ninja](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/become-an-insider-risk-management-ninja/ba-p/3282306) | Riesgo interno: licencias, permisos, analíticas, políticas y casos | Legado aún útil (abril de 2022, con actualizaciones posteriores) |
| [Data Lifecycle and Records Management Ninja (anuncio)](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--become-a-microsoft-purview-data-lifecycle-and-records-management-ninja/3883998) | Retención, etiquetas, plan de archivos y disposición | Legado aún útil (julio de 2023) |
| [Compliance Manager Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) | Evaluaciones y acciones de mejora; documenta el certificado por portal de atestación | Legado aún útil (edición Q1 2023) |
| [Become a Microsoft Priva Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888) | Privacidad y solicitudes de derechos de los titulares | Legado aún útil (julio de 2023) |
| [Escenarios Ninja de Purview en Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) | Information Protection y DLP en cinco escenarios, con insignia | Vigente; formato hacia el que migra la familia (el Ninja de MIP se retiró de Tech Community en julio de 2025) |

**Del Ninja oficial a esta edición**

| Ninja oficial | Contenido | En esta edición |
|---|---|---|
| eDiscovery Ninja 2026 · Fundamentos y transición | Experiencia unificada, del clásico al moderno, licencias | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| eDiscovery Ninja 2026 · Permisos | eDiscovery Manager, eDiscovery Administrator y roles | [I1](01_Nivel_1_Inicial.md#i1), [O1](04_Nivel_4_Operacion.md#o1) |
| eDiscovery Ninja 2026 · Retenciones | Holds de caso, por consulta y por fechas | [M1](02_Nivel_2_Intermedio.md#m1) |
| eDiscovery Ninja 2026 · Búsqueda y recolección | Orígenes de datos, condiciones, KeyQL, estadísticas; Teams y Copilot | [I3](01_Nivel_1_Inicial.md#i3), [A1](03_Nivel_3_Avanzado.md#a1) |
| eDiscovery Ninja 2026 · Review sets y analítica | Revisión, etiquetado, casi duplicados, hilos y temas | [M2](02_Nivel_2_Intermedio.md#m2) |
| eDiscovery Ninja 2026 · Exportaciones | Exportación de búsquedas y de review sets | [M4](02_Nivel_2_Intermedio.md#m4) |
| eDiscovery Ninja 2026 · Guías interactivas | Recorridos guiados del portal | [I0](01_Nivel_1_Inicial.md#i0) |
| Advanced eDiscovery Ninja 2021 · Overview y Getting Started | Licencias, permisos y configuración inicial | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| Advanced eDiscovery Ninja 2021 · Identification y Preservation | Custodios, orígenes de datos y holds | [M1](02_Nivel_2_Intermedio.md#m1) |
| Advanced eDiscovery Ninja 2021 · Collection & Processing | Colecciones (hoy estadísticas) e indexación avanzada | [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2) |
| Advanced eDiscovery Ninja 2021 · Review & Analysis | Review sets, analítica y codificación predictiva | [M2](02_Nivel_2_Intermedio.md#m2) |
| Advanced eDiscovery Ninja 2021 · Production | Exportación y redacción | [M4](02_Nivel_2_Intermedio.md#m4) |
| Advanced eDiscovery Ninja 2021 · Advanced | Escenarios avanzados; en esta edición, automatización y API | [A2](03_Nivel_3_Avanzado.md#a2) |
| Ruta SC-401 «Audit and search activity» · módulo de Audit | Configuración, búsqueda, Copilot e IA, MailItemsAccessed | [I2](01_Nivel_1_Inicial.md#i2), [M3](02_Nivel_2_Intermedio.md#m3), [A1](03_Nivel_3_Avanzado.md#a1) |
| Ruta SC-401 «Audit and search activity» · módulo de eDiscovery | Búsqueda de contenido con eDiscovery | [I3](01_Nivel_1_Inicial.md#i3) |
| Nuevo en esta edición | AuditLogQuery, respuesta a incidentes y SOC, Data Security Investigations, Security Copilot, operación y gobierno en MCSA, comunidad | [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3), [C1](05_Comunidad.md#c1), [C2](05_Comunidad.md#c2) |

**Recursos sobre el Ninja oficial y su familia**

- [Tag:"ninja training" | Microsoft Community Hub](https://techcommunity.microsoft.com/tag/ninja%20training) · Blog oficial · Oficial · Nuevo · Microsoft Tech Community · 5 may 2026. Índice oficial de los Ninja Trainings en Tech Community donde figura "Become a Microsoft Purview eDiscovery Ninja" (Stefanie_Bier, 05-may-2026, ~226K vistas) junto al resto de la familia Ninja.
- [New Blog Post | Become a Microsoft 365 Advanced eDiscovery NINJA](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog-post--become-a-microsoft-365-advanced-ediscovery-ninja/2810216) · Blog oficial · Oficial · Legado aún útil · AshleyMartin · Microsoft Tech Community · 4 oct 2021. Anuncio de 2021 del Ninja de Advanced eDiscovery con ocho secciones alineadas al EDRM y una verificación de conocimientos tras cada nivel. *Nota:* Estructura histórica (Advanced eDiscovery -> eDiscovery Premium -> eDiscovery unificado); útil para entender el formato original del Ninja
- [Learn - MS Cloud Explorers (Microsoft Ninja Training Guides – All in One Place)](https://mscloudexplorers.com/learn/) · Blog · Comunidad · MS Cloud Explorers. Índice comunitario de todos los Ninja oficiales que describe la versión vigente del eDiscovery Ninja (experiencia unificada, holds, búsquedas en Teams y Copilot, review sets, analítica, exportación y transición clásica→moderna).
- [Secure Sensitive Data with Microsoft Purview Ninja Training Scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Curso · Oficial · Microsoft Learn. Ruta de Learn que muestra cómo la familia Purview Ninja migró a Microsoft Learn con escenarios y badge (MIP+DLP), modelo a imitar para el programa.
- [Microsoft Purview Compliance Manager (MSPCM) Ninja Training: Q1 2023](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-purview-compliance-manager-mspcm-ninja-training-q1-2023/3181322) · Blog oficial · Empleado de Microsoft · Legado aún útil · garyasp · Microsoft Tech Community · 18 feb 2022. Ejemplo del mecanismo Ninja de Purview: tres niveles con knowledge check y certificado de participación vía portal de atestación (no es certificación oficial). *Nota:* Referencia del formato de evaluación/certificado de la familia Purview Ninja
- [Retired: The Microsoft Purview Information Protection Ninja Training is here!](https://techcommunity.microsoft.com/blog/microsoft-security-blog/retired-the-microsoft-purview-information-protection-ninja-training-is-here/2887478/replies/4185815) · Blog oficial · Empleado de Microsoft · Retirado · Sarahzin_Shane · Microsoft Tech Community · 28 ago 2025. Muestra el retiro (jul-2025) del Ninja de MIP en Tech Community y su traslado a un nuevo hospedaje (aka.ms/MIPNinja) en agosto de 2025. *Nota:* Evidencia de que la familia Purview Ninja se está reubicando; útil para la sección (f)

<a id="cambios"></a>

## Qué cambió y por qué importa

Cada fila remite al módulo donde se explica en detalle.

| Tema | Antes | Ahora (noviembre de 2026) | Módulo |
|---|---|---|---|
| Portal | Centro de cumplimiento clásico | Portal de Microsoft Purview, en disponibilidad general desde julio de 2024; el portal clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 | [P0](01_Nivel_1_Inicial.md#p0) |
| Licencia | Microsoft 365 E5 Compliance | Microsoft Purview Suite (cambio de nombre del 1 de octubre de 2025, sin cambio funcional), complemento sobre E3 | [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1) |
| Experiencia de eDiscovery | Content Search, eDiscovery (Standard) y eDiscovery (Premium) separados | eDiscovery unificado con funciones estándar y premium; el clásico se retiró el 31 de agosto de 2025 (salvo 21Vianet) | [I1](01_Nivel_1_Inicial.md#i1) |
| Content Search | Herramienta independiente con holds | Caso generado por el sistema; desde el 16 de febrero de 2026 solo busca y exporta (holds y review sets requieren un caso completo) | [I1](01_Nivel_1_Inicial.md#i1), [M4](02_Nivel_2_Intermedio.md#m4) |
| Recolección | Colecciones y borradores de colección | Estadísticas y muestras en la búsqueda; indexación avanzada automática | [I3](01_Nivel_1_Inicial.md#i3), [M2](02_Nivel_2_Intermedio.md#m2) |
| Exportación por PowerShell | `New-ComplianceSearchAction -Export` | Parámetros de exportación retirados el 26 de mayo de 2025: se exporta desde el portal o con la API de Graph | [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2) |
| Vida de una exportación de búsqueda | Sin vencimiento corto | 14 días desde el 16 de febrero de 2026; las exportaciones de review set se descargan dentro de 30 días | [M4](02_Nivel_2_Intermedio.md#m4) |
| Automatización desatendida de eDiscovery | Cmdlets con autenticación solo aplicación | Sin soporte desde agosto de 2026: migrar a Microsoft Graph | [A2](03_Nivel_3_Avanzado.md#a2) |
| Retención de Audit (Standard) | 90 días | 180 días para registros generados desde el 17 de octubre de 2023 | [I2](01_Nivel_1_Inicial.md#i2) |
| Búsqueda de auditoría | Búsqueda clásica en el portal | Trabajos de búsqueda asíncronos (la clásica se retiró el 30 de noviembre de 2023) | [I2](01_Nivel_1_Inicial.md#i2) |
| Eventos de investigación de buzones | MailItemsAccessed y otros eventos clave asociados a Audit (Premium) | MailItemsAccessed, envíos y búsquedas en Audit (Standard) para E3 y E5, con playbook de la CISA del 15 de enero de 2025 | [M3](02_Nivel_2_Intermedio.md#m3) |
| Búsqueda programática de auditoría | `Search-UnifiedAuditLog` | API AuditLogQuery de Graph, GA en octubre de 2026; el cmdlet se retira el 15 de octubre de 2027 | [A2](03_Nivel_3_Avanzado.md#a2) |
| Evidencia de IA | Correo, documentos y chats | Prompts y respuestas de Copilot, agentes y apps de IA en el buzón del usuario y en Audit; IA no Microsoft con pago por uso | [A1](03_Nivel_3_Avanzado.md#a1) |
| Licencias para agentes | Sin un plan específico | Microsoft 365 E7 y Agent 365 disponibles en general desde el 1 de mayo de 2026; Purview para agentes gestionados con Agent 365 (incluidas auditoría y eDiscovery) requiere E7 o Agent 365 | [A1](03_Nivel_3_Avanzado.md#a1) |
| Contenedores de SharePoint Embedded | Fuera de alcance | Loop, Copilot Pages y Copilot Notebooks se buscan, retienen y exportan (anuncio del 24 de septiembre de 2026; Learn lo marca en vista previa) | [A1](03_Nivel_3_Avanzado.md#a1) |
| Contenido retenido | Un hold impedía cualquier eliminación | Priority Cleanup (vista previa) puede eliminarlo con simulación y tres aprobaciones, una de un administrador de eDiscovery | [A1](03_Nivel_3_Avanzado.md#a1), [O3](04_Nivel_4_Operacion.md#o3) |
| Investigaciones de datos con IA | No existían | Data Security Investigations: GA en enero de 2026, pago por uso; OCR GA en julio de 2026 | [A4](03_Nivel_3_Avanzado.md#a4) |
| IA dentro de eDiscovery | Sin asistencia | Security Copilot redacta KeyQL (vista previa) y resume ítems; incluido en E5 con 400 SCU al mes por cada 1.000 licencias pagadas | [A4](03_Nivel_3_Avanzado.md#a4) |
| Roles de Purview | Asignaciones permanentes y cambios con poco detalle | Fecha de expiración para asignaciones (salvo eDiscovery Administrator y Manager) desde julio de 2026 y nuevas operaciones de auditoría de RBAC | [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2) |
| Marco de referencia | EDRM clásico y NIST SP 800-61 Rev. 2 | EDRM 2.0 (1 de septiembre de 2026) y NIST SP 800-61 Rev. 3 (abril de 2025) | [O1](04_Nivel_4_Operacion.md#o1) |
| Credenciales | SC-400 y MS-101 | SC-401 (habilidades al 28 de octubre de 2026) y Applied Skills de retención, eDiscovery y Communication Compliance | [I0](01_Nivel_1_Inicial.md#i0) |
| Normativa en MCSA | Leyes de datos anteriores | Ley 21.719 de Chile vigente desde el 1 de diciembre de 2026, nueva LFPDPPP de México (20 de marzo de 2025) y Ley 7593/2025 de Paraguay, entre otras | [O3](04_Nivel_4_Operacion.md#o3) |

<a id="rutas"></a>

## Rutas por rol

Las horas son estimaciones de lectura y práctica.

- **Gestor de eDiscovery y asesoría legal** (~37 h). Litigios, requerimientos regulatorios y preservación defendible, del caso a la producción. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3).
- **Investigador interno** (~46 h). Investigaciones laborales, de fraude y de conducta, en coordinación con RR. HH. y Legal. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1).
- **Registros y cumplimiento** (~32 h). Retención, holds, respuesta a reguladores y evidencia de cumplimiento. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Auditoría interna** (~31 h). Pruebas de control sobre la auditoría, la retención, los accesos a casos y las exportaciones. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I2](01_Nivel_1_Inicial.md#i2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [A2](03_Nivel_3_Avanzado.md#a2), [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2), [O3](04_Nivel_4_Operacion.md#o3).
- **Analista del SOC** (~37 h). La auditoría como fuente de investigación, la preservación en incidentes y la correlación en Sentinel y Defender XDR. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4).
- **Oficial de privacidad** (~28 h). Proporcionalidad, minimización, transferencias y derechos de los titulares en cada búsqueda, auditoría y exportación. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M4](02_Nivel_2_Intermedio.md#m4), [A1](03_Nivel_3_Avanzado.md#a1), [A4](03_Nivel_3_Avanzado.md#a4), [O1](04_Nivel_4_Operacion.md#o1), [O3](04_Nivel_4_Operacion.md#o3).

<a id="plan"></a>

## Plan de entrenamiento sugerido

Calendario de referencia de 13 semanas para una dedicación de 4 a 8 horas por semana (unas 70 horas). Cada semana deja un entregable verificable; las evaluaciones cierran las semanas 3, 7, 11 y 13. Si tu rol tiene una ruta propia, recorre solo sus módulos y conserva el orden.

| Semana | Módulos | Foco | Entregable |
|---|---|---|---|
| 1 | [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0) | Purview, licencias, roles y pago por uso; cómo aprender | Laboratorio con auditoría activa, roles asignados, matriz de licencias y plan personal alineado con SC-401 |
| 2 | [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2) | eDiscovery unificado; Audit Standard frente a Premium | Caso PRUEBA- con miembros y permisos verificados; tres búsquedas de auditoría exportadas y una política de retención de un año |
| 3 | [I3](01_Nivel_1_Inicial.md#i3), [C2](05_Comunidad.md#c2) | Búsqueda y KeyQL; rutina de actualización | Consulta KeyQL con keyword report y registro de versiones; evaluación del nivel 1 aprobada |
| 4 | [M1](02_Nivel_2_Intermedio.md#m1) | Retenciones legales y custodios | Hold infinito y hold por consulta con su tiempo hasta efectividad y procedimiento de liberación |
| 5 | [M2](02_Nivel_2_Intermedio.md#m2) | Conjuntos de revisión y analítica | Review set con analítica, etiquetas, redacciones y consultas guardadas |
| 6 | [M3](02_Nivel_2_Intermedio.md#m3) | Audit para investigaciones de seguridad | Informe de alcance de un BEC simulado con MailItemsAccessed y línea de tiempo |
| 7 | [M4](02_Nivel_2_Intermedio.md#m4) | Exportación y cadena de custodia | Producción conciliada, con hash y formulario de custodia; evaluación del nivel 2 aprobada |
| 8 | [A1](03_Nivel_3_Avanzado.md#a1), [C1](05_Comunidad.md#c1) | Copilot, agentes y apps de IA como evidencia; referentes | Búsqueda de interacciones de IA, registro de auditoría de un agente anotado y política de eliminación de datos de IA |
| 9 | [A2](03_Nivel_3_Avanzado.md#a2) | Automatización con Microsoft Graph y PowerShell | Script que crea caso, búsqueda y hold, y extracción con AuditLogQuery con manejo de HTTP 429 |
| 10 | [A3](03_Nivel_3_Avanzado.md#a3) | Respuesta a incidentes, Sentinel y Defender XDR | Consultas en OfficeActivity y CloudAppEvents y playbook de BEC con preservación previa |
| 11 | [A4](03_Nivel_3_Avanzado.md#a4) | Security Copilot y Data Security Investigations | Estimación de costo de DSI, criterios de uso de IA y prueba en caso piloto; evaluación del nivel 3 aprobada |
| 12 | [O1](04_Nivel_4_Operacion.md#o1), [O2](04_Nivel_4_Operacion.md#o2) | Modelo operativo y métricas | RACI, formulario de intake, catálogo de roles con PIM y tablero de diez métricas |
| 13 | [O3](04_Nivel_4_Operacion.md#o3) | Gobierno, privacidad y normativa en MCSA | Registro de decisiones de privacidad revisado por Legal; evaluación del track de operación y reto final |

<a id="laboratorio"></a>

## Tu laboratorio

**Tu entorno.** Una prueba de Microsoft 365 E5 (un mes, 25 licencias) incluye las funciones premium de eDiscovery y Audit (Premium); si tu organización parte de E3, la [prueba de Microsoft Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) asigna 25 licencias durante 90 días. Suma una suscripción de Azure con los créditos de Visual Studio Enterprise para lo que se factura por uso —auditoría de apps de IA no Microsoft, Data Security Investigations, exportaciones por Graph con E3 y un workspace de Sentinel— y asóciala al tenant como indica el [modelo de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models). En tenants de prueba la auditoría puede venir apagada: actívala el día 0, porque tarda hasta 60 minutos y los eventos pueden demorar horas en ser buscables ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).

**Datos y nombres de práctica.** Crea cuentas, buzones, OneDrive, un sitio y un equipo de Teams con contenido sintético (por ejemplo, un «Proyecto Cóndor» con correos, adjuntos y chats fechados) y anota lo que siembras: será tu verdad de referencia para medir la precisión de las búsquedas. Nombra todo con el prefijo `PRUEBA-` y registra cada ejercicio como un cambio.

**Qué no se puede practicar en el laboratorio.** Holds y exportaciones a escala (miles de custodios o terabytes), interacciones reales de Microsoft 365 Copilot (sus licencias no vienen en la prueba E5), la inclusión de Security Copilot (aplica a licencias E5 pagadas), el complemento de retención de auditoría de 10 años, Data Security Investigations sobre datos reales, multigeografía y notificaciones de retención legal a custodios reales. Para esos casos, cada ejercicio describe la forma segura de practicar en producción.

**Costos a vigilar.** Almacenamiento y unidades de cómputo de Data Security Investigations (las insights proactivas consumen de forma continua), auditoría por uso de apps de IA no Microsoft, exportaciones por Graph con pago por uso, SCU de Security Copilot fuera del pool incluido e ingesta en el SIEM: los registros ampliados pueden multiplicar el volumen. Configura presupuestos y alertas al 50, 75 y 90 % antes del primer ejercicio y revisa el [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) (vista previa).

**Práctica en producción, siempre con Legal.** En eDiscovery, practicar en producción significa tocar datos de personas: usa cuentas y buzones de prueba, casos rotulados como entrenamiento, roles asignados justo a tiempo con [PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure), ninguna exportación de contenido real y la aprobación previa de Legal, RR. HH. y privacidad. Tu propia actividad queda en el registro de auditoría ([actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)): úsala como evidencia de que practicaste dentro de lo acordado.

**Limpieza.** Libera los holds, cierra y elimina los casos de práctica (los review sets solo se eliminan con el caso), borra las investigaciones de Data Security Investigations, revoca secretos y registros de aplicaciones, quita los roles temporales y desasocia la facturación por uso si no la vas a seguir usando. Ojo: si un hold de eDiscovery es lo único que mantiene un buzón inactivo, liberarlo o cerrar el caso elimina ese buzón ([buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)).

La matriz de qué se puede practicar en el laboratorio y qué solo en producción está en [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md). La guía para construir el entorno está en el [anexo común](../Anexo_Entorno_de_practica.md).

<a id="mapa"></a>

## Mapa de módulos

- **Nivel 1 · Inicial:** [P0 Prerrequisitos y licencias](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender](01_Nivel_1_Inicial.md#i0) · [I1 eDiscovery unificado](01_Nivel_1_Inicial.md#i1) · [I2 Audit Standard y Premium](01_Nivel_1_Inicial.md#i2) · [I3 Búsqueda y KeyQL](01_Nivel_1_Inicial.md#i3)
- **Nivel 2 · Intermedio:** [M1 Holds y custodios](02_Nivel_2_Intermedio.md#m1) · [M2 Review sets y analítica](02_Nivel_2_Intermedio.md#m2) · [M3 Audit para investigaciones](02_Nivel_2_Intermedio.md#m3) · [M4 Exportación y custodia](02_Nivel_2_Intermedio.md#m4)
- **Nivel 3 · Avanzado:** [A1 IA y agentes como evidencia](03_Nivel_3_Avanzado.md#a1) · [A2 Graph y PowerShell](03_Nivel_3_Avanzado.md#a2) · [A3 IR, Sentinel y Defender XDR](03_Nivel_3_Avanzado.md#a3) · [A4 Security Copilot y DSI](03_Nivel_3_Avanzado.md#a4)
- **Nivel 4 · Operación:** [O1 Modelo operativo](04_Nivel_4_Operacion.md#o1) · [O2 Métricas y mejora continua](04_Nivel_4_Operacion.md#o2) · [O3 Gobierno, privacidad y MCSA](04_Nivel_4_Operacion.md#o3)
- **Comunidad:** [C1 Referentes y libros](05_Comunidad.md#c1) · [C2 Español y actualización](05_Comunidad.md#c2)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

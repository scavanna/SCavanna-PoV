# Cierre, glosario y fuentes

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de eDiscovery y Audit no es saber dónde está cada botón, sino poder defender cada decisión: por qué preservaste ese alcance, por qué esa consulta, quién tuvo acceso a la evidencia, cuánto se retiene la auditoría y cómo se entregó. Tus siguientes pasos: el knowledge check del [Ninja oficial de eDiscovery](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108), el examen [SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y la credencial [Applied Skills de retención, eDiscovery y Communication Compliance](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/).

Continúa con los programas hermanos según tu rol: ciclo de vida de los datos y registros (retenciones de Purview), riesgo interno y cumplimiento de comunicaciones (los casos que se escalan a eDiscovery), Information Protection (etiquetas y cifrado), DSPM y seguridad de datos para IA, Compliance Manager (normativa regional) y, del lado del SOC, Sentinel, Defender XDR y Security Copilot. Dedica media hora al mes a [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) y revisa los avisos del Message Center antes de cambiar un procedimiento.

Si encuentras un enlace roto, un dato desactualizado o un recurso que debería estar aquí, anótalo y compártelo con tu equipo: la guía está pensada para revisarse periódicamente, como el Ninja original.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| AIAppInteraction | Tipo de registro de auditoría de las interacciones con apps de IA no Microsoft; se factura por uso y se retiene 180 días. |
| Audit (Premium) | Nivel de auditoría con un año de retención por defecto para Exchange, SharePoint, OneDrive y Entra ID, políticas personalizadas, opción de 10 años con complemento y mayor ancho de banda de API. |
| Audit (Standard) | Auditoría habilitada por defecto, con búsqueda en el portal, PowerShell y API, y 180 días de retención. |
| AuditLogQuery | API de Microsoft Graph para consultar el registro de auditoría de forma asíncrona; GA en octubre de 2026 y reemplazo de Search-UnifiedAuditLog. |
| Cadena de custodia | Registro documentado de quién recolectó, accedió, transfirió y entregó la evidencia, cuándo y cómo se preservó su integridad (por ejemplo, con hash). |
| Caso | Unidad central del eDiscovery unificado: agrupa miembros, orígenes de datos, búsquedas, holds, review sets y exportaciones de un asunto. |
| Content Search | Búsqueda de contenido que hoy vive en un caso generado por el sistema y, desde febrero de 2026, solo busca y exporta. |
| Custodio | Persona cuyos datos se preservan y analizan en un asunto; para funciones premium necesita E5 o un complemento equivalente. |
| Data Security Investigations (DSI) | Solución de Purview para investigar incidentes de datos con búsqueda vectorial e IA generativa; se factura por almacenamiento y unidades de cómputo. |
| EDRM | Electronic Discovery Reference Model; su versión 2.0 (septiembre de 2026) agrupa etapas en Data Acquisition y agrega la disposición. |
| Estadísticas | Resumen de volumen, ubicaciones y aporte de cada término de una búsqueda; reemplazaron a las colecciones del eDiscovery clásico. |
| Hold (retención legal) | Política que preserva el contenido de los orígenes de un caso mientras dura el asunto; puede tardar hasta 24 horas en aplicarse. |
| Indexación avanzada | Reprocesamiento de ítems parcialmente indexados; en la experiencia unificada corre de forma automática. |
| Issuing officer | Persona en cuyo nombre se emiten las notificaciones de retención legal a los custodios. |
| KeyQL | Keyword Query Language: sintaxis de búsqueda de eDiscovery. No es lo mismo que KQL. |
| KQL | Kusto Query Language: lenguaje de Sentinel y Defender XDR; un subconjunto se usa en el explorador avanzado de review sets. |
| Límites de cumplimiento | Filtros de permisos de búsqueda que restringen qué contenido puede buscar cada grupo, por ejemplo por país o subsidiaria (compliance boundaries). |
| MailItemsAccessed | Evento de auditoría que registra accesos a mensajes (sync por carpeta y bind agregado cada dos minutos) para acotar compromisos de buzón. |
| Management Activity API | API de suscripción y descarga de blobs de Office 365 para enviar la auditoría a un SIEM. |
| OfficeActivity | Tabla de Sentinel con la auditoría de Exchange, SharePoint y Teams. |
| Priority Cleanup | Limpieza prioritaria (vista previa) que puede eliminar contenido retenido con simulación y aprobaciones; lo eliminado deja de ser descubrible. |
| Purview Suite | Complemento de Purview (antes Microsoft 365 E5 Compliance) que agrega a E3, entre otras capacidades, Audit (Premium) y eDiscovery premium. |
| Redacción (PDF burn) | Ocultamiento permanente de contenido en un ítem del review set; al exportar se entrega el PDF redactado en lugar del original. |
| Review set (conjunto de revisión) | Copia estática de ítems en almacenamiento de Azure gestionado por Microsoft para revisar, analizar, etiquetar y exportar. |
| RMS Decrypt | Rol que permite descifrar contenido protegido con etiquetas al agregarlo a review sets o exportarlo. |
| SCU | Security Compute Unit: capacidad de Security Copilot; E5 y E7 incluyen 400 SCU al mes por cada 1.000 licencias pagadas, hasta 10.000. |
| Search And Purge | Rol que permite eliminar en bloque el contenido que coincide con una búsqueda, incluidos los datos de IA. |
| Search-UnifiedAuditLog | Cmdlet de Exchange Online PowerShell para buscar en la auditoría; se retira el 15 de octubre de 2027. |
| SearchQueryInitiated | Eventos de auditoría de búsquedas en Exchange y SharePoint; el de Exchange se habilita buzón por buzón. |
| SharePoint Embedded | Contenedores de archivos de apps como Loop, Copilot Pages y Copilot Notebooks, incorporados a eDiscovery en 2026. |
| UAL | Unified Audit Log: registro de auditoría unificado de Microsoft 365. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Retención de Audit (Standard): algunas guías de licenciamiento de terceros siguen citando 90 días, mientras Learn indica 180 días para registros generados desde el 17 de octubre de 2023 ([guía de terceros](https://microsoftnegotiations.com/blog/microsoft-purview-licensing-guide) frente a [Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)).
- Exportación por la API de Graph: el aviso MC1055528 (abril de 2025) la asociaba a E5 y eDiscovery (Premium); la página de la API (mayo de 2026) permite exportar con E3 delegado mediante pago por uso. Confírmalo en tu tenant antes de diseñar automatizaciones ([MC1055528](https://mc.merill.net/message/MC1055528), [API de eDiscovery](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)).
- SharePoint Embedded (Loop, Copilot Pages y Copilot Notebooks): el blog de seguridad del 24 de septiembre de 2026 lo presenta como disponible y Learn lo marca en vista previa ([blog](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/), [componentes de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-features-components)).
- Codificación predictiva: «Learn about eDiscovery» la menciona dentro de los review sets, pero sus artículos siguen en vista previa y con el aviso de retiro del clásico; trátala como no confirmada en la experiencia unificada ([Learn about eDiscovery](https://learn.microsoft.com/en-us/purview/edisc), [codificación predictiva](https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-overview?redirectSourcePath=%252fde-de%252farticle%252ftagging-and-assessment-b5c82de7-ed2f-4cc6-becd-db403faf4d18&view=o365-worldwide)).
- Notificaciones de retención legal e issuing officers: están documentadas para eDiscovery (Premium) con aviso de retiro, y un análisis comunitario —con preguntas abiertas no confirmadas por Microsoft— las describe en el portal nuevo. Confirma su ubicación y alcance en tu tenant ([comunicaciones](https://learn.microsoft.com/th-th/purview/ediscovery-managing-custodian-communications?view=o365-worldwide), [eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/)).
- El Ninja oficial de 2026 todavía se describe como «eDiscovery Premium solution», aunque el clásico Premium está retirado. La línea de investigación de este programa no logró abrir el post directamente; su URL proviene de la investigación de formato Ninja de la serie y del [índice de Tech Community](https://techcommunity.microsoft.com/tag/ninja%20training).
- La guía de MailItemsAccessed usa `Search-UnifiedAuditLog` en sus ejemplos; los ejercicios de esta edición agregan AuditLogQuery porque el cmdlet se retira el 15 de octubre de 2027 ([guía](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts), [MC1505599](https://mc.merill.net/message/MC1505599)).
- Exportación de review sets a una cuenta propia de Azure Storage: el procedimiento está redactado para la interfaz de eDiscovery (Premium); valida que exista una opción equivalente en la experiencia unificada ([procedimiento](https://learn.microsoft.com/en-us/purview/ediscovery-download-export-jobs)).
- La versión en español de la página de la API de eDiscovery dice «suscripción A3» donde la versión en inglés dice E3; usa la versión en inglés ([versión en español](https://learn.microsoft.com/es-es/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)).
- «Insights inteligentes» y eventos de alto valor: la página de soluciones de auditoría sigue asociándolos a Audit (Premium), mientras MailItemsAccessed, los envíos y las búsquedas ya están en Audit (Standard). Verifica qué eventos y propiedades quedan como exclusivos de Premium antes de justificar una compra ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).
- Registros de entidades no usuario (service principals, sistema y apps): la investigación indica un año fijo de retención sin políticas personalizadas; confirma si aplica igual en tenants sin licencias Premium ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).
- Fecha de disponibilidad general de Data Security Investigations: las fuentes la sitúan a fines de enero de 2026 (nota de prensa del 27 de enero y AMA oficial del 5 de febrero); no se encontró una fecha exacta en Learn ([AMA](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393), [Help Net Security](https://www.helpnetsecurity.com/2026/01/27/microsoft-purview-data-security-investigations/)).
- La limitación de las búsquedas de contenido a buscar y exportar (MC1216266) se conoce por un análisis comunitario; no se localizó el aviso original ([análisis](https://office365itpros.com/2026/01/15/content-searches-change/)).
- Inclusión de Security Copilot en E5: se calcula sobre licencias pagadas, por lo que un tenant de prueba no debería esperar SCU incluidas (inferencia de la investigación de la serie; confírmalo con Microsoft). Tampoco cubre Data Security Investigations no agéntico ([inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).
- Los precios de referencia (Microsoft Purview Suite, Microsoft 365 E5 y medidores de DSI) varían por región y acuerdo; usa las páginas oficiales y tu calculadora ([precios de Purview](https://www.microsoft.com/en-us/security/microsoft-purview-pricing), [precios de consumo](https://azure.microsoft.com/en-us/pricing/details/purview/)).
- El playbook de la CISA tendría una revisión posterior (mayo de 2026) según la comunidad; no se confirmó en la fuente oficial ([CISA](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook)).
- El libro *Microsoft eDiscovery In-Depth* no muestra fecha de edición: verifica que cubra la experiencia unificada antes de usarlo como texto de estudio ([ficha](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707)).
- El cómputo de IA de Data Security Investigations no ofrece ubicación en Latinoamérica (Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»). No es una contradicción, pero sí una decisión que Legal y privacidad deben tomar en cada país ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).
- Aprobaciones de la limpieza prioritaria: el aviso MC1183292 (noviembre de 2025) y un resumen comunitario de octubre de 2026 hablan de dos aprobaciones, mientras las novedades de Purview de julio de 2026 exigen tres (administración de limpieza prioritaria, de retención y de eDiscovery). Confirma el flujo vigente en tu tenant antes de escribir el procedimiento ([MC1183292](https://mc.merill.net/message/MC1183292), [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new), [resumen de octubre de 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/)).
- Auditoría y eDiscovery de agentes: la página de auditoría de Copilot e IA indica que los registros de Copilot Studio y Microsoft Foundry (con `AgentId` y `AgentName`) se generan en Audit (Standard), mientras la descripción de servicio de Agent 365 ubica la auditoría y el eDiscovery de Purview para agentes entre las capacidades que requieren Microsoft 365 E7 o Agent 365. La diferencia parece estar en los agentes gestionados con Agent 365; confírmala antes de prometer cobertura a Legal ([auditoría de Copilot e IA](https://learn.microsoft.com/en-us/purview/audit-copilot), [Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)).
- Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar, días después de la fecha de corte, el estado de funciones en vista previa: explorador avanzado de review sets, consulta For Review, KeyQL con Copilot, clave del cliente en exportaciones, SharePoint Embedded, Priority Cleanup y el Posture Agent de DSI.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

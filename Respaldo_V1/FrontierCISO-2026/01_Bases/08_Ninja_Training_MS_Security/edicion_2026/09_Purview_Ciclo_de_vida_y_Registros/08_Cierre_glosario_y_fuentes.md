# Cierre, glosario y fuentes

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja en ciclo de vida y registros es un hábito: revisar cada mes las novedades de Purview, conciliar eventos y eliminaciones pendientes, medir la deuda de retención y volver a la tabla de retención cada vez que cambia una ley o un proceso. Para credenciales, el siguiente paso es SC-401 y la Applied Skill de retención, eDiscovery y Communication Compliance; para profundizar, sigue los programas hermanos de eDiscovery y Audit, Information Protection, DSPM y seguridad de datos para IA, y Compliance Manager.

Si encuentras un dato desactualizado, un enlace roto o un recurso que debería estar aquí, anótalo y compártelo con tu equipo: la guía está pensada para revisarse periódicamente. Y recuerda que no es asesoría legal: ante una duda regulatoria, Legal y privacidad tienen la última palabra, y tu trabajo es dejar cada decisión documentada, aprobada y reflejada en el plan de archivos.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Ámbito adaptable | Consulta diaria sobre atributos de usuarios, grupos o sitios (departamento, país) que define a quién aplica una directiva; requiere nivel E5. |
| Ámbito estático | Lista explícita de ubicaciones incluidas o excluidas; si quitas la última inclusión, la directiva vuelve a aplicarse a «Todos». |
| Archivo de expansión automática | Crecimiento del buzón de archivo hasta 1,5 TB, o 3 TB con licencias elegibles desde octubre de 2026; se habilita por PowerShell y es irreversible. |
| Biblioteca de conservación | Biblioteca oculta (Preservation Hold) de SharePoint y OneDrive que guarda lo editado o eliminado bajo retención; cuenta para la cuota. |
| Buzón inactivo | Buzón de una cuenta eliminada que se conserva sin licencia porque tenía una retención con acción de retener o un hold. |
| Clasificador entrenable | Modelo de aprendizaje automático que reconoce categorías de contenido, como contratos o currículums, para autoaplicar etiquetas. |
| Delay hold | Retención temporal al quitar un hold; desde agosto de 2026 se aplica automáticamente durante 30 días al quitar el último hold de un buzón inactivo. |
| Directiva de recopilación | Directiva de Purview que captura eventos y contenido de apps de IA; requisito para retener IA distinta de Microsoft 365 Copilot y Copilot Studio. |
| Directiva de retención | Regla que retiene, elimina o retiene y luego elimina el contenido de ubicaciones completas; es la base del diseño. |
| Etiqueta de retención | Configuración que se aplica a elementos concretos (manual, predeterminada o automáticamente) y puede declararlos registros. |
| Hold de eDiscovery | Retención legal asociada a un caso que suspende toda eliminación; prevalece porque retener gana sobre eliminar. |
| ID de activo (Asset ID) | Propiedad de SharePoint y OneDrive que vincula documentos con un evento concreto, como un número de contrato o de empleado. |
| KQL (Keyword Query Language) | Lenguaje de búsqueda por palabras clave y propiedades de Microsoft 365 usado en la autoaplicación y en eDiscovery; distinto del Kusto Query Language de Sentinel. |
| Limpieza prioritaria | Eliminación permanente y acelerada de contenido sensible pese a retenciones y holds, con tres aprobaciones; en vista previa y sin efecto sobre registros. |
| Límites de cumplimiento | Filtros de permisos que restringen las búsquedas de eDiscovery por atributo, como país o subsidiaria. |
| Microsoft 365 Archive | Nivel de almacenamiento frío de SharePoint para sitios y archivos inactivos, con pago por uso por encima de la cuota. |
| MRM | Messaging Records Management: directivas y etiquetas de retención heredadas de Exchange; Microsoft no las recomienda salvo requisito específico. |
| Pago por uso | Modelo de facturación de Purview a través de una suscripción de Azure vinculada al tenant; lo exigen las ubicaciones de IA y Microsoft 365 Archive. |
| Plan de archivos | Vista de Records Management para crear, importar y exportar etiquetas con descriptores: función, categoría, tipo de autoridad y cita. |
| Preservation Lock | Bloqueo que impide desactivar, eliminar o hacer menos restrictiva una directiva; se usa ante requisitos regulatorios y es irreversible. |
| Principios de retención | Reglas de precedencia: retener gana sobre eliminar, gana el período de retención más largo, lo explícito gana sobre lo implícito y gana la eliminación más corta. |
| Prueba de eliminación | Evidencia exportable, desde la página de eliminación, de los elementos pendientes y eliminados. |
| Recoverable Items | Carpeta de Exchange donde se conservan los elementos eliminados o modificados bajo retención o hold. |
| Registro | Elemento con una etiqueta que lo declara registro: bloqueado (no se edita ni se elimina) o desbloqueado (se edita y conserva la etiqueta). |
| Registro regulatorio | Registro que no permite editar, eliminar, cambiar ni quitar la etiqueta, ni siquiera a los administradores; es irreversible. |
| Retención basada en eventos | Retención cuyo período empieza con un evento, como la salida de un empleado o el fin de un contrato. |
| Revisión de eliminación | Aprobación humana, en una o varias etapas, de lo que ocurre al final del período de retención. |
| SIT | Tipo de información confidencial (sensitive information type): patrón que detecta datos como números de identificación o de tarjeta. |
| SubstrateHolds | Carpeta oculta donde se conservan los mensajes de Teams y Viva Engage y las interacciones con Copilot e IA retenidos. |
| TRD | Tabla de retención documental definida por la Ley 594 de 2000 de Colombia: series documentales con su plazo y disposición final. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Limpieza prioritaria en SharePoint y OneDrive: el mensaje [MC1183292](https://mc.merill.net/message/MC1183292) (6 de noviembre de 2025) la anuncia con disponibilidad general en GCC, mientras que las [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new) de agosto de 2026 la listan en vista previa.
- Aprobaciones de la limpieza prioritaria: MC1183292 habla de dos administradores; desde julio de 2026 la documentación exige tres aprobaciones separadas ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)).
- Archivo de expansión automática: la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) sigue indicando 1,5 TB, mientras que [Learn](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving) anuncia 3 TB desde mediados de octubre de 2026 para licencias elegibles con el plan Records Management habilitado.
- Azure PST Import: [MC1281505](https://mc.merill.net/message/MC1281505) sitúa el despliegue mundial desde fines de enero de 2027 y [MC1455013](https://mc.merill.net/message/MC1455013) lo lleva a fines de marzo o abril de 2027. Confírmalo en el Centro de mensajes de tu tenant.
- Microsoft 365 Archive: la [página de producto](https://www.microsoft.com/en-us/microsoft-365/microsoft-365-archive) dice que la búsqueda de usuario final no está soportada y que el archivado por archivo está en vista previa; la [documentación de Learn](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide) dice lo contrario.
- Acción de archivo en retención (MC1325441): [Microsoft 365 for IT Pros](https://office365itpros.com/2026/08/20/microsoft-365-archive-retention/) indica disponibilidad general a fin de septiembre de 2026 y [purview365](https://purview365.com/blog/sharepoint-online-14-retention-labels-policies) entre inicios de octubre y noviembre de 2026; Learn no lo confirmaba al corte.
- Celdas «No verificado» de la [matriz de retención](00_Programa.md#matriz-retencion): etiquetas y autoaplicación en carpetas públicas de Exchange, ámbitos adaptables para registros de llamadas de Teams, Skype Empresarial y Planner, y la licencia de las tareas de Planner.
- Datos de fuentes comunitarias pendientes de confirmar en Learn: la retención de tareas de Planner (MC1384412), que la opción de registro regulatorio esté oculta y se habilite con Set-RegulatoryComplianceUI, los límites de la revisión de eliminación (hasta 5 etapas, eliminación 15 días después de la aprobación final y autoaprobación de 7 a 365 días) y que la autoaplicación nunca etiquete carpetas ni conjuntos de documentos.
- Licencias de IA: la descripción del servicio indica, en tiempo futuro, que las capacidades de Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra se licenciarán con Microsoft 365 E7 y SKU de Agent 365; la investigación no encontró para Enterprise AI apps y Other AI apps un requisito de plan por usuario más allá del pago por uso.
- Licencias de autoaplicación: la fila de clasificadores entrenables de la descripción del servicio no incluye Office 365 E5, a diferencia de la autoaplicación por SIT o palabras clave. Verifícalo antes de diseñar sobre Office 365 E5.
- Ninja oficial: el enlace corto aka.ms/DLM/NinjaTraining, citado en 2024, no se pudo resolver y el post de 2023 no muestra actualizaciones posteriores. La fecha del webinar «Getting Started with Deploying…» (23 de enero de 2023) podría corresponder a 2024.
- Normativa: la investigación de este programa cubrió las leyes de archivos de México y Colombia, pero no las leyes de protección de datos personales; el módulo O3 usa fuentes oficiales reunidas por los programas de Compliance Manager, Insider Risk e Information Protection, sin revisión jurídica. Ninguna referencia de esta guía reemplaza la validación de Legal.
- Fuentes comunitarias con autor no verificado (purview365, The Purview Practitioner, el laboratorio de indra-pr y el canal de video sobre directivas de retención): úsalas como apoyo didáctico y contrástalas con Learn.
- Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa poco después del corte, por ejemplo de la limpieza prioritaria, Azure PST Import o las directivas de archivos inactivos de SharePoint Advanced Management. Las versiones en español de Learn se actualizan después que las de inglés.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

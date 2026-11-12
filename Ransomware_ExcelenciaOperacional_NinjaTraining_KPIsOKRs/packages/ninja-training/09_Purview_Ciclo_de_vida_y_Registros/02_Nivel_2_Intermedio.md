# Nivel 2 · Intermedio · Automatizar y eliminar con evidencia

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Autoaplicación con SIT, KQL y clasificadores entrenables; revisión y prueba de eliminación; limpieza prioritaria; retención basada en eventos; archivo, buzones inactivos e importación. Terminas con el ciclo de vida completo de un registro, del etiquetado a la eliminación con evidencia.

*L300 · 4 módulos · ~17 horas · 19 recursos*

**Módulos de este nivel:** [M1 Autoaplicación de etiquetas](#m1) · [M2 Revisión de eliminación](#m2) · [M3 Retención por eventos](#m3) · [M4 Archivo, inactivos y PST](#m4)

<a id="m1"></a>

## M1 · Aplicación automática de etiquetas de retención

*L300 · ~5 h · Origen: Ninja oficial de ciclo de vida y registros (2023): aplicación automática y Syntex*

Las etiquetas publicadas dependen de que las personas las apliquen, y eso no escala. La **autoaplicación** las asigna por ti a partir de cuatro tipos de condición: tipos de información confidencial (SIT), palabras clave o propiedades buscables con **KQL** (Keyword Query Language, el lenguaje de búsqueda de Microsoft 365; no lo confundas con el Kusto Query Language de Sentinel), **clasificadores entrenables** y datos adjuntos en la nube. Antes de activar puedes ejecutar una **simulación** con SIT y consultas, con límites: 30 trabajos cada 12 horas, 100 muestras por buzón y hasta 20.000 ubicaciones con ámbitos adaptables. No sirve para registros regulatorios ni para etiquetas predeterminadas.

La publicación también tiene su arte: las etiquetas aparecen en SharePoint y OneDrive normalmente en un día (hasta siete) y en Exchange en hasta siete días; las directivas de publicación no admiten unidades administrativas; y en SharePoint puedes fijar una **etiqueta predeterminada** para bibliotecas, carpetas o conjuntos de documentos. Un detalle que señala la comunidad: la autoaplicación etiqueta elementos, nunca carpetas ni conjuntos de documentos en sí mismos.

Revisa la licencia antes de diseñar: autoaplicar por SIT o KQL está en el nivel E5 (incluido Office 365 E5), pero la fila de clasificadores entrenables de la descripción del servicio no incluye Office 365 E5.

**Por qué importa**

La autoaplicación hace medible y consistente la cobertura del plan de archivos, sin depender de que cada persona etiquete bien. También es donde más daño puede hacer un error: una consulta demasiado amplia puede etiquetar —y más tarde eliminar— miles de elementos. La simulación iterativa sobre un piloto reduce ese riesgo y deja evidencia de cada decisión.

**Qué vas a lograr**

- Elegir la condición adecuada (SIT, KQL, clasificador entrenable o adjuntos en la nube) para cada categoría del plan de archivos.
- Escribir consultas KQL sobre propiedades buscables de Microsoft 365.
- Ejecutar una simulación, revisar muestras e iterar antes de activar.
- Configurar etiquetas predeterminadas en SharePoint y publicar etiquetas para Outlook.
- Explicar los límites y los tiempos de aplicación de las etiquetas.

> **Atención.** Licencias: autoaplicar por SIT, palabras clave o propiedades está en el nivel E5, incluido Office 365 E5, pero la fila de clasificadores entrenables de la descripción del servicio lista Microsoft 365 E5, A5 y G5, Purview Suite, Defender + Purview Suite FLW e IP&G, sin Office 365 E5 ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Verifícalo antes de diseñar sobre Office 365 E5.

> **Consejo Ninja.** Simula antes de activar: la simulación admite SIT y consultas, con hasta 30 trabajos cada 12 horas, 100 muestras por buzón y 20.000 ubicaciones con ámbitos adaptables. La autoaplicación no sirve para registros regulatorios ni para etiquetas predeterminadas ([autoaplicación](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically)).

> **Atención.** Tiempos y límites de publicación: las etiquetas aparecen en SharePoint y OneDrive normalmente en 1 día (hasta 7) y en Exchange en hasta 7 días, y las directivas de publicación no admiten unidades administrativas ([publicar etiquetas](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels)). Según la comunidad, la autoaplicación etiqueta elementos, nunca carpetas ni conjuntos de documentos en sí mismos ([Joanne Klein](https://joannecklein.com/category/microsoft-purview/)).

> **Consejo Ninja.** Aquí KQL es Keyword Query Language, la misma sintaxis de propiedades y palabras clave que usarás en eDiscovery ([lenguaje de consultas](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language)). Los tipos de información confidencial y los clasificadores entrenables se profundizan en el programa de Information Protection, módulo I2 ([SIT](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about), [clasificadores entrenables](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with)).

**¿Tienes poco tiempo?**

- [Automatically apply a retention label to retain or delete content](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically) · Documentación
- [Publish retention labels and apply them in apps](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels) · Documentación
- [Implement and manage retention with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-implement-manage-retention/) · Curso

**Cómo elegir la condición de autoaplicación**

| Condición | Funciona bien para | Simulación | Licencia | Cuidado |
|---|---|---|---|---|
| Tipo de información confidencial (SIT) | Contenido con datos reconocibles por patrón, como identificaciones o números de tarjeta | Sí | Nivel E5 (incluido Office 365 E5) | Ajusta instancias y confianza: los datos de prueba no reflejan producción |
| Palabras clave o propiedades buscables (KQL) | Contenido identificable por nombre, asunto, ruta o una propiedad del sitio | Sí | Nivel E5 (incluido Office 365 E5) | Una consulta amplia etiqueta de más: versiona la consulta y revísala por pares |
| Clasificador entrenable | Categorías de negocio sin patrón fijo, como contratos o currículums | No (la simulación admite SIT y consultas) | Microsoft 365 E5, A5 o G5, Purview Suite, Defender + Purview Suite FLW o IP&G (Office 365 E5 no figura) | Necesita volumen real: empieza con una etiqueta sin eliminación y un alcance pequeño |
| Datos adjuntos en la nube | Archivos compartidos como vínculo en conversaciones y correos | No (la simulación admite SIT y consultas) | Nivel E5 | Revisa el alcance y el comportamiento en la documentación antes de activarla |
| Etiqueta predeterminada de SharePoint (no es una directiva de autoaplicación) | Bibliotecas, carpetas o conjuntos de documentos con contenido homogéneo | No aplica | Nivel E5 | Comunícala a los usuarios: la etiqueta llega sin que nadie la elija |

Fuentes: [autoaplicación](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically), [publicar etiquetas](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels) y [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). Datos al 6 de noviembre de 2026.

### Documentación, cursos y credenciales

- [Automatically apply a retention label to retain or delete content](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically) · Documentación · Oficial · Microsoft Learn. Guía de autoaplicación de etiquetas por tipos de información confidencial, palabras clave o propiedades, clasificadores entrenables y datos adjuntos en la nube, con modo de simulación.
- [Publish retention labels and apply them in apps](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels) · Documentación · Oficial · Microsoft Learn. Cómo publicar etiquetas con directivas estáticas o adaptables y aplicarlas manualmente, por reglas de Outlook o como etiqueta predeterminada de bibliotecas, carpetas y conjuntos de documentos de SharePoint.

**Manos a la obra**

1. `Laboratorio parcial` Sube al sitio piloto 20 documentos ficticios que contengan un SIT (por ejemplo, números de tarjeta de prueba), espera a que se indexen y crea una directiva de autoaplicación por ese SIT en modo simulación, con una etiqueta sin eliminación ([autoaplicación](https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically)). Revisa las muestras y ajusta el número de instancias. Limitación: necesitas documentos indexados y los datos sintéticos no reflejan la variedad de producción. Evidencia: resumen de la simulación y la decisión de ajuste.
2. `Laboratorio parcial` Crea una segunda simulación con una consulta KQL sobre propiedades, por ejemplo `filename:contrato*` para SharePoint y `subject:contrato` para Exchange, y comprueba la sintaxis en la [referencia de KQL](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language). Limitación: la misma del paso anterior, porque la simulación solo ve contenido indexado. Evidencia: muestras de ambas simulaciones y la consulta final versionada.
3. `Laboratorio parcial` Crea una directiva con un clasificador entrenable predefinido (por ejemplo, de contratos o de currículums) limitada al sitio piloto y con una etiqueta de solo retener: como la simulación solo admite SIT y consultas, el alcance reducido es tu red de seguridad ([clasificadores entrenables](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with)). Limitación: los clasificadores necesitan volumen real y en el laboratorio verás pocos aciertos. Evidencia: elementos etiquetados una semana después y tu valoración de la precisión.
4. `Laboratorio` Configura una etiqueta predeterminada en una biblioteca del sitio piloto, sube tres documentos nuevos y verifica que la heredan; mueve uno a otra biblioteca y anota qué ocurre con su etiqueta. Evidencia: capturas de la columna de etiqueta.
5. `Laboratorio` Publica etiquetas para buzones piloto y, cuando aparezcan en Outlook en la web (hasta 7 días), aplica una a un correo y otra a una carpeta; observa qué etiqueta reciben los correos que muevas a esa carpeta ([publicar etiquetas](https://learn.microsoft.com/en-us/purview/create-apply-retention-labels)). Evidencia: capturas de ambos casos.
6. `Laboratorio` Para cada categoría del [plan de archivos de ejemplo](00_Programa.md#plan-archivos), decide el método de aplicación (manual, predeterminada, SIT, KQL, clasificador entrenable o evento) con la tabla de este módulo y justifica la elección. Evidencia: matriz de métodos revisada por el gestor de registros.
7. `Solo producción` Activa la autoaplicación sobre contenido real. Cómo hacerlo seguro: simula primero en un único sitio piloto, revisa las muestras con el dueño de los datos, amplía por iteraciones (sitio, departamento, organización) y usa en la primera ola etiquetas sin eliminación; activa solo con aprobación registrada. Evidencia: bitácora de iteraciones con muestras revisadas y aprobaciones.

<a id="m2"></a>

## M2 · Revisión de eliminación, prueba de eliminación y limpieza prioritaria

*L300 · ~4 h · Origen: Ninja oficial de ciclo de vida y registros (2023): fin de la retención y eliminación*

Al final del período de retención no todo debe borrarse automáticamente. La **revisión de eliminación** pide a personas designadas que aprueben la eliminación, extiendan el período o cambien la etiqueta, en una o varias etapas secuenciales con al menos un revisor por etapa. Para revisar se necesita el rol Disposition Management, del grupo Records Management —el administrador global no lo tiene por defecto— y la auditoría debe estar activa al menos un día antes. La página de eliminación permite filtrar y exportar los elementos pendientes y los ya eliminados: esa exportación es tu **prueba de eliminación**.

La **limpieza prioritaria**, en vista previa, es el mecanismo de excepción para borrar de forma permanente contenido sensible de buzones —por ejemplo, datos personales enviados por error— aunque haya retención, holds o Preservation Lock. No aplica a registros, exige buzones con al menos 10 MB, se sigue en la auditoría por su ID y puede desactivarse para todo el tenant. Desde julio de 2026 requiere tres aprobaciones separadas: administrador de limpieza prioritaria, administrador de retención y administrador de eDiscovery. Para SharePoint y OneDrive también está en vista previa, con señales contradictorias sobre su estado.

**Por qué importa**

Eliminar es irreversible. Un proceso de revisión con separación de funciones y prueba exportable protege a la organización de dos hallazgos clásicos de auditoría: registros que se conservan sin justificación y registros eliminados sin autorización. La limpieza prioritaria, bien gobernada, reduce el impacto de un derrame de datos sin abrir una puerta trasera para borrar evidencia.

**Qué vas a lograr**

- Configurar una etiqueta con revisión de eliminación en varias etapas y revisores con mínimo privilegio.
- Ejecutar y documentar una revisión, y exportar la prueba de eliminación.
- Explicar las restricciones, aprobaciones y estado de la limpieza prioritaria.
- Diseñar la separación de funciones entre diseño, revisión y limpieza.

> **Atención.** Para revisar eliminaciones hace falta el rol Disposition Management, del grupo Records Management, que el administrador global no tiene por defecto, y la auditoría debe estar activa al menos un día antes ([eliminación](https://learn.microsoft.com/en-us/purview/disposition)). Asigna la revisión a un grupo personalizado de revisores, no a los administradores.

> **Qué cambió.** Desde julio de 2026, la limpieza prioritaria de buzones requiere tres aprobaciones separadas: administrador de limpieza prioritaria, administrador de retención y administrador de eDiscovery ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Está en vista previa, no aplica a registros, exige buzones con al menos 10 MB y puede desactivarse para todo el tenant ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)).

> **Atención.** Señales contradictorias: [MC1183292](https://mc.merill.net/message/MC1183292) (noviembre de 2025) anunció la limpieza prioritaria de SharePoint y OneDrive con disponibilidad general en GCC y con dos administradores, mientras que las novedades de agosto de 2026 la listan en vista previa. Trátala como vista previa y diseña las aprobaciones para tres personas.

> **Consejo Ninja.** Según la comunidad, la revisión admite hasta 5 etapas, el contenido aprobado se elimina unos 15 días después de la aprobación final y la autoaprobación se configura entre 7 y 365 días, con 14 por defecto ([purview365](https://purview365.com/blog/sharepoint-online-14-retention-labels-policies)). En la API, las etapas (`dispositionReviewStages`) son secuenciales y cada una exige al menos un revisor ([retentionLabel](https://learn.microsoft.com/en-us/graph/api/resources/security-retentionlabel?view=graph-rest-1.0)).

**¿Tienes poco tiempo?**

- [Disposition of content](https://learn.microsoft.com/en-us/purview/disposition) · Documentación
- [Expedite the permanent deletion of sensitive information from mailboxes (priority cleanup)](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Documentación
- [Manage records and disposition with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-manage-records/) · Curso

**Qué puede ocurrir al final del período de retención**

| Opción | Cuándo usarla | Evidencia que deja | Requisito o límite |
|---|---|---|---|
| Eliminar automáticamente | Contenido sin valor residual y con plazo claro | La regla y el período documentados en el plan de archivos | Irreversible pasados los plazos de papelera o de Recoverable Items |
| Revisión de eliminación | Registros de alto valor o sensibles a litigios | Exportación de pendientes y eliminados desde la página de eliminación (prueba de eliminación) | Nivel E5; rol Disposition Management; auditoría activa |
| Cambiar la etiqueta (reetiquetar) | Encadenar etapas, por ejemplo de activo a histórico | La nueva etiqueta aplicada al elemento | Nivel E5 |
| Ejecutar un flujo de Power Automate | Notificar, mover a un archivo central o integrar con otro sistema | Historial de ejecuciones del flujo | Solo en etiquetas nuevas; flujo en «My flows»; no reetiqueta a registro regulatorio |
| Mover a Microsoft 365 Archive y luego eliminar (MC1325441) | Contenido que conviene conservar a bajo costo antes de eliminarlo | Estado archivado del archivo | Pago por uso; puede tardar hasta 10 días; fechas de disponibilidad en conflicto |
| Limpieza prioritaria (excepción) | Datos sensibles en buzones que deben eliminarse pese a retenciones y holds | Registro de auditoría con el ID de la limpieza | Vista previa; tres aprobaciones; no aplica a registros |

Fuentes: [revisión de eliminación](https://learn.microsoft.com/en-us/purview/disposition), [flujo al final de la retención](https://learn.microsoft.com/en-us/purview/retention-label-flow), [acción de archivo (comunidad)](https://office365itpros.com/2026/08/20/microsoft-365-archive-retention/), [limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) y [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).

### Documentación, cursos y credenciales

- [Disposition of content](https://learn.microsoft.com/en-us/purview/disposition) · Documentación · Oficial · Microsoft Learn. Cómo gestionar revisiones de eliminación y prueba de eliminación de registros, permisos (Disposition Management), grupo de seguridad para ver todo y requisitos de auditoría.
- [Expedite the permanent deletion of sensitive information from mailboxes (priority cleanup)](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica la limpieza prioritaria que permite borrar contenido sensible pese a retenciones y holds, con aprobaciones múltiples, simulación, auditoría y diferencias entre Exchange y SharePoint/OneDrive. *Nota:* La página indica 'rolling out in preview'; no aplica a registros ni registros regulatorios; puede desactivarse a nivel de tenant

### Comunidad: blogs, libros, newsletters y eventos

- [MC1183292 - Microsoft Purview | Data Lifecycle Management - Introducing secure priority cleanup workflows for OneDrive/SharePoint](https://mc.merill.net/message/MC1183292) · Newsletter · Oficial · Vista previa · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 6 nov 2025. Mensaje del Centro de mensajes que anuncia flujos de limpieza prioritaria para OneDrive/SharePoint (grabaciones y transcripciones de Teams) con simulación, auditoría y dos administradores. *Nota:* Contradicción: el MC habla de disponibilidad general en GCC (nov-dic 2025) mientras 'What's new' (ago-2026) lo lista como vista previa para SharePoint/OneDrive
- [Retention labels and policies for SharePoint Online (SharePoint Online series, part 14)](https://purview365.com/blog/sharepoint-online-14-retention-labels-policies) · Blog · Comunidad · Nuevo · Adam Crawford · PurviewPro Consultancy (purview365.com) · 30 sep 2026. Guía práctica 2026 sobre biblioteca de conservación, principios de retención, registros regulatorios, revisión de eliminación multietapa (hasta 5 etapas) y la nueva acción de archivo hacia Microsoft 365 Archive (MC1325441).

**Manos a la obra**

1. `Laboratorio` Crea un grupo de seguridad con correo habilitado «Disposition Reviewers» y un grupo de roles personalizado con el rol Disposition Management; asígnalo a dos cuentas de prueba distintas de la del gestor de registros ([eliminación](https://learn.microsoft.com/en-us/purview/disposition)). Evidencia: captura del grupo de roles y de sus miembros.
2. `Laboratorio parcial` Crea una etiqueta «Retener 1 día y luego revisar» con dos etapas (dueño de los datos y Legal), aplícala a cinco documentos de prueba y espera a que lleguen a la página de eliminación. Limitación: los temporizadores pueden tardar hasta 7 días y los revisores deben ser un grupo con correo habilitado. Evidencia: elementos visibles en la primera etapa.
3. `Laboratorio parcial` Ejecuta la revisión: aprueba la eliminación de tres elementos, extiende el período de uno y reetiqueta otro; luego exporta los elementos eliminados como prueba de eliminación. Limitación: depende de los tiempos del paso anterior. Evidencia: CSV exportado y una nota por cada decisión.
4. `Laboratorio` Escribe el procedimiento de revisión: plazos de respuesta, criterios para aprobar, extender o reetiquetar, qué hacer si un elemento está bajo hold y dónde se archiva cada mes la prueba de eliminación. Evidencia: procedimiento revisado por un par y por quien cumpla el papel de Legal en tu equipo.
5. `Laboratorio` Redacta el runbook de limpieza prioritaria: quién la solicita, los tres aprobadores con nombre, la consulta previa a eDiscovery y Legal sobre holds vigentes, la simulación y el seguimiento por su ID en la auditoría ([limpieza prioritaria](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange)). Evidencia: runbook aprobado y ensayado en una mesa de simulación.
6. `Solo producción` Ejecuta una limpieza prioritaria ante un incidente real de datos sensibles en buzones. Cómo hacerlo seguro: prueba primero con un buzón de prueba y solo en simulación, asigna Priority Cleanup Viewer a quienes observan, exige las tres aprobaciones a personas distintas, confirma con Legal que no hay obligación de preservar y, si usas Preservation Lock y no necesitas la limpieza, mantenla desactivada en el tenant. Evidencia: registro de auditoría con el ID de la limpieza y las tres aprobaciones.

**¿Quieres profundizar?**

- [MC1183292 - Microsoft Purview | Data Lifecycle Management - Introducing secure priority cleanup workflows for OneDrive/SharePoint](https://mc.merill.net/message/MC1183292) · Newsletter

<a id="m3"></a>

## M3 · Retención basada en eventos

*L300 · ~3 h · Origen: Ninja oficial de ciclo de vida y registros (2023): retención basada en eventos*

Muchas obligaciones no dicen «cinco años desde la creación», sino «cinco años desde que termina el contrato» o «desde la baja del empleado». La **retención basada en eventos** resuelve ese caso con cuatro piezas: un **tipo de evento** (por ejemplo, fin de contrato), una **etiqueta** cuyo período comienza con ese tipo de evento, un **identificador** que vincula el contenido —el ID de activo (Asset ID) en SharePoint y OneDrive, o palabras clave en Exchange— y el **evento** con su fecha. Cuando lo creas, Purview sincroniza la fecha en hasta siete días.

La trampa está en lo que no ocurre: un elemento con etiqueta basada en eventos cuyo evento nunca se registra se retiene indefinidamente. Por eso la clave es automatizar desde el sistema de origen —recursos humanos, ERP, gestión de contratos— con PowerShell o con Microsoft Graph: la etiqueta usa `retentionTrigger` con el valor `dateOfEvent` asociado a un `retentionEventType`, y el evento se crea con consultas como `AssetID:1234`.

**Por qué importa**

La mayoría de las tablas de retención de recursos humanos, contratos y clientes dependen de eventos. Sin eventos automatizados, esos registros quedan retenidos para siempre (deuda de retención, costo y exposición) o se eliminan en un momento incorrecto. Un flujo de eventos conciliado cada mes es la diferencia entre una tabla de retención en papel y una que se cumple.

**Qué vas a lograr**

- Diseñar tipos de evento, etiquetas e ID de activo para un caso real, como empleados o contratos.
- Disparar un evento desde el portal y verificar el inicio del período de retención.
- Automatizar la creación de eventos desde un sistema de origen.
- Detectar registros con eventos pendientes que quedarían retenidos indefinidamente.

> **Atención.** Un elemento con etiqueta basada en eventos cuyo evento nunca se registra se retiene indefinidamente, y la fecha de un evento se sincroniza en hasta 7 días ([retención por eventos](https://learn.microsoft.com/en-us/purview/event-driven-retention)). Sin un proceso que dispare los eventos, la etiqueta se convierte en deuda de retención.

> **Consejo Ninja.** El evento encuentra el contenido por el ID de activo (Asset ID) en SharePoint y OneDrive, y por palabras clave en Exchange ([retención por eventos](https://learn.microsoft.com/en-us/purview/event-driven-retention)). Acuerda con el sistema de origen un formato único para el identificador, por ejemplo el número de contrato sin espacios, antes de etiquetar el primer documento.

> **Novedad.** En Microsoft Graph v1.0, una etiqueta con `retentionTrigger` igual a `dateOfEvent` se asocia a un `retentionEventType`, y el `retentionEvent` usa `eventQueries` como `AssetID:1234` ([API de registros](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0)). Es la vía para disparar eventos desde recursos humanos o el ERP, que verás en [A2](03_Nivel_3_Avanzado.md#a2).

**¿Tienes poco tiempo?**

- [Start retention when an event occurs](https://learn.microsoft.com/en-us/purview/event-driven-retention) · Documentación
- [Use the Microsoft Graph records management APIs](https://learn.microsoft.com/en-us/graph/api/resources/security-recordsmanagement-overview?view=graph-rest-1.0) · Documentación

### Documentación, cursos y credenciales

- [Start retention when an event occurs](https://learn.microsoft.com/en-us/purview/event-driven-retention) · Documentación · Oficial · Microsoft Learn. Explica la relación entre tipos de evento, etiquetas, eventos e ID de activo (o palabras clave en Exchange), con ejemplos de salida de empleados, contratos y vida de producto y automatización por PowerShell o Graph.

**Manos a la obra**

1. `Laboratorio` Diseña el caso «Fin de contrato»: tipo de evento, etiqueta «Contratos: 10 años desde el fin del contrato» (período ilustrativo), formato del ID de activo y quién dispara el evento en el negocio. Evidencia: ficha de diseño validada por el dueño del proceso.
2. `Laboratorio` Crea el tipo de evento y la etiqueta basada en eventos, sin acción de eliminación por ahora; publícala para el sitio piloto, aplícala a tres documentos y completa su propiedad ID de activo con tres números de contrato distintos ([retención por eventos](https://learn.microsoft.com/en-us/purview/event-driven-retention)). Evidencia: captura de la biblioteca con la etiqueta y el ID de activo.
3. `Laboratorio parcial` Crea el evento en el portal para uno de los contratos (consulta `AssetID:` seguida del número) y verifica después de la sincronización que solo ese documento quedó asociado. Limitación: la sincronización tarda hasta 7 días. Evidencia: estado del evento en el portal y detalle del documento afectado.
4. `Laboratorio parcial` Repite el caso en Exchange: aplica la etiqueta a correos que mencionen el número de contrato y crea el evento con esa palabra clave. Limitación: además de la sincronización, la retención solo se aplica a buzones con al menos 10 MB. Evidencia: estado del evento y lista de correos afectados.
5. `Laboratorio` Concilia: compara la lista de contratos cerrados del sistema de origen (en el laboratorio, una hoja de cálculo) con los eventos creados y detecta los que faltan, que dejarían documentos retenidos indefinidamente. Evidencia: informe de conciliación con acciones.
6. `Solo producción` Conecta la retención por eventos con el sistema real de recursos humanos o de contratos. Cómo hacerlo seguro: empieza con un tipo de evento y una etiqueta de prueba sin acción de eliminación, usa una app con permisos mínimos y valida dos veces el ID de activo antes de disparar cada evento, porque un evento erróneo inicia la cuenta hacia una eliminación. Evidencia: primer lote de eventos conciliado y aprobado por el dueño del proceso.

<a id="m4"></a>

## M4 · Archivo, buzones inactivos e importación

*L300 · ~5 h · Origen: Ampliación de esta edición: funciones heredadas del Ninja de 2023 más archivo, buzones inactivos, PST y Microsoft 365 Archive*

El **buzón de archivo** amplía el espacio del usuario y el **archivo de expansión automática** lo hace crecer hasta 1,5 TB; desde mediados de octubre de 2026, hasta 3 TB para buzones con Microsoft 365 E5, A5 o G5, Purview Suite, F5 Compliance o E7, siempre que el plan Records Management de la licencia siga habilitado. Ojo: se habilita solo con Exchange Online PowerShell, puede tardar hasta 30 días, es irreversible e impide recuperar o restaurar buzones inactivos.

Un **buzón inactivo** conserva el contenido de una persona que dejó la organización sin consumir licencia, pero solo si, antes de eliminar la cuenta, el buzón tenía una directiva con acción de retener (no de solo eliminar) o un hold. Microsoft recomienda la retención de Microsoft 365 frente a Litigation Hold, y desde agosto de 2026 al quitar el último hold se aplica un delay hold de 30 días. Para traer correo histórico, la **importación de PST** por red es gratuita; el envío de discos tiene costo y solo existe con Enterprise Agreement; y **Azure PST Import**, solo por PowerShell desde Azure Blob Storage, entró en vista previa a mediados de octubre de 2026.

En SharePoint, **Microsoft 365 Archive** es un nivel frío para sitios y archivos inactivos que conserva permisos y cumplimiento y que Copilot no usa: cuesta USD 0,05 por GB al mes solo por encima de la cuota del tenant. En 2026 se sumó una acción de retención que mueve archivos al archivo antes de eliminarlos, con fechas de disponibilidad general que difieren según la fuente.

**Por qué importa**

Crecimiento de buzones, salida de empleados y PST heredados son el día a día de los administradores de Exchange, y aquí los errores son caros: un archivo de expansión automática no se puede desactivar y una cuenta eliminada sin retención previa no deja buzón inactivo. Microsoft 365 Archive, bien usado, baja el costo de almacenamiento de SharePoint sin perder cumplimiento.

**Qué vas a lograr**

- Habilitar y gestionar buzones de archivo, y decidir cuándo usar el archivo de expansión automática.
- Preservar buzones de exempleados como inactivos y gestionar sus holds.
- Importar PST por red con filtros y con un rol temporal.
- Evaluar Microsoft 365 Archive y la acción de archivo en retención, con su costo.

> **Novedad.** Desde mediados de octubre de 2026, el archivo de expansión automática llega a 3 TB para buzones con Microsoft 365 E5, A5 o G5, Purview Suite, F5 Compliance o E7, si el plan Records Management de la licencia sigue habilitado ([archivo de expansión automática](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving)); la descripción del servicio aún dice 1,5 TB. Es irreversible, se habilita solo con Exchange Online PowerShell, tarda hasta 30 días e impide recuperar o restaurar buzones inactivos ([habilitarlo](https://learn.microsoft.com/en-us/purview/enable-autoexpanding-archiving)).

> **Qué cambió.** Desde agosto de 2026, al quitar el último hold de un buzón inactivo se aplica automáticamente un delay hold de 30 días ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Un buzón solo pasa a inactivo si, antes de borrar la cuenta, tenía una retención con acción de retener o un hold, y como inactivo no consume licencia ([buzones inactivos](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365)).

> **Novedad.** Azure PST Import (solo PowerShell, desde tu Azure Blob Storage) entró en vista previa a mediados de octubre de 2026, con disponibilidad general anunciada para fines de enero de 2027 ([MC1281505](https://mc.merill.net/message/MC1281505)) o para marzo–abril de 2027 ([MC1455013](https://mc.merill.net/message/MC1455013)). La carga por red sigue sin costo y el envío de discos tiene costo, solo con Enterprise Agreement, con 10 TB por disco y 10 discos por trabajo ([importación de PST](https://learn.microsoft.com/en-us/purview/pst-import-overview)).

> **Atención.** Microsoft 365 Archive cobra USD 0,05 por GB al mes solo por encima de la cuota; la reactivación no tiene cargo desde el 31 de marzo de 2025 (no aplica a OneDrive) y lo reactivado no puede volver a archivarse durante 4 meses ([precios](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide)). Copilot no usa contenido archivado ([Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide)), y la nueva acción de retención que mueve archivos a Archive (MC1325441) puede tardar hasta 10 días en actuar ([Microsoft 365 for IT Pros](https://office365itpros.com/2026/08/20/microsoft-365-archive-retention/)).

**¿Tienes poco tiempo?**

- [Learn about inactive mailboxes](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365) · Documentación
- [Learn about auto-expanding archiving](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving) · Documentación
- [Learn about importing your organization's PST files](https://learn.microsoft.com/en-us/purview/pst-import-overview) · Documentación
- [Overview of Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide) · Documentación

**Archivo, conservación de buzones e importación: qué usar**

| Necesidad | Opción | Licencia o costo | ¿Reversible? | Fuente |
|---|---|---|---|---|
| Buzones que superan el archivo estándar | Archivo de expansión automática | Hasta 1,5 TB; 3 TB con Microsoft 365 E5, A5 o G5, Purview Suite, F5 Compliance o E7 desde octubre de 2026 | No: es irreversible | [Archivo de expansión automática](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving) |
| Conservar el correo de quien deja la organización | Buzón inactivo (retención con acción de retener o hold antes de borrar la cuenta) | El buzón inactivo no requiere licencia | Se puede recuperar o restaurar, salvo si tenía archivo de expansión automática | [Buzones inactivos](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365) |
| Traer correo histórico desde PST | Carga por red | Sin costo adicional; rol Mailbox Import Export | No aplica | [Importación de PST](https://learn.microsoft.com/en-us/purview/pst-import-overview) |
| Grandes volúmenes de PST | Envío de discos | Con costo; solo Enterprise Agreement; 10 TB por disco y 10 discos por trabajo | No aplica | [Importación de PST](https://learn.microsoft.com/en-us/purview/pst-import-overview) |
| Importación automatizada desde Azure | Azure PST Import (vista previa, solo PowerShell) | Tu propio Azure Blob Storage; disponibilidad general prevista en 2027 con fechas en conflicto | No aplica | [MC1281505](https://mc.merill.net/message/MC1281505) |
| Sitios y archivos inactivos de SharePoint | Microsoft 365 Archive | USD 0,05 por GB al mes por encima de la cuota (pago por uso) | Sí: reactivación sin cargo desde el 31 de marzo de 2025 (no aplica a OneDrive); no se puede volver a archivar durante 4 meses | [Precios de Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide) |

Datos al 6 de noviembre de 2026. La descripción del servicio aún indica 1,5 TB para el archivo de expansión automática: ver [puntos a confirmar](08_Cierre_glosario_y_fuentes.md#metodologia).

### Documentación, cursos y credenciales

- [Pricing model for Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-pricing?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Modelo de precio de Microsoft 365 Archive: USD 0,05/GB/mes solo por encima de la cuota de SharePoint del tenant, sin tarifa de reactivación desde el 31-mar-2025 y con calculadora de costos.
- [Learn about auto-expanding archiving](https://learn.microsoft.com/en-us/purview/autoexpanding-archiving) · Documentación · Oficial · Microsoft Learn. Explica el archivo de expansión automática (de 100 GB hasta 1,5 TB) y anuncia el aumento a 3 TB para buzones con licencias E5/Purview Suite/E7 desde mediados de octubre de 2026.
- [Enable auto-expanding archiving](https://learn.microsoft.com/en-us/purview/enable-autoexpanding-archiving) · Documentación · Oficial · Microsoft Learn. Procedimiento con Exchange Online PowerShell (Set-OrganizationConfig -AutoExpandingArchive) y restricciones: irreversible, sin ajuste de cuota y sin poder recuperar/restaurar buzones inactivos con archivo expandido.
- [Learn about importing your organization's PST files](https://learn.microsoft.com/en-us/purview/pst-import-overview) · Documentación · Oficial · Microsoft Learn. Compara carga por red (gratuita, incluye región México y Brasil) y envío de discos (con costo, solo EA, 10 TB por disco) para importar PST a Exchange Online, con roles requeridos y filtros de importación inteligente.
- [Learn about inactive mailboxes](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365) · Documentación · Oficial · Microsoft Learn. Explica cómo un buzón con retención o hold se convierte en inactivo al eliminar la cuenta, por qué preferir retención de Microsoft 365 frente a Litigation Hold y cómo actúa la retención diferida (delay hold).
- [Overview of Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-overview?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Describe Microsoft 365 Archive como nivel frío dentro de SharePoint para sitios y archivos inactivos, que conserva búsqueda, permisos y cumplimiento (retención, eDiscovery) y no es usado por Copilot.
- [Create and manage inactive mailboxes](https://learn.microsoft.com/en-us/purview/create-and-manage-inactive-mailboxes) · Documentación · Oficial · Microsoft Learn. Pasos para crear, listar (hasta 5.000 en portal), buscar, recuperar, restaurar y eliminar buzones inactivos, con escenarios de retención indefinida o temporal.
- [Manage Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-manage?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn. Cómo archivar sitios y archivos, controlar el archivado manual por PowerShell (AllowFileArchive) y entender que retención y eDiscovery siguen aplicando a contenido archivado.

### Laboratorios, GitHub y herramientas

- [Microsoft 365 Archive | SharePoint Cold Data Storage](https://www.microsoft.com/en-us/microsoft-365/microsoft-365-archive) · Herramienta · Oficial. Página de producto con precio pago por uso (USD 0,05/GB), diferencias con SharePoint Advanced Management y preguntas frecuentes (holds legales, búsqueda y archivado por archivo).

### Comunidad: blogs, libros, newsletters y eventos

- [New Archiving Capability for Purview Data Lifecycle Management](https://office365itpros.com/2026/08/20/microsoft-365-archive-retention/) · Blog · MVP · Vista previa · Nuevo · Tony Redmond · Microsoft 365 for IT Pros (office365itpros.com) · 20 ago 2026. Analiza MC1325441: directivas y etiquetas de retención pueden mover archivos de SharePoint/OneDrive a Microsoft 365 Archive como paso intermedio antes de la eliminación (vista previa con GA prevista para fin de septiembre de 2026). *Nota:* Requiere Microsoft 365 Archive configurado con facturación; puede tardar hasta 10 días en actuar. Estado GA no confirmado en Learn
- [MC1281505 - Microsoft Purview: Data Lifecycle Management - Azure PST Import](https://mc.merill.net/message/MC1281505) · Newsletter · Oficial · Vista previa · Nuevo · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 22 oct 2026. Anuncia Azure PST Import, flujo solo por PowerShell que importa PST desde Azure Blob Storage con análisis previo, informes y auditoría; vista previa desde mediados de octubre de 2026 y despliegue mundial desde fines de enero de 2027. *Nota:* Contradicción de fechas: MC1455013 (mismo tema) indica despliegue global desde fines de marzo de 2027
- [MC1455013 - Microsoft Purview: Data Lifecycle Management - Azure PST Import](https://mc.merill.net/message/MC1455013) · Newsletter · Oficial · Vista previa · Nuevo · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 22 oct 2026. Segundo mensaje sobre Azure PST Import que retrasa el despliegue global a fines de marzo-abril de 2027 y detalla prerrequisitos (rol Storage Blob Data Reader, modo Analyze, validación de cuotas). *Nota:* Fechas en conflicto con MC1281505; confirmar en el Centro de mensajes del tenant

**Manos a la obra**

1. `Laboratorio` Habilita el buzón de archivo de un usuario de prueba con `Enable-Mailbox -Identity ana@contoso.com -Archive`, mueve correos al archivo desde Outlook en la web y verifica el estado con `Get-Mailbox -Identity ana@contoso.com | Format-List ArchiveStatus`. Evidencia: salida de ambos cmdlets.
2. `Laboratorio` Crea un buzón inactivo: siembra al menos 10 MB de correo en el buzón de un usuario de prueba, aplícale una directiva de solo retener, verifica la retención con `Get-Mailbox -Identity luis@contoso.com | Format-List InPlaceHolds`, elimina la cuenta y confirma el resultado con `Get-Mailbox -InactiveMailboxOnly` ([crear y administrar buzones inactivos](https://learn.microsoft.com/en-us/purview/create-and-manage-inactive-mailboxes)). Evidencia: salidas antes y después de eliminar la cuenta.
3. `Laboratorio` Contraste: elimina otra cuenta de prueba cuyo buzón solo tenía una directiva de solo eliminar y comprueba que no aparece como buzón inactivo ([buzones inactivos](https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365)). Evidencia: salida de `Get-Mailbox -InactiveMailboxOnly` y una nota que explique la diferencia.
4. `Laboratorio parcial` Importa un PST pequeño por red a un buzón de prueba: asigna temporalmente el rol Mailbox Import Export, usa los filtros de importación y retira el rol al terminar ([importación de PST](https://learn.microsoft.com/en-us/purview/pst-import-overview)). Limitación: el envío de discos no es practicable (solo con Enterprise Agreement y con costo) y Azure PST Import está en vista previa. Evidencia: trabajo de importación completado y retiro del rol.
5. `Laboratorio parcial` Con el pago por uso habilitado, archiva en Microsoft 365 Archive un sitio inactivo de prueba y reactívalo; anota los tiempos y el costo esperado según la cuota de tu tenant ([administrar Microsoft 365 Archive](https://learn.microsoft.com/en-us/microsoft-365/archive/archive-manage?view=o365-worldwide)). Limitación: requiere pago por uso, solo cobra por encima de la cuota y lo reactivado no puede volver a archivarse durante 4 meses. Evidencia: capturas del sitio archivado y reactivado y la estimación de costo.
6. `Solo producción` Habilita el archivo de expansión automática para los buzones que lo necesiten. Cómo hacerlo seguro: es irreversible y solo actúa cuando el archivo supera unos 90 GB, así que haz un piloto con usuarios aprobados por escrito, verifica las licencias si esperas 3 TB, actívalo por usuario con `Enable-Mailbox -Identity ana@contoso.com -AutoExpandingArchive` y nunca para toda la organización ([habilitarlo](https://learn.microsoft.com/en-us/purview/enable-autoexpanding-archiving)). Evidencia: lista de aprobados y verificación por PowerShell.
7. `Laboratorio` Con la tabla de este módulo, decide qué opción usarías en tres casos de tu organización —exempleado de un área regulada, PST heredados de una adquisición y sitios de proyectos cerrados— con su costo y su reversibilidad. Evidencia: ficha de decisión revisada por el administrador de Exchange y por el gestor de registros.

**¿Quieres profundizar?**

- [New Archiving Capability for Purview Data Lifecycle Management](https://office365itpros.com/2026/08/20/microsoft-365-archive-retention/) · Blog
- [MC1281505 - Microsoft Purview: Data Lifecycle Management - Azure PST Import](https://mc.merill.net/message/MC1281505) · Newsletter
- [Microsoft 365 Archive | SharePoint Cold Data Storage](https://www.microsoft.com/en-us/microsoft-365/microsoft-365-archive) · Herramienta

<a id="reto-intermedio"></a>

## Reto del nivel

**Ciclo de vida completo de un contrato.** En tu laboratorio, y con un período de prueba de 1 día, recorre un registro de punta a punta y documenta la evidencia de cada paso: (1) una etiqueta basada en el evento «Fin de contrato» con revisión de eliminación en dos etapas; (2) su aplicación automática simulada con una consulta KQL y después activada sobre el sitio piloto; (3) el evento disparado para un contrato y la verificación de que solo afecta a ese contrato; (4) la revisión ejecutada y la prueba de eliminación exportada; y (5) en paralelo, el buzón inactivo de un exempleado de prueba y una decisión documentada sobre Microsoft 365 Archive para los sitios de proyectos cerrados. Entregable: informe de 3 a 5 páginas con capturas, tiempos reales observados y lecciones aprendidas.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué licencia NO figura en la fila de la descripción del servicio para autoaplicar etiquetas de retención con clasificadores entrenables?
   - a) Microsoft 365 E5
   - b) E5 Information Protection & Governance
   - c) Microsoft Purview Suite
   - d) Office 365 E5

2. La simulación de una directiva de autoaplicación de etiquetas de retención admite…
   - a) SIT y consultas por palabras clave o propiedades
   - b) Solo clasificadores entrenables
   - c) Etiquetas predeterminadas de SharePoint
   - d) Etiquetas de registro regulatorio

3. ¿Cuánto pueden tardar las etiquetas de retención publicadas en aparecer en Exchange?
   - a) Una hora
   - b) Hasta 7 días
   - c) Exactamente 24 horas
   - d) 30 días

4. ¿Qué etiqueta NO puede aplicarse con una directiva de autoaplicación?
   - a) Una etiqueta de solo retener
   - b) Una etiqueta de solo eliminar
   - c) Una etiqueta de registro regulatorio
   - d) Una etiqueta que retiene y luego elimina

5. En la autoaplicación de etiquetas de retención, KQL significa…
   - a) Keyword Query Language, el lenguaje de búsqueda de Microsoft 365
   - b) Kusto Query Language, el lenguaje de Sentinel
   - c) Knowledge Query Layer, una función de Copilot
   - d) Una lista de palabras clave sin sintaxis

6. ¿Tiene el administrador global el rol Disposition Management por defecto?
   - a) Sí, siempre
   - b) Solo si tiene licencia E5
   - c) Solo si activa su rol con PIM
   - d) No: debe asignarse de forma explícita

7. ¿Qué NO puede eliminar la limpieza prioritaria de buzones?
   - a) Correo bajo un hold de eDiscovery
   - b) Registros y registros regulatorios
   - c) Correo con una directiva de retención
   - d) Correo bajo Preservation Lock

8. Desde julio de 2026, ¿cuántas aprobaciones separadas requiere la limpieza prioritaria de buzones?
   - a) Una
   - b) Dos
   - c) Tres
   - d) Cuatro

9. ¿Cómo obtienes la prueba de eliminación?
   - a) Desde la papelera de reciclaje del sitio
   - b) Con un informe de Compliance Manager
   - c) Desde el explorador de actividad
   - d) Exportando los elementos eliminados desde la página de eliminación

10. En la retención basada en eventos, ¿qué identifica los correos de Exchange afectados por un evento?
   - a) El ID de activo
   - b) Palabras clave
   - c) Una etiqueta de confidencialidad
   - d) La fecha de creación

11. ¿Qué ocurre con un elemento con etiqueta basada en eventos cuyo evento nunca se crea?
   - a) Se elimina a los 7 días
   - b) Pierde la etiqueta
   - c) Se retiene indefinidamente
   - d) Se convierte en registro regulatorio

12. ¿Qué es cierto del archivo de expansión automática?
   - a) Es irreversible y se habilita con Exchange Online PowerShell
   - b) Se desactiva desde el centro de administración de Exchange
   - c) Se habilita desde el portal de Purview
   - d) Siempre ofrece 3 TB

13. ¿Qué configuración previa NO convierte un buzón en inactivo al eliminar la cuenta?
   - a) Una directiva de solo retener
   - b) Una directiva de retener y luego eliminar
   - c) Litigation Hold
   - d) Una directiva de solo eliminar

14. ¿Cuándo cobra Microsoft 365 Archive?
   - a) Por cada usuario licenciado
   - b) Solo por el almacenamiento archivado que supera la cuota, a USD 0,05 por GB al mes
   - c) Cada vez que se reactiva un sitio
   - d) Siempre, desde el primer GB

15. Desde agosto de 2026, ¿qué ocurre al quitar el último hold de un buzón inactivo?
   - a) Se elimina de inmediato
   - b) Pasa a ser un buzón compartido
   - c) Se aplica automáticamente un delay hold de 30 días
   - d) Se exporta a un PST

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

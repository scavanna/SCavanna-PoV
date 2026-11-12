# Nivel 2 · Intermedio · Preservar, revisar, investigar y producir

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Retenciones legales y custodios, conjuntos de revisión y analítica, auditoría forense para investigaciones de seguridad y exportación con cadena de custodia. Terminas con un asunto simulado de punta a punta y su expediente de evidencia.

*L300 · 4 módulos · ~21 horas · 22 recursos*

**Módulos de este nivel:** [M1 Holds y custodios](#m1) · [M2 Review sets y analítica](#m2) · [M3 Audit para investigaciones](#m3) · [M4 Exportación y custodia](#m4)

<a id="m1"></a>

## M1 · Retenciones legales y custodios

*L300 · ~5 h · Origen: Ninja de Advanced eDiscovery (2021): Identification y Preservation; Ninja oficial de eDiscovery (2026): retenciones*

La preservación es la obligación que más riesgo legal concentra: cuando se anticipa un litigio o una investigación, la organización debe evitar que la información pertinente se modifique o elimine. En eDiscovery lo haces con **políticas de hold** dentro de un caso —infinitas, por consulta o por rango de fechas— sobre buzones, sitios, grupos y equipos de Teams. Dos detalles operativos cambian procedimientos: un hold puede tardar hasta 24 horas en aplicarse, y la membresía de un grupo se toma como instantánea al crear la política, de modo que quien se suma después no queda retenido.

Los holds conviven con las políticas de retención de Purview: retener gana sobre eliminar, y un hold suspende incluso la eliminación de contenido de Teams, Viva Engage y Copilot que espera en SubstrateHolds. También tienen límites —hasta 2.000 buzones y 2.000 sitios por hold de caso con funciones premium— y efectos colaterales, como que liberar el único hold de un buzón inactivo lo elimina o que la cuota de Elementos recuperables crece. El módulo cierra con las **notificaciones** a custodios y los issuing officers, documentados para la experiencia premium, cuya ubicación en el portal unificado conviene confirmar.

**Por qué importa**

Una preservación tardía o incompleta puede derivar en sanciones, pérdida de credibilidad ante un tribunal o un regulador y costos de reconstrucción. Un proceso de holds con tiempos medidos, alcance verificado y liberación documentada convierte una obligación legal en un procedimiento repetible y auditable, y evita retener de más, lo que también tiene costo y riesgo de privacidad.

**Qué vas a lograr**

- Crear holds infinitos, por consulta y por rango de fechas, y verificar cuándo se hacen efectivos.
- Explicar el efecto de la instantánea de membresía de grupos y cómo compensarlo.
- Aplicar los límites de holds por caso y por organización al diseñar un asunto grande.
- Coordinar holds con políticas de retención, buzones inactivos y canales privados de Teams.
- Diseñar con Legal el flujo de notificación, recordatorio y liberación a custodios.

> **Atención.** Un hold puede tardar hasta 24 horas en aplicarse y la membresía de un grupo se toma como instantánea al crear la política: quien se suma después no queda retenido. F1 y F3 no incluyen derechos para ser objeto de hold, y los holds por consulta, por fechas o por custodio requieren capacidades premium ([crear holds](https://learn.microsoft.com/en-us/purview/edisc-hold-create)).

> **Consejo Ninja.** Con un hold, la cuota de Elementos recuperables pasa de 30 a 100 GB y puede llenarse si el archivo no está habilitado ([cuota de Elementos recuperables](https://learn.microsoft.com/en-us/purview/edisc-hold-increase-recoverable-item-quota)). Y si un hold de eDiscovery es lo único que mantiene un buzón inactivo, liberarlo o cerrar el caso elimina ese buzón ([buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)).

> **Qué cambió.** Canales privados de Teams: con el modelo de cumplimiento basado en grupos (septiembre de 2025), las versiones retenidas antes de la migración no se trasladan y quedan en los buzones de los usuarios. Revisa el alcance de búsquedas y holds de los asuntos abiertos ([Tech Community](https://techcommunity.microsoft.com/blog/microsoft-security-blog/teams-private-channels-group-based-compliance-model--purview-ediscovery-consider/4457229)).

> **Atención.** Las notificaciones de retención legal (emisión, reemisión, liberación, recordatorios y escalamiento) y los issuing officers, con un máximo de 15 por organización, están documentados para eDiscovery (Premium) con aviso de retiro del clásico. Confirma su ubicación en el portal unificado antes de escribir el procedimiento ([comunicaciones](https://learn.microsoft.com/th-th/purview/ediscovery-managing-custodian-communications?view=o365-worldwide), [issuing officers](https://learn.microsoft.com/en-au/purview/ediscovery-issuing-officers?view=o365-worldwide), [eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/)).

**¿Tienes poco tiempo?**

- [Create holds in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Documentación
- [Limits in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Documentación
- [New Purview eDiscovery Portal – eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/) · Blog

**Límites de eDiscovery para planificar un asunto**

| Límite | Funciones estándar | Funciones premium | Implicancia práctica |
|---|---|---|---|
| Casos por organización | 10.000 | 50.000 | Política de cierre y depuración de casos |
| Políticas de hold por organización | 10.000 | 20.000 | Inventario de holds con dueño y fecha de revisión |
| Políticas de hold por caso | 100 | 200 | Agrupa custodios por política |
| Buzones por hold de caso | 1.000 | 2.000 | Divide asuntos grandes en varias políticas |
| Sitios por hold de caso | 1.000 | 2.000 | Igual que los buzones |
| Listas de distribución como origen | No se aceptan con más de 100 miembros | Igual | Usa la lista de personas o grupos de Microsoft 365 |
| Búsquedas, holds y exportaciones por caso | Recomendación: hasta 1.000 | Igual | Recomendación de rendimiento, no un límite duro |
| Documentos por caso en review sets | No aplica | 40 millones | Planifica varios casos si el volumen lo supera |
| Tamaño y cantidad de review sets | No aplica | 1 TB por review set y 100 por caso | Agrega por lotes y por custodio |
| Etiquetas únicas por caso | No aplica | 1.000 | Un panel de etiquetas corto y estable |
| Exportación por búsqueda y por día | 2 TB | 5 TB | Calendario de lotes |
| Ítems por exportación | 500.000 | 500.000 | Divide producciones grandes |
| Formato y velocidad de exportación | PST de hasta 10 GB, paquetes de 40 GB y 2 GB por hora por buzón | Igual | Estima tiempos antes de comprometer fechas |
| Duración de una exportación | Se cancela si supera siete días | Igual | Lotes que terminen antes del plazo |

Fuente: [Limits in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-ref-limits). Revísala antes de cada asunto grande: los límites cambian.

### Documentación, cursos y credenciales

- [Create holds in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Documentación · Oficial · Microsoft Learn. Cómo crear políticas de hold (infinitas, por consulta o por rango de fechas), que pueden tardar hasta 24 h, y que la membresía de grupos se captura como instantánea al crear la política.
- [Limits in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Documentación · Oficial · Microsoft Learn. Tabla de límites de casos, holds, review sets, exportación, indexación y purga, diferenciando funciones estándar y premium.
- [Work with communications in eDiscovery (Premium)](https://learn.microsoft.com/th-th/purview/ediscovery-managing-custodian-communications?view=o365-worldwide) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 8 ene 2025. Describe el flujo de notificaciones de retención legal (emisión, reemisión, liberación, recordatorios y escalamientos) a custodios. *Nota:* Página marcada como aplicable a la experiencia clásica; verificar disponibilidad de comunicaciones en la experiencia unificada (eDJ menciona biblioteca de comunicaciones y Issuing officer en la configuración)
- [Manage issuing officers in eDiscovery (Premium)](https://learn.microsoft.com/en-au/purview/ediscovery-issuing-officers?view=o365-worldwide) · Documentación · Oficial · Legado aún útil · Microsoft Learn · 2 sep 2025. Explica el rol de "issuing officer" en avisos de hold y el máximo de 15 issuing officers a nivel organización. *Nota:* Lleva el aviso de retiro del clásico (31-ago-2025)

### Comunidad: blogs, libros, newsletters y eventos

- [New Purview eDiscovery Portal – eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/) · Blog · Comunidad · eDJ · eDiscovery Journal · 5 mar 2026. Análisis práctico del portal nuevo para equipos legales: casos como eje, Content Search en casos dedicados, ajustes de comunicaciones, detección de privilegio y opciones de recolección.

**Manos a la obra**

1. `Laboratorio` En el caso `PRUEBA-002` crea un hold infinito sobre el buzón y el OneDrive de una cuenta de prueba y un hold por consulta (tu consulta de [I3](01_Nivel_1_Inicial.md#i3)) sobre un equipo de Teams. Anota la hora de creación y revisa el estado hasta que el hold quede efectivo. Evidencia: línea de tiempo con el tiempo hasta efectividad, que puede llegar a 24 horas ([crear holds](https://learn.microsoft.com/en-us/purview/edisc-hold-create)).
2. `Laboratorio` Comprueba la instantánea de membresía: crea un hold sobre un grupo de Microsoft 365, suma después a un nuevo integrante y verifica que su buzón no quedó retenido (por ejemplo, revisando con Exchange Online PowerShell las retenciones aplicadas a ese buzón). Escribe el control compensatorio (actualizar el hold o agregar a la persona como ubicación) y aplícalo. Evidencia: capturas de antes y después.
3. `Laboratorio` Demuestra que el hold preserva: con el buzón retenido, elimina de forma permanente desde Outlook un correo sembrado y encuéntralo después con una búsqueda del caso. Evidencia: captura del resultado y nota sobre por qué el contenido retenido sigue siendo descubrible ([cómo funciona la retención](https://learn.microsoft.com/en-us/purview/retention)).
4. `Laboratorio parcial` Revisa la cuota de Elementos recuperables de un buzón retenido (pasa de 30 a 100 GB) y habilita su archivo. Limitación: en el laboratorio no vas a llenar la cuota; en producción, programa un monitoreo de los buzones con hold y una alerta antes del límite ([cuota de Elementos recuperables](https://learn.microsoft.com/en-us/purview/edisc-hold-increase-recoverable-item-quota)). Evidencia: captura de la cuota y del archivo habilitado.
5. `Laboratorio` Escribe y ejecuta el procedimiento de liberación de `PRUEBA-002`: aprobación escrita de Legal (simulada), verificación de que ningún buzón inactivo dependa solo de ese hold, liberación, registro de la fecha y revisión en la auditoría. Evidencia: lista de verificación firmada ([buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)).
6. `Laboratorio parcial` Busca en la configuración del portal unificado las comunicaciones a custodios y los issuing officers. Si existen, redacta un aviso de retención con acuse, recordatorio y liberación; si no, documenta la alternativa manual (correo de Legal con acuse de recibo). Limitación: su disponibilidad en la experiencia unificada no está confirmada y no debes enviar avisos a personas reales ([análisis de eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/)). Evidencia: plantilla del aviso o informe de la brecha.
7. `Solo producción` Diseña el hold de un asunto con miles de custodios: calcula cuántas políticas necesitas con 1.000 o 2.000 buzones y sitios por hold, 100 o 200 holds por caso y la exclusión de listas de distribución de más de 100 miembros ([límites](https://learn.microsoft.com/en-us/purview/edisc-ref-limits)). Cómo hacerlo seguro: revisión con un rol de solo lectura, piloto sobre un grupo pequeño con aprobación de Legal y procedimiento de liberación documentado. Evidencia: plan de holds y resultado del piloto.

<a id="m2"></a>

## M2 · Conjuntos de revisión y analítica

*L300 · ~6 h · Origen: Ninja de Advanced eDiscovery (2021): Review & Analysis; Ninja oficial de eDiscovery (2026): review sets y analítica*

El **conjunto de revisión** (review set) es donde la búsqueda se convierte en evidencia analizable. Al agregar resultados, la búsqueda se vuelve a ejecutar, los ítems se copian a un almacenamiento de Azure gestionado por Microsoft para ese caso y se reindexan; si hay adjuntos cifrados, hace falta el rol RMS Decrypt. El review set es estático: no se pueden borrar ítems ni conjuntos, salvo eliminando el caso completo, lo que tiene implicancias directas para la cadena de custodia.

Dentro del review set agrupas por familias y conversaciones; revisas con visores de origen, texto, anotación, metadatos y actividad de Copilot; etiquetas, redactas y filtras con el generador de condiciones, load sets, KeyQL o el **explorador avanzado** con KQL (vista previa). La **analítica** detecta casi duplicados, reconstruye hilos de correo y agrupa por temas, y ofrece consultas automáticas como «For Review – Unique items only» (vista previa). Security Copilot puede resumir ítems. La codificación predictiva sigue documentada en vista previa: trátala como no confirmada.

**Por qué importa**

La revisión es la etapa más cara de un asunto: buena parte del presupuesto de eDiscovery se va en horas de personas leyendo documentos. Deduplicar, agrupar por hilos y priorizar con analítica reduce el volumen que alguien debe leer, acelera la respuesta a Legal y mejora la consistencia del etiquetado entre revisores.

**Qué vas a lograr**

- Agregar resultados a un review set y explicar qué ocurre con los ítems, el almacenamiento y el cifrado.
- Ejecutar la analítica y usar las consultas For Review y de ítems potencialmente irrelevantes.
- Organizar la revisión con etiquetas, agrupación por familias y conversaciones, y consultas guardadas.
- Consultar el review set con KQL en el explorador avanzado y comparar con KeyQL.
- Aplicar los límites de los review sets al planificar un asunto.

> **Atención.** Un review set no se puede depurar: no se borran ítems ni conjuntos, salvo eliminando el caso completo ([administrar review sets](https://learn.microsoft.com/en-us/purview/edisc-review-set-manage)). Agrega solo lo que la consulta justifica y nunca mezcles práctica con asuntos reales en el mismo caso.

> **Novedad.** En vista previa: el explorador avanzado ejecuta un subconjunto de KQL sobre `ReviewSetTable` para filtrar, agregar y graficar ([explorador avanzado](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer)), y la consulta automática «For Review – Unique items only» acompaña a la analítica de casi duplicados, hilos y temas ([analítica](https://learn.microsoft.com/en-us/purview/edisc-review-set-analytics)).

> **Atención.** Codificación predictiva: «Learn about eDiscovery» la menciona, pero sus artículos siguen en vista previa (rondas de 50 ítems y un mínimo de 2.000) y con el aviso de retiro del clásico ([codificación predictiva](https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-overview?redirectSourcePath=%252fde-de%252farticle%252ftagging-and-assessment-b5c82de7-ed2f-4cc6-becd-db403faf4d18&view=o365-worldwide)). No la incluyas en un procedimiento hasta confirmarla en tu tenant.

> **Consejo Ninja.** Planifica con los límites: 40 millones de documentos por caso, 1 TB por review set, 100 review sets por caso y 1.000 etiquetas únicas por caso ([límites](https://learn.microsoft.com/en-us/purview/edisc-ref-limits)). Los conteos del generador de condiciones son estimados y cada página muestra hasta 1.000 ítems ([buscar en un review set](https://learn.microsoft.com/en-us/purview/edisc-review-set-search)).

**¿Tienes poco tiempo?**

- [Add search results to a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Documentación
- [Analyze data in a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-analytics) · Documentación
- [Group and view items in a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-view) · Documentación
- [eDiscovery New User Experience for Premium (webinar)](https://www.youtube.com/watch?v=EUrJy_oGXfw) · Webinar

### Documentación, cursos y credenciales

- [Analyze data in a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-analytics) · Documentación · Oficial · Microsoft Learn. Cómo ejecutar analítica (casi duplicados, hilos de correo, temas) y usar las consultas automáticas For Review (preview) y Potentially Immaterial Items.
- [Manage review sets in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-manage) · Documentación · Oficial · Microsoft Learn. Gestión de review sets: no se pueden borrar ítems ni review sets (solo eliminando el caso), paginación, pestaña de KQL avanzado y dashboard (preview).
- [Group and view items in a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-view) · Documentación · Oficial · Microsoft Learn. Opciones de agrupación (familias, conversaciones), visores (source, texto, anotación, metadatos, actividad de Copilot) y resumen de ítems con Security Copilot.
- [Search content in a review set with the query condition builder](https://learn.microsoft.com/en-us/purview/edisc-review-set-search) · Documentación · Oficial · Microsoft Learn. Uso del generador de condiciones, load sets, KeyQL y consultas guardadas para filtrar review sets.
- [Search content in a review set with the Advanced review set explorer (preview)](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer) · Documentación · Oficial · Vista previa · Microsoft Learn. Permite ejecutar un subconjunto de KQL (Kusto) sobre ReviewSetTable para filtrar, agregar y graficar contenido del review set. *Nota:* Puente natural para analistas SOC que ya dominan KQL
- [Predictive coding module for eDiscovery (Premium) (preview)](https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-overview?redirectSourcePath=%252fde-de%252farticle%252ftagging-and-assessment-b5c82de7-ed2f-4cc6-becd-db403faf4d18&view=o365-worldwide) · Documentación · Oficial · Vista previa · Microsoft Learn · 2 sep 2025. Describe la codificación predictiva: modelos entrenados con rondas de 50 ítems, review set mínimo de 2.000 ítems y filtro por puntaje de predicción. *Nota:* Estado incierto en la experiencia unificada: la página lleva el aviso de retiro del clásico, aunque "Learn about eDiscovery" sigue mencionando modelos de predictive coding

### Webinars, videos y podcasts

- [eDiscovery New User Experience for Premium (webinar)](https://www.youtube.com/watch?v=EUrJy_oGXfw) · Webinar · Empleado de Microsoft · Aaron Thorp, John Wirtala, Alastair Sharp · Microsoft Security Community (YouTube) · 4 jun 2025. Webinar oficial sobre la experiencia premium: categorías y reportes, muestras y estadísticas, process manager, agregar a review set, holds y exportaciones.

**Manos a la obra**

1. `Laboratorio` Agrega a un review set de `PRUEBA-003` los resultados de tu consulta de [I3](01_Nivel_1_Inicial.md#i3) y compara el conteo antes y después: la búsqueda se vuelve a ejecutar al agregar. Si sembraste un documento con una etiqueta que cifra, comprueba el resultado sin y con el rol RMS Decrypt. Evidencia: conteos y capturas ([agregar a un review set](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set)).
2. `Laboratorio` Ejecuta la analítica (casi duplicados, hilos de correo y temas) y aplica las consultas automáticas «For Review – Unique items only» (vista previa) y de ítems potencialmente irrelevantes. Calcula cuánto volumen te ahorras frente al total. Evidencia: porcentaje de reducción y captura del panel ([analítica](https://learn.microsoft.com/en-us/purview/edisc-review-set-analytics)).
3. `Laboratorio` Crea un panel de etiquetas (Pertinente, No pertinente, Privilegiado, Requiere redacción), revisa 30 ítems agrupados por familia y por conversación, y guarda dos consultas del review set. Evidencia: conteo por etiqueta y consultas guardadas ([agrupar y ver ítems](https://learn.microsoft.com/en-us/purview/edisc-review-set-view), [buscar en un review set](https://learn.microsoft.com/en-us/purview/edisc-review-set-search)).
4. `Laboratorio` Redacta en el visor de anotaciones los datos personales de dos documentos y déjalos listos para la producción de [M4](#m4). Evidencia: captura de cada redacción y lista de ítems redactados con su justificación.
5. `Laboratorio parcial` En el explorador avanzado, escribe tres consultas KQL sobre `ReviewSetTable` (un filtro, una agregación por remitente y un gráfico por fecha) y repite el filtro con KeyQL. Limitación: la función está en vista previa y puede no estar en todos los tenants ([explorador avanzado](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer)). Evidencia: consultas, resultados y diferencias encontradas.
6. `Laboratorio parcial` Pide a Security Copilot el resumen de tres ítems del review set y compáralo con tu lectura: anota omisiones, errores y lo que sí te ahorró. Limitación: consume SCU y la inclusión aplica a licencias E5 pagadas; en producción, solo en un caso piloto con datos de prueba. Evidencia: tabla de comparación por ítem.

<a id="m3"></a>

## M3 · Audit para investigaciones de seguridad

*L300 · ~6 h · Origen: Módulo de Learn «Investigate threats using audit in Microsoft Defender XDR and Microsoft Purview (Premium)»; ampliado en esta edición*

Para el SOC y los investigadores, la auditoría es la fuente que responde las preguntas de alcance: qué mensajes leyó un atacante, qué buscó en el buzón o en SharePoint, qué reglas creó y desde qué IP. El evento estrella es **MailItemsAccessed**, que forma parte de Audit (Standard) para usuarios E3 y E5 y cubre POP, IMAP, MAPI, EWS, Exchange ActiveSync y REST. Distingue accesos *sync* —registrados por carpeta cuando Outlook de escritorio sincroniza— de accesos *bind*, agregados cada dos minutos con el InternetMessageId de cada mensaje.

En enero de 2025 la CISA publicó un playbook para operacionalizar estos registros ampliados (accesos, envíos y búsquedas) e ingerirlos en Sentinel o Splunk. Microsoft advierte que pueden multiplicar hasta diez veces el volumen del registro de auditoría hacia el SIEM y que SearchQueryInitiated no viene habilitado por defecto. Este módulo combina esas fuentes con la guía de respuesta a cuentas de correo comprometidas (BEC) para pasar de una alerta a un informe de alcance defendible.

**Por qué importa**

En un compromiso de correo, la diferencia entre «el atacante tuvo acceso al buzón» y «el atacante leyó estos 37 mensajes» cambia por completo la conversación sobre notificaciones a reguladores, clientes y titulares. La auditoría bien usada acota el impacto con evidencia, da a Legal un alcance verificable y acelera la contención.

**Qué vas a lograr**

- Interpretar registros MailItemsAccessed de tipo sync y bind y acotar los mensajes accedidos.
- Combinar MailItemsAccessed, envíos, SearchQueryInitiated y cambios de reglas en una línea de tiempo.
- Seguir la guía de respuesta a un BEC con preservación previa a la remediación.
- Planificar la ingesta de los registros ampliados en el SIEM con su impacto de volumen.

> **Novedad.** El 15 de enero de 2025 la CISA publicó el «Microsoft Expanded Cloud Logs Implementation Playbook» para operacionalizar los registros ampliados (accesos a correo, envíos y búsquedas) e ingerirlos en Sentinel o Splunk ([CISA](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook)). La comunidad menciona una revisión de mayo de 2026 que no se confirmó en la fuente oficial.

> **Atención.** Microsoft advierte que los registros ampliados pueden multiplicar hasta 10 veces el volumen del registro de auditoría que llega al SIEM y que SearchQueryInitiated no viene habilitado por defecto ([Tech Community](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661)). Estima el costo antes de habilitar la ingesta completa.

> **Consejo Ninja.** Distingue los dos tipos de acceso de MailItemsAccessed: *sync* se registra por carpeta cuando Outlook de escritorio sincroniza, por lo que no identifica mensajes individuales; *bind* se agrega cada dos minutos e incluye el InternetMessageId de cada mensaje. El evento cubre POP, IMAP, MAPI, EWS, Exchange ActiveSync y REST ([MailItemsAccessed](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts)).

> **Qué cambió.** La guía de MailItemsAccessed todavía usa `Search-UnifiedAuditLog`, que se retira el 15 de octubre de 2027: practica también la misma consulta con AuditLogQuery ([guía](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts), [MC1505599](https://mc.merill.net/message/MC1505599)).

**¿Tienes poco tiempo?**

- [Use MailItemsAccessed to investigate compromised accounts](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Documentación
- [CISA Releases Microsoft Expanded Cloud Logs Implementation Playbook](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook) · Documentación
- [CISA, OMB, ONCD and Microsoft collaborate on new logging playbook for Federal agencies](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661) · Blog oficial

### Documentación, cursos y credenciales

- [Use MailItemsAccessed to investigate compromised accounts](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Documentación · Oficial · Microsoft Learn. Guía forense de MailItemsAccessed: accesos sync (por carpeta, Outlook escritorio) y bind (agregados cada 2 minutos con InternetMessageId) para acotar el alcance de un compromiso.
- [CISA Releases Microsoft Expanded Cloud Logs Implementation Playbook](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook) · Documentación · Comunidad · CISA · 15 ene 2025. Playbook de CISA para operacionalizar los registros ampliados de Audit (Standard) (MailItemsAccessed, envíos, búsquedas en Exchange/SharePoint) e ingerirlos en Sentinel o Splunk.
- [Investigate threats using audit in Microsoft Defender XDR and Microsoft Purview (Premium)](https://learn.microsoft.com/en-us/training/modules/investigate-threats-using-audit-in-microsoft-365-defender-microsoft-purview-premium/) · Curso · Oficial · Microsoft Learn. Módulo (46 min) orientado a analistas SOC sobre Audit (Premium), políticas de retención e investigación de buzones comprometidos.
- [Manage Microsoft Purview Audit (Premium) (MS-101)](https://learn.microsoft.com/en-us/training/modules/manage-microsoft-purview-audit-premium/) · Curso · Oficial · Legado aún útil · Microsoft Learn. Módulo heredado de MS-101 sobre diferencias Standard/Premium, retención y forense de cuentas comprometidas. *Nota:* MS-101 fue reemplazado; el contenido sigue siendo válido conceptualmente

### Anuncios y blogs oficiales

- [CISA, OMB, ONCD and Microsoft collaborate on new logging playbook for Federal agencies](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661) · Blog oficial · Empleado de Microsoft · ckahsen · Microsoft Public Sector Blog · 21 feb 2024. Explica la ampliación de registros en Audit (Standard), su posible aumento de hasta 10x en el volumen del UAL hacia el SIEM y que SearchQueryInitiated no viene habilitado por defecto.

**Manos a la obra**

1. `Laboratorio` Simula un BEC con dos cuentas de prueba: desde la cuenta «comprometida» crea una regla de bandeja de entrada que reenvíe a otra cuenta interna, lee diez mensajes concretos en Outlook en la web, busca «factura» y envía un correo. Anota la hora exacta de cada acción: es tu verdad de referencia ([responder a una cuenta comprometida](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account)).
2. `Laboratorio` Horas después, investiga con la auditoría: la creación de la regla, los accesos `MailItemsAccessed` de tipo bind con sus InternetMessageId, las búsquedas y el envío. Arma una línea de tiempo y compárala con tu verdad de referencia. Evidencia: línea de tiempo y lista de mensajes accedidos ([MailItemsAccessed](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts)).
3. `Laboratorio` Abre el mismo buzón con Outlook de escritorio en la máquina virtual del laboratorio para generar un acceso sync y localiza el registro por carpeta. Escribe qué puedes concluir con un sync y qué no, frente a un bind. Evidencia: los dos registros y tu conclusión en tres líneas.
4. `Laboratorio` Preserva antes de erradicar: mientras contienes la cuenta como indica la guía de respuesta (la contención no espera), aplica un hold al buzón comprometido ([M1](#m1)) y exporta los resultados de auditoría con su hash; recién después elimina la regla y los reenvíos. Evidencia: hold, archivo con hash y lista de verificación con horas.
5. `Laboratorio parcial` Estima el volumen: cuenta los registros de auditoría por usuario y por día de tu laboratorio, extrapola a la plantilla de tu organización y aplica la advertencia de hasta 10 veces más volumen con los registros ampliados ([Tech Community](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661)). Limitación: el laboratorio no tiene tráfico real. Evidencia: estimación de GB por día y costo de ingesta.
6. `Solo producción` Acota una cuenta comprometida real: con Audit Reader asignado por PIM y la justificación en el ticket, determina qué mensajes se accedieron y desde qué IP. Cómo hacerlo seguro: solo metadatos (sin abrir contenido), Legal informado desde el inicio y tus propias búsquedas revisadas después en la auditoría. Evidencia: informe de alcance para Legal.

<a id="m4"></a>

## M4 · Exportación y cadena de custodia

*L300 · ~4 h · Origen: Ninja de Advanced eDiscovery (2021): Production; Ninja oficial de eDiscovery (2026): exportaciones*

La producción es el momento en que la evidencia sale de la plataforma y la cadena de custodia empieza a depender de tu proceso. Hay dos caminos con reglas distintas. La **exportación de resultados de búsqueda** genera paquetes que, desde el 16 de febrero de 2026, expiran a los 14 días; quien exporta necesita licencia E3 o E5, y los archivos restringidos por DLP o en sitios bloqueados no se exportan. La **exportación del review set** se retiene durante la vida del caso, pero debe descargarse dentro de 30 días, y si confirmaste redacciones entrega un PDF `_burn.pdf` en lugar del original.

También cambió la herramienta: desde el 26 de mayo de 2025 no se exporta con `New-ComplianceSearchAction -Export`, y desde el 16 de febrero de 2026 la Content Search se limita a buscar y exportar. Los límites importan al planificar: 2 TB (estándar) o 5 TB (premium) por búsqueda y por día, 500.000 ítems por exportación, archivos PST de hasta 10 GB, y una exportación que dura más de siete días se cancela. Este módulo te deja un procedimiento de exportación con conciliación, hash y registro de custodia.

**Por qué importa**

Una exportación vencida obliga a repetir el trabajo; una exportación sin conciliación ni registro de custodia expone a la organización a impugnaciones sobre la integridad de la evidencia. Un procedimiento estándar con ventanas de 14 y 30 días controladas, verificación de conteos y hash, y responsables definidos protege la defensa del asunto y reduce el riesgo de fuga durante la entrega.

**Qué vas a lograr**

- Diferenciar la exportación de búsquedas de la exportación de review sets: plazos, contenido y redacción.
- Exportar, descargar y conciliar el informe de ítems con las estadísticas dentro de la ventana de 14 días.
- Producir documentos redactados como PDF y verificar que no se entregó el original.
- Registrar la cadena de custodia: quién, cuándo, qué, hash y medio de entrega.
- Aplicar los límites de exportación al dividir producciones grandes.

> **Qué cambió.** Desde el 16 de febrero de 2026, los paquetes de exportación de búsquedas expiran 14 días después de su creación; las exportaciones de review set no cambian ([MC1217141](https://mc.merill.net/message/MC1217141)). Descarga, calcula el hash y registra la custodia dentro de la misma semana.

> **Atención.** Quien exporta necesita licencia E3 o E5 (y la de SharePoint del nivel E3 para contenido de SharePoint). Los archivos restringidos por DLP o en sitios bloqueados no se exportan, la descarga puede registrar eventos `FileAccessed` en la auditoría y la clave del cliente para exportaciones directas está en vista previa ([exportar resultados](https://learn.microsoft.com/en-us/purview/edisc-search-export)).

> **Consejo Ninja.** Las exportaciones de review set se retienen durante la vida del caso, pero hay que descargarlas dentro de 30 días; con redacciones confirmadas se entrega `_burn.pdf` en lugar del nativo ([exportar desde un review set](https://learn.microsoft.com/en-us/purview/edisc-review-set-export)). Límites: 500.000 ítems por exportación, PST de hasta 10 GB, paquetes de 40 GB y cancelación si la exportación supera siete días ([límites](https://learn.microsoft.com/en-us/purview/edisc-ref-limits)).

> **Atención.** La exportación a una cuenta propia de Azure Storage con URL de contenedor y token SAS está documentada para la interfaz de eDiscovery (Premium). Valida que exista una opción equivalente en la experiencia unificada y protege el token como una credencial ([procedimiento](https://learn.microsoft.com/en-us/purview/ediscovery-download-export-jobs)).

**¿Tienes poco tiempo?**

- [Export search results in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-export) · Documentación
- [Export items from a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Documentación
- [MC1217141 - Microsoft Purview eDiscovery | Direct export expiration change](https://mc.merill.net/message/MC1217141) · Documentación

**Relojes del proceso: plazos que vencen**

| Evento | Plazo | Qué hacer | Fuente |
|---|---|---|---|
| Activación de la auditoría en un tenant nuevo | Hasta 60 minutos; los eventos pueden tardar horas en ser buscables | Actívala el día 0 | [Learn](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) |
| Hold recién creado | Hasta 24 horas para aplicarse | Créalo antes de anunciar el asunto y verifica su estado | [Learn](https://learn.microsoft.com/en-us/purview/edisc-hold-create) |
| Retención de Copilot e IA | Temporizador de 1 a 7 días | Verifica por eDiscovery una semana después | [Learn](https://learn.microsoft.com/en-us/purview/retention-policies-copilot) |
| Paquete de exportación de una búsqueda | Expira a los 14 días (desde el 16 de febrero de 2026) | Descarga, hash y custodia en la misma semana | [MC1217141](https://mc.merill.net/message/MC1217141) |
| Exportación de review set | Descarga dentro de 30 días; se retiene durante la vida del caso | Descarga y concilia apenas termine | [Learn](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) |
| Exportación en curso | Se cancela si supera siete días | Divide en lotes | [Learn](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) |
| Resultados de búsquedas de auditoría | Se conservan 30 días | Exporta el CSV al expediente | [Learn](https://learn.microsoft.com/en-us/purview/audit-search) |
| Registros de Audit (Standard) | 180 días | Envía a un SIEM o configura Premium si necesitas más | [Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Registros de Audit (Premium) | Un año por defecto (Exchange, SharePoint, OneDrive y Entra ID) | Políticas personalizadas; 10 años con complemento | [Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) |
| Accesos bind de MailItemsAccessed | Se agregan cada dos minutos | Lee el InternetMessageId de cada mensaje | [Learn](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) |
| Primer blob de la Management Activity API | Hasta 12 horas; sin orden garantizado | Ordena por marca de tiempo en el SIEM | [Learn](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) |
| Search-UnifiedAuditLog | Se retira el 15 de octubre de 2027 | Migra a AuditLogQuery | [MC1505599](https://mc.merill.net/message/MC1505599) |

Imprime esta tabla junto al formulario de custodia: la mayoría de los errores de producción son plazos vencidos.

### Documentación, cursos y credenciales

- [Export search results in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-export) · Documentación · Oficial · Microsoft Learn. Consideraciones de exportación: paquetes que expiran a los 14 días, licencias E3/E5 (y SharePoint E3) del usuario que exporta, archivos restringidos por DLP excluidos, eventos FileAccessed y CMK para exportaciones directas (preview).
- [Export items from a review set in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Documentación · Oficial · Microsoft Learn. Opciones de exportación de review sets (selección, familias y conversaciones asociadas, solo reporte o ítems con reporte, etiquetas, redacción como PDF "burn") y plazo de 30 días para descargar.
- [MC1217141 - Microsoft Purview eDiscovery | Direct export expiration change](https://mc.merill.net/message/MC1217141) · Documentación · Oficial · Message Center (archivo mc.merill.net) · 13 ene 2026. Desde el 16-feb-2026 los paquetes de exportación directa expiran 14 días después de su creación; no afecta exportaciones de review sets.
- [Export documents in a review set to an Azure Storage account](https://learn.microsoft.com/en-us/purview/ediscovery-download-export-jobs) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Procedimiento para exportar documentos de un review set a una cuenta de Azure Storage propia mediante URL de contenedor y token SAS, y descargarlos con Azure Storage Explorer. *Nota:* Redactado para la UI de eDiscovery (Premium); confirmar opciones equivalentes en la experiencia unificada y proteger el token SAS

### Comunidad: blogs, libros, newsletters y eventos

- [Purview eDiscovery Simplifies Content Searches in Feb 2026](https://office365itpros.com/2026/01/15/content-searches-change/) · Blog · MVP · Tony Redmond · Office 365 for IT Pros · 15 ene 2026. Explica MC1216266 (content searches reducidas a buscar y exportar desde el 16-feb-2026) y MC1217141 (expiración de 14 días), con recomendaciones de exportar cuanto antes.

**Manos a la obra**

1. `Laboratorio` Exporta los resultados de la búsqueda de `PRUEBA-001`, descárgalos el mismo día, calcula el hash SHA-256 del paquete (por ejemplo, con `Get-FileHash`) y concilia el informe de ítems con las estadísticas. Registra fecha y hora UTC, responsable y hash antes de que venza la ventana de 14 días ([exportar resultados](https://learn.microsoft.com/en-us/purview/edisc-search-export)). Evidencia: formulario de custodia con la conciliación.
2. `Laboratorio` Exporta desde el review set de [M2](#m2) los ítems pertinentes con sus redacciones y verifica que los documentos redactados llegan como `_burn.pdf` y sin el nativo. Evidencia: listado de archivos y del informe de exportación ([exportar desde un review set](https://learn.microsoft.com/en-us/purview/edisc-review-set-export)).
3. `Laboratorio` Busca en la auditoría las huellas de tus exportaciones (actividades de eDiscovery y posibles `FileAccessed`) y anéxalas al expediente: son la prueba de quién exportó y cuándo ([actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)). Evidencia: CSV de la búsqueda.
4. `Laboratorio` Diseña el formulario de cadena de custodia: asunto, solicitante y base de la solicitud, consulta y versión, fecha y hora UTC, responsable, hash, medio de entrega, receptor, vencimiento del paquete (14 o 30 días) y destrucción de copias. Complétalo para las dos exportaciones. Evidencia: formulario lleno y firmado.
5. `Laboratorio` Planifica una producción de 1,2 millones de ítems: divídela en lotes que respeten 500.000 ítems por exportación, 2 o 5 TB por día, PST de 10 GB, paquetes de 40 GB y la cancelación a los siete días ([límites](https://learn.microsoft.com/en-us/purview/edisc-ref-limits)). Evidencia: plan de lotes con calendario.
6. `Solo producción` Entrega una producción real a un tercero (por ejemplo, un estudio jurídico externo). Cómo hacerlo seguro: alcance aprobado por Legal, descarga solo en equipos administrados y cifrados (nunca personales), canal de entrega seguro con acuse, formulario de custodia completo y eliminación verificada de copias intermedias. Evidencia: formulario y acuse del receptor.

**¿Quieres profundizar?**

- [Purview eDiscovery Simplifies Content Searches in Feb 2026](https://office365itpros.com/2026/01/15/content-searches-change/) · Blog

<a id="reto-intermedio"></a>

## Reto del nivel

**Asunto simulado de punta a punta.** Legal pide preservar y producir los correos y chats del «Proyecto Cóndor» de tres custodios, y el SOC sospecha que una de esas cuentas fue comprometida. Entrega el expediente completo: hold efectivo con el tiempo medido y el control de membresía de grupos; review set con analítica, etiquetas y al menos dos redacciones; producción con el `_burn.pdf` verificado, hash SHA-256, conciliación con las estadísticas y formulario de custodia dentro de la ventana de 14 o 30 días; e informe de alcance del compromiso con `MailItemsAccessed` (InternetMessageId de los mensajes accedidos) en una línea de tiempo, preservado antes de erradicar. Cierra con el procedimiento de liberación ejecutado.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuánto puede tardar una política de hold de eDiscovery en aplicarse?
   - a) Hasta una hora
   - b) Hasta 24 horas
   - c) Hasta siete días
   - d) Se aplica al instante

2. Creas un hold sobre un grupo de Microsoft 365 y al día siguiente se suma una persona al grupo. ¿Qué ocurre?
   - a) Queda retenida automáticamente
   - b) Queda retenida solo si tiene E5
   - c) No queda retenida: la membresía se tomó como instantánea al crear la política
   - d) El hold se suspende hasta volver a aplicarlo

3. Con funciones premium, ¿cuántos buzones admite como máximo una política de hold de caso?
   - a) 100
   - b) 1.000
   - c) 10.000
   - d) 2.000

4. Un hold de eDiscovery es lo único que mantiene un buzón inactivo. ¿Qué pasa si liberas el hold o cierras el caso?
   - a) El buzón inactivo se elimina
   - b) El buzón vuelve a estar activo
   - c) El buzón queda retenido 180 días más
   - d) Nada cambia

5. ¿Qué ocurre al agregar los resultados de una búsqueda a un review set?
   - a) Los ítems se mueven fuera del buzón original
   - b) La búsqueda se vuelve a ejecutar y los ítems se copian a almacenamiento de Azure gestionado por Microsoft, donde se reindexan
   - c) Se crea un vínculo a los ítems sin copiarlos
   - d) Se exportan automáticamente a PST

6. ¿Cómo eliminas ítems o un review set completo?
   - a) Desde el menú del review set
   - b) Con el rol Search And Purge
   - c) Esperando 30 días a que expire
   - d) Solo eliminando el caso completo

7. ¿Qué rol necesitas para procesar adjuntos cifrados al agregarlos a un review set?
   - a) Reviewer
   - b) Search And Purge
   - c) Audit Reader
   - d) RMS Decrypt

8. ¿Cada cuánto se agregan los accesos bind de MailItemsAccessed?
   - a) Cada minuto
   - b) Cada cinco minutos
   - c) Cada dos minutos
   - d) Cada hora

9. Según Microsoft, ¿cuánto puede crecer el volumen del registro de auditoría hacia el SIEM con los registros ampliados?
   - a) Hasta 10 veces
   - b) Hasta 2 veces
   - c) Hasta 100 veces
   - d) No cambia

10. ¿Qué evento de búsqueda de Exchange no viene habilitado por defecto y se activa buzón por buzón?
   - a) MailItemsAccessed
   - b) SearchQueryInitiatedExchange
   - c) Send
   - d) FileAccessed

11. En un compromiso de correo, ¿qué conviene hacer antes de eliminar las reglas de reenvío creadas por el atacante?
   - a) Preservar la evidencia: hold sobre el buzón y exportación de la auditoría con hash
   - b) Desactivar la auditoría del buzón para no generar ruido
   - c) Purgar los mensajes que envió el atacante
   - d) Esperar a que la auditoría cumpla 180 días

12. Desde el 16 de febrero de 2026, ¿cuándo expiran los paquetes de exportación de búsquedas?
   - a) A los 7 días
   - b) A los 30 días
   - c) Nunca
   - d) A los 14 días

13. Exportas un review set con redacciones confirmadas. ¿Qué recibe el destinatario por cada documento redactado?
   - a) El nativo y el PDF
   - b) El PDF redactado (_burn.pdf) en lugar del nativo
   - c) Nada: los ítems redactados no se exportan
   - d) Solo el informe de ítems

14. ¿Qué pasa con una exportación que dura más de siete días?
   - a) Se pausa hasta que la reanudes
   - b) Se divide en paquetes de 40 GB
   - c) Se cancela
   - d) Se completa en archivos PST de 10 GB

15. ¿Dentro de qué plazo hay que descargar una exportación de review set?
   - a) 14 días
   - b) 7 días
   - c) 30 días
   - d) 90 días

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

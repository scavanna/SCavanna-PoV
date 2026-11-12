# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Portal, permisos y licencias; clasificación con tipos de información confidencial, EDM y clasificadores; taxonomía y publicación de etiquetas. Terminas con una taxonomía piloto publicada, un SIT propio probado y el mapa de licencias de tu organización.

*L100–L200 · 5 módulos · ~19 horas · 34 recursos*

**Módulos de este nivel:** [P0 Portal, permisos y facturación](#p0) · [I0 Cómo aprender](#i0) · [I1 Qué incluye E3, E5 y E7](#i1) · [I2 Clasificación de datos](#i2) · [I3 Taxonomía y publicación](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, el portal unificado y los permisos

*L100–L200 · ~3 h · Origen: Nuevo en esta edición (la ruta Ninja de Learn asume un nivel L100–L200 en Information Protection y DLP)*

Antes de etiquetar el primer documento conviene dominar el escenario. El **portal de Microsoft Purview** es el lugar único donde se configuran la clasificación de datos, las etiquetas de confidencialidad, la DLP, la retención y el resto de las soluciones de Purview. Llegó a disponibilidad general en julio de 2024 y el portal clásico de cumplimiento se retiró entre noviembre y diciembre de ese año, así que las guías que mencionan el centro de cumplimiento de Microsoft 365 necesitan traducción. También necesitas lo básico de Entra ID (usuarios, grupos y roles), de Exchange Online y de SharePoint y OneDrive, porque las etiquetas viajan con el contenido que vive allí.

El segundo pilar son los **permisos**. Purview usa grupos de roles propios —Information Protection, Information Protection Admins, Analysts, Investigators y Readers, entre otros—, roles de Entra, PIM para grupos y unidades administrativas para delegar por país o por área; el etiquetado admite unidades administrativas en grupos de roles, políticas de etiquetas y políticas de auto-etiquetado. El tercero es la **facturación**: además de las licencias por usuario, algunas capacidades se cobran por uso mediante una suscripción de Azure vinculada al tenant, algo que solo un Global Administrator puede habilitar.

**Por qué importa**

Muchos despliegues de Information Protection fallan por permisos mal asignados o por una facturación que nadie entendía: administradores globales para todo, analistas que leen contenido en los exploradores o pago por uso activado sin presupuesto. Empezar con mínimo privilegio, unidades administrativas y un límite de costos reduce la exposición interna, evita facturas sorpresa y simplifica las auditorías sobre quién cambió qué etiqueta.

**Qué vas a lograr**

- Navegar el portal de Microsoft Purview y ubicar Information Protection, los clasificadores, los exploradores y los informes.
- Diseñar una matriz de roles de mínimo privilegio con los grupos de roles de Information Protection y unidades administrativas.
- Explicar el modelo de licencias por usuario frente al pago por uso y quién puede habilitar este último.
- Preparar un tenant de laboratorio con auditoría activa, personas de prueba y un presupuesto con alertas.

> **Qué cambió.** El portal de Microsoft Purview está en disponibilidad general desde el 2 de julio de 2024 ([MC807798](https://mc.merill.net/message/MC807798)) y el portal clásico de cumplimiento se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 ([MC939918](https://mc.merill.net/message/MC939918)). Si una guía menciona el centro de cumplimiento de Microsoft 365, tradúcela al portal actual y permite sus URL en firewalls y proxies.

> **Atención.** Habilitar el pago por uso exige vincular el tenant a una suscripción y un grupo de recursos de Azure: solo un Global Administrator puede hacerlo, la página está marcada en vista previa y el país o región queda fijo para el tenant ([habilitar pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement)). En Information Protection se cobra por uso el etiquetado de orígenes no Microsoft 365 (activos en el alcance de una política de protección por día) y la clasificación bajo demanda; las experiencias de Microsoft 365 Copilot no se cobran ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)).

> **Consejo Ninja.** Delegación por país o área: las unidades administrativas de Entra se pueden usar en grupos de roles, políticas de etiquetas y políticas de auto-etiquetado, y el explorador de actividades hereda el filtrado ([unidades administrativas](https://learn.microsoft.com/en-us/purview/purview-admin-units)). Los grupos de roles de Exchange Online no comparten membresía con los de Purview ([roles y grupos de roles](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions)).

> **Consejo Ninja.** Para los informes de Information Protection existen roles de lectura (Information Protection Reader y equivalentes) y Microsoft recomienda mínimo privilegio ([informes de postura](https://learn.microsoft.com/en-us/purview/purview-reports)). Ver los grupos de roles requiere Global Administrator o el rol Role Management, que por defecto solo tiene Organization Management ([permisos](https://learn.microsoft.com/en-us/purview/purview-permissions)).

**¿Tienes poco tiempo?**

- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación
- [Administrative units in Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview-admin-units) · Documentación

### Documentación, cursos y credenciales

- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación · Oficial · Microsoft Learn. Explica el modelo RBAC del portal de Purview (roles, grupos de roles, roles de Entra, PIM para grupos, permisos temporales) y enlaza a los permisos por solución.
- [Administrative units in Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview-admin-units) · Documentación · Oficial · Microsoft Learn. Cómo usar unidades administrativas de Entra para delegar por región o departamento en Purview; el etiquetado admite unidades en grupos de roles, políticas de etiquetas y políticas de auto-etiquetado.
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación · Oficial · Microsoft Learn · 6 ene 2026. Explica el modelo por usuario (E3/E5/A5/F5/G5) frente al pago por uso de Purview y lista qué capacidades se facturan por consumo, como etiquetas en orígenes no Microsoft 365 (activos/día), clasificación bajo demanda y seguridad de datos de red e IA.
- [Enable Microsoft Purview pay-as-you-go features via subscription](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement) · Documentación · Oficial · Vista previa · Microsoft Learn · 3 feb 2026. Procedimiento para habilitar las funciones de pago por uso de Purview asociando el tenant a una suscripción y grupo de recursos de Azure (solo un Global Administrator puede hacerlo). *Nota:* La página indica que la característica está en preview; facturación visible en Azure Cost Management; el país/región queda fijo para el tenant
- [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions) · Documentación · Oficial · Microsoft Learn. Tabla de referencia con todos los grupos de roles predeterminados de Purview/Defender for Office 365 y los roles que contiene cada uno.
- [Manage pay-as-you-go and per-user licensing usage](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Documentación · Oficial · Vista previa · Microsoft Learn · 19 nov 2025. Describe el Usage center del portal de Purview para ver consumo de pago por uso por característica y detectar usuarios en alcance de políticas premium sin licencia. *Nota:* Usage center en preview; Information Protection y On-Demand Classification son medidores que se pueden pausar

### Comunidad: blogs, libros, newsletters y eventos

- [MC939918 - Reminder: Microsoft Purview classic compliance portal will retire](https://mc.merill.net/message/MC939918) · Blog · Oficial · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (mc.merill.net) · 22 nov 2024. Aviso del Centro de mensajes: el portal clásico de cumplimiento de Purview se retiró entre el 14-nov y el 14-dic-2024 y toda la configuración pasó con paridad al nuevo portal de Purview.
- [MC807798 - Microsoft Purview: The new Microsoft Purview Portal enters GA](https://mc.merill.net/message/MC807798) · Blog · Oficial · Microsoft (archivado por Merill Fernando) · Microsoft 365 Message Center Archive (mc.merill.net) · 2 jul 2024. Mensaje oficial que anunció la GA del nuevo portal unificado purview.microsoft.com (despliegue jul-sep 2024) y el retiro del portal de cumplimiento clásico a fines de 2024.

**Manos a la obra**

1. `Laboratorio` Prepara el entorno siguiendo [Tu laboratorio](00_Programa.md#laboratorio): prueba de Microsoft 365 E5, diez cuentas de prueba con un atributo común (por ejemplo, PRUEBA-PURVIEW) y un segundo tenant para el invitado externo. Activa la auditoría el día 0, porque en los tenants de prueba viene apagada y tarda hasta 60 minutos ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)). Evidencia: captura del estado de la auditoría y lista de cuentas.
2. `Laboratorio` Recorre el portal de Purview y documenta con capturas dónde están las etiquetas de confidencialidad, los clasificadores (SIT, EDM y clasificadores entrenables), Data explorer, Content explorer (classic), el explorador de actividades y los informes de postura.
3. `Laboratorio` Asigna a tres cuentas de prueba los grupos de roles Information Protection Admins, Information Protection Analysts e Information Protection Readers y documenta qué puede ver y cambiar cada una ([permisos](https://learn.microsoft.com/en-us/purview/purview-permissions), [grupos de roles](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions)). Entrega la matriz de mínimo privilegio.
4. `Laboratorio` Crea una unidad administrativa de Entra para un país, asígnala a un grupo de roles de Information Protection y verifica que la persona delegada solo administra las políticas de etiquetas de su ámbito ([unidades administrativas](https://learn.microsoft.com/en-us/purview/purview-admin-units)).
5. `Laboratorio parcial` Vincula el pago por uso a una suscripción de Azure del mismo tenant, con presupuesto y alertas al 50, 75 y 90 %, y revisa el Usage center ([habilitar pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement), [uso y licencias](https://learn.microsoft.com/en-us/purview/purview-billing-usage)). Limitación: las páginas revisadas no confirman que el crédito de Visual Studio cubra los medidores de Purview; no crees políticas de pago por uso hasta el módulo M3.
6. `Solo producción` Exporta la membresía actual de los grupos de roles de Purview en producción y compárala con tu matriz de mínimo privilegio. Forma segura: usa una cuenta con rol de solo lectura, no cambies nada durante el análisis y propone los ajustes como cambios aprobados, con activación justo a tiempo mediante PIM para grupos.

**¿Quieres profundizar?**

- [MC939918 - Reminder: Microsoft Purview classic compliance portal will retire](https://mc.merill.net/message/MC939918) · Blog

<a id="i0"></a>

## I0 · Cómo aprender y dónde pedir ayuda

*L100 · ~2 h · Origen: Ruta Ninja oficial de Microsoft Learn y otras opciones de aprendizaje*

Este programa es extenso, pero no está solo. El Ninja oficial de Information Protection vive hoy en Microsoft Learn como la ruta **Secure sensitive data with Microsoft Purview Ninja training scenarios**: cinco módulos de nivel intermedio basados en escenarios, con evaluación por módulo e insignia, también en español. Si buscas una credencial formal, el examen **SC-401: Information Security Administrator** mide protección de la información, DLP y retención, y riesgos, alertas y actividades, incluida la protección de los datos que usan los servicios de IA. Para validar tareas concretas en un laboratorio real existe la credencial **Applied Skills SC-5003**, con una ruta de casi cinco horas y un módulo de ejercicios guiados.

Si ya dominas el producto, lo que necesitas es mantenerte al día: la página **What's new in Microsoft Purview**, el blog de Purview en Tech Community, los resúmenes mensuales de Microsoft Security y los archivos públicos del Centro de mensajes son tu radar. Para practicar, los laboratorios oficiales del curso SC-401T00 en GitHub se adaptan a un tenant de prueba propio. Y si tienes un problema puntual, el foro de Data Security de Tech Community y las Purview Lightning Talks suelen responder más rápido que cualquier curso. Este módulo te ayuda a combinar todo en un plan personal.

**Por qué importa**

Un equipo que aprende solo desde el portal repite errores que otros ya documentaron. Alinear el programa con SC-401 y con la ruta Ninja oficial da metas medibles (certificación e insignia), un vocabulario común con el soporte de Microsoft y un tiempo de incorporación más corto para cada administrador nuevo; seguir los canales oficiales de cambios evita diseñar sobre funciones que cambiaron hace semanas.

**Qué vas a lograr**

- Identificar las rutas formales: la ruta Ninja de Learn, el examen SC-401 y la credencial SC-5003.
- Mapear las habilidades medidas de SC-401 a los módulos de esta guía.
- Configurar un radar de novedades con What's new, el blog de Purview y el Centro de mensajes.
- Saber dónde preguntar y cómo escalar una duda técnica.

> **Novedad.** La guía de estudio de SC-401 refleja las habilidades medidas al 28 de octubre de 2026: protección de la información, DLP y retención, y riesgos, alertas y actividades pesan entre 30 y 35 % cada una, e incluyen proteger los datos que usan los servicios de IA. Se aprueba con 700 y la renovación anual en Learn es gratuita ([guía SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)).

> **Atención.** Las versiones traducidas del examen se actualizan unas ocho semanas después de la versión en inglés; si el examen no está en tu idioma puedes pedir 30 minutos adicionales ([guía en español](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-401)).

> **Qué cambió.** El Ninja oficial de Information Protection ya no es un post de Tech Community: desde agosto de 2025 su alias apunta a la ruta de Learn [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/), con evaluación por módulo e insignia, pero sin certificado con nota mínima. Esta guía agrega la evaluación por nivel al 80 %.

> **Consejo Ninja.** Los laboratorios oficiales del curso SC-401T00 recorren desde roles, SIT, etiquetas y cifrado de mensajes hasta DSPM para IA y se adaptan a un tenant de prueba E5 propio ([laboratorios SC-401](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs)). El módulo práctico de la credencial SC-5003 dura cerca de una hora ([ejercicio guiado](https://learn.microsoft.com/en-us/training/modules/purview-exercise-information-protection-data-loss-prevention/)).

**¿Tienes poco tiempo?**

- [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Curso
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial
- [MicrosoftLearning/SC-401T00-Information-Security-Administrator - Labs](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs) · GitHub

### Documentación, cursos y credenciales

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía oficial del examen SC-401 (Information Security Administrator) con habilidades medidas al 28-oct-2026: protección de la información, DLP y retención, y riesgos/alertas/actividades (30-35% cada una), incluido proteger datos usados por servicios de IA.

### Anuncios y blogs oficiales

- [Microsoft Purview Blog (Microsoft Tech Community)](https://techcommunity.microsoft.com/category/microsoft-purview/blog/microsoft-purview-blog) · Blog oficial · Oficial · Equipo de producto de Microsoft Purview · Microsoft Tech Community. Blog oficial del equipo de producto de Purview donde se publican anuncios, guías de despliegue y la serie de webinars y Lightning Talks.

### Laboratorios, GitHub y herramientas

- [MicrosoftLearning/SC-401T00-Information-Security-Administrator - Labs](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs) · GitHub · Oficial · Microsoft Worldwide Learning · GitHub - MicrosoftLearning. Instrucciones oficiales de laboratorio del curso SC-401T00, desde roles, SIT, etiquetas y cifrado de mensajes hasta DSPM para IA, reutilizables como prácticas guiadas del programa.

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio de SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y marca, por cada habilidad del dominio de protección de la información, el módulo de esta guía que la cubre. Entrega la tabla.
2. `Laboratorio` Completa la [ruta Ninja de Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) (cerca de dos horas), guarda la insignia y anota qué módulos son de DLP y se profundizan en el programa de DLP de esta serie.
3. `Laboratorio` Haz el módulo práctico [Implement information protection and data loss prevention with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-exercise-information-protection-data-loss-prevention/) en tu tenant de prueba y guarda capturas del SIT, la etiqueta y la política creados.
4. `Laboratorio` Suscríbete al [blog de Purview](https://techcommunity.microsoft.com/category/microsoft-purview/blog/microsoft-purview-blog) y agenda una revisión mensual de [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new); redacta una nota con tres cambios recientes y su impacto en tu tenant.

<a id="i1"></a>

## I1 · Purview Information Protection hoy y qué incluye Microsoft 365 E5

*L100–L200 · ~3 h · Origen: Prerrequisitos de la ruta Ninja de Learn, ampliados con el licenciamiento de 2026*

Information Protection es la parte de Purview que te ayuda a **conocer y proteger** los datos: conocer con tipos de información confidencial, clasificadores entrenables y exploradores; proteger con etiquetas de confidencialidad que aplican cifrado y marcas, con etiquetas para contenedores, con el cifrado de mensajes, Double Key Encryption, Customer Key, el cliente y el escáner para Windows, el etiquetado en Data Map y el MIP SDK. Junto con la DLP, que se profundiza en otro programa de esta serie, completa el ciclo de prevenir la pérdida de datos. El mapa de capacidades de Microsoft Learn es el mejor punto de partida.

La otra mitad del módulo es el **licenciamiento**. Purview se licencia por beneficio y la descripción del servicio agrupa los derechos de nivel E5 en Microsoft 365 E5, A5 y G5, Microsoft Purview Suite (antes E5 Compliance, renombrado el 1 de octubre de 2025), E5 Information Protection and Governance y Office 365 E5. El mapa indicativo de Microsoft ubica el etiquetado manual y la etiqueta predeterminada en E3, y el auto-etiquetado, EDM, las entidades con nombre, las huellas digitales y los clasificadores entrenables en E5; la clasificación bajo demanda se cobra por uso. Microsoft 365 E7 y Agent 365, disponibles desde el 1 de mayo de 2026, suman Copilot y agentes.

Por último, el arranque cambió: para clientes nuevos con licencia elegible, Purview crea automáticamente etiquetas y políticas predeterminadas, incluidas políticas de auto-etiquetado en cliente y en servicio, y los clientes existentes pueden activarlas desde DSPM. Saber qué crea Microsoft por ti evita duplicar etiquetas y te da una base para el taller de taxonomía del módulo I3.

**Por qué importa**

Los errores de licencias son los más caros en Information Protection: activar auto-etiquetado para personas sin derechos de nivel E5 crea una exposición contractual, y comprar E5 para todos cuando solo algunos equipos se benefician desperdicia presupuesto. Saber exactamente quién se beneficia de cada capacidad permite desplegar por oleadas, justificar Purview Suite sobre E3 y evitar sorpresas con el pago por uso y con Copilot.

**Qué vas a lograr**

- Describir las capacidades de Information Protection para conocer, proteger y prevenir la pérdida de datos.
- Distinguir qué aporta Microsoft 365 E3, qué exige E5 o Purview Suite y qué se cobra por uso o llega con E7 y Agent 365.
- Aplicar la regla de licencias por beneficio a sitios, grupos y canales compartidos.
- Reconocer los nombres vigentes de productos y SKU después de los cambios de 2024 a 2026.

> **Qué cambió.** Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama **Microsoft Purview Suite** y E5 Security pasó a ser Microsoft Defender Suite; E5 Information Protection and Governance conserva su nombre. La fuente es un análisis de partner que conviene contrastar con los Product Terms ([renombres](https://samexpert.com/microsoft-365-defender-purview-renames/)); algunas páginas, como la FAQ de Data Map, todavía dicen «E5 Compliance».

> **Atención.** Licencia por beneficio: necesita licencia cada persona que se beneficia de una capacidad; en ubicaciones compartidas la necesitan propietarios y miembros, no visitantes ni roles de solo lectura ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). El mapa que asigna E3 y E5 a cada característica de etiquetado es indicativo y Microsoft pide confirmarlo en esa descripción ([arquitectura de referencia](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html)).

> **Novedad.** Microsoft 365 E7 y Agent 365 están en disponibilidad general desde el 1 de mayo de 2026 ([anuncios a partners](https://learn.microsoft.com/en-us/partner-center/announcements/)); E7 incluye Microsoft 365 E5, Microsoft 365 Copilot, Entra Suite y Agent 365 ([anuncio](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295)). Según la descripción del servicio, las capacidades de Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra se soportarán con E7 y los SKU de Agent 365.

> **Consejo Ninja.** Los clientes nuevos con licencia elegible reciben etiquetas y políticas predeterminadas, incluidas políticas de auto-etiquetado en cliente y en servicio; los existentes pueden activarlas desde DSPM ([etiquetas predeterminadas](https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies)). Revísalas antes de ampliar: son un punto de partida, no tu taxonomía final.

**¿Tienes poco tiempo?**

- [Protect your sensitive data with Microsoft Purview (Microsoft Purview Information Protection)](https://learn.microsoft.com/en-us/purview/information-protection) · Documentación
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación
- [Microsoft Purview — Classification & Labeling Interactive Reference Architecture](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) · Herramienta
- [Labeling Files is Worth It | Speed & Protection Benefits in Microsoft Purview](https://www.youtube.com/watch?v=Jn09iBRLxqw) · Video

### Documentación, cursos y credenciales

- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn - Service Descriptions. Fuente oficial de licenciamiento de Purview: qué usuarios necesitan licencia y qué planes (M365 E5, Purview Suite, E5 Information Protection and Governance, Office 365 E5, etc.) habilitan cada capacidad de Information Protection.
- [Protect your sensitive data with Microsoft Purview (Microsoft Purview Information Protection)](https://learn.microsoft.com/en-us/purview/information-protection) · Documentación · Oficial · Microsoft Learn. Mapa de capacidades de Information Protection (conocer, proteger y prevenir pérdida de datos): SIT, clasificadores, exploradores, etiquetas, cliente MPIP, DKE, OME, Customer Key, IRM de SharePoint, conector RMS, escáner, MDCA, Data Map y MIP SDK.
- [Partner Center announcements (índice 2025-2026)](https://learn.microsoft.com/en-us/partner-center/announcements/) · Documentación · Oficial · Nuevo · Microsoft Learn - Partner Center · 5 nov 2026. Índice oficial de anuncios a partners que fecha cambios comerciales clave: Microsoft 365 E7 y Agent 365 GA (1-may-2026), deprecación de DLP en Defender for Cloud Apps (6-jul-2026) y descuentos de Purview Suite.
- [Microsoft 365 guidance for security & compliance](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance) · Documentación · Oficial · Nuevo · Microsoft Learn - Service Descriptions · 21 ago 2026. Página índice que remite a las descripciones de servicio consolidadas por familia (Defender, Entra, Intune, Priva y Purview) para evitar acceso sin licencia.

### Webinars, videos y podcasts

- [Labeling Files is Worth It | Speed & Protection Benefits in Microsoft Purview](https://www.youtube.com/watch?v=Jn09iBRLxqw) · Video · Empleado de Microsoft · Jeremy Chapman, Matt McSpirit · Microsoft Mechanics (YouTube). Video oficial de Microsoft Mechanics que demuestra los beneficios de velocidad y protección de etiquetar archivos con Microsoft Purview.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft 365 Security & Compliance Product Renames](https://samexpert.com/microsoft-365-defender-purview-renames/) · Blog · Comunidad · Alexander Golev · SAMexpert · 2 oct 2025. Análisis de licenciamiento del cambio de nombre efectivo el 1-oct-2025: Microsoft 365 E5 Compliance pasa a Microsoft Purview Suite (y E5 Security a Defender Suite), mientras los componentes como E5 Information Protection and Governance conservan su nombre.

**Manos a la obra**

1. `Laboratorio` Lee el [mapa de capacidades de Information Protection](https://learn.microsoft.com/en-us/purview/information-protection) y clasifica cada capacidad en conocer, proteger o prevenir; entrega una tabla de una página con el módulo de esta guía que la cubre.
2. `Laboratorio` Con la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) y la tabla [Licencias](00_Programa.md#licencias), calcula para una empresa de 5.000 personas con Microsoft 365 E3 cuántas licencias de nivel E5 necesita si solo Finanzas y Legal (800 personas) usan auto-etiquetado, y cómo cambia el cálculo si quiere Customer Key para Exchange y Teams.
3. `Laboratorio` Mira el video de Microsoft Mechanics [Labeling Files is Worth It](https://www.youtube.com/watch?v=Jn09iBRLxqw) y redacta tres argumentos de negocio para tu organización, cada uno con la métrica que lo demostraría.
4. `Laboratorio` Revisa la [arquitectura de referencia interactiva](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) y marca qué capacidades aparecen como E3, E5, pago por uso, vista previa o roadmap; anota las que debes confirmar en la descripción del servicio.
5. `Solo producción` Exporta el inventario de licencias asignadas en producción (Microsoft 365 E3 y E5, Purview Suite, E5 IP&G, Copilot y E7) y contrástalo con los grupos piloto previstos. Forma segura: rol de lectura de facturación o de informes, sin cambiar asignaciones, y entrega del resultado al dueño del presupuesto.

**¿Quieres profundizar?**

- [Microsoft 365 Security & Compliance Product Renames](https://samexpert.com/microsoft-365-defender-purview-renames/) · Blog

<a id="i2"></a>

## I2 · Clasificación de datos: tipos sensibles, EDM, clasificadores y exploradores

*L200 · ~6 h · Origen: Ruta Ninja de Learn · módulo 1 «Discover and define sensitive information types»*

La clasificación es la base de todo: el auto-etiquetado, la DLP, la retención y las protecciones para Copilot dependen de reconocer qué es sensible. Purview ofrece **tipos de información confidencial (SIT)** integrados, de entidades con nombre, personalizados y de **Exact Data Match (EDM)**, todos con los mismos componentes: elemento primario, evidencia de apoyo, nivel de confianza y proximidad. Suma las **huellas digitales de documento**, que reconocen formularios y plantillas, y los **clasificadores entrenables**, que aprenden categorías de documentos. Los SIT sintácticos (expresiones regulares, palabras clave y diccionarios) están en E3 y E5; EDM, entidades con nombre, huellas y clasificadores entrenables, en E5 según el mapa indicativo.

La nueva experiencia de **EDM** crea esquema y SIT en un solo flujo a partir de un archivo de muestra de 10 a 20 filas y carga los datos con hash mediante el EDM Upload Agent. Los **clasificadores entrenables personalizados** piden entre 50 y 500 muestras positivas y entre 150 y 1.500 negativas en SharePoint, y procesan hasta las 2.000 más recientes. En MCSA, buena parte del trabajo está en crear SIT para identificadores y formatos propios de cada país y empresa, siempre probados con datos sintéticos.

Para ver dónde está lo sensible tienes tres exploradores: **Data explorer** y **Content explorer (classic)** muestran una instantánea de los elementos con etiquetas o SIT y permiten leer su contenido, por lo que su acceso se restringe; el **explorador de actividades** muestra hasta 30 días de acciones sobre contenido etiquetado y sensible, con una latencia de 60 a 90 minutos.

**Por qué importa**

Sin una buena clasificación, el auto-etiquetado y la DLP se vuelven ruido: falsos positivos que las personas aprenden a ignorar o falsos negativos que dejan datos de clientes sin proteger. Invertir aquí —SIT para identificadores locales y EDM para las tablas de clientes y empleados— mejora la precisión medida en las simulaciones, reduce excepciones y le da al dueño de los datos un inventario defendible de dónde vive la información sensible.

**Qué vas a lograr**

- Explicar los componentes de un SIT y elegir entre SIT integrado, personalizado, EDM, huella digital o clasificador entrenable.
- Crear y probar un SIT personalizado con datos sintéticos.
- Construir un SIT EDM con la nueva experiencia y un archivo de muestra sintético.
- Usar Data explorer, Content explorer (classic) y el explorador de actividades con el rol mínimo necesario.

> **Novedad.** La nueva experiencia de EDM crea el esquema y el SIT en un solo flujo a partir de un archivo de muestra de 10 a 20 filas e incluye guardarraíles de rendimiento; EDM sirve en DLP, auto-etiquetado en cliente y en servicio, eDiscovery y Defender for Cloud Apps, y Brasil es la única región de Sudamérica listada ([EDM](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview)). Elige entre 1 y 10 elementos primarios únicos y evita campos repetidos como nombre o fecha de nacimiento ([esquema EDM](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-schema-rule-package)).

> **Atención.** Desde mayo de 2026, navegar Data explorer y Content explorer (classic) exige el rol Data Classification List Viewer, incluso a quienes tenían Organization Management. La fuente es un blog comunitario que resume un aviso del Centro de mensajes: confírmalo en la documentación de permisos ([Topedia](https://blog.topedia.com/posts/updates-to-permissions-for-microsoft-purview-data-explorer-and-content-explorer)). El acceso a estos exploradores debe ser muy restringido porque permiten leer contenido ([Data explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer)).

> **Consejo Ninja.** Clasificadores entrenables personalizados: entre 50 y 500 muestras positivas y entre 150 y 1.500 negativas en carpetas dedicadas de SharePoint; procesan hasta las 2.000 muestras más recientes y solo archivos de texto, y un flujo automatizado en vista previa reduce el proceso de 12 a 2 días. Communication Compliance solo admite los integrados ([clasificadores entrenables](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with)).

> **Qué cambió.** El explorador de contenido aparece ahora como «Content explorer (classic)» junto al nuevo Data explorer en la página de informes ([informes](https://learn.microsoft.com/en-us/purview/purview-reports)). Los SIT de escaneo de credenciales requieren licencia E5 ([SIT](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about)), y el explorador de actividades conserva hasta 30 días con una latencia típica de 60 a 90 minutos ([explorador de actividades](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)).

**¿Tienes poco tiempo?**

- [Learn about sensitive information types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about) · Documentación
- [Get started with exact data match sensitive information types in Microsoft Purview](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) · Documentación
- [Get started with trainable classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with) · Documentación
- [Get started with data explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer) · Documentación

### Documentación, cursos y credenciales

- [Implement information protection and data loss prevention by using Microsoft Purview (SC-5003)](https://learn.microsoft.com/en-us/training/paths/purview-implement-information-protection-data-loss-prevention/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje (~4 h 55 min) de la credencial aplicada SC-5003 que cubre SIT, EDM, fingerprinting, entidades con nombre, diccionarios, etiquetas, auto-etiquetado y DLP con un módulo de ejercicios.
- [Get started with exact data match sensitive information types in Microsoft Purview](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) · Documentación · Oficial · Microsoft Learn. Compara la nueva experiencia EDM (esquema y SIT en un solo flujo, archivo de muestra de 10-20 filas, guardarraíles de rendimiento) con la clásica y PowerShell, y lista regiones admitidas.
- [Get started with trainable classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with) · Documentación · Oficial · Microsoft Learn. Cómo crear y probar un clasificador entrenable personalizado con muestras positivas (50-500) y negativas (150-1.500) en carpetas dedicadas de SharePoint.
- [Learn about sensitive information types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about) · Documentación · Oficial · Microsoft Learn. Explica las categorías de SIT (integrados, entidades con nombre agrupadas o no, personalizados y EDM), sus componentes (elemento primario, evidencia, confianza, proximidad) y dónde se usan.
- [Create and manage sensitive information types (training module)](https://learn.microsoft.com/en-us/training/modules/create-manage-sensitive-information-types/) · Curso · Oficial · Microsoft Learn. Módulo de ~1 h sobre SIT integrados vs personalizados, EDM, fingerprinting de documentos, entidades con nombre y diccionarios de palabras clave, con evaluación.
- [Get started with data explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer) · Documentación · Oficial · Microsoft Learn. Describe el explorador de datos que muestra una instantánea de elementos con etiquetas de confidencialidad o retención o con SIT detectados, y los roles Data Explorer List viewer y Content viewer.
- [Create exact data match sensitive information type in the New Experience workflow](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-workflow) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Resume las 5 fases del flujo EDM nuevo: exportar datos, crear archivo de muestra, crear el SIT, hashear y subir con EDM Upload Agent, y probar.
- [Create an EDM SIT schema and rule package (New experience)](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-schema-rule-package) · Documentación · Oficial · Microsoft Learn. Detalla cómo elegir elementos primarios únicos (1 a 10 por SIT), usar coincidencia multi-token y mapear SIT ajustados al formato para mejorar precisión y rendimiento.

### Laboratorios, GitHub y herramientas

- [Microsoft Purview — Classification & Labeling Interactive Reference Architecture](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) · Herramienta · Oficial · Nuevo · Microsoft (GitHub Pages microsoft/purview) · 2 nov 2026. Arquitectura de referencia interactiva que recorre clasificación, etiquetado, protección e insights en Microsoft 365, marcando para cada capacidad si es E3, E5 o pago por uso y si está en preview o roadmap.
- [Implement information protection and data loss prevention with Microsoft Purview (exercise module)](https://learn.microsoft.com/en-us/training/modules/purview-exercise-information-protection-data-loss-prevention/) · Laboratorio · Oficial · Microsoft Learn. Módulo práctico de ~1 h con ejercicios guiados para configurar el entorno, crear un SIT personalizado, crear y publicar una etiqueta y crear una política DLP.

### Comunidad: blogs, libros, newsletters y eventos

- [Updates to permissions for Microsoft Purview Data Explorer and Content Explorer](https://blog.topedia.com/posts/updates-to-permissions-for-microsoft-purview-data-explorer-and-content-explorer) · Blog · Comunidad · Nuevo · Tobias Asböck · Topedia Blog · 20 may 2026. Explica el cambio de mayo de 2026 que exige el rol Data Classification List Viewer para navegar Data explorer y Content explorer (classic), incluso a quienes tenían Organization Management.

**Manos a la obra**

1. `Laboratorio` Crea un SIT personalizado para un identificador propio de tu organización (por ejemplo, un número de póliza o de cliente con formato fijo) con expresión regular, palabras clave en español, proximidad y niveles de confianza. Pruébalo con un archivo que coincide y otro que no ([SIT](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about), [probar un SIT](https://learn.microsoft.com/en-us/purview/sit-test-a-sit)). Evidencia: capturas de ambos resultados.
2. `Laboratorio parcial` Construye un SIT EDM con la nueva experiencia: archivo de muestra sintético de 10 a 20 filas, esquema con 1 a 3 elementos primarios, carga con el EDM Upload Agent desde una VM y prueba al menos una hora después de indexar ([flujo EDM](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-workflow), [archivo de muestra](https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-sample-file)). Limitación: con datos sintéticos no mides precisión ni rendimiento reales; en producción, carga un subconjunto con hash, con aprobación del dueño de los datos y de Privacidad.
3. `Laboratorio parcial` Usa un clasificador entrenable integrado en una política de auto-etiquetado en modo simulación y anota los falsos positivos. Limitación: entrenar uno personalizado exige entre 50 y 500 muestras reales que un tenant de prueba no tiene; en producción, usa un sitio de acceso mínimo y borra las muestras al publicar ([clasificadores entrenables](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with)).
4. `Laboratorio` Da a una cuenta de prueba solo el rol necesario para navegar Data explorer y compara lo que ve frente a una cuenta sin él; documenta quién en tu organización debería tenerlo ([Data explorer](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer)).
5. `Laboratorio` Genera actividad sobre archivos con SIT (abrir, etiquetar, copiar y compartir) y al día siguiente filtra el explorador de actividades por SIT y por usuario; guarda el conjunto de filtros y exporta el resultado ([explorador de actividades](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)).
6. `Laboratorio` Completa el módulo de Learn [Create and manage sensitive information types](https://learn.microsoft.com/en-us/training/modules/create-manage-sensitive-information-types/) y su evaluación.

**¿Quieres profundizar?**

- [Microsoft Purview — Classification & Labeling Interactive Reference Architecture](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) · Herramienta
- [Implement information protection and data loss prevention with Microsoft Purview (exercise module)](https://learn.microsoft.com/en-us/training/modules/purview-exercise-information-protection-data-loss-prevention/) · Laboratorio

<a id="i3"></a>

## I3 · Etiquetas de confidencialidad: taxonomía, políticas y publicación

*L200 · ~5 h · Origen: Ruta Ninja de Learn · módulo 2 «Classify and protect sensitive data with sensitivity labels» (primera parte)*

Una **etiqueta de confidencialidad** es un metadato persistente que clasifica el contenido y, si lo configuras, lo protege con cifrado y marcas (encabezado, pie de página y marca de agua). Funciona en Word, Excel, PowerPoint y Outlook de escritorio y web en Windows, macOS, iOS y Android, y también protege contenedores: equipos de Teams, grupos, sitios, comunidades de Viva Engage y áreas de trabajo de Loop. Requiere una edición de Office por suscripción —no Office perpetuo— y, en Outlook, buzones en Exchange Online. Como la etiqueta viaja con el archivo, el resto de los controles (DLP, Copilot, retención) pueden leerla.

Las etiquetas se crean, se ordenan por prioridad y se **publican** mediante políticas de etiquetas que definen la etiqueta predeterminada para documentos, correo y reuniones, el etiquetado obligatorio, la justificación para bajar de nivel y el vínculo de ayuda. Los tenants creados desde el 1 de octubre de 2025 usan el esquema moderno de **grupos de etiquetas**; migrar etiquetas padre a grupos es irreversible. Microsoft sugiere empezar por Personal, Público, General, Confidencial y Altamente confidencial, con no más de cinco etiquetas principales con cinco subetiquetas y descripciones probadas con usuarios.

El último paso habilitador es **habilitar las etiquetas para SharePoint y OneDrive**, que sigue siendo manual aunque uses las etiquetas predeterminadas: sin él no hay coautoría, búsqueda ni eDiscovery sobre archivos cifrados. Los cambios en etiquetas y políticas tardan hasta 24 horas en propagarse, así que planifica la publicación con calma.

**Por qué importa**

La taxonomía es el contrato del programa con las personas: si los nombres y las descripciones no se entienden, se etiqueta mal y cada control posterior (DLP, Copilot, retención) hereda el error. Una taxonomía pequeña, probada con usuarios, con etiqueta predeterminada y bajadas justificadas, eleva rápido la cobertura, genera evidencia de auditoría y simplifica las decisiones posteriores de auto-etiquetado y cifrado.

**Qué vas a lograr**

- Diseñar una taxonomía de cuatro o cinco etiquetas con subetiquetas, nombres y descripciones probados con usuarios.
- Crear etiquetas y ordenarlas por prioridad con el esquema moderno de grupos de etiquetas.
- Publicar una política piloto con etiqueta predeterminada, etiquetado obligatorio y justificación para bajar de nivel.
- Habilitar las etiquetas para SharePoint y OneDrive y verificar la experiencia en Office web y de escritorio.
- Diferenciar las etiquetas de confidencialidad de las de retención.

> **Qué cambió.** Los tenants creados desde el 1 de octubre de 2025 usan el esquema moderno de etiquetas, con grupos de etiquetas ([crear etiquetas](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)). Migrar etiquetas padre a grupos es irreversible y Microsoft entrega scripts de PowerShell para despublicar las subetiquetas creadas en la migración: pruébalo antes en un tenant de prueba ([migración](https://learn.microsoft.com/en-us/purview/migrate-sensitivity-label-scheme)).

> **Atención.** Requisitos: edición de Office por suscripción (no Office perpetuo) y buzones en Exchange Online; la directiva «Use the Azure Information Protection add-in» debe quedar sin configurar o deshabilitada ([etiquetas en Office](https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps)). Los cambios en etiquetas y políticas tardan hasta 24 horas (24 a 48 si dependen de grupos nuevos): no diagnostiques antes.

> **Consejo Ninja.** Taxonomía: no más de cinco etiquetas principales con cinco subetiquetas, nombres autoexplicativos y controles por nivel; Microsoft reemplazó «Internal» por «General» en su propio marco ([taxonomía de referencia](https://learn.microsoft.com/en-us/compliance/assurance/assurance-data-classification-and-labels)). En las Purview Lightning Talks de abril de 2026 se defendieron taxonomías de cuatro etiquetas como máximo ([agenda](https://techcommunity.microsoft.com/discussions/data-security/welcome-purview-lightning-talks-audience/4516006)).

> **Atención.** Habilitar las etiquetas para SharePoint y OneDrive sigue siendo un paso manual aunque uses las etiquetas predeterminadas, y sin él no hay coautoría, búsqueda ni eDiscovery sobre archivos cifrados ([habilitar en SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files)). Para no confundir funciones, compara etiquetas de confidencialidad y de retención con [esta infografía](https://joannecklein.com/2026/07/30/a-contrast-and-comparison-of-retention-and-sensitivity-labels/); la retención se profundiza en el programa de Ciclo de vida y Registros.

**¿Tienes poco tiempo?**

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels) · Documentación
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) · Documentación
- [Learn about the default sensitivity labels and policies to protect your data](https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies) · Documentación
- [Data classification and sensitivity label taxonomy (Microsoft Service Assurance)](https://learn.microsoft.com/en-us/compliance/assurance/assurance-data-classification-and-labels) · Documentación

### Documentación, cursos y credenciales

- [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels) · Documentación · Oficial · Microsoft Learn. Documento conceptual central de etiquetas de confidencialidad: qué pueden hacer (cifrado, marcas, contenedores, reuniones, Power BI, Data Map, SDK), qué controlan las políticas de etiquetas y cómo interactúan con Microsoft 365 Copilot.
- [Get started with sensitivity labels](https://learn.microsoft.com/en-us/purview/get-started-with-sensitivity-labels) · Documentación · Oficial · Microsoft Learn. Flujo de despliegue (crear, definir, publicar), requisitos de licencia y facturación, grupos de roles de Information Protection y soporte de unidades administrativas para etiquetas.
- [Create and configure sensitivity labels and their policies](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) · Documentación · Oficial · Microsoft Learn. Procedimiento para crear etiquetas (esquema clásico o moderno), definir su alcance, ordenarlas por prioridad y publicarlas mediante políticas de etiquetas, incluido PowerShell.
- [Learn about the default sensitivity labels and policies to protect your data](https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies) · Documentación · Oficial · Microsoft Learn. Describe las etiquetas, la política de publicación y las políticas de auto-etiquetado (cliente y servicio) que Purview crea por defecto para clientes nuevos o que se activan desde DSPM.
- [Migrate parent sensitivity labels to sensitivity label groups](https://learn.microsoft.com/en-us/purview/migrate-sensitivity-label-scheme) · Documentación · Oficial · Microsoft Learn. Guía para migrar del esquema de etiquetas padre al esquema moderno de grupos de etiquetas, con scripts de PowerShell para despublicar subetiquetas creadas en la migración.

### Comunidad: blogs, libros, newsletters y eventos

- [A Contrast and Comparison of Retention and Sensitivity Labels](https://joannecklein.com/2026/07/30/a-contrast-and-comparison-of-retention-and-sensitivity-labels/) · Blog · MVP · Nuevo · Joanne Klein · Joanne C Klein · 30 jul 2026. Infografía actualizada que compara 20 comportamientos clave entre etiquetas de confidencialidad y de retención para evitar confusiones de diseño.

**Manos a la obra**

1. `Laboratorio` Activa las etiquetas y políticas predeterminadas desde DSPM (o revísalas si tu tenant ya las tiene), habilita las etiquetas para SharePoint y OneDrive y publícalas a un grupo piloto ([etiquetas predeterminadas](https://learn.microsoft.com/en-us/purview/default-sensitivity-labels-policies), [laboratorios SC-401](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs)). Evidencia: lista de etiquetas, políticas y estado de la habilitación.
2. `Laboratorio` Taller de taxonomía: a partir de la [Taxonomía de ejemplo](00_Programa.md#taxonomia), redacta nombres y descripciones en español neutro y valídalos con cinco personas de distintas áreas pidiéndoles que etiqueten diez documentos de muestra. Mide cuántos aciertan y ajusta lo que confunda.
3. `Laboratorio` Crea tu taxonomía con prefijo PRUEBA- en el esquema moderno, ordénala por prioridad y publica una política piloto con etiqueta predeterminada para documentos y correo, etiquetado obligatorio y justificación para bajar de nivel ([crear y publicar](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels)). Espera 24 horas y verifica la barra de confidencialidad en Word y Outlook web.
4. `Laboratorio` Con una persona del piloto, baja un documento de Confidencial a General y localiza en el explorador de actividades el evento con su justificación.
5. `Laboratorio` Exporta la configuración con `Get-Label` y `Get-LabelPolicy` en Security & Compliance PowerShell y guárdala como línea base ([inventario con PowerShell](https://office365itpros.com/2026/06/11/sensitivity-label-ps/)).
6. `Solo producción` Publica la taxonomía en producción por oleadas: primero una política para un grupo piloto de voluntarios informados y, dos semanas después, una segunda política para el resto. Forma segura: etiquetas sin cifrado en la primera oleada, comunicación previa, espera de 24 horas antes de diagnosticar y, para revertir, quitar la etiqueta de la política en lugar de eliminarla.

**¿Quieres profundizar?**

- [A Contrast and Comparison of Retention and Sensitivity Labels](https://joannecklein.com/2026/07/30/a-contrast-and-comparison-of-retention-and-sensitivity-labels/) · Blog

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primera taxonomía publicada.** En tu laboratorio, diseña una taxonomía de cuatro o cinco etiquetas con subetiquetas a partir de la [Taxonomía de ejemplo](00_Programa.md#taxonomia), redacta sus descripciones y valídalas con cinco personas. Publícala a un grupo piloto con etiqueta predeterminada, etiquetado obligatorio y justificación para bajar de nivel; crea un SIT personalizado y un SIT EDM con datos sintéticos. Entrega un informe de una página con capturas, el evento de una bajada justificada en el explorador de actividades y el mapa de licencias de tu organización.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Quién puede habilitar las funciones de pago por uso de Purview vinculando el tenant a una suscripción de Azure?
   - a) Cualquier persona con el rol Compliance Administrator
   - b) Solo un Global Administrator
   - c) El propietario de la suscripción de Azure, sin ningún rol en Entra
   - d) Cualquier miembro del grupo de roles Information Protection Admins

2. ¿Cuándo se retiró el portal clásico de cumplimiento?
   - a) El 2 de julio de 2024, el mismo día de la disponibilidad general del nuevo portal
   - b) El 11 de abril de 2024, junto con el complemento de AIP para Office
   - c) Entre el 14 de noviembre y el 14 de diciembre de 2024
   - d) El 1 de octubre de 2025, junto con el cambio de nombre a Purview Suite

3. ¿Con qué puntaje se aprueba el examen SC-401?
   - a) 700
   - b) 600
   - c) 750
   - d) 800

4. En un sitio de SharePoint donde se aplica una capacidad premium de Purview, ¿quiénes necesitan licencia?
   - a) Todas las personas del tenant, incluidos los visitantes con acceso de solo lectura
   - b) Solo el administrador que crea y publica la política, porque es quien la configura
   - c) Solo los propietarios del sitio; los miembros quedan cubiertos por la licencia del propietario
   - d) Los propietarios y los miembros, pero no los visitantes ni los roles de solo lectura

5. Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama…
   - a) Microsoft Defender Suite
   - b) Microsoft 365 E7
   - c) Microsoft Purview Suite
   - d) E5 Information Protection and Governance

6. Según el mapa indicativo de Microsoft, ¿qué capacidad de clasificación se factura por uso?
   - a) Los SIT con expresiones regulares y palabras clave
   - b) La clasificación bajo demanda
   - c) Los clasificadores entrenables
   - d) La etiqueta predeterminada de la política

7. ¿Con qué licencias se soportarán las capacidades de Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra?
   - a) Microsoft 365 E3
   - b) Microsoft Purview Suite sobre E3
   - c) Office 365 E5
   - d) Microsoft 365 E7 y los SKU de Agent 365

8. ¿Qué archivo de muestra pide la nueva experiencia de EDM para definir el esquema?
   - a) Entre 10 y 20 filas con valores sintéticos que imitan el formato de la tabla real
   - b) La tabla real completa, sin hash, para que el esquema sea exacto
   - c) Exactamente 1.000 filas reales elegidas al azar de la tabla
   - d) Ninguno: el esquema se escribe a mano en XML, sin archivo de muestra

9. Para entrenar un clasificador entrenable personalizado, ¿qué muestras necesitas?
   - a) Entre 10 y 20 positivas, como el archivo de muestra de EDM
   - b) Solo muestras negativas, porque las positivas las aporta Microsoft
   - c) Entre 50 y 500 positivas y entre 150 y 1.500 negativas
   - d) Al menos 2.000 positivas y ninguna negativa

10. ¿Por qué el acceso a Data explorer y a Content explorer (classic) debe estar muy restringido?
   - a) Porque cada consulta se cobra por uso a la suscripción de Azure vinculada
   - b) Porque permiten ver el contenido de los elementos con etiquetas o SIT
   - c) Porque al abrirlos se cambian las etiquetas de los archivos listados
   - d) Porque desactivan la auditoría unificada mientras se navegan

11. ¿Qué esquema de etiquetas usan los tenants creados desde el 1 de octubre de 2025?
   - a) El esquema moderno de grupos de etiquetas
   - b) Etiquetas padre con subetiquetas, sin opción de migrar
   - c) Un esquema sin prioridades
   - d) El esquema del complemento de AIP

12. ¿Qué requisitos tiene el etiquetado integrado en Outlook?
   - a) Office 2019 perpetuo con el complemento de etiquetado
   - b) El complemento de AIP instalado en cada equipo con Outlook
   - c) Una licencia de Teams Premium para cada remitente
   - d) Un buzón en Exchange Online y una edición de Office por suscripción

13. ¿Qué tamaño máximo de taxonomía recomienda la guía de Microsoft?
   - a) Tres etiquetas principales, sin ninguna subetiqueta
   - b) Diez etiquetas principales, una por tipo de documento
   - c) Cinco etiquetas principales con cinco subetiquetas
   - d) Una etiqueta principal por cada departamento de la organización

14. Publicas etiquetas que cifran sin haber habilitado las etiquetas para SharePoint y OneDrive. ¿Qué pierdes sobre esos archivos?
   - a) La posibilidad de etiquetar y cifrar el correo en Outlook
   - b) La coautoría, Office web, la búsqueda y eDiscovery
   - c) Las marcas de contenido (encabezado, pie y marca de agua) en Word
   - d) El etiquetado manual en las apps de Office para iOS y Android

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview Data Loss Prevention Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

El portal de Purview, las ubicaciones y licencias de DLP, el diseño de directivas en modo de simulación y la protección de endpoints y navegadores. Terminas con un tenant de práctica listo, tu matriz de cobertura y una primera directiva en simulación con un equipo Windows 11 incorporado.

*L100–L200 · 5 módulos · ~26 horas · 37 recursos*

**Módulos de este nivel:** [P0 Portal, roles y prueba](#p0) · [I0 Cómo aprender](#i0) · [I1 Ubicaciones y licencias](#i1) · [I2 Diseño y simulación](#i2) · [I3 Endpoints y navegadores](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview y el portal unificado

*L100–L200 · ~3 h · Origen: Nuevo en esta edición (la ruta Ninja de Learn asume estos conocimientos)*

DLP vive dentro de Microsoft Purview y, antes de crear la primera directiva, conviene conocer bien su casa. Todas las directivas se crean en el **portal de Microsoft Purview**, se guardan en un almacén central y se sincronizan a Exchange (y desde allí a Outlook), SharePoint, OneDrive, las apps de Office y Teams; en general entran en vigor alrededor de una hora después de activarlas. El portal de cumplimiento clásico está retirado, así que cualquier guía que lo mencione está desactualizada.

El segundo pilar es el **modelo de permisos**: roles y grupos de roles de Purview, roles de Entra ID, PIM para grupos (los permisos pueden tardar hasta dos horas en aplicarse) y unidades administrativas para acotar qué ve cada administrador. Desde julio de 2026 las asignaciones a grupos de roles pueden vencer, y la DLP de Copilot tiene su propio rol de mínimo privilegio. El tercero es tu **entorno de práctica**: una prueba de Microsoft 365 E5 o, si tu tenant productivo tiene E3, la prueba de Microsoft Purview Suite (antes Microsoft 365 E5 Compliance).

**Por qué importa**

Un modelo de roles mal diseñado produce dos riesgos opuestos: administradores con más poder del necesario sobre directivas capaces de bloquear al negocio, y analistas sin permisos para investigar. Definir desde el inicio roles de mínimo privilegio, asignaciones con vencimiento y alcance por unidad administrativa reduce los cambios no autorizados, acelera las investigaciones y deja evidencia auditable para cumplimiento.

**Qué vas a lograr**

- Navegar el portal de Purview y ubicar las soluciones, la configuración y los roles que usa DLP.
- Diseñar un modelo de roles de mínimo privilegio con grupos de roles, PIM, vencimientos y unidades administrativas.
- Identificar el rol Purview Data Security AI Admin para administrar la DLP de Copilot sin leer prompts.
- Preparar un tenant de práctica con la prueba adecuada, la auditoría activa y personas de prueba marcadas.

> **Qué cambió.** El portal de cumplimiento clásico está retirado: todo se administra en el [portal de Microsoft Purview](https://learn.microsoft.com/en-us/purview/purview-portal). Si usas PIM para grupos, los permisos pueden tardar hasta dos horas en hacerse efectivos, así que no diagnostiques un «acceso denegado» antes de ese plazo.

> **Novedad.** Desde julio de 2026, las asignaciones a grupos de roles de Purview pueden tener fecha de expiración, de un día a dos años, salvo eDiscovery Administrator y eDiscovery Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Úsalo para accesos temporales de consultores, auditores o proyectos.

> **Consejo Ninja.** Para la DLP de Copilot, el rol de mínimo privilegio es **Purview Data Security AI Admin**: edita directivas de la ubicación Copilot sin poder leer prompts ni respuestas ([DLP para Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)). El resto del modelo —roles, grupos de roles, roles de Entra, PIM y unidades administrativas— está en [permisos del portal](https://learn.microsoft.com/en-us/purview/purview-permissions).

> **Atención.** La [prueba de Microsoft Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) (antes Microsoft 365 E5 Compliance) da 25 licencias por 90 días, ampliables en los últimos 15 días, solo a tenants con Microsoft 365 E3 u Office 365 E3 + EMS E3, y no está disponible en Government. Si no cumples esas condiciones, usa la prueba de Microsoft 365 E5 descrita en el anexo común del entorno de práctica.

**¿Tienes poco tiempo?**

- [Learn about the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-portal) · Documentación
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación
- [Learn about the Microsoft Purview Suite trial](https://learn.microsoft.com/en-us/purview/purview-trial) · Documentación

### Documentación, cursos y credenciales

- [Learn about the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-portal) · Documentación · Oficial · Microsoft Learn. Recorrido por el portal unificado de Microsoft Purview: página de inicio, navegación por solución, configuración y roles centralizados, búsqueda global y funciones reubicadas desde el portal de cumplimiento retirado.
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación · Oficial · Microsoft Learn. Modelo RBAC de Purview: roles, grupos de roles, roles de Entra, PIM para grupos, ámbito por unidades administrativas y enlaces a permisos específicos de DLP, Device Onboarding, EDM y agentes de triaje.
- [Learn about the Microsoft Purview Suite trial](https://learn.microsoft.com/en-us/purview/purview-trial) · Documentación · Oficial · Microsoft Learn. Prueba gratuita de 90 días que asigna 25 licencias de Microsoft Purview Suite (antes Microsoft 365 E5 Compliance) a tenants con M365 E3 u O365 E3 + EMS E3.

**Manos a la obra**

1. `Laboratorio` Activa la auditoría unificada del tenant de práctica y verifica `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` en Exchange Online PowerShell (en Security & Compliance PowerShell esa propiedad siempre aparece en False); en tenants de prueba viene apagada y tarda hasta 60 minutos en activarse ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)). Evidencia: captura con el valor True.
2. `Laboratorio` Recorre el [portal de Purview](https://learn.microsoft.com/en-us/purview/purview-portal) y ubica Data Loss Prevention, el explorador de actividad, la configuración de Endpoint DLP, la incorporación de dispositivos y los roles. Evidencia: mapa de navegación de una página para tu equipo.
3. `Laboratorio` Crea tres grupos de roles personalizados —administración de DLP, investigación de alertas y solo lectura— con asignaciones que venzan en 30 días, y acota un administrador a una unidad administrativa de prueba ([permisos](https://learn.microsoft.com/en-us/purview/purview-permissions), [unidades administrativas](https://learn.microsoft.com/en-us/purview/purview-admin-units)). Evidencia: tabla rol, grupo, persona y vencimiento, y captura de lo que ve el administrador acotado.
4. `Laboratorio` Crea entre 10 y 16 personas de prueba con atributos completos (Department y país) y márcalas con un atributo común, por ejemplo `CustomAttribute15 = PRUEBA-PURVIEW`, para usarlas en ámbitos y excluirlas de reportes ([ámbitos adaptables](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes)); publica la convención de nombres `PRUEBA-DLP-<objetivo>-v<n>-<AAAAMM>`. Evidencia: lista de cuentas y convención documentada.
5. `Solo producción` Si tu organización tiene E3, evalúa la [prueba de Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) en el tenant productivo: no crea nada automáticamente ni afecta a las personas, pero al terminar no podrás editar las ubicaciones de Teams y dispositivos de las directivas creadas. Cómo hacerlo seguro: inícialo con un rol de Billing o Compliance Administrator y la aprobación del dueño del presupuesto, crea solo directivas `PRUEBA-` en simulación para un grupo piloto y documenta qué desactivar al vencer la prueba.

<a id="i0"></a>

## I0 · Cómo aprender DLP y dónde pedir ayuda

*L100–L200 · ~4 h · Origen: Ruta Ninja de Microsoft Learn y ruta oficial de DLP para SC-401*

Este recorrido es extenso, pero no reemplaza a las otras puertas: conviene saber cuáles son y cuándo usar cada una. La **ruta Ninja de Microsoft Learn** (cinco módulos, unas dos horas e insignia) es la referencia oficial por escenarios; la ruta **Implement and manage Microsoft Purview Data Loss Prevention** profundiza en planificar, crear y operar directivas; y los **laboratorios del curso SC-401** en GitHub ofrecen ejercicios guiados de DLP, Endpoint DLP, protección adaptativa y DSPM para IA, pensados para tenants de clase pero adaptables a una prueba E5.

Para mantenerte al día, la fuente primaria es la página mensual **What's new in Microsoft Purview** (última actualización: 16 de octubre de 2026), complementada con el blog oficial de Purview en Tech Community y los avisos del Centro de mensajes. Si buscas una credencial formal, la guía del examen **SC-401** se actualizó el 28 de octubre de 2026 e incluye la protección de datos usados por IA. Este módulo te ayuda a combinar todo en una rutina semanal y a ubicar a la comunidad que verás en [C1](05_Comunidad.md#c1) y [C2](05_Comunidad.md#c2).

**Por qué importa**

DLP cambia cada mes: en 2026 aparecieron ubicaciones, acciones y modelos de licencia nuevos, y varios estados de vista previa se contradicen entre fuentes. Un equipo sin rutina de actualización decide con información vencida, por ejemplo integrando con una API ya retirada o prometiendo una protección que todavía está en vista previa. Media hora semanal con fuentes primarias evita retrabajo y protege la credibilidad del equipo ante el negocio.

**Qué vas a lograr**

- Identificar las rutas oficiales de aprendizaje, los laboratorios y las credenciales relacionadas con DLP.
- Completar la ruta Ninja de Microsoft Learn y obtener su insignia.
- Mapear las habilidades del examen SC-401 a los módulos de esta guía.
- Armar una rutina semanal de actualización con fuentes primarias y secundarias.

> **Novedad.** La [guía del examen SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) se actualizó el 28 de octubre de 2026: protección de la información, DLP y retención, y riesgos, alertas y actividades pesan entre 30 y 35 % cada uno, e incluye Endpoint DLP con JIT, protección adaptativa, DLP con Defender for Cloud Apps, respuesta a alertas en Defender XDR y DSPM para IA. Se aprueba con 700 y la renovación anual es gratuita.

> **Qué cambió.** El Ninja de Information Protection de Tech Community, que incluía DLP, pasó a «en construcción» en julio de 2025 y desde agosto de 2025 redirige a la [ruta Ninja de Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/), que otorga una insignia pero no un certificado al 80 %. Este programa agrega esa evaluación por nivel.

> **Consejo Ninja.** La fuente primaria de estados de disponibilidad general y vista previa es [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) (última actualización: 16 de octubre de 2026). Para el detalle de cada aviso del Centro de mensajes, el archivo comunitario de Merill Fernando replica los mensajes oficiales, por ejemplo [MC1477182](https://mc.merill.net/message/MC1477182) sobre Cowork.

> **Atención.** Las versiones localizadas de la [ruta de DLP para SC-401](https://learn.microsoft.com/en-us/training/paths/purview-implement-manage-dlp/) muestran duraciones menores que la versión en inglés por una traducción desfasada; si estudias en español, contrasta con el original antes del examen.

**¿Tienes poco tiempo?**

- [Secure sensitive data with Microsoft Purview Ninja training scenarios](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) · Curso
- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial

### Documentación, cursos y credenciales

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía oficial del examen SC-401 con habilidades medidas al 28-oct-2026: protección de información, DLP y retención, y riesgos/alertas/actividades (30-35% cada una), incluida la protección de datos usados por IA.
- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Registro mensual oficial de novedades de Purview, imprescindible para seguir cambios de DLP (estados preview/GA, nuevas ubicaciones y actualizaciones de documentación).
- [Implement and manage Microsoft Purview Data Loss Prevention (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-implement-manage-dlp/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje oficial de DLP alineada al SC-401 (5 módulos, ~4 h): planificar, crear y gestionar directivas, Endpoint DLP con extensión y JIT, DLP para Defender for Cloud Apps/Power Platform e investigación de alertas.

### Anuncios y blogs oficiales

- [Microsoft Purview Blog](https://techcommunity.microsoft.com/category/microsoft-purview/blog/microsoft-purview-blog) · Blog oficial · Oficial · Nuevo · Equipo de producto Purview · Microsoft Tech Community · 3 nov 2026. Blog oficial del producto con guías prácticas recientes (clasificadores, autoetiquetado, protección en capas, API de estado de dispositivos, unidades administrativas, IA).

### Webinars, videos y podcasts

- [Microsoft Purview: New Data Loss Prevention (DLP) controls for the browser & network](https://www.youtube.com/watch?v=86gxrO2Aw1Q) · Video · Empleado de Microsoft · Roberto Yglesias · Microsoft Mechanics (YouTube). Episodio de Microsoft Mechanics que muestra DLP unificado en apps de Microsoft 365, Edge for Business, endpoints Windows/macOS y red HTTPS, más evaluación de directivas con DSPM.

**Manos a la obra**

1. `Laboratorio` Completa la [ruta Ninja de Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) (cinco módulos, unas dos horas) con el *module assessment* de cada módulo. Evidencia: insignia en tu perfil de Learn.
2. `Laboratorio` Descarga la [guía de SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y marca, por cada habilidad de DLP, el módulo de esta guía que la cubre. Evidencia: tabla habilidad y módulo, con los huecos señalados.
3. `Laboratorio` Revisa los [laboratorios de SC-401T00](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs) e identifica los ejercicios de DLP, Endpoint DLP y protección adaptativa que harás en tu tenant de prueba (están pensados para tenants de clase y se adaptan a una prueba E5). Evidencia: lista de laboratorios con fecha planificada.
4. `Laboratorio` Arma tu rutina semanal de 30 minutos con las [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new), el [blog de Purview](https://techcommunity.microsoft.com/category/microsoft-purview/blog/microsoft-purview-blog) y una fuente comunitaria de [C2](05_Comunidad.md#c2). Evidencia: tres novedades de DLP del último mes resumidas en una línea cada una, con su estado (disponibilidad general o vista previa).

**¿Quieres profundizar?**

- [Microsoft Purview: New Data Loss Prevention (DLP) controls for the browser & network](https://www.youtube.com/watch?v=86gxrO2Aw1Q) · Video

<a id="i1"></a>

## I1 · Purview DLP hoy: ubicaciones y qué incluye Microsoft 365 E5

*L100–L200 · ~5 h · Origen: Ruta Ninja de Learn, módulo 4 (DLP en Exchange, SharePoint, OneDrive y Teams), ampliado a todas las ubicaciones*

Purview DLP detecta información sensible —con tipos de información confidencial, clasificadores y etiquetas— y aplica acciones de protección donde los datos se usan o se mueven. Hoy organiza sus ubicaciones en dos familias: **aplicaciones y dispositivos empresariales** (Exchange, SharePoint, OneDrive, chats y canales de Teams, apps de Office, Windows 10/11 y las tres últimas versiones de macOS, apps no Microsoft, repositorios locales, Fabric y Power BI, Microsoft 365 Copilot y apps en la nube gestionadas) y **tráfico web en línea** (Edge for Business y la red, que alcanza más de 35.000 apps del catálogo de Defender for Cloud Apps).

Saber qué ubicación cubre qué riesgo es tan importante como saber qué licencia la habilita. Microsoft 365 E3 incluye DLP para Exchange, SharePoint y OneDrive; Teams, Endpoint DLP y las sugerencias avanzadas de Outlook requieren Microsoft 365 E5, Microsoft Purview Suite o E5 Information Protection & Governance; y la red con socios, el navegador hacia apps no gestionadas y los datos fuera de Microsoft 365 se suman con **pago por uso**, que complementa y no reemplaza la licencia por usuario. Microsoft 365 E7 incluye todo lo de E5 y agrega Microsoft 365 Copilot, Entra Suite y Agent 365.

El mapa también se mueve: la ubicación clásica «Instances» de Defender for Cloud Apps se retira el 6 de enero de 2027 y su reemplazo, las apps no Microsoft conectadas, está en vista previa desde agosto de 2026. Este módulo te deja la [Matriz de cobertura de DLP](00_Programa.md#cobertura-dlp) y la tabla de [Licencias](00_Programa.md#licencias) aplicadas a tu organización.

**Por qué importa**

Elegir mal la ubicación o suponer una licencia que no tienes produce huecos invisibles: un equipo cree que protege los chats de Teams con E3 o que la red está cubierta sin pago por uso. La matriz de cobertura convierte el riesgo de negocio en decisiones concretas de ubicación, licencia y presupuesto, y es la base de la conversación con compras, con el equipo de cuenta y con la dirección.

**Qué vas a lograr**

- Describir las dos familias de ubicaciones de DLP y qué protege cada una.
- Distinguir qué incluye Microsoft 365 E3, qué agrega E5 o Purview Suite y qué requiere E7, complementos o pago por uso.
- Explicar las limitaciones de Fabric y Power BI, los repositorios locales y las apps no Microsoft.
- Planificar la migración de la ubicación «Instances» antes del 6 de enero de 2027.
- Construir la matriz de cobertura de tu organización con sus brechas.

> **Atención.** Licencias según la [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description), verificada el 6 de noviembre de 2026: DLP de Exchange, SharePoint y OneDrive desde Microsoft 365 E3 (también Business Premium y los planes 2 de cada servicio); Teams y Endpoint DLP requieren Microsoft 365 E5/A5/G5, Microsoft Purview Suite o E5 Information Protection & Governance, y Teams además el plan de servicio «Microsoft Communications DLP» habilitado en la licencia de cada persona. El detalle está en la tabla [Licencias](00_Programa.md#licencias).

> **Qué cambió.** La ubicación clásica «Instances» de Defender for Cloud Apps se retira el **6 de enero de 2027**, junto con las directivas de archivos de Defender for Cloud Apps ([Instances](https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps), [migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview)). Su reemplazo, las [apps no Microsoft conectadas](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications), está en vista previa desde agosto de 2026: solo reglas avanzadas, sin sugerencias, invalidaciones, simulación ni unidades administrativas, y no clasifica archivos cifrados ni PDF.

> **Novedad.** Aclaración de agosto de 2026: en los chats de Teams con acceso externo aplica la DLP del tenant que inició la conversación; en los canales compartidos, cada persona se evalúa con la DLP de su propio tenant ([DLP y Teams](https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams)).

> **Atención.** Fabric y Power BI: solo áreas de trabajo en capacidad Fabric o Premium, solo plantilla personalizada, sin EDM, clasificadores entrenables, credenciales ni entidades con nombre, sin modelos DirectQuery o live connection, y la acción «restringir acceso» en vista previa; además, la evaluación consume capacidad ([DLP para Fabric y Power BI](https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started), 22 de julio de 2026). En repositorios locales, todas las personas que agregan o consumen archivos del repositorio necesitan licencia, no solo la cuenta del escáner ([repositorios locales](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-get-started)).

**¿Tienes poco tiempo?**

- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · Documentación
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación

### Documentación, cursos y credenciales

- [Get started with DLP for Fabric and Power BI](https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jul 2026. Cómo funcionan las directivas DLP para áreas de trabajo de Fabric y Power BI: eventos que disparan la evaluación, tipos de elementos admitidos, acciones (sugerencia, alerta, restringir acceso) y limitaciones.
- [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Artículo base de DLP en Purview: qué es, cómo analiza contenido, las dos familias de ubicaciones (aplicaciones y dispositivos empresariales vs. tráfico web en línea) y el ciclo planificar-diseñar-desplegar-investigar.
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn (Service Descriptions). Descripción de servicio oficial que define qué licencias dan derecho a cada capacidad DLP: Exchange/SharePoint/OneDrive desde E3; Teams, Endpoint, navegador y red con E5, Purview Suite o E5 IP&G; Copilot por etiquetas solo E5, prompts para todos.
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación · Oficial · Microsoft Learn. Explica los dos modelos complementarios: licencia por usuario para Microsoft 365 y endpoints Windows/macOS, y pago por uso (facturado vía Azure) para datos no Microsoft 365, red, apps/agentes de IA y otras capacidades.
- [Migrate file policies to Microsoft Purview](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) · Documentación · Oficial · Microsoft Learn (Defender for Cloud Apps). Guía oficial para migrar las directivas de archivos de Defender for Cloud Apps a DLP o autoetiquetado de Purview antes de su retiro el 6-ene-2027, con asistente de migración y tabla de paridad.
- [Data loss prevention and Microsoft Teams](https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams) · Documentación · Oficial · Microsoft Learn. DLP en chats y canales de Teams: escenarios, licencias (chats requieren E5), alcance por tipo de grupo, sugerencias de directiva y reglas para canales compartidos y chats entre tenants.
- [Use Microsoft Purview data loss prevention policies for non-Microsoft connected apps (preview)](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 28 ago 2026. Nueva ubicación (preview) para proteger datos en reposo en SaaS de terceros (Box, Dropbox, Google Workspace, Salesforce, AWS, Cisco Webex, ServiceNow) usando los conectores de Defender for Cloud Apps y el mismo motor de clasificación de Microsoft 365. *Nota:* Preview (actualizado 28-ago-2026), despliegue por fases. Apps: Box, Dropbox, Google Workspace, Salesforce, AWS, Cisco Webex, ServiceNow vía conectores de Defender for Cloud Apps. Solo plantilla personalizada y reglas avanzadas; no combina con otras ubicaciones…
- [Microsoft Purview licensing guidance](https://www.microsoft.com/licensing/guidance/Microsoft-Purview) · Documentación · Oficial · Microsoft Licensing Resources. Guía de licenciamiento de Purview: modelo por usuario (planes Microsoft 365 y add-ons como Microsoft Purview Suite) más pago por uso para datos fuera de Microsoft 365, con reglas de multiplexación y reasignación a 90 días.
- [Get started with data loss prevention for on-premises repositories](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-get-started) · Documentación · Oficial · Microsoft Learn. Prerrequisitos y pasos para usar la ubicación de repositorios locales: cliente y escáner de Information Protection, trabajo de escaneo con reglas DLP, ejecución del escaneo y directiva en simulación.
- [Learn about data loss prevention on-premises repositories](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn) · Documentación · Oficial · Microsoft Learn · 31 mar 2025. Ubicación de repositorios locales: DLP sobre recursos compartidos y bibliotecas SharePoint on-premises mediante el escáner de Information Protection, con cuatro acciones de protección (bloqueos, herencia de permisos, cuarentena).
- [Use DLP policies for non-Microsoft cloud apps](https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 28 ago 2026. Ubicación clásica "Instances" que aplica directivas DLP a apps en la nube conectadas a Defender for Cloud Apps (Box, Dropbox, Google Workspace, Salesforce, Webex, AWS, ServiceNow), creando la directiva espejo en Defender for Cloud Apps. *Nota:* Se retira el 6-ene-2027 junto con las directivas de archivos de Defender for Cloud Apps; recrear en las ubicaciones dedicadas de apps no Microsoft conectadas (preview) antes de esa fecha

### Laboratorios, GitHub y herramientas

- [Microsoft Purview Pricing](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Herramienta · Oficial · Microsoft Security. Página de precios: Microsoft 365 E5 (USD 60 usuario/mes con Teams) incluye Purview premium y Security Copilot; Microsoft Purview Suite (USD 12) es el add-on sobre E3 con DLP; las ofertas de consumo requieren suscripción Azure.

**Manos a la obra**

1. `Laboratorio` Lee [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp) y completa, para tu organización, la [Matriz de cobertura de DLP](00_Programa.md#cobertura-dlp): qué ubicaciones usas, qué riesgo cubre cada una y qué licencia tienes. Evidencia: matriz con las brechas marcadas.
2. `Laboratorio` Con la [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) y los [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models), clasifica diez escenarios de tu negocio en «incluido en E3», «requiere E5 o Purview Suite», «requiere E7 o complemento» y «pago por uso». Evidencia: tabla revisada con tu equipo de licenciamiento.
3. `Laboratorio` Crea en simulación una directiva para chats y canales de Teams y otra para SharePoint y OneDrive, comparte en Teams un archivo sintético y comprueba que se evalúa por SharePoint y OneDrive ([DLP y Teams](https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams)). Evidencia: capturas de ambos paneles de simulación.
4. `Laboratorio parcial` Repositorios locales: en una VM Windows Server de Azure con un recurso SMB, instala el escáner de Information Protection (con SQL Express), crea un trabajo de escaneo con reglas DLP y Enforce en Off y luego una directiva en simulación ([guía](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-get-started)). Limitación: costo de la VM y de SQL, y la ubicación no ofrece sugerencias de directiva. Evidencia: informe del escaneo con coincidencias.
5. `Laboratorio parcial` Fabric y Power BI: activa una capacidad de prueba de Fabric, crea una directiva personalizada sobre un área de trabajo y verifica la sugerencia y la alerta al publicar un modelo semántico con datos sintéticos ([guía](https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started)). Limitación: solo con capacidad Fabric o Premium y con «restringir acceso» en vista previa. Evidencia: captura de la sugerencia en el área de trabajo.
6. `Laboratorio parcial` Apps no Microsoft conectadas (vista previa): conecta una cuenta de prueba de Box o Google Workspace a Defender for Cloud Apps y crea una regla avanzada solo con notificaciones ([guía](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications)). Limitación: sin simulación ni sugerencias, por lo que debes usar una instancia de prueba. Evidencia: regla creada y evento registrado.
7. `Solo producción` Inventaria las directivas de la ubicación «Instances» y las directivas de archivos de Defender for Cloud Apps de tu tenant y planifica su migración antes del 6 de enero de 2027 con el asistente y la tabla de paridad; considera que Purview no modifica el uso compartido existente y aplica el alcance por sitio, no por carpeta ([migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview)). Cómo hacerlo seguro: inventario con rol de solo lectura, recreación de cada directiva en la nueva ubicación solo con notificaciones para un grupo piloto, comparación de resultados durante dos semanas y retiro de la original solo después.

**¿Quieres profundizar?**

- [Microsoft Purview Pricing](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Herramienta

<a id="i2"></a>

## I2 · Diseño de directivas y modo de simulación

*L100–L200 · ~6 h · Origen: Ruta Ninja de Learn, módulo 4, y ruta oficial de DLP para SC-401*

Una buena directiva DLP empieza como una frase, no como una casilla. La metodología oficial propone redactar una **declaración de intención** —qué quieres proteger, de quién, dónde y qué debe pasar— y traducirla a la configuración: alcance, ubicaciones, condiciones, excepciones, acciones, notificaciones e informes de incidentes. Conocer los límites de la plataforma evita sorpresas: 600 reglas DLP por tenant, 100 KB por directiva y por regla, solo los primeros 2 millones de caracteres de cada elemento y nombres de hasta 64 caracteres.

El **modo de simulación**, que reemplazó a los antiguos estados de prueba, ejecuta la directiva sin aplicar acciones y muestra las coincidencias en un panel propio; sus alertas no llegan al panel de alertas DLP ni a Defender, y conserva 30 días de datos. Puedes simular con o sin sugerencias de directiva y configurar la activación automática si nadie la modifica en 15 días. El patrón profesional es copiar la directiva (v2), ajustarla en simulación y conmutar cuando cumpla el criterio de salida acordado con el dueño del proceso.

**Por qué importa**

Una directiva que bloquea sin haber sido simulada puede detener la facturación, la nómina o una licitación en minutos, y el costo de esa interrupción supera al de muchos incidentes. Simular en todas las ubicaciones, educar primero con sugerencias de directiva y activar con un criterio de salida acordado reduce las interrupciones, aumenta la aceptación del programa y deja evidencia de diligencia.

**Qué vas a lograr**

- Redactar una declaración de intención y traducirla a una directiva DLP.
- Aplicar los límites de la plataforma y el orden de evaluación al diseño de reglas.
- Ejecutar una directiva en modo de simulación e interpretar su panel.
- Explicar dónde aparecen y dónde no las sugerencias de directiva.
- Definir un criterio de salida de la simulación con el dueño del proceso.

> **Consejo Ninja.** Límites que condicionan el diseño: 600 reglas DLP por tenant, 10.000 directivas MIP+MIG, 100 KB por directiva y por regla, se escanean los primeros 2 millones de caracteres y hasta tres niveles de anidación, nombres de directiva y de regla de 64 caracteres y 16.384 caracteres para la configuración de Endpoint DLP ([referencia de directivas](https://learn.microsoft.com/en-us/purview/dlp-policy-reference)). Hay cuatro directivas predeterminadas: la de Office 365 (tarjetas de crédito compartidas externamente), la de Teams, la de dispositivos (solo auditoría) y la de la ubicación Microsoft 365 Copilot.

> **Atención.** En simulación las acciones no se aplican y «Stop processing more rules» no funciona; las alertas de simulación no llegan al panel de alertas DLP ni a Defender, y para ver elementos de endpoints hace falta la recolección de evidencia ([simulación](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn), [primeros pasos](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started)). En Exchange, Teams y dispositivos solo se evalúan elementos nuevos: genera actividad después de iniciar la simulación.

> **Atención.** No hay sugerencias de directiva en los clientes de escritorio de SharePoint y OneDrive, en las apps móviles de Office, en apps de terceros ni on-premises, y en Teams no se muestran para archivos ([referencia de sugerencias](https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference)). Outlook clásico solo procesa los primeros 4 MB del mensaje y hasta 2 MB de adjuntos para las sugerencias y, sin E5, necesita el plan «Information Protection for Office 365 - Premium» ([sugerencias en Outlook](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips)).

> **Novedad.** Desde abril de 2026 puedes exportar la configuración de directivas DLP y de etiquetas a un ZIP con XML, útil para soporte, control de cambios y análisis ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). En vista previa también puedes renombrar directivas y reglas, aunque los registros anteriores conservan el nombre previo ([crear y desplegar](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy)).

**¿Tienes poco tiempo?**

- [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) · Documentación
- [Learn about data loss prevention simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) · Documentación
- [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference) · Documentación

### Documentación, cursos y credenciales

- [Plan for data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp) · Documentación · Oficial · Microsoft Learn. Buenas prácticas de planificación DLP: identificar partes interesadas, categorías de información sensible, objetivos, estrategia y enfoques de despliegue.
- [Design a data loss prevention policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) · Documentación · Oficial · Microsoft Learn. Metodología para redactar una declaración de intención de directiva y mapearla a la configuración (qué monitorear, alcance, dónde, condiciones y acciones).
- [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference) · Documentación · Oficial · Microsoft Learn. Anatomía completa de una directiva DLP: límites de plataforma, directivas predeterminadas, plantillas, alcance, reglas, condiciones, excepciones, acciones, notificaciones, invalidaciones e informes de incidentes.
- [Create and deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) · Documentación · Oficial · Microsoft Learn. Escenarios guiados de creación y despliegue de directivas (correo con tarjetas, uso compartido externo, Endpoint, Power BI, Edge for Business, red) y controles de estado/alcance para desplegar sin interrumpir el negocio.
- [Get started with data loss prevention simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started) · Documentación · Oficial · Microsoft Learn. Procedimiento para poner directivas en simulación (con o sin sugerencias), activarlas automáticamente tras 15 días sin cambios e interpretar el estado de escaneo por ubicación.
- [Data Loss Prevention policy tips reference](https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference) · Documentación · Oficial · Microsoft Learn. Matriz de soporte de sugerencias de directiva DLP por aplicación y plataforma (Outlook, OWA, nuevo Outlook, SharePoint/OneDrive web, Office, Teams, endpoints Windows y macOS), con condiciones y SIT admitidos.
- [Learn about data loss prevention simulation mode](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn) · Documentación · Oficial · Microsoft Learn · 14 mar 2025. Explica el modo de simulación, que reemplazó a los estados "Test": ejecuta la directiva sin aplicar acciones y muestra coincidencias y alertas en un panel separado.

### Laboratorios, GitHub y herramientas

- [SC-401T00 Information Security Administrator - Labs](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs) · GitHub · Oficial · Microsoft Learning · MicrosoftLearning (GitHub). Laboratorios oficiales del curso SC-401T00 con ejercicios de directivas DLP, Endpoint DLP, Adaptive Protection, DSPM para IA y validación de directivas.

**Manos a la obra**

1. `Laboratorio` Redacta la declaración de intención de una directiva para un caso real de tu país (por ejemplo, «impedir que documentos con datos de tarjetas de clientes se compartan fuera de la organización por correo o enlaces») y tradúcela a alcance, ubicaciones, condiciones, excepciones y acciones con la [metodología de diseño](https://learn.microsoft.com/en-us/purview/dlp-policy-design). Evidencia: ficha de diseño de una página.
2. `Laboratorio` Crea desde la plantilla de datos personales de tu país una directiva para Exchange, SharePoint y OneDrive en modo de simulación con sugerencias de directiva, nombrada `PRUEBA-DLP-<país>-v1-202611` ([crear y desplegar](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy), [simulación](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-get-started)). Evidencia: captura del panel de simulación con el estado de escaneo por ubicación.
3. `Laboratorio` Genera actividad con las personas de prueba (correos y archivos compartidos con datos sintéticos que coinciden y que no coinciden) y, al día siguiente, revisa las coincidencias por regla. Practica el patrón «copiar la directiva (v2), ajustar y conmutar»: crea la v2, cambia un umbral y compara ([simulación](https://learn.microsoft.com/en-us/purview/dlp-simulation-mode-learn)). Evidencia: tabla v1 frente a v2 con coincidencias por regla.
4. `Laboratorio` Prueba las sugerencias de directiva en Outlook en la web, el nuevo Outlook y SharePoint en la web, y documenta dónde no aparecen (OneDrive de escritorio, apps móviles de Office y apps de terceros) con la [referencia de sugerencias](https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference). Evidencia: matriz de sugerencias observadas con capturas.
5. `Laboratorio` Exporta la configuración de directivas a ZIP y guárdala como línea base antes de cualquier cambio ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)). Evidencia: archivo ZIP con fecha y una nota de lo que contiene.
6. `Solo producción` Define con un dueño de proceso real el criterio de salida de la simulación (por ejemplo, menos de 5 % de coincidencias revisadas como falso positivo durante dos semanas) y activa la directiva por ubicación, primero con sugerencias y después con bloqueo con invalidación. Cómo hacerlo seguro: copia v2 en simulación sin tocar la productiva, grupo piloto, aprobación del dueño del proceso y de seguridad, ventana de cambio y reversión inmediata devolviendo la directiva a simulación.

**¿Quieres profundizar?**

- [SC-401T00 Information Security Administrator - Labs](https://github.com/MicrosoftLearning/SC-401T00-Information-Security-Administrator/tree/master/Instructions/Labs) · GitHub

<a id="i3"></a>

## I3 · DLP en endpoints y navegadores

*L100–L200 · ~8 h · Origen: Ruta Ninja de Learn, módulo 5 (Endpoint DLP y Conditional Access App Control)*

**Endpoint DLP** extiende las directivas a Windows 10/11 y a las tres últimas versiones de macOS: audita o restringe copiar a USB, imprimir, subir a la nube, usar el portapapeles, copiar a recursos de red, RDP, Bluetooth y, en disponibilidad general desde octubre de 2026, las transferencias FTP y SFTP. La incorporación es compartida con Defender for Endpoint y admite Intune, directiva de grupo, Configuration Manager, script local, VDI no persistente y, en macOS, Intune o JAMF. Desde junio de 2026 puedes acotar directivas por grupos de dispositivos dinámicos de Entra.

La **protección just-in-time (JIT)** cubre el hueco de los archivos que todavía no se clasificaron: protege las salidas mientras termina la evaluación, requiere el cliente antimalware 4.18.23080 o posterior y no genera eventos DLPRuleMatch ni alertas. En el navegador hay dos caminos: la extensión de Purview para Chrome en Windows y la **protección en línea de Edge for Business**, que no necesita incorporar el dispositivo y distingue apps gestionadas (incluidas en E5) de apps no gestionadas o de IA (pago por uso). La red, Copilot y los agentes llegan en [M3](02_Nivel_2_Intermedio.md#m3).

**Por qué importa**

Buena parte de la fuga real ocurre en el endpoint: el USB de quien renuncia, el contrato pegado en un chatbot o la carga a una nube personal. Endpoint DLP y la protección en el navegador cierran esos caminos con evidencia de cada intento, y el despliegue por fases —auditoría, grupo piloto, invalidación con justificación— evita frenar procesos legítimos como la impresión en planta, los respaldos o las transferencias SFTP con bancos.

**Qué vas a lograr**

- Incorporar un equipo Windows 11 y verificar su estado y la sincronización de directivas.
- Configurar las opciones globales de Endpoint DLP: grupos de USB, impresoras, recursos de red, dominios y exclusiones.
- Desplegar la protección just-in-time por fases y medir su impacto.
- Comparar la extensión para Chrome y la protección en línea de Edge for Business, con sus requisitos y licencias.
- Planificar Endpoint DLP en macOS, incluidos los cambios de permisos de macOS 27.

> **Novedad.** Octubre de 2026: Endpoint DLP monitorea y restringe transferencias FTP y SFTP en disponibilidad general; la actividad no viene activa por defecto y la guía recomienda un piloto en solo auditoría ([FTP y SFTP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-ftp-sftp-short), [novedades](https://learn.microsoft.com/en-us/purview/whats-new)). En junio de 2026 llegaron el alcance por grupos de dispositivos dinámicos de Entra y la columna `DlpInfo` de `DeviceInfo`, consultable con búsqueda avanzada.

> **Atención.** Edge for Business (página del 15 de septiembre de 2026): las apps gestionadas (SSO de Entra) se protegen en dispositivos gestionados y no gestionados, solo en el perfil de trabajo y mediante Conditional Access app control; las apps no gestionadas o de IA (ChatGPT de consumo, Gemini, DeepSeek, Copilot de consumo y otras), solo en Windows 10/11 gestionados por Intune, en todos los perfiles. Requiere Edge 144 o posterior, no aplica a invitados B2B ni a tenants con aprobación multiadministrador de Intune, y si hay conflicto prevalece Endpoint DLP ([DLP en Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn)).

> **Atención.** Licencias del navegador: proteger lo que va de dispositivos gestionados a apps no gestionadas en Edge for Business es **pago por uso**; los escenarios con apps gestionadas registradas en Entra están incluidos en E5 o equivalente ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). En macOS, la descripción de servicio dice «Catalina 10.15 y superior» y Learn, «las tres versiones más recientes»: planifica con la más restrictiva y prepara los cambios de permisos de macOS 27 (cliente 101.26072 o posterior, vista previa de agosto de 2026).

> **Consejo Ninja.** La protección just-in-time no genera eventos DLPRuleMatch ni alertas y deja el portapapeles en auditoría por defecto ([JIT](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit)). Despliégala por fases con la acción de reserva «permitir» y mide el impacto en el explorador de actividad antes de pasar a bloqueo ([primeros pasos con JIT](https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit)).

**¿Tienes poco tiempo?**

- [Get started with endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started) · Documentación
- [Endpoint DLP policy scenarios in Microsoft Purview](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using) · Laboratorio
- [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · Documentación

**Endpoint DLP, extensión para Chrome y Edge for Business: qué elegir**

| Opción | Requisitos | Qué controla | Licencia | Fuente |
|---|---|---|---|---|
| Endpoint DLP | Dispositivo incorporado (Windows 10/11 o macOS); en Windows, cliente antimalware 4.18.2110 o posterior con protección en tiempo real | USB, impresión, nube, portapapeles, recursos de red, RDP, Bluetooth, FTP/SFTP y pegado en el navegador | E5, Purview Suite o E5 IP&G | [Primeros pasos](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started) |
| Protección just-in-time | Endpoint DLP y cliente antimalware 4.18.23080 o posterior | Salidas de archivos aún no clasificados o con clasificación obsoleta; no genera DLPRuleMatch ni alertas | La de Endpoint DLP | [JIT](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit) |
| Extensión de Purview para Chrome | Windows 10/11 incorporado; despliegue manual, con Intune o por directiva de grupo | Subida a la nube, impresión, portapapeles, USB y recursos de red desde Chrome | La de Endpoint DLP | [Extensión para Chrome](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about) |
| Edge for Business con apps gestionadas | Edge 144 o posterior, perfil de trabajo y Conditional Access app control; dispositivos gestionados o no gestionados | Subir texto y archivos, descargar, copiar, pegar e imprimir en apps con SSO de Entra | Incluida en E5 o equivalente | [Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) |
| Edge for Business con apps no gestionadas o de IA | Windows 10/11 gestionados por Intune, todos los perfiles; sin aprobación multiadministrador de Intune; sin invitados B2B | Las mismas actividades hacia apps de IA de consumo y otras apps no gestionadas | Pago por uso | [Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · [Descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) |

Si una actividad está cubierta a la vez por Endpoint DLP y por la directiva en línea de Edge for Business, prevalece Endpoint DLP. Fuentes: páginas de Learn citadas en cada fila, verificadas al 6 de noviembre de 2026.

### Documentación, cursos y credenciales

- [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn) · Documentación · Oficial · Nuevo · Microsoft Learn · 15 sep 2026. DLP integrado en Edge for Business sin incorporar el dispositivo: protege apps gestionadas (SSO Entra) en dispositivos gestionados y no gestionados, y apps no gestionadas/IA (ChatGPT, Gemini, DeepSeek, Copilot consumer, etc.) desde dispositivos Intune.
- [Get started with endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 21 ago 2026. Requisitos e incorporación de dispositivos a Endpoint DLP: Windows 10/11 (GPO, ConfigMgr, Intune, script, VDI no persistente) y macOS (Intune o JAMF, con o sin Defender for Endpoint).
- [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about) · Documentación · Oficial · Microsoft Learn. Conceptos de Endpoint DLP: cuándo se clasifican los archivos, actividades monitoreables, soporte Windows 10/11, macOS (3 últimas) y Windows Server 2019+, comportamiento offline y JIT.
- [Configure endpoint data loss prevention settings](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings) · Documentación · Oficial · Microsoft Learn. Configuración central de Endpoint DLP: clasificación avanzada en la nube, exclusiones de rutas, apps restringidas y grupos, Bluetooth, restricciones de navegadores y dominios, grupos de impresoras/USB/recursos de red, VPN y servidores.
- [Protect FTP and SFTP transfers with Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-ftp-sftp-short) · Documentación · Oficial · Nuevo · Microsoft Learn · 20 oct 2026. Cómo agregar la actividad "transferencias FTP y SFTP" a reglas de Endpoint DLP en Windows gestionados (auditar, bloquear, bloquear con invalidación, permitir) y revisarla en Activity explorer con evidencia completa opcional.
- [Learn about Endpoint DLP just-in-time protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit) · Documentación · Oficial · Microsoft Learn. Conceptos de la protección just-in-time: bloquea o audita salidas (USB, red, impresión, RDP, Bluetooth, portapapeles, subida a dominios restringidos) mientras se completa la clasificación de archivos no evaluados o con clasificación obsoleta.
- [Get started with Endpoint DLP Just-in-time protection](https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit) · Documentación · Oficial · Microsoft Learn. Guía de despliegue por fases de JIT: cliente antimalware 4.18.23080+, alcance, acción de reserva "permitir", estimación de impacto N/S con Activity explorer y exclusiones.
- [Learn about the Microsoft Purview extension for Chrome](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about) · Documentación · Oficial · Microsoft Learn · 6 oct 2025. Extensión de Purview para Chrome en Windows 10/11 que permite auditar o bloquear subida a la nube, impresión, portapapeles, USB y recursos de red desde Chrome.

### Laboratorios, GitHub y herramientas

- [Endpoint DLP policy scenarios in Microsoft Purview](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using) · Laboratorio · Oficial · Nuevo · Microsoft Learn · 26 jun 2026. Escenarios guiados de Endpoint DLP: crear desde plantilla en auditoría con simulación, agregar alertas, bloquear con invalidación y validar en Activity explorer.

**Manos a la obra**

1. `Laboratorio` Incorpora una VM Windows 11 de Azure (unida o registrada en Entra, con cliente antimalware 4.18.2110 o posterior y protección en tiempo real) con el script local o con Intune, y verifica *Configuration status* y *Policy sync status* ([primeros pasos](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started), [incorporación](https://learn.microsoft.com/en-us/purview/device-onboarding-overview)). En una VM, la copia a USB se registra como copia a recurso compartido de red. Evidencia: equipo visible en la lista de dispositivos con la sincronización correcta.
2. `Laboratorio` Ejecuta en orden los escenarios oficiales: directiva desde plantilla en auditoría con simulación, alerta por datos personales, bloqueo con invalidación y pegado en el navegador; valida cada uno en el explorador de actividad ([escenarios de Endpoint DLP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-using)). Si en tu organización se usa Chrome, despliega antes la [extensión de Purview para Chrome](https://learn.microsoft.com/en-us/purview/dlp-chrome-learn-about). Evidencia: cuatro eventos con su regla y su acción.
3. `Laboratorio` Configura las opciones globales: un grupo de USB autorizados, un grupo de impresoras, un recurso de red permitido, la exclusión de una ruta y un dominio de servicio restringido ([configuración de Endpoint DLP](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings)). Evidencia: captura de la configuración y un evento permitido gracias a un grupo.
4. `Laboratorio` Despliega JIT por fases: verifica la versión del cliente antimalware con la consulta KQL de la guía, activa JIT para la VM con la acción de reserva «permitir» y mide en el explorador de actividad cuántos archivos se evaluaron y qué se habría bloqueado ([JIT](https://learn.microsoft.com/en-us/purview/endpoint-dlp-get-started-jit)). Evidencia: resultado de la consulta y conteo de eventos.
5. `Laboratorio` Agrega la actividad «transferencias FTP y SFTP» en solo auditoría, transfiere un archivo sintético a un servidor SFTP de prueba y revisa el evento con su evidencia ([FTP y SFTP](https://learn.microsoft.com/en-us/purview/endpoint-dlp-ftp-sftp-short)). Evidencia: evento en el explorador de actividad.
6. `Laboratorio parcial` Edge for Business: desde la VM gestionada por Intune, crea una directiva que primero audite y luego bloquee pegar o subir datos sintéticos a una app de IA no gestionada ([Edge for Business](https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn)). Limitación: es pago por uso —vincula una suscripción de Azure del mismo tenant con presupuesto, porque la cobertura por el crédito de Visual Studio no está confirmada— y no funciona si el tenant usa aprobación multiadministrador de Intune. Evidencia: evento de auditoría, evento de bloqueo y consumo en el [uso de pago por uso](https://learn.microsoft.com/en-us/purview/purview-billing-usage).
7. `Laboratorio parcial` Endpoint DLP en macOS: requiere un Mac físico, porque el presupuesto de Azure del laboratorio no cubre VM macOS. Incorpóralo con Intune o JAMF, aplica una directiva solo de auditoría y revisa los permisos que pide macOS 27 ([primeros pasos](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)). Limitación: sin Mac no hay práctica; en producción, usa un Mac de prueba dentro de un grupo de dispositivos piloto. Evidencia: Mac incorporado y un evento auditado.
8. `Solo producción` Despliega Endpoint DLP en equipos reales por oleadas. Cómo hacerlo seguro: grupo de dispositivos piloto con personas voluntarias informadas, directiva en auditoría durante dos semanas, revisión con sus dueños de los procesos críticos (impresión en planta, respaldos a USB, transferencias SFTP a bancos), bloqueo con invalidación y justificación antes del bloqueo total, y revisión semanal del [panel de salud de dispositivos](https://learn.microsoft.com/en-us/purview/device-onboarding-health-reports-dashboard).

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primera directiva de punta a punta.** En el laboratorio, redacta la declaración de intención de una directiva para un dato crítico de tu país (por ejemplo, identificadores fiscales de clientes), créala en simulación para Exchange, SharePoint, OneDrive, Teams y dispositivos, incorpora la VM Windows 11 y genera actividad que coincida y que no. Entregables: ficha de diseño, matriz de cobertura y de licencias de tu organización, panel de simulación con coincidencias por ubicación, criterio de salida propuesto y la lista de brechas que E3 no cubre.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué licencia otorga derecho a DLP para chats y canales de Microsoft Teams?
   - a) Microsoft 365 E3
   - b) Exchange Online Plan 2
   - c) Microsoft 365 E5, Microsoft Purview Suite o E5 Information Protection & Governance
   - d) Microsoft 365 Business Premium

2. ¿Qué ocurre con la ubicación «Instances» de Defender for Cloud Apps en DLP?
   - a) Pasó a disponibilidad general en 2026
   - b) Se fusiona con la ubicación de red
   - c) Seguirá sin cambios
   - d) Se retira el 6 de enero de 2027 y sus directivas deben recrearse como apps no Microsoft conectadas

3. ¿Cuántas reglas DLP admite un tenant?
   - a) 100
   - b) 600
   - c) 10.000
   - d) Ilimitadas

4. ¿Qué afirmación sobre el modo de simulación es correcta?
   - a) Sus alertas llegan a Defender XDR como incidentes de severidad baja
   - b) Aplica las acciones solo al grupo piloto
   - c) «Stop processing more rules» funciona igual que en modo activo
   - d) No aplica acciones y sus alertas no llegan al panel de alertas DLP ni a Defender

5. ¿En cuál de estos clientes NO se muestran sugerencias de directiva DLP?
   - a) Outlook en la web
   - b) SharePoint en la web
   - c) Cliente de escritorio de OneDrive
   - d) Nuevo Outlook

6. ¿Dónde aplican las directivas de Edge for Business para apps de IA no gestionadas?
   - a) En cualquier dispositivo con Edge
   - b) En Windows 10/11 gestionados por Intune, en todos los perfiles de Edge
   - c) Solo en el perfil de trabajo de dispositivos no gestionados
   - d) Solo en Mac gestionados con JAMF

7. ¿Qué es cierto sobre la protección just-in-time de Endpoint DLP?
   - a) Protege las salidas mientras se clasifica un archivo no evaluado y no genera eventos DLPRuleMatch ni alertas
   - b) Genera eventos DLPRuleMatch y alertas como cualquier regla
   - c) Solo funciona en macOS
   - d) Requiere pago por uso

8. ¿Qué cambió en Endpoint DLP en octubre de 2026?
   - a) Se retiró el soporte para macOS
   - b) Se retiró la extensión de Purview para Chrome
   - c) Llegó a disponibilidad general el control de transferencias FTP y SFTP
   - d) El alcance por grupos de dispositivos volvió a vista previa

9. Quieres impedir con Edge for Business que, desde equipos gestionados, se peguen datos sensibles en una app de IA no gestionada. ¿Cómo se licencia ese escenario?
   - a) Está incluido en Microsoft 365 E3
   - b) Solo requiere Entra ID P1
   - c) Requiere obligatoriamente Microsoft 365 E7
   - d) Es pago por uso, facturado mediante una suscripción de Azure

10. ¿Qué rol de mínimo privilegio permite editar las directivas DLP de la ubicación Copilot sin leer prompts ni respuestas?
   - a) Global Administrator
   - b) Compliance Administrator
   - c) Purview Data Security AI Admin
   - d) Security Reader

11. ¿Qué condición debe cumplir un tenant para iniciar la prueba de Microsoft Purview Suite?
   - a) Tener Microsoft 365 E3, u Office 365 E3 con EMS E3, y no tener E5
   - b) Tener Microsoft 365 E5
   - c) Estar en una nube de Government
   - d) Tener al menos 300 usuarios

12. ¿Qué ofrece la ruta Ninja oficial de Purview en Microsoft Learn?
   - a) Un examen final con certificado al 80 %
   - b) Cinco módulos con evaluación por módulo y una insignia
   - c) Un tenant de laboratorio incluido
   - d) Una certificación de Microsoft

13. ¿Qué es cierto sobre DLP para Fabric y Power BI?
   - a) Solo admite áreas de trabajo en capacidad Fabric o Premium y solo la plantilla personalizada
   - b) Admite EDM y clasificadores entrenables
   - c) Admite modelos DirectQuery y live connection
   - d) La evaluación no consume capacidad

14. ¿Qué afirmación sobre el pago por uso de Purview es correcta?
   - a) Reemplaza a la licencia por usuario
   - b) Se suma a la licencia por usuario y se factura mediante una suscripción de Azure
   - c) Solo aplica a Microsoft 365 Copilot
   - d) Es gratuito mientras la función esté en vista previa

15. Asignaste un rol de Purview mediante PIM para grupos. ¿Cuánto pueden tardar los permisos en hacerse efectivos?
   - a) Se aplican al instante
   - b) 24 horas
   - c) 7 días
   - d) Hasta 2 horas

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre monitoreo, evidencias, privacidad y normativa corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

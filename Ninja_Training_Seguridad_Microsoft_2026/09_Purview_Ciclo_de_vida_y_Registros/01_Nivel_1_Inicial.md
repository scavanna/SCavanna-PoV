# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview Ciclo de vida de los datos y Gestión de registros Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Portal, licencias y roles; principios de retención, directivas, etiquetas y ámbitos adaptables; retención en cada carga de trabajo; registros y plan de archivos. Terminas con una arquitectura de retención de base y un plan de archivos importado en tu laboratorio.

*L100–L200 · 5 módulos · ~16 horas · 32 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos y licencias](#p0) · [I0 Cómo aprender](#i0) · [I1 Directivas y etiquetas](#i1) · [I2 Retención por carga de trabajo](#i2) · [I3 Registros y plan de archivos](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, licencias y roles

*L100–L200 · ~2 h · Origen: Ninja oficial de ciclo de vida y registros (2023): introducción, primeros pasos, licencias y permisos*

Microsoft Purview reúne en un mismo portal las soluciones de gobierno y cumplimiento de Microsoft 365. Dos de ellas son el centro de este programa: **Data Lifecycle Management (DLM)**, el nuevo nombre de Microsoft Information Governance, que te ayuda a conservar lo que debes y eliminar lo que ya no necesitas, y **Records Management**, reservado para el contenido de alto valor con obligaciones legales, regulatorias o de negocio: plan de archivos, registros, revisión de eliminación y prueba de eliminación. Ambas comparten el mismo motor de retención —directivas, etiquetas y ámbitos— que usarás en todo el recorrido.

Antes de configurar nada conviene resolver tres preguntas: qué incluye tu licencia, quién tiene permisos y qué funciones heredadas conviven en tu tenant. La retención básica está en Microsoft 365 E3, pero los ámbitos adaptables, el plan de archivos, los registros, los eventos y la revisión de eliminación exigen nivel E5. Los permisos se asignan con grupos de roles de Purview —Retention Management, Records Management y sus variantes de solo lectura— que desde julio de 2026 pueden vencer automáticamente. Las directivas MRM de Exchange y las reglas de diario siguen existiendo, pero Microsoft no las recomienda salvo un requisito específico.

**Por qué importa**

La mayoría de los tropiezos iniciales no son técnicos: funciones que no aparecen porque la licencia no las incluye, un administrador global que no puede revisar eliminaciones o directivas heredadas que contradicen las nuevas. Resolver licencias, roles y herencia el primer día evita compras innecesarias, configuraciones que no se pueden sostener y hallazgos de auditoría por usar funciones sin licencia.

**Qué vas a lograr**

- Distinguir DLM de Records Management y ubicar ambas soluciones en el portal de Microsoft Purview.
- Determinar qué capacidades incluye tu licencia (E3, E5, Purview Suite o IP&G) y cuáles requieren pago por uso.
- Asignar los grupos de roles mínimos para retención y registros, con roles de solo lectura y fecha de expiración.
- Identificar funciones heredadas (MRM, reglas de diario) que no conviene usar en diseños nuevos.

> **Qué cambió.** Data Lifecycle Management es el nuevo nombre de Microsoft Information Governance, y Records Management se reserva para el contenido de alto valor con obligaciones legales, regulatorias o de negocio ([DLM](https://learn.microsoft.com/en-us/purview/data-lifecycle-management)). Ambas viven en el portal de Microsoft Purview, que llegó a disponibilidad general en julio de 2024 ([MC807798](https://mc.merill.net/message/MC807798)); el portal de cumplimiento clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 ([MC939918](https://mc.merill.net/message/MC939918)).

> **Novedad.** Desde julio de 2026, las asignaciones a grupos de roles de Purview pueden tener fecha de expiración, de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Úsala para auditores externos, proyectos de migración y revisores temporales de eliminación.

> **Atención.** Tres permisos que sorprenden: Priority Cleanup Admin no está incluido por defecto en Compliance Administrator ([primeros pasos con DLM](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management)); el administrador global no tiene el rol Disposition Management ([eliminación](https://learn.microsoft.com/en-us/purview/disposition)); y las unidades administrativas no deben usarse en directivas de etiquetas dirigidas a sitios de SharePoint ([primeros pasos con registros](https://learn.microsoft.com/en-us/purview/get-started-with-records-management)).

> **Consejo Ninja.** Las directivas MRM de Exchange y las reglas de diario son funciones heredadas que no pasaron al nuevo centro de administración de Exchange, y Microsoft no recomienda usarlas salvo un requisito específico ([DLM](https://learn.microsoft.com/en-us/purview/data-lifecycle-management)). Inventaríalas antes de diseñar: conviven con las directivas de Purview y complican el diagnóstico de por qué se conserva o se borra un correo.

**¿Tienes poco tiempo?**

- [Learn about Microsoft Purview Data Lifecycle Management](https://learn.microsoft.com/en-us/purview/data-lifecycle-management) · Documentación
- [Get started with data lifecycle management](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management) · Documentación
- [Microsoft Purview service description (Data Lifecycle & Records Management)](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación

### Documentación, cursos y credenciales

- [Get started with data lifecycle management](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management) · Documentación · Oficial · Microsoft Learn. Guía de arranque de DLM con hoja de ruta, licencias, roles (Retention Management, View-Only, Priority Cleanup Admin), unidades administrativas y la exigencia de facturación pago por uso para ubicaciones de IA.
- [Microsoft Purview service description (Data Lifecycle & Records Management)](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn (Service Descriptions). Fuente autorizada de licenciamiento: qué funciones de retención entran en E3 y cuáles exigen E5/Purview Suite/IP&G (ámbitos adaptables, autoaplicación, registros, eventos, disposición, plan de archivos, limpieza prioritaria) y límites de archivo de buzones.
- [Data lifecycle and records management in Microsoft Purview (overview)](https://learn.microsoft.com/en-us/purview/manage-data-governance) · Documentación · Oficial · Microsoft Learn · 27 feb 2026. Mapa de capacidades que separa DLM (mantener lo necesario y borrar lo demás) de Records Management (plan de archivos, registros, disposición y prueba de eliminación).
- [Deploy Microsoft Purview data lifecycle and records management solutions](https://learn.microsoft.com/en-us/purview/data-governance-solution) · Documentación · Oficial · Microsoft Learn · 27 feb 2026. Guía prescriptiva de despliegue por pasos para DLM y RM con enlaces a guías interactivas y módulos de formación.
- [Learn about Microsoft Purview Data Lifecycle Management](https://learn.microsoft.com/en-us/purview/data-lifecycle-management) · Documentación · Oficial · Microsoft Learn · 26 sep 2025. Visión general de DLM: directivas de retención como pilar, etiquetas para excepciones, Adaptive Protection, limpieza prioritaria, archivo de buzones, buzones inactivos e importación PST, y desaconseja MRM salvo necesidad.
- [Prevent data loss and govern the data lifecycle with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/prevent-data-loss-lifecycle-purview/) · Curso · Oficial · Microsoft Learn. Módulo avanzado para administradores de Microsoft 365 que vincula requisitos de DLP, ciclo de vida de datos y DSPM para IA dentro de la gobernanza del tenant.

**Manos a la obra**

1. `Laboratorio` Activa tu prueba de Microsoft 365 E5 (o el sandbox E5 de desarrollador que describe el anexo de entorno de práctica) y, en el portal de Microsoft Purview, ubica Data Lifecycle Management y Records Management con sus páginas de directivas, etiquetas, ámbitos adaptables y eliminación ([primeros pasos con DLM](https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management)). Evidencia: capturas de ambas soluciones y una nota con lo que ofrece cada una.
2. `Laboratorio` Completa la tabla de [Licencias](00_Programa.md#licencias) para tu organización: por cada capacidad, indica si la tienes con E3, E5, Purview Suite, IP&G o pago por uso, y marca las brechas. Contrasta cada fila con la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description). Evidencia: tabla completada con fecha y fuente.
3. `Laboratorio` Asigna el grupo de roles Records Management a la cuenta del gestor de registros y View-Only Retention Management a una cuenta de auditoría, ambas con fecha de expiración; comprueba que la cuenta de auditoría ve las directivas pero no puede editarlas ([permisos de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)). Evidencia: captura de las asignaciones y del intento de edición denegado.
4. `Laboratorio` En Exchange Online PowerShell, verifica que la auditoría está activa con `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled` ([activar o desactivar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)); la revisión de eliminación la necesita activa al menos un día antes. Evidencia: salida del cmdlet.
5. `Laboratorio` Inventaría las funciones heredadas con `Get-RetentionPolicy` (directivas MRM) y `Get-JournalRule` (reglas de diario) y decide para cada una si se mantiene, se migra a Purview o se retira. Evidencia: inventario con la decisión y su motivo.
6. `Laboratorio parcial` Vincula una suscripción de Azure del mismo tenant para el pago por uso de Purview (requiere Global Administrator) y crea un presupuesto con alertas al 50 % y al 80 % ([habilitar pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement), [presupuestos de Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)); lo usarás en [M4](02_Nivel_2_Intermedio.md#m4) y [A1](03_Nivel_3_Avanzado.md#a1). Limitación: las páginas revisadas no confirman que el crédito de Visual Studio cubra los medidores de Purview, así que revisa los costos a las 48 horas. Evidencia: captura de la vinculación y del presupuesto.

<a id="i0"></a>

## I0 · Cómo aprender y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Ninja oficial de ciclo de vida y registros (2023): sección de examen (SC-400, hoy SC-401)*

Este programa ordena el material como un curso, pero no reemplaza a las credenciales oficiales. El examen **SC-401: Administering Information Security in Microsoft 365**, sucesor de SC-400, evalúa la retención dentro del bloque «Implementar DLP y retención», que pesa entre 30 y 35 % con las habilidades vigentes desde el 28 de octubre de 2026: etiquetas, ámbitos adaptables, autoaplicación, precedencia y recuperación de contenido retenido. Para practicar con evaluación en laboratorio, la credencial **Applied Skills** de retención, eDiscovery y Communication Compliance (ruta SC-5007) valida tareas reales en un entorno provisto por Microsoft.

Para mantenerte al día, la página de novedades de Purview se actualiza cada mes, el Centro de mensajes anuncia los despliegues con fecha y los webinars del equipo de producto se publican en el canal de la Microsoft Security Community. Ten en cuenta dos vacíos: el último webinar dedicado a ciclo de vida y registros que encontró la investigación es de julio de 2024, y Microsoft Mechanics no publicó un episodio específico en 2025–2026. Por eso este programa se apoya también en referentes de la comunidad, que conocerás en [C1](05_Comunidad.md#c1).

**Por qué importa**

La retención mezcla tecnología, archivística y derecho. Un administrador que domina el portal pero no los principios de retención, o un gestor de registros que no conoce los límites técnicos, toman malas decisiones. Una ruta de aprendizaje común y credenciales reconocidas dan al equipo un vocabulario compartido y aceleran las conversaciones con Legal y auditoría.

**Qué vas a lograr**

- Ubicar las credenciales oficiales (SC-401 y Applied Skills) y qué parte del temario cubre cada una.
- Armar un plan personal que combine esta guía, Microsoft Learn y los webinars del equipo de producto.
- Identificar los canales oficiales y comunitarios para resolver dudas y seguir las novedades.

> **Novedad.** Las habilidades medidas de SC-401 se actualizaron el 28 de octubre de 2026: «Implementar DLP y retención» pesa entre 30 y 35 % e incluye planificar retención y eliminación con etiquetas, ámbitos adaptables, publicar y autoaplicar etiquetas, interpretar la precedencia con la búsqueda de directivas (policy lookup) y recuperar contenido retenido ([guía de estudio SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)). La [guía en español](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-401) se actualiza después de la inglesa.

> **Consejo Ninja.** Dos rutas oficiales complementan esta guía: la de retención de SC-401, con 2 módulos y cerca de 1 h 19 min ([ruta SC-401](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/)), y la de SC-5007, con 9 módulos y cerca de 7 h 50 min ([ruta SC-5007](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention-ediscovery-communication-compliance/)), que prepara la [credencial Applied Skills](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview) de retención, eDiscovery y Communication Compliance.

> **Atención.** El último webinar del equipo de producto dedicado a ciclo de vida y registros que encontró la investigación es de julio de 2024 ([webinar DLM y RM](https://www.youtube.com/watch?v=lHGaAJTdCF8)), y Microsoft Mechanics no publicó un episodio específico en 2025–2026 ([lista de Purview de Microsoft Mechanics](https://www.youtube.com/playlist?list=PLXtHYVsvn_b-6Safd1jYAOIQwdg_9Clyc)). Contrasta los videos con la documentación vigente: desde entonces cambiaron las ubicaciones de Teams y de Copilot.

> **Consejo Ninja.** Una página de preparación de terceros advierte que la gestión de registros en profundidad queda fuera del foco de SC-401 ([msftuniversity, fuente no oficial](https://msftuniversity.com/exam/sc-401)). El examen te da la base; el plan de archivos, los eventos y la eliminación con evidencia los vas a dominar con la práctica de este programa.

**¿Tienes poco tiempo?**

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial
- [Implement and manage Microsoft 365 retention and recovery (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/) · Curso
- [Data Lifecycle Management & Records Management (DLM & RM) Services (webinar)](https://www.youtube.com/watch?v=lHGaAJTdCF8) · Webinar

### Documentación, cursos y credenciales

- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía oficial del examen SC-401 con habilidades vigentes desde el 28-oct-2026, donde 'Implementar DLP y retención' pesa 30-35% e incluye etiquetas, ámbitos adaptables, autoaplicación, precedencia y recuperación de contenido retenido.
- [Implement and manage Microsoft 365 retention and recovery (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/) · Curso · Oficial · Microsoft Learn. Ruta de Learn alineada con SC-401 (2 módulos, ~1 h 19 min) sobre etiquetas y directivas de retención, ámbitos adaptables, precedencia y recuperación de contenido eliminado.
- [Implement retention, eDiscovery, and Communication compliance in Microsoft Purview (SC-5007)](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention-ediscovery-communication-compliance/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (9 módulos, ~7 h 50 min) asociada a la credencial Applied Skills SC-5007 con ejercicios de retención estática/adaptable, etiquetas para finanzas y RR. HH., clasificadores entrenables y revisión de eliminación.
- [SC-401 exam prep — Information Security Administrator](https://msftuniversity.com/exam/sc-401) · Curso · Comunidad · Alex de Jong · Microsoft University (msftuniversity.com). Página de preparación de terceros que resume SC-401 como sucesor de SC-400 y aclara que la gestión de registros profunda y eDiscovery quedan fuera del foco del examen.

### Webinars, videos y podcasts

- [Data Lifecycle Management & Records Management (DLM & RM) Services (webinar)](https://www.youtube.com/watch?v=lHGaAJTdCF8) · Webinar · Empleado de Microsoft · Legado aún útil · Rahul Srivastava · Microsoft Security Community (YouTube) · 9 jul 2024. Webinar del equipo de producto con novedades de DLM/RM: directiva para Copilot, ámbitos adaptables en autoaplicación, APIs de Graph, Power Automate, Microsoft 365 Archive y hoja de ruta. *Nota:* De 2024: algunas novedades ya son GA y la ubicación de Copilot se amplió a apps de IA
- [Introduction to Data Lifecycle Management DLM - Compliance Manager - Part 1 (webinar)](https://www.youtube.com/watch?v=DnK16U_EyAg) · Webinar · Empleado de Microsoft · Legado aún útil · Ashish Kumar · Microsoft Security Community (YouTube) · 16 oct 2024. Webinar sobre motivadores de negocio de DLM, casos de uso, novedades y demostración, vinculándolo con Compliance Manager.
- [Getting Started with Deploying Microsoft Purview Data Lifecycle and Records Management (webinar)](https://www.youtube.com/watch?v=6AN8S1jBA0g) · Webinar · Empleado de Microsoft · Legado aún útil · Sophie Ke · Microsoft Security Community (YouTube) · 23 ene 2023. Sesión introductoria del equipo de producto para desplegar DLM y RM con escenarios y buenas prácticas de arranque. *Nota:* La fecha mostrada en la página (martes 23-ene-2023) puede ser 2024; contenido previo al portal unificado

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio de SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y arma una tabla: por cada habilidad del bloque de retención, el módulo de esta guía que la cubre y tu nivel de confianza del 1 al 5. Evidencia: tabla de brechas con fecha.
2. `Laboratorio` Completa la [ruta de retención de SC-401](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention/) y anota tres conceptos que este programa amplía, por ejemplo las ubicaciones de IA o la limpieza prioritaria. Evidencia: notas con el enlace a cada módulo.
3. `Laboratorio` Inicia la [ruta SC-5007](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention-ediscovery-communication-compliance/) y agenda la evaluación de la credencial Applied Skills para después del nivel intermedio. Evidencia: fecha agendada en tu plan de estudio.
4. `Laboratorio` Mira el [webinar de 2024](https://www.youtube.com/watch?v=lHGaAJTdCF8) y lista tres cosas que cambiaron desde entonces (por ejemplo, canales privados, registros de llamadas de Teams o ubicaciones de IA), cada una con su fuente actual en las [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new). Evidencia: lista con enlaces.
5. `Laboratorio` Crea tu rutina de actualización: la página de novedades de Purview cada mes y el Centro de mensajes filtrado por Data Lifecycle Management cada semana (o su archivo público en mc.merill.net), con un canal del equipo donde publiques cada cambio con su fecha y el módulo afectado. Evidencia: primera entrada publicada.

<a id="i1"></a>

## I1 · Ciclo de vida de los datos hoy: principios, directivas, etiquetas y ámbitos adaptables

*L100–L200 · ~4 h · Origen: Ninja oficial de ciclo de vida y registros (2023): retención, principios de retención, ámbitos adaptables y unidades administrativas*

En Microsoft 365 la retención tiene tres resultados posibles: **solo retener**, **solo eliminar** o **retener y luego eliminar**. El contenido se retiene en su lugar y, cuando alguien lo edita o lo borra, se conserva una copia: en la biblioteca de conservación (Preservation Hold) de SharePoint y OneDrive —que cuenta para la cuota—, en Recoverable Items de Exchange o en la carpeta oculta SubstrateHolds para Teams, Viva Engage y las interacciones con Copilot e IA. Tienes dos herramientas: las **directivas de retención**, que fijan la base por ubicación, y las **etiquetas de retención**, que se aplican a elementos concretos y permiten declarar registros.

Cuando varias reglas aplican al mismo elemento deciden los **principios de retención**, en este orden: retener gana sobre eliminar; gana el período de retención más largo; lo explícito gana sobre lo implícito para la eliminación (la etiqueta sobre la directiva, y una directiva con ámbito sobre una de toda la organización); y, por último, gana el período de eliminación más corto. Un elemento solo puede tener una etiqueta de retención a la vez.

Los **ámbitos adaptables** reemplazan las listas manuales por consultas diarias sobre atributos de usuarios, grupos y sitios, como el departamento o el país; admiten unidades administrativas y permiten una sola directiva para Teams y Viva Engage. Los ámbitos estáticos siguen siendo útiles para pilotos, pero esconden una trampa: si quitas la última inclusión de una directiva, vuelve a aplicarse a «Todos».

**Por qué importa**

Los principios de retención deciden qué se conserva y qué se borra. Entenderlos mal lleva a dos riesgos opuestos: eliminar algo que debías conservar (riesgo legal) o conservar todo para siempre (costo, exposición en litigios y riesgo de privacidad). Los ámbitos adaptables alinean la retención con el ciclo de vida de personas y sitios sin mantenimiento manual, y reducen errores y deuda de retención.

**Qué vas a lograr**

- Explicar las tres acciones de retención y dónde se guardan las copias retenidas en cada carga de trabajo.
- Aplicar los cuatro principios de retención para resolver conflictos entre directivas, etiquetas y holds.
- Elegir entre directivas y etiquetas, y entre ámbitos estáticos y adaptables, según el caso.
- Crear y validar un ámbito adaptable respetando sus límites.
- Detectar configuraciones de alto riesgo, como una directiva de eliminación que vuelve a aplicarse a «Todos».

> **Atención.** Si quitas la última inclusión de una directiva estática, vuelve a aplicarse a «Todos»: en una directiva de eliminación, eso puede borrar contenido de toda la organización. Además, la retención de Exchange solo se aplica a buzones con al menos 10 MB ([configuración común](https://learn.microsoft.com/en-us/purview/retention-settings)).

> **Consejo Ninja.** Límites de los ámbitos adaptables: 200 caracteres por valor, 10 atributos por grupo, 10 grupos y 10.000 caracteres en la consulta avanzada. Las consultas se ejecutan a diario y la membresía puede tardar hasta 5 días en poblarse: valídala antes de asociar el ámbito a una directiva ([ámbitos adaptables](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes)).

> **Qué cambió.** No existe una directiva para «todas las ubicaciones»: en directivas estáticas, elegir Teams o Viva Engage excluye el resto ([crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies)), mientras que con ámbitos adaptables una misma directiva puede incluir Teams y Viva Engage ([ámbitos adaptables](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes)). Diseña la base como un conjunto pequeño de directivas por carga de trabajo.

> **Consejo Ninja.** Para explicar a los dueños de datos en qué se diferencian las etiquetas de retención de las de confidencialidad, Joanne Klein actualizó en julio de 2026 una infografía que compara 20 comportamientos de ambas ([comparación](https://joannecklein.com/2026/07/30/a-contrast-and-comparison-of-retention-and-sensitivity-labels/)). Los cuatro principios de retención, con ejemplos, están en [retención](https://learn.microsoft.com/en-us/purview/retention) y en la tabla de este módulo.

**¿Tienes poco tiempo?**

- [Learn about retention policies and retention labels](https://learn.microsoft.com/en-us/purview/retention) · Documentación
- [Adaptive scopes](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes) · Documentación
- [Understand retention in Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-understand-retention/) · Curso
- [Data Lifecycle Management (Part 1): Retention Policies (video)](https://www.youtube.com/watch?v=z9BsOGzWLWs) · Video

**Principios de retención aplicados: seis casos**

| Situación | Resultado | Principio que decide |
|---|---|---|
| Directiva «retener 7 años» y etiqueta «eliminar a los 2 años» | Se conserva 7 años | 1. Retener gana sobre eliminar |
| Dos directivas: «retener 3 años y eliminar» y «retener 5 años y eliminar» | Se conserva 5 años y luego se elimina | 2. Gana el período de retención más largo |
| Directiva de toda la organización «eliminar a los 3 años» y directiva con ámbito «eliminar a los 5 años» | Se elimina a los 5 años | 3. Lo explícito gana sobre lo implícito para la eliminación |
| Etiqueta «eliminar a los 5 años» y directiva «eliminar a 1 año» | Se elimina a los 5 años | 3. La etiqueta es más explícita que la directiva |
| Dos directivas de toda la organización: «eliminar a los 2 años» y «eliminar a los 4 años» | Se elimina a los 2 años | 4. Gana el período de eliminación más corto |
| Cualquier configuración de eliminación y un hold de eDiscovery | Se conserva mientras dure el hold | 1. Retener gana sobre eliminar |

Fuentes: [principios de retención](https://learn.microsoft.com/en-us/purview/retention) y la explicación con ejemplos de [The Purview Practitioner](https://www.thepurviewpractitioner.com/learn/retention-precedence-four-principles) (autor no identificado: valida cada caso con Learn).

### Documentación, cursos y credenciales

- [Implement and manage retention with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-implement-manage-retention/) · Curso · Oficial · Microsoft Learn. Módulo práctico de 11 unidades que cubre directivas vs etiquetas, ámbitos adaptables y estáticos, publicación de etiquetas y retención basada en eventos con dos ejercicios guiados.
- [Learn about retention policies and retention labels](https://learn.microsoft.com/en-us/purview/retention) · Documentación · Oficial · Microsoft Learn. Artículo central sobre retención en Microsoft 365: retener/eliminar in situ, biblioteca de conservación, carpeta SubstrateHolds, ámbitos adaptables vs estáticos, principios de retención, Preservation Lock y comparación con retenciones de eDiscovery.
- [Create and configure retention policies](https://learn.microsoft.com/en-us/purview/create-retention-policies) · Documentación · Oficial · Microsoft Learn. Procedimiento para crear directivas de retención por ubicación (Exchange, SharePoint, OneDrive, Grupos, Teams, IA, Viva Engage, Skype) incluida la separación de la antigua ubicación 'Teams chats and Copilot interactions'.
- [Adaptive scopes](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes) · Documentación · Oficial · Microsoft Learn. Explica los ámbitos adaptables basados en consultas diarias a atributos de Entra/Exchange/SharePoint, su integración con unidades administrativas y sus límites (200 caracteres por valor, 10 atributos, 10 grupos, 10.000 caracteres en consulta avanzada).
- [Common settings for retention policies and retention label policies](https://learn.microsoft.com/en-us/purview/retention-settings) · Documentación · Oficial · Microsoft Learn. Configuración común de ámbitos (adaptables y estáticos), ubicaciones y advertencias críticas como el requisito de 10 MB en buzones y que eliminar la última inclusión revierte la directiva a 'All'.
- [Understand retention in Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-understand-retention/) · Curso · Oficial · Microsoft Learn. Módulo introductorio (24 min) que explica casos de uso de la retención, su relación con DLP y qué controla y qué no controla la retención.

### Webinars, videos y podcasts

- [Data Lifecycle Management (Part 1): Retention Policies (video)](https://www.youtube.com/watch?v=z9BsOGzWLWs) · Video · Comunidad · Alan Cox · YouTube (canal Alan Cox). Recorrido práctico por directivas de retención y ámbitos adaptables en el portal de Purview, útil como demostración visual del nivel inicial.

### Laboratorios, GitHub y herramientas

- [Data Lifecycle Management - Microsoft Security Workshop (lab)](https://indra-pr.github.io/msft-security-workshop/purview/data-compliance/data-lifecycle-management/) · Laboratorio · Comunidad · indra-pr · GitHub Pages (msft-security-workshop). Laboratorio comunitario con 5 casos (directiva estática, etiquetas, ámbitos adaptables, eventos, archivo/PST) y script para generar datos de prueba.

### Comunidad: blogs, libros, newsletters y eventos

- [The 4 principles that decide what Purview actually keeps](https://www.thepurviewpractitioner.com/learn/retention-precedence-four-principles) · Blog · Comunidad · The Purview Practitioner · 12 feb 2026. Explicación didáctica con ejemplos de los cuatro principios de retención (retener gana a eliminar, mayor período gana, explícito gana a implícito, menor eliminación gana).

**Manos a la obra**

1. `Laboratorio` Crea un sitio piloto de SharePoint y una directiva estática «retener 3 años y luego eliminar» solo para ese sitio. Edita dos archivos de prueba, borra un tercero y verifica las copias en la biblioteca de conservación (Preservation Hold) ([SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint)). Evidencia: captura de la biblioteca con las versiones conservadas.
2. `Laboratorio` Completa el atributo Department de cinco usuarios de prueba (tres con «Finanzas») y crea un ámbito adaptable de usuarios con la consulta Department igual a Finanzas. Espera hasta 5 días y valida la membresía en el portal y por PowerShell antes de usarlo en una directiva ([ámbitos adaptables](https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes)). Evidencia: lista de miembros comparada con la esperada.
3. `Laboratorio` Resuelve tres conflictos aplicando los cuatro principios en orden y anota cuál decide: (a) directiva «retener 7 años» y etiqueta «eliminar a los 2 años»; (b) dos directivas que retienen 3 y 5 años; (c) directiva de toda la organización «eliminar a los 3 años» y directiva con ámbito «eliminar a los 5 años». Luego usa la búsqueda de directivas (policy lookup) para ver qué directivas aplican a un usuario y a un sitio de prueba ([retención](https://learn.microsoft.com/en-us/purview/retention)). Evidencia: tu tabla de resultados comparada con la tabla de este módulo.
4. `Laboratorio` Crea las etiquetas «Retener 1 año» y «Eliminar a los 30 días», publícalas para el sitio piloto (pueden tardar hasta 7 días en aparecer) y aplica una a un documento; después aplica la otra y confirma que reemplaza a la primera, porque un elemento solo admite una etiqueta de retención. Evidencia: capturas de la columna de etiqueta antes y después.
5. `Laboratorio` Demuestra la trampa de los ámbitos estáticos con una directiva de prueba de solo retener: quita su única inclusión, confirma que pasa a aplicarse a «Todos» y restaura la inclusión ([configuración común](https://learn.microsoft.com/en-us/purview/retention-settings)). Evidencia: capturas antes y después y una regla nueva en tu lista de revisión por pares.
6. `Laboratorio` Opcional: recorre el [laboratorio comunitario de DLM](https://indra-pr.github.io/msft-security-workshop/purview/data-compliance/data-lifecycle-management/) (directiva estática, etiquetas, ámbitos adaptables, eventos y archivo) y anota dónde difiere de Learn; su autor no está verificado. Evidencia: lista de diferencias con la fuente oficial de cada una.

<a id="i2"></a>

## I2 · Retención en Exchange, SharePoint, OneDrive, Teams y Viva Engage

*L100–L200 · ~4 h · Origen: Ninja oficial de ciclo de vida y registros (2023): cargas de trabajo (Yammer, hoy Viva Engage)*

Cada carga de trabajo retiene a su manera. En **Exchange**, las copias van a Recoverable Items y la retención solo se aplica a buzones con al menos 10 MB. En **SharePoint y OneDrive**, la biblioteca de conservación guarda lo editado o eliminado; un trabajo de temporizador se ejecuta cada 7 días sobre el contenido con más de 30 días en la biblioteca (hasta 37 días) y después el elemento pasa por la papelera de segunda etapa (93 días). Loop y Copilot Pages en SharePoint Embedded se tratan como sitios, los elementos de lista solo admiten etiquetas y las directivas no aplican a estructuras como bibliotecas o carpetas.

**Teams** cambió mucho entre 2025 y 2026. Los mensajes de canales privados migraron a buzones de grupo entre octubre y diciembre de 2025 y heredan la directiva de mensajes de canal del equipo, y desde finales de abril de 2026 los nuevos registros de llamadas ya no entran en las directivas de chats: necesitan directivas «Teams call logs» creadas por PowerShell. Las grabaciones y transcripciones de reuniones se rigen por el OneDrive o el SharePoint del organizador o del canal.

En **Viva Engage**, los mensajes de usuarios y comunidades se guardan en carpetas ocultas de buzones y los archivos necesitan sus propias directivas de SharePoint u OneDrive. Y una novedad que conviene confirmar en tu tenant: desde mediados de 2026, según la comunidad, las directivas de retención también pueden retener o eliminar tareas de Planner.

**Por qué importa**

Una directiva que funciona en una carga de trabajo puede comportarse distinto en otra. Si el equipo no sabe dónde viven las copias retenidas ni cuánto tarda realmente la eliminación, aparecen tickets de «la retención no funciona», cuotas que crecen sin control y brechas por los cambios de 2026, como los registros de llamadas de Teams que quedaron fuera de las directivas de chat.

**Qué vas a lograr**

- Describir dónde y cómo se retiene el contenido en cada carga de trabajo.
- Configurar directivas para Teams (chats, canales y registros de llamadas) considerando los cambios de 2025–2026.
- Estimar los tiempos reales de eliminación en SharePoint y OneDrive.
- Explicar la retención en Viva Engage y en las tareas de Planner.
- Documentar la matriz de retención de tu tenant.

> **Qué cambió.** Desde finales de abril de 2026, los nuevos registros de llamadas de Teams ya no entran en las directivas de chats: necesitan directivas «Teams call logs», que se crean por PowerShell ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)). Si tenías requisitos sobre registros de llamadas, revisa tu matriz: hoy pueden estar sin cubrir.

> **Qué cambió.** Los mensajes de canales privados migraron a buzones de grupo entre octubre y diciembre de 2025 (las nubes especiales, a inicios de 2026) y heredan la directiva de mensajes de canal del equipo; los límites subieron a 1.000 canales privados por equipo y 5.000 miembros ([anuncio de Teams](https://techcommunity.microsoft.com/blog/microsoftteamsblog/new-enhancements-in-private-channels-in-microsoft-teams-unlock-their-full-potent/4438767), [retención en Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams)).

> **Atención.** En SharePoint y OneDrive, el temporizador corre cada 7 días sobre lo que lleva más de 30 días en la biblioteca de conservación (hasta 37 días) y luego el elemento pasa 93 días en la papelera de segunda etapa: una eliminación puede tardar unos 130 días en ser definitiva. La biblioteca de conservación cuenta para la cuota del sitio ([SharePoint y OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint)).

> **Novedad.** Según la comunidad, el mensaje MC1384412 agregó directivas de retención para tareas de Planner, con disponibilidad general entre mediados de julio y mediados de agosto de 2026 ([Microsoft 365 for IT Pros](https://office365itpros.com/2026/07/28/planner-tasks-retention/)). Confirma la ubicación en tu tenant antes de documentarla.

**¿Tienes poco tiempo?**

- [Learn about retention for Microsoft Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams) · Documentación
- [Learn about retention for SharePoint and OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint) · Documentación
- [New enhancements in Private Channels in Microsoft Teams unlock their full potential](https://techcommunity.microsoft.com/blog/microsoftteamsblog/new-enhancements-in-private-channels-in-microsoft-teams-unlock-their-full-potent/4438767) · Blog oficial

### Documentación, cursos y credenciales

- [Learn about retention for Microsoft Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams) · Documentación · Oficial · Microsoft Learn. Detalla qué se retiene en chats, canales estándar/compartidos/privados y registros de llamadas de Teams, y la migración de mensajes de canales privados a buzones de grupo a fines de 2025.
- [Learn about retention for SharePoint and OneDrive](https://learn.microsoft.com/en-us/purview/retention-policies-sharepoint) · Documentación · Oficial · Microsoft Learn. Explica la biblioteca de conservación (Preservation Hold), versiones, adjuntos en la nube, OneNote, Loop/Copilot Pages en SharePoint Embedded, sitios archivados y los tiempos de los trabajos de temporizador (hasta 37 días + papelera de 93 días).
- [Learn about retention for Viva Engage](https://learn.microsoft.com/en-us/purview/retention-policies-viva-engage) · Documentación · Oficial · Microsoft Learn. Detalla la retención de mensajes de usuario y de comunidad de Viva Engage, su almacenamiento en carpetas ocultas de buzones y el paso por SubstrateHolds.

### Anuncios y blogs oficiales

- [New enhancements in Private Channels in Microsoft Teams unlock their full potential](https://techcommunity.microsoft.com/blog/microsoftteamsblog/new-enhancements-in-private-channels-in-microsoft-teams-unlock-their-full-potent/4438767) · Blog oficial · Empleado de Microsoft · cduggirala · Microsoft Tech Community (Microsoft Teams Blog) · 1 ago 2025. Anuncia que los canales privados pasan a buzón de grupo (migración oct-dic 2025) y explica cómo ajustar retención, holds y DLP antes y después.

### Comunidad: blogs, libros, newsletters y eventos

- [Data Lifecycle Management Adds Support for Planner Retention Policies](https://office365itpros.com/2026/07/28/planner-tasks-retention/) · Blog · MVP · Nuevo · Tony Redmond · Microsoft 365 for IT Pros (office365itpros.com) · 28 jul 2026. Explica MC1384412: las directivas de retención pueden retener o eliminar tareas de Planner (planes personales y de grupo) con despliegue GA de mediados de julio a mediados de agosto de 2026, e incluye script de análisis.

**Manos a la obra**

1. `Laboratorio` Crea una directiva de solo retener (1 año) para chats de Teams y otra para mensajes de canal, con alcance a tus usuarios y al equipo piloto. Envía, edita y borra mensajes y localízalos con una búsqueda de eDiscovery ([retención en Teams](https://learn.microsoft.com/en-us/purview/retention-policies-teams)). Evidencia: resultados de la búsqueda que incluyen los mensajes eliminados.
2. `Laboratorio` Crea un canal privado en el equipo piloto, publica mensajes y verifica con eDiscovery que quedan cubiertos por la directiva de mensajes de canal del equipo y no por una ubicación aparte. Evidencia: búsqueda que los encuentra en el buzón del grupo.
3. `Laboratorio` Crea una directiva «Teams call logs» con Security & Compliance PowerShell siguiendo [crear directivas](https://learn.microsoft.com/en-us/purview/create-retention-policies) y verifícala con `Get-RetentionCompliancePolicy`. Evidencia: salida del cmdlet con la nueva directiva y sus ubicaciones.
4. `Laboratorio` Crea una directiva para mensajes de comunidad y de usuario de Viva Engage, publica y borra un mensaje con un archivo adjunto y documenta qué directiva de SharePoint u OneDrive cubre ese archivo ([retención en Viva Engage](https://learn.microsoft.com/en-us/purview/retention-policies-viva-engage)). Evidencia: ficha con mensaje, adjunto y directiva de cada uno.
5. `Laboratorio` Dibuja la línea de tiempo de un archivo borrado en un sitio con retención: biblioteca de conservación, temporizador semanal, papelera de segunda etapa y momento en que deja de ser recuperable. Agrega la cuota consumida por la biblioteca del sitio piloto. Evidencia: línea de tiempo con días y la captura del almacenamiento del sitio.
6. `Laboratorio` Completa la [matriz de retención](00_Programa.md#matriz-retencion) para tu tenant: por cada ubicación, la directiva que la cubre, su período, su ámbito y su dueño, y marca las celdas «No verificado» que probaste. Evidencia: matriz versionada con fecha.
7. `Laboratorio parcial` Busca la ubicación de tareas de Planner al crear una directiva; si aparece, crea una directiva piloto de solo retener para un plan de prueba ([Microsoft 365 for IT Pros](https://office365itpros.com/2026/07/28/planner-tasks-retention/)). Limitación: la fuente es comunitaria y la ubicación puede no estar en tu tenant; si no aparece, documenta su ausencia con fecha. Evidencia: captura de la ubicación o de su ausencia.

**¿Quieres profundizar?**

- [Data Lifecycle Management Adds Support for Planner Retention Policies](https://office365itpros.com/2026/07/28/planner-tasks-retention/) · Blog

<a id="i3"></a>

## I3 · Gestión de registros: etiquetas de registro y plan de archivos

*L100–L200 · ~4 h · Origen: Ninja oficial de ciclo de vida y registros (2023): plan de archivos, declarar registros y otros usos de las etiquetas*

La gestión de registros convierte una etiqueta de retención en una declaración formal. Hay cuatro grados de restricción: la **etiqueta estándar** solo retiene o elimina; el **registro bloqueado** impide editar y eliminar; el **registro desbloqueado** permite editar mientras conserva la etiqueta; y el **registro regulatorio** impide editar, eliminar y cambiar o quitar la etiqueta, incluso a los administradores. Ningún tipo de registro puede ser anulado por la limpieza prioritaria. Con el **versionado de registros**, cada versión bloqueada se guarda como registro en la carpeta Records de la biblioteca de conservación; no aplica a registros regulatorios.

El **plan de archivos** es el puente entre tu tabla de retención documental y Purview: importa etiquetas desde una hoja de cálculo, las exporta para revisión y agrega descriptores —función o departamento, categoría, tipo de autoridad y cita o disposición legal— que hacen trazable cada etiqueta. Es la pieza que mostrarás a auditoría y a Legal, y la que te permite llevar, por ejemplo, una tabla de retención documental (TRD) o un catálogo de disposición documental a etiquetas concretas. Mira el [plan de archivos de ejemplo](00_Programa.md#plan-archivos) antes de empezar.

**Por qué importa**

Un registro exige prueba: quién lo declaró, cuándo, y que no se modificó ni se eliminó antes de tiempo. Un plan de archivos construido desde la tabla de retención de la organización hace defendible cada decisión ante auditoría. Y como el registro regulatorio es irreversible, usarlo sin necesidad crea restricciones permanentes que nadie podrá deshacer.

**Qué vas a lograr**

- Distinguir etiqueta estándar, registro bloqueado, registro desbloqueado y registro regulatorio, con sus restricciones.
- Construir e importar un plan de archivos con descriptores desde una hoja de cálculo.
- Usar el versionado de registros y comprobar dónde se guardan las versiones.
- Decidir cuándo usar, y cuándo no, registros regulatorios.

> **Atención.** El registro regulatorio es irreversible: nadie puede quitar ni cambiar la etiqueta, ni editar o eliminar el contenido, y no admite versionado de registros ([registros](https://learn.microsoft.com/en-us/purview/records-management), [versionado](https://learn.microsoft.com/en-us/purview/record-versioning)). Según la comunidad, la opción está oculta por defecto y se habilita con `Set-RegulatoryComplianceUI` ([purview365](https://purview365.com/blog/sharepoint-online-14-retention-labels-policies)): úsala solo con aprobación escrita de Legal.

> **Consejo Ninja.** El plan de archivos importa etiquetas desde una hoja de cálculo, las exporta para revisión y agrega descriptores —función, categoría, tipo de autoridad y cita— que hacen trazable cada etiqueta; para usarlo necesitas Retention Manager o View-only Retention Manager ([plan de archivos](https://learn.microsoft.com/en-us/purview/file-plan-manager)). La página también está [en español](https://learn.microsoft.com/es-es/purview/file-plan-manager).

> **Atención.** Licencias: crear y publicar etiquetas está en E3, F3 y F1, pero marcar contenido como registro o registro regulatorio, el plan de archivos y las etiquetas predeterminadas de SharePoint exigen nivel E5: Microsoft 365 E5, Office 365 E5, Purview Suite o IP&G ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).

**¿Tienes poco tiempo?**

- [Learn about records management](https://learn.microsoft.com/en-us/purview/records-management) · Documentación
- [Use file plan to create and manage retention labels](https://learn.microsoft.com/en-us/purview/file-plan-manager) · Documentación
- [Manage records and disposition with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-manage-records/) · Curso

### Documentación, cursos y credenciales

- [Manage records and disposition with Microsoft Purview](https://learn.microsoft.com/en-us/training/modules/purview-manage-records/) · Curso · Oficial · Microsoft Learn. Módulo de Learn sobre plan de archivos, autoaplicación con clasificador entrenable, declaración de registros, revisiones de eliminación y precedencia de etiquetas, con ejercicios de laboratorio.
- [Learn about records management](https://learn.microsoft.com/en-us/purview/records-management) · Documentación · Oficial · Microsoft Learn. Describe la gestión de registros en Microsoft 365 y la tabla de restricciones entre etiqueta estándar, registro bloqueado/desbloqueado y registro regulatorio, incluida la exclusión de la limpieza prioritaria.
- [Use file plan to create and manage retention labels](https://learn.microsoft.com/en-us/purview/file-plan-manager) · Documentación · Oficial · Microsoft Learn. Describe el plan de archivos de Records Management: importación masiva desde hoja de cálculo, exportación para revisión, columnas de configuración y descriptores (función, categoría, autoridad, cita).
- [Get started with records management](https://learn.microsoft.com/en-us/purview/get-started-with-records-management) · Documentación · Oficial · Microsoft Learn. Hoja de ruta de arranque de Records Management con licencias, grupo de roles Records Management, View-Only Record Management, unidades administrativas y escenarios comunes.
- [Use record versioning to update records stored in SharePoint or OneDrive](https://learn.microsoft.com/en-us/purview/record-versioning) · Documentación · Oficial · Microsoft Learn. Cómo bloquear y desbloquear registros para conservar cada versión como registro en la carpeta Records de la biblioteca de conservación, y cómo deshabilitarlo a nivel de tenant.

**Manos a la obra**

1. `Laboratorio` Descarga la plantilla del plan de archivos, completa cinco etiquetas tomadas del [plan de archivos de ejemplo](00_Programa.md#plan-archivos) con sus descriptores, impórtala y exporta el resultado ([plan de archivos](https://learn.microsoft.com/en-us/purview/file-plan-manager)). Evidencia: CSV exportado con las cinco etiquetas y sus descriptores.
2. `Laboratorio` Crea una etiqueta que declare el contenido como registro, publícala para el sitio piloto y aplícala a un documento; intenta editarlo y eliminarlo como propietario del sitio y como administrador. Evidencia: capturas de los bloqueos.
3. `Laboratorio` Desbloquea el registro, edítalo y vuelve a bloquearlo; comprueba que la versión anterior quedó como registro en la carpeta Records de la biblioteca de conservación ([versionado de registros](https://learn.microsoft.com/en-us/purview/record-versioning)). Evidencia: captura de la carpeta Records con las versiones.
4. `Laboratorio` Toma tres series de la tabla de retención documental de tu organización (o del ejemplo) y define para cada una la etiqueta, los descriptores, el período, el disparador, la acción final y el tipo de registro; marca cuáles merecen revisión de eliminación. Evidencia: hoja revisada por el dueño de los datos.
5. `Laboratorio parcial` Solo en un tenant desechable (por ejemplo, un sandbox que no reutilizarás), habilita la opción de registro regulatorio, aplica la etiqueta a un documento de prueba y comprueba que ni el administrador puede quitarla. Limitación: es irreversible; nunca lo hagas en el tenant de práctica que seguirás usando ni en producción ([registros](https://learn.microsoft.com/en-us/purview/records-management)). Evidencia: capturas del intento de cambio rechazado.
6. `Solo producción` Valida el plan de archivos con Legal y los dueños de datos antes de usarlo con personas reales. Cómo hacerlo seguro: publica primero las etiquetas de registro solo para los gestores de registros, sin autoaplicación, sobre un sitio piloto, y registra la aprobación de cada etiqueta con fecha y responsable. Evidencia: acta de aprobación y exportación del plan de archivos aprobado.

<a id="reto-inicial"></a>

## Reto del nivel

**Arquitectura de retención de base.** En tu laboratorio, entrega: (1) la [matriz de retención](00_Programa.md#matriz-retencion) completa para tu tenant, con las celdas «No verificado» que probaste; (2) una directiva estática piloto y un ámbito adaptable validado, con capturas; (3) un plan de archivos con al menos cinco etiquetas y sus descriptores, importado y exportado; (4) un registro con versionado probado; y (5) una página para un dueño de datos que explique qué se conserva, durante cuánto tiempo y qué principio de retención lo decide. Criterio de éxito: un colega puede reconstruir tu configuración solo con tu documentación.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué es Data Lifecycle Management en Microsoft Purview?
   - a) Una solución nueva que reemplaza a Records Management
   - b) Un complemento de pago por uso para archivar sitios inactivos
   - c) El nuevo nombre de Microsoft Information Governance
   - d) El nombre actual de eDiscovery Standard

2. ¿Cuál de estas capacidades está incluida en Microsoft 365 E3 sin complementos?
   - a) Directivas de retención estáticas
   - b) Ámbitos adaptables
   - c) Revisión de eliminación
   - d) Retención basada en eventos

3. Un administrador global intenta revisar elementos pendientes de eliminación y no puede. ¿Cuál es la causa más probable?
   - a) La revisión solo puede hacerse con PowerShell
   - b) Su cuenta no tiene licencia E5
   - c) La auditoría está desactivada por diseño
   - d) No tiene el rol Disposition Management, que no recibe por defecto

4. Desde julio de 2026, ¿qué cambio tienen las asignaciones a grupos de roles de Purview?
   - a) Solo pueden hacerse con PIM
   - b) Pueden tener fecha de expiración de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager
   - c) Vencen automáticamente a los 90 días
   - d) Ya no admiten grupos de seguridad

5. En SC-401, con las habilidades vigentes desde el 28 de octubre de 2026, ¿cuánto pesa el bloque «Implementar DLP y retención»?
   - a) 10–15 %
   - b) 15–20 %
   - c) 20–25 %
   - d) 30–35 %

6. Un elemento tiene una directiva «retener 7 años» y una etiqueta «eliminar a los 2 años». ¿Qué ocurre?
   - a) Se elimina a los 2 años porque la etiqueta es más explícita
   - b) Se elimina a los 2 años y queda una copia por 5 años más
   - c) Se conserva durante 7 años porque retener gana sobre eliminar
   - d) El elemento queda bloqueado por conflicto

7. Dos directivas de solo eliminar aplican al mismo sitio: una de toda la organización (3 años) y otra con ámbito específico para ese sitio (5 años). ¿Cuándo se elimina el contenido?
   - a) A los 5 años, porque la directiva con ámbito es más explícita
   - b) A los 3 años, porque gana el período de eliminación más corto
   - c) Nunca, porque las directivas entran en conflicto
   - d) A los 8 años, porque los períodos se suman

8. ¿Cuántos atributos admite como máximo un grupo de un ámbito adaptable?
   - a) 5
   - b) 20
   - c) Sin límite
   - d) 10

9. ¿Qué ocurre si quitas la última inclusión de una directiva de retención con ámbito estático?
   - a) La directiva se desactiva
   - b) Se convierte en una directiva con ámbito adaptable
   - c) Vuelve a aplicarse a «Todos»
   - d) Se elimina la directiva

10. ¿Qué requisito mínimo tiene un buzón de Exchange para que se le aplique la retención?
   - a) Tener al menos 10 MB
   - b) Tener al menos 1 GB
   - c) Tener el buzón de archivo habilitado
   - d) Tener licencia E5

11. Desde finales de abril de 2026, ¿cómo se retienen los nuevos registros de llamadas de Teams?
   - a) Siguen incluidos en la directiva de chats de Teams
   - b) Con etiquetas autoaplicadas
   - c) No se pueden retener
   - d) Con directivas «Teams call logs» creadas por PowerShell

12. Tras la migración de los canales privados a buzones de grupo, ¿qué ubicación retiene sus mensajes?
   - a) Teams chats
   - b) Teams channel messages
   - c) Teams private channel messages
   - d) Los buzones de Exchange de cada miembro

13. ¿Cada cuánto corre el trabajo del temporizador que procesa la biblioteca de conservación en SharePoint y OneDrive?
   - a) Cada 24 horas
   - b) Cada 93 días
   - c) Cada 7 días
   - d) Cada 30 días

14. ¿Qué tipo de etiqueta permite editar el contenido sin perder la etiqueta?
   - a) Registro regulatorio
   - b) Registro desbloqueado
   - c) Registro bloqueado
   - d) Ninguno: ningún registro admite edición

15. Con el versionado de registros, ¿dónde se guardan las versiones bloqueadas?
   - a) En la carpeta Records de la biblioteca de conservación
   - b) En la papelera de segunda etapa
   - c) En Recoverable Items
   - d) En SubstrateHolds

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones de retención y eliminación deben validarse con Legal y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

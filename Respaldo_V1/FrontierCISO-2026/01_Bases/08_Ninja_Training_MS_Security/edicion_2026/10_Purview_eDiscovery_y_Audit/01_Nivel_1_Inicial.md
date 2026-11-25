# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Purview y sus licencias, la experiencia unificada de eDiscovery, Audit Standard y Premium y la sintaxis de búsqueda. Terminas con un caso de práctica, una consulta KeyQL validada con estadísticas y una política de retención de auditoría propia.

*L100–L200 · 5 módulos · ~16 horas · 28 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos y licencias](#p0) · [I0 Cómo aprender](#i0) · [I1 eDiscovery unificado](#i1) · [I2 Audit Standard y Premium](#i2) · [I3 Búsqueda y KeyQL](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, el portal unificado y las licencias

*L100–L200 · ~2 h · Origen: Ninja de Advanced eDiscovery (2021): Overview y Getting Started, actualizado al portal de Purview*

eDiscovery y Audit son dos soluciones de **Microsoft Purview**, la familia de gobierno, protección y cumplimiento de datos de Microsoft. Hoy se operan desde el portal unificado de Purview, que llegó a disponibilidad general en julio de 2024 y reemplazó al antiguo centro de cumplimiento, retirado entre noviembre y diciembre de 2024. Antes de crear el primer caso necesitas entender tres cosas: dónde está cada función, quién puede usarla (roles y grupos de roles) y qué licencia necesita cada persona involucrada.

La licencia merece atención especial porque Purview combina dos modelos: licencias por usuario —Microsoft 365 E3 o E5, o el complemento **Microsoft Purview Suite**, el nuevo nombre de Microsoft 365 E5 Compliance— y pago por uso facturado en una suscripción de Azure asociada al tenant. En eDiscovery la licencia premium la necesita el custodio cuyos datos se analizan; en Audit, la retención depende de la licencia de quien generó el registro. Equivocarse aquí significa descubrir en pleno asunto que la evidencia ya venció o que la analítica prometida a Legal no está disponible.

**Por qué importa**

Sin una base clara de licencias y permisos, los asuntos se frenan en el peor momento: un custodio sin licencia premium, un investigador sin el rol para descifrar, una auditoría que retuvo 180 días cuando el regulador pide un año. Este módulo te deja una matriz de licencias y roles validada que reduce retrabajo, evita compras de emergencia y habilita decisiones informadas sobre Premium y el pago por uso.

**Qué vas a lograr**

- Ubicar eDiscovery, Audit y Data Security Investigations en el portal de Microsoft Purview.
- Distinguir las licencias por usuario (E3, E5, Purview Suite y complementos) del pago por uso facturado en Azure.
- Identificar los roles mínimos para buscar en la auditoría y para trabajar en un caso.
- Verificar que la auditoría está habilitada en tu tenant y documentar la evidencia.

> **Qué cambió.** Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama **Microsoft Purview Suite**, sin cambio funcional. Se agrega a Microsoft 365 E3 (u Office 365 E3 con EMS E3) e incluye Audit y eDiscovery; Microsoft 365 E5 ya lo trae ([cambio de nombre](https://samexpert.com/microsoft-365-defender-purview-renames/), [precios de Purview](https://www.microsoft.com/en-us/security/microsoft-purview-pricing)).

> **Atención.** Purview combina licencias por usuario con pago por uso facturado en Azure, que exige asociar el tenant a una suscripción activa ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)). Solo un Global Administrator puede hacer la asociación, el país o región queda fijo para el tenant y la habilitación por suscripción figura en vista previa ([habilitar el pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement)). En este programa se pagan por uso la auditoría de apps de IA no Microsoft, Data Security Investigations y la exportación por Graph con E3.

> **Consejo Ninja.** En tenants de prueba la auditoría puede venir apagada y tarda hasta 60 minutos en activarse ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)). Verifica `UnifiedAuditLogIngestionEnabled` con Exchange Online PowerShell: en Security & Compliance PowerShell esa propiedad siempre devuelve False ([buscar en la auditoría](https://learn.microsoft.com/en-us/purview/audit-search)).

> **Novedad.** La inclusión de Security Copilot en Microsoft 365 E5 se despliega de forma gradual desde el 18 de noviembre de 2025 y hoy alcanza también a E7: 400 SCU al mes por cada 1.000 licencias **pagadas**, hasta 10.000. Es la capacidad que consume Security Copilot dentro de eDiscovery; un tenant de prueba no debería contar con ella ([inclusión de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).

**¿Tienes poco tiempo?**

- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación
- [Get started with auditing solutions](https://learn.microsoft.com/en-us/purview/audit-get-started) · Documentación
- [Microsoft Purview Pricing | Microsoft Security](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Documentación

### Documentación, cursos y credenciales

- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación · Oficial · Microsoft Learn. Explica los dos modelos complementarios de Purview (licencia por usuario E3/E5 y pago por uso en Azure) y qué capacidades, como Data Security Investigations, se facturan por consumo.
- [Get started with auditing solutions](https://learn.microsoft.com/en-us/purview/audit-get-started) · Documentación · Oficial · Microsoft Learn. Pasos de puesta en marcha: licencias, roles Audit Manager/Audit Reader, habilitar SearchQueryInitiatedExchange por buzón, licenciar Audit (Premium) y crear políticas de retención.
- [Microsoft Purview Pricing | Microsoft Security](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Documentación · Oficial. Página de precios que ubica Purview en Microsoft 365 E5, el add-on Microsoft Purview Suite (incluye Audit y eDiscovery, requiere E3) y las ofertas de consumo.

**Manos a la obra**

1. `Laboratorio` Verifica la auditoría el día 0: en Exchange Online PowerShell ejecuta `Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled`; si devuelve False, actívala desde el portal de Purview y anota la hora. Unas horas después, busca una actividad tuya en Audit. Evidencia: captura del comando, hora de activación y primer registro encontrado ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).
2. `Laboratorio` Asigna roles con mínimo privilegio a tres cuentas de prueba: Audit Reader a la persona del SOC, eDiscovery Manager a la gestora de eDiscovery y ningún rol de Purview a la persona custodia. Comprueba que Audit Reader puede buscar pero no cambiar la configuración de auditoría y que eDiscovery Manager solo ve sus casos. Evidencia: matriz de roles con capturas ([empezar con la auditoría](https://learn.microsoft.com/en-us/purview/audit-get-started), [permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions)).
3. `Laboratorio` Arma la matriz de licencias de tu laboratorio: por cada cuenta de prueba, su licencia, si sus datos admiten funciones premium como custodio y cuánto se retiene su auditoría. Usa la tabla [Licencias](00_Programa.md#licencias) de esta guía y marca cada celda con su fuente. Evidencia: planilla con una fila por persona.
4. `Laboratorio` Con un Global Administrator, asocia el tenant a tu suscripción de Azure de Visual Studio Enterprise en un grupo de recursos exclusivo para Purview, crea un presupuesto con alertas al 50, 75 y 90 % y abre el Usage center para ver los medidores. Recuerda que la habilitación por suscripción está en vista previa y que el país o región queda fijo. Evidencia: captura de la asociación y del presupuesto ([habilitar el pago por uso](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement), [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage)).
5. `Solo producción` Haz el inventario real de licencias: cuenta usuarios con E3, E5, Purview Suite y el complemento «eDiscovery and Audit», y crúzalo con los perfiles que suelen ser custodios (dirección, finanzas, compras, Legal). Cómo hacerlo seguro: rol de solo lectura, sin cambiar asignaciones, y un informe con cifras agregadas para el dueño del presupuesto. Evidencia: informe de brechas con la recomendación (Premium, complemento o pago por uso).

<a id="i0"></a>

## I0 · Cómo aprender eDiscovery y Audit y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Ninja oficial de eDiscovery (2026): guías interactivas y recursos de aprendizaje; ruta de Learn de Audit (SC-401)*

Antes de entrar en materia conviene conocer las otras puertas. Para una credencial formal, el examen **SC-401** (Administering Information Security in Microsoft 365) mide licencias de Audit (Premium), investigación con Audit, políticas de retención de auditoría y búsquedas con eDiscovery dentro de su bloque de riesgos, alertas y actividades. La credencial **Applied Skills** «Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview» evalúa tareas en un laboratorio real. Y el **Ninja oficial de eDiscovery** en Tech Community, actualizado en mayo de 2026, mantiene su propio knowledge check.

Para mantenerte al día, tu radar es la página **What's new in Microsoft Purview**, que se actualiza cada mes, los avisos del Message Center y los webinars de la Microsoft Security Community: en 2025 hubo tres sesiones oficiales sobre la nueva experiencia de eDiscovery y el retiro del clásico. El portal de adopción de Purview agrupa por rol el Ninja, la guía interactiva de eDiscovery y las comunidades. Este módulo te ayuda a armar tu propio plan combinando esta guía con esas fuentes.

**Por qué importa**

Un equipo que aprende con fuentes desactualizadas toma decisiones con pantallas, límites y licencias que ya no existen. Definir desde el inicio qué credencial persigue cada rol, qué fuentes oficiales se revisan y con qué frecuencia reduce errores operativos y acorta la curva de aprendizaje de quienes se suman al equipo.

**Qué vas a lograr**

- Identificar las credenciales oficiales relacionadas (SC-401, Applied Skills y el Ninja de eDiscovery) y lo que mide cada una.
- Conocer los canales oficiales de novedades, webinars y comunidad de Purview.
- Armar un plan de estudio personal que combine esta guía con Microsoft Learn.

> **Novedad.** Las habilidades medidas de SC-401 se actualizaron el 28 de octubre de 2026. El bloque «Manage risks, alerts, and activities» incluye asignar licencias de Audit (Premium), investigar con Audit, configurar la retención de auditoría y buscar con eDiscovery ([guía de estudio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)). La versión en español llega unas ocho semanas después ([guía en español](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-401)).

> **Consejo Ninja.** No existe un «Audit Ninja» oficial: lo más cercano es la ruta de Learn [Audit and search activity in Microsoft Purview](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/), de cerca de 1 h 31 min y dos módulos, alineada con SC-401. Al Ninja oficial de eDiscovery se llega desde el [índice de Ninja Training](https://techcommunity.microsoft.com/tag/ninja%20training) o el [portal de adopción de Purview](https://adoption.microsoft.com/en-us/microsoft-security/purview/), que también reúne la guía interactiva y la credencial Applied Skills.

> **Atención.** Los tres webinars oficiales de 2025 —nueva experiencia y retiro del clásico (22 de abril), experiencia premium (4 de junio) y flujo moderno (26 de agosto)— se grabaron antes o durante el retiro del 31 de agosto de 2025, así que algunas pantallas pueden variar ([abril](https://www.youtube.com/watch?v=bmpY8QRmBnw), [junio](https://www.youtube.com/watch?v=EUrJy_oGXfw), [agosto](https://www.youtube.com/watch?v=B09em9NuZ20)).

> **Qué cambió.** La ruta de Applied Skills de retención, eDiscovery y Communication Compliance tiene nueve módulos (unas 7 h 50 min) y termina en una evaluación práctica para la credencial ([ruta](https://learn.microsoft.com/en-us/training/paths/purview-implement-retention-ediscovery-communication-compliance/), [credencial](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/)). Es el complemento práctico de SC-401.

**¿Tienes poco tiempo?**

- [Audit and search activity in Microsoft Purview (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) · Curso
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial
- [Microsoft Purview – Microsoft Adoption](https://adoption.microsoft.com/en-us/microsoft-security/purview/) · Documentación

### Documentación, cursos y credenciales

- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · oct 2026. Registro mensual de novedades de Purview; agosto de 2026 indica que la autenticación solo-aplicación para cmdlets de eDiscovery en Security & Compliance PowerShell no está soportada.
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Guía de estudio con las habilidades medidas desde el 28-oct-2026, donde el bloque "Manage risks, alerts, and activities" incluye licencias de Audit (Premium), investigación con Audit, políticas de retención de auditoría y búsquedas con eDiscovery.
- [Microsoft Purview – Microsoft Adoption](https://adoption.microsoft.com/en-us/microsoft-security/purview/) · Documentación · Oficial · Microsoft Adoption. Portal de adopción que agrupa por rol el eDiscovery Ninja training, la guía interactiva de eDiscovery, la ruta de auditoría y búsqueda, el Applied Skill SC-5007 y las comunidades de Purview.
- [Audit and search activity in Microsoft Purview (SC-401)](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje (≈1 h 31 min) con dos módulos: investigaciones con Purview Audit (incluye Copilot e IA) y búsqueda de contenido con eDiscovery, alineada al examen SC-401.
- [考试 SC-401 学习指南：在 Microsoft 365 中管理信息安全](https://learn.microsoft.com/zh-cn/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Versión localizada de la guía SC-401 cuyo texto completo lista explícitamente "Assign Purview Audit (Premium) licenses", "Investigate activities using Audit", "Configure audit retention policies" y "Search using eDiscovery".

### Webinars, videos y podcasts

- [eDiscovery New User Experience and Retirement of Classic (webinar)](https://www.youtube.com/watch?v=bmpY8QRmBnw) · Webinar · Empleado de Microsoft · David Robbins, John Wirtala, Alastair Sharp · Microsoft Security Community (YouTube) · 22 abr 2025. Webinar oficial que recorre la nueva experiencia de eDiscovery, la Content Search unificada, creación de casos, exportación y holds, y explica el retiro de la UI clásica.

**Manos a la obra**

1. `Laboratorio` Abre la [guía de estudio de SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y lleva a una tabla las cuatro habilidades de Audit y eDiscovery del bloque «Manage risks, alerts, and activities», con el módulo de esta guía que cubre cada una. Evidencia: tabla de correspondencia.
2. `Laboratorio` Completa la ruta [Audit and search activity in Microsoft Purview](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) (cerca de 1 h 31 min) y guarda el logro en tu perfil de Learn. Evidencia: captura del logro y tres dudas que quieras resolver en esta guía.
3. `Laboratorio` Mira el webinar oficial del [flujo moderno de eDiscovery](https://www.youtube.com/watch?v=B09em9NuZ20) (26 de agosto de 2025) con tu tenant abierto y anota, con su minuto, tres pantallas u opciones que hoy se vean distintas. Evidencia: notas con minuto y captura actual.
4. `Laboratorio` Crea tu registro de cambios: un recordatorio mensual para [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) y una primera entrada con tres novedades de 2026 que afecten a eDiscovery o Audit, cada una con fecha, estado y módulo de esta guía. Evidencia: registro con la primera entrada.
5. `Laboratorio` Desde el [portal de adopción de Purview](https://adoption.microsoft.com/en-us/microsoft-security/purview/) ubica el Ninja de eDiscovery, la guía interactiva y la credencial Applied Skills, y escribe tu plan personal: credencial objetivo, fecha y módulos de esta guía por semana. Evidencia: plan de una página aprobado por tu líder.

**¿Quieres profundizar?**

- [eDiscovery New User Experience and Retirement of Classic (webinar)](https://www.youtube.com/watch?v=bmpY8QRmBnw) · Webinar

<a id="i1"></a>

## I1 · eDiscovery hoy: la experiencia unificada, los permisos y las licencias

*L100–L200 · ~4 h · Origen: Ninja oficial de eDiscovery (2026): fundamentos, permisos y transición del clásico al moderno*

En la experiencia unificada de eDiscovery el **caso** es la unidad central: reúne a los miembros, los orígenes de datos, las búsquedas, las retenciones legales, los conjuntos de revisión y las exportaciones de un asunto. Ya no hay productos separados: las funciones estándar y premium conviven en el mismo flujo y se habilitan según la licencia. Las **estadísticas** reemplazaron a las colecciones, la indexación avanzada corre de forma automática y la antigua Content Search vive en un caso generado por el sistema. Los orígenes cubren Exchange Online, Teams, grupos de Microsoft 365, OneDrive, SharePoint y Viva Engage.

El cambio llegó por etapas: vista previa de la experiencia moderna en agosto de 2024, retiro de Content Search clásica y de los casos clásicos estándar el 26 de mayo de 2025, y retiro de todas las experiencias clásicas el 31 de agosto de 2025, salvo en los tenants operados por 21Vianet. Este módulo recorre el flujo de cinco pasos —evento disparador, caso, búsqueda y refinamiento, holds o exportación, y conjuntos de revisión—, los permisos (eDiscovery Manager frente a eDiscovery Administrator) y qué licencia necesita cada persona, que es la pregunta que más confusiones genera.

**Por qué importa**

Los asuntos legales y las investigaciones fallan más por el proceso que por la tecnología: un caso sin dueño, miembros con más acceso del necesario o custodios sin licencia para la analítica que se prometió a Legal. Entender el modelo unificado permite estandarizar cómo nace un asunto, quién lo ve y cuánto cuesta, y retirar procedimientos escritos para pantallas que ya no existen.

**Qué vas a lograr**

- Describir el flujo de trabajo de eDiscovery en cinco pasos, del evento disparador a los conjuntos de revisión.
- Explicar qué cambió frente al clásico: el caso como unidad central, las estadísticas y Content Search en un caso del sistema.
- Diferenciar eDiscovery Manager de eDiscovery Administrator y aplicar mínimo privilegio.
- Determinar qué licencia necesita un custodio para funciones premium y cuál no necesita quien revisa.
- Conocer los límites de casos por organización con funciones estándar y premium.

> **Qué cambió.** Línea de retiro del clásico: el 26 de mayo de 2025 se retiraron Content Search clásica, los casos clásicos de eDiscovery (Standard) y los parámetros de exportación de `New-ComplianceSearchAction`; los demás cmdlets de casos, holds, búsqueda y purga siguen soportados ([MC1055528](https://mc.merill.net/message/MC1055528)). El 31 de agosto de 2025 se retiraron todas las experiencias clásicas, salvo en los tenants operados por 21Vianet ([soluciones heredadas](https://learn.microsoft.com/en-us/purview/ediscovery)).

> **Atención.** La licencia premium la necesita el **custodio**: para analizar sus datos con funciones premium debe tener E5, o E1/E3 con Purview Suite o el complemento «eDiscovery and Audit». Los miembros del caso que recolectan y revisan no necesitan E5. Solo grupos de seguridad habilitados para correo pueden ser eDiscovery Managers y los eDiscovery Administrators deben ser usuarios individuales ([permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions)).

> **Novedad.** Desde el 16 de febrero de 2026, el caso de Content Search solo busca y exporta; holds y review sets requieren un caso completo ([Office 365 for IT Pros](https://office365itpros.com/2026/01/15/content-searches-change/)). El flujo recomendado tiene cinco pasos: evento disparador, caso, búsqueda y refinamiento, holds o exportación, y review sets ([flujo de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-workflow)).

> **Consejo Ninja.** Hay un límite de 10.000 casos por organización con funciones estándar y de 50.000 con premium ([límites](https://learn.microsoft.com/en-us/purview/edisc-ref-limits)). Define desde el primer día una convención de nombres, un dueño por caso y una política de cierre.

**¿Tienes poco tiempo?**

- [Learn about eDiscovery](https://learn.microsoft.com/en-us/purview/edisc) · Documentación
- [Learn about the eDiscovery workflow](https://learn.microsoft.com/en-us/purview/edisc-workflow) · Documentación
- [Assign permissions in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Documentación

### Documentación, cursos y credenciales

- [Learn about eDiscovery](https://learn.microsoft.com/en-us/purview/edisc) · Documentación · Oficial · Nuevo · Microsoft Learn · 29 jun 2026. Página central del eDiscovery unificado: cambios frente al clásico (indexación avanzada automática, estadísticas en lugar de colecciones, caso como unidad central) y tabla de funciones estándar vs. premium, incluido Security Copilot.
- [Learn about the eDiscovery workflow](https://learn.microsoft.com/en-us/purview/edisc-workflow) · Documentación · Oficial · Microsoft Learn. Describe el flujo en cinco pasos (evento disparador, caso, búsqueda y refinamiento, holds/exportación, review sets) y recuerda que las exportaciones de búsqueda expiran a los 14 días.
- [Assign permissions in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Documentación · Oficial · Microsoft Learn. Detalla los subgrupos eDiscovery Manager y eDiscovery Administrator, los roles RBAC relacionados y qué licencias necesitan los usuarios cuyos datos se analizan con funciones premium.
- [MC1055528 - Retiring Classic Content Search, Classic eDiscovery (Standard) Cases, Export PowerShell Parameters](https://mc.merill.net/message/MC1055528) · Documentación · Oficial · Message Center (archivo mc.merill.net) · 14 abr 2025. Anuncia el retiro el 26-may-2025 de la Content Search clásica, los casos clásicos de eDiscovery (Standard) y los parámetros de exportación de New/Get/Set-ComplianceSearchAction.
- [MC1002399 - Microsoft Purview: Classic eDiscovery experience will retire](https://mc.merill.net/message/MC1002399) · Documentación · Oficial · Message Center (archivo mc.merill.net) · 11 feb 2025. Aviso de Message Center (11-feb-2025) del retiro del eDiscovery clásico entre el 1-ago y el 1-sep de 2025 a favor del eDiscovery unificado.
- [Learn about eDiscovery features and components](https://learn.microsoft.com/en-us/purview/edisc-features-components) · Documentación · Oficial · Microsoft Learn. Resume componentes clave (auditoría de actividades, casos, caso Content Search, cloud attachments, orígenes de datos, descifrado, exportaciones, holds) e incluye soporte en preview para contenedores de SharePoint Embedded.
- [Microsoft Purview eDiscovery legacy solutions](https://learn.microsoft.com/en-us/purview/ediscovery) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Documento heredado que confirma que Microsoft retiró todas las experiencias clásicas (Content Search, eDiscovery Standard y Premium) el 31-ago-2025 y que su guía solo aplica a tenants operados por 21Vianet. *Nota:* Útil para entender la terminología antigua (Standard/Premium, custodios como eje)

### Anuncios y blogs oficiales

- [eDiscovery launches a modern, intuitive user experience](https://techcommunity.microsoft.com/blog/microsoft-security-blog/ediscovery-launches-a-modern-intuitive-user-experience/4215184) · Blog oficial · Empleado de Microsoft · Legado aún útil · ninachen · Microsoft Security Community Blog · 12 ago 2024. Lanzamiento en preview (ago-2024) de la nueva experiencia unificada de eDiscovery: mismo flujo para estándar y premium, Content Search dentro de un caso, selector de orígenes de datos y borrador de consultas con Copilot. *Nota:* Describe la preview; hoy la experiencia es la única disponible (salvo 21Vianet)

### Comunidad: blogs, libros, newsletters y eventos

- [Purview eDiscovery guide: cases, holds and exports (EpiFive)](https://www.epifive.com/blog/purview-ediscovery-new-experience-guide) · Blog · Comunidad · Nuevo · EpiFive · 11 oct 2026. Guía práctica de partner (oct-2026) para operar casos, holds, búsquedas KeyQL y exportaciones en la experiencia unificada, con requisitos de licencias y apps empresariales.
- [Microsoft Purview eDiscovery’s new look](https://alberthoitingh.com/2024/10/15/microsoft-purview-ediscoverys-new-look/) · Blog · MVP · Legado aún útil · Albert Hoitingh · Albert Hoitingh (blog) · 15 oct 2024. Comparación de un MVP entre el flujo clásico de eDiscovery Premium (custodios, colecciones, review sets) y la nueva interfaz unificada con nuevas condiciones de búsqueda. *Nota:* Escrito durante la preview; algunas limitaciones mencionadas pueden haber cambiado

**Manos a la obra**

1. `Laboratorio` Crea el caso `PRUEBA-001` con una convención de nombres y un dueño. Agrega como miembros a la gestora de eDiscovery y a un grupo de seguridad habilitado para correo, y verifica con una segunda cuenta eDiscovery Manager que no es miembro que no ve el caso. Evidencia: capturas de miembros y de la vista de la segunda cuenta ([permisos de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-permissions)).
2. `Laboratorio` Recorre los cinco pasos del [flujo de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-workflow) con una solicitud simulada de Legal: evento disparador, caso, búsqueda sobre un usuario y un equipo de Teams, estadísticas y una muestra. Evidencia: solicitud simulada, captura de las estadísticas y nota de qué harías a continuación (hold o exportación).
3. `Laboratorio` Abre el caso de Content Search generado por el sistema, ejecuta una búsqueda e intenta crear un hold o agregar resultados a un review set. Documenta que, desde el 16 de febrero de 2026, ese caso solo busca y exporta ([Office 365 for IT Pros](https://office365itpros.com/2026/01/15/content-searches-change/)). Evidencia: captura de las opciones disponibles.
4. `Laboratorio parcial` Comprueba la regla de licencia por custodio: en una búsqueda sobre un custodio con E5 confirma que las funciones premium están disponibles y documenta qué cambiaría con un custodio E3 sin complemento. Limitación: la prueba de Microsoft 365 E5 solo trae licencias E5; para ver el caso E3 necesitas un tenant con E3 y la [prueba de Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial). Evidencia: tabla de funciones por tipo de custodio.
5. `Solo producción` Revisa quién integra eDiscovery Manager y eDiscovery Administrator en producción y compáralo con la lista autorizada por Legal. Cómo hacerlo seguro: solo lectura de la membresía de los grupos de roles, ningún cambio directo, propuesta de reducción por gestión de cambios y comparación con la tabla oficial de [roles y grupos de roles](https://learn.microsoft.com/en-us/defender-office-365/scc-permissions). Evidencia: informe con personas a retirar y justificación de las que quedan.

<a id="i2"></a>

## I2 · Audit Standard y Audit Premium

*L100–L200 · ~4 h · Origen: Ruta de Learn «Audit and search activity in Microsoft Purview» (SC-401), módulo de Audit*

El registro de auditoría unificado de Microsoft 365 responde la pregunta que toda investigación se hace primero: quién hizo qué, cuándo, desde dónde y sobre qué objeto. **Audit (Standard)** viene habilitado por defecto en los tenants administrados, retiene 180 días los registros generados desde el 17 de octubre de 2023 —antes eran 90— y se consulta con trabajos de búsqueda que siguen corriendo aunque cierres el navegador: hasta diez simultáneos por usuario, conservados durante 30 días.

**Audit (Premium)** agrega un año de retención por defecto para Exchange, SharePoint, OneDrive y Entra ID de los usuarios con licencia, hasta 50 políticas de retención personalizadas, la opción de 10 años con un complemento y aproximadamente el doble de ancho de banda en la Management Activity API. Microsoft sigue presentándolo como la solución con insights para investigaciones forenses, pero eventos clave como MailItemsAccessed, los envíos y las búsquedas ya llegan también a Standard. Este módulo te enseña a decidir con datos qué necesitas realmente.

**Por qué importa**

La auditoría es evidencia que vence. Si tu organización necesita reconstruir hechos de hace ocho meses y solo retiene 180 días, la respuesta llega tarde y no hay forma de recuperarla. Elegir entre Standard y Premium, y qué políticas configurar, es una decisión de riesgo con costo conocido que conviene tomar antes del primer incidente o requerimiento regulatorio.

**Qué vas a lograr**

- Comparar Audit (Standard) y Audit (Premium) en retención, eventos, propiedades y ancho de banda de API.
- Ejecutar búsquedas de auditoría por trabajos y exportar sus resultados.
- Crear una política de retención de auditoría y explicar por qué no es retroactiva.
- Habilitar y verificar los eventos de búsqueda SearchQueryInitiated.
- Identificar qué registros tienen retención fija y cuáles dependen de la licencia del usuario.

> **Qué cambió.** Audit (Standard) retiene 180 días los registros generados desde el 17 de octubre de 2023; antes eran 90. Algunas guías de licenciamiento de terceros siguen diciendo 90 días: manda Learn ([retención de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)).

> **Atención.** Una política de retención de auditoría no es retroactiva: lo que ya venció no vuelve. Admite hasta 50 políticas y requiere el rol Organization Configuration ([retención de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)). Los registros de entidades no usuario (service principals, sistema y apps) se retienen un año fijo y no aceptan políticas personalizadas ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).

> **Novedad.** La búsqueda de auditoría trabaja con trabajos asíncronos que siguen corriendo con el navegador cerrado: hasta 10 simultáneos por usuario (solo uno sin filtros), con resultados conservados 30 días. La búsqueda clásica se retiró el 30 de noviembre de 2023 ([buscar en la auditoría](https://learn.microsoft.com/en-us/purview/audit-search), [soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).

> **Consejo Ninja.** Antes de justificar Premium, compara con datos: MailItemsAccessed, los envíos y las búsquedas ya están en Standard para E3 y E5. Premium aporta la retención extendida (un año por defecto y hasta 10 con complemento), los insights inteligentes y eventos de alto valor que Microsoft sigue asociando a investigaciones forenses, propiedades como `SensitivityLabel` en MailItemsAccessed y `AppAccessContext` en actividades de Teams, y cerca del doble de ancho de banda en la Management Activity API ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)). Qué eventos siguen siendo exclusivos de Premium es un punto abierto: revisa la sección de limitaciones.

**¿Tienes poco tiempo?**

- [Learn about auditing solutions in Microsoft Purview](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) · Documentación
- [Manage audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Documentación
- [Search the audit log](https://learn.microsoft.com/en-us/purview/audit-search) · Documentación

### Documentación, cursos y credenciales

- [Learn about auditing solutions in Microsoft Purview](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 may 2026. Compara Audit (Standard) y Audit (Premium): retención de 180 días vs. 1 año por defecto, 10 años con add-on, insights inteligentes y mayor ancho de banda en la Management Activity API.
- [Manage audit log retention policies](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Documentación · Oficial · Microsoft Learn. Explica la política por defecto de Audit (Premium) (1 año para Exchange, SharePoint, OneDrive y Entra), el límite de 50 políticas y los requisitos de licencia para 1 y 10 años.
- [Search the audit log](https://learn.microsoft.com/en-us/purview/audit-search) · Documentación · Oficial · Microsoft Learn. Describe la búsqueda por trabajos (hasta 10 simultáneos por usuario, uno sin filtro, conservados 30 días), los roles necesarios y cómo verificar UnifiedAuditLogIngestionEnabled.
- [Conduct investigations with Microsoft Purview Audit](https://learn.microsoft.com/en-us/training/modules/purview-audit-search-investigate/) · Curso · Oficial · Microsoft Learn. Módulo (57 min) para configurar Audit, buscar en portal y PowerShell, investigar actividad de Copilot/IA y analizar MailItemsAccessed con Audit (Premium).

**Manos a la obra**

1. `Laboratorio` Lanza tres trabajos de búsqueda de auditoría: toda la actividad de una cuenta de prueba en siete días, solo `MailItemsAccessed` de esa cuenta y `FileAccessed` sobre un sitio de SharePoint. Cierra el navegador, vuelve más tarde y exporta los tres CSV. Evidencia: lista de trabajos y archivos exportados ([buscar en la auditoría](https://learn.microsoft.com/en-us/purview/audit-search)).
2. `Laboratorio` Habilita SearchQueryInitiatedExchange en el buzón de prueba siguiendo la [guía de puesta en marcha](https://learn.microsoft.com/en-us/purview/audit-get-started), busca «licitación» en Outlook en la web y en SharePoint, y unas horas después encuentra ambos eventos. Evidencia: los dos registros con la consulta escrita y la hora.
3. `Laboratorio` Crea una política de retención de auditoría de un año para una carga que la política predeterminada de Premium no cubre (por ejemplo, Teams) y una cuenta de prueba. Anota la fecha de creación: es la línea desde la que rige, porque no es retroactiva ([retención de auditoría](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)). Evidencia: captura de la política y nota de alcance.
4. `Laboratorio parcial` Abre un registro `MailItemsAccessed` y un registro de mensajes de Teams de una cuenta E5, y marca las propiedades que aporta Premium (`SensitivityLabel`, `AppAccessContext`). Limitación: en la prueba E5 todos los usuarios tienen Premium, así que no puedes comparar lado a lado con un usuario solo Standard ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)). Evidencia: JSON anotado.
5. `Solo producción` Mide la brecha de retención: para una muestra de usuarios E3 y E5, consulta la fecha del registro más antiguo disponible y compárala con tu política interna o con lo que exige el regulador. Cómo hacerlo seguro: rol Audit Reader asignado por tiempo limitado, consultas solo de metadatos, sin exportar contenido y con la justificación registrada en el ticket. Evidencia: informe de brecha con la recomendación (Premium, política personalizada o SIEM).

<a id="i3"></a>

## I3 · Búsqueda de contenido y sintaxis de consultas (KeyQL)

*L100–L200 · ~4 h · Origen: Ninja oficial de eDiscovery (2026): búsqueda y recolección; ruta SC-401, módulo de búsqueda con eDiscovery*

Buscar bien es la diferencia entre producir lo pertinente y entregarlo todo. En eDiscovery construyes la consulta con el **generador de condiciones** (palabras clave, operadores y condiciones por propiedad) o escribes directamente en **KeyQL** (Keyword Query Language), con un editor que autocompleta propiedades, sugiere valores y marca errores. Las reglas básicas importan: todas las búsquedas usan UTC, no distinguen mayúsculas, los operadores AND, OR, NOT y NEAR van en mayúsculas, un espacio equivale a OR y una condición vacía devuelve todo el alcance.

Antes de retener o exportar, valida la consulta con **estadísticas** y muestras: el keyword report muestra cuántos ítems aporta cada término, siempre que uses al menos dos cuadrículas de palabras clave. Ojo con la confusión más común: KeyQL no es KQL. El explorador avanzado de review sets, en vista previa, usa un subconjunto de Kusto; la búsqueda usa KeyQL. Security Copilot puede proponerte un borrador de KeyQL a partir de lenguaje natural, que siempre debes revisar.

**Por qué importa**

Una consulta mal construida tiene costos visibles: horas de revisión de material irrelevante, exportaciones que exceden límites o, peor, evidencia pertinente que nunca se preservó. Documentar consultas probadas con estadísticas permite defender ante la contraparte o un regulador por qué se buscó así, y reduce el volumen que llega a revisión.

**Qué vas a lograr**

- Construir consultas con el generador de condiciones y con el editor de KeyQL.
- Aplicar las reglas de sintaxis: UTC, operadores en mayúsculas, espacio como OR y condiciones vacías.
- Obtener un keyword report con dos o más cuadrículas y ajustar la consulta según el aporte de cada término.
- Distinguir KeyQL de KQL y saber cuándo se usa cada uno.
- Documentar una consulta con su justificación, sus estadísticas y su versión.

> **Atención.** Una condición vacía devuelve **todo** el alcance, un espacio entre términos equivale a OR, los operadores AND, OR, NOT y NEAR van en mayúsculas y todas las búsquedas usan UTC: convierte tus fechas antes de filtrar ([crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query)).

> **Consejo Ninja.** Para obtener el keyword report en las estadísticas necesitas al menos dos cuadrículas de palabras clave, que al convertirse a KeyQL se separan con `c:s` ([generador de condiciones](https://learn.microsoft.com/en-us/purview/edisc-condition-builder)). El editor de KeyQL autocompleta propiedades, sugiere valores y marca errores, pero no admite comillas anidadas ([KeyQL](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language)).

> **Novedad.** Security Copilot puede redactar un borrador de KeyQL desde lenguaje natural, en vista previa ([crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query)). Es un borrador: valídalo con estadísticas y conserva en el expediente la versión final que ejecutaste.

> **Qué cambió.** La antigua herramienta User Data Search para solicitudes de titulares de datos se integró en eDiscovery ([crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query)). Coordina esas búsquedas con privacidad: se tratan en [O3](04_Nivel_4_Operacion.md#o3).

**¿Tienes poco tiempo?**

- [Create a search for a case in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Documentación
- [Use the condition builder to create search queries in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-condition-builder) · Documentación
- [eDiscovery Workflow in the Modern UX (webinar)](https://www.youtube.com/watch?v=B09em9NuZ20) · Webinar

**KeyQL frente a KQL: dos lenguajes que se confunden**

| Aspecto | KeyQL (búsquedas de eDiscovery) | KQL (explorador avanzado de review sets, Sentinel y Defender XDR) |
|---|---|---|
| Dónde se usa | Búsquedas del caso, holds por consulta y consultas dentro del review set | Explorador avanzado de review sets (vista previa, sobre `ReviewSetTable`), Sentinel y búsqueda avanzada de Defender XDR |
| Qué consulta | El índice de contenido de Exchange, Teams, grupos de Microsoft 365, OneDrive, SharePoint y Viva Engage | Tablas estructuradas: `ReviewSetTable`, `OfficeActivity`, `CloudAppEvents` |
| Operadores | AND, OR, NOT y NEAR en mayúsculas; un espacio equivale a OR | Operadores de tabla encadenados con una barra vertical (filtrar, agrupar, proyectar) |
| Mayúsculas en los términos | La búsqueda no distingue mayúsculas | Depende del operador de comparación que elijas |
| Fechas | UTC en todas las búsquedas | Campos de tiempo en UTC |
| Validación | Estadísticas, keyword report (con dos o más cuadrículas) y muestras | Conteos y agregaciones sobre el propio resultado |
| Asistencia de IA | Security Copilot redacta un borrador de KeyQL (vista previa) | Se trata en los programas de Sentinel y Defender XDR |
| Error típico | Una condición vacía devuelve todo el alcance | Pegar una consulta de Sentinel en el editor de búsquedas del caso |

Fuentes: [crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query), [generador de condiciones](https://learn.microsoft.com/en-us/purview/edisc-condition-builder), [KeyQL](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language) y [explorador avanzado](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer).

### Documentación, cursos y credenciales

- [Create a search for a case in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Documentación · Oficial · Microsoft Learn. Reglas de búsqueda: zona horaria UTC, búsquedas insensibles a mayúsculas, operadores AND/OR/NOT/NEAR en mayúsculas, el espacio equivale a OR y una condición vacía devuelve todo; incluye borrador de KeyQL con Copilot (preview).
- [Use the condition builder to create search queries in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-condition-builder) · Documentación · Oficial · Microsoft Learn. Explica el generador de condiciones (Keywords, AND/OR, operadores por condición) y cómo varias cuadrículas de palabras clave generan informes de palabra clave separados por c:s.
- [Use Keyword Query Language to create search queries in eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language) · Documentación · Oficial · Microsoft Learn · 4 sep 2025. Describe el editor KeyQL con autocompletado, sugerencias de valores y detección de errores, útil para pegar consultas complejas de la contraparte.

### Webinars, videos y podcasts

- [eDiscovery Workflow in the Modern UX (webinar)](https://www.youtube.com/watch?v=B09em9NuZ20) · Webinar · Empleado de Microsoft · David Robbins, Aaron Thorp, Mahantesh Hurkadli, Natasha Mahapatro · Microsoft Security Community (YouTube) · 26 ago 2025. Webinar oficial sobre la pestaña de orígenes de datos, el nuevo generador de consultas y las opciones de exportación de la experiencia moderna.
- [Introducing the New Purview eDiscovery User Interface & Exclusive Look at DSPM for AI](https://www.youtube.com/watch?v=vSK5Gndenr0) · Video · Empleado de Microsoft · Bhavana Bhatia, Sergio Salinas · Microsoft SLED Security & Compliance (YouTube). Recorrido de especialistas técnicos de Microsoft por la nueva UI (búsqueda, generador de consultas, orígenes de datos, exportación y políticas de hold) con enfoque sector público.

**Manos a la obra**

1. `Laboratorio` Siembra el contenido sintético del «Proyecto Cóndor» (veinte correos, cinco documentos y un chat de Teams con términos y fechas conocidos) y guarda la lista como verdad de referencia. Luego crea con el [generador de condiciones](https://learn.microsoft.com/en-us/purview/edisc-condition-builder) una consulta con dos cuadrículas de palabras clave, fechas y remitente, y obtén el keyword report. Evidencia: keyword report comparado con tu lista.
2. `Laboratorio` Convierte la consulta a KeyQL, ubica el separador `c:s` y prueba las reglas de sintaxis con conteos: «Cóndor licitación» frente a «Cóndor AND licitación», el operador en minúsculas y una condición vacía. Evidencia: tabla con la consulta y su conteo ([crear una búsqueda](https://learn.microsoft.com/en-us/purview/edisc-search-query), [KeyQL](https://learn.microsoft.com/en-us/purview/edisc-keyword-query-language)).
3. `Laboratorio` Comprueba el efecto de UTC: siembra un correo enviado a las 22:00 de tu hora local y busca ese día con y sin convertir el rango a UTC (Ciudad de México está en UTC−6, Buenos Aires en UTC−3 y Santiago en UTC−4 o UTC−3 según la época del año). Evidencia: los dos conteos y la regla que adoptas para el equipo.
4. `Laboratorio` Mide la calidad de la consulta: con la muestra y tu verdad de referencia calcula cuántos ítems sembrados encontró (exhaustividad) y cuántos de los encontrados eran pertinentes (precisión). Ajusta a una versión 2 y anótala en un registro de consultas con versión, fecha, autor, justificación y estadísticas. Evidencia: registro con dos versiones.
5. `Laboratorio parcial` Pide a Security Copilot un borrador de KeyQL desde lenguaje natural («correos de Ana a proveedores externos sobre la licitación Cóndor en marzo de 2026») y compáralo en estadísticas con tu consulta manual. Limitación: la función está en vista previa y la inclusión de SCU aplica a licencias E5 pagadas; en producción, usa un caso piloto con datos de prueba y vigila el consumo ([inclusión de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)). Evidencia: ambas consultas con sus conteos y tu corrección.

<a id="reto-inicial"></a>

## Reto del nivel

**Expediente de arranque.** Legal (simulado) te pide confirmar si el «Proyecto Cóndor» dejó rastros en correo, Teams y OneDrive de dos cuentas de prueba. Entrega un documento de dos páginas con: el caso `PRUEBA-` con sus miembros verificados; la consulta KeyQL en su versión 2, con keyword report, precisión y exhaustividad medidas contra tu verdad de referencia; una búsqueda de auditoría que muestre tu propia actividad sobre el caso; la política de retención de auditoría que creaste y su fecha de vigencia; y la matriz de licencias que explica qué funciones premium aplican a cada custodio. Todas las fechas en UTC y cada afirmación con su fuente.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuánto tiempo retiene Audit (Standard) los registros generados desde el 17 de octubre de 2023?
   - a) 90 días
   - b) 180 días
   - c) Un año
   - d) Diez años

2. ¿Cuándo retiró Microsoft todas las experiencias clásicas de eDiscovery (Content Search, Standard y Premium), salvo en los tenants operados por 21Vianet?
   - a) 26 de mayo de 2025
   - b) 16 de febrero de 2026
   - c) 31 de agosto de 2025
   - d) 15 de octubre de 2027

3. ¿Quién puede quitar miembros de un caso de eDiscovery?
   - a) La persona que creó el caso
   - b) Cualquier eDiscovery Manager que sea miembro del caso
   - c) Un integrante de Organization Management
   - d) Un eDiscovery Administrator

4. Un custodio tiene Microsoft 365 E3 sin complementos. ¿Qué hace falta para analizar sus datos con funciones premium?
   - a) Nada: basta con que quien revisa tenga E5
   - b) Que el custodio tenga Purview Suite o el complemento «eDiscovery and Audit»
   - c) Una licencia de Security Copilot para el custodio
   - d) Que el caso lo cree un eDiscovery Administrator

5. En una búsqueda de eDiscovery, ¿qué significa un espacio entre dos términos?
   - a) AND
   - b) NEAR
   - c) Frase exacta
   - d) OR

6. ¿Qué devuelve una condición vacía en una búsqueda de eDiscovery?
   - a) Ningún resultado
   - b) Todo el contenido del alcance de la búsqueda
   - c) Solo los ítems parcialmente indexados
   - d) Un error de sintaxis

7. ¿Qué necesitas para que las estadísticas de una búsqueda muestren el keyword report?
   - a) Al menos dos cuadrículas de palabras clave
   - b) Una licencia de Security Copilot
   - c) Agregar los resultados a un review set
   - d) Escribir la consulta en KQL

8. ¿Cuántos trabajos de búsqueda de auditoría simultáneos puede tener un usuario?
   - a) Tres
   - b) Cinco
   - c) Diez
   - d) Cincuenta

9. Hoy creas una política de retención de auditoría de un año. ¿Qué pasa con los registros que ya vencieron?
   - a) Se recuperan los de los últimos doce meses
   - b) Nada: los cambios no son retroactivos
   - c) Se recuperan solo los de usuarios con E5
   - d) Se recuperan si agregas el complemento de 10 años

10. ¿Qué hace falta para usar funciones de pago por uso de Purview, como Data Security Investigations?
   - a) Tener Microsoft 365 E7
   - b) Activar Audit (Premium)
   - c) Comprar SCU de Security Copilot
   - d) Asociar el tenant a una suscripción de Azure activa

11. ¿Qué es Microsoft Purview Suite?
   - a) El nuevo nombre de Microsoft 365 E5 Compliance: un complemento sobre E3 que incluye Audit y eDiscovery
   - b) Un plan de pago por uso para Data Security Investigations
   - c) Una edición gratuita de Purview para tenants E3
   - d) El paquete de Security Copilot para Purview

12. Para usuarios con licencias E3 y E5, ¿en qué nivel de auditoría está el evento MailItemsAccessed?
   - a) Solo en Audit (Premium)
   - b) Solo con el complemento de 10 años
   - c) En Audit (Standard)
   - d) Solo con pago por uso

13. No existe un «Audit Ninja» oficial. ¿Qué recurso oficial es lo más cercano?
   - a) La ruta de Learn «Audit and search activity in Microsoft Purview», alineada con SC-401
   - b) Los escenarios Ninja de Information Protection y DLP en Learn
   - c) El módulo de MS-101 sobre Audit (Premium)
   - d) El Ninja de Communication Compliance

14. ¿Dónde se usa un subconjunto de KQL (Kusto) dentro de eDiscovery?
   - a) En el editor de búsquedas del caso
   - b) En el generador de condiciones de los holds
   - c) En la configuración de la exportación
   - d) En el explorador avanzado de review sets (vista previa)

15. ¿Qué grupo de roles permite buscar en la auditoría sin poder cambiar su configuración?
   - a) Audit Manager
   - b) Audit Reader
   - c) eDiscovery Administrator
   - d) Organization Configuration

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

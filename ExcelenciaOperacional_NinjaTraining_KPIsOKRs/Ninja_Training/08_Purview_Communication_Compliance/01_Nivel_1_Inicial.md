# Nivel 1 · Inicial · Fundamentos

*Microsoft Purview Communication Compliance e Information Barriers Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

El portal unificado y sus permisos, qué canales supervisa Communication Compliance y con qué licencias, cómo se diseñan políticas con plantillas, clasificadores y condiciones, y cómo se revisa y remedia una alerta. Terminas con una política piloto probada y su flujo de revisión documentado.

*L100–L200 · 5 módulos · ~17 horas · 22 recursos*

**Módulos de este nivel:** [P0 Portal y permisos](#p0) · [I0 Cómo aprender](#i0) · [I1 Canales y licencias](#i1) · [I2 Políticas y clasificadores](#i2) · [I3 Revisión y remediación](#i3)

<a id="p0"></a>

## P0 · Prerrequisitos: Microsoft Purview, el portal unificado y los permisos

*L100–L200 · ~2 h · Origen: Ninja oficial de CC · Getting Started (permisos), actualizado al portal unificado de Purview*

Communication Compliance e Information Barriers viven hoy en el **portal de Microsoft Purview**, que reemplazó al portal de cumplimiento clásico entre el 14 de noviembre y el 14 de diciembre de 2024, con paridad de configuraciones. En el portal unificado, lo que ves depende de tus permisos y de las suscripciones del tenant: si una solución no aparece, casi siempre falta un rol o una licencia. Por eso este módulo empieza por el modelo de permisos de Purview: roles, grupos de roles, roles de Microsoft Entra ID, PIM para grupos y unidades administrativas.

Communication Compliance es especialmente sensible a los permisos: un administrador global no tiene acceso por defecto a sus alertas, y la separación entre quien configura políticas y quien revisa mensajes es parte del diseño. En julio de 2026 llegó una pieza útil para revisores temporales y consultores: las asignaciones a grupos de roles con fecha de vencimiento. También vas a dejar activa la auditoría, que en muchos tenants de prueba viene apagada y es la base de toda la evidencia que construirás después.

**Por qué importa**

Un permiso mal asignado en Communication Compliance no es un problema técnico: es una persona leyendo conversaciones que no debía leer o un equipo de cumplimiento sin acceso a alertas regulatorias. Dominar el portal y el control de acceso de Purview desde el inicio reduce ese riesgo, acelera las revisiones de accesos que piden las auditorías y evita semanas de diagnóstico cuando una solución «no aparece».

**Qué vas a lograr**

- Ubicar Communication Compliance, Information Barriers, Auditoría y Roles y alcances en el portal de Microsoft Purview.
- Explicar la diferencia entre roles, grupos de roles, roles de Entra ID y PIM para grupos, y sus tiempos de aplicación.
- Asignar un grupo de roles con fecha de vencimiento a una cuenta de prueba y verificar sus efectos.
- Comprobar que la auditoría unificada está activa en el tenant de laboratorio.

> **Qué cambió.** El portal de cumplimiento clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 y las configuraciones pasaron con paridad al portal de Microsoft Purview. Actualiza procedimientos internos, capturas de capacitación y listas de permitidos del proxy que aún apunten al portal anterior ([MC939918](https://mc.merill.net/message/MC939918)).

> **Atención.** En el portal unificado, la visibilidad de cada solución depende de tus permisos y de la suscripción del tenant. Si usas PIM para grupos de seguridad asignados a grupos de roles de Purview, la activación puede tardar hasta 2 horas en aplicarse: no la dejes para el día de una revisión urgente ([portal de Purview](https://learn.microsoft.com/en-us/purview/purview-portal)).

> **Novedad.** Desde julio de 2026, las asignaciones a grupos de roles de Purview pueden tener fecha de vencimiento (de 1 día a 2 años), ideal para revisores temporales o consultores; no aplica a los roles eDiscovery Administrator ni eDiscovery Manager ([novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new)).

> **Consejo Ninja.** En muchos tenants de prueba la auditoría viene apagada y tarda hasta 60 minutos en activarse: hazlo el día 0, porque es la base de toda la evidencia de Communication Compliance e Information Barriers ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).

**¿Tienes poco tiempo?**

- [Learn about the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-portal) · Documentación
- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación
- [MC939918 - Reminder: Microsoft Purview classic compliance portal will retire](https://mc.merill.net/message/MC939918) · Herramienta

### Documentación, cursos y credenciales

- [Permissions in the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-permissions) · Documentación · Oficial · Microsoft Learn. Modelo RBAC del portal de Microsoft Purview (roles, grupos de roles, roles de Entra, PIM para grupos, precedencia y alcance) con enlaces a permisos por solución, incluidas CC e IB.
- [Learn about the Microsoft Purview portal](https://learn.microsoft.com/en-us/purview/purview-portal) · Documentación · Oficial · Microsoft Learn. Describe el portal unificado de Microsoft Purview (inicio, búsqueda global, configuración y roles centralizados) y qué funciones se reubicaron al retirarse el portal de cumplimiento clásico.

### Laboratorios, GitHub y herramientas

- [MC939918 - Reminder: Microsoft Purview classic compliance portal will retire](https://mc.merill.net/message/MC939918) · Herramienta · Oficial · Microsoft (Message Center) · Microsoft 365 Message Center Archive (mc.merill.net) · 22 nov 2024. Aviso oficial archivado: el portal de cumplimiento clásico se retiró entre el 14-nov y el 14-dic-2024 y todas las configuraciones pasaron con paridad al nuevo portal de Purview.

**Manos a la obra**

1. `Laboratorio` En tu prueba de Microsoft 365 E5, verifica que la auditoría unificada esté activa (actívala si no lo está y espera hasta 60 minutos) y guarda la captura o la salida de PowerShell como evidencia del día 0 ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).
2. `Laboratorio` Recorre el portal de Purview y documenta en una tabla dónde están Communication Compliance, Information Barriers, Auditoría y Roles y alcances; anota qué soluciones no ves y qué permiso o licencia falta en cada caso ([portal de Purview](https://learn.microsoft.com/en-us/purview/purview-portal)).
3. `Laboratorio` Asigna a una cuenta de prueba el grupo de roles Communication Compliance Analysts con una fecha de vencimiento de 7 días, verifica en Roles y alcances la asignación y su vencimiento, y comprueba qué puede ver esa cuenta ([permisos de Purview](https://learn.microsoft.com/en-us/purview/purview-permissions)).
4. `Laboratorio` Inicia sesión con un administrador global sin roles de Communication Compliance, intenta abrir las alertas de la solución y documenta el resultado: no debería verlas ([guía de privacidad](https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy)).
5. `Laboratorio` Configura PIM para un grupo de seguridad asignado a un grupo de roles de CC, activa la pertenencia y mide cuánto tarda en aplicarse el permiso (puede llegar a 2 horas); registra los tiempos para tu procedimiento ([portal de Purview](https://learn.microsoft.com/en-us/purview/purview-portal)).

<a id="i0"></a>

## I0 · Cómo aprender Communication Compliance e Information Barriers y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Ninja oficial de CC · knowledge checks y recursos adicionales*

Antes de entrar en materia, conoce las otras puertas. Microsoft Learn ofrece un módulo específico sobre Communication Compliance (algo más de una hora, con evaluación final) que forma parte de dos rutas: la de retención, eDiscovery y Communication Compliance, y la de protección de las interacciones de Microsoft 365 Copilot. La credencial **Applied Skills «Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview»** (APL-5007) evalúa en un laboratorio interactivo de 2 horas tareas como delegar permisos de Communication Compliance y crear sus políticas, y se puede rendir en español.

El examen **SC-401** es la certificación de referencia de seguridad de la información en Microsoft 365, pero su guía de estudio vigente no mide Communication Compliance ni Information Barriers: si necesitas una credencial formal sobre CC, la Applied Skill es la vía. El Ninja oficial de 2022, con sus knowledge checks por sección, sigue sirviendo para los conceptos. Para mantenerte al día, la página de novedades de Purview y los archivos del Message Center son tu radar, y para dudas técnicas, la Microsoft Security Community. Este módulo te ayuda a combinar todo en un plan propio.

**Por qué importa**

Un equipo de cumplimiento que aprende sin un plan termina con conocimiento disperso y sin evidencia de competencia. Alinear esta guía con la Applied Skill APL-5007 y con las fuentes oficiales de novedades da una ruta verificable, reduce el tiempo de incorporación de nuevos revisores y deja constancia de capacitación, algo que los reguladores y la auditoría interna suelen pedir a quienes supervisan comunicaciones.

**Qué vas a lograr**

- Identificar las rutas de Learn y las credenciales que cubren Communication Compliance e Information Barriers.
- Distinguir qué mide SC-401 y qué mide la Applied Skill APL-5007.
- Armar un plan de estudio personal que combine esta guía, el Ninja oficial y los laboratorios de Learn.
- Configurar una rutina de seguimiento de novedades con la página What’s new de Purview y el Message Center.

> **Atención.** La guía de estudio de SC-401 (actualizada el 14 de septiembre de 2026) cubre protección de la información, DLP, retención y riesgos y alertas (Insider Risk, Audit y DSPM para IA), pero no menciona Communication Compliance ni Information Barriers ([guía SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401)). Para una credencial sobre CC, usa la Applied Skill.

> **Consejo Ninja.** La Applied Skill de retención, eDiscovery y Communication Compliance se evalúa en un laboratorio interactivo de 2 horas, tiene una ruta de preparación de 7 h 50 min en 9 módulos y se puede rendir en español; si lanzas el laboratorio, debes esperar 72 horas para relanzarlo ([credencial](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/), [guía APL-5007](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-5007)).

> **Qué cambió.** El Ninja oficial de Communication Compliance (19 de abril de 2022, actualizado en junio de 2023) usa nombres antiguos y no cubre Copilot, el pago por uso ni Information Barriers, pero sus knowledge checks por sección siguen sirviendo para repasar conceptos ([Become a Communication Compliance Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283)).

**¿Tienes poco tiempo?**

- [Detect and address communication risks with Microsoft Purview Communication Compliance](https://learn.microsoft.com/en-us/training/modules/m365-compliance-insider-prepare-communication-compliance/) · Curso
- [Microsoft Applied Skills: Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/) · Credencial
- [Study guide for the Applied Skills assessment lab: Implement retention, eDiscovery, and Microsoft Purview Communication Compliance (APL-5007)](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-5007) · Credencial

### Documentación, cursos y credenciales

- [Study guide for the Applied Skills assessment lab: Implement retention, eDiscovery, and Microsoft Purview Communication Compliance (APL-5007)](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-5007) · Credencial · Oficial · Nuevo · Microsoft Learn · 14 sep 2026. Lista de tareas evaluadas: delegar permisos de CC, crear políticas de CC y configurar sus ajustes, junto con retención y eDiscovery.
- [Detect and address communication risks with Microsoft Purview Communication Compliance](https://learn.microsoft.com/en-us/training/modules/m365-compliance-insider-prepare-communication-compliance/) · Curso · Oficial · Microsoft Learn. Módulo de Learn (1 h 6 min, 11 unidades) que cubre planificación, flujo de trabajo, políticas, alertas, reportes, interacciones riesgosas en apps de IA e integración con SIEM, con evaluación final.
- [Microsoft Applied Skills: Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/) · Credencial · Oficial · Microsoft Learn. Credencial con laboratorio interactivo de 2 h que evalúa, entre otras tareas, implementar Communication Compliance; ruta de preparación de 7 h 50 min y 9 módulos.
- [Study guide for Exam SC-401: Administering Information Security in Microsoft 365](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · Microsoft Learn · 14 sep 2026. Guía oficial del examen SC-401 (skills al 28-oct-2026): protección de información, DLP/retención y riesgos/alertas (IRM, Audit, DSPM for AI); no menciona Communication Compliance ni Information Barriers.

### Webinars, videos y podcasts

- [Utilizing communication compliance in Microsoft Purview | SC-401 | Episode 11](https://www.youtube.com/watch?v=sRng0zP83BM) · Video · Oficial · Microsoft Learn (YouTube) · mar 2026. Episodio 11 de 15 de la serie oficial SC-401: cómo CC identifica mensajes, revisa elementos marcados, registra notas del revisor y escala casos.

### Laboratorios, GitHub y herramientas

- [Implement retention, eDiscovery, and Communication compliance in Microsoft Purview (exercise module)](https://learn.microsoft.com/en-us/training/modules/purview-exercise-implement-retention-ediscovery-communication-compliance/) · Laboratorio · Oficial · Microsoft Learn. Módulo de ejercicios guiados (1 h 4 min) que incluye crear una política de Communication Compliance junto con retención y una búsqueda de eDiscovery.

**Manos a la obra**

1. `Laboratorio` Completa el módulo de Learn sobre Communication Compliance y su evaluación final; anota tres conceptos nuevos y en qué módulo de esta guía se profundizan ([módulo de Learn](https://learn.microsoft.com/en-us/training/modules/m365-compliance-insider-prepare-communication-compliance/)).
2. `Laboratorio` Haz el módulo de ejercicios guiados de retención, eDiscovery y Communication Compliance en tu tenant de prueba y guarda la política creada como evidencia ([ejercicios guiados](https://learn.microsoft.com/en-us/training/modules/purview-exercise-implement-retention-ediscovery-communication-compliance/)).
3. `Laboratorio` Con la guía APL-5007, marca por cada tarea evaluada el módulo de esta guía que la cubre y agenda el laboratorio de la credencial para cuando termines el nivel inicial ([guía APL-5007](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-5007)).
4. `Laboratorio` Crea un registro mensual de cambios de CC e IB para tu equipo a partir de la página de novedades de Purview y del Message Center, con fecha, cambio, impacto y responsable ([novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

**¿Quieres profundizar?**

- [Implement retention, eDiscovery, and Communication compliance in Microsoft Purview (exercise module)](https://learn.microsoft.com/en-us/training/modules/purview-exercise-implement-retention-ediscovery-communication-compliance/) · Laboratorio
- [Utilizing communication compliance in Microsoft Purview | SC-401 | Episode 11](https://www.youtube.com/watch?v=sRng0zP83BM) · Video

<a id="i1"></a>

## I1 · Communication Compliance hoy: canales, licencias y pago por uso

*L100–L200 · ~3 h · Origen: Ninja oficial de CC · secciones Why y Overview, y licencias de Getting Started*

Communication Compliance (CC) es la solución de Microsoft Purview que detecta, captura y permite revisar mensajes que podrían infringir políticas internas o requisitos regulatorios: acoso, amenazas, discriminación, fuga de información confidencial, conflictos de intereses o conductas financieras indebidas. No bloquea la comunicación: la analiza después de enviada, con clasificadores, condiciones y revisión humana, y separa a quien configura de quien revisa. Solo está disponible en regiones con las dependencias de servicio de Azure compatibles.

Los canales crecieron mucho: Exchange Online, Microsoft Teams (incluidos adjuntos modernos y transcripciones), Viva Engage en modo nativo, Microsoft 365 Copilot y Copilot Chat, otros Copilots (Copilot Studio, Fabric y Security Copilot), apps de IA empresariales, otras apps de IA y fuentes de terceros mediante conectores. Con ellos llegó un segundo modelo de cobro: además de la licencia por usuario (Microsoft 365 E5, Microsoft Purview Suite —antes E5 Compliance—, el complemento E5 Insider Risk Management u Office 365 E5), la IA que no es de Microsoft 365 se factura por **pago por uso**, en registros de texto de 1.000 caracteres.

Microsoft 365 E3 no incluye Communication Compliance; Microsoft 365 Copilot exige su licencia además de E5 o Purview Suite; y Microsoft 365 E7, en GA desde el 1 de mayo de 2026, reúne E5, Copilot, Entra Suite y Agent 365. Este módulo te deja una matriz clara de qué canal requiere qué licencia o medidor y de los límites de cada canal que condicionan el diseño.

**Por qué importa**

Elegir mal el licenciamiento o el canal tiene costo directo: políticas que no capturan lo que el regulador espera, personas supervisadas sin licencia o facturas de pago por uso inesperadas. Una matriz de canales y licencias validada con tu equipo de licenciamiento permite presupuestar, explicar a Legal qué se supervisa y qué no, y evitar puntos ciegos como los canales públicos de Teams con más de 250 usuarios o los canales compartidos.

**Qué vas a lograr**

- Explicar qué hace Communication Compliance y qué no hace (no bloquea mensajes en tiempo real).
- Enumerar los canales compatibles y sus límites operativos: modo nativo, adjuntos, canales públicos y compartidos, transcripciones y fuentes de terceros.
- Distinguir qué incluyen Microsoft 365 E3, E5 y Purview Suite, y cuándo se requiere Copilot, E7, Agent 365 o pago por uso.
- Calcular los registros de texto de pago por uso para un volumen de mensajes dado.

> **Novedad.** Licencias según la descripción de servicio vigente: CC está incluido en Microsoft 365 E5/A5/G5, Microsoft Purview Suite, el complemento Microsoft 365 E5 Insider Risk Management y Office 365 E5, y cada usuario que se beneficia necesita licencia, incluidos quienes tienen roles de Purview. El análisis de prompts y respuestas de Microsoft 365 Copilot solo figura con «E5 + Copilot» o «Purview Suite + Copilot» ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Microsoft 365 E3 no lo incluye.

> **Atención.** Pago por uso: 1 registro de texto equivale a 1.000 caracteres, redondeados hacia arriba (un mensaje de 7.500 caracteres son 8 registros). El medidor premium cubre odio, autolesión, violencia, contenido sexual, Prompt Shields y material protegido, y si un mensaje se evalúa con ambos medidores se cobra solo el premium. Para Microsoft 365 Copilot no hay cargos de pago por uso (página del 6 de enero de 2026, [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)).

> **Atención.** Límites por canal: Viva Engage requiere modo nativo; los canales públicos de Teams se limitan a 250 usuarios con ámbitos estáticos y no se cubren con ámbitos adaptables; hay un máximo de 25 adjuntos por coincidencia; los adjuntos modernos se analizan en chats y canales privados, pero no en canales compartidos; y el contenido de terceros tarda de 24 a 48 horas ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).

> **Qué cambió.** Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama Microsoft Purview Suite, sin cambios de servicio ni de precio ([precios](https://www.microsoft.com/en-us/security/pricing-overview)). Microsoft 365 E7, en GA desde el 1 de mayo de 2026, reúne E5, Microsoft 365 Copilot, Entra Suite y Agent 365 ([anuncio](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295)).

**¿Tienes poco tiempo?**

- [Learn about Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance) · Documentación
- [Detect channel signals with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · Documentación
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación

### Documentación, cursos y credenciales

- [Learn about Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance) · Documentación · Oficial · Microsoft Learn. Introducción oficial: escenarios (políticas corporativas, riesgo, cumplimiento regulatorio como FINRA 3110), áreas clave, separación de funciones e integración con Insider Risk.
- [Microsoft Purview service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Documentación · Oficial · Microsoft Learn (Service Descriptions). Fuente oficial de licenciamiento: Communication Compliance incluido en Microsoft 365 E5/A5/G5, Purview Suite, E5 Insider Risk Management y Office 365 E5; el análisis de prompts de Copilot exige además licencia de Microsoft 365 Copilot.
- [Microsoft Teams and Microsoft Purview Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-teams) · Documentación · Oficial · Microsoft Learn. Integración con Teams: políticas a nivel de usuario o de canal, mensajes reportados por usuarios ('Report inappropriate content') y acciones sobre mensajes inapropiados.
- [Learn about Microsoft Purview billing models](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Documentación · Oficial · Microsoft Learn · 6 ene 2026. Explica licencias por usuario vs pay-as-you-go; Communication Compliance para IA no Microsoft 365 se factura por registros de texto (1.000 caracteres) con medidores estándar y premium.
- [Detect channel signals with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-channels) · Documentación · Oficial · Microsoft Learn · 28 ago 2025. Describe los canales soportados (IA generativa, Teams incluidas transcripciones, Exchange, Viva Engage y fuentes no Microsoft), retención de copias y límites por canal.

**Manos a la obra**

1. `Laboratorio` Construye la matriz de canales de tu organización: por cada canal (Exchange, Teams, Viva Engage, Microsoft 365 Copilot, otras IA y terceros) indica si se usa, la licencia requerida, si genera pago por uso y sus límites; valídala con tu equipo de licenciamiento ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels), [descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
2. `Laboratorio` Calcula los registros de texto de un mes con 10.000 prompts de 1.200 caracteres y 5.000 de 300 caracteres (resultado esperado: 25.000 registros) y documenta qué clasificadores llevarían la política al medidor premium ([modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models)).
3. `Laboratorio` En el tenant de prueba, confirma que Viva Engage está en modo nativo y que las cuentas revisoras tienen buzón de Exchange Online; guarda el resultado como lista de prerrequisitos ([configurar CC](https://learn.microsoft.com/en-us/purview/communication-compliance-configure)).
4. `Laboratorio` Crea un canal público de Teams de prueba y documenta cómo lo cubrirías (ámbito estático, hasta 250 usuarios) y por qué un ámbito adaptable no lo cubre; agrega el hallazgo a la matriz de canales ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).
5. `Laboratorio` Escribe un párrafo para Legal que explique qué hace Communication Compliance, qué no hace (no bloquea mensajes) y en qué regiones está disponible, citando la documentación oficial ([introducción a CC](https://learn.microsoft.com/en-us/purview/communication-compliance)).

<a id="i2"></a>

## I2 · Políticas, plantillas, clasificadores y condiciones

*L200 · ~6 h · Origen: Ninja oficial de CC · Getting Started (políticas) y sección de ajuste de condiciones*

Una política de CC define a quién se supervisa (usuarios o grupos, con exclusiones), en qué canales, con qué condiciones (clasificadores, tipos de información confidencial, diccionarios de palabras clave y operadores AND, OR y NOT), qué porcentaje se revisa y quién revisa. Hay siete plantillas —conflicto de intereses, interacciones de Copilot, contenido inapropiado, imágenes inapropiadas, texto inapropiado, cumplimiento normativo financiero e información confidencial— y una política aparte para los mensajes que las propias personas notifican en Teams. Según la página de políticas, PowerShell no es compatible para administrarlas (hay una contradicción documental) y CC no admite clasificadores entrenables personalizados.

El idioma decide la calidad de la detección en MCSA. Threat, Harassment y Profanity funcionan en 12 idiomas, incluido el español (con un mínimo de 6 palabras), pero Discrimination y los seis clasificadores financieros solo funcionan en inglés, y los clasificadores de seguridad de contenido basados en LLM (Hate, Sexual, Violence y Self-harm) solo evalúan Copilot, Teams y Viva Engage. Por eso un buen diseño combina plantillas con diccionarios en español, tipos de información confidencial y exclusiones, y se valida con la prueba de condiciones antes de exponer mensajes reales a los revisores.

Ten presentes también los límites: cada política guarda hasta 100 GB o 1 millón de mensajes y se desactiva al alcanzarlos; los diccionarios no pueden superar 100 KB comprimidos; el OCR de CC es propio y puede tardar hasta 48 horas; y Policy health (vista previa) te sugiere filtrar envíos masivos y cerrar puntos ciegos de alcance.

**Por qué importa**

La política es donde se juega la proporcionalidad. Una condición mal pensada expone a los revisores a conversaciones irrelevantes y genera fatiga; una demasiado estrecha deja pasar el riesgo que el regulador espera ver. Diseñar con plantillas, idioma y pruebas reduce falsos positivos, protege la privacidad de los empleados y produce alertas que justifican el tiempo de revisión.

**Qué vas a lograr**

- Seleccionar la plantilla adecuada para un riesgo de conducta, regulatorio o de información confidencial.
- Combinar clasificadores, SIT y diccionarios con AND, OR y NOT, y validarlos con la prueba de condiciones.
- Explicar los límites de idioma de cada familia de clasificadores y cómo compensarlos en español.
- Aplicar los límites operativos de almacenamiento por política, OCR, latencia y tamaño de diccionarios.
- Interpretar las recomendaciones de Policy health (vista previa).

> **Novedad.** Definiciones de clasificadores actualizadas el 16 de octubre de 2026: Threat, Harassment y Profanity funcionan en 12 idiomas, incluidos español y portugués (con un mínimo de 6 palabras en español), mientras Discrimination y los clasificadores financieros son solo en inglés ([definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)).

> **Atención.** Límites que cambian el diseño: cada política almacena hasta 100 GB o 1 millón de mensajes, avisa al 80, 90 y 95 % y se desactiva al llegar al límite (copiarla mantiene la cobertura); los diccionarios admiten hasta 100 KB comprimidos, que también es el límite del tenant; PowerShell no es compatible para administrar políticas y no hay clasificadores personalizados ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).

> **Consejo Ninja.** Los clasificadores LLM (Hate, Sexual, Violence y Self-harm) solo evalúan Copilot, Teams y Viva Engage, alertan desde severidad 4, analizan hasta 10.000 caracteres por mensaje y no evalúan adjuntos, OCR ni transcripciones. El OCR de CC es propio (imágenes .jpg, .png, .bmp o .tiff de 100 KB a 4 MB en correo y chats de Teams, hasta 48 horas) y no usa la configuración OCR de Purview ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).

> **Atención.** Contradicciones abiertas: la plantilla de texto inapropiado cita «Targeted harassment», pero las definiciones solo tienen «Harassment»; la página de políticas dice que los clasificadores LLM evalúan mensajes de 3 o más palabras y, más abajo, de 5 o más; y la página de canales (agosto de 2025) mantiene latencias de 24 a 48 horas frente a la hora que indica la de políticas ([canales](https://learn.microsoft.com/en-us/purview/communication-compliance-channels)).

**¿Tienes poco tiempo?**

- [Create and manage Communication Compliance policies](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Documentación
- [Trainable classifier definitions](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Documentación
- [Configuración de condiciones para escenarios clave de cumplimiento de comunicaciones](https://learn.microsoft.com/es-es/purview/communication-compliance-conditions-scenarios) · Documentación

### Documentación, cursos y credenciales

- [Trainable classifier definitions](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 oct 2026. Definiciones e idiomas de los clasificadores preentrenados, incluidos los de conducta (Threat, Harassment, Discrimination, Profanity), regulatorios (Stock manipulation, Money laundering, etc.), GenAI (Prompt Shields, Protected material) e imágenes.
- [Create and manage Communication Compliance policies](https://learn.microsoft.com/en-us/purview/communication-compliance-policies) · Documentación · Oficial · Microsoft Learn. Tabla de plantillas (conflicto de interés, Copilot, contenido inapropiado, imágenes, texto, cumplimiento financiero, información sensible), política de mensajes reportados por usuarios, salud de políticas y configuración.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Purview Communication Compliance: A Practical Guide for Admins](https://blog.apps4.pro/purview-communication-compliance) · Blog · MVP · Nuevo · Narasima Perumal Chandramohan · Apps4.Pro · 30 jun 2026. Guía práctica reciente: qué hace CC, supervisión de Copilot, prerrequisitos, orden de configuración, elección de plantillas y cómo evitar sobrecarga de alertas.

**Manos a la obra**

1. `Laboratorio` Define el nombre antes de crear (los nombres de política no se pueden cambiar) y crea «PRUEBA-CC-TextoInapropiado-v1» desde la plantilla Detect inappropriate text, con OCR, para un grupo de cuentas de prueba; envía mensajes sintéticos (al menos 3 palabras en inglés o 6 en español) y revisa las coincidencias desde la primera hora y hasta 48 horas después, porque las páginas de políticas y de canales dan plazos distintos ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
2. `Laboratorio` Construye un diccionario de palabras clave en español con términos de conducta y financieros locales (los clasificadores financieros son solo en inglés), combínalo con un SIT usando AND, OR y NOT y valida con «Probar condiciones» antes de guardar ([condiciones en español](https://learn.microsoft.com/es-es/purview/communication-compliance-conditions-scenarios)).
3. `Laboratorio` Envía el mismo mensaje sintético de amenaza en español y en inglés, y otro discriminatorio en ambos idiomas; registra qué clasificadores coinciden en cada caso en una tabla de idiomas ([definiciones](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)).
4. `Laboratorio` Crea una política desde la plantilla de información confidencial con un SIT de tu país y revisión del 10 %, y documenta por qué elegiste ese porcentaje y esa población ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
5. `Laboratorio` Crea una política desde la plantilla Detect inappropriate content (clasificadores LLM) para Teams y Viva Engage con cuentas de prueba y verifica que una imagen o una transcripción no generan coincidencia con esos clasificadores ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
6. `Laboratorio` Revisa Policy health (vista previa) en tu política piloto y aplica la recomendación de Filter email blasts si aparece; documenta el antes y el después ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).

**¿Quieres profundizar?**

- [Microsoft Purview Communication Compliance: A Practical Guide for Admins](https://blog.apps4.pro/purview-communication-compliance) · Blog

<a id="i3"></a>

## I3 · Revisión, remediación y flujo de trabajo

*L200 · ~4 h · Origen: Ninja oficial de CC · Getting Started (investigación y remediación)*

Una alerta de CC es el comienzo de un proceso humano. El revisor abre las coincidencias de la política, filtra, mira el mensaje en su vista de origen, de texto, de conversación o traducida, revisa la actividad de la persona y decide: **resolver**, **notificar** con una plantilla de aviso, **etiquetar**, **escalar** a otro revisor, **escalar para investigación** —que crea un caso de eDiscovery (Premium)— o **quitar el mensaje** de Teams. Cada acción queda registrada y forma parte de la evidencia de supervisión.

Desde el 1 de junio de 2025, la conservación de coincidencias de política es configurable (de 1 mes a 7 años, con 1 año por defecto) y las coincidencias más antiguas que el período elegido pueden eliminarse definitivamente, una decisión que conviene tomar con Legal y gestión de registros. Security Copilot ya resume coincidencias de políticas basadas en clasificadores entrenables, y las mejoras de alertas por política (frecuencia y destinatarios) siguen en camino: su vista previa mundial se retrasó a octubre de 2026.

**Por qué importa**

El valor de Communication Compliance lo decide la calidad de la revisión, no la cantidad de alertas. Un flujo definido —quién revisa, en qué plazo, con qué criterio y qué evidencia deja— reduce el tiempo hasta la decisión, evita notificar a personas por falsos positivos y produce el registro que piden la auditoría interna y los reguladores.

**Qué vas a lograr**

- Recorrer el flujo completo de revisión de una alerta y elegir la acción de remediación adecuada.
- Configurar plantillas de aviso y la conservación de coincidencias con criterios documentados.
- Escalar una alerta a investigación y reconocer el caso de eDiscovery (Premium) resultante.
- Usar Security Copilot para resumir coincidencias y documentar el criterio del revisor.

> **Qué cambió.** La conservación de coincidencias de política entró en vigor el 1 de junio de 2025: va de 1 mes a 7 años, con 1 año por defecto, y las coincidencias más antiguas que el período elegido pueden eliminarse definitivamente ([investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate)). Decide el período con Legal y gestión de registros, no por defecto.

> **Novedad.** Security Copilot resume coincidencias de políticas basadas en clasificadores entrenables y admite prompts para profundizar; requiere habilitar la fuente Microsoft Purview en Security Copilot y consume unidades de cómputo según tu licenciamiento ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)).

> **Atención.** Las mejoras de alertas por política (frecuencia y destinatarios de correo) cambiaron varias veces de fecha: la vista previa pública mundial se retrasó a octubre de 2026 y la GA está por anunciarse ([MC920304](https://mc.merill.net/message/MC920304)), mientras RM529852 anunció GA en enero de 2026 solo para GCC, GCC High y DoD ([RM529852](https://mc.merill.net/message/RM529852)).

> **Consejo Ninja.** Límites prácticos: «Escalar para investigación» admite hasta 100 mensajes por caso de eDiscovery (Premium) y las descargas de mensajes tienen límites documentados de 3 MB y 3 GB ([investigar y remediar](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate)). La política de mensajes notificados por usuarios puede tardar hasta 30 días en estar disponible ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).

**¿Tienes poco tiempo?**

- [Investigate and remediate Communication Compliance alerts](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate) · Documentación
- [Get started with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-configure) · Documentación
- [Communication Compliance case study (Contoso) - versión en español](https://learn.microsoft.com/es-es/purview/communication-compliance-case-study) · Documentación

### Documentación, cursos y credenciales

- [Investigate and remediate Communication Compliance alerts](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate) · Documentación · Oficial · Nuevo · Microsoft Learn · 22 jun 2026. Flujo de revisión: páginas de políticas y alertas, filtros, vistas (origen, texto, conversación, traducción, actividad del usuario), resumen con Copilot en Purview y acciones Resolve, Notify, Tag, Escalate, Escalate for investigation y Remove message in Teams.
- [Get started with Communication Compliance](https://learn.microsoft.com/en-us/purview/communication-compliance-configure) · Documentación · Oficial · Microsoft Learn. Guía paso a paso: permisos, auditoría, grupos, modo nativo de Viva Engage, primera política, límites de cumplimiento, plantillas de aviso, seudonimización y prueba de la política.
- [Communication Compliance case study (Contoso) - versión en español](https://learn.microsoft.com/es-es/purview/communication-compliance-case-study) · Documentación · Oficial · ES · Microsoft Learn (español). Caso práctico en español: Contoso planifica, accede, configura una política de texto inapropiado e investiga y corrige alertas.
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn. Experiencias integradas y autónomas de Security Copilot en Purview; en CC resume coincidencias de políticas basadas en clasificadores entrenables y ofrece prompts interactivos para profundizar.

### Laboratorios, GitHub y herramientas

- [Communication Compliance - Microsoft Security Workshop (lab)](https://indra-pr.github.io/msft-security-workshop/purview/data-compliance/communication-compliance/) · Laboratorio · Comunidad · indra-pr · Microsoft Security Workshop (GitHub Pages, indra-pr). Laboratorio comunitario paso a paso (~2,25 h) con cinco escenarios: texto inapropiado, información sensible, conflicto de interés, regulatorio y fuentes de terceros, con generación de datos de prueba.

**Manos a la obra**

1. `Laboratorio` Recorre el flujo completo sobre alertas de cuentas de prueba: resolver, notificar con una plantilla de aviso, etiquetar, escalar a otro revisor, quitar un mensaje de Teams y «Escalar para investigación» hacia un caso de eDiscovery (Premium); guarda una captura de cada paso ([investigar y remediar](https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate)).
2. `Laboratorio` Crea dos plantillas de aviso (recordatorio de política y aviso formal) y somételas a una revisión simulada de RR. HH. y Legal antes de usarlas; documenta la versión aprobada ([configurar CC](https://learn.microsoft.com/en-us/purview/communication-compliance-configure)).
3. `Laboratorio` Configura la conservación de coincidencias de política con un período justificado por escrito (por ejemplo, alineado con tu tabla de retención) y verifica el valor aplicado ([investigar y remediar](https://learn.microsoft.com/es-es/purview/communication-compliance-investigate-remediate)).
4. `Laboratorio` Sigue de punta a punta el caso práctico de Contoso en español y compara sus decisiones de alcance y remediación con las tuyas ([caso Contoso](https://learn.microsoft.com/es-es/purview/communication-compliance-case-study)).
5. `Laboratorio parcial` Habilita los mensajes notificados por usuarios en Teams mediante la política de mensajería y asigna revisores. Limitación: la política puede tardar hasta 30 días en aparecer tras la compra de la licencia, así que en una prueba de un mes quizá no llegues a verla. Práctica segura en producción: cuentas de prueba y comunicación del canal de denuncia a un grupo piloto ([políticas](https://learn.microsoft.com/en-us/purview/communication-compliance-policies)).
6. `Laboratorio parcial` Usa Security Copilot para resumir las coincidencias de una política basada en clasificadores y anota qué agrega al criterio del revisor. Limitación: la capacidad incluida con E5 se calcula sobre licencias pagas, por lo que un trial de 25 licencias no da capacidad útil. Práctica segura en producción: política piloto, revisores autorizados y seguimiento del consumo ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)).

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primera política defendible.** En tu laboratorio, activa la auditoría, asigna roles con separación de funciones y crea una política piloto («PRUEBA-CC-…») desde la plantilla de texto inapropiado, con un diccionario en español validado con «Probar condiciones». Genera mensajes sintéticos en español e inglés, recorre el flujo de revisión completo (resolver, notificar, etiquetar, escalar) y entrega un informe de dos páginas: alcance, condiciones, resultados por idioma, decisiones del revisor con su evidencia, licencias necesarias y lo que cambiarías antes de un piloto real.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Con qué combinación queda incluido el análisis de prompts y respuestas de Microsoft 365 Copilot en Communication Compliance?
   - a) Office 365 E5, sin ninguna licencia adicional de Copilot
   - b) Microsoft 365 E5 o Purview Suite más una licencia de Microsoft 365 Copilot
   - c) Microsoft 365 E3 más el complemento E5 Insider Risk Management
   - d) Cualquier licencia de Microsoft 365 Copilot, aunque el usuario no tenga E5

2. Un mensaje de 7.500 caracteres analizado con pago por uso equivale a:
   - a) 1 registro de texto
   - b) 7 registros de texto
   - c) 8 registros de texto
   - d) 75 registros de texto

3. ¿Qué clasificadores usa la plantilla Detect inappropriate text?
   - a) Hate, Violence, Sexual y Self-harm
   - b) Prompt Shields y Protected material
   - c) Adult y Racy
   - d) Threat, Discrimination y Targeted harassment

4. Para mensajes en español, ¿qué afirmación es correcta?
   - a) Todos los clasificadores admiten español con un mínimo de 3 palabras
   - b) Threat, Harassment y Profanity admiten español (mínimo 6 palabras), pero los financieros son solo en inglés
   - c) Solo los clasificadores financieros admiten español; los de conducta son solo en inglés
   - d) Discrimination y Threat funcionan en 12 idiomas, pero Harassment solo en inglés

5. ¿Qué ocurre cuando una política alcanza 100 GB o 1 millón de mensajes?
   - a) Se desactiva automáticamente; copiar la política mantiene la cobertura
   - b) Elimina las coincidencias más antiguas para liberar espacio
   - c) Sigue capturando y factura el excedente por pago por uso
   - d) Amplía su capacidad a 200 GB si tienes Audit (Premium)

6. ¿Cuándo se retiró el portal de cumplimiento clásico?
   - a) Entre el 14 de noviembre y el 14 de diciembre de 2024
   - b) El 1 de junio de 2025
   - c) El 15 de octubre de 2027
   - d) Sigue disponible en paralelo al portal de Purview

7. Un administrador global sin roles de Communication Compliance intenta abrir las alertas. ¿Qué ocurre?
   - a) Ve todas las alertas por defecto
   - b) Puede revisarlas, pero no remediarlas
   - c) Solo ve las alertas de su unidad administrativa
   - d) No tiene acceso por defecto a las alertas de CC

8. ¿Qué acción de revisión crea un caso de eDiscovery (Premium) a partir de una alerta de CC?
   - a) Resolver
   - b) Etiquetar
   - c) Escalar para investigación
   - d) Notificar

9. ¿Cuál es el período por defecto de conservación de coincidencias de política, vigente desde el 1 de junio de 2025?
   - a) 30 días
   - b) 1 año
   - c) 7 años
   - d) Indefinido

10. ¿Qué requisito tiene el canal Viva Engage en Communication Compliance?
   - a) Una licencia de Copilot
   - b) Pago por uso
   - c) Estar en modo nativo
   - d) Un conector de terceros

11. ¿Qué afirmación sobre los clasificadores LLM de seguridad de contenido (Hate, Sexual, Violence y Self-harm) es correcta?
   - a) Evalúan correo, adjuntos, OCR y transcripciones de Teams
   - b) Generan alerta desde severidad 1 en cualquier canal
   - c) Solo funcionan sobre contenido importado por conectores de terceros
   - d) Solo evalúan Copilot, Teams y Viva Engage y alertan desde severidad 4

12. ¿Qué credencial valida en un laboratorio la implementación de Communication Compliance?
   - a) El examen SC-401, cuyo temario vigente incluye CC e IB
   - b) El examen SC-900 de fundamentos de seguridad, cumplimiento e identidad
   - c) Applied Skills «Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview»
   - d) El Ninja oficial de 2022, que emite una certificación de Microsoft

13. ¿Qué límite aplica a los canales públicos de Teams en Communication Compliance?
   - a) Hasta 250 usuarios con ámbitos estáticos y sin cobertura con ámbitos adaptables
   - b) Hasta 1.000 usuarios con cualquier tipo de ámbito
   - c) Solo se cubren con ámbitos adaptables, sin límite de usuarios
   - d) No se supervisan: CC solo cubre chats y canales privados

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: las decisiones sobre supervisión de comunicaciones, privacidad, avisos a empleados y relaciones laborales corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

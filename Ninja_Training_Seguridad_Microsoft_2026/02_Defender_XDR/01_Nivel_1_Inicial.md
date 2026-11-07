# Nivel 1 · Inicial · Fundamentos

*Microsoft Defender XDR Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

La plataforma, las licencias y los cuatro productos —Office 365, Endpoint, Identity y Entra ID Protection— desde cero, más KQL y tu laboratorio. Terminas con un entorno funcionando y tu primer incidente investigado de punta a punta.

*L100–L200 · 10 módulos · ~54 horas · 55 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos](#p0) · [I0 Cómo aprender](#i0) · [I1 Defender XDR hoy](#i1) · [I2 Licencias, piloto y roles](#i2) · [I3 MDO: fundamentos](#i3) · [I4 MDE: fundamentos](#i4) · [I5 MDI: fundamentos](#i5) · [I6 ID Protection: fundamentos](#i6) · [I7 KQL y búsqueda avanzada](#i7) · [I8 Laboratorios](#i8)

<a id="p0"></a>

## P0 · Prerrequisitos: identidad, endpoint, correo y datos de seguridad

*L100–L200 · ~4 h · Origen: Sin equivalente directo (el Ninja oficial asume estos conocimientos)*

Defender XDR no es un producto aislado: es la capa que correlaciona señales de **correo y colaboración** (Defender for Office 365), **endpoints** (Defender for Endpoint), **identidades** híbridas (Defender for Identity y Microsoft Entra ID Protection) y **aplicaciones en la nube** en un solo flujo de incidentes, búsqueda y respuesta. Para aprovecharlo necesitas fundamentos de cada dominio: cómo fluye el correo en Exchange Online, cómo se autentica un usuario en Microsoft Entra ID y en Active Directory, qué es un proceso, un servicio o una tarea programada en Windows, y cómo se organiza un inquilino de Microsoft 365.

También necesitas un mínimo de lenguaje de datos —tablas, filtros y agregaciones—, porque la búsqueda avanzada usa KQL y casi todo en este programa termina en una consulta. Con un nivel equivalente a SC-900, conceptos básicos de Active Directory y Windows, y curiosidad por leer registros, el resto del recorrido tendrá sentido. Si vienes del programa de Sentinel, ya tienes la mitad del camino.

**Por qué importa**

Los equipos que saltan directo a la consola confunden productos, licencias y permisos, y terminan escalando problemas que son de configuración básica. Nivelar fundamentos reduce el tiempo de incorporación de cada analista nuevo, evita errores de alcance (por ejemplo, confundir Entra ID Protection con Defender for Identity) y crea un vocabulario común entre el SOC, identidad y mensajería.

**Qué vas a lograr**

- Explicar qué protege cada carga de Defender XDR y qué señales aporta al incidente.
- Describir el recorrido de un correo, un inicio de sesión y un proceso sospechoso hasta convertirse en alerta.
- Distinguir Active Directory de Microsoft Entra ID, y Defender for Identity de Entra ID Protection.
- Preparar un inquilino de práctica y una suscripción de Azure con presupuesto.

> **Consejo Ninja.** Antes de abrir el portal, entiende el recorrido completo de un ataque típico: Defender for Office 365 ve el correo y el clic, Defender for Endpoint el proceso en el equipo, Entra ID Protection el inicio de sesión riesgoso y Defender for Cloud Apps la actividad en la nube. La guía de Zero Trust con Sentinel y Defender XDR muestra qué detecta cada producto en cada paso ([Zero Trust con Sentinel y Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement)), y hay una guía introductoria en español ([respuesta a incidentes con XDR e SIEM integrado](https://learn.microsoft.com/es-es/security/zero-trust/siem-xdr-overview)).

> **Atención.** Entra ID Protection no forma parte de Defender XDR: es una capacidad de Microsoft Entra ID P2 que envía sus alertas al portal de Defender. Defender for Identity, en cambio, protege Active Directory local con sensores en los controladores de dominio. La guía oficial de piloto lo aclara y recomienda pilotar en el inquilino de producción ([piloto de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-overview)).

> **Atención.** La prueba comercial de Microsoft 365 E5 dura un mes, trae 25 licencias, pide tarjeta de crédito y se convierte en suscripción pagada si no desactivas la renovación ([probar o comprar Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/commerce/try-or-buy-microsoft-365?view=o365-worldwide)). Anota la fecha de vencimiento el primer día y planifica los ejercicios de cada nivel dentro de esa ventana.

> **Qué cambió.** Varios nombres cambiaron y verás los anteriores en material antiguo: Microsoft Defender Suite es el nombre actual de Microsoft 365 E5 Security ([registro oficial](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-whats-new?view=o365-worldwide)), Defender Vulnerability Management reemplazó a Threat & Vulnerability Management y hoy vive bajo Exposure Management ([DVM](https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities)), y Microsoft Entra ID es el nombre actual de Azure AD (el directorio en la nube de Microsoft).

**¿Tienes poco tiempo?**

- [Zero Trust security with Microsoft Sentinel and Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement) · Documentación
- [How do I pilot and deploy Microsoft Defender?](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-overview) · Documentación
- [Respuesta a incidentes con XDR e SIEM integrado](https://learn.microsoft.com/es-es/security/zero-trust/siem-xdr-overview) · Documentación

**Manos a la obra**

1. `Laboratorio` Crea el inquilino de práctica con la prueba de Microsoft 365 E5 ([probar o comprar](https://learn.microsoft.com/en-us/microsoft-365/commerce/try-or-buy-microsoft-365?view=o365-worldwide)) y, el mismo día, desactiva la renovación automática y registra la fecha de vencimiento. Evidencia: captura de las licencias asignadas y del estado de facturación.
2. `Laboratorio` Activa el crédito mensual de Azure de tu suscripción de Visual Studio Enterprise ([crédito para suscriptores](https://azure.microsoft.com/en-us/pricing/member-offers/credit-for-visual-studio-subscribers/)) y crea un presupuesto con alertas al 50 % y al 80 % ([presupuestos de Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)). Evidencia: captura del presupuesto con sus destinatarios.
3. `Laboratorio` Crea dos cuentas de acceso de emergencia ([cuentas de emergencia](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access)), tres cuentas de administración separadas de tu cuenta diaria y entre cinco y diez usuarios de prueba con nombres que los identifiquen como tales. Evidencia: lista de cuentas con su propósito y las exclusiones previstas en el acceso condicional.
4. `Laboratorio` Dibuja el recorrido de un phishing con robo de credenciales por las cargas de Defender XDR usando la [guía de Zero Trust con Sentinel y Defender XDR](https://learn.microsoft.com/en-us/security/zero-trust/siem-xdr-implement): para cada paso anota el producto que lo detecta y la tabla de búsqueda avanzada donde quedará la evidencia (`EmailEvents`, `UrlClickEvents`, `EntraIdSignInEvents`, `DeviceProcessEvents`, `CloudAppEvents`). Evidencia: diagrama de una página.
5. `Laboratorio` Escribe una tabla comparativa de Active Directory frente a Microsoft Entra ID, y de Defender for Identity frente a Entra ID Protection: qué protegen, dónde se despliegan, qué licencia piden y en qué módulo de esta guía se profundizan ([I5](#i5), [I6](#i6)). Evidencia: tabla revisada por un compañero.

<a id="i0"></a>

## I0 · Cómo aprender Defender XDR y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Ninja oficial de Defender XDR, Fundamentals (comunidad y recursos de aprendizaje)*

Este programa es extenso, pero no está solo. Microsoft mantiene una página oficial para capacitar al personal de seguridad en Defender XDR que reúne el **Ninja oficial** (Fundamentals, Intermediate y Expert, con un knowledge check por nivel), rutas de Microsoft Learn, un entorno de prueba y simulaciones de ataque. Cada producto tiene además su propio Ninja —Endpoint, Office 365, Identity, Vulnerability Management— y el **Virtual Ninja Show** publica episodios a demanda con los equipos de producto.

Si buscas una credencial formal, el examen **SC-200: Microsoft Security Operations Analyst** cubre Defender XDR junto con Sentinel y Security Copilot; sus habilidades medidas se actualizaron el 21 de octubre de 2026. Para el día a día, la Microsoft Security Community, los foros de Tech Community y los repositorios de la comunidad responden más rápido que cualquier curso. Este módulo te ayuda a combinar todo en un plan propio.

**Por qué importa**

Un SOC de alto rendimiento no depende de un curso: depende de un hábito de aprendizaje con fuentes confiables. Saber dónde está la información oficial, cuándo cambia y quién la explica bien reduce el tiempo para resolver un problema, evita decisiones basadas en documentación vieja y le da a cada analista una ruta de certificación medible.

**Qué vas a lograr**

- Identificar las rutas formales (Ninja oficial, Microsoft Learn, SC-200) y sus mecanismos de evaluación.
- Usar los canales oficiales de novedades, comunidad y soporte.
- Armar un plan de estudio personal que combine esta guía con Microsoft Learn.

> **Novedad.** Las habilidades medidas del examen SC-200 se actualizaron el 21 de octubre de 2026: gestionar el entorno de operaciones de seguridad pesa 40–45 %, responder a incidentes 35–40 % y la búsqueda de amenazas 20–25 %. Se aprueba con 700, hay una nueva evaluación de práctica en AI Skills Navigator y las versiones traducidas llegan unas ocho semanas después ([guía de estudio SC-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200)).

> **Atención.** La certificación Security Operations Analyst Associate dura 12 meses y se renueva gratis. El examen supervisado dura 100 minutos según la [página oficial](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/), aunque algunas guías de terceros dicen 120: ante la diferencia, prevalece la página oficial.

> **Consejo Ninja.** El Ninja oficial de Defender XDR tiene tres niveles —Fundamentals, Intermediate y Expert— con un knowledge check por nivel, y no cubre a fondo cada producto: Endpoint, Office 365 e Identity tienen su propio Ninja ([Train your security staff](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff)). Úsalo como complemento: esta guía sigue su orden y agrega Entra ID Protection, la integración con Sentinel, la automatización y el track de excelencia del SOC.

> **Novedad.** El [Virtual Ninja Show](https://adoption.microsoft.com/en-us/ninja-show/) va por su temporada 16 en 2026, con episodios sobre la migración al sensor v3.x de Defender for Identity, el chat de Security Copilot en Defender y los agentes de IA locales. La [playlist de webinars de la comunidad](https://www.youtube.com/playlist?list=PLmAptfqzxVEUEF0pNXGwAX97ci1keplfx) incluye una sesión de Defender XDR en español.

**¿Tienes poco tiempo?**

- [Train your security staff for Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff) · Documentación
- [Study guide for Exam SC-200: Microsoft Security Operations Analyst](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Credencial
- [Microsoft Defender Virtual Ninja Show](https://adoption.microsoft.com/en-us/ninja-show/) · Webinar

### Documentación, cursos y credenciales

- [Study guide for Exam SC-200: Microsoft Security Operations Analyst](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Guía oficial del SC-200 con habilidades medidas al 21-oct-2026: gestionar el entorno de SecOps (40-45%), responder a incidentes (35-40%) y cazar amenazas (20-25%).
- [Microsoft Certified: Security Operations Analyst Associate](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Página de la certificación SC-200 (nivel intermedio, renovación anual gratuita, examen proctored de 100 minutos) con rutas de Learn de Defender XDR, MDE, Security Copilot y Sentinel.
- [Train your security staff for Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Página oficial que reúne el Ninja de Defender XDR (tres niveles con knowledge check), rutas de Learn, entorno de prueba y simulación de ataques para capacitar al SOC.
- [Entrenar al personal de seguridad para Microsoft Defender XDR](https://learn.microsoft.com/es-es/defender-xdr/microsoft-365-defender-train-security-staff) · Documentación · Oficial · Nuevo · ES · Microsoft Learn · 14 ago 2026. Versión en español de la guía de capacitación: Ninja, rutas de aprendizaje, laboratorio de prueba y ataques simulados.

### Webinars, videos y podcasts

- [Microsoft Defender Virtual Ninja Show](https://adoption.microsoft.com/en-us/ninja-show/) · Webinar · Oficial · Heike Ritter (presentadora) · Microsoft Adoption. Show oficial de episodios a demanda sobre Defender (temporada 16 en 2026: seguridad de Teams, agentes de IA locales, Security Copilot en Defender, MDI v3, agentes autónomos).
- [Microsoft Defender XDR (playlist, Microsoft Security Community)](https://www.youtube.com/playlist?list=PLmAptfqzxVEUEF0pNXGwAX97ci1keplfx) · Webinar · Oficial · Microsoft Security Community · YouTube - Microsoft Security Community. Lista de webinars de la comunidad sobre Defender XDR: attack disruption, AIR de MDO, MDVM, licenciamiento y sesiones en español y portugués.

### Laboratorios, GitHub y herramientas

- [Defender Resource Hub](https://github.com/alexverboon/DefenderResourceHub) · GitHub · MVP · Nuevo · Alex Verboon · GitHub (alexverboon) · sep 2026. Colección curada por un MVP de documentación, blogs, videos, podcasts y repositorios sobre Defender, Entra y Sentinel, actualizada en septiembre de 2026.

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio de SC-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) y arma una hoja con cada habilidad medida y el módulo de esta guía que la cubre. Evidencia: hoja con las habilidades sin cobertura marcadas para reforzar con Microsoft Learn.
2. `Laboratorio` Haz la evaluación de práctica de SC-200 que menciona la guía de estudio antes de empezar el nivel intermedio y guarda el puntaje por dominio como línea base. Evidencia: captura del resultado con la fecha.
3. `Laboratorio` Elige tres episodios de la temporada 16 del [Virtual Ninja Show](https://adoption.microsoft.com/en-us/ninja-show/) vinculados a tu rol y regístralos en tu plan con el módulo al que corresponden. Evidencia: plan personal de estudio con fechas, basado en el [plan semanal](00_Programa.md#plan).
4. `Laboratorio` Guarda en favoritos el [Ninja oficial](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/become-a-microsoft-defender-ninja/1789376?wdOrigin=OFFICECOM-WEB.APPBAR) y el [Defender Resource Hub](https://github.com/alexverboon/DefenderResourceHub), y agenda el knowledge check del nivel Fundamentals para cuando termines el nivel inicial de esta guía. Evidencia: evento en el calendario.

**¿Quieres profundizar?**

- [Defender Resource Hub](https://github.com/alexverboon/DefenderResourceHub) · GitHub
- [Microsoft Defender XDR (playlist, Microsoft Security Community)](https://www.youtube.com/playlist?list=PLmAptfqzxVEUEF0pNXGwAX97ci1keplfx) · Webinar

<a id="i1"></a>

## I1 · Defender XDR hoy: la plataforma unificada

*L100–L200 · ~4 h · Origen: Ninja oficial de Defender XDR, Fundamentals (visión general y primeros pasos)*

Microsoft Defender XDR —que muchos todavía conocen como Microsoft 365 Defender (su nombre anterior)— correlaciona automáticamente las señales de endpoints, identidades, correo, colaboración y aplicaciones en la nube para convertir cientos de alertas en pocos incidentes con su historia de ataque completa, y responder desde un solo lugar: el **portal de Defender**. Allí conviven la cola de incidentes y los casos, la búsqueda avanzada, el Action center, la interrupción automática de ataques, Exposure Management, la inteligencia de amenazas y Security Copilot.

2026 cambió el mapa. Microsoft Sentinel opera dentro del mismo portal (el portal de Azure deja de tener soporte para Sentinel el 31 de marzo de 2027), los **incident cases** reemplazan progresivamente a la cola clásica y, desde el 23 de septiembre de 2026, el **Integrated Security Operations Center (ISOC)**, en vista previa, ofrece capacidades SIEM a clientes de Defender Suite, Microsoft 365 E5 o E7 que todavía no tienen un workspace de Sentinel. Este módulo te da la foto completa antes de entrar producto por producto.

**Por qué importa**

Entender la plataforma como un sistema —no como cinco consolas— es lo que permite reducir el tiempo de respuesta: un incidente correlacionado evita que tres analistas investiguen la misma intrusión por separado, y la interrupción automática contiene en minutos lo que antes tomaba horas. También es la base para decidir con datos cuándo hace falta un SIEM completo y cuándo alcanza con ISOC.

**Qué vas a lograr**

- Describir los componentes del portal de Defender y qué aporta cada carga al incidente unificado.
- Explicar qué es ISOC, quién puede usarlo y qué funciones requieren un workspace.
- Ubicar las novedades de 2026 (casos de incidente, agentes, reglas de ajuste) en el flujo del SOC.
- Leer las novedades mensuales de Defender XDR y decidir qué afecta a tu operación.

> **Novedad.** Desde el 23 de septiembre de 2026, **ISOC** (Integrated Security Operations Center) está en vista previa para clientes de Defender Suite, Microsoft 365 E5 o E7 sin un workspace de Sentinel activo. Casos, workbooks y playbooks en lenguaje natural funcionan sin workspace; UEBA, Content hub, CI/CD, inteligencia de amenazas e ingesta de terceros requieren un workspace de ISOC y una suscripción de Azure ([ISOC](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview)).

> **Atención.** Costos de ISOC: los datos de Defender no pagan ingesta y su retención de 30 días sube a 90 el 15 de noviembre de 2026; la ingesta adicional cuesta 2,40 USD por GB desde el 1 de octubre de 2026 ([anuncio de ISOC](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/integrated-security-operations-center-in-microsoft-defender/4559097)). Nunca desconectes un Sentinel productivo para calificar a la vista previa.

> **Novedad.** Noticias mensuales de 2026: en enero destacaron el Security Alert Triage Agent y el Threat Intelligence Briefing Agent en GA, y el Dynamic Threat Detection Agent y el Threat Hunting Agent en vista previa; en mayo, las reglas integradas de ajuste de alertas pasaron a GA (no afectan a AIR), la pestaña Activities del incidente empezó a mostrar el estado de la interrupción automática y del predictive shielding (vista previa) y Defender Experts ganó su propia entrada en el menú ([etiqueta ninja training](https://techcommunity.microsoft.com/tag/ninja%20training)).

> **Consejo Ninja.** Para entender hacia dónde va la plataforma, lee la visión del SOC para la era agéntica publicada junto con ISOC el 23 de septiembre de 2026: señales, contexto y actuadores en un solo sistema, con la interrupción automática como ejemplo del bucle de protección ([Reimagining the SOC](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/)). La retomas en [S6](04_Nivel_4_Excelencia_del_SOC.md#s6).

**¿Tienes poco tiempo?**

- [Integrated Security Operations Center (ISOC) in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview) · Documentación
- [Integrated Security Operations Center in Microsoft Defender](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/integrated-security-operations-center-in-microsoft-defender/4559097) · Blog oficial
- [Microsoft Defender XDR (playlist, Microsoft Security)](https://www.youtube.com/playlist?list=PL3ZTgFEc7Lyt1O81TZol31YXve4e6lyQu) · Video

### Documentación, cursos y credenciales

- [Integrated Security Operations Center (ISOC) in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 23 sep 2026. ISOC integra XDR, SIEM, inteligencia, automatización e IA en el portal Defender para clientes Defender Suite, M365 E5 o E7 sin workspace activo de Sentinel, con casos, workbooks y playbooks en lenguaje natural sin workspace. *Nota:* Requiere workspace ISOC (y suscripción Azure) para UEBA, Content hub, CI/CD, TI e ingesta de terceros; no desconectar Sentinel productivo para calificar

### Anuncios y blogs oficiales

- [Reimagining the SOC for the agentic era in Microsoft Defender](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/) · Blog oficial · Empleado de Microsoft · Nuevo · Rob Lefferts · Microsoft Security Blog · 23 sep 2026. Visión de Microsoft del SOC agéntico: ISOC como base de señales, contexto y actuadores, con el bucle de protección integrado ejemplificado por attack disruption.
- [Integrated Security Operations Center in Microsoft Defender](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/integrated-security-operations-center-in-microsoft-defender/4559097) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Tomer Brand · Microsoft Tech Community (Microsoft Defender XDR Blog) · 23 sep 2026. Anuncio técnico de la preview pública de ISOC: datos de Defender sin cargo de ingesta, retención de 30 días que pasa a 90 días el 15-nov-2026 y conectores adicionales a 2,40 USD/GB desde el 1-oct-2026. *Nota:* Fuentes incluidas: MDE, MDO, MDI, MDCA, Defender for Cloud, logs de Entra ID Protection y actividad de Azure/Office 365 vía conector
- [What's new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Resumen mensual oficial con el resumen de detonación de correo generado por Security Copilot, control de agentes de IA locales y novedades de Purview/Entra.
- [What's new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 30 jul 2026. Resumen mensual oficial: Project Perception (agentes rojo/azul/verde), protección contra prompt injection en correo (preview), convergencia de Defender Threat Intelligence y nuevos servicios Defender Experts (Threat Intelligence y MDR).

### Webinars, videos y podcasts

- [Microsoft Defender XDR (playlist, Microsoft Security)](https://www.youtube.com/playlist?list=PL3ZTgFEc7Lyt1O81TZol31YXve4e6lyQu) · Video · Oficial · Microsoft Security · YouTube - Microsoft Security. Lista oficial de videos cortos (65) sobre Defender: onboarding de MDE, KQL, Security Analyst Agent, Security Alert Triage Agent, predictive shielding y herramienta de despliegue.

### Comunidad: blogs, libros, newsletters y eventos

- [Defending with Microsoft: A Deep Dive into the Microsoft Defender Suite - Blog series intro](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/) · Blog · MVP · Jeffrey Appel · jeffreyappel.nl · 23 mar 2026. Introducción a una serie que recorre la historia y configuración de toda la suite Defender (MDE, MDI, MDO, MDCA, XDR, attack disruption y Exposure Management).
- [Microsoft Defender XDR vanaf Q2 2026, wat er echt verandert voor je SOC](https://www.itcowboys.nl/microsoft-defender-xdr-vanaf-q2-2026-wat-er-echt-verandert-voor-je-soc/) · Blog · Comunidad · Nuevo · Jordy Herber · ITCowboys.nl · 8 oct 2026. Tabla comentada de cambios de Defender XDR desde abril de 2026 (alert tuning GA, aislamiento automático, DisruptionAndResponseEvents GA, AgentsInfo, ISOC) y su impacto en el SOC.
- [Defender XDR (categoría) - Cloudbrothers](https://www.cloudbrothers.info/en/categories/defender-xdr/) · Blog · MVP · Fabian Bader · Cloudbrothers · 7 abr 2026. Investigaciones de un MVP sobre Defender XDR: XDRInternals, bypasses de acceso condicional vía cookie del portal Defender y guía de exclusiones de MDE.

**Manos a la obra**

1. `Laboratorio` En tu inquilino de prueba, arma un mapa del portal de Defender: para Defender for Office 365, Endpoint, Identity, Entra ID Protection y Cloud Apps anota la sección del portal donde se configura, el tipo de alertas que produce y dos tablas de búsqueda avanzada que alimenta. Evidencia: mapa de una página que reutilizarás en [M1](02_Nivel_2_Intermedio.md#m1).
2. `Laboratorio` Lee las [novedades de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/whats-new) de los últimos tres meses y clasifica cada cambio como «afecta la operación», «afecta licencias» o «informativo», con un dueño para los dos primeros. Evidencia: tabla de al menos diez cambios.
3. `Laboratorio` Con la [página de ISOC](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview), construye una tabla de dos columnas: funciones disponibles sin workspace y funciones que exigen un workspace de ISOC con suscripción de Azure. Evidencia: tabla y una recomendación de tres líneas para tu organización.
4. `Solo producción` Evalúa ISOC (casos, workbooks y playbooks en lenguaje natural). Requiere Defender Suite, E5 o E7 y no tener un workspace de Sentinel activo, por lo que no se reproduce en un laboratorio que ya usa Sentinel. Cómo hacerlo seguro: usa un inquilino secundario elegible, nunca desconectes el Sentinel productivo para calificar y no conectes ingesta de terceros, para evitar el cargo de 2,40 USD por GB.
5. `Laboratorio` Elige dos videos sobre incidentes y búsqueda avanzada de la [playlist de Microsoft Defender XDR](https://www.youtube.com/playlist?list=PL3ZTgFEc7Lyt1O81TZol31YXve4e6lyQu) y resume en cinco viñetas qué cambia respecto de tu herramienta actual. Evidencia: resumen compartido con el equipo.

**¿Quieres profundizar?**

- [Defending with Microsoft: A Deep Dive into the Microsoft Defender Suite - Blog series intro](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/) · Blog

<a id="i2"></a>

## I2 · Evaluación, piloto, licencias y roles

*L100–L200 · ~6 h · Origen: Ninja oficial de Defender XDR, Fundamentals (primeros pasos) y guía oficial de piloto y despliegue*

Antes de operar hay que saber qué tienes. Defender XDR se licencia por carga de trabajo y por suite: **Microsoft 365 E5** incluye Defender for Office 365 Plan 2, Defender for Endpoint Plan 2, Defender for Identity, Defender for Cloud Apps y Entra ID P2; **Microsoft Defender Suite** (antes Microsoft 365 E5 Security) suma esas capacidades a un E3; y **Microsoft 365 E7**, disponible desde el 1 de mayo de 2026, agrega Microsoft 365 Copilot, Agent 365 y Entra Suite sobre E5. Desde el 1 de julio de 2026, además, Office 365 E3 y Microsoft 365 E3 incluyen Defender for Office 365 Plan 1.

Con las licencias claras, el segundo paso es el **piloto**. Microsoft recomienda pilotar en el inquilino de producción, con un orden definido y criterios de salida, y gobernar el acceso con el **RBAC unificado** (URBAC) del portal, que ya es el modelo predeterminado para inquilinos nuevos de Endpoint e Identity desde 2025 y para nuevas organizaciones de Office 365 Plan 2 desde julio de 2026. Este módulo te enseña a leer la matriz de licencias sin sorpresas, a planificar el piloto y a diseñar roles de mínimo privilegio.

**Por qué importa**

La mitad de las preguntas difíciles de un SOC son de licencias o permisos: por qué un analista no ve Threat Explorer, por qué la interrupción automática no actuó, por qué un agente no tiene SCU. Una matriz de licencias validada y un modelo de roles de mínimo privilegio evitan brechas de cobertura, gastos duplicados y accesos excesivos que ningún auditor aceptaría.

**Qué vas a lograr**

- Leer la matriz de licencias de Defender XDR y explicar qué cubren E3, E5, Defender Suite y E7.
- Planificar un piloto con orden de despliegue, grupos y criterios de salida.
- Activar el RBAC unificado y diseñar roles de mínimo privilegio para el SOC.
- Identificar qué capacidades se pagan aparte: complementos, consumo o servicios.

> **Qué cambió.** **Microsoft Defender Suite** es el nombre actual de Microsoft 365 E5 Security: el registro oficial lo muestra como complemento de Business Premium desde marzo de 2025 y como Defender Suite for Business Premium desde septiembre de 2025 ([novedades de seguridad para empresas](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-whats-new?view=o365-worldwide)). **Microsoft 365 E7** (GA el 1 de mayo de 2026, 99 USD por usuario al mes) suma a E5 Microsoft 365 Copilot, Agent 365 y Entra Suite ([E7](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7)).

> **Novedad.** Desde el 1 de julio de 2026, Defender for Office 365 **Plan 1** está incluido en Office 365 E3 y Microsoft 365 E3. El Plan 2 (Threat Explorer, AIR, Attack simulation training e integración con Defender XDR) sigue en E5, A5, G5 o Defender Suite, y Safe Documents solo viene con Microsoft 365 E5 o Defender Suite ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description)).

> **Atención.** El RBAC unificado es el modelo predeterminado para inquilinos nuevos de MDE y MDI desde 2025 y para organizaciones nuevas de MDO P2 desde julio de 2026 (MC1246006). Activarlo exige al menos Security Administrator y no admite GDAP ni entidades de servicio para Sentinel ([activar URBAC](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac)). Diseña los roles antes de abrir el portal a todo el equipo.

> **Novedad.** Security Copilot está incluido en Microsoft 365 E5: 400 SCU al mes por cada 1.000 licencias, hasta 10.000 ([Security Copilot en E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5)), con un despliegue por fases entre el 20 de abril y el 30 de junio de 2026. El data lake de Sentinel, Logic Apps, los agentes de terceros y Data Security Investigations no agéntico de Purview se pagan aparte ([MC1261596](https://mc.merill.net/message/MC1261596)).

**¿Tienes poco tiempo?**

- [Activate Microsoft Defender unified role-based access control (URBAC)](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac) · Documentación
- [Microsoft Defender for Office 365 service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description) · Documentación
- [How do I pilot and deploy Microsoft Defender?](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-overview) · Documentación
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Defender for Office 365 service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description) · Documentación · Oficial · Nuevo · Microsoft Learn (Service Descriptions) · jul 2026. Descripción de servicio con la matriz Plan 1 vs Plan 2: desde el 1-jul-2026 MDO P1 se incluye en Office 365 E3 y Microsoft 365 E3, mientras P2 (Explorer, AIR, AST, integración XDR) sigue en E5/A5/G5 o Defender Suite.
- [Activate Microsoft Defender unified role-based access control (URBAC)](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac) · Documentación · Oficial · Microsoft Learn. Pasos para activar el RBAC unificado por carga de trabajo (MDE, MDI, MDO, DVM, Exposure Management, Sentinel) y sus limitaciones antes de la activación.
- [How do I pilot and deploy Microsoft Defender?](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-overview) · Documentación · Oficial · Microsoft Learn. Serie oficial para pilotar en el tenant de producción y desplegar MDI, MDO, MDE, MDCA e investigar/responder con Defender XDR, con arquitectura y orden recomendado.
- [What's new in security in Microsoft 365 for business (Defender Suite)](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-whats-new?view=o365-worldwide) · Documentación · Oficial · Microsoft Learn · 24 sep 2025. Registro oficial del cambio de nombre: Microsoft Defender Suite (antes Microsoft 365 E5 Security) como add-on para Business Premium desde marzo-2025 y Defender Suite for Business Premium desde septiembre-2025.
- [Microsoft Defender for Office 365 Features service description](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-defender-for-office-365-features) · Documentación · Oficial · Nuevo · Microsoft Learn (Service Descriptions) · jul 2026. Describe cada capacidad de MDO (Safe Attachments, Safe Links, Safe Documents, protección SPO/ODB/Teams, Explorer) y aclara que E3 recibe solo P1 desde julio de 2026.
- [Microsoft 365 E7 for Enterprise](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7) · Documentación · Oficial · Nuevo · Microsoft 365 · may 2026. Página oficial de Microsoft 365 E7 (99 USD/usuario/mes), que incluye M365 E5, Microsoft 365 Copilot, Agent 365 y Entra Suite.

### Anuncios y blogs oficiales

- [Introducing new security and compliance add-ons for Microsoft 365 Business Premium](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-new-security-and-compliance-add-ons-for-microsoft-365-business-premi/4449297) · Blog oficial · Empleado de Microsoft · Nora Zhang · Microsoft Tech Community (Microsoft Security Community Blog) · 3 sep 2025. Anuncio de Defender Suite for Business Premium (10 USD/usuario/mes) con Entra ID P2, MDI, MDE P2, MDO P2 y MDCA para pymes de hasta 300 usuarios.
- [Secure agentic AI for your Frontier Transformation](https://www.microsoft.com/en-us/security/blog/2026/03/09/secure-agentic-ai-for-your-frontier-transformation/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 9 mar 2026. Anuncio de Agent 365 y Microsoft 365 E7 (GA 1-may-2026) con señales de riesgo de agentes en Defender, Entra y Purview.

**Manos a la obra**

1. `Laboratorio` Completa la tabla [Licencias](00_Programa.md#licencias) para tu organización: marca qué capacidades ya tienes, cuáles requieren complemento o consumo y cuáles no aplican, con la fuente de cada fila. Evidencia: matriz revisada por tu responsable de licenciamiento.
2. `Laboratorio` Activa el RBAC unificado para Defender for Endpoint y Defender for Office 365 en el inquilino de prueba ([activar URBAC](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac)) y crea un rol de analista N1 de mínimo privilegio. Comprueba con una cuenta de prueba que puede ver incidentes pero no ejecutar acciones de respuesta. Evidencia: captura del rol y del intento de acción denegado.
3. `Laboratorio` Configura el alcance de datos ([scoping](https://learn.microsoft.com/en-us/defender-xdr/scoping)) para que un analista regional solo vea los dispositivos de un grupo, como en una operación con varios países. Evidencia: captura de la vista filtrada con la cuenta de prueba.
4. `Laboratorio` Escribe el plan de piloto con la [guía oficial](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-overview) y el [orden de despliegue recomendado](https://learn.microsoft.com/en-au/unified-secops/overview-deploy) para operaciones unificadas (Defender for Identity, Office 365, Endpoint, gestión de vulnerabilidades y Cloud Apps; luego Entra ID Protection, Defender for Cloud, Security Copilot, el workspace de Sentinel y RBAC): grupos piloto, criterios de salida y responsables. Evidencia: plan de una página.
5. `Laboratorio` Calcula las SCU incluidas para tu número de licencias pagas de E5 (por ejemplo, 4.000 licencias equivalen a 1.600 SCU al mes) y compáralas con el consumo que esperas de los agentes que planeas usar en [A6](03_Nivel_3_Avanzado.md#a6). Evidencia: hoja de cálculo con supuestos.
6. `Solo producción` Verifica en producción la capacidad de Security Copilot asignada por la inclusión de E5 y su consumo ([uso de SCU](https://learn.microsoft.com/en-us/copilot/security/manage-usage)). La inclusión solo cuenta licencias pagas, así que no aparece en la prueba. Cómo hacerlo seguro: usa un rol de solo lectura, no cambies la capacidad ni el excedente y comparte el resultado con el dueño del presupuesto.

<a id="i3"></a>

## I3 · Defender for Office 365: fundamentos

*L100–L200 · ~6 h · Origen: Ninja oficial de Defender for Office 365 (fundamentos y configuración)*

El correo sigue siendo la puerta de entrada favorita: phishing, malware, compromiso de correo empresarial (BEC) y, cada vez más, códigos QR y enlaces en Teams. **Defender for Office 365** protege Exchange Online, Teams, SharePoint y OneDrive con Safe Links, Safe Attachments, anti-phishing con protección contra suplantación y detonación en sandbox; en el Plan 2 suma investigación y respuesta automatizadas, Threat Explorer y simulación de ataques.

La configuración inicial decide buena parte del resultado. Microsoft propone un plan de ocho pasos que empieza por la autenticación del correo (SPF, DKIM y DMARC), sigue con las **políticas preestablecidas** Standard y Strict, los permisos, las cuentas prioritarias, los reportes de usuario y la lista de permitidos y bloqueados, y termina en simulaciones e investigación. En 2026 llegaron, además, la protección contra inyección de instrucciones en correo, nuevos reportes de Teams y la tabla `CallActivityEvents`.

**Por qué importa**

Cada mensaje malicioso que llega al buzón cuesta tiempo de analista y riesgo de credenciales robadas. Aplicar las políticas recomendadas por Microsoft en lugar de configuraciones artesanales reduce la deriva de configuración, mejora la detección sin ajustes manuales y le deja al SOC una línea base medible con el Configuration analyzer.

**Qué vas a lograr**

- Configurar SPF, DKIM y DMARC y explicar por qué van antes que las políticas.
- Asignar las políticas preestablecidas Standard y Strict y validarlas con el Configuration analyzer.
- Distinguir las capacidades del Plan 1 y del Plan 2.
- Habilitar los reportes de usuario como fuente de señales para el SOC.

> **Consejo Ninja.** La guía de inicio de Defender for Office 365 propone ocho pasos en orden: SPF, DKIM y DMARC; políticas; permisos; cuentas prioritarias; reportes de usuario; Tenant Allow/Block List; Attack simulation training, e investigación ([guía de inicio](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide)). Corrige la autenticación antes de ajustar políticas y usa el Configuration analyzer y ORCA para encontrar desvíos ([configuración recomendada](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365)).

> **Consejo Ninja.** Las políticas preestablecidas **Standard** y **Strict** aplican la configuración recomendada por Microsoft y se actualizan solas; **Built-in protection** da Safe Links y Safe Attachments básicos a quien no esté en otra política ([políticas preestablecidas](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies)). Empieza por ellas y personaliza solo con una razón documentada.

> **Novedad.** Novedades recientes de Defender for Office 365: en octubre de 2026, la tabla `CallActivityEvents`, el campo `ApproverUpn` y el informe de reuniones de Teams; en septiembre, la configuración de reportes de Teams separada (MC1478463); en julio, la protección contra prompt injection en el correo ([novedades de MDO](https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new)).

> **Atención.** DMARC necesita un dominio propio con DNS administrable: el dominio onmicrosoft.com no sirve para publicar tu propio DMARC. En producción, empieza con `p=none` y reportes `rua`, y sube de forma gradual a `quarantine` y luego a `reject` ([guía de inicio](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide)).

**¿Tienes poco tiempo?**

- [Get started with Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide) · Documentación
- [Preset security policies in cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies) · Documentación
- [Set up steps for the Standard or Strict preset security policies in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies) · Laboratorio

### Documentación, cursos y credenciales

- [What's new in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · oct 2026. Novedades mensuales de MDO: tabla CallActivityEvents y reportes de reuniones de Teams (oct-2026), ajustes separados de reporte de Teams (sep-2026), MDO P1 en E3, URBAC por defecto y protección contra prompt injection (jul-2026).
- [Preset security policies in cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies) · Documentación · Oficial · Microsoft Learn. Explica las políticas preestablecidas Standard, Strict y Built-in protection, su precedencia y cómo asignarlas a usuarios para aplicar la configuración recomendada por Microsoft.
- [Recommended email and collaboration threat policy settings for cloud organizations](https://learn.microsoft.com/en-us/defender-office-365/recommended-settings-for-eop-and-office365) · Documentación · Oficial · Microsoft Learn. Tablas de valores por defecto, Standard y Strict para anti-malware, anti-spam, anti-phishing, Safe Attachments y Safe Links, con la recomendación de corregir SPF/DKIM/DMARC antes de ajustar.
- [Get started with Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide) · Documentación · Oficial · Microsoft Learn. Plan de 8 pasos para nuevas organizaciones: SPF/DKIM/DMARC, políticas de amenazas, permisos, cuentas prioritarias, reportes de usuario, Tenant Allow/Block List, simulaciones e investigación.

### Laboratorios, GitHub y herramientas

- [Set up steps for the Standard or Strict preset security policies in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies) · Laboratorio · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Guía paso a paso (5 minutos) para asignar usuarios a Standard o Strict y luego validar con Configuration analyzer.

**Manos a la obra**

1. `Laboratorio` Asigna la política preestablecida Strict a un grupo de cuentas prioritarias de prueba y Standard al resto, siguiendo la [guía paso a paso](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies), y valida con el Configuration analyzer. Evidencia: informe sin desvíos para ambos grupos.
2. `Laboratorio parcial` Configura SPF, DKIM y DMARC con `p=none` y reportes `rua`, y luego pasa a `quarantine` ([guía de inicio](https://learn.microsoft.com/en-us/defender-office-365/mdo-deployment-guide)). Limitación: necesitas un dominio propio con DNS administrable; onmicrosoft.com no sirve. En producción, sube la política por etapas y revisa los reportes de cada fase antes de avanzar. Evidencia: registros DNS publicados y primer reporte agregado.
3. `Laboratorio` Marca como cuentas prioritarias a dos usuarios de prueba y configura los reportes de usuario para que lleguen a un buzón de reportes y a Microsoft; envía un reporte de prueba desde Outlook. Evidencia: el reporte visible en el portal de Defender.
4. `Laboratorio` Crea en la Tenant Allow/Block List una entrada de bloqueo con vencimiento para una URL de prueba y verifica que un mensaje de prueba con esa URL queda bloqueado. Evidencia: captura de la entrada y del mensaje o clic bloqueado.
5. `Laboratorio` Con la [descripción de funciones de MDO](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-defender-for-office-365-features), arma una tabla de qué ejercicios de [I3](#i3) y [M2](02_Nivel_2_Intermedio.md#m2) requieren Plan 2. Evidencia: tabla que usarás para justificar licencias.

<a id="i4"></a>

## I4 · Defender for Endpoint: fundamentos

*L100–L200 · ~6 h · Origen: Ninja oficial de Defender for Endpoint, rol SecAdmin (Fundamentals)*

**Defender for Endpoint** es la plataforma de protección y respuesta de endpoints: antivirus de nueva generación, reducción de superficie de ataque, detección y respuesta (EDR), gestión de vulnerabilidades y acciones de respuesta como aislar un equipo o recolectar un paquete de investigación. Cubre Windows, macOS, Linux, Android e iOS, y en servidores se licencia, de forma recomendada, con **Defender for Servers Plan 2** de Defender for Cloud.

Desplegarlo bien es un proyecto, no un clic: se incorpora por **anillos** (evaluación con unas 50 máquinas, piloto de 50 a 100 y despliegue total) con criterios de salida, se elige la conectividad simplificada o estándar y se usa la herramienta adecuada (Intune, Configuration Manager, GPO o scripts). En 2026 llegaron el descubrimiento de agentes de IA locales, el modo auditoría del antivirus en Linux y el soporte de escritorios Linux en vista previa.

**Por qué importa**

Sin cobertura completa de endpoints, la interrupción automática no puede aislar el equipo comprometido y el SOC investiga a ciegas. Un despliegue por anillos con criterios de salida reduce incidentes operativos, y una cobertura medida —equipos incorporados, con el antivirus en modo activo y saludables— es la métrica de base que cualquier comité de riesgos entiende.

**Qué vas a lograr**

- Planificar la incorporación por anillos con criterios de salida.
- Elegir el método de incorporación y la conectividad adecuados.
- Incorporar servidores con Defender for Servers Plan 2 y explicar por qué.
- Validar la incorporación con la prueba de detección y el estado del sensor.

> **Consejo Ninja.** Incorpora por anillos y con criterios de salida: evaluación (unos 50 equipos), piloto (50 a 100) y despliegue total, con conectividad Streamlined o Standard según tu red ([incorporación](https://learn.microsoft.com/en-us/defender-endpoint/onboarding)). Para el laboratorio, el script local admite hasta 10 dispositivos ([script local](https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-script)).

> **Atención.** Servidores: Microsoft recomienda Defender for Servers Plan 2, con incorporación automática, gestión de vulnerabilidades premium y 500 MB diarios de ingesta incluidos; las licencias independientes de MDE P1 y P2 no cubren servidores ([incorporar servidores](https://learn.microsoft.com/en-us/defender-endpoint/onboard-server)).

> **Novedad.** Octubre de 2026: descubrimiento de agentes de IA locales en GA (Windows con la plataforma 4.18.26090.9 y macOS 101.26072.0017), modo auditoría del antivirus en Linux en GA y evaluación de apps de Microsoft Store en GA. Septiembre: escritorios Linux en vista previa, plugin de contenedores WSL en GA y recomendaciones de AI-Readiness en Secure Score en GA ([novedades de MDE](https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint)).

**¿Tienes poco tiempo?**

- [Onboard devices to Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/onboarding) · Documentación
- [Onboard servers to Microsoft Defender](https://learn.microsoft.com/en-us/defender-endpoint/onboard-server) · Documentación
- [New features in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint) · Documentación

### Documentación, cursos y credenciales

- [New features in Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/whats-new-in-microsoft-defender-endpoint) · Documentación · Oficial · Nuevo · Microsoft Learn · nov 2026. Novedades de MDE de los últimos seis meses: descubrimiento de agentes de IA locales (GA oct-2026), modo auditoría AV en Linux (GA), soporte de escritorios Linux (preview sep-2026), recomendaciones AI-Readiness de Secure Score y WSL containers.
- [Onboard devices to Microsoft Defender for Endpoint](https://learn.microsoft.com/en-us/defender-endpoint/onboarding) · Documentación · Oficial · Microsoft Learn. Proceso de incorporación por herramientas (Intune, ConfigMgr, GPO, scripts) con conectividad Streamlined/Standard y despliegue por anillos (evaluación, piloto, total) con criterios de salida.
- [Onboard servers to Microsoft Defender](https://learn.microsoft.com/en-us/defender-endpoint/onboard-server) · Documentación · Oficial · Microsoft Learn. Opciones de licencia y despliegue para servidores, recomendando Defender for Servers Plan 2 (Defender for Cloud) con onboarding automático, DVM premium y 500 MB/día de ingesta incluida.
- [Migrate to Microsoft Defender for Endpoint - Phase 3: Onboard](https://learn.microsoft.com/en-us/defender-endpoint/switch-to-mde-phase-3) · Documentación · Oficial · Microsoft Learn. Fase final de migración desde un EDR/AV de terceros: incorporar, probar detección, confirmar modo pasivo, actualizar Defender AV y desinstalar la solución anterior.

### Comunidad: blogs, libros, newsletters y eventos

- [Jeffrey Appel - Microsoft Security blog](https://jeffreyappel.nl/) · Blog · MVP · Nuevo · Jeffrey Appel · jeffreyappel.nl · 26 oct 2026. Blog de un MVP con series profundas de MDE y Defender: aislamiento automático por attack disruption (sep-2026), custom data collection rules, live response y Defender Monthly News comentado.
- [Simplified onboarding of Microsoft Defender for Endpoint using the Defender deployment tool](https://jeffreyappel.nl/simplified-onboarding-of-microsoft-defender-for-endpoint-using-the-defender-deployment-package/) · Blog · MVP · Nuevo · Jeffrey Appel · jeffreyappel.nl · 11 may 2026. Paso a paso de la nueva herramienta de despliegue de Defender (paquete .exe con onboarding, prerrequisitos, VDI, claves y caducidad del paquete).

**Manos a la obra**

1. `Laboratorio` Crea dos VM con Windows 11 Enterprise a partir de las [imágenes de cliente](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/client-images) disponibles con tu suscripción de Visual Studio, con apagado automático ([auto-shutdown](https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm)). Evidencia: VM con etiquetas `env=lab` y apagado programado.
2. `Laboratorio` Incorpora una VM con Intune y la otra con el [script local](https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-script), y ejecuta la [prueba de detección](https://learn.microsoft.com/en-us/defender-endpoint/run-detection-test) en ambas. Evidencia: los dos equipos activos en el inventario y la alerta de la prueba en el portal.
3. `Laboratorio` Redacta los criterios de salida del anillo 1 (salud del sensor, modo del antivirus, protección contra alteraciones, conectividad e impacto en aplicaciones) según la [guía de incorporación](https://learn.microsoft.com/en-us/defender-endpoint/onboarding) y verifícalos con una consulta a `DeviceInfo`. Evidencia: lista de verificación con la consulta y su resultado.
4. `Laboratorio parcial` Incorpora un servidor Windows o Linux con Defender for Servers Plan 2 ([incorporar servidores](https://learn.microsoft.com/en-us/defender-endpoint/onboard-server)). Limitación: Defender for Servers se cobra por servidor y por hora en Azure; usa una sola VM durante pocas horas y desactiva el plan al terminar. Evidencia: servidor visible en el inventario con su plan.
5. `Laboratorio` Lee el artículo sobre la [incorporación simplificada con el paquete de despliegue de Defender](https://jeffreyappel.nl/simplified-onboarding-of-microsoft-defender-for-endpoint-using-the-defender-deployment-package/) (mayo de 2026) y compara ese método con el script local en una tabla de ventajas y riesgos. Evidencia: tabla con tu recomendación para el anillo piloto.

**¿Quieres profundizar?**

- [Jeffrey Appel - Microsoft Security blog](https://jeffreyappel.nl/) · Blog
- [Simplified onboarding of Microsoft Defender for Endpoint using the Defender deployment tool](https://jeffreyappel.nl/simplified-onboarding-of-microsoft-defender-for-endpoint-using-the-defender-deployment-package/) · Blog

<a id="i5"></a>

## I5 · Defender for Identity: fundamentos y sensor v3.x

*L100–L200 · ~5 h · Origen: Ninja oficial de Defender for Identity (planificación y sensores; versión 9.0 de enero de 2024), actualizado al sensor v3.x*

La mayoría de los ataques graves terminan en Active Directory: reconocimiento LDAP, robo de tickets Kerberos, DCSync, abuso de certificados de AD CS. **Defender for Identity** (MDI) observa esas actividades con sensores en los controladores de dominio y en servidores AD FS, AD CS y Microsoft Entra Connect, y las convierte en alertas, evaluaciones de postura y datos de búsqueda avanzada en las tablas `Identity*`.

El gran cambio es el **sensor v3.x**, unificado con Defender for Endpoint: se activa desde el portal, usa solo LocalSystem, se actualiza por Windows Update y requiere Windows Server 2019 o posterior con la actualización acumulativa de septiembre de 2026 (sensor 3.0.10 o superior). La migración desde v2.x llegó a GA en julio de 2026, la activación sin MDE en octubre, y desde el 13 de septiembre los clientes nuevos de MDE reciben el sensor y la auditoría activados automáticamente.

**Por qué importa**

Detectar el movimiento lateral y la escalada en Active Directory acorta el tiempo de permanencia del atacante y habilita la contención de cuentas en la interrupción automática. Además, las evaluaciones de postura de identidad convierten configuraciones heredadas riesgosas en un backlog priorizado y medible para el equipo de identidad.

**Qué vas a lograr**

- Explicar la arquitectura del sensor v3.x y sus requisitos.
- Activar el sensor en un controlador de dominio y validar su salud.
- Distinguir las limitaciones del v3.x frente al v2.x.
- Reconocer las tablas Identity* que el sensor alimenta.

> **Novedad.** Requisitos del sensor v3.x (página actualizada el 19 de octubre de 2026): Windows Server 2019 o posterior con la actualización acumulativa de septiembre de 2026 o posterior (sensor 3.0.10+), sin sensor v2.x instalado y con el servidor incorporado a Defender for Endpoint, o con la activación sin MDE en servidores elegibles. Si lo despliegas en AD FS, AD CS o Entra Connect, necesitas al menos un sensor v3.x en un controlador de dominio ([sensor v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3)).

> **Atención.** Limitaciones del v3.x: no integra VPN, no envía notificaciones syslog y tiene limitaciones con ExpressRoute; usa solo LocalSystem (ni DSA ni gMSA), limita la CPU al 30 % y la memoria a 1,5 GB, y la herramienta de dimensionamiento solo aplica al v2.x ([sensor v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3)). Revisa estos puntos antes de prometer paridad con el sensor clásico.

> **Qué cambió.** Activación automática: los clientes nuevos de MDE (primer dispositivo incorporado desde el 13 de septiembre de 2026) reciben el v3.x y la auditoría de Windows sin pasos manuales; los clientes existentes de MDI ven un aviso de 30 días con opción de exclusión antes de la activación gradual. Desde octubre de 2026 (vista previa) el v2.x queda restringido en workspaces nuevos a Windows Server 2016 o anterior, y desde mayo cada workspace admite 1.000 sensores, antes 350 ([novedades de MDI](https://learn.microsoft.com/en-us/defender-for-identity/whats-new)).

> **Atención.** Estado por rol: la página de despliegue marca en vista previa la activación manual en servidores AD FS, AD CS y Entra Connect que no son controladores de dominio, mientras las novedades de octubre de 2026 anuncian GA de la activación sin MDE para esos roles en despliegues nuevos. Verifica en el portal la opción disponible para servidores que no son DC (detalle en [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia)).

**¿Tienes poco tiempo?**

- [Deploy the Microsoft Defender for Identity sensor v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3) · Documentación
- [Seamless Migration to the Unified MDI Sensor (V3)](https://www.youtube.com/watch?v=fp_JpsZ3Oos) · Webinar
- [Safeguard your environment with Microsoft Defender for Identity](https://learn.microsoft.com/en-us/training/modules/m365-threat-safeguard/) · Curso

### Documentación, cursos y credenciales

- [Deploy the Microsoft Defender for Identity sensor v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 oct 2026. Guía oficial para activar el sensor unificado v3.x en controladores de dominio y servidores AD FS, AD CS y Entra Connect, con requisitos de SO, actualización acumulativa, licencias, RBAC, red y memoria.
- [Safeguard your environment with Microsoft Defender for Identity](https://learn.microsoft.com/en-us/training/modules/m365-threat-safeguard/) · Curso · Oficial · Microsoft Learn. Módulo gratuito de Microsoft Learn (aprox. 1 h) sobre capacidades, sensores, revisión de cuentas comprometidas e integración de Defender for Identity, con evaluación del módulo.

### Webinars, videos y podcasts

- [Seamless Migration to the Unified MDI Sensor (V3)](https://www.youtube.com/watch?v=fp_JpsZ3Oos) · Webinar · Empleado de Microsoft · Ronit Litinski · Microsoft Security Community (YouTube). Episodio sobre la migración desde el portal del sensor clásico v2.x al sensor unificado v3.x sin tiempo de inactividad ni duplicación de datos.
- [The new Defender for Identity sensor explained](https://www.youtube.com/watch?v=edWVJlt8MmQ) · Video · Empleado de Microsoft · Legado aún útil · Mark Thomas · Microsoft Security Community (YouTube). Explicación del nuevo sensor de Defender for Identity (requisitos, despliegue simplificado y próximos pasos) por un Senior Product Manager. *Nota:* Publicado hace ~1 año (fines de 2025); requisitos actualizados en 2026 (AD CS/AD FS/Entra Connect, activación sin MDE)
- [Microsoft Defender for Identity SC-300 | Episode 14](https://www.youtube.com/watch?v=_9ns92u5eh8) · Video · Empleado de Microsoft · Waleed Mir · Microsoft Learn (YouTube). Episodio de la serie SC-300 sobre detecciones de Defender for Identity, despliegue de sensores y uso de honeytokens.

**Manos a la obra**

1. `Laboratorio` Despliega en Azure un controlador de dominio Windows Server 2022 (B2ms) con la actualización acumulativa de septiembre de 2026 y activa el sensor en Settings > Identities > Sensor management, con MDE o con la [activación sin MDE](https://learn.microsoft.com/en-us/defender-for-identity/deploy/activate-sensor). Valida la salud del sensor y la auditoría automática. Evidencia: sensor saludable y sin problemas de salud abiertos.
2. `Laboratorio` Comprueba que el sensor alimenta la búsqueda avanzada: inicia sesión con un usuario de prueba, ejecuta una consulta LDAP benigna y busca los eventos en `IdentityLogonEvents`, `IdentityDirectoryEvents` e `IdentityQueryEvents`. Evidencia: tres consultas con resultados.
3. `Laboratorio` Verifica qué permisos te dejan crear el workspace y gestionar sensores: Security Administrator o los permisos del RBAC unificado «System settings (Read and manage)» y «Security settings (All permissions)» ([sensor v3.x](https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3)). Evidencia: rol personalizado documentado para el ingeniero de identidad.
4. `Laboratorio` Arma una tabla v2.x frente a v3.x (cuenta de servicio, Npcap, VPN, syslog, forma de actualización y límites de recursos) para tu plan de migración de [M4](02_Nivel_2_Intermedio.md#m4), con apoyo del video [Seamless Migration to the Unified MDI Sensor (V3)](https://www.youtube.com/watch?v=fp_JpsZ3Oos). Evidencia: tabla revisada por el dueño de Active Directory.
5. `Laboratorio` Completa el módulo [Safeguard your environment with Microsoft Defender for Identity](https://learn.microsoft.com/en-us/training/modules/m365-threat-safeguard/) y anota qué partes describen el sensor clásico. Evidencia: lista de diferencias con el v3.x.

**¿Quieres profundizar?**

- [The new Defender for Identity sensor explained](https://www.youtube.com/watch?v=edWVJlt8MmQ) · Video

<a id="i6"></a>

## I6 · Entra ID Protection: fundamentos

*L100–L200 · ~5 h · Origen: Nuevo en esta edición (los Ninja oficiales de Defender no lo cubren; se profundiza en el programa de Entra)*

**Microsoft Entra ID Protection** evalúa el riesgo de cada inicio de sesión y de cada usuario con detecciones en tiempo real y fuera de línea: tokens anómalos, adversario en el medio (AiTM), password spray, credenciales filtradas, IP de actores verificados, propiedades de inicio de sesión desconocidas y más. Ese riesgo alimenta el acceso condicional y llega al portal de Defender como alertas que el SOC investiga junto con el resto del incidente.

Es independiente de Defender XDR: viene con **Entra ID P2**, incluido en Microsoft 365 E5 y E7, Microsoft Defender Suite y EMS E5; sin P2 solo se ve una detección genérica («Additional risk detected»). En este nivel aprendes a leer el catálogo de detecciones, a simular algunas de forma segura y a ubicar las señales en el portal; las directivas y la remediación llegan en [M5](02_Nivel_2_Intermedio.md#m5) y se profundizan en el programa de Entra (módulo M2).

**Por qué importa**

Las identidades son hoy el primer objetivo del atacante: con una contraseña válida o un token robado no hace falta malware. Entender qué detecta ID Protection, con qué latencia y con qué licencia permite al SOC priorizar alertas de identidad con criterio, y al equipo de identidad diseñar controles que se disparan solos, sin esperar a un analista.

**Qué vas a lograr**

- Distinguir riesgo de inicio de sesión y riesgo de usuario, en tiempo real y fuera de línea.
- Reconocer las detecciones clave y cuáles requieren P2.
- Simular detecciones de forma segura en el laboratorio.
- Encontrar las alertas de ID Protection en el portal de Defender.

> **Novedad.** El catálogo oficial de detecciones (actualizado el 21 de octubre de 2026) separa el riesgo de inicio de sesión del riesgo de usuario, las detecciones en tiempo real de las fuera de línea y las Premium (P2) de las no Premium: sin P2 solo verás «Additional risk detected» ([detecciones de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)).

> **Atención.** Lee bien cada detección: **Password spray** solo se dispara si el atacante valida con éxito la contraseña de un usuario; **Attacker in the Middle** detecta proxies inversos maliciosos y requiere Microsoft 365 E5 con EMS E5 a través de Defender for Cloud Apps; **Anomalous Token** cubre tokens de sesión y de actualización ([detecciones de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks)).

> **Qué cambió.** Desde el 11 de diciembre de 2025 (vista previa), el valor predeterminado de las alertas de Entra ID Protection en Defender XDR es enviar solo las de riesgo alto ([investigar alertas](https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts)). Si tu SOC esperaba alertas de riesgo medio, revisa esa configuración.

> **Consejo Ninja.** Entra ID P2 viene en Microsoft 365 E5 y E7, Defender Suite, Defender Suite FLW, Defender + Purview Suite FLW y EMS E5; Entra Suite, que también incluye ID Protection, está en E7 ([licencias de Entra](https://learn.microsoft.com/en-us/entra/fundamentals/licensing)). El acceso condicional y la gobernanza se profundizan en el programa de Entra.

**¿Tienes poco tiempo?**

- [What are risk detections? - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Documentación
- [Simulate Risk Detections in Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk) · Laboratorio
- [Stop identity attacks in real time with Microsoft Entra ID Protection](https://www.youtube.com/watch?v=669bhT3XprM) · Webinar

### Documentación, cursos y credenciales

- [What are risk detections? - Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) · Documentación · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Catálogo oficial de detecciones de riesgo de inicio de sesión y de usuario (tiempo real vs offline, Premium vs no Premium y riskEventType para Graph), incluidas Anomalous Token, Attacker in the Middle, Password spray, Leaked credentials y Microsoft Entra threat intelligence.
- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Documentación · Oficial · Microsoft Learn. Referencia oficial de licencias de Entra: Entra ID P2 (que habilita ID Protection) se incluye en Microsoft 365 E5 y E7, Microsoft Defender Suite (antes Microsoft 365 E5 Security) y EMS E5, y Entra Suite se incluye en E7.

### Webinars, videos y podcasts

- [Stop identity attacks in real time with Microsoft Entra ID Protection](https://www.youtube.com/watch?v=669bhT3XprM) · Webinar · Oficial · Microsoft Security Community (YouTube). Sesión del canal Microsoft Security Community sobre remediación adaptativa de riesgo, detecciones y cobertura de identidades humanas, de aplicaciones y agentes con integración en Defender y Security Copilot.
- [Microsoft Entra ID Protection | SC-300 | Episode 13](https://www.youtube.com/watch?v=0Sf7c4OKGxY) · Video · Oficial · Microsoft Learn (YouTube). Episodio de la serie SC-300 que introduce detección, investigación y remediación de riesgo con ID Protection y su relación con Defender for Identity.

### Laboratorios, GitHub y herramientas

- [Simulate Risk Detections in Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk) · Laboratorio · Oficial · Microsoft Learn. Guía oficial para simular detecciones (IP anónima, propiedades de inicio de sesión desconocidas, viaje atípico y credenciales filtradas de workload identities) y probar directivas de riesgo.

**Manos a la obra**

1. `Laboratorio` Simula una detección de IP anónima: inicia sesión con un usuario de prueba desde el navegador Tor, como indica la [guía de simulación](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk), y localiza el evento en Risky sign-ins. Evidencia: captura de la detección con su nivel de riesgo.
2. `Laboratorio` Simula propiedades de inicio de sesión desconocidas con otro usuario de prueba según la misma guía y compara cuánto tarda cada detección en aparecer. Evidencia: tabla con la hora del inicio de sesión y la hora de la detección.
3. `Laboratorio` Lista las detecciones con Microsoft Graph siguiendo el [tutorial de la API de riesgo](https://learn.microsoft.com/en-us/graph/tutorial-riskdetection-api) y descarta el riesgo del usuario con una cuenta que tenga el rol Security Operator. Evidencia: salida de la API y entrada en el historial de riesgo.
4. `Laboratorio` En el portal de Defender, filtra las alertas por el producto de Entra ID Protection ([investigar riesgo](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk)) y revisa qué niveles de riesgo envía tu configuración. Evidencia: captura del filtro y de la configuración.
5. `Laboratorio` Arma una ficha de diez detecciones con el tipo de riesgo, si es en tiempo real o fuera de línea, si requiere P2 y si se puede simular de forma segura. Evidencia: ficha que reutilizarás en [M5](02_Nivel_2_Intermedio.md#m5).

<a id="i7"></a>

## I7 · KQL y búsqueda avanzada esencial

*L100–L200 · ~8 h · Origen: Ninja oficial de Defender XDR, Fundamentals (búsqueda avanzada) y Ninja de MDE, rol SecOps*

La **búsqueda avanzada** (advanced hunting) es el corazón analítico del portal de Defender: consulta con KQL hasta 30 días de datos crudos de endpoints, correo, identidades y aplicaciones en la nube y, si incorporaste un workspace de Sentinel, también sus tablas según la retención del nivel de analítica. Con ella investigas incidentes, cazas amenazas, construyes detecciones personalizadas y das contexto a los agentes de IA.

Este módulo te lleva de cero a consultas útiles: el esquema por dominios (`Device*`, `Email*`, `Identity*`, `EntraId*`, `CloudAppEvents`, `Alert*`), los operadores esenciales, los límites del servicio (100.000 filas, 10 minutos y 64 MB por consulta, más una cuota de CPU por inquilino) y las buenas prácticas que hacen que una consulta escale. También verás los cambios de esquema de 2026, como `EntraIdSignInEvents` y `AgentsInfo`.

**Por qué importa**

KQL es la diferencia entre un analista que mira pantallas y uno que responde preguntas. Un SOC que escribe consultas eficientes investiga más rápido, convierte hallazgos en detecciones y evita que consultas mal escritas agoten la cuota de CPU del inquilino en medio de un incidente.

**Qué vas a lograr**

- Escribir consultas KQL con where, project, extend, summarize, join y let.
- Navegar el esquema de búsqueda avanzada por dominio y entidad.
- Aplicar buenas prácticas de rendimiento y respetar los límites del servicio.
- Identificar los cambios de tablas de 2026 y su impacto en las consultas guardadas.

> **Atención.** Límites de la búsqueda avanzada: 30 días de datos crudos de Defender XDR, 100.000 filas, 10 minutos de ejecución y 64 MB por resultado; la cuota de CPU depende del tamaño del inquilino y se mide en ciclos de 15 minutos, y todos los datos están en UTC ([búsqueda avanzada](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)). Desde enero de 2026 (vista previa), si el resultado supera 64 MB recibes resultados parciales en lugar de un error ([novedades](https://learn.microsoft.com/en-us/defender-xdr/whats-new)).

> **Qué cambió.** Esquema 2026: `EntraIdSignInEvents`, `EntraIdSpnSignInEvents`, `IdentityAccountInfo` y `GraphAPIAuditEvents` pasaron a GA en febrero; `DisruptionAndResponseEvents`, `CloudAuditEvents`, `CloudDnsEvents` y `CloudProcessEvents`, en junio; `AgentsInfo` reemplazó a `AIAgentsInfo`, accesible solo hasta el 1 de julio de 2026 ([novedades](https://learn.microsoft.com/en-us/defender-xdr/whats-new)), y `EntraIdSignInEvents` reemplazó a `AADSignInEventsBeta` el 19 de octubre de 2026 con migración automática ([EntraIdSignInEvents](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)).

> **Consejo Ninja.** Las buenas prácticas que más rinden: filtra por tiempo primero, usa `has` en lugar de `contains`, evita términos de tres caracteres o menos, pon la tabla más pequeña a la izquierda del `join` y usa las sugerencias `shuffle` o `broadcast` cuando corresponda ([buenas prácticas](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-best-practices)).

> **Atención.** Los permisos del RBAC unificado son granulares: «Email & collaboration metadata (read)» habilita `EmailEvents`, `UrlClickEvents`, `CampaignInfo` y las tablas de mensajes de Teams, y «Security data basics (read)» las de alertas y comportamientos. Los datos que viven solo en el data lake de Sentinel no se consultan desde la búsqueda avanzada ([búsqueda avanzada](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview)).

**¿Tienes poco tiempo?**

- [Proactively hunt for threats with advanced hunting in Microsoft Defender (Advanced hunting overview)](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) · Documentación
- [Understand the advanced hunting schema (Data tables in the Microsoft Defender XDR advanced hunting schema)](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables) · Documentación
- [Advanced hunting query best practices](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-best-practices) · Documentación

### Documentación, cursos y credenciales

- [Understand the advanced hunting schema (Data tables in the Microsoft Defender XDR advanced hunting schema)](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Referencia de todas las tablas del esquema (Device*, Email*, Identity*, EntraId*, CloudAppEvents, Alert*, Exposure*, Message* de Teams, AgentsInfo, etc.) con su estado preview o GA.
- [What's new in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 sep 2026. Registro mensual de novedades de Defender XDR (tablas de búsqueda avanzada, detecciones personalizadas, alert tuning, threat analytics, ISOC) imprescindible para mantener el temario al día.
- [Proactively hunt for threats with advanced hunting in Microsoft Defender (Advanced hunting overview)](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Explica qué es la búsqueda avanzada (30 días de datos crudos de Defender XDR, modos guiado y avanzado), permisos URBAC por esquema y los límites de servicio (100.000 filas, 10 minutos, 64 MB, cuota de CPU cada 15 minutos).
- [Advanced hunting query best practices](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-best-practices) · Documentación · Oficial · Microsoft Learn. Buenas prácticas para optimizar consultas KQL de búsqueda avanzada (filtrar temprano, has vs contains, joins con tabla pequeña a la izquierda, hints, summarize) y respetar la cuota de CPU.

**Manos a la obra**

1. `Laboratorio` Escribe cuatro consultas, una por dominio, sobre `DeviceProcessEvents`, `EmailEvents`, `IdentityLogonEvents` y `CloudAppEvents`; anota el indicador de uso de recursos y reescríbelas aplicando las [buenas prácticas](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-best-practices). Evidencia: tabla antes y después con el tiempo de ejecución.
2. `Laboratorio` Practica `let`, `summarize`, `join` y `make_set` con una pregunta concreta —los diez procesos que más lanzan PowerShell con comandos codificados en tus VM— y guárdala como consulta compartida. Evidencia: consulta guardada con su descripción.
3. `Laboratorio` Resuelve al menos el primer caso de [Kusto Detective Agency](https://detective.kusto.io/) para afianzar la sintaxis fuera del portal. Evidencia: captura del caso resuelto.
4. `Laboratorio` Revisa tus consultas guardadas y detecciones en busca de `AADSignInEventsBeta` o `AIAgentsInfo` y migra cada referencia a `EntraIdSignInEvents` o `AgentsInfo`. Evidencia: lista de consultas cambiadas con el antes y el después.
5. `Laboratorio` Con la [referencia del esquema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables), arma un mapa de tablas por dominio (Device, Email, Identity, EntraId, CloudAppEvents, Alert, Exposure, Teams y agentes) y marca las que están en vista previa. Evidencia: mapa de una página.

<a id="i8"></a>

## I8 · Laboratorios de práctica

*L100–L200 · ~8 h · Origen: Guía oficial «Investigate and respond using Microsoft Defender» y laboratorios del curso SC-200*

El Ninja siempre fue práctico. Microsoft publica una guía oficial para generar incidentes reales en un entorno de prueba: una campaña de **Attack simulation training**, los tutoriales y simulaciones de Defender for Endpoint, un **ataque sin archivos** contra un controlador de dominio aislado con el sensor de Defender for Identity y un ejercicio de búsqueda que termina en una detección personalizada. Los laboratorios del curso SC-200 agregan simulaciones con Atomic Red Team y demos de Sentinel.

Arma tu laboratorio una vez y reutilízalo en todo el programa: un inquilino de prueba de Microsoft 365 E5, un controlador de dominio y un cliente Windows en Azure, y un presupuesto con alertas desde el primer día. Lo que no puedas practicar —volumen real, varios inquilinos, licencias pagas de Security Copilot— está marcado en cada ejercicio con su estrategia de práctica segura en producción.

**Por qué importa**

Un analista que nunca vio un incidente completo en un entorno controlado aprende en producción, bajo presión y con errores caros. Un laboratorio reproducible permite entrenar a cada persona nueva en días, probar cambios antes de aplicarlos y demostrar a auditoría que las detecciones funcionan.

**Qué vas a lograr**

- Construir un laboratorio con controlador de dominio, cliente Windows, MDE, MDI y MDO en un inquilino de prueba.
- Generar incidentes con las simulaciones oficiales y resolverlos de punta a punta.
- Validar el sensor de MDI con pruebas de alertas y de acciones de remediación.
- Controlar el costo y limpiar el laboratorio.

> **Consejo Ninja.** La guía oficial de práctica genera incidentes con cuatro ejercicios: Attack simulation training, los tutoriales de MDE «Document drops backdoor» y «Automated investigation backdoor», un ataque sin archivos contra un controlador de dominio aislado (con sensor de MDI y un cliente Windows unido al dominio e incorporado a MDE) y una búsqueda que termina en una detección personalizada ([investigar y responder](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-investigate-respond)).

> **Atención.** Attack simulation training requiere Microsoft 365 E5 o Defender for Office 365 Plan 2 (E3 solo trae una prueba limitada con el payload Credential Harvest), está disponible en las regiones LAM, BRA, CHL y MEX y no admite RBAC unificado ni PowerShell; el portal ofrece una prueba de 90 días de MDO Plan 2 ([Attack simulation training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)).

> **Atención.** Algunos laboratorios públicos envejecieron: la Zero Trust Lab Guide de Defender for Identity usa el flujo del sensor clásico con DSA ([cloudlab](https://microsoft.github.io/cloudlab/defidentity/)) y la guía de piloto todavía muestra AIR de MDE en la simulación, aunque desde el 1 de septiembre de 2026 ya no corre como experiencia separada. Los laboratorios del curso SC-200 siguen vigentes y usan Atomic Red Team para simular Mimikatz y SharpHound ([laboratorio SC-200](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst/blob/master/Instructions/VTD_Demos/02-mitigate-threats-defender-for-endpoint.md)).

> **Consejo Ninja.** Controla el costo desde el primer día: una VM B2ms encendida todo el mes cuesta unos 60 USD ([precio de referencia](https://azurehub.org/tools/vm-pricing/Standard_B2ms/)), así que programa el apagado automático ([auto-shutdown](https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm)) y usa presupuestos con alertas. El anexo común del entorno de práctica detalla el laboratorio completo y su costo mensual.

**¿Tienes poco tiempo?**

- [Investigate and respond using Microsoft Defender (pilot: attack simulations, isolated DC lab, hunting exercise)](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-investigate-respond) · Laboratorio
- [Validate sensor deployment on domain controllers (Defender for Identity)](https://learn.microsoft.com/en-us/defender-for-identity/deploy/test-sensor) · Laboratorio
- [Get started using Attack simulation training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started) · Documentación
- [SC-200T00A labs - Module 2 Demo: Mitigate Attacks with Microsoft Defender for Endpoint](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst/blob/master/Instructions/VTD_Demos/02-mitigate-threats-defender-for-endpoint.md) · Laboratorio

### Documentación, cursos y credenciales

- [Get started using Attack simulation training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 jul 2026. Requisitos y roles para simulaciones de phishing (M365 E5 o MDO P2), regiones soportadas incluyendo LAM, BRA, CHL y MEX, y ausencia de soporte de RBAC unificado.
- [Mitigate threats using Microsoft Defender XDR (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-365-defender/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje de 6 módulos (~6 h) alineada a SC-200 sobre incidentes, remediación con MDO, Entra ID Protection, MDI y Defender for Cloud Apps.

### Laboratorios, GitHub y herramientas

- [Investigate and respond using Microsoft Defender (pilot: attack simulations, isolated DC lab, hunting exercise)](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-investigate-respond) · Laboratorio · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Guía oficial de práctica que crea incidentes con simulaciones (MDO attack simulation training, tutoriales de MDE, ataque sin archivos contra un controlador de dominio aislado con MDI) y recorre triage, AIR, hunting y creación de una detección personalizada.
- [Validate sensor deployment on domain controllers (Defender for Identity)](https://learn.microsoft.com/en-us/defender-for-identity/deploy/test-sensor) · Laboratorio · Oficial · Microsoft Learn. Guía para validar sensores MDI: datos en el portal, tablas de hunting, recomendaciones ISPM y pruebas de alertas (honeytoken, servicio sospechoso, comando remoto) y de acciones de remediación.
- [SC-200T00A labs - Module 2 Demo: Mitigate Attacks with Microsoft Defender for Endpoint](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst/blob/master/Instructions/VTD_Demos/02-mitigate-threats-defender-for-endpoint.md) · Laboratorio · Oficial · Microsoft Learning · GitHub - MicrosoftLearning · abr 2026. Demo oficial del curso SC-200 que ejecuta ataques simulados (Mimikatz, SharpHound vía Atomic Red Team) para observar detecciones de MDE.
- [Defender for Identity | Zero Trust Lab Guide](https://microsoft.github.io/cloudlab/defidentity/) · Laboratorio · Oficial · Legado aún útil · Microsoft (GitHub Pages - cloudlab). Laboratorio guiado para instalar el sensor MDI en un DC en Azure, quitar el periodo de aprendizaje y generar alertas con simulaciones. *Nota:* Usa nombres antiguos (Microsoft 365 Defender, Azure ATP) y el sensor clásico con Directory Service Account; el sensor unificado v3.x es GA desde nov-2025

**Manos a la obra**

1. `Laboratorio` Arma el laboratorio base del anexo común: inquilino con prueba de E5, controlador de dominio con sensor v3.x, un cliente Windows 11 unido al dominio e incorporado a MDE y políticas de MDO. Etiqueta todo con `env=lab`, `owner` y `expires`. Evidencia: inventario de recursos con sus etiquetas.
2. `Laboratorio` Ejecuta la simulación de ataque sin archivos contra el controlador de dominio aislado de la [guía oficial](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-investigate-respond), investiga el incidente de punta a punta y ciérralo con la clasificación de prueba de seguridad. Evidencia: línea de tiempo del incidente y su clasificación.
3. `Laboratorio` Ejecuta el tutorial «Document drops backdoor» en el cliente de prueba y documenta qué alertas se correlacionan en el incidente y qué acciones aparecen en el Action center. Evidencia: captura del incidente y del historial de acciones.
4. `Laboratorio` Valida el sensor de MDI con las pruebas oficiales —inicio de sesión con una cuenta honeytoken, servicio sospechoso en el DC y comando remoto como administrador— y con una acción de remediación sobre un usuario de prueba ([validar el sensor](https://learn.microsoft.com/en-us/defender-for-identity/deploy/test-sensor)). Evidencia: tres alertas y la acción en el historial.
5. `Laboratorio` Lanza una campaña de Attack simulation training con el payload Credential Harvest a tres usuarios de prueba y asigna una capacitación ([guía](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)). Evidencia: informe de la simulación con clics, credenciales ingresadas y reportes.
6. `Laboratorio parcial` Reproduce la demo del curso SC-200 que usa Atomic Red Team para simular Mimikatz y SharpHound contra MDE ([laboratorio SC-200](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst/blob/master/Instructions/VTD_Demos/02-mitigate-threats-defender-for-endpoint.md)). Limitación: solo en una VM aislada del laboratorio y nunca fuera de él; algunas técnicas pueden bloquearse antes de producir la alerta esperada. Evidencia: alertas obtenidas frente a las esperadas.
7. `Laboratorio` Cierra el nivel con la limpieza: apaga o elimina las VM, revisa el costo acumulado y deshabilita las cuentas que no vayas a reutilizar. Evidencia: informe de costo del período y lista de verificación de limpieza.

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primer incidente de punta a punta.** En tu laboratorio, aplica las políticas Standard y Strict de Defender for Office 365, incorpora dos equipos a Defender for Endpoint, activa el sensor v3.x de Defender for Identity en el controlador de dominio y simula una detección de riesgo de Entra ID Protection. Luego ejecuta el ataque sin archivos de la guía de piloto, investiga el incidente de punta a punta y ciérralo con su clasificación. Entrega un informe de una página con la línea de tiempo, cinco consultas KQL que usaste y la matriz de licencias que explica qué aportó cada producto.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué dominio tiene más peso en el examen SC-200 según las habilidades medidas del 21 de octubre de 2026?
   - a) Búsqueda de amenazas (20–25 %)
   - b) Responder a incidentes (35–40 %)
   - c) Gestionar el entorno de operaciones de seguridad (40–45 %)
   - d) Configurar Microsoft Purview (30 %)

2. ¿Cómo evalúa el avance el Ninja oficial de Defender XDR?
   - a) Con un examen supervisado al final del programa
   - b) Con un knowledge check al final de cada nivel
   - c) Con una insignia de Credly del examen SC-200
   - d) No tiene evaluación

3. ¿Quién puede usar la vista previa de ISOC en Microsoft Defender desde el 23 de septiembre de 2026?
   - a) Cualquier cliente con un workspace de Sentinel
   - b) Solo los clientes de Microsoft 365 E7
   - c) Solo los proveedores de servicios gestionados
   - d) Clientes de Defender Suite, Microsoft 365 E5 o E7 sin un workspace de Sentinel activo

4. Desde el 1 de julio de 2026, ¿qué incluye Microsoft 365 E3 respecto de Defender for Office 365?
   - a) El Plan 1: Safe Links, Safe Attachments, anti-phishing y Real-time detections
   - b) El Plan 2 completo, con Threat Explorer y AIR
   - c) Solo Exchange Online Protection
   - d) Solo Attack simulation training

5. Un inquilino tiene 4.000 licencias pagas de Microsoft 365 E5. ¿Cuántas SCU de Security Copilot al mes recibe por la inclusión?
   - a) 400
   - b) 1.600
   - c) 4.000
   - d) 10.000

6. Según la guía de inicio de Defender for Office 365, ¿qué conviene resolver antes de ajustar las políticas de amenazas?
   - a) Lanzar una campaña de Attack simulation training
   - b) Crear reglas de flujo de correo personalizadas
   - c) La autenticación del correo: SPF, DKIM y DMARC
   - d) Desactivar la protección integrada

7. ¿Qué recomienda Microsoft para incorporar servidores a Defender for Endpoint?
   - a) Defender for Servers Plan 2
   - b) Una licencia independiente de MDE P1
   - c) Una licencia independiente de MDE P2
   - d) Microsoft 365 E3

8. ¿Qué cuenta usa el sensor v3.x de Defender for Identity para leer Active Directory y ejecutar acciones?
   - a) Una cuenta de servicio de directorio (DSA)
   - b) Una gMSA
   - c) La cuenta de servicio de Entra Connect
   - d) LocalSystem del servidor

9. ¿Cuál de estas NO es una limitación del sensor v3.x de Defender for Identity?
   - a) No integra VPN
   - b) Requiere Npcap
   - c) No envía notificaciones syslog
   - d) Tiene limitaciones con ExpressRoute

10. ¿Cuándo se dispara la detección «Password spray» de Entra ID Protection?
   - a) Ante cualquier intento fallido de inicio de sesión
   - b) Cuando se bloquea una cuenta por intentos fallidos
   - c) Cuando el atacante valida con éxito la contraseña de un usuario del inquilino
   - d) Cuando se usa autenticación heredada

11. Sin licencia Entra ID P2, ¿cómo ves las detecciones Premium de ID Protection?
   - a) Con el detalle completo de cada detección
   - b) No ves nada: no se registra ningún riesgo
   - c) Solo como detecciones fuera de línea
   - d) Solo como «Additional risk detected»

12. ¿Cuántas filas puede devolver como máximo una consulta de búsqueda avanzada en el portal de Defender?
   - a) 10.000
   - b) 50.000
   - c) 1.000.000
   - d) 100.000

13. ¿Qué tabla reemplazó a AIAgentsInfo en la búsqueda avanzada?
   - a) AgentsInventory
   - b) AgentsInfo
   - c) CloudAppEvents
   - d) BehaviorInfo

14. ¿Qué pasa con los datos que viven solo en el data lake de Sentinel?
   - a) No se consultan desde la búsqueda avanzada; se usan la exploración del data lake o los search jobs
   - b) Se consultan directamente en la búsqueda avanzada
   - c) Se copian solos al nivel de análisis
   - d) Solo se consultan por API

15. ¿Qué licencia requiere Attack simulation training completo?
   - a) Microsoft 365 E3 sin complementos
   - b) Exchange Online Plan 2
   - c) Microsoft 365 E5 o Defender for Office 365 Plan 2
   - d) Defender for Endpoint P2

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 4 · Identidad para agentes de IA · Preparar el tenant para agentes

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Nivel 3 · Avanzado](03_Nivel_3_Avanzado.md) · [Índice del programa](README.md) · [Comunidad →](05_Comunidad.md)

<a id="agentes"></a>

La identidad como plano de control de los agentes: Entra Agent ID, acceso condicional y permisos, ciclo de vida con Agent 365, agentes de Security Copilot en Entra, Copilot Studio y Microsoft Foundry. Cierra con el proyecto integrador «preparar el tenant para agentes».

*L300–L400 · 7 módulos · ~40 horas · 78 recursos*

**Módulos de este nivel:** [X1 Identidad: plano de control](#x1) · [X2 Microsoft Entra Agent ID](#x2) · [X3 Acceso y permisos de agentes](#x3) · [X4 Ciclo de vida y Agent 365](#x4) · [X5 Security Copilot en Entra](#x5) · [X6 Copilot Studio y Foundry](#x6) · [X7 Proyecto: tenant para agentes](#x7)

<a id="x1"></a>

## X1 · La identidad como plano de control de los agentes de IA

*L300–L400 · ~3 h · Origen: Nuevo en esta edición (Zero Trust Workshop · pilar de IA)*

Los agentes de IA ya no solo responden: leen correo, consultan APIs, modifican registros e invocan herramientas mediante MCP. Para hacerlo necesitan credenciales y permisos, y eso los convierte en identidades que hay que **autenticar, autorizar, auditar y poder apagar**. Microsoft respondió con **Entra Agent ID**, anunciado el 19 de mayo de 2025 y en disponibilidad general desde mayo de 2026, y con **Agent 365**, el plano de control para observar, gobernar y proteger agentes, GA el 1 de mayo de 2026 junto con Microsoft 365 E7.

La identidad es el plano de control porque es el único punto común a todos los agentes, sin importar dónde se construyan: Copilot Studio, Microsoft Foundry, Security Copilot o un framework de terceros. Sin una política de acceso condicional del tipo «bloquear salvo aprobado», **toda solicitud de token de un agente se permite por defecto**. Y usar cuentas de usuario humanas o service principals genéricos para agentes rompe el acceso condicional, ID Protection y la gobernanza.

Este módulo te da el marco del track: cronología, patrones de acceso (en nombre de un usuario, autónomo o con cuenta de usuario del agente), el reparto de responsabilidades entre Entra (acceso), Purview (datos) y Defender (amenazas), y el **OWASP Top 10 for Agentic Applications 2026**, cuyo riesgo ASI03, «Identity and Privilege Abuse», es el más ligado a Entra. La seguridad de la IA en el SOC se profundiza en el programa de Security Copilot (módulos X3 y X4) y la protección de datos para IA, en el programa de Purview DSPM.

**Por qué importa**

Las organizaciones de MCSA están pasando de pilotos de IA a agentes que actúan con datos reales. Si cada agente usa una cuenta compartida o un secreto en un repositorio, nadie podrá responder quién hizo qué, con qué permiso ni cómo apagarlo. Tratar la identidad como plano de control permite adoptar agentes rápido y con controles verificables. Métricas: agentes inventariados con sponsor, con identidad propia y cubiertos por acceso condicional.

**Qué vas a lograr**

- Explicar por qué los agentes necesitan un tipo de identidad propio.
- Reconstruir la cronología de Agent ID, Agent 365 y Microsoft 365 E7.
- Distinguir los patrones de acceso interactivo, autónomo y con cuenta de usuario del agente.
- Relacionar los riesgos del OWASP Top 10 agéntico con controles de identidad.

> **Novedad.** Cronología: Microsoft anunció Entra Agent ID el 19 de mayo de 2025; en Ignite, el 18 de noviembre de 2025, presentó Agent 365 —registro, control de acceso, visualización, interoperabilidad y seguridad— y llegaron en vista previa el acceso condicional y el riesgo para agentes; Ignite 2025 fue la mayor expansión de Entra, con más de 50 artículos nuevos de Agent ID; y el 1 de mayo de 2026 llegaron a GA Agent 365 y Microsoft 365 E7 ([novedades de seguridad para IA](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new), [Ignite 2025](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/), [Entra en Ignite 2025](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025)).

> **Atención.** Sin una política de acceso condicional «bloquear salvo aprobado», toda solicitud de token de un agente se permite por defecto ([pilar de IA del Zero Trust Assessment](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar)). Y usar cuentas de usuario humanas o service principals genéricos para agentes rompe el acceso condicional, ID Protection y la gobernanza ([conceptos clave](https://learn.microsoft.com/en-us/entra/agent-id/key-concepts)).

> **Consejo Ninja.** Agent 365 reparte la seguridad de los agentes entre Entra (acceso), Purview (datos) y Defender (amenazas), con visibilidad central en el centro de administración de Microsoft 365: úsalo como mapa de responsabilidades ([seguridad de agentes con Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security)). El riesgo ASI03 «Identity and Privilege Abuse» del OWASP Top 10 agéntico, publicado el 9 de diciembre de 2025, es el más ligado a Entra ([OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)).

**¿Tienes poco tiempo?**

- [What's new in Microsoft AI security?](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new) · Documentación
- [Microsoft Ignite: Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial
- [Configure agent identity security with the Zero Trust Assessment (AI pillar)](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar) · Herramienta
- [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) · Documentación

### Documentación, cursos y credenciales

- [What's new in Microsoft AI security?](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new) · Documentación · Oficial · Microsoft Learn · abr 2026. Registro cronológico de novedades de seguridad para IA en Entra, Defender, Purview y Foundry, desde el anuncio de Agent ID (mayo 2025) hasta Agent 365 y el Security Dashboard for AI.
- [Microsoft Entra Ignite 2025: Key Announcements and Updates](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new-ignite-2025) · Documentación · Oficial · Microsoft Learn · nov 2025. Índice de todo lo anunciado para Entra en Ignite 2025, con Agent ID como eje (más de 50 artículos nuevos) y novedades de autenticación, gobernanza, Security Copilot y Global Secure Access.

### Anuncios y blogs oficiales

- [Microsoft Ignite: Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial · Oficial · Legado aún útil · Vasu Jakkal · Microsoft Security Blog · 18 nov 2025. Visión de Microsoft para la seguridad de la era agéntica y presentación de Agent 365 con sus cinco capacidades: registro, control de acceso, visualización, interoperabilidad y seguridad. *Nota:* Escrito cuando Agent 365 estaba en preview (Frontier); la GA llegó el 1-may-2026

**Manos a la obra**

1. `Laboratorio parcial` Con el rol AI Reader, revisa el inventario de agentes y la tabla `AgentsInfo` de tu tenant de prueba y clasifica cada agente por plataforma y patrón de acceso. Limitación: un tenant de prueba tiene pocos agentes; crea uno en Copilot Studio ([X6](#x6)) para tener datos ([convergencia del registro](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence)).
2. `Laboratorio` Arma la cronología 2025–2026 de Agent ID, Agent 365 y Microsoft 365 E7 con su fuente y escribe en una página qué cambia para tu organización ([novedades de seguridad para IA](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new)).
3. `Laboratorio` Mapea los riesgos del [OWASP Top 10 agéntico](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) a controles de Entra, Purview y Defender, con un dueño por control; usa el reparto de responsabilidades de [Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security).
4. `Solo producción` Entrevista a tres equipos que ya construyen agentes y documenta qué identidad usa cada agente (cuenta de usuario, service principal o Agent ID) y quién responde por él. Cómo hacerlo seguro: solo lectura y sin cambios; entrega los hallazgos al comité como línea base de [X7](#x7).

<a id="x2"></a>

## X2 · Microsoft Entra Agent ID: blueprints, identidades de agente y usuarios de agente

*L300–L400 · ~6 h · Origen: Nuevo en esta edición*

**Microsoft Entra Agent ID** es el marco de identidad y seguridad de Entra para agentes de IA y está en disponibilidad general: la página de novedades de la GA está fechada el 1 de mayo de 2026, aunque el asistente del portal para crear blueprints sigue en vista previa. Su modelo tiene cuatro piezas: el **blueprint** de identidad de agente, plantilla y contenedor de credenciales; el **principal del blueprint**; la **identidad de agente**, un service principal especial sin credenciales propias y de un solo tenant; y, opcionalmente, una **cuenta de usuario del agente** 1:1 para escenarios que necesitan buzón o Teams.

Las credenciales —federadas, certificados o secretos— viven solo en el blueprint, que puede ser multitenant. Los permisos OAuth concedidos al blueprint **se heredan** en todas sus identidades y deshabilitarlo deshabilita a todos sus agentes: el blueprint es tu frontera de credenciales y de radio de impacto. Cada identidad y cada blueprint necesitan al menos un **sponsor** (responsable de negocio); los **owners** son opcionales y técnicos, y los **managers** reflejan la jerarquía y pueden pedir paquetes de acceso.

Hay salvaguardas: los agentes no pueden recibir roles como Global Administrator, Privileged Role Administrator o User Administrator ni pertenecer a grupos asignables a roles, y los roles **Agent ID Administrator** y **Agent ID Developer**, junto con la opción de tenant «Users can create agent blueprints», controlan quién crea. Foundry, Copilot Studio y Security Copilot asignan Agent ID automáticamente; para otros frameworks se recomienda la CLI o el SDK de Agent 365. Agent ID está disponible para todos los clientes de Entra; extender la seguridad de Entra a los agentes requiere Agent 365.

**Por qué importa**

Sin un tipo de identidad específico, los agentes nacen como service principals genéricos o, peor, como cuentas de usuario compartidas, y se pierden la atribución, el ciclo de vida y los controles. Agent ID da a cada agente identidad propia, un responsable de negocio y un contenedor de credenciales gobernable. Métricas: agentes con sponsor, blueprints con credenciales federadas y agentes sin owner.

**Qué vas a lograr**

- Describir el modelo de objetos de Agent ID: blueprint, principal, identidad de agente y usuario de agente.
- Crear un blueprint e identidades de agente con el portal o con Microsoft Graph.
- Asignar owners, sponsors y managers y explicar la responsabilidad de cada uno.
- Controlar quién puede crear blueprints y qué roles pueden recibir los agentes.
- Planificar la arquitectura de identidades de agente de la organización.

> **Novedad.** Agent ID está en disponibilidad general: la página de novedades de la GA, fechada el 1 de mayo de 2026, trajo patrones de diseño, el SDK sidecar, integración de agentes no Microsoft, migraciones, gobernanza con paquetes de acceso y plantillas de acceso condicional. El asistente del portal para crear blueprints sigue en vista previa ([novedades de Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id)).

> **Atención.** Licencia: Agent ID está disponible para todos los clientes de Entra, pero extender las funciones de seguridad de Entra a los agentes requiere Agent 365 (incluido en Microsoft 365 E7; complemento para E5, A5 o Business Premium, o para Defender Suite más Purview Suite) ([qué es Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id)).

> **Consejo Ninja.** Un grupo dinámico como sponsor puede tardar hasta 24 horas en reflejarse y no todos los tipos de grupo se admiten; los owners pueden ser usuarios o service principals, no grupos. Gestionar owners y sponsors requiere Agent ID Administrator o ser owner ([administrar owners y sponsors](https://learn.microsoft.com/en-us/entra/agent-id/manage-owners-sponsors-agents), [relaciones administrativas](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers)).

> **Atención.** Según el capítulo comunitario de identidades de agente (septiembre de 2026), los creadores quedan como owners por defecto, los permisos heredados del blueprint solo se ven en el token y AI Administrator debería tratarse como Tier 0; Datadog Security Labs analizó el radio de impacto de blueprints multitenant de terceros ([Attack & Defense: Agent Identities](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md), [radio de impacto del blueprint](https://securitylabs.datadoghq.com/articles/agent-id-blueprint-blast-radius/)).

**¿Tienes poco tiempo?**

- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Documentación
- [Microsoft Entra Agent ID key concepts](https://learn.microsoft.com/en-us/entra/agent-id/key-concepts) · Documentación
- [Agent identity blueprints in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint) · Documentación
- [Create an agent identity blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) · Laboratorio

### Documentación, cursos y credenciales

- [What is Microsoft Entra Agent ID?](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 24 jun 2026. Define Agent ID como el marco de identidad y seguridad de Entra para agentes de IA (identidades de agente y blueprints) y aclara qué requiere licencia de Agent 365.
- [What's new in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 may 2026. Resume lo que trajo la disponibilidad general de Entra Agent ID: conceptos, patrones de diseño, SDK sidecar, integración de agentes no Microsoft, migraciones, gobernanza por paquetes de acceso y plantillas de acceso condicional para agentes.
- [Agent identity blueprints in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-blueprint) · Documentación · Oficial · Microsoft Learn. Explica el blueprint como plantilla y contenedor de identidades de agente: guarda credenciales, permisos heredables y permite aplicar acceso condicional o deshabilitar a todos sus agentes de una vez.
- [Administrative relationships in Microsoft Entra Agent ID (Owners, sponsors, and managers)](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers) · Documentación · Oficial · Microsoft Learn. Diferencia owners (administración técnica), sponsors (responsabilidad de negocio, obligatorios) y managers (jerarquía, solicitud de paquetes de acceso) para blueprints e identidades de agente.
- [Microsoft Entra Agent ID key concepts](https://learn.microsoft.com/en-us/entra/agent-id/key-concepts) · Documentación · Oficial · Microsoft Learn. Glosario base: identidad de agente, blueprint, principal del blueprint, cuenta de usuario del agente y patrones interactivo vs autónomo, y por qué no usar service principals ni usuarios normales para agentes.
- [Planeamiento de la arquitectura de identidad del agente (es-es)](https://learn.microsoft.com/es-es/entra/agent-id/how-to-plan-agent-identity-architecture) · Documentación · Oficial · ES · Microsoft Learn. Guía de decisiones en cuatro pasos: tipo de identidad, patrón de operación, número de blueprints e identidades por blueprint, y por qué no usar service principals ni usuarios normales para agentes.
- [Agent identities in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Documentación · Oficial · Microsoft Learn. Anatomía de una identidad de agente: service principal especial sin credenciales propias, sponsor, blueprint, cuenta de usuario opcional y alcance de un solo tenant.
- [Add and manage owners and sponsors for agent identities and blueprints](https://learn.microsoft.com/en-us/entra/agent-id/manage-owners-sponsors-agents) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 may 2026. Procedimiento en el centro de administración de Entra para asignar y quitar owners y sponsors en blueprints e identidades de agente.
- [Novedades de Agente de Microsoft Entra ID (es-es)](https://learn.microsoft.com/es-es/entra/agent-id/whats-new-agent-id) · Documentación · Oficial · Nuevo · ES · Microsoft Learn · 1 may 2026. Versión en español de las novedades de la GA de Agent ID, útil para presentar el producto a equipos hispanohablantes.
- [What is the Microsoft agent identity platform](https://learn.microsoft.com/en-us/entra/agent-id/what-is-agent-id-platform) · Documentación · Oficial · Microsoft Learn. Arquitectura de la plataforma de identidad para agentes: servicio de autenticación OAuth 2.0/OIDC, SDK (Microsoft Identity Web y sidecar) y gestión/registro de agentes en Entra.
- [Microsoft Entra Agent ID documentation](https://learn.microsoft.com/en-us/entra/agent-id/) · Documentación · Oficial · Microsoft Learn. Portal de documentación de Agent ID con rutas para administrar, gobernar y proteger agentes, conceptos clave, planificación y desarrollo sobre la plataforma.

### Anuncios y blogs oficiales

- [Build AI agents for production with secure identities from day one](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606) · Blog oficial · Oficial · Nuevo · ArLucaID · Microsoft Entra Blog (Tech Community) · 2 jun 2026. Explica blueprint, identidad de agente, sponsors y owners, y los canales de aprovisionamiento: Foundry, Copilot Studio y Security Copilot reciben Agent ID automáticamente; otros frameworks usan la CLI/SDK de Agent 365.

### Laboratorios, GitHub y herramientas

- [Create an agent identity blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) · Laboratorio · Oficial · Microsoft Learn. Guía paso a paso para crear un blueprint y su principal desde el portal (asistente en preview) o con Microsoft Graph/PowerShell, incluyendo credenciales, URI y scopes.
- [Creating a custom agent with Agent ID (MasterclassELDK26 lab 4)](https://github.com/IdentityMan/MasterclassELDK26/blob/main/labs/lab-4-agent-id/readme.md) · Laboratorio · Comunidad · Comunidad (masterclass Experts Live Denmark 2026; commits de Merill Fernando) · IdentityMan/MasterclassELDK26 (GitHub) · feb 2026. Laboratorio comunitario para crear un blueprint e identidad de agente con los módulos beta de Entra PowerShell y conectar un agente de ejemplo con permisos heredables.

### Comunidad: blogs, libros, newsletters y eventos

- [Machine Identities: the accounts that no one counts](https://www.securitytoday.de/en/2026/05/15/enter-agent-id-machine-identities/) · Blog · Comunidad · Nuevo · Alec Chizhik · SecurityToday · 15 may 2026. Análisis independiente del modelo de Agent ID (blueprint, principal, identidad y usuario de agente) y del riesgo de proliferación de cuentas no humanas.

**Manos a la obra**

1. `Laboratorio` Crea un blueprint y una identidad de agente con Microsoft Graph o PowerShell, asigna un owner y un sponsor (un grupo dinámico) y compruébalo en el portal ([crear un blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint)).
2. `Laboratorio` Revisa la opción de tenant «Users can create agent blueprints» y asigna Agent ID Developer como rol elegible en PIM a un desarrollador de prueba ([crear un blueprint](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint)).
3. `Laboratorio` Intenta asignar Global Administrator a la identidad de agente y documenta el bloqueo; después asigna un rol permitido y justifícalo por escrito ([autorización en Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/authorization-agent-id)).
4. `Laboratorio` Sigue el [laboratorio comunitario de Agent ID](https://github.com/IdentityMan/MasterclassELDK26/blob/main/labs/lab-4-agent-id/readme.md) para conectar un agente de ejemplo con permisos heredables, reemplazando el secreto de desarrollo por una credencial federada o un certificado.
5. `Laboratorio` Diseña la arquitectura de identidades de agente de tu organización con la [guía de cuatro pasos](https://learn.microsoft.com/es-es/entra/agent-id/how-to-plan-agent-identity-architecture): tipo de identidad, patrón de operación, número de blueprints e identidades por blueprint.
6. `Solo producción` Piloto en producción con un blueprint, owner y sponsor asignados. Cómo hacerlo seguro: un solo agente de bajo riesgo, permisos enumerados mínimos, revisión de acceso programada y fecha de vencimiento de las credenciales.

**¿Quieres profundizar?**

- [Creating a custom agent with Agent ID (MasterclassELDK26 lab 4)](https://github.com/IdentityMan/MasterclassELDK26/blob/main/labs/lab-4-agent-id/readme.md) · Laboratorio

<a id="x3"></a>

## X3 · Acceso condicional, protección y permisos para agentes

*L300–L400 · ~6 h · Origen: Nuevo en esta edición (laboratorio 3B de Microsoft Learning)*

El acceso condicional para agentes requiere **Microsoft 365 E7, o Agent 365 más al menos Entra ID P1 o Microsoft 365 E3**. La clave es apuntar al **sujeto del token**: si el agente actúa en nombre de un usuario (OBO), la política se asigna a usuarios y grupos; si actúa solo (app-only), a la identidad de agente o a su blueprint; y si usa una cuenta de usuario del agente, a **Agent Users**, porque las políticas asignadas a «Users» no la cubren. Una política no cubre a la otra.

Hay límites que debes conocer: el acceso condicional no protege recursos a los que el agente accede con claves de API y no se aplica si los valores predeterminados de seguridad están activos. Con la GA llegaron plantillas para bloquear agentes de alto riesgo y para controlar el acceso de agentes autónomos y en nombre de usuarios, y la condición **Agent execution environments** (vista previa) para los Cloud PC de agentes. **ID Protection para agentes** suma detecciones fuera de línea —reconocimiento del directorio, picos de inicios de sesión, uso sospechoso de credenciales del blueprint, acceso inusual a recursos— y, en flujos OBO, atribuye el riesgo al usuario.

El tercer pilar es el **mínimo privilegio**: identidad dedicada con owner y sponsor, permisos efectivos sumados (los heredados del blueprint solo se ven en las reclamaciones del token), herramientas denegadas por defecto, privilegios temporales y rutas de revocación probadas. Si tus agentes usan MCP, Entra puede ser el servidor de autorización: tokens v2, metadatos de recurso protegido (RFC 9728) y validación con librerías probadas.

**Por qué importa**

Un agente con permisos amplios y sin políticas es una cuenta de servicio que además decide: si lo engañan con una inyección de prompts, usará todos sus permisos. El acceso condicional, el riesgo de agentes y el mínimo privilegio limitan qué puede hacer, desde dónde y por cuánto tiempo. Métricas: agentes con política aplicable, permisos efectivos por agente y agentes de riesgo alto bloqueados.

**Qué vas a lograr**

- Diseñar políticas de acceso condicional según el sujeto del token del agente.
- Interpretar detecciones de riesgo de agentes y aplicar acceso condicional basado en riesgo.
- Aplicar el patrón de mínimo privilegio: permisos efectivos, herramientas restringidas y privilegios temporales.
- Proteger un servidor MCP con Microsoft Entra ID como servidor de autorización.

> **Atención.** Licencia del acceso condicional para agentes: Microsoft 365 E7, o Agent 365 más al menos Entra ID P1 o Microsoft 365 E3. No protege recursos accedidos con claves de API, no se aplica con los valores predeterminados de seguridad activos y las políticas asignadas a «Users» no cubren las cuentas de usuario de agente ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)).

> **Novedad.** Con la GA de Agent ID llegaron plantillas para bloquear agentes de alto riesgo y controlar el acceso de agentes autónomos y en nombre de usuarios, y la condición «Agent execution environments» (vista previa) para los Cloud PC de agentes. ID Protection para agentes suma detecciones fuera de línea —reconocimiento del directorio, picos de inicios de sesión, uso sospechoso de credenciales del blueprint, acceso inusual a recursos— y su licencia está en revisión ([novedades de Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id), [ID Protection para agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)).

> **Consejo Ninja.** Al proteger un servidor MCP con Entra ID, el paso que más se omite es `requestedAccessTokenVersion=2`; publica los metadatos de recurso protegido (RFC 9728) y no escribas tu propia validación de tokens ([proteger un servidor MCP](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id)). OWASP publica una guía práctica para desarrollar servidores MCP seguros ([Agentic Security Initiative](https://genai.owasp.org/initiatives/agentic-security-initiative/)).

> **Consejo Ninja.** Patrón de mínimo privilegio: identidad dedicada con owner y sponsor, permisos efectivos sumados, herramientas denegadas por defecto, privilegios temporales y rutas de revocación probadas. Microsoft recomienda privilegios a tiempo (JIT) en lugar de identidades efímeras por tarea ([mínimo privilegio para agentes](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents), [blog de julio de 2026](https://www.microsoft.com/en-us/security/blog/2026/07/16/least-privilege-for-ai-agents-identity-access-and-tool-binding/)).

**¿Tienes poco tiempo?**

- [Conditional Access for agents](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Documentación
- [ID Protection for agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) · Documentación
- [Least privilege for AI agents with Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents) · Documentación
- [Secure a Model Context Protocol (MCP) server with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id) · Laboratorio

**A qué apunta la política según el patrón de acceso del agente**

| Patrón de acceso | Sujeto del token | Objeto al que apunta la política | Ten en cuenta |
|---|---|---|---|
| En nombre de un usuario (OBO) | El usuario | Usuarios y grupos | En ID Protection, el riesgo también se atribuye al usuario |
| Autónomo (app-only) | La identidad de agente | La identidad de agente o su blueprint | Una política sobre el blueprint alcanza a todas sus identidades |
| Con cuenta de usuario del agente | La cuenta de usuario del agente | «Agent Users» | Las políticas asignadas a «Users» no la cubren; estas cuentas solo existen en tenants del programa Frontier |
| Recurso accedido con clave de API | Ninguno emitido por Entra | No aplica | El acceso condicional no protege estos recursos: migra a autenticación con Entra |

Fuentes: [acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id), [ID Protection para agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) e [identidad en Agent 365](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/identity).

### Documentación, cursos y credenciales

- [Conditional Access for agents](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 sep 2026. Explica cómo el acceso condicional evalúa tokens de agentes según el patrón de acceso (en nombre de un usuario, identidad propia o cuenta de usuario del agente) y a qué objeto apuntar en cada caso.
- [ID Protection for agents](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) · Documentación · Oficial · Microsoft Learn. Describe las detecciones de riesgo para identidades de agente (reconocimiento de directorio, picos de inicios de sesión, uso sospechoso de credenciales del blueprint, acceso a recursos inusuales), el informe de agentes riesgosos y el acceso condicional basado en riesgo de agente.
- [Authorization in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/authorization-agent-id) · Documentación · Oficial · Microsoft Learn. Detalla los roles de Entra y permisos de Graph permitidos y bloqueados para identidades de agente, con salvaguardas que impiden asignarles roles muy privilegiados.
- [Least privilege for AI agents with Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents) · Documentación · Oficial · Microsoft Learn (Zero Trust / SFI Patterns & Practices). Patrón de mínimo privilegio para agentes: identidad dedicada con owner/sponsor, permisos efectivos agregados, herramientas denegadas por defecto, privilegios JIT y rutas de revocación probadas.

### Anuncios y blogs oficiales

- [Least privilege for AI agents: Identity, access, and tool binding](https://www.microsoft.com/en-us/security/blog/2026/07/16/least-privilege-for-ai-agents-identity-access-and-tool-binding/) · Blog oficial · Oficial · Nuevo · Yesenia Yser, Toby Kohlenberg · Microsoft Security Blog · 16 jul 2026. Argumenta tratar cada agente como principal de primera clase con identidad gestionada, roles por tarea, herramientas restringidas por manifiesto y auditoría de extremo a extremo.

### Laboratorios, GitHub y herramientas

- [Agent Identities (Entra ID Attack & Defense Playbook)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) · GitHub · MVP · Nuevo · Robbe Van den Daele, Sami Lamppu, Thomas Naunheim (revisor: Derk van der Woude) · Cloud-Architekt/AzureAD-Attack-Defense (GitHub) · sep 2026. Capítulo del playbook comunitario de ataque y defensa sobre identidades de agente: modelo de amenazas en tres fases, flujo autónomo de tokens, escalamiento por ownership y permisos heredables, detecciones KQL y mitigaciones.
- [Secure a Model Context Protocol (MCP) server with Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id) · Laboratorio · Oficial · Microsoft Learn. Guía para usar Entra ID como servidor de autorización de un servidor MCP: registro con tokens v2, metadatos de recurso protegido (RFC 9728), validación de tokens y conexión de un cliente con Agent ID.
- [Protección de un servidor MCP con Microsoft Entra ID (es-es)](https://learn.microsoft.com/es-es/entra/agent-id/secure-mcp-server-with-entra-id) · Laboratorio · Oficial · ES · Microsoft Learn. Versión en español de la guía de autorización MCP con Entra ID, útil como material de laboratorio para equipos hispanohablantes.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra Agent ID: The blueprint blast radius](https://securitylabs.datadoghq.com/articles/agent-id-blueprint-blast-radius/) · Blog · Comunidad · Nuevo · Katie Knowles · Datadog Security Labs · 11 jun 2026. Investigación independiente sobre permisos heredables, invisibilidad de scopes delegados heredados y el radio de impacto de blueprints multitenant de terceros.

**Manos a la obra**

1. `Laboratorio` Construye la matriz agente → patrón de acceso (en nombre de un usuario, autónomo o con cuenta de usuario del agente) → objeto al que apunta la política, para tres agentes de ejemplo ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)).
2. `Laboratorio` Simula con What If (identidades de agente, en vista previa) qué políticas aplicarían a tu identidad de agente de prueba y guarda el resultado ([What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool)).
3. `Solo producción` Crea CA15 «bloquear salvo aprobado» para un agente piloto; requiere E7 o Agent 365 (el programa Frontier no debe usarse para evaluar). Cómo hacerlo seguro: política en solo informe con alcance a ese agente, revisión del impacto en los registros antes de activarla y reversión documentada; en el laboratorio, deja el diseño versionado como código ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)).
4. `Laboratorio` Protege un servidor MCP de ejemplo con Entra ID —tokens v2, metadatos RFC 9728 y validación con librería— y conéctalo con una identidad de agente ([proteger un servidor MCP](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id)).
5. `Laboratorio` Calcula los permisos efectivos de tu agente (propios más heredados del blueprint, decodificando un token de prueba) y elimina los que no use ([administrar identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin)).
6. `Laboratorio parcial` Sigue el [laboratorio oficial 3B](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md): Foundry, Copilot Studio, acceso condicional para agentes y radio de impacto en Defender. Limitación: el acceso condicional para agentes requiere E7 o Agent 365 y Foundry usa tu suscripción de Azure; en producción, políticas en solo informe y un agente piloto.

**¿Quieres profundizar?**

- [Agent Identities (Entra ID Attack & Defense Playbook)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) · GitHub
- [Entra Agent ID: The blueprint blast radius](https://securitylabs.datadoghq.com/articles/agent-id-blueprint-blast-radius/) · Blog

<a id="x4"></a>

## X4 · Gobernanza del ciclo de vida de agentes y Agent 365

*L300–L400 · ~5 h · Origen: Nuevo en esta edición*

**Agent 365** es el plano de control de Microsoft para observar, gobernar y proteger agentes. Llegó a disponibilidad general el 1 de mayo de 2026, incluido en Microsoft 365 E7 (99 USD por usuario al mes) o como complemento de 15 USD por usuario al mes; cada licencia cubre a una persona que gestiona, patrocina o usa agentes. Funciona mejor con Microsoft 365 E5 y requiere al menos un usuario con licencia para habilitarse. Desde el 1 de octubre de 2026 cumple los controles de FedRAMP High, con la autorización final pendiente.

La línea entre lo incluido y lo pago es importante. Con los planes de Microsoft 365 tienes el **inventario del registro** de agentes, acciones básicas de gobernanza, reglas de ciclo de vida y sincronización desde plataformas externas; ver el inventario completo solo requiere el rol AI Reader o AI Administrator. Las plantillas de políticas, la observabilidad, los paquetes de acceso para agentes, el acceso condicional y ID Protection para agentes, los controles de red, Purview y Defender para agentes requieren **E7 o Agent 365**.

El registro de agentes de Entra converge en Agent 365, que inventaría incluso agentes sin Agent ID, mientras Entra gestiona identidades, acceso y gobernanza: paquetes de acceso, flujos de sponsors y reglas de inactividad. En Defender, la tabla **AgentsInfo** —que reemplazó a AIAgentsInfo, accesible hasta el 1 de julio de 2026— cruza agentes, blueprints, permisos y servidores MCP. Los datos que usan los agentes se gobiernan con Purview y se profundizan en el programa de Purview DSPM.

**Por qué importa**

Los agentes se crean más rápido que las personas: sin reglas de ciclo de vida quedan agentes huérfanos con permisos y credenciales vigentes y sin nadie que responda por ellos. Agent 365 y la gobernanza de Entra convierten el inventario en controles: quién patrocina, a qué accede y cuándo expira. Métricas: agentes sin sponsor, agentes inactivos y paquetes de acceso de agentes revisados.

**Qué vas a lograr**

- Distinguir qué incluyen los planes de Microsoft 365 sin Agent 365 y qué requiere E7 o Agent 365.
- Usar el registro de agentes y la tabla AgentsInfo para el inventario.
- Gobernar el acceso de los agentes con paquetes de acceso, sponsors y reglas de ciclo de vida.
- Planificar licencias de Agent 365 según las personas que gestionan, patrocinan o usan agentes.

> **Novedad.** Agent 365 llegó a GA el 1 de mayo de 2026, incluido en Microsoft 365 E7 (99 USD por usuario al mes) o como complemento de 15 USD por usuario al mes; cada licencia cubre a una persona que gestiona, patrocina o usa agentes. Los agentes delegados y los autónomos que trabajan en segundo plano están en GA y los agentes en flujos de equipo, en vista previa ([GA de E7 y Agent 365](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295), [Agent 365 en GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)).

> **Atención.** Sin Agent 365, los planes de Microsoft 365 incluyen el inventario del registro, acciones básicas de gobernanza, reglas de ciclo de vida y sincronización desde plataformas externas. Las plantillas de políticas, la observabilidad, los paquetes de acceso para agentes, el acceso condicional e ID Protection para agentes, los controles de red, Purview y Defender para agentes requieren E7/G7 o Agent 365. Desde el 1 de octubre de 2026 cumple los controles de FedRAMP High, con la autorización final pendiente ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)).

> **Qué cambió.** En Defender, la tabla AIAgentsInfo pasó a AgentsInfo (la antigua siguió accesible hasta el 1 de julio de 2026), con Agent ID, blueprint, permisos, owners, servidores MCP, herramientas y estado de ciclo de vida; AgentsInfo también existe en Log Analytics, con soporte para los niveles Basic y data lake ([AgentsInfo en Defender](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table), [AgentsInfo en Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/agentsinfo)).

> **Consejo Ninja.** Agent 365 funciona mejor con Microsoft 365 E5 como prerrequisito y requiere al menos un usuario con licencia para habilitarse; algunas funciones salen primero en el programa Frontier con términos de vista previa ([visión general](https://learn.microsoft.com/en-us/microsoft-agent-365/overview), [gestión en el centro de administración](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview)). La gobernanza de agentes con ID Governance requiere E7, o Agent 365 más P1 o E3 ([gobernar identidades de agente](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)).

**¿Tienes poco tiempo?**

- [Microsoft Agent 365 - Service Descriptions](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365) · Documentación
- [Agent Registry convergence with Microsoft Agent 365](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence) · Documentación
- [Governing Agent Identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) · Documentación
- [AgentsInfo table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table) · Documentación

### Documentación, cursos y credenciales

- [AgentsInfo table in the advanced hunting schema](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table) · Documentación · Oficial · Nuevo · Microsoft Learn · 13 oct 2026. Referencia de la tabla AgentsInfo de búsqueda avanzada con el inventario de agentes de varias plataformas: Agent ID, blueprint, permisos, owners, servidores MCP, herramientas y estado de ciclo de vida.
- [Microsoft Agent 365 - Service Descriptions](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365) · Documentación · Oficial · Nuevo · Microsoft Learn (Service Descriptions) · 1 oct 2026. Tabla oficial de funciones de Agent 365 que separa lo incluido en planes Microsoft 365 (inventario, gobernanza básica, reglas, sincronización) de lo que requiere E7/G7 o Agent 365 (plantillas, observabilidad, CA, ID Protection, paquetes de acceso, Purview y Defender para agentes).
- [Microsoft Agent 365 overview](https://learn.microsoft.com/en-us/microsoft-agent-365/overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 ago 2026. Describe los pilares observar, gobernar y proteger de Agent 365, su GA comercial por usuario desde el 1-may-2026 y los prerrequisitos de licencia.
- [Agent 365 identity](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/identity) · Documentación · Oficial · Microsoft Learn. Describe el modelo de identidad que usa Agent 365 (blueprint, identidad de agente y cuenta de usuario opcional), los modos S2S, OBO y de usuario de agente, y dónde se configuran las credenciales.
- [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) · Documentación · Oficial · Microsoft Learn. Muestra cómo Agent 365 reparte la seguridad de agentes entre Entra (acceso), Purview (datos) y Defender (amenazas) con visibilidad central en el centro de administración de Microsoft 365.
- [Agent Registry convergence with Microsoft Agent 365](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence) · Documentación · Oficial · Microsoft Learn. Aclara que el registro de agentes converge en Agent 365 (inventario completo, incluso agentes sin Agent ID) mientras Entra gestiona identidades, acceso condicional y gobernanza.
- [Administración de identidades de agente en la organización (es-es)](https://learn.microsoft.com/es-es/entra/agent-id/manage-agent-identities-admin) · Documentación · Oficial · ES · Microsoft Learn. Guía en español de las tareas de administración de agentes: ver y filtrar identidades, gestionar blueprints, controlar acceso, monitorear, responder a riesgo, supervisar sponsors y deshabilitar agentes.
- [Governing Agent Identities](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview) · Documentación · Oficial · Microsoft Learn. Cómo ID Governance aplica paquetes de acceso, sponsors y flujos de ciclo de vida a identidades de agente, y cómo Foundry, Copilot Studio y Teams crean blueprints.
- [Agent management in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview) · Documentación · Oficial · Microsoft Learn. Explica la gobernanza de agentes desde el centro de administración de Microsoft 365: incorporación aprobada por TI, plantillas de políticas, reglas automáticas (agentes sin owner, agentes riesgosos) y auditoría.
- [Manage agent identities in your organization](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) · Documentación · Oficial · Microsoft Learn. Guía operativa para administradores y sponsors: ver, filtrar, deshabilitar y gobernar identidades de agente, permisos heredables enumerados vs 'all allowed', monitoreo y riesgo.
- [Azure Monitor Logs reference - AgentsInfo](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/agentsinfo) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 jul 2026. Referencia de AgentsInfo en Log Analytics/Sentinel, con soporte para niveles Basic y Auxiliary/data lake para retener el inventario de agentes.
- [Identidades de agentes gobernantes (vista previa) (eu-es)](https://learn.microsoft.com/eu-es/entra/id-governance/agent-id-governance-overview) · Documentación · Oficial · Legado aún útil · ES · Microsoft Learn. Panorama en español de cómo ID Governance gestiona ciclo de vida y acceso de identidades de agente, con sponsors responsables y cómo Foundry aprovisiona identidades por proyecto y por agente publicado. *Nota:* Versión localizada desactualizada: aún dice que Agent ID está en Frontier/preview; la GA ocurrió el 1-may-2026

### Anuncios y blogs oficiales

- [Microsoft 365 E7 and Agent 365 are now generally available](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) · Blog oficial · Oficial · Nuevo · carolinestanford · Microsoft 365 Blog (Tech Community) · 1 may 2026. Anuncia la GA de Microsoft 365 E7 (E5 + Copilot + Entra Suite + Agent 365) y de Agent 365 como plano de control para observar, gobernar y proteger agentes.
- [Microsoft Agent 365, now generally available, expands capabilities and integrations](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) · Blog oficial · Oficial · Nuevo · Nirav Shah, Rob Lefferts, Jason Roszak · Microsoft Security Blog · 1 may 2026. Detalla la GA de Agent 365 y las previews de descubrimiento de shadow AI con Defender e Intune, sincronización del registro con AWS Bedrock y Google Cloud, Windows 365 for Agents y controles de red de Entra para agentes.
- [A new era of agents, a new era of posture](https://www.microsoft.com/en-us/security/blog/2026/01/21/new-era-of-agents-new-era-of-posture/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 21 ene 2026. Explica la gestión de postura de agentes de IA en Defender: agentes conectados a datos sensibles, riesgo de inyección indirecta de prompts y rutas de ataque multicloud.
- [Lead Frontier Transformation with Microsoft 365 E7, now generally available](https://partner.microsoft.com/en-us/blog/article/microsoft-365-e7-general-availability) · Blog oficial · Oficial · Nuevo · Nicole Dezen · Microsoft Partner Blog · 1 may 2026. Visión para partners de E7 y Agent 365: qué es transaccionable desde la GA y ofertas típicas de gobernanza de agentes (aceleradores de 2 a 6 semanas).

**Manos a la obra**

1. `Laboratorio parcial` Consulta `AgentsInfo` en la búsqueda avanzada y migra una consulta antigua que usara AIAgentsInfo. Limitación: con pocos agentes de prueba los resultados son escasos y algunas columnas dependen de Agent 365 ([AgentsInfo](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table)).
2. `Laboratorio` Arma la matriz de licencias de Agent 365: personas que gestionan, patrocinan o usan agentes frente a E7 o complemento, y qué funciones quedan sin cubrir ([descripción de servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)).
3. `Laboratorio` Diseña las reglas de ciclo de vida de tus agentes: inactividad, agentes sin owner o sin sponsor, transferencia de patrocinio y vencimiento de paquetes de acceso ([gobernar identidades de agente](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)).
4. `Solo producción` Flujos de ciclo de vida de sponsors y paquetes de acceso para agentes, que requieren Agent 365 o E7 y movimientos reales de personal. Cómo hacerlo seguro: piloto con un blueprint y un grupo de sponsors de prueba, y notificaciones antes de transferir el patrocinio.
5. `Solo producción` Plantillas de políticas y reglas automáticas del centro de administración de Microsoft 365 (agentes sin owner, agentes riesgosos). Cómo hacerlo seguro: alcance a un piloto, revisión antes de aplicar cada acción y auditoría ([gestión de agentes en Microsoft 365](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-365-overview)).

<a id="x5"></a>

## X5 · Agentes de Security Copilot en Entra

*L300–L400 · ~4 h · Origen: Nuevo en esta edición; se profundiza en el programa de Security Copilot (módulos M3, M6 y M7)*

Security Copilot está integrado en el centro de administración de Entra desde el 14 de julio de 2025, cuando llegaron a disponibilidad general la experiencia embebida y el **agente de optimización de acceso condicional**. Desde el 18 de noviembre de 2025, Microsoft 365 E5 y E7 incluyen Security Copilot: **400 SCU al mes por cada 1.000 licencias de usuario pagas, hasta 10.000 SCU mensuales**, con un despliegue gradual y aviso previo.

El agente de optimización de acceso condicional requiere P1 y SCU disponibles: revisa hasta 300 usuarios y 150 aplicaciones por ejecución, detecta usuarios, apps e identidades de agente sin cobertura y propone políticas —o las crea en modo solo informe si lo autorizas—, con disparadores diarios y por actividad (vista previa). El **Identity Risk Management Agent** (vista previa) investiga hasta 100 usuarios riesgosos por ejecución y propone remediaciones que siempre requieren aprobación manual; el **Access Review Agent** (vista previa desde septiembre de 2025) ayuda a los revisores desde Teams.

Cada agente de Entra crea su propia identidad de agente con permisos fijos que no se pueden cambiar. Vas a configurarlos, revisar sus sugerencias, controlar el consumo de SCU y definir quién aprueba. La operación de un parque de agentes de seguridad y el gobierno de Security Copilot se profundizan en el programa de Security Copilot.

**Por qué importa**

Los equipos de identidad tienen más políticas, usuarios y agentes de los que pueden revisar a mano. Los agentes de Security Copilot en Entra encuentran brechas de cobertura del acceso condicional, investigan usuarios riesgosos y preparan decisiones de revisión, siempre con aprobación humana. Métricas: brechas de cobertura cerradas, tiempo de investigación de usuarios riesgosos y SCU consumidas por resultado.

**Qué vas a lograr**

- Explicar la inclusión de Security Copilot en Microsoft 365 E5 y E7 y su capacidad de SCU.
- Configurar el agente de optimización de acceso condicional y revisar sus sugerencias.
- Evaluar el Identity Risk Management Agent y el Access Review Agent en vista previa.
- Gobernar la identidad, los permisos y el consumo de los agentes de Entra.

> **Novedad.** Microsoft 365 E5 y E7 incluyen Security Copilot desde el 18 de noviembre de 2025, con despliegue gradual y aviso de 30 días: 400 SCU al mes por cada 1.000 licencias de usuario pagas, hasta 10.000 SCU mensuales, sin costo adicional, lo que habilita los agentes de Entra en esos tenants ([inclusión en E5 y E7](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion), [anuncio de Ignite 2025](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/)).

> **Consejo Ninja.** El agente de optimización de acceso condicional está en GA desde el 14 de julio de 2025 ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/smarter-identity-security-starts-with-ai/4429001)). Por defecto no crea políticas; tiene disparadores diarios y por actividad (vista previa), instrucciones personalizadas e integración con ServiceNow (vista previa). Su página de configuración se contradice sobre las ejecuciones por actividad: como máximo cada seis horas o con un enfriamiento de cuatro ([configuración](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-settings)).

> **Atención.** Identity Risk Management Agent (vista previa): investiga hasta 100 usuarios riesgosos por ejecución, no analiza workload identities y toda remediación exige aprobación manual. Su página pide P2, mientras el catálogo de agentes de Entra indica «Microsoft Entra Agent ID» como licencia ([el agente](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started), [catálogo de agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents)).

> **Consejo Ninja.** La exploración de datos en cuadrícula de Security Copilot en Entra está en vista previa y limitada a prompts simples; para auditorías de gobernanza hay prompts de ejemplo sobre revisiones de acceso, paquetes de acceso y asignaciones de PIM ([escenarios en Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-security-scenarios), [gobernanza con Security Copilot](https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization)). El Access Review Agent está en vista previa desde el 30 de septiembre de 2025 ([Access Review Agent](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-microsoft-entra-agent-for-smarter-access-governance-access-review-agent/4279689)).

**¿Tienes poco tiempo?**

- [Microsoft Entra Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Documentación
- [Microsoft Entra agents](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) · Documentación
- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación
- [Smarter identity security starts with AI](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/smarter-identity-security-starts-with-ai/4429001) · Blog oficial

### Documentación, cursos y credenciales

- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Microsoft Learn. Explica la inclusión de Security Copilot en Microsoft 365 E5 y E7: despliegue gradual desde el 18-nov-2025, aprovisionamiento automático y capacidad incluida de SCU.
- [Microsoft Entra Conditional Access Optimization Agent](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Documentación · Oficial · Microsoft Learn. Agente de Security Copilot que detecta usuarios, apps e identidades de agente no cubiertos por acceso condicional y propone o crea políticas en solo informe y consolidaciones; aquí solo como enlace (otro investigador cubre agentes).
- [Microsoft Entra agents](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) · Documentación · Oficial · Microsoft Learn · 1 abr 2026. Catálogo de agentes de Security Copilot para Entra con identidad, licencias, permisos, roles y disparadores de cada uno, más el Security Store embebido en el portal de Entra.
- [Identity Risk Management Agent (Preview)](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 1 may 2026. Agente de Security Copilot en ID Protection que investiga usuarios riesgosos, resume factores de riesgo y propone remediaciones que requieren aprobación manual. *Nota:* Requiere Entra ID P2 y SCU; hasta 100 usuarios por ejecución; no analiza workload identities; la página de agentes de Entra indica en cambio licencia 'Microsoft Entra Agent ID'
- [Microsoft Entra Conditional Access Optimization Agent settings](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-settings) · Documentación · Oficial · Microsoft Learn. Explica la configuración del agente: disparadores diarios y por actividad, objetos a monitorear, permiso para crear políticas en solo informe, instrucciones personalizadas y notificaciones.
- [Microsoft Security Copilot scenarios in Microsoft Entra overview](https://learn.microsoft.com/en-us/entra/security-copilot/entra-security-scenarios) · Documentación · Oficial · Microsoft Learn. Mapa de escenarios de Security Copilot embebido en Entra (usuarios, registros, acceso condicional, riesgo de usuarios y apps, gobernanza, Global Secure Access) con requisitos de rol y licencia.
- [Microsoft Security Copilot agents overview](https://learn.microsoft.com/en-us/copilot/security/agents-overview) · Documentación · Oficial · Microsoft Learn · 18 mar 2026. Introduce la terminología de agentes de Security Copilot (disparadores, permisos, identidad, plugins) y las dos opciones de identidad: Agent ID dedicada o cuenta de usuario existente.
- [Identity Governance and optimization with Microsoft Security Copilot](https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization) · Documentación · Oficial · Microsoft Learn · 23 sep 2025. Ejemplos de prompts de Security Copilot en Entra para analizar revisiones de acceso, paquetes de acceso de entitlement management y asignaciones de PIM de cara a una auditoría.

### Anuncios y blogs oficiales

- [Agents built into your workflow: Get Security Copilot with Microsoft 365 E5](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/) · Blog oficial · Oficial · Dorothy Li · Microsoft Security Blog · 18 nov 2025. Anuncio de Ignite 2025: Security Copilot incluido en Microsoft 365 E5 y 12 nuevos agentes de Microsoft en preview, incluidos agentes de Entra para riesgo de usuarios, acceso condicional, revisiones de acceso y ciclo de vida de apps.
- [Smarter identity security starts with AI](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/smarter-identity-security-starts-with-ai/4429001) · Blog oficial · Oficial · Alex Simons · Microsoft Entra Blog (Tech Community) · 14 jul 2025. Anuncia la disponibilidad general del Conditional Access Optimization Agent y de Security Copilot integrado en Microsoft Entra, con la nueva hoja Agents del centro de administración.
- [The Microsoft Entra agent for smarter access governance: Access Review Agent](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-microsoft-entra-agent-for-smarter-access-governance-access-review-agent/4279689) · Blog oficial · Oficial · Vista previa · ManmeetBawa · Microsoft Entra Blog (Tech Community) · 30 sep 2025. Presenta el Access Review Agent de Security Copilot, que analiza actividad de inicio de sesión y pares para recomendar decisiones de revisión de acceso y conversa con los revisores en Microsoft Teams. *Nota:* Public preview anunciada el 30-sep-2025; verificar estado actual en el portal antes de usarlo en producción

**Manos a la obra**

1. `Laboratorio` Calcula la capacidad de Security Copilot incluida para tu organización (400 SCU al mes por cada 1.000 licencias pagas, con tope de 10.000) y estima cuántas ejecuciones del agente de optimización puedes programar ([inclusión en E5 y E7](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).
2. `Laboratorio parcial` Documenta, a partir del [catálogo de agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents), la identidad, los permisos, los roles y la licencia de cada agente. Limitación: sin SCU no puedes activarlos para verlos en tu tenant.
3. `Laboratorio parcial` En una sesión corta con 1 SCU aprovisionada y excedente en 0, prueba prompts de gobernanza en Entra (revisiones de acceso, PIM) y borra la capacidad al terminar. Limitación: Security Copilot no tiene prueba gratuita y la capacidad se factura por hora ([gobernanza con Security Copilot](https://learn.microsoft.com/en-us/entra/security-copilot/entra-governance-optimization)).
4. `Solo producción` Configura el agente de optimización de acceso condicional con disparador diario y revisa sus sugerencias; requiere SCU y datos reales. Cómo hacerlo seguro: deja desactivada la creación de políticas, aprueba solo políticas en solo informe y asigna Security Reader a los observadores ([configuración del agente](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-settings)).
5. `Solo producción` Evalúa el Identity Risk Management Agent sobre usuarios riesgosos reales. Cómo hacerlo seguro: alcance a un grupo piloto, aprobación manual de cada remediación y registro de las decisiones ([Identity Risk Management Agent](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started)).

<a id="x6"></a>

## X6 · Copilot Studio y Microsoft Foundry: identidades y permisos de agentes

*L300–L400 · ~6 h · Origen: Nuevo en esta edición; se profundiza en el programa de Security Copilot (módulos A6 y A7)*

En **Copilot Studio**, cada agente nuevo recibe un Entra Agent ID desde mayo de 2026; los agentes anteriores conservan sus registros de aplicación hasta que se migren y el owner del agente se agrega como sponsor. Nadie en tu tenant, ni siquiera un administrador, puede emitir tokens con la identidad de un agente de Copilot Studio: la gestiona un blueprint propiedad de Microsoft con credenciales federadas. Los conectores del agente aparecen como permisos de API en su Agent ID y pueden ser objetivo del acceso condicional.

El gobierno en Copilot Studio pasa por las **políticas de datos de Power Platform**, que controlan la autenticación de makers y usuarios, las fuentes de conocimiento, los conectores, HTTP, los canales y los disparadores. Microsoft documentó diez configuraciones inseguras frecuentes —agentes compartidos con toda la organización, sin autenticación, con credenciales del maker, con secretos embebidos o con herramientas MCP sin control— y publicó consultas para detectarlas en Defender.

En **Microsoft Foundry**, cuyo nombre anterior era Azure AI Foundry (así lo verás en material de 2025), cada agente recibe automáticamente un blueprint y una identidad con credencial federada, sin secretos, pero **sin permisos**: debes concederlos con Azure RBAC de mínimo privilegio, y la audiencia del token debe ser el recurso de destino, no la URL del servidor MCP. Cierras mapeando el OWASP Top 10 agéntico a controles concretos.

**Por qué importa**

La mayoría de los agentes de una organización los crearán makers y desarrolladores, no el equipo de identidad. Si las políticas de datos, la autenticación y los permisos no se definen antes, los agentes nacerán compartidos con toda la organización, sin autenticación o con las credenciales de su creador. Métricas: agentes sin autenticación (meta: cero), agentes con credenciales del maker y agentes de Foundry con RBAC mínimo.

**Qué vas a lograr**

- Explicar cómo Copilot Studio y Foundry asignan identidades de agente y quién puede emitir sus tokens.
- Configurar políticas de datos de Power Platform por entorno para agentes seguros.
- Asignar permisos de mínimo privilegio con Azure RBAC a agentes de Foundry.
- Detectar configuraciones inseguras de agentes con búsqueda avanzada en Defender.
- Relacionar el OWASP Top 10 agéntico con controles concretos en Copilot Studio y Agent 365.

> **Qué cambió.** Copilot Studio crea un Entra Agent ID para cada agente nuevo desde mayo de 2026; los agentes anteriores siguen con registros de aplicación hasta su migración y el owner se agrega como sponsor. Versiones localizadas anteriores decían julio de 2026 y que desde entonces no hay opt-out ([Agent ID en Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities)).

> **Consejo Ninja.** En Copilot Studio, los agentes del tenant comparten un único blueprint y los conectores se autentican mayormente en nombre del usuario bajo políticas de datos: los permisos se gobiernan desde el centro de administración de Power Platform, no por blueprint ([integración de identidad en Copilot Studio](https://learn.microsoft.com/en-us/microsoft-agent-365/builder/identity)).

> **Novedad.** Microsoft documentó en febrero de 2026 diez configuraciones inseguras frecuentes de agentes, con consultas en Defender (Advanced hunting > Community queries > carpeta AI Agent) ([configuraciones inseguras](https://www.microsoft.com/en-us/security/blog/2026/02/12/detecting-and-mitigating-common-agent-misconfigurations/)); y en agosto de 2026 llegó en vista previa Agent ID para Dataverse, con usuarios de agente y roles de mínimo privilegio ([Agent ID para Dataverse](https://www.microsoft.com/en-us/power-platform/blog/2026/08/06/microsoft-entra-agent-id-for-dataverse/)).

> **Atención.** En Microsoft Foundry, la identidad del agente nace sin permisos y la audiencia del token debe coincidir con el recurso de destino, no con la URL del servidor MCP ([identidad de agentes en Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)). La página en español de México es traducción automática y menciona Azure AI Foundry (hoy Microsoft Foundry); ante dudas, prevalece la versión en inglés.

**¿Tienes poco tiempo?**

- [Agent identities and authentication for Copilot Studio (App registration, agent identities, and authentication)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/govern-agents-identities-overview) · Documentación
- [Microsoft Entra Agent IDs for Copilot Studio agents (Manage Entra Agent IDs)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities) · Documentación
- [Agent identity concepts in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Documentación
- [Detecting and mitigating common agent misconfigurations](https://www.microsoft.com/en-us/security/blog/2026/02/12/detecting-and-mitigating-common-agent-misconfigurations/) · Blog oficial

### Documentación, cursos y credenciales

- [Agent identities and authentication for Copilot Studio (App registration, agent identities, and authentication)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/govern-agents-identities-overview) · Documentación · Oficial · Microsoft Learn. Preguntas frecuentes sobre cómo Copilot Studio identifica a sus agentes: Entra Agent ID para agentes nuevos, registros de aplicación heredados, el owner agregado como sponsor y quién puede emitir tokens.
- [Microsoft Entra Agent IDs for Copilot Studio agents (Manage Entra Agent IDs)](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities) · Documentación · Oficial · Microsoft Learn. Explica la creación automática de Entra Agent ID para cada agente nuevo de Copilot Studio, el blueprint global, los permisos de conectores visibles como permisos de API y su uso como objetivo de acceso condicional.
- [Agent identity concepts in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Documentación · Oficial · Microsoft Learn. Explica cómo Foundry aprovisiona automáticamente un blueprint e identidad de agente por agente, usa credenciales federadas sin secretos y obliga a conceder permisos con Azure RBAC de mínimo privilegio.
- [Key concepts - Copilot Studio security and governance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance) · Documentación · Oficial · Microsoft Learn. Inventario de controles de seguridad de Copilot Studio: políticas de datos (autenticación de makers y usuarios, conectores, HTTP, canales, disparadores), escaneo automático de seguridad, auditoría en Purview y Sentinel, e integración con Agent 365.
- [Secure your Copilot Studio projects](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase3) · Documentación · Oficial · Microsoft Learn (Copilot Studio guidance). Recomendaciones prácticas: licencias y acceso por grupos de Entra, políticas de datos restrictivas por entorno, publicación de agentes de IA generativa controlada, secretos en Key Vault y despliegue con compuertas.
- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · Documentación · Comunidad · OWASP Agentic Security Initiative · OWASP Gen AI Security Project · 9 dic 2025. Marco revisado por pares con los diez riesgos críticos de aplicaciones agénticas (secuestro de objetivos, mal uso de herramientas, abuso de identidad y privilegios, cadena de suministro, agentes rebeldes, etc.).
- [Agent identity integration for Copilot Studio](https://learn.microsoft.com/en-us/microsoft-agent-365/builder/identity) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 may 2026. Describe cómo los agentes de Copilot Studio comparten un único blueprint por tenant, reciben su Agent ID al crearse y autentican conectores mayormente en nombre del usuario bajo políticas DLP.
- [Conceptos de identidad del agente en Microsoft Foundry (es-mx)](https://learn.microsoft.com/es-mx/azure/ai-foundry/agents/concepts/agent-identity?view=foundry) · Documentación · Oficial · ES · Microsoft Learn. Versión en español del concepto de identidad de agente en Foundry, útil para equipos hispanohablantes que inician con agentes pro-code.
- [Seguridad y gobernanza - Microsoft Copilot Studio (es-es)](https://learn.microsoft.com/es-es/microsoft-copilot-studio/security-and-governance) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de los controles de seguridad y gobernanza de Copilot Studio, apta para formar a makers y administradores hispanohablantes.

### Anuncios y blogs oficiales

- [Addressing the OWASP Top 10 Risks in Agentic AI with Microsoft Copilot Studio](https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/) · Blog oficial · Oficial · Efim Hudis · Microsoft Security Blog · 30 mar 2026. Mapea los riesgos del OWASP Top 10 agéntico a mitigaciones concretas con Agent 365 y Copilot Studio, destacando el abuso de identidad y privilegios.
- [Detecting and mitigating common agent misconfigurations](https://www.microsoft.com/en-us/security/blog/2026/02/12/detecting-and-mitigating-common-agent-misconfigurations/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 12 feb 2026. Diez configuraciones inseguras frecuentes en agentes (compartidos con toda la organización, sin autenticación, credenciales del maker, secretos embebidos, herramientas MCP) con consultas de búsqueda avanzada y mitigaciones en Copilot Studio.
- [Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) · Blog oficial · Oficial · Nuevo · Microsoft Defender Experts / Incident Response · Microsoft Security Blog · 30 jun 2026. Caso de envenenamiento de descripciones de herramientas MCP en un flujo financiero de Copilot Studio y guía para detectarlo, contenerlo y prevenirlo.
- [From runtime risk to real-time defense: Securing AI agents](https://www.microsoft.com/en-us/security/blog/2026/01/23/runtime-risk-realtime-defense-securing-ai-agents/) · Blog oficial · Oficial · Microsoft Defender Security Research Team · Microsoft Security Blog · 23 ene 2026. Muestra cómo la protección en tiempo real de Defender inspecciona cada invocación de herramienta de agentes de Copilot Studio y bloquea acciones inseguras inducidas por prompts.
- [Secured and Governed your AI Agents: Microsoft Entra Agent ID for Dataverse](https://www.microsoft.com/en-us/power-platform/blog/2026/08/06/microsoft-entra-agent-id-for-dataverse/) · Blog oficial · Oficial · Vista previa · Nuevo · Paul Liew · Microsoft Power Platform Blog · 6 ago 2026. Presenta los usuarios de agente en Dataverse vinculados a una identidad de Entra Agent ID para asignar roles de seguridad de mínimo privilegio y auditar las acciones del agente. *Nota:* Public preview (ago-2026); recomienda empezar en un entorno que no sea de producción

### Laboratorios, GitHub y herramientas

- [Agentic Security Initiative (OWASP GenAI)](https://genai.owasp.org/initiatives/agentic-security-initiative/) · Herramienta · Comunidad · OWASP · OWASP Gen AI Security Project. Portal de la iniciativa de seguridad agéntica de OWASP con la guía práctica para servidores MCP seguros, el Agent Control Standard y el estado de la gobernanza agéntica.

### Comunidad: blogs, libros, newsletters y eventos

- [OWASP GenAI Security Project Releases Top 10 Risks and Mitigations for Agentic AI Security](https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/) · Blog · Comunidad · Scott Clinton · OWASP Gen AI Security Project · 9 dic 2025. Comunicado del lanzamiento del Top 10 agéntico con el contexto de recursos complementarios (guía de agentes seguros, CTF FinBot, landscape de soluciones).

**Manos a la obra**

1. `Laboratorio` En Copilot Studio (prueba), crea un agente, localiza su Entra Agent ID en Settings > Advanced > Metadata y revisa en Entra los permisos de sus conectores ([Agent ID en Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities)).
2. `Laboratorio` Crea una política de datos de Power Platform que impida agentes sin autenticación y restrinja HTTP en el entorno de desarrollo, y verifica que tu agente de prueba la cumple ([seguridad y gobierno de Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance), [recomendaciones por fase](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/sec-gov-phase3)).
3. `Laboratorio parcial` Ejecuta en Defender las consultas comunitarias de la carpeta «AI Agent» y la tabla AgentsInfo. Limitación: con pocos agentes de prueba los resultados son escasos y algunas columnas dependen de Agent 365; en producción, solo lectura con Security Reader ([configuraciones inseguras](https://www.microsoft.com/en-us/security/blog/2026/02/12/detecting-and-mitigating-common-agent-misconfigurations/)).
4. `Laboratorio` En Microsoft Foundry, con tu suscripción de Azure, crea un agente, revisa su blueprint y su identidad y asígnale el rol de Azure mínimo para leer un recurso de prueba ([identidad de agentes en Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)).
5. `Laboratorio` Mapea el OWASP Top 10 agéntico a controles de Copilot Studio y Agent 365 con el [análisis de Microsoft de marzo de 2026](https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/).
6. `Solo producción` Revisa los agentes reales de tu organización contra las diez configuraciones inseguras. Cómo hacerlo seguro: solo lectura con Security Reader, informe a los makers y corrección entorno por entorno con los dueños.

**¿Quieres profundizar?**

- [Agentic Security Initiative (OWASP GenAI)](https://genai.owasp.org/initiatives/agentic-security-initiative/) · Herramienta

<a id="x7"></a>

## X7 · Proyecto integrador: preparar el tenant para agentes

*L300–L400 · ~10 h · Origen: Nuevo en esta edición (equivale a la evaluación práctica final del track)*

El cierre del track es preparar tu tenant de punta a punta para adoptar agentes con controles verificables. Usarás como lista de verificación la tabla [Preparación del tenant para agentes de IA](00_Programa.md#preparacion-agentes) y como guion el **pilar de IA del Zero Trust Workshop** (actualizado el 31 de mayo de 2026): mapear el riesgo de IA, registrar agentes, asegurar autenticación, red y datos, construir agentes seguros y detectar y responder. El **Zero Trust Assessment** verifica de forma automática buena parte de esos controles.

El proyecto está organizado en fases con entregables: diagnóstico, identidad, acceso, permisos y herramientas, plataformas (Copilot Studio y Foundry), gobierno, monitoreo y respuesta, y presentación al comité. Los patrones de la Secure Future Initiative —defensa en profundidad para agentes autónomos y gestión del riesgo agéntico— te ayudan a justificar cada decisión.

Al terminar tendrás un portafolio reutilizable: políticas en solo informe exportadas como código, blueprints con credenciales federadas, un runbook para deshabilitar un agente comprometido, un plan de licencias y métricas de adopción segura. Lo que se evalúa no es usar todas las funciones, sino el criterio: qué controlar primero, qué licencia hace falta y cómo se mide.

**Por qué importa**

Preparar el tenant antes de escalar agentes es mucho más barato que corregir después. Este proyecto deja una línea base que permite decir que sí a nuevos agentes con criterios claros: identidad propia, sponsor, permisos mínimos, acceso condicional, monitoreo y un plan de respuesta. Métricas: controles de la tabla en verde, hallazgos del pilar de IA cerrados y tiempo de aprobación de un nuevo agente.

**Qué vas a lograr**

- Evaluar el tenant con el Zero Trust Assessment (pilar de IA) y la tabla de preparación.
- Implementar los controles mínimos de identidad, acceso, gobierno y monitoreo para agentes.
- Documentar la arquitectura, las licencias necesarias y el plan de respuesta.
- Presentar el resultado a un comité con métricas y hoja de ruta.

> **Consejo Ninja.** Usa como guion el pilar de IA del Zero Trust Workshop (actualizado el 31 de mayo de 2026) y verifica con el pilar de IA del Zero Trust Assessment; la misma guía se publica dentro de la documentación de Entra, así que cita una sola ([Zero Trust Workshop · AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security), [pilar de IA](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar)).

> **Novedad.** Los patrones de la Secure Future Initiative para agentes —defensa en profundidad con controles por capas (modelo, sistema de seguridad, aplicación con identidad única y supervisión humana determinista) y reducción del riesgo agéntico (adherencia a la tarea, secuestro, fuga de datos, cadena de suministro y proliferación)— sirven para justificar cada decisión ante el comité ([sistemas agénticos seguros](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems), [riesgo agéntico](https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk)).

> **Atención.** El laboratorio 3B es un trabajo en curso (pasos válidos al 30 de junio de 2026, sin entorno prearmado) y el kit comunitario A365 Hub tiene la mayoría de sus módulos planificados o en desarrollo: úsalos solo en un tenant de laboratorio dedicado ([laboratorio 3B](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md), [A365 Hub](https://github.com/Cyberlorians/a365-hub/tree/main)).

**¿Tienes poco tiempo?**

- [Microsoft Zero Trust Workshop - AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Herramienta
- [Configure agent identity security with the Zero Trust Assessment (AI pillar)](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar) · Herramienta
- [Secure Microsoft Entra Agent Identities (Supplemental Lab 3B)](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md) · Laboratorio
- [Secure autonomous agentic AI systems](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems) · Documentación

### Documentación, cursos y credenciales

- [Secure autonomous agentic AI systems](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems) · Documentación · Oficial · Microsoft Learn (Zero Trust / SFI Patterns & Practices). Patrón de defensa en profundidad para agentes autónomos con controles por capas: modelo, sistema de seguridad, aplicación (mínimo privilegio, identidad única, HITL determinista) y posicionamiento.
- [Reduce autonomous agentic AI risk](https://learn.microsoft.com/en-us/security/zero-trust/sfi/manage-agentic-risk) · Documentación · Oficial · Microsoft Learn (Zero Trust / SFI Patterns & Practices). Identifica riesgos de diseño y seguridad de agentes autónomos (adherencia a la tarea, supervisión humana, secuestro, fuga de datos, cadena de suministro, proliferación) y pilares de mitigación.
- [Configure Microsoft Entra agent identities for increased security (Entra fundamentals)](https://learn.microsoft.com/en-us/entra/fundamentals/zero-trust-ai) · Documentación · Oficial · Microsoft Learn. Misma guía del pilar de IA del Zero Trust Assessment publicada dentro de la documentación de Entra, con acciones de remediación enlazadas.

### Laboratorios, GitHub y herramientas

- [Microsoft Zero Trust Workshop - AI security](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Herramienta · Oficial · Nuevo · Microsoft Learn · 31 may 2026. Pilar de IA del Zero Trust Workshop: mapear riesgo de IA, registrar agentes, asegurar autenticación, red y datos, construir agentes seguros y detectar/responder.
- [Configure agent identity security with the Zero Trust Assessment (AI pillar)](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar) · Herramienta · Oficial · Microsoft Learn. Recomendaciones y verificaciones automáticas del Zero Trust Assessment para agentes: exigir autenticación Entra, acceso condicional sobre identidades y usuarios de agente, gobernanza de ciclo de vida y roles de IA con responsables.
- [Secure Microsoft Entra Agent Identities (Supplemental Lab 3B)](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md) · Laboratorio · Oficial · Vista previa · Nuevo · Microsoft Learning · MicrosoftLearning (GitHub) · 30 jun 2026. Laboratorio oficial de 60 minutos: localizar una identidad de agente, crear políticas de acceso condicional para identidades y usuarios de agente, analizar el radio de impacto en Defender XDR y activar protección en tiempo real en Copilot Studio. *Nota:* Marcado como 'work in progress': pasos válidos al 30-jun-2026; sin entorno de laboratorio prearmado
- [TechLab: Entra Suite for Frontier Transformation](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) · Laboratorio · Oficial · Nuevo · Microsoft (GitHub) · oct 2026. Laboratorio de 4 horas de Entra Suite: ciclo de vida, Private Access, acceso JIT con revisiones y filtrado de contenido, descubrimiento de tráfico MCP y protección contra inyección de prompts para humanos y agentes.
- [A365 Hub - open workshop kit for Microsoft Entra Agent ID and Agent 365](https://github.com/Cyberlorians/a365-hub/tree/main) · GitHub · Comunidad · Cyberlorians · Cyberlorians (GitHub). Kit de taller abierto sobre identidad agéntica, Agent ID y Agent 365, con aprovisionamiento de asistentes sin secretos (identidades administradas y TAP) y una hoja de ruta de laboratorios y CTF.

**Manos a la obra**

1. `Laboratorio` Fase 1 · Diagnóstico: ejecuta el Zero Trust Assessment (pilar de IA) y completa el estado de cada control en la tabla de [preparación del tenant para agentes](00_Programa.md#preparacion-agentes) ([pilar de IA](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar)).
2. `Laboratorio` Fase 2 · Identidad: un blueprint con credencial federada, dos identidades de agente con sponsor y los roles de IA solo elegibles en PIM (controles 2 a 8).
3. `Solo producción` Fase 3 · Acceso: CA15 a CA17 y la plantilla de agentes de alto riesgo (controles 9 a 13), que requieren E7 o Agent 365. Cómo hacerlo seguro: todas en solo informe, alcance a un agente piloto, revisión del impacto y reversión documentada; en el laboratorio, deja las políticas diseñadas como código.
4. `Laboratorio` Fase 4 · Permisos y herramientas: servidor MCP protegido con Entra, permisos heredables enumerados, herramientas denegadas por defecto y consentimiento restringido (controles 14 a 16).
5. `Laboratorio` Fase 5 · Plataformas: política de datos de Copilot Studio, Agent ID en todos sus agentes y Azure RBAC mínimo en Foundry (controles 17 a 19).
6. `Laboratorio parcial` Fase 6 · Gobierno y monitoreo: reglas de ciclo de vida, registros en Log Analytics, `AgentsInfo` y una alerta por agente nuevo sin sponsor (controles 20, 21 y 23). Limitación: los paquetes de acceso para agentes requieren E7 o Agent 365.
7. `Laboratorio` Fase 7 · Respuesta: runbook para deshabilitar un agente y luego su blueprint, ensayado y cronometrado (control 22).
8. `Solo producción` Fase 8 · Comité: presenta arquitectura, licencias (control 24), métricas y hoja de ruta de seis meses, y decide sobre el primer agente productivo con los criterios del proyecto. Cómo hacerlo seguro: piloto con un agente de bajo riesgo, políticas en solo informe al inicio, evaluación trimestral (control 25) y revisión a los 30 días.

**¿Quieres profundizar?**

- [TechLab: Entra Suite for Frontier Transformation](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) · Laboratorio

<a id="reto-agentes"></a>

## Reto del nivel

**Defensa ante el comité: el tenant listo para agentes.** Presenta el proyecto integrador [X7](#x7) como ante el comité de riesgos: inventario de agentes, arquitectura de blueprints e identidades, políticas por sujeto del token, permisos efectivos, plan de licencias (E7 frente a Agent 365 más P1 o E3), monitoreo y runbook de contención, con el estado de los 25 controles de la [tabla de preparación](00_Programa.md#preparacion-agentes) y los hallazgos del Zero Trust Assessment. Formato: diez minutos de exposición, una página de resumen ejecutivo y la decisión sobre el primer agente productivo.

<a id="quiz-agentes"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-agentes). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuándo anunció Microsoft Entra Agent ID?
   - a) 18 de noviembre de 2025
   - b) 19 de mayo de 2025
   - c) 1 de mayo de 2026
   - d) 14 de julio de 2025

2. Sin una política de acceso condicional «bloquear salvo aprobado», las solicitudes de token de un agente…
   - a) Se permiten por defecto
   - b) Se bloquean por defecto
   - c) Requieren la aprobación del sponsor
   - d) Requieren MFA del agente

3. ¿Dónde residen las credenciales de una identidad de agente?
   - a) En la identidad de agente
   - b) En la cuenta de usuario del agente
   - c) En el blueprint
   - d) En Key Vault, automáticamente

4. ¿Qué relación administrativa es obligatoria en Agent ID?
   - a) Owner
   - b) Manager
   - c) Ninguna
   - d) Sponsor

5. ¿Cuál de estos roles impide Entra asignar a una identidad de agente?
   - a) Privileged Role Administrator
   - b) Ninguno: los agentes pueden recibir cualquier rol
   - c) Solo los roles de Azure RBAC
   - d) Solo los roles personalizados

6. Un agente actúa en nombre de un usuario (OBO). ¿A qué apunta la política de acceso condicional?
   - a) A la identidad de agente
   - b) Al blueprint
   - c) A los usuarios y grupos
   - d) A la cuenta de usuario del agente

7. ¿En cuál de estos casos NO protege el acceso condicional a un agente?
   - a) Cuando actúa de forma autónoma con su identidad
   - b) Cuando accede a un recurso con una clave de API
   - c) Cuando actúa en nombre de un usuario
   - d) Cuando el tenant tiene Microsoft 365 E7

8. Al proteger un servidor MCP con Entra ID, ¿qué paso se omite con más frecuencia?
   - a) Habilitar MFA para el servidor
   - b) Crear un secreto de cliente
   - c) Configurar requestedAccessTokenVersion en 2
   - d) Desactivar el acceso condicional

9. ¿Cuándo llegó Agent 365 a disponibilidad general y a qué precio independiente?
   - a) 18 de noviembre de 2025, 30 USD por usuario
   - b) 14 de julio de 2025, incluido en E5
   - c) Enero de 2026, por agente
   - d) 1 de mayo de 2026, 15 USD por usuario al mes o incluido en E7

10. ¿Qué necesitas para ver el inventario completo de agentes en el centro de administración de Microsoft 365?
   - a) Una licencia de Agent 365
   - b) Solo el rol AI Reader o AI Administrator
   - c) Global Administrator y E7
   - d) Entra ID P2

11. ¿Qué tabla de Defender reemplazó a AIAgentsInfo?
   - a) AgentsInfo
   - b) IdentityInfo
   - c) EntraIdSignInEvents
   - d) CloudAppEvents

12. ¿Qué requiere el agente de optimización de acceso condicional?
   - a) Entra ID P2 y Microsoft 365 E7
   - b) Agent 365
   - c) Nada adicional
   - d) Entra ID P1 y SCU disponibles

13. ¿Quién puede emitir tokens con el Agent ID de un agente de Copilot Studio?
   - a) El Global Administrator
   - b) El maker que creó el agente
   - c) Cualquier Application Administrator
   - d) Nadie del tenant: lo gestiona un blueprint de Microsoft con credenciales federadas

14. En Microsoft Foundry, ¿qué permisos recibe una identidad de agente recién creada?
   - a) Contributor sobre la suscripción
   - b) Ninguno: hay que concederlos con Azure RBAC de mínimo privilegio
   - c) Los permisos de quien la creó
   - d) Los de un secreto de cliente compartido

15. ¿Qué cubre el pilar de IA del Zero Trust Workshop, guion del proyecto integrador?
   - a) Solo las licencias de Copilot
   - b) Solo la configuración de Copilot Studio
   - c) Mapear el riesgo de IA, registrar agentes, asegurar autenticación, red y datos, construir agentes seguros y detectar y responder
   - d) Solo el entrenamiento de modelos

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

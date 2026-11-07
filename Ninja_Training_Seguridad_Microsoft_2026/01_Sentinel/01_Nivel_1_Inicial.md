# Nivel 1 · Inicial · Fundamentos

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Qué es Sentinel hoy, cómo se usa, cómo desplegarlo, KQL esencial y tu laboratorio. Al terminar tendrás un entorno funcionando y la base para todo lo demás.

*L100–L200 · 7 módulos · ~37 horas · 138 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos](#p0) · [I0 Cómo aprender y soporte](#i0) · [I1 Sentinel hoy](#i1) · [I2 Cómo se usa](#i2) · [I3 Despliegue y primeros pasos](#i3) · [I4 KQL esencial](#i4) · [I5 Laboratorios](#i5)

<a id="p0"></a>

## P0 · Prerrequisitos: nube, identidad y datos

*L100 · ~6 h · Origen: Sin equivalente directo (el Ninja original asumía estos conocimientos)*

Sentinel se apoya en cuatro pilares que conviene dominar antes de empezar. El primero es **Azure**: suscripciones, grupos de recursos, control de acceso basado en roles (RBAC) e identidades administradas, porque Sentinel, sus workspaces y sus playbooks son recursos de Azure. El segundo es **Microsoft Entra ID**: usuarios, grupos, roles, registros de inicio de sesión y auditoría, que son a la vez fuente de datos crítica y el modelo de permisos de toda la plataforma.

El tercero es **Azure Monitor Logs**: el workspace de Log Analytics es el almacén de Sentinel y entender tablas, planes de tabla, retención y consultas te ahorrará muchas dudas más adelante. El cuarto es **Microsoft Defender XDR**, porque hoy Sentinel se opera desde el mismo portal y comparte incidentes, búsqueda avanzada y automatización. No necesitas ser experto: con un nivel equivalente a SC-900 y AZ-900 el resto del recorrido tendrá sentido.

**Qué vas a lograr**

- Explicar qué es una suscripción, un grupo de recursos, un rol de Azure y una identidad administrada.
- Reconocer los objetos y registros principales de Microsoft Entra ID.
- Describir qué es un workspace de Log Analytics y cómo se organizan sus tablas.
- Ubicar Defender XDR y Sentinel dentro del portafolio de seguridad de Microsoft.

> **Qué cambió.** Un workspace de Sentinel es un workspace de Log Analytics con Sentinel habilitado: todos sus datos quedan sujetos a los precios de Sentinel y cada tabla admite retención de largo plazo de hasta 12 años ([Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)).

> **Novedad.** Microsoft Entra ID incorporó las identidades de agente (Entra Agent ID), un nuevo tipo de identidad que reaparece en el nivel experto cuando gobiernes agentes de IA ([conceptos de identidad](https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts)).

> **Consejo Ninja.** Si vienes del mundo on-premises, invierte primero en Azure RBAC e identidades administradas: la mayoría de los problemas con conectores y playbooks nacen en permisos mal asignados.

**¿Tienes poco tiempo?**

- [Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900)](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/) · Credencial

### Documentación, cursos y credenciales

- [Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900)](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Certificación de fundamentos de seguridad, cumplimiento e identidad con cuatro rutas oficiales (conceptos SCI, Entra, soluciones de seguridad y Purview) que incluyen SIEM/SOAR y Sentinel a nivel conceptual.
- [Log Analytics workspace overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview) · Documentación · Oficial · Microsoft Learn. Explica qué es un workspace de Log Analytics (tablas, retención interactiva y de largo plazo hasta 12 años, acceso, transformaciones con DCR) y que el 'workspace de Sentinel' es el mismo workspace habilitado.
- [What is Microsoft Defender XDR?](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender) · Documentación · Oficial · Microsoft Learn. Visión general de Defender XDR: correlación de señales de endpoint, identidad, correo y apps en incidentes, interrupción automática de ataques, autorreparación y hunting avanzado.
- [Study guide for Exam SC-900: Microsoft Security, Compliance, and Identity Fundamentals](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-900) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Guía oficial del SC-900 con habilidades al 21-oct-2026; incluye definir SIEM y SOAR, describir detección y mitigación con Sentinel y los servicios de Defender XDR.
- [Microsoft Certified: Azure Fundamentals (AZ-900)](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/) · Credencial · Oficial · Nuevo · Microsoft Learn · 20 jul 2026. Fundamentos de nube y Azure (suscripciones, grupos de recursos, regiones, gobierno) necesarios para entender dónde vive un workspace de Sentinel y cómo se factura.
- [Overview of Log Analytics in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview) · Documentación · Oficial · Microsoft Learn. Describe la herramienta Log Analytics con sus modos Simple y KQL, el panel de tablas, consultas de ejemplo, funciones e historial.
- [What is Microsoft Entra?](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra) · Documentación · Oficial · Microsoft Learn. Presenta la familia Microsoft Entra (Entra ID, ID Protection, ID Governance, External ID, Private/Internet Access, Workload ID, Verified ID) y su integración con Security Copilot.
- [Identity and access management fundamental concepts](https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts) · Documentación · Oficial · Microsoft Learn. Conceptos básicos de IAM: identidad, autenticación vs. autorización, MFA, SSO, proveedores de identidad y tipos de identidad (humana, carga de trabajo, dispositivo y agente de IA).
- [What is extended detection and response (XDR)?](https://www.microsoft.com/en-us/security/business/security-101/what-is-xdr) · Documentación · Oficial · Microsoft Security · 6 ene 2026. Artículo divulgativo 'Security 101' que explica qué es XDR, cómo funciona y en qué se diferencia de SIEM y otras tecnologías.

**Manos a la obra**

1. `Laboratorio` Repasa la ruta de aprendizaje de SC-900 o, como mínimo, sus módulos sobre Sentinel y Defender XDR ([certificación SC-900](https://learn.microsoft.com/en-us/credentials/certifications/security-compliance-and-identity-fundamentals/)).
2. `Laboratorio` Crea una suscripción de laboratorio con la [cuenta gratuita de Azure](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) y define de inmediato una alerta de presupuesto.
3. `Laboratorio` Recorre el [tutorial de Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial): abre una tabla, filtra por tiempo y cambia entre el modo simple y el modo KQL.
4. `Laboratorio` En tu tenant de prueba, identifica qué roles de Entra ID y de Azure tienes asignados y en qué ámbito.

<a id="i0"></a>

## I0 · Cómo aprender Sentinel y dónde pedir ayuda

*L100 · ~2 h · Origen: Módulo 0 · Other learning and support options*

Antes de entrar en materia, conviene conocer las otras puertas. Este entrenamiento es extenso, pero sigue un guion y no puede profundizar en cada tema; por eso cada módulo enlaza a la documentación de referencia. Si buscas una credencial formal, el examen **SC-200: Microsoft Security Operations Analyst** cubre Sentinel junto con Defender XDR y Security Copilot; para una visión más amplia del portafolio, **SC-900** es el punto de partida, y las credenciales **Applied Skills** validan tareas concretas en un laboratorio real.

Si ya dominas el producto, lo que necesitas es mantenerte al día: la página de novedades de Sentinel, el blog de Sentinel en Tech Community y los webinars de la Microsoft Security Community son tu radar. Y si tienes un problema puntual, los foros de Tech Community y Microsoft Q&A suelen responder más rápido que cualquier curso. Este módulo reúne todas esas opciones para que elijas la combinación que mejor se adapte a tu objetivo.

**Qué vas a lograr**

- Identificar las rutas formales de aprendizaje y certificación relacionadas con Sentinel.
- Conocer los canales oficiales de soporte, comunidad y novedades.
- Armar tu propio plan de estudio combinando esta guía con Microsoft Learn.

> **Novedad.** Las habilidades medidas del examen SC-200 se actualizaron el 21 de octubre de 2026. El dominio de mayor peso es gestionar el entorno de operaciones de seguridad (40–45 %), y el temario ya incluye data lake, KQL jobs, summary rules, Sentinel graph, notebooks conectados al servidor MCP e investigación con Security Copilot ([guía de estudio SC-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200)).

> **Atención.** Las versiones traducidas del examen, como la de español, se actualizan unas ocho semanas después de la versión en inglés ([guía en español](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-200)). La credencial Applied Skills «Configure SIEM security operations using Microsoft Sentinel» se retiró el 30 de abril de 2025, aunque su ruta de aprendizaje sigue publicada ([aviso de retiro](https://techcommunity.microsoft.com/discussions/skills-hub-discussions/microsoft-applied-skills-upcoming-retirements/4397751)).

> **Qué cambió.** El registro a webinars pasó de aka.ms/SecurityWebinars a [securitycommunity.microsoft.com/VirtualEvents](https://securitycommunity.microsoft.com/VirtualEvents/), y las grabaciones se publican en el [canal de YouTube de la Microsoft Security Community](https://www.youtube.com/MicrosoftSecurityCommunity).

> **Consejo Ninja.** El Ninja oficial de Tech Community se reorganizó por roles en octubre de 2025 y mantiene su evaluación con certificado de participación al 80 % ([Become a Microsoft Sentinel Ninja](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-ninja-the-complete-level-400-training/1246310)). Úsalo como complemento: esta guía sigue el orden por niveles y agrega la expansión agéntica.

**¿Tienes poco tiempo?**

- [Microsoft Sentinel skill-up training (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/sentinel/skill-up-resources) · Documentación
- [Study guide for Exam SC-200: Microsoft Security Operations Analyst](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Credencial
- [What's new in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Certified: Security Operations Analyst Associate](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Página de la certificación asociada al SC-200 con rutas de aprendizaje oficiales, sandbox, videos de preparación, práctica en AI Skills Navigator y renovación anual gratuita.
- [Microsoft Sentinel skill-up training (Microsoft Learn)](https://learn.microsoft.com/en-us/azure/sentinel/skill-up-resources) · Documentación · Oficial · Nuevo · Ninja original · Microsoft (doc author: guywi-ms) · Microsoft Learn · 7 ago 2026. Versión en Microsoft Learn del Ninja de nivel 400: 21 módulos autoguiados (Module 0-21) en cinco partes que siguen el ciclo de vida del SOC, con docs, blogs y webinars (YouTube/MP4/presentación). *Nota:* Página 'Last updated on 08/07/2026'; añade el 'Microsoft Sentinel Training Lab' (hunting, detecciones, investigación, costos y data lake). Gran parte del contenido enlazado es 2020-2022 (Azure portal, Fusion, Basic/Archive tiers, MMA)…
- [Enhance security operations by using Microsoft Security Copilot (SC-5006)](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (6 módulos, ~6 h) sobre Security Copilot que incluye un módulo dedicado a agentes (identidades, permisos, agentes de Entra/Defender/Purview/Intune y creación de agentes propios).
- [Deploy and operate Microsoft Security Copilot (learning path)](https://learn.microsoft.com/en-us/training/paths/deploy-operate-security-copilot/) · Curso · Oficial · Microsoft Learn. Ruta de Learn (3 módulos, ~1 h 41 min) para desplegar Security Copilot: prompts, workspaces con SCU y residencia de datos, roles, gobierno de plugins y ciclo de vida de agentes Microsoft y de partners (Security Store).
- [Configure your Microsoft Sentinel environment (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-configure-azure-sentinel-environment/) · Curso · Oficial · Microsoft Learn. Ruta de aprendizaje oficial (6 módulos) que cubre introducción a Sentinel, workspaces, consultas de logs, watchlists, inteligencia de amenazas e integración con Defender XDR.
- [Train your security staff for Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Página oficial que agrupa el Ninja de Defender XDR (tres niveles con knowledge check por nivel), rutas de Learn, el learning hub del portal, entornos de prueba y simulación de ataques.
- [Microsoft Security Academy](https://microsoft.github.io/PartnerResources/skilling/microsoft-security-academy) · Curso · Oficial · Microsoft Partner Resources (GitHub Pages). Plataforma de aprendizaje con rutas y módulos sobre soluciones de seguridad de Microsoft (Sentinel, Defender, Entra, Purview) creada por equipos de seguridad de Microsoft.
- [Mitigate threats using Microsoft Security Copilot (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-mitigate-threats-using-microsoft-copilot-for-security/) · Curso · Oficial · Microsoft Learn. Ruta de Learn alineada con SC-200 (5 módulos, ~4 h 54 min) que introduce IA generativa y agentes, Security Copilot, sus funciones, experiencias embebidas y simulaciones guiadas.
- [Implement activity and event collection in Microsoft Sentinel](https://learn.microsoft.com/en-us/training/paths/implement-activity-event-collection-sentinel/) · Curso · Oficial · Microsoft Learn. Ruta de 8 módulos orientada a ingenieros de seguridad: workspace, Content hub, conectores de Microsoft, Syslog/CEF, Windows, automatización con Logic Apps y gestión de retención y auditoría.
- [Configure SIEM security operations using Microsoft Sentinel (SC-5001 learning path)](https://learn.microsoft.com/en-us/training/paths/configure-security-information-event-management-operations-using-microsoft-sentinel/) · Curso · Oficial · Microsoft Learn. Ruta práctica de 6 módulos (~4,5 h) con ejercicios para crear el workspace, instalar soluciones del Content hub, configurar reglas DCR, simular un ataque y conectar Sentinel a Defender XDR.
- [SC-200: Microsoft Security Operations Analyst](https://learn.microsoft.com/en-us/certifications/exams/sc-200) · Credencial · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 0 ('Otras opciones de aprendizaje y soporte') del skill-up de Learn: certificacion «SC-200: Microsoft Security Operations Analyst».
- [SC-900: Microsoft Security, Compliance, and Identity Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/sc-900) · Credencial · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 0 ('Otras opciones de aprendizaje y soporte') del skill-up de Learn: certificacion «SC-900: Microsoft Security, Compliance, and Identity Fundamentals».
- [Course SC-5001-A: Configure SIEM security operations using Microsoft Sentinel](https://learn.microsoft.com/en-us/training/courses/sc-5001) · Curso · Oficial · Legado aún útil · Microsoft Learn. Curso de un día (dirigido o autodidacta, disponible también en español) para configurar el workspace, desplegar soluciones del Content hub, conectar Windows y configurar analítica y automatización. *Nota:* El curso sigue listado, pero la credencial Applied Skills que lo acompañaba fue retirada el 30-abr-2025

### Anuncios y blogs oficiales

- [Microsoft Sentinel Blog](https://techcommunity.microsoft.com/category/microsoft-sentinel/blog/microsoftsentinelblog) · Blog oficial · Oficial · Nuevo · Equipo de producto de Microsoft Sentinel · Microsoft Tech Community · 30 oct 2026. Blog oficial del equipo de Sentinel con la serie mensual 'What's new' y anuncios de funciones (p. ej., Unified Data Management, acceso delegado entre tenants, 500+ conectores).
- [What's new in Microsoft Sentinel: September 2026](https://techcommunity.microsoft.com/blog/MicrosoftSentinelBlog/what%E2%80%99s-new-in-microsoft-sentinel-september-2026/4560902) · Blog oficial · Empleado de Microsoft · Nuevo · vkokkengada · Microsoft Tech Community - Microsoft Sentinel Blog · 30 sep 2026. Resumen mensual oficial: Case Management en Defender (preview pública desde el 23-sep-2026), roles personalizados URBAC para GDAP, conectores CCF multi-cuenta y más de 500 conectores de datos.
- [Microsoft Sentinel | Microsoft Community Hub](https://techcommunity.microsoft.com/category/microsoft-sentinel) · Blog oficial · Oficial · Microsoft y comunidad · Microsoft Tech Community. Hub oficial de Sentinel en Tech Community con foros de discusión (~8.500 hilos), blogs del producto, eventos e ideas.
- [Microsoft Applied Skills: Upcoming Retirements](https://techcommunity.microsoft.com/discussions/skills-hub-discussions/microsoft-applied-skills-upcoming-retirements/4397751) · Blog oficial · Empleado de Microsoft · PujaA · Microsoft Tech Community - Skills Hub · 26 mar 2025. Aviso oficial que lista credenciales Applied Skills retiradas, entre ellas 'Configure SIEM security operations using Microsoft Sentinel' (retirada el 30 de abril de 2025).
- [Microsoft Sentinel Tech Community](https://techcommunity.microsoft.com/t5/microsoft-sentinel/bd-p/MicrosoftSentinel) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 0 ('Otras opciones de aprendizaje y soporte') del skill-up de Learn: blog-oficial «Microsoft Sentinel Tech Community».

### Webinars, videos y podcasts

- [Microsoft Security Community (canal de YouTube)](https://www.youtube.com/MicrosoftSecurityCommunity) · Video · Oficial · YouTube – Microsoft Security Community. Canal oficial (~40K suscriptores, ~955 vídeos) donde se publican las grabaciones de los webinars de la comunidad, con listas por producto (Sentinel, Security Copilot, Defender XDR Virtual Ninja Show, etc.).
- [Microsoft Sentinel (playlist del canal Microsoft Security Community)](https://www.youtube.com/playlist?list=PLmAptfqzxVEUD7-w180kVApknWHJCXf0j) · Video · Oficial · Microsoft Security Community · YouTube – Microsoft Security Community. Lista de reproducción oficial de Sentinel (~149 vídeos) con los webinars 2023-2026: migración a Defender, data lake, graph, MCP, UEBA Behaviors, case management, multi-workspace y repositorios.
- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar · Oficial · Equipos de producto de Microsoft Security · YouTube – Microsoft Security Community. Serie de webinars (≈18 vídeos) de Security Copilot con Defender, Entra, Intune y Purview, agentes personalizados, 'Logic Apps vs. agentes de Security Copilot' y una sesión de un MVP sobre agentes.
- [Getting Started with Security Copilot (Security Copilot Skilling Series)](https://www.youtube.com/watch?v=g2I1rozWGVI) · Webinar · Oficial · YouTube – Microsoft Security Community. Sesión práctica sobre qué incluye Security Copilot con E5, experiencias principales y agentes de día uno para pasar del onboarding al uso real.
- [Introducing the UEBA Behaviors Layer in Microsoft Sentinel](https://www.youtube.com/watch?v=SqbxmGdMP7c) · Webinar · Oficial · Michal Shechter, Taylor Wong · YouTube – Microsoft Security Community · 17 feb 2026. Webinar sobre la nueva capa de Behaviors de UEBA que traduce telemetría cruda en comportamientos legibles, con casos de uso y demo.
- [Microsoft Sentinel graph | Unlocking Graph-based Security and Analysis](https://www.youtube.com/watch?v=U6rh0UnXZvg) · Webinar · Oficial · Sourin Paul, Shirley Kochavi · YouTube – Microsoft Security Community · 11 feb 2026. Webinar sobre hunting graph, blast radius y grafos personalizados (efímeros vs. materializados) creados desde VS Code y notebooks, con demo de gestión de acceso privilegiado.
- [Microsoft Sentinel | AI-Powered Entity Analysis in Sentinel's MCP Server](https://www.youtube.com/watch?v=adQ3Q38pPZ8) · Webinar · Oficial · Alexander Kolmann, Matt Lichtinger · YouTube – Microsoft Security Community · 27 ene 2026. Presenta el Entity Analyzer del servidor MCP de Sentinel para evaluar riesgo de entidades desde agentes de IA y su integración nativa con Logic Apps.
- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar · Oficial · Jeremy Tan, Maria de Sousa-Valadas Castano · YouTube – Microsoft Security Community · 16 dic 2025. Segunda parte de la transición a Defender: onboarding, modelos de permisos, conectores, data lake, SOC optimization, custom detections unificadas y multi-workspace/multi-tenant.
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar · Oficial · Neelam Nursee, Naomi Christis · YouTube – Microsoft Security Community · 9 dic 2025. Recorrido de un día en el SOC dentro del portal de Defender: navegación, cola unificada de incidentes, UEBA, TI, watchlists, automatización y case management.
- [Microsoft Sentinel | Hyper scale your SOC: Manage delegated access and role based scoping in Microsoft Defender (Webinar Details)](https://securitycommunity.microsoft.com/VirtualEvents/Webinar-Details/?id=19dbede2-92e9-480b-acde-02ddf7c8e431) · Webinar · Oficial · Nuevo · Microsoft Security Community · 12 may 2026. Webinar sobre RBAC unificado con scoping a nivel de fila en un Sentinel compartido y expansión de GDAP para MSSP y organizaciones multi-tenant en el portal de Defender.
- [Unlocking Security Context with Microsoft Sentinel Graph](https://www.youtube.com/watch?v=MVyHJR6TJjU) · Video · Oficial · Yaniv Shasha · YouTube – Microsoft Security Community. Explica cómo Sentinel graph convierte tablas fragmentadas en un grafo de conocimiento de seguridad y cómo extenderlo con grafos propios (empleados, activos, CVE, tickets).
- [UEBA behaviors boost: Anomalies on top of behaviors layer](https://www.youtube.com/watch?v=73XRo0U6qDQ) · Video · Oficial · Michal Shechter, Dror Cohen · YouTube – Microsoft Security Community. Introduce detección de anomalías sobre la capa de behaviors de UEBA (primera vez visto, patrones poco comunes, coincidencias de TI) para hunting proactivo.
- [Microsoft Defender Virtual Ninja Show (Microsoft Adoption)](https://adoption.microsoft.com/en-us/ninja-show/) · Video · Oficial · Microsoft Adoption. Programa en vídeo por temporadas (Temporada 16 en 2026) con episodios a demanda sobre Defender, Sentinel (data lake con Jupyter, estimador de costos) y Security Copilot.
- [Microsoft Sentinel & Defender XDR Virtual Ninja Training (Microsoft Learn Shows)](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/) · Video · Oficial · Legado aún útil · Heike Ritter (presentadora) · Microsoft Learn Shows · 5 feb 2025. Archivo en Learn (48 episodios) del Virtual Ninja Show 'basado en los blogs Ninja', con episodios como data tiering de Sentinel, migración, correlaciones y Copilot con Logic Apps. *Nota:* Último episodio en Learn: 5-feb-2025; los episodios nuevos (temporadas 15-16, 2026) están en adoption.microsoft.com y YouTube

### Laboratorios, GitHub y herramientas

- [Microsoft Sentinel Training Lab (Azure/Azure-Sentinel)](https://github.com/Azure/Azure-Sentinel/tree/master/Tools/Microsoft-Sentinel-Training-Lab) · Laboratorio · Oficial · Ninja original · GitHub – Azure/Azure-Sentinel. Laboratorio oficial de bajo costo (~10 MB de datos pregrabados) con onboarding a Defender y 17 ejercicios: hunting, MDTI, detecciones, costos, data lake (KQL jobs), MCP, federación y custom graph. *Nota:* Enlazado desde el Module 0 del skill-up de Learn (2026). Requiere workspace en el portal de Defender; recomienda activar Sentinel data lake. Mapa: -> I5
- [Microsoft Q&A - Microsoft Security | Microsoft Sentinel](https://learn.microsoft.com/en-us/answers/tags/817/microsoft-security-microsoft-sentinel?nocomments=true&answerfilter=all) · Herramienta · Oficial · Comunidad y moderadores de Microsoft · Microsoft Q&A. Foro oficial de preguntas y respuestas de Microsoft con la etiqueta de Sentinel (~1.460 preguntas) moderado por personal de Microsoft y MVPs.

### Comunidad: blogs, libros, newsletters y eventos

- [Webinars | Microsoft Security Community (Upcoming Virtual Events)](https://securitycommunity.microsoft.com/VirtualEvents/) · Evento · Oficial · Microsoft Security Community. Portal actual de webinars de la Microsoft Security Community donde se listan y registran los eventos virtuales por producto (motor de los webinars que alimentan los Ninja).
- [Which Microsoft community is right for me? (copia sindicada)](https://thewindowsupdate.com/2023/03/02/which-microsoft-community-is-right-for-me/) · Blog · Empleado de Microsoft · Legado aún útil · Kristina Quick · TheWindowsUpdate.com (republicación de Tech Community) · 2 mar 2023. Explica las comunidades públicas (webinars, grabaciones, Ninja y certificados vía aka.ms/SecurityCommunity) y privadas bajo NDA (roadmaps, private previews, badges vía aka.ms/joinccp) de Microsoft Security. *Nota:* Original en Tech Community, republicado y actualizado 23-ene-2026 ('Learn more about Microsoft Security Communities'). En 2026 el programa privado se presenta como 'Security Advisors Program'
- [SC-200 Security Operations Analyst Study Guide with KQL Practice](https://www.epifive.com/blog/sc-200-study-guide-security-operations-analyst) · Blog · Comunidad · Nuevo · EpiFive · 25 oct 2026. Guía de terceros con plan de estudio de cuatro semanas, laboratorios y consultas KQL alineados con las habilidades del SC-200 del 21-oct-2026.

**Manos a la obra**

1. `Laboratorio` Lee la [guía de estudio de SC-200](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) y marca, por cada habilidad medida, el módulo de esta guía que la cubre.
2. `Laboratorio` Suscríbete a los [eventos virtuales de la Security Community](https://securitycommunity.microsoft.com/VirtualEvents/) y al blog de Sentinel en Tech Community.
3. `Laboratorio` Agenda el knowledge check del [Ninja oficial](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-ninja-the-complete-level-400-training/1246310) para cuando termines el nivel intermedio.

**¿Quieres profundizar?**

- [Which Microsoft community is right for me? (copia sindicada)](https://thewindowsupdate.com/2023/03/02/which-microsoft-community-is-right-for-me/) · Blog
- [Webinars | Microsoft Security Community (Upcoming Virtual Events)](https://securitycommunity.microsoft.com/VirtualEvents/) · Evento
- [Microsoft Security Community (canal de YouTube)](https://www.youtube.com/MicrosoftSecurityCommunity) · Video
- [Microsoft Sentinel (playlist del canal Microsoft Security Community)](https://www.youtube.com/playlist?list=PLmAptfqzxVEUD7-w180kVApknWHJCXf0j) · Video

<a id="i1"></a>

## I1 · Qué es Microsoft Sentinel hoy

*L100 · ~3 h · Origen: Módulo 1 · Get started with Microsoft Sentinel*

Microsoft Sentinel es el SIEM nativo en la nube de Microsoft: recolecta datos a escala de todo tu entorno —nube, centros de datos, SaaS, OT—, detecta amenazas con analítica y machine learning, permite investigar y cazar de forma proactiva y orquesta la respuesta con automatización. Lo que cambió en los últimos años es **dónde y cómo se usa**: Sentinel se integró al portal de Microsoft Defender junto con Defender XDR, Exposure Management, la inteligencia de amenazas y Security Copilot, en lo que Microsoft llama la plataforma unificada de operaciones de seguridad. Incidentes, búsqueda avanzada y automatización son ahora comunes a SIEM y XDR.

En 2025 llegó un segundo salto: el **data lake** de Sentinel separa el almacenamiento económico de largo plazo de la capa de analítica, **Sentinel graph** modela relaciones entre entidades y el **servidor MCP** abre los datos a agentes de IA. Este módulo te da la foto completa antes de entrar en detalle: qué hace cada pieza, cómo se factura y qué implica la transición desde el portal de Azure.

**Qué vas a lograr**

- Describir las capacidades de Sentinel: recolección, detección, investigación, búsqueda y respuesta.
- Explicar qué es la plataforma unificada de operaciones de seguridad en el portal de Defender.
- Conocer el calendario de transición desde el portal de Azure.
- Entender los modelos de facturación y los beneficios de datos incluidos en licencias de Microsoft 365.

> **Novedad.** Después del **31 de marzo de 2027**, Sentinel deja de estar soportado en el portal de Azure y queda solo en el portal de Defender. La fecha original era el 1 de julio de 2026 y se extendió el 29 de enero de 2026 ([anuncio de la nueva fecha](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464)). Algunas páginas, como la de buenas prácticas, todavía mencionan julio de 2026: prevalece el anuncio más reciente.

> **Novedad.** Desde julio de 2025, los clientes nuevos (primer workspace del tenant, con rol Owner o User Access Administrator y sin delegación por Lighthouse) se incorporan automáticamente al portal de Defender. Usar Sentinel en Defender no requiere Defender XDR ni licencias E5 y no tiene costo adicional ([Sentinel en el portal de Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal)).

> **Novedad.** El data lake de Sentinel llegó a disponibilidad general el 30 de septiembre de 2025; ese día entraron en vista previa Sentinel graph y el servidor MCP ([anuncio de GA](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342)). Desde el 23 de septiembre de 2026, el onboarding del SIEM y del data lake es uno solo ([novedades de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

> **Atención.** Precios en una línea: la prueba gratuita cubre 10 GB/día en el nivel de analítica durante 31 días (hasta 20 workspaces por tenant; no cubre automatización ni cargos del data lake) y los niveles de compromiso arrancan en 100 GB/día ([facturación](https://learn.microsoft.com/en-us/azure/sentinel/billing)). Los clientes de Microsoft 365 E5, E7, A5, F5 y G5 reciben hasta 5 MB por usuario por día de ingesta de datos de Microsoft 365 elegibles ([oferta](https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/)). Verifica siempre la [página de precios](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/), que publica promociones con fecha de vencimiento.

> **Novedad.** Integrated SOC (ISOC) en Microsoft Defender, en vista previa, ofrece capacidades SIEM a clientes con Defender Suite, Microsoft 365 E5 o E7 que todavía no tienen un workspace de Sentinel, con 30 días de retención para datos de Defender ([ISOC](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview)).

**¿Tienes poco tiempo?**

- [Microsoft Sentinel in the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal) · Documentación
- [UPDATE: New timeline for transitioning Sentinel experience to Defender portal](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) · Blog oficial
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar

### Documentación, cursos y credenciales

- [What is Microsoft Sentinel?](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-overview) · Documentación · Oficial · Microsoft Learn. Presenta Sentinel como SIEM nativo de nube y plataforma de seguridad para la defensa agéntica: SIEM + data lake + graph + servidor MCP + experiencia de desarrollador (Security Store).
- [Microsoft Sentinel documentation](https://learn.microsoft.com/en-us/azure/sentinel/) · Documentación · Oficial · Microsoft Learn. Página raíz de la documentación oficial de Sentinel con accesos a overview, quickstart, guía de despliegue, data lake, operaciones unificadas, conectores, detección e investigación.
- [Transition your Microsoft Sentinel environment to the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender) · Documentación · Oficial · Microsoft Learn. Guía oficial paso a paso para pasar de Sentinel en el portal de Azure al portal de Defender: planificación, permisos, diferencias de almacenamiento/privacidad, configuración y operación.
- [Microsoft Sentinel benefit for Microsoft 365 E7, E5, A5, F5, and G5 customers](https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/) · Documentación · Oficial · Microsoft Azure. Detalla la concesión de hasta 5 MB por usuario/día de ingesta gratuita de datos de Microsoft 365 (Entra ID, MDCA, MIP, hunting avanzado de M365) para clientes E7/E5/A5/F5/G5 y sus variantes Security.
- [Microsoft Sentinel Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) · Documentación · Oficial · Microsoft Security. Página oficial de precios con niveles de análisis (PAYG y compromisos), medidores del data lake y del graph, nivel promocional de 50 GB y el beneficio de hasta 5 MB/usuario/día de ingesta gratuita.
- [Microsoft Defender XDR in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-portal) · Documentación · Oficial · Microsoft Learn. Describe el portal de Defender (security.microsoft.com) que reúne incidentes, hunting, acciones y análisis de amenazas, y reitera que Sentinel funciona allí con o sin Defender XDR o E5 y que tras el 31-mar-2027 solo estará disponible en ese portal.
- [Integrated Security Operations Center (ISOC) in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/isoc-overview) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 23 sep 2026. Describe ISOC en Defender (preview): capacidades SIEM listas para usar en el portal de Defender para clientes con Defender Suite, M365 E5 o E7 sin workspace de Sentinel activo, con 30 días de retención incluidos para datos de Defender. *Nota:* Case management, workbooks y generación de playbooks no requieren workspace; UEBA, Content hub, CI/CD, TI y datos de terceros requieren un 'ISOC workspace'. No desconectar un workspace productivo de Sentinel para calificar

### Anuncios y blogs oficiales

- [Microsoft Sentinel data lake is now generally available](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342) · Blog oficial · Empleado de Microsoft · vkokkengada · Microsoft Tech Community - Microsoft Security Community Blog · 30 sep 2025. Anuncia la disponibilidad general del data lake de Sentinel y presenta casos de uso (investigaciones de largo plazo, líneas base de comportamiento, enriquecimiento, hunting retrospectivo).
- [Empowering defenders in the era of agentic AI with Microsoft Sentinel](https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 30 sep 2025. Anuncio ejecutivo de Sentinel como plataforma agéntica: GA del data lake y vista previa pública de Sentinel graph y del servidor MCP, más el constructor de agentes sin código de Security Copilot.
- [Become a Microsoft Defender XDR Ninja](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/become-a-microsoft-defender-ninja/1789376?wdOrigin=OFFICECOM-WEB.APPBAR) · Blog oficial · Oficial · Ninja original · Heike Ritter · Microsoft Tech Community – Microsoft Defender XDR Blog · 19 oct 2020. Ninja de Defender XDR (antes Microsoft 365 Defender) en tres niveles —Fundamentals (9 módulos), Intermediate (6) y Expert (3)— con leyenda de tipos de enlace, knowledge check tras cada nivel y certificado 'divertido' no oficial. *Nota:* Publicado 19-oct-2020; banner 'July 2024: updated' incluye la plataforma unificada; la etiqueta 'ninja training' muestra actividad/actualización 19-oct-2026. Short links: aka.ms/DefenderXDRNinja y aka.ms/m365dninja. El fetch devolvió sólo el título…
- [What's new in Microsoft Sentinel: June 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-june-2026/4531902) · Blog oficial · Empleado de Microsoft · Nuevo · TomerBrand · Microsoft Tech Community - Microsoft Sentinel Blog · 30 jun 2026. Resumen mensual que anuncia la serie de seis blogs sobre la transición de Sentinel al portal de Defender, ampliaciones de ASIM y herramientas de grafo en el servidor MCP.
- [Microsoft Sentinel data lake: Unify signals, cut costs, and power agentic AI](https://www.microsoft.com/en-us/security/blog/2025/07/22/microsoft-sentinel-data-lake-unify-signals-cut-costs-and-power-agentic-ai/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Scott Woodgate; Krishna Kumar Parthasarathy · Microsoft Security Blog · 22 jul 2025. Presenta el data lake de Sentinel en vista previa pública y anuncia la convergencia de las capacidades de MDTI en Defender XDR y Sentinel sin costo adicional. *Nota:* Anuncio de preview (jul-2025); el lake es GA desde sep-2025. Fuente oficial del cambio de licenciamiento de MDTI (desde oct-2025 reportes, perfiles e IoC en Defender XDR). Ver M4
- [Planning your move to Microsoft Defender portal for all Microsoft Sentinel customers](https://techcommunity.microsoft.com/blog/microsoft-security-blog/planning-your-move-to-microsoft-defender-portal-for-all-microsoft-sentinel-custo/4428613) · Blog oficial · Empleado de Microsoft · Legado aún útil · TomerBrand · Microsoft Tech Community - Microsoft Security Community Blog · 1 jul 2025. Anuncio original (jul-2025) de la estrategia de operaciones unificadas y del plan para retirar la experiencia de Sentinel en el portal de Azure, con beneficios del portal de Defender. *Nota:* Fijaba el 1-jul-2026 como fecha de retiro; esa fecha fue reemplazada por el 31-mar-2027 en el anuncio del 29-ene-2026. Útil para contexto histórico y motivos del cambio
- [Azure Sentinel achieves a Leader placement in Forrester Wave, with top ranking in Strategy](https://www.microsoft.com/security/blog/2020/12/01/azure-sentinel-achieves-a-leader-placement-in-forrester-wave-with-top-ranking-in-strategy/) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Security Blog. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: blog-oficial «Azure Sentinel achieves a Leader placement in Forrester Wave, with top ranking in Strategy».

### Webinars, videos y podcasts

- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar · Oficial · Jeremy Tan, Maria de Sousa-Valadas Castano · YouTube – Microsoft Security Community · 16 dic 2025. Segunda parte de la transición a Defender: onboarding, modelos de permisos, conectores, data lake, SOC optimization, custom detections unificadas y multi-workspace/multi-tenant.
- [Accelerating Defense with Microsoft Security Solutions](https://www.youtube.com/watch?v=dSODQy9bWjU) · Video · Empleado de Microsoft · Nuevo · John Savill · John Savill's Technical Training (YouTube) · nov 2026. Panorama reciente de las soluciones de seguridad de Microsoft con IA, incluyendo Project Perception y Defender ISOC.
- [New data lake in Microsoft Sentinel (Microsoft Mechanics)](https://www.youtube.com/watch?v=4CUK-eJBNI0) · Video · Empleado de Microsoft · Vandana Mahtani · Microsoft Mechanics (YouTube). Demo de ~9 minutos del data lake de Sentinel: gestión de tablas, niveles analytics/data lake, exploración, hunting avanzado, jobs programados y notebooks para ML.
- [Empowering the Modern SOC (Microsoft Sentinel and Microsoft Defender XDR)](https://www.youtube.com/watch?v=bSFcBfHmr1o) · Webinar · Empleado de Microsoft · Benji Kovacevic, Javier Soriano · Microsoft Security Community (YouTube) · 2 dic 2025. Panorama de la experiencia unificada SIEM+XDR para detectar, responder y cazar, con demos del data lake y del grafo de Sentinel y agentes de Security Copilot.
- [Latest Ignite presentation on Microsoft Sentinel](https://www.youtube.com/watch?v=kGctnb4ddAE) · Video · Oficial · Legado aún útil · Ninja original · YouTube. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: video «Latest Ignite presentation on Microsoft Sentinel».
- [Microsoft Sentinel overview webinar](https://youtu.be/7An7BB-CcQI) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube. Material enlazado en el Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: webinar «Microsoft Sentinel overview webinar» ofrecido en YouTube, MP4, presentation.
- [Insight's Microsoft Sentinel setup and configuration video](https://www.youtube.com/watch?v=Cyd16wVwxZc) · Video · Oficial · Legado aún útil · Ninja original · YouTube. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: video «Insight's Microsoft Sentinel setup and configuration video».
- [Functionality and Usage of Microsoft Sentinel - AZ-900 Certification Course](https://www.youtube.com/watch?v=xaqiPXL6tz0) · Video · Empleado de Microsoft · Legado aún útil · John Savill · John Savill's Technical Training (YouTube). Explicación breve y clara de qué es Sentinel y para qué sirve, dentro del curso AZ-900. *Nota:* Grabado hace ~4 años con la experiencia del portal de Azure; útil solo para conceptos básicos

### Comunidad: blogs, libros, newsletters y eventos

- [Proactive phishing with Azure Sentinel, part 1 (Stuart Gregg, ASOS)](https://medium.com/@stuart.gregg/proactive-phishing-with-azure-sentinel-part-1-b570fff3113) · Blog · Comunidad · Legado aún útil · Ninja original · Medium. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: blog-comunidad «Blog post from the Microsoft Sentinel experience, focusing on hunting».

**Manos a la obra**

1. `Laboratorio` Lee [Sentinel en el portal de Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal) y anota cinco diferencias con la experiencia del portal de Azure.
2. `Laboratorio` Con la [página de precios](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) y el artículo de [facturación](https://learn.microsoft.com/en-us/azure/sentinel/billing), estima el costo mensual de un escenario de 50 GB/día con el beneficio de Microsoft 365 E5 y las fuentes gratuitas.
3. `Laboratorio` Explica en un párrafo, como si fuera para un CISO, qué aportan el data lake, el graph y el servidor MCP.

**¿Quieres profundizar?**

- [Accelerating Defense with Microsoft Security Solutions](https://www.youtube.com/watch?v=dSODQy9bWjU) · Video
- [New data lake in Microsoft Sentinel (Microsoft Mechanics)](https://www.youtube.com/watch?v=4CUK-eJBNI0) · Video
- [Empowering the Modern SOC (Microsoft Sentinel and Microsoft Defender XDR)](https://www.youtube.com/watch?v=bSFcBfHmr1o) · Webinar
- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar

<a id="i2"></a>

## I2 · Cómo se usa Microsoft Sentinel

*L100 · ~2 h · Origen: Módulo 2 · How is Microsoft Sentinel used?*

Muchas organizaciones usan Sentinel como su SIEM principal, y la mayor parte de este curso parte de ese escenario. Pero no es el único. Sentinel se combina con Defender XDR y Defender for Cloud como **SIEM + XDR** para cubrir identidades, endpoints, correo, aplicaciones y nube con un mismo flujo de incidentes; se usa para **monitorear entornos multinube**, donde la nube suele estar menos vigilada que los sistemas tradicionales; convive **lado a lado con otro SIEM** durante una migración o de forma permanente; y es la base de servicios gestionados de **proveedores MSSP**, gracias a que no requiere infraestructura propia.

Conocer estos patrones —y lo que otras organizaciones y los analistas de la industria dicen de ellos— te ayuda a tomar mejores decisiones de arquitectura desde el primer día y a explicar el valor de la plataforma a tu organización o a tus clientes.

**Qué vas a lograr**

- Distinguir los escenarios de uso: SIEM principal, SIEM + XDR, multinube, lado a lado y MSSP.
- Conocer casos públicos de clientes y el reconocimiento de analistas de la industria.
- Identificar los patrones de integración con ITSM y con otros SIEM.

> **Consejo Ninja.** Para operar lado a lado con otro SIEM, Microsoft recomienda enviar las alertas del SIEM existente a Sentinel y no duplicar logs entre ambos, lo que duplica costos ([despliegue lado a lado](https://learn.microsoft.com/en-us/azure/sentinel/deploy-side-by-side)).

> **Novedad.** Microsoft fue reconocido como Líder en el Gartner Magic Quadrant de SIEM en 2024 y 2025 ([anuncio 2025](https://www.microsoft.com/en-us/security/blog/2025/10/16/microsoft-named-a-leader-in-the-2025-gartner-magic-quadrant-for-siem/)) y en The Forrester Wave: Security Analytics Platforms, Q2 2025 ([anuncio](https://www.microsoft.com/en-us/security/blog/2025/06/24/microsoft-is-named-a-leader-in-the-forrester-wave-security-analytics-platforms-2025/)). Al 6 de noviembre de 2026 no se encontró un Magic Quadrant de SIEM 2026 publicado.

> **Consejo Ninja.** Para proveedores de servicios, Microsoft publica una guía de implementación del modelo MSSP en el portal de Defender: multi-inquilino, distribución de contenido y operación diaria ([guía MSSP](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security)).

**¿Tienes poco tiempo?**

- [Microsoft Defender portal implementation guide for Managed Security Service Providers (MSSPs)](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Defender portal implementation guide for Managed Security Service Providers (MSSPs)](https://learn.microsoft.com/en-us/defender-xdr/playbook-managed-security) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Guía oficial para MSSP en el portal de Defender: preparar el entorno y la delegación multitenant, gestionar contenido una vez y distribuirlo, y operar incidentes y hunting entre clientes.
- [Microsoft Defender XDR integration with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Documentación · Oficial · Microsoft Learn. Explica cómo SIEM (Sentinel) y XDR (Defender) se integran: cola de incidentes única, sincronización bidireccional, correlación y recolección de eventos de hunting avanzado.
- [Manage multiple tenants in Microsoft Sentinel as an MSSP](https://learn.microsoft.com/en-us/azure/sentinel/multiple-tenants-service-providers) · Documentación · Oficial · Legado aún útil · Nuevo · Microsoft Learn · 8 ago 2026. Explica cómo un MSSP gestiona workspaces de clientes con Azure Lighthouse y remite a la guía del portal de Defender para MSSP. *Nota:* Incluye aviso de retiro del Azure portal (31-mar-2027) y que no se pueden desplegar conectores desde un workspace gestionado solo con Lighthouse: también se requiere GDAP
- [The Azure Security compass](https://aka.ms/azuresecuritycompass) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft (aka.ms). Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: doc «The Azure Security compass».
- [The cloud is (still) new and often not monitored as extensively as on-premises workloads. Read this to learn how Microsoft Sentinel can help](https://techcommunity.microsoft.com/gxcuf89792/attachments/gxcuf89792/AzureSentinelBlog/243/1/L400-P2%20Use%20cases.pdf) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Material enlazado en el Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: recurso «The cloud is (still) new and often not monitored as extensively as on-premises workloads. Read this to learn how Microsoft Sentinel can help» ofrecido en presentation. *Nota:* Grabación/archivo heredado (2020-2023): verificar vigencia de UI (Azure portal -> Defender portal)
- [Microsoft Sentinel Technical Playbooks for MSSPs](https://aka.ms/azsentinelmssp) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft (aka.ms). Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: doc «Microsoft Sentinel Technical Playbooks for MSSPs».

### Anuncios y blogs oficiales

- [Microsoft named a Leader in the 2025 Gartner Magic Quadrant for SIEM](https://www.microsoft.com/en-us/security/blog/2025/10/16/microsoft-named-a-leader-in-the-2025-gartner-magic-quadrant-for-siem/) · Blog oficial · Empleado de Microsoft · Rob Lefferts · Microsoft Security Blog · 16 oct 2025. Anuncio oficial de Microsoft como Líder en el Gartner Magic Quadrant de SIEM 2025 y resumen de capacidades (data lake, graph, MCP, SOC optimization, UEBA, SOAR).
- [Microsoft is named a Leader in The Forrester Wave: Security Analytics Platforms, 2025](https://www.microsoft.com/en-us/security/blog/2025/06/24/microsoft-is-named-a-leader-in-the-forrester-wave-security-analytics-platforms-2025/) · Blog oficial · Empleado de Microsoft · Rob Lefferts · Microsoft Security Blog · 24 jun 2025. Anuncio de Microsoft como Líder en The Forrester Wave: Security Analytics Platforms, Q2 2025, con puntuación máxima en nueve criterios.
- [Pacífico Seguros implementa Microsoft Copilot for Security con un enfoque Zero Trust y XDR](https://www.microsoft.com/es-co/customers/story/1761512190744606726-pacifico-microsoft-365-insurance-en-peru) · Blog oficial · Oficial · Legado aún útil · ES · Microsoft Customer Stories. Caso de una aseguradora peruana (grupo Credicorp) que adoptó una plataforma unificada Zero Trust/XDR con Sentinel para visibilidad y respuesta, junto con el partner TC1 Labs. *Nota:* Caso de la región MCSA en español; usa el nombre antiguo 'Copilot for Security' (hoy Microsoft Security Copilot)
- [OMV cuts incident resolution time in half, unifies security with Microsoft Sentinel](https://www.microsoft.com/en/customers/story/25951-omv-aktiengesellschaft-microsoft-sentinel/) · Blog oficial · Oficial · Microsoft Customer Stories. Caso de migración desde un SIEM on-premises a Sentinel + Defender XDR con automatización vía Logic Apps, reduciendo el MTTR a la mitad y procesando 5 TB/día.
- [AVEVA achieves secure SaaS migration goals and cuts security costs with Microsoft Sentinel SIEM](https://www.microsoft.com/en/customers/story/25198-aveva-microsoft-sentinel) · Blog oficial · Oficial · Microsoft Customer Stories. Migración 'like-for-like' desde otro SIEM a Sentinel con el MSSP BlueVoyant, consolidando herramientas y evitando costos.
- [Cielo speeds threat detection and response with Microsoft Defender XDR and Microsoft Sentinel](https://www.microsoft.com/en/customers/story/1765090070873727497-cielo-sa-microsoft-defender-for-office-365-p1-banking-and-capital-markets-en-brazil) · Blog oficial · Oficial · Microsoft Customer Stories. Empresa de pagos latinoamericana que consolidó su seguridad en Defender XDR + Sentinel + Intune, reduciendo costos, complejidad y tiempos de respuesta.
- [Our comprehensive SIEM+XDR solution combining Microsoft Sentinel and Microsoft Defender XDR](https://techcommunity.microsoft.com/t5/azure-sentinel/whats-new-azure-sentinel-and-microsoft-365-defender-incident/ba-p/2191090) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «Our comprehensive SIEM+XDR solution combining Microsoft Sentinel and Microsoft Defender XDR».
- [Read and watch how such a setup helps detect and respond to a WebShell attack: or](https://techcommunity.microsoft.com/t5/azure-sentinel/analysing-web-shell-attacks-with-azure-defender-data-in-azure/ba-p/1724130) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Material enlazado en el Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: recurso «Read and watch how such a setup helps detect and respond to a WebShell attack: or» ofrecido en blog, video demo.
- [Sending alerts enriched with supporting events from Microsoft Sentinel to third-party SIEMs](https://techcommunity.microsoft.com/t5/azure-sentinel/sending-alerts-enriched-with-supporting-events-from-azure/ba-p/1456976) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «Sending alerts enriched with supporting events from Microsoft Sentinel to third-party SIEMs».
- [Send data and notable events from Splunk to Microsoft Sentinel](https://techcommunity.microsoft.com/t5/azure-sentinel/how-to-export-data-from-splunk-to-azure-sentinel/ba-p/1891237) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «Send data and notable events from Splunk to Microsoft Sentinel».
- [Send QRadar offenses to Microsoft Sentinel](https://techcommunity.microsoft.com/t5/azure-sentinel/migrating-qradar-offenses-to-azure-sentinel/ba-p/2102043) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «Send QRadar offenses to Microsoft Sentinel».
- [List of MISA (Microsoft Intelligent Security Association) member-managed security service providers (MSSPs) that use Microsoft Sentinel](https://www.microsoft.com/security/blog/2020/07/14/microsoft-intelligent-security-association-managed-security-service-providers/) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Security Blog. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «List of MISA (Microsoft Intelligent Security Association) member-managed security service providers (MSSPs) that use Microsoft Sentinel».
- [Microsoft is again named a Leader in the 2024 Gartner Magic Quadrant for Security Information and Event Management](https://www.microsoft.com/en-us/security/blog/2024/05/13/microsoft-is-again-named-a-leader-in-the-2024-gartner-magic-quadrant-for-security-information-and-event-management/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Rob Lefferts · Microsoft Security Blog · 13 may 2024. Anuncio de Microsoft como Líder en el Gartner MQ de SIEM 2024, junto con el lanzamiento de la plataforma unificada de operaciones de seguridad y la herramienta de migración desde Splunk. *Nota:* Usa el nombre antiguo 'Copilot for Security' (hoy Microsoft Security Copilot). Cifras de ROI citadas provienen de estudio encargado por Microsoft

### Webinars, videos y podcasts

- [OT and IOT attack detection, investigation, and response.](https://youtu.be/S8DlZmzYO2s) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: webinar «OT and IOT attack detection, investigation, and response.“».
- [Best practices for converting detection rules – migration webinar](https://youtu.be/njXK1h9lfR4) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube · 19 feb 2021. Material enlazado en el Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: webinar «Best practices for converting detection rules – migration webinar» ofrecido en YouTube, MP4, presentation.

**Manos a la obra**

1. `Laboratorio` Dibuja la arquitectura actual de tu organización o de un cliente y marca qué patrón aplica: SIEM principal, SIEM + XDR, multinube, lado a lado o MSSP.
2. `Laboratorio` Si conviven dos SIEM, define el flujo de alertas recomendado y los criterios para dar por terminada la convivencia ([lado a lado](https://learn.microsoft.com/en-us/azure/sentinel/deploy-side-by-side)).

<a id="i3"></a>

## I3 · Despliegue y primeros pasos

*L200 · ~6 h · Origen: Módulo 1 (onboarding) y "Next steps" del skill-up de Learn*

Desplegar Sentinel es rápido; desplegarlo bien requiere decisiones. Necesitas un workspace de Log Analytics con los permisos adecuados, el onboarding de Sentinel al portal de Defender y una primera ola de conectores que entregue valor inmediato: **Defender XDR, Microsoft Entra ID, la actividad de Azure y Microsoft 365**. Desde el **Content hub** instalas soluciones empaquetadas —conectores, reglas, libros, consultas y playbooks— y activas tus primeras reglas de analítica a partir de plantillas.

Este módulo sigue el orden recomendado por Microsoft: prerrequisitos, onboarding, conectores iniciales, contenido, roles y permisos, y una lista de verificación de buenas prácticas. Al terminarlo tendrás un entorno funcionando y generando tus primeros incidentes.

**Qué vas a lograr**

- Completar los prerrequisitos y el onboarding de Sentinel al portal de Defender.
- Conectar las fuentes de Microsoft que aportan más valor inicial.
- Instalar soluciones del Content hub y activar reglas a partir de plantillas.
- Asignar roles de Sentinel y de Defender con el principio de mínimo privilegio.

> **Novedad.** El quickstart oficial (actualizado en julio de 2026) recorre el flujo completo: crear el workspace, habilitar Sentinel, entrar desde el portal de Defender, instalar la solución Azure Activity desde el Content hub, configurar el conector con Azure Policy, habilitar una regla de plantilla y consultar `AzureActivity` en la búsqueda avanzada ([quickstart](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard)).

> **Atención.** Para conectar un workspace al portal de Defender necesitas al menos Security Administrator en Entra ID y Owner sobre la suscripción (o User Access Administrator más Microsoft Sentinel Contributor). La ruta es Sistema > Configuración > Microsoft Sentinel > Conectar un workspace ([onboarding a Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)).

> **Atención.** El conector de Defender XDR se habilita automáticamente al incorporar Sentinel a Defender. Al conectarlo, los conectores individuales de cada producto Defender se desconectan en segundo plano y cambia el esquema de alertas: revisa reglas y libros que dependan de él ([conector Defender XDR](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender)). Los registros de inicio de sesión de Entra ID requieren licencia P1 o P2 ([conector Entra ID](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory)).

> **Consejo Ninja.** Asignación típica: analistas con Microsoft Sentinel Responder más Playbook Operator; ingenieros con Microsoft Sentinel Contributor más Logic App Contributor. El data lake usa roles de Entra ID, no de Azure ([roles y permisos](https://learn.microsoft.com/en-us/azure/sentinel/roles)). El RBAC unificado de Defender ya admite Sentinel, pero no las entidades de servicio ([URBAC](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac)).

> **Qué cambió.** Para reglas nuevas, Microsoft recomienda hoy las detecciones personalizadas (custom detections) del portal de Defender; las reglas de analítica existentes siguen funcionando ([detección de amenazas](https://learn.microsoft.com/en-us/azure/sentinel/threat-detection)). Lo verás en detalle en el módulo M7.

**¿Tienes poco tiempo?**

- [Onboarding documentation](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · Documentación
- [Connect Microsoft Sentinel to the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) · Documentación
- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar

### Documentación, cursos y credenciales

- [Connect Microsoft Sentinel to the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Procedimiento y permisos para conectar un workspace de Sentinel al portal de Defender (workspace primario y secundarios), explorar funciones y desconectar.
- [Stream data from Microsoft Defender XDR to Microsoft Sentinel in the Azure portal](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Configura el conector Defender XDR (incidentes y alertas, entidades de AD vía MDI y eventos de hunting avanzado) y cómo verificar la ingesta con SecurityIncident.
- [Deployment guide for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/deploy-overview) · Documentación · Oficial · Microsoft Learn. Guía de despliegue en tres fases (planificar y preparar, desplegar, ajustar y revisar) con una lista de verificación posterior al despliegue.
- [Microsoft Defender unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac) · Documentación · Oficial · Microsoft Learn. Explica el modelo URBAC del portal de Defender, que ya admite Sentinel para workspaces incorporados: las asignaciones se sincronizan con Azure RBAC y URBAC pasa a ser la fuente de permisos al activarse.
- [Discover and manage Microsoft Sentinel out-of-the-box content (Content hub)](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-deploy) · Documentación · Oficial · Microsoft Learn. Cómo buscar, instalar, actualizar en lote y habilitar el contenido de soluciones del Content hub desde el portal de Defender (Microsoft Sentinel > Content management > Content hub).
- [Send Microsoft Entra ID data to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory) · Documentación · Oficial · Microsoft Learn. Conector de Microsoft Entra ID: tipos de logs (SigninLogs, AuditLogs, no interactivos, service principals, Graph activity, riesgos) y requisitos de licencia y permisos.
- [Threat detection in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/threat-detection) · Documentación · Oficial · Microsoft Learn. Tipos de reglas de análisis (programadas, NRT, anomalías, seguridad de Microsoft, TI, Fusion, ML) y la recomendación de partir de plantillas del Content hub.
- [Pre-deployment activities and prerequisites for deploying Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/prerequisites) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Pre-deployment activities and prerequisites for deploying Microsoft Sentinel».
- [Microsoft Certified: Security Operations Analyst Associate](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/?practice-assessment-type=certification) · Credencial · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: certificacion «Microsoft Certified: Security Operations Analyst Associate».
- [SC-200 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/practice/assessment?assessment-type=practice&assessmentId=59&practice-assessment-type=certification) · Credencial · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: certificacion «Practice Assessment».
- [What's new in Microsoft Defender unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/defender-xdr/whats-new-in-microsoft-defender-urbac) · Documentación · Oficial · Microsoft Learn. Historial de cambios de URBAC, incluido que desde julio de 2025 los permisos del data lake de Sentinel se gestionan con URBAC (preview).

### Webinars, videos y podcasts

- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar · Oficial · Neelam Nursee, Naomi Christis · YouTube – Microsoft Security Community · 9 dic 2025. Recorrido de un día en el SOC dentro del portal de Defender: navegación, cola unificada de incidentes, UEBA, TI, watchlists, automatización y case management.

### Laboratorios, GitHub y herramientas

- [Microsoft Sentinel All-in-One (v2)](https://github.com/Azure/Azure-Sentinel/tree/master/Tools/Sentinel-All-In-One) · Herramienta · Empleado de Microsoft · Legado aún útil · Javier Soriano y colaboradores · GitHub - Azure/Azure-Sentinel. Plantilla ARM que automatiza crear el workspace, habilitar Sentinel, retención, UEBA, salud, soluciones del Content hub, conectores y reglas de análisis en pocos clics. *Nota:* Sin cambios funcionales relevantes en ~3 años (solo actualización de enlaces en 2026); usa nombres antiguos (Azure AD, Microsoft 365 Defender) y no contempla incorporación al portal de Defender ni data lake. Útil para laboratorios rápidos
- [Tutorial: Detect threats by using analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-log4j-detection) · Laboratorio · Oficial · Legado aún útil · Microsoft Learn. Tutorial para crear una regla programada desde plantilla (Log4j), revisar la lógica KQL, mapear entidades, configurar incidentes y respuestas automáticas. *Nota:* Pasos escritos para el portal de Azure; el concepto aplica igual en Defender, donde además se recomiendan custom detections

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft exam sandbox (demo experience)](https://go.microsoft.com/fwlink/?linkid=2226877) · Blog · Oficial · Legado aún útil · Ninja original · go.microsoft.com. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: blog-comunidad «EXAM SANDBOX».

**Manos a la obra**

1. `Laboratorio` Sigue el [quickstart](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) completo con la solución Azure Activity hasta ver tu primera consulta en la búsqueda avanzada.
2. `Laboratorio` Conecta el workspace al portal de Defender como workspace principal ([onboarding](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)) y verifica que el conector de Defender XDR quedó activo.
3. `Laboratorio` Instala la solución de Microsoft Entra ID desde el Content hub y habilita los registros de auditoría (y de inicio de sesión si tienes P1 o P2).
4. `Laboratorio` Activa cinco reglas de plantilla relevantes para tus conectores y revisa cómo cambia la cobertura en la página de MITRE ATT&CK.
5. `Laboratorio` Asigna roles por grupos: Responder para analistas y Contributor para ingenieros, siguiendo [roles y permisos](https://learn.microsoft.com/en-us/azure/sentinel/roles).
6. `Laboratorio` Recorre la [guía de despliegue](https://learn.microsoft.com/en-us/azure/sentinel/deploy-overview) y su lista de verificación posterior.

**¿Quieres profundizar?**

- [Microsoft Sentinel All-in-One (v2)](https://github.com/Azure/Azure-Sentinel/tree/master/Tools/Sentinel-All-In-One) · Herramienta
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar
- [Tutorial: Detect threats by using analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-log4j-detection) · Laboratorio

<a id="i4"></a>

## I4 · KQL esencial

*L200 · ~10 h · Origen: Módulo 10 · Kusto Query Language (primera parte)*

KQL (Kusto Query Language) es la lengua franca de Sentinel: lo usas para explorar registros, escribir reglas de detección, cazar amenazas, construir libros y, cada vez más, para darles herramientas a los agentes de IA. La buena noticia es que su lógica de tubería —tabla, filtro, proyección, agregación— se aprende rápido y se lee casi como una oración.

Este módulo te lleva de cero a escribir consultas útiles sobre datos de seguridad: filtrar con `where`, elegir columnas con `project`, contar y agrupar con `summarize`, ordenar, unir tablas con `join` y visualizar con `render`. Las técnicas de optimización, funciones, series temporales y grafos llegan en el nivel avanzado. La recomendación Ninja de siempre sigue vigente: escribe consultas todos los días, aunque sean pequeñas.

**Qué vas a lograr**

- Escribir consultas KQL con where, project, extend, summarize, order by y join.
- Usar entornos gratuitos para practicar sin costo.
- Leer y adaptar consultas de detección y búsqueda publicadas por Microsoft y la comunidad.

> **Qué cambió.** Con Sentinel en el portal de Defender, las consultas se escriben en la búsqueda avanzada (Advanced hunting), que reemplaza a la vista Logs del portal de Azure para el trabajo diario ([recursos para aprender KQL](https://learn.microsoft.com/en-us/kusto/query/kql-learning-resources?view=microsoft-fabric)).

> **Consejo Ninja.** Practica gratis: el clúster gratuito de Azure Data Explorer no requiere suscripción ni tarjeta ([empezar gratis](https://learn.microsoft.com/en-us/azure/data-explorer/start-for-free)), y el entorno de demostración de Log Analytics trae datos reales de ejemplo ([tutorial](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial)), aunque en octubre de 2026 la comunidad reportó problemas intermitentes de acceso.

> **Consejo Ninja.** Para aprender jugando, [Kusto Detective Agency](https://detective.kusto.io/) propone casos policiales que se resuelven con KQL; su tercera temporada comenzó en junio de 2025.

**¿Tienes poco tiempo?**

- [Write your first query with Kusto Query Language](https://learn.microsoft.com/en-us/training/modules/write-first-query-kusto-query-language/) · Curso
- [KQL quick reference](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference?view=microsoft-fabric) · Documentación
- [Must Learn KQL (GitHub repository)](https://github.com/rod-trent/MustLearnKQL) · GitHub

### Documentación, cursos y credenciales

- [Learning module (SC-200 part 4)](https://learn.microsoft.com/en-us/training/paths/sc-200-utilize-kql-for-azure-sentinel/) · Curso · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: curso «Learning module (SC-200 part 4)».
- [Kusto Query Language (KQL) overview](https://learn.microsoft.com/en-us/kusto/query/?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Introducción oficial a KQL (consultas de solo lectura, sentencias tabulares, let y set, operadores encadenados con '|') con una sección específica sobre por qué KQL es central en Sentinel.
- [KQL quick reference](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn. Tabla de referencia rápida de operadores y funciones KQL agrupados por tarea (filtrar, fechas, columnas, ordenar/agregar, formatear).
- [Write your first query with Kusto Query Language](https://learn.microsoft.com/en-us/training/modules/write-first-query-kusto-query-language/) · Curso · Oficial · Microsoft Learn. Módulo de 39 minutos, nivel principiante, con ejercicios prácticos de take, project, where, count y sort sobre datos de ejemplo.
- [Blu Raven Academy](https://academy.bluraven.io/) · Curso · MVP · Mehmet Ergene · Blu Raven. Academia de Mehmet Ergene con cursos de KQL, threat hunting e ingeniería de detección para tecnologías de seguridad Microsoft.
- [Kusto Query Language learning resources](https://learn.microsoft.com/en-us/kusto/query/kql-learning-resources?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn · 16 sep 2025. Página oficial que reúne recursos para aprender KQL: entorno demo de Log Analytics, tutoriales, Kusto Detective Agency, Must Learn KQL y la ruta SC-200 de KQL.
- [SQL to Kusto Query Language cheat sheet](https://learn.microsoft.com/en-us/kusto/query/sql-cheat-sheet?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn · 28 may 2025. Equivalencias SQL→KQL (SELECT, WHERE, GROUP BY, JOIN, UNION, TOP, HAVING) y el truco '-- explain' para traducir SQL a KQL en ADX.
- [Kusto Query Language (KQL)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: doc «Kusto Query Language (KQL)».
- [Query optimization best practices](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/query-optimization) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: doc «Query optimization best practices».
- [Kusto Query Language (KQL) from Scratch (Pluralsight)](https://www.pluralsight.com/courses/kusto-query-language-kql-from-scratch) · Curso · Comunidad · Legado aún útil · Ninja original · Pluralsight. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: curso «Pluralsight KQL course».
- [Must Learn KQL (Rod Trent)](https://aka.ms/MustLearnKQL) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft (aka.ms). Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: doc «Must Learn KQL».
- [Pluralsight advanced KQL course](https://www.pluralsight.com/courses/microsoft-azure-data-explorer-advanced-query-capabilities) · Curso · Comunidad · Legado aún útil · Ninja original · Pluralsight. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: curso «Pluralsight advanced KQL course».

### Webinars, videos y podcasts

- [Call of the Cyber Duty (Kusto Detective Agency Season 3 launch video)](https://www.youtube.com/watch?v=9wfmneYa3qg) · Video · Oficial · Azure Data Explorer team · Azure Data Explorer (YouTube) · jun 2025. Video de lanzamiento de la temporada 3 del Kusto Detective Agency, un thriller de ciberespionaje que se resuelve con KQL.

### Laboratorios, GitHub y herramientas

- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta · Comunidad · Nuevo · Ugur Koc y comunidad · kqlsearch.com · nov 2026. Buscador comunitario de consultas KQL para Sentinel, Defender y Azure Monitor, filtrable por tabla y autor, con aportes actualizados de la comunidad.
- [Tutorial: Use Log Analytics (Log Analytics demo environment)](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial) · Laboratorio · Oficial · Microsoft Learn. Tutorial guiado de Log Analytics usando el entorno demo con datos de ejemplo: esquema, consultas, filtros, gráficos y exportación.
- [Kusto Detective Agency](https://detective.kusto.io/) · Herramienta · Oficial · Microsoft (Azure Data Explorer team). Juego gamificado oficial para aprender KQL resolviendo casos de investigación de datos en la ciudad ficticia de Digitown.
- [Must Learn KQL (GitHub repository)](https://github.com/rod-trent/MustLearnKQL) · GitHub · Empleado de Microsoft · Legado aún útil · Rod Trent · GitHub - rod-trent · 14 mar 2025. Serie gratuita de 21 partes para aprender KQL desde cero orientada a Sentinel, con eBook, consultas, datasets, workshop, app y certificado de finalización por evaluación. *Nota:* Partes 1-20 publicadas en 2021-2022 y parte 21 en mar-2025; repo con commits recientes. Las capturas usan el portal de Azure/Log Analytics; en Defender se practica en Advanced hunting. Existe libro 'Advanced Must Learn KQL'
- [Create a free Azure Data Explorer cluster](https://learn.microsoft.com/en-us/azure/data-explorer/start-for-free-web-ui) · Laboratorio · Oficial · Nuevo · Microsoft Learn · 23 jul 2026. Paso a paso para crear el clúster gratuito de ADX desde la interfaz web, crear base de datos, ingerir datos y ejecutar consultas.
- [What is a free Azure Data Explorer cluster?](https://learn.microsoft.com/en-us/azure/data-explorer/start-for-free) · Herramienta · Oficial · Nuevo · Microsoft Learn · 11 jun 2026. Explica el clúster gratuito de Azure Data Explorer (sin suscripción ni tarjeta) con ~100 GB de almacenamiento, ideal para practicar KQL y para el Kusto Detective Agency.
- [definitive-guide-kql (companion GitHub repo)](https://github.com/KQLMSPress/definitive-guide-kql/) · GitHub · Empleado de Microsoft · Mark Morowczynski; Rod Trent; Matthew Zorich · GitHub - KQLMSPress. Repositorio abierto con todas las consultas y datos de ejemplo del libro, organizados por capítulo y con consultas aportadas por empleados de Microsoft.
- [Jupyter notebooks version](https://github.com/jjsantanna/azure_sentinel_learn_kql_lab/blob/master/azure_sentinel_learn_kql_lab.ipynb) · GitHub · Comunidad · Legado aún útil · Ninja original · GitHub. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: github «Jupyter notebooks version».

### Comunidad: blogs, libros, newsletters y eventos

- [The Definitive Guide to KQL: Using Kusto Query Language for operations, defending, and threat hunting](https://www.microsoftpressstore.com/store/definitive-guide-to-kql-using-kusto-query-language-9780138293383) · Libro · Empleado de Microsoft · Mark Morowczynski; Rod Trent; Matthew Zorich · Microsoft Press · 14 may 2024. Libro de 480 páginas de Microsoft Press que cubre KQL desde fundamentos hasta casos avanzados de ciberseguridad, hunting y operaciones.
- [KQL Sources - 2025 Update](https://kqlquery.com/posts/kql-sources-2025/) · Blog · Comunidad · Bert-Jan Pals · kqlquery.com · 2 ene 2025. Lista anual curada de fuentes y repositorios comunitarios de KQL para seguridad (kqlsearch, newsletter Kusto Insights, Definitive Guide to KQL y decenas de repos de detecciones) útil para seguir aprendiendo tras los fundamentos.
- [The KQL cheat sheet (mbsecure.nl)](https://www.mbsecure.nl/blog/2019/12/kql-cheat-sheet) · Blog · Comunidad · Legado aún útil · Ninja original · mbsecure.nl. Enlace del Módulo 10 ('Kusto Query Language') del skill-up de Learn: blog-comunidad «The KQL Cheat Sheet».
- [Kusto Detective Agency (serie de soluciones comentadas)](https://straightforwardsql.com/series/kusto-detective-agency/) · Blog · Comunidad · Legado aún útil · straightforwardsql.com. Serie de soluciones explicadas de los casos de Kusto Detective Agency para aprender técnicas de KQL paso a paso. *Nota:* Contiene spoilers; autor y fecha no verificados
- [KQL Security Sources (kqlquery.com)](https://kqlquery.com/posts/kql_sources/) · Blog · Comunidad · Legado aún útil · Bert-Jan Pals · kqlquery.com · 7 sep 2023. Recopilación de las principales fuentes comunitarias de KQL de seguridad (kqlsearch, repositorio Azure-Sentinel, Sentinel-Queries, FalconFriday, etc.). *Nota:* El autor publica actualizaciones anuales (p. ej., 'KQL Sources: 2026 Update' en la categoría Sentinel del sitio)

**Manos a la obra**

1. `Laboratorio` Escribe cinco consultas sobre `SigninLogs` o `AzureActivity`: fallos por aplicación, IP distintas por usuario, operaciones por hora, top 10 de llamadores y una visualización con `render timechart`.
2. `Laboratorio` Traduce tres consultas SQL que conozcas con la [hoja de equivalencias SQL a KQL](https://learn.microsoft.com/en-us/kusto/query/sql-cheat-sheet?view=microsoft-fabric).
3. `Laboratorio` Resuelve al menos un caso de [Kusto Detective Agency](https://detective.kusto.io/).
4. `Laboratorio` Toma una regla de plantilla, lee su consulta línea por línea y explica qué detecta.

**¿Quieres profundizar?**

- [The Definitive Guide to KQL: Using Kusto Query Language for operations, defending, and threat hunting](https://www.microsoftpressstore.com/store/definitive-guide-to-kql-using-kusto-query-language-9780138293383) · Libro
- [definitive-guide-kql (companion GitHub repo)](https://github.com/KQLMSPress/definitive-guide-kql/) · GitHub
- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta
- [Tutorial: Use Log Analytics (Log Analytics demo environment)](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial) · Laboratorio

<a id="i5"></a>

## I5 · Laboratorios de práctica

*L200 · ~8 h · Origen: Laboratorios del skill-up (KQL Lab, Training Lab) y SC-200*

El Ninja siempre fue práctico: leer no alcanza. Antes de pasar al nivel intermedio, arma tu laboratorio. La solución **Microsoft Sentinel Training Lab** del Content hub carga datos y contenido de ejemplo para practicar sin conectar fuentes reales; los laboratorios oficiales del curso **SC-200** en GitHub recorren paso a paso las tareas del examen; y series comunitarias proponen ejercicios progresivos para analistas.

Cuida los costos desde el primer día: usa la prueba gratuita, define alertas de presupuesto en Azure, desactiva lo que no uses y elimina el grupo de recursos cuando termines. Un laboratorio barato y desechable es la mejor inversión de esta ruta.

**Qué vas a lograr**

- Desplegar un entorno de práctica con datos de ejemplo.
- Completar los laboratorios guiados de SC-200 relacionados con Sentinel.
- Controlar el costo del laboratorio con presupuestos y limpieza de recursos.

> **Novedad.** El nuevo Microsoft Sentinel Training Lab carga unos 10 MB de datos pregrabados y propone 17 ejercicios (hunting, inteligencia de amenazas, MITRE, automatización, costos, niveles de tablas, data lake, MCP, transformaciones y grafos personalizados). Requiere un workspace incorporado al portal de Defender como principal ([Training Lab en GitHub](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/README.md)).

> **Novedad.** Los laboratorios del curso SC-200 ya están en su versión para el portal de Defender ([laboratorios SC-200](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/)).

> **Atención.** SimuLand, el proyecto de Microsoft para simular ataques en laboratorio, fue archivado el 26 de octubre de 2026: sigue siendo consultable, pero ya no recibe mantenimiento ([Azure/SimuLand](https://github.com/Azure/SimuLand)).

**¿Tienes poco tiempo?**

- [Kusto Detective Agency](https://detective.kusto.io/) · Herramienta

### Laboratorios, GitHub y herramientas

- [Kusto Detective Agency](https://detective.kusto.io/) · Herramienta · Oficial · Microsoft (Azure Data Explorer team). Juego gamificado oficial para aprender KQL resolviendo casos de investigación de datos en la ciudad ficticia de Digitown.
- [Azure account: pay as you go or Azure free account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) · Herramienta · Oficial · Microsoft Azure. Opciones de cuenta de Azure: la cuenta gratuita ofrece 200 USD de crédito por 30 días, servicios gratuitos 12 meses y protección de gasto.
- [Microsoft Sentinel Training Lab (Tools/Microsoft-Sentinel-Training-Lab)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/README.md) · Laboratorio · Oficial · Microsoft Sentinel team · GitHub - Azure/Azure-Sentinel. Laboratorio oficial renovado que despliega un workspace con ~10 MB de datos pregrabados y 17 ejercicios (hunting, TI, MITRE, automatización, costos, niveles de tablas, data lake, MCP, federación, transformaciones y grafos personalizados).
- [SC-200T00A Microsoft Security Operations Analyst - Online Hosted Instructions (labs)](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/) · Laboratorio · Oficial · Microsoft Learning · MicrosoftLearning (GitHub Pages). Índice HTML de los laboratorios oficiales del curso SC-200: Defender XDR, Security Copilot, Purview, MDE, KQL, despliegue de Sentinel en Defender, conectores, playbooks, detecciones, UEBA, ASIM, workbooks, repositorios, hunting y notebooks.
- [MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst (GitHub)](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · GitHub · Oficial · Nuevo · Microsoft Learning · GitHub - MicrosoftLearning · ago 2026. Repositorio fuente de los labs SC-200 (instrucciones, scripts KQL en Allfiles y demos VTD, incluidos data lake, incidentes y SOC optimization en Defender).
- [Microsoft Sentinel SOC 101 (GitHub)](https://github.com/rod-trent/Sentinel-SOC-101) · GitHub · Empleado de Microsoft · Legado aún útil · Rod Trent · GitHub - rod-trent · feb 2024. Serie con eBook y consultas KQL para detectar y mitigar ataques comunes con Sentinel (fuerza bruta, phishing, malware, robo de tokens, cuentas inactivas, etc.). *Nota:* Publicada entre sep-2023 y feb-2024; las consultas siguen siendo válidas, pero la navegación y nombres de tablas/portal pueden haber cambiado
- [Azure-Sentinel-Training-Lab (Solutions/Training, versión anterior)](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Training/Azure-Sentinel-Training-Lab) · Laboratorio · Oficial · Legado aún útil · Microsoft Sentinel team · GitHub - Azure/Azure-Sentinel. Ubicación original de la solución 'Training Lab' del Content hub con ejercicios guiados de Sentinel sobre datos pregrabados. *Nota:* Diseñada para la experiencia del portal de Azure; preferir la versión renovada en Tools/Microsoft-Sentinel-Training-Lab orientada al portal de Defender

**Manos a la obra**

1. `Laboratorio` Despliega el [Training Lab](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/README.md) y completa los primeros cuatro ejercicios.
2. `Laboratorio` Completa los [laboratorios de SC-200](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/) de KQL, despliegue, conectores, detecciones y hunting.
3. `Laboratorio` Configura un presupuesto con alerta al 50 % y al 80 %, y al terminar elimina el grupo de recursos del laboratorio.

**¿Quieres profundizar?**

- [Microsoft Sentinel SOC 101 (GitHub)](https://github.com/rod-trent/Sentinel-SOC-101) · GitHub
- [Azure account: pay as you go or Azure free account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) · Herramienta
- [Microsoft Sentinel Training Lab (Tools/Microsoft-Sentinel-Training-Lab)](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/README.md) · Laboratorio
- [SC-200T00A Microsoft Security Operations Analyst - Online Hosted Instructions (labs)](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/) · Laboratorio

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primer SOC en un día.** En tu laboratorio, incorpora el workspace al portal de Defender, conecta Microsoft Entra ID, la actividad de Azure y Defender XDR, y activa cinco reglas de plantilla. Provoca un incidente controlado (por ejemplo, varios inicios de sesión fallidos con una cuenta de prueba), investígalo y entrega un informe de una página con la línea de tiempo y las consultas KQL que usaste.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿A partir de qué fecha Microsoft Sentinel deja de estar soportado en el portal de Azure?
   - a) 1 de julio de 2025
   - b) 1 de julio de 2026
   - c) 31 de marzo de 2027
   - d) 31 de diciembre de 2027

2. ¿Qué se requiere para usar Microsoft Sentinel en el portal de Defender?
   - a) Licencia Microsoft 365 E5 obligatoria
   - b) Tener Defender XDR desplegado
   - c) Un workspace con Sentinel habilitado y los roles adecuados
   - d) Una licencia de Security Copilot

3. ¿Qué incluye la prueba gratuita de Sentinel?
   - a) 5 GB/día durante 30 días
   - b) 10 GB/día en el nivel de analítica durante 31 días
   - c) 100 GB/día durante 14 días
   - d) Ingesta ilimitada durante 90 días

4. ¿Cuál es el beneficio de ingesta para clientes de Microsoft 365 E5, E7, A5, F5 y G5?
   - a) 5 GB por usuario al mes
   - b) Hasta 5 MB por usuario por día de datos de Microsoft 365 elegibles
   - c) 10 GB por día por tenant
   - d) No existe beneficio

5. Un analista debe asignarse incidentes y cambiar su estado, pero no crear reglas. ¿Qué rol mínimo necesita?
   - a) Microsoft Sentinel Reader
   - b) Microsoft Sentinel Responder
   - c) Microsoft Sentinel Contributor
   - d) Owner

6. ¿Qué rol se necesita para instalar o actualizar soluciones del Content hub?
   - a) Sentinel Reader en el workspace
   - b) Sentinel Responder en la suscripción
   - c) Sentinel Contributor en el grupo de recursos
   - d) Logic App Contributor

7. Al incorporar un workspace de Sentinel al portal de Defender, el conector de Microsoft Defender XDR…
   - a) Debe configurarse siempre de forma manual
   - b) Se habilita automáticamente
   - c) No está soportado
   - d) Requiere un playbook de Logic Apps

8. ¿Qué operador de KQL filtra filas según una condición?
   - a) project
   - b) summarize
   - c) where
   - d) extend

9. ¿Cuál es el equivalente en KQL de GROUP BY en SQL?
   - a) summarize … by
   - b) join
   - c) distinct
   - d) top

10. ¿Cuándo alcanzó disponibilidad general el data lake de Microsoft Sentinel?
   - a) 22 de julio de 2025
   - b) 30 de septiembre de 2025
   - c) 29 de enero de 2026
   - d) 31 de marzo de 2027

11. En las habilidades del SC-200 vigentes desde el 21 de octubre de 2026, ¿qué dominio tiene mayor peso?
   - a) Realizar búsqueda de amenazas
   - b) Responder a incidentes de seguridad
   - c) Gestionar un entorno de operaciones de seguridad
   - d) Todos pesan igual

12. ¿Qué requisito tiene el nuevo Microsoft Sentinel Training Lab?
   - a) Un clúster dedicado de 500 GB/día
   - b) Un workspace incorporado al portal de Defender como principal
   - c) Una licencia de Security Copilot
   - d) Un tenant de proveedor CSP

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

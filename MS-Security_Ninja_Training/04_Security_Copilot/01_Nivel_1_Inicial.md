# Nivel 1 · Inicial · Fundamentos

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Qué es Security Copilot hoy, cómo se licencia y dimensiona, cómo se usa en la experiencia independiente y embebida y cómo escribir buenos prompts. Terminas con un laboratorio de costo controlado y tus tres primeros casos de uso documentados.

*L100–L200 · 8 módulos · ~31 horas · 71 recursos*

**Módulos de este nivel:** [P0 Prerrequisitos de IA](#p0) · [I0 Cómo aprender](#i0) · [I1 Qué es hoy](#i1) · [I2 Licencias y capacidad](#i2) · [I3 Experiencia independiente](#i3) · [I4 Experiencias embebidas](#i4) · [I5 Prompting para seguridad](#i5) · [I6 Laboratorio y primeros usos](#i6)

<a id="p0"></a>

## P0 · Prerrequisitos: IA generativa, agentes y seguridad

*L100–L200 · ~3 h · Origen: Ninja oficial de 2024, parte 1 (módulo extra de IA generativa e ingeniería de prompts)*

Antes de abrir Security Copilot conviene entender qué hay detrás. Un **modelo de lenguaje grande (LLM)** predice texto a partir de un prompt; no «sabe» lo que pasa en tu tenant. Security Copilot le agrega lo que le falta: un **orquestador** que interpreta tu pedido, elige plugins y herramientas, trae datos de seguridad con tus permisos (**grounding**) y recién entonces llama al modelo. Los modelos de Azure OpenAI que usa el producto no se entrenan con los datos de tu organización: el contexto llega en el momento de la consulta.

Un **agente** va un paso más allá: recibe un objetivo, usa herramientas, se dispara solo (por horario o por evento), recuerda lo que le enseñaste y trabaja con una identidad y permisos propios. Eso abre riesgos nuevos que todo el equipo debe reconocer: la **inyección de prompts** directa o escondida en los datos que el agente lee (XPIA), la **agencia excesiva** de un agente con demasiados permisos, el **consumo no acotado** —que en Security Copilot se traduce en unidades de cómputo (SCU)— y la **sobreconfianza** en salidas que parecen correctas y no lo son.

En 2026 Microsoft separa dos ideas que verás en todo el programa: Security Copilot es la **IA que asiste** (chat, experiencias embebidas, promptbooks y agentes de tarea) y Project Perception, la **IA que actúa** (un sistema multiagente supervisado). Con este vocabulario común, el SOC, riesgo, privacidad y la dirección pueden discutir agentes sin malentendidos.

**Por qué importa**

Un equipo que no entiende cómo funciona un LLM cae en uno de dos extremos: confía en cualquier respuesta o descarta la herramienta al primer error. Nivelar fundamentos reduce el riesgo de ejecutar un KQL inválido o un veredicto mal fundado, acelera la incorporación de analistas nuevos y crea un lenguaje común para evaluar riesgos de agentes con privacidad, auditoría y la dirección.

**Qué vas a lograr**

- Explicar qué es un LLM, un prompt y el grounding, y por qué un modelo puede alucinar.
- Distinguir un asistente de IA de un agente: herramientas, disparadores, memoria, identidad y autonomía.
- Relacionar la inyección de prompts, la agencia excesiva y el consumo no acotado con escenarios del SOC.
- Describir cómo Security Copilot obtiene contexto de seguridad sin entrenar los modelos con tus datos.

> **Novedad.** La Application card de Security Copilot —que reemplazó a la Responsible AI FAQ; última actualización del 22 de junio de 2026— explica que el producto usa modelos de Azure OpenAI servidos mediante Foundry Models, que esos modelos no se entrenan con los datos del cliente y que el contexto de seguridad llega por plugins y grounding en el momento de la consulta ([Application card](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card)).

> **Atención.** La misma ficha advierte del riesgo de sobreconfianza: un KQL o un script generados pueden parecer válidos y no serlo. Trata cada salida como un borrador que una persona valida antes de actuar; los filtros de contenido detectan jailbreak e inyección indirecta de prompts, pero no reemplazan la revisión ([Application card](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card)).

> **Consejo Ninja.** Usa el OWASP Top 10 for LLM Applications 2025 como marco neutral para hablar de riesgos con auditoría: LLM01 (inyección de prompts), LLM06 (agencia excesiva) y LLM10 (consumo no acotado, que en Security Copilot se traduce en SCU) son los que más aparecen en el SOC ([OWASP](https://genai.owasp.org/llm-top-10/)).

> **Qué cambió.** Desde 2026 Microsoft distingue entre la «IA que asiste» (Security Copilot) y la «IA que actúa» (Project Perception), y aclara que funcionan juntas ([Project Perception](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system)).

**¿Tienes poco tiempo?**

- [Introduction to generative AI and agents](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) · Curso
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) · Documentación
- [Application card: Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card) · Documentación

### Documentación, cursos y credenciales

- [Introduction to generative AI and agents](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) · Curso · Oficial · Microsoft Learn. Módulo de 37 minutos sobre LLM, prompts y agentes con un ejercicio práctico, primer módulo de la ruta SC-5006.
- [AI concepts for developers and technology professionals](https://learn.microsoft.com/en-us/training/paths/ai-concepts/) · Curso · Oficial · Microsoft Learn. Ruta de 3 h 51 min sobre conceptos de IA (IA generativa y agentes, PLN, visión, extracción y RAG) que prepara para el examen AI-901.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) · Documentación · Comunidad · OWASP · OWASP Gen AI Security Project · 18 nov 2024. Los 10 riesgos principales de aplicaciones con LLM (inyección de prompts, divulgación de datos sensibles, agencia excesiva, consumo no acotado, etc.) con mitigaciones.

### Webinars, videos y podcasts

- [What is Microsoft Copilot Security? (Flight School, Part 1 of 11)](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/what-is-microsoft-copilot-for-security) · Video · Empleado de Microsoft · Legado aún útil · Ryan Munsch · Microsoft Learn Shows · 23 sep 2024. Introducción de 11 minutos a la IA generativa y los LLM, sus límites en dominios especializados como la seguridad y los principios de IA responsable aplicados a Security Copilot. *Nota:* Usa el nombre antiguo 'Copilot for Security'

### Comunidad: blogs, libros, newsletters y eventos

- [Michalis Michalos – blog (Testing Microsoft Defender for Office 365's Prompt-Injection Protection, oct-2026)](https://www.michalos.net/author/cyb3rmik3/) · Blog · Empleado de Microsoft · Nuevo · Michalis Michalos · michalos.net · 8 oct 2026. Página de autor con su evaluación práctica de la detección de inyección de prompts en correos dirigidos a asistentes de IA y otros artículos de KQL y auditoría.
- [Configure AI agent runtime protection (preview) with Microsoft Defender for Endpoint](https://jeffreyappel.nl/configure-ai-agent-runtime-protection-preview-with-microsoft-defender-for-endpoint/) · Blog · MVP · Vista previa · Nuevo · Jeffrey Appel · jeffreyappel.nl · 22 jun 2026. Explica la inyección de prompts en agentes y cómo Defender inspecciona prompts, llamadas a herramientas y respuestas mediante hooks o inspección de red. *Nota:* Contexto de seguridad de agentes; profundizar en X3

**Manos a la obra**

1. `Laboratorio` Completa el módulo [Introduction to generative AI and agents](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) (37 min) de la ruta SC-5006, incluido su ejercicio. Evidencia: captura del módulo completado y un glosario propio de 15 términos (LLM, token, grounding, alucinación, agente, herramienta, disparador, memoria, orquestador y XPIA, entre otros).
2. `Laboratorio` Arma una tabla de riesgos aplicada al SOC con el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/): para LLM01, LLM06 y LLM10 describe un escenario concreto con Security Copilot o un agente (por ejemplo, un correo reportado con instrucciones ocultas o un playbook que llama a Copilot en cada incidente) y el control que lo mitiga. Evidencia: tabla revisada por un par.
3. `Laboratorio` Lee la sección de limitaciones y mitigaciones de la [Application card](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card) y lista tres situaciones del SOC en las que la salida debe verificarse siempre antes de actuar (KQL generado, análisis de un script, veredicto de un agente). Evidencia: lista con la mitigación que propone Microsoft para cada una.
4. `Laboratorio` Mira el [primer episodio de Flight School](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/what-is-microsoft-copilot-for-security) y la [página de Project Perception](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system), y escribe un párrafo que explique a un analista nuevo la diferencia entre la IA que asiste y la IA que actúa. Evidencia: párrafo publicado en la wiki del equipo.

**¿Quieres profundizar?**

- [What is Microsoft Copilot Security? (Flight School, Part 1 of 11)](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/what-is-microsoft-copilot-for-security) · Video

<a id="i0"></a>

## I0 · Cómo aprender Security Copilot y dónde pedir ayuda

*L100–L200 · ~2 h · Origen: Ninja oficial de 2024, parte 1, módulo 0 (otras opciones de aprendizaje y soporte)*

Este programa es extenso, pero no está solo. El **Ninja oficial de Security Copilot** (Tech Community, abril de 2024, versión 4.0 de noviembre de 2024) sigue siendo útil para fundamentos, plugins y Logic Apps, y su knowledge check permite pedir un certificado de participación con 80 %. Microsoft Learn ofrece la ruta **SC-5006** (seis módulos, unas seis horas, con simulaciones guiadas que no requieren tenant), el curso **SC-5006-A** de un día —también en español— y la ruta intermedia **Deploy and operate Microsoft Security Copilot**. Ninguna otorga certificación; el examen **SC-200** sí incluye la investigación con Security Copilot.

Para mantenerte al día, las fuentes vivas son el blog de Security Copilot en Tech Community, la **Security Copilot Skilling Series** (webinars técnicos desde octubre de 2025), el hub de adopción con videos y talleres, el repositorio **Azure/Security-Copilot** en GitHub y, si tu organización participa, el **Customer Connection Program**, con vistas previas privadas y capacitaciones semanales. La página «What's new» de Learn ayuda, pero al corte de esta guía su última entrada era de abril de 2026.

**Por qué importa**

Security Copilot cambia casi cada mes: nombres, estados de vista previa, licencias y agentes. Saber qué fuente es oficial, cuál está desactualizada y quién explica bien cada tema evita decisiones basadas en documentación vieja —por ejemplo, creer que los plugins solo se gestionan por usuario— y le da a cada persona del equipo una ruta de aprendizaje medible.

**Qué vas a lograr**

- Identificar las rutas formales (Ninja oficial, SC-5006, Deploy and operate y SC-200) y qué evalúa cada una.
- Reconocer qué partes del Ninja de 2024 siguen vigentes y cuáles quedaron superadas.
- Usar los canales oficiales de novedades, comunidad y soporte, incluido el Customer Connection Program.
- Armar un plan de estudio personal que combine esta guía con Microsoft Learn.

> **Atención.** El Ninja oficial se publicó el 15 de abril de 2024 y su última versión visible es la 4.0, del 19 de noviembre de 2024: conserva el nombre de lanzamiento del producto y afirma que los plugins solo se gestionan por usuario, algo superado por la gestión por organización y por workspace, en disponibilidad general desde junio de 2025 ([Ninja oficial](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928), [What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)).

> **Novedad.** La ruta SC-5006 reúne seis módulos (6 h 12 min): IA generativa y agentes, qué es Security Copilot, sus funciones principales, experiencias embebidas, agentes y simulaciones guiadas. El curso SC-5006-A dura un día y está disponible en español; ninguno otorga certificación y no se encontró una credencial Applied Skills específica de Security Copilot ([SC-5006](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/), [curso SC-5006-A](https://learn.microsoft.com/en-us/training/courses/sc-5006)).

> **Consejo Ninja.** El Customer Connection Program da acceso a vistas previas privadas, capacitaciones técnicas semanales gratuitas y una comunidad en Teams; la participación es voluntaria y la gestiona tu organización ([qué es Security Copilot](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot)).

> **Atención.** La página «What's new» de Learn dice actualizarse cada mes, pero al 6 de noviembre de 2026 su última entrada visible es de abril de 2026. Compleméntala con el blog de Security Copilot, la Skilling Series y las novedades mensuales de Microsoft Security (ver [C3](05_Comunidad.md#c3)).

**¿Tienes poco tiempo?**

- [Enhance security operations by using Microsoft Security Copilot (SC-5006)](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/) · Curso
- [Microsoft Security Copilot – Microsoft Adoption (adoption hub)](https://adoption.microsoft.com/en-us/security-copilot/) · Herramienta
- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar

### Documentación, cursos y credenciales

- [Deploy and operate Microsoft Security Copilot (learning path)](https://learn.microsoft.com/en-us/training/paths/deploy-operate-security-copilot/) · Curso · Oficial · Microsoft Learn. Ruta intermedia de 1 h 41 min y 3 módulos: describir Security Copilot, configurar workspaces (SCU, residencia de datos, roles, plugins, asignación a agentes, monitoreo) y gestionar plugins y agentes (Microsoft y Security Store).
- [Enhance security operations by using Microsoft Security Copilot (SC-5006)](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/) · Curso · Oficial · Microsoft Learn. Ruta oficial de 6 h 12 min con 6 módulos: IA generativa y agentes, qué es Security Copilot, funciones principales, experiencias embebidas, agentes y simulaciones guiadas interactivas.
- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación · Oficial · Microsoft Learn · 17 abr 2026. Registro mensual oficial de novedades (agentes, inclusión E5, workspaces, overage, auditoría de agentes en Purview, GPT-4.1, idiomas, residencia de datos) indicando si cada cambio aplica a la experiencia independiente o embebida.
- [Course SC-5006-A: Enhance security operations by using Microsoft Security Copilot](https://learn.microsoft.com/en-us/training/courses/sc-5006) · Curso · Oficial · Microsoft Learn. Curso de un día (autodidacta o con instructor) para analistas, administradores y gerentes de SOC que cubre fundamentos de IA generativa, experiencias independiente y embebidas y ejercicios basados en simulación.

### Webinars, videos y podcasts

- [Microsoft Security Copilot video hub](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) · Video · Oficial · Microsoft Adoption. Colección oficial de vídeos cortos y deep dives (agentes, funciones, partners y casos de clientes), incluida la guía rápida y el vídeo de configuración inicial y asignación de usuarios.
- [Getting Started with Security Copilot (Skilling Series)](https://www.youtube.com/watch?v=g2I1rozWGVI) · Webinar · Oficial · Microsoft Security Community · Microsoft Security Community (YouTube). Sesión práctica sobre qué incluye E5, requisitos para empezar, experiencias principales y agentes de 'día uno'.
- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar · Oficial · Microsoft Security Community · Microsoft Security Community (YouTube). Lista de 18 webinars 2025-2026 sobre Security Copilot en Defender, Entra, Intune y Purview, agentes personalizados, Logic Apps vs. agentes y primeros pasos.
- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar · MVP · Ugur Koc · Microsoft Security Community (YouTube) · 19 feb 2026. Webinar de un MVP sobre cómo pasar de una idea a un agente fiable: iterar objetivos e instrucciones, elegir herramientas y validar decisiones con evidencia (lenguaje natural, Agent Builder y YAML).
- [Mitigate threats using Microsoft Security Copilot | SC-200 | Episode 2](https://www.youtube.com/watch?v=QmvVYOG4uWI) · Video · Oficial · Microsoft Learn (YouTube). Episodio del curso SC-200 que repasa IA generativa, procesamiento de prompts, plugins, promptbooks, workspaces, bases de conocimiento y experiencias embebidas de Security Copilot.
- [Microsoft Security Copilot Flight School](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/) · Video · Empleado de Microsoft · Legado aún útil · Ryan Munsch · Microsoft Learn Shows · 23 sep 2024. Serie de 11 vídeos cortos (IA generativa, orquestación, experiencias, plugins, prompting, promptbooks, Logic Apps y extensibilidad) para una base conceptual rápida. *Nota:* Grabada en sep-oct 2024 como 'Copilot for Security'; no cubre agentes, workspaces ni inclusión E5/E7

### Laboratorios, GitHub y herramientas

- [Microsoft Security Copilot – Microsoft Adoption (adoption hub)](https://adoption.microsoft.com/en-us/security-copilot/) · Herramienta · Oficial · Microsoft Adoption. Hub oficial de adopción con agentes por dominio, video hub, serie global de talleres técnicos, estudios de impacto, casos de clientes, Security Store y FAQ de inclusión en E5/E7.
- [Azure/Security-Copilot (repositorio oficial de la comunidad)](https://github.com/Azure/Security-Copilot) · GitHub · Empleado de Microsoft · Legado aún útil · Sean Wasonga y colaboradores · GitHub – Azure. Repositorio oficial con plugins de ejemplo, muestras de promptbooks, prompts, escenarios de Logic Apps, monitoreo y talleres técnicos usados por el Ninja. *Nota:* Último commit hace ~9 meses (≈ febrero 2026); varios enlaces del README apuntan a rutas antiguas de Learn y al nombre Copilot-For-Security

### Comunidad: blogs, libros, newsletters y eventos

- [Rod's Blog – etiqueta Security Copilot](https://rodtrent.substack.com/t/security-copilot) · Blog · Empleado de Microsoft · Nuevo · Rod Trent · Rod's Blog (Substack) · ago 2026. Serie de artículos sobre inclusión en E5, workspaces, calculadora, overage SCU y 'Prompt of the Day', además del boletín THE PROMPT for Microsoft Security.

**Manos a la obra**

1. `Laboratorio` Recorre la ruta [SC-5006](https://learn.microsoft.com/en-us/training/paths/security-copilot-and-ai/) y la ruta [Deploy and operate Microsoft Security Copilot](https://learn.microsoft.com/en-us/training/paths/deploy-operate-security-copilot/) y registra qué módulo de esta guía cubre cada uno de sus módulos. Evidencia: tabla de correspondencia dentro de tu plan de estudio personal.
2. `Laboratorio` Lee con ojo crítico el [Ninja oficial de 2024](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928) y clasifica cinco de sus afirmaciones en «vigente», «superada» o «falta» (por ejemplo, la gestión de plugins solo por usuario o la ausencia de agentes), con el módulo de esta guía que la actualiza. Evidencia: lista de hallazgos.
3. `Laboratorio` Elige tres webinars de la [Security Copilot Skilling Series](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) —uno de agentes, uno de automatización y uno del portal de tu rol— y agéndalos en las semanas del plan que les corresponden. Evidencia: plan de estudio con fechas.
4. `Laboratorio` Suscríbete al [RSS del blog de Security Copilot](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SecurityCopilotBlog) y revisa la página [What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security); anota la fecha de su última entrada y qué otras fuentes usarás para no depender solo de ella. Evidencia: captura del lector de feeds configurado.
5. `Laboratorio` Recorre el [hub de adopción](https://adoption.microsoft.com/en-us/security-copilot/) y su [versión en español](https://adoption.microsoft.com/es-es/security-copilot/), y elige tres recursos para tu equipo (un video, un estudio y la FAQ de inclusión). Evidencia: mensaje al equipo con los tres enlaces y el motivo de cada uno.

**¿Quieres profundizar?**

- [Agents That Actually Work: From an MVP (Skilling Series)](https://www.youtube.com/watch?v=1KsM2k2dP7U) · Webinar
- [Azure/Security-Copilot (repositorio oficial de la comunidad)](https://github.com/Azure/Security-Copilot) · GitHub
- [Rod's Blog – etiqueta Security Copilot](https://rodtrent.substack.com/t/security-copilot) · Blog
- [Microsoft Security Copilot Flight School](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/) · Video

<a id="i1"></a>

## I1 · Qué es Security Copilot hoy

*L100–L200 · ~3 h · Origen: Ninja oficial de 2024, parte 1, módulos 1 y 3 (introducción y arquitectura)*

Microsoft Security Copilot es la plataforma de IA generativa de Microsoft para seguridad. El Ninja de 2024 la describía como un **sistema de IA compuesto**: un orquestador recibe tu prompt, lo pre-procesa trayendo contexto con plugins (Defender, Sentinel, Entra, Intune, Purview, inteligencia de amenazas o los tuyos), llama al modelo y post-procesa la respuesta con más llamadas antes de devolverla, siempre con **tus permisos** (autenticación on-behalf-of). Se usa en una **experiencia independiente**, **embebido** en los portales de seguridad y a través de **agentes**, y se dimensiona en **Security Compute Units (SCU)**.

Desde su disponibilidad general, el 1 de abril de 2024, el producto cambió de escala: los primeros agentes se anunciaron el 24 de marzo de 2025, el **Security Store** abrió en vista previa en septiembre de 2025, en Ignite 2025 llegaron 12 agentes nuevos de Microsoft y más de 30 de partners y, desde el 18 de noviembre de 2025, Security Copilot viene **incluido en Microsoft 365 E5** (y luego en E7). Los clientes nuevos de E5/E7 ven una portada centrada en agentes.

En julio de 2026 Microsoft presentó **Project Perception**, un sistema multiagente dentro del portal de Defender —agentes rojo, azul y verde coordinados por playbooks— en vista previa limitada por invitación, y en septiembre de 2026 el **Integrated SOC (ISOC)**. Este módulo te da la foto completa antes de entrar en detalle, con una advertencia: Security Copilot no está diseñado para las nubes de gobierno de EE. UU.

**Por qué importa**

Para invertir bien hay que saber qué se compra y qué se usa. Entender las piezas —independiente, embebido, agentes y Perception— evita duplicar herramientas, fija expectativas realistas (asistir no es actuar) y permite explicar a la dirección por qué la capacidad es compartida y cómo se reparte entre experiencias.

**Qué vas a lograr**

- Describir el flujo de orquestación: pre-procesamiento, grounding con plugins, modelo y post-procesamiento.
- Distinguir la experiencia independiente, las experiencias embebidas, los agentes y Project Perception.
- Ubicar los hitos 2024–2026: GA, agentes, inclusión en E5/E7, Security Store, Perception e ISOC.
- Reconocer las limitaciones de disponibilidad (nubes de gobierno) y de estado (vista previa).

> **Novedad.** Project Perception se anunció el 27 de julio de 2026 como un sistema multiagente —agentes rojo, azul y verde con una arquitectura multimodelo que incluye MAI-Cyber-1-Flash— dentro del portal de Defender ([anuncio](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/)). Learn lo describe como vista previa pública limitada, solo por invitación, con URBAC en todas las cargas: Security Admin configura los agentes y Security Reader los usa ([primeros pasos con Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-get-started)).

> **Qué cambió.** Los clientes nuevos de E5/E7 ven una portada centrada en agentes; el chat se abre desde All history > New session ([primeros pasos con Security Copilot](https://learn.microsoft.com/en-us/copilot/security/get-started-security-copilot)).

> **Novedad.** En Ignite 2025 (18 de noviembre) Microsoft sumó 12 agentes propios y más de 30 de partners; el Security Store está en vista previa desde septiembre de 2025 ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security), [anuncio de Ignite](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/)).

> **Atención.** Security Copilot no está diseñado para las nubes de gobierno de EE. UU. (GCC, GCC High, DoD y Azure Government) ([qué es Security Copilot](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot)).

**¿Tienes poco tiempo?**

- [What is Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot) · Documentación
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Documentación
- [Rethinking security for the age of AI](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/) · Blog oficial

### Documentación, cursos y credenciales

- [Microsoft Security Copilot documentation (hub)](https://learn.microsoft.com/en-us/copilot/security/) · Documentación · Oficial · Microsoft Learn. Índice oficial de la documentación: conceptos, agentes, plugins, promptbooks, guías de administración, experiencias embebidas por producto, privacidad, application cards y contenido para desarrolladores.
- [What is Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot) · Documentación · Oficial · Microsoft Learn · 20 abr 2026. Define Security Copilot, sus casos de uso principales y el flujo de orquestación (grounding con plugins → LLM → post-procesamiento con plugins → respuesta), además del Customer Connection Program.
- [Project Perception | Microsoft Security](https://www.microsoft.com/en-us/security/business/ai-powered-cybersecurity/project-perception-agentic-system) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Security · jul 2026. Página de producto que distingue Project Perception (sistema agéntico: 'IA que actúa') de Security Copilot (interfaz de chat asistida: 'IA que asiste'), indica que arranca en Microsoft Defender y se factura por consumo en SCU. *Nota:* Precio por consumo (pago por uso) con tasas distintas por agente; se lanza dentro de Microsoft Defender
- [Perception documentation](https://learn.microsoft.com/en-us/security/agentic-security/) · Documentación · Oficial · Vista previa · Microsoft Learn. Hub de documentación de Perception con conceptos, agentes red/blue/green (Recon, Attack Investigation, Detection Authoring, Triage, Threat Intelligence, Posture Prioritization), playbooks, sesiones y ficha de IA responsable.
- [Get started with Project Perception](https://learn.microsoft.com/en-us/security/agentic-security/agentic-security-get-started) · Documentación · Oficial · Vista previa · Microsoft Learn. Guía de inicio de Perception en el portal de Defender: requisitos (URBAC en todas las cargas), permisos (Security Admin configura, Security Reader usa) y tres rutas (chat, agentes, playbooks). *Nota:* Estado indicado: Limited Public Preview (solo por invitación)
- [Microsoft Security Copilot | Microsoft Security (página de producto)](https://www.microsoft.com/en-in/security/business/ai-machine-learning/microsoft-security-copilot) · Documentación · Oficial · Microsoft Security. Página de producto con agentes embebidos, de partners y de la comunidad, productos integrados (Sentinel, Defender, Intune, Entra, Purview, Defender for Cloud) y métricas de estudios.

### Anuncios y blogs oficiales

- [Rethinking security for the age of AI](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Hayete Gallot · The Official Microsoft Blog · 27 jul 2026. Anuncio de Project Perception, un sistema agéntico con agentes red, blue y green, arquitectura multimodelo (incluido MAI-Cyber-1-Flash) y preview pública a partir del 3 de agosto. *Nota:* El blog habla de 'public preview' el 3-ago-2026, mientras que Learn la describe como 'Limited Public Preview' por invitación
- [Ambient and autonomous security for the agentic era](https://www.microsoft.com/en-us/security/blog/2025/11/18/ambient-and-autonomous-security-for-the-agentic-era/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 18 nov 2025. Visión de Ignite 2025 sobre seguridad 'ambiente y autónoma': Agent 365, protección de agentes y uso de agentes de Security Copilot para equipos de seguridad e IT.

### Webinars, videos y podcasts

- [Microsoft Security Copilot agents (Microsoft Mechanics)](https://www.youtube.com/watch?v=al9OSFGqd8I) · Video · Empleado de Microsoft · Dilip Radhakrishnan · Microsoft Mechanics · 3 oct 2025. Demo de 8 minutos de agentes (triage de phishing y alertas, revisiones de acceso, optimización de Acceso Condicional, remediación de vulnerabilidades) y creación de agentes propios.

**Manos a la obra**

1. `Laboratorio` Dibuja el diagrama de orquestación de Security Copilot a partir de [qué es Security Copilot](https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot): prompt, pre-procesamiento y grounding con plugins, modelo, post-procesamiento y respuesta; marca dónde se aplican los permisos on-behalf-of y dónde intervienen los agentes. Evidencia: diagrama versionado.
2. `Laboratorio` Construye una línea de tiempo con ocho hitos de 2024 a 2026 —GA del 1 de abril de 2024, primeros agentes del 24 de marzo de 2025, Security Store en septiembre de 2025, inclusión en E5 del 18 de noviembre de 2025, E7 y Agent 365 del 1 de mayo de 2026, Project Perception del 27 de julio de 2026 e [ISOC del 23 de septiembre de 2026](https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/)—, cada uno con su fuente. Evidencia: línea de tiempo con enlaces.
3. `Laboratorio` Mira el video de [Microsoft Mechanics sobre los agentes de Security Copilot](https://www.youtube.com/watch?v=al9OSFGqd8I) (octubre de 2025) y compara los agentes que muestra con su estado actual en el [inventario de agentes](00_Programa.md#inventario-agentes). Evidencia: lista de agentes con sus cambios de nombre, estado o retiro.
4. `Laboratorio` Redacta una nota de una página para el CISO: qué es Security Copilot, qué es Project Perception, cómo se relacionan, qué está en vista previa y qué decisiones hay que tomar este trimestre, con el [anuncio de Perception](https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/) y la [documentación de Perception](https://learn.microsoft.com/en-us/security/agentic-security/) como fuentes. Evidencia: nota revisada por tu líder.

**¿Quieres profundizar?**

- [Microsoft Security Copilot agents (Microsoft Mechanics)](https://www.youtube.com/watch?v=al9OSFGqd8I) · Video

<a id="i2"></a>

## I2 · Licenciamiento, capacidad y aprovisionamiento

*L100–L200 · ~5 h · Origen: Ninja oficial de 2024, parte 1, módulo 1 (onboarding, entonces solo con capacidad aprovisionada)*

Hoy hay dos caminos para tener capacidad. El primero es la **inclusión en Microsoft 365 E5 y E7**: 400 SCU al mes por cada 1.000 licencias de usuario **pagas**, con un tope de 10.000 y escalado lineal (400 licencias dan 160 SCU), que se reinicia cada mes sin acumularse. Se activa sin clics, con una **Default Security Copilot Capacity** virtual que no se factura por hora ni se puede modificar y que comparte todo el tenant. El segundo es la **capacidad aprovisionada** en Azure —4 USD por SCU y hora a precio de lista, mínimo 1 SCU, por bloques de hora de reloj— más **SCU de excedente** a 6 USD, con tope opcional.

La inclusión no cubre todo: el data lake de Sentinel, la experiencia no agéntica de Data Security Investigations, los cargos de Logic Apps, las licencias de agentes de partners y los prerrequisitos fuera de E5/E7 se pagan aparte, y los clientes que solo tienen Sentinel no son elegibles. Además, la capacidad vive en un **workspace** con decisiones que importan: la ubicación de almacenamiento (que no se puede cambiar después), dónde se evalúan los prompts —en MCSA, normalmente de forma global—, la compartición de datos con Microsoft y el acceso a datos de Microsoft 365.

Este módulo te enseña a calcular lo que tienes, a dimensionar lo que te falta y a configurar workspaces con criterio de privacidad y costo.

**Por qué importa**

El error más caro de 2026 tiene dos caras: pagar SCU que ya tienes por E5 o agotar el pool con automatizaciones que nadie planificó. Un modelo de costos por escenario le permite al CISO decidir qué agentes encender, y entender la residencia de datos evita decisiones irreversibles, porque la ubicación del workspace no se cambia después de crearlo.

**Qué vas a lograr**

- Calcular las SCU incluidas para una organización con E5 o E7 y explicar qué no cubre la inclusión.
- Explicar la facturación de SCU aprovisionadas y de excedente y cuándo conviene cada una.
- Decidir la ubicación de datos, la evaluación de prompts y la compartición de datos de un workspace.
- Construir un modelo de costos con tres escenarios de uso.

> **Novedad.** Inclusión en E5 y E7: 400 SCU al mes por cada 1.000 licencias de usuario pagas, con tope de 10.000 y escalado lineal (400 licencias → 160 SCU; 4.000 → 1.600). El pool se reinicia cada mes sin acumularse y vive en una Default Security Copilot Capacity virtual que no se factura por hora ni se puede modificar. El despliegue empezó el 18 de noviembre de 2025 y los agentes no se activan solos ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).

> **Atención.** La inclusión no cubre el cómputo ni el almacenamiento del data lake de Sentinel, la experiencia no agéntica de Data Security Investigations, los cargos de Logic Apps, las licencias de agentes de partners ni los prerrequisitos fuera de E5/E7, y los clientes que solo tienen Sentinel no son elegibles. Si tu organización ya tenía capacidad aprovisionada, la FAQ pide no eliminarla ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)). Las fechas del despliegue y el tratamiento del uso por encima del pool tienen versiones distintas según la fuente: revísalas en [Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia).

> **Atención.** Precios de lista: 4 USD por SCU aprovisionada y hora —mínimo 1 SCU y máximo 100 en el onboarding manual, por bloques de hora de reloj; lo no usado expira— y 6 USD por SCU de excedente, medida con un decimal y con tope opcional. El onboarding manual sugiere 3 SCU con excedente ilimitado para explorar: en un laboratorio deja el excedente en cero ([capacidad](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity), [precios](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/), [onboarding manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding)).

> **Consejo Ninja.** En MCSA el auto-aprovisionamiento suele dejar la evaluación de prompts en modo global (EE. UU., Reino Unido, UE y Australia-Nueva Zelanda), porque los datos no residen en la UE; la ubicación de almacenamiento sigue la geografía de Entra y no se puede cambiar después de crear el workspace. Involucra a privacidad antes de crear workspaces adicionales ([auto-aprovisionamiento](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot), [privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)).

**¿Tienes poco tiempo?**

- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación
- [Microsoft Security Copilot Security Compute Units and capacity](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Documentación
- [Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot) · Documentación
- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/) · Documentación

### Documentación, cursos y credenciales

- [Learn about Security Copilot for Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Documentación · Oficial · Nuevo · Microsoft Learn · 19 jun 2026. FAQ oficial de la inclusión de Security Copilot en Microsoft 365 E5/E7: 400 SCU al mes por cada 1.000 licencias de usuario de pago (tope 10.000), despliegue desde el 18-nov-2025, qué incluye y qué no.
- [Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 jun 2026. Explica qué se aprovisiona automáticamente con E5/E7 (capacidad virtual y workspace por defecto, ubicación de datos, compartición de datos desactivada, ubicación de evaluación de prompts, acceso a datos de M365 y roles por defecto).
- [Configure workspaces for Microsoft Security Copilot (módulo)](https://learn.microsoft.com/en-us/training/modules/configure-security-copilot-workspaces/) · Curso · Oficial · Microsoft Learn. Módulo de 45 minutos para planificar y crear workspaces con SCU, ubicación de datos y compartición, asignar roles, configurar plugins y owner settings por workspace, asignar workspaces a agentes y vigilar la capacidad.
- [Get started with Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/get-started-security-copilot) · Documentación · Oficial · Microsoft Learn. Guía de incorporación que distingue clientes E5/E7 (auto-aprovisionados) de los demás (aprovisionamiento manual de SCU) y describe la nueva página de inicio centrada en agentes.
- [Onboarding to Microsoft Security Copilot for non-Microsoft 365 E5 and E7 customers](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding) · Documentación · Oficial · Microsoft Learn. Pasos para aprovisionar capacidad (desde el portal, recomendado, o desde Azure): workspace, suscripción, grupo de recursos, ubicación de evaluación de prompts, SCU y overage, compartición de datos y auditoría en Purview.
- [Microsoft Security Copilot – Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/) · Documentación · Oficial · Microsoft Security. Página oficial de precios: SCU aprovisionada a 4 USD/hora y SCU de overage a 6 USD/hora (precios de lista estimados), con FAQ sobre la inclusión en E5/E7 y la calculadora de capacidad.
- [Microsoft Security Copilot Security Compute Units and capacity](https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity) · Documentación · Oficial · Microsoft Learn · 29 abr 2026. Define las SCU y compara capacidad aprovisionada (mínimo 1 SCU, bloques de hora de reloj, sin acumulación), overage (facturación por consumo con décimas) y capacidad de inclusión E5/E7, con ejemplos de facturación.
- [Security Copilot agents in Microsoft 365 E5](https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5) · Documentación · Oficial · Microsoft Security. Página de producto de los agentes incluidos en Microsoft 365 E5 con FAQ del beneficio de SCU y enlaces a adopción, blog y talleres.
- [MC1478465 – Security Copilot is now included as part of your Microsoft 365 E5/E7 plan (archivo del Message Center)](https://mc.merill.net/message/MC1478465) · Documentación · Comunidad · Nuevo · Merill Fernando (archivo comunitario) · Microsoft 365 Message Center Archive (mc.merill.net) · 24 sep 2026. Archivo del aviso oficial que resume la inclusión (400 SCU/1.000 licencias, tope 10.000) y lo que no cubre, con su historial de versiones.

### Anuncios y blogs oficiales

- [Agents built into your workflow: Get Security Copilot with Microsoft 365 E5](https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/) · Blog oficial · Empleado de Microsoft · Dorothy Li · Microsoft Security Blog · 18 nov 2025. Anuncio oficial de la inclusión de Security Copilot en Microsoft 365 E5 con 12 nuevos agentes de Microsoft y más de 30 de partners, y aviso de 30 días antes de la activación.
- [Microsoft 365 E7 and Agent 365 are now generally available](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) · Blog oficial · Empleado de Microsoft · Nuevo · Caroline Stanford · Microsoft Tech Community – Microsoft 365 Blog · 1 may 2026. GA de Microsoft 365 E7 (Frontier Suite: M365 E5 + Entra Suite + Microsoft 365 Copilot + Agent 365) a 99 USD/usuario/mes y de Agent 365 (15 USD/usuario/mes standalone).
- [New tools for Security Copilot management and capacity planning](https://techcommunity.microsoft.com/blog/securitycopilotblog/new-tools-for-security-copilot-management-and-capacity-planning/4432723) · Blog oficial · Oficial · Microsoft Tech Community – Microsoft Security Copilot Blog · 14 jul 2025. Anuncio de los workspaces (preview) para segmentar datos, acceso y capacidad por equipo o región, y de la calculadora de capacidad de SCU en el portal independiente.

### Laboratorios, GitHub y herramientas

- [Security Copilot SCU Calculator (comunidad)](https://www.scucalculator.com/) · Herramienta · MVP · Ugur Koc · scucalculator.com. Calculadora comunitaria que estima el costo mensual combinando el pool incluido de E5/E7, uso de chat por administradores y agentes seleccionados.
- [Security Copilot capacity calculator](https://securitycopilot.microsoft.com/calculator) · Herramienta · Oficial · Microsoft Security Copilot · 14 jul 2025. Calculadora oficial que estima las SCU necesarias según usuarios por experiencia embebida y uso previsto, como punto de partida para aprovisionar y presupuestar.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Security Copilot for a 100-User Organization: What It Does and What It Costs](https://o365hq.com/blog/microsoft-security-copilot-for-a-100-user-organization-pricing-and-what-it-does) · Blog · Comunidad · Nuevo · IT Partner · IT Partner (o365hq.com) · 11 oct 2026. Ejemplo aritmético de costos: 1 SCU aprovisionada ≈ 2.880 USD/mes (30 días) frente a 40 SCU/mes incluidas para 100 licencias E5.

**Manos a la obra**

1. `Laboratorio` Calcula con la [FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) las SCU mensuales de tres organizaciones con 400, 4.000 y 30.000 licencias pagas de E5, y explica por qué la tercera queda en el tope. Evidencia: tabla con el cálculo (160, 1.600 y 10.000 SCU).
2. `Laboratorio` Estima tres escenarios —piloto de diez analistas, SOC con resúmenes de incidentes por severidad y SOC con dos agentes programados— con la [calculadora de capacidad](https://securitycopilot.microsoft.com/calculator) y compáralos con el pool de E5/E7 y con capacidad aprovisionada a precio de lista. Si usas la [calculadora comunitaria](https://www.scucalculator.com/), anota que trata el uso por encima del pool como excedente facturable. Evidencia: modelo de costos de tres escenarios.
3. `Laboratorio` Completa el módulo [Configure workspaces for Microsoft Security Copilot](https://learn.microsoft.com/en-us/training/modules/configure-security-copilot-workspaces/) y documenta para tu organización las decisiones de ubicación de datos, evaluación de prompts, compartición de datos y acceso a datos de Microsoft 365, con su justificación y el visto bueno de privacidad. Evidencia: ficha del workspace.
4. `Laboratorio parcial` Haz el [onboarding manual](https://learn.microsoft.com/en-us/copilot/security/manual-onboarding) en una suscripción de laboratorio separada, con presupuesto y alertas: 1 SCU, excedente en cero, workspace con la ubicación elegida y compartición de datos desactivada; verifica el recurso en Azure y elimina la capacidad al terminar. Limitación: cuesta 4 USD por hora iniciada, no está confirmado que el crédito de Visual Studio lo cubra y la inclusión de E5 no aplica a licencias de prueba. Evidencia: capturas de la configuración y de la eliminación.
5. `Solo producción` En un tenant con licencias pagas de E5 o E7, verifica la Default Security Copilot Capacity, el workspace por defecto y los valores preseleccionados del [auto-aprovisionamiento](https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot), y compáralos con tu ficha del workspace. Cómo hacerlo seguro: revisión en modo lectura por un owner, sin cambiar configuración en esta etapa, sin eliminar capacidad aprovisionada existente (la FAQ pide conservarla) y con cualquier ajuste posterior registrado como cambio con plan de reversión. Evidencia: informe de diferencias.

**¿Quieres profundizar?**

- [Security Copilot SCU Calculator (comunidad)](https://www.scucalculator.com/) · Herramienta
- [Security Copilot capacity calculator](https://securitycopilot.microsoft.com/calculator) · Herramienta

<a id="i3"></a>

## I3 · Experiencia independiente: sesiones, plugins y promptbooks

*L100–L200 · ~4 h · Origen: Ninja oficial de 2024, parte 1, módulos 2 y 3, y parte 2, módulo 4 (configuración, plugins y gestión de plugins)*

El portal independiente de Security Copilot es donde se cruzan productos: una misma **sesión** puede combinar un incidente de Defender, inicios de sesión de Entra, el estado de un dispositivo en Intune e inteligencia de amenazas. Allí trabajas con prompts, fijas en el **pin board** lo importante, revisas el **registro de proceso** (qué plugins y skills usó Copilot, de dónde sacó los datos y cuánto tardó) y compartes la sesión con un compañero en modo de solo lectura.

Los **plugins** definen qué puede consultar Copilot: los de Microsoft vienen preinstalados, los de terceros se habilitan y los personalizados los agregas tú. Desde junio de 2025 se gestionan **por organización y por workspace**, no solo por usuario como decía el Ninja de 2024; por defecto solo los owners suben plugins personalizados y restringir un plugin preinstalado también afecta a las experiencias embebidas. Los **promptbooks** integrados —investigación de incidentes, análisis de scripts, perfil de actor, evaluación de vulnerabilidades y otros— y la biblioteca filtrable por rol te dan procedimientos listos para usar.

**Por qué importa**

Estandarizar cómo el equipo usa sesiones, plugins y promptbooks vuelve los resultados reproducibles y auditables. Restringir plugins es un control de exposición de datos, el registro de proceso permite verificar fuentes antes de actuar y compartir sesiones de solo lectura acelera el traspaso entre turnos sin repetir consultas ni gastar SCU de más.

**Qué vas a lograr**

- Navegar sesiones, pin board, historial y registro de proceso, y compartir una sesión de solo lectura.
- Gestionar plugins por organización y por workspace y anticipar su efecto en las experiencias embebidas.
- Ejecutar promptbooks integrados y comparar su consumo de SCU.
- Usar la biblioteca de prompts y promptbooks filtrada por rol y plugin.

> **Qué cambió.** Desde junio de 2025 la gestión de plugins por organización y por workspace está en disponibilidad general. Por defecto solo los owners suben plugins personalizados, restringir un plugin preinstalado también lo quita de las experiencias embebidas, los plugins con engranaje se configuran por usuario y los que exige un agente se habilitan solo para ese agente ([gestionar plugins](https://learn.microsoft.com/en-us/copilot/security/manage-plugins)).

> **Atención.** Una sesión compartida es de solo lectura, funciona solo dentro del mismo tenant y quien la ve **no necesita acceso a los datos del plugin usado**: compartir puede exponer información a personas sin permisos sobre esa fuente ([autenticación](https://learn.microsoft.com/en-us/copilot/security/authentication)). Los archivos subidos solo los ve quien los sube y las sesiones inactivas se borran a los 180 días ([privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)).

> **Novedad.** *Continue on failure* en promptbooks está en disponibilidad general desde marzo de 2025, y la llamada directa a capacidades del sistema, en vista previa, puede reducir el consumo de SCU ([What's new](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security)). Lo aprovecharás a fondo en [A1](03_Nivel_3_Avanzado.md#a1).

> **Consejo Ninja.** La biblioteca de prompts y promptbooks se filtra por rol y por plugin, y el registro de proceso muestra acciones, fuentes y tiempos: revísalo antes de confiar en una respuesta ([prompting en Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot)).

**¿Tienes poco tiempo?**

- [Navigate Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/navigating-security-copilot) · Documentación
- [Manage plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-plugins) · Documentación
- [Use promptbooks in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) · Documentación

### Documentación, cursos y credenciales

- [Use promptbooks in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jun 2026. Lista y explica los promptbooks prediseñados (impacto de artículo de amenaza externo, investigación de incidentes de Sentinel/Defender XDR, análisis de usuario, script sospechoso, perfil de actor, TI 360 y evaluación de vulnerabilidad) con sus entradas.
- [Manage plugins in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-plugins) · Documentación · Oficial · Microsoft Learn. Explica cómo los owners controlan quién agrega y publica plugins personalizados, cómo restringir plugins preinstalados (afecta también a experiencias embebidas) y cómo agregar, actualizar o borrar plugins.
- [Navigate Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/navigating-security-copilot) · Documentación · Oficial · Microsoft Learn. Describe las dos portadas (agents-first nueva y chat-first existente), el menú (Agents, Promptbooks, Build, All history, Owner), el process log, el pin board, compartir sesiones y el cambio de tenant.

### Laboratorios, GitHub y herramientas

- [samilamppu/SecurityCopilot](https://github.com/samilamppu/SecurityCopilot) · GitHub · MVP · Sami Lamppu · GitHub – samilamppu. Repositorio personal con plugins, prompts y promptbooks de ejemplo para Security Copilot.

**Manos a la obra**

1. `Laboratorio parcial` Con la capacidad temporal de la sesión de laboratorio (ver [I6](#i6)), ejecuta tres [promptbooks integrados](https://learn.microsoft.com/en-us/copilot/security/using-promptbooks) que no dependen de datos del tenant —script sospechoso, evaluación de vulnerabilidades y perfil de actor— y compara su consumo en el panel de uso. Limitación: consumen SCU y, sin datos reales, no se prueban los promptbooks de incidentes. Evidencia: tabla de SCU por promptbook.
2. `Laboratorio parcial` En una sesión, fija en el pin board las tres respuestas más útiles, revisa el registro de proceso (plugins, skills y tiempos) y comparte la sesión con un compañero; comprueba que la vista es de solo lectura ([navegar Security Copilot](https://learn.microsoft.com/en-us/copilot/security/navigating-security-copilot)). Limitación: requiere capacidad activa y un segundo usuario del tenant. Evidencia: capturas del pin board y de la sesión compartida.
3. `Laboratorio parcial` Revisa la [configuración de plugins](https://learn.microsoft.com/en-us/copilot/security/manage-plugins) por organización y por workspace: deja la carga de plugins personalizados solo para owners, identifica los plugins que se configuran por usuario y documenta qué pasaría en las experiencias embebidas si restringes un plugin preinstalado. Limitación: requiere ser owner con capacidad activa. Evidencia: configuración de plugins revisada.
4. `Laboratorio` Revisa las muestras del [repositorio Azure/Security-Copilot](https://github.com/Azure/Security-Copilot) y elige dos promptbooks para tu SOC; para cada uno anota entradas, plugins requeridos, datos que expone al compartirlo y quién debería poder ejecutarlo. Evidencia: ficha de dos promptbooks.
5. `Solo producción` Acuerda con el equipo la regla de uso de sesiones y archivos: qué no se sube (credenciales o datos personales innecesarios), con quién se comparten sesiones y qué pasa con las sesiones inactivas, que se borran a los 180 días ([privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)). Cómo hacerlo seguro: piloto con un equipo pequeño, revisión mensual de las sesiones compartidas por un owner y registro de la regla en la política de gobierno ([M7](02_Nivel_2_Intermedio.md#m7)). Evidencia: regla aprobada.

<a id="i4"></a>

## I4 · Experiencias embebidas en los portales de seguridad

*L100–L200 · ~5 h · Origen: Ninja oficial de 2024, parte 1, módulo 3, y parte 2, módulo 1 (experiencias embebidas y plugins de productos Microsoft)*

La mayor parte del valor diario está en las **experiencias embebidas**: Copilot dentro del portal donde ya trabajas, con el contexto de esa consola. En el **portal de Defender** —la consola unificada donde hoy también opera Sentinel— resume incidentes de hasta 100 alertas, propone respuestas guiadas, analiza scripts, traduce lenguaje natural a KQL, redacta informes y, en vista previa, ofrece un **chat de Defender** que propone planes que el analista aprueba o rechaza. En **Entra** ayuda con usuarios en riesgo, inicios de sesión, acceso condicional y gobierno de identidades; en **Intune**, con políticas, dispositivos y scripts respetando RBAC y scope tags; en **Purview**, con alertas de DLP y riesgo interno, Communication Compliance, eDiscovery y DSPM.

En Azure, Copilot llega a **Defender for Cloud** y **Azure Firewall** a través de Copilot en Azure; **Azure WAF** solo funciona desde la experiencia independiente y **Defender EASM** se usa como plugin. Todas las experiencias consumen del mismo workspace, y hay un detalle que sorprende: **ocultar el panel lateral no reduce el consumo**, porque el resumen de incidentes se sigue generando. Por eso el modo de generación —siempre, por severidad o bajo demanda— es una decisión de costo, no de interfaz.

**Por qué importa**

Las experiencias embebidas están en el flujo del analista, así que concentran la adopción y el ahorro de tiempo; también consumen SCU en silencio cuando los resúmenes son automáticos. Elegir el modo de generación y los roles adecuados define a la vez la calidad, el costo y quién puede ver qué.

**Qué vas a lograr**

- Enumerar las experiencias embebidas vigentes y qué hace Copilot en cada portal.
- Usar Security Copilot en el portal de Defender sobre incidentes de Defender XDR y Sentinel.
- Configurar el modo de generación del resumen de incidentes según severidad y costo.
- Identificar qué integraciones de Azure son embebidas, solo independientes o plugins.

> **Atención.** Ocultar el panel lateral de Copilot no cambia el consumo de SCU: el resumen de incidentes se sigue generando ([experiencias](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot)). Controla el costo con el modo de generación —siempre, por severidad con estimación de SCU o bajo demanda— y aprovecha la caché de una semana sin costo cuando el incidente no cambió ([resumen de incidentes](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary)).

> **Qué cambió.** La experiencia de Defender se llama hoy Security Copilot and Chat in Microsoft Defender: suma un chat contextual, en vista previa, que propone planes que el analista aprueba o rechaza ([Copilot y chat en Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-in-microsoft-365-defender)).

> **Consejo Ninja.** Con Sentinel, la experiencia independiente usa los plugins Microsoft Sentinel (Preview) y Natural language to KQL for Microsoft Sentinel (Preview): fija un workspace por defecto o indícalo en el prompt ([Security Copilot con Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot)). En el portal de Azure, el resumen de incidentes de Sentinel sigue en vista previa ([resumen en Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot-incident-summary)).

> **Atención.** Azure WAF funciona solo desde la experiencia independiente; Defender EASM se usa como plugin (algunas skills funcionan sin comprar EASM); Azure Firewall requiere logs estructurados de IDPS en Log Analytics; y Defender for Cloud funciona sin planes pagos, aunque su capacidad completa requiere Defender CSPM ([WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/waf-copilot), [EASM](https://learn.microsoft.com/en-us/azure/external-attack-surface-management/easm-copilot), [Firewall](https://learn.microsoft.com/en-us/azure/firewall/firewall-copilot), [Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/copilot-security-in-defender-for-cloud)).

**¿Tienes poco tiempo?**

- [Microsoft Security Copilot experiences](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot) · Documentación
- [Microsoft Security Copilot and Chat in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-in-microsoft-365-defender) · Documentación
- [Security Copilot with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Security Copilot in Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/copilot-security-in-defender-for-cloud) · Documentación · Oficial · Nuevo · Microsoft Learn (Defender for Cloud) · 15 jul 2026. Integración vía Copilot en Azure para analizar, resumir, remediar y delegar recomendaciones; funciona sin planes pagos pero con capacidad completa solo con Defender CSPM.
- [Microsoft Security Copilot and Chat in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-in-microsoft-365-defender) · Documentación · Oficial · Microsoft Learn (Defender XDR). Describe Copilot embebido en el portal de Defender (resúmenes de incidentes, respuesta guiada, scripts, archivos, dispositivos, identidades, informes) y el nuevo Defender Chat contextual con planes que el analista aprueba.
- [Security Copilot with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot) · Documentación · Oficial · Microsoft Learn (Sentinel). Explica los plugins Microsoft Sentinel y NL to KQL (preview), cómo fijar un workspace por defecto y cómo aprovechar incidentes unificados en el portal de Defender.
- [Security Copilot in Microsoft Entra](https://learn.microsoft.com/en-us/entra/security-copilot/security-copilot-in-entra) · Documentación · Oficial · Microsoft Learn (Entra). Cómo habilitar el plugin de Entra, prompts de ejemplo y el Copilot chat del centro de administración de Entra con chat de agentes (p. ej., optimización de Acceso Condicional).
- [Security Copilot in Microsoft Intune features overview](https://learn.microsoft.com/en-us/intune/copilot/) · Documentación · Oficial · Microsoft Learn (Intune). Copilot embebido en el centro de administración de Intune (exploración de datos, políticas, troubleshooting y agentes) sin licencias adicionales de Intune, respetando RBAC y scope tags.
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn (Purview). Capacidades embebidas e independientes en DSPM, DLP, Insider Risk, Communication Compliance y eDiscovery, incluidos resúmenes de alertas y promptbooks de DLP/IRM.
- [Security Copilot Agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn (Purview) · 23 mar 2026. Resume los agentes de Purview (triage de DLP e IRM, posture agent de DSPM y de Data Security Investigations en preview) y sus disparadores.
- [Microsoft Security Copilot experiences](https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot) · Documentación · Oficial · Microsoft Learn · 17 nov 2025. Compara la experiencia independiente y las embebidas y lista las embebidas por producto (Azure Firewall, Defender for Cloud, Defender TI, Defender XDR, Entra, Intune, Purview, Sentinel) además de los escenarios de desarrollador.
- [Microsoft Security Copilot scenarios in Microsoft Entra overview](https://learn.microsoft.com/en-us/entra/security-copilot/entra-security-scenarios) · Documentación · Oficial · Microsoft Learn (Entra). Tabla de escenarios por producto de Entra (ID, ID Protection, ID Governance, Global Secure Access) y exploración de datos en preview con la URL de Graph visible para verificar.
- [Security Copilot in Microsoft Intune](https://learn.microsoft.com/en-us/intune/copilot/security-copilot) · Documentación · Oficial · Microsoft Learn (Intune). Uso del plugin de Intune desde la experiencia independiente con enfoque SOC (dispositivos, cumplimiento, comparación de equipos y Cloud PC) y prompts de ejemplo.
- [Azure Firewall integration in Microsoft Security Copilot](https://learn.microsoft.com/en-us/azure/firewall/firewall-copilot) · Documentación · Oficial · Microsoft Learn (Azure Firewall). Investigación en lenguaje natural del tráfico interceptado por IDPS en toda la flota de firewalls, desde el portal independiente o desde Azure Copilot.
- [Azure Web Application Firewall integration in Microsoft Security Copilot](https://learn.microsoft.com/en-us/azure/web-application-firewall/waf-copilot) · Documentación · Oficial · Microsoft Learn (Azure WAF). Habilidades para reglas WAF más disparadas, IP ofensivas y resúmenes de SQLi y XSS en WAF de Application Gateway y Front Door, desde la experiencia independiente.
- [Microsoft Security Copilot in Defender EASM](https://learn.microsoft.com/en-us/azure/external-attack-surface-management/easm-copilot) · Documentación · Oficial · Microsoft Learn (Defender EASM). Uso del plugin de Defender EASM para obtener una foto de la superficie de ataque externa, priorizar CVE y curar activos con lenguaje natural.
- [Summarize Microsoft Sentinel incidents with Security Copilot](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot-incident-summary) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn (Sentinel) · 2 jul 2026. Resumen enriquecido de incidentes de Sentinel (hasta 100 alertas) con cronología, activos, IoC, actores, riesgo de usuario/dispositivo y coincidencias de watchlists.

### Webinars, videos y podcasts

- [Standalone and Embedded Experiences (Flight School, Part 3 of 11)](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/standalone-and-embedded-experiences) · Video · Empleado de Microsoft · Legado aún útil · Ryan Munsch · Microsoft Learn Shows · 1 oct 2024. Demostración de cuándo usar la experiencia independiente frente a la embebida en Defender XDR (resumen de incidentes, respuesta guiada, análisis de scripts, NL2KQL). *Nota:* Interfaz de 2024; hoy el portal de Defender incluye Sentinel y agentes

**Manos a la obra**

1. `Laboratorio parcial` En el portal de Defender, con la capacidad temporal y un incidente de prueba (por ejemplo, el de una prueba de detección de Defender for Endpoint en una VM de laboratorio), compara el [resumen de incidentes](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-m365d-incident-summary) con tu triage manual: tiempo, hallazgos, omisiones y errores. Limitación: telemetría de prueba y SCU por hora. Evidencia: tabla comparativa.
2. `Laboratorio parcial` Revisa la configuración de generación del resumen —siempre, por severidad o bajo demanda—, registra la estimación de SCU que muestra y decide el modo para tu SOC con su justificación de costo y valor. Limitación: el volumen de incidentes del laboratorio no refleja el real. Evidencia: decisión documentada.
3. `Laboratorio parcial` Haz tres preguntas en [Copilot en Entra](https://learn.microsoft.com/en-us/entra/security-copilot/security-copilot-in-entra) (usuarios en riesgo, inicios de sesión fallidos y políticas de acceso condicional) y tres en [Copilot en Intune](https://learn.microsoft.com/en-us/intune/copilot/) (comparación de perfiles, un dispositivo y un script); verifica que las respuestas respetan tu rol y, en Intune, tus scope tags. Limitación: pocos datos en un tenant de prueba; Intune exige completar la primera ejecución. Evidencia: capturas de preguntas y respuestas.
4. `Laboratorio parcial` Prueba la integración con [Azure WAF](https://learn.microsoft.com/en-us/azure/web-application-firewall/waf-copilot) (solo desde la experiencia independiente) o con [Azure Firewall](https://learn.microsoft.com/en-us/azure/firewall/firewall-copilot) (requiere logs estructurados de IDPS en Log Analytics) sobre un recurso de laboratorio. Limitación: costo de los recursos de Azure y poco tráfico malicioso real. Evidencia: prompt, respuesta y consulta de logs que la respalda.
5. `Solo producción` Usa el resumen y las respuestas guiadas sobre incidentes reales de Defender ([Copilot en Defender](https://learn.microsoft.com/en-us/defender-xdr/security-copilot-in-microsoft-365-defender)). Cómo hacerlo seguro: roles de solo lectura (Security Reader) para quienes aprenden, generación bajo demanda durante el piloto y validación humana antes de cualquier acción de contención. Evidencia: registro de cinco incidentes con la decisión tomada.
6. `Solo producción` Resume alertas reales de DLP o de riesgo interno con [Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) y compáralo con la revisión manual. Cómo hacerlo seguro: rol de analista sin permisos de administración, alertas ya cerradas y, para riesgo interno, acuerdo previo con privacidad, Legal y RR. HH. Evidencia: comparación de tres alertas.

<a id="i5"></a>

## I5 · Prompting para seguridad

*L100–L200 · ~3 h · Origen: Ninja oficial de 2024, parte 1 (módulo extra) y parte 2, módulo 3 (prompts efectivos)*

Un buen prompt de seguridad tiene cuatro elementos: **objetivo** (qué necesitas), **contexto** (por qué y sobre qué: «el incidente 15134 en Defender XDR»), **expectativas** (formato y audiencia: tabla para el SOC o resumen para la dirección) y **fuente** (qué plugin o datos usar). Microsoft recomienda ser específico, iterar, dar instrucciones en positivo y dirigirte a Copilot como «tú».

Los errores típicos también están documentados: prompts vagos («Pearl Sleet actor»), no indicar el workspace de Sentinel cuando no es el predeterminado, prompts tan largos que superan los límites de tokens y, sobre todo, aceptar resultados sin verificarlos. Y hay una regla de diseño que cambió desde 2024: los prompts son para lo **ad hoc**; lo estructurado y repetible va a **promptbooks** y **agentes**. Este módulo te deja una guía de prompts del SOC lista para compartir.

**Por qué importa**

Un prompt mal escrito cuesta dos veces: más SCU por respuesta útil y más tiempo de analista para verificarla. Una guía de prompts compartida da resultados consistentes entre turnos, reduce el riesgo de actuar sobre una salida inventada y acelera la incorporación de analistas nuevos.

**Qué vas a lograr**

- Escribir prompts con los cuatro elementos: objetivo, contexto, expectativas y fuente.
- Evitar los errores comunes: prompts vagos, workspace equivocado, prompts demasiado largos y falta de verificación.
- Verificar una respuesta con el registro de proceso y las fuentes citadas.
- Decidir cuándo un prompt debe convertirse en promptbook o en agente.

> **Consejo Ninja.** Los cuatro elementos de un buen prompt son objetivo, contexto, expectativas y fuente. Sé específico, itera, da contexto con identificadores («el incidente 15134 en Defender XDR»), usa instrucciones en positivo y dirígete a Copilot como «tú» ([prompts efectivos](https://learn.microsoft.com/en-us/copilot/security/prompting-tips)).

> **Atención.** Errores frecuentes: prompts vagos («Pearl Sleet actor»), no indicar el workspace de Sentinel cuando no es el predeterminado, prompts que superan los límites de tokens y aceptar resultados sin verificarlos ([Security Copilot con Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-security-copilot), [Application card](https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card)).

> **Qué cambió.** La recomendación actual es usar prompts para preguntas ad hoc y agentes para flujos estructurados y repetibles; el Ninja de 2024 resolvía casi todo con prompts y promptbooks ([prompting en Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot)).

**¿Tienes poco tiempo?**

- [Create effective prompts (Best practices for effective prompts)](https://learn.microsoft.com/en-us/copilot/security/prompting-tips) · Documentación
- [Prompting in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot) · Documentación
- [Security Copilot Prompt Library: Samples, Templates, and Promptbooks](https://github.com/rod-trent/Security-Copilot/blob/main/Prompts/Readme.md) · GitHub

### Documentación, cursos y credenciales

- [Create effective prompts (Best practices for effective prompts)](https://learn.microsoft.com/en-us/copilot/security/prompting-tips) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jun 2026. Guía oficial de prompting: los cuatro elementos (objetivo, contexto, expectativas, fuente) y consejos como ser específico, iterar, dar contexto, instrucciones positivas y dirigirse a Copilot como 'tú'.
- [Prompting in Microsoft Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jun 2026. Cómo iniciar sesiones, usar la biblioteca de prompts y promptbooks con filtros por rol y plugin, leer el process log y cuándo usar prompts (ad hoc) frente a agentes (flujos repetibles).

### Anuncios y blogs oficiales

- [Rod Trent – autor en Microsoft Security Blog (Get the most out of Microsoft Copilot for Security with good prompt engineering)](https://www.microsoft.com/en-us/security/blog/author/rod-trent/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Rod Trent · Microsoft Security Blog · 21 feb 2024. Página de autor que enlaza su artículo oficial sobre ingeniería de prompts para Security Copilot, base de la guía de prompting del Ninja. *Nota:* Escrito con el nombre 'Copilot for Security'; la guía vigente es 'Create effective prompts' en Learn

### Laboratorios, GitHub y herramientas

- [Security Copilot Prompt Library: Samples, Templates, and Promptbooks](https://github.com/rod-trent/Security-Copilot/blob/main/Prompts/Readme.md) · GitHub · Empleado de Microsoft · Legado aún útil · Rod Trent · GitHub – rod-trent. Biblioteca comunitaria de prompts por plugin, plantillas por producto y promptbooks de ejemplo (usuario riesgoso, script sospechoso, priorización de incidentes, KQL). *Nota:* Creada en la etapa 'Copilot for Security'; revisar nombres de plugins actuales

**Manos a la obra**

1. `Laboratorio` Taller sin consumo: reescribe diez prompts vagos de tu SOC con los cuatro elementos de los [prompts efectivos](https://learn.microsoft.com/en-us/copilot/security/prompting-tips) (objetivo, contexto, expectativas y fuente) y pide revisión entre pares. Evidencia: tabla de antes y después.
2. `Laboratorio` Arma la versión 1 de la guía de prompts del SOC: diez prompts por tarea (triage, caza e informe ejecutivo), cada uno con la fuente o el plugin esperado y su criterio de verificación, con ideas de la [biblioteca de Rod Trent](https://github.com/rod-trent/Security-Copilot/blob/main/Prompts/Readme.md). Evidencia: guía publicada para el equipo.
3. `Laboratorio parcial` Con la capacidad temporal, ejecuta el mismo pedido en tres versiones —vago, específico y específico con fuente y formato— y compara la calidad de la respuesta y las SCU en el [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage). Limitación: SCU por hora y datos de prueba. Evidencia: tabla de calidad y consumo.
4. `Laboratorio parcial` Pide una consulta en lenguaje natural con el [asistente de consultas](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-security-copilot-query-assistant) de la búsqueda avanzada, ejecútala y documenta qué tuviste que corregir antes de que fuera válida. Limitación: poca telemetría en un tenant de prueba. Evidencia: KQL generado y KQL corregido.
5. `Laboratorio` Clasifica quince tareas de tu SOC en «prompt ad hoc», «promptbook» o «agente», con la justificación de frecuencia, estructura, volumen y riesgo ([prompting en Security Copilot](https://learn.microsoft.com/en-us/copilot/security/prompting-security-copilot)). Evidencia: matriz de clasificación.

<a id="i6"></a>

## I6 · Laboratorio y primeros casos de uso

*L100–L200 · ~6 h · Origen: Ninja oficial de 2024, parte 1, módulo 3 (casos de uso), actualizado con las simulaciones guiadas de SC-5006*

Practicar Security Copilot exige planificar el costo. Hay cuatro caminos, de menor a mayor gasto: las **simulaciones guiadas** de Microsoft Learn (casi dos horas de práctica de owner settings, prompts, promptbooks, Purview, Defender XDR, creación de agentes y el agente de acceso condicional, sin tenant ni SCU); una **sesión corta con capacidad aprovisionada** (1 SCU con excedente en cero, un guion preparado y la capacidad eliminada al terminar); la **inclusión de E5/E7 en un tenant pago**, si tu organización ya la tiene; y la producción con aprobación formal.

La regla de este programa: la inclusión se calcula sobre licencias pagas, así que en un tenant de prueba no deberías esperar SCU incluidas. Una SCU cuesta 4 USD por hora de reloj iniciada, los cambios tardan hasta 30 minutos y eliminar la capacidad es irreversible y requiere al menos Security Administrator. Con ese marco, el módulo te lleva a documentar tus **tres primeros casos de uso** —con tiempo, calidad y SCU— y a configurar un primer agente de bajo riesgo: el **Threat Intelligence Briefing Agent**, de solo lectura.

**Por qué importa**

Un laboratorio bien planificado de dos horas con 1 SCU cuesta unos 8 USD; una SCU olvidada cuesta 96 USD al día. Documentar los primeros casos de uso con tiempo y costo medidos le da al caso de negocio sus primeros datos reales y evita que la adopción dependa de impresiones.

**Qué vas a lograr**

- Practicar con las simulaciones guiadas sin tenant ni SCU.
- Planificar y ejecutar una sesión de laboratorio de costo controlado y eliminar la capacidad al terminar.
- Documentar tres casos de uso iniciales con tiempo, calidad y SCU.
- Configurar un primer agente de bajo riesgo con identidad dedicada y permisos de solo lectura.

> **Atención.** La inclusión de E5/E7 se calcula sobre licencias de usuario pagas: en un tenant de prueba no deberías esperar SCU incluidas. Es una inferencia de la documentación que conviene confirmar con Microsoft, y tampoco está confirmado que el crédito de Visual Studio cubra el medidor de Security Copilot ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).

> **Consejo Ninja.** Para no pagar de más: crea la capacidad al inicio de una hora de reloj (1 SCU = 4 USD por hora iniciada), recuerda que los cambios tardan hasta 30 minutos y elimínala al terminar; eliminarla requiere al menos Security Administrator, es irreversible y los datos se borran en un plazo de 180 días ([gestionar uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage), [privacidad](https://learn.microsoft.com/en-us/copilot/security/privacy-data-security)).

> **Novedad.** Las funciones en disponibilidad general y en vista previa pública consumen SCU; las de vista previa privada no ([gestionar uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage)). El Dynamic Threat Detection Agent es gratuito mientras siga en vista previa ([Dynamic Threat Detection Agent](https://learn.microsoft.com/en-us/defender-xdr/dynamic-threat-detection-agent)).

> **Consejo Ninja.** Si todavía no puedes pagar capacidad, los videos de ejercicios del curso SC-5006 muestran cada práctica paso a paso ([videos de SC-5006](https://www.youtube.com/playlist?list=PLahhVEj9XNTfiHTLmqoEbndksKnJynfwR)).

**¿Tienes poco tiempo?**

- [Experience Security Copilot through guided simulations](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) · Laboratorio
- [Security Copilot use cases for security and IT roles](https://learn.microsoft.com/en-us/copilot/security/use-case-role-overview) · Documentación
- [Manage security compute unit usage in Security Copilot](https://learn.microsoft.com/en-us/copilot/security/manage-usage) · Documentación

### Documentación, cursos y credenciales

- [Security Copilot use cases for security and IT roles](https://learn.microsoft.com/en-us/copilot/security/use-case-role-overview) · Documentación · Oficial · Microsoft Learn. Casos de uso por rol (SOC, identidad, CISO, TI, seguridad de datos, nube) con enlaces a promptbooks y tutoriales para elegir los primeros escenarios.
- [Microsoft Security Copilot Threat Intelligence Briefing Agent (standalone)](https://learn.microsoft.com/en-us/copilot/security/threat-intel-briefing-agent) · Documentación · Oficial · Microsoft Learn. Documentación del agente de briefings de inteligencia de amenazas: plugins requeridos, identidad del agente (recomendada) y permisos mínimos con rol personalizado de Defender XDR.

### Webinars, videos y podcasts

- [SC-5006: Get started with Microsoft Copilot for Security (playlist de vídeos del curso)](https://www.youtube.com/playlist?list=PLahhVEj9XNTfiHTLmqoEbndksKnJynfwR) · Video · Oficial · Legado aún útil · Microsoft Learn (YouTube) · 4 nov 2025. 20 vídeos del curso SC-5006 con ejercicios grabados: aprovisionar capacidad, navegar la experiencia independiente, plugin de Sentinel, plugins personalizados, archivos, promptbooks, Defender XDR y Purview. *Nota:* Usa el nombre 'Copilot for Security'; útil para ver los ejercicios sin consumir SCU

### Laboratorios, GitHub y herramientas

- [Experience Security Copilot through guided simulations](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) · Laboratorio · Oficial · Microsoft Learn. Módulo de 1 h 53 min con guías interactivas (sin tenant ni SCU) para practicar owner settings, prompts, promptbooks, Purview, Defender XDR, creación de agentes y el agente de optimización de Acceso Condicional.

### Comunidad: blogs, libros, newsletters y eventos

- [Security Copilot Threat Intelligence Briefing Agent – Deep Dive](https://samilamppu.com/2025/09/05/security-copilot-threat-intelligence-briefing-agent-deep-dive/) · Blog · MVP · Sami Lamppu · Sam's Corner · 5 sep 2025. Recorrido práctico del agente de briefings de TI: prerrequisitos (1 SCU mínimo, plugins, identidad dedicada), configuración, memoria de feedback, mapa de actividad y envío por correo.

**Manos a la obra**

1. `Laboratorio` Completa el módulo de [simulaciones guiadas](https://learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/) (1 h 53 min): owner settings, prompts, promptbook personalizado, Purview, Defender XDR, creación de agentes y el agente de acceso condicional, sin tenant ni SCU. Evidencia: módulo completado en tu perfil de Learn.
2. `Laboratorio` Prepara el guion de la sesión antes de crear la capacidad: objetivos, prompts y promptbooks a ejecutar, tiempos, quién elimina la capacidad y cómo se verifica (anexo del entorno de práctica, fase 9). Evidencia: guion aprobado.
3. `Laboratorio parcial` Ejecuta una sesión de dos horas: crea 1 SCU con excedente en cero al inicio de una hora de reloj, corre el guion, exporta el [panel de uso](https://learn.microsoft.com/en-us/copilot/security/manage-usage) a Excel y elimina la capacidad (requiere Security Administrator y es irreversible); al día siguiente verifica en Cost Management que no hay cargos nuevos. Limitación: 4 USD por SCU y hora iniciada; los cambios tardan hasta 30 minutos. Evidencia: exportación del panel y captura de la eliminación.
4. `Laboratorio parcial` Documenta tres casos de uso iniciales a partir de los [casos de uso por rol](https://learn.microsoft.com/en-us/copilot/security/use-case-role-overview): para cada uno, prompt o promptbook, tiempo manual frente a asistido, calidad y SCU. Limitación: datos de prueba. Evidencia: tres fichas de caso de uso.
5. `Laboratorio parcial` Configura el [Threat Intelligence Briefing Agent](https://learn.microsoft.com/en-us/copilot/security/threat-intel-briefing-agent) en la experiencia independiente como primer agente: identidad dedicada, permisos de solo lectura y ejecución manual; revisa el informe y anota qué le faltó. Limitación: sin EASM ni Defender for Endpoint el informe es menos contextual y cada ejecución consume SCU. Evidencia: informe generado y nota de calidad.
6. `Solo producción` Mide el consumo real del pool de E5/E7 con el volumen real de incidentes y agentes ([FAQ de inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)). Cómo hacerlo seguro: grupo piloto, carga de plugins personalizados solo para owners, revisión semanal del panel de uso y sin eliminar capacidad existente. Evidencia: informe mensual de consumo por experiencia.

**¿Quieres profundizar?**

- [SC-5006: Get started with Microsoft Copilot for Security (playlist de vídeos del curso)](https://www.youtube.com/playlist?list=PLahhVEj9XNTfiHTLmqoEbndksKnJynfwR) · Video

<a id="reto-inicial"></a>

## Reto del nivel

**Tu primera sesión con valor medido.** Con el guion de [I6](#i6), ejecuta una sesión de dos horas (1 SCU y excedente en cero) en la que corras tus tres casos de uso iniciales, tres promptbooks y tu guía de prompts. Entrega: la ficha del workspace con las decisiones de privacidad, el modelo de costos de tres escenarios, la guía de prompts del SOC (versión 1), la exportación del panel de uso con las SCU por caso de uso y una recomendación de una página al CISO sobre qué experiencias habilitar, con qué modo de generación y con qué capacidad (pool de E5/E7 o aprovisionada). La capacidad debe quedar eliminada y verificada al día siguiente.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Cuántas SCU mensuales recibe por la inclusión una organización con 4.000 licencias pagas de Microsoft 365 E5?
   - a) 400
   - b) 1.600
   - c) 4.000
   - d) 10.000

2. ¿Qué pasa con las SCU incluidas en E5/E7 que no se usan durante el mes?
   - a) Se acumulan hasta tres meses
   - b) Se convierten en SCU de excedente
   - c) Se reembolsan como crédito de Azure
   - d) Se pierden: el pool se reinicia cada mes sin acumularse

3. ¿Cómo se factura la capacidad aprovisionada de Security Copilot?
   - a) Por bloques de hora de reloj, con un mínimo de 1 SCU; lo no usado expira al final de cada hora
   - b) Por minuto de uso real
   - c) Por prompt ejecutado
   - d) Con una tarifa mensual fija por usuario

4. En un tenant de MCSA auto-aprovisionado con E5, cuyos datos no residen en la UE, ¿dónde se evalúan los prompts por defecto?
   - a) Solo en EE. UU.
   - b) En la región del workspace de Sentinel
   - c) De forma global (EE. UU., Reino Unido, UE y Australia-Nueva Zelanda)
   - d) Solo en la UE

5. Según Microsoft, ¿cómo se relacionan Project Perception y Security Copilot?
   - a) Perception reemplaza y retira a Security Copilot
   - b) Perception es un plugin de la experiencia independiente
   - c) Son productos sin relación
   - d) Perception es el sistema agéntico que actúa y Security Copilot la IA que asiste; trabajan juntos

6. ¿En qué estado está Project Perception según la documentación de Learn al 6 de noviembre de 2026?
   - a) Vista previa pública limitada, solo por invitación, dentro del portal de Defender
   - b) Disponibilidad general incluida en E5
   - c) Vista previa privada sin costo
   - d) Retirado

7. Un analista comparte una sesión con un compañero que no tiene permisos sobre los datos de Sentinel usados en ella. ¿Qué ocurre?
   - a) El compañero no puede abrir la sesión
   - b) El compañero la ve en solo lectura, aunque no tenga acceso a los datos del plugin
   - c) El compañero puede continuar la sesión con sus propios prompts
   - d) La sesión se comparte también fuera del tenant

8. Un owner restringe un plugin preinstalado de Microsoft en la configuración de plugins. ¿Qué efecto tiene?
   - a) Ninguno sobre las experiencias embebidas
   - b) Solo afecta a los agentes de partners
   - c) También afecta a las experiencias embebidas que usan ese plugin
   - d) Elimina el plugin del tenant de forma irreversible

9. Un analista oculta el panel lateral de Copilot en el portal de Defender para ahorrar SCU. ¿Funciona?
   - a) Sí, el resumen deja de generarse
   - b) No: el resumen de incidentes se sigue generando; el costo se controla con el modo de generación
   - c) Sí, pero solo en incidentes de severidad baja
   - d) No, porque el resumen de incidentes no consume SCU

10. ¿Qué integración de Azure funciona solo desde la experiencia independiente de Security Copilot?
   - a) Azure WAF
   - b) Defender for Cloud
   - c) Azure Firewall
   - d) Intune

11. ¿Cuál NO es uno de los cuatro elementos de un prompt efectivo según Microsoft?
   - a) Objetivo
   - b) Contexto
   - c) Fuente
   - d) Temperatura del modelo

12. ¿Qué funciones de Security Copilot consumen SCU?
   - a) Solo las de disponibilidad general
   - b) Solo las de vista previa privada
   - c) Las de disponibilidad general y las de vista previa pública
   - d) Ninguna en vista previa

13. Quieres practicar prompts, promptbooks y la creación de agentes sin tenant ni SCU. ¿Qué recurso usas?
   - a) El Customer Connection Program
   - b) El onboarding manual con 3 SCU y excedente ilimitado
   - c) La calculadora de capacidad
   - d) Las simulaciones guiadas de la ruta SC-5006

14. En el OWASP Top 10 para aplicaciones LLM 2025, ¿qué riesgo se relaciona más directamente con el costo de un playbook que llama a Copilot en cada incidente?
   - a) LLM01 · Inyección de prompts
   - b) LLM06 · Agencia excesiva
   - c) LLM10 · Consumo no acotado
   - d) Ninguno: el costo no es un riesgo de seguridad

15. ¿Qué puntaje del knowledge check del Ninja oficial permite pedir el certificado de participación?
   - a) 100 %
   - b) 80 %
   - c) 75 %
   - d) 70 %

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

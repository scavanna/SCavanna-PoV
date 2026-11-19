# Nivel 1 · Inicial · Fundamentos de la arquitectura segura

*Seguridad de agentes de IA en Microsoft Foundry Ninja Training · Edición 2026*

[← Programa](00_Programa.md) · [Índice del programa](README.md) · [Nivel 2 · Intermedio →](02_Nivel_2_Intermedio.md)

<a id="inicial"></a>

Modelos, RAG, agentes y MCP; cómo está hecho Microsoft Foundry y qué parte de la seguridad es tuya; la infografía corregida capa por capa; el modelo de amenazas; la identidad sin claves y tu laboratorio con presupuesto. Terminas con una arquitectura de referencia corregida, el modelo de amenazas de tu agente piloto y un recurso de Foundry sin claves locales ni roles de más.

*L100–L200 · 7 módulos · ~32 horas · 57 recursos*

**Módulos de este nivel:** [P0 Modelos, RAG, agentes y MCP](#p0) · [F0 Cómo usar y ruta integrada](#f0) · [F1 Foundry por dentro](#f1) · [F2 Arquitectura por capas](#f2) · [F3 Modelado de amenazas](#f3) · [F4 Identidad y acceso](#f4) · [F5 Laboratorio seguro](#f5)

<a id="p0"></a>

## P0 · Prerrequisitos: modelos, RAG, agentes, herramientas y MCP en Azure

*L100–L200 · ~4 h · Origen: Nuevo en esta edición (no existe Ninja oficial de Foundry ni de seguridad de IA); se apoya en los cursos abiertos de Microsoft «AI Agents for Beginners» y «MCP for Beginners»*

Antes de asegurar un agente necesitas un vocabulario preciso. Un modelo de Foundry genera texto; **RAG** lo ancla en datos recuperados de un índice, como Azure AI Search o File Search; un **agente** suma instrucciones, herramientas y estado, y decide qué herramienta llamar. Foundry Agent Service es el runtime administrado de agentes de Microsoft Foundry, basado en la Responses API, con *prompt agents* (declarativos, en cómputo de Microsoft) y *hosted agents* (tu código en contenedores administrados). Las herramientas —AI Search, File Search, Code Interpreter, OpenAPI, Azure Functions, A2A, Bing, SharePoint o MCP— conectan al agente con datos y acciones. En la infografía, este módulo prepara la **Capa 1 · Desarrollo** y el flujo del usuario completo.

Cada herramienta tiene su propio camino de red y de identidad, y ahí empiezan los riesgos. **MCP** (Model Context Protocol) es el estándar abierto para que un agente descubra y llame herramientas de un servidor; en Foundry, un servidor MCP se autentica con clave, identidad de agente de Entra, identidad administrada u OAuth identity passthrough. La inyección indirecta llega escondida en un documento, una página web o la salida de una herramienta, y la descripción de una herramienta MCP puede contener instrucciones ocultas: por eso este programa trata todo contenido externo como no confiable. El modelo de amenazas completo llega en [F3](#f3) y la configuración segura de herramientas, en [M2](02_Nivel_2_Intermedio.md#m2).

**Por qué importa**

Seguridad, plataforma y desarrollo suelen discutir sobre «el agente» con significados distintos y deciden a ciegas. Entender qué hace el modelo, qué agrega RAG, qué decide el agente y por dónde viaja cada llamada a herramienta permite ubicar cada control del programa en su lugar, explicar por qué un agente con acciones exige más control que uno de solo lectura y evitar que un servidor MCP entre sin revisión.

**Qué vas a lograr**

- Explicar con un ejemplo en Foundry la diferencia entre modelo, RAG, agente, herramienta y servidor MCP.
- Distinguir prompt agents y hosted agents de Foundry Agent Service y qué administra Microsoft en cada caso.
- Trazar el flujo de una solicitud desde el usuario hasta una herramienta y marcar dónde actúan identidad, contenido y red.
- Diferenciar la inyección directa de la indirecta y explicar por qué la salida de una herramienta es entrada no confiable.
- Elegir entre Foundry, Agent Builder y Copilot Studio con criterios de código, despliegue, seguridad y costo.

> **Novedad.** La nueva generación de Foundry Agent Service, sobre la Responses API, quedó en GA el 16 de marzo de 2026 con SDK de producción para Python, JavaScript, Java y .NET ([anuncio en Tech Community](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-production-ready-secure-observable-ai-agents-with-real-time-voice-with-/4501074)). Si vienes del paquete `azure-ai-agents`, los agentes pasan a ser operaciones de `AIProjectClient` en `azure-ai-projects` ([blog de Foundry](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/)). Los hosted agents llegaron a GA el 9 de julio de 2026 ([novedades de julio y agosto](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/)).

> **Atención.** Las herramientas no viajan todas por el mismo camino. En un proyecto con red aislada, AI Search y File Search usan private endpoint; MCP, OpenAPI, Functions y A2A salen por tu subred; Code Interpreter usa la red troncal de Microsoft; y Bing, Web Search y SharePoint salen por endpoint público. Fabric data agent, Logic Apps, Browser Automation, Computer Use e Image Generation no se admiten con red aislada ([aislamiento de red de Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link)). Lo trabajarás en [M2](02_Nivel_2_Intermedio.md#m2) y [M5](02_Nivel_2_Intermedio.md#m5).

> **Consejo Ninja.** Para nivelar al equipo, «AI Agents for Beginners» tiene 18 lecciones con traducción al español, ya migradas a la Responses API y a Foundry; la lección 06 trata agentes confiables (mensajes de sistema, amenazas y humano en el bucle) ([curso](https://github.com/microsoft/ai-agents-for-beginners), [lección 06](https://github.com/microsoft/ai-agents-for-beginners/tree/main/06-building-trustworthy-agents)). El currículo «MCP for Beginners» incluye un módulo de seguridad actualizado a la especificación MCP 2026-07-28 ([MCP for Beginners](https://github.com/microsoft/mcp-for-beginners)).

> **Qué cambió.** Nombres que verás en material anterior: Azure AI Foundry (y antes Azure AI Studio) es hoy Microsoft Foundry; Azure AI Agent Service es Foundry Agent Service; Semantic Kernel y AutoGen convergen en Microsoft Agent Framework; y AI Toolkit para VS Code pasó a llamarse Foundry Toolkit ([cambios de nombre en la comunidad](https://microsoft.github.io/AI_Agents_Hackathon/), [novedades de abril de 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)). En este programa usamos siempre los nombres vigentes.

**¿Tienes poco tiempo?**

- [microsoft/ai-agents-for-beginners (18 lecciones)](https://github.com/microsoft/ai-agents-for-beginners) · GitHub
- [Deep dive into Foundry Agent Service networking](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agents-networking-deep-dive) · Documentación
- [microsoft/mcp-for-beginners (Model Context Protocol curriculum)](https://github.com/microsoft/mcp-for-beginners) · GitHub
- [Picking the right Agent Builder solution (John Savill's Technical Training)](https://tech.hub.ms/azure/videos/picking-the-right-agent-builder-solution) · Video

### Documentación, cursos y credenciales

- [ai-agents-for-beginners – 06 Building Trustworthy AI Agents](https://github.com/microsoft/ai-agents-for-beginners/tree/main/06-building-trustworthy-agents) · Curso · Empleado de Microsoft · Nuevo · Lee Stott y equipo de Cloud Advocates · GitHub (Microsoft) · jul 2026. Lección gratuita del curso «AI Agents for Beginners» sobre agentes confiables: marco de mensajes de sistema, amenazas a agentes, humano en el bucle y privacidad, con notebooks.

### Webinars, videos y podcasts

- [Picking the right Agent Builder solution (John Savill's Technical Training)](https://tech.hub.ms/azure/videos/picking-the-right-agent-builder-solution) · Video · Empleado de Microsoft · John Savill · Tech Hub (ficha del video de YouTube) · 23 mar 2026. Criterios para elegir entre Agent Builder, Copilot Studio y Microsoft Foundry: complejidad de código, selección de modelos, destino de despliegue, ciclo de vida, observabilidad, evaluaciones, seguridad, herramientas, multiagente, memoria y control de costos.

### Laboratorios, GitHub y herramientas

- [microsoft/ai-agents-for-beginners (18 lecciones)](https://github.com/microsoft/ai-agents-for-beginners) · GitHub · Empleado de Microsoft · Lee Stott y colaboradores (Microsoft Cloud Advocates) · GitHub · Microsoft. Curso abierto de 18 lecciones (con traducción al español) sobre agentes: patrones, uso de herramientas, RAG agéntico, agentes confiables, multiagente, MCP/A2A, memoria, Microsoft Agent Framework, despliegue escalable y lección 18 de seguridad de agentes.
- [microsoft/mcp-for-beginners (Model Context Protocol curriculum)](https://github.com/microsoft/mcp-for-beginners) · GitHub · Empleado de Microsoft · Lee Stott y colaboradores (Microsoft Cloud Advocates) · GitHub · Microsoft. Currículo abierto de MCP con ejemplos en .NET, Java, TypeScript, JavaScript, Rust y Python; incluye un módulo dedicado a seguridad (02-Security), buenas prácticas, laboratorios y traducción al español.

**Manos a la obra**

1. `Laboratorio` Recorre las lecciones 1, 4, 5, 6, 11 y 18 de [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) (unas 2,5 h; hay traducción al español) y redacta un glosario propio de 15 términos: modelo, despliegue, RAG, índice vectorial, agente, prompt agent, hosted agent, herramienta, function calling, MCP, servidor MCP, A2A, inyección directa, inyección indirecta y humano en el bucle. Evidencia: glosario revisado por una persona de otro equipo (datos, plataforma o SOC).
2. `Laboratorio` Con [la arquitectura de red del Agent Service](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agents-networking-deep-dive) y [el aislamiento de red de Foundry](https://learn.microsoft.com/en-us/azure/foundry/how-to/configure-private-link), dibuja el flujo del usuario de la infografía (usuario → Entra ID → Agent Service → SharePoint, AI Search, Logic Apps y MCP) y anota, para cada herramienta, su autenticación, por dónde sale (subred propia, private endpoint, red troncal de Microsoft o endpoint público) y dónde queda el dato. Evidencia: diagrama de una página que reutilizarás en [F2](#f2) y [F3](#f3).
3. `Laboratorio` Completa la credencial Applied Skills [Get started developing agents in Microsoft Foundry](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-developing-agents-in-microsoft-foundry/): un laboratorio evaluado de 45 minutos en el que despliegas un modelo, creas un agente y lo pruebas, sin usar tu suscripción. Al terminar, anota qué controles de seguridad no se evaluaron (identidad, red, guardrails, registro). Evidencia: credencial en tu perfil de Learn y lista de brechas con el módulo de este programa que las cubre.
4. `Laboratorio` Lee las [buenas prácticas de seguridad de MCP for Beginners](https://github.com/microsoft/mcp-for-beginners/blob/main/02-Security/mcp-security-best-practices.md) (especificación 2026-07-28) y el blog de Microsoft sobre [inyección indirecta en MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/). Arma una tabla con cinco reglas (el servidor no acepta tokens emitidos para otro, verifica cada solicitud, no usa la sesión como autenticación, descripciones tratadas como no confiables, aprobación de escrituras) y el control de Foundry o API Management que la hace cumplir. Evidencia: tabla regla → control → módulo ([M2](02_Nivel_2_Intermedio.md#m2), [M4](02_Nivel_2_Intermedio.md#m4)).
5. `Laboratorio` Mira el video de John Savill [Picking the right Agent Builder solution](https://tech.hub.ms/azure/videos/picking-the-right-agent-builder-solution) y completa una matriz de decisión para tres casos de uso de tu organización: Foundry, Agent Builder o Copilot Studio, con criterios de código, modelos, despliegue, evaluaciones, seguridad y costo. Indica qué programa de la serie gobierna cada opción (por ejemplo, Copilot Studio se trabaja en el programa Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio). Evidencia: matriz con la decisión y su justificación.
6. `Laboratorio` Con el blog del MSRC sobre [cómo Microsoft se defiende de la inyección indirecta](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks), escribe tres escenarios concretos de inyección indirecta contra un agente de Foundry (un documento indexado en AI Search, una página traída por Bing y la salida de una herramienta MCP) y la capa de defensa que corresponde a cada uno: prompts endurecidos, spotlighting, Prompt Shields, consentimiento o bloqueo determinístico. Evidencia: ficha de una página para el comité.

<a id="f0"></a>

## F0 · Cómo usar este programa: la ruta integrada con los demás programas de la serie

*L100–L200 · ~2 h · Origen: Equivale al módulo «cómo aprender» de los Ninja oficiales; no existe Ninja oficial de Foundry ni de seguridad de IA (etiqueta «ninja training» de Tech Community revisada al 7 de noviembre de 2026)*

Este es un programa complementario: nace del análisis de la infografía «Secure Architecture for AI Agents — Microsoft Azure» frente a los programas 01 a 14 de la serie. De 110 elementos evaluados, incluidos 15 que la imagen omite, la serie cubría 35 de forma completa, 34 de forma parcial, 17 solo los mencionaba y 24 no los cubría. Identidad, postura, amenazas de IA y datos ya tenían programas con laboratorios; las brechas estaban en API Management, perímetro y red, guardrails y desarrollo de agentes. En la infografía, este módulo no asegura una capa concreta: es el **mapa transversal** de las capas 1 a 8 y de la banda de red.

La ruta integrada suma 315 horas en nueve fases (145 de este programa sin la comunidad y 170 de otros), pero nadie la recorre completa: cada rol toma sus filas. Un arquitecto de IA necesita unas 207 horas; un ingeniero de plataforma, 218; un desarrollador de agentes, 138; seguridad de datos, 107; el SOC, 124; y gobierno o CISO, 97. Con poco tiempo, la ruta mínima por rol va de 35 a 73 horas. El detalle elemento por elemento está en el documento de la serie «Plan integrado: arquitectura segura para agentes de IA en Azure» (archivo `Plan_Arquitectura_Segura_Agentes_IA_Azure.md`, en la carpeta raíz de la serie); aquí eliges tu ruta, tu credencial oficial y tu radar de novedades.

**Por qué importa**

Sin una ruta, los equipos repiten módulos que ya estudiaron en Entra o en Purview y se saltan lo que nadie enseña, como el AI gateway o el egreso de los agentes. Una ruta por rol reduce horas de formación, asigna cada capa de la arquitectura a un responsable y conecta el aprendizaje con credenciales verificables (SC-500, AI-103, SC-100 o AB-100), lo que facilita justificar la inversión ante la dirección.

**Qué vas a lograr**

- Ubicar cada capa de la infografía en el programa y el módulo de la serie que la cubren.
- Elegir tu ruta completa o mínima según tu rol y estimar sus horas.
- Definir la credencial oficial objetivo y mapear sus habilidades a módulos de este programa.
- Configurar un radar de novedades con una revisión extraordinaria después de Microsoft Ignite 2026.
- Saber a qué canal acudir según el tipo de duda: diseño, error del producto o estado de una función.

> **Atención.** No existe un Ninja oficial de Microsoft Foundry ni de seguridad de IA: la etiqueta «ninja training» de Tech Community reúne 49 publicaciones y la más reciente es «Become a Microsoft Defender Ninja», del 19 de octubre de 2026 ([etiqueta ninja training](https://techcommunity.microsoft.com/tag/ninja%20training)). Lo oficial más cercano es la ruta «Implement security for AI» (9 módulos, 3 h 59 min), que incluye módulos de Agent 365 y Copilot Studio que este programa no cubre ([ruta de Learn](https://learn.microsoft.com/en-us/training/paths/implement-ai-security/)); «Secure AI-ready infrastructure» todavía enseña el modelo de hubs ([ruta de Learn](https://learn.microsoft.com/en-us/training/paths/secure-ai-ready-infrastructure/)).

> **Novedad.** Ola de certificaciones 2026: AZ-500 se retiró el 31 de agosto de 2026 y lo reemplaza **SC-500** (Cloud and AI Security Engineer Associate), cuyo bloque «Implement security for AI» pide desplegar el AI gateway de API Management para Foundry, habilitar Defender for AI Services y configurar guardrails de agentes ([guía de SC-500](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500)); AI-102 dio paso a **AI-103** el 30 de junio de 2026 ([Skills Hub](https://techcommunity.microsoft.com/blog/skills-hub-blog/the-ai-job-boom-is-here-are-you-ready-to-showcase-your-skills/4494128)). SC-500 cuesta USD 165, dura 120 minutos y aún no tiene Practice Assessment ([certificación](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/)).

> **Consejo Ninja.** Desde el 27 de agosto de 2026, Learning Agent de Microsoft Copilot recomienda contenido de AI Skills Navigator, que ofrece playlists por rol y Practice Assessments de SC-100, AI-103 y AB-100 ([anuncio](https://techcommunity.microsoft.com/blog/skills-hub-blog/ai-skills-navigator-is-now-available-in-microsoft-copilot/4543633), [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/)). Úsalo junto con este programa, no en su lugar; el MVP Charbel Nemnom publica una guía de estudio de SC-500 ([guía comunitaria](https://charbelnemnom.com/sc-500-exam-study-guide/)).

> **Qué cambió.** Microsoft Ignite (17 al 20 de noviembre de 2026) cae después del corte de este programa y puede cambiar estados de guardrails de agentes, AI gateway, red administrada o Control Plane ([guía de seguridad en Ignite 2026](https://www.microsoft.com/en-us/security/blog/2026/09/30/secure-whats-next-your-guide-to-microsoft-security-at-microsoft-ignite-2026/)). Además, el temario nuevo de AB-100 rige desde el 16 de noviembre de 2026 ([AB-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100)). Agenda una revisión del programa después del evento.

**¿Tienes poco tiempo?**

- [Study guide for Exam SC-500: Implementing End-to-End Security Controls for Cloud and AI Workloads](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500) · Credencial
- [Implement security for AI](https://learn.microsoft.com/en-us/training/paths/implement-ai-security/) · Curso
- [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/) · Curso
- [What’s New – Category | Microsoft Foundry Blog](https://devblogs.microsoft.com/foundry/category/whats-new/) · Newsletter

**Ruta integrada en nueve fases (315 horas en total; cada rol toma solo sus filas)**

| Fase | Objetivo | Programas y módulos | Horas | Resultado |
|---|---|---|---|---|
| 1 · Fundamentos y modelo de amenazas | Entender Foundry, la arquitectura por capas corregida y el modelo de amenazas de los agentes | Este programa · P0, F0, F1, F2, F3 | 21 | Arquitectura de referencia corregida y modelo de amenazas del agente piloto |
| 2 · Identidad de agentes (capa 3) | Dominar tokens y OBO, identidades de carga de trabajo, Entra Agent ID, el ciclo de vida de los agentes y la frontera de Agent 365; aplicarlo a Foundry | Entra: identidad y agentes · P0, A1, X2, X3, X6 (31 h) y X1, X4 (8 h); este programa · F4, F5 (11 h) | 50 | Identidades de agente con sponsor y permisos mínimos, servidor MCP protegido con Entra y laboratorio de Foundry sin claves |
| 3 · Construir y ejecutar agentes seguros (capas 1, 2 y 4) | Desarrollar con Agent Framework, configurar el Agent Service y aplicar guardrails | Este programa · M1, M2, M3 | 21 | Agente con aprobación de herramientas, MCP gobernado y Prompt Shields para documentos |
| 4 · Tráfico, red y datos (capas 5 y 6 y banda de red) | Poner el AI gateway y la red Zero Trust delante y alrededor del agente; endurecer datos y gobernar modelos | Este programa · M4, M5 (15 h) y M6, M7 (12 h) | 27 | APIM con límites y validación de tokens; WAF, DDoS, private endpoints y egreso controlado; datos sin claves y modelos aprobados |
| 5 · Postura y protección de cargas (capas 6.5 y 7) | Operar la postura y la protección de amenazas de las cargas de IA y conectarlas con Foundry | Defender for Cloud · B1, B2, M2, A1, A2 (31 h) y M6, M7, M8 (17 h); este programa · A3 (6 h) | 54 | Defender CSPM con AI-SPM y Defender for AI Services con contexto de usuario en las alertas |
| 6 · Datos y cumplimiento (capa 8) | Proteger los datos que usan los agentes, investigar interacciones de IA y evidenciar el cumplimiento | Purview DSPM y seguridad de datos para IA · I2, M2, A2, A4 (23 h); Purview eDiscovery y Audit · A1 (4 h); Purview Compliance Manager · M3 (4 h); este programa · A4 (6 h) | 37 | Purview para Foundry con contexto de usuario, auditoría verificada y evaluación con plantillas de IA |
| 7 · Ingeniería avanzada | Evaluar antes de publicar, observar en producción, asegurar la cadena de suministro y acotar el multiagente | Este programa · A1, A2, A6, A7 | 25 | Red teaming y evaluaciones en CI/CD, trazas con OpenTelemetry, registro privado de MCP y límites de autoridad |
| 8 · Detección y respuesta (SOC) | Responder a alertas de cargas de IA dentro del alcance de licencias y contener incidentes de agentes de Foundry | Defender for Cloud · A3, A4, A5 (22 h); Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio · A4, A5, A8 (21 h); este programa · A5 (8 h) | 51 | Reglas de Sentinel y playbooks de contención con telemetría de APIM, WAF, trazas y Defender for AI Services |
| 9 · Gobierno, operación y proyecto integrador | Gobernar la IA en Azure, operar el ciclo de vida, controlar costos, ubicar la regulación de MCSA y cerrar con el proyecto integrador | Este programa · O1, O2, O3, O4 (20 h); Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio · O1, O6 (9 h) | 29 | Marco de gobierno, RACI, controles de costo y arquitectura de punta a punta con evidencias |

Fuente: análisis de cobertura de la serie y ruta integrada al 7 de noviembre de 2026 (documento «Plan integrado: arquitectura segura para agentes de IA en Azure»). Las filas del programa Defender for Cloud se evaluaron a partir de su temario.

**Ruta mínima por rol, si tienes poco tiempo**

| Rol | Ruta completa | Ruta mínima: módulos de este programa | Ruta mínima: módulos de otros programas | Horas mínimas |
|---|---|---|---|---|
| Arquitecto de IA y de nube | 207 h | F1, F2, F3, F4, M2, M4, M5, M6, A3, A4, O4 | Defender for Cloud · A1 | 73 h |
| Ingeniero de plataforma de IA y landing zones | 218 h | F4, F5, M2, M4, M5, M6, M7, A2 | Defender for Cloud · A1, A2 | 65 h |
| Desarrollador de agentes | 138 h | P0, F3, F4, M1, M2, M3, A1, A6 | Entra: identidad y agentes · X6 | 54 h |
| Seguridad de datos para IA | 107 h | F2, M6, A4 | Purview DSPM y seguridad de datos para IA · M2, A4; Purview Compliance Manager · M3 | 35 h |
| Analista e ingeniero de SOC | 124 h | F3, A2, A5 | Defender for Cloud · A2, A4; Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio · A5, A8 | 47 h |
| Gobierno, riesgo y cumplimiento de IA y CISO | 97 h | F2, F3, O1, O2, O3 | Entra: identidad y agentes · X4; Purview Compliance Manager · M3; Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio · O6 | 37 h |

Fuente: análisis de cobertura de la serie al 7 de noviembre de 2026, detallado en el documento «Plan integrado: arquitectura segura para agentes de IA en Azure». No se cuentan los prerrequisitos: el SOC llega con los niveles 1 y 2 de Microsoft Sentinel y Defender XDR; seguridad de datos, con la base de Purview Information Protection y Purview DLP; e identidad, con los niveles 1 y 2 de Entra. Credenciales oficiales sugeridas: [SC-500](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500), [AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [SC-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100) y [AB-100](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100).

### Documentación, cursos y credenciales

- [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/) · Curso · Oficial · Nuevo · Microsoft Global Skilling · Microsoft · nov 2026. Plataforma oficial de formación en IA con playlists por rol (incluida Security Professional), sesiones con coach de IA, credenciales (certificaciones, Applied Skills, Pro Badge) y prácticas de examen.

### Anuncios y blogs oficiales

- [What’s new in AI Skills Navigator: October 2026](https://techcommunity.microsoft.com/blog/skills-hub-blog/what%E2%80%99s-new-in-ai-skills-navigator-october-2026/4565287) · Blog oficial · Empleado de Microsoft · Nuevo · vaishalikartik (Microsoft) · Microsoft Tech Community (Skills Hub Blog) · 23 oct 2026. Novedades de AI Skills Navigator: sesiones con coach de IA, playlists destacadas por rol, reportes organizacionales de progreso y preparación integrada para certificaciones y Applied Skills.
- [AI Skills Navigator is now available in Microsoft Copilot](https://techcommunity.microsoft.com/blog/skills-hub-blog/ai-skills-navigator-is-now-available-in-microsoft-copilot/4543633) · Blog oficial · Empleado de Microsoft · Nuevo · Matt Erni · Microsoft Tech Community (Skills Hub Blog) · 27 ago 2026. El Learning Agent de Microsoft Copilot recomienda módulos, rutas, sesiones y credenciales de AI Skills Navigator (p. ej., «¿qué cursos me ayudan a asegurar mi agente de IA?») y guarda el progreso.

**Manos a la obra**

1. `Laboratorio` Arma tu ruta personal con la tabla «Ruta mínima por rol» de este módulo y el documento de la serie «Plan integrado: arquitectura segura para agentes de IA en Azure»: marca las filas de tu rol, los módulos que ya aprobaste en otros programas (por ejemplo Entra: identidad y agentes X2, X3 y X6; Defender for Cloud A1 y A2; Purview DSPM y seguridad de datos para IA M2 y A4) y las horas que te quedan. Evidencia: calendario semanal con módulos y horas, aprobado por tu líder.
2. `Laboratorio` Copia cada habilidad del bloque «Implement security for AI» de la [guía de SC-500](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-500) y asígnale el módulo que la cubre (AI gateway → [M4](02_Nivel_2_Intermedio.md#m4), guardrails de agentes → [M3](02_Nivel_2_Intermedio.md#m3), Defender for AI Services → [A3](03_Nivel_3_Avanzado.md#a3), Entra Agent ID → [F4](#f4)); si eres desarrollador, repite con la sección de seguridad de la [guía de AI-103](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103). Evidencia: matriz habilidad oficial → módulo → recurso, con tus tres temas más débiles marcados.
3. `Laboratorio` Crea tu perfil en [AI Skills Navigator](https://aiskillsnavigator.microsoft.com/), elige la playlist de tu rol y realiza la Practice Assessment disponible para tu credencial objetivo (SC-100, AI-103 o AB-100; SC-500 todavía no la tiene). Evidencia: resultado de la práctica y plan para los temas con menos aciertos.
4. `Laboratorio` Diseña tu radar de novedades: suscríbete por RSS al [resumen mensual del blog de Foundry](https://devblogs.microsoft.com/foundry/category/whats-new/) y a [Azure service updates](https://www.microsoft.com/releasecommunications/api/v2/azure/rss), y agrega [What's new in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/whats-new-foundry) sabiendo que va con desfase (el 30 de octubre de 2026 todavía resumía agosto). Define quién lo revisa, dónde registras cada cambio y una revisión extraordinaria después de Ignite (17 al 20 de noviembre de 2026). Evidencia: procedimiento de una página con responsable y registro «fecha, cambio, fuente, módulo afectado».
5. `Laboratorio` Define dónde pedir ayuda según el tipo de problema: el Discord de Microsoft Foundry, con más de 25.000 desarrolladores ([novedades de marzo de 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-mar-2026/)), las sesiones de Microsoft Reactor como [Secure and Govern Agents, MCP Servers, and AI Tools with AI Gateway](https://developer.microsoft.com/es-es/reactor/events/27397/) y los foros de soporte de tu contrato. Evidencia: tabla tipo de duda → canal → tiempo de respuesta esperado, compartida con el equipo.

<a id="f1"></a>

## F1 · Microsoft Foundry por dentro: recursos, proyectos, modelos, Agent Service y responsabilidad compartida

*L100–L200 · ~5 h · Origen: Nuevo en esta edición; se apoya en la tabla oficial de disponibilidad general del portal de Foundry, la documentación de Foundry Models y el modelo de responsabilidad compartida para agentes de IA de Microsoft Learn*

Microsoft Foundry organiza todo en tres ámbitos. El **recurso de Foundry** es el límite administrativo, de seguridad, de red y de monitoreo; el **proyecto** es un subámbito para organizar el trabajo y controlar el acceso; y el **agente** es el ámbito más estrecho, útil para dar acceso solo a su endpoint. La arquitectura baseline recomienda un recurso dedicado por carga de producción. El portal nuevo (ai.azure.com) está en GA y trabaja solo con proyectos de Foundry: los proyectos basados en hub y los recursos Azure OpenAI independientes siguen en Foundry (classic) hasta migrar. En la infografía, este módulo cubre la **Capa 2 · Despliegue y gobierno** y la base transversal de las demás capas.

Foundry Agent Service de nueva generación —la «Agent Service v2» de la infografía— está en GA desde el 16 de marzo de 2026 sobre la Responses API, y los hosted agents, desde el 9 de julio. Los agentes clásicos (Assistants) se retiran el 31 de marzo de 2027 y los workflows de Foundry, el 1 de diciembre de 2026. Los modelos vendidos por Azure tienen soporte, SLA y revisión de IA responsable de Microsoft; los de socios y comunidad los respalda su proveedor. Los despliegues Data Zone existen para EE. UU., la UE y APAC, no para América Latina. Y en agentes PaaS, instrucciones, herramientas, orquestación, memoria e identidad siguen siendo responsabilidad tuya.

**Por qué importa**

Las decisiones más caras de revertir se toman en la primera semana: tipo de despliegue y residencia, configuración básica o estándar, red privada desde el inicio y qué modelos se permiten. Conocer el modelo de recursos, las generaciones del servicio y las responsabilidades que conserva tu organización evita construir sobre funciones que se retiran, prometer una residencia que no existe en MCSA y suponer que Microsoft cubre controles que te corresponden.

**Qué vas a lograr**

- Explicar la jerarquía recurso, proyecto y agente de Foundry y el límite de seguridad que define cada uno.
- Distinguir la nueva generación de Foundry Agent Service de los agentes clásicos y planificar los retiros de 2026 y 2027.
- Elegir el tipo de despliegue de modelos según la residencia que exige tu organización en MCSA.
- Describir los compromisos de privacidad, el monitoreo de abuso y el Customer Copyright Commitment de los modelos vendidos por Azure.
- Repartir responsabilidades entre Microsoft y tu organización con el modelo de responsabilidad compartida para agentes.

> **Qué cambió.** Generaciones y retiros: los agentes clásicos (Assistants, threads y runs) se retiran el 31 de marzo de 2027 y la migración pasa a conversaciones y respuestas ([migración](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate)); los workflows de Foundry, en preview, se retiran el **1 de diciembre de 2026** y Microsoft recomienda Microsoft Agent Framework ([tabla de disponibilidad del portal](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability)); y los Connected Agents no existen en el servicio nuevo: se reemplazan por la herramienta A2A ([A2A](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent)).

> **Atención.** Hosted agents está en GA desde el 9 de julio de 2026, pero la página oficial de precios seguía mostrando **N/A** para vCPU-hora y GiB-hora al 7 de noviembre de 2026 ([precios de Foundry Agent Service](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/)). No cotices con tarifas de blogs de socios: valídalas con la calculadora o con tu equipo de cuenta. Crear agentes de prompt no tiene cargo; pagas tokens y herramientas.

> **Atención.** Residencia en MCSA: Data Zone existe para EE. UU., la UE y APAC (esta última en GA desde el 9 de julio de 2026); Global procesa en cualquier región; y los datos en reposo siempre quedan en la geografía designada ([tipos de despliegue](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types)). No hay Data Zone de América Latina: si tu regulador exige procesamiento local, evalúa Standard o Regional Provisioned en una región aceptada, confirma la disponibilidad del modelo y valida con Legal y privacidad.

> **Consejo Ninja.** Privacidad: prompts, respuestas y datos de entrenamiento no están disponibles para otros clientes ni para OpenAI, no mejoran sus modelos y se rigen por el DPA; con modified abuse monitoring aprobado no hay almacenamiento ni revisión humana y el recurso muestra `ContentLogging=false` en su vista JSON ([datos, privacidad y seguridad](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy)). La página vigente no indica un plazo de retención del monitoreo de abuso: no repitas cifras de versiones antiguas. Estos compromisos son para modelos vendidos por Azure; los de socios tienen términos propios ([Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview)).

**¿Tienes poco tiempo?**

- [Microsoft Foundry portal general availability overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability) · Documentación
- [AI agent shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent) · Documentación
- [Deployment types for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types) · Documentación
- [Foundry Agent Service + Microsoft Agent Framework Explained (Microsoft Mechanics)](https://www.youtube.com/watch?v=iR7_57lJOz8) · Video

**Estados y fechas clave de Foundry al 7 de noviembre de 2026**

| Componente | Estado | Fecha | Implicación de seguridad | Módulo |
|---|---|---|---|---|
| Foundry Agent Service, nueva generación (Responses API) | GA | 16-mar-2026 | Agentes y workflows exigen Entra ID; base de los controles del programa | M2 |
| Hosted agents | GA | 9-jul-2026 | Sandbox por sesión aislado por hipervisor; la página de precios muestra N/A | M2 |
| Agentes clásicos (Assistants, threads y runs) | Deprecados | Retiro: 31-mar-2027 | No aparecen en el portal nuevo; migrar a conversaciones y respuestas | M2 |
| Proyectos basados en hub y Azure OpenAI independiente | Solo en Foundry (classic) | — | No funcionan en el portal nuevo; planifica la migración | F1 |
| Workflows de Foundry | Preview en retiro | Retiro: 1-dic-2026 | Migrar a Microsoft Agent Framework o a Logic Apps | M1 |
| Connected Agents | No existen en el servicio nuevo | — | Usar la herramienta A2A (GA, protocolo 1.0) | M2 |
| Herramienta Fabric data agent | Deprecada | 6-nov-2026 | Reemplazo: Fabric IQ; no enseñarla como vigente | M2 |
| Memoria del agente | Preview | Desde 25-nov-2025 | Sin integración con VNet; Brazil South sí, México no | M2 |
| Guardrails para agentes | Preview | Desde 18-nov-2025 | Solo agentes de Foundry Agent Service; acción anotar y bloquear | M3 |
| Microsoft Copilot harness | Preview | 28-oct-2026 | Extiende los controles de egreso del guardrail a prompt agents | M3 |
| Operate (Overview, Assets, Compliance) y AI Gateway del portal | Preview | Tabla del 14-ago-2026 | No bases el cumplimiento solo en estas vistas | M7 |
| Data Zone APAC | GA | 9-jul-2026 | Hay Data Zone para EE. UU., la UE y APAC; no para América Latina | F1 |

Fuentes: [tabla de disponibilidad del portal](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability), [GA de Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-production-ready-secure-observable-ai-agents-with-real-time-voice-with-/4501074), [novedades de julio y agosto](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/), [migración](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate), [A2A](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent), [Fabric data agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/fabric), [memoria](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-memory), [guardrails](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview), [Copilot harness](https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/) y [tipos de despliegue](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types). Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estos estados.

### Documentación, cursos y credenciales

- [AI agent shared responsibility model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent) · Documentación · Oficial · Nuevo · Microsoft Learn · 26 ago 2026. Extiende el modelo de responsabilidad compartida a agentes SaaS, PaaS (p. ej. Foundry Agent Service) e IaaS con tres capas nuevas (orquestación, herramientas y acciones, memoria y estado) y una matriz cliente/Microsoft/compartida.
- [Microsoft Foundry portal general availability overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 ago 2026. Tabla oficial de qué está en GA y qué sigue en preview en el nuevo portal de Foundry (Operate, AI Gateway, guardrails de agentes, Foundry IQ, trazas en VNet) y qué queda en el portal clásico (hubs, Azure OpenAI independiente, Assistants).
- [Deployment types for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types) · Documentación · Oficial · Nuevo · Microsoft Learn · 12 ago 2026. Compara los tipos Global, Data Zone (EE. UU., UE, APAC), Standard regional, Provisioned, Batch y Developer, indicando dónde se procesan los datos y cómo restringir tipos con Azure Policy sobre sku.name.
- [Microsoft Foundry Models overview](https://learn.microsoft.com/en-us/azure/foundry/concepts/foundry-models-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jul 2026. Distingue los modelos vendidos por Azure (hospedados y vendidos por Microsoft bajo los Product Terms, con soporte, SLA y revisión de IA responsable) de los modelos de socios y comunidad (soportados por el proveedor, p. ej. Anthropic o Hugging Face).
- [Data, privacy, and security for Foundry Models sold by Azure in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy) · Documentación · Oficial · Nuevo · Microsoft Learn · 18 may 2026. Compromisos contractuales sobre prompts, respuestas, embeddings y datos de entrenamiento (no se comparten con otros clientes ni con OpenAI, no entrenan modelos), dónde se almacenan los datos con estado y cómo funciona el monitoreo de abuso.
- [Foundry Agent Service pricing](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/) · Documentación · Oficial · Microsoft Azure (precios). Precios de lista: crear y ejecutar agentes nativos (prompts y workflows) sin cargo adicional; se pagan tokens del modelo y herramientas: File Search USD 0,11/GB-día de vector storage (1 GB gratis), Code Interpreter USD 0,033/sesión, Web Search y Custom Search USD 14 por 1.000 transacciones.
- [Customer Copyright Commitment Required Mitigations](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/customer-copyright-commitment) · Documentación · Oficial · Microsoft Learn · 20 mar 2026. Mitigaciones que el cliente debe implementar para mantener la defensa contractual de Microsoft ante reclamaciones de propiedad intelectual sobre contenido de Azure OpenAI: metaprompt anti-infracción, informe de pruebas conservado y controles por caso de uso.
- [Foundry Hosted Agents (Microsoft Agent Framework hosting)](https://learn.microsoft.com/en-us/agent-framework/hosting/foundry-hosted-agent) · Documentación · Oficial · Microsoft Learn. Confirma que el servicio administrado Foundry Hosted Agents es GA y que cada agente desplegado obtiene su propia identidad de Entra; explica los protocolos Responses e Invocations.

### Anuncios y blogs oficiales

- [What’s New in Hosted Agents in Foundry Agent Service](https://devblogs.microsoft.com/foundry/hosted-agents-build26/) · Blog oficial · Empleado de Microsoft · Nuevo · Tina Schuchman, Pranav · Microsoft Foundry Blog (devblogs) · 2 jun 2026. Cada sesión de un hosted agent corre en un sandbox aislado por hipervisor con sistema de archivos persistente, identidad de agente de Entra aprovisionada automáticamente y trazas OpenTelemetry; ahora se despliega también desde código fuente.
- [What’s new in Microsoft Foundry | Build Edition](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-build-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Nick Brady · Microsoft Foundry Blog (devblogs) · 2 jun 2026. Resumen de Build 2026: hosted agents con sesiones en sandbox (GA prevista para inicios de julio), Toolboxes en preview, memoria en preview, Foundry IQ y, en confianza y evaluación, ASSERT, Agent Control Specification (ACS), Guided Guardrail Setup, Rubric, trazas, Agent Optimizer y Agent ROI.
- [Foundry Agent Service, Observability, and Foundry Portal Now Generally Available](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-production-ready-secure-observable-ai-agents-with-real-time-voice-with-/4501074) · Blog oficial · Empleado de Microsoft · Amanda Silver · Microsoft Tech Community (Microsoft Foundry Blog) · 16 mar 2026. Anuncio de GA del nuevo Foundry Agent Service (sobre Responses API), de evaluaciones, trazas y monitoreo en Foundry Control Plane y del portal de Foundry, con redes privadas y observabilidad.
- [Foundry Agent Service is GA: private networking, Voice Live, and enterprise-grade evaluations](https://devblogs.microsoft.com/foundry/foundry-agent-service-ga/) · Blog oficial · Empleado de Microsoft · Bala, Jeff, Nick (equipo de producto de Foundry) · Microsoft Foundry Blog (devblogs) · 16 mar 2026. Detalle técnico de la GA de Agent Service: runtime sobre Responses API, red privada BYO VNet sin egreso público extendida a MCP, AI Search y Fabric, y autenticación MCP por clave, Agent Identity, identidad administrada u OAuth passthrough.
- [What’s new in Microsoft Foundry: July and August 2026](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Nick Brady · Microsoft Foundry Blog (devblogs) · 9 sep 2026. Resumen de julio y agosto de 2026: Hosted Agents, integración con Voice Live y Toolboxes en GA, herramientas de Claude hospedadas en Azure, cambios de Model Router y SDK estables (Python y JS 2.5.0, Java 2.4.0; .NET 3.0.0 en preview).
- [GPT-5.6 now available in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/) · Blog oficial · Empleado de Microsoft · Nuevo · Tina Schuchman · Microsoft Azure Blog · 9 jul 2026. Anuncio de la GA de GPT-5.6, de la Data Zone de Asia-Pacífico y de los agentes de producción (hosted agents, toolboxes y publicación en Microsoft 365 Copilot y Teams).
- [Introducing the new hosted agents in Foundry Agent Service: secure, scalable compute built for agents](https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/) · Blog oficial · Empleado de Microsoft · Takuto, Jeff Hollan, Lakshmi · Microsoft Foundry Blog (devblogs) · 22 abr 2026. Explica el modelo de aislamiento de hosted agents: un sandbox con aislamiento por hipervisor por sesión, sistema de archivos persistente, identidad Entra por agente y soporte de BYO VNet para el tráfico saliente.
- [Build and run agents at scale with Microsoft Foundry at Build 2026](https://devblogs.microsoft.com/foundry/agent-service-build2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Tina Schuchman · Microsoft Foundry Blog (devblogs) · 2 jun 2026. Visión build/deploy/operate de la plataforma de agentes: Agent Framework estable, Toolboxes con un endpoint MCP administrado, hosted agents, publicación en Teams y Microsoft 365 Copilot, y trazas/evaluación con Agent Optimizer.
- [Introducing the Microsoft Copilot harness in Foundry Agent Service](https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/) · Blog oficial · Empleado de Microsoft · Vista previa · Nuevo · Jeff, Viswajeeet, Anthony (equipo de Foundry Agent Service) · Microsoft Foundry Blog (devblogs) · 28 oct 2026. Presenta en preview el Copilot harness administrado (skills, herramientas conectadas con autenticación y aprobaciones explícitas, subagentes) y la GA de la resiliencia de larga duración de hosted agents. *Nota:* Novedad de fines de octubre de 2026; revisar estado tras Ignite (17–20-nov-2026)

### Webinars, videos y podcasts

- [Microsoft AI Update September 2026 (John Savill's Technical Training)](https://www.youtube.com/watch?v=Ypzjqzoh6KY) · Video · Empleado de Microsoft · Nuevo · John Savill · YouTube · John Savill's Technical Training · 4 oct 2026. Repaso mensual de novedades de IA de Microsoft de septiembre de 2026, con énfasis en Foundry: controles de egreso de red para hosted agents, permisos administrados por la empresa para operaciones de agentes, A2A v1.0 y publicación de agentes en Microsoft 365 Copilot y Teams.
- [Foundry Agent Service + Microsoft Agent Framework Explained (Microsoft Mechanics)](https://www.youtube.com/watch?v=iR7_57lJOz8) · Video · Oficial · Nuevo · Microsoft Mechanics · YouTube · Microsoft Mechanics · may 2026. Demostración de despliegue de agentes desde VS Code a Foundry: Entra Agent ID por agente, sesiones en microVM aisladas, permisos acotados u OBO, trazas, publicación en Microsoft 365/Teams y grounding con Work IQ, Fabric IQ y Foundry IQ.

**Manos a la obra**

1. `Laboratorio` Con la [tabla de disponibilidad general del portal](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability) (14 de agosto de 2026), clasifica 15 capacidades que usará tu agente piloto (agentes, herramientas, toolboxes, guardrails para modelos y para agentes, memoria, monitoreo, trazas en VNet, Operate, AI Gateway, workflows) como GA, preview o en retiro, con su fecha. Evidencia: registro de estados con fecha y URL, que revisarás después de Ignite.
2. `Laboratorio` En tu laboratorio ([F5](#f5)) crea un recurso de Foundry y un proyecto, y documenta qué se configura en el recurso (red, cifrado, autenticación local, conexiones de recurso, límites de 100 recursos por región, 250 proyectos y 32 despliegues) y qué en el proyecto (agentes, conexiones de proyecto, identidad del proyecto), con la ayuda de [RBAC de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) y [cuotas y límites](https://learn.microsoft.com/hi-in/azure/foundry/foundry-models/quotas-limits). Evidencia: salida JSON de `az cognitiveservices account show` con las propiedades de seguridad resaltadas.
3. `Laboratorio` Caso de residencia: para un banco mexicano que exige que la inferencia no salga de una zona definida, compara Global Standard, Data Zone Standard y Standard con [tipos de despliegue](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types), y explica por qué no existe una Data Zone de América Latina. Crea en modo Audit la política personalizada que deniega `GlobalStandard` sobre `sku.name`. Evidencia: memorando de decisión de una página y asignación de la política.
4. `Laboratorio` Abre la vista JSON de tu recurso y busca la propiedad `ContentLogging`; con [datos, privacidad y seguridad](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy) y el [monitoreo de abuso](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/abuse-monitoring), documenta qué hace Microsoft con prompts marcados, quién los revisa y qué cambiaría con modified abuse monitoring aprobado. Evidencia: captura y nota de una página para privacidad y Legal.
5. `Laboratorio` Completa la matriz de [responsabilidad compartida para agentes](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility-ai-agent) para un prompt agent con AI Search y una herramienta MCP: 17 responsabilidades (datos, identidad, hosting del modelo, seguridad de contenido, instrucciones, herramientas, identidad del agente, autorización por acción, aprobación humana, orquestación, multiagente, memoria, egreso, auditoría, runtime, infraestructura y uso aceptable), quién la tiene y el dueño en tu organización. Evidencia: matriz firmada por arquitectura y seguridad.
6. `Laboratorio` Mira [Foundry Agent Service + Microsoft Agent Framework Explained](https://www.youtube.com/watch?v=iR7_57lJOz8) (Microsoft Mechanics) y [Microsoft AI Update September 2026](https://www.youtube.com/watch?v=Ypzjqzoh6KY) de John Savill, y lista cinco capacidades de seguridad que cambiaron de estado en 2026 con su fecha y el módulo de este programa que las trata. Evidencia: lista con fecha y fuente.

**¿Quieres profundizar?**

- [Microsoft AI Update September 2026 (John Savill's Technical Training)](https://www.youtube.com/watch?v=Ypzjqzoh6KY) · Video

<a id="f2"></a>

## F2 · La arquitectura segura por capas: análisis de la infografía y versión corregida

*L100–L200 · ~5 h · Origen: Nuevo en esta edición; analiza como material de estudio la infografía «Secure Architecture for AI Agents — Microsoft Azure» y la contrasta con la arquitectura baseline de Foundry, Zero Trust para IA y la documentación vigente*

La infografía resume en ocho capas y media una idea correcta: seguridad en cada capa, de Agent Framework a Purview, con una banda de red Zero Trust de punta a punta y ocho amenazas cubiertas. Acierta en la defensa en profundidad, en «un agente, una identidad», en API Management contra el abuso de recursos, en guardrails con PII y material protegido, y en aislar con VNet, private endpoints y egreso controlado, como la baseline de Foundry. Pero de sus 95 elementos, 26 son correctos tal cual, 52 correctos con matices, 9 imprecisos, 6 desactualizados y 2 incorrectos. Este módulo revisa **todas las capas**, con foco en los protectores de la **Capa 8**, la **Capa 6.5** y la **Capa 4**.

Los errores que más importan: «Agent Service v2», «AI Foundry Guardrails» y «Defender for AI» no son nombres oficiales; Defender for AI Services no tiene alertas de «data poisoning» ni de «model misuse»; «DDoS Std/Adv» no existe; los guardrails no reciben el tráfico desde APIM, sino que se aplican dentro de Foundry; y «Defender en todos los componentes» omite que no hay plan de Defender para Application Gateway y que, desde el 1 de julio de 2026, la seguridad a nivel de agente exige Agent 365. Además, sus ocho amenazas tocan solo 7 de 14 dominios: faltan cadena de suministro, egreso, shadow AI y la ceguera del SOC. Terminarás con la versión corregida.

**Por qué importa**

Una infografía atractiva se convierte rápido en la arquitectura «oficial» de un comité. Adoptada sin revisar, lleva a prometer controles que no existen (detección de envenenamiento), dejar apagados los que importan (Prompt Shields para documentos) y no presupuestar lo necesario (un WAF delante de APIM v2, Agent 365 o sus alternativas). Corregirla capa por capa produce una arquitectura de referencia defendible ante auditoría y un plan de trabajo priorizado.

**Qué vas a lograr**

- Mapear cada nombre de la infografía a su nombre vigente y a su estado (GA, preview o retirado), con fuente.
- Clasificar los elementos de la infografía en correctos, con matices, imprecisos, desactualizados e incorrectos.
- Corregir el protector de cada capa e identificar los componentes que no tienen plan de Defender.
- Reescribir los nueve flujos de conexión de la imagen con el camino real de cada solicitud y su evidencia.
- Producir el diagrama corregido de la arquitectura con el estado y la licencia de cada control.

> **Atención.** La lista de alertas de Defender for AI Services (actualizada el 6 de julio de 2026) incluye jailbreak bloqueado o detectado, robo de credenciales, URL maliciosas, ASCII smuggling, IP anonimizada o sospechosa, wallet attack (`DOWVolumeAnomaly` y `DOWDuplicateRequests`), acceso anómalo e invocación anómala de herramientas, pero **ninguna** llamada «data poisoning», «data leakage» o «model misuse» ([alertas de cargas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads)). El envenenamiento se mitiga con integridad del dato y permisos en el grounding ([M6](02_Nivel_2_Intermedio.md#m6)); la fuga, con Purview y egreso controlado ([M5](02_Nivel_2_Intermedio.md#m5)).

> **Qué cambió.** Desde el 1 de julio de 2026, el descubrimiento, la postura y la detección y el bloqueo de amenazas **a nivel de agente** de Foundry requieren Microsoft Agent 365: Defender CSPM sigue descubriendo cuentas y proyectos, Defender for AI Services sigue cubriendo los modelos, la tabla AIAgentsInfo pasó a AgentsInfo y las reglas de bloqueo de Agent 365 dejaron de bloquear ese día ([transición a Agent 365](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365)). Este programa no enseña Agent 365: marca la frontera y la alternativa dentro del alcance.

> **Atención.** «1 agente = 1 identidad» es correcto con matices y las fuentes se contradicen: la página de identidad de agente (28 de octubre de 2026) dice que cada agente nuevo recibe blueprint e identidad propios al crearse ([identidad de agente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)); la de gobierno de Entra Agent ID, que los agentes no publicados comparten la identidad por defecto del proyecto ([gobierno de Agent ID](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)); y la baseline, que los prompt agents usan la identidad administrada del proyecto para llegar a Cosmos DB, Storage y AI Search. Lo resuelves en [F4](#f4) y lo revalidas después de Ignite.

> **Consejo Ninja.** Para la versión corregida parte de la arquitectura baseline de Foundry: Application Gateway con WAF es el único recurso expuesto a internet, el resto usa private endpoints y todo el egreso de los agentes pasa por Azure Firewall con reglas FQDN ([baseline](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [implementación de referencia](https://github.com/Azure-Samples/microsoft-foundry-baseline)). Contrástala con el enfoque por capas de la plataforma de agentes de Microsoft (7 de octubre de 2026) ([Tech Community](https://techcommunity.microsoft.com/blog/microsoft-security-blog/the-microsoft-ai-and-agent-platform-%E2%80%94-securing-and-governing-intelligent-agents/4562204)) y con la lista de controles que en octubre de 2026 seguían en preview ([diseño multiagente, parte 1](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/global-enterprise-multi-agent-systems-in-production-design-and-security-part-1/4564913)).

**¿Tienes poco tiempo?**

- [Baseline Microsoft Foundry chat reference architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) · Documentación
- [Alerts for AI services (Microsoft Defender for Cloud)](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) · Documentación
- [The Microsoft AI and Agent Platform — Securing and Governing Intelligent Agents](https://techcommunity.microsoft.com/blog/microsoft-security-blog/the-microsoft-ai-and-agent-platform-%E2%80%94-securing-and-governing-intelligent-agents/4562204) · Blog oficial
- [New tools and guidance: Announcing Zero Trust for AI](https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/) · Blog oficial

**Versión corregida, capa por capa**

| Capa | Lo que muestra la infografía | Veredicto | Versión corregida (control y protector) | Módulos |
|---|---|---|---|---|
| 8 · Datos y cumplimiento | Purview (catálogo y linaje, clasificación, auditoría, eDiscovery, cumplimiento) con «Defender for Cloud Apps» como protector | Correcto con matices; protector impreciso | Purview para Foundry activado desde el Control Plane: Audit incluido, políticas con pago por uso o Agent 365, tokens de usuario y sin aislamiento de red; Defender for Cloud Apps sirve para shadow AI, no protege los datos de Foundry | M6, A4 |
| 7 · Postura | Defender for Cloud con CSPM, CIEM, CWPP y contenedores | Correcto | Defender CSPM con AI-SPM para cuentas y proyectos, Azure Policy de Foundry y modelos aprobados; la postura por agente exige Agent 365 | M7, A3 |
| 6.5 · «Defender for AI» | Detección de prompt injection, data poisoning y model misuse | Desactualizado; dos capacidades incorrectas | Plan Defender for AI Services de Defender for Cloud (capa 7): jailbreak, robo de credenciales, wallet attack, acceso anómalo, invocación anómala de herramientas; sin alertas de envenenamiento ni de mal uso | A3, A5 |
| 6 · Perímetro de red | Application Gateway con WAF, DDoS «Std/Adv», TLS y mTLS | Correcto con matices; DDoS desactualizado | WAF v2 con DRS 2.2, sin reglas de prompt injection y con exclusiones para chat; DDoS IP Protection o Network Protection; no hay plan de Defender para Application Gateway | M5 |
| 5 · Control de tráfico | APIM con cuotas, throttling, trazabilidad y Defender for APIs | Correcto con matices | Políticas llm-* (llm-token-limit y llm-content-safety con shield-prompt activado), identidad administrada hacia Foundry y registro de tokens; Defender for APIs solo cubre APIs de APIM y no inspecciona prompts | M4 |
| 4 · Seguridad de contenido | «AI Foundry Guardrails» con prompt injection, filtros, temas, copyright y PII; protector «Defender for Cloud» | Nombre desactualizado; protector impreciso | Guardrails de Microsoft Foundry: Prompt Shields para documentos activado a mano, PII y Task Adherence en preview, sin moderación de MCP; el protector correcto es Defender for AI Services, alimentado por Prompt Shields | M3 |
| 3 · Identidad y acceso | Entra ID con MFA y acceso condicional, OBO, mínimo privilegio y una identidad por agente; protector «Defender for Identity» | Correcto con matices; protector impreciso | Entra Agent ID por agente y sin permisos iniciales, RBAC de Foundry y autenticación sin claves; el acceso condicional y ID Protection para agentes exigen Agent 365 o E7; Defender for Identity protege a personas | F4 |
| 2 · Despliegue y gobierno | «Agent Service v2» con ejecución segura, OpenTelemetry, guardrails, identidad, versiones y «tenant isolation» | Nombre desactualizado; aislamiento impreciso | Foundry Agent Service en configuración estándar con recursos propios y aislamiento por proyecto; trazas en Application Insights; la autorización por usuario la implementa la aplicación | M2, A2 |
| 1 · Desarrollo | Agent Framework con multiagente, orquestación, memoria, middleware y MCP; protector «Defender for DevOps» | Correcto con matices; protector desactualizado | Microsoft Agent Framework 1.0 con aprobación de herramientas y middleware; DevOps security de Defender for Cloud con GitHub Advanced Security | M1, A6, A7 |
| Banda de red Zero Trust | DDoS, WAF, APIM, VNet con subredes, private endpoints, NSG y UDR, acceso privado a datos | Correcto con matices | Subred del agente definida al crear el recurso, DNS privado y egreso por Azure Firewall con FQDN; web search, Bing y SharePoint salen por endpoint público | M5, M6 |
| Cierre: seguridad «intrínseca» y Defender «en todo» | Entra, Defender, Purview, APIM y guardrails integrados desde el primer día | Impreciso | Muchos controles se activan a mano, se pagan aparte o están en preview, y la detección por agente exige Agent 365 | F2 |

Fuentes: análisis de la infografía (veredictos del 21 de octubre de 2026 revisados al 7 de noviembre de 2026); [Purview desde el Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security), [AI-SPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture), [Defender for AI Services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection), [alertas de cargas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads), [WAF en Application Gateway](https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview), [niveles de DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison), [Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction), [guardrails](https://learn.microsoft.com/en-us/azure/foundry/guardrails/guardrails-overview), [identidad de agente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity), [configuración estándar](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/standard-agent-setup), [GitHub Advanced Security en Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview) y [transición a Agent 365](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365).

**Los nueve flujos de la infografía: qué ocurre realmente en Azure**

| Flujo de la infografía | Veredicto | Qué ocurre en Azure | Control y evidencia | Módulo |
|---|---|---|---|---|
| 1. La telemetría de datos y auditoría fluye a Purview | Correcto con matices | Purview para Foundry se activa por suscripción desde el Foundry Control Plane; sin pago por uso ni Agent 365 solo funciona Audit, las políticas exigen tokens de usuario de Entra y no admite aislamiento de red | Interruptor de Purview y registros de Audit | A4 |
| 2. La postura y el contexto van a Defender for Cloud | Correcto con matices | Defender CSPM descubre cuentas y proyectos de Foundry, el AI BOM y rutas de ataque; la postura por agente exige Agent 365 desde el 1-jul-2026 | Recomendaciones y rutas de ataque de AI-SPM | A3, M7 |
| 3. La telemetría de seguridad de IA va a «Defender for AI» | Desactualizado | Es el plan Defender for AI Services: analiza prompts y respuestas de los despliegues de modelos con Prompt Shields e inteligencia de amenazas; el contexto del usuario final solo viaja con la API de Azure OpenAI | Alertas en Defender XDR con UserSecurityContext | A3, A5 |
| 4. Todo el tráfico entra por Application Gateway con WAF | Correcto con matices | Es la única entrada pública en la baseline, pero ninguna regla del WAF detecta prompt injection y el contenido de chat provoca falsos positivos | Registros del WAF y exclusiones acotadas al campo de mensajes | M5 |
| 5. APIM aplica políticas, cuotas y throttling | Correcto | Las políticas llm-* limitan tokens por consumidor (429 y 403); los tiers v2 de APIM no admiten DDoS Protection, así que el WAF va delante | Política llm-token-limit y ApiManagementGatewayLlmLog | M4 |
| 6. APIM envía las solicitudes a los guardrails | Impreciso | Los guardrails se aplican dentro de Foundry, en el despliegue o en el agente; APIM puede sumar llm-content-safety para cualquier backend, MCP y A2A, con shield-prompt apagado por defecto | Anotaciones del guardrail y 403 del gateway | M3, M4 |
| 7. Entra ID autentica y valida el JWT en cada salto | Correcto con matices | Solo si eliminas las claves: una API key da acceso total y evita el acceso condicional; la audiencia del token cambia entre el portal nuevo y el clásico; APIM y los servidores MCP deben validar la audiencia | disableLocalAuth, validate-azure-ad-token y registros de inicio de sesión | F4, M4 |
| 8. «Agent Service v2» ejecuta agentes con identidad administrada y guardrails | Desactualizado | Es Foundry Agent Service: cada agente nuevo tiene identidad de Entra Agent ID sin permisos; la plataforma usa la identidad del proyecto para sus dependencias; los guardrails de agente están en preview y no moderan MCP | Asignaciones de roles por identidad y guardrail asignado al agente | F4, M2, M3 |
| 9. Agent Framework orquesta con SDK, MCP y herramientas | Correcto con matices | Microsoft Agent Framework 1.0 (abril de 2026) ejecuta las herramientas sin aprobación por defecto; hay que marcar las de alto impacto y validar argumentos | Pruebas de aprobación y middleware de registro | M1 |

Fuentes: transcripción de la infografía y análisis de cobertura de la serie; [Purview desde el Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security), [AI-SPM](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture), [transición a Agent 365](https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365), [contexto del usuario final](https://learn.microsoft.com/en-us/azure/defender-for-cloud/gain-end-user-context-ai), [baseline](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [tiers v2 de APIM](https://learn.microsoft.com/en-us/azure/api-management/v2-service-tiers-overview), [llm-content-safety](https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy), [acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id), [identidad de agente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) y [Agent Safety](https://learn.microsoft.com/en-us/agent-framework/concepts/agents/safety).

**Lo que la infografía omite y dónde lo cubre la versión corregida**

| Elemento omitido | Por qué importa | Control en Azure | Estado o licencia | Módulo |
|---|---|---|---|---|
| Inyección indirecta y secuestro del objetivo | Es el vector más confiable contra agentes | Prompt Shields para documentos (apagado por defecto), Task Adherence, spotlighting en código | Prompt Shields GA; Task Adherence en preview | M3, M1 |
| Abuso de herramientas | Un agente manipulado actúa con sus permisos | Aprobación humana, allowed_tools explícito, mínimo privilegio por herramienta | GA | M1, M2 |
| Cadena de suministro (modelos, MCP, dependencias) | Un modelo o servidor MCP comprometido entra con los permisos del agente | Modelos aprobados con Azure Policy, registro privado de MCP en API Center, escaneo de modelos | Escaneo de modelos en preview | M7, A6 |
| Sobreexposición en RAG | El agente responde con datos que el usuario no debería ver | Filtros de seguridad por documento en AI Search y Foundry IQ con identidad del usuario | Filtros GA; ACL y etiquetas en preview | M6 |
| Claves robadas y LLMjacking | Una clave da acceso total y evita el acceso condicional | disableLocalAuth, Key Vault, alertas de IP anonimizada y acceso anómalo | GA | F4, O3 |
| Exfiltración por el egreso | Las herramientas pueden sacar datos a cualquier destino | Azure Firewall con FQDN, subred propia; web search no pasa por el firewall | GA; red administrada como no GA | M5 |
| Alucinaciones y propiedad intelectual | Riesgo legal y de reputación | Material protegido, Customer Copyright Commitment y evaluaciones | Groundedness detection se retira el 30-abr-2027 | M3, A1 |
| Shadow AI | Recursos y apps de IA sin control | AI-SPM, DSPM para IA y Defender for Cloud Apps | Programas Defender for Cloud y Purview DSPM | M7 |
| Ceguera del SOC | La infografía termina en «alerts & investigations» | Telemetría de Foundry, APIM, WAF y Defender en Sentinel con reglas y playbooks | Detecciones por agente con Agent 365 | A2, A5 |
| Agentes sin dueño ni ciclo de vida | Nadie responde por un agente comprometido | Inventario del Control Plane, sponsors y owners en Entra Agent ID | Operate en preview | M7, O2 |
| Evaluación antes de publicar | Sin umbrales no hay criterio para salir a producción | AI Red Teaming Agent, PyRIT y evaluadores en CI/CD | Escaneos de contenido disponibles; agénticos y programados en preview | A1 |

Fuentes: análisis de cobertura de la serie (catálogo de 14 dominios de amenazas); [Catalog of AI Attack Techniques](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques), [Prompt Shields](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields), [control de acceso por documento](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview), [baseline](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat), [alertas de cargas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) y [AI Red Teaming Agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent).

### Anuncios y blogs oficiales

- [Global enterprise multi-agent systems in production: Design and security (Part 1)](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/global-enterprise-multi-agent-systems-in-production-design-and-security-part-1/4564913) · Blog oficial · Empleado de Microsoft · Nuevo · Kapil Dhanger (dhangerkapil) · Microsoft Tech Community · Microsoft Foundry Blog · 26 oct 2026. Siete prácticas de diseño y seguridad de implementaciones reales con hosted agents: qué gestiona la plataforma (identidad por agente, sandbox por sesión, red privada, trazas) y qué sigue siendo del cliente (autorización de la aplicación, efectos de negocio, datos y evidencias).
- [The Microsoft AI and Agent Platform — Securing and Governing Intelligent Agents](https://techcommunity.microsoft.com/blog/microsoft-security-blog/the-microsoft-ai-and-agent-platform-%E2%80%94-securing-and-governing-intelligent-agents/4562204) · Blog oficial · Empleado de Microsoft · Nuevo · lmurthy (Microsoft) · Microsoft Tech Community (Microsoft Security Community Blog) · 7 oct 2026. Arquitectura de confianza por capas para la plataforma de agentes de Microsoft: preguntas de confianza (identidad, datos, herramientas, aprobación humana, aislamiento, auditoría) y controles en cada capa.
- [Advance Zero Trust for AI: New tools and guidance to secure AI agents and DevSecOps](https://www.microsoft.com/en-us/security/blog/2026/08/04/advance-zero-trust-for-ai-new-tools-and-guidance-to-secure-ai-agents-and-devsecops/) · Blog oficial · Empleado de Microsoft · Nuevo · Ron Pessner · Microsoft Security Blog · 4 ago 2026. Amplía Zero Trust for AI con chequeos de IA, SecOps e infraestructura en el Zero Trust Assessment, un pilar DevSecOps en el Workshop y guía sobre memoria de IA como frontera de seguridad.
- [New tools and guidance: Announcing Zero Trust for AI](https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/) · Blog oficial · Empleado de Microsoft · Mike Adams · Microsoft Security Blog · 19 mar 2026. Lanza Zero Trust for AI: pilar de IA en el Zero Trust Workshop (700 controles), pilares de Datos y Red en el Zero Trust Assessment y una arquitectura de referencia para IA basada en verificar explícitamente, mínimo privilegio y asumir brecha.
- [Secure agentic AI end-to-end](https://www.microsoft.com/en-us/security/blog/2026/03/20/secure-agentic-ai-end-to-end/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 20 mar 2026. Visión de RSAC 2026: Agent 365 como plano de control de agentes (GA el 1-may-2026, incluido en Microsoft 365 E7) y capacidades de Defender, Entra y Purview para asegurar agentes y sus fundamentos.
- [Agent Factory: Creating a blueprint for safe and secure AI agents](https://azure.microsoft.com/blog/agent-factory-creating-a-blueprint-for-safe-and-secure-ai-agents/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Yina Arenas · Microsoft Azure Blog · 17 sep 2025. Plantea el enfoque por capas de Microsoft para agentes confiables: identidad única, protección de datos por diseño, controles integrados, evaluación contra amenazas y supervisión continua, mapeados a capacidades de Foundry. *Nota:* Autora: Corporate Vice President, Microsoft Foundry. Usa el nombre anterior Azure AI Foundry; la asignación automática de Entra Agent ID que anunciaba como 'próxima' ya está disponible

### Comunidad: blogs, libros, newsletters y eventos

- [Zero Trust for AI: Rebuilding security controls for autonomous and agentic systems (e-book)](https://www.microsoft.com/en-us/security/security-insider/emerging-trends/zt4ai-book) · Libro · Empleado de Microsoft · Nuevo · TJ Cutting · Microsoft Security Insider · 31 jul 2026. Libro electrónico que explica qué supuestos de seguridad se rompen con agentes autónomos (humano en el bucle, fuentes confiables, privilegios) y cómo aplicar Zero Trust a identidad, memoria, herramientas y desarrollo.
- [Securing Microsoft Azure OpenAI (Wiley)](https://www.wiley.com/en-us/Securing+Microsoft+Azure+OpenAI-p-9781394291106) · Libro · MVP · Legado aún útil · Karl Ots · Wiley · mar 2025. Libro sobre seguridad de aplicaciones con Azure OpenAI: modelo de responsabilidad compartida para IA, MCSB, Azure Policy, control de acceso, red y OWASP LLM. *Nota:* Escrito antes del cambio de nombre a Microsoft Foundry y de Agent Service; los principios (MCSB, Policy, red, identidad) siguen válidos, pero los roles y nombres cambiaron (p. ej., Azure AI User → Foundry User)

**Manos a la obra**

1. `Laboratorio` Inventario de nombres: recorre las nueve capas y los «protectores» de la infografía y completa nombre en la imagen → nombre vigente → estado (GA, preview, retirado o inexistente) → fuente, usando la [tabla de disponibilidad](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability), las [alertas de cargas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads) y la [comparación de DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison). Evidencia: tabla de al menos 20 filas, contrastada con la tabla «Versión corregida, capa por capa» de este módulo.
2. `Laboratorio` Reescribe los nueve flujos de conexión de la imagen con el camino real de la solicitud, usando la tabla de flujos de este módulo: dónde se valida el token, dónde se aplica el guardrail (dentro de Foundry, no después de APIM), qué agrega [llm-content-safety](https://learn.microsoft.com/en-us/azure/api-management/llm-content-safety-policy) y qué registro deja cada salto. Evidencia: diagrama de secuencia corregido con control y registro por salto.
3. `Laboratorio` Corrige los protectores: para cada capa identifica el servicio que realmente protege cada componente y si existe un plan de Defender, con [Defender for APIs](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-apis-introduction) (solo APIs publicadas en APIM y sin inspección de prompts), [Defender for AI Services](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-threat-protection) y los [precios de Defender for Cloud](https://azure.microsoft.com/en-us/pricing/details/defender-for-cloud/). Evidencia: tabla capa → protector correcto → plan o licencia → precio de lista.
4. `Laboratorio` Lee el anuncio de [Zero Trust para IA](https://www.microsoft.com/en-us/security/blog/2026/03/19/new-tools-and-guidance-announcing-zero-trust-for-ai/) (19 de marzo de 2026) y el [libro electrónico](https://www.microsoft.com/en-us/security/security-insider/emerging-trends/zt4ai-book), y asigna a cada capa de la infografía un control concreto para cada principio: verificar explícitamente, mínimo privilegio y asumir la brecha. Evidencia: tabla de nueve filas y tres columnas con un control de Azure por celda.
5. `Laboratorio` Dibuja la versión corregida de la arquitectura a partir de la [baseline de Foundry](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat) y su [implementación de referencia](https://github.com/Azure-Samples/microsoft-foundry-baseline): usuario → Application Gateway WAF con DDoS → API Management → Foundry Agent Service en configuración estándar con tu VNet → herramientas por private endpoint o por el firewall de egreso → servicios de datos; a los lados, Defender for AI Services, Defender CSPM, Purview y Sentinel. Marca lo que está en preview y lo que exige Agent 365. Evidencia: diagrama v1 que reutilizarás en [F5](#f5) y en el proyecto integrador [O4](04_Nivel_4_Gobierno_y_operacion.md#o4).
6. `Laboratorio` Agrega las amenazas omitidas: con la tabla de elementos omitidos de este módulo y el [Catalog of AI Attack Techniques](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques), ubica en tu diagrama corregido dónde se previene, detecta y contiene cada una (cadena de suministro, egreso, shadow AI, ceguera del SOC, agentes sin dueño). Evidencia: diagrama anotado y lista de controles nuevos con su módulo.

**¿Quieres profundizar?**

- [Zero Trust for AI: Rebuilding security controls for autonomous and agentic systems (e-book)](https://www.microsoft.com/en-us/security/security-insider/emerging-trends/zt4ai-book) · Libro
- [Securing Microsoft Azure OpenAI (Wiley)](https://www.wiley.com/en-us/Securing+Microsoft+Azure+OpenAI-p-9781394291106) · Libro

<a id="f3"></a>

## F3 · Modelado de amenazas para agentes de IA: OWASP, MITRE ATLAS y la taxonomía de Microsoft

*L100–L200 · ~5 h · Origen: Nuevo en esta edición; se apoya en el OWASP Top 10 for LLM Applications 2025, el OWASP Top 10 for Agentic Applications 2026, MITRE ATLAS y la taxonomía de modos de fallo en sistemas agénticos del AI Red Team de Microsoft*

Modelar las amenazas de un agente es modelar un sistema que decide: además de los activos clásicos, proteges instrucciones, memoria, herramientas e identidades que actúan en tu nombre. Cuatro marcos dan el vocabulario: el **OWASP Top 10 for LLM Applications 2025** (de LLM01 Prompt Injection a LLM10 Unbounded Consumption, con versión en español); el **OWASP Top 10 for Agentic Applications 2026**, publicado el 9 de diciembre de 2025 (de ASI01 Agent Goal Hijack a ASI10 Rogue Agents); **MITRE ATLAS**, con datos v2026.10 y cadencia mensual; y la **taxonomía de modos de fallo agénticos** de Microsoft, cuya v2.0 suma siete modos. En la infografía, este módulo trabaja la columna **«Threats covered»** sobre todas las capas.

El Cloud Adoption Framework recomienda partir del método que ya usas, como STRIDE, y complementarlo con ATLAS y OWASP. Microsoft aporta además dos catálogos de Zero Trust del 1 de agosto de 2026: el **Catalog of AI Attack Techniques**, con 14 técnicas en cinco familias, y **AI Defense Capabilities**, con nueve familias de defensa y un dueño por función. El dato más útil de la v2.0 de la taxonomía: en 12 meses de red teaming, el bypass del humano en el circuito fue el fallo más explotado. Aquí construyes el modelo de amenazas del agente piloto que usarás en todo el programa y corriges las ocho amenazas de la infografía.

**Por qué importa**

Sin un modelo de amenazas compartido, cada equipo compra o configura controles por intuición y los auditores no pueden trazar el riesgo hasta el control. Mapear cada amenaza a un identificador de OWASP o ATLAS y a un control de Azure con dueño convierte la seguridad del agente en una lista verificable, prioriza el presupuesto donde el riesgo es mayor y da al SOC un vocabulario común para clasificar incidentes.

**Qué vas a lograr**

- Aplicar STRIDE a un agente de Foundry y complementarlo con OWASP LLM 2025, OWASP Agentic 2026 y MITRE ATLAS.
- Explicar los siete modos de fallo nuevos de la taxonomía v2.0 y su mitigación de diseño.
- Usar el Catalog of AI Attack Techniques y AI Defense Capabilities para pasar de amenaza a control y a dueño.
- Corregir las ocho amenazas de la infografía y agregar las que omite.
- Clasificar la severidad de un hallazgo con la escala de MSRC para IA.

> **Novedad.** La taxonomía de modos de fallo agénticos v2.0 (4 de junio de 2026) agrega siete modos: cadena de suministro agéntica, secuestro de objetivos, escalada de confianza entre agentes, ataque visual a agentes de uso de computadora, contaminación del contexto de sesión, abuso de MCP o plugins y divulgación de capacidades; además cita 99 CVE relacionadas con MCP publicadas en 2025 ([blog del AI Red Team](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/)). La v1.0 es del 24 de abril de 2025 ([whitepaper](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf)).

> **Qué cambió.** MITRE ATLAS publica datos con cadencia mensual: la release v2026.10 (v6.1.0) tiene 16 tácticas, 129 técnicas, 92 subtécnicas, 44 mitigaciones y 77 casos de estudio, y renombra «AI Supply Chain Compromise» como *Supply Chain Compromise* (AML.T0010) y la mitigación de AI BOM como *Maintain an AI Bill of Materials* (AML.M0023) ([releases de ATLAS](https://github.com/mitre-atlas/atlas-data/releases)). Cita siempre versión de datos y fecha; en marzo de 2026 se sumaron las subtécnicas de *Cost Harvesting* ([actualización de marzo](https://github.com/mitre-atlas/atlas-website/blob/main/public/content/update-files/2026-03.md)).

> **Atención.** El título del Top 10 agéntico dice «for 2026», pero OWASP lo publicó el 9 de diciembre de 2025: cítalo como «Top 10 for Agentic Applications 2026 (dic-2025)» ([OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)). Y cuidado con la sigla **ACS**: OWASP publica un *Agent Control Standard* y Microsoft una *Agent Control Specification* dentro del Agent Governance Toolkit, en public preview; no son lo mismo ([iniciativa agéntica de OWASP](https://genai.owasp.org/initiatives/agentic-security-initiative/), [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)).

> **Consejo Ninja.** Para clasificar hallazgos usa la escala de severidad de MSRC para IA, que gradúa por impacto la inyección de prompts, la perturbación de entradas, la divulgación inferencial y la manipulación de modelos; la inyección que solo afecta al atacante queda fuera de alcance ([MSRC AI bug bar](https://www.microsoft.com/en-us/msrc/aibugbar)). Para el comité, el video «Why do AI Agents Fail» de John Savill (26 de octubre de 2026) resume las causas en lenguaje de negocio ([video](https://www.youtube.com/watch?v=xKgY5vnzjMQ)).

**¿Tienes poco tiempo?**

- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · Documentación
- [Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) · Blog oficial
- [Catalog of AI Attack Techniques (CAAT)](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques) · Documentación
- [Build Secure AI Agents: Microsoft’s Stack, Your Innovation | BRK261](https://www.youtube.com/watch?v=GWV7VXjYeFM) · Video

**Las ocho amenazas de la infografía: control asignado y control correcto**

| Amenaza de la infografía | Referencia OWASP o ATLAS | Control que asigna la imagen | Control correcto en Azure | Cobertura previa en la serie | Módulos |
|---|---|---|---|---|---|
| Prompt injection | LLM01, ASI01 | Guardrails, Defender for AI y Defender por componente | Prompt Shields para usuario y documentos (documentos apagado por defecto), spotlighting en código, Defender for AI Services a nivel de modelo y llm-content-safety en APIM | Parcial | M3, M1, A1, A5 |
| Acceso no autorizado | ASI03 | Entra ID, mínimo privilegio y acceso condicional | Entra ID sin claves, RBAC de Foundry por persona y red privada; el acceso condicional para agentes exige Agent 365 o E7 | Parcial | F4, M5, M7 |
| Uso excesivo de recursos | LLM10; ATLAS Cost Harvesting | APIM con cuotas y throttling | llm-token-limit, cuotas, presupuestos y alertas DOWVolumeAnomaly y DOWDuplicateRequests | Mención | M4, M7, O3 |
| Envenenamiento de datos | LLM04, ASI06 | Detección de Defender for AI (no existe) | Integridad del grounding y de la memoria, permisos por documento y evaluaciones | Mención | M6, A1, A6 |
| Identidad comprometida | ASI03 | Entra ID con una identidad por agente, acceso condicional y riesgo | Agent ID con credencial federada y sin secretos, deshabilitar el blueprint; ID Protection para agentes con P2 en preview | Completa | F4, A5 |
| Ataques web y a APIs | OWASP API Top 10 | WAF, DDoS, TLS y Zero Trust | WAF v2 con DRS 2.2 (sin reglas de prompt injection), DDoS IP o Network Protection, TLS 1.2 o superior y Defender for APIs solo para APIs en APIM | Parcial | M5, M4 |
| Configuraciones erróneas y vulnerabilidades | LLM03 | Defender for Cloud | Defender CSPM con AI-SPM, Azure Policy de Foundry y modelos aprobados | Completa | M7, A3 |
| Fuga o mal uso de datos | LLM02 | Purview | Purview para Foundry (Audit; políticas con pago por uso o Agent 365), permisos por documento y egreso controlado | Completa | A4, M6, M5 |

Fuentes: [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/), [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [actualización de ATLAS de marzo de 2026](https://github.com/mitre-atlas/atlas-website/blob/main/public/content/update-files/2026-03.md), [alertas de cargas de IA](https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-ai-workloads), [acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id), [ID Protection para agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents) y [comparación de DDoS Protection](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-sku-comparison). La cobertura previa es la del análisis de la serie al 7 de noviembre de 2026.

### Documentación, cursos y credenciales

- [Catalog of AI Attack Techniques (CAAT)](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 ago 2026. Catálogo de 14 técnicas de ataque a IA en 5 familias (manipulación de instrucciones, estado y memoria, confianza y cadena de suministro, ejecución y autonomía, recursos y extracción) con controles y mapeo OWASP/MITRE.
- [AI Defense Capabilities for Enterprise AI Security](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 ago 2026. Complemento defensivo del CAAT: nueve familias de capacidades (gobierno y respuesta, cadena de suministro, identidad, higiene de entradas, endurecimiento del modelo, aislamiento, salida segura, monitoreo y forense, gobierno de recursos) alineadas con ATLAS, OWASP y NIST.
- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · Documentación · Comunidad · OWASP Agentic Security Initiative · OWASP GenAI Security Project · 9 dic 2025. Marco revisado por más de 100 expertos con los 10 riesgos de aplicaciones agénticas (ASI01 secuestro de objetivo, ASI02 uso indebido de herramientas, ASI03 abuso de identidad y privilegios… ASI10 agentes rebeldes).
- [OWASP Top 10 for LLM Applications 2025 (LLM Risks)](https://genai.owasp.org/llm-top-10/) · Documentación · Comunidad · OWASP Top 10 for LLM team · OWASP Gen AI Security Project · 18 nov 2024. Lista 2025 de riesgos para aplicaciones LLM (LLM01 inyección de prompts a LLM10 consumo no acotado) con versión oficial en español publicada el 12-mar-2025.
- [Taxonomy of Failure Mode in Agentic AI Systems (whitepaper v1.0)](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf) · Documentación · Empleado de Microsoft · Legado aún útil · Pete Bryan, Giorgio Severi, Mark Russinovich, Ram Shankar Siva Kumar y otros (Microsoft) · Microsoft AI Red Team · abr 2025. Versión original con modos de falla nuevos de sistemas multiagente (compromiso, inyección, suplantación y manipulación de flujo de agentes) y mitigaciones de identidad, endurecimiento de memoria, control de flujo, aislamiento, UX, logging y controles XPIA. *Nota:* La v2.0 (jun-2026) añade siete categorías; confirmar que el PDF descargado sea la versión vigente

### Anuncios y blogs oficiales

- [Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) · Blog oficial · Oficial · Nuevo · Microsoft AI Red Team · Microsoft Security Blog · 4 jun 2026. Explica los siete modos de falla nuevos; define el escalamiento de confianza entre agentes como un confused deputy inducido por lenguaje natural cuando el orquestador no verifica identidad ni permisos declarados por otro agente.
- [New whitepaper outlines the taxonomy of failure modes in AI agents](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Ram Shankar Siva Kumar · Microsoft Security Blog · 24 abr 2025. Presentación de la taxonomía v1.0: método de construcción, ejes nuevo/existente y seguridad/protección, y cómo usarla en el SDL y el modelado de amenazas. *Nota:* Actualizada por la v2.0 del 4-jun-2026

### Laboratorios, GitHub y herramientas

- [MITRE ATLAS data release v2026.10 (v6.1.0)](https://github.com/mitre-atlas/atlas-data/releases) · GitHub · Comunidad · Nuevo · MITRE ATLAS team · MITRE (GitHub mitre-atlas/atlas-data) · oct 2026. Versión más reciente de los datos de ATLAS: 16 tácticas, 129 técnicas, 92 subtécnicas, 44 mitigaciones y 77 casos de estudio, con nuevas técnicas de exfiltración por interfaz de IA y mitigaciones como «Maintain an AI Bill of Materials».

### Comunidad: blogs, libros, newsletters y eventos

- [OWASP Top 10 for Agentic Applications - The Benchmark for Agentic Security in the Age of Autonomous AI](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) · Blog · Comunidad · John Sotiropoulos, Keren Katz y Ron F. Del Rosario · OWASP Gen AI Security Project · 9 dic 2025. Artículo de lanzamiento que explica cada riesgo ASI con incidentes reales (EchoLeak, Amazon Q, exploit del MCP de GitHub) y menciona la revisión de líderes del Microsoft AI Red Team.
- [MITRE ATLAS Grows through Collaboration with CTID and Industry](https://ctid.mitre.org/blog/2026/05/06/secure-ai-v2-release/) · Blog · Comunidad · Nuevo · Mike Cunningham y Marissa Dotter · MITRE Center for Threat-Informed Defense · 6 may 2026. Resume la fase 2026 del proyecto Secure AI (con Microsoft entre los participantes): más de 45 técnicas nuevas, cadencia mensual, Knowledge Graph y emulación de amenazas para IA.

**Manos a la obra**

1. `Laboratorio` Modelo STRIDE + ATLAS: dibuja el flujo de un agente de Foundry con AI Search y una herramienta MCP, aplica STRIDE por elemento y mapea cada amenaza a OWASP LLM o ASI, a MITRE ATLAS y al [Catalog of AI Attack Techniques](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/catalog-ai-attack-techniques), como propone el [Cloud Adoption Framework](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/secure). Evidencia: matriz de al menos 15 amenazas con control y módulo, que reutilizarás en el proyecto integrador.
2. `Laboratorio` Para cada uno de los siete modos de fallo nuevos de la [taxonomía v2.0](https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/) escribe un escenario concreto en Foundry (por ejemplo, contaminación del contexto de sesión a través de la memoria o abuso de MCP mediante la descripción de una herramienta) y su mitigación de diseño (inventario de componentes del agente, versiones fijadas, descripciones tratadas como código). Evidencia: tabla de siete filas.
3. `Laboratorio` Corrige las ocho amenazas de la infografía con la tabla de este módulo y agrega las omitidas; usa el [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) y el [Top 10 agéntico](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) para asignar identificadores. Evidencia: tabla de 18 amenazas con identificador, control preventivo, detectivo y correctivo.
4. `Laboratorio` Asigna dueños con [AI Defense Capabilities](https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-defense-capabilities/catalog-ai-defense-capabilities): cada control de tu matriz va a arquitectura, ingeniería, operaciones de seguridad o riesgo; identifica al menos tres controles sin dueño. Evidencia: matriz con dueños y agenda para cerrar los vacíos.
5. `Laboratorio` Clasifica cinco hallazgos hipotéticos con la [escala de severidad de MSRC para IA](https://www.microsoft.com/en-us/msrc/aibugbar): un jailbreak que revela el prompt de sistema, una inyección indirecta que envía un correo con una herramienta, un LLMjacking con una clave filtrada, una inyección que solo afecta al propio atacante y un rug pull de un servidor MCP. Evidencia: tabla con severidad y justificación.
6. `Laboratorio` Mira [AI Red Teaming 101](https://www.youtube.com/watch?v=DwFVhFdD2fs) (episodios de inyección directa e indirecta) y la sesión de Ignite [Build Secure AI Agents (BRK261)](https://www.youtube.com/watch?v=GWV7VXjYeFM), y escribe cinco casos de ataque benigno que probarás en el laboratorio y en [A1](03_Nivel_3_Avanzado.md#a1), cada uno con su amenaza OWASP y su criterio de éxito. Evidencia: plan de pruebas versionado.

**¿Quieres profundizar?**

- [MITRE ATLAS data release v2026.10 (v6.1.0)](https://github.com/mitre-atlas/atlas-data/releases) · GitHub
- [OWASP Top 10 for Agentic Applications - The Benchmark for Agentic Security in the Age of Autonomous AI](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/) · Blog

<a id="f4"></a>

## F4 · Identidad y acceso en Foundry: Azure RBAC, identidades administradas, Entra Agent ID y autenticación sin claves

*L100–L200 · ~5 h · Origen: Nuevo en esta edición; complementa el programa Entra: identidad y agentes (módulos X2, X3 y X6) con lo propio de Foundry: roles, planos de control y de datos, autenticación sin claves e identidad de agente*

Foundry separa el **plano de control** (acciones de Azure RBAC sobre recursos, proyectos, red, cifrado, conexiones y despliegues) del **plano de datos** (*dataActions*: agentes, evaluaciones e inferencia). La página de RBAC del 16 de septiembre de 2026 documenta los nombres nuevos —Foundry User, Foundry Owner, Foundry Account Owner y Foundry Project Manager, antes Azure AI User, Owner, Account Owner y Project Manager, con los mismos IDs— y un rol nuevo, **Foundry Agent Consumer**, para solo invocar agentes, asignable incluso a un agente concreto. Con una clave API, en cambio, se obtiene acceso total, sin roles ni acceso condicional. En la infografía, este módulo asegura la **Capa 3 · Identidad y acceso** y la identidad de la **Capa 2 · Despliegue y gobierno**.

La identidad del agente es el punto con más matices. Según la página de Foundry del 28 de octubre de 2026, cada agente nuevo recibe un blueprint y una identidad de Microsoft Entra Agent ID, con credencial federada y **sin permisos**: tú concedes cada rol en el servicio destino. La guía de gobierno de Entra dice, en cambio, que los agentes no publicados comparten la identidad del proyecto, y la baseline usa la identidad administrada del proyecto para que la plataforma llegue a Cosmos DB, Storage y AI Search. Son dos planos distintos, y aquí aprendes a verificarlos. El acceso condicional para agentes exige Microsoft 365 E7 o Agent 365 con Entra ID P1: este programa enseña la alternativa.

**Por qué importa**

Las claves API están detrás de los casos de LLMjacking más conocidos, como el de Storm-2139, y anulan el acceso condicional, la auditoría por persona y el mínimo privilegio. Pasar a autenticación sin claves, asignar roles por persona con su GUID y conceder a cada agente solo lo que su herramienta necesita reduce el radio de impacto de una credencial robada o de un agente manipulado y deja evidencia auditable de quién hizo qué.

**Qué vas a lograr**

- Asignar roles de Foundry por persona con mínimo privilegio, usando los GUID en IaC, y validar el acceso efectivo.
- Deshabilitar la autenticación local con Azure Policy y verificar el corte con una respuesta 401.
- Localizar el blueprint y la identidad de un agente en Entra, concederle permisos mínimos y auditar sus inicios de sesión.
- Distinguir la identidad del agente para herramientas de la identidad administrada del proyecto para la plataforma.
- Explicar qué requiere Agent 365 o E7 (acceso condicional e ID Protection para agentes) y aplicar la alternativa dentro del alcance.

> **Qué cambió.** Roles renombrados con los mismos IDs: Foundry User `53ca6127-db72-4b80-b1b0-d745d6d5456d`, Foundry Owner `c883944f-8b7b-4483-af10-35834be79c4a`, Foundry Account Owner `e47c6f54-e4a2-4754-9501-8e0985b135e1` y Foundry Project Manager `eadc314b-1a2d-4efa-be10-5d325db5065e`; el nuevo Foundry Agent Consumer es `eed3b665-ab3a-47b6-8f48-c9382fb1dad6` y el portal solo lo asigna a nivel de cuenta, así que usa la CLI para proyecto o agente. No uses Azure AI Developer en proyectos de Foundry: aplica a hubs y Azure Machine Learning ([RBAC de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry)). Los nombres viejos conviven en plantillas: usa los GUID.

> **Atención.** Identidad de agente, dos versiones: la página de Foundry (28 de octubre de 2026) dice que cada agente nuevo recibe blueprint e identidad propios, que la identidad compartida del proyecto queda solo para agentes legacy y que su migración no transfiere asignaciones de roles ([identidad de agente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)); la guía de gobierno de Entra dice que los agentes no publicados comparten la del proyecto ([gobierno de Agent ID](https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview)). Además, el código de un hosted agent no puede usar la identidad administrada del proyecto. Compruébalo en tu laboratorio y revalídalo después de Ignite.

> **Atención.** Audiencia del token: el portal nuevo documenta el alcance `ai.azure.com/.default` y la versión clásica `cognitiveservices.azure.com/.default` ([autenticación y autorización](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry)); verifica cuál usa tu SDK. Y al deshabilitar las claves el corte no es inmediato: la puerta de enlace puede aceptarlas de minutos a horas, así que verifica con un 401 ([deshabilitar autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth)). PIM no puede hacer elegibles service principals ni identidades administradas ([PIM en Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration)).

> **Novedad.** Entra Agent ID está en GA desde Build 2026 y Foundry asigna la identidad automáticamente; los blueprints exigen sponsor (responsable de negocio) y recomiendan owner (configuración técnica) ([Tech Community](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606)). El acceso condicional para agentes requiere Microsoft 365 E7, o Agent 365 con Entra ID P1 o E3, y las claves API lo evitan por completo ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)); que el patrón OBO se gobierne con políticas sobre usuarios es una interpretación de esa página que conviene confirmar con licenciamiento. Se profundiza en el programa Entra: identidad y agentes, módulos X2, X3 y X6.

**¿Tienes poco tiempo?**

- [Role-based access control for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · Documentación
- [Agent identity concepts in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Documentación
- [Disable local authentication in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) · Documentación
- [Build AI agents for production with secure identities from day one](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606) · Blog oficial

**Roles de Foundry y mínimo privilegio**

| Rol | ID del rol | Alcance | Puede | No puede | Persona típica |
|---|---|---|---|---|---|
| Foundry Agent Consumer | eed3b665-ab3a-47b6-8f48-c9382fb1dad6 | Proyecto o agente (con la CLI; el portal solo lo asigna en la cuenta) | Interactuar con endpoints de agentes; lo exige el agente destino de la herramienta A2A | Crear o modificar agentes, gestionar modelos | Usuario final, app cliente u otro agente |
| Foundry User (antes Azure AI User) | 53ca6127-db72-4b80-b1b0-d745d6d5456d | Proyecto, más Reader en el recurso | Construir y probar agentes (dataActions) y leer recursos | Crear proyectos o cuentas, asignar roles, gestionar modelos, publicar | Desarrollador |
| Foundry Project Manager | eadc314b-1a2d-4efa-be10-5d325db5065e | Recurso | Crear y gestionar proyectos, construir y publicar agentes, asignar solo Foundry User | Crear cuentas, gestionar modelos | Líder técnico |
| Foundry Account Owner | e47c6f54-e4a2-4754-9501-8e0985b135e1 | Recurso | Crear cuentas y proyectos, gestionar modelos y conexiones, asignar Foundry User, activar Purview | Construir en proyectos (dataActions), publicar | Plataforma de IA |
| Foundry Owner | c883944f-8b7b-4483-af10-35834be79c4a | Recurso | Todo lo anterior, incluidos construir y publicar | Nada: es muy privilegiado | Equipos pequeños sin separación de funciones |
| Owner, Contributor y Reader de Azure | Roles integrados de Azure | Suscripción, grupo de recursos o recurso | Owner: todo el plano de control; Contributor: crear recursos y desplegar modelos; Reader: leer | Ninguno da dataActions de agentes | TI, automatización y auditoría |
| Cognitive Services Usages Reader | Rol integrado de Azure | Suscripción | Ver la cuota y validar despliegues | Nada más | Quien despliega modelos |
| Azure AI Developer | Rol integrado de Azure | Hubs y Azure Machine Learning | Trabajar en hubs (Foundry classic) | No aplica a proyectos de Foundry ni a hosted agents | No usar en Foundry |
| Owner o Resource Policy Contributor | Roles integrados de Azure | Suscripción o grupo de recursos | Asignar políticas de modelos y de guardrails | — | Gobierno de plataforma |
| Azure AI Enterprise Network Connection Approver | Rol integrado de Azure | Recurso destino | Aprobar los private endpoints de la red administrada | — | Identidad del recurso de Foundry |
| Agent ID Administrator y Agent ID Developer | Roles de Microsoft Entra | Tenant | Gestionar identidades de agente y crear blueprints | — | Identidad y desarrollo |
| Conditional Access Administrator | Rol de Microsoft Entra | Tenant | Crear políticas de acceso condicional para agentes (requieren E7, o Agent 365 con Entra ID P1) | — | Equipo de identidad |

Fuentes: [RBAC de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) (16 de septiembre de 2026), [cumplimiento y seguridad en el Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-manage-compliance-security), [red administrada](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network), [administración de identidades de agente](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) y [acceso condicional para identidades de agente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities). Usa los ID en IaC: los nombres antiguos conviven en portal, CLI y plantillas. Ninguna asignación elegible de PIM sirve para identidades administradas.

### Documentación, cursos y credenciales

- [Agent identity concepts in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 oct 2026. Explica blueprints e identidades de agente de Entra en Foundry: credencial federada sin secretos, intercambio de tokens en cuatro pasos, acceso solo-aplicación vs delegado (OBO), herramientas soportadas y auditoría en los registros de Entra.
- [Conditional Access for agents in Microsoft Entra](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Documentación · Oficial · Nuevo · Microsoft Learn · 30 sep 2026. Explica cómo Conditional Access evalúa a los agentes según el sujeto del token (OBO, solo aplicación o cuenta de usuario del agente) y cómo dirigir políticas a identidades o blueprints.
- [Role-based access control for Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) · Documentación · Oficial · Nuevo · Microsoft Learn · 16 sep 2026. Referencia de roles integrados de Foundry (Foundry Agent Consumer, User, Project Manager, Account Owner, Owner), alcances recurso/proyecto/agente, matriz de permisos y mapeos por persona para aislar funciones.
- [Disable local authentication in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jun 2026. Cómo forzar Entra ID deshabilitando las claves (política integrada, propiedad disableLocalAuth en Bicep/ARM o PowerShell) y cómo verificar que una clave antigua ya devuelve 401.
- [Authentication and authorization in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry) · Documentación · Oficial · Microsoft Learn. Separa plano de control (Azure RBAC actions: recursos, proyectos, red, cifrado, conexiones, despliegues) y plano de datos (dataActions: agentes, evaluaciones, inferencia) y compara Entra ID (tokens, CA, identidades administradas) con claves API (solo prototipos).
- [Eligible and time-bound role assignments in Azure RBAC (PIM integration)](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration) · Documentación · Oficial · Microsoft Learn. Con Entra ID P2 o Entra ID Governance, PIM permite asignaciones elegibles y temporales de roles de Azure (activación con MFA, justificación o aprobación) desde la página IAM.
- [Target agent identities in Microsoft Entra Conditional Access policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities) · Documentación · Oficial · Microsoft Learn. Paso a paso para crear políticas que apunten a todas las identidades de agente, a seleccionadas por atributos de seguridad o a blueprints, y a recursos registrados como aplicaciones empresariales (incluidos servidores MCP propios).
- [Assign Azure resource roles in Privileged Identity Management](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles) · Documentación · Oficial · Microsoft Learn. Paso a paso para hacer elegibles roles de recursos de Azure (Owner, User Access Administrator, Contributor y roles personalizados como los de Foundry) con duración, aprobación y condiciones ABAC.
- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Documentación · Oficial · Microsoft Learn. Opciones de licencia de Entra: P1 incluido en Microsoft 365 E3/E5/E7; P2 (necesario para PIM) incluido en Microsoft 365 E5/E7 y Defender Suite; Entra Suite (con ID Governance) incluida en E7. Las identidades administradas no requieren licencia.

### Anuncios y blogs oficiales

- [Build AI agents for production with secure identities from day one](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606) · Blog oficial · Empleado de Microsoft · Nuevo · ArLucaID (equipo de Microsoft Entra) · Microsoft Tech Community · Microsoft Entra Blog · 2 jun 2026. Explica los conceptos de Entra Agent ID (ya GA): blueprint, identidad por instancia con registros de inicio de sesión propios y 'kill switch', sponsors y owners, y los canales de aprovisionamiento (Foundry automático; Agent 365 CLI/SDK para otros frameworks).
- [Authorization and Identity Governance Inside AI Agents](https://techcommunity.microsoft.com/blog/microsoft-security-blog/authorization-and-identity-governance-inside-ai-agents/4496977) · Blog oficial · Empleado de Microsoft · ashwinijwaghmare7 · Microsoft Tech Community · Microsoft Security Community Blog · 25 feb 2026. Patrón para que la autorización la aplique el sistema de identidad (Entra ID y Graph) fuera del modelo y no instrucciones en el prompt; ejemplo con Copilot Studio y Power Automate trasladable a herramientas de agentes de Foundry.
- [Announcing Microsoft Entra Agent ID: Secure and manage your AI agents](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/announcing-microsoft-entra-agent-id-secure-and-manage-your-ai-agents/3827392) · Blog oficial · Empleado de Microsoft · Legado aún útil · Alex Simons · Microsoft Tech Community · Microsoft Entra Blog · 19 may 2025. Anuncio de la preview de Entra Agent ID en Build 2025 con el directorio unificado de identidades de agentes creadas en Azure AI Foundry y Copilot Studio. *Nota:* Hito histórico; hoy Agent ID es GA y el inventario converge con el registro de Agent 365

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Entra Agent ID Brings Real Governance to AI Agents, With One Important Catch](https://themicrosoftcloudblog.com/2026/04/microsoft-entra-agent-id-brings-real-governance-to-ai-agents-with-one-important-catch/) · Blog · Comunidad · Richard Hogan · The Microsoft Cloud Blog · 26 abr 2026. Análisis crítico de Entra Agent ID: el modelo de gestión, gobierno y protección es sólido, pero solo cubre agentes inscritos en Entra; los agentes informales quedan fuera del registro.

**Manos a la obra**

1. `Laboratorio` Roles por persona: en tu recurso y proyecto de laboratorio asigna con la CLI y los GUID de [RBAC de Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/rbac-foundry) Foundry Account Owner a un «gerente», Foundry User en el proyecto más Reader en el recurso a un «desarrollador» y Foundry Agent Consumer en el ámbito de un solo agente a una identidad de prueba; valida con *Check access* que el consumidor no ve otros agentes. Evidencia: comandos, exportación de asignaciones y captura de *Check access*.
2. `Laboratorio` Sin claves: asigna en modo Audit la política «Azure AI Services resources should have key access disabled» ([referencia de políticas](https://learn.microsoft.com/en-us/azure/ai-services/policy-reference)), revisa el cumplimiento, guarda una clave para la prueba negativa y aplica `disableLocalAuth` ([deshabilitar autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth)); mide cuánto tarda la clave en devolver 401 y luego pasa la política a Deny en un grupo de recursos de prueba. Evidencia: línea de tiempo con códigos HTTP y captura de cumplimiento.
3. `Laboratorio` Identidad de agente: crea un prompt agent, localiza su blueprint y su identidad en el centro de administración de Entra, filtra los inicios de sesión por tipo de agente y concédele solo Storage Blob Data Reader en un contenedor ([identidad de agente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity)); verifica que una herramienta con permiso funciona y otra sin permiso falla. Evidencia: capturas del blueprint, del registro filtrado y del resultado de la prueba.
4. `Laboratorio` Dos planos de identidad: en la configuración estándar compara los roles que recibió la identidad administrada del proyecto (Cosmos DB Operator, Storage Account Contributor, Search Index Data Contributor y otros) con los de la identidad del agente (ninguno hasta que los concedes), usando la [configuración estándar](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/standard-agent-setup) y la [baseline](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat). Evidencia: tabla comparativa y recomendación de aislamiento de dependencias.
5. `Laboratorio` Audiencia del token: obtén con `az account get-access-token` un token para cada alcance documentado en [autenticación y autorización](https://learn.microsoft.com/en-us/azure/foundry/concepts/authentication-authorization-foundry) y llama al endpoint del proyecto con cada uno; documenta cuál usa tu versión del SDK y qué error obtienes con el incorrecto. Evidencia: dos llamadas con su código HTTP y la versión del SDK.
6. `Laboratorio` PIM para roles de Azure: con Entra ID P2 de la prueba de Microsoft 365 E5, haz elegible Foundry Account Owner para tu cuenta de administración en el grupo de recursos, con MFA y justificación al activar ([PIM en Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/pim-integration), [asignar roles de recursos](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles)); intenta hacer elegible la identidad administrada del proyecto y documenta por qué no es posible. Evidencia: historial de activación y error documentado.
7. `Solo producción` Acceso condicional para identidades de agente: requiere Microsoft 365 E7, o Agent 365 con Entra ID P1 o E3, y agentes reales ([acceso condicional para agentes](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id)). Por qué en producción: el crédito de Azure no paga licencias y la prueba de Agent 365 queda fuera del alcance del programa. Cómo hacerlo seguro: política en modo solo informe dirigida a un blueprint piloto ([dirigir políticas a identidades de agente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-target-agent-identities)), cuentas de prueba, revisión de inicios de sesión antes de activarla y reversión deshabilitando la política. Mientras tanto aplica la alternativa: RBAC mínimo, sin claves, red privada y deshabilitar el blueprint como interruptor de emergencia. Evidencia: resultados del modo solo informe.

<a id="f5"></a>

## F5 · Laboratorio de práctica: un entorno de Foundry seguro con créditos de Visual Studio

*L100–L200 · ~6 h · Origen: Nuevo en esta edición; aplica el anexo de la serie «Anexo de laboratorio en Azure: Defender for Cloud y Foundry» y la matriz de laboratorio del programa*

Casi toda la arquitectura de este programa cabe en el crédito mensual de USD 150 de Visual Studio Enterprise si separas lo permanente de lo caro. Permanente y sin costo fijo: un recurso de Foundry AIServices S0 sin claves, un proyecto, un modelo económico como gpt-5-mini en GlobalStandard, Key Vault, Content Safety gratuito y AI Search Free. Por sesiones de 3 o 4 horas: la configuración estándar con red privada, API Management con red, Application Gateway WAF v2, Azure Firewall y DDoS IP Protection, que se borran al terminar. Este módulo construye el entorno en el que practicarás **todas las capas** de la infografía, de la 1 a la 8, y la banda de red.

Hay tres trampas. Application Insights figura entre las exclusiones del crédito y usarlo con el límite de gasto activo suspende la suscripción, así que las trazas van a OpenTelemetry local o a una segunda suscripción de pago por uso. Grounding with Bing no admite suscripciones de crédito patrocinado. Y Application Gateway, Azure Firewall y Private Link cobran la hora parcial como completa. Por eso trabajarás con etiquetas de expiración, presupuestos con alertas al 50, 75 y 90 % y un procedimiento de limpieza que purga la cuenta antes de borrar la VNet. La guía paso a paso está en el anexo de la serie (archivo `Anexo_Laboratorio_Azure_Defender_for_Cloud_y_Foundry.md`).

**Por qué importa**

Un laboratorio mal planificado termina en una suscripción suspendida a mitad de mes o en recursos caros encendidos sin dueño. Un entorno base sin claves, con presupuestos, etiquetas y sesiones acotadas te permite practicar cada control con evidencia real, repetir los ejercicios cuando Microsoft cambie un estado después de Ignite y ensayar la disciplina de costos que exigirás a los equipos de producción.

**Qué vas a lograr**

- Preparar la suscripción del crédito con proveedores registrados, grupos etiquetados y presupuestos con alertas.
- Desplegar un recurso de Foundry sin claves con un proyecto, un modelo económico con cuota baja y RBAC mínimo.
- Planificar las sesiones con tiempo limitado para los componentes caros y estimar su costo.
- Identificar lo que el crédito no paga y aplicar la alternativa: OpenTelemetry local o una suscripción de pago por uso.
- Ejecutar el procedimiento de limpieza y purga sin dejar costos residuales.

> **Atención.** Application Insights figura entre las exclusiones del crédito de Visual Studio, y usar un servicio excluido con el límite de gasto activo suspende la suscripción por el resto del periodo ([crédito para suscriptores de Visual Studio](https://azure.microsoft.com/en-us/pricing/member-offers/credit-for-visual-studio-subscribers/), [límite de gasto](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/spending-limit)). La plantilla oficial 15 de red privada crea siempre Application Insights: ejecútala en la suscripción de pago por uso o quita ese módulo de tu copia y documenta el cambio.

> **Consejo Ninja.** Modelo y presupuesto del laboratorio, según el anexo de la serie: gpt-5-mini (2025-08-07) en GlobalStandard con capacidad 10 cuesta USD 0,25 por 1M de tokens de entrada y USD 2 por 1M de salida, con retiro previsto el 13 de julio de 2027, mientras gpt-4o-mini y gpt-4.1-mini ya figuran como obsoletos. Crea un presupuesto mensual de USD 120 (80 % del crédito) con alertas al 50, 75 y 90 % y una pronosticada al 100 %; en una suscripción nueva puede tardar hasta 48 horas en estar disponible y sus alertas avisan, pero no detienen recursos ([presupuestos](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)).

> **Atención.** Regiones: el laboratorio usa East US 2 porque admite la plantilla 15, el red teaming en la nube y el tier AI Gateway. Para MCSA ten presente que la plantilla de red privada admite `brazilsouth` pero no `mexicocentral`, que la red administrada incluye Brazil South pero no México y que las regiones de despliegue completo de AI Landing Zones no incluyen la región ([AI Landing Zones](https://github.com/Azure/AI-Landing-Zones), [red administrada](https://learn.microsoft.com/en-us/azure/foundry/how-to/managed-virtual-network)). En producción, la residencia depende de toda la ruta: gateway, backends y registros.

**¿Tienes poco tiempo?**

- [Disable local authentication in Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth) · Documentación
- [Foundry Agent Service pricing](https://azure.microsoft.com/en-us/pricing/details/foundry-agent-service/) · Documentación
- [microsoft-foundry/foundry-samples · 15-private-network-standard-agent-setup](https://github.com/microsoft-foundry/foundry-samples/tree/main/infrastructure/infrastructure-setup-bicep/15-private-network-standard-agent-setup) · GitHub
- [Configure tracing for AI agent frameworks (preview)](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-framework) · Documentación

**Perfiles del laboratorio y sesiones con tiempo limitado**

| Perfil o sesión | Qué incluye | Costo estimado con el crédito | Fuera del crédito | Módulos |
|---|---|---|---|---|
| Perfil mínimo | Foundry sin claves, modelo y guardrails, herramientas sin red privada, Agent Framework local, AI gateway creado desde Foundry, un escaneo pequeño de red teaming, trazas locales, Defender y Sentinel en prueba | ≈ USD 12 al mes | Nada | F4, F5, M1, M3, M4 |
| Perfil recomendado | Mínimo, más cuatro sesiones de red privada, una de APIM Standard v2, dos escaneos en la nube, Defender CSPM y Purview con la prueba de E5 | ≈ USD 35 al mes | Application Insights (0 a 2 USD) y Security Copilot opcional (≈ USD 12 por sesión de 3 h) | M2, M5, M6, A1, A3, A4 |
| Perfil completo por sesiones | Recomendado, más WAF v2, Firewall Basic y DDoS IP Protection por sesiones; DDoS Network Protection opcional | ≈ USD 48 al mes (≈ 64 con DDoS Network Protection) | Igual que el recomendado | M5, A5 |
| Sesiones S1 y S2: red privada (4 h cada una) | Plantilla 15, AI Search Basic, endpoints privados y jumpbox | ≈ USD 1,5 por sesión | Application Insights que crea la plantilla | M2, M5, M6 |
| Sesión S3: APIM Standard v2 con red (4 h) | Integración con VNet y endpoint privado hacia el Foundry privado | ≈ USD 4 | — | M4 |
| Sesión S4: WAF v2 y DDoS IP Protection (4 h) | Detección y luego Prevención, exclusiones y métricas de DDoS sin tráfico de ataque | ≈ USD 3,5 | — | M5 |
| Sesión S5: egreso con Firewall Basic (3 h) | Ruta 0.0.0.0/0, reglas FQDN y registros | ≈ USD 1,5 | — | M5 |
| Sesión S7: red teaming y evaluaciones (2 h) | Escaneo en la nube en East US 2 contra el despliegue de prueba; evaluaciones de seguridad a USD 20 y 60 por 1M de tokens de entrada y salida | ≈ USD 5 a 10 | — | A1 |

Fuente: «Anexo de laboratorio en Azure: Defender for Cloud y Foundry» de la serie (estimaciones con precios de lista en USD al 7 de noviembre de 2026; confirma en la calculadora). Precios: [Application Gateway](https://azure.microsoft.com/en-us/pricing/details/application-gateway/), [Azure Firewall](https://azure.microsoft.com/en-us/pricing/details/azure-firewall/), [DDoS Protection](https://azure.microsoft.com/en-us/pricing/details/ddos-protection/), [API Management](https://azure.microsoft.com/en-us/pricing/details/api-management/), [Private Link](https://azure.microsoft.com/en-us/pricing/details/private-link/) y [observabilidad de Foundry](https://azure.microsoft.com/en-us/pricing/details/foundryobservability/). Application Gateway, Azure Firewall y Private Link cobran la hora parcial como completa.

**Manos a la obra**

1. `Laboratorio` Prepara la suscripción del crédito: registra los proveedores Microsoft.CognitiveServices, Microsoft.App, Microsoft.Search, Microsoft.Network, Microsoft.KeyVault, Microsoft.Storage y Microsoft.ContainerService; crea `rg-lab-fdy-base`, `rg-lab-fdy-gw` y `rg-lab-fdy-mcp` con la etiqueta `programa=foundry-sec`; y crea un [presupuesto](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets) de USD 120 con alertas al 50, 75 y 90 % y otro de USD 20 para los grupos de red y de borde. Evidencia: `az provider show` en estado Registered, lista de grupos filtrada por etiqueta y captura de los presupuestos.
2. `Laboratorio` Foundry sin claves: crea `aif-lab-fdy-eus2` (AIServices S0, con identidad asignada y gestión de proyectos) y el proyecto `prj-lab-fdy`; asigna Foundry User por GUID en el ámbito del proyecto; guarda una clave para la prueba negativa y deshabilita la autenticación local ([deshabilitar autenticación local](https://learn.microsoft.com/en-us/azure/ai-services/disable-local-auth)). Evidencia: `properties.disableLocalAuth` en `true`, respuesta 401 con la clave y 200 con Entra ID.
3. `Laboratorio` Modelo y cuota: despliega `gpt-5-mini` en GlobalStandard con capacidad 10 y un segundo despliegue `gpt-5-mini-rt` como objetivo de red teaming; asigna en Audit la política de modelos aprobados con un asset ID terminado en `/` ([políticas de despliegue de modelos](https://learn.microsoft.com/en-us/azure/foundry/how-to/model-deployment-policy)) y espera 15 minutos antes de probar. Evidencia: lista de despliegues con su capacidad y estado de cumplimiento de la política.
4. `Laboratorio` Batería de ataques benignos: crea un archivo versionado con un canario de jailbreak (por ejemplo, una palabra secreta en las instrucciones y diez paráfrasis en español para intentar que la revele), un documento con instrucciones ocultas, una descripción de herramienta envenenada para tu servidor MCP de prueba y un script de abuso de tokens; define reglas de enfrentamiento (solo tus recursos, datos sintéticos, aviso previo al SOC) siguiendo la [guía de planificación de red teaming](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/red-teaming). Evidencia: repositorio con la batería y correo de aviso al SOC.
5. `Laboratorio parcial` Trazas sin Application Insights: en una ejecución local de Agent Framework activa `AZURE_EXPERIMENTAL_ENABLE_GENAI_TRACING=true` con `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=false` y exporta a la consola o por OTLP a Aspire Dashboard ([trazas con Agent Framework](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-framework)). Limitación: Application Insights está excluido del crédito; si lo necesitas, créalo en la suscripción de pago por uso con un límite diario. Evidencia: spans del agente, del modelo y de cada herramienta sin texto de prompts.
6. `Laboratorio` Plan de sesiones: con la tabla de perfiles de este módulo y los precios de lista de [Application Gateway](https://azure.microsoft.com/en-us/pricing/details/application-gateway/), [Azure Firewall](https://azure.microsoft.com/en-us/pricing/details/azure-firewall/) y [Private Link](https://azure.microsoft.com/en-us/pricing/details/private-link/), agenda las sesiones de red privada, APIM con red, WAF, egreso y red teaming del mes; cada una con etiqueta `expira`, plantilla guardada para recrearla y dueño. Evidencia: calendario de sesiones con costo estimado frente al presupuesto.
7. `Laboratorio` Limpieza y purga: ensaya el procedimiento del anexo de la serie en el orden correcto (eliminar la cuenta de Foundry, listarla entre las eliminadas, purgarla con Contributor en la suscripción, esperar unos 20 minutos a que se libere la subred y recién entonces borrar el grupo) y comprueba que no queda nada con `az resource list --tag programa=foundry-sec`. Evidencia: script de limpieza, salida vacía y revisión de Cost Management al día siguiente.

<a id="reto-inicial"></a>

## Reto del nivel

**Arquitectura de referencia corregida y laboratorio base.** Con tu equipo, entrega: (1) el entorno base de [F5](#f5) sin claves (prueba de 401 con la clave antigua), con RBAC por persona asignado por GUID y presupuestos con alertas; (2) el diagrama corregido de la infografía ([F2](#f2)) con el nombre vigente, el estado (GA o preview) y la licencia de cada control, incluida la frontera de Agent 365 y E7; (3) el modelo de amenazas del agente piloto ([F3](#f3)) con al menos 15 amenazas mapeadas a OWASP LLM o agéntico y a MITRE ATLAS, con control y dueño; (4) la matriz de responsabilidad compartida ([F1](#f1)) firmada por arquitectura y seguridad; y (5) la ruta por rol y la credencial objetivo de cada integrante ([F0](#f0)). Formato: informe de tres páginas, el diagrama y una presentación de 10 minutos al comité de arquitectura.

<a id="quiz-inicial"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-inicial). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué describe correctamente a la nueva generación de Foundry Agent Service?
   - a) Un SDK de código abierto que solo se ejecuta en tu equipo
   - b) El runtime administrado de agentes de Foundry, basado en la Responses API
   - c) El nombre nuevo de Copilot Studio para desarrolladores profesionales de agentes
   - d) Una API de Azure OpenAI limitada a Assistants y threads

2. En un proyecto de Foundry con red aislada, ¿qué herramienta del agente sigue saliendo por un endpoint público?
   - a) Azure AI Search
   - b) Un servidor MCP privado en tu subred
   - c) Code Interpreter
   - d) Grounding with Bing Search

3. ¿Qué examen reemplazó a AZ-500, retirado el 31 de agosto de 2026?
   - a) SC-500 (Cloud and AI Security Engineer Associate)
   - b) SC-100 (Cybersecurity Architect Expert)
   - c) AI-103 (Developing AI Apps and Agents on Azure)
   - d) SC-401 (Information Security Administrator Associate)

4. Al 7 de noviembre de 2026, ¿existe un Ninja oficial de Microsoft dedicado a la seguridad de Foundry o de la IA?
   - a) Sí: el «Foundry Security Ninja», publicado en 2026
   - b) Sí: un módulo de IA dentro del último Ninja de Defender
   - c) No: lo más cercano son rutas de Learn y la certificación SC-500
   - d) Sí: el «AI Ninja», con certificado oficial dentro de AI Skills Navigator

5. Un banco de México exige que la inferencia no salga de una zona definida. ¿Qué es correcto?
   - a) Existe una Data Zone de América Latina
   - b) Global Standard garantiza el procesamiento en la región del recurso
   - c) Data Zone solo existe para EE. UU., la UE y APAC
   - d) El tipo Developer garantiza la residencia de los datos

6. ¿Qué ocurre el 1 de diciembre de 2026 en Microsoft Foundry?
   - a) Se retiran los workflows de Foundry
   - b) Los hosted agents pasan a disponibilidad general
   - c) Se retiran los agentes clásicos (Assistants)
   - d) Cambian de nombre los roles Azure AI User

7. En el modelo de responsabilidad compartida para agentes PaaS como Foundry Agent Service, ¿qué conserva siempre el cliente?
   - a) El hosting del modelo base y sus pesos
   - b) La aprobación humana de las acciones de alto impacto
   - c) La seguridad de la infraestructura física de los centros de datos
   - d) El runtime del agente y el hosting de sus contenedores

8. La infografía atribuye a «Defender for AI» la detección de «data poisoning» y «model misuse». ¿Qué es correcto?
   - a) Ambas alertas existen desde 2025 en Defender for AI Services
   - b) Solo existe la alerta de data poisoning, en preview
   - c) Ninguna de las dos existe como alerta de Defender for AI Services
   - d) Ambas existen, pero solo se activan con una licencia de Agent 365 por usuario

9. Desde el 1 de julio de 2026, ¿qué capacidad de seguridad para Foundry requiere Microsoft Agent 365?
   - a) Defender for AI Services para modelos como Azure OpenAI
   - b) El descubrimiento de cuentas y proyectos de Foundry en Defender CSPM con AI-SPM
   - c) Los guardrails de Foundry
   - d) El descubrimiento, la postura y la detección de amenazas a nivel de agente

10. En el OWASP Top 10 for Agentic Applications, publicado el 9 de diciembre de 2025, ¿qué riesgo es ASI04?
   - a) Agent Goal Hijack
   - b) Agentic Supply Chain Vulnerabilities
   - c) Rogue Agents
   - d) Cascading Failures

11. Según la v2.0 de la taxonomía de modos de fallo agénticos de Microsoft, ¿cuál fue el fallo más explotado en 12 meses de red teaming?
   - a) La fuga del prompt de sistema
   - b) El bypass del humano en el circuito
   - c) El agotamiento de la cuota de tokens
   - d) El ataque visual a agentes de uso de computadora

12. ¿Qué rol permite solo interactuar con el endpoint de un agente concreto?
   - a) Foundry User
   - b) Azure AI Developer
   - c) Cognitive Services OpenAI User asignado en el proyecto
   - d) Foundry Agent Consumer en el ámbito del agente

13. Deshabilitaste la autenticación local de un recurso de Foundry durante un incidente. ¿Qué haces antes de darlo por contenido?
   - a) Nada: el corte de las claves es inmediato y definitivo
   - b) Reiniciar el recurso para forzar el cambio
   - c) Verificar que la clave antigua devuelva 401
   - d) Eliminar el proyecto y crear uno nuevo

14. ¿Qué licencia exige el acceso condicional dirigido a identidades de agente?
   - a) Entra ID P1 sin otros complementos
   - b) Microsoft 365 E5 con Entra ID P2 y Defender for Identity
   - c) Workload ID Premium para cada agente
   - d) Microsoft 365 E7, o Agent 365 con Entra ID P1 o E3

15. ¿Por qué el laboratorio envía las trazas a OpenTelemetry local o a una suscripción de pago por uso?
   - a) Porque Application Insights está excluido del crédito de Visual Studio
   - b) Porque Foundry no admite Application Insights como destino
   - c) Porque las trazas de agentes solo funcionan en la región Brazil South de Azure
   - d) Porque OpenTelemetry está prohibido en suscripciones de pago

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD y sin impuestos, y cambian: confírmalos en la calculadora de precios de Azure antes de presupuestar. La infografía analizada pertenece a su autor y se usa solo como material de estudio. El contenido regulatorio y de privacidad es una referencia y no constituye asesoría legal: las decisiones corresponden a tus áreas de Legal, privacidad y cumplimiento. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

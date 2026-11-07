# Comunidad · Referentes, canales y cómo mantenerse al día

*Microsoft Security Copilot Ninja Training: hacia el SOC agéntico · Edición 2026*

[← Nivel 4 · SOC agéntico](04_Nivel_4_SOC_agentico.md) · [Índice del programa](README.md) · [Evaluaciones y respuestas →](06_Evaluaciones_y_respuestas.md)

<a id="comunidad"></a>

Referentes verificados, canales, libros y recursos en español, y una rutina para mantenerte al día en un producto que cambia cada semana.

*Transversal · 3 módulos · ~3 horas · 20 recursos*

**Módulos de este nivel:** [C1 Referentes](#c1) · [C2 Canales y recursos en español](#c2) · [C3 Mantenerse actualizado](#c3)

<a id="c1"></a>

## C1 · Referentes

*Transversal · ~1 h · Origen: Nuevo en esta edición*

Detrás de Security Copilot hay personas que lo explican todos los días: gerentes de producto que presentan los agentes y la extensibilidad, ingenieros y arquitectos de Microsoft que publican muestras y laboratorios, y MVP que prueban cada novedad en tenants reales y cuentan lo que funciona y lo que no. Seguirlos es la forma más rápida de enterarte de un cambio, entender un comportamiento extraño o encontrar un plugin que alguien ya escribió.

El directorio de este módulo reúne referentes con evidencia pública de su rol —empleados de Microsoft y MVP—, sus temas y sus canales principales. Úsalo como punto de partida, prioriza a quienes publican con fecha y fuente, y contrasta siempre con la documentación oficial: en un producto que cambia cada mes, un buen post de hace un año puede estar desactualizado.

**Por qué importa**

Los referentes aceleran el aprendizaje y el diagnóstico: muchas veces el primer análisis de un agente nuevo o de un cambio de licencias aparece en el blog de un MVP o en un webinar del equipo de producto antes que en la documentación. Un equipo conectado con la comunidad también comparte mejor sus propias lecciones.

**Qué vas a lograr**

- Identificar referentes por tema: plataforma, agentes, extensibilidad, MCP, identidad y operación del SOC.
- Distinguir contenido oficial, de empleados de Microsoft y de MVP.
- Armar tu lista de seguimiento semanal.

> **Consejo Ninja.** Prioriza a quienes publican con fecha y fuente, y verifica su rol: el directorio de este módulo incluye la evidencia pública de cada referente. Un buen punto de partida son los autores de la [Skilling Series](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) y del repositorio [Azure/Security-Copilot](https://github.com/Azure/Security-Copilot).

**¿Tienes poco tiempo?**

- [Experimenting-With-Security-Copilot (repositorio)](https://github.com/mariocuomo/Experimenting-With-Security-Copilot) · GitHub
- [Innocent Wafula, Author at Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/author/innocent-wafula/) · Blog oficial

### Directorio de referentes verificados

- **Alonso Adán Méndez García** (Empleado de Microsoft): Sr. Solution Engineer de Seguridad en Microsoft que difunde en español las novedades de agentes de Security Copilot y sus métricas. [Evidencia de rol](https://es.linkedin.com/posts/aamendez_from-alert-overload-to-decisive-action-how-activity-7444394615765372928-L2qD)
- **Bi Yue Xu** (Empleado de Microsoft): Principal Security Cloud Solution Architect en Microsoft (DFIR, MDE); coautora del libro Microsoft Security Copilot. [Evidencia de rol](https://www.packtpub.com/en-us/product/microsoft-security-copilot-9781835884522/chapter/the-power-of-promptbooks-in-security-copilot-6/section/the-power-of-promptbooks-in-security-copilot-6)
- **Henning Rauch (Professor Smoke)** (Empleado de Microsoft, Alemania): Principal PM de Kusto: grafos en KQL/GQL, NL2KQL, MCP para Kusto y Kusto Detective Agency. [YouTube](https://www.youtube.com/watch?v=Lc-TgF9Oklg) · [Otro](https://detective.kusto.io) · [Evidencia de rol](https://sessionize.com/henning-rauch/)
- **Hesham Saad** (Empleado de Microsoft, Emiratos Árabes Unidos): Coautor de Sentinel All-in-One; repositorios de playbooks de Defender y plugins/promptbooks/Logic Apps para Security Copilot. [GitHub](https://github.com/hesaad/) · [Evidencia de rol](https://github.com/hesaad/)
- **Iftekhar Hussain** (Empleado de Microsoft): Autor de guías prácticas sobre razonamiento agéntico con el MCP de Sentinel sobre datos de larga retención. [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/the-agentic-soc-era-how-sentinel-mcp-enables-autonomous-security-reasoning/4491003)
- **Innocent Wafula** (Empleado de Microsoft, EE. UU.): Principal Product Manager de Agentic Security en Microsoft (antes PM de Security Copilot y de Security for AI); autor de plugins, promptbooks y guías de Logic Apps y de agentes personalizados. [Blog](https://www.microsoft.com/en-us/security/blog/author/innocent-wafula/) · [GitHub](https://github.com/Azure/Security-Copilot/commits?author=inwafula) · [YouTube](https://www.youtube.com/watch?v=vPcLa1xy_74) · [Evidencia de rol](https://www.linkedin.com/in/innocent-wafula-75b3831)
- **Javier Soriano** (Empleado de Microsoft, España): Principal Product Manager de Sentinel (Madrid); pionero de Sentinel como código y del acelerador All-in-One; hoy habla de data lake, graph y MCP. [GitHub](https://github.com/javiersoriano/sentinel-all-in-one) · [Otro](https://rss.com/podcasts/talking-security/2354020/) · [Evidencia de rol](https://sessionize.com/javier-soriano/)
- **Mario Cuomo** (Empleado de Microsoft): Security Cloud Solution Architect en Microsoft; experimentos públicos con plugins, agentes, automatizaciones y promptbooks de Security Copilot y una skill de GitHub Copilot que genera manifiestos YAML. [GitHub](https://github.com/mariocuomo/Experimenting-With-Security-Copilot) · [Evidencia de rol](https://github.com/mariocuomo/Experimenting-With-Security-Copilot)
- **Michalis Michalos (cyb3rmik3)** (Empleado de Microsoft, Grecia): SecOps, DFIR y TI con KQL para Sentinel/Defender XDR; ex-MVP de Security (su perfil de GitHub indica Microsoft como empresa). [Blog](https://www.michalos.net/) · [GitHub](https://github.com/cyb3rmik3) · [Evidencia de rol](https://github.com/cyb3rmik3)
- **Omri Amdursky** (Empleado de Microsoft): Product manager del servidor MCP de Sentinel; autor del anuncio de GA con herramientas KQL personalizadas, entity analyzer, grafo y triage. [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-mcp-server---generally-available-with-exciting-new-capabiliti/4470125)
- **Rod Trent** (Empleado de Microsoft, EE. UU.): Senior Product Manager y Security MVP Lead en Microsoft; divulga a diario sobre Security Copilot, agentes, seguridad de IA, Sentinel y KQL; coautor del libro Microsoft Security Copilot (Packt, 2025). [Blog](https://rodtrent.substack.com/) · [GitHub](https://github.com/rod-trent/MustLearnKQL) · [Otro](https://rodtrent.substack.com/s/the-prompt-for-microsoft-security) · [Evidencia de rol](https://mms2026atmoa.sched.com/speaker/rod_trent.28kie72h)
- **Sean Wasonga** (Empleado de Microsoft): Autor del Ninja Training oficial de Security Copilot (2024) y copresentador de sesiones sobre agentes personalizados; mantenedor del repositorio Azure/Security-Copilot. [GitHub](https://github.com/Azure/Security-Copilot) · [YouTube](https://www.youtube.com/watch?v=vPcLa1xy_74) · [Evidencia de rol](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928)
- **Alex Verboon** (MVP de Microsoft, Suiza): KQL para Defender XDR/Sentinel, Defender Resource Hub y co-anfitrión de KQL Cafe. [GitHub](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · [YouTube](https://www.youtube.com/c/KQLCafe/videos) · [Otro](https://defenderresourcehub.info/) · [Evidencia de rol](https://mvp.microsoft.com/publicprofile/5003805)
- **Derk van der Woude** (MVP de Microsoft, Países Bajos): Defender XDR e identidad; serie reciente sobre seguridad de identidades de agentes (Entra Agent ID). [Otro](https://mvp.microsoft.com/en-us/PublicProfile/5004588) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5004588)
- **Jeffrey Appel** (MVP de Microsoft): Defender XDR/MDE en profundidad, data lake de Sentinel, costos y retención; resumen mensual 'Defender Monthly News'. [Blog](https://jeffreyappel.nl/) · [Otro](https://jeffreyappel.nl/feed/) · [Evidencia de rol](https://jeffreyappel.nl/)
- **Jorge Castañeda** (MVP de Microsoft, Perú): MVP de Security (SIEM & XDR) en español: Defender XDR, Sentinel, Purview, priorización de CVEs y laboratorios; fundador de MUG Perú. [Blog](https://blog.d3fend.me/) · [Otro](https://blog.d3fend.me/about/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5000594)
- **Morten Knudsen** (MVP de Microsoft, Dinamarca): Recolección de logs con AMA/DCR/Logs Ingestion API, transformaciones, costos (Auxiliary) y gestión de tablas del data lake; capacidad de Security Copilot. [Blog](https://mortenknudsen.net/) · [GitHub](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · [Otro](https://mortenknudsen.net/?page_id=12) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5005156)
- **Sami Lamppu** (MVP de Microsoft, Finlandia): Sentinel + Defender XDR y Security Copilot (MVP en ambas áreas); coautor del Unified XDR & SIEM Handbook y del Entra ID Attack & Defense Playbook. [Blog](https://samilamppu.com/) · [Otro](https://samilamppu.com/category/microsoft-sentinel/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/06ab3a7e-e0d7-eb11-bacb-000d3a154f10)
- **Sergio Albea** (MVP de Microsoft, Suiza (originario de España)): Threat hunting con KQL en Defender XDR, feeds de TI con IA/MISP vía Logic Apps; hispanohablante (perfil MVP incluye español y catalán). [GitHub](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · [YouTube](https://www.youtube.com/watch?v=e-mg6XYcCAY) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/27a80f6f-c617-486e-9bb3-dd1ad4194635)
- **Steven Lim (KQLWizard)** (MVP de Microsoft, Singapur): Consultas KQL de detección/caza para Defender XDR y Sentinel publicadas casi a diario; compilaciones 'KQL Grimoire'. [Otro](https://sg.linkedin.com/in/0x534c) · [Evidencia de rol](https://mvp.microsoft.com/en-US/MVP/profile/efcdd649-549b-4a6c-9e00-b6c302f6a545)
- **Thomas Naunheim** (MVP de Microsoft, Alemania): Identidad y ITDR: detección de workload identities en Sentinel/Defender, EntraOps, playbook Entra ID Attack & Defense. [Blog](https://www.cloud-architekt.net/tags) · [GitHub](https://github.com/cloud-architekt) · [Otro](https://poddtoppen.se/podcast/1571989723/cloud-inspires/20-kql-kusto-and-the-ocean-of-data) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5003945)
- **Ugur Koc** (MVP de Microsoft, Alemania): MVP en Security Copilot e Intune; enseña a construir agentes de Security Copilot fiables (NL, agent builder, YAML), creador de KQL Search y de herramientas comunitarias; desde abr-2026 VP of AI en SoftwareCentral. [Blog](https://ugurkoc.de/) · [GitHub](https://github.com/ugurkocde/KQL-Search) · [YouTube](https://www.youtube.com/watch?v=1KsM2k2dP7U) · [Otro](https://speakers.run.events/ugur-koc) · [Evidencia de rol](https://mvp.microsoft.com/en-US/MVP/profile/20a68a2e-857e-4d8d-be89-a59ee5f3aa35)
- **David Alonso Domínguez** (Comunidad): Detección y monitoreo de agentes de IA (Copilot Studio, Foundry, M365 Copilot, MCP local) con Sentinel y Defender XDR; rol MVP/Microsoft no verificado. [Blog](https://davidalonsodominguez.substack.com/about) · [GitHub](https://github.com/davidalonsod/Dalonso-Security-Repo) · [YouTube](https://youtube.com/@davidalonso1867?si=p4Eu_B5KuqUlWBCA) · [Otro](https://davidalonsod.github.io/Dalonso-Security-Repo/) · [Evidencia de rol](https://davidalonsodominguez.substack.com/about)

### Anuncios y blogs oficiales

- [Innocent Wafula, Author at Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/author/innocent-wafula/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Innocent Wafula · Microsoft Security Blog. Página de autor de Innocent Wafula (hoy Principal PM de Agentic Security en Microsoft), autor de contenidos sobre Security Copilot, Logic Apps y agentes personalizados. *Nota:* Sus contenidos 2025-2026 están en Tech Community y la Skilling Series

### Laboratorios, GitHub y herramientas

- [Experimenting-With-Security-Copilot (repositorio)](https://github.com/mariocuomo/Experimenting-With-Security-Copilot) · GitHub · Empleado de Microsoft · Mario Cuomo · GitHub (mariocuomo). Colección de experimentos con plugins, agentes personalizados, automatizaciones, promptbooks y monitorización de Security Copilot.
- [Ugur Koc | Most Valuable Professionals (perfil MVP)](https://mvp.microsoft.com/en-US/MVP/profile/20a68a2e-857e-4d8d-be89-a59ee5f3aa35) · Herramienta · MVP · Ugur Koc · Microsoft MVP Program. Perfil MVP de Ugur Koc con área técnica Microsoft Security Copilot e Intune, referente en agentes y herramientas comunitarias.

### Comunidad: blogs, libros, newsletters y eventos

- [A Microsoft FTE's Reflections from MVP Summit 2026: Deep Insights & Connections](https://techcommunity.microsoft.com/blog/microsoft-security-blog/a-microsoft-fte%E2%80%99s-reflections-from-mvp-summit-2026-deep-insights--connections/4506986/replies/4507426) · Blog · Empleado de Microsoft · Rod Trent · Microsoft Security Community Blog · 31 mar 2026. Reflexión de Rod Trent sobre el MVP Summit 2026 y el valor de la comunidad MVP de seguridad para el producto.

**Manos a la obra**

1. Elige cinco referentes del directorio de este módulo —al menos un empleado de Microsoft del equipo de producto y un MVP— y suscríbete a sus canales principales; anota qué tema cubre cada uno y qué módulo de esta guía complementa.
2. Revisa el repositorio [Experimenting-With-Security-Copilot](https://github.com/mariocuomo/Experimenting-With-Security-Copilot) y comparte con tu equipo un plugin o agente de ejemplo que adaptarías, con el motivo.

<a id="c2"></a>

## C2 · Canales, podcasts, libros y recursos en español

*Transversal · ~1 h · Origen: Ninja oficial de 2024, parte 1, módulo 0 (otras opciones de aprendizaje)*

El canal principal es la **Security Copilot Skilling Series**, con webinars técnicos sobre agentes, Logic Apps, Entra, Intune, Purview y Defender; la complementan **Flight School** (fundamentos de 2024, anterior a los agentes), los videos de **Microsoft Mechanics** y el video hub del sitio de adopción. Como libro de referencia, **Microsoft Security Copilot** (Packt, julio de 2025), escrito por empleados de Microsoft, cubre prompts, promptbooks, plugins y un apéndice de agentes.

En español hay más de lo que parece: el curso SC-5006-A, el hub de adopción, páginas de Learn sobre MCP y agentes, y el laboratorio IdentityDrift traducido. Recuerda que las traducciones suelen ir unas semanas detrás del inglés, y que algunas muestras de GitHub y videos de 2024 todavía usan el nombre de lanzamiento del producto.

**Por qué importa**

Cada persona aprende distinto: un buen programa ofrece video, texto y práctica, y no deja afuera a quien prefiere el español. Una biblioteca curada evita que cada analista dependa de búsquedas al azar o de contenido de 2024 que ya no refleja el producto.

**Qué vas a lograr**

- Elegir canales en video y texto según tu forma de aprender.
- Usar recursos en español sin perder la vigencia de la versión en inglés.
- Incorporar un libro de referencia al plan de estudio del equipo.

> **Novedad.** Hay material en español en Learn sobre el servidor MCP y los agentes: herramientas de creación de agentes ([es-mx](https://learn.microsoft.com/es-mx/azure/sentinel/datalake/sentinel-mcp-agent-creation-tool)), MCP en Security Copilot ([es-es](https://learn.microsoft.com/es-es/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot)), el quickstart de MCP ([es-es](https://learn.microsoft.com/es-es/copilot/security/developer/mcp-quickstart)) y la gestión del uso ([es-es](https://learn.microsoft.com/es-es/copilot/security/manage-usage)). Las traducciones suelen ir unas semanas detrás del inglés.

**¿Tienes poco tiempo?**

- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar
- [Recopilación de herramientas de creación de agentes en el servidor MCP de Microsoft Sentinel (es-mx)](https://learn.microsoft.com/es-mx/azure/sentinel/datalake/sentinel-mcp-agent-creation-tool) · Documentación
- [Desarrollo de una solución de plataforma de seguridad con agente de Security Copilot (IdentityDrift, es-es)](https://learn.microsoft.com/es-es/azure/sentinel/isv/build-agent-security-copilot) · Laboratorio

### Documentación, cursos y credenciales

- [Recopilación de herramientas de creación de agentes en el servidor MCP de Microsoft Sentinel (es-mx)](https://learn.microsoft.com/es-mx/azure/sentinel/datalake/sentinel-mcp-agent-creation-tool) · Documentación · Oficial · ES · Microsoft Learn · 30 ene 2026. Referencia en español de las cinco herramientas de la colección de creación de agentes (search_for_tools, start_agent_creation, compose_agent, get_evaluation, deploy_agent) y sus parámetros.
- [Usar las herramientas MCP de Microsoft Sentinel en Microsoft Security Copilot (es-es)](https://learn.microsoft.com/es-es/azure/sentinel/datalake/sentinel-mcp-use-tool-security-copilot) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la guía para añadir colecciones MCP de Sentinel o propias a agentes personalizados de Security Copilot.
- [Seguridad y gobernanza - Microsoft Copilot Studio (es-es)](https://learn.microsoft.com/es-es/microsoft-copilot-studio/security-and-governance) · Documentación · Oficial · ES · Microsoft Learn. Versión en español del catálogo de controles de seguridad y gobierno de Copilot Studio (directivas de datos, auditoría, protección en tiempo de ejecución, Agent 365).

### Webinars, videos y podcasts

- [Security Copilot Skilling Series (playlist)](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK) · Webinar · Oficial · Microsoft Security Community · Microsoft Security Community (YouTube). Lista de 18 webinars 2025-2026 sobre Security Copilot en Defender, Entra, Intune y Purview, agentes personalizados, Logic Apps vs. agentes y primeros pasos.

### Laboratorios, GitHub y herramientas

- [Desarrollo de una solución de plataforma de seguridad con agente de Security Copilot (IdentityDrift, es-es)](https://learn.microsoft.com/es-es/azure/sentinel/isv/build-agent-security-copilot) · Laboratorio · Oficial · ES · Microsoft Learn. Tutorial en español para crear capacidad SCU, un workspace y el agente IdentityDrift con datos del data lake, ideal como laboratorio guiado del track avanzado.
- [SecurityCopilotCustomAgentWorkshop (taller en japonés)](https://github.com/hisashin0728/SecurityCopilotCustomAgentWorkshop/tree/main) · Laboratorio · Comunidad · Nuevo · hisashin0728 · GitHub (hisashin0728) · ago 2026. Taller de ~5 h para crear plugins KQL/API/GPT, agentes interactivos y Logic Apps de Security Copilot con VS Code, GitHub Copilot y el MCP de Sentinel.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Security Copilot: Master strategies for AI-driven cyber defense (Packt, 2025)](https://www.packtpub.com/en-us/product/microsoft-security-copilot-9781835884522/chapter/the-power-of-promptbooks-in-security-copilot-6/section/the-power-of-promptbooks-in-security-copilot-6) · Libro · Empleado de Microsoft · Bi Yue Xu; Rod Trent · Packt · jul 2025. Libro de 576 páginas con capítulos de plugins, prompt engineering, promptbooks, Logic Apps, precios SCU y un apéndice de agentes.
- [Rod's Blog – etiqueta Security Copilot](https://rodtrent.substack.com/t/security-copilot) · Blog · Empleado de Microsoft · Nuevo · Rod Trent · Rod's Blog (Substack) · ago 2026. Serie de artículos sobre inclusión en E5, workspaces, calculadora, overage SCU y 'Prompt of the Day', además del boletín THE PROMPT for Microsoft Security.

**Manos a la obra**

1. Arma la biblioteca del equipo con la [Skilling Series](https://www.youtube.com/playlist?list=PLmAptfqzxVEWGjqfUaMx9R2DjPjrXrfjK), [Flight School](https://learn.microsoft.com/en-us/shows/microsoft-security-copilot-flight-school/), el [video hub](https://adoption.microsoft.com/en-us/security-copilot/video-hub/) y el libro [Microsoft Security Copilot](https://www.packtpub.com/en-us/product/microsoft-security-copilot-9781835884522/chapter/the-power-of-promptbooks-in-security-copilot-6/section/the-power-of-promptbooks-in-security-copilot-6), indicando qué módulo de esta guía complementa cada recurso.
2. Recorre el laboratorio IdentityDrift [en español](https://learn.microsoft.com/es-es/azure/sentinel/isv/build-agent-security-copilot) y compáralo con la versión en inglés: anota diferencias de fecha o de contenido.

**¿Quieres profundizar?**

- [Microsoft Security Copilot: Master strategies for AI-driven cyber defense (Packt, 2025)](https://www.packtpub.com/en-us/product/microsoft-security-copilot-9781835884522/chapter/the-power-of-promptbooks-in-security-copilot-6/section/the-power-of-promptbooks-in-security-copilot-6) · Libro
- [Rod's Blog – etiqueta Security Copilot](https://rodtrent.substack.com/t/security-copilot) · Blog

<a id="c3"></a>

## C3 · Cómo mantenerse actualizado

*Transversal · ~1 h · Origen: Ninja oficial de 2024, parte 1, módulo 0 (novedades y soporte)*

Security Copilot cambia cada semana: agentes nuevos, estados que pasan de vista previa a disponibilidad general, retiros con fecha y cambios de licencias. Un equipo de primer nivel tiene una **rutina de actualización** con dueños: qué se revisa cada semana (el blog de Security Copilot y la newsletter THE PROMPT), cada mes (las novedades de Microsoft Security y el archivo de Security Copilot del Security Blog), cada trimestre (este inventario y la política de gobierno) y después de cada evento grande.

Hay dos trampas conocidas: la página «What's new» de Learn dice actualizarse cada mes, pero su última entrada visible es de abril de 2026, y los avisos del centro de mensajes pueden corregirse después de publicados. Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar el estado de Perception, NL2Agent, los plugins MCP y varios agentes: revisa las fuentes oficiales después del evento y actualiza tu inventario.

**Por qué importa**

Un retiro que nadie vio a tiempo —como los agentes de Intune en 2026— o un cambio de licencias no detectado se convierte en un proceso roto o en un costo inesperado. Una rutina con dueños transforma las novedades en mantenimiento planificado del inventario, los agentes y la política de gobierno.

**Qué vas a lograr**

- Definir una rutina semanal, mensual, trimestral y por evento de actualización.
- Convertir los cambios relevantes en tareas con dueño sobre el inventario de agentes y la política de gobierno.
- Verificar en la fuente oficial lo que reportan los rastreadores comunitarios.

> **Atención.** La página «What's new» de Learn no registra entradas desde abril de 2026: para las novedades usa el blog de Security Copilot, el archivo del Security Blog y las novedades mensuales de Microsoft Security, y revisa todo después de Ignite (17 al 20 de noviembre de 2026) ([archivo de Security Copilot](https://www.microsoft.com/en-us/security/blog/product/microsoft-security-copilot/), [novedades de septiembre de 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/)).

**¿Tienes poco tiempo?**

- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación
- [THE PROMPT for Microsoft Security (newsletter semanal)](https://rodtrent.substack.com/s/the-prompt-for-microsoft-security) · Newsletter
- [Microsoft Security Copilot Archives (Microsoft Security Blog)](https://www.microsoft.com/en-us/security/blog/product/microsoft-security-copilot/) · Blog oficial

### Documentación, cursos y credenciales

- [What's new in Microsoft Security Copilot?](https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security) · Documentación · Oficial · Microsoft Learn · 17 abr 2026. Registro mensual oficial de novedades (agentes, inclusión E5, workspaces, overage, auditoría de agentes en Purview, GPT-4.1, idiomas, residencia de datos) indicando si cada cambio aplica a la experiencia independiente o embebida.

### Anuncios y blogs oficiales

- [Microsoft Security Copilot Archives (Microsoft Security Blog)](https://www.microsoft.com/en-us/security/blog/product/microsoft-security-copilot/) · Blog oficial · Oficial · Nuevo · Microsoft Security Blog · 28 oct 2026. Archivo filtrado del Microsoft Security Blog con todas las entradas etiquetadas Security Copilot (SOC agéntico, taxonomía de fallos, TEI, novedades mensuales).
- [Microsoft Security Copilot Blog (Microsoft Community Hub)](https://techcommunity.microsoft.com/category/microsoft-security-product/blog/securitycopilotblog) · Blog oficial · Oficial · Equipo de producto de Security Copilot · Microsoft Tech Community · 20 mar 2026. Blog del equipo de producto con anuncios, inmersiones técnicas y buenas prácticas (agentes, Secret Finder, Logic Apps, Store).
- [What's new in Microsoft Security: September 2026](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 24 sep 2026. Incluye el nuevo resumen de detonación de correo generado por Security Copilot para explicar resultados de sandboxing de URL y archivos en investigaciones.
- [What's new in Microsoft Security: July 2026](https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Alym Rayani · Microsoft Security Blog · 30 jul 2026. Novedades de julio 2026: Project Perception, protección contra prompt injection en correo, Threat Intelligence Agent mejorado y convergencia de Defender Threat Intelligence.

### Comunidad: blogs, libros, newsletters y eventos

- [THE PROMPT for Microsoft Security (newsletter semanal)](https://rodtrent.substack.com/s/the-prompt-for-microsoft-security) · Newsletter · Empleado de Microsoft · Nuevo · Rod Trent · Substack · 23 oct 2026. Boletín semanal con novedades de la plataforma de operaciones de seguridad de Microsoft, agentes, Security Copilot y Sentinel.
- [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · Blog · Comunidad · Marcel_Graewer · Microsoft Tech Community (foro) · 25 abr 2026. Análisis práctico de un miembro de la comunidad sobre qué agentes de Defender están GA o en preview, trampas de configuración y cómo controlar el consumo de SCU.
- [Microsoft Security Copilot Blog (feed RSS)](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SecurityCopilotBlog) · Newsletter · Oficial · Equipo de producto de Security Copilot · Microsoft Tech Community · mar 2026. Feed RSS del blog de Security Copilot para suscribirse a novedades desde un lector o Teams/Outlook.

**Manos a la obra**

1. Define la rutina del equipo con un dueño por fuente: semanal ([blog de Security Copilot](https://techcommunity.microsoft.com/category/microsoft-security-product/blog/securitycopilotblog) y [THE PROMPT](https://rodtrent.substack.com/s/the-prompt-for-microsoft-security)), mensual ([archivo del Security Blog](https://www.microsoft.com/en-us/security/blog/product/microsoft-security-copilot/)), trimestral (inventario de agentes y política de gobierno) y por evento (después de Ignite).
2. Después de Microsoft Ignite (17 al 20 de noviembre de 2026), revisa el [inventario de agentes](00_Programa.md#inventario-agentes) y las limitaciones de esta guía ([Metodología y fuentes](08_Cierre_glosario_y_fuentes.md#metodologia)) y registra qué cambió de estado, de nombre o de precio.

**¿Quieres profundizar?**

- [Security Copilot Agents in Defender XDR: where things actually stand](https://techcommunity.microsoft.com/discussions/microsoft-security/security-copilot-agents-in-defender-xdr-where-things-actually-stand/4514689) · Blog
- [Microsoft Security Copilot Blog (feed RSS)](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SecurityCopilotBlog) · Newsletter

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

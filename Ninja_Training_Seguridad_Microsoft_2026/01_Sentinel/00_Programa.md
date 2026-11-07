# Programa: cómo usar, justificación, rutas y plan

*Microsoft Sentinel Ninja Training · Edición 2026*

[Índice del programa](README.md) · [Nivel 1 · Inicial →](01_Nivel_1_Inicial.md)

<a id="como-usar"></a>

## Cómo usar esta guía

¿Quieres convertirte en Ninja de Microsoft Sentinel? Esta guía te ayuda a llegar. Reúne, ordenados como un curso, los mejores recursos públicos para dominar Sentinel de punta a punta: documentación de Microsoft Learn, anuncios y blogs de los equipos de producto, webinars de la Microsoft Security Community, laboratorios y repositorios de GitHub, y el trabajo de MVPs y empleados de Microsoft que enseñan el producto todos los días.

Puedes seguirla de principio a fin o saltar directamente a tu rol. Cada nivel cierra con una evaluación de conocimientos y, si alcanzas el 80 %, puedes generar tu certificado de finalización, como en el Ninja original. Y como el SOC ya no termina en el playbook, el recorrido continúa hasta el SOC agéntico: Security Copilot, agentes, el servidor MCP de Sentinel y la automatización con Azure Logic Apps.

**Estructura.** Cuatro niveles —Inicial (L100–L200), Intermedio (L300), Avanzado (L400) y Experto agéntico (L400+)— más una sección transversal de comunidad. Los niveles inicial, intermedio y avanzado reconstruyen los 22 módulos del Ninja original (0 a 21) actualizados a 2026; el nivel experto es la ampliación hacia Security Copilot, agentes, MCP y Logic Apps.

**Cada módulo** sigue la forma Ninja: una introducción que explica por qué el tema importa, lo que vas a lograr, las novedades y advertencias con fecha y fuente, una ruta rápida (*¿Tienes poco tiempo?*), los recursos agrupados por tipo, una práctica guiada (*Manos a la obra*) y lecturas para ir más allá (*¿Quieres profundizar?*).

**Evaluación y certificado.** Al final de cada nivel hay una evaluación de opción múltiple con la explicación y la fuente de cada respuesta. Con 80 % o más puedes generar e imprimir un certificado de finalización del nivel. Es una autoevaluación de esta guía, no una certificación de Microsoft: para eso están el examen SC-200 y la evaluación del Ninja oficial de Tech Community, que entrega un certificado de participación.

**Progreso y búsqueda.** Marca cada módulo como completado (se guarda en tu navegador) y usa la barra superior para buscar y filtrar recursos por tipo, autoría, estado o idioma.

**Fechas y estados.** Cada dato tiene su fuente y su fecha. Microsoft Ignite se realiza del 17 al 20 de noviembre de 2026 y puede cambiar estados de vista previa: ante la duda, verifica la página de novedades del producto. La documentación en español suele actualizarse después que la versión en inglés.

**Leyenda de etiquetas**

| Etiqueta | Significado |
|---|---|
| Microsoft oficial | Documentación, blogs y videos publicados por Microsoft. |
| Empleado de Microsoft | Material de ingenieros, gerentes de producto o arquitectos de Microsoft en canales propios o comunitarios. |
| MVP de Microsoft | Material de Most Valuable Professionals de seguridad, con estado verificado en fuentes públicas. |
| Comunidad o partner | Autores de la comunidad o de partners; útil, pero contrástalo con la documentación oficial. |
| Vista previa | Funcionalidad en preview: puede cambiar y no siempre tiene soporte de producción. |
| Legado aún útil | Recurso anterior a los cambios de 2025–2026 que sigue explicando bien el concepto; lee la nota de qué cambió. |
| Ninja original | Recurso que formaba parte del Ninja original o del skill-up de Microsoft Learn. |
| Nuevo | Recurso publicado o actualizado desde mayo de 2026. |
| ES | Recurso disponible en español. |
| Laboratorio | Ejercicio que puedes hacer completo en el entorno de práctica (prueba de Microsoft 365 E5 o sandbox y suscripción de Azure). |
| Laboratorio parcial | Ejercicio posible en el entorno de práctica con limitaciones (volumen de datos, días de línea base, costo de cómputo o funciones en vista previa). |
| Solo producción | Requiere licencias pagas, datos o usuarios reales, o sistemas que no existen en el laboratorio: síguelo con la estrategia de práctica segura en producción. |

<a id="por-que"></a>

## Por qué este programa

**Por qué ahora.** Microsoft Sentinel cambió más entre 2025 y 2026 que en los cinco años anteriores: pasó al portal de Defender, sumó el data lake y el graph, unificó las detecciones personalizadas con las reglas de analítica, incorporó incident cases, el servidor MCP y Security Copilot incluido en Microsoft 365 E5. Un equipo formado con el material de 2022 opera con un modelo mental desactualizado: busca opciones en el portal de Azure (que deja de tener soporte el 31 de marzo de 2027), paga de más por datos que podrían ir al lago y no aprovecha la correlación de Defender XDR.

**Qué gana la organización.** El programa apunta a resultados medibles: cobertura de técnicas de MITRE ATT&CK por fuente de datos, tiempo medio de triage y de respuesta, porcentaje de incidentes con automatización, costo por GB y por caso de uso, y deuda de contenido (reglas sin dueño, sin prueba o sin mapeo de entidades). Cada nivel deja entregables que el SOC puede usar el lunes siguiente: un laboratorio reproducible, reglas versionadas, playbooks con aprobación humana y un tablero de salud y consumo.

**Para quién.** Analistas de SOC de primer a tercer nivel, ingenieros de detección, ingenieros de automatización y de plataforma, arquitectos de seguridad y líderes de SOC. Las rutas por rol permiten que cada perfil recorra solo lo que necesita, con un tronco común en el nivel inicial.

**Cómo se conecta con el resto de la serie.** Sentinel es el plano de datos y de correlación del SOC: el programa de **Defender XDR** profundiza la detección y respuesta en endpoint, correo e identidad; el de **Entra** explica las señales y los controles de identidad que Sentinel consume; el de **Security Copilot** lleva el nivel experto a un SOC agéntico; y los programas de **Purview** aportan las alertas de DLP, riesgo interno y auditoría que también llegan al portal de Defender.

<a id="formato"></a>

## El formato Ninja: historia y familia

El Ninja de Sentinel nació el 12 de abril de 2020 en el blog de Microsoft Sentinel en Tech Community, escrito por Ofer Shezaf, como un entrenamiento de nivel 400 que ordenaba documentación, artículos y grabaciones de webinars (en YouTube, MP4 y diapositivas) en partes y módulos. En agosto de 2021 sumó una evaluación de conocimientos: 30 preguntas de opción múltiple, aprobación con 80 % y un certificado de participación enviado por correo, con la aclaración de que no era una certificación oficial. Durante años se actualizó mes a mes, con la fecha junto a cada tema y marcadores «new!».

En 2022 su contenido pasó a Microsoft Learn como **Microsoft Sentinel skill-up training**: 21 módulos en cinco partes que siguen el ciclo de vida de un SOC (actualizado por última vez el 7 de agosto de 2026, cuando incorporó el Training Lab). En octubre de 2025, el post original de Tech Community se reorganizó por roles —fundamentos de operaciones de seguridad, arquitectos, ingenieros y analistas— y renovó la evaluación y el certificado. Alrededor de Sentinel creció una familia: Notebooks Ninja (2021), Automation Ninja (2022), Unified SOC Platform Ninja (2024) y Security Copilot Ninja (2024), además de los Ninja de Defender XDR, Defender for Endpoint, Office 365, Identity, Cloud Apps, Cloud, Threat Intelligence y Purview, y el Virtual Ninja Show.

Esta edición respeta esa forma —módulos con introducción, recursos curados, práctica y evaluación— y la combina con las dos organizaciones oficiales: el orden por niveles de la familia Ninja y las rutas por rol del Ninja de 2025.

**La familia Ninja relacionada**

| Entrenamiento | Estructura | Evaluación | Última actualización conocida |
|---|---|---|---|
| [Become a Microsoft Sentinel Ninja](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-ninja-the-complete-level-400-training/1246310) | Por roles: fundamentos, arquitectos, ingenieros y analistas | Knowledge check y certificado de participación (80 %) | Octubre de 2025 |
| [Microsoft Sentinel skill-up training](https://learn.microsoft.com/en-us/azure/sentinel/skill-up-resources) | 21 módulos en 5 partes (ciclo de vida del SOC) | Remite a SC-200 | 7 de agosto de 2026 |
| [Security Copilot Ninja](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928) | Getting started, Become proficient, Grow into an expert | Knowledge check y certificado (80 %) | 19 de noviembre de 2024 (no cubre agentes ni MCP) |
| [Notebooks Ninja](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/becoming-a-microsoft-sentinel-notebooks-ninja---the-series/2693491) | Partes 1, 2, 3, 3.5 y 4 | Knowledge check y certificado (80 %) | 28 de octubre de 2022 |
| [Automation Ninja](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-automation-ninja/3563377) | SOAR de lo básico a lo avanzado | Sin datos | 1 de julio de 2022 |
| [Unified SOC Platform Ninja](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/unified-operation-platform-features-released-at-public-preview/4014565) | Visión general y operación XDR + SIEM | Sin datos | Enero de 2024 (era vista previa privada) |
| [Defender XDR Ninja](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-train-security-staff) | Fundamentals, Intermediate y Expert | Knowledge check por nivel | Octubre de 2026 |

**Del Ninja oficial a esta edición**

| Módulo del Ninja original | Módulo de esta edición |
|---|---|
| 0 · Other learning and support options | [I0](01_Nivel_1_Inicial.md#i0) |
| 1 · Get started with Microsoft Sentinel | [I1](01_Nivel_1_Inicial.md#i1), [I3](01_Nivel_1_Inicial.md#i3) |
| 2 · How is Microsoft Sentinel used? | [I2](01_Nivel_1_Inicial.md#i2) |
| 3 · Workspace and tenant architecture | [M1](02_Nivel_2_Intermedio.md#m1), [A9](03_Nivel_3_Avanzado.md#a9) |
| 4 · Data collection | [M2](02_Nivel_2_Intermedio.md#m2), [A5](03_Nivel_3_Avanzado.md#a5) |
| 5 · Log management | [M3](02_Nivel_2_Intermedio.md#m3), [A8](03_Nivel_3_Avanzado.md#a8) |
| 6 · Enrichment: threat intelligence, watchlists, and more | [M4](02_Nivel_2_Intermedio.md#m4) |
| 7 · Log transformation | [M5](02_Nivel_2_Intermedio.md#m5) |
| 8 · Migration | [M6](02_Nivel_2_Intermedio.md#m6) |
| 9 · ASIM and normalization | [A1](03_Nivel_3_Avanzado.md#a1) |
| 10 · Kusto Query Language | [I4](01_Nivel_1_Inicial.md#i4), [A2](03_Nivel_3_Avanzado.md#a2) |
| 11 · Analytics | [M7](02_Nivel_2_Intermedio.md#m7) |
| 12 · Implementing SOAR | [M13](02_Nivel_2_Intermedio.md#m13), [X1](04_Nivel_4_Experto_agentico.md#x1) |
| 13 · Workbooks, reporting, and visualization | [M8](02_Nivel_2_Intermedio.md#m8) |
| 14 · Notebooks | [A7](03_Nivel_3_Avanzado.md#a7) |
| 15 · Use cases and solutions | [A3](03_Nivel_3_Avanzado.md#a3) |
| 16 · A day in a SOC analyst's life, incident management, and investigation | [M9](02_Nivel_2_Intermedio.md#m9) |
| 17 · Hunting | [M10](02_Nivel_2_Intermedio.md#m10) |
| 18 · UEBA | [M11](02_Nivel_2_Intermedio.md#m11) |
| 19 · Monitoring Microsoft Sentinel's health | [M12](02_Nivel_2_Intermedio.md#m12) |
| 20 · Extending and integrating using the Microsoft Sentinel APIs | [A6](03_Nivel_3_Avanzado.md#a6) |
| 21 · Build-your-own machine learning | [A7](03_Nivel_3_Avanzado.md#a7) |
| Nuevo en esta edición | [P0](01_Nivel_1_Inicial.md#p0), [A4](03_Nivel_3_Avanzado.md#a4), [A8](03_Nivel_3_Avanzado.md#a8), [X2](04_Nivel_4_Experto_agentico.md#x2) a [X7](04_Nivel_4_Experto_agentico.md#x7), [C1](05_Comunidad.md#c1) a [C5](05_Comunidad.md#c5) |

**Recursos sobre el Ninja oficial y su familia**

- [What's new in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · oct 2026. Enlace del Módulo 0 ('Otras opciones de aprendizaje y soporte') del skill-up de Learn: doc «What's new».
- [Study guide for Exam SC-200: Microsoft Security Operations Analyst](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · Credencial · Oficial · Nuevo · Microsoft Learn · 21 oct 2026. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: certificacion «Study Guide».
- [Onboarding documentation](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: doc «Onboarding documentation».
- [What is Microsoft Sentinel?](https://learn.microsoft.com/en-us/azure/sentinel/overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Enlace del Módulo 1 ('Introducción a Microsoft Sentinel') del skill-up de Learn: doc «What is Microsoft Sentinel?».
- [Automate threat response with automation rules](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules) · Documentación · Oficial · Nuevo · Microsoft Learn · 11 may 2026. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «Automation rules».
- [Roles and permissions in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/roles) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 may 2026. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Roles and permissions in Microsoft Sentinel».
- [Plan costs and understand Microsoft Sentinel pricing and billing](https://learn.microsoft.com/en-us/azure/sentinel/billing) · Documentación · Oficial · Nuevo · Microsoft Learn · 6 may 2026. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Plan costs and understand Microsoft Sentinel pricing and billing».
- [Microsoft Sentinel in the Microsoft Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal) · Documentación · Oficial · Microsoft Learn. Doc oficial que compara Sentinel en Azure vs. Defender (incidentes unificados, attack story, blast radius, hunting unificado con data lake, Copilot) y confirma el fin del soporte en Azure tras el 31-mar-2027.
- [Extend Microsoft Sentinel across workspaces and tenants](https://learn.microsoft.com/en-us/azure/sentinel/extend-sentinel-across-workspaces-tenants) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 3 ('Arquitectura de workspaces y tenants') del skill-up de Learn: doc «Extend Microsoft Sentinel across workspaces and tenants».
- [Protect MSSP intellectual property in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mssp-protect-intellectual-property) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 3 ('Arquitectura de workspaces y tenants') del skill-up de Learn: doc «Protect MSSP intellectual property in Microsoft Sentinel».
- [Microsoft Sentinel data connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Microsoft Sentinel data connectors».
- [Use watchlists in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/watchlists) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: doc «Use watchlists in Microsoft Sentinel».
- [Logs Ingestion API in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-ingestion-api-overview) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 7 ('Transformación de logs') del skill-up de Learn: doc «** Logs ingestion API**».
- [The Microsoft Sentinel Logic Apps connector](https://learn.microsoft.com/en-us/connectors/azuresentinel/) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «The Microsoft Sentinel Logic Apps connector».
- [Visualize and monitor your data by using workbooks](https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: doc «Documentation».
- [Entity pages in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/entity-pages) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: doc «Entity pages».
- [Hunt for threats with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/hunting) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 17 ('Hunting') del skill-up de Learn: doc «Hunt for threats with Microsoft Sentinel».
- [User and Entity Behavior Analytics (UEBA)](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 18 ('UEBA') del skill-up de Learn: doc «User and Entity Behavior Analytics (UEBA)».
- [Manage your SOC better with incident metrics](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 19 ('Monitoreo de salud') del skill-up de Learn: doc «Security operations».
- [Monitor the health of your data connectors](https://learn.microsoft.com/en-us/azure/sentinel/monitor-data-connector-health) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 19 ('Monitoreo de salud') del skill-up de Learn: doc «Monitor the health of your data connectors».
- [Best practices for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/best-practices) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Best practices for Microsoft Sentinel».
- [UPDATE: New timeline for transitioning Sentinel experience to Defender portal](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464) · Blog oficial · Oficial · aklausner · Microsoft Tech Community – Microsoft Sentinel Blog · 29 ene 2026. Anuncia la extensión del retiro de Sentinel en el portal de Azure del 1-jul-2026 al 31-mar-2027 y lista capacidades exclusivas del portal de Defender (Security Copilot, data lake, graph, SOC optimization).
- [Become a Microsoft Sentinel Ninja: The complete level 400 training](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-ninja-the-complete-level-400-training/1246310) · Blog oficial · Oficial · Ofer Shezaf · Microsoft Tech Community – Microsoft Sentinel Blog · 12 abr 2020. Entrenamiento Ninja oficial de Sentinel, hoy reorganizado por roles (Fundamentos, Arquitectos, Ingenieros, Analistas) con enlaces a docs, blogs, webinars y skill checks de Learn, más knowledge check (≥80%) y certificado de participación.
- [ASIM hunting queries from GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Hunting%20Queries) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub. Enlace del Módulo 9 ('ASIM y normalización') del skill-up de Learn: github «ASIM hunting queries from GitHub». *Nota:* El repo también contiene Detections, Parsers ASIM, Sentinel Behaviors y Summary rules
- [Playbooks folder (Azure-Sentinel on GitHub)](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks) · GitHub · Oficial · Legado aún útil · Microsoft y comunidad · GitHub. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: github «_ Playbooks_ folder». *Nota:* Repositorio activo; muchos playbooks heredados usan disparadores/acciones antiguas: revisar versión del conector y preferir variantes con identidad administrada. Los playbooks de soluciones viven en Solutions/<Solución>/Playbooks
- [How to Become a Microsoft Security Copilot Ninja: The Complete Level 400 Training](https://techcommunity.microsoft.com/blog/securitycopilotblog/how-to-become-a-microsoft-security-copilot-ninja-the-complete-level-400-training/4106928) · Blog oficial · Oficial · Legado aún útil · Sean Wasonga · Microsoft Tech Community – Microsoft Security Copilot Blog · 15 abr 2024. Ninja de Security Copilot en tres partes (Getting Started, Become Proficient, Grow into an Expert) que cubre onboarding, roles, plugins, prompts, promptbooks, plugins personalizados, Logic Apps y bases de conocimiento, con knowledge check y certificado. *Nota:* Versión 4.0 actualizada 19-nov-2024 (título original 'Copilot for Security'). No cubre agentes (2025), SCU por workspace ni el portal de Defender unificado; complementar con X2-X5. Short link aka.ms/SecurityCopilotNinja
- [Tag: "ninja training" | Microsoft Community Hub](https://techcommunity.microsoft.com/tag/ninja%20training) · Herramienta · Oficial · Nuevo · Microsoft Tech Community · 19 oct 2026. Índice vivo de Tech Community con las 49 publicaciones etiquetadas 'ninja training', útil para comprobar fechas de actualización de cada Ninja y los 'Monthly news' de Defender.
- [Machine learning capabilities](https://learn.microsoft.com/en-us/azure/sentinel/bring-your-own-ml) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: doc «Machine learning capabilities».
- [About Microsoft Sentinel content and solutions](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 15 ('Casos de uso y soluciones') del skill-up de Learn: doc «About Microsoft Sentinel content and solutions».
- [Integrating with Microsoft Teams directly from Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/collaborate-in-microsoft-teams) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: doc «Integrating with Microsoft Teams directly from Microsoft Sentinel».
- [Microsoft Sentinel sample workspace designs](https://learn.microsoft.com/en-us/azure/sentinel/sample-workspace-designs) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Microsoft Sentinel sample workspace designs».
- [Deploy Microsoft Sentinel side-by-side with an existing SIEM](https://learn.microsoft.com/en-us/azure/sentinel/deploy-side-by-side) · Documentación · Oficial · Microsoft Learn. Enlace del Módulo NS ('Próximos pasos') del skill-up de Learn: doc «Deploy Microsoft Sentinel side-by-side with an existing SIEM».
- [Microsoft Ninja Training Hub (Unofficial Tracker) – README](https://github.com/peterschmidtdk/Microsoft-Ninja-Training/blob/main/README.md) · GitHub · Comunidad · Peter Schmidt · GitHub – peterschmidtdk · 27 feb 2026. Tracker comunitario con todas las trainings Ninja de seguridad (Sentinel, Automation, Notebooks, Defender XDR y workloads, Exposure Management, IR Hub, Purview, Priva, Azure Network Security) y la descripción de su formato por niveles.
- [Become a Microsoft Ninja: All the Free Microsoft Security Training in One Place](https://blog.cdoherty.co.uk/become-a-microsoft-ninja-all-the-free-microsoft-security-training-in-one-place) · Blog · Comunidad · Ciaran Doherty · blog.cdoherty.co.uk · 19 jun 2025. Recopilatorio comunitario de todos los entrenamientos Ninja de seguridad de Microsoft (Sentinel, Notebooks, Unified SOC, Defender XDR, Security Copilot, MDC, Purview, MDI, MDCA, EASM, MDTI, Azure Network Security, IoT) con sus URLs.
- [Become a Microsoft Security Ninja in 2025!](https://www.performanta.com/post/become-a-microsoft-security-ninja-in-2025) · Blog · Comunidad · José Lázaro Pinos y Marcus Burnap · Performanta · 8 ene 2025. Tercera edición del recopilatorio anual de la serie Microsoft Security Ninja Training (Sentinel, MDE, MDO, MDI, MDCA, MDTI, Security Copilot, MIP, DLP, DVM, IoT, EASM, eDiscovery) con sus short links.
- [Become a Microsoft Unified SOC Platform Ninja (URL actual: Unified operation platform features released at public preview)](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/unified-operation-platform-features-released-at-public-preview/4014565) · Blog oficial · Oficial · Legado aún útil · Microsoft Tech Community – Microsoft Sentinel Blog · ene 2024. Ninja de la plataforma unificada SIEM+XDR (Sentinel en el portal de Defender) con dos bloques: visión general (beneficios, primeros pasos, casos de uso) y operación (conexión a Defender XDR, incidentes unificados, automatización, advanced hunting, SOC optimization, soporte). *Nota:* Publicado ~enero 2024 cuando la integración estaba en private preview; el seed t5/.../become-a-microsoft-unified-soc-platform-ninja/ba-p/4014565 hoy resuelve a este slug renombrado (según listado de C. Doherty). El fetch directo no devolvió contenido…
- [Passing The Microsoft Sentinel Ninja Training](https://charbelnemnom.com/passing-the-microsoft-sentinel-ninja-training/) · Blog · MVP · Legado aún útil · Charbel Nemnom · charbelnemnom.com · 26 jun 2022. Testimonio de un MVP sobre el knowledge check del Ninja de Sentinel: 30 preguntas de opción múltiple, aprobado con 80% (24 puntos), sin límite de tiempo, con respuestas visibles al enviar y certificado por correo en ~1 día hábil. *Nota:* Describe la versión 2021-2022 (16 módulos y actualizaciones mensuales con fecha junto a cada tema); el mecanismo de knowledge check + certificado no oficial sigue vigente (oct-2025)
- [Splunk Search Processing Language (SPL) to KQL mappings](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/RuleMigration/SPL%20to%20KQL.md) · GitHub · Oficial · Legado aún útil · Microsoft (tatecksi) · GitHub. Enlace del Módulo 8 ('Migración') del skill-up de Learn: github «Splunk Search Processing Language (SPL) to KQL mappings». *Nota:* Recurso de la Ninja Training original (módulo de migración); sigue vigente como referencia manual aunque hoy la traducción inicial la hace la experiencia de migración SIEM
- [What's new: Microsoft Sentinel Ninja Training Knowledge Check](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/whats-new-microsoft-sentinel-ninja-training-knowledge-check/2677696/replies/4279223) · Blog oficial · Oficial · Legado aún útil · Sarah Young · Microsoft Tech Community – Microsoft Sentinel Blog · 23 ago 2021. Anuncio del knowledge check del Ninja de Sentinel: quien supere el 80% puede solicitar un certificado que acredita sus habilidades ninja. *Nota:* URL vista apunta a un comentario (/replies/4279223) del post 2677696; actualizado 03-nov-2021. Hay comentarios de 2024 sobre demoras en la entrega del certificado
- [Using Microsoft Sentinel incident bi-directional sync with ServiceNow](https://techcommunity.microsoft.com/t5/azure-sentinel/azure-sentinel-incident-bi-directional-sync-with-servicenow/ba-p/1667771) · Blog oficial · Oficial · Legado aún útil · Yaniv Shasha · Microsoft Tech Community · 15 sep 2020. Enlace del Módulo 2 ('Cómo se usa Microsoft Sentinel') del skill-up de Learn: blog-oficial «Using Microsoft Sentinel incident bi-directional sync with ServiceNow». *Nota:* Usa playbooks adjuntos a reglas de análisis (obsoleto desde mar-2026): hoy usar reglas de automatización e identidad administrada
- [Become a Microsoft Purview eDiscovery Ninja](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108) · Blog oficial · Oficial · Nuevo · Stefanie Bier · Microsoft Tech Community – Microsoft Security Community Blog · 5 may 2026. Ninja de Purview eDiscovery (experiencia unificada) desde fundamentos a flujos avanzados: permisos, retenciones, búsqueda y colección (incluye Teams y Copilot), review sets y exportación.
- [Become a Microsoft Defender for Cloud Ninja](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/become-a-microsoft-defender-for-cloud-ninja/1608761) · Blog oficial · Oficial · Microsoft Tech Community – Microsoft Defender for Cloud Blog. Ninja de Defender for Cloud (CNAPP: postura, protección de cargas, alertas, integraciones) con knowledge check de 30 preguntas (aprobado 24/30 = 80%) y certificados separados de Defender for Cloud y Defender for Servers.
- [Become a Microsoft Defender Vulnerability Management Ninja](https://techcommunity.microsoft.com/blog/vulnerability-management/become-a-microsoft-defender-vulnerability-management-ninja/4003011) · Blog oficial · Oficial · Microsoft Tech Community – Vulnerability Management Blog. Ninja de Defender Vulnerability Management para construir y operar un programa de gestión de vulnerabilidades con las capacidades de Microsoft.
- [Purview Information Protection Ninja (short link)](https://aka.ms/MIPNinja) · Blog oficial · Oficial · Microsoft Tech Community. Ninja de Purview Information Protection sobre clasificación y etiquetas de sensibilidad, de fundamentos a escenarios avanzados.
- [Purview Data Loss Prevention (DLP) Ninja (short link)](https://aka.ms/DLPNinja) · Blog oficial · Oficial · Microsoft Tech Community. Ninja de Purview DLP sobre diseño y operación de políticas, reporting y escenarios comunes.
- [Microsoft Security Exposure Management Ninja Training](https://techcommunity.microsoft.com/blog/securityexposuremanagement/microsoft-security-exposure-management-ninja-training/4444285) · Blog oficial · Oficial · Microsoft Tech Community – Security Exposure Management Blog. Ninja de Microsoft Security Exposure Management con conceptos y escenarios para planificar y operar la gestión de exposición (attack paths, activos críticos).
- [Welcome to the Microsoft Defender Experts Ninja Hub](https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/welcome-to-the-microsoft-defender-experts-ninja-hub/4442210) · Blog oficial · Oficial · Microsoft Tech Community – Microsoft Security Experts Blog. Hub Ninja con recursos de inicio y aprendizaje continuo para los servicios gestionados Defender Experts (MDR/hunting).
- [Microsoft Security Ninja training resources 2025](https://itworldjd.wordpress.com/2025/03/17/microsoft-security-ninja-training-resources-2025/) · Blog · Comunidad · Jacques Dalbera · Jacques Dalbera's IT world · 17 mar 2025. Republicación del recopilatorio 'Become a Microsoft Security Ninja in 2025' con la lista de trainings Ninja de seguridad.
- [Become a Microsoft Defender for Office 365 Ninja! | June 2022](https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/become-a-microsoft-defender-for-office-365-ninja--june-2022/2187392) · Blog oficial · Oficial · Angela Marafino (base de Heike Ritter) · Microsoft Tech Community – Microsoft Defender for Office 365 Blog · 5 abr 2021. Ninja de MDO para dos roles (SecOps y Email Security) en tres niveles (Fundamentals, Intermediate, Advanced) con knowledge check tras cada nivel, certificado no oficial y leyenda de tipos de enlace (docs, blogs, vídeos, webcasts, guías interactivas, GitHub).
- [Become a Microsoft Defender for Endpoint Ninja](https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/become-a-microsoft-defender-for-endpoint-ninja/1515647) · Blog oficial · Oficial · Heike Ritter · Microsoft Tech Community – Microsoft Defender for Endpoint Blog · 13 jul 2020. Ninja de MDE organizado por dos roles (SecOps y SecAdmin) y tres niveles (Fundamentals, Intermediate, Expert), con módulos de ASR, NGP, investigación, AIR, hunting, IOCs, reporting e integraciones.
- [Microsoft Defender for IoT Ninja Training](https://techcommunity.microsoft.com/blog/microsoftdefenderiotblog/microsoft-defender-for-iot-ninja-training/2428899) · Blog oficial · Oficial · Legado aún útil · Microsoft Tech Community – Microsoft Defender for IoT Blog. Ninja de Defender for IoT (OT/ICS) con más de 28 vídeos por módulos: visión general, despliegue, integración con Sentinel y temas avanzados como sensores pasivos y MITRE ICS. *Nota:* Fecha no visible (ID 2428899 ≈ 2021). Short link aka.ms/DefenderIoTNinja (citado por el usuario)
- [Become a Microsoft Defender External Attack Surface Management Ninja (Level 400)](https://techcommunity.microsoft.com/blog/defenderexternalattacksurfacemgmtblog/become-a-microsoft-defender-external-attack-surface-management-ninja-level-400-t/3743985/replies/3958720) · Blog oficial · Oficial · Legado aún útil · Microsoft Tech Community – Defender EASM Blog. Ninja de nivel 400 de Defender EASM: configuración de descubrimiento, inventario continuo, priorización de riesgos y análisis de activos, con knowledge check y certificado al superar 80%. *Nota:* URL vista apunta a un comentario (/replies/3958720) del post 3743985 (~2023). Short link aka.ms/DefenderEASMNinja (citado por el usuario)
- [skill-up-resources.md (fuente Markdown del skill-up training en MicrosoftDocs/defender-docs)](https://raw.githubusercontent.com/MicrosoftDocs/defender-docs/public/sentinel/skill-up-resources.md) · GitHub · Oficial · Legado aún útil · guywi-ms (ms.author: guywild) · GitHub – MicrosoftDocs/defender-docs · 16 may 2024. Fuente Markdown pública del artículo skill-up de Learn, útil para extraer todos los hipervínculos por módulo. *Nota:* La rama 'public' muestra ms.date 05/16/2024 y no incluye la línea del Training Lab que sí aparece en la página viva (08/07/2026); usar sólo como inventario de enlaces
- [Become a Microsoft Unified SOC Platform Ninja (copia sindicada)](https://thewindowsupdate.com/2024/01/02/become-a-microsoft-unified-soc-platform-ninja/) · Blog · Comunidad · Legado aún útil · Syndicated News · TheWindowsUpdate.com (republicación RSS de Tech Community) · 2 ene 2024. Copia RSS del Ninja de la plataforma unificada que conserva la tabla de contenidos original (XDR+SIEM Overview módulos 1-3 y Operating módulos 1-6). *Nota:* Útil para ver la estructura original 'Last updated January 2024'; el contenido técnico está superado por la GA de Sentinel en Defender
- [Microsoft Defender for Cloud Apps Ninja Training | June 2022](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-defender-for-cloud-apps-ninja-training--june-2022/2751518) · Blog oficial · Oficial · Legado aún útil · Microsoft Tech Community – Microsoft Security Community Blog · jun 2022. Ninja de Defender for Cloud Apps sobre descubrimiento de shadow IT, gobierno de apps, políticas y controles de sesión, protección de información y detección de amenazas, con knowledge checks y certificado. *Nota:* Edición 'June 2022'; short link aka.ms/MDCANinjaTraining. Fecha exacta de publicación no verificada
- [Microsoft Defender for Identity Ninja Training](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-defender-for-identity-ninja-training/2117904) · Blog oficial · Empleado de Microsoft · Legado aún útil · Brandon Lawson · Microsoft Tech Community – Microsoft Security Community Blog · 24 feb 2021. Ninja de Defender for Identity con módulos de despliegue de sensores, postura de identidad, detecciones de movimiento lateral, investigación e integración con hunting. *Nota:* Última versión visible 9.0 (22-ene-2024); autor hoy 'Former Employee'. No refleja el sensor unificado v3.x (2025-2026). Short link aka.ms/MDINinja

<a id="cambios"></a>

## Qué cambió y por qué importa

Cada fila remite al módulo donde se explica en detalle.

| Tema | Ninja original (2020–2024) | Hoy (noviembre de 2026) | Módulo |
|---|---|---|---|
| Portal | Portal de Azure | Portal de Microsoft Defender; el soporte en el portal de Azure termina el 31 de marzo de 2027 | [I1](01_Nivel_1_Inicial.md#i1) |
| Agente | Agente de Log Analytics (MMA/OMS) | Azure Monitor Agent con reglas de recolección de datos (MMA retirado el 31 de agosto de 2024) | [M2](02_Nivel_2_Intermedio.md#m2) |
| Ingesta personalizada | HTTP Data Collector API | API de ingesta de logs y CCF (fin de soporte de la API anterior el 14 de septiembre de 2026) | [M2](02_Nivel_2_Intermedio.md#m2), [A5](03_Nivel_3_Avanzado.md#a5) |
| Conectores propios | Azure Functions | Codeless Connector Framework (renombrado en junio de 2025) y agente constructor de conectores | [A5](03_Nivel_3_Avanzado.md#a5) |
| Retención larga | Basic, Archive y Azure Data Explorer | Data lake de Sentinel: GA el 30 de septiembre de 2025, hasta 12 años, onboarding integrado desde el 23 de septiembre de 2026 | [M3](02_Nivel_2_Intermedio.md#m3), [A8](03_Nivel_3_Avanzado.md#a8) |
| Correlación | Fusion | Motor de correlación de Defender XDR | [M7](02_Nivel_2_Intermedio.md#m7) |
| Reglas | Reglas de analítica | Detecciones personalizadas recomendadas para reglas nuevas desde octubre de 2025; las reglas existentes siguen vigentes | [M7](02_Nivel_2_Intermedio.md#m7) |
| Incidentes | Incidentes en Sentinel | Cola unificada en Defender e incident cases (vista previa) | [M9](02_Nivel_2_Intermedio.md#m9) |
| Inteligencia de amenazas | ThreatIntelligenceIndicator y MDTI independiente | ThreatIntelIndicators y ThreatIntelObjects; capacidades de MDTI incluidas en Defender y Sentinel | [M4](02_Nivel_2_Intermedio.md#m4) |
| Hunting | Livestream y marcadores | Hunts, KQL jobs y búsqueda avanzada unificada (livestream retirado) | [M10](02_Nivel_2_Intermedio.md#m10) |
| UEBA | Anomalías y perfiles | Más fuentes y la capa de UEBA behaviors con IA generativa | [M11](02_Nivel_2_Intermedio.md#m11) |
| Notebooks y ML | Azure Machine Learning y BYO-ML | Notebooks Spark sobre el data lake desde VS Code y orientación a Microsoft Fabric | [A7](03_Nivel_3_Avanzado.md#a7) |
| Multi-inquilino | Lighthouse y workspace manager | Gestión multi-inquilino de Defender, distribución de contenido, GDAP (vista previa) y RBAC por fila | [M1](02_Nivel_2_Intermedio.md#m1), [A9](03_Nivel_3_Avanzado.md#a9) |
| Migración | Webinars y mapeos manuales | Experiencia de migración de SIEM en Defender (GA en RSAC 2026) | [M6](02_Nivel_2_Intermedio.md#m6) |
| SOAR | Playbooks desde reglas de analítica | Reglas de automatización (lo anterior quedó en desuso en marzo de 2026), Logic Apps Standard y Agent Loop | [M13](02_Nivel_2_Intermedio.md#m13), [X1](04_Nivel_4_Experto_agentico.md#x1) |
| IA | Copilot for Security (2024) | Security Copilot incluido en Microsoft 365 E5 y E7, agentes y Security Store | [X2](04_Nivel_4_Experto_agentico.md#x2), [X5](04_Nivel_4_Experto_agentico.md#x5) |
| Plataforma agéntica | No existía | Servidor MCP de Sentinel (GA el 18 de noviembre de 2025) y Sentinel graph | [X6](04_Nivel_4_Experto_agentico.md#x6), [A8](03_Nivel_3_Avanzado.md#a8) |
| APIs | Graph /security/alerts | alerts_v2 e incidents (el endpoint anterior se retiró el 15 de octubre de 2026) y runHuntingQuery | [A6](03_Nivel_3_Avanzado.md#a6) |
| Credenciales | Applied Skills de Sentinel | SC-200 actualizado el 21 de octubre de 2026 (la Applied Skill se retiró el 30 de abril de 2025) | [I0](01_Nivel_1_Inicial.md#i0) |
| Laboratorios | KQL Lab, SimuLand | Nuevo Training Lab con 17 ejercicios y laboratorios SC-200 para Defender (SimuLand archivado) | [I5](01_Nivel_1_Inicial.md#i5) |
| Webinars | aka.ms/SecurityWebinars | securitycommunity.microsoft.com/VirtualEvents y el canal de YouTube de la Security Community | [C2](05_Comunidad.md#c2) |

<a id="rutas"></a>

## Rutas por rol

Las horas son estimaciones de lectura y práctica.

- **Fundamentos de operaciones de seguridad** (~37 h). Todos los perfiles: el punto de partida común. Módulos: [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3), [I4](01_Nivel_1_Inicial.md#i4), [I5](01_Nivel_1_Inicial.md#i5).
- **Arquitecto de seguridad** (~72 h). Diseño de plataforma, datos, costos, residencia y gobierno. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M1](02_Nivel_2_Intermedio.md#m1), [M2](02_Nivel_2_Intermedio.md#m2), [M3](02_Nivel_2_Intermedio.md#m3), [M4](02_Nivel_2_Intermedio.md#m4), [M5](02_Nivel_2_Intermedio.md#m5), [M6](02_Nivel_2_Intermedio.md#m6), [A1](03_Nivel_3_Avanzado.md#a1), [A8](03_Nivel_3_Avanzado.md#a8), [A9](03_Nivel_3_Avanzado.md#a9), [X2](04_Nivel_4_Experto_agentico.md#x2), [X6](04_Nivel_4_Experto_agentico.md#x6).
- **Ingeniero de seguridad** (~119 h). Conectores, contenido, detección, automatización y contenido como código. Módulos: [I3](01_Nivel_1_Inicial.md#i3), [I4](01_Nivel_1_Inicial.md#i4), [M2](02_Nivel_2_Intermedio.md#m2), [M4](02_Nivel_2_Intermedio.md#m4), [M5](02_Nivel_2_Intermedio.md#m5), [M7](02_Nivel_2_Intermedio.md#m7), [M8](02_Nivel_2_Intermedio.md#m8), [M12](02_Nivel_2_Intermedio.md#m12), [M13](02_Nivel_2_Intermedio.md#m13), [A1](03_Nivel_3_Avanzado.md#a1), [A2](03_Nivel_3_Avanzado.md#a2), [A3](03_Nivel_3_Avanzado.md#a3), [A4](03_Nivel_3_Avanzado.md#a4), [A5](03_Nivel_3_Avanzado.md#a5), [A6](03_Nivel_3_Avanzado.md#a6), [A7](03_Nivel_3_Avanzado.md#a7), [X1](04_Nivel_4_Experto_agentico.md#x1), [X4](04_Nivel_4_Experto_agentico.md#x4).
- **Analista del SOC** (~68 h). Triage, investigación, búsqueda y uso diario de la IA. Módulos: [I4](01_Nivel_1_Inicial.md#i4), [M7](02_Nivel_2_Intermedio.md#m7), [M9](02_Nivel_2_Intermedio.md#m9), [M10](02_Nivel_2_Intermedio.md#m10), [M11](02_Nivel_2_Intermedio.md#m11), [M13](02_Nivel_2_Intermedio.md#m13), [A2](03_Nivel_3_Avanzado.md#a2), [X2](04_Nivel_4_Experto_agentico.md#x2), [X5](04_Nivel_4_Experto_agentico.md#x5).
- **Automatización e IA** (~65 h). SOAR avanzado, Security Copilot, agentes y MCP (ampliación de esta edición). Módulos: [M13](02_Nivel_2_Intermedio.md#m13), [X1](04_Nivel_4_Experto_agentico.md#x1), [X2](04_Nivel_4_Experto_agentico.md#x2), [X3](04_Nivel_4_Experto_agentico.md#x3), [X4](04_Nivel_4_Experto_agentico.md#x4), [X5](04_Nivel_4_Experto_agentico.md#x5), [X6](04_Nivel_4_Experto_agentico.md#x6), [X7](04_Nivel_4_Experto_agentico.md#x7).
- **Líder del SOC o CISO** (~36 h). Valor, costos, métricas, riesgos y gobierno de la IA. Módulos: [I1](01_Nivel_1_Inicial.md#i1), [I2](01_Nivel_1_Inicial.md#i2), [M3](02_Nivel_2_Intermedio.md#m3), [M6](02_Nivel_2_Intermedio.md#m6), [M12](02_Nivel_2_Intermedio.md#m12), [X2](04_Nivel_4_Experto_agentico.md#x2), [X5](04_Nivel_4_Experto_agentico.md#x5).

<a id="plan"></a>

## Plan de entrenamiento sugerido

Calendario de referencia de 25 semanas para una dedicación de 8 a 12 horas por semana (unas 237 horas). Cada semana deja un entregable verificable; las evaluaciones cierran las semanas 4, 12, 19 y 25.

| Semana | Módulos | Foco | Entregable |
|---|---|---|---|
| 1 | [P0](01_Nivel_1_Inicial.md#p0), [I0](01_Nivel_1_Inicial.md#i0), [I1](01_Nivel_1_Inicial.md#i1) | Fundamentos de nube, identidad y datos; qué es Sentinel hoy | Suscripción de laboratorio con presupuesto y alertas; resumen de Sentinel para un CISO |
| 2 | [I2](01_Nivel_1_Inicial.md#i2), [I3](01_Nivel_1_Inicial.md#i3) | Patrones de uso y despliegue | Workspace incorporado al portal de Defender con Entra ID y cinco reglas activas |
| 3 | [I4](01_Nivel_1_Inicial.md#i4) | KQL esencial | Cinco consultas propias documentadas y un caso de Kusto Detective Agency |
| 4 | [I5](01_Nivel_1_Inicial.md#i5), [C1](05_Comunidad.md#c1), [C5](05_Comunidad.md#c5) | Laboratorio y rutina de actualización | Training Lab desplegado; evaluación del nivel 1 aprobada |
| 5 | [M1](02_Nivel_2_Intermedio.md#m1), [M3](02_Nivel_2_Intermedio.md#m3) | Arquitectura de workspaces, niveles de datos y costos | Árbol de decisión aplicado a un caso y estimación de costos con dos escenarios |
| 6 | [M2](02_Nivel_2_Intermedio.md#m2) | Recolección de datos con AMA, CEF/Syslog y API de ingesta | Reenviador Linux y eventos de Windows funcionando con alerta de salud |
| 7 | [M4](02_Nivel_2_Intermedio.md#m4), [M5](02_Nivel_2_Intermedio.md#m5) | Enriquecimiento y transformación | Watchlists en uso, regla de coincidencia de indicadores y una transformación split |
| 8 | [M7](02_Nivel_2_Intermedio.md#m7) | Analítica y detecciones personalizadas | Regla programada, NRT y detección personalizada con acción de respuesta |
| 9 | [M9](02_Nivel_2_Intermedio.md#m9), [M8](02_Nivel_2_Intermedio.md#m8) | Incidentes, investigación y reportes | Incidente investigado con línea de tiempo y libro de eficiencia del SOC |
| 10 | [M10](02_Nivel_2_Intermedio.md#m10) | Hunting | Un hunt documentado convertido en regla |
| 11 | [M11](02_Nivel_2_Intermedio.md#m11), [M12](02_Nivel_2_Intermedio.md#m12) | UEBA, salud y optimización | UEBA habilitado y regla que alerta sobre cambios en reglas de analítica |
| 12 | [M13](02_Nivel_2_Intermedio.md#m13), [M6](02_Nivel_2_Intermedio.md#m6) | Automatización esencial y migración | Reglas de automatización y playbook en uso; plan de migración; evaluación del nivel 2 aprobada |
| 13 | [A1](03_Nivel_3_Avanzado.md#a1), [A3](03_Nivel_3_Avanzado.md#a3) | ASIM y casos de uso | Regla independiente de la fuente y diseño completo de un caso de uso |
| 14 | [A2](03_Nivel_3_Avanzado.md#a2) | KQL avanzado y optimización | Detección de anomalías con series temporales y una función reutilizable |
| 15 | [A4](03_Nivel_3_Avanzado.md#a4) | Contenido como código y CI/CD | Repositorio conectado con despliegue de reglas y una prueba de detección |
| 16 | [A5](03_Nivel_3_Avanzado.md#a5), [A6](03_Nivel_3_Avanzado.md#a6) | Conectores CCF y APIs | Conector CCF propio y automatización con la API de Graph |
| 17 | [A7](03_Nivel_3_Avanzado.md#a7) | Notebooks y machine learning | Notebook programado que escribe una tabla consumida por una regla |
| 18 | [A8](03_Nivel_3_Avanzado.md#a8) | Data lake, graph y trabajos | KQL job sobre el lago que alimenta una detección |
| 19 | [A9](03_Nivel_3_Avanzado.md#a9), [C2](05_Comunidad.md#c2), [C3](05_Comunidad.md#c3), [C4](05_Comunidad.md#c4) | Multi-inquilino, MSSP y comunidad | Matriz de delegación para un MSSP; evaluación del nivel 3 aprobada |
| 20 | [X1](04_Nivel_4_Experto_agentico.md#x1) | SOAR avanzado con Logic Apps | Playbook con aprobación en Teams, identidad administrada y contención |
| 21 | [X2](04_Nivel_4_Experto_agentico.md#x2) | Security Copilot en el SOC | Guía de prompts del SOC y comparación con el triage manual |
| 22 | [X3](04_Nivel_4_Experto_agentico.md#x3), [X4](04_Nivel_4_Experto_agentico.md#x4) | Security Copilot con Logic Apps, plugins y promptbooks | Playbook que invoca Security Copilot y un plugin KQL propio |
| 23 | [X5](04_Nivel_4_Experto_agentico.md#x5), [X6](04_Nivel_4_Experto_agentico.md#x6) | Agentes y servidor MCP | Agente propio con herramientas MCP y su ficha de gobierno |
| 24 | [X7](04_Nivel_4_Experto_agentico.md#x7) | Proyecto integrador: fases 1 a 4 | Plataforma, datos, detección y validación funcionando |
| 25 | [X7](04_Nivel_4_Experto_agentico.md#x7) | Proyecto integrador: fases 5 a 8 | Automatización, IA, agentes y gobierno; evaluación del nivel 4 y reto final |

<a id="laboratorio"></a>

## Tu laboratorio

**Tenant y suscripción de laboratorio.** Nunca practiques con datos de producción ni de clientes sin autorización. Usa una suscripción propia con la cuenta gratuita de Azure o una suscripción de pruebas, y configura un presupuesto con alertas desde el primer día.

**Sentinel.** La prueba gratuita cubre 10 GB/día durante 31 días en el nivel de analítica. Conecta el workspace al portal de Defender como principal, porque el Training Lab y muchas funciones nuevas lo requieren.

**Datos de práctica.** El Microsoft Sentinel Training Lab carga datos pregrabados y 17 ejercicios; para KQL puro, el clúster gratuito de Azure Data Explorer y Kusto Detective Agency no requieren suscripción.

**Costos a vigilar.** Consultas y cómputo del data lake, ejecuciones de Logic Apps, el plan de Logic Apps Standard y las SCU de Security Copilot. Si tu tenant tiene Microsoft 365 E5, la inclusión de Security Copilot puede cubrir la práctica; si aprovisionas SCU, recuerda que se cobran por hora y desaprovisiona al terminar.

**Limpieza.** Al terminar cada nivel, elimina lo que no vayas a reutilizar. Un laboratorio barato y desechable es la mejor inversión de esta ruta.

La matriz de qué se puede practicar en el laboratorio y qué solo en producción está en [07_Laboratorio_y_practica_en_produccion.md](07_Laboratorio_y_practica_en_produccion.md). La guía para construir el entorno está en el [anexo común](../Anexo_Entorno_de_practica.md).

<a id="mapa"></a>

## Mapa de módulos

- **Nivel 1 · Inicial:** [P0 Prerrequisitos](01_Nivel_1_Inicial.md#p0) · [I0 Cómo aprender y soporte](01_Nivel_1_Inicial.md#i0) · [I1 Sentinel hoy](01_Nivel_1_Inicial.md#i1) · [I2 Cómo se usa](01_Nivel_1_Inicial.md#i2) · [I3 Despliegue y primeros pasos](01_Nivel_1_Inicial.md#i3) · [I4 KQL esencial](01_Nivel_1_Inicial.md#i4) · [I5 Laboratorios](01_Nivel_1_Inicial.md#i5)
- **Nivel 2 · Intermedio:** [M1 Workspaces y tenants](02_Nivel_2_Intermedio.md#m1) · [M2 Recolección de datos](02_Nivel_2_Intermedio.md#m2) · [M3 Logs, niveles y costos](02_Nivel_2_Intermedio.md#m3) · [M4 Enriquecimiento](02_Nivel_2_Intermedio.md#m4) · [M5 Transformación de logs](02_Nivel_2_Intermedio.md#m5) · [M6 Migración](02_Nivel_2_Intermedio.md#m6) · [M7 Analítica y detecciones](02_Nivel_2_Intermedio.md#m7) · [M8 Workbooks y reportes](02_Nivel_2_Intermedio.md#m8) · [M9 Incidentes](02_Nivel_2_Intermedio.md#m9) · [M10 Hunting](02_Nivel_2_Intermedio.md#m10) · [M11 UEBA](02_Nivel_2_Intermedio.md#m11) · [M12 Salud y optimización](02_Nivel_2_Intermedio.md#m12) · [M13 Automatización esencial](02_Nivel_2_Intermedio.md#m13)
- **Nivel 3 · Avanzado:** [A1 ASIM](03_Nivel_3_Avanzado.md#a1) · [A2 KQL avanzado](03_Nivel_3_Avanzado.md#a2) · [A3 Casos de uso](03_Nivel_3_Avanzado.md#a3) · [A4 Contenido como código](03_Nivel_3_Avanzado.md#a4) · [A5 Conectores CCF](03_Nivel_3_Avanzado.md#a5) · [A6 APIs](03_Nivel_3_Avanzado.md#a6) · [A7 Notebooks y ML](03_Nivel_3_Avanzado.md#a7) · [A8 Data lake y graph](03_Nivel_3_Avanzado.md#a8) · [A9 Multi-inquilino y MSSP](03_Nivel_3_Avanzado.md#a9)
- **Nivel 4 · Experto agéntico:** [X1 SOAR con Logic Apps](04_Nivel_4_Experto_agentico.md#x1) · [X2 Security Copilot](04_Nivel_4_Experto_agentico.md#x2) · [X3 Copilot + Logic Apps](04_Nivel_4_Experto_agentico.md#x3) · [X4 Plugins y promptbooks](04_Nivel_4_Experto_agentico.md#x4) · [X5 Agentes](04_Nivel_4_Experto_agentico.md#x5) · [X6 Servidor MCP](04_Nivel_4_Experto_agentico.md#x6) · [X7 Proyecto integrador](04_Nivel_4_Experto_agentico.md#x7)
- **Comunidad:** [C1 Referentes](05_Comunidad.md#c1) · [C2 YouTube y podcasts](05_Comunidad.md#c2) · [C3 Libros](05_Comunidad.md#c3) · [C4 En español](05_Comunidad.md#c4) · [C5 Mantenerse al día](05_Comunidad.md#c5)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

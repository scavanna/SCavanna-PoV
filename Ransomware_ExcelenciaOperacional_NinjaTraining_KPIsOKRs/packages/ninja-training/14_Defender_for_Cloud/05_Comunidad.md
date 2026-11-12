# Comunidad · Referentes, canales y cómo mantenerse al día

*Microsoft Defender for Cloud Ninja Training · Edición 2026*

[← Track · Operación y excelencia](04_Track_Operacion_y_excelencia.md) · [Índice del programa](README.md) · [Evaluaciones y respuestas →](06_Evaluaciones_y_respuestas.md)

<a id="comunidad"></a>

MVP y empleados de Microsoft que enseñan Defender for Cloud, los canales oficiales y comunitarios, repositorios, videos, eventos y recursos en español. Terminas con una rutina semanal para seguir un producto que publica cambios varias veces al mes.

*Transversal · 3 módulos · ~6 horas · 25 recursos*

**Módulos de este nivel:** [C1 Referentes](#c1) · [C2 Canales y repositorios](#c2) · [C3 Recursos en español](#c3)

<a id="c1"></a>

## C1 · Referentes: MVP y empleados de Microsoft

*Transversal · ~2 h · Origen: Formato Ninja: comunidad (directorio de referentes verificados)*

El espíritu Ninja es aprender de quienes construyen y usan el producto. El Ninja de Defender for Cloud nació en 2020, inspirado en el de Defender for Endpoint, y su última actualización conocida es de diciembre de 2025. El directorio de este módulo reúne referentes con rol público verificado —product managers de Defender for Cloud, MVP que publican sobre Defender for Servers, Sentinel, KQL y costos, y voces hispanohablantes— con su foco, sus canales y una pieza insignia. Úsalo para armar tu radar personal: sigue a pocos, con constancia, y contrasta siempre lo que leas con la documentación oficial y su fecha.

2026 trajo cambios en el equipo: el autor del Ninja dejó Microsoft a fines de octubre, otros referentes históricos de Defender for Servers salieron en la misma época y algunas product managers pasaron a la seguridad de agentes. Su contenido sigue siendo valioso, pero preséntalos como ex-Microsoft y verifica si lo que enseñan sigue vigente: muchos materiales de 2023 y 2024 todavía describen el agente de Log Analytics o los controles de aplicación adaptables, ya retirados. La investigación encontró pocos referentes con base en MCSA que publiquen con regularidad sobre Defender for Cloud: es un espacio abierto para tu equipo.

**Por qué importa**

Defender for Cloud cambia cada mes y muchos matices —una contradicción de precios, una consulta que dejó de funcionar o una función que pasó a Agent 365— aparecen primero en blogs, repositorios y webinars de quienes trabajan con el producto. Seguir a referentes verificados acorta tu tiempo de actualización y te ayuda a detectar lo que la documentación todavía no explica.

**Qué vas a lograr**

- Identificar referentes confiables por especialidad: postura, servidores, SOC y KQL, IA, costos y comunidad en español.
- Construir una lista de seguimiento personal con fuentes verificadas y vigentes.
- Distinguir contenido oficial, de empleados, de MVP y de la comunidad al evaluar una recomendación.

> **Atención.** Varios referentes históricos de Defender for Cloud ya no están en Microsoft: el creador del Ninja oficial anunció su salida a fines de octubre de 2026. Su contenido sigue siendo útil, pero preséntalo como de un ex-Microsoft y verifica que siga vigente ([publicación de despedida](https://www.linkedin.com/posts/yuridiogenes_microsoft-cybersecurity-gratitude-share-7521869559776051200-urIA)).

> **Consejo Ninja.** Buenos ejemplos del formato comunitario: el análisis de costos de Defender CSPM de un MVP y la sincronización de alertas de Defender for Cloud con incidentes de Sentinel de otro. Contrástalos siempre con la página de precios vigente, el modelo DWU y la integración actual con Defender XDR ([costos de Defender CSPM](https://thoor.tech/Demystifying-MDC-and-CSPM-cost/), [alertas e incidentes](https://cloudbrothers.info/en/sync-defender-cloud-alerts-sentinel-incidents/)).

### Directorio de referentes verificados

- **Dick Lake** (Empleado de Microsoft): Senior Program Manager; mantiene laboratorios de Defender for Cloud (preparación del entorno, cargas de IA) y presenta sesiones de seguridad de IA. [GitHub](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Labs/Modules/Module-1-Preparing-the-Environment.md) · [Otro](https://developer.microsoft.com/en-us/reactor/events/26862/) · [Evidencia de rol](https://developer.microsoft.com/en-us/reactor/events/26862/)
- **Fernanda Vela** (Empleado de Microsoft, EE. UU. (trayectoria previa en México y LATAM)): Senior Product Manager de Microsoft Security en Defender for Cloud (seguridad de almacenamiento, multinube) y MDASH; ex-Premier Field Engineer para Latinoamérica; presenta webinars en español. [GitHub](https://github.com/velahuer) · [YouTube](https://www.youtube.com/watch?v=eYv2tFrY9qk) · [Otro](https://securitycommunity.microsoft.com/VirtualEvents/Webinar-Details/?id=2fa0bdef-866b-f111-a825-6045bd06ff19) · [Evidencia de rol](https://www.linkedin.com/in/mfvelah)
- **Gal Fenigshtein** (Empleado de Microsoft, Israel): Senior Product Manager de Defender for Cloud centrado en Defender for Servers: FIM basado en MDE y detección de malware sin agente. [YouTube](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-fifty-three) · [Evidencia de rol](https://il.linkedin.com/in/gal-fenigshtein)
- **Giulio Astori** (Empleado de Microsoft): Product manager de Defender CSPM: rutas de ataque, exposición a Internet, gobernanza, cumplimiento regulatorio y reporting (workbooks, Power BI). [Blog](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-adds-four-new-regulatory-frameworks/4433440) · [YouTube](https://www.youtube.com/watch?v=twFUk_rmueg) · [Otro](https://www.youtube.com/watch?v=SxZdqBZTqks) · [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-defender-for-cloud-adds-four-new-regulatory-frameworks/4433440)
- **Gladys Rodriguez** (Empleado de Microsoft): Co-anfitriona de The Azure Security Podcast (presentado como podcast de expertos de seguridad de Microsoft). [Otro](https://music.amazon.com/podcasts/a526c965-4e12-4482-8527-7a8de7b7d7c2/the-azure-security-podcast) · [Evidencia de rol](https://azuresecuritypodcast.azurewebsites.net/)
- **Heike Ritter** (Empleado de Microsoft): Autora y mantenedora de los Ninja de Defender for Endpoint y Defender XDR (actualizados en sep/oct-2026), modelo del que nació el Ninja de Defender for Cloud. [Otro](https://techcommunity.microsoft.com/tag/ninja%20training) · [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/become-a-microsoft-defender-for-endpoint-ninja/1515647)
- **John Savill** (Empleado de Microsoft, EE. UU.): CTO de Americas Markets and Industries en Microsoft; su canal personal publica el «Azure Weekly Update» (incluye novedades de Defender for Cloud) y videos de seguridad y arquitectura. [YouTube](https://www.youtube.com/@NTFAQGuy/videos) · [Otro](https://www.youtube.com/watch?v=HxalS8yjSyk) · [Evidencia de rol](https://azuresecuritypodcast.azurewebsites.net/)
- **Lior Arviv** (Empleado de Microsoft): Principal Product Manager de Defender for Cloud: postura, gobernanza y la «NextGen Defender for Cloud» integrada en el portal de Defender. [YouTube](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-twenty-six) · [Otro](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-four) · [Evidencia de rol](https://www.linkedin.com/posts/lior-arviv_nextgen-defender-for-cloud-phase-1-public-activity-7399687114604449792-HqJ4)
- **Madalina Iosif** (Empleado de Microsoft, Rumania): Technical Product Manager y SME de CSPM en Defender for Cloud; ayudó a mantener actualizado el Ninja oficial en 2025. [GitHub](https://github.com/MadalinaIosif) · [Otro](https://www.linkedin.com/posts/yuridiogenes_mdc-defenderforcloud-ninjatraining-activity-7412143098379661312-37M0) · [Evidencia de rol](https://himalayas.app/@madalinaiosif)
- **Matt McSpirit** (Empleado de Microsoft): Presentador de Microsoft Mechanics (canal oficial de Microsoft para TI) con demos de extremo a extremo de Defender for Cloud. [YouTube](https://www.youtube.com/watch?v=CnqmC-CQs48) · [Evidencia de rol](https://www.youtube.com/watch?v=CnqmC-CQs48)
- **Safeena Begum Lepakshi** (Empleado de Microsoft, EE. UU.): Principal PM Manager; antes en Defender for Cloud (CIEM, DevOps, APIs, IA) y hoy en gobierno, seguridad y observabilidad de agentes con Agent 365. [Blog](https://muckrack.com/safeena-begum-lepakshi/articles) · [GitHub](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Labs/Modules/Module%2024%20-%20AI%20Workloads.md) · [YouTube](https://www.youtube.com/watch?v=lRf5b2Kev9A) · [Evidencia de rol](https://www.linkedin.com/in/safeena-begum-550a5740)
- **Sarah Young** (Empleado de Microsoft): Co-anfitriona de The Azure Security Podcast y coautora del Exam Ref SC-200 (2.ª ed., 2026), que cubre Defender for Cloud. [Otro](https://azuresecuritypodcast.azurewebsites.net/) · [Evidencia de rol](https://azuresecuritypodcast.azurewebsites.net/)
- **Yura Lee** (Empleado de Microsoft): Product manager de Defender for Cloud (APIs, bases de datos) y autora del «Microsoft Defender for Cloud Customer Newsletter» mensual hasta su última edición (ago-2026). [Blog](https://techcommunity.microsoft.com/category/microsoft-defender-for-cloud/blog/MicrosoftDefenderCloudBlog/all-posts) · [GitHub](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Labs/Modules/Module-12-Microsoft-Defender-for-Cloud-database-protection.md) · [YouTube](https://www.youtube.com/watch?v=9GS_uWfz6mE) · [Evidencia de rol](https://www.youtube.com/watch?v=9GS_uWfz6mE)
- **Charbel Nemnom** (MVP de Microsoft, Suiza): Arquitecto de nube y seguridad (MVP de Azure desde 2014 según su sitio): Sentinel, Defender XDR/Defender for Cloud, guías de certificación (SC-500, AZ-802) y ahorro de costos SIEM. [Blog](https://charbelnemnom.com/) · [Otro](https://charbelnemnom.com/author/charbel-nemnom/) · [Evidencia de rol](https://charbelnemnom.com/about/)
- **Fabian Bader** (MVP de Microsoft, Alemania): Detección e identidad (SIEM & XDR); en Cloudbrothers documenta la sincronización de alertas de Defender for Cloud con Sentinel y rutas de ataque en Azure. [Blog](https://cloudbrothers.info/) · [GitHub](https://github.com/f-bader/AzSentinelQueries) · [Otro](https://cloudbrothers.info/en/categories/defender-for-cloud/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5004810)
- **Jeffrey Appel** (MVP de Microsoft, Países Bajos): MVP de seguridad con series profundas sobre Defender for Endpoint y Defender for Cloud (FIM vía MDE, Defender for Storage, onboarding directo, protección de IA) y nueva serie sobre toda la suite Defender (2026). [Blog](https://jeffreyappel.nl/tag/Defender-for-Cloud/) · [Otro](https://jeffreyappel.nl/defending-with-microsoft-a-deep-dive-into-the-microsoft-defender-suite-blog-series-intro/) · [Evidencia de rol](https://jeffreyappel.nl/)
- **Jorge Castañeda** (MVP de Microsoft, Perú): MVP de Security en español (SIEM & XDR): laboratorios con Defender XDR y Sentinel, priorización de CVE y comunidad MUG Perú; referente LATAM para C3. [Blog](https://blog.d3fend.me/) · [Otro](https://blog.d3fend.me/about/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5000594)
- **Kaido Järvemets** (MVP de Microsoft, Estonia): MVP (desde 2010) en Azure híbrido y seguridad: Azure Arc, Defender for Servers en híbrido, automatización; parte del contenido es de pago. [Blog](https://docs.kaidojarvemets.com/articles) · [Otro](https://docs.kaidojarvemets.com/training/defender-for-servers) · [Evidencia de rol](https://docs.kaidojarvemets.com/about)
- **Morten Knudsen** (MVP de Microsoft, Dinamarca): Recolección de logs con AMA/DCR/Logs Ingestion API y costos de Log Analytics; citado por Yuri Diogenes en la difusión de Defender for AI Services (2026). [Blog](https://mortenknudsen.net/) · [GitHub](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · [Otro](https://www.linkedin.com/feed/update/urn:li:activity:7433171249780121600/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5005156)
- **Pierre Thoor** (MVP de Microsoft, Suecia): MVP de Security con área Cloud Security (Defender for Cloud, seguridad de red de Azure, GitHub Advanced Security) y SIEM & XDR; costos de Defender CSPM y policy-as-code. [Blog](https://thoor.tech/) · [Otro](https://thoor.tech/blog/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/6fba834e-4a7f-ec11-8d21-0022482837b1)
- **Sami Lamppu** (MVP de Microsoft, Finlandia): Sentinel, Defender XDR y Security Copilot; entradas sobre Defender for Cloud (integración con MDE, auditoría de planes con Policy, monitoreo de la extensión MDE en Azure/Arc). [Blog](https://samilamppu.com/) · [Otro](https://samilamppu.com/category/microsoft-defender-for-cloud/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/06ab3a7e-e0d7-eb11-bacb-000d3a154f10)
- **Sergio Albea** (MVP de Microsoft, Suiza (originario de España)): Threat hunting con KQL en Defender XDR y feeds de TI con Logic Apps; hispanohablante (perfil MVP con español). [GitHub](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · [YouTube](https://www.youtube.com/watch?v=e-mg6XYcCAY) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/27a80f6f-c617-486e-9bb3-dd1ad4194635)
- **Thomas Naunheim** (MVP de Microsoft, Alemania): Seguridad de identidad en la nube (workload identities, EntraOps, Entra ID Attack & Defense), complemento para CIEM y rutas de ataque basadas en identidad. [Blog](https://www.cloud-architekt.net/tags) · [GitHub](https://github.com/cloud-architekt) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5003945)
- **Tom Janetscheck** (Comunidad, Alemania): Referente de Defender for Servers (despliegue a escala, agentes, integración con MDVM) y coautor del libro de Microsoft Press; Senior PM de Microsoft hasta los despidos de 2026 según el post de recomendación de Yuri Diogenes. [GitHub](https://github.com/Azure/Microsoft-Defender-for-Cloud/blob/main/Workbooks/README.md) · [YouTube](https://learn.microsoft.com/en-us/azure/defender-for-cloud/episode-twenty-seven) · [Otro](https://www.getprog.ai/profile/32520935) · [Evidencia de rol](https://www.linkedin.com/feed/update/urn:li:activity:7510017901672804353/)
- **Yuri Diogenes** (Comunidad, EE. UU.): Creador (2020) y mantenedor del Ninja oficial de Defender for Cloud y presentador de «Defender for Cloud in the Field»; Principal PM Manager del equipo CxE de Defender for Cloud (y desde ene-2026 también de Azure Network Security) hasta su salida de Microsoft el 30-oct-2026; autor de 36 libros. [YouTube](https://www.youtube.com/playlist?list=PL3ZTgFEc7LysiX4PfHhdJPR7S8mGO14YS) · [Otro](https://learn.microsoft.com/en-us/shows/mdc-in-the-field/) · [Evidencia de rol](https://www.linkedin.com/posts/yuridiogenes_microsoft-cybersecurity-gratitude-share-7521869559776051200-urIA)

**Manos a la obra**

1. Elige seis referentes del directorio —uno por especialidad: postura, servidores, SOC y KQL, IA, costos y comunidad en español— y síguelos en su blog, GitHub o YouTube; marca quiénes siguen en Microsoft a noviembre de 2026.
2. Cada mes, comparte con tu equipo una pieza de un referente y contrástala con la página oficial de Learn: anota la fecha, el estado (vista previa o GA) y si sigue vigente después de los retiros de 2024 a 2026.

<a id="c2"></a>

## C2 · Canales, repositorios, videos y eventos

*Transversal · ~2 h · Origen: Formato Ninja: comunidad (webinars, repositorios, laboratorios y eventos)*

La práctica de este programa se apoya en canales oficiales. El repositorio **Azure/Microsoft-Defender-for-Cloud** reúne laboratorios (28 módulos en tres niveles, versión 3.0 de mayo de 2024, algunos desactualizados), workbooks, plantillas de Logic Apps, definiciones de Policy, simulaciones y scripts, sin SLA. La serie **Defender for Cloud in the Field** suma 66 episodios en Learn —el último numerado, del 3 de febrero de 2026, trata la nueva puntuación segura— y su lista de YouTube incorpora cortos «Start Secure / Stay Secure». Los webinars de la Microsoft Security Community, Microsoft Mechanics y las sesiones grabadas de Ignite 2025 completan el material en video.

Para el pulso semanal: el blog oficial en Tech Community, cuya entrada del 20 de octubre de 2026 presentó la DWU, con su feed RSS; el Microsoft Defender Monthly News, que desde abril de 2026 incluyó Defender for Cloud en el portal de Defender y cuya última edición oficial es de agosto (un MVP lo continúa desde octubre como edición comunitaria); The Azure Security Podcast; el canal de John Savill, y los repositorios de EPAC y Azure Landing Zones para policy-as-code. El boletín mensual propio de Defender for Cloud terminó el 3 de agosto de 2026. Noviembre trae **Microsoft Ignite**, del 17 al 20 en San Francisco y en línea gratis, con un pre-día de seguridad el 16.

**Por qué importa**

La documentación dice qué hace cada control; los repositorios, laboratorios y webinars muestran cómo se configura, qué falla en producción y qué cambió esta semana. Un puñado de canales bien elegidos sostiene la práctica del programa y evita depender de capturas de pantalla desactualizadas.

**Qué vas a lograr**

- Suscribirte a los canales oficiales que mantienen vigente tu conocimiento.
- Usar los repositorios y laboratorios oficiales como base de tu práctica, sabiendo qué partes están desactualizadas.
- Planificar tu participación en eventos, webinars y sesiones de Ignite.

> **Novedad.** Agenda de noviembre de 2026: Microsoft Ignite, del 17 al 20 en San Francisco y en línea gratis, con un pre-día de seguridad el 16 de noviembre; puede cambiar estados de vista previa de varias funciones de este programa ([Microsoft Ignite](https://ignite.microsoft.com/), [guía de seguridad en Ignite 2026](https://www.microsoft.com/en-us/security/blog/2026/09/30/secure-whats-next-your-guide-to-microsoft-security-at-microsoft-ignite-2026/)).

> **Atención.** El repositorio oficial no tiene SLA y parte de sus laboratorios es de 2023 o 2024; Arc Jumpstart está en modo de mantenimiento y su escenario de Defender for Cloud todavía usa un área de trabajo de Log Analytics heredada ([repositorio](https://github.com/Azure/Microsoft-Defender-for-Cloud), [Arc Jumpstart](https://jumpstart.azure.com/azure_arc_jumpstart/azure_arc_servers/day2/arc_defender)).

**¿Tienes poco tiempo?**

- [Defender for Cloud in the Field (YouTube playlist)](https://www.youtube.com/playlist?list=PL3ZTgFEc7LysiX4PfHhdJPR7S8mGO14YS) · Video
- [Microsoft Defender for Cloud Blog – All posts](https://techcommunity.microsoft.com/category/microsoft-defender-for-cloud/blog/MicrosoftDefenderCloudBlog/all-posts) · Blog oficial
- [Azure/Microsoft-Defender-for-Cloud (repositorio de la comunidad)](https://github.com/Azure/Microsoft-Defender-for-Cloud) · GitHub

### Anuncios y blogs oficiales

- [Microsoft Defender for Cloud Blog – All posts](https://techcommunity.microsoft.com/category/microsoft-defender-for-cloud/blog/MicrosoftDefenderCloudBlog/all-posts) · Blog oficial · Oficial · Nuevo · Equipo de producto de Defender for Cloud · Microsoft Tech Community · 20 oct 2026. Listado completo del blog oficial (DWU, MDASH, newsletters, serverless, multinube, contenedores, hardened images) para seguir anuncios con autor y fecha.
- [Secure what's next: Your guide to Microsoft Security at Microsoft Ignite 2026](https://www.microsoft.com/en-us/security/blog/2026/09/30/secure-whats-next-your-guide-to-microsoft-security-at-microsoft-ignite-2026/) · Blog oficial · Empleado de Microsoft · Nuevo · Lindsay Myers · Microsoft Security Blog · 30 sep 2026. Guía de seguridad para Ignite 2026: Security Pre-Day el 16-nov (13-17 h PT), keynote el 17-nov en Chase Center, Security Innovation Session, «Secure the Night» y vecindario Security & Agent 365.

### Webinars, videos y podcasts

- [Defender for Cloud in the Field (YouTube playlist)](https://www.youtube.com/playlist?list=PL3ZTgFEc7LysiX4PfHhdJPR7S8mGO14YS) · Video · Oficial · Nuevo · Microsoft Security · YouTube – Microsoft Security · oct 2026. Lista de 68 videos con todos los episodios numerados (#32-#66: APIs, CSPM, FIM nuevo, drift binario, gated deployment, reachability, Secure Score nuevo) más los cortos «Start Secure/Stay Secure» de 2026.
- [Microsoft Defender for Cloud (playlist de webinars de la Microsoft Security Community)](https://www.youtube.com/playlist?list=PLmAptfqzxVEUvnWqb-AcIx7jABPTtyjdv) · Webinar · Oficial · Nuevo · Microsoft Security Community · YouTube – Microsoft Security Community · oct 2026. 122 webinars de una hora de los PM de Defender for Cloud (CSPM, contenedores, Storage, Servers, APIs, IA, SANS) con preguntas y respuestas; el formato que el Ninja oficial enlazaba como «webcast».
- [John Savill's Technical Training (canal de YouTube)](https://www.youtube.com/@NTFAQGuy/videos) · Video · Empleado de Microsoft · Nuevo · John Savill · YouTube · nov 2026. Canal con «Azure Weekly Update» semanal (p. ej., 4-sep-2026: Defender for Cloud en Azure Container Apps) y videos de seguridad como «Accelerating Defense with Microsoft Security Solutions» (oct-2026).
- [The Azure Security Podcast](https://azuresecuritypodcast.azurewebsites.net/) · Podcast · Empleado de Microsoft · Nuevo · Michael Howard, Sarah Young, Gladys Rodriguez, Mark Simos · Azure Security Podcast · 22 sep 2026. Podcast quincenal de seguridad en Azure; episodios útiles: #73 Defender for Cloud as Code, #75 novedades de MDC, #96 CNAPP y #131 MDASH (jul-2026); el #133 (22-sep-2026) comenta el GA de postura para Azure Container Apps.
- [Microsoft Security (YouTube, listas de reproducción)](https://www.youtube.com/@MicrosoftSecurity/playlists) · Video · Oficial · Microsoft Security · YouTube – Microsoft Security. Canal oficial (≈65 000 suscriptores) con listas «Defender for Cloud in the Field» (68), «Microsoft Ignite 2025» (84) y «Microsoft Sentinel is now in Defender».

### Laboratorios, GitHub y herramientas

- [Azure/Microsoft-Defender-for-Cloud (repositorio de la comunidad)](https://github.com/Azure/Microsoft-Defender-for-Cloud) · GitHub · Oficial · Nuevo · Equipo de Defender for Cloud y contribuidores · GitHub – Azure · oct 2026. Repositorio oficial con Labs, workbooks, Logic Apps de workflow automation, definiciones de Azure Policy, scripts de PowerShell, Power BI, simulaciones y Terraform (≈2 000 estrellas, 3 175 commits).

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Ignite 2026 (17-20 de noviembre, San Francisco y online)](https://ignite.microsoft.com/) · Evento · Oficial · Nuevo · Microsoft · 17 nov 2026. Evento anual en el Moscone Center y online (acceso digital gratuito a keynotes y sesiones; pase presencial 2 325 USD) con examen de certificación gratuito in situ.
- [Webinars | Microsoft Security Community (Upcoming Virtual Events)](https://securitycommunity.microsoft.com/VirtualEvents/) · Evento · Oficial · Microsoft Security Community. Calendario oficial de webinars por producto (incluido Defender for Cloud) y acceso al Security Advisors Program para previews y feedback.
- [Monthly News - August 2026 (Microsoft Defender Monthly news)](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/monthly-news-august-2026/4544388) · Newsletter · Empleado de Microsoft · Nuevo · Ed Fisher (EdFisher) · Microsoft Tech Community – Microsoft Defender XDR Blog · 5 ago 2026. Resumen mensual «What's new» de toda la familia Defender; desde la edición de abril de 2026 incluye las novedades de Defender for Cloud en el portal de Defender y abre cada número con el episodio nuevo del Virtual Ninja Show.

**Manos a la obra**

1. Marca con «Watch» los repositorios [Azure/Microsoft-Defender-for-Cloud](https://github.com/Azure/Microsoft-Defender-for-Cloud) y [Defender for Cloud Attack Simulation](https://github.com/microsoft/Defender-for-Cloud-Attack-Simulation), y suscríbete a los [eventos virtuales de la Microsoft Security Community](https://securitycommunity.microsoft.com/VirtualEvents/).
2. Mira tres videos de la lista [Defender for Cloud in the Field](https://www.youtube.com/playlist?list=PL3ZTgFEc7LysiX4PfHhdJPR7S8mGO14YS) o de Ignite 2025 —por ejemplo, [BRK262](https://www.youtube.com/watch?v=97BHmGoj0aE)— y anota tres controles que vas a revisar en tu entorno.
3. Arma una agenda en línea de cinco sesiones de seguridad en la nube de [Microsoft Ignite 2026](https://ignite.microsoft.com/) y, al cierre del evento el 20 de noviembre, contrasta los anuncios con What's new.

**¿Quieres profundizar?**

- [John Savill's Technical Training (canal de YouTube)](https://www.youtube.com/@NTFAQGuy/videos) · Video
- [The Azure Security Podcast](https://azuresecuritypodcast.azurewebsites.net/) · Podcast
- [Monthly News - August 2026 (Microsoft Defender Monthly news)](https://techcommunity.microsoft.com/blog/MicrosoftThreatProtectionBlog/monthly-news-august-2026/4544388) · Newsletter
- [Microsoft Ignite 2026 (17-20 de noviembre, San Francisco y online)](https://ignite.microsoft.com/) · Evento

<a id="c3"></a>

## C3 · Recursos en español y cómo mantenerse al día

*Transversal · ~2 h · Origen: Formato Ninja: comunidad (recursos en español y rutina de actualización)*

Microsoft Learn ofrece en español buena parte de este programa: What's new de Defender for Cloud con el mismo feed RSS —el 7 de noviembre de 2026 la versión en español llegaba hasta octubre, mientras la inglesa ya incluía el 4 de noviembre—, la página de recomendaciones y alertas, la ruta «Manage security posture» traducida y la ficha de la serie In the Field, con audio en inglés. La Customer Success Unit de Microsoft para México, Centroamérica y Sudamérica publicó en enero de 2026 una guía consolidada en español; hay además un webinar en español de una product manager del equipo, episodios de partners de la región y eventos como Global Azure Perú.

Mantenerse al día es un hábito: una revisión semanal de What's new y de los cambios de recomendaciones y alertas, una revisión mensual de las páginas que más usas contrastadas con su versión en inglés y una revisión después de cada evento. En credenciales, **AZ-500 se retiró el 31 de agosto de 2026** sin ruta de transición y el equipo de cursos de Microsoft anunció su reemplazo por **SC-500**, «Microsoft Certified: Cloud and AI Security Engineer Associate» (120 minutos, disponible en español y todavía sin evaluación de práctica); la Applied Skill de cumplimiento regulatorio con Defender for Cloud sigue vigente.

**Por qué importa**

Los equipos de MCSA aprenden más rápido en su idioma, pero las traducciones se rezagan semanas y los estados cambian después de cada evento. Combinar recursos en español con una rutina breve de verificación en las fuentes oficiales evita recomendar funciones retiradas o en vista previa como si fueran definitivas.

**Qué vas a lograr**

- Ubicar material confiable en español para los equipos de la región.
- Establecer una rutina semanal y mensual de actualización basada en fuentes oficiales.
- Planificar la ruta de credenciales vigente: Applied Skill, SC-500, SC-200 y SC-100.

> **Atención.** Credenciales: AZ-500 se retiró el 31 de agosto de 2026 y el equipo de cursos de Microsoft anunció su reemplazo por el curso y el examen SC-500; un moderador de Microsoft Q&A aclara que no hay ruta de transición y un sitio comunitario habla de 100 minutos de examen frente a los 120 de la página oficial. Usa siempre la página oficial ([credenciales retiradas](https://learn.microsoft.com/en-us/credentials/support/credential-retirement), [SC-500](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/), [anuncio de retiro](https://techcommunity.microsoft.com/blog/iltcommunicationblog/course-retirement-announcements/4504191)).

> **Atención.** Las páginas en español se actualizan después de la versión en inglés y algunas copias traducidas conservan contenido que ya se retiró en inglés, como el opt-in de Foundational CSPM. Ante cualquier diferencia, manda el inglés ([What's new en español](https://learn.microsoft.com/es-es/azure/defender-for-cloud/release-notes)).

> **Consejo Ninja.** El Ninja oficial redirige a la portada del blog en la comprobación del 7 de noviembre de 2026: mientras tanto, usa los knowledge checks de Learn y la Applied Skill de cumplimiento regulatorio como evidencia de aprendizaje, y vuelve a comprobar después de Ignite ([Applied Skill](https://learn.microsoft.com/en-us/credentials/applied-skills/secure-azure-services-and-workloads-with-microsoft-defender-for-cloud-regulatory-compliance-controls/)).

**¿Tienes poco tiempo?**

- [What's new in Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Documentación
- [Microsoft Defender for Cloud Blog (Tech Community) y su feed RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Category?category.id=microsoft-defender-for-cloud) · Blog oficial
- [Microsoft Defender for Cloud (Enero 2026) – Microsoft Security | MCSA CSU](https://es.linkedin.com/pulse/microsoft-defender-cloud-enero-2026-microsoft-mcsa-csu-security-ksn8f) · Newsletter

### Documentación, cursos y credenciales

- [What's new in Defender for Cloud features](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 nov 2026. Notas de versión mensuales (GA, preview, cambios próximos y retiros) con feed RSS aka.ms/mdc/rss; incluye el GA de la integración en el portal de Defender (5-may-2026) y la gestión de planes con DWU (20-oct-2026).
- [Novedades de las características de Defender for Cloud](https://learn.microsoft.com/es-es/azure/defender-for-cloud/release-notes) · Documentación · Oficial · Nuevo · ES · Microsoft Learn (español) · 28 oct 2026. Versión en español de las notas de versión, con el mismo feed RSS y las entradas de oct-2026 (políticas de postura y exenciones en el portal de Defender, nueva experiencia de servidores, DWU).
- [New and upcoming changes in recommendations, alerts, and incidents](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes-recommendations-alerts) · Documentación · Oficial · Nuevo · Microsoft Learn · 31 jul 2026. Registro de recomendaciones, alertas e incidentes nuevos, modificados y retirados (feed aka.ms/mdc/rss-recommendations-alerts), p. ej. el retiro de recomendaciones agrupadas (31-jul-2026).
- [Administración de la posición de seguridad mediante Microsoft Defender for Cloud (ruta en español)](https://learn.microsoft.com/es-es/training/paths/manage-security-posture-defender-cloud/) · Curso · Oficial · ES · Microsoft Learn (español). Ruta oficial traducida (6 módulos, 3 h 33 min) sobre conectar híbrido/multinube, CSPM, EASM, cumplimiento, CWPP y DVM, con comprobaciones de conocimiento.
- [Cambios nuevos y próximos en recomendaciones, alertas e incidentes](https://learn.microsoft.com/es-es/azure/defender-for-cloud/release-notes-recommendations-alerts) · Documentación · Oficial · Nuevo · ES · Microsoft Learn (español) · 31 jul 2026. Versión en español del registro de cambios de recomendaciones y alertas, con su feed RSS.
- [Retirement: Microsoft Defender for Cloud Deprecation in Microsoft Azure Operated by 21Vianet Announcement (Azure Updates)](https://azure.microsoft.com/en-gb/updates?id=498749) · Documentación · Oficial · Azure Updates (Microsoft Azure) · 20 ago 2025. Ejemplo de cómo Azure Updates publica retiros de Defender for Cloud (filtrables por producto y tipo «Retirements», con servidor MCP de Microsoft Release Communications para consultas con IA): anuncia el retiro de todas las funciones de Defender for Cloud en Azure operado por 21Vianet (China).

### Anuncios y blogs oficiales

- [Microsoft Defender for Cloud Blog (Tech Community) y su feed RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Category?category.id=microsoft-defender-for-cloud) · Blog oficial · Oficial · Nuevo · Equipo de producto (p. ej., Daniela Cardon en el anuncio DWU) · Microsoft Tech Community · 20 oct 2026. Feed del blog oficial; su entrada más reciente presenta la Defender Workload Unit: una unidad y un precio comunes, contenedores por nodo en lugar de vCore, APIs y bases de datos consolidadas en un plan, estimador y panel de costos en el portal de Defender.

### Webinars, videos y podcasts

- [Defender for Cloud sobre el terreno (Learn Shows en español)](https://learn.microsoft.com/es-es/shows/mdc-in-the-field/) · Video · Oficial · ES · Yuri Diogenes (presentador) · Microsoft Learn Shows (español) · 3 feb 2026. Ficha en español de la serie «Defender for Cloud in the Field» con títulos y descripciones traducidos (los videos están en inglés con subtítulos).
- [Cloud Security Posture Management and Workload Protection (Spanish) | Azure Security Center Webinar](https://www.youtube.com/watch?v=eYv2tFrY9qk) · Webinar · Empleado de Microsoft · Legado aún útil · ES · Fernanda Vela · YouTube – Microsoft Security Community · 22 jul 2021. Webinar íntegramente en español sobre CSPM y CWPP (entonces Azure Security Center/Azure Defender) e integración con Purview, presentado por una PM mexicana del equipo. *Nota:* Nombres antiguos (Azure Security Center/Azure Defender → Defender for Cloud)
- [Defender for Servers: postura, vulnerabilidades y protección de workloads (webinar Migesa, 19-nov-2026)](https://www.migesamicrosoft.com/evento/defender-for-servers-postura-vulnerabilidades-y-proteccion-de-workloadstemas-tecnologias-microsoft-defender-for-cloud-defender-for-servers-cwpp-cspm/) · Webinar · Comunidad · Nuevo · ES · Iván Israel Carmona Flores · Migesa Microsoft · 19 nov 2026. Webinar gratuito en español (jueves 19-nov-2026, 10:00-11:00, por Teams) para habilitar Defender for Servers: postura, recomendaciones priorizadas, vulnerabilidades, integración y quick wins para iniciar un piloto con impacto medible.
- [Microsoft Defender for Cloud CNAPP | T3 EP11 Cloud Wizards](https://www.youtube.com/watch?v=0cKnLjMoHkA) · Video · Comunidad · Nuevo · ES · Grupo Migesa · YouTube – Grupo Migesa · ago 2026. Episodio en español de un partner mexicano que muestra cómo activar Defender for Cloud, revisar recomendaciones y alertas y mejorar la postura multinube.

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Defender for Cloud (Enero 2026) – Microsoft Security | MCSA CSU](https://es.linkedin.com/pulse/microsoft-defender-cloud-enero-2026-microsoft-mcsa-csu-security-ksn8f) · Newsletter · Empleado de Microsoft · ES · Microsoft Customer Success Unit México, Centro y Sudamérica · LinkedIn – Microsoft Security | MCSA CSU · 26 ene 2026. Guía consolidada en español para MCSA: cobertura por carga, integración con Arc, consideraciones de cobro (prueba de 30 días, 500 MB/día, descuento MDE, prepago DCU de hasta 22 %) y operación.
- [Global Azure Perú 2026 (Lima, 18 de abril de 2026)](https://www.globalazureperu.com/) · Evento · Comunidad · ES · Comunidad (speakers incl. Jorge Castañeda, Microsoft MVP Security) · Global Azure Perú / Microsoft User Group Perú · 18 abr 2026. Evento comunitario gratuito en OpenPUCP (Lima) con más de 20 sesiones en 4 salas, incluido un track de Security; es el ejemplo LATAM de evento liderado por MVP (Jorge Castañeda, MVP de Security) donde encontrar sesiones de seguridad en Azure en español.
- [Defender for Cloud: CIEM en GA y threat protection para agentes de IA en preview](https://rfernandezdo.github.io/blog/2026/02/11/defender-for-cloud-ciem-en-ga-y-threat-protection-para-agentes-de-ia-en-preview/) · Blog · MVP · Legado aún útil · ES · Rafael Fernández Domínguez · Un Rinconcito donde contar lo que quiera (blog) · 11 feb 2026. Entrada en español que resume la GA de CIEM y la preview de protección de amenazas para agentes de Foundry dentro de Defender for AI Services (febrero de 2026). *Nota:* MVP de Azure (perfil oficial). Contenido asistido por IA según el propio blog; la parte de agentes quedó superada por la transición a Agent 365 (1-jul-2026) y algunos detalles de cobertura no coinciden con Learn

**Manos a la obra**

1. **Cada semana (unos 30 minutos):** revisa [What's new en inglés](https://learn.microsoft.com/en-us/azure/defender-for-cloud/release-notes) y [en español](https://learn.microsoft.com/es-es/azure/defender-for-cloud/release-notes), los cambios de recomendaciones y alertas y una pieza en español, como la [guía de la Customer Success Unit de MCSA](https://es.linkedin.com/pulse/microsoft-defender-cloud-enero-2026-microsoft-mcsa-csu-security-ksn8f).
2. **Cada mes y después de cada evento:** contrasta las páginas en español que más usas con su versión en inglés, actualiza tu matriz de estados (vista previa o GA) y de precios y registra lo que cambie después de Ignite.
3. **Plan de credenciales:** completa la ruta de la [Applied Skill de cumplimiento regulatorio](https://learn.microsoft.com/en-us/training/paths/secure-azure-services-workloads-defender-cloud/) y agenda el examen [SC-500](https://learn.microsoft.com/en-us/credentials/certifications/cloud-and-ai-security-engineer-associate/) en español.

**¿Quieres profundizar?**

- [Cloud Security Posture Management and Workload Protection (Spanish) | Azure Security Center Webinar](https://www.youtube.com/watch?v=eYv2tFrY9qk) · Webinar
- [Defender for Cloud sobre el terreno (Learn Shows en español)](https://learn.microsoft.com/es-es/shows/mdc-in-the-field/) · Video

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los precios son de lista, en USD, cambian con frecuencia y dependen de tu contrato, canal, región y moneda: confírmalos en la página oficial y con tu proveedor antes de presupuestar. El contenido regulatorio es una referencia y no constituye asesoría legal: las decisiones de cumplimiento corresponden a tus áreas de Legal, riesgo y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 7 de noviembre de 2026

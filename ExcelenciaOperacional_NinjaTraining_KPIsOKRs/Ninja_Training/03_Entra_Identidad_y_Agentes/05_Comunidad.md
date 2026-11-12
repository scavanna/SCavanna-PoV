# Comunidad · Referentes, canales y cómo mantenerse al día

*Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA · Edición 2026*

[← Nivel 4 · Identidad para agentes de IA](04_Nivel_4_Identidad_para_agentes_de_IA.md) · [Índice del programa](README.md) · [Evaluaciones y respuestas →](06_Evaluaciones_y_respuestas.md)

<a id="comunidad"></a>

Quién enseña Entra e identidad de agentes, dónde aprender en español y una rutina semanal, mensual y trimestral para convertir cada anuncio en una tarea.

*Transversal · 3 módulos · ~6 horas · 9 recursos*

**Módulos de este nivel:** [C1 Referentes](#c1) · [C2 Canales y recursos en español](#c2) · [C3 Mantenerse actualizado](#c3)

<a id="c1"></a>

## C1 · Referentes de identidad y agentes

*Transversal · ~2 h · Origen: Formato Ninja: comunidad*

Buena parte del conocimiento práctico de Entra lo publican MVPs y empleados de Microsoft: investigaciones sobre robo de tokens, guías de acceso condicional, herramientas de código abierto y, desde 2025, análisis profundos de Agent ID. La lista de referentes de este programa —con su rol verificado, país, foco y canales— aparece en este nivel y en la hoja «Referentes» del libro de Excel.

Dos obras comunitarias merecen un lugar fijo en tu lectura: el **Attack & Defense Playbook** de Entra, de Sami Lamppu y Thomas Naunheim, que en septiembre de 2026 sumó un capítulo sobre identidades de agente, y el catálogo de Jan Bakker para aprender agentes desde Entra (actualizado en abril de 2026). Contrasta siempre lo que leas con la documentación oficial y verifica el rol actual de cada autor: los cambios de empresa son frecuentes.

**Por qué importa**

Seguir a pocas personas bien elegidas ahorra horas de búsqueda y te expone a hallazgos antes de que lleguen a la documentación oficial, como el abuso de permisos heredables de los blueprints o el escalamiento por propietarios de catálogo. Métrica: un artículo comunitario leído y contrastado por semana.

**Qué vas a lograr**

- Identificar referentes verificados en identidad, ITDR y agentes.
- Usar el Attack & Defense Playbook y los catálogos comunitarios como complemento de Learn.
- Contrastar las fuentes comunitarias con la documentación oficial.

> **Atención.** Verifica siempre el rol actual de cada autor: Merill Fernando dejó Microsoft en 2026 para fundar Jozra, aunque algunas páginas aún lo presentan como gerente de producto de Microsoft ([merill.net](https://merill.net/about/)). La hoja «Referentes» del libro de Excel registra la evidencia de rol de cada persona.

**¿Tienes poco tiempo?**

- [Jan's resource catalog to learn all about agents (from an Entra ID perspective)](https://janbakker.tech/jans-resource-catalog-to-learn-all-about-agents/) · Blog
- [Agent Identities (Entra ID Attack & Defense Playbook)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) · GitHub

### Directorio de referentes verificados

- **Arturo Lucatero** (Empleado de Microsoft): Product Manager de Microsoft Entra Agent ID; firma en el blog de Entra como ArLucaID (correspondencia inferida) sobre identidades de agente seguras desde el diseño; invitado de Entra.Chat sobre secretos creados por agentes de código. [Blog](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/build-ai-agents-for-production-with-secure-identities-from-day-one/4524606) · [Otro](https://entra.news/archive) · [Evidencia de rol](https://entra.news/archive)
- **Mark Morowczynski** (Empleado de Microsoft): Investigador principal del equipo GHOST de Microsoft, con foco en identidad y KQL; coautor de The Definitive Guide to KQL. [Blog](https://markmorow.com/content/) · [Otro](https://runasradio.com/Shows/Show/969) · [Evidencia de rol](https://runasradio.com/Shows/Show/969)
- **Matt Zorich (reprise99)** (Empleado de Microsoft, Australia): Caza de amenazas e investigación forense en Entra ID/M365 con KQL (equipo GHOST); consultas útiles para auditar service principals y consentimientos. [Blog](https://learnsentinel.blog/author/mzorich/) · [GitHub](https://github.com/reprise99/Sentinel-Queries) · [Otro](https://infosec.exchange/@reprise_99) · [Evidencia de rol](https://www.pearson.com/en-us/subject-catalog/p/the-definitive-guide-to-kql/P200000011890?view=educator)
- **Rod Trent** (Empleado de Microsoft): Divulgación diaria sobre Security Copilot, seguridad de IA y agentes; boletín semanal 'THE PROMPT for Microsoft Security'. [Blog](https://rodtrent.substack.com/) · [GitHub](https://github.com/rod-trent/MustLearnKQL) · [Otro](https://microsoftdefender.substack.com/archive) · [Evidencia de rol](https://www.linkedin.com/posts/rodtrent_whats-new-in-microsoft-sentinel-february-activity-7427441069581152256-i1Vp)
- **Sarah Young** (Empleado de Microsoft): Co-anfitriona de The Azure Security Podcast (episodio 123 sobre identidad agéntica) y coautora del Exam Ref SC-200 (2.ª ed.). [Otro](https://azuresecuritypodcast.azurewebsites.net/) · [Evidencia de rol](https://azuresecuritypodcast.azurewebsites.net/)
- **Christopher Brumm** (MVP de Microsoft, Alemania): Identidad e ITDR (Entra, Global Secure Access) y monitoreo de seguridad de identidad. [Blog](https://chris-brumm.com/archive/) · [Otro](https://chris-brumm.com/speaking/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/MVP/profile/cad9c18c-40fe-475d-b9d9-dbec9bce58c3)
- **Derk van der Woude** (MVP de Microsoft, Países Bajos): Serie extensa sobre seguridad de identidades de agente (Agent ID, acceso condicional, ID Protection, herencia de permisos) y misconfiguraciones de Copilot Studio; revisor del capítulo de agentes del playbook Attack & Defense. [Otro](https://mvp.microsoft.com/en-us/PublicProfile/5004588) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5004588)
- **Fabian Bader** (MVP de Microsoft, Alemania): Seguridad de identidad y detección (SIEM & XDR), PowerShell y contribuciones a Maester; blog cloudbrothers.info. [Blog](https://cloudbrothers.info/en/aboutme/) · [GitHub](https://github.com/f-bader/AzSentinelQueries) · [Otro](https://sessionize.com/FabianBader/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5004810)
- **Jan Bakker** (MVP de Microsoft, Países Bajos): Arquitecto IAM; guías prácticas de Entra (passkeys, acceso condicional, políticas de aplicaciones, restringir creación de blueprints) y catálogo curado de recursos para aprender agentes desde Entra. [Blog](https://janbakker.tech/categories/entra/) · [Otro](https://janbakker.tech/posts/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5004164)
- **Jorge Castañeda** (MVP de Microsoft, Perú): MVP de Security en español (SIEM & XDR); referente hispanohablante en LATAM para laboratorios con Defender XDR, Sentinel y Purview; la identidad no es su foco principal. [Blog](https://blog.d3fend.me/) · [Otro](https://blog.d3fend.me/about/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5000594)
- **Michael Morten Sonne** (MVP de Microsoft, Dinamarca): Defender XDR e identidad (Entra, MDI) y herramientas PowerShell; miembro de varios programas de comunidad incluido Security Copilot. [Blog](https://blog.sonnes.cloud/topics/security/) · [Otro](https://sonnes.cloud/about/) · [Evidencia de rol](https://sonnes.cloud/about/)
- **Nathan McNulty** (MVP de Microsoft, EE. UU.): MVP de seguridad (Identity & Access y SIEM/XDR): acceso condicional, passkeys, auditoría avanzada y PIM; invitado frecuente de Entra.Chat; perfil MVP destaca su 'Conditional Access Masterclass'. [Blog](https://nathanmcnulty.com/blog/) · [GitHub](https://github.com/nathanmcnulty/nathanmcnulty/blob/master/README.md) · [Otro](https://nathanmcnulty.com/tags/entra/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/MVP/profile/58f4fa40-eb0e-4336-8d27-25e506e4ee2c)
- **Robbe Van den Daele** (MVP de Microsoft, Bélgica): SOC engineering con Defender XDR y Sentinel (HybridBrothers); coautor del capítulo de identidades de agente del playbook Attack & Defense y autor de guías para administrar agentes de Copilot Studio. [Blog](https://hugo.hybridbrothers.com/) · [GitHub](https://github.com/HybridBrothers/Hunting-Queries-Detection-Rules/tree/main) · [Otro](https://sessionize.com/robbe-van-den-daele/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/f6095ac4-5535-4a96-823b-f332add1cb41)
- **Sami Lamppu** (MVP de Microsoft, Finlandia): MVP de seguridad (SIEM/XDR y Security Copilot); coautor del capítulo de identidades de agente del playbook Entra ID Attack & Defense y del Unified XDR & SIEM Handbook. [Blog](https://samilamppu.com/) · [Otro](https://samilamppu.com/category/microsoft-sentinel/) · [Evidencia de rol](https://mvp.microsoft.com/en-US/mvp/profile/06ab3a7e-e0d7-eb11-bacb-000d3a154f10)
- **Thomas Naunheim** (MVP de Microsoft, Alemania): Referente en workload identities e ITDR de Entra: serie de blog sobre ciclo de vida, detección y respuesta de service principals; coautor del playbook Entra ID Attack & Defense, incluido el capítulo de identidades de agente (sep-2026); creador de EntraOps. [Blog](https://www.cloud-architekt.net/blog/) · [GitHub](https://github.com/cloud-architekt) · [Otro](https://www.cloud-architekt.net/publications/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5003945)
- **Merill Fernando** (Comunidad, Australia): Ex Principal Product Manager de Entra (dejó Microsoft en 2026 para fundar Jozra); edita Entra.News y el podcast Entra.Chat; creador de Maester, Graph X-Ray, cmd.ms y coautor del Zero Trust Assessment. [Blog](https://merill.net/) · [Otro](https://entra.news/) · [Evidencia de rol](https://merill.net/about/)

### Comunidad: blogs, libros, newsletters y eventos

- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog · MVP · Nuevo · Thomas Naunheim · cloud-architekt.net · 29 sep 2026. Blog de investigación sobre identidad privilegiada (EntraOps, RMAU, Tenant Governance, identidades de carga de trabajo y robo de tokens) del co-creador del Azure AD Attack & Defense Playbook.
- [Jan's resource catalog to learn all about agents (from an Entra ID perspective)](https://janbakker.tech/jans-resource-catalog-to-learn-all-about-agents/) · Blog · MVP · Jan Bakker · JanBakker.tech · 17 abr 2026. Catálogo curado de recursos oficiales y comunitarios para aprender identidad de agentes desde Entra: artículos, series de Derk van der Woude, videos, podcast y herramientas.
- [Nathan McNulty - Blog (Sign-in Frequency, device code flow, RMAU)](https://nathanmcnulty.com/blog/) · Blog · MVP · Nuevo · Nathan McNulty · 13 oct 2026. Blog con artículos sobre frecuencia de inicio de sesión, auditoría previa al bloqueo de device code flow, unidades administrativas de administración restringida y el cambio a passkeys por defecto.
- [Entra ID - Agent Identity Security (MVP activity)](https://mvp.microsoft.com/en-US/activities/363464) · Blog · MVP · Derk van der Woude · Microsoft MVP Program · 20 ene 2026. Ficha de actividad MVP de la serie de blog de Derk van der Woude sobre productos de seguridad para identidades de agente (ID Protection, acceso condicional, Secure Access y gobernanza).
- [Agent Identity demystified (MVP activity)](https://mvp.microsoft.com/en-US/activities/362805) · Blog · MVP · Derk van der Woude · Microsoft MVP Program · 15 ene 2026. Ficha de la serie 'Agent Identity demystified' que explica la seguridad de identidades de agente en Entra paso a paso.

**Manos a la obra**

1. Elige tres referentes de la hoja «Referentes» según tu rol, suscríbete a sus blogs y registra cada semana una idea aplicable a tu tenant.
2. Lee el capítulo [Agent Identities del Attack & Defense Playbook](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AgentIdentities.md) y anota dos detecciones que quieras construir.
3. Recorre el [catálogo de Jan Bakker](https://janbakker.tech/jans-resource-catalog-to-learn-all-about-agents/) y arma tu lista de lectura del track de agentes.

**¿Quieres profundizar?**

- [Thomas Naunheim - Blog posts](https://www.cloud-architekt.net/blog/) · Blog
- [Nathan McNulty - Blog (Sign-in Frequency, device code flow, RMAU)](https://nathanmcnulty.com/blog/) · Blog
- [Entra ID - Agent Identity Security (MVP activity)](https://mvp.microsoft.com/en-US/activities/363464) · Blog

<a id="c2"></a>

## C2 · Canales, podcasts, libros y recursos en español

*Transversal · ~2 h · Origen: Formato Ninja: comunidad*

Para el día a día: **Entra.News**, boletín semanal (la edición 173 salió el 1 de noviembre de 2026) con el podcast **Entra.Chat**; **The Azure Security Podcast**, cuyo episodio 123 (21 de enero de 2026) trata la identidad agéntica; la lista de Microsoft Mechanics sobre Entra; y la serie oficial de SC-300 en YouTube. En libros, la investigación no encontró títulos sobre Entra actualizados a 2026: con un producto que cambia cada mes, prioriza documentación, blogs y podcasts.

En español hay versiones de Learn de varias guías clave —SC-300, valores predeterminados de seguridad, SAML, Zero Trust para identidad, MCRA, Entra PowerShell, Agent ID, servidores MCP y seguridad de Copilot Studio—, además de la página de identidad de agentes de Foundry en español de México. Son útiles para formar equipos, pero muchas son traducciones automáticas y algunas están desfasadas: ante cualquier diferencia, prevalece la versión en inglés.

**Por qué importa**

Que todo el equipo comparta las mismas fuentes reduce malentendidos y acelera la adopción. Los recursos en español facilitan formar a mesas de ayuda, makers y responsables de negocio, siempre que se verifiquen contra la versión en inglés. Métrica: glosario y biblioteca de fuentes comunes publicados para el equipo.

**Qué vas a lograr**

- Suscribirte a los canales semanales y mensuales de identidad.
- Identificar los recursos oficiales disponibles en español y sus limitaciones.
- Armar una biblioteca de referencia para tu equipo.

> **Novedad.** Entra.News sigue semanal (edición 173 del 1 de noviembre de 2026) e incluye episodios de Entra.Chat como «Your AI Coding Agent Is Creating Secrets», con el PM de Agent ID, y «Stop the Bleeding», sobre limpieza de apps, secretos y consentimientos ([archivo de Entra.News](https://entra.news/archive)).

**¿Tienes poco tiempo?**

- [Entra.News - Your weekly dose of Microsoft Entra](https://entra.news/) · Newsletter
- [The Azure Security Podcast - Episode 123 - Agentic Identity](https://azuresecuritypodcast.azurewebsites.net/episodes/Episode0123.html) · Podcast

### Webinars, videos y podcasts

- [The Azure Security Podcast - Episode 123 - Agentic Identity](https://azuresecuritypodcast.azurewebsites.net/episodes/Episode0123.html) · Podcast · Empleado de Microsoft · Michael Howard, Sarah Young, Gladys Rodriguez, Mark Simos · The Azure Security Podcast · 21 ene 2026. Episodio dedicado a la identidad agéntica y sus problemas de mínimo privilegio, conducido por expertos de seguridad de Microsoft.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra.News - Your weekly dose of Microsoft Entra](https://entra.news/) · Newsletter · Comunidad · Nuevo · Merill Fernando, Joshua Fernando · Entra.News (Substack) · 1 nov 2026. Boletín semanal gratuito que resume las novedades de Entra de Microsoft y la comunidad, con el podcast Entra.Chat de entrevistas a gerentes de producto y profesionales.

**Manos a la obra**

1. Suscríbete a [Entra.News](https://entra.news/) y escucha el [episodio 123 de The Azure Security Podcast](https://azuresecuritypodcast.azurewebsites.net/episodes/Episode0123.html) sobre identidad agéntica.
2. Arma una biblioteca en español para tu equipo con las versiones de Learn de la [guía del SC-300](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-300), los [valores predeterminados de seguridad](https://learn.microsoft.com/es-es/entra/fundamentals/security-defaults), [Agent ID](https://learn.microsoft.com/es-es/entra/agent-id/whats-new-agent-id), [MCP](https://learn.microsoft.com/es-es/entra/agent-id/secure-mcp-server-with-entra-id) y [Copilot Studio](https://learn.microsoft.com/es-es/microsoft-copilot-studio/security-and-governance), y marca cuáles son traducción automática.

<a id="c3"></a>

## C3 · Cómo mantenerse actualizado

*Transversal · ~2 h · Origen: Formato Ninja: comunidad*

Ser Ninja es un hábito. Una rutina sostenible: **cada semana**, Entra.News y THE PROMPT de Rod Trent; **cada mes**, las novedades de Entra, de Agent ID y de seguridad para IA; **cada trimestre**, la descripción de servicio de Agent 365 (licencias) y el Attack & Defense Playbook. El archivo comunitario del Centro de mensajes ayuda a seguir avisos como el retiro de SMS y voz o la migración de perfiles de passkey.

Noviembre y diciembre de 2026 son meses de cambio: Microsoft Ignite se realiza del 17 al 20 de noviembre y el equipo de Entra anunció webinars de profundización del 15 al 17 de diciembre sobre acceso adaptativo, gobernanza, PIM, Tenant Governance, Backup and Recovery y seguridad de identidades de agente. Revisa las tablas de licencias y de preparación para agentes de esta guía después de esas fechas.

**Por qué importa**

Las fechas de retiro, los cambios de licencia y los pasos de vista previa a disponibilidad general afectan decisiones de arquitectura y de compras. Una rutina de 30 minutos semanales evita sorpresas como una sincronización detenida o políticas que se activan solas. Métrica: revisión trimestral de las tablas de referencia con fecha y responsable.

**Qué vas a lograr**

- Definir una rutina semanal, mensual y trimestral de actualización.
- Seguir avisos del Centro de mensajes y páginas de novedades con fuente RSS.
- Actualizar las tablas de referencia del programa después de cada anuncio mayor.

> **Novedad.** Agenda: Microsoft Ignite, del 17 al 20 de noviembre de 2026, y los webinars de profundización de Entra del 15 al 17 de diciembre sobre acceso adaptativo sin proliferación de políticas; gobernanza, PIM, Tenant Governance y Backup and Recovery; y seguridad de identidades de agente ([anuncio](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-deep-dives-join-our-december-15%E2%80%9317-webinar-series/4448760), [webinar del 16 de diciembre](https://techcommunity.microsoft.com/event/microsoft-security-events/strengthen-governance-privileged-access-and-resilience-across-every-identity-and/4569719)).

**¿Tienes poco tiempo?**

- [Entra.News archive](https://entra.news/archive) · Newsletter
- [Microsoft Entra releases and announcements (What's new)](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new) · Documentación
- [What's new in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) · Documentación

### Laboratorios, GitHub y herramientas

- [Microsoft Ninja Training Hub (Unofficial Tracker)](https://github.com/peterschmidtdk/Microsoft-Ninja-Training/tree/main/) · GitHub · Comunidad · Peter Schmidt · GitHub (peterschmidtdk) · 27 feb 2026. Tracker comunitario de todos los Ninja Trainings públicos de seguridad de Microsoft, útil para verificar que no existe un Ninja oficial de Entra.

### Comunidad: blogs, libros, newsletters y eventos

- [Entra.News archive](https://entra.news/archive) · Newsletter · Comunidad · Nuevo · Merill Fernando, Joshua Fernando · Entra.News (Substack) · nov 2026. Archivo de ediciones y episodios, útil para revisar el historial de anuncios de Agent ID, apps y passkeys semana a semana.

**Manos a la obra**

1. Define tu rutina: cada semana, Entra.News y [THE PROMPT](https://microsoftdefender.substack.com/archive); cada mes, las novedades de [Entra](https://learn.microsoft.com/en-us/entra/fundamentals/whats-new), [Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id) y [seguridad para IA](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new); cada trimestre, la descripción de servicio de Agent 365 y el Attack & Defense Playbook.
2. Suscríbete al RSS de novedades de Entra y al de versiones de Entra Connect (aka.ms/aadconnectrss), y agenda la revisión de las tablas de licencias y de preparación para agentes después de Ignite.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

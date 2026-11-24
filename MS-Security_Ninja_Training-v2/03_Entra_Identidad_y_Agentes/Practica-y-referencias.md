# Práctica y referencias

[Índice del programa](README.md)


<a id="comunidad"></a>

## Comunidad


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

<a id="evaluaciones-y-respuestas"></a>

## Evaluaciones y respuestas


<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Qué plan de Microsoft Entra incluye Microsoft 365 E5?**

- a) Entra Suite
- b) Entra ID P2  ✅
- c) Entra ID Governance completo
- d) Internet Access

*Respuesta: b).* E5 incluye Entra ID P2. Entra Suite —con ID Governance, Private Access e Internet Access— viene en Microsoft 365 E7 o se compra aparte. [Fuente](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué licencia necesita el perfil de tráfico de Microsoft de Global Secure Access?**

- a) Entra Suite
- b) Internet Access
- c) Workload ID Premium
- d) Entra ID P1 o P2  ✅

*Respuesta: d).* El perfil de tráfico de Microsoft solo requiere P1 o P2, así que está disponible con E3 y E5; Private Access e Internet Access requieren su propia licencia, Entra Suite o E7. [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Qué se necesita para aplicar acceso condicional a los agentes de IA?**

- a) Solo Entra ID P1
- b) Workload ID Premium
- c) Microsoft 365 E7, o Agent 365 más al menos P1 o E3  ✅
- d) Nada adicional: Agent ID es gratuito para todos

*Respuesta: c).* Agent ID está disponible para todos los clientes de Entra, pero el acceso condicional para agentes requiere E7, o Agent 365 más al menos Entra ID P1 o Microsoft 365 E3. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. ¿A qué operaciones afecta la fase 2 del MFA obligatorio de Azure, vigente desde el 1 de octubre de 2025?**

- a) Crear, actualizar y borrar recursos de Azure por CLI, PowerShell, IaC, REST y SDK  ✅
- b) Solo el inicio de sesión en el portal de Azure
- c) Las identidades administradas y los service principals
- d) Solo las lecturas de la API

*Respuesta: a).* La fase 1 cubrió los portales de administración; la fase 2 alcanza la gestión de Azure desde herramientas y código. Las workload identities no se ven afectadas. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**5. ¿Qué método recomienda Microsoft para proteger las cuentas de emergencia?**

- a) SMS
- b) Llamada de voz
- c) Passkey FIDO2  ✅
- d) Ninguno: deben quedar sin MFA

*Respuesta: c).* Las cuentas de emergencia también deben cumplir el MFA obligatorio; Microsoft recomienda passkey FIDO2 (o CBA) y monitorear cada uso. [Fuente](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**6. Asocias una acción protegida a una política de acceso condicional que está en modo solo informe. ¿Qué ocurre?**

- a) Protege igual que una política activa
- b) Bloquea a todos los administradores
- c) Solo resta puntos en Identity Secure Score
- d) No protege la acción: la política debe estar activada  ✅

*Respuesta: d).* Para que una acción protegida funcione, la política asociada a su contexto de autenticación debe estar activada; en solo informe no exige nada. [Fuente](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/protected-actions-add) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**7. ¿Cuándo deja Microsoft de entregar SMS y voz a los Global Administrators activos y a los usuarios externos?**

- a) 1 de febrero de 2027
- b) 1 de julio de 2027  ✅
- c) 1 de septiembre de 2026
- d) 7 de abril de 2027

*Respuesta: b).* Según el documento vigente de Learn, el retiro general es el 1 de febrero de 2027 y el de Global Administrators activos y usuarios externos, el 1 de julio de 2027. El blog de julio de 2026 daba una sola fecha. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. Desde el 30 de septiembre de 2025, ¿dónde se gestionan los métodos de autenticación?**

- a) En la política de métodos de autenticación  ✅
- b) En la configuración de MFA por usuario
- c) En la política heredada de SSPR
- d) En los valores predeterminados de seguridad

*Respuesta: a).* Desde esa fecha ya no se pueden gestionar métodos en las políticas heredadas de MFA y SSPR; solo las preguntas de seguridad siguen en la configuración heredada de SSPR. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**9. ¿Qué método NO satisface la fortaleza de autenticación «MFA resistente al phishing»?**

- a) Llave de seguridad FIDO2
- b) CBA multifactor
- c) Temporary Access Pass  ✅
- d) Windows Hello for Business

*Respuesta: c).* TAP solo satisface la fortaleza MFA; la resistente al phishing admite Windows Hello o la credencial de plataforma, FIDO2 y CBA multifactor. [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**10. Una política de acceso condicional administrada por Microsoft se crea en solo informe. ¿Cuándo se activa?**

- a) Al menos 30 días después de crearse, con aviso dos semanas antes  ✅
- b) De inmediato
- c) A los 7 días
- d) Nunca, salvo que la actives tú

*Respuesta: a).* Microsoft las activa automáticamente tras al menos 30 días en solo informe y avisa dos semanas antes; no se pueden renombrar ni borrar. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**11. ¿Qué NO evalúa la herramienta What If de acceso condicional?**

- a) Inicios de sesión de usuarios
- b) Service principals
- c) Identidades de agente (vista previa)
- d) Dependencias de servicio, como la de Teams con Exchange Online  ✅

*Respuesta: d).* What If usa la API What If Evaluation de Microsoft Graph y simula usuarios, service principals e identidades de agente, pero no evalúa las dependencias de servicio. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) · Repasa [I4](01_Nivel_1_Inicial.md#i4)

**12. ¿Qué necesita Entra Connect Sync para seguir sincronizando después del 7 de abril de 2027?**

- a) La versión 2.5.79.0
- b) Migrar a AD FS
- c) La versión 2.6.84.0 o superior con autenticación basada en aplicación  ✅
- d) Activar Connect Health

*Respuesta: c).* El aviso vigente exige 2.6.84.0 o superior con autenticación basada en aplicación; el aviso anterior pedía 2.5.79.0 antes del 30 de septiembre de 2026. [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**13. ¿Por qué conviene activar la sincronización de hash de contraseñas aunque uses PTA o federación?**

- a) Porque reemplaza a Cloud Sync
- b) Porque la detección de credenciales filtradas de ID Protection la necesita  ✅
- c) Porque elimina la necesidad de MFA
- d) Porque es obligatoria desde 2026

*Respuesta: b).* PHS es la opción más simple y resiliente, y algunas capacidades, como la detección de credenciales filtradas, la requieren aunque uses otro método. [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/choose-ad-authn) · Repasa [I5](01_Nivel_1_Inicial.md#i5)

**14. ¿Cuánto dura por defecto un token de acceso de Microsoft Entra?**

- a) 5 minutos
- b) 24 horas
- c) 90 días
- d) 1 hora  ✅

*Respuesta: d).* Un token de acceso dura una hora por defecto; CAE acorta la reacción ante eventos críticos en los servicios compatibles. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**15. Lanzas el laboratorio de la credencial Applied Skills de identidades y acceso y no lo terminas. ¿Qué ocurre?**

- a) Debes esperar 72 horas para relanzarlo  ✅
- b) Puedes relanzarlo de inmediato
- c) Pierdes tu certificación SC-300
- d) Debes pagar un nuevo intento

*Respuesta: a).* La evaluación es un laboratorio interactivo de 2 horas y, una vez lanzado, hay que esperar 72 horas para volver a lanzarlo. [Fuente](https://learn.microsoft.com/en-us/credentials/applied-skills/get-started-with-identities-and-access-using-microsoft-entra/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Proteger, gobernar y observar

**1. La protección de tokens para apps nativas está en disponibilidad general en:**

- a) Solo Windows
- b) Windows, iOS/iPadOS y macOS  ✅
- c) Solo navegadores
- d) Android y Linux

*Respuesta: b).* Está en GA para apps nativas en Windows, iOS/iPadOS y macOS; las apps de navegador hacia Azure Resource Manager siguen en vista previa. La propia página aún muestra «Apple (Preview)» en una sección. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué valores puede tomar un contexto de autenticación?**

- a) C1 a C99  ✅
- b) A1 a A9
- c) R1 a R25
- d) Cualquier texto libre

*Respuesta: a).* Los contextos de autenticación usan identificadores de C1 a C99, que las apps, PIM o las acciones protegidas solicitan para exigir una política más estricta. [Fuente](https://learn.microsoft.com/en-us/entra/identity-platform/developer-guide-conditional-access-authentication-context) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. Desde septiembre de 2024, una política de flujos de autenticación dirigida a «All resources» también aplica a:**

- a) Las identidades administradas
- b) Los agentes de Copilot Studio
- c) El Device Registration Service  ✅
- d) Las cuentas de emergencia

*Respuesta: c).* Desde septiembre de 2024 esas políticas también aplican al Device Registration Service: revisa su impacto en el registro de dispositivos. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Cuándo se retiraron las políticas de riesgo heredadas de ID Protection?**

- a) 30 de septiembre de 2025
- b) 1 de marzo de 2027
- c) 1 de octubre de 2026  ✅
- d) No se retiraron

*Respuesta: c).* Se retiraron el 1 de octubre de 2026; la vía soportada son las políticas de acceso condicional basadas en riesgo. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**5. Con «Require risk remediation», ¿qué ocurre con un usuario sin contraseña que tiene riesgo de usuario alto?**

- a) Debe cambiar la contraseña
- b) Queda bloqueado hasta que un administrador lo libere
- c) No ocurre nada
- d) Se revocan sus sesiones y debe volver a iniciar sesión  ✅

*Respuesta: d).* El control adapta la remediación: cambio seguro de contraseña para usuarios con contraseña, revocación de sesiones para usuarios sin contraseña y deshabilitación del dispositivo si lo agregó un atacante. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Cuánto pueden tardar en aparecer las detecciones de riesgo fuera de línea?**

- a) 5 minutos
- b) Hasta 48 horas  ✅
- c) 30 días
- d) 6 meses

*Respuesta: b).* Las detecciones en tiempo real aparecen en 5 a 10 minutos y las fuera de línea, hasta en 48 horas; seis meses es lo que tarda en caducar el riesgo bajo. [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/concept-risk-detection-types) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué rol mínimo necesitas para configurar las opciones de un rol de Entra en PIM?**

- a) Security Administrator
- b) Global Reader
- c) Privileged Role Administrator  ✅
- d) User Administrator

*Respuesta: c).* Configurar la duración de activación, la aprobación o el contexto de autenticación de un rol requiere al menos Privileged Role Administrator. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**8. Si vence la licencia que habilita PIM, ¿qué pasa con las asignaciones?**

- a) No pasa nada
- b) Se eliminan las elegibles y las activas temporales pasan a permanentes  ✅
- c) Se eliminan todas
- d) Todas pasan a elegibles

*Respuesta: b).* Es un riesgo poco conocido: sin licencia, las asignaciones elegibles se eliminan y las activas temporales quedan como permanentes. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. ¿Qué función de gobernanza NO está incluida en Microsoft 365 E5?**

- a) PIM for Groups
- b) Revisiones de acceso de roles de Entra
- c) Controles de acceso condicional en PIM
- d) Lifecycle Workflows  ✅

*Respuesta: d).* Lifecycle Workflows requiere ID Governance o Entra Suite; PIM, PIM for Groups y las revisiones básicas vienen con P2. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**10. ¿Qué licencia requiere sincronizar grupos entre tenants?**

- a) Entra ID P1
- b) Entra ID P2
- c) ID Governance o Entra Suite  ✅
- d) Workload ID Premium

*Respuesta: c).* La sincronización de usuarios entre tenants requiere P1; la de grupos, en GA desde junio de 2026, requiere ID Governance o Entra Suite. [Fuente](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**11. Una empresa con dirección de facturación en México, ¿puede usar App governance?**

- a) Sí, con Microsoft 365 E5
- b) No: México está entre los países excluidos  ✅
- c) Sí, con Purview Suite
- d) Solo en vista previa

*Respuesta: b).* App governance no está disponible si la dirección de facturación está en México, Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán. [Fuente](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**12. Desde junio de 2026, el bloqueo de propiedades de instancia:**

- a) Está retirado
- b) Solo aplica a apps SAML
- c) Requiere Workload ID Premium
- d) Viene habilitado por defecto en apps nuevas, single-tenant y multitenant  ✅

*Respuesta: d).* El bloqueo viene habilitado por defecto en las apps nuevas desde junio de 2026 y ya no se limita a las apps multitenant. [Fuente](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) · Repasa [M5](02_Nivel_2_Intermedio.md#m5)

**13. ¿Qué se necesita para recibir las alertas de monitoreo de salud de Entra?**

- a) P1 o P2 que no sea de prueba y al menos 100 usuarios activos al mes  ✅
- b) Solo la edición gratuita
- c) Microsoft Sentinel
- d) ID Governance

*Respuesta: a).* Las alertas de salud, en vista previa, exigen P1 o P2 que no sean de prueba y al menos 100 usuarios activos al mes; un tenant nuevo tarda unos 30 días en generarlas. [Fuente](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts) · Repasa [M6](02_Nivel_2_Intermedio.md#m6)

**14. ¿Cuál es un requisito de Platform SSO para macOS?**

- a) Windows Hello for Business
- b) AD FS
- c) Workload ID Premium
- d) Company Portal 5.2404.0 o posterior  ✅

*Respuesta: d).* Platform SSO requiere macOS 13 o superior (se recomienda 14) y Company Portal 5.2404.0 o posterior, y se configura con el catálogo de Intune. [Fuente](https://learn.microsoft.com/en-us/entra/identity/devices/macos-psso) · Repasa [M7](02_Nivel_2_Intermedio.md#m7)

**15. ¿En qué orden evalúa el cliente de Global Secure Access los perfiles de reenvío?**

- a) Microsoft, Private Access, Internet Access  ✅
- b) Internet Access, Private Access, Microsoft
- c) Private Access, Microsoft, Internet Access
- d) Todos en paralelo

*Respuesta: a).* El orden es perfil de tráfico de Microsoft, luego Private Access y luego Internet Access; el perfil de sistema de tráfico de Entra se activa con cualquiera de ellos. [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding) · Repasa [M8](02_Nivel_2_Intermedio.md#m8)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · Cargas de trabajo, amenazas y arquitectura

**1. ¿Cómo se licencia Workload ID Premium?**

- a) Incluido en Microsoft 365 E5
- b) Incluido en Entra ID P2
- c) SKU independiente de 3 USD por identidad al mes  ✅
- d) Gratis para las identidades administradas

*Respuesta: c).* Es un SKU independiente, no incluido en E5, E7 ni en otros planes; las identidades administradas ni siquiera entran en el alcance de su acceso condicional. [Fuente](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿A qué se aplica el acceso condicional para workload identities?**

- a) A identidades administradas
- b) A service principals de un solo tenant asignados directamente a la política  ✅
- c) A apps SaaS multitenant
- d) A grupos que contienen service principals

*Respuesta: b).* Solo cubre service principals de un solo tenant registrados en tu tenant; si la política apunta a un grupo que los contiene, no se aplica. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/workload-identity) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. ¿Qué vida máxima para certificados de aplicación recomienda el tutorial de políticas de administración de apps?**

- a) 180 días  ✅
- b) 30 días
- c) 90 días
- d) 2 años

*Respuesta: a).* La recomendación es deshabilitar secretos y limitar los certificados a 180 días, con rotación automática en Key Vault. [Fuente](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/tutorial-enforce-secret-standards) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿En qué condiciones funciona CAE para workload identities?**

- a) Contra cualquier recurso y sin licencia
- b) Solo con identidades administradas
- c) Solo en apps multitenant
- d) Contra Microsoft Graph, si la app declara la capacidad cp1 y con Workload ID Premium  ✅

*Respuesta: d).* CAE para workload identities revoca casi en tiempo real tokens de hasta 24 horas, pero solo contra Microsoft Graph, con apps que declaran cp1 y con Workload ID Premium. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-workload) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Cuál es la latencia máxima típica de CAE ante eventos críticos, como deshabilitar una cuenta?**

- a) Instantánea
- b) 1 hora
- c) 24 horas
- d) Hasta 15 minutos  ✅

*Respuesta: d).* Los eventos críticos se aplican en hasta 15 minutos; los cambios de ubicación IP, al instante en los servicios compatibles. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. La interrupción automática de ataques de Defender deshabilita usuarios en Entra ID y AD cuando la confianza es de al menos:**

- a) 50 %
- b) 75 %
- c) 99 %  ✅
- d) 100 %, con aprobación manual

*Respuesta: c).* Actúa con una confianza de al menos 99 % y ya soporta Okta y AWS en vista previa. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué tabla de la búsqueda avanzada reemplazó a AADSignInEventsBeta el 19 de octubre de 2026?**

- a) IdentityLogonEvents
- b) EntraIdSignInEvents  ✅
- c) SigninLogs
- d) AgentsInfo

*Respuesta: b).* EntraIdSignInEvents reemplazó a AADSignInEventsBeta y requiere Entra ID P2. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Cuál es el estado de EntraExporter en noviembre de 2026?**

- a) En disponibilidad general
- b) En vista previa
- c) Integrado en Entra PowerShell
- d) Archivado desde el 22 de octubre de 2026  ✅

*Respuesta: d).* El repositorio quedó archivado; para instantáneas y deriva se usan Tenant Governance o Microsoft365DSC. [Fuente](https://github.com/microsoft/EntraExporter/blob/main/README.md) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**9. ¿Qué versión de Maester conviene fijar en un pipeline en noviembre de 2026?**

- a) La 2.3.0, porque la 3.0 está en vista previa  ✅
- b) La 3.0, porque es la única compatible
- c) La 1.0
- d) Siempre la última disponible

*Respuesta: a).* Maester 3.0 está en vista previa y rompe compatibilidad; la recomendación es fijar la 2.3.0 hasta que la 3.0 sea estable. [Fuente](https://maester.dev/blog/maester-3-0) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué incluye Tenant Governance con licencias P1 o P2?**

- a) Monitoreo ilimitado
- b) Hasta 30 monitores y 800 recursos por día  ✅
- c) Solo instantáneas manuales
- d) Nada: requiere ID Governance

*Respuesta: b).* Con P1 o P2 hay hasta 30 monitores y 800 recursos por día, y 20.000 recursos al mes en instantáneas; ID Governance amplía los límites. [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/tenant-governance/licensing) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. En el modelo de acceso empresarial, ¿en qué se convierte el antiguo Tier 0?**

- a) En el plano de datos y cargas de trabajo
- b) En el acceso de usuarios
- c) En el plano de control  ✅
- d) En el plano de aplicaciones

*Respuesta: c).* El Tier 0 pasa a ser el plano de control; el Tier 1 se divide en plano de administración y de datos y cargas, y el Tier 2 en acceso de usuarios y de aplicaciones. [Fuente](https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**12. ¿Qué NO puede hacer Entra Backup and Recovery?**

- a) Restaurar una política de acceso condicional modificada
- b) Generar un informe de diferencias
- c) Recuperar objetos por tipo o por ID
- d) Recuperar objetos eliminados definitivamente  ✅

*Respuesta: d).* No recupera objetos eliminados definitivamente ni los que tienen su origen de autoridad en AD local; por eso conviene proteger el borrado definitivo con acciones protegidas. [Fuente](https://learn.microsoft.com/en-us/entra/backup/overview) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**13. Ante una cuenta híbrida comprometida, ¿qué combinación recomienda Microsoft?**

- a) Deshabilitarla, restablecer la contraseña dos veces en AD, revocar los tokens de actualización y deshabilitar sus dispositivos  ✅
- b) Solo borrar la cuenta
- c) Esperar a que expire el token de acceso
- d) Cambiarle la licencia

*Respuesta: a).* La revocación de emergencia combina varias acciones; recuerda además que Entra ID no revoca las cookies de sesión de las aplicaciones. [Fuente](https://learn.microsoft.com/en-us/entra/identity/users/users-revoke-access) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

**14. ¿Dónde viven ahora los playbooks de respuesta a incidentes de Microsoft?**

- a) En el Ninja de Defender XDR
- b) En la disciplina SecOps del Security Adoption Framework  ✅
- c) En la página de licencias de Entra
- d) Solo en GitHub

*Respuesta: b).* Pasaron a las rutas security/zero-trust/security-operations-playbook-* de la disciplina SecOps del Security Adoption Framework. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-password-spray) · Repasa [A5](03_Nivel_3_Avanzado.md#a5)

<a id="eval-agentes"></a>

## Nivel 4 · Identidad para agentes de IA · Preparar el tenant para agentes

**1. ¿Cuándo anunció Microsoft Entra Agent ID?**

- a) 18 de noviembre de 2025
- b) 19 de mayo de 2025  ✅
- c) 1 de mayo de 2026
- d) 14 de julio de 2025

*Respuesta: b).* Se anunció el 19 de mayo de 2025; en Ignite 2025 llegaron Agent 365 y el acceso condicional para agentes en vista previa, y la GA llegó en mayo de 2026. [Fuente](https://learn.microsoft.com/en-us/security/security-for-ai/whats-new) · Repasa [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1)

**2. Sin una política de acceso condicional «bloquear salvo aprobado», las solicitudes de token de un agente…**

- a) Se permiten por defecto  ✅
- b) Se bloquean por defecto
- c) Requieren la aprobación del sponsor
- d) Requieren MFA del agente

*Respuesta: a).* El pilar de IA del Zero Trust Assessment advierte que, sin esa política, toda solicitud de token de un agente se permite por defecto. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/assessment/ai-pillar) · Repasa [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1)

**3. ¿Dónde residen las credenciales de una identidad de agente?**

- a) En la identidad de agente
- b) En la cuenta de usuario del agente
- c) En el blueprint  ✅
- d) En Key Vault, automáticamente

*Respuesta: c).* La identidad de agente no tiene credenciales propias: se autentica con las del blueprint (credenciales federadas, certificados o secretos). [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**4. ¿Qué relación administrativa es obligatoria en Agent ID?**

- a) Owner
- b) Manager
- c) Ninguna
- d) Sponsor  ✅

*Respuesta: d).* Cada identidad de agente y cada blueprint necesitan al menos un sponsor, responsable de negocio; los owners son opcionales. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**5. ¿Cuál de estos roles impide Entra asignar a una identidad de agente?**

- a) Privileged Role Administrator  ✅
- b) Ninguno: los agentes pueden recibir cualquier rol
- c) Solo los roles de Azure RBAC
- d) Solo los roles personalizados

*Respuesta: a).* Las salvaguardas impiden asignar a agentes roles como Global Administrator, Privileged Role Administrator o User Administrator, y que pertenezcan a grupos asignables a roles. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/authorization-agent-id) · Repasa [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2)

**6. Un agente actúa en nombre de un usuario (OBO). ¿A qué apunta la política de acceso condicional?**

- a) A la identidad de agente
- b) Al blueprint
- c) A los usuarios y grupos  ✅
- d) A la cuenta de usuario del agente

*Respuesta: c).* En OBO el sujeto del token es el usuario; en modo autónomo es la identidad de agente o su blueprint, y con cuenta de usuario del agente, «Agent Users». [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**7. ¿En cuál de estos casos NO protege el acceso condicional a un agente?**

- a) Cuando actúa de forma autónoma con su identidad
- b) Cuando accede a un recurso con una clave de API  ✅
- c) Cuando actúa en nombre de un usuario
- d) Cuando el tenant tiene Microsoft 365 E7

*Respuesta: b).* El acceso condicional no protege los recursos a los que se accede con claves de API, y tampoco se aplica si los valores predeterminados de seguridad están activos. [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**8. Al proteger un servidor MCP con Entra ID, ¿qué paso se omite con más frecuencia?**

- a) Habilitar MFA para el servidor
- b) Crear un secreto de cliente
- c) Configurar requestedAccessTokenVersion en 2  ✅
- d) Desactivar el acceso condicional

*Respuesta: c).* Sin tokens v2 no se puede usar la URL del servidor como Application ID URI; además hay que publicar los metadatos RFC 9728 y validar con librerías probadas. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/secure-mcp-server-with-entra-id) · Repasa [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3)

**9. ¿Cuándo llegó Agent 365 a disponibilidad general y a qué precio independiente?**

- a) 18 de noviembre de 2025, 30 USD por usuario
- b) 14 de julio de 2025, incluido en E5
- c) Enero de 2026, por agente
- d) 1 de mayo de 2026, 15 USD por usuario al mes o incluido en E7  ✅

*Respuesta: d).* Agent 365 y Microsoft 365 E7 llegaron a GA el 1 de mayo de 2026; por separado, Agent 365 cuesta 15 USD por usuario al mes. [Fuente](https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**10. ¿Qué necesitas para ver el inventario completo de agentes en el centro de administración de Microsoft 365?**

- a) Una licencia de Agent 365
- b) Solo el rol AI Reader o AI Administrator  ✅
- c) Global Administrator y E7
- d) Entra ID P2

*Respuesta: b).* Ver el inventario no requiere licencia; aplicar acceso condicional o gobernanza a los agentes, sí. [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/agent-registry-convergence) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**11. ¿Qué tabla de Defender reemplazó a AIAgentsInfo?**

- a) AgentsInfo  ✅
- b) IdentityInfo
- c) EntraIdSignInEvents
- d) CloudAppEvents

*Respuesta: a).* AgentsInfo reemplazó a AIAgentsInfo, que siguió accesible hasta el 1 de julio de 2026: hay que migrar las consultas. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-agentsinfo-table) · Repasa [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4)

**12. ¿Qué requiere el agente de optimización de acceso condicional?**

- a) Entra ID P2 y Microsoft 365 E7
- b) Agent 365
- c) Nada adicional
- d) Entra ID P1 y SCU disponibles  ✅

*Respuesta: d).* Requiere P1 y SCU de Security Copilot; por defecto no crea políticas y, si se lo autorizas, las crea en solo informe. [Fuente](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization) · Repasa [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5)

**13. ¿Quién puede emitir tokens con el Agent ID de un agente de Copilot Studio?**

- a) El Global Administrator
- b) El maker que creó el agente
- c) Cualquier Application Administrator
- d) Nadie del tenant: lo gestiona un blueprint de Microsoft con credenciales federadas  ✅

*Respuesta: d).* La identidad la gestiona un blueprint propiedad de Microsoft con credenciales federadas; nadie del tenant, ni siquiera un administrador, puede emitir tokens con ella. [Fuente](https://learn.microsoft.com/en-us/microsoft-copilot-studio/govern-agents-identities-overview) · Repasa [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6)

**14. En Microsoft Foundry, ¿qué permisos recibe una identidad de agente recién creada?**

- a) Contributor sobre la suscripción
- b) Ninguno: hay que concederlos con Azure RBAC de mínimo privilegio  ✅
- c) Los permisos de quien la creó
- d) Los de un secreto de cliente compartido

*Respuesta: b).* Foundry crea el blueprint y la identidad con credencial federada, pero no asigna permisos de Azure RBAC automáticamente. [Fuente](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-identity) · Repasa [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6)

**15. ¿Qué cubre el pilar de IA del Zero Trust Workshop, guion del proyecto integrador?**

- a) Solo las licencias de Copilot
- b) Solo la configuración de Copilot Studio
- c) Mapear el riesgo de IA, registrar agentes, asegurar autenticación, red y datos, construir agentes seguros y detectar y responder  ✅
- d) Solo el entrenamiento de modelos

*Respuesta: c).* Es el guion del proyecto integrador y se complementa con las verificaciones automáticas del pilar de IA del Zero Trust Assessment. [Fuente](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-ai-security) · Repasa [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="laboratorio-y-practica"></a>

## Laboratorio y práctica


Este archivo responde tres preguntas para este programa: qué puedes practicar en el entorno de laboratorio, qué requiere producción (y por qué), y cómo hacerlo con riesgo controlado. La guía para construir el entorno con los créditos de Azure de Visual Studio Enterprise y una prueba de Microsoft 365 E5 está en el [anexo común](../Anexo_Entorno_de_practica.md).

**Tu entorno.** Un tenant nuevo con la prueba comercial de Microsoft 365 E5 —que incluye Entra ID P2, Intune, Defender for Identity y Defender for Cloud Apps— más una suscripción de Azure con los créditos mensuales de Visual Studio Enterprise en ese mismo tenant: Log Analytics para los registros, una máquina virtual con Active Directory para Cloud Sync y Defender for Identity, Logic Apps para las extensiones de gobernanza y Foundry para el track de agentes. Encadena pruebas a medida que avanzas: Entra Suite (Private Access, Internet Access e ID Governance), ID Governance (una sola vez por tenant) y Workload ID Premium (90 días). La prueba de E5 dura un mes y pide tarjeta: planifica bloques de cuatro semanas. El paso a paso está en el anexo común.

**Qué no se puede practicar en el laboratorio.** Las alertas de monitoreo de salud (exigen P1 que no sea de prueba y al menos 100 usuarios activos al mes), las detecciones de riesgo basadas en comportamiento (solo algunas se simulan), la actualización de un Connect Sync real y el staged rollout desde AD FS, App governance si tu facturación es de México, el acceso condicional y la gobernanza de agentes sin Agent 365 o E7 (el programa Frontier no debe usarse para evaluar), la inclusión de Security Copilot (solo cuenta licencias pagas) y la sincronización entre tenants si tienes uno solo. Esos ejercicios están marcados como *Laboratorio parcial* o *Solo producción*, con su forma segura de practicar.

**Costos a vigilar.** Ingesta y retención de Log Analytics (mide uno o dos días antes de dejarlo activo), máquinas virtuales encendidas, ejecuciones de Logic Apps, SCU de Security Copilot si aprovisionas capacidad (se facturan por hora desde que la creas: bórrala al terminar), Workload ID Premium al vencer la prueba, licencias de Agent 365 (15 USD por usuario al mes) y, desde 2027, el proveedor telefónico si mantienes SMS o voz.

**Práctica segura en producción.** Políticas en modo solo informe y simuladas con What If antes de activarlas, grupos piloto y cuentas de prueba, roles de solo lectura (Global Reader, Security Reader, Reports Reader) para observar, exclusión de las cuentas de emergencia en toda política activa que pueda bloquear, ventanas de cambio con reversión documentada y la ficha de práctica en producción del anexo común.

**Limpieza.** Al cerrar cada nivel, elimina máquinas virtuales, workspaces y apps de prueba, blueprints e identidades de agente de prueba con sus credenciales, y las políticas que no vayas a reutilizar; cancela o desactiva la renovación de las pruebas antes de que se conviertan en suscripciones pagas.

<a id="matriz-laboratorio"></a>

## Matriz de laboratorio y producción

| Capacidad | ¿Laboratorio? | Requisito o limitación | Cómo practicar en producción | Riesgo | Mitigación | Fuente |
|---|---|---|---|---|---|---|
| Política de métodos de autenticación, passkeys y TAP | Sí | Los registros de passkeys requieren un teléfono o PC reales. | Campaña por grupos con acceso condicional de registro y comunicación previa. | Usuarios sin método válido o bloqueados. | Piloto, TAP para recuperación y soporte de mesa de ayuda. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-methods-manage) |
| Cuentas de emergencia | Parcial | Idealmente requieren llaves FIDO2 y un workspace para la alerta. | Crear en ventana controlada, guardar credenciales con custodia dual y probar cada trimestre. | Pérdida de acceso administrativo al inquilino. | Dos cuentas, exclusión de políticas, alerta de uso y prueba documentada. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) |
| Acceso condicional en solo informe con What If | Sí | Poco volumen de inicios de sesión en el laboratorio. | Medir 2 a 4 semanas en solo informe antes de activar por grupos. | Bloqueo masivo o de administradores. | Exclusión de emergencia, activación gradual y reversión preparada. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-report-only) |
| Políticas de riesgo y detecciones simuladas | Parcial | Solo algunas detecciones se pueden simular (Tor, propiedades desconocidas). | Políticas de riesgo en solo informe y revisión de detecciones reales. | Usuarios bloqueados por falsos positivos. | Remediación con cambio de contraseña seguro y exclusión de emergencia. | [Fuente](https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-simulate-risk) |
| PIM para roles y grupos | Sí | Con E5 de prueba hay Entra ID P2. | Convertir asignaciones permanentes en elegibles por oleadas. | Administradores sin acceso en una emergencia. | Cuentas de emergencia, aprobadores de respaldo y comunicación previa. | [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure) |
| Lifecycle workflows con extensión de Logic Apps | Parcial | Requiere la prueba de ID Governance (una vez por inquilino) y suscripción de Azure. | Usar el modo what-if y alcance a un grupo piloto. | Deshabilitar o modificar cuentas reales por error. | Revisión de alcance, ejecución bajo demanda primero y registro de auditoría. | [Fuente](https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-extensibility) |
| Acceso condicional para identidades de carga de trabajo | Parcial | Requiere Workload ID Premium (prueba de 90 días; 3 USD por identidad al mes). | Política en solo informe para un service principal piloto. | Romper integraciones de aplicaciones. | Revisar inicios de sesión de service principals antes de activar. | [Fuente](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) |
| Alertas de monitoreo de salud de Entra | No | Exigen P1/P2 que no sean de prueba y al menos 100 usuarios activos al mes. | Activarlas en producción con notificación a un grupo de prueba. | Fatiga de alertas. | Rol Reports Reader y umbrales revisados. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-investigate-health-scenario-alerts) |
| Migración de AD FS a sincronización de hash (staged rollout) | No | Requiere dominio federado y usuarios reales. | Grupo piloto pequeño manteniendo AD FS como respaldo. | Usuarios sin poder autenticarse. | Reversión documentada y ventana de cambio. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-staged-rollout) |
| Cloud Sync desde un AD de laboratorio | Parcial | AD en una VM de Azure con créditos; no reproduce la complejidad de un bosque real. | Servidor de sincronización en modo staging y migración por OU piloto. | Objetos duplicados o borrados en Entra. | Exportar configuración, alcance por OU y umbral de borrado accidental. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide) |
| Global Secure Access: perfil de tráfico de Microsoft | Parcial | Private e Internet Access requieren la prueba de Entra Suite. | Desplegar por oleadas con plan de reversión. | Pérdida de conectividad a servicios de Microsoft. | Validar restauración de IP de origen antes de exigir red conforme en acceso condicional. | [Fuente](https://learn.microsoft.com/en-us/entra/global-secure-access/tutorial-microsoft-traffic-enable-profile) |
| Blueprints e identidades de agente | Sí | Entra Agent ID se crea sin licencia adicional; el gobierno avanzado requiere Agent 365. | Piloto con un blueprint, owner y sponsor asignados. | Agentes con permisos persistentes sin dueño. | Sponsor obligatorio, revisión de acceso y vencimiento de credenciales. | [Fuente](https://learn.microsoft.com/en-us/entra/agent-id/create-blueprint) |
| Acceso condicional para agentes | No | Requiere Agent 365 (E7 o complemento con P1/E3). | Política en solo informe para un agente piloto. | Bloquear agentes que soportan procesos de negocio. | Alcance por agente, revisión del impacto y reversión. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) |
| Sincronización entre inquilinos | Parcial | Necesita dos inquilinos de prueba; los grupos requieren ID Governance. | Aprovisionamiento a demanda con un usuario de prueba. | Exponer usuarios o grupos al otro inquilino. | Alcance mínimo y revisión de la configuración de acceso entre inquilinos. | [Fuente](https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure) |
| App governance | Parcial | No disponible con facturación en México y otros países, según la investigación de la serie; activación de hasta 10 h. | Solo alertas, sin deshabilitar apps hasta validar. | Deshabilitar una app crítica. | Políticas en modo alerta y revisión con dueños de aplicaciones. | [Fuente](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) |

## Principios para practicar en producción

1. **Primero observar, después actuar.** Usa los modos de solo informe, auditoría o simulación antes de cualquier bloqueo o acción automática.
2. **Alcance mínimo.** Grupos piloto, usuarios y dispositivos de prueba etiquetados, unidades administrativas y ámbitos adaptables pequeños.
3. **Privilegio justo a tiempo.** Roles de solo lectura para estudiar y activación con PIM, aprobación y justificación para cambiar.
4. **Cuentas de emergencia excluidas y monitoreadas.** Nunca practiques acceso condicional o protección de identidad sin cuentas de emergencia probadas.
5. **Cambio registrado y reversible.** Cada práctica tiene responsable, ventana, criterio de éxito, plan de reversión y limpieza al terminar.
6. **Privacidad y áreas de negocio.** Para riesgo interno, comunicaciones o eDiscovery, acuerda con RR. HH., Legal y privacidad antes de crear políticas, aunque sean de prueba.

<a id="ejercicios"></a>

## Índice de ejercicios

Resumen: Laboratorio: 96, Laboratorio parcial: 31, Solo producción: 29, Sin etiqueta: 7.

| Módulo | N.º | Entorno | Ejercicio |
|---|---|---|---|
| [P0](01_Nivel_1_Inicial.md#p0) | 1 | Laboratorio | Registra una app de prueba, inicia sesión con OIDC y decodifica el token de ID y el de acceso con una herramienta local o un script: anota emisor (`iss`), audiencia (`aud`), scopes (`scp`) y expiración (`exp`).… |
| [P0](01_Nivel_1_Inicial.md#p0) | 2 | Laboratorio | Configura una aplicación empresarial SAML de prueba, captura la AuthnRequest y la respuesta con las herramientas del navegador e identifica NameID, audiencia y firma. Evidencia: archivo HAR anotado (protocolo SAML). |
| [P0](01_Nivel_1_Inicial.md#p0) | 3 | Laboratorio | En una VM Windows 11 unida a Entra con tus créditos de Azure (inicio de sesión en VM con Entra ID), ejecuta `dsregcmd /status` y documenta el estado del dispositivo y del PRT (PRT). |
| [P0](01_Nivel_1_Inicial.md#p0) | 4 | Laboratorio | Revoca las sesiones de un usuario de prueba con `Revoke-MgUserSignInSession` mientras tiene Outlook en la web abierto y mide cuánto tarda en pedir credenciales; compáralo con la vida del token de acceso (revocar acceso). |
| [P0](01_Nivel_1_Inicial.md#p0) | 5 | Laboratorio | Crea un usuario, un grupo, una asignación de rol, un registro de app y su service principal, y explica con capturas qué objeto recibe cada permiso. Entregable: tu glosario de objetos de una página. |
| [I0](01_Nivel_1_Inicial.md#i0) | 1 | Laboratorio | Lee la guía del SC-300 y arma una tabla «habilidad medida → módulo de esta guía → semana prevista»; súmala a tu plan. |
| [I0](01_Nivel_1_Inicial.md#i0) | 2 | Laboratorio | Suscribe la página What's new por RSS y Entra.News, y crea un canal o carpeta donde el equipo registre cada novedad con la acción que implica. |
| [I0](01_Nivel_1_Inicial.md#i0) | 3 | Laboratorio | Completa la ruta de Learn Implement an identity management solution (unas 4 horas) y guarda el registro de finalización. |
| [I0](01_Nivel_1_Inicial.md#i0) | 4 | Laboratorio | Agenda la evaluación Applied Skills para cuando termines I2 a I4; el laboratorio lo provee Microsoft, así que no necesitas tenant propio. |
| [I1](01_Nivel_1_Inicial.md#i1) | 1 | Laboratorio | En tu laboratorio, lista las licencias y planes de servicio activos (Entra ID P1/P2, Intune, Defender) y regístralos en la tabla de Licencias de identidad. Evidencia: hoja con plan, cantidad y fecha de vencimiento. |
| [I1](01_Nivel_1_Inicial.md#i1) | 2 | Laboratorio | Exporta las SKU del tenant con `Get-MgSubscribedSku` (Microsoft Graph PowerShell) y marca qué capacidades de este programa quedan cubiertas y cuáles requieren complemento (licencias de Entra). |
| [I1](01_Nivel_1_Inicial.md#i1) | 3 | Laboratorio | Mira la demostración de Entra Suite de Microsoft Mechanics y anota qué capacidades viste que no están en Microsoft 365 E5. |
| [I1](01_Nivel_1_Inicial.md#i1) | 4 | Solo producción | Construye la matriz de brechas de tu organización: por cada riesgo prioritario (phishing, privilegios, invitados, workload identities y agentes), el control, la licencia necesaria y si la tienes. Cómo hacerlo seguro:… |
| [I2](01_Nivel_1_Inicial.md#i2) | 1 | Laboratorio parcial | Crea dos cuentas de emergencia solo en la nube (*.onmicrosoft.com) con Global Administrator, protégelas con passkey FIDO2 y configura una alerta de inicio de sesión en Log Analytics. Evidencia: inicio de sesión de… |
| [I2](01_Nivel_1_Inicial.md#i2) | 2 | Laboratorio | Crea una unidad administrativa por país (por ejemplo, México y Colombia), delega User Administrator con ámbito en una de ellas y prueba que ese administrador no puede modificar usuarios de la otra. Luego crea una… |
| [I2](01_Nivel_1_Inicial.md#i2) | 3 | Laboratorio | Crea un contexto de autenticación, asócialo a una política **activa** que exija MFA resistente al phishing y protege con él la actualización de políticas de acceso condicional; intenta editar una política con y sin… |
| [I2](01_Nivel_1_Inicial.md#i2) | 4 | Laboratorio | Ejecuta Maester (versión 2.3.0) y el Zero Trust Assessment en solo lectura, compáralos con Identity Secure Score y prioriza cinco acciones con dueño y fecha. |
| [I2](01_Nivel_1_Inicial.md#i2) | 5 | Laboratorio | Consulta el estado de los valores predeterminados de seguridad con `Get-MgPolicyIdentitySecurityDefaultEnforcementPolicy`; desactívalos solo cuando tu línea base de acceso condicional esté lista y documenta la… |
| [I2](01_Nivel_1_Inicial.md#i2) | 6 | Solo producción | Inventaria los Global Administrators y las asignaciones privilegiadas permanentes de tu tenant y compáralos con las metas (menos de 5 y menos de 10). Cómo hacerlo seguro: usa Global Reader, exporta con Microsoft… |
| [I3](01_Nivel_1_Inicial.md#i3) | 1 | Laboratorio | Migra los métodos de las políticas heredadas de MFA y SSPR a la política de métodos con el asistente y habilita passkeys y TAP para un grupo piloto. Evidencia: migración marcada como completada y política exportada… |
| [I3](01_Nivel_1_Inicial.md#i3) | 2 | Laboratorio parcial | Crea dos perfiles de passkey —vinculadas al dispositivo con atestación para administradores y sincronizadas para usuarios— y lanza una campaña de registro para el piloto. Limitación: registrar passkeys exige un… |
| [I3](01_Nivel_1_Inicial.md#i3) | 3 | Laboratorio | Crea una fortaleza de autenticación personalizada y comprueba con What If y con un inicio de sesión real qué métodos la satisfacen; confirma que TAP solo satisface la fortaleza MFA (fortalezas). |
| [I3](01_Nivel_1_Inicial.md#i3) | 4 | Laboratorio parcial | Registra para la misma cuenta de prueba una passkey en Microsoft Authenticator y otra en una llave de seguridad, y verifica en los registros de inicio de sesión qué método usó cada acceso. Limitación: requiere… |
| [I3](01_Nivel_1_Inicial.md#i3) | 5 | Laboratorio | Diseña tu plan por persona con la guía de despliegue: administradores, usuarios regulados y el resto, con credencial portable o local, versiones mínimas de sistema operativo y fases de registro, uso y cumplimiento. |
| [I3](01_Nivel_1_Inicial.md#i3) | 6 | Solo producción | Plan de retiro de SMS y voz: ejecuta el script oficial para encontrar usuarios que dependen de SMS o voz, clasifícalos por persona y decide entre passkeys y proveedor telefónico. Cómo hacerlo seguro: lectura con… |
| [I4](01_Nivel_1_Inicial.md#i4) | 1 | Laboratorio | Despliega CA01 a CA05 de la línea base en modo solo informe —parte de las plantillas de acceso condicional cuando existan, como la de bloqueo de autenticación heredada— con las cuentas de emergencia excluidas en las… |
| [I4](01_Nivel_1_Inicial.md#i4) | 2 | Laboratorio | Simula con What If tres escenarios —usuario con autenticación heredada, administrador desde un equipo no administrado y cuenta de emergencia— y guarda el resultado de cada uno. |
| [I4](01_Nivel_1_Inicial.md#i4) | 3 | Laboratorio | Revisa durante una semana la pestaña de solo informe de los registros y la vista de impacto de políticas; clasifica los resultados en éxito, fallo, acción de usuario requerida y no aplicado (solo informe). |
| [I4](01_Nivel_1_Inicial.md#i4) | 4 | Laboratorio | Audita quién usa device code flow antes de bloquearlo y documenta las excepciones legítimas, como salas de reuniones (bloquear flujos de autenticación). |
| [I4](01_Nivel_1_Inicial.md#i4) | 5 | Laboratorio parcial | Habilita el workbook de información e informes sobre Log Analytics y mide el impacto de dos políticas. Limitación: Log Analytics tiene costo de ingesta y el laboratorio genera poco volumen; en producción, usa… |
| [I4](01_Nivel_1_Inicial.md#i4) | 6 | Solo producción | Revisa las políticas administradas por Microsoft de tu tenant antes de su activación automática: estado, exclusiones y fecha. Cómo hacerlo seguro: Security Reader o Global Reader, comparación con tu línea base y una… |
| [I5](01_Nivel_1_Inicial.md#i5) | 1 | Laboratorio | Recorre el árbol de decisión de métodos de autenticación con los datos de tu organización y documenta la elección (PHS, PTA o federación) con sus dependencias (elegir el método). |
| [I5](01_Nivel_1_Inicial.md#i5) | 2 | Laboratorio parcial | Despliega un AD de laboratorio en una VM de Azure, instala el agente de Cloud Sync, sincroniza una OU piloto y prueba el umbral de borrado accidental. Limitación: no reproduce la complejidad de un bosque real (guía… |
| [I5](01_Nivel_1_Inicial.md#i5) | 3 | Laboratorio parcial | Instala Connect Sync en otra VM del laboratorio, ejecuta la evaluación de preparación y prueba la herramienta guiada de migración a Cloud Sync. Limitación: el laboratorio no tiene las reglas personalizadas de un… |
| [I5](01_Nivel_1_Inicial.md#i5) | 4 | Laboratorio | Inventaria los activos Tier 0 de tu identidad híbrida (servidores de Connect, AD FS y PKI, y las cuentas que los administran) y verifica que las cuentas privilegiadas de Entra sean solo de nube. |
| [I5](01_Nivel_1_Inicial.md#i5) | 5 | Solo producción | Actualiza Connect Sync a 2.6.84.0 o superior con autenticación basada en aplicación antes del 7 de abril de 2027. Cómo hacerlo seguro: actualiza primero el servidor en modo staging, respalda y exporta la… |
| [I5](01_Nivel_1_Inicial.md#i5) | 6 | Solo producción | Staged rollout de AD FS a PHS con un grupo piloto pequeño. Cómo hacerlo seguro: mantén AD FS como respaldo, comunica al piloto, monitorea los inicios de sesión fallidos y documenta la reversión antes de convertir el… |
| [I6](01_Nivel_1_Inicial.md#i6) | 1 | Laboratorio | Arma tu laboratorio según el anexo común: prueba de Microsoft 365 E5, suscripción de Azure con presupuesto y alertas, convención de nombres y un administrador separado de tu cuenta de uso diario. Evidencia: captura… |
| [I6](01_Nivel_1_Inicial.md#i6) | 2 | Laboratorio | Crea diez usuarios de prueba en tres departamentos y dos países, con atributos de RR. HH. como employeeHireDate, que reutilizarás en M4 y X4. |
| [I6](01_Nivel_1_Inicial.md#i6) | 3 | Laboratorio | Programa Maester en GitHub Actions o Azure DevOps con la versión 2.3.0 fijada y un informe diario. |
| [I6](01_Nivel_1_Inicial.md#i6) | 4 | Laboratorio | Completa la evaluación Applied Skills de identidades y acceso y guarda la credencial. |
| [I6](01_Nivel_1_Inicial.md#i6) | 5 | Laboratorio parcial | Usa el TechLab de Entra Suite como guion con la prueba de Entra Suite activa. Limitación: el TechLab pide datos de un formato interno; adapta los pasos a tu tenant. |
| [I6](01_Nivel_1_Inicial.md#i6) | 6 | Laboratorio | Define y prueba tu rutina de limpieza: apagar VMs, revisar Cost Management y registrar la fecha de vencimiento de cada prueba para cancelarla a tiempo. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 1 | Laboratorio | Crea un contexto de autenticación (C1), asígnalo a una política que exija MFA resistente al phishing y úsalo en la activación de un rol de PIM; valida con un usuario de prueba y guarda el registro de inicio de sesión… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 2 | Laboratorio parcial | Despliega la protección de tokens (CA09) en solo informe con una VM Windows 11 unida a Entra y revisa los inicios de sesión interactivos y no interactivos. Limitación: la compatibilidad real de las apps solo se ve… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 3 | Laboratorio | Crea una política con filtro de dispositivo que solo permita administrar desde equipos marcados como PAW (por ejemplo, con un atributo de extensión) y pruébala en solo informe y con What If. |
| [M1](02_Nivel_2_Intermedio.md#m1) | 4 | Laboratorio parcial | Configura el acceso entre tenants para confiar en el MFA de un socio de prueba y crea la política CA12 para invitados; verifica el resultado en los registros. Limitación: necesitas un segundo tenant de prueba que… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 5 | Laboratorio parcial | Habilita el workbook de CAE y compara las IP que ve Entra con las que ven los recursos antes de considerar el modo estricto de ubicación. Limitación: requiere Log Analytics y tráfico desde redes variadas (CAE estricto). |
| [M1](02_Nivel_2_Intermedio.md#m1) | 6 | Solo producción | Ejecuta el agente de optimización de acceso condicional y revisa sus sugerencias sin aplicarlas; requiere SCU facturadas y datos reales. Cómo hacerlo seguro: creación de políticas desactivada, revisión con Security… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 1 | Laboratorio | Crea CA06 (riesgo de inicio de sesión medio o alto) y CA07 (riesgo de usuario alto con «Require risk remediation») en solo informe, con exclusión de las cuentas de emergencia, y revisa su impacto durante una semana… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 2 | Laboratorio parcial | Simula detecciones de riesgo (por ejemplo, navegador Tor o propiedades desconocidas) con un usuario de prueba y sigue la detección hasta el informe. Limitación: solo algunas detecciones se pueden simular (simular… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 3 | Laboratorio | Lista con Microsoft Graph PowerShell los usuarios riesgosos (`Get-MgRiskyUser`), confirma o descarta el riesgo de un usuario de prueba y documenta qué rol usaste (visión general de ID Protection). |
| [M2](02_Nivel_2_Intermedio.md#m2) | 4 | Laboratorio | Recorre como usuario la autorremediación (MFA y cambio seguro de contraseña) y redacta la comunicación para la mesa de ayuda (experiencia del usuario). |
| [M2](02_Nivel_2_Intermedio.md#m2) | 5 | Solo producción | Verifica que tu tenant real tenga políticas de acceso condicional basadas en riesgo que reemplacen a las heredadas retiradas el 1 de octubre de 2026, y mide los usuarios de riesgo alto sin remediar. Cómo hacerlo… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 1 | Laboratorio | Haz elegible a un usuario de prueba para User Administrator con aprobación, justificación, MFA y contexto de autenticación; actívalo y revisa la auditoría de la activación (configuración de roles en PIM). |
| [M3](02_Nivel_2_Intermedio.md#m3) | 2 | Laboratorio | Crea un grupo asignable a roles, gestiónalo con PIM for Groups con aprobación, asígnale un rol de Entra y programa una revisión de acceso del rol (PIM for Groups). |
| [M3](02_Nivel_2_Intermedio.md#m3) | 3 | Laboratorio | Configura las alertas de seguridad de PIM y provoca una (por ejemplo, una asignación hecha fuera de PIM) para ver su corrección (alertas de seguridad). |
| [M3](02_Nivel_2_Intermedio.md#m3) | 4 | Laboratorio | Crea una asignación elegible con ámbito de unidad administrativa y verifica que solo aplica a los objetos de esa unidad (asignar roles en PIM). |
| [M3](02_Nivel_2_Intermedio.md#m3) | 5 | Solo producción | Convierte las asignaciones permanentes de tu tenant en elegibles, por oleadas. Cómo hacerlo seguro: empieza por roles de bajo impacto, deja las dos cuentas de emergencia como únicas permanentes, designa aprobadores… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 1 | Laboratorio | Crea un catálogo y un paquete de acceso para los invitados de un proyecto, con aprobación, expiración a 90 días y revisión trimestral (entitlement management). |
| [M4](02_Nivel_2_Intermedio.md#m4) | 2 | Laboratorio | Configura una revisión de acceso de un grupo con aplicación automática de resultados y un revisor de prueba; documenta la decisión y su efecto (revisiones de acceso). |
| [M4](02_Nivel_2_Intermedio.md#m4) | 3 | Laboratorio parcial | Activa la prueba de ID Governance y crea un flujo de alta y otro de baja en Lifecycle Workflows a partir de employeeHireDate; ejecútalos en modo what-if. Limitación: la prueba se activa una sola vez por tenant… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 4 | Laboratorio parcial | Configura la sincronización entre tenants de usuarios y aprovisiona a demanda un usuario de prueba. Limitación: necesitas dos tenants de prueba y los grupos requieren ID Governance (configurar la sincronización). |
| [M4](02_Nivel_2_Intermedio.md#m4) | 5 | Laboratorio | Revisa la configuración predeterminada de acceso entre tenants y documenta con qué socio confiarías en el MFA y en las reclamaciones de dispositivo, y por qué (acceso entre tenants). |
| [M4](02_Nivel_2_Intermedio.md#m4) | 6 | Solo producción | Identifica en tu tenant los invitados sin patrocinador y sin actividad y diseña su limpieza. Cómo hacerlo seguro: inventario con Global Reader, revisión de acceso con los dueños de negocio antes de borrar y un… |
| [M5](02_Nivel_2_Intermedio.md#m5) | 1 | Laboratorio | Restringe el consentimiento de usuarios a editores verificados y permisos de bajo riesgo, habilita el flujo de consentimiento del administrador con dos revisores y aprueba la solicitud de una app de prueba… |
| [M5](02_Nivel_2_Intermedio.md#m5) | 2 | Laboratorio | Respalda la política de administración de apps actual, aplica una que bloquee secretos nuevos y limite la vida de los certificados, y comprueba que agregar un secreto falla (políticas de administración de apps). |
| [M5](02_Nivel_2_Intermedio.md#m5) | 3 | Laboratorio | Crea una app nueva y verifica que el bloqueo de propiedades de instancia está habilitado por defecto (bloqueo de propiedades). |
| [M5](02_Nivel_2_Intermedio.md#m5) | 4 | Laboratorio | Inventaria con Microsoft Graph PowerShell las apps con permisos de aplicación de alto riesgo (por ejemplo, de lectura y escritura de correo o del directorio) y las que usan secretos en lugar de certificados o… |
| [M5](02_Nivel_2_Intermedio.md#m5) | 5 | Laboratorio parcial | Activa App governance y revisa sus políticas predefinidas. Limitación: no está disponible con facturación en México y otros países, y la activación puede tardar hasta 10 horas; en producción, solo alertas, sin… |
| [M5](02_Nivel_2_Intermedio.md#m5) | 6 | Solo producción | Si tu facturación excluye App governance, arma la alternativa con consultas sobre la auditoría de consentimientos y el playbook de concesión ilícita de consentimiento. Cómo hacerlo seguro: consultas de solo lectura y… |
| [M6](02_Nivel_2_Intermedio.md#m6) | 1 | Laboratorio | Crea una configuración de diagnóstico que envíe a Log Analytics los inicios de sesión interactivos y no interactivos, de service principals y de identidades administradas, la auditoría, el aprovisionamiento y los… |
| [M6](02_Nivel_2_Intermedio.md#m6) | 2 | Laboratorio | Escribe cinco consultas KQL: autenticación heredada (`SigninLogs` por `ClientAppUsed`), resultados de solo informe, cambios en políticas de acceso condicional (`AuditLogs`), consentimientos a aplicaciones y fallos de… |
| [M6](02_Nivel_2_Intermedio.md#m6) | 3 | Laboratorio | Habilita AADGraphActivityLogs y busca patrones de reconocimiento con herramientas como ROADtools o AADInternals usando las consultas del artículo de Fabian Bader. |
| [M6](02_Nivel_2_Intermedio.md#m6) | 4 | Laboratorio | Mide la ingesta de dos días con la tabla `Usage`, proyecta el costo mensual por tabla y propone qué tablas podrían ir a niveles más económicos (opciones de integración). |
| [M6](02_Nivel_2_Intermedio.md#m6) | 5 | Laboratorio | Revisa Identity Secure Score y las recomendaciones de Entra; marca una acción como «riesgo aceptado» con justificación y otra como planeada con fecha (Identity Secure Score). |
| [M6](02_Nivel_2_Intermedio.md#m6) | 6 | Solo producción | Activa las alertas de monitoreo de salud, que exigen P1 o P2 no de prueba y al menos 100 usuarios activos al mes. Cómo hacerlo seguro: rol Reports Reader, notificaciones a un grupo de prueba y umbrales revisados para… |
| [M7](02_Nivel_2_Intermedio.md#m7) | 1 | Laboratorio | Une a Entra una VM Windows 11 de laboratorio, inscríbela en Intune, crea una política de cumplimiento y verifica el estado del dispositivo y del PRT con `dsregcmd /status` (planificar la unión a Entra). |
| [M7](02_Nivel_2_Intermedio.md#m7) | 2 | Laboratorio | Despliega CA08 (dispositivo conforme) en solo informe y analiza los resultados por plataforma (solo informe). |
| [M7](02_Nivel_2_Intermedio.md#m7) | 3 | Laboratorio parcial | Configura Platform SSO con la clave de Secure Enclave en un Mac de prueba inscrito en Intune. Limitación: requiere hardware Apple; en producción, piloto con Company Portal 5.2404.0 o posterior y macOS 14 (configurar… |
| [M7](02_Nivel_2_Intermedio.md#m7) | 4 | Laboratorio | Documenta el árbol de decisión de tu organización: qué equipos van con registro, con unión a Entra o con unión híbrida, y por qué (planificar dispositivos). |
| [M7](02_Nivel_2_Intermedio.md#m7) | 5 | Solo producción | Limpia los dispositivos obsoletos de tu tenant. Cómo hacerlo seguro: exporta primero, deshabilita antes de eliminar, acuerda un umbral de inactividad con los dueños y prueba la eliminación temporal (vista previa)… |
| [M8](02_Nivel_2_Intermedio.md#m8) | 1 | Laboratorio parcial | Habilita el perfil de tráfico de Microsoft para un grupo piloto, instala el cliente en una VM Windows 11 y verifica las reglas de reenvío. Limitación: Private Access e Internet Access requieren la prueba de Entra… |
| [M8](02_Nivel_2_Intermedio.md#m8) | 2 | Laboratorio parcial | Activa la restauración de la IP de origen y la condición de red conforme, y crea CA13 en solo informe. Limitación: el laboratorio no reproduce el volumen ni la diversidad de redes de producción (guía de despliegue). |
| [M8](02_Nivel_2_Intermedio.md#m8) | 3 | Laboratorio parcial | Configura las restricciones universales de inquilino y comprueba que, desde el dispositivo con cliente, un usuario no puede iniciar sesión en un tenant ajeno. Limitación: necesitas una cuenta de otro tenant para… |
| [M8](02_Nivel_2_Intermedio.md#m8) | 4 | Laboratorio parcial | Con la prueba de Entra Suite, publica con Private Access una app interna de la VM de AD (por ejemplo, RDP) y exígele MFA con acceso condicional, como en el episodio del Virtual Ninja Show. Limitación: requiere la… |
| [M8](02_Nivel_2_Intermedio.md#m8) | 5 | Solo producción | Plan de despliegue por oleadas del perfil de tráfico de Microsoft en producción. Cómo hacerlo seguro: grupos por oleada, plan de reversión probado, monitoreo de conectividad y validación de la restauración de la IP… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 1 | Laboratorio | Inventaria con Microsoft Graph PowerShell los service principals, las identidades administradas (filtro `servicePrincipalType eq 'ManagedIdentity'`) y las credenciales con su fecha de vencimiento; marca los secretos… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 2 | Laboratorio | Respalda la política de administración de apps del tenant y aplica una que bloquee secretos nuevos y limite los certificados a 180 días; prueba que un secreto nuevo falla (tutorial). |
| [A1](03_Nivel_3_Avanzado.md#a1) | 3 | Laboratorio | Federa un workflow de GitHub Actions con una identidad administrada asignada por el usuario, sin secretos, y despliega un recurso de prueba; luego crea una credencial federada flexible atada a `repository_id`… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 4 | Laboratorio parcial | Activa la prueba de Workload ID Premium y crea CA14 para un service principal propio, primero en solo informe, revisando los inicios de sesión de service principals. Limitación: la prueba dura 90 días; en producción,… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 5 | Laboratorio parcial | Revisa el informe de workload identities riesgosas y prepara el runbook de respuesta para credenciales filtradas. Limitación: en un tenant de prueba es raro ver detecciones reales; sin Premium el detalle es limitado… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 6 | Solo producción | Elimina los secretos de los service principals de producción por oleadas, migrando a certificados o federación. Cómo hacerlo seguro: inventario de dependencias con los dueños, ventana de cambio, prueba del nuevo… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 1 | Laboratorio | Arma tu mapa de señales: para password spray, AiTM, phishing de código de dispositivo, consentimiento ilícito y robo de PRT, indica qué fuente lo detecta (ID Protection, Defender for Identity, Defender for Cloud Apps… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 2 | Laboratorio parcial | Provoca unos pocos inicios de sesión fallidos controlados sobre cuentas de prueba y sigue la guía de clasificación de alertas de password spray. Limitación: un intento de laboratorio no siempre dispara la detección… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 3 | Laboratorio parcial | Despliega el sensor v3.x de Defender for Identity en el controlador de dominio del laboratorio y revisa las recomendaciones de postura. Limitación: requiere la VM de AD con Windows Server 2019 o posterior y costo de… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 4 | Laboratorio | Importa dos consultas del Attack & Defense Playbook y las del análisis de la campaña AiTM de abril de 2026 a la búsqueda avanzada, adáptalas a EntraIdSignInEvents y documenta qué devuelven. |
| [A2](03_Nivel_3_Avanzado.md#a2) | 5 | Laboratorio | Revoca la sesión de un usuario de prueba con clientes compatibles abiertos y mide el efecto de CAE frente a un cliente que no lo admite (CAE). |
| [A2](03_Nivel_3_Avanzado.md#a2) | 6 | Solo producción | Caza AiTM y robo de tokens con telemetría real y revisa la configuración de la interrupción automática. Cómo hacerlo seguro: consultas de solo lectura con Security Reader, un ejercicio de mesa con el playbook de robo… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 1 | Laboratorio | Migra un script heredado de AzureAD o MSOnline a Microsoft Graph PowerShell o Entra PowerShell y ejecútalo con una identidad de carga de trabajo federada, no con una cuenta de usuario (Entra PowerShell). |
| [A3](03_Nivel_3_Avanzado.md#a3) | 2 | Laboratorio | Exporta tus políticas de acceso condicional a JSON con Microsoft Graph, versiónalas en un repositorio y aprueba un cambio mediante pull request con revisión por pares. |
| [A3](03_Nivel_3_Avanzado.md#a3) | 3 | Laboratorio | Ejecuta Maester en GitHub Actions con `Install-Module Maester -RequiredVersion 2.3.0` y publica el informe como artefacto del pipeline (Maester 3.0 y cómo fijar versiones). |
| [A3](03_Nivel_3_Avanzado.md#a3) | 4 | Laboratorio | Crea en Tenant Governance una instantánea y un monitor de deriva sobre una política de acceso condicional de prueba; modifícala y comprueba que la deriva se detecta (anuncio de Tenant Governance). |
| [A3](03_Nivel_3_Avanzado.md#a3) | 5 | Laboratorio parcial | Extiende un flujo de Lifecycle Workflows con una Logic App («launch and continue») autorizada por identidad administrada. Limitación: requiere la prueba de ID Governance y una suscripción de Azure; el rol Logic App… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 6 | Solo producción | Descubre los tenants relacionados y crea relaciones de gobierno con Tenant Governance. Cómo hacerlo seguro: según fuentes comunitarias el descubrimiento es una acción de un solo sentido; empieza con instantáneas y… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 1 | Laboratorio | Clasifica los roles y grupos privilegiados de tu laboratorio en planos de control, administración y datos con EntraOps o con una hoja propia, y marca las rupturas de nivel. |
| [A4](03_Nivel_3_Avanzado.md#a4) | 2 | Laboratorio | Diseña las rutas de acceso privilegiado: PAW o equivalente, PIM con contexto de autenticación, la política CA10 y una unidad de administración restringida para las cuentas Tier 0. Entregable: diagrama y matriz de… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 3 | Laboratorio | Ejecuta el Zero Trust Assessment y mapea sus hallazgos de identidad a las cuatro etapas de la hoja de ruta de acceso privilegiado. |
| [A4](03_Nivel_3_Avanzado.md#a4) | 4 | Laboratorio | Recorre el Zero Trust Workshop · Identidad y prioriza tres áreas de implementación para tu organización con su justificación. |
| [A4](03_Nivel_3_Avanzado.md#a4) | 5 | Solo producción | Inventario Tier 0 real: Global Administrators, Privileged Role Administrators, servidores de Entra Connect, AD FS y PKI, y el rol AI Administrator. Cómo hacerlo seguro: inventario de solo lectura, acceso restringido… |
| [A5](03_Nivel_3_Avanzado.md#a5) | 1 | Laboratorio | Simulacro de revocación sobre un usuario de prueba: deshabilitar, restablecer la contraseña, `Revoke-MgUserSignInSession` y deshabilitar dispositivos; mide cuánto tardan Outlook y Teams en perder acceso (revocar el… |
| [A5](03_Nivel_3_Avanzado.md#a5) | 2 | Laboratorio | Con Backup and Recovery, modifica una política de acceso condicional de prueba, genera el informe de diferencias y recupérala (recuperar objetos). |
| [A5](03_Nivel_3_Avanzado.md#a5) | 3 | Laboratorio | Haz un ejercicio de mesa con el playbook de robo de tokens: árbol de decisión, quién hace qué y en cuánto tiempo. |
| [A5](03_Nivel_3_Avanzado.md#a5) | 4 | Laboratorio | Investiga una concesión ilícita simulada (una app de prueba con permisos excesivos consentida por un usuario de prueba) siguiendo el playbook de consentimiento y documenta la contención. |
| [A5](03_Nivel_3_Avanzado.md#a5) | 5 | Laboratorio | Protege con una acción protegida el borrado definitivo de objetos, para que un atacante no pueda eliminar lo que Backup and Recovery no recupera (acciones protegidas). |
| [A5](03_Nivel_3_Avanzado.md#a5) | 6 | Solo producción | Simulacro integral con el SOC en producción. Cómo hacerlo seguro: cuentas de prueba creadas para el ejercicio, aviso previo al SOC y a la mesa de ayuda, criterios de parada y revisión posterior con lecciones aprendidas. |
| [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1) | 1 | Laboratorio parcial | Con el rol AI Reader, revisa el inventario de agentes y la tabla `AgentsInfo` de tu tenant de prueba y clasifica cada agente por plataforma y patrón de acceso. Limitación: un tenant de prueba tiene pocos agentes;… |
| [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1) | 2 | Laboratorio | Arma la cronología 2025–2026 de Agent ID, Agent 365 y Microsoft 365 E7 con su fuente y escribe en una página qué cambia para tu organización (novedades de seguridad para IA). |
| [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1) | 3 | Laboratorio | Mapea los riesgos del OWASP Top 10 agéntico a controles de Entra, Purview y Defender, con un dueño por control; usa el reparto de responsabilidades de Agent 365. |
| [X1](04_Nivel_4_Identidad_para_agentes_de_IA.md#x1) | 4 | Solo producción | Entrevista a tres equipos que ya construyen agentes y documenta qué identidad usa cada agente (cuenta de usuario, service principal o Agent ID) y quién responde por él. Cómo hacerlo seguro: solo lectura y sin… |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 1 | Laboratorio | Crea un blueprint y una identidad de agente con Microsoft Graph o PowerShell, asigna un owner y un sponsor (un grupo dinámico) y compruébalo en el portal (crear un blueprint). |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 2 | Laboratorio | Revisa la opción de tenant «Users can create agent blueprints» y asigna Agent ID Developer como rol elegible en PIM a un desarrollador de prueba (crear un blueprint). |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 3 | Laboratorio | Intenta asignar Global Administrator a la identidad de agente y documenta el bloqueo; después asigna un rol permitido y justifícalo por escrito (autorización en Agent ID). |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 4 | Laboratorio | Sigue el laboratorio comunitario de Agent ID para conectar un agente de ejemplo con permisos heredables, reemplazando el secreto de desarrollo por una credencial federada o un certificado. |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 5 | Laboratorio | Diseña la arquitectura de identidades de agente de tu organización con la guía de cuatro pasos: tipo de identidad, patrón de operación, número de blueprints e identidades por blueprint. |
| [X2](04_Nivel_4_Identidad_para_agentes_de_IA.md#x2) | 6 | Solo producción | Piloto en producción con un blueprint, owner y sponsor asignados. Cómo hacerlo seguro: un solo agente de bajo riesgo, permisos enumerados mínimos, revisión de acceso programada y fecha de vencimiento de las credenciales. |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 1 | Laboratorio | Construye la matriz agente → patrón de acceso (en nombre de un usuario, autónomo o con cuenta de usuario del agente) → objeto al que apunta la política, para tres agentes de ejemplo (acceso condicional para agentes). |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 2 | Laboratorio | Simula con What If (identidades de agente, en vista previa) qué políticas aplicarían a tu identidad de agente de prueba y guarda el resultado (What If). |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 3 | Solo producción | Crea CA15 «bloquear salvo aprobado» para un agente piloto; requiere E7 o Agent 365 (el programa Frontier no debe usarse para evaluar). Cómo hacerlo seguro: política en solo informe con alcance a ese agente, revisión… |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 4 | Laboratorio | Protege un servidor MCP de ejemplo con Entra ID —tokens v2, metadatos RFC 9728 y validación con librería— y conéctalo con una identidad de agente (proteger un servidor MCP). |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 5 | Laboratorio | Calcula los permisos efectivos de tu agente (propios más heredados del blueprint, decodificando un token de prueba) y elimina los que no use (administrar identidades de agente). |
| [X3](04_Nivel_4_Identidad_para_agentes_de_IA.md#x3) | 6 | Laboratorio parcial | Sigue el laboratorio oficial 3B: Foundry, Copilot Studio, acceso condicional para agentes y radio de impacto en Defender. Limitación: el acceso condicional para agentes requiere E7 o Agent 365 y Foundry usa tu… |
| [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) | 1 | Laboratorio parcial | Consulta `AgentsInfo` en la búsqueda avanzada y migra una consulta antigua que usara AIAgentsInfo. Limitación: con pocos agentes de prueba los resultados son escasos y algunas columnas dependen de Agent 365 (AgentsInfo). |
| [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) | 2 | Laboratorio | Arma la matriz de licencias de Agent 365: personas que gestionan, patrocinan o usan agentes frente a E7 o complemento, y qué funciones quedan sin cubrir (descripción de servicio). |
| [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) | 3 | Laboratorio | Diseña las reglas de ciclo de vida de tus agentes: inactividad, agentes sin owner o sin sponsor, transferencia de patrocinio y vencimiento de paquetes de acceso (gobernar identidades de agente). |
| [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) | 4 | Solo producción | Flujos de ciclo de vida de sponsors y paquetes de acceso para agentes, que requieren Agent 365 o E7 y movimientos reales de personal. Cómo hacerlo seguro: piloto con un blueprint y un grupo de sponsors de prueba, y… |
| [X4](04_Nivel_4_Identidad_para_agentes_de_IA.md#x4) | 5 | Solo producción | Plantillas de políticas y reglas automáticas del centro de administración de Microsoft 365 (agentes sin owner, agentes riesgosos). Cómo hacerlo seguro: alcance a un piloto, revisión antes de aplicar cada acción y… |
| [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) | 1 | Laboratorio | Calcula la capacidad de Security Copilot incluida para tu organización (400 SCU al mes por cada 1.000 licencias pagas, con tope de 10.000) y estima cuántas ejecuciones del agente de optimización puedes programar… |
| [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) | 2 | Laboratorio parcial | Documenta, a partir del catálogo de agentes de Entra, la identidad, los permisos, los roles y la licencia de cada agente. Limitación: sin SCU no puedes activarlos para verlos en tu tenant. |
| [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) | 3 | Laboratorio parcial | En una sesión corta con 1 SCU aprovisionada y excedente en 0, prueba prompts de gobernanza en Entra (revisiones de acceso, PIM) y borra la capacidad al terminar. Limitación: Security Copilot no tiene prueba gratuita… |
| [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) | 4 | Solo producción | Configura el agente de optimización de acceso condicional con disparador diario y revisa sus sugerencias; requiere SCU y datos reales. Cómo hacerlo seguro: deja desactivada la creación de políticas, aprueba solo… |
| [X5](04_Nivel_4_Identidad_para_agentes_de_IA.md#x5) | 5 | Solo producción | Evalúa el Identity Risk Management Agent sobre usuarios riesgosos reales. Cómo hacerlo seguro: alcance a un grupo piloto, aprobación manual de cada remediación y registro de las decisiones (Identity Risk Management… |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 1 | Laboratorio | En Copilot Studio (prueba), crea un agente, localiza su Entra Agent ID en Settings > Advanced > Metadata y revisa en Entra los permisos de sus conectores (Agent ID en Copilot Studio). |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 2 | Laboratorio | Crea una política de datos de Power Platform que impida agentes sin autenticación y restrinja HTTP en el entorno de desarrollo, y verifica que tu agente de prueba la cumple (seguridad y gobierno de Copilot Studio,… |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 3 | Laboratorio parcial | Ejecuta en Defender las consultas comunitarias de la carpeta «AI Agent» y la tabla AgentsInfo. Limitación: con pocos agentes de prueba los resultados son escasos y algunas columnas dependen de Agent 365; en… |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 4 | Laboratorio | En Microsoft Foundry, con tu suscripción de Azure, crea un agente, revisa su blueprint y su identidad y asígnale el rol de Azure mínimo para leer un recurso de prueba (identidad de agentes en Foundry). |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 5 | Laboratorio | Mapea el OWASP Top 10 agéntico a controles de Copilot Studio y Agent 365 con el análisis de Microsoft de marzo de 2026. |
| [X6](04_Nivel_4_Identidad_para_agentes_de_IA.md#x6) | 6 | Solo producción | Revisa los agentes reales de tu organización contra las diez configuraciones inseguras. Cómo hacerlo seguro: solo lectura con Security Reader, informe a los makers y corrección entorno por entorno con los dueños. |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 1 | Laboratorio | Fase 1 · Diagnóstico: ejecuta el Zero Trust Assessment (pilar de IA) y completa el estado de cada control en la tabla de preparación del tenant para agentes (pilar de IA). |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 2 | Laboratorio | Fase 2 · Identidad: un blueprint con credencial federada, dos identidades de agente con sponsor y los roles de IA solo elegibles en PIM (controles 2 a 8). |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 3 | Solo producción | Fase 3 · Acceso: CA15 a CA17 y la plantilla de agentes de alto riesgo (controles 9 a 13), que requieren E7 o Agent 365. Cómo hacerlo seguro: todas en solo informe, alcance a un agente piloto, revisión del impacto y… |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 4 | Laboratorio | Fase 4 · Permisos y herramientas: servidor MCP protegido con Entra, permisos heredables enumerados, herramientas denegadas por defecto y consentimiento restringido (controles 14 a 16). |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 5 | Laboratorio | Fase 5 · Plataformas: política de datos de Copilot Studio, Agent ID en todos sus agentes y Azure RBAC mínimo en Foundry (controles 17 a 19). |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 6 | Laboratorio parcial | Fase 6 · Gobierno y monitoreo: reglas de ciclo de vida, registros en Log Analytics, `AgentsInfo` y una alerta por agente nuevo sin sponsor (controles 20, 21 y 23). Limitación: los paquetes de acceso para agentes… |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 7 | Laboratorio | Fase 7 · Respuesta: runbook para deshabilitar un agente y luego su blueprint, ensayado y cronometrado (control 22). |
| [X7](04_Nivel_4_Identidad_para_agentes_de_IA.md#x7) | 8 | Solo producción | Fase 8 · Comité: presenta arquitectura, licencias (control 24), métricas y hoja de ruta de seis meses, y decide sobre el primer agente productivo con los criterios del proyecto. Cómo hacerlo seguro: piloto con un… |
| [C1](Practica-y-referencias.md#c1) | 1 | — | Elige tres referentes de la hoja «Referentes» según tu rol, suscríbete a sus blogs y registra cada semana una idea aplicable a tu tenant. |
| [C1](Practica-y-referencias.md#c1) | 2 | — | Lee el capítulo Agent Identities del Attack & Defense Playbook y anota dos detecciones que quieras construir. |
| [C1](Practica-y-referencias.md#c1) | 3 | — | Recorre el catálogo de Jan Bakker y arma tu lista de lectura del track de agentes. |
| [C2](Practica-y-referencias.md#c2) | 1 | — | Suscríbete a Entra.News y escucha el episodio 123 de The Azure Security Podcast sobre identidad agéntica. |
| [C2](Practica-y-referencias.md#c2) | 2 | — | Arma una biblioteca en español para tu equipo con las versiones de Learn de la guía del SC-300, los valores predeterminados de seguridad, Agent ID, MCP y Copilot Studio, y marca cuáles son traducción automática. |
| [C3](Practica-y-referencias.md#c3) | 1 | — | Define tu rutina: cada semana, Entra.News y THE PROMPT; cada mes, las novedades de Entra, Agent ID y seguridad para IA; cada trimestre, la descripción de servicio de Agent 365 y el Attack & Defense Playbook. |
| [C3](Practica-y-referencias.md#c3) | 2 | — | Suscríbete al RSS de novedades de Entra y al de versiones de Entra Connect (aka.ms/aadconnectrss), y agenda la revisión de las tablas de licencias y de preparación para agentes después de Ignite. |

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="glosario-y-fuentes"></a>

## Cierre, glosario y fuentes


<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja no es un estado, es un hábito. Entra publica novedades cada mes y 2027 trae fechas que no se pueden perder —el fin de SMS y voz entregados por Microsoft y la actualización obligatoria de Connect Sync—. Dedica media hora por semana a la rutina de [C3](Practica-y-referencias.md#c3), vuelve a esta guía cuando un cambio afecte a tu operación y repasa las tablas de [licencias](00_Programa.md#licencias) y de [preparación para agentes](00_Programa.md#preparacion-agentes) después de Ignite y de los webinars de profundización de Entra del 15 al 17 de diciembre de 2026.

Próximos pasos: el examen SC-300 y la credencial Applied Skills de identidades y acceso; el programa de **Defender XDR** para operar ITDR desde el SOC; el de **Sentinel** para los datos y las detecciones de identidad; el de **Security Copilot** para el parque de agentes de seguridad; y el de **Purview DSPM** para los datos que usan los agentes. Si encuentras un enlace roto o un dato desactualizado, regístralo y compártelo con tu equipo: la guía está pensada para revisarse después de cada Ignite, como los Ninja oficiales.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Acción protegida | Permiso sensible de Entra (editar el acceso condicional, el acceso entre tenants o las ubicaciones con nombre, o borrar de forma definitiva) que exige cumplir una política de acceso condicional mediante un contexto de autenticación. |
| Agent 365 | Plano de control de Microsoft para observar, gobernar y proteger agentes; GA el 1 de mayo de 2026, incluido en Microsoft 365 E7 o como complemento por usuario. |
| AiTM | Adversario en el medio: phishing con un proxy que roba la cookie de sesión después del MFA; se mitiga con credenciales resistentes al phishing y con protección de la sesión. |
| Blueprint de identidad de agente | Plantilla y contenedor de credenciales de un tipo de agente; sus permisos se heredan en todas sus identidades de agente. |
| CAE | Continuous access evaluation: evaluación continua que revoca sesiones casi en tiempo real ante eventos críticos (hasta 15 minutos) y aplica al instante los cambios de ubicación en servicios compatibles. |
| Contexto de autenticación | Etiqueta (C1 a C99) que una aplicación, PIM o una acción protegida solicitan para exigir una política de acceso condicional más estricta. |
| Cuenta de emergencia | Cuenta solo en la nube con Global Administrator, protegida con passkey FIDO2 o CBA, excluida de las políticas que bloquean y monitoreada; se recomiendan al menos dos. |
| Entra Agent ID | Marco de identidad y seguridad de Entra para agentes de IA: blueprints, identidades de agente y usuarios de agente. |
| Entra Suite | Paquete de Private Access, Internet Access, ID Governance, ID Protection y Verified ID premium; se vende aparte (requiere P1) o viene en Microsoft 365 E7. |
| Fortaleza de autenticación | Control de acceso condicional que define qué combinaciones de métodos se aceptan: MFA, MFA sin contraseña, MFA resistente al phishing o una personalizada. |
| Global Secure Access | Servicio de borde de seguridad (SSE) de Microsoft: perfil de tráfico de Microsoft, Private Access e Internet Access. |
| Identidad administrada | Service principal especial cuyas credenciales gestiona Azure; puede estar asignada por el sistema o por el usuario. |
| Identidad de agente | Service principal especial, de un solo tenant y sin credenciales propias, que representa a un agente de IA. |
| ITDR | Identity threat detection and response: disciplina de detectar y responder a ataques contra identidades en Active Directory y en la nube. |
| MCP | Model Context Protocol: estándar abierto para que los agentes descubran y usen herramientas; Entra puede actuar como su servidor de autorización. |
| OBO | On-behalf-of: flujo en el que un agente o una API actúa en nombre de un usuario; el sujeto del token es el usuario. |
| PAW | Estación de trabajo de acceso privilegiado: dispositivo aislado y endurecido, reservado para tareas administrativas. |
| Passkey | Credencial FIDO2 resistente al phishing; puede estar vinculada al dispositivo (llave de seguridad o Authenticator) o sincronizada entre los dispositivos del usuario. |
| PHS | Sincronización de hash de contraseñas: el método de autenticación híbrida más simple y resiliente, necesario para detectar credenciales filtradas. |
| PIM | Privileged Identity Management: asignaciones elegibles y activación de roles justo a tiempo, con aprobación, MFA y auditoría. |
| PRT | Primary Refresh Token: artefacto de inicio de sesión único en Windows, macOS, iOS, Android y Linux que transporta las reclamaciones del dispositivo. |
| RMAU | Unidad administrativa de administración restringida: solo los administradores con ámbito en ella pueden modificar sus objetos. |
| SCU | Security Compute Unit: unidad de capacidad de Security Copilot. |
| Sponsor | Persona responsable de negocio de un blueprint o de una identidad de agente; es obligatoria en Agent ID. |
| TAP | Temporary Access Pass: código temporal para el arranque y la recuperación de credenciales; solo cuenta como MFA. |
| Tenant Governance | Capacidad de Entra (GA el 10 de agosto de 2026) para líneas base, deriva de configuración, instantáneas y relaciones de administración delegada entre tenants. |
| Usuario de agente | Cuenta de usuario opcional, 1:1 con una identidad de agente, para escenarios con buzón o Teams; solo en tenants del programa Frontier. |
| Workload ID Premium | SKU de 3 USD por identidad al mes para acceso condicional, ID Protection y CAE de workload identities; no está incluido en E5 ni en E7. |
| Workload identity federation | Confianza en tokens de un proveedor externo (GitHub, Kubernetes, AWS, Google Cloud) para eliminar los secretos de apps e identidades administradas. |
| Zero Trust Assessment | Herramienta de solo lectura que evalúa el tenant en siete pilares, incluido el de IA; proyecto comunitario mantenido por empleados de Microsoft. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **No hay Ninja oficial de Entra.** La [etiqueta ninja training](https://techcommunity.microsoft.com/tag/ninja%20training) y los rastreadores comunitarios no muestran uno al 6 de noviembre de 2026. El certificado de participación al 80 % de la familia Ninja se describe en resúmenes comunitarios ([MS Cloud Explorers](https://mscloudexplorers.com/learn/)) y no se reverificó en una fuente oficial.
- **Ponderación del SC-300.** La misma [guía de estudio](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-300) asigna 25–30 % al dominio «Implement authentication and access management» en el resumen y 20–25 % en el detalle.
- **Retiro de SMS y voz.** El [blog del 13 de julio de 2026](https://www.microsoft.com/en-us/security/blog/2026/07/13/microsoft-entra-id-security-updates-passkeys-are-the-default-authentication-method-in-entra-id/) fija una sola fecha (1 de febrero de 2027, sin opt-out); el [documento de Learn](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) y el aviso [MC1426371](https://mc.merill.net/message/MC1426371) (actualizado el 15 de septiembre de 2026) agregan el 1 de julio de 2027 para Global Administrators activos y usuarios externos y una exclusión temporal de la habilitación automática. Esta guía usa la versión más reciente; según la [FAQ](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement-faq), un Global Administrator solo elegible en PIM sigue la fecha de febrero.
- **Licencia de las políticas administradas.** Su [página](https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies) pide «P2 o Business Premium» como requisito, mientras la [página de licencias](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) indica que el acceso condicional requiere P1.
- **Protección de tokens en Apple.** La tabla de plataformas de la [página de protección de tokens](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) marca iOS/iPadOS y macOS como GA, pero su sección de dispositivos aún dice «Apple (Preview)» y la versión en español sigue en vista previa.
- **Fecha límite de Connect Sync.** Avisos anteriores exigían la versión 2.5.79.0 antes del 30 de septiembre de 2026; el aviso vigente exige 2.6.84.0 con autenticación basada en aplicación antes del 7 de abril de 2027 ([historial de versiones](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history)).
- **Credencial de plataforma de macOS.** La [guía de prerrequisitos passwordless](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication) la etiqueta «(preview)» mientras Platform SSO se documenta como soportado: verifica el estado en tu tenant.
- **Applied Skills.** La evaluación [APL-0501](https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-0501) aún evalúa el MFA por usuario heredado, aunque Microsoft recomienda convertirlo a acceso condicional.
- **Nombre comercial en la guía de Global Secure Access.** La [guía del perfil de tráfico de Microsoft](https://learn.microsoft.com/en-us/entra/architecture/gsa-deployment-guide-microsoft-traffic) menciona «Microsoft Entra Secure Access Essentials», un nombre que no aparece en la página de licencias.
- **Estado del Zero Trust Assessment.** A veces se lo presenta como un módulo de Microsoft, pero su [README](https://github.com/microsoft/zerotrustassessment) aclara que es un proyecto comunitario mantenido por empleados, sin soporte oficial; un resultado de búsqueda antiguo lo mostraba como archivado, pero el repositorio verificado está activo.
- **Rol de Merill Fernando.** Su [sitio personal](https://merill.net/about/) indica que dejó Microsoft en 2026 para fundar Jozra; la [página «About» de Entra.News](https://entra.news/about) y la de autores de Maester aún lo presentan como gerente de producto de Microsoft.
- **Historial de Backup and Recovery.** Learn indica 7 días ([visión general](https://learn.microsoft.com/en-us/entra/backup/overview)) y la [API de Graph](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-backup-recovery-overview?view=graph-rest-1.0) 5 días: planifica con el valor menor.
- **PIM for Groups.** Un [sitio de asesoría de licencias](https://microsoftnegotiations.com/blog/microsoft-identity-governance-licensing) afirma que requiere ID Governance; la [documentación oficial](https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals) lo incluye en P2. Esta guía sigue la oficial.
- **Bloqueo de propiedades de instancia.** Versiones anteriores de la [guía](https://learn.microsoft.com/en-us/entra/identity-platform/howto-configure-app-instance-property-locks) decían que aplicaba solo a apps multitenant o creadas en el portal; la vigente (2 de octubre de 2026) lo aplica a single-tenant y multitenant.
- **Tenant Governance.** Según fuentes comunitarias, sus APIs de Graph seguían en beta y el descubrimiento de tenants relacionados es una acción de un solo sentido ([anuncio de GA](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638), [transición desde Microsoft365DSC](https://github.com/Microsoft365DSC/Microsoft365DSC/blob/Dev/docs/docs/blog/2026/utcm-transition/utcm-transition.md)): pruébalo primero sobre recursos no críticos.
- **Fecha de Agent ID en Copilot Studio.** La [página en inglés](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities) dice mayo de 2026; [versiones localizadas anteriores](https://learn.microsoft.com/bs-latn-ba/microsoft-copilot-studio/admin-use-entra-agent-identities) dicen julio de 2026 y que desde entonces no hay opt-out.
- **Licencia de ID Protection para agentes.** «Pronto requerirá Agent 365» ([riesgo de agentes](https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents)) frente a «Entra ID P2 durante la vista previa» ([administración de agentes](https://learn.microsoft.com/es-es/entra/agent-id/manage-agent-identities-admin)) frente a la [descripción de servicio de Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365), que la ubica en E7 o Agent 365.
- **Licencia del Identity Risk Management Agent.** Su [página](https://learn.microsoft.com/en-us/entra/id-protection/identity-risk-management-agent-get-started) pide Entra ID P2; el [catálogo de agentes de Entra](https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents) indica «Microsoft Entra Agent ID».
- **Licencia del acceso condicional para agentes.** Una versión anterior de la [página](https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id) pedía P1 o P2 más Agent 365 por usuario, con un «enforcement coming soon»; la vigente (30 de septiembre de 2026) pide E7, o Agent 365 más P1 o E3.
- **Agente de optimización de acceso condicional.** La misma página de [configuración](https://learn.microsoft.com/en-us/entra/security-copilot/conditional-access-agent-optimization-settings) dice que las ejecuciones por actividad ocurren como máximo cada seis horas y luego describe un enfriamiento de cuatro horas.
- **Páginas localizadas desactualizadas.** La versión eu-es de [gobernanza de identidades de agente](https://learn.microsoft.com/eu-es/entra/id-governance/agent-id-governance-overview) aún dice vista previa o Frontier, y varias páginas en español de Agent ID, MCP, Foundry y Copilot Studio son traducciones automáticas: prevalece la versión en inglés.
- **Licenciamiento de Workload ID Premium.** La [FAQ](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-faqs) dice que hay que licenciar cada identidad elegible y, a la vez, que una licencia en el tenant desbloquea las funciones para todas: distingue la habilitación técnica del cumplimiento contractual y confírmalo con tu equipo de cuenta.
- **Fecha de EntraIdSignInEvents.** Versiones localizadas antiguas daban el 9 de diciembre de 2025 para el reemplazo de AADSignInEventsBeta; la versión en inglés vigente dice 19 de octubre de 2026 ([tabla](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-entraidsigninevents-table)).
- **App governance en MCSA.** No está disponible si la dirección de facturación está en México (ni en Singapur, Polonia, Italia, Qatar, Israel, España o Taiwán), según la [guía de activación](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-get-started) y la [FAQ](https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-faq); confirma con tu equipo de cuenta la situación de cada país de la región.
- **Infraestructura como código.** La investigación no verificó guías oficiales vigentes de Terraform o Bicep para Entra; el módulo [A3](03_Nivel_3_Avanzado.md#a3) se apoya en Microsoft Graph, Tenant Governance, Microsoft365DSC y Maester. Tampoco encontró libros sobre Entra actualizados a 2026.
- **Estados por confirmar tras Ignite.** Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa y licencias de Agent 365, ID Protection para agentes, CAE universal, Hard Deletion Protection y las alertas de salud. El [laboratorio 3B](https://github.com/MicrosoftLearning/mslearn-sec-identity/blob/master/Instructions/Labs/Supplemental_Lab-3B-Secure-Entra-AgentID.md) es un trabajo en curso con pasos válidos al 30 de junio de 2026, y el [TechLab de Entra Suite](https://github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation/) está pensado para un formato interno: úsalo como guion en tu tenant de prueba.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

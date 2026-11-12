# Comunidad · Referentes, canales y cómo mantenerse al día

*Microsoft Purview Insider Risk Management Ninja Training · Edición 2026*

[← Nivel 4 · Operación](04_Nivel_4_Operacion.md) · [Índice del programa](README.md) · [Evaluaciones y respuestas →](06_Evaluaciones_y_respuestas.md)

<a id="comunidad"></a>

Referentes, canales, libros y recursos en español, y una rutina para seguir los cambios de Insider Risk Management en fuentes oficiales.

*Transversal · 2 módulos · ~4 horas · 10 recursos*

**Módulos de este nivel:** [C1 Referentes y libros](#c1) · [C2 Español y actualización](#c2)

<a id="c1"></a>

## C1 · Referentes, canales y libros

*Transversal · ~2 h · Origen: Nuevo en esta edición*

Detrás de IRM hay un equipo de producto que publica con frecuencia: el blog de seguridad de Microsoft (con un archivo dedicado a Insider Risk Management), los anuncios de Tech Community, los episodios de Microsoft Mechanics y las sesiones del Virtual Ninja Show. A eso se suman MVP y empleados de Microsoft que enseñan el producto con escenarios reales: cómo lograr la primera señal, Protección adaptativa para el SOC, protección de Copilot con DLP e IRM y preparación para SC-401. La lista verificada de referentes aparece en esta sección y en el libro de Excel.

Para el marco conceptual, dos lecturas agnósticas de la herramienta valen tanto como cualquier libro de producto: la guía de CISA y la Common Sense Guide de SEI/CERT. El libro de Peter Rising sobre administración de seguridad, cumplimiento e identidad en Microsoft 365 (Packt, 2023) incluye un capítulo de riesgo interno, aunque usa nombres anteriores como Azure AD (hoy Entra ID) y no cubre agentes ni el Triage Agent.

**Por qué importa**

Los cambios de IRM se explican primero en blogs, podcasts y videos del equipo de producto y de la comunidad, mucho antes de llegar a un libro. Seguir pocas fuentes buenas reduce el tiempo de actualización y ayuda a contrastar los anuncios con lo que funciona en un tenant.

**Qué vas a lograr**

- Elegir tres fuentes oficiales y dos de la comunidad para seguir de forma regular.
- Distinguir contenido oficial, de empleados de Microsoft, de MVP y de la comunidad.
- Usar marcos agnósticos de la herramienta para contrastar decisiones de producto.

> **Consejo Ninja.** El archivo de Insider Risk Management del [blog de seguridad de Microsoft](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-insider-risk-management/) reúne los resúmenes mensuales de novedades y análisis de amenazas internas; el índice de episodios de [M365.FM](https://www.m365.fm/entity/insider-risk-management/) y el blog [EzCloudInfo](https://ezcloudinfo.com/) de Sathish Veerapandian (MVP de Security) publican escenarios prácticos, como la investigación del uso riesgoso de Microsoft 365 Copilot con IRM (octubre de 2026).

> **Atención.** El libro de Peter Rising ([Packt, 2023](https://www.oreilly.com/library/view/microsoft-365-security/9781804611920/)) usa nombres anteriores —Azure AD (hoy Entra ID), Microsoft 365 Defender (hoy Defender XDR), portal de cumplimiento— y no cubre agentes ni el Triage Agent: úsalo para conceptos, no para pantallas.

**¿Tienes poco tiempo?**

- [Microsoft Purview Insider Risk Management Archives | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-insider-risk-management/) · Blog oficial
- [Microsoft Purview Insider Risk Management (M365.FM)](https://www.m365.fm/entity/insider-risk-management/) · Podcast
- [Common Sense Guide to Mitigating Insider Threats, Seventh Edition](https://www.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/) · Documentación

### Directorio de referentes verificados

- **Erin Miyake** (Empleado de Microsoft): Principal Product Manager de Microsoft Purview; explica Protección adaptativa y su integración con Acceso condicional de Entra. [YouTube](https://www.youtube.com/watch?v=C9jXvvZqVyI) · [Evidencia de rol](https://www.youtube.com/watch?v=C9jXvvZqVyI)
- **Jeremy Chapman** (Empleado de Microsoft): Conductor de Microsoft Mechanics; demos oficiales de IRM, agentes de triage y protección de Copilot con Purview. [YouTube](https://www.youtube.com/watch?v=Ynkfu8OF0wQ) · [Evidencia de rol](https://techcommunity.microsoft.com/event/microsoft-copilot-events/prevent-data-loss-and-insider-risks-for-microsoft-365-copilot-with-microsoft-pur/4420208)
- **Maayan Magenheim** (Empleado de Microsoft): Experta de producto en la integración de IRM con Defender XDR (contexto de seguridad de datos para el SOC). [Evidencia de rol](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management)
- **Michelle Slotwinski** (Empleado de Microsoft): Equipo de producto de IRM; autora del anuncio de la experiencia unificada de alertas (jun-2026). [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714)
- **Nathalia Borges** (Empleado de Microsoft): Marketing de producto de seguridad de datos de Purview; anuncios de IRM en Defender XDR (2024) y de los agentes de triage (2025). [Otro](https://techcommunity.microsoft.com/discussions/microsoft-security/new-blog--empower-multiple-teams-and-prioritize-investigations-with-insider-risk/4134970) · [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoft-security-blog/announcing-alert-triage-agents-in-microsoft-purview-powered-by-security-copilot/4396041)
- **Patrick David** (Empleado de Microsoft, Estados Unidos): Principal Product Manager de Microsoft (CxE CAT Compliance) desde mar-2025; actualizó el Ninja oficial de IRM en 2023 (certificado 'Ninja Cat' no oficial) y presenta los agentes de triage de DLP e IRM en sesiones oficiales de skilling. [Otro](https://www.linkedin.com/in/patrick-m-david) · [Evidencia de rol](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/improving-security-posture-management-with-copilot-for-security-innovations)
- **Ryan John Murphy** (Empleado de Microsoft, Reino Unido): Senior AI Data Security Consultant en Microsoft (desde dic-2023) y ex-MVP; autor de un libro de eDiscovery y co-conductor del podcast 'All Things M365 Compliance' (Purview, riesgo interno, eDiscovery); difunde las actualizaciones del Ninja de IRM. [Blog](https://msftcompliance.com) · [Otro](https://mvp.microsoft.com/zh-TW/activities/298127) · [Evidencia de rol](https://uk.linkedin.com/in/ryanjmurphym365consultant)
- **Sravan Kumar Mera** (Empleado de Microsoft): Experto de producto que co-presentó la integración de IRM en Defender XDR (incidentes, caza y página de usuario). [Evidencia de rol](https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management)
- **Alan Cox** (MVP de Microsoft, Estados Unidos): MVP (según su perfil público y M365.FM) enfocado en Microsoft 365, Purview y Copilot; explica cómo proteger Copilot con DLP e IRM y publica el boletín Microsoft 365 Digest. Estatus MVP no confirmado en el directorio oficial: verificar antes de citar. [Otro](https://www.linkedin.com/in/alancox-mvp) · [Evidencia de rol](https://www.m365.fm/show/episodes/protecting-microsoft-copilot-with-purview-dlp-insider-risk-with-alan-cox-mvp/)
- **Charbel Nemnom** (MVP de Microsoft): MVP/MCT de seguridad en la nube; guía de estudio SC-401 actualizada con experiencia real del examen. [Evidencia de rol](https://charbelnemnom.com/sc-401-exam-study-guide/)
- **Jorge Castañeda** (MVP de Microsoft, Perú): MVP de Security (SIEM & XDR) en español: Defender XDR, Sentinel, Purview, priorización de CVEs y laboratorios; fundador de MUG Perú. Reutilizado del catálogo verificado de comunidad; referente hispanohablante para el track C2. [Blog](https://blog.d3fend.me/) · [Otro](https://blog.d3fend.me/about/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5000594)
- **Mirko Peters** (MVP de Microsoft, Alemania): MVP (categoría M365, área Microsoft 365 Copilot) y anfitrión de M365.FM; publica guías de Insider Risk Management con versiones en español traducidas con IA, útiles como lectura introductoria (contrastar siempre con Microsoft Learn). [Blog](https://www.m365.fm/community/u/mirko-p/) · [Otro](https://www.m365.fm/press/) · [Evidencia de rol](https://mvp.microsoft.com/de-DE/mvp/profile/9b0ca797-db5a-493a-a845-8b9158046cf5)
- **Nikki Chapple** (MVP de Microsoft, Reino Unido): Doble MVP (Microsoft 365 y Security) enfocada en Purview (DLP, etiquetas, riesgo interno, DSPM) y preparación para Copilot; co-conduce 'All Things M365 Compliance'. [Blog](https://nikkichapple.com/) · [Otro](https://www.linkedin.com/in/nikkichapple/) · [Evidencia de rol](https://techcommunity.microsoft.com/discussions/azurepurview/purview-youtube-show-and-podcast/4457587)
- **Peter Rising** (MVP de Microsoft, Reino Unido): MVP de Security (área Microsoft Purview, 6 años en el programa según el directorio MVP); autor de un libro de administración de seguridad y cumplimiento de Microsoft 365 con capítulo de riesgo interno; entrevistado en M365.FM sobre Purview para Copilot (jun-2026). [Otro](https://www.oreilly.com/library/view/microsoft-365-security/9781804611920/) · [Evidencia de rol](https://mvp.microsoft.com/de-de/PublicProfile/5004008)
- **Sathish Veerapandian** (MVP de Microsoft, Países Bajos): MVP de Security (13 años en el programa) muy activo en IRM: bases para la primera señal, Protección adaptativa para el SOC y uso riesgoso de Copilot. [Blog](https://ezcloudinfo.com/) · [YouTube](https://www.youtube.com/watch?v=-SWX3R2ECPA) · [Otro](https://mvp.microsoft.com/en-us/PublicProfile/5001105) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5001105)
- **Talhah Mir** (Comunidad, Estados Unidos): Fundador de Insider Risk Management en Microsoft: lideró el programa interno de amenazas internas (2017-2018) y fue Partner GM de Purview Data Security (nov-2018 a ago-2026); desde sep-2026 es SVP de Producto en Salesforce. Su contenido histórico sigue explicando bien el 'por qué' de IRM. [Otro](https://microsoftmechanics.libsyn.com/podcast/introducing-microsoft-purview-alert-triage-agents-for-data-loss-prevention-insider-risk-management) · [Evidencia de rol](https://www.linkedin.com/in/talhahm)

### Webinars, videos y podcasts

- [Microsoft Purview Insider Risk Management (M365.FM)](https://www.m365.fm/entity/insider-risk-management/) · Podcast · Comunidad · Nuevo · Mirko Peters · M365.FM · 2 nov 2026. Índice de episodios de podcast/video sobre IRM (despliegue responsable, explicación simple, Copilot + DLP + IRM con un MVP) actualizado a nov-2026.

### Comunidad: blogs, libros, newsletters y eventos

- [EzCloudInfo (blog de Sathish Veerapandian)](https://ezcloudinfo.com/) · Blog · MVP · Nuevo · Sathish Veerapandian · EzCloudInfo · 26 oct 2026. Blog práctico de un MVP de Security con guías recientes de Purview, IRM y seguridad de IA, como la investigación de uso riesgoso de Microsoft 365 Copilot con IRM (oct-2026).
- [Microsoft 365 Security, Compliance, and Identity Administration (Packt)](https://www.oreilly.com/library/view/microsoft-365-security/9781804611920/) · Libro · MVP · Legado aún útil · Peter Rising · Packt Publishing · ago 2023. Libro de referencia (630 páginas) que incluye un capítulo sobre gestión de soluciones de riesgo interno en Microsoft 365. *Nota:* Edición 2023: usa nombres antiguos (Azure AD, Microsoft 365 Defender, portal de cumplimiento); no cubre agentes ni Triage Agent

**Manos a la obra**

1. Elige tres fuentes oficiales (blog de seguridad de Microsoft, Centro de mensajes y Microsoft Mechanics) y dos de la comunidad de la lista de referentes, y suscríbete. Evidencia: lista con la frecuencia de revisión de cada una.
2. Lee la práctica 22 de la [Common Sense Guide de SEI/CERT](https://www.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/) («aprender de incidentes pasados») y conviértela en una pregunta fija de tu revisión mensual de casos.
3. Escucha un episodio de [M365.FM sobre IRM](https://www.m365.fm/entity/insider-risk-management/) y anota una idea para tu laboratorio y una afirmación que debas contrastar con Learn.

**¿Quieres profundizar?**

- [EzCloudInfo (blog de Sathish Veerapandian)](https://ezcloudinfo.com/) · Blog

<a id="c2"></a>

## C2 · Recursos en español y cómo mantenerse actualizado

*Transversal · ~2 h · Origen: Nuevo en esta edición*

En español tienes la ruta oficial de SC-401 sobre IRM, la página de introducción, la guía de configuración inicial (con la cláusula de responsabilidad legal, útil para circular entre RR. HH. y Legal), la guía del Triage Agent y la matriz de permisos. Son traducciones automáticas: la solución aparece como «Administración de riesgos internos» y conviene contrastar fechas y estados con la versión en inglés. En la comunidad hispanohablante destacan las guías de Mirko Peters en M365.FM (traducidas con IA) y el trabajo de Jorge Castañeda, MVP de Security en Perú.

Para mantenerte al día, define una rutina mensual de 30 minutos: la página de novedades de Purview, los avisos del Centro de mensajes sobre IRM, el archivo de IRM del blog de seguridad de Microsoft y, después de Microsoft Ignite (17 al 20 de noviembre de 2026), una revisión de los estados de vista previa de este programa. Registra cada cambio con su fecha y el módulo afectado.

**Por qué importa**

RR. HH., Legal y privacidad deciden mejor cuando leen en su idioma, y un equipo que revisa novedades cada mes no descubre los retiros cuando ya ocurrieron, como pasó con «Alerts (classic)». Una rutina corta y documentada también deja evidencia de diligencia ante auditoría y mantiene alineado el material interno de capacitación con la versión vigente del producto.

**Qué vas a lograr**

- Ubicar los recursos oficiales en español y conocer sus límites de traducción.
- Armar una rutina mensual de actualización con registro de cambios.
- Compartir material en español con RR. HH., Legal y privacidad.

> **Consejo Ninja.** Recursos oficiales en español: [introducción a IRM](https://learn.microsoft.com/es-es/purview/insider-risk-management), [configuración inicial](https://learn.microsoft.com/es-es/purview/insider-risk-management-configure), [Triage Agent](https://learn.microsoft.com/es-es/purview/copilot-in-purview-triage-irm-agent-get-started), [permisos](https://learn.microsoft.com/es-es/purview/insider-risk-management-permissions) y la [ruta de SC-401](https://learn.microsoft.com/es-es/training/paths/purview-implement-insider-risk-management/). Son traducciones automáticas («Administración de riesgos internos»): contrasta fechas y estados con la versión en inglés.

> **Consejo Ninja.** En la comunidad hispanohablante, las guías de [Mirko Peters en M365.FM](https://www.m365.fm/es/community/u/mirko-p/blog/a-step-by-step-guide-to-implementing-microsoft-purview-insider-risk-management/) (traducidas con IA) y el blog de [Jorge Castañeda](https://blog.d3fend.me/), MVP de Security en Perú, son buenos puntos de partida; verifica siempre contra Learn antes de aplicar una recomendación.

**¿Tienes poco tiempo?**

- [Implementar y administrar Administración de riesgos internos de Microsoft Purview (SC-401)](https://learn.microsoft.com/es-es/training/paths/purview-implement-insider-risk-management/) · Curso
- [Más información sobre Insider Risk Management](https://learn.microsoft.com/es-es/purview/insider-risk-management) · Documentación
- [Introducción al agente de Microsoft Purview Triage en Insider Risk Management](https://learn.microsoft.com/es-es/purview/copilot-in-purview-triage-irm-agent-get-started) · Documentación
- [Introducción a Insider Risk Management](https://learn.microsoft.com/es-es/purview/insider-risk-management-configure) · Documentación

### Documentación, cursos y credenciales

- [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) · Documentación · Oficial · Nuevo · Microsoft Learn · oct 2026. Registro mensual oficial de novedades de Purview; incluye entradas de IRM como la experiencia unificada de alertas y notas en alertas/casos (julio 2026).
- [Implementar y administrar Administración de riesgos internos de Microsoft Purview (SC-401)](https://learn.microsoft.com/es-es/training/paths/purview-implement-insider-risk-management/) · Curso · Oficial · ES · Microsoft Learn (es-es). Versión en español de la ruta oficial de IRM (5 módulos, ~4 h) para equipos de RR. HH., Legal y Seguridad hispanohablantes.
- [Introducción al agente de Microsoft Purview Triage en Insider Risk Management](https://learn.microsoft.com/es-es/purview/copilot-in-purview-triage-irm-agent-get-started) · Documentación · Oficial · ES · Microsoft Learn (es-es). Versión en español (traducción automática) de la guía de despliegue del agente de triage de IRM, útil para equipos hispanohablantes.
- [Asignación de permisos en Insider Risk Management](https://learn.microsoft.com/es-es/purview/insider-risk-management-permissions) · Documentación · Oficial · ES · Microsoft Learn (es-es). Versión en español de la matriz de grupos de roles de IRM, útil para acordar separación de funciones con RR. HH., Legal y Seguridad.
- [Más información sobre Insider Risk Management](https://learn.microsoft.com/es-es/purview/insider-risk-management) · Documentación · Oficial · ES · Microsoft Learn (es-es). Versión en español de la página de introducción a IRM con principios, analíticas y flujo de trabajo.
- [Introducción a Insider Risk Management](https://learn.microsoft.com/es-es/purview/insider-risk-management-configure) · Documentación · Oficial · ES · Microsoft Learn (es-es). Versión en español de la guía de configuración inicial, incluida la cláusula de responsabilidad legal del cliente.

### Anuncios y blogs oficiales

- [Microsoft Purview Insider Risk Management Archives | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-insider-risk-management/) · Blog oficial · Oficial · Nuevo · Microsoft Security Blog · 30 jul 2026. Archivo filtrado del Microsoft Security Blog con artículos sobre IRM, incluidos los resúmenes mensuales de novedades y análisis de amenazas internas como empleados falsos.

**Manos a la obra**

1. Arma tu rutina mensual de 30 minutos: [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new), avisos del Centro de mensajes sobre IRM y el [blog de seguridad de Microsoft](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-insider-risk-management/); registra cada cambio con su fecha y el módulo afectado en tu radar.
2. Comparte con RR. HH. y Legal la [ruta de SC-401 en español](https://learn.microsoft.com/es-es/training/paths/purview-implement-insider-risk-management/) y la [guía de configuración inicial en español](https://learn.microsoft.com/es-es/purview/insider-risk-management-configure), y reúne sus dudas para la próxima reunión del comité.
3. Después de Microsoft Ignite (17 al 20 de noviembre de 2026), revisa los estados de vista previa de este programa —Risky Agents, la integración con Defender XDR y la cola unificada— y actualiza tu radar.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

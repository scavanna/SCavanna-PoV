# Práctica y referencias

[Índice del programa](README.md)


<a id="comunidad"></a>

## Comunidad


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

<a id="evaluaciones-y-respuestas"></a>

## Evaluaciones y respuestas


<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos con privacidad por diseño

**1. ¿Cuál de estas combinaciones **no** otorga derechos de uso de Insider Risk Management?**

- a) Microsoft 365 E5
- b) Microsoft 365 E3 con Microsoft Purview Suite (antes E5 Compliance)
- c) Microsoft 365 E3 con el complemento Microsoft 365 E5 Insider Risk Management
- d) Microsoft 365 E3 con Microsoft Defender Suite (antes E5 Security)  ✅

*Respuesta: d).* Defender Suite incluye Defender for Endpoint P2, Defender for Office 365 P2, Defender for Identity, Defender for Cloud Apps y Entra ID P2, pero no IRM; IRM viene en E5, en Purview Suite o en el complemento de IRM. [Fuente](https://www.hbs.net/blog/microsoft-365-security-smbs) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**2. ¿Qué cambió el 1 de octubre de 2025 con Microsoft 365 E5 Compliance?**

- a) Pasó a llamarse Microsoft Purview Suite, sin cambios de servicio, funcionalidad ni precio  ✅
- b) Se fusionó con Microsoft Defender Suite en un único SKU de seguridad y cumplimiento
- c) Pasó a incluir Microsoft 365 Copilot y subió de precio para los clientes nuevos
- d) Dejó de requerir Microsoft 365 E3 como base y se vende como plan independiente

*Respuesta: a).* Es un cambio de nombre: Purview Suite mantiene el servicio y el precio (USD 12 por usuario al mes con pago anual) y sigue requiriendo Microsoft 365 E3 u Office 365 E3 más EMS E3. [Fuente](https://www.microsoft.com/en-us/security/pricing-overview) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. Vas a practicar con una prueba de Microsoft 365 E5 en un tenant nuevo no administrado. ¿Qué debes verificar antes de crear políticas de IRM?**

- a) Que haya SCU de Security Copilot aprovisionadas, porque IRM las usa para puntuar el riesgo
- b) Que el registro de auditoría unificado esté activo, porque en esos tenants puede venir apagado  ✅
- c) Que la solución de IRM de Sentinel esté instalada, porque IRM guarda allí sus alertas
- d) Que la seudonimización esté desactivada, porque impide que las políticas generen alertas

*Respuesta: b).* IRM usa el registro de auditoría para sus políticas y analíticas; en tenants no administrados con pruebas gratuitas puede no venir activado, y activarlo tarda hasta 60 minutos. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**4. Desde julio de 2026, ¿qué admiten las asignaciones a grupos de roles de Purview?**

- a) Aprobación obligatoria de dos administradores para cualquier grupo de roles de Purview
- b) Asignación exclusiva mediante unidades administrativas, sin asignaciones a todo el tenant
- c) Fecha de vencimiento de 1 día a 2 años, salvo eDiscovery Administrator y eDiscovery Manager  ✅
- d) Herencia automática desde los roles de Entra ID, sin necesidad de una asignación explícita

*Respuesta: c).* La novedad de julio de 2026 permite dar acceso temporal, por ejemplo a investigadores, con vencimiento de 1 día a 2 años. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**5. ¿Qué examen cubre hoy Insider Risk Management dentro de su dominio «Manage risks, alerts, and activities»?**

- a) SC-400
- b) SC-200
- c) MS-102
- d) SC-401  ✅

*Respuesta: d).* SC-401 reemplazó a SC-400 (retirado el 31 de mayo de 2025); su guía de estudio se actualizó el 28 de octubre de 2026 y ese dominio pesa entre 30 y 35 %. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**6. Según Microsoft, ¿quién es responsable de que el uso de IRM cumpla la ley aplicable?**

- a) Microsoft, porque la herramienta seudonimiza a los usuarios por defecto
- b) El cliente, que además debe hacer su propia investigación sin basarse solo en IRM  ✅
- c) El revendedor que vendió la licencia y configuró el tenant inicial
- d) La autoridad de protección de datos del país donde está hospedado el tenant

*Respuesta: b).* La guía de inicio aclara que el cliente es el único responsable y que no debe basarse solo en las conclusiones de IRM; por eso se involucra a Legal, RR. HH. y privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. ¿En qué estado vienen los indicadores globales de IRM al empezar?**

- a) Todos desactivados; hay que activar al menos uno para crear una política  ✅
- b) Todos activados, incluidos los de pago por uso, hasta que alguien los apague
- c) Solo los de dispositivo activados; los de Office se activan al crear una política
- d) Activados según la plantilla elegida, sin posibilidad de cambiarlos globalmente

*Respuesta: a).* Es parte de la privacidad por diseño: nada se recolecta hasta que alguien decide activar indicadores. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**8. ¿Cuál de estos indicadores requiere activar el pago por uso?**

- a) Indicadores de Office, como descargas y uso compartido en SharePoint
- b) Interacciones de los usuarios con Microsoft 365 Copilot en sus aplicaciones
- c) Almacenamiento en la nube de terceros, como Box, Dropbox o Google Drive  ✅
- d) Booster de riesgo por pertenencia a un grupo de usuarios prioritarios

*Respuesta: c).* Los indicadores de nube, red de terceros, Fabric y varias experiencias de IA son de pago por uso; Microsoft 365 Copilot no genera cargo de pago por uso. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. ¿Cuál es un límite real del conector de RR. HH.?**

- a) Solo acepta renuncias; los cambios de nivel y las evaluaciones requieren otro conector
- b) Requiere el rol Global Administrator en cada carga, además de la app registrada en Entra
- c) Admite hasta 5.000 registros por archivo, cargados solo de forma manual desde el portal
- d) Hasta 500 registros por CSV en cada carga; los perfiles sin actualizar se borran a los 30 días  ✅

*Respuesta: d).* La guía (30 de marzo de 2026) fija 500 registros por CSV, la ventana de LastWorkingDate, el rol Data Connector Admin y el borrado de los perfiles sin actualizar a los 30 días. [Fuente](https://learn.microsoft.com/en-us/purview/import-hr-data) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**10. ¿Qué acepta el conector Insider Risk Indicators (vista previa)?**

- a) Señales crudas de cualquier SIEM, que IRM agrega y normaliza por su cuenta
- b) Detecciones de terceros ya agregadas y procesadas, por ejemplo desde Sentinel o Splunk  ✅
- c) Solo datos de RR. HH. en CSV, como alternativa al conector de RR. HH.
- d) Registros de historias clínicas exportados desde un sistema de salud

*Respuesta: b).* Importa detecciones agregadas para usarlas como disparadores o indicadores personalizados; no acepta señales crudas. [Fuente](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**11. Según MC1430536, ¿qué se retira con la experiencia unificada de alertas?**

- a) La seudonimización de los nombres en la cola de alertas
- b) Los casos, que pasan a gestionarse dentro de la cola
- c) La pestaña «Alerts (classic)» y Alert Spotlight  ✅
- d) El Triage Agent, que se reemplaza por reglas de prioridad

*Respuesta: c).* «Alerts (classic)» se deprecó el 1 de octubre de 2026 en la nube comercial (el 31 de octubre en gobierno) y se retiró Alert Spotlight; la privacidad no cambia. [Fuente](https://mc.merill.net/message/MC1430536) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**12. ¿Cuánto tardan, aproximadamente, las primeras alertas después de crear una política?**

- a) Unas 24 horas  ✅
- b) Aparecen de inmediato
- c) 7 días
- d) 30 días

*Respuesta: a).* La guía de inicio indica que las alertas comienzan unas 24 horas después de crear la política; las analíticas tardan hasta 48 horas. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**13. ¿Qué ocurre con el perfil de usuario ampliado (datos de Entra) cuando la seudonimización está activa?**

- a) Muestra todos los datos de Entra
- b) Se envía automáticamente a RR. HH.
- c) Muestra solo el departamento
- d) Queda oculto  ✅

*Respuesta: d).* MC1430534 indica que los detalles ampliados del perfil se ocultan si la seudonimización está activa. [Fuente](https://mc.merill.net/message/MC1430534) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Políticas, investigación y respuesta proporcional

**1. En Data theft by departing users, ¿qué puede reemplazar al conector de RR. HH. como disparador, según la página de plantillas?**

- a) Una alerta DLP de severidad alta
- b) El borrado de la cuenta del usuario en Microsoft Entra  ✅
- c) Una alerta de Defender for Endpoint
- d) Un mensaje detectado por Communication Compliance

*Respuesta: b).* La plantilla permite elegir el borrado de la cuenta en Entra. Ojo: «Get started» lista el conector como requerido, una contradicción documentada en Limitaciones. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Qué alertas DLP **no** se evalúan cuando una política DLP actúa como disparador de Data leaks?**

- a) Las de Exchange Online y SharePoint Online de severidad alta
- b) Las de OneDrive de severidad alta escritas en la auditoría
- c) Las de SharePoint Online y OneDrive de severidad alta
- d) Las de Endpoint DLP, Teams y Microsoft 365 Copilot  ✅

*Respuesta: d).* Solo cuentan las alertas de severidad alta de Exchange Online, SharePoint Online y OneDrive. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. ¿Cuántas políticas DLP puedes asignar como disparador de una política Data leaks?**

- a) Hasta 5
- b) Hasta 10
- c) Hasta 20  ✅
- d) Hasta 100

*Respuesta: c).* Data leaks admite hasta 20 políticas DLP; el límite de 100 corresponde a las políticas por plantilla. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué plantillas permiten personalizar los eventos desencadenantes?**

- a) Data leaks y Data leaks by priority users  ✅
- b) Todas las plantillas
- c) Solo Data theft by departing users
- d) Solo Risky AI usage

*Respuesta: a).* Solo esas dos plantillas permiten elegir indicadores desencadenantes propios en lugar de la alerta DLP. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿Qué necesitas para usar las plantillas Security policy violations?**

- a) El conector de acceso físico y un grupo de activos físicos prioritarios configurado
- b) Defender for Endpoint activo y su integración con IRM habilitada en las funciones avanzadas  ✅
- c) Microsoft 365 E7 y la política Risky Agents activa por defecto en el tenant
- d) El complemento de evidencia forense y el cliente de Purview en cada dispositivo

*Respuesta: b).* Usan alertas de Defender for Endpoint, que se importan a diario según los estados de triage elegidos. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**6. Sobre la evidencia forense, ¿qué afirmación es correcta?**

- a) Viene activada por defecto para todos los usuarios con licencia de IRM
- b) Los clips se conservan mientras el caso siga abierto, sin límite de tiempo
- c) Antes de capturar a un usuario se requiere la aprobación del grupo IRM Approvers  ✅
- d) Funciona en macOS y en Windows siempre que el equipo esté incorporado

*Respuesta: c).* Está desactivada por defecto, usa doble autorización, borra los clips a los 120 días y solo admite Windows 10/11 Enterprise de 64 bits. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué equipo cumple los requisitos de la evidencia forense?**

- a) Windows 11 Enterprise de 64 bits con GPU integrada y el cliente de Microsoft Purview  ✅
- b) Windows 11 Pro de 64 bits con GPU discreta y la extensión de Purview para Edge
- c) macOS en una de sus tres últimas versiones con la extensión de Purview para Chrome
- d) Cualquier VM Windows con 4 GB de RAM, 2 vCPU y el dispositivo incorporado

*Respuesta: a).* Requiere Windows 10/11 Enterprise de 64 bits (incluido Windows 365) con GPU integrada, el cliente de Purview y, en VM, 16 GB de RAM y 8 vCPU. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Qué es cierto sobre el informe de actividad de usuario?**

- a) Cubre hasta 7 días y se genera para todos los usuarios de una política
- b) Está disponible para cualquier administrador global sin roles de IRM
- c) Se genera en tiempo real a partir de la cola unificada de alertas
- d) Requiere el grupo IRM Investigators y cubre hasta 90 días por usuario  ✅

*Respuesta: d).* Los datos llegan unas 48 horas después y el informe tarda hasta 10 horas en generarse. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. Por defecto, ¿cuánto dura un nivel de riesgo interno de Protección adaptativa antes de restablecerse?**

- a) 24 horas, renovables por el analista
- b) 7 días, configurable de 5 a 30  ✅
- c) 30 días fijos, sin opción de cambio
- d) 120 días, igual que la retención de clips

*Respuesta: b).* Tanto la vigencia del nivel como la detección de actividad previa valen 7 días por defecto. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué hace la integración de Protección adaptativa con Data Lifecycle Management?**

- a) Bloquea el acceso a aplicaciones en la nube a los usuarios con nivel Elevated
- b) Aplica etiquetas de confidencialidad al contenido que crea un usuario Elevated
- c) Activa la evidencia forense para los usuarios que alcanzan el nivel Elevated
- d) Preserva durante 120 días el contenido que borra un usuario con nivel Elevated  ✅

*Respuesta: d).* Una política de retención creada automáticamente preserva lo borrado en SharePoint, OneDrive y Exchange (vista previa). [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Dónde aparecen nombres reales (sin seudonimizar) al usar Protección adaptativa?**

- a) En Acceso condicional, en las alertas DLP y en el explorador de actividad  ✅
- b) En ninguna parte: la seudonimización se conserva en todos los productos
- c) Solo en los informes de analíticas, que se exportan con identidades
- d) Solo en el panel de políticas de IRM, visible para los administradores

*Respuesta: a).* La seudonimización de IRM no se conserva en esos lugares; inclúyelo en la evaluación de impacto de privacidad. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿En qué ubicaciones actúa la DLP adaptativa?**

- a) SharePoint y OneDrive
- b) Todas las ubicaciones de DLP
- c) Exchange, Teams y dispositivos  ✅
- d) Solo Power BI

*Respuesta: c).* Aunque la política DLP tenga otras ubicaciones, la Protección adaptativa solo actúa en esas tres. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**13. ¿Qué ocurre con el equipo de Teams de un caso de IRM (vista previa) cuando se resuelve el caso?**

- a) Se elimina con su contenido
- b) Se archiva: queda oculto y de solo lectura  ✅
- c) Se convierte en un equipo público
- d) Se transfiere a RR. HH.

*Respuesta: b).* El equipo privado del caso se archiva al resolverlo, lo que preserva la colaboración sin dejarla activa. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-teams) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. ¿A quién se envían las plantillas de aviso de IRM?**

- a) A todo el departamento del usuario
- b) Al gerente del usuario
- c) Al equipo de RR. HH.
- d) Solo al correo del usuario del caso  ✅

*Respuesta: d).* Los avisos se envían únicamente al usuario del caso y quedan en su historial; su redacción conviene validarla con RR. HH. y Legal. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-notices) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. Cuando un caso de IRM necesita preservación y revisión legal, ¿a qué se escala?**

- a) A eDiscovery (Premium)  ✅
- b) A Communication Compliance
- c) A Compliance Manager
- d) A Defender for Cloud Apps

*Respuesta: a).* El escalamiento a eDiscovery (Premium) permite retener, revisar y exportar con cadena de custodia. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-cases) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, agentes, SOC y automatización

**1. ¿Qué interacción de IA **no** genera cargos de pago por uso en IRM?**

- a) Enterprise AI apps
- b) Microsoft 365 Copilot  ✅
- c) Other AI apps detectadas por el navegador
- d) Copilot experiences con datos que no son de Microsoft 365

*Respuesta: b).* Las interacciones con Microsoft 365 Copilot no tienen cargo de pago por uso; las otras tres opciones sí. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Qué agentes cubre la política Risky Agents?**

- a) Solo agentes de Copilot Studio publicados en Teams
- b) Cualquier agente de terceros, aunque no tenga conector
- c) Copilot Studio, Microsoft Foundry y agentes creados con el SDK P4AI  ✅
- d) Solo agentes registrados en Agent 365 con identidad propia

*Respuesta: c).* Así lo indica la página de monitoreo de agentes (4 de agosto de 2026); MC1200579 suma los agentes de Agent 365. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. Según MC1280556, ¿qué licencia es necesaria para Insider Risk Management para agentes?**

- a) Microsoft 365 E7 o Agent 365  ✅
- b) Microsoft Purview Suite
- c) Microsoft Defender Suite
- d) Microsoft 365 E3

*Respuesta: a).* El aviso marca la disponibilidad general entre junio y julio de 2026 e indica que no está disponible sin E7 o Agent 365; Learn todavía la marca en vista previa. [Fuente](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Qué ve el equipo de IRM cuando un usuario invitado interactúa con un agente monitoreado por Risky Agents?**

- a) El prompt completo y la respuesta del agente, como con empleados
- b) Nada: los invitados quedan fuera de toda política de IRM
- c) El historial de navegación del invitado durante la sesión
- d) Solo indicadores de tipos de información sensible, no el contenido  ✅

*Respuesta: d).* Con invitados, la política solo muestra los indicadores de información sensible; además, las unidades administrativas no admiten alertas de agentes. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Qué ocurre al activar los indicadores de Azure AI Content Safety en IRM?**

- a) Se crea una política de Communication Compliance  ✅
- b) Se desactiva la seudonimización de los prompts
- c) Se crea automáticamente un caso de eDiscovery
- d) Se habilita la evidencia forense del dispositivo

*Respuesta: a).* Esos indicadores se apoyan en una política de Communication Compliance creada para ese fin. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. ¿Qué dato de IRM **todavía no** llega a la integración con Defender XDR?**

- a) El estado de la alerta
- b) La severidad
- c) Los eventos de Risky AI usage  ✅
- d) La clasificación de la alerta

*Respuesta: c).* Tampoco llegan la exfiltración por correo, las apps cloud de terceros, los eventos previos a la alerta ni las exclusiones. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Por qué la integración de IRM con Defender XDR puede romper automatizaciones de Sentinel?**

- a) Porque cambia el esquema de todas las tablas
- b) Porque los incidentes de IRM no contienen alertas  ✅
- c) Porque desactiva el conector de Defender XDR
- d) Porque elimina la seudonimización en Sentinel

*Respuesta: b).* Microsoft recomienda usar el conector de IRM para Sentinel o desactivar el uso compartido de datos. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Qué necesita un analista del SOC para ver alertas de IRM en Defender XDR?**

- a) Global Administrator, que ya incluye el acceso a los datos de IRM en Defender
- b) Solo el grupo IRM Auditors, que exporta los registros de IRM a Defender
- c) Security Administrator más IRM Approvers, que aprueba el uso compartido
- d) Security Operator o Security Reader, más pertenecer a IRM, IRM Analysts o IRM Investigators  ✅

*Respuesta: d).* Además debe estar activado el uso compartido de datos en IRM. [Fuente](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. ¿Qué ocurre con la seudonimización al exportar alertas por la Office 365 Management Activity API?**

- a) Se conserva siempre
- b) No se conserva; la exportación a CSV sí la conserva  ✅
- c) Se conserva solo en alertas de severidad alta
- d) La API no exporta alertas de IRM

*Respuesta: b).* La exportación por API corre cada 60 minutos, está desactivada por defecto y no conserva la seudonimización. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**10. ¿Qué ocurre con el Triage Agent 90 días después de la última vez que se guardó su configuración?**

- a) Se elimina y hay que desplegar una nueva instancia del agente
- b) Pasa a modo manual y solo clasifica alertas a pedido del analista
- c) Deja de ejecutarse hasta que alguien vuelva a guardar su configuración  ✅
- d) Reinicia la ventana de alertas y vuelve a clasificar todo el historial

*Respuesta: c).* El agente corre con el contexto del último usuario que guardó la configuración, y esa autenticación dura 90 días. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. Según Learn, ¿qué necesita el Triage Agent de IRM además de la licencia por usuario de IRM?**

- a) El modelo de pago por uso y SCU de Security Copilot aprovisionadas  ✅
- b) Solo Microsoft 365 E7, que reemplaza la licencia de IRM
- c) El complemento de evidencia forense con capacidad adicional
- d) Una licencia de Microsoft 365 Copilot para cada analista

*Respuesta: a).* También requiere el tenant incorporado a Security Copilot, el uso compartido de datos de Microsoft 365 y el plugin de Purview habilitado. [Fuente](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Cuántas SCU aporta la inclusión de Security Copilot en Microsoft 365 E5 y E7?**

- a) 100 SCU fijas al mes por tenant, sin importar las licencias
- b) 1 SCU por usuario licenciado, sin tope mensual
- c) Ninguna: las SCU siempre se compran aparte por hora
- d) 400 SCU al mes por cada 1.000 licencias pagas, hasta 10.000  ✅

*Respuesta: d).* Se calcula sobre licencias pagas y se despliega gradualmente desde el 18 de noviembre de 2025; un tenant de prueba no la garantiza. [Fuente](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**13. ¿Qué pasa con las plantillas de Power Automate para IRM si la seudonimización está activa?**

- a) Funcionan igual
- b) No funcionan como se espera  ✅
- c) La seudonimización se desactiva automáticamente
- d) Exigen una licencia premium

*Respuesta: b).* La documentación advierte que, con la seudonimización activa, estas plantillas no funcionan como se espera. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-power-automate) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Dónde se pueden usar los indicadores personalizados del conector Insider Risk Indicators?**

- a) En todas las plantillas, incluidas las de agentes
- b) Solo en Risky AI usage y Risky browser usage
- c) Solo en las plantillas Data theft y Data leaks  ✅
- d) Solo en las variantes de Security policy violations

*Respuesta: c).* Además, tras actualizar un indicador hay que esperar 24 horas antes de cargar datos. [Fuente](https://learn.microsoft.com/en-us/purview/import-insider-risk-indicators) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué grupo de roles puede ver las capturas de evidencia forense y el explorador de contenido?**

- a) IRM Analysts
- b) IRM Auditors
- c) IRM Investigators  ✅
- d) IRM Admins

*Respuesta: c).* Solo IRM Investigators accede a las capturas forenses y al explorador de contenido; por eso es el rol más sensible. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Quién aprueba la captura de evidencia forense de un usuario?**

- a) El grupo IRM Approvers  ✅
- b) El administrador global
- c) El propio usuario
- d) El grupo IRM Analysts

*Respuesta: a).* La evidencia forense usa doble autorización: IRM o IRM Admins solicitan e IRM Approvers aprueba. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. ¿Qué notificaciones a administradores ofrece IRM?**

- a) Solo un resumen mensual de alertas, enviado por correo al administrador global del tenant
- b) Avisos por SMS al usuario investigado y a su gerente directo cuando se abre un caso
- c) Ninguna: el equipo debe revisar el portal de Purview cada día para ver alertas nuevas
- d) Primera alerta, resumen diario de alertas altas y resumen semanal de advertencias de políticas  ✅

*Respuesta: d).* Se configuran en los ajustes globales de IRM y evitan depender de que alguien abra el portal. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Qué marco agnóstico de la herramienta organiza un programa de riesgo interno en detectar, evaluar y gestionar, con una edición de 2026?**

- a) La Insider Threat Mitigation Guide de CISA  ✅
- b) La guía de estudio de SC-401
- c) La descripción del servicio de Purview
- d) El Ninja oficial de IRM

*Respuesta: a).* La edición 2026 de la guía de CISA incorpora el trabajo híbrido y la IA y propone un equipo multidisciplinario con gobierno y cultura. [Fuente](https://www.cisa.gov/resources-tools/resources/insider-threat-mitigation-guide) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Cómo calcula el panel de políticas la eficacia de las alertas?**

- a) Alertas activas / alertas totales generadas en los últimos 30 días
- b) Alertas confirmadas / (confirmadas + descartadas) en los últimos 365 días  ✅
- c) Casos cerrados / casos abiertos durante el último trimestre
- d) Alertas de severidad alta / alertas de severidad baja del año

*Respuesta: b).* Se calcula sobre las acciones de los últimos 365 días y sirve para comparar políticas y versiones de una misma política. [Fuente](https://learn.microsoft.com/es-es/purview/insider-risk-management-policies) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Cómo funcionan las analíticas de IRM?**

- a) Requieren crear al menos tres políticas activas antes de ejecutar el primer escaneo
- b) Muestran en tiempo real los nombres de los usuarios más riesgosos de la organización
- c) Escanean a diario hasta 10 días de actividad y entregan resultados agregados y anonimizados  ✅
- d) Solo funcionan con pago por uso y una suscripción de Azure vinculada al tenant

*Respuesta: c).* Permiten estimar el riesgo sin crear políticas y recomiendan umbrales en tiempo real. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Qué riesgo tiene elegir «Fewer alerts» en las detecciones inteligentes?**

- a) Que aumenten los falsos positivos
- b) Que se desactive la seudonimización
- c) Que se borren las alertas existentes
- d) Que se oculten verdaderos positivos  ✅

*Respuesta: d).* «Fewer alerts» puede ocultar verdaderos positivos y «More alerts» sube los falsos positivos: registra y mide cada cambio. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-intelligent-detections) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Qué indicador de los informes de IRM mide de forma directa la agilidad del triage?**

- a) Días promedio en «Needs review»  ✅
- b) Número de políticas por plantilla
- c) Capacidad usada de evidencia forense
- d) Cantidad de indicadores activados

*Respuesta: a).* El informe de alertas muestra los días promedio en «Needs review»; el de casos, los días promedio activos. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-reports) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**9. ¿En cuál de estos casos se conserva la seudonimización de IRM?**

- a) En las alertas DLP generadas por la Protección adaptativa
- b) En la exportación a CSV  ✅
- c) En la exportación por la Office 365 Management Activity API
- d) En el panel del Triage Agent

*Respuesta: b).* La exportación a CSV conserva la seudonimización; la exportación por API, las alertas DLP y el panel del agente muestran nombres. [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. Según el texto de LeyChile citado en este programa, ¿desde cuándo rige la Ley 21.719 de Chile?**

- a) 1 de enero de 2025
- b) 20 de marzo de 2025
- c) 1 de diciembre de 2026  ✅
- d) 26 de mayo de 2026

*Respuesta: c).* Entra en vigencia el 1 de diciembre de 2026 y crea la Agencia de Protección de Datos Personales. El 20 de marzo de 2025 es la publicación de la nueva LFPDPPP de México y el 26 de mayo de 2026, la aprobación de los Estándares Iberoamericanos. Su aplicación a tu caso la define Legal. [Fuente](https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. Si la normativa local lo exige, ¿qué recomienda la guía de planificación de IRM?**

- a) Desactivar IRM en ese país hasta que la autoridad local apruebe expresamente su uso
- b) Usar una única política global sin segmentación, para tratar a todos los usuarios igual
- c) Reemplazar la seudonimización por cifrado de los nombres de usuario en esa región
- d) Usar políticas idénticas separadas por región e investigadores que hablen el idioma de los usuarios  ✅

*Respuesta: d).* La guía también pide involucrar desde el inicio a TI, Cumplimiento, Privacidad, Seguridad, RR. HH. y Legal. [Fuente](https://learn.microsoft.com/es-es/purview/insider-risk-management-plan) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="laboratorio-y-practica"></a>

## Laboratorio y práctica


Este archivo responde tres preguntas para este programa: qué puedes practicar en el entorno de laboratorio, qué requiere producción (y por qué), y cómo hacerlo con riesgo controlado. La guía para construir el entorno con los créditos de Azure de Visual Studio Enterprise y una prueba de Microsoft 365 E5 está en el [anexo común](../Anexo_Entorno_de_practica.md).

**Tu entorno.** Una prueba de Microsoft 365 E5 (25 licencias durante un mes) incluye Insider Risk Management, y la propia guía de inicio la sugiere si no tienes E5 ([Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)); si tu organización parte de Microsoft 365 E3, la [prueba de Microsoft Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) asigna 25 licencias durante 90 días. Suma una suscripción de Azure con los créditos de Visual Studio Enterprise en el **mismo tenant** para lo que se factura por uso —indicadores de nube, OCR, Data Security Investigations— y una VM Windows 11 incorporada para los indicadores de dispositivo y, si la presupuestas, la evidencia forense. El día 0, verifica la auditoría: en tenants de prueba no administrados puede venir apagada ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).

**Personas y datos sintéticos.** Crea cuentas de prueba con nombres evidentes, un CSV de RR. HH. inventado (renuncias y fechas dentro de la ventana permitida), documentos con datos sensibles ficticios y un sitio de SharePoint como contenido prioritario. Nunca uses datos de empleados reales en el laboratorio. Nombra todo con `PRUEBA-IRM-<objetivo>-v<n>-<AAAAMM>`: los nombres de las políticas de IRM no se pueden cambiar después de crearlas.

**Tiempos a planificar.** Las analíticas tardan hasta 48 horas, las primeras alertas unas 24 horas después de crear la política, la configuración rápida de Protección adaptativa hasta 72 horas, el primer análisis del Triage Agent hasta 2 horas y los informes de actividad de usuario hasta 10 horas. Lanza esas tareas al comienzo de cada semana del plan.

**Qué no se puede practicar en el laboratorio.** Semanas de comportamiento real para medir falsos positivos (el ajuste necesita unos 30 días de actividad), datos reales de RR. HH., Patient data misuse con un sistema clínico real, la evidencia forense a escala, las SCU incluidas de Security Copilot (se calculan sobre licencias pagas), Microsoft 365 Copilot (sus licencias no vienen en la prueba E5), los agentes que requieren Microsoft 365 E7 o Agent 365 y los procesos con la representación de los trabajadores. Para esos casos, cada ejercicio describe la forma segura de practicar en producción.

**Costos a vigilar.** Indicadores de pago por uso (nube, red, Fabric e IA que no es de Microsoft 365), OCR, Data Security Investigations, SCU aprovisionadas (USD 4 por SCU y hora, según los [precios de Security Copilot](https://www.microsoft.com/en-us/security/pricing/microsoft-security-copilot/)) y una VM de 16 GB y 8 vCPU para la evidencia forense. No está confirmado que el crédito de Visual Studio cubra los medidores de Purview: configura presupuestos con alertas al 50, 75 y 90 % antes del primer ejercicio y revisa el [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) a las 48 horas de cada prueba.

**Práctica en producción, siempre con aprobaciones.** En riesgo interno, practicar en producción significa monitorear personas. Antes de cualquier política sobre usuarios reales necesitas la aprobación de Legal, RR. HH. y privacidad y, cuando la ley o un contrato colectivo lo exijan, de la representación de los trabajadores. Después: seudonimización activa, políticas de prueba acotadas a un piloto informado, roles de solo lectura para quien no investiga, analíticas agregadas como primer paso, auditoría de las acciones de los investigadores y un plan de reversión (eliminar la política y expirar los niveles de riesgo).

**Limpieza.** Elimina las políticas, los casos y los clips forenses de práctica; borra las investigaciones de Data Security Investigations; elimina la capacidad de SCU; desconecta el conector de RR. HH. y borra el CSV y los secretos de la app; quita los roles temporales y desvincula el pago por uso si no lo vas a seguir usando.

<a id="matriz-laboratorio"></a>

## Matriz de laboratorio y producción

| Capacidad | ¿Laboratorio? | Requisito o limitación | Cómo practicar en producción | Riesgo | Mitigación | Fuente |
|---|---|---|---|---|---|---|
| Configuración base: roles, auditoría y analíticas | Sí | En tenants de prueba no administrados la auditoría viene apagada; activarla tarda hasta 60 min y la analítica hasta 48 h. | Ejecuta el escaneo de analítica, sin directivas, para dimensionar el riesgo antes de crear políticas. | Acceso indebido a información sobre el comportamiento de empleados. | Roles separados (administración, análisis, investigación), seudonimización activa y revisión de accesos. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure) |
| Directivas por plantilla y ventanas de tiempo | Sí | Las alertas llegan unas 24 h después de crear la directiva; ventana de activación de 1-30 días y detección previa de 0-90 días (10 para correo). | Directiva de fuga de datos con alcance a un grupo piloto aprobado y umbrales por defecto. | Monitorear empleados sin base legal ni aviso. | Aprobación de Legal, Privacidad y RR. HH., aviso según la normativa local y alcance mínimo. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-timeframes) |
| Conector de RR. HH. por CSV | Sí | CSV con UserPrincipalName, ResignationDate y LastWorkingDate (ISO 8601), hasta 500 registros por archivo, app de Entra, rol Data Connector Admin y acceso a webhook.ingestion.office.com. | Carga datos reales solo con acuerdo formal con RR. HH. y columnas mínimas. | Exportar datos de personal sensibles como desempeño o renuncias. | Minimización, transferencia cifrada, borrado del CSV tras la carga y secreto en Key Vault. | [Fuente](https://learn.microsoft.com/en-us/purview/import-hr-data) |
| Indicadores de dispositivo y navegador | Sí | Requiere un Windows incorporado y la extensión de navegador para señales de navegación. | Incorpora equipos de un grupo piloto voluntario e informado. | Captura excesiva de actividad personal. | Solo los indicadores necesarios, exclusiones globales y revisión de privacidad. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-browser-support) |
| Evidencia forense (capturas de pantalla) | Parcial | Requiere el cliente de Microsoft Purview en el equipo, aprobación por usuario y capacidad facturable. | Solo para usuarios concretos con solicitud aprobada por Legal y RR. HH. | Capturar datos personales de terceros en pantalla. | Flujo de aprobación con el rol de aprobadores, retención mínima y acceso restringido. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence-manage) |
| Seudonimización y exportación de alertas | Sí | La seudonimización viene activa por defecto; la exportación por API hacia SIEM no la conserva. | Mantén la seudonimización y revela identidades solo al escalar a caso. | Filtrar identidades al exportar alertas a Sentinel. | Evalúa la exportación con Privacidad y limita el acceso al área de trabajo. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-share-data) |
| Indicadores de nube de terceros y Fabric | Parcial | Se facturan por unidades de procesamiento (una por 10.000 actividades) y exigen pago por uso y conexión de apps en Defender. | Activa un solo indicador con alcance piloto y presupuesto. | Costos variables difíciles de prever. | Presupuesto y alertas de Azure y revisión semanal del Usage center. | [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) |
| Riesgo interno en el uso de IA y agentes | Parcial | Requiere Copilot o apps de IA con pago por uso; la cobertura de agentes depende de E7 o Agent 365. | Directiva de uso riesgoso de IA con alcance piloto. | Capturar prompts con datos personales. | Seudonimización, acceso mínimo y retención acotada. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents) |
| Agente de triage de Insider Risk | Parcial | Consume SCU y requiere pago por uso; su panel no seudonimiza nombres en las alertas priorizadas. | Actívalo solo para analistas autorizados y mide el consumo. | Exponer identidades pese a la seudonimización. | Restricción de roles y revisión de Privacidad antes de habilitarlo. | [Fuente](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy) |
| Investigación con Data Security Investigations desde un caso | Parcial | Pago por uso (GB almacenados y unidades de cómputo) con suscripción de Azure en el mismo tenant. | Alcance de 1-2 buzones de prueba con estimador de costos previo. | Costos y copia de contenido sensible fuera del flujo normal. | Presupuesto con alertas al 50/75/90 % y borrado de la investigación al terminar. | [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) |

## Principios para practicar en producción

1. **Primero observar, después actuar.** Usa los modos de solo informe, auditoría o simulación antes de cualquier bloqueo o acción automática.
2. **Alcance mínimo.** Grupos piloto, usuarios y dispositivos de prueba etiquetados, unidades administrativas y ámbitos adaptables pequeños.
3. **Privilegio justo a tiempo.** Roles de solo lectura para estudiar y activación con PIM, aprobación y justificación para cambiar.
4. **Cuentas de emergencia excluidas y monitoreadas.** Nunca practiques acceso condicional o protección de identidad sin cuentas de emergencia probadas.
5. **Cambio registrado y reversible.** Cada práctica tiene responsable, ventana, criterio de éxito, plan de reversión y limpieza al terminar.
6. **Privacidad y áreas de negocio.** Para riesgo interno, comunicaciones o eDiscovery, acuerda con RR. HH., Legal y privacidad antes de crear políticas, aunque sean de prueba.

<a id="ejercicios"></a>

## Índice de ejercicios

Resumen: Laboratorio: 54, Laboratorio parcial: 19, Solo producción: 16, Sin etiqueta: 6.

| Módulo | N.º | Entorno | Ejercicio |
|---|---|---|---|
| [P0](01_Nivel_1_Inicial.md#p0) | 1 | Laboratorio | En tu prueba de Microsoft 365 E5, verifica en el portal de Purview si el registro de auditoría unificado está activo; si no lo está, actívalo siguiendo la guía oficial y anota la hora. Evidencia: captura del estado… |
| [P0](01_Nivel_1_Inicial.md#p0) | 2 | Laboratorio | Crea cuatro cuentas de prueba y asígnales los grupos IRM Admins, IRM Analysts, IRM Investigators e IRM Approvers con fecha de vencimiento (permisos de IRM). Comprueba que una cuenta con Global Administrator y sin rol… |
| [P0](01_Nivel_1_Inicial.md#p0) | 3 | Laboratorio | Define la convención de nombres `PRUEBA-IRM-<objetivo>-v<n>-<AAAAMM>` para políticas, grupos, casos y conectores, y regístrala en un documento de cambios: los nombres de las políticas de IRM no se pueden cambiar… |
| [P0](01_Nivel_1_Inicial.md#p0) | 4 | Laboratorio | Recorre los ajustes globales de IRM (privacidad, indicadores, ventanas de política, detecciones inteligentes, notificaciones y exclusiones globales) y documenta el valor por defecto de cada uno antes de tocar nada… |
| [P0](01_Nivel_1_Inicial.md#p0) | 5 | Solo producción | Inventaría quién tiene hoy acceso a IRM en producción, incluidos los roles de Entra que lo otorgan y los grupos de roles de Purview. Cómo hacerlo seguro: revisión de solo lectura con un rol de auditor, sin cambios… |
| [I0](01_Nivel_1_Inicial.md#i0) | 1 | Laboratorio | Descarga la guía de estudio de SC-401 y arma una matriz habilidad medida → módulo de este programa para el dominio de riesgo interno. Evidencia: hoja de cálculo con cada habilidad cubierta y las brechas que detectes. |
| [I0](01_Nivel_1_Inicial.md#i0) | 2 | Laboratorio | Completa el módulo Understand Microsoft Purview Insider Risk Management (28 minutos) y el ejercicio guiado «Investigate potential data theft using Insider Risk Management» de la ruta oficial. Evidencia: progreso o… |
| [I0](01_Nivel_1_Inicial.md#i0) | 3 | Laboratorio | Crea tu radar de novedades: guarda What's new in Microsoft Purview en favoritos y registra en una tabla tres avisos del Centro de mensajes —MC1430536, MC1438568 y MC1200579— con fecha, impacto y módulo afectado.… |
| [I0](01_Nivel_1_Inicial.md#i0) | 4 | Laboratorio | Mira el episodio 8 de la serie SC-401 y anota cinco conceptos que vas a configurar en I2: indicadores, RBAC, conectores, privacidad y Protección adaptativa. Evidencia: nota de una página con una pregunta abierta por… |
| [I1](01_Nivel_1_Inicial.md#i1) | 1 | Laboratorio | Arma un mapa de licencias para tres poblaciones de tu organización (usuarios con E5, con E3 y de primera línea): qué plan les da IRM —E5, Purview Suite o el complemento de IRM— y cuál no (E3 sola, Defender Suite),… |
| [I1](01_Nivel_1_Inicial.md#i1) | 2 | Laboratorio | En tu laboratorio, abre la configuración de privacidad de IRM, confirma que la seudonimización está activa y documenta qué oculta (nombres en alertas y casos, perfil de usuario, grafo de riesgo) y qué no (el panel… |
| [I1](01_Nivel_1_Inicial.md#i1) | 3 | Laboratorio | Redacta una carta de intención del programa para Legal, RR. HH. y privacidad: finalidades, poblaciones, señales, responsables y la cláusula de responsabilidad del cliente, apoyándote en la guía de planificación y en… |
| [I1](01_Nivel_1_Inicial.md#i1) | 4 | Laboratorio | Mira Manage Data Risks from Employee Insiders with Microsoft Purview y anota qué cambió desde 2022 en la interfaz y en los nombres (del portal de cumplimiento al portal de Purview, de la cola clásica a la unificada).… |
| [I1](01_Nivel_1_Inicial.md#i1) | 5 | Solo producción | Concilia licencias en producción: compara los usuarios que quedarían en el alcance de tus políticas con los que tienen derechos de IRM, porque todo usuario que se beneficia necesita licencia (descripción del… |
| [I2](01_Nivel_1_Inicial.md#i2) | 1 | Laboratorio | Activa las analíticas, espera hasta 48 horas y revisa Informes > Analíticas; guarda los principales hallazgos y crea una política de prueba desde una recomendación (analíticas; informes). Evidencia: captura de los… |
| [I2](01_Nivel_1_Inicial.md#i2) | 2 | Laboratorio | Conector de RR. HH. con datos sintéticos: registra la app en Entra, crea el conector y prepara un CSV con UserPrincipalName, ResignationDate y LastWorkingDate (formato ISO 8601) para tres usuarios de prueba, con… |
| [I2](01_Nivel_1_Inicial.md#i2) | 3 | Laboratorio | Indicadores de dispositivo: incorpora una VM Windows 11 en Azure, activa los indicadores de dispositivo y genera actividad con una cuenta de prueba —subida a la nube con Edge, impresión y copia a un recurso de red—… |
| [I2](01_Nivel_1_Inicial.md#i2) | 4 | Laboratorio | Crea un grupo de usuarios prioritarios (`PRUEBA-IRM-Finanzas`), un grupo de detección y una exclusión global justificada, por ejemplo el dominio de un proveedor aprobado (Get started; detecciones inteligentes).… |
| [I2](01_Nivel_1_Inicial.md#i2) | 5 | Laboratorio parcial | Conector de acceso físico con un JSON sintético de tres eventos fuera de horario y un activo físico prioritario (conector de acceso físico). Evidencia: eventos importados. Limitación: para correlacionarlo con… |
| [I2](01_Nivel_1_Inicial.md#i2) | 6 | Laboratorio parcial | Indicador de pago por uso: vincula una suscripción de Azure del mismo tenant (habilitar el pago por uso), activa un solo indicador de nube con alcance piloto y fija presupuesto y alertas al 50, 75 y 90 %; revisa el… |
| [I2](01_Nivel_1_Inicial.md#i2) | 7 | Solo producción | Conector de registros de salud (EMR) y Patient data misuse: requieren un sistema clínico real (conector Microsoft Healthcare o Epic) y el perfil de empleado del conector de RR. HH. (Get started). Cómo hacerlo seguro:… |
| [I3](01_Nivel_1_Inicial.md#i3) | 1 | Laboratorio | Con una política de prueba activa desde hace al menos 24 horas, filtra la cola unificada por severidad y por categoría del agente y clasifica tres alertas: confirma una, descarta otra con motivo y deja la tercera en… |
| [I3](01_Nivel_1_Inicial.md#i3) | 2 | Laboratorio | Crea un caso desde la alerta confirmada, asígnalo a la cuenta de IRM Investigators, agrega una nota del investigador y verifica las notas automáticas del sistema (casos; MC1430534). Evidencia: captura del caso con… |
| [I3](01_Nivel_1_Inicial.md#i3) | 3 | Laboratorio | Redacta la versión 0 de tu procedimiento de triage (una página): criterios para confirmar o descartar, motivos de descarte estandarizados, tiempo máximo en «Needs review», quién puede ver identidades y qué evidencia… |
| [I3](01_Nivel_1_Inicial.md#i3) | 4 | Laboratorio | Con la seudonimización activa, entra con la cuenta de IRM Analysts y luego con la de IRM Investigators y compara qué ve cada una en la alerta, el perfil de usuario y el explorador de contenido (permisos; privacidad).… |
| [I3](01_Nivel_1_Inicial.md#i3) | 5 | Solo producción | Migración desde «Alerts (classic)»: inventaría filtros guardados, manuales y procedimientos que mencionen la pestaña clásica o Alert Spotlight y actualízalos a la cola unificada (MC1430536). Cómo hacerlo seguro:… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 1 | Laboratorio | Crea `PRUEBA-IRM-SalidaEmpleados-v1` con la plantilla Data theft by departing users, alcance a los tres usuarios del CSV de I2 y el conector de RR. HH. como disparador; genera descargas y copias de archivos de prueba… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 2 | Laboratorio parcial | Data leaks con DLP de severidad alta: crea una política DLP para Exchange, SharePoint y OneDrive con «Incident reports = High», asígnala como disparador y provoca coincidencias con datos sintéticos (plantillas).… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 3 | Laboratorio parcial | Security policy violations: activa la integración entre Defender for Endpoint e IRM en las funciones avanzadas de MDE, incorpora la VM de I2, elige los estados de alerta a importar y genera una alerta de prueba… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 4 | Laboratorio | Risky browser usage (vista previa): en la VM Windows 11 incorporada de I2 (la extensión requiere Windows 10 x64 1809 o posterior), despliega la extensión de navegador (manual, con Intune o por GPO), activa al menos… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 5 | Laboratorio | Data leaks by priority users: usa el grupo prioritario de I2 y define como contenido prioritario un sitio de SharePoint con documentos de prueba; compara la severidad de las alertas con la política Data leaks general… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 6 | Laboratorio | Crea una variante de indicador (por ejemplo, excluir el dominio de un socio aprobado) y documenta el orden de evaluación: exclusiones globales, variante y contenido prioritario (indicadores). Evidencia: ficha de… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 7 | Solo producción | Patient data misuse (vista previa) para organizaciones de salud: requiere el conector Microsoft Healthcare o Epic y el conector de RR. HH. con perfil de empleado (plantillas; Get started). Cómo hacerlo seguro: piloto… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 1 | Laboratorio | Genera un informe de actividad de usuario de 90 días para una cuenta de prueba de I2 y compara su contenido con el explorador de actividad (informes). Evidencia: hora de solicitud, hora de disponibilidad (hasta 10… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 2 | Laboratorio | Flujo de aprobación forense: con la cuenta de IRM Admins solicita la captura de un usuario de prueba y apruébala con la de IRM Approvers; configura la plantilla de notificación al usuario aprobado y revisa la… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 3 | Laboratorio parcial | Captura forense con voluntarios: usa una VM con 16 GB de RAM y 8 vCPU (costosa en créditos), instala el cliente de Microsoft Purview (x64), habilita la captura «Specific activities» con la capacidad de prueba de 20… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 4 | Laboratorio parcial | Desde el caso de I3, crea una investigación de Data Security Investigations sobre uno o dos buzones de prueba, con contexto en lenguaje natural y una estimación de costos previa (crear una investigación). Evidencia:… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 5 | Laboratorio parcial | OCR (vista previa, pago por uso): actívalo y sube una imagen con datos sensibles sintéticos desde el endpoint Windows de prueba; comprueba si la detección aparece en la actividad (Get started). Evidencia: evento con… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 6 | Solo producción | Evidencia forense en producción: solo con aprobación previa de Legal y RR. HH., para usuarios concretos con un caso abierto, en ventanas cortas y con aviso a los usuarios según la política interna (evidencia… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 1 | Laboratorio | Ejecuta la configuración rápida de Protección adaptativa y, cuando termine (hasta 72 horas), revisa la política Data leaks, la política de Acceso condicional en solo informe y las dos políticas DLP en modo prueba… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 2 | Laboratorio parcial | Lleva a un usuario de prueba al nivel Elevated generando actividad de exfiltración simulada y verifica el resultado de las DLP en modo prueba (Protección adaptativa). Evidencia: nivel asignado y coincidencias DLP.… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 3 | Laboratorio | Fuerza la expiración del nivel de riesgo de ese usuario y documenta qué datos aparecieron sin seudonimizar mientras estuvo vigente: alertas DLP, explorador de actividad y Acceso condicional (Protección adaptativa).… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 4 | Laboratorio | Revisa la política de Acceso condicional con la condición de riesgo interno en modo solo informe y consulta en los registros de inicio de sesión qué habría hecho con el usuario Elevated; el video Insider Risk in… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 5 | Laboratorio parcial | Data Lifecycle Management (vista previa): verifica la política de retención creada automáticamente y borra un archivo de prueba con el usuario Elevated; comprueba que queda preservado (Protección adaptativa).… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 6 | Solo producción | Pasar la DLP adaptativa de modo prueba a aplicación requiere una línea base real de falsos positivos. Cómo hacerlo seguro: grupo piloto aprobado, dos semanas en modo prueba, revisión de coincidencias con el negocio,… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 1 | Laboratorio | Crea una plantilla de aviso en HTML (recordatorio de la política de uso aceptable) y envíala desde un caso a un usuario de prueba (plantillas de aviso). Evidencia: correo recibido y entrada en el historial del caso. |
| [M4](02_Nivel_2_Intermedio.md#m4) | 2 | Laboratorio | Habilita la colaboración en Teams (vista previa), crea un caso y verifica la membresía del equipo privado; resuelve el caso y comprueba que el equipo queda archivado (Teams para casos). Evidencia: capturas antes y… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 3 | Laboratorio | Escala un caso de prueba a eDiscovery (Premium) y verifica en eDiscovery el caso creado y sus custodios (gestionar casos; IRM en español). Evidencia: identificador del caso de eDiscovery y nota en el caso de IRM. |
| [M4](02_Nivel_2_Intermedio.md#m4) | 4 | Laboratorio | Acota por región con unidades administrativas: crea una unidad con los usuarios de prueba de un país, asigna un analista con ese alcance y verifica que solo ve los casos de su región (permisos). Evidencia: captura… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 5 | Laboratorio | Arma la matriz RACI del traspaso de un caso entre Seguridad, RR. HH., Legal y privacidad, con tiempos objetivo y la evidencia a entregar en cada paso, apoyándote en la tabla Gobierno, privacidad y proceso de casos.… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 6 | Solo producción | Ejercicio de mesa con RR. HH., Legal, privacidad y, si corresponde, la representación de los trabajadores, sobre un caso ficticio de salida de un empleado (planificar IRM). Cómo hacerlo seguro: datos inventados,… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 1 | Laboratorio parcial | Risky AI usage: despliega la extensión Microsoft Insider risk (Edge) o Microsoft Purview (Chrome), crea la política desde DSPM for AI o desde IRM con alcance a dos usuarios de prueba y genera prompts con datos… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 2 | Laboratorio parcial | Selección de apps de IA (disponibilidad general desde junio de 2026): deja solo dos apps monitoreadas, documenta el motivo de cada una y estima el costo de pago por uso del piloto (What's new; indicadores).… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 3 | Laboratorio parcial | Risky Agents: crea un agente de Copilot Studio (prueba) que consulte un sitio con datos sensibles de prueba, ejercítalo con prompts de riesgo y revisa la política de agentes y la sección Agents (monitoreo de… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 4 | Laboratorio parcial | Privacidad en IA: con la seudonimización activa, revisa qué contenido de prompts y respuestas ve cada rol y qué ocurre con un usuario invitado (solo indicadores de tipos de información sensible) (monitoreo de… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 5 | Solo producción | Risky AI usage con usuarios reales requiere aprobaciones previas de Legal, RR. HH., privacidad y, cuando corresponda, la representación de los trabajadores (plantillas; Get started). Cómo hacerlo seguro:… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 6 | Solo producción | Agentes con Microsoft 365 E7 o Agent 365: confirma la licencia, inventaría los agentes con actividad y elige uno o dos de bajo riesgo cuyo dueño sea TI (MC1280556). Cómo hacerlo seguro: política de agentes separada… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 1 | Laboratorio parcial | Activa el uso compartido de datos en IRM, asigna Security Reader e IRM Analysts a una cuenta del SOC y filtra los incidentes por la fuente «Microsoft Purview Insider Risk Management» (IRM en Defender XDR). Evidencia:… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 2 | Laboratorio parcial | Consulta en la búsqueda avanzada la tabla DataSecurityEvents para un usuario de prueba durante siete días y DataSecurityBehaviors para ver la agregación diaria; guarda ambas consultas KQL (DataSecurityEvents;… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 3 | Laboratorio | En un workspace de Sentinel de laboratorio, instala la solución de IRM desde el Content hub, activa «Export alerts» en IRM y verifica la llegada de datos en la hora siguiente; comprueba que los nombres llegan sin… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 4 | Laboratorio | Revisa las reglas de automatización y los playbooks de Sentinel que dependan de alertas dentro de incidentes y documenta el impacto de los incidentes de IRM sin alertas; decide entre uso compartido y conector (IRM en… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 5 | Laboratorio | Mira la sesión del Virtual Ninja Show sobre IRM en Defender XDR y redacta un procedimiento de traspaso para dos escenarios: cuenta comprometida (lo lleva el SOC) y posible amenaza interna (lo lleva el equipo de… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 6 | Solo producción | Traspaso SOC–IRM en producción: define qué analistas del SOC ven incidentes de IRM (Security Reader más IRM Analysts, solo para personas designadas) y qué datos mínimos reciben (IRM en Defender XDR). Cómo hacerlo… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 1 | Laboratorio parcial | Despliegue del Triage Agent: aprovisiona 1 SCU por unas horas (y elimínala al terminar), habilita el plugin de Purview, verifica el uso compartido de datos de Microsoft 365 y despliega el agente sobre las políticas… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 2 | Laboratorio parcial | Da retroalimentación sobre tres categorizaciones del agente y observa si cambia la priorización; registra el consumo de SCU de la sesión (agentes de Purview). Evidencia: categorías antes y después y SCU consumidas.… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 3 | Laboratorio | Ficha de gobierno del agente: responsable del servicio (quien guarda la configuración), calendario de reautenticación cada 90 días, roles necesarios (Purview Content Analyst y grupos de IRM), quién ve el panel sin… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 4 | Laboratorio | Mira New Agents in Microsoft Purview y compara lo que muestra con tu laboratorio actual (nombre del agente, cola unificada, categorías y contexto). Evidencia: lista de diferencias con su fecha. |
| [A3](03_Nivel_3_Avanzado.md#a3) | 5 | Solo producción | Medir el valor del agente con alertas reales: compara durante 30 días el tiempo hasta el triage de «Needs attention» frente al resto y el porcentaje de categorizaciones corregidas por analistas (Triage Agent;… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 1 | Laboratorio | Crea un flujo de IRM con Power Automate (vista previa) que, al confirmar una alerta, notifique en Teams a la cuenta del investigador o cree un ticket de prueba; documenta los campos que envía y quién los recibe… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 2 | Laboratorio | Automatiza la carga del conector de RR. HH. con el script programado a diario o con la plantilla de Power Automate, y verifica que los perfiles de empleado se renuevan antes de los 30 días (conector de RR. HH.).… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 3 | Laboratorio parcial | Conector Insider Risk Indicators: carga un CSV agregado con detecciones sintéticas de un tercero (por ejemplo, «exportación masiva desde el CRM»), mapéalo a un indicador personalizado en una política Data leaks y… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 4 | Laboratorio parcial | Graph security API: registra una aplicación con los permisos mínimos para leer alertas, lista las alertas de IRM compartidas con Defender y guarda la respuesta (IRM en Defender XDR). Evidencia: respuesta de la API… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 5 | Laboratorio | Inventario de flujos de datos: por cada automatización (Power Automate, exportación de alertas, conector de Sentinel, Graph), registra los datos que mueve, el destino, si conserva la seudonimización, los permisos y… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 6 | Solo producción | Integración con ServiceNow con tickets reales: cola restringida, campos mínimos (identificador de caso seudonimizado, severidad y política) y aprobación de privacidad (Power Automate en IRM; casos). Cómo hacerlo… |
| [O1](04_Nivel_4_Operacion.md#o1) | 1 | Laboratorio | Matriz RACI de los siete roles del programa (administrador de Insider Risk, analista o investigador, socio de RR. HH., asesoría legal, oficial de privacidad, analista del SOC y CISO) mapeada a los grupos de roles de… |
| [O1](04_Nivel_4_Operacion.md#o1) | 2 | Laboratorio | Configura las notificaciones a administradores y verifica en el laboratorio el correo de primera alerta (ajustes de IRM). Evidencia: captura del correo y de la configuración. |
| [O1](04_Nivel_4_Operacion.md#o1) | 3 | Laboratorio | Revisión de accesos: con la cuenta de IRM Auditors, exporta la membresía de los grupos de roles y busca en la auditoría los cambios de roles de IRM del último mes (permisos; auditoría). Evidencia: informe de revisión… |
| [O1](04_Nivel_4_Operacion.md#o1) | 4 | Laboratorio | Escribe y prueba el procedimiento de «cero administradores»: quién tiene el acceso de emergencia, cómo se activa con PIM y cómo se audita (permisos de IRM; permisos del portal de Purview). Evidencia: procedimiento… |
| [O1](04_Nivel_4_Operacion.md#o1) | 5 | Solo producción | Aprobación del estatuto del programa ante el comité (CISO, RR. HH., Legal, privacidad y, cuando corresponda, la representación de los trabajadores) (guía de CISA; planificar IRM). Cómo hacerlo seguro: ninguna… |
| [O2](04_Nivel_4_Operacion.md#o2) | 1 | Laboratorio | Exporta a CSV los informes de alertas y casos y arma un tablero mensual con el KPI de días en «Needs review», la eficacia por política y los motivos de descarte (informes; políticas). Evidencia: tablero en Excel o… |
| [O2](04_Nivel_4_Operacion.md#o2) | 2 | Laboratorio | Revisa el informe de uso de pago por uso y crea un presupuesto de Azure con alertas; calcula el costo por política del piloto (informes; Usage center). Evidencia: tabla de costo por política y alerta de presupuesto… |
| [O2](04_Nivel_4_Operacion.md#o2) | 3 | Laboratorio | Revisa el panel de recomendaciones de políticas y registra cada brecha de cobertura detectada, con la decisión tomada y su dueño (MC1387681). Evidencia: registro de decisiones. |
| [O2](04_Nivel_4_Operacion.md#o2) | 4 | Laboratorio | Compara las analíticas antes y después de un cambio de configuración (por ejemplo, un indicador nuevo) usando el escaneo diario y sus recomendaciones de umbrales (analíticas). Evidencia: dos capturas fechadas y una… |
| [O2](04_Nivel_4_Operacion.md#o2) | 5 | Solo producción | Ajuste con volumen real: hacen falta unos 30 días de actividad real para medir falsos positivos (detecciones inteligentes). Cómo hacerlo seguro: copia la política, cambia umbrales o variantes en la copia acotada a un… |
| [O3](04_Nivel_4_Operacion.md#o3) | 1 | Laboratorio | Paquete de evidencia de privacidad del laboratorio: capturas de la seudonimización activa, de los grupos de roles con vencimiento y una búsqueda de auditoría de las acciones de un investigador (quién vio qué y… |
| [O3](04_Nivel_4_Operacion.md#o3) | 2 | Laboratorio | Hoja de insumos para la evaluación de impacto de privacidad: finalidad, categorías de datos (indicadores activados), destinatarios (SOC, RR. HH., Legal), retenciones (clips forenses, 120 días; preservación de DLM,… |
| [O3](04_Nivel_4_Operacion.md#o3) | 3 | Laboratorio | Mapa regional: a partir de la hoja «Normativa MCSA», lista las normas de los países donde opera tu organización y redacta preguntas para Legal, sin interpretarlas, por ejemplo sobre aviso a los empleados,… |
| [O3](04_Nivel_4_Operacion.md#o3) | 4 | Laboratorio | Borrador de comunicación a empleados con RR. HH.: qué se monitorea, para qué, con qué salvaguardas (seudonimización, roles, auditoría) y a quién consultar, coherente con la cláusula de responsabilidad del cliente… |
| [O3](04_Nivel_4_Operacion.md#o3) | 5 | Solo producción | Aprobación y comunicación del programa: presenta el estatuto, la evaluación de impacto y la comunicación a Legal, RR. HH., privacidad y, cuando corresponda, la representación de los trabajadores (planificar IRM; Get… |
| [C1](Practica-y-referencias.md#c1) | 1 | — | Elige tres fuentes oficiales (blog de seguridad de Microsoft, Centro de mensajes y Microsoft Mechanics) y dos de la comunidad de la lista de referentes, y suscríbete. Evidencia: lista con la frecuencia de revisión de… |
| [C1](Practica-y-referencias.md#c1) | 2 | — | Lee la práctica 22 de la Common Sense Guide de SEI/CERT («aprender de incidentes pasados») y conviértela en una pregunta fija de tu revisión mensual de casos. |
| [C1](Practica-y-referencias.md#c1) | 3 | — | Escucha un episodio de M365.FM sobre IRM y anota una idea para tu laboratorio y una afirmación que debas contrastar con Learn. |
| [C2](Practica-y-referencias.md#c2) | 1 | — | Arma tu rutina mensual de 30 minutos: What's new in Microsoft Purview, avisos del Centro de mensajes sobre IRM y el blog de seguridad de Microsoft; registra cada cambio con su fecha y el módulo afectado en tu radar. |
| [C2](Practica-y-referencias.md#c2) | 2 | — | Comparte con RR. HH. y Legal la ruta de SC-401 en español y la guía de configuración inicial en español, y reúne sus dudas para la próxima reunión del comité. |
| [C2](Practica-y-referencias.md#c2) | 3 | — | Después de Microsoft Ignite (17 al 20 de noviembre de 2026), revisa los estados de vista previa de este programa —Risky Agents, la integración con Defender XDR y la cola unificada— y actualiza tu radar. |

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="glosario-y-fuentes"></a>

## Cierre, glosario y fuentes


<a id="cierre"></a>

## ¿Y ahora?

**Próximos pasos.** Si buscas una credencial formal, prepara SC-401 con su guía de estudio del 28 de octubre de 2026 y completa la ruta oficial de IRM en Microsoft Learn. Haz también los knowledge checks del Ninja oficial de Tech Community: aunque su última actualización conocida es de 2024, sus fundamentos siguen vigentes y otorgan el certificado no oficial «Ninja Cat».

**Sigue con la serie.** Purview DLP, para las políticas que disparan y ejecutan la Protección adaptativa; Communication Compliance, para las señales de conducta; DSPM y seguridad de datos para IA, para la postura de Copilot y de los agentes; eDiscovery y Audit, para la preservación y la cadena de custodia; Defender XDR y Sentinel, para la correlación en el SOC; Entra, para el Acceso condicional y Global Secure Access; y Security Copilot, para las SCU y los agentes.

**Mantente al día.** Revisa cada mes la página de novedades de Purview y el Centro de mensajes y, después de Microsoft Ignite (17 al 20 de noviembre de 2026), confirma los estados que esta edición marca como vista previa o como contradictorios en la lista de puntos a confirmar.

**Y recuerda lo esencial.** Insider Risk Management protege a la organización y a las personas solo si se usa con proporcionalidad: aprobaciones previas, seudonimización, roles separados, auditoría de los investigadores y decisiones finales en manos de RR. HH. y Legal, con evidencia completa.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Riesgo interno (insider risk) | Riesgo de que personas con acceso legítimo —empleados, contratistas o agentes— causen, por error o con intención, fugas, robos o violaciones de seguridad. |
| Insider Risk Management (IRM) | Solución de Microsoft Purview que correlaciona señales para detectar, investigar y responder al riesgo interno; en Learn en español aparece como «Administración de riesgos internos». |
| Política (directiva) | Configuración basada en una plantilla que define a quién se evalúa, con qué disparadores e indicadores y con qué umbrales; la documentación en español usa «directiva». |
| Seudonimización | Reemplazo de los nombres de usuario por alias dentro de IRM, activo por defecto; no se conserva en Acceso condicional, alertas DLP, el explorador de actividad, la exportación por API ni el panel del Triage Agent. |
| Evento desencadenante | Señal que pone a un usuario en el alcance de una política, como una renuncia informada por el conector de RR. HH. o una alerta DLP de severidad alta. |
| Indicador global e indicador de política | El global define qué actividad recolecta IRM en el tenant (todos vienen desactivados); el de política define qué actividad puntúa en una política concreta. |
| Variante de indicador | Versión ajustada de un indicador, por ejemplo con un dominio excluido; hasta 10 por indicador y 100 en total. |
| Booster de riesgo | Factor que eleva la puntuación: actividad inusual, caso previo confirmado, pertenencia a un grupo prioritario o usuario de alto impacto. |
| Exfiltración acumulativa | Detección que compara los últimos 30 días del usuario con la organización y con su grupo de pares. |
| Grupo de usuarios prioritarios | Usuarios de mayor impacto cuyas alertas reciben más severidad; obligatorio en las plantillas «by priority users» y no combinable con unidades administrativas. |
| Exclusiones globales | Usuarios, dominios, rutas o actividades que IRM no evalúa; hoy se configuran en «Global exclusions (preview)». |
| Analíticas | Escaneo diario de hasta 10 días de actividad con resultados agregados y anonimizados para estimar el riesgo antes de crear políticas. |
| Cola unificada de alertas | Experiencia que reúne las alertas clásicas y las del Triage Agent, con la vista «Needs attention»; disponibilidad general en octubre de 2026. |
| Caso | Expediente centrado en un usuario que reúne alertas, actividad, contenido, notas, avisos y acciones de escalamiento. |
| Plantilla de aviso | Correo que se envía al usuario de un caso para recordarle políticas o capacitación y que deja rastro auditable. |
| Evidencia forense | Complemento opcional que graba clips de video de actividad riesgosa en dispositivos Windows; requiere la aprobación de IRM Approvers y borra los clips a los 120 días. |
| Protección adaptativa | Capacidad que aplica controles de DLP, Acceso condicional y Data Lifecycle Management según el nivel de riesgo interno. |
| Nivel de riesgo interno | Elevated, Moderate o Minor: clasificación dinámica del usuario o del agente para la Protección adaptativa, distinta de la severidad de la alerta. |
| Conector de RR. HH. | Importación por CSV de renuncias, cambios de nivel, evaluaciones, planes de mejora y perfiles de empleado. |
| Conector Insider Risk Indicators | Conector en vista previa que importa detecciones de terceros ya agregadas para usarlas como disparadores o indicadores personalizados. |
| Pago por uso (PAYG) | Facturación por consumo en una suscripción de Azure del mismo tenant para indicadores de nube, red, Fabric e IA de terceros, OCR y Data Security Investigations. |
| SCU | Unidad de cómputo de seguridad de Security Copilot; el Triage Agent la consume según el número y el tipo de alertas. |
| Triage Agent | Agente de Security Copilot (Microsoft Purview Triage Agent) que clasifica las alertas en Needs attention, Less urgent y Not categorized. |
| Risky AI usage | Plantilla que detecta prompts y respuestas riesgosos o con datos sensibles y visitas a sitios de IA generativa. |
| Risky Agents | Política para agentes de Copilot Studio, Microsoft Foundry y el SDK P4AI; en vista previa según Learn y sujeta a E7 o Agent 365 según MC1280556. |
| DataSecurityEvents y DataSecurityBehaviors | Tablas de la búsqueda avanzada de Defender XDR con eventos enriquecidos y comportamientos diarios generados por IRM (vista previa). |
| Data Security Investigations (DSI) | Solución de pago por uso para analizar contenido a escala con IA; puede iniciarse desde un caso de IRM. |
| Eficacia de alertas | Alertas confirmadas sobre confirmadas más descartadas en los últimos 365 días, por política. |
| Microsoft Purview Suite | Nombre de Microsoft 365 E5 Compliance desde el 1 de octubre de 2025; incluye IRM y se agrega a Microsoft 365 E3. |
| Microsoft 365 E7 y Agent 365 | E7 suma Microsoft 365 E5, Microsoft 365 Copilot, Entra Suite y Agent 365; Agent 365 también se vende aparte. Según MC1280556, son el requisito de IRM para agentes. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- **Conector de RR. HH. en las plantillas de salida.** La página de plantillas permite usar el borrado de la cuenta en Entra en lugar del conector en Data theft by departing users, pero «Get started» lo lista como requerido para esa plantilla y para Security policy violations by departing users ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) frente a [Get started](https://learn.microsoft.com/en-us/purview/insider-risk-management-configure)).
- **Estado de Risky Agents.** MC1200579 reprogramó la disponibilidad general para mediados de junio a fines de julio de 2026 y MC1280556 la anuncia con E7 o Agent 365 como requisito, pero las páginas de Learn de plantillas, indicadores y monitoreo de agentes (4 de agosto de 2026) siguen diciendo «preview» ([MC1200579](https://mc.merill.net/message/MC1200579); [MC1280556](https://message.cengizyilmaz.net/message/mc1280556-microsoft-purview-for-agents-ai-observability-and-insider-risk-management-now-generally-available); [monitoreo de agentes](https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents)).
- **Licencias para agentes en futuro.** La descripción del servicio de Purview todavía dice que las capacidades para agentes de Microsoft Foundry y apps conectadas a Entra «se soportarán» con E7 y Agent 365, aunque MC1280556 ya marca la disponibilidad general ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)).
- **Fechas internas de MC1430536.** El aviso dice que ambas experiencias de alertas convivirían «al menos 60 días» con soporte «hasta el 31 de agosto de 2026», fecha anterior a la disponibilidad general de octubre y a la depreciación del 1 de octubre; además, What's new solo registra la vista previa de julio ([MC1430536](https://mc.merill.net/message/MC1430536); [What's new](https://learn.microsoft.com/en-us/purview/whats-new)).
- **Etiqueta de Risky AI usage.** La plantilla no lleva etiqueta de vista previa, pero los indicadores de Risky AI usage sí ([plantillas](https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates) frente a [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).
- **Nubes de gobierno de EE. UU.** La página de Protección adaptativa dice que IRM no está disponible en esas nubes, mientras que MC1430536 fija fechas para ellas y el conector de RR. HH. existe en GCC; el impacto es bajo para MCSA ([Protección adaptativa](https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection); [conector de RR. HH.](https://learn.microsoft.com/en-us/purview/import-hr-data)).
- **Integración con Defender XDR.** El documento base (17 de febrero de 2025) sigue en *prerelease*, pero MC1438568 ya agrega los resúmenes del Triage Agent en Defender, con disponibilidad general prevista para diciembre de 2026; el estado de disponibilidad general de la integración base no está confirmado ([IRM en Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender); [MC1438568](https://mc.merill.net/message/MC1438568)).
- **Retención de clips forenses.** La página dice que los clips se borran a los 120 días «o al final del período de vista previa», texto que parece heredado; confirma el estado comercial y la capacidad adicional de 100 GB con tu revendedor ([evidencia forense](https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence); [CDW](https://www.cdw.com/product/microsoft-365-insider-risk-management-forensic-evidence-subscription-lice/7387563)).
- **Licencia del Triage Agent.** Learn exige el modelo de pago por uso además de las SCU, mientras que la inclusión de Security Copilot en E5 y E7 aporta SCU; valida en tu tenant si hace falta vincular una suscripción de Azure. Además, algunas páginas de agentes de Purview todavía lo titulan «(preview)» pese a la disponibilidad general anunciada en MC1180884 ([Triage Agent](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started); [inclusión de Security Copilot](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion); [agentes en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents)).
- **Product Terms y SKU de componente.** Tras el cambio de nombre de octubre de 2025, los Product Terms siguen mostrando nombres anteriores como prerrequisitos y los SKU de componente de IRM no cambiaron de nombre; confirma el SKU exacto con tu revendedor ([SAMexpert](https://samexpert.com/microsoft-365-defender-purview-renames/)).
- **Plantilla rápida para apps que no son de Microsoft 365.** Sus prerrequisitos (indicadores de nube conectados en Microsoft Defender y una señal de salida) y si consume pago por uso se infieren de la documentación de indicadores; no se confirmaron en una página propia ([What's new](https://learn.microsoft.com/en-us/purview/whats-new); [indicadores](https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators)).
- **Indicadores de red y métrica de facturación.** Las fuentes confirman que los indicadores de red de terceros son de pago por uso, pero no su estado. La matriz de laboratorio de la serie indica que los indicadores de nube de terceros y Fabric se facturan por unidades de procesamiento (una por cada 10.000 actividades): confirma la métrica y el precio vigentes en los [modelos de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models) antes de presupuestar.
- **Crédito de Visual Studio.** No hay confirmación oficial de que el crédito de Azure de Visual Studio Enterprise cubra los medidores de pago por uso de Purview ni las SCU de Security Copilot; trátalo como un gasto no garantizado.
- **Ninja oficial.** La descarga directa del post de Tech Community falló en la verificación y la nota mínima del 80 % típica de la familia no se pudo confirmar para el Ninja de IRM; su estructura se reconstruyó con la [copia sindicada de abril de 2022](https://thewindowsupdate.com/2022/04/19/become-a-insider-risk-management-ninja/) y las publicaciones de 2023 y 2024.
- **Referentes en otros programas.** El programa de DSPM lista a Talhah Mir como empleado de Microsoft, pero según esta investigación dejó la empresa en agosto de 2026; en este programa figura como ex empleado.
- **Traducciones.** Las páginas de Learn en español son traducciones automáticas y pueden ir atrasadas respecto de la versión en inglés; ante cualquier diferencia, prevalece la versión en inglés.
- **Microsoft Ignite 2026.** Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa y nombres después de la fecha de corte de esta edición.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal ni laboral: usar Insider Risk Management sobre personas reales exige la evaluación previa de tus áreas de Legal, RR. HH. y privacidad y, cuando corresponda, de la representación de los trabajadores. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

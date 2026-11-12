# Comunidad · Referentes, canales y cómo mantenerse al día

*Microsoft Purview eDiscovery y Audit Ninja Training · Edición 2026*

[← Nivel 4 · Operación](04_Nivel_4_Operacion.md) · [Índice del programa](README.md) · [Evaluaciones y respuestas →](06_Evaluaciones_y_respuestas.md)

<a id="comunidad"></a>

MVPs y empleados de Microsoft que enseñan eDiscovery y Audit, libros, recursos en español y una rutina de actualización basada en fuentes oficiales.

*Transversal · 2 módulos · ~4 horas · 10 recursos*

**Módulos de este nivel:** [C1 Referentes y libros](#c1) · [C2 Español y actualización](#c2)

<a id="c1"></a>

## C1 · Referentes, canales y libros

*Transversal · ~2 h · Origen: Sin equivalente en el Ninja original*

eDiscovery y Audit cambian cada mes, y la documentación no siempre cuenta el porqué. Los referentes de la comunidad sí: Tony Redmond analiza cada aviso del Message Center con mirada crítica, Albert Hoitingh publica un resumen mensual de Purview, y especialistas en detección como Bert-Jan Pals o Matt Zorich muestran cómo usar la auditoría en el SOC. Del lado de Microsoft, los webinars de la Security Community y los autores del Ninja oficial explican el producto desde adentro.

Los libros siguen siendo útiles para los fundamentos, pero revisa la edición: el eBook *Microsoft Purview for IT Pros*, separado de *Microsoft 365 for IT Pros* en su edición 2027, se actualiza cada mes; otros títulos se escribieron antes de la experiencia unificada y conviene leerlos con esa advertencia.

**Por qué importa**

Seguir a pocos referentes confiables, con constancia, es la forma más barata de enterarte a tiempo de un cambio que rompe un procedimiento o un script, y de entender su impacto antes de que llegue el próximo asunto. También te da criterio para distinguir un anuncio general de un cambio con fecha, licencia y fuente oficial.

**Qué vas a lograr**

- Identificar referentes confiables por especialidad: Purview, eDiscovery, auditoría y respuesta a incidentes.
- Elegir lecturas de fondo según tu rol y nivel, revisando su vigencia.
- Armar una lista de seguimiento personal breve y constante.

> **Novedad.** El 1 de julio de 2026, la edición 2027 de *Microsoft 365 for IT Pros* separó el eBook *Microsoft Purview for IT Pros*: siete capítulos y 330 páginas sobre eDiscovery, ciclo de vida de los datos y DLP, con actualizaciones mensuales ([anuncio](https://office365itpros.com/2026/07/01/microsoft-365-for-it-pros/)).

> **Consejo Ninja.** El archivo de eDiscovery del Microsoft Security Blog muestra su última entrada en febrero de 2025: las novedades recientes están en Tech Community y en What's new in Microsoft Purview ([archivo](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-ediscovery/), [novedades](https://learn.microsoft.com/en-us/purview/whats-new)).

**¿Tienes poco tiempo?**

- [Announcing Microsoft 365 for IT Pros (2027 Edition)](https://office365itpros.com/2026/07/01/microsoft-365-for-it-pros/) · Libro
- [Things to Know About Microsoft Purview – October 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/) · Blog

### Directorio de referentes verificados

- **John Wirtala (John_Wirtala1608)** (Empleado de Microsoft): Presentador de los webinars oficiales de Microsoft Security Community sobre la nueva experiencia de eDiscovery y el retiro del clásico (2025) y autor del Ninja de Priva en Tech Community. [YouTube](https://www.youtube.com/watch?v=bmpY8QRmBnw) · [Otro](https://www.youtube.com/watch?v=EUrJy_oGXfw) · [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-priva-ninja/3876888)
- **Matt Zorich (reprise99)** (Empleado de Microsoft, Australia): Caza de amenazas e investigación forense en Entra ID/M365 con KQL (equipo GHOST, antes DART); ex-MVP y coautor de The Definitive Guide to KQL. Relevante para M3/A3: consultas KQL sobre OfficeActivity y registros de Entra en investigaciones de compromiso. [Blog](https://learnsentinel.blog/author/mzorich/) · [GitHub](https://github.com/reprise99/Sentinel-Queries) · [Otro](https://infosec.exchange/@reprise_99) · [Evidencia de rol](https://www.pearson.com/en-us/subject-catalog/p/the-definitive-guide-to-kql/P200000011890?view=educator)
- **ninachen (Tech Community)** (Empleado de Microsoft): Autora del anuncio oficial de la experiencia moderna y unificada de eDiscovery (ago-2024): flujo único estándar/premium, Content Search dentro de casos, selector de orígenes de datos y borrador de consultas con Copilot. [Evidencia de rol](https://techcommunity.microsoft.com/blog/microsoft-security-blog/ediscovery-launches-a-modern-intuitive-user-experience/4215184)
- **Albert Hoitingh** (MVP de Microsoft): Consultor/arquitecto de Microsoft 365 centrado en Purview (gobierno de información, eDiscovery, protección de datos e IA); publica un resumen mensual "Things to Know About Microsoft Purview" y es coautor de un libro sobre eDiscovery. [Blog](https://alberthoitingh.com/category/microsoft-purview/) · [Otro](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707) · [Evidencia de rol](https://alberthoitingh.com/author/alberthoitingh/)
- **Bert-Jan Pals** (MVP de Microsoft, Países Bajos): Ingeniería de detección, caza e IR con KQL en Sentinel y Defender XDR; repositorio de consultas más usado de la comunidad. Relevante para A3: detección e IR con auditoría de M365 en Sentinel/Defender XDR. [Blog](https://kqlquery.com) · [GitHub](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) · [Otro](https://kqlquery.com/posts/kql-sources-2024-update/) · [Evidencia de rol](https://kqlquery.com/whoami/)
- **Jorge Castañeda** (MVP de Microsoft, Perú): MVP de Security (SIEM & XDR) en español: Defender XDR, Sentinel, Purview, priorización de CVEs y laboratorios; fundador de MUG Perú. Referente hispanohablante para el track C2 de este programa. [Blog](https://blog.d3fend.me/) · [Otro](https://blog.d3fend.me/about/) · [Evidencia de rol](https://mvp.microsoft.com/en-us/PublicProfile/5000594)
- **Tony Redmond** (MVP de Microsoft, Irlanda): Referente en administración de Microsoft 365 y Purview (eDiscovery, Audit, retención) con análisis críticos de cada cambio del Message Center y automatización con PowerShell/Graph; editor principal de Microsoft 365 for IT Pros. [Otro](https://o365itpros.gumroad.com/l/O365IT) · [Evidencia de rol](https://techcommunity.microsoft.com/discussions/microsoft-365/announcing-microsoft-365-for-it-pros-2027-edition/4532426)

### Anuncios y blogs oficiales

- [Microsoft Purview eDiscovery Archives | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/product/microsoft-purview-ediscovery/) · Blog oficial · Oficial · Legado aún útil · Microsoft Security Blog. Archivo de publicaciones oficiales sobre eDiscovery (Legalweek, IA generativa, APIs de Graph GA en 2022). *Nota:* Última entrada visible: feb-2025; las novedades recientes están en Tech Community y "What's new"

### Comunidad: blogs, libros, newsletters y eventos

- [Announcing Microsoft 365 for IT Pros (2027 Edition)](https://office365itpros.com/2026/07/01/microsoft-365-for-it-pros/) · Libro · MVP · Nuevo · Tony Redmond · Office 365 for IT Pros · 1 jul 2026. Anuncio de la edición 2027 (13.ª) del libro, que separa un nuevo eBook "Microsoft Purview for IT Pros" de 7 capítulos y 330 páginas con eDiscovery, DLM y DLP.
- [Microsoft eDiscovery In-Depth (Packt)](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707) · Libro · MVP · Legado aún útil · Ryan John Murphy, Purav Desai, Albert Hoitingh · Packt (Amazon). Libro dedicado a Microsoft Purview eDiscovery escrito por MVPs, iniciado antes de la nueva experiencia y reescrito parcialmente por el rediseño del portal. *Nota:* Fecha de edición no visible; verificar que cubra la experiencia unificada (post ago-2025)

**Manos a la obra**

1. Elige tres referentes de esta sección según tu rol (Purview, eDiscovery o detección en el SOC), suscríbete a sus canales y anota en tu registro de cambios la primera publicación útil de cada uno, con su fecha.
2. Lee el resumen mensual de [octubre de 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/) y marca qué novedades obligan a cambiar un procedimiento o un script de tu equipo.
3. Elige tu libro de referencia: si optas por *Microsoft eDiscovery In-Depth*, verifica que cubra la experiencia unificada (posterior a agosto de 2025) antes de usarlo como texto de estudio ([ficha](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707)).

**¿Quieres profundizar?**

- [Microsoft eDiscovery In-Depth (Packt)](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707) · Libro

<a id="c2"></a>

## C2 · Recursos en español y cómo mantenerse actualizado

*Transversal · ~2 h · Origen: Sin equivalente en el Ninja original*

Microsoft Learn ofrece en español buena parte de la documentación de eDiscovery y Audit: permisos, búsqueda de auditoría, datos de IA, auditoría de Copilot, la API de Graph y la exportación de review sets. Son traducciones que llegan después de la versión en inglés y a veces con errores: la página en español de la API de eDiscovery dice «suscripción A3» donde el original dice E3. Ante una diferencia, manda el inglés.

El hábito Ninja es una rutina breve y constante: cada mes, What's new in Microsoft Purview y los avisos del Message Center; cada trimestre, los cambios de examen y los webinars; y antes de cada recomendación, la verificación de fecha y estado en la fuente oficial. Microsoft Ignite, del 17 al 20 de noviembre de 2026, puede cambiar estados de vista previa justo después de la fecha de corte de esta guía.

**Por qué importa**

Los equipos de la región aprenden más rápido en su idioma, pero un dato desactualizado en una traducción puede terminar en una decisión de licencias o de retención equivocada. Una rutina de contraste con la fuente en inglés evita ese riesgo.

**Qué vas a lograr**

- Ubicar material confiable en español y contrastarlo con la versión en inglés.
- Establecer una rutina mensual de actualización basada en fuentes oficiales.
- Verificar fecha, estado y licencia de una novedad en la fuente oficial antes de cambiar un procedimiento.

> **Atención.** Las traducciones llegan después y pueden tener errores: la página en español de la API de eDiscovery dice «suscripción A3» donde el original dice E3 ([versión en español](https://learn.microsoft.com/es-es/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0), [original](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)). Ante una diferencia, manda el inglés.

**¿Tienes poco tiempo?**

- [Guía de estudio para el examen SC-401: Administración de la seguridad de la información en Microsoft 365](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-401) · Credencial
- [Asignar permisos en eDiscovery](https://learn.microsoft.com/es-es/purview/edisc-permissions) · Documentación
- [Búsquedas en el registro de auditoría](https://learn.microsoft.com/es-es/purview/audit-search) · Documentación

### Documentación, cursos y credenciales

- [Guía de estudio para el examen SC-401: Administración de la seguridad de la información en Microsoft 365](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/sc-401) · Credencial · Oficial · Nuevo · ES · Microsoft Learn · 28 oct 2026. Versión en español de la guía SC-401 con las competencias medidas desde el 28-oct-2026.
- [Asignar permisos en eDiscovery](https://learn.microsoft.com/es-es/purview/edisc-permissions) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la guía de roles y grupos de eDiscovery (Manager vs. Administrator) y requisitos de licencia.
- [Búsquedas en el registro de auditoría](https://learn.microsoft.com/es-es/purview/audit-search) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la búsqueda de auditoría (trabajos de búsqueda, roles, retención por licencia).
- [Búsqueda y eliminación de datos de aplicaciones de inteligencia artificial en eDiscovery](https://learn.microsoft.com/es-es/purview/edisc-search-copilot-data) · Documentación · Oficial · ES · Microsoft Learn. Versión en español del flujo de búsqueda y eliminación de datos de Copilot y otras apps de IA.
- [Registros de auditoría para Copilot y aplicaciones de IA](https://learn.microsoft.com/es-es/purview/audit-copilot?view=o365-worldwide) · Documentación · Oficial · ES · Microsoft Learn. Versión en español sobre registros de auditoría de Copilot, Cowork y apps de IA, incluida la facturación por uso para IA no-Microsoft.
- [Exportación de elementos de un conjunto de revisión en eDiscovery](https://learn.microsoft.com/es-es/purview/edisc-review-set-export) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la exportación desde conjuntos de revisión con sus opciones y el plazo de 30 días de descarga.
- [Uso de la API de Microsoft Purview eDiscovery en Microsoft Graph](https://learn.microsoft.com/es-es/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) · Documentación · Oficial · Nuevo · ES · Microsoft Learn (Graph) · 8 may 2026. Versión en español de la visión general de la API eDiscovery de Graph y su matriz de licencias.

**Manos a la obra**

1. Compara la versión en español y en inglés de tres páginas de esta guía (permisos de eDiscovery, búsqueda de auditoría y API de Graph) y registra cada diferencia de contenido o de fecha ([permisos en español](https://learn.microsoft.com/es-es/purview/edisc-permissions), [auditoría en español](https://learn.microsoft.com/es-es/purview/audit-search)).
2. Arma tu rutina: un recordatorio mensual para What's new in Microsoft Purview y el Message Center y uno trimestral para la guía de SC-401 y los webinars, y registra la primera revisión con fecha.
3. Prepara para tu equipo un glosario español-inglés de veinte términos tomados del glosario de esta guía, para alinear la conversación con la interfaz, que está en inglés.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

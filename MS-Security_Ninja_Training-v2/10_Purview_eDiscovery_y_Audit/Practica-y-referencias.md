# Práctica y referencias

[Índice del programa](README.md)


<a id="comunidad"></a>

## Comunidad


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

<a id="evaluaciones-y-respuestas"></a>

## Evaluaciones y respuestas


<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Cuánto tiempo retiene Audit (Standard) los registros generados desde el 17 de octubre de 2023?**

- a) 90 días
- b) 180 días  ✅
- c) Un año
- d) Diez años

*Respuesta: b).* La retención de Audit (Standard) pasó de 90 a 180 días para los registros generados desde esa fecha. Un año es la política predeterminada de Audit (Premium) y diez años requiere un complemento. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**2. ¿Cuándo retiró Microsoft todas las experiencias clásicas de eDiscovery (Content Search, Standard y Premium), salvo en los tenants operados por 21Vianet?**

- a) 26 de mayo de 2025
- b) 16 de febrero de 2026
- c) 31 de agosto de 2025  ✅
- d) 15 de octubre de 2027

*Respuesta: c).* El retiro completo fue el 31 de agosto de 2025. El 26 de mayo de 2025 se retiraron Content Search clásica y los casos Standard; el 16 de febrero de 2026 se limitaron las content searches, y el 15 de octubre de 2027 se retira Search-UnifiedAuditLog. [Fuente](https://learn.microsoft.com/en-us/purview/ediscovery) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**3. ¿Quién puede quitar miembros de un caso de eDiscovery?**

- a) La persona que creó el caso
- b) Cualquier eDiscovery Manager que sea miembro del caso
- c) Un integrante de Organization Management
- d) Un eDiscovery Administrator  ✅

*Respuesta: d).* eDiscovery Administrator ve todos los casos, configura la solución y es el único que puede quitar miembros. eDiscovery Manager solo trabaja en los casos donde es miembro. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**4. Un custodio tiene Microsoft 365 E3 sin complementos. ¿Qué hace falta para analizar sus datos con funciones premium?**

- a) Nada: basta con que quien revisa tenga E5
- b) Que el custodio tenga Purview Suite o el complemento «eDiscovery and Audit»  ✅
- c) Una licencia de Security Copilot para el custodio
- d) Que el caso lo cree un eDiscovery Administrator

*Respuesta: b).* La licencia premium la necesita el custodio cuyos datos se analizan: E5, o E1/E3 con Purview Suite o «eDiscovery and Audit». Los miembros del caso que recolectan y revisan no necesitan E5. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. En una búsqueda de eDiscovery, ¿qué significa un espacio entre dos términos?**

- a) AND
- b) NEAR
- c) Frase exacta
- d) OR  ✅

*Respuesta: d).* Un espacio equivale a OR. Para exigir ambos términos usa AND en mayúsculas y, para una frase exacta, comillas. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**6. ¿Qué devuelve una condición vacía en una búsqueda de eDiscovery?**

- a) Ningún resultado
- b) Todo el contenido del alcance de la búsqueda  ✅
- c) Solo los ítems parcialmente indexados
- d) Un error de sintaxis

*Respuesta: b).* Una condición vacía no filtra nada: devuelve todo el alcance, con el riesgo de exponer contenido y de exportar de más. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-query) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**7. ¿Qué necesitas para que las estadísticas de una búsqueda muestren el keyword report?**

- a) Al menos dos cuadrículas de palabras clave  ✅
- b) Una licencia de Security Copilot
- c) Agregar los resultados a un review set
- d) Escribir la consulta en KQL

*Respuesta: a).* El keyword report aparece cuando la consulta tiene al menos dos cuadrículas de palabras clave; al convertirla a KeyQL, las cuadrículas se separan con c:s. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-condition-builder) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**8. ¿Cuántos trabajos de búsqueda de auditoría simultáneos puede tener un usuario?**

- a) Tres
- b) Cinco
- c) Diez  ✅
- d) Cincuenta

*Respuesta: c).* Hasta diez trabajos simultáneos por usuario, solo uno de ellos sin filtros; los resultados se conservan 30 días y los trabajos siguen corriendo aunque cierres el navegador. [Fuente](https://learn.microsoft.com/en-us/purview/audit-search) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. Hoy creas una política de retención de auditoría de un año. ¿Qué pasa con los registros que ya vencieron?**

- a) Se recuperan los de los últimos doce meses
- b) Nada: los cambios no son retroactivos  ✅
- c) Se recuperan solo los de usuarios con E5
- d) Se recuperan si agregas el complemento de 10 años

*Respuesta: b).* Los cambios en las políticas de retención de auditoría no son retroactivos. Por eso la retención se decide antes del incidente o del requerimiento. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**10. ¿Qué hace falta para usar funciones de pago por uso de Purview, como Data Security Investigations?**

- a) Tener Microsoft 365 E7
- b) Activar Audit (Premium)
- c) Comprar SCU de Security Copilot
- d) Asociar el tenant a una suscripción de Azure activa  ✅

*Respuesta: d).* El pago por uso se factura en Azure y exige asociar el tenant a una suscripción activa. No depende de E7, de Audit (Premium) ni de Security Copilot. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-models) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**11. ¿Qué es Microsoft Purview Suite?**

- a) El nuevo nombre de Microsoft 365 E5 Compliance: un complemento sobre E3 que incluye Audit y eDiscovery  ✅
- b) Un plan de pago por uso para Data Security Investigations
- c) Una edición gratuita de Purview para tenants E3
- d) El paquete de Security Copilot para Purview

*Respuesta: a).* Microsoft 365 E5 Compliance pasó a llamarse Microsoft Purview Suite, sin cambio funcional. Se agrega a Microsoft 365 E3 y ya viene incluido en Microsoft 365 E5. [Fuente](https://www.microsoft.com/en-us/security/microsoft-purview-pricing) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**12. Para usuarios con licencias E3 y E5, ¿en qué nivel de auditoría está el evento MailItemsAccessed?**

- a) Solo en Audit (Premium)
- b) Solo con el complemento de 10 años
- c) En Audit (Standard)  ✅
- d) Solo con pago por uso

*Respuesta: c).* MailItemsAccessed forma parte de Audit (Standard) para usuarios E3 y E5; Audit (Premium) le agrega propiedades como SensitivityLabel y una retención más larga. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**13. No existe un «Audit Ninja» oficial. ¿Qué recurso oficial es lo más cercano?**

- a) La ruta de Learn «Audit and search activity in Microsoft Purview», alineada con SC-401  ✅
- b) Los escenarios Ninja de Information Protection y DLP en Learn
- c) El módulo de MS-101 sobre Audit (Premium)
- d) El Ninja de Communication Compliance

*Respuesta: a).* La ruta «Audit and search activity in Microsoft Purview» (cerca de 1 h 31 min) cubre investigaciones con Audit y búsquedas con eDiscovery. El módulo de MS-101 es heredado y los otros Ninja tratan otras soluciones. [Fuente](https://learn.microsoft.com/en-us/training/paths/purview-audit-search/) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**14. ¿Dónde se usa un subconjunto de KQL (Kusto) dentro de eDiscovery?**

- a) En el editor de búsquedas del caso
- b) En el generador de condiciones de los holds
- c) En la configuración de la exportación
- d) En el explorador avanzado de review sets (vista previa)  ✅

*Respuesta: d).* Las búsquedas del caso usan KeyQL. El explorador avanzado de review sets, en vista previa, ejecuta un subconjunto de Kusto sobre ReviewSetTable. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**15. ¿Qué grupo de roles permite buscar en la auditoría sin poder cambiar su configuración?**

- a) Audit Manager
- b) Audit Reader  ✅
- c) eDiscovery Administrator
- d) Organization Configuration

*Respuesta: b).* Audit Reader tiene el rol View-Only Audit Logs. Audit Manager tiene Audit Logs, que también permite administrar la configuración, y Organization Configuration se usa para las políticas de retención de auditoría. [Fuente](https://learn.microsoft.com/en-us/purview/audit-get-started) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Preservar, revisar, investigar y producir

**1. ¿Cuánto puede tardar una política de hold de eDiscovery en aplicarse?**

- a) Hasta una hora
- b) Hasta 24 horas  ✅
- c) Hasta siete días
- d) Se aplica al instante

*Respuesta: b).* Un hold puede tardar hasta 24 horas en aplicarse: créalo antes de anunciar el asunto y verifica su estado antes de dar por preservado a un custodio. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. Creas un hold sobre un grupo de Microsoft 365 y al día siguiente se suma una persona al grupo. ¿Qué ocurre?**

- a) Queda retenida automáticamente
- b) Queda retenida solo si tiene E5
- c) No queda retenida: la membresía se tomó como instantánea al crear la política  ✅
- d) El hold se suspende hasta volver a aplicarlo

*Respuesta: c).* La membresía del grupo se captura al crear la política; las altas posteriores no quedan retenidas hasta que actualices el hold. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. Con funciones premium, ¿cuántos buzones admite como máximo una política de hold de caso?**

- a) 100
- b) 1.000
- c) 10.000
- d) 2.000  ✅

*Respuesta: d).* Con funciones premium, 2.000 buzones y 2.000 sitios por hold de caso; con funciones estándar, 1.000 de cada uno. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. Un hold de eDiscovery es lo único que mantiene un buzón inactivo. ¿Qué pasa si liberas el hold o cierras el caso?**

- a) El buzón inactivo se elimina  ✅
- b) El buzón vuelve a estar activo
- c) El buzón queda retenido 180 días más
- d) Nada cambia

*Respuesta: a).* Si ningún otro hold o retención lo mantiene, el buzón inactivo se elimina. Por eso la liberación se verifica antes en el procedimiento. [Fuente](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿Qué ocurre al agregar los resultados de una búsqueda a un review set?**

- a) Los ítems se mueven fuera del buzón original
- b) La búsqueda se vuelve a ejecutar y los ítems se copian a almacenamiento de Azure gestionado por Microsoft, donde se reindexan  ✅
- c) Se crea un vínculo a los ítems sin copiarlos
- d) Se exportan automáticamente a PST

*Respuesta: b).* Al agregar, la búsqueda se vuelve a ejecutar y los ítems se copian al almacenamiento del caso y se reindexan; los originales no se mueven. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**6. ¿Cómo eliminas ítems o un review set completo?**

- a) Desde el menú del review set
- b) Con el rol Search And Purge
- c) Esperando 30 días a que expire
- d) Solo eliminando el caso completo  ✅

*Respuesta: d).* No se pueden borrar ítems ni review sets; solo desaparecen al eliminar el caso. Ese carácter estático favorece la cadena de custodia. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-manage) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. ¿Qué rol necesitas para procesar adjuntos cifrados al agregarlos a un review set?**

- a) Reviewer
- b) Search And Purge
- c) Audit Reader
- d) RMS Decrypt  ✅

*Respuesta: d).* RMS Decrypt permite descifrar el contenido protegido al agregarlo a un review set o al exportarlo. Asígnalo solo a quien lo necesite en cada asunto. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Cada cuánto se agregan los accesos bind de MailItemsAccessed?**

- a) Cada minuto
- b) Cada cinco minutos
- c) Cada dos minutos  ✅
- d) Cada hora

*Respuesta: c).* Los accesos bind se agregan en ventanas de dos minutos e incluyen el InternetMessageId de cada mensaje; los sync se registran por carpeta. [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**9. Según Microsoft, ¿cuánto puede crecer el volumen del registro de auditoría hacia el SIEM con los registros ampliados?**

- a) Hasta 10 veces  ✅
- b) Hasta 2 veces
- c) Hasta 100 veces
- d) No cambia

*Respuesta: a).* Microsoft advierte que los registros ampliados pueden multiplicar hasta 10 veces el volumen hacia el SIEM: estima el costo antes de habilitar la ingesta completa. [Fuente](https://techcommunity.microsoft.com/blog/publicsectorblog/cisa-omb-oncd-and-microsoft-collaborate-on-new-logging-playbook-for-federal-agen/4063661) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**10. ¿Qué evento de búsqueda de Exchange no viene habilitado por defecto y se activa buzón por buzón?**

- a) MailItemsAccessed
- b) SearchQueryInitiatedExchange  ✅
- c) Send
- d) FileAccessed

*Respuesta: b).* SearchQueryInitiatedExchange se habilita por buzón; el de SharePoint viene habilitado. Decide con privacidad sobre quién se activa. [Fuente](https://learn.microsoft.com/en-us/purview/audit-get-started) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. En un compromiso de correo, ¿qué conviene hacer antes de eliminar las reglas de reenvío creadas por el atacante?**

- a) Preservar la evidencia: hold sobre el buzón y exportación de la auditoría con hash  ✅
- b) Desactivar la auditoría del buzón para no generar ruido
- c) Purgar los mensajes que envió el atacante
- d) Esperar a que la auditoría cumpla 180 días

*Respuesta: a).* La contención no espera, pero la erradicación sí: preservar primero conserva la prueba del alcance que Legal necesitará para decidir notificaciones. [Fuente](https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. Desde el 16 de febrero de 2026, ¿cuándo expiran los paquetes de exportación de búsquedas?**

- a) A los 7 días
- b) A los 30 días
- c) Nunca
- d) A los 14 días  ✅

*Respuesta: d).* Expiran 14 días después de su creación. El cambio no afecta a las exportaciones de review sets. [Fuente](https://mc.merill.net/message/MC1217141) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**13. Exportas un review set con redacciones confirmadas. ¿Qué recibe el destinatario por cada documento redactado?**

- a) El nativo y el PDF
- b) El PDF redactado (_burn.pdf) en lugar del nativo  ✅
- c) Nada: los ítems redactados no se exportan
- d) Solo el informe de ítems

*Respuesta: b).* Con redacciones confirmadas, la exportación reemplaza el nativo por el PDF redactado _burn.pdf. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**14. ¿Qué pasa con una exportación que dura más de siete días?**

- a) Se pausa hasta que la reanudes
- b) Se divide en paquetes de 40 GB
- c) Se cancela  ✅
- d) Se completa en archivos PST de 10 GB

*Respuesta: c).* Una exportación que supera siete días se cancela; planifica lotes que terminen antes. Los paquetes de 40 GB y los PST de 10 GB son límites de formato, no una salida al plazo. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. ¿Dentro de qué plazo hay que descargar una exportación de review set?**

- a) 14 días
- b) 7 días
- c) 30 días  ✅
- d) 90 días

*Respuesta: c).* Las exportaciones de review set se retienen durante la vida del caso, pero hay que descargarlas dentro de 30 días; los 14 días aplican a las exportaciones de búsquedas. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-export) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, automatización y SOC

**1. ¿Dónde se guardan los prompts y respuestas de Copilot que eDiscovery puede buscar, retener y exportar?**

- a) En el OneDrive del usuario
- b) En el workspace de Sentinel
- c) En el buzón del usuario  ✅
- d) En el review set del caso

*Respuesta: c).* Prompts y respuestas de Copilot y de otras apps de IA se guardan en el buzón del usuario, identificados por clase de ítem; por eso eDiscovery los trata como cualquier otro contenido. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. ¿Qué rol se requiere para eliminar datos de IA con el flujo de búsqueda y eliminación de eDiscovery?**

- a) eDiscovery Manager
- b) Audit Reader
- c) Reviewer
- d) Search And Purge  ✅

*Respuesta: d).* Search And Purge permite eliminar el contenido que coincide con la búsqueda, hasta 10 ítems por buzón por vez y retirando antes holds y retención. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. La auditoría de interacciones con apps de IA no Microsoft (AIAppInteraction)…**

- a) …está incluida en E5 sin costo adicional
- b) …requiere pago por uso y se retiene 180 días  ✅
- c) …requiere Audit (Premium) y se retiene un año
- d) …no se audita

*Respuesta: b).* Las apps de IA de Microsoft se auditan en Audit (Standard); las no Microsoft se facturan por uso y se retienen 180 días. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. En un registro de auditoría de Copilot, ¿qué propiedad de los recursos consultados señala una posible inyección de instrucciones?**

- a) AgentId
- b) AppAccessContext
- c) XPIADetected  ✅
- d) InternetMessageId

*Respuesta: c).* AccessedResources incluye SensitivityLabelId y XPIADetected. AgentId identifica a un agente, AppAccessContext es una propiedad de Teams y InternetMessageId identifica mensajes en MailItemsAccessed. [Fuente](https://learn.microsoft.com/en-us/purview/audit-copilot) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Qué reemplaza a Search-UnifiedAuditLog, que se retira el 15 de octubre de 2027?**

- a) La API AuditLogQuery de Microsoft Graph  ✅
- b) La Management Activity API
- c) Get-AdminAuditLogConfig
- d) Content Search

*Respuesta: a).* AuditLogQuery llegó a disponibilidad general en octubre de 2026. La Management Activity API sigue existiendo, pero para suscripciones hacia un SIEM. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**6. ¿Cuál de estos es un límite documentado de AuditLogQuery por tenant?**

- a) Diez consultas por día
- b) Mil registros por consulta
- c) Una consulta en cola por usuario
- d) 200 envíos cada 24 horas  ✅

*Respuesta: d).* Cada tenant admite 200 envíos cada 24 horas y 50 consultas en cola o en ejecución (HTTP 429 al exceder); cada consulta devuelve hasta un millón de registros. [Fuente](https://mc.merill.net/message/MC1505599) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. Con E3 y permisos delegados, ¿qué automatizas con la API de eDiscovery de Graph sin pago adicional?**

- a) Casos, búsquedas y holds  ✅
- b) Review sets y analítica
- c) Autenticación solo aplicación
- d) Descargas masivas

*Respuesta: a).* Con E3 delegado: casos, búsquedas y holds. Exportar con E3 requiere pago por uso; review sets, analítica y solo aplicación requieren E5, y la API no está pensada para descargas masivas. [Fuente](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. Desde agosto de 2026, ¿qué no admiten los cmdlets de eDiscovery de Security & Compliance PowerShell?**

- a) La creación de holds
- b) La autenticación solo aplicación  ✅
- c) Las búsquedas
- d) La purga

*Respuesta: b).* La autenticación solo aplicación dejó de estar soportada en esos cmdlets: los procesos desatendidos deben migrar a Microsoft Graph. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. En la Management Activity API, ¿cuánto puede tardar el primer blob después de crear una suscripción?**

- a) Cinco minutos
- b) Una hora
- c) Hasta 12 horas  ✅
- d) Siete días

*Respuesta: c).* El primer blob puede tardar hasta 12 horas y los eventos no llegan en orden: el SIEM debe ordenar por marca de tiempo. [Fuente](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**10. ¿Qué tabla de Sentinel contiene la auditoría de Exchange, SharePoint y Teams?**

- a) SigninLogs
- b) AzureActivity
- c) CloudAppEvents
- d) OfficeActivity  ✅

*Respuesta: d).* OfficeActivity reúne la auditoría de Exchange, SharePoint y Teams. CloudAppEvents es una tabla de la búsqueda avanzada de Defender XDR. [Fuente](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/officeactivity) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. ¿Qué advierte el conector de Purview Information Protection para Sentinel (vista previa)?**

- a) Que solo funciona con Audit (Premium)
- b) Que, si el workspace está en otra región que Office 365, los datos pueden transmitirse entre regiones  ✅
- c) Que no admite el nivel data lake
- d) Que requiere Security Copilot

*Respuesta: b).* La advertencia de transmisión entre regiones convierte la ubicación del workspace en una decisión de privacidad. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Cómo se licencia Data Security Investigations?**

- a) Incluida en Microsoft 365 E5
- b) Complemento por usuario
- c) Pago por uso de almacenamiento y Compute Units  ✅
- d) Solo con capacidad aprovisionada de Security Copilot

*Respuesta: c).* DSI no requiere licencia dedicada: se factura por almacenamiento (GB al mes) y por Data Security Investigations Compute Units. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**13. ¿Dónde puede ejecutarse el cómputo de IA de Data Security Investigations?**

- a) Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»  ✅
- b) En la región del tenant, incluida Latinoamérica
- c) Solo en EE. UU.
- d) En el workspace de Sentinel

*Respuesta: a).* No hay opción en Latinoamérica: la elección de ubicación es una decisión para Legal y privacidad en cada país. [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Qué afirmación sobre Security Copilot en eDiscovery es correcta?**

- a) Puede ver todos los casos aunque el usuario no sea miembro
- b) Requiere el rol eDiscovery Administrator
- c) Ejecuta exportaciones automáticamente
- d) Actúa en nombre del usuario y nunca excede sus permisos  ✅

*Respuesta: d).* Security Copilot usa autenticación en nombre del usuario: solo ve lo que el usuario puede ver en Purview. Sus roles owner y contributor no son roles de Entra. [Fuente](https://learn.microsoft.com/en-us/copilot/security/authentication) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Modelo operativo, métricas y gobierno

**1. ¿Qué etapas agrupa EDRM 2.0 bajo «Data Acquisition»?**

- a) Revisión, análisis y producción
- b) Identificación, preservación, recolección y procesamiento  ✅
- c) Disposición y gobierno de la información
- d) Presentación y producción

*Respuesta: b).* EDRM 2.0 (1 de septiembre de 2026) agrupa identificación, preservación, recolección y procesamiento en «Data Acquisition», agrega la disposición y se apoya en el IGRM. [Fuente](https://edrm.net/edrm-model/current/) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué publicación de NIST reemplazó en abril de 2025 a la SP 800-61 Rev. 2?**

- a) SP 800-53 Rev. 5
- b) CSF 2.0
- c) SP 800-61 Rev. 3  ✅
- d) SP 800-86

*Respuesta: c).* SP 800-61 Rev. 3 reemplazó a la Rev. 2 y alinea la respuesta a incidentes con CSF 2.0. [Fuente](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. Desde julio de 2026 las asignaciones a grupos de roles de Purview admiten fecha de expiración. ¿Cuáles quedan excluidas?**

- a) Audit Reader y Audit Manager
- b) eDiscovery Administrator y eDiscovery Manager  ✅
- c) Organization Configuration
- d) Reviewer

*Respuesta: b).* eDiscovery Administrator y eDiscovery Manager no admiten fecha de expiración: contrólalos con PIM para grupos y revisiones de acceso. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. ¿Por qué conviene mantener pequeño el grupo eDiscovery Administrator?**

- a) Porque consume licencias E5 adicionales
- b) Porque solo admite cinco miembros
- c) Porque su actividad no se audita
- d) Porque accede a todos los casos y a sus datos  ✅

*Respuesta: d).* eDiscovery Administrator ve todos los casos y sus datos sensibles. Su actividad sí se audita y no tiene un límite de cinco miembros. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-permissions) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Qué dato registran en Audit las actividades de la experiencia unificada de eDiscovery y faltaba en las heredadas?**

- a) La dirección IP del cliente  ✅
- b) El hash del paquete exportado
- c) El nombre del abogado responsable
- d) El consumo de SCU

*Respuesta: a).* Las actividades de la experiencia unificada incluyen la IP del cliente; un IP vacío indica la experiencia heredada. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**6. ¿Qué anunció MC1473155 para fines de septiembre y octubre de 2026?**

- a) El retiro de Audit (Standard)
- b) Nuevas operaciones de auditoría de RBAC en Purview  ✅
- c) La expiración de exportaciones a 14 días
- d) La disponibilidad general de AuditLogQuery

*Respuesta: b).* MC1473155 agrega operaciones como CheckUsersInRoles y CheckUserInRolesWithScopes, útiles para vigilar quién obtiene permisos; no son retroactivas. [Fuente](https://mc.merill.net/message/MC1473155) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. ¿Dónde ves el consumo de pago por uso de Purview por función?**

- a) En el Usage center de Purview (vista previa)  ✅
- b) En el panel de SCU de Security Copilot
- c) En la tabla OfficeActivity
- d) En el review set del caso

*Respuesta: a).* El Usage center muestra el consumo de pago por uso por función; el panel de Security Copilot muestra SCU, que es otra capacidad. [Fuente](https://learn.microsoft.com/en-us/purview/purview-billing-usage) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Dónde se aprovisiona el almacenamiento de un review set?**

- a) En la región del workspace de Sentinel
- b) En una cuenta de Azure Storage del cliente
- c) En la geografía del caso, con soporte de Customer Key  ✅
- d) En el OneDrive del eDiscovery Manager

*Respuesta: c).* El almacenamiento del review set lo gestiona Microsoft, se aprovisiona en la geografía del caso, admite Customer Key y no ofrece acceso directo por SAS. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**9. ¿Cuándo entra en vigencia la Ley 21.719 de protección de datos personales de Chile?**

- a) 13 de diciembre de 2024
- b) 20 de marzo de 2025
- c) 1 de diciembre de 2026  ✅
- d) 15 de octubre de 2027

*Respuesta: c).* Se publicó en diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026, con reglas de transferencia internacional. El 20 de marzo de 2025 corresponde a la nueva LFPDPPP de México. [Fuente](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**10. Legal duda si entregar una exportación a un estudio jurídico de otro país es una transferencia internacional. ¿Qué corresponde según esta guía?**

- a) Decidirlo según la región del tenant
- b) Llevar la pregunta a Legal y privacidad con la evidencia técnica y las fuentes oficiales  ✅
- c) Exportar primero y notificar después
- d) Procesarla en DSI con ubicación «en cualquier lugar»

*Respuesta: b).* La guía no interpreta la ley: aporta el dato técnico (qué sale, adónde y cuándo vence) y la pregunta va a Legal y privacidad, con la norma oficial de cada país. [Fuente](https://www.bcn.cl/leychile/N?i=1209272&f=2026-12-01) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**11. ¿Qué permite restringir las búsquedas de un equipo de eDiscovery a un país o a una empresa del grupo?**

- a) Las Compute Units de DSI
- b) Las etiquetas de retención
- c) El rol Reviewer
- d) Los límites de cumplimiento (filtros de permisos de búsqueda)  ✅

*Respuesta: d).* Los límites de cumplimiento usan filtros de permisos de búsqueda por atributo (país, subsidiaria) y aplican también a Data Security Investigations. [Fuente](https://learn.microsoft.com/en-us/purview/edisc-compliance-boundaries) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Qué consecuencia tiene la limpieza prioritaria (vista previa) para eDiscovery?**

- a) El contenido eliminado deja de ser descubrible  ✅
- b) El contenido pasa a un review set
- c) Se crea un hold automático
- d) Solo afecta a registros regulatorios

*Respuesta: a).* La limpieza prioritaria puede eliminar contenido aunque esté retenido, y lo eliminado deja de ser descubrible. No aplica a registros ni a registros regulatorios. [Fuente](https://learn.microsoft.com/en-us/purview/priority-cleanup-exchange) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. Desde julio de 2026, ¿qué aprobaciones exige la limpieza prioritaria?**

- a) Una, del Global Administrator
- b) Dos, de cualquier administrador de Purview
- c) Tres: limpieza prioritaria, retención y eDiscovery  ✅
- d) Ninguna si antes se ejecutó la simulación

*Respuesta: c).* Las novedades de julio de 2026 exigen tres aprobaciones separadas; avisos anteriores hablaban de dos administradores. Inclúyelo en el procedimiento y en el registro de decisiones. [Fuente](https://learn.microsoft.com/en-us/purview/whats-new) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="laboratorio-y-practica"></a>

## Laboratorio y práctica


Este archivo responde tres preguntas para este programa: qué puedes practicar en el entorno de laboratorio, qué requiere producción (y por qué), y cómo hacerlo con riesgo controlado. La guía para construir el entorno con los créditos de Azure de Visual Studio Enterprise y una prueba de Microsoft 365 E5 está en el [anexo común](../Anexo_Entorno_de_practica.md).

**Tu entorno.** Una prueba de Microsoft 365 E5 (un mes, 25 licencias) incluye las funciones premium de eDiscovery y Audit (Premium); si tu organización parte de E3, la [prueba de Microsoft Purview Suite](https://learn.microsoft.com/en-us/purview/purview-trial) asigna 25 licencias durante 90 días. Suma una suscripción de Azure con los créditos de Visual Studio Enterprise para lo que se factura por uso —auditoría de apps de IA no Microsoft, Data Security Investigations, exportaciones por Graph con E3 y un workspace de Sentinel— y asóciala al tenant como indica el [modelo de facturación](https://learn.microsoft.com/en-us/purview/purview-billing-models). En tenants de prueba la auditoría puede venir apagada: actívala el día 0, porque tarda hasta 60 minutos y los eventos pueden demorar horas en ser buscables ([activar la auditoría](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable)).

**Datos y nombres de práctica.** Crea cuentas, buzones, OneDrive, un sitio y un equipo de Teams con contenido sintético (por ejemplo, un «Proyecto Cóndor» con correos, adjuntos y chats fechados) y anota lo que siembras: será tu verdad de referencia para medir la precisión de las búsquedas. Nombra todo con el prefijo `PRUEBA-` y registra cada ejercicio como un cambio.

**Qué no se puede practicar en el laboratorio.** Holds y exportaciones a escala (miles de custodios o terabytes), interacciones reales de Microsoft 365 Copilot (sus licencias no vienen en la prueba E5), la inclusión de Security Copilot (aplica a licencias E5 pagadas), el complemento de retención de auditoría de 10 años, Data Security Investigations sobre datos reales, multigeografía y notificaciones de retención legal a custodios reales. Para esos casos, cada ejercicio describe la forma segura de practicar en producción.

**Costos a vigilar.** Almacenamiento y unidades de cómputo de Data Security Investigations (las insights proactivas consumen de forma continua), auditoría por uso de apps de IA no Microsoft, exportaciones por Graph con pago por uso, SCU de Security Copilot fuera del pool incluido e ingesta en el SIEM: los registros ampliados pueden multiplicar el volumen. Configura presupuestos y alertas al 50, 75 y 90 % antes del primer ejercicio y revisa el [Usage center](https://learn.microsoft.com/en-us/purview/purview-billing-usage) (vista previa).

**Práctica en producción, siempre con Legal.** En eDiscovery, practicar en producción significa tocar datos de personas: usa cuentas y buzones de prueba, casos rotulados como entrenamiento, roles asignados justo a tiempo con [PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure), ninguna exportación de contenido real y la aprobación previa de Legal, RR. HH. y privacidad. Tu propia actividad queda en el registro de auditoría ([actividades de eDiscovery en Audit](https://learn.microsoft.com/en-us/purview/edisc-ref-audit-log)): úsala como evidencia de que practicaste dentro de lo acordado.

**Limpieza.** Libera los holds, cierra y elimina los casos de práctica (los review sets solo se eliminan con el caso), borra las investigaciones de Data Security Investigations, revoca secretos y registros de aplicaciones, quita los roles temporales y desasocia la facturación por uso si no la vas a seguir usando. Ojo: si un hold de eDiscovery es lo único que mantiene un buzón inactivo, liberarlo o cerrar el caso elimina ese buzón ([buzones inactivos](https://learn.microsoft.com/en-us/purview/change-the-hold-duration-for-an-inactive-mailbox)).

<a id="matriz-laboratorio"></a>

## Matriz de laboratorio y producción

| Capacidad | ¿Laboratorio? | Requisito o limitación | Cómo practicar en producción | Riesgo | Mitigación | Fuente |
|---|---|---|---|---|---|---|
| Casos, búsquedas KeyQL y estadísticas | Sí | Disponible en trial E5 o sandbox; una condición vacía devuelve todo el alcance. | Casos de práctica con nombre PRUEBA- y fuentes limitadas a cuentas de prueba. | Búsquedas amplias que exponen contenido sensible a quien practica. | Rol eDiscovery Manager en lugar de Administrator y límites de cumplimiento. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-query) |
| Holds de eDiscovery | Sí | Un hold tarda hasta 24 h en aplicarse y toma la membresía del grupo como instantánea. | Hold sobre cuentas de prueba con procedimiento de liberación documentado. | Holds olvidados que retienen datos indefinidamente. | Inventario de holds con responsable y fecha de revisión. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-create) |
| Impacto de los holds en el almacenamiento | Parcial | Con hold, la cuota de Elementos recuperables sube de 30 a 100 GB; sin archivo habilitado puede llenarse. | Monitorea Elementos recuperables de los buzones bajo hold. | Buzones llenos y crecimiento de almacenamiento retenido. | Archivo habilitado y alertas de cuota. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-hold-increase-recoverable-item-quota) |
| Conjuntos de revisión y analítica | Sí | No se pueden borrar elementos ni conjuntos de revisión salvo eliminando el caso. | Caso de práctica separado que se elimina al terminar. | Copias de contenido sensible en el almacenamiento del caso. | Eliminación del caso de práctica y acceso mínimo. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-review-set-manage) |
| Exportación y cadena de custodia | Sí | Los paquetes de exportación de búsquedas expiran a los 14 días. | Exporta solo datos de prueba y registra responsable, fecha y verificación. | Exportaciones guardadas en equipos personales. | Equipos administrados, cifrado y formulario de custodia. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-export) |
| Audit Standard y Premium y retención de auditoría | Sí | La auditoría viene apagada en tenants de prueba no administrados y los eventos tardan horas en ser buscables. | Directivas de retención de auditoría para usuarios de prueba. | Desactivar la auditoría por error. | Alerta ante cambios de configuración de auditoría. | [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable) |
| Automatización con Microsoft Graph | Sí | La API de eDiscovery con permisos de aplicación requiere E5, disponible en el trial. | App registrada con permisos mínimos y secretos en Key Vault. | Una app con permisos amplios accede a todo el contenido. | Permisos mínimos, rotación de secretos y revisión de consentimientos. | [Fuente](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0) |
| Búsqueda y purga de interacciones de Copilot | Parcial | Requiere usuarios con Copilot y el rol Search And Purge; purga hasta 10 elementos por buzón por vez. | Cuenta de prueba y rol asignado temporalmente con PIM. | Purgar contenido equivocado o bajo hold. | Doble aprobación, verificación de holds y registro en auditoría. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data) |
| Security Copilot en eDiscovery | Parcial | Consume SCU; la inclusión de SCU depende de licencias E5 pagadas. | Caso piloto con datos de prueba y monitoreo de consumo. | Consumo no previsto y resúmenes inexactos. | Validación humana y límite de unidades de exceso. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc) |
| Data Security Investigations | Parcial | Pago por uso (GB/mes y unidades de cómputo), suscripción de Azure en el mismo tenant y Global Administrator para configurar. | Alcance de 1-2 buzones de prueba y estimador de costos previo. | Costos continuos y procesamiento de IA fuera de la región. | Borrado de investigaciones al terminar, alertas de presupuesto y elección de ubicación con Privacidad. | [Fuente](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing) |
| Holds y límites a escala | No | Requiere miles de custodios y volumen real. | Rol de solo lectura y hold sobre un grupo piloto. | Superar límites por caso o por hold. | Diseño de holds por consulta y revisión de límites. | [Fuente](https://learn.microsoft.com/en-us/purview/edisc-ref-limits) |
| Investigación de cuentas comprometidas con auditoría (MailItemsAccessed) y Sentinel | Parcial | La simulación de un BEC con cuentas de prueba es viable; la ingesta en Sentinel consume créditos de Azure y el volumen es bajo. | Consultas de solo lectura sobre la auditoría real con los roles Audit Reader o View-Only Audit Logs. | Acceso amplio a la actividad de todos los usuarios. | Rol de solo lectura, justificación por consulta y revisión de las búsquedas en auditoría. | [Fuente](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts) |

## Principios para practicar en producción

1. **Primero observar, después actuar.** Usa los modos de solo informe, auditoría o simulación antes de cualquier bloqueo o acción automática.
2. **Alcance mínimo.** Grupos piloto, usuarios y dispositivos de prueba etiquetados, unidades administrativas y ámbitos adaptables pequeños.
3. **Privilegio justo a tiempo.** Roles de solo lectura para estudiar y activación con PIM, aprobación y justificación para cambiar.
4. **Cuentas de emergencia excluidas y monitoreadas.** Nunca practiques acceso condicional o protección de identidad sin cuentas de emergencia probadas.
5. **Cambio registrado y reversible.** Cada práctica tiene responsable, ventana, criterio de éxito, plan de reversión y limpieza al terminar.
6. **Privacidad y áreas de negocio.** Para riesgo interno, comunicaciones o eDiscovery, acuerda con RR. HH., Legal y privacidad antes de crear políticas, aunque sean de prueba.

<a id="ejercicios"></a>

## Índice de ejercicios

Resumen: Laboratorio: 53, Laboratorio parcial: 21, Solo producción: 13, Sin etiqueta: 6.

| Módulo | N.º | Entorno | Ejercicio |
|---|---|---|---|
| [P0](01_Nivel_1_Inicial.md#p0) | 1 | Laboratorio | Verifica la auditoría el día 0: en Exchange Online PowerShell ejecuta `Get-AdminAuditLogConfig \| Format-List UnifiedAuditLogIngestionEnabled`; si devuelve False, actívala desde el portal de Purview y anota la hora.… |
| [P0](01_Nivel_1_Inicial.md#p0) | 2 | Laboratorio | Asigna roles con mínimo privilegio a tres cuentas de prueba: Audit Reader a la persona del SOC, eDiscovery Manager a la gestora de eDiscovery y ningún rol de Purview a la persona custodia. Comprueba que Audit Reader… |
| [P0](01_Nivel_1_Inicial.md#p0) | 3 | Laboratorio | Arma la matriz de licencias de tu laboratorio: por cada cuenta de prueba, su licencia, si sus datos admiten funciones premium como custodio y cuánto se retiene su auditoría. Usa la tabla Licencias de esta guía y… |
| [P0](01_Nivel_1_Inicial.md#p0) | 4 | Laboratorio | Con un Global Administrator, asocia el tenant a tu suscripción de Azure de Visual Studio Enterprise en un grupo de recursos exclusivo para Purview, crea un presupuesto con alertas al 50, 75 y 90 % y abre el Usage… |
| [P0](01_Nivel_1_Inicial.md#p0) | 5 | Solo producción | Haz el inventario real de licencias: cuenta usuarios con E3, E5, Purview Suite y el complemento «eDiscovery and Audit», y crúzalo con los perfiles que suelen ser custodios (dirección, finanzas, compras, Legal). Cómo… |
| [I0](01_Nivel_1_Inicial.md#i0) | 1 | Laboratorio | Abre la guía de estudio de SC-401 y lleva a una tabla las cuatro habilidades de Audit y eDiscovery del bloque «Manage risks, alerts, and activities», con el módulo de esta guía que cubre cada una. Evidencia: tabla de… |
| [I0](01_Nivel_1_Inicial.md#i0) | 2 | Laboratorio | Completa la ruta Audit and search activity in Microsoft Purview (cerca de 1 h 31 min) y guarda el logro en tu perfil de Learn. Evidencia: captura del logro y tres dudas que quieras resolver en esta guía. |
| [I0](01_Nivel_1_Inicial.md#i0) | 3 | Laboratorio | Mira el webinar oficial del flujo moderno de eDiscovery (26 de agosto de 2025) con tu tenant abierto y anota, con su minuto, tres pantallas u opciones que hoy se vean distintas. Evidencia: notas con minuto y captura… |
| [I0](01_Nivel_1_Inicial.md#i0) | 4 | Laboratorio | Crea tu registro de cambios: un recordatorio mensual para What's new in Microsoft Purview y una primera entrada con tres novedades de 2026 que afecten a eDiscovery o Audit, cada una con fecha, estado y módulo de esta… |
| [I0](01_Nivel_1_Inicial.md#i0) | 5 | Laboratorio | Desde el portal de adopción de Purview ubica el Ninja de eDiscovery, la guía interactiva y la credencial Applied Skills, y escribe tu plan personal: credencial objetivo, fecha y módulos de esta guía por semana.… |
| [I1](01_Nivel_1_Inicial.md#i1) | 1 | Laboratorio | Crea el caso `PRUEBA-001` con una convención de nombres y un dueño. Agrega como miembros a la gestora de eDiscovery y a un grupo de seguridad habilitado para correo, y verifica con una segunda cuenta eDiscovery… |
| [I1](01_Nivel_1_Inicial.md#i1) | 2 | Laboratorio | Recorre los cinco pasos del flujo de eDiscovery con una solicitud simulada de Legal: evento disparador, caso, búsqueda sobre un usuario y un equipo de Teams, estadísticas y una muestra. Evidencia: solicitud simulada,… |
| [I1](01_Nivel_1_Inicial.md#i1) | 3 | Laboratorio | Abre el caso de Content Search generado por el sistema, ejecuta una búsqueda e intenta crear un hold o agregar resultados a un review set. Documenta que, desde el 16 de febrero de 2026, ese caso solo busca y exporta… |
| [I1](01_Nivel_1_Inicial.md#i1) | 4 | Laboratorio parcial | Comprueba la regla de licencia por custodio: en una búsqueda sobre un custodio con E5 confirma que las funciones premium están disponibles y documenta qué cambiaría con un custodio E3 sin complemento. Limitación: la… |
| [I1](01_Nivel_1_Inicial.md#i1) | 5 | Solo producción | Revisa quién integra eDiscovery Manager y eDiscovery Administrator en producción y compáralo con la lista autorizada por Legal. Cómo hacerlo seguro: solo lectura de la membresía de los grupos de roles, ningún cambio… |
| [I2](01_Nivel_1_Inicial.md#i2) | 1 | Laboratorio | Lanza tres trabajos de búsqueda de auditoría: toda la actividad de una cuenta de prueba en siete días, solo `MailItemsAccessed` de esa cuenta y `FileAccessed` sobre un sitio de SharePoint. Cierra el navegador, vuelve… |
| [I2](01_Nivel_1_Inicial.md#i2) | 2 | Laboratorio | Habilita SearchQueryInitiatedExchange en el buzón de prueba siguiendo la guía de puesta en marcha, busca «licitación» en Outlook en la web y en SharePoint, y unas horas después encuentra ambos eventos. Evidencia: los… |
| [I2](01_Nivel_1_Inicial.md#i2) | 3 | Laboratorio | Crea una política de retención de auditoría de un año para una carga que la política predeterminada de Premium no cubre (por ejemplo, Teams) y una cuenta de prueba. Anota la fecha de creación: es la línea desde la… |
| [I2](01_Nivel_1_Inicial.md#i2) | 4 | Laboratorio parcial | Abre un registro `MailItemsAccessed` y un registro de mensajes de Teams de una cuenta E5, y marca las propiedades que aporta Premium (`SensitivityLabel`, `AppAccessContext`). Limitación: en la prueba E5 todos los… |
| [I2](01_Nivel_1_Inicial.md#i2) | 5 | Solo producción | Mide la brecha de retención: para una muestra de usuarios E3 y E5, consulta la fecha del registro más antiguo disponible y compárala con tu política interna o con lo que exige el regulador. Cómo hacerlo seguro: rol… |
| [I3](01_Nivel_1_Inicial.md#i3) | 1 | Laboratorio | Siembra el contenido sintético del «Proyecto Cóndor» (veinte correos, cinco documentos y un chat de Teams con términos y fechas conocidos) y guarda la lista como verdad de referencia. Luego crea con el generador de… |
| [I3](01_Nivel_1_Inicial.md#i3) | 2 | Laboratorio | Convierte la consulta a KeyQL, ubica el separador `c:s` y prueba las reglas de sintaxis con conteos: «Cóndor licitación» frente a «Cóndor AND licitación», el operador en minúsculas y una condición vacía. Evidencia:… |
| [I3](01_Nivel_1_Inicial.md#i3) | 3 | Laboratorio | Comprueba el efecto de UTC: siembra un correo enviado a las 22:00 de tu hora local y busca ese día con y sin convertir el rango a UTC (Ciudad de México está en UTC−6, Buenos Aires en UTC−3 y Santiago en UTC−4 o UTC−3… |
| [I3](01_Nivel_1_Inicial.md#i3) | 4 | Laboratorio | Mide la calidad de la consulta: con la muestra y tu verdad de referencia calcula cuántos ítems sembrados encontró (exhaustividad) y cuántos de los encontrados eran pertinentes (precisión). Ajusta a una versión 2 y… |
| [I3](01_Nivel_1_Inicial.md#i3) | 5 | Laboratorio parcial | Pide a Security Copilot un borrador de KeyQL desde lenguaje natural («correos de Ana a proveedores externos sobre la licitación Cóndor en marzo de 2026») y compáralo en estadísticas con tu consulta manual.… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 1 | Laboratorio | En el caso `PRUEBA-002` crea un hold infinito sobre el buzón y el OneDrive de una cuenta de prueba y un hold por consulta (tu consulta de I3) sobre un equipo de Teams. Anota la hora de creación y revisa el estado… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 2 | Laboratorio | Comprueba la instantánea de membresía: crea un hold sobre un grupo de Microsoft 365, suma después a un nuevo integrante y verifica que su buzón no quedó retenido (por ejemplo, revisando con Exchange Online PowerShell… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 3 | Laboratorio | Demuestra que el hold preserva: con el buzón retenido, elimina de forma permanente desde Outlook un correo sembrado y encuéntralo después con una búsqueda del caso. Evidencia: captura del resultado y nota sobre por… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 4 | Laboratorio parcial | Revisa la cuota de Elementos recuperables de un buzón retenido (pasa de 30 a 100 GB) y habilita su archivo. Limitación: en el laboratorio no vas a llenar la cuota; en producción, programa un monitoreo de los buzones… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 5 | Laboratorio | Escribe y ejecuta el procedimiento de liberación de `PRUEBA-002`: aprobación escrita de Legal (simulada), verificación de que ningún buzón inactivo dependa solo de ese hold, liberación, registro de la fecha y… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 6 | Laboratorio parcial | Busca en la configuración del portal unificado las comunicaciones a custodios y los issuing officers. Si existen, redacta un aviso de retención con acuse, recordatorio y liberación; si no, documenta la alternativa… |
| [M1](02_Nivel_2_Intermedio.md#m1) | 7 | Solo producción | Diseña el hold de un asunto con miles de custodios: calcula cuántas políticas necesitas con 1.000 o 2.000 buzones y sitios por hold, 100 o 200 holds por caso y la exclusión de listas de distribución de más de 100… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 1 | Laboratorio | Agrega a un review set de `PRUEBA-003` los resultados de tu consulta de I3 y compara el conteo antes y después: la búsqueda se vuelve a ejecutar al agregar. Si sembraste un documento con una etiqueta que cifra,… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 2 | Laboratorio | Ejecuta la analítica (casi duplicados, hilos de correo y temas) y aplica las consultas automáticas «For Review – Unique items only» (vista previa) y de ítems potencialmente irrelevantes. Calcula cuánto volumen te… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 3 | Laboratorio | Crea un panel de etiquetas (Pertinente, No pertinente, Privilegiado, Requiere redacción), revisa 30 ítems agrupados por familia y por conversación, y guarda dos consultas del review set. Evidencia: conteo por… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 4 | Laboratorio | Redacta en el visor de anotaciones los datos personales de dos documentos y déjalos listos para la producción de M4. Evidencia: captura de cada redacción y lista de ítems redactados con su justificación. |
| [M2](02_Nivel_2_Intermedio.md#m2) | 5 | Laboratorio parcial | En el explorador avanzado, escribe tres consultas KQL sobre `ReviewSetTable` (un filtro, una agregación por remitente y un gráfico por fecha) y repite el filtro con KeyQL. Limitación: la función está en vista previa… |
| [M2](02_Nivel_2_Intermedio.md#m2) | 6 | Laboratorio parcial | Pide a Security Copilot el resumen de tres ítems del review set y compáralo con tu lectura: anota omisiones, errores y lo que sí te ahorró. Limitación: consume SCU y la inclusión aplica a licencias E5 pagadas; en… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 1 | Laboratorio | Simula un BEC con dos cuentas de prueba: desde la cuenta «comprometida» crea una regla de bandeja de entrada que reenvíe a otra cuenta interna, lee diez mensajes concretos en Outlook en la web, busca «factura» y… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 2 | Laboratorio | Horas después, investiga con la auditoría: la creación de la regla, los accesos `MailItemsAccessed` de tipo bind con sus InternetMessageId, las búsquedas y el envío. Arma una línea de tiempo y compárala con tu verdad… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 3 | Laboratorio | Abre el mismo buzón con Outlook de escritorio en la máquina virtual del laboratorio para generar un acceso sync y localiza el registro por carpeta. Escribe qué puedes concluir con un sync y qué no, frente a un bind.… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 4 | Laboratorio | Preserva antes de erradicar: mientras contienes la cuenta como indica la guía de respuesta (la contención no espera), aplica un hold al buzón comprometido (M1) y exporta los resultados de auditoría con su hash;… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 5 | Laboratorio parcial | Estima el volumen: cuenta los registros de auditoría por usuario y por día de tu laboratorio, extrapola a la plantilla de tu organización y aplica la advertencia de hasta 10 veces más volumen con los registros… |
| [M3](02_Nivel_2_Intermedio.md#m3) | 6 | Solo producción | Acota una cuenta comprometida real: con Audit Reader asignado por PIM y la justificación en el ticket, determina qué mensajes se accedieron y desde qué IP. Cómo hacerlo seguro: solo metadatos (sin abrir contenido),… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 1 | Laboratorio | Exporta los resultados de la búsqueda de `PRUEBA-001`, descárgalos el mismo día, calcula el hash SHA-256 del paquete (por ejemplo, con `Get-FileHash`) y concilia el informe de ítems con las estadísticas. Registra… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 2 | Laboratorio | Exporta desde el review set de M2 los ítems pertinentes con sus redacciones y verifica que los documentos redactados llegan como `_burn.pdf` y sin el nativo. Evidencia: listado de archivos y del informe de… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 3 | Laboratorio | Busca en la auditoría las huellas de tus exportaciones (actividades de eDiscovery y posibles `FileAccessed`) y anéxalas al expediente: son la prueba de quién exportó y cuándo (actividades de eDiscovery en Audit).… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 4 | Laboratorio | Diseña el formulario de cadena de custodia: asunto, solicitante y base de la solicitud, consulta y versión, fecha y hora UTC, responsable, hash, medio de entrega, receptor, vencimiento del paquete (14 o 30 días) y… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 5 | Laboratorio | Planifica una producción de 1,2 millones de ítems: divídela en lotes que respeten 500.000 ítems por exportación, 2 o 5 TB por día, PST de 10 GB, paquetes de 40 GB y la cancelación a los siete días (límites).… |
| [M4](02_Nivel_2_Intermedio.md#m4) | 6 | Solo producción | Entrega una producción real a un tercero (por ejemplo, un estudio jurídico externo). Cómo hacerlo seguro: alcance aprobado por Legal, descarga solo en equipos administrados y cifrados (nunca personales), canal de… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 1 | Laboratorio parcial | Busca en un caso las interacciones de Copilot de una cuenta de prueba usando las clases de ítem de IA, agrégalas a un review set y revísalas con el visor de actividad de Copilot. Limitación: las licencias de… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 2 | Laboratorio parcial | Busca en Audit los registros de interacción con Copilot o con un agente y anota, para uno de ellos, `AccessedResources` (con `SensitivityLabelId` y `XPIADetected`), `AgentId` y `AgentName`. Limitación: necesitas… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 3 | Laboratorio parcial | Practica el flujo de búsqueda y eliminación de datos de IA sobre una cuenta de prueba: verifica holds y retención, retíralos de forma controlada, purga hasta 10 ítems por buzón, confirma con una nueva búsqueda y… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 4 | Laboratorio parcial | Si tu tenant de prueba tiene Loop, crea un espacio de trabajo con contenido sintético y búscalo en eDiscovery; al exportar, prueba la conversión HTML. Limitación: Learn marca en vista previa el soporte de SharePoint… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 5 | Laboratorio | Calcula cuánto costaría auditar apps de IA no Microsoft (`AIAppInteraction`, pago por uso, 180 días de retención) para tu organización y quién debe aprobarlo. Evidencia: nota de decisión con supuestos, costo estimado… |
| [A1](03_Nivel_3_Avanzado.md#a1) | 6 | Solo producción | Gobierna la limpieza prioritaria antes de que alguien la use: con Legal, retención y eDiscovery define si se habilita o se desactiva a nivel de tenant, quién da cada una de las tres aprobaciones y cómo se verifica… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 1 | Laboratorio | Registra una app en Entra ID con el permiso mínimo de eDiscovery que indica la API de eDiscovery, guarda el secreto en Key Vault y, con Microsoft Graph PowerShell, crea un caso, una búsqueda y un hold; repite con… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 2 | Laboratorio | Crea una consulta AuditLogQuery filtrada por fechas, tipo de registro, operación y usuario; consulta su estado hasta que termine, descarga los registros y agrega reintentos con espera ante HTTP 429. Compara el conteo… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 3 | Laboratorio | Migra un script: toma una búsqueda de `MailItemsAccessed` de siete días hecha con `Search-UnifiedAuditLog` y reescríbela con AuditLogQuery. Documenta las diferencias: asincronía, límites de 200 envíos al día y 50… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 4 | Laboratorio parcial | Crea suscripciones de la Management Activity API a Audit.Exchange y Audit.General con tu app, espera el primer blob (puede tardar hasta 12 horas) y verifica que los eventos no llegan en orden comparando sus marcas de… |
| [A2](03_Nivel_3_Avanzado.md#a2) | 5 | Solo producción | Inventaria los scripts y procesos de tu organización que usan `Search-UnifiedAuditLog`, `-Export` en `New-ComplianceSearchAction` o cmdlets de eDiscovery con autenticación solo aplicación, y fija su fecha de… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 1 | Laboratorio parcial | En un workspace de Sentinel pagado con los créditos de Visual Studio, conecta la auditoría de Microsoft 365 y verifica que llegan filas a `OfficeActivity`. Escribe una consulta KQL que reconstruya el BEC de M3:… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 2 | Laboratorio parcial | Repite la reconstrucción en la búsqueda avanzada de Defender XDR con `CloudAppEvents` y compara con `OfficeActivity`: campos, latencia y cobertura. Limitación: necesitas datos de aplicaciones en la nube en el tenant… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 3 | Laboratorio | Escribe el playbook de BEC con las fases de NIST SP 800-61 Rev. 3 y un paso explícito de preservación (hold y exportación de la auditoría con hash) antes de la erradicación, con los puntos de decisión de Legal y RR.… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 4 | Laboratorio parcial | Escala a eDiscovery: desde una alerta de Communication Compliance usa «Escalate for investigation», o desde un caso de Insider Risk Management usa el escalamiento a eDiscovery, y verifica el caso creado y su… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 5 | Laboratorio | Adquiere la auditoría de la cuenta del BEC con Microsoft-Extractor-Suite usando una cuenta de solo lectura, calcula el hash de lo adquirido, completa el formulario de custodia de M4 y compara con tu extracción por… |
| [A3](03_Nivel_3_Avanzado.md#a3) | 6 | Solo producción | Lleva el circuito al SOC real: agrega al runbook de incidentes el paso «preservar antes de erradicar» y una consulta de búsqueda proactiva sobre reglas de reenvío sospechosas y picos de `MailItemsAccessed`. Cómo… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 1 | Laboratorio parcial | En un caso piloto con datos sintéticos, usa Security Copilot para redactar una consulta KeyQL, resumir tres ítems del review set y resumir el caso; valida cada salida contra tu lectura y anota el consumo en el panel… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 2 | Laboratorio parcial | Con el pago por uso asociado en P0, configura Data Security Investigations y crea una investigación sobre uno o dos buzones de prueba con datos sensibles sintéticos; ejecuta la categorización y el examen con IA,… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 3 | Laboratorio | Prepara la decisión de ubicación del cómputo de IA de DSI para cada país donde operas (Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar») con las preguntas que debe responder Legal, sin… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 4 | Laboratorio parcial | Crea una investigación de DSI desde un caso de Insider Risk Management de prueba, con el contexto en lenguaje natural, y revisa la búsqueda por auditoría antes de agregar datos al alcance. Limitación: necesitas un… |
| [A4](03_Nivel_3_Avanzado.md#a4) | 5 | Solo producción | Usa DSI en un incidente de datos real. Cómo hacerlo seguro: alcance mínimo, estimación de costo previa, presupuesto y alertas de Azure al 50, 75 y 90 %, ubicación del cómputo aprobada por Legal y privacidad, ninguna… |
| [O1](04_Nivel_4_Operacion.md#o1) | 1 | Laboratorio | Organiza una mesa de trabajo de 90 minutos con Legal, RR. HH., TI, seguridad, privacidad y auditoría interna, y completa la RACI de referencia de este módulo para cuatro tipos de asunto (litigio, investigación… |
| [O1](04_Nivel_4_Operacion.md#o1) | 2 | Laboratorio | Diseña el formulario de intake con los datos mínimos: solicitante, tipo de asunto, base de la solicitud, custodios, rango de fechas, orígenes, urgencia, revisión de privacidad y aprobación de Legal. Pruébalo con dos… |
| [O1](04_Nivel_4_Operacion.md#o1) | 3 | Laboratorio | Escribe tu procedimiento estándar de caso, del intake al cierre, usando como lista de control el runbook de 18 pasos validado contra Learn, y ejecútalo de punta a punta en `PRUEBA-005`. Evidencia: procedimiento… |
| [O1](04_Nivel_4_Operacion.md#o1) | 4 | Laboratorio | Arma el catálogo de roles: por cada función, grupo de roles, tipo de asignación (permanente, justo a tiempo con PIM para grupos o con fecha de expiración donde Purview lo permite), aprobador y revisión trimestral.… |
| [O1](04_Nivel_4_Operacion.md#o1) | 5 | Solo producción | Pilotea el modelo con una solicitud real de baja sensibilidad. Cómo hacerlo seguro: patrocinio de Legal, alcance mínimo, roles asignados justo a tiempo, tiempos medidos en cada etapa y revisión posterior sin… |
| [O2](04_Nivel_4_Operacion.md#o2) | 1 | Laboratorio | Extrae de la auditoría las actividades de eDiscovery de tu laboratorio (creación de casos, búsquedas, holds, review sets y exportaciones) y calcula tres métricas de servicio: tiempo del caso al hold, de la búsqueda a… |
| [O2](04_Nivel_4_Operacion.md#o2) | 2 | Laboratorio | Cambia la membresía de un grupo de roles de prueba, encuentra el cambio en la auditoría (incluidas las operaciones de RBAC de MC1473155) y redacta el criterio de alerta para cambios en eDiscovery Administrator,… |
| [O2](04_Nivel_4_Operacion.md#o2) | 3 | Laboratorio | Construye el tablero mínimo de este módulo con datos del laboratorio en una planilla o en Power BI: al menos una métrica de servicio, una de calidad, una de costo y una de control, cada una con su fuente de datos.… |
| [O2](04_Nivel_4_Operacion.md#o2) | 4 | Laboratorio parcial | Registra el costo del laboratorio: consumo por uso en el Usage center de Purview (vista previa) y en Azure Cost Management, y SCU en el panel de Security Copilot si tienes capacidad. Limitación: sin licencias E5… |
| [O2](04_Nivel_4_Operacion.md#o2) | 5 | Solo producción | Haz la primera revisión trimestral con métricas reales. Cómo hacerlo seguro: extracción con roles de solo lectura, métricas individuales acordadas antes con privacidad y RR. HH., publicación agregada y acciones de… |
| [O3](04_Nivel_4_Operacion.md#o3) | 1 | Laboratorio | Completa el registro de decisiones con al menos ocho entradas —ubicación del review set, destino de exportaciones, cómputo de DSI, alcance de SearchQueryInitiated, retención de auditoría, limpieza prioritaria,… |
| [O3](04_Nivel_4_Operacion.md#o3) | 2 | Laboratorio | Con la hoja «Normativa MCSA» del libro de Excel, arma el mapa de tus países de operación: norma, autoridad, enlace oficial y las preguntas para Legal sobre preservación, exportación y transferencias, sin interpretar… |
| [O3](04_Nivel_4_Operacion.md#o3) | 3 | Laboratorio | Configura un límite de cumplimiento para dos «países» de prueba (atributo en las cuentas sintéticas) y verifica que una investigadora del país A no encuentra contenido del país B. Evidencia: filtro creado y dos… |
| [O3](04_Nivel_4_Operacion.md#o3) | 4 | Laboratorio parcial | Ejecuta una búsqueda de solicitud de titular de datos (DSR) sobre una persona sintética con eDiscovery y prepara el informe de ubicaciones. Limitación: una solicitud real tiene plazos legales, verificación de… |
| [O3](04_Nivel_4_Operacion.md#o3) | 5 | Solo producción | Presenta el registro de decisiones a Legal y privacidad para la revisión de impacto del programa de eDiscovery y Audit: a quién se le habilita SearchQueryInitiated, cuánto se retiene la auditoría, qué exportaciones… |
| [C1](Practica-y-referencias.md#c1) | 1 | — | Elige tres referentes de esta sección según tu rol (Purview, eDiscovery o detección en el SOC), suscríbete a sus canales y anota en tu registro de cambios la primera publicación útil de cada uno, con su fecha. |
| [C1](Practica-y-referencias.md#c1) | 2 | — | Lee el resumen mensual de octubre de 2026 y marca qué novedades obligan a cambiar un procedimiento o un script de tu equipo. |
| [C1](Practica-y-referencias.md#c1) | 3 | — | Elige tu libro de referencia: si optas por *Microsoft eDiscovery In-Depth*, verifica que cubra la experiencia unificada (posterior a agosto de 2025) antes de usarlo como texto de estudio (ficha). |
| [C2](Practica-y-referencias.md#c2) | 1 | — | Compara la versión en español y en inglés de tres páginas de esta guía (permisos de eDiscovery, búsqueda de auditoría y API de Graph) y registra cada diferencia de contenido o de fecha (permisos en español, auditoría… |
| [C2](Practica-y-referencias.md#c2) | 2 | — | Arma tu rutina: un recordatorio mensual para What's new in Microsoft Purview y el Message Center y uno trimestral para la guía de SC-401 y los webinars, y registra la primera revisión con fecha. |
| [C2](Practica-y-referencias.md#c2) | 3 | — | Prepara para tu equipo un glosario español-inglés de veinte términos tomados del glosario de esta guía, para alinear la conversación con la interfaz, que está en inglés. |

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

<a id="glosario-y-fuentes"></a>

## Cierre, glosario y fuentes


<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de eDiscovery y Audit no es saber dónde está cada botón, sino poder defender cada decisión: por qué preservaste ese alcance, por qué esa consulta, quién tuvo acceso a la evidencia, cuánto se retiene la auditoría y cómo se entregó. Tus siguientes pasos: el knowledge check del [Ninja oficial de eDiscovery](https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-microsoft-purview-ediscovery-ninja/2793108), el examen [SC-401](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) y la credencial [Applied Skills de retención, eDiscovery y Communication Compliance](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-retention-ediscovery-and-communication-compliance-in-microsoft-purview/).

Continúa con los programas hermanos según tu rol: ciclo de vida de los datos y registros (retenciones de Purview), riesgo interno y cumplimiento de comunicaciones (los casos que se escalan a eDiscovery), Information Protection (etiquetas y cifrado), DSPM y seguridad de datos para IA, Compliance Manager (normativa regional) y, del lado del SOC, Sentinel, Defender XDR y Security Copilot. Dedica media hora al mes a [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) y revisa los avisos del Message Center antes de cambiar un procedimiento.

Si encuentras un enlace roto, un dato desactualizado o un recurso que debería estar aquí, anótalo y compártelo con tu equipo: la guía está pensada para revisarse periódicamente, como el Ninja original.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| AIAppInteraction | Tipo de registro de auditoría de las interacciones con apps de IA no Microsoft; se factura por uso y se retiene 180 días. |
| Audit (Premium) | Nivel de auditoría con un año de retención por defecto para Exchange, SharePoint, OneDrive y Entra ID, políticas personalizadas, opción de 10 años con complemento y mayor ancho de banda de API. |
| Audit (Standard) | Auditoría habilitada por defecto, con búsqueda en el portal, PowerShell y API, y 180 días de retención. |
| AuditLogQuery | API de Microsoft Graph para consultar el registro de auditoría de forma asíncrona; GA en octubre de 2026 y reemplazo de Search-UnifiedAuditLog. |
| Cadena de custodia | Registro documentado de quién recolectó, accedió, transfirió y entregó la evidencia, cuándo y cómo se preservó su integridad (por ejemplo, con hash). |
| Caso | Unidad central del eDiscovery unificado: agrupa miembros, orígenes de datos, búsquedas, holds, review sets y exportaciones de un asunto. |
| Content Search | Búsqueda de contenido que hoy vive en un caso generado por el sistema y, desde febrero de 2026, solo busca y exporta. |
| Custodio | Persona cuyos datos se preservan y analizan en un asunto; para funciones premium necesita E5 o un complemento equivalente. |
| Data Security Investigations (DSI) | Solución de Purview para investigar incidentes de datos con búsqueda vectorial e IA generativa; se factura por almacenamiento y unidades de cómputo. |
| EDRM | Electronic Discovery Reference Model; su versión 2.0 (septiembre de 2026) agrupa etapas en Data Acquisition y agrega la disposición. |
| Estadísticas | Resumen de volumen, ubicaciones y aporte de cada término de una búsqueda; reemplazaron a las colecciones del eDiscovery clásico. |
| Hold (retención legal) | Política que preserva el contenido de los orígenes de un caso mientras dura el asunto; puede tardar hasta 24 horas en aplicarse. |
| Indexación avanzada | Reprocesamiento de ítems parcialmente indexados; en la experiencia unificada corre de forma automática. |
| Issuing officer | Persona en cuyo nombre se emiten las notificaciones de retención legal a los custodios. |
| KeyQL | Keyword Query Language: sintaxis de búsqueda de eDiscovery. No es lo mismo que KQL. |
| KQL | Kusto Query Language: lenguaje de Sentinel y Defender XDR; un subconjunto se usa en el explorador avanzado de review sets. |
| Límites de cumplimiento | Filtros de permisos de búsqueda que restringen qué contenido puede buscar cada grupo, por ejemplo por país o subsidiaria (compliance boundaries). |
| MailItemsAccessed | Evento de auditoría que registra accesos a mensajes (sync por carpeta y bind agregado cada dos minutos) para acotar compromisos de buzón. |
| Management Activity API | API de suscripción y descarga de blobs de Office 365 para enviar la auditoría a un SIEM. |
| OfficeActivity | Tabla de Sentinel con la auditoría de Exchange, SharePoint y Teams. |
| Priority Cleanup | Limpieza prioritaria (vista previa) que puede eliminar contenido retenido con simulación y aprobaciones; lo eliminado deja de ser descubrible. |
| Purview Suite | Complemento de Purview (antes Microsoft 365 E5 Compliance) que agrega a E3, entre otras capacidades, Audit (Premium) y eDiscovery premium. |
| Redacción (PDF burn) | Ocultamiento permanente de contenido en un ítem del review set; al exportar se entrega el PDF redactado en lugar del original. |
| Review set (conjunto de revisión) | Copia estática de ítems en almacenamiento de Azure gestionado por Microsoft para revisar, analizar, etiquetar y exportar. |
| RMS Decrypt | Rol que permite descifrar contenido protegido con etiquetas al agregarlo a review sets o exportarlo. |
| SCU | Security Compute Unit: capacidad de Security Copilot; E5 y E7 incluyen 400 SCU al mes por cada 1.000 licencias pagadas, hasta 10.000. |
| Search And Purge | Rol que permite eliminar en bloque el contenido que coincide con una búsqueda, incluidos los datos de IA. |
| Search-UnifiedAuditLog | Cmdlet de Exchange Online PowerShell para buscar en la auditoría; se retira el 15 de octubre de 2027. |
| SearchQueryInitiated | Eventos de auditoría de búsquedas en Exchange y SharePoint; el de Exchange se habilita buzón por buzón. |
| SharePoint Embedded | Contenedores de archivos de apps como Loop, Copilot Pages y Copilot Notebooks, incorporados a eDiscovery en 2026. |
| UAL | Unified Audit Log: registro de auditoría unificado de Microsoft 365. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Retención de Audit (Standard): algunas guías de licenciamiento de terceros siguen citando 90 días, mientras Learn indica 180 días para registros generados desde el 17 de octubre de 2023 ([guía de terceros](https://microsoftnegotiations.com/blog/microsoft-purview-licensing-guide) frente a [Learn](https://learn.microsoft.com/en-us/purview/audit-log-retention-policies)).
- Exportación por la API de Graph: el aviso MC1055528 (abril de 2025) la asociaba a E5 y eDiscovery (Premium); la página de la API (mayo de 2026) permite exportar con E3 delegado mediante pago por uso. Confírmalo en tu tenant antes de diseñar automatizaciones ([MC1055528](https://mc.merill.net/message/MC1055528), [API de eDiscovery](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)).
- SharePoint Embedded (Loop, Copilot Pages y Copilot Notebooks): el blog de seguridad del 24 de septiembre de 2026 lo presenta como disponible y Learn lo marca en vista previa ([blog](https://www.microsoft.com/en-us/security/blog/2026/09/24/whats-new-in-microsoft-security-september-2026/), [componentes de eDiscovery](https://learn.microsoft.com/en-us/purview/edisc-features-components)).
- Codificación predictiva: «Learn about eDiscovery» la menciona dentro de los review sets, pero sus artículos siguen en vista previa y con el aviso de retiro del clásico; trátala como no confirmada en la experiencia unificada ([Learn about eDiscovery](https://learn.microsoft.com/en-us/purview/edisc), [codificación predictiva](https://learn.microsoft.com/en-us/purview/ediscovery-predictive-coding-overview?redirectSourcePath=%252fde-de%252farticle%252ftagging-and-assessment-b5c82de7-ed2f-4cc6-becd-db403faf4d18&view=o365-worldwide)).
- Notificaciones de retención legal e issuing officers: están documentadas para eDiscovery (Premium) con aviso de retiro, y un análisis comunitario —con preguntas abiertas no confirmadas por Microsoft— las describe en el portal nuevo. Confirma su ubicación y alcance en tu tenant ([comunicaciones](https://learn.microsoft.com/th-th/purview/ediscovery-managing-custodian-communications?view=o365-worldwide), [eDiscovery Journal](https://ediscoveryjournal.com/docs/microsoft/purview-ediscovery/new-purview-ediscovery-portal/)).
- El Ninja oficial de 2026 todavía se describe como «eDiscovery Premium solution», aunque el clásico Premium está retirado. La línea de investigación de este programa no logró abrir el post directamente; su URL proviene de la investigación de formato Ninja de la serie y del [índice de Tech Community](https://techcommunity.microsoft.com/tag/ninja%20training).
- La guía de MailItemsAccessed usa `Search-UnifiedAuditLog` en sus ejemplos; los ejercicios de esta edición agregan AuditLogQuery porque el cmdlet se retira el 15 de octubre de 2027 ([guía](https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts), [MC1505599](https://mc.merill.net/message/MC1505599)).
- Exportación de review sets a una cuenta propia de Azure Storage: el procedimiento está redactado para la interfaz de eDiscovery (Premium); valida que exista una opción equivalente en la experiencia unificada ([procedimiento](https://learn.microsoft.com/en-us/purview/ediscovery-download-export-jobs)).
- La versión en español de la página de la API de eDiscovery dice «suscripción A3» donde la versión en inglés dice E3; usa la versión en inglés ([versión en español](https://learn.microsoft.com/es-es/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0)).
- «Insights inteligentes» y eventos de alto valor: la página de soluciones de auditoría sigue asociándolos a Audit (Premium), mientras MailItemsAccessed, los envíos y las búsquedas ya están en Audit (Standard). Verifica qué eventos y propiedades quedan como exclusivos de Premium antes de justificar una compra ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).
- Registros de entidades no usuario (service principals, sistema y apps): la investigación indica un año fijo de retención sin políticas personalizadas; confirma si aplica igual en tenants sin licencias Premium ([soluciones de auditoría](https://learn.microsoft.com/en-us/purview/audit-solutions-overview)).
- Fecha de disponibilidad general de Data Security Investigations: las fuentes la sitúan a fines de enero de 2026 (nota de prensa del 27 de enero y AMA oficial del 5 de febrero); no se encontró una fecha exacta en Learn ([AMA](https://techcommunity.microsoft.com/event/microsoft-security-events/ask-microsoft-anything-purview-data-security-investigations-part-2/4485393), [Help Net Security](https://www.helpnetsecurity.com/2026/01/27/microsoft-purview-data-security-investigations/)).
- La limitación de las búsquedas de contenido a buscar y exportar (MC1216266) se conoce por un análisis comunitario; no se localizó el aviso original ([análisis](https://office365itpros.com/2026/01/15/content-searches-change/)).
- Inclusión de Security Copilot en E5: se calcula sobre licencias pagadas, por lo que un tenant de prueba no debería esperar SCU incluidas (inferencia de la investigación de la serie; confírmalo con Microsoft). Tampoco cubre Data Security Investigations no agéntico ([inclusión](https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion)).
- Los precios de referencia (Microsoft Purview Suite, Microsoft 365 E5 y medidores de DSI) varían por región y acuerdo; usa las páginas oficiales y tu calculadora ([precios de Purview](https://www.microsoft.com/en-us/security/microsoft-purview-pricing), [precios de consumo](https://azure.microsoft.com/en-us/pricing/details/purview/)).
- El playbook de la CISA tendría una revisión posterior (mayo de 2026) según la comunidad; no se confirmó en la fuente oficial ([CISA](https://www.cisa.gov/news-events/alerts/2025/01/15/cisa-releases-microsoft-expanded-cloud-logs-implementation-playbook)).
- El libro *Microsoft eDiscovery In-Depth* no muestra fecha de edición: verifica que cubra la experiencia unificada antes de usarlo como texto de estudio ([ficha](https://www.amazon.co.uk/Microsoft-eDiscovery-Depth-Purview-content/dp/1835462707)).
- El cómputo de IA de Data Security Investigations no ofrece ubicación en Latinoamérica (Australia y Nueva Zelanda, UE, Reino Unido, EE. UU. o «en cualquier lugar»). No es una contradicción, pero sí una decisión que Legal y privacidad deben tomar en cada país ([facturación de DSI](https://learn.microsoft.com/en-us/purview/data-security-investigations-billing)).
- Aprobaciones de la limpieza prioritaria: el aviso MC1183292 (noviembre de 2025) y un resumen comunitario de octubre de 2026 hablan de dos aprobaciones, mientras las novedades de Purview de julio de 2026 exigen tres (administración de limpieza prioritaria, de retención y de eDiscovery). Confirma el flujo vigente en tu tenant antes de escribir el procedimiento ([MC1183292](https://mc.merill.net/message/MC1183292), [novedades de Purview](https://learn.microsoft.com/en-us/purview/whats-new), [resumen de octubre de 2026](https://alberthoitingh.com/2026/10/07/things-to-know-about-microsoft-purview-october-2026/)).
- Auditoría y eDiscovery de agentes: la página de auditoría de Copilot e IA indica que los registros de Copilot Studio y Microsoft Foundry (con `AgentId` y `AgentName`) se generan en Audit (Standard), mientras la descripción de servicio de Agent 365 ubica la auditoría y el eDiscovery de Purview para agentes entre las capacidades que requieren Microsoft 365 E7 o Agent 365. La diferencia parece estar en los agentes gestionados con Agent 365; confírmala antes de prometer cobertura a Legal ([auditoría de Copilot e IA](https://learn.microsoft.com/en-us/purview/audit-copilot), [Agent 365](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365)).
- Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar, días después de la fecha de corte, el estado de funciones en vista previa: explorador avanzado de review sets, consulta For Review, KeyQL con Copilot, clave del cliente en exportaciones, SharePoint Embedded, Priority Cleanup y el Posture Agent de DSI.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No constituye asesoría legal: las decisiones sobre preservación, exportación, transferencias y privacidad corresponden a tus áreas de Legal, RR. HH. y privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

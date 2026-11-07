# Cierre, glosario y fuentes

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Laboratorio y práctica en producción](07_Laboratorio_y_practica_en_produccion.md) · [Índice del programa](README.md)

<a id="cierre"></a>

## ¿Y ahora?

Ser Ninja de Information Protection es un hábito: la taxonomía, los SIT y los derechos de uso se revisan cada trimestre, y Purview publica novedades cada mes. Próximos pasos: la certificación SC-401, la insignia de la ruta Ninja de Learn y la credencial SC-5003; después, los programas de DLP y de DSPM de esta serie, que usan directamente lo que construiste aquí, y los de Sentinel y Security Copilot para llevar las señales de etiquetas al SOC.

Si encuentras un enlace roto, un dato desactualizado o una contradicción, anótalo y compártelo con tu equipo: la guía está pensada para mantenerse viva con revisiones periódicas, como el Ninja original. Para preguntas técnicas, el foro de Data Security de Tech Community, el blog de Purview y las Purview Lightning Talks son los mejores lugares; para decisiones sobre datos personales, siempre Legal y Privacidad.

<a id="glosario"></a>

## Glosario

| Término | Definición |
|---|---|
| Advanced Message Encryption (AME) | Capacidad de nivel E5 del cifrado de mensajes de Purview que agrega varias plantillas de marca, expiración y revocación del correo enviado a externos por el portal de OME. |
| Agent 365 y Microsoft 365 E7 | SKU en disponibilidad general desde el 1 de mayo de 2026; E7 incluye Microsoft 365 E5, Microsoft 365 Copilot, Entra Suite y Agent 365, y habilita Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra. |
| Auto-etiquetado en cliente | Configuración de una etiqueta para que las apps de Office la recomienden o la apliquen mientras la persona trabaja, según SIT o clasificadores; el usuario puede rechazar una recomendación. |
| Auto-etiquetado en servicio | Políticas que etiquetan archivos en reposo de SharePoint y OneDrive y correo en tránsito de Exchange, con modo simulación previo; no actúan sobre buzones en reposo. |
| BlockContentAnalysisServices | Configuración avanzada de etiqueta, solo por PowerShell, que impide que Microsoft 365 Copilot y otras experiencias conectadas analicen los archivos con esa etiqueta. |
| Clasificador entrenable | Modelo de aprendizaje automático que reconoce categorías de documentos; hay integrados y personalizados, que se entrenan con muestras positivas y negativas. |
| Cliente de Purview Information Protection (MPIP) | Cliente para Windows con escáner, etiquetador del Explorador de archivos, visor y módulo de PowerShell; reemplazó al cliente de etiquetado unificado de AIP. |
| Content explorer (classic) y Data explorer | Exploradores que muestran una instantánea de los elementos con etiquetas o SIT detectados; permiten ver contenido, por lo que su acceso debe restringirse. |
| Customer Key | Cifrado de servicio en reposo con claves raíz del cliente en Azure Key Vault, aplicado mediante políticas de cifrado de datos. |
| Data Map y Unified Catalog | Mapa de datos de Purview para orígenes fuera de Microsoft 365; el etiquetado de sus activos está en vista previa y se aplica solo como metadatos. |
| DEP (Data Encryption Policy) | Política de cifrado de Customer Key: multicarga, de buzones de Exchange o de SharePoint y OneDrive. |
| Derechos de uso | Permisos de Rights Management (VIEW, EDIT, EXTRACT, PRINT, EXPORT, FORWARD, OWNER, entre otros) que definen qué puede hacer cada persona con el contenido cifrado. |
| Double Key Encryption (DKE) | Cifrado con dos claves, una bajo control exclusivo del cliente y otra en Azure; Microsoft no puede descifrar el contenido y varios servicios dejan de procesarlo. |
| Encrypt-Only y Do Not Forward | Opciones de cifrado de correo: la primera cifra y concede todos los derechos salvo exportar y control total; la segunda impide reenviar, imprimir o copiar. |
| Entidad con nombre | Tipo de información confidencial que reconoce, con modelos, nombres de personas, direcciones o condiciones médicas. |
| Escáner de Information Protection | Servicio de Windows Server que descubre, clasifica y protege archivos en recursos SMB, NFS (vista previa) y bibliotecas de SharePoint Server, por ciclos y no en tiempo real. |
| Esquema moderno (grupos de etiquetas) | Forma de organizar las etiquetas en grupos en lugar de etiquetas padre; es el esquema de los tenants creados desde el 1 de octubre de 2025. |
| Etiqueta de confidencialidad | Metadato persistente que clasifica el contenido y puede aplicar cifrado, marcas de contenido y controles en contenedores, reuniones y otros servicios. |
| Etiqueta de contenedor | Etiqueta aplicada a equipos de Teams, grupos, sitios, comunidades de Viva Engage o áreas de trabajo de Loop que controla privacidad, invitados, uso compartido y dispositivos; no etiqueta los elementos internos. |
| Etiqueta predeterminada | Etiqueta que una política aplica al contenido nuevo sin etiqueta (documentos, correo, reuniones o Power BI) o que se asigna a una biblioteca de SharePoint. |
| Exact Data Match (EDM) | Tipo de información confidencial que detecta valores exactos de una tabla sensible cargada con hash, por ejemplo clientes o empleados. |
| Huella digital de documento | Tipo de información confidencial creado a partir de un formulario o plantilla para detectar documentos derivados de ella. |
| Licencia de uso | Certificado que permite abrir contenido cifrado; habilita el acceso sin conexión hasta su vencimiento (30 días por defecto), incluso después de una revocación. |
| Microsoft Purview Suite | Nombre de Microsoft 365 E5 Compliance desde el 1 de octubre de 2025; se agrega sobre Microsoft 365 E3 para obtener las capacidades de nivel E5 de Purview. |
| MIP SDK | Kit de desarrollo (File, Policy y Protection) para que aplicaciones propias o de terceros lean y apliquen etiquetas y cifrado. |
| Pago por uso (PAYG) | Facturación por consumo de Purview mediante una suscripción de Azure vinculada al tenant; en Information Protection cubre etiquetas fuera de Microsoft 365 y clasificación bajo demanda. |
| Política de etiquetas | Publicación de etiquetas a usuarios o grupos con etiqueta predeterminada, etiquetado obligatorio, justificación para bajar de nivel y vínculo de ayuda. |
| Rights Management (Azure RMS) | Servicio de cifrado de Purview Information Protection que aplica la protección definida en las etiquetas y emite las licencias de uso. |
| SIT (tipo de información confidencial) | Patrón de clasificación con elemento primario, evidencia de apoyo, nivel de confianza y proximidad; puede ser integrado, personalizado, de entidad con nombre o EDM. |
| Superusuario | Característica de Rights Management que concede control total sobre todo el contenido cifrado del tenant para recuperación y descubrimiento; viene deshabilitada. |

<a id="metodologia"></a>

## Metodología y fuentes

Esta guía se construyó con líneas de investigación en paralelo sobre fuentes públicas: la forma y la historia del Ninja oficial, cada nivel técnico, la operación y la comunidad. Cada enlace se registró solo si apareció literalmente en un resultado de búsqueda o en una página leída, y luego se consolidó, se depuró y se verificó. Se descartaron recursos retirados, alojados en espacios no públicos o duplicados. Fecha de corte: 6 de noviembre de 2026.

Puntos a confirmar en fuentes oficiales antes de recomendarlos:

- Defender for Cloud Apps y etiquetas en apps de terceros: [«Learn about sensitivity labels»](https://learn.microsoft.com/en-us/purview/sensitivity-labels) todavía dice que Defender for Cloud Apps etiqueta contenido en apps de terceros, pero las directivas de archivo se retiran el 6 de enero de 2027 y el reemplazo de Purview para apps no Microsoft es solo DLP en vista previa, sin auto-etiquetado equivalente listado ([guía de migración](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview)).
- Alcance de la herramienta de migración de Defender for Cloud Apps: la versión en inglés indica que convierte directivas de SharePoint y OneDrive en DLP o auto-etiquetado y que aún no migra las de apps no Microsoft; la versión en español describe un alcance menor ([versión en español](https://learn.microsoft.com/es-es/defender-cloud-apps/migrate-file-policies-to-purview)). Prevalece el inglés; verifícalo en tu tenant antes de planificar.
- Fechas de Defender for Cloud Apps: el [índice de anuncios a partners](https://learn.microsoft.com/en-us/partner-center/announcements/) registra la deprecación de DLP en Defender for Cloud Apps el 6 de julio de 2026, mientras la guía de migración fija el retiro de las directivas de archivo el 6 de enero de 2027; aquí se interpretan como anuncio y retiro.
- Límite de 500.000 archivos por día: la documentación de auto-etiquetado y el [blog de agosto de 2026](https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/) lo presentan como vigente, mientras la [arquitectura de referencia interactiva](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) de Microsoft aún marca el aumento como vista previa pública.
- MC1477181 (etiqueta de biblioteca aplicada a archivos existentes): un MVP la describe como disponible en general ([análisis](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/)) y la arquitectura de referencia de Microsoft la marca como vista previa pública; además, la página de la etiqueta predeterminada de biblioteca todavía dice que no aplica a archivos existentes en reposo.
- Etiqueta predeterminada de biblioteca y permisos definidos por el usuario: la [página de Learn](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-default-label) indica que no admite etiquetas con permisos definidos por el usuario, expiración ni DKE, mientras un [análisis de febrero de 2026](https://office365itpros.com/2026/02/26/sensitivity-label-extend-protection/) muestra cómo extender los permisos de SharePoint a archivos descargados con una etiqueta de biblioteca con permisos definidos por el usuario (MC1208688 y `ExtendPermissionsToUnprotectedFiles`). Pruébalo en tu tenant antes de diseñar sobre esa combinación.
- Nombres de licencias: la [descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) usa «Microsoft Purview Suite», mientras la FAQ de Data Map y la guía de migración de Defender for Cloud Apps siguen diciendo «Microsoft 365 E5 Compliance». El renombre del 1 de octubre de 2025 proviene de una [fuente de partner](https://samexpert.com/microsoft-365-defender-purview-renames/) que conviene contrastar con los Product Terms.
- Licencias por característica de etiquetado: la tabla de etiquetado de la descripción del servicio no pudo leerse completa en esta revisión. Las asignaciones E3 y E5 marcadas como «indicativo» provienen del mapa interactivo de Microsoft (verificado el 2 de noviembre de 2026), que pide confirmarlas en esa descripción; lo mismo vale para las etiquetas de contenedor, el escáner y DKE.
- Rol Data Classification List Viewer para Data explorer y Content explorer (classic) desde mayo de 2026: la fuente es un [blog comunitario](https://blog.topedia.com/posts/updates-to-permissions-for-microsoft-purview-data-explorer-and-content-explorer) que resume un aviso del Centro de mensajes; confírmalo en la documentación de permisos.
- Versiones del cliente de Information Protection: el [Download Center](https://www.microsoft.com/en-sa/download/details.aspx?id=53018) mostraba la versión GA 3.2.176.0 (23 de octubre de 2026) y otras réplicas, la 3.2.173.0 (19 de octubre de 2026). La información sobre la versión preliminar 3.2.89.0 del escáner (abril de 2026) proviene de un agregador sin autor identificable y no se usó como fuente.
- Agentes: la descripción del servicio dice que las capacidades de Purview para agentes de Microsoft Foundry y apps conectadas a Entra «se soportarán» con E7 y Agent 365, en tiempo futuro, aunque esos SKU están disponibles desde el 1 de mayo de 2026. El estado detallado se sigue en el programa de DSPM y seguridad de datos para IA.
- Etiquetas en conectores de Power Platform y respuestas de agentes de Copilot Studio: el [plan de lanzamiento](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/view-sensitivity-labels-connectors) (vista previa en noviembre de 2025 y disponibilidad general prevista para junio de 2026) está archivado desde octubre de 2026; verifica el estado real en la documentación de Copilot Studio.
- El [conector de Purview Information Protection para Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) sigue en vista previa y su página describe el portal de Azure, aunque Sentinel se opera hoy desde el portal de Defender.
- La [ruta Ninja de Learn](https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/) no muestra fecha de actualización ni entrega certificado con nota mínima: el certificado al 80 % es propio de esta guía. Tampoco se confirmó un Ninja exclusivo de DLP; el MIP Ninja original incluía DLP.
- Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar estados de vista previa: informes de postura, etiquetado en Data Map, opciones de reuniones y la política de MC1477181. Revisa [What's new in Microsoft Purview](https://learn.microsoft.com/en-us/purview/whats-new) el 21 de noviembre de 2026.

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

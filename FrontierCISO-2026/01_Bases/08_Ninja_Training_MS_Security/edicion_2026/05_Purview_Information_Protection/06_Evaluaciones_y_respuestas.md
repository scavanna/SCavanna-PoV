# Evaluaciones y respuestas

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Comunidad](05_Comunidad.md) · [Índice del programa](README.md) · [Laboratorio y práctica en producción →](07_Laboratorio_y_practica_en_produccion.md)

<a id="respuestas"></a>

Cada evaluación tiene preguntas de opción múltiple. Con 80 % o más el nivel se considera aprobado. Es una autoevaluación de esta guía, no una certificación de Microsoft.

<a id="eval-inicial"></a>

## Nivel 1 · Inicial · Fundamentos

**1. ¿Quién puede habilitar las funciones de pago por uso de Purview vinculando el tenant a una suscripción de Azure?**

- a) Cualquier persona con el rol Compliance Administrator
- b) Solo un Global Administrator  ✅
- c) El propietario de la suscripción de Azure, sin ningún rol en Entra
- d) Cualquier miembro del grupo de roles Information Protection Admins

*Respuesta: b).* La vinculación con una suscripción y un grupo de recursos de Azure solo la puede hacer un Global Administrator; la página está en vista previa y el país o región queda fijo para el tenant. [Fuente](https://learn.microsoft.com/en-us/purview/purview-payg-subscription-based-enablement) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**2. ¿Cuándo se retiró el portal clásico de cumplimiento?**

- a) El 2 de julio de 2024, el mismo día de la disponibilidad general del nuevo portal
- b) El 11 de abril de 2024, junto con el complemento de AIP para Office
- c) Entre el 14 de noviembre y el 14 de diciembre de 2024  ✅
- d) El 1 de octubre de 2025, junto con el cambio de nombre a Purview Suite

*Respuesta: c).* El 2 de julio de 2024 fue la disponibilidad general del nuevo portal (MC807798) y el 11 de abril de 2024, el retiro del complemento de AIP; el portal clásico se retiró entre el 14 de noviembre y el 14 de diciembre de 2024 (MC939918). [Fuente](https://mc.merill.net/message/MC939918) · Repasa [P0](01_Nivel_1_Inicial.md#p0)

**3. ¿Con qué puntaje se aprueba el examen SC-401?**

- a) 700  ✅
- b) 600
- c) 750
- d) 800

*Respuesta: a).* Se aprueba con 700 y la certificación se renueva cada año de forma gratuita en Microsoft Learn. [Fuente](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-401) · Repasa [I0](01_Nivel_1_Inicial.md#i0)

**4. En un sitio de SharePoint donde se aplica una capacidad premium de Purview, ¿quiénes necesitan licencia?**

- a) Todas las personas del tenant, incluidos los visitantes con acceso de solo lectura
- b) Solo el administrador que crea y publica la política, porque es quien la configura
- c) Solo los propietarios del sitio; los miembros quedan cubiertos por la licencia del propietario
- d) Los propietarios y los miembros, pero no los visitantes ni los roles de solo lectura  ✅

*Respuesta: d).* Purview se licencia por beneficio: en ubicaciones compartidas como sitios, grupos y canales la licencia la necesitan propietarios y miembros. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**5. Desde el 1 de octubre de 2025, Microsoft 365 E5 Compliance se llama…**

- a) Microsoft Defender Suite
- b) Microsoft 365 E7
- c) Microsoft Purview Suite  ✅
- d) E5 Information Protection and Governance

*Respuesta: c).* E5 Security pasó a ser Microsoft Defender Suite y E5 IP&G conserva su nombre; E7 es otro SKU, que incluye E5, Microsoft 365 Copilot, Entra Suite y Agent 365. [Fuente](https://samexpert.com/microsoft-365-defender-purview-renames/) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**6. Según el mapa indicativo de Microsoft, ¿qué capacidad de clasificación se factura por uso?**

- a) Los SIT con expresiones regulares y palabras clave
- b) La clasificación bajo demanda  ✅
- c) Los clasificadores entrenables
- d) La etiqueta predeterminada de la política

*Respuesta: b).* La clasificación bajo demanda es pago por uso; los SIT sintácticos y la etiqueta predeterminada se ubican en E3 y los clasificadores entrenables en E5, siempre como referencia indicativa. [Fuente](https://microsoft.github.io/purview/purview-classification-labeling-reference-architecture.html) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**7. ¿Con qué licencias se soportarán las capacidades de Purview para agentes de Microsoft Foundry y apps de IA conectadas a Entra?**

- a) Microsoft 365 E3
- b) Microsoft Purview Suite sobre E3
- c) Office 365 E5
- d) Microsoft 365 E7 y los SKU de Agent 365  ✅

*Respuesta: d).* La descripción del servicio asocia esas capacidades a E7 y Agent 365, redactado en futuro; ambos SKU están disponibles desde el 1 de mayo de 2026. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [I1](01_Nivel_1_Inicial.md#i1)

**8. ¿Qué archivo de muestra pide la nueva experiencia de EDM para definir el esquema?**

- a) Entre 10 y 20 filas con valores sintéticos que imitan el formato de la tabla real  ✅
- b) La tabla real completa, sin hash, para que el esquema sea exacto
- c) Exactamente 1.000 filas reales elegidas al azar de la tabla
- d) Ninguno: el esquema se escribe a mano en XML, sin archivo de muestra

*Respuesta: a).* El archivo de muestra de 10 a 20 filas define el esquema; los datos reales se cargan después con hash mediante el EDM Upload Agent. [Fuente](https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-based-sits-overview) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**9. Para entrenar un clasificador entrenable personalizado, ¿qué muestras necesitas?**

- a) Entre 10 y 20 positivas, como el archivo de muestra de EDM
- b) Solo muestras negativas, porque las positivas las aporta Microsoft
- c) Entre 50 y 500 positivas y entre 150 y 1.500 negativas  ✅
- d) Al menos 2.000 positivas y ninguna negativa

*Respuesta: c).* Las muestras van en carpetas dedicadas de SharePoint; el clasificador procesa hasta las 2.000 más recientes y solo archivos de texto. [Fuente](https://learn.microsoft.com/en-us/purview/trainable-classifiers-get-started-with) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**10. ¿Por qué el acceso a Data explorer y a Content explorer (classic) debe estar muy restringido?**

- a) Porque cada consulta se cobra por uso a la suscripción de Azure vinculada
- b) Porque permiten ver el contenido de los elementos con etiquetas o SIT  ✅
- c) Porque al abrirlos se cambian las etiquetas de los archivos listados
- d) Porque desactivan la auditoría unificada mientras se navegan

*Respuesta: b).* Los exploradores muestran una instantánea de los elementos y permiten leer su contenido; por eso existen roles específicos para listar y para ver contenido. [Fuente](https://learn.microsoft.com/en-us/purview/data-classification-data-explorer) · Repasa [I2](01_Nivel_1_Inicial.md#i2)

**11. ¿Qué esquema de etiquetas usan los tenants creados desde el 1 de octubre de 2025?**

- a) El esquema moderno de grupos de etiquetas  ✅
- b) Etiquetas padre con subetiquetas, sin opción de migrar
- c) Un esquema sin prioridades
- d) El esquema del complemento de AIP

*Respuesta: a).* Los tenants nuevos usan grupos de etiquetas; los existentes pueden migrar sus etiquetas padre a grupos, una migración irreversible. [Fuente](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**12. ¿Qué requisitos tiene el etiquetado integrado en Outlook?**

- a) Office 2019 perpetuo con el complemento de etiquetado
- b) El complemento de AIP instalado en cada equipo con Outlook
- c) Una licencia de Teams Premium para cada remitente
- d) Un buzón en Exchange Online y una edición de Office por suscripción  ✅

*Respuesta: d).* Office perpetuo y los buzones locales no admiten las etiquetas integradas, y el complemento de AIP se retiró en 2024. [Fuente](https://learn.microsoft.com/en-us/purview/sensitivity-labels-office-apps) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**13. ¿Qué tamaño máximo de taxonomía recomienda la guía de Microsoft?**

- a) Tres etiquetas principales, sin ninguna subetiqueta
- b) Diez etiquetas principales, una por tipo de documento
- c) Cinco etiquetas principales con cinco subetiquetas  ✅
- d) Una etiqueta principal por cada departamento de la organización

*Respuesta: c).* La guía propone de 3 a 5 niveles con nombres autoexplicativos y no más de cinco etiquetas principales con cinco subetiquetas. [Fuente](https://learn.microsoft.com/en-us/compliance/assurance/assurance-data-classification-and-labels) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

**14. Publicas etiquetas que cifran sin haber habilitado las etiquetas para SharePoint y OneDrive. ¿Qué pierdes sobre esos archivos?**

- a) La posibilidad de etiquetar y cifrar el correo en Outlook
- b) La coautoría, Office web, la búsqueda y eDiscovery  ✅
- c) Las marcas de contenido (encabezado, pie y marca de agua) en Word
- d) El etiquetado manual en las apps de Office para iOS y Android

*Respuesta: b).* Habilitar las etiquetas para SharePoint y OneDrive es el requisito para que el servicio procese archivos cifrados (coautoría, búsqueda, eDiscovery, DLP y Office web); no aplica a DKE ni HYOK. [Fuente](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files) · Repasa [I3](01_Nivel_1_Inicial.md#i3)

<a id="eval-intermedio"></a>

## Nivel 2 · Intermedio · Automatizar y proteger

**1. ¿Cuál es el techo del auto-etiquetado en servicio para SharePoint y OneDrive desde agosto de 2026?**

- a) 25.000 archivos por día
- b) 100.000 archivos por día
- c) 500.000 archivos por día  ✅
- d) Sin límite diario

*Respuesta: c).* El límite subió de 100.000 a 500.000 archivos por día; es un techo por tenant, no una tasa garantizada. [Fuente](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**2. ¿Sobre qué correo actúa el auto-etiquetado en servicio de Exchange?**

- a) Sobre el correo en tránsito  ✅
- b) Sobre todos los buzones en reposo
- c) Solo sobre carpetas públicas
- d) Sobre archivos PST importados

*Respuesta: a).* El etiquetado en servicio actúa sobre SharePoint y OneDrive en reposo y sobre Exchange en tránsito; no etiqueta buzones en reposo. [Fuente](https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**3. La pestaña Insights de una política de auto-etiquetado en modo de aplicación muestra métricas de 30 días para…**

- a) Exchange y Teams
- b) Endpoints con Windows
- c) Activos de Data Map
- d) Solo SharePoint y OneDrive  ✅

*Respuesta: d).* Para Exchange hay que usar el explorador de actividades, con una latencia de 60 a 90 minutos. [Fuente](https://learn.microsoft.com/en-us/purview/auto-label-insights-tab) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**4. ¿Qué agrega la política especial de MC1477181 (22 de septiembre de 2026)?**

- a) El etiquetado de buzones de Exchange en reposo, con hasta 10 buzones por política
- b) Aplicar la etiqueta predeterminada de biblioteca a archivos existentes sin etiqueta (una política por tenant y hasta 10 sitios)  ✅
- c) El auto-etiquetado de reuniones de Teams a partir de la etiqueta de contenedor del equipo, sin Teams Premium
- d) El cifrado con DKE de bibliotecas completas de SharePoint mediante la etiqueta predeterminada de biblioteca

*Respuesta: b).* Antes, la etiqueta predeterminada de biblioteca solo actuaba sobre archivos nuevos o editados; su estado (GA o vista previa) varía según la fuente. [Fuente](https://office365itpros.com/2026/11/05/auto-label-policy-default-label/) · Repasa [M1](02_Nivel_2_Intermedio.md#m1)

**5. ¿Qué afirmación sobre el escáner de Information Protection es correcta?**

- a) Etiqueta en tiempo real cada archivo que se guarda
- b) Solo admite recursos NFS y ya en disponibilidad general
- c) Rastrea por ciclos y admite un modo solo descubrimiento  ✅
- d) No admite bibliotecas de SharePoint Server

*Respuesta: c).* El escáner rastrea recursos SMB, NFS (vista previa) y bibliotecas de SharePoint Server por ciclos, admite clústeres multinodo y modo solo descubrimiento. [Fuente](https://learn.microsoft.com/en-us/purview/deploy-scanner) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**6. ¿Qué nivel de permisos de Rights Management incluye el derecho EXTRACT (Copiar)?**

- a) Visor
- b) Revisor
- c) Ninguno: EXTRACT solo se concede por PowerShell
- d) Coautor  ✅

*Respuesta: d).* EXTRACT está en Coautor y Copropietario; Visor y Revisor no lo incluyen, algo que afecta, por ejemplo, a Copilot. [Fuente](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**7. Con Advanced Message Encryption, ¿qué correos se pueden revocar?**

- a) Los entregados por el portal de OME con una plantilla de marca personalizada  ✅
- b) Cualquier correo cifrado, incluso si el destinatario lo recibió de forma nativa en Outlook
- c) Solo los correos internos cifrados con Encrypt-Only
- d) Solo los correos cifrados con DKE desde Outlook para Windows

*Respuesta: a).* Si el destinatario recibió la experiencia nativa, con una cuenta de Microsoft 365 o Microsoft, el correo no se puede revocar. [Fuente](https://learn.microsoft.com/en-us/purview/revoke-ome-encrypted-mail) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**8. ¿Cuál es el estado predeterminado de la característica de superusuario de Rights Management?**

- a) Habilitada para todos los Global Administrators
- b) Deshabilitada; se habilita cuando hace falta y se audita  ✅
- c) Habilitada solo para el contenido cifrado con DKE
- d) Habilitada de forma permanente para el grupo Information Protection Admins

*Respuesta: b).* Concede control total sobre todo el contenido cifrado del tenant; conviene habilitarla solo cuando se necesita y auditarla con Get-AipServiceAdminLog. [Fuente](https://learn.microsoft.com/en-us/purview/encryption-super-users) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**9. Ya no quieres usar una etiqueta que cifra. ¿Qué conviene hacer?**

- a) Eliminarla y borrar su plantilla de protección
- b) Cambiarle el nombre a Público
- c) Quitarla de la política de etiquetas  ✅
- d) Eliminarla y crearla de nuevo con el mismo nombre

*Respuesta: c).* Si se elimina, su plantilla de protección se archiva; si además se borra, el contenido cifrado queda inaccesible. [Fuente](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) · Repasa [M2](02_Nivel_2_Intermedio.md#m2)

**10. Sobre las etiquetas para reuniones de Teams, ¿qué es cierto?**

- a) Admiten auto-etiquetado a partir del contenido de la invitación
- b) Pueden usar DKE para cifrar la invitación y el chat
- c) Aplican también a los eventos en vivo de Teams
- d) Varias opciones de reunión requieren Teams Premium  ✅

*Respuesta: d).* No admiten auto-etiquetado, S/MIME ni DKE y no aplican a eventos en vivo; «Apply meeting label to artifacts» está en vista previa. [Fuente](https://learn.microsoft.com/en-us/purview/sensitivity-labels-meetings) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**11. ¿Qué licencias se requieren para aplicar etiquetas a elementos de Power BI?**

- a) Solo Power BI gratuito, porque la etiqueta no restringe el acceso
- b) AIP Premium P1 o P2 (incluidas en las suites) más Power BI Pro o PPU  ✅
- c) Solo Teams Premium para las personas que crean informes
- d) Una capacidad F64, sin licencias por usuario

*Respuesta: b).* Ver y aplicar etiquetas requiere AIP Premium P1 o P2, y aplicarlas a elementos de Power BI y Fabric requiere además Pro o PPU. [Fuente](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-enable-data-sensitivity-labels) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**12. ¿Cómo funcionan hoy las etiquetas en Data Map?**

- a) Solo auto-etiquetado como metadatos del activo, en vista previa y con pago por uso para orígenes no Microsoft 365  ✅
- b) Cifran los archivos de origen en Azure Storage y Amazon S3 con Rights Management
- c) Admiten etiquetado manual y automático, con las mismas marcas de contenido que Office
- d) Están en disponibilidad general e incluidas en Microsoft 365 E3 sin costo adicional

*Respuesta: a).* No hay cifrado, marcas ni etiquetado manual, y no admiten SIT personalizados ni clasificadores avanzados (FAQ del 1 de junio de 2026). [Fuente](https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-faq) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**13. Aplicas la etiqueta de contenedor Altamente confidencial a un equipo de Teams. ¿Qué pasa con los archivos del equipo?**

- a) Heredan la etiqueta y se cifran
- b) Se mueven a una biblioteca protegida
- c) No heredan la etiqueta del contenedor  ✅
- d) Se cifran con DKE

*Respuesta: c).* La etiqueta de contenedor gobierna privacidad, invitados, uso compartido y dispositivos; para los archivos usa una etiqueta predeterminada de biblioteca o auto-etiquetado. [Fuente](https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites) · Repasa [M3](02_Nivel_2_Intermedio.md#m3)

**14. ¿Cuándo se retiran las directivas de archivo de Defender for Cloud Apps?**

- a) El 11 de abril de 2024
- b) El 6 de enero de 2027  ✅
- c) El 31 de marzo de 2027
- d) El 1 de octubre de 2026

*Respuesta: b).* La guía de migración, actualizada el 28 de agosto de 2026, fija el 6 de enero de 2027 y pide recrearlas como DLP o auto-etiquetado de Purview. [Fuente](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

**15. ¿Qué hace hoy la herramienta de migración de directivas de archivo de Defender for Cloud Apps?**

- a) Migra todas las directivas, incluidas las de apps no Microsoft, a políticas de auto-etiquetado
- b) Solo funciona en nubes gubernamentales y soberanas, como paso previo al retiro
- c) Convierte las directivas en políticas de cifrado de Customer Key para SharePoint
- d) Convierte las directivas de SharePoint y OneDrive en DLP o auto-etiquetado de Purview; las de apps no Microsoft, todavía no  ✅

*Respuesta: d).* La DLP de Purview para Box, Dropbox, Google Workspace y Salesforce está en vista previa y requiere el conector; la herramienta no está disponible en nubes gubernamentales o soberanas. [Fuente](https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview) · Repasa [M4](02_Nivel_2_Intermedio.md#m4)

<a id="eval-avanzado"></a>

## Nivel 3 · Avanzado · IA, código, claves y SOC

**1. ¿Qué derechos de uso debe tener una persona para que Copilot use contenido cifrado en su nombre?**

- a) VIEW y EXTRACT  ✅
- b) EDIT y PRINT
- c) Solo OWNER
- d) FORWARD y EXPORT

*Respuesta: a).* La arquitectura de protección de datos de Copilot, actualizada el 3 de noviembre de 2026, exige VIEW y EXTRACT sobre el contenido cifrado. [Fuente](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**2. Copilot crea un documento a partir de un archivo General y otro Confidencial. Cuando se admite la herencia, ¿qué etiqueta recibe el nuevo contenido?**

- a) La de menor prioridad de las fuentes, General
- b) Ninguna: el contenido nuevo siempre nace sin etiqueta
- c) La de mayor prioridad de las fuentes, Confidencial  ✅
- d) Siempre Altamente confidencial, sin importar las fuentes

*Respuesta: c).* El contenido generado hereda la etiqueta de mayor prioridad; en las apps de Office la herencia requiere la licencia de Microsoft 365 Copilot. [Fuente](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**3. Según la arquitectura de protección de datos de Copilot, ¿qué archivos no pueden leer los agentes?**

- a) Los archivos sin ninguna etiqueta de confidencialidad
- b) Los archivos con permisos definidos por el usuario  ✅
- c) Los correos internos enviados dentro del tenant
- d) Los PDF exportados desde Office con etiqueta

*Respuesta: b).* Para el contenido que deben consumir agentes, usa etiquetas con permisos asignados por el administrador. [Fuente](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**4. ¿Cómo se configura BlockContentAnalysisServices y qué efecto colateral tiene?**

- a) En el portal de Purview, como una opción más de la etiqueta y sin efectos colaterales
- b) En Entra ID, como una directiva de Acceso condicional que bloquea a Copilot
- c) En el centro de administración de Teams; además desactiva la grabación de reuniones
- d) Solo por PowerShell; también desactiva la comprobación DLP del cliente en Outlook clásico  ✅

*Respuesta: d).* Se configura con Set-Label -Settings y se amplió a Microsoft 365 Copilot con MC1297982 en mayo de 2026; además dejan de funcionar las respuestas sugeridas y la predicción de texto. [Fuente](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**5. ¿Qué licencias habilitan la DLP que impide a Copilot procesar archivos y correos etiquetados?**

- a) Microsoft 365 E3
- b) Microsoft 365 Business Premium sin complementos
- c) Microsoft 365 E5 o A5, Purview Suite, E5 IP&G u Office 365 E5  ✅
- d) Ninguna: está incluida para todos los usuarios de Copilot Chat

*Respuesta: c).* La DLP sobre prompts sí está disponible para todos los usuarios de Copilot y Copilot Chat; la restricción sobre contenido etiquetado es de nivel E5. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [A1](03_Nivel_3_Avanzado.md#a1)

**6. ¿Qué describe mejor a assignSensitivityLabel de Microsoft Graph?**

- a) Una API protegida y medida, asíncrona, que pide justificación para bajar o quitar una etiqueta  ✅
- b) Una API gratuita y síncrona que también aplica las marcas de contenido
- c) Una API disponible solo en nubes gubernamentales y soberanas
- d) Un cmdlet del cliente de Information Protection para archivos locales

*Respuesta: a).* Requiere habilitar las API medidas; Office no aplica marcas de contenido a los archivos etiquetados por esta vía y la API devuelve el error 423 con DKE. [Fuente](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**7. ¿Qué buena práctica aplica a Export-ContentExplorerData?**

- a) Un único script para todas las etiquetas, sin reconectar la sesión
- b) Un script por etiqueta o SIT, reconectando la sesión porque el token expira en cerca de una hora  ✅
- c) Ejecutarlo solo desde el portal de Purview, porque no admite certificados
- d) Usarlo solo con archivos cifrados con DKE en OneDrive

*Respuesta: b).* También conviene reanudar con PageCookie y usar autenticación por certificado con el rol Content Explorer List Viewer. [Fuente](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**8. ¿Desde qué versión admite DKE el MIP SDK?**

- a) Desde la 1.0
- b) Desde la 1.18
- c) No admite DKE
- d) Desde la 1.7  ✅

*Respuesta: d).* La documentación de DKE indica soporte desde la versión 1.7; la documentación del SDK referencia la 1.18 como versión actual. [Fuente](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Repasa [A2](03_Nivel_3_Avanzado.md#a2)

**9. ¿Qué NO funciona con contenido cifrado con DKE?**

- a) Etiquetar desde el Explorador de archivos
- b) La coautoría y AutoSave  ✅
- c) Guardar el archivo en SharePoint
- d) Abrir un PDF con DKE en el visor del cliente

*Respuesta: b).* DKE deshabilita la coautoría y AutoSave; el archivo se puede guardar en SharePoint, aunque el servicio no lo procesa. [Fuente](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**10. ¿Qué exige Customer Key en cuanto a licencias?**

- a) Una licencia por cada administrador que gestiona las claves en Azure Key Vault
- b) Licencias solo para los usuarios de SharePoint, porque Exchange y Teams se cuentan aparte
- c) Al menos tantas licencias como usuarios con Exchange o Teams; si faltan, vuelve al cifrado de servicio predeterminado  ✅
- d) Pago por uso por cada clave raíz y por cada política de cifrado creada

*Respuesta: c).* Está incluido en Microsoft 365 E5, A5 y G5, Purview Suite, E5 IP&G y Office 365 E5; SharePoint se cuenta aparte. [Fuente](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**11. ¿Qué cubre la política de cifrado multicarga de Customer Key?**

- a) Teams, interacciones de Microsoft 365 Copilot, Exchange, datos de EDM y configuraciones de etiquetas  ✅
- b) Solo los archivos de SharePoint y OneDrive, incluidas sus versiones anteriores
- c) Solo los buzones de Exchange, con un máximo de 50 políticas activas
- d) Los endpoints con Windows y los recursos compartidos que rastrea el escáner

*Respuesta: a).* Las otras dos políticas son de buzones de Exchange y de SharePoint y OneDrive; revocar las claves inicia la eliminación criptográfica de los datos. [Fuente](https://learn.microsoft.com/en-us/purview/customer-key-overview) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**12. ¿Para qué proporción de los datos sugiere Microsoft usar DKE?**

- a) Para todos los datos de la organización, por defecto
- b) Para cerca de la mitad de los datos, los etiquetados como Confidencial
- c) Para ningún dato en producción: solo para pruebas
- d) Para cerca del 5 % de los datos más sensibles  ✅

*Respuesta: d).* DKE quita capacidades importantes (coautoría, procesamiento en SharePoint, Copilot), por lo que se reserva para una fracción pequeña de datos muy sensibles. [Fuente](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Repasa [A3](03_Nivel_3_Avanzado.md#a3)

**13. ¿En qué tabla deja los eventos el conector de Purview Information Protection para Sentinel?**

- a) SecurityEvent
- b) MicrosoftPurviewInformationProtection  ✅
- c) AzureActivity
- d) InformationProtectionLogs_CL

*Respuesta: b).* El conector, en vista previa, reemplaza al de AIP y envía eventos de etiquetado, protección y escáner a esa tabla. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**14. ¿Qué latencia típica tiene el explorador de actividades?**

- a) Tiempo real, en menos de un minuto
- b) Hasta siete días
- c) Entre 60 y 90 minutos  ✅
- d) Treinta días, igual que su retención

*Respuesta: c).* Conserva hasta 30 días de datos y los eventos aparecen típicamente entre 60 y 90 minutos después. [Fuente](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

**15. ¿Qué requisito de licencia y configuración tiene el conector de Purview Information Protection para Sentinel?**

- a) Microsoft 365 E5 o Purview Suite para todas las personas auditadas, sin auditoría
- b) Teams Premium y la auditoría habilitada en el tenant de Sentinel
- c) Una licencia de Security Copilot con SCU aprovisionadas en la región del workspace
- d) Una licencia con Audit (E3, A3, Business Basic o superior) y la auditoría habilitada  ✅

*Respuesta: d).* Además, su página todavía describe el portal de Azure, aunque Sentinel se opera hoy desde el portal de Defender. [Fuente](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Repasa [A4](03_Nivel_3_Avanzado.md#a4)

<a id="eval-operacion"></a>

## Nivel 4 · Operación · Programa, métricas y gobierno

**1. ¿Cuál es el primer paso del modelo secure by default de Microsoft Purview?**

- a) Aplicar DKE a todo el contenido
- b) Empezar con etiquetado predeterminado  ✅
- c) Bloquear todo el correo externo
- d) Auto-etiquetar los buzones en reposo

*Respuesta: b).* El paso 1 propone una taxonomía con etiquetado predeterminado y su configuración de cifrado, marcas y DLP. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step1) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**2. ¿Qué propone enseñar a las personas el modelo secure by default?**

- a) A decidir cuándo proteger cada archivo
- b) A configurar Rights Management
- c) A gestionar las excepciones  ✅
- d) A escribir consultas KQL

*Respuesta: c).* Si todo se protege por defecto, la capacitación se concentra en cómo y cuándo pedir una excepción. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**3. En el paso 2 del modelo secure by default, ¿qué se recomienda auto-etiquetar como Altamente confidencial?**

- a) Todas las credenciales  ✅
- b) Todas las presentaciones
- c) Todos los PDF
- d) Todos los correos externos

*Respuesta: a).* El paso 2 también prioriza los sitios críticos con etiqueta de sitio y de biblioteca y usa DLP para el contenido sin etiqueta. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step2) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**4. Publicaste cambios en una política de etiquetas dirigida a un grupo recién creado. ¿Cuándo conviene empezar a diagnosticar?**

- a) De inmediato, porque los cambios son instantáneos
- b) A los 5 minutos, cuando termina la sincronización
- c) A los 30 días, cuando se renueva la licencia de uso
- d) Después de 24 a 48 horas  ✅

*Respuesta: d).* Los cambios en etiquetas y políticas tardan hasta 24 horas, y de 24 a 48 si dependen de grupos nuevos. [Fuente](https://learn.microsoft.com/en-us/purview/create-sensitivity-labels) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**5. ¿Desde dónde recomienda la guía de despliegue de Microsoft arrancar un programa de Information Protection?**

- a) Desde DSPM, con las etiquetas y políticas predeterminadas  ✅
- b) Desde el escáner local, inventariando primero los recursos compartidos
- c) Desde Customer Key, cifrando primero todos los buzones
- d) Desde el portal clásico de cumplimiento

*Respuesta: a).* La guía organiza el despliegue en conocer, proteger y prevenir y recomienda exigir justificación para bajar una etiqueta. [Fuente](https://learn.microsoft.com/en-us/purview/information-protection-solution) · Repasa [O1](04_Nivel_4_Operacion.md#o1)

**6. Los informes de postura de Information Protection…**

- a) Están en disponibilidad general y conservan un año de historial
- b) Están en vista previa, usan una ventana móvil de 30 días y conviene guardarlos en PDF  ✅
- c) Solo existen con Microsoft 365 E3
- d) Requieren Microsoft Sentinel

*Respuesta: b).* Muestran distribución y adopción de etiquetas, cobertura de auto-etiquetado y actividad; para conservar histórico hay que guardarlos o exportar datos. [Fuente](https://learn.microsoft.com/en-us/purview/purview-reports) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**7. Necesitas la tendencia anual de bajadas de etiqueta. ¿Qué haces?**

- a) Pides al soporte que amplíe la retención del explorador
- b) Usas el informe de etiquetas de Unified Catalog, que guarda un año de tendencia
- c) Exportas periódicamente con Export-ActivityExplorerData hacia un almacén propio  ✅
- d) Cambias a 365 días la ventana del informe de postura en su configuración

*Respuesta: c).* El explorador de actividades conserva 30 días; las series largas se construyen con exportaciones programadas. [Fuente](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**8. ¿Cuándo muestra datos el informe clásico de etiquetas de Unified Catalog?**

- a) Siempre, para todo el contenido de Microsoft 365 y del Data Map
- b) Solo en tenants con Microsoft 365 E3 sin Purview Suite
- c) Solo para el correo de Exchange
- d) Solo si extendiste las etiquetas al Data Map  ✅

*Respuesta: d).* Mide la cobertura de etiquetas en activos del Data Map (Azure, SQL, Amazon S3 y RDS, Power BI), una capacidad en vista previa con pago por uso. [Fuente](https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-sensitivity-labels) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**9. ¿Cuál de estas es una rutina operativa del paso 4 del modelo secure by default?**

- a) Revisar sitios sin etiqueta y desalineaciones entre la etiqueta del sitio y la de la biblioteca con Graph  ✅
- b) Eliminar cada mes las etiquetas que cifran y crearlas de nuevo con permisos actualizados
- c) Desactivar la auditoría unificada fuera del horario laboral para ahorrar costos
- d) Reentrenar cada semana los clasificadores integrados con documentos del tenant

*Respuesta: a).* El paso 4 también propone DLP para etiquetas sin protección y el seguimiento de usuarios de riesgo con Insider Risk. [Fuente](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-step4) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**10. ¿Qué fuente usarías para medir las bajadas de etiqueta con su justificación?**

- a) El Usage center de Purview, que registra cada cambio de etiqueta
- b) Compliance Manager, en las acciones de mejora de etiquetado
- c) El explorador de actividades o la tabla MicrosoftPurviewInformationProtection  ✅
- d) El informe clásico de etiquetas de Unified Catalog

*Respuesta: c).* La tabla incluye columnas como LabelName, OldSensitivityLabelId, JustificationText y Operation. [Fuente](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/microsoftpurviewinformationprotection) · Repasa [O2](04_Nivel_4_Operacion.md#o2)

**11. ¿Desde cuándo rige la Ley 21.719 de protección de datos personales de Chile?**

- a) Desde el 13 de diciembre de 2024
- b) Desde el 1 de diciembre de 2026  ✅
- c) Desde el 20 de marzo de 2025
- d) Desde el 30 de noviembre de 2024

*Respuesta: b).* Se publicó el 13 de diciembre de 2024 y entra en vigencia el 1 de diciembre de 2026; el 20 de marzo de 2025 corresponde a la nueva LFPDPPP de México y el 30 de noviembre de 2024 al reglamento peruano. [Fuente](https://www.leychile.cl/leychile/navegar?idNorma=1209272) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**12. ¿Cuántas regulaciones premium sin costo, además de la línea base de Microsoft, permiten usar las licencias A5, E5 y G5 en Compliance Manager?**

- a) Una
- b) Diez
- c) Todas
- d) Tres  ✅

*Respuesta: d).* La lista de regulaciones incluye secciones de América Latina y Sudamérica; las plantillas adicionales consumen cupo. [Fuente](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

**13. Ante el requisito de una ley de datos personales, ¿cuál es el papel del equipo de Information Protection?**

- a) Traducir los requisitos que Legal y Privacidad validaron en SIT, etiquetas, cifrado y evidencias  ✅
- b) Interpretar la ley por su cuenta y decidir los controles sin consultar a otras áreas
- c) Esperar la primera auditoría del regulador para decidir qué controles aplicar
- d) Aplicar DKE a todos los datos personales para cumplir cualquier norma de la región

*Respuesta: a).* Esta guía no da asesoría legal: Legal y Privacidad interpretan la norma y el equipo técnico la convierte en controles medibles, apoyándose en herramientas como las plantillas de Compliance Manager. [Fuente](https://learn.microsoft.com/es-es/purview/compliance-manager-regulations-list) · Repasa [O3](04_Nivel_4_Operacion.md#o3)

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

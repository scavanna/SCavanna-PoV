# Nivel 3 · Avanzado · IA, código, claves y SOC

*Microsoft Purview Information Protection Ninja Training: clasificación, etiquetado y cifrado · Edición 2026*

[← Nivel 2 · Intermedio](02_Nivel_2_Intermedio.md) · [Índice del programa](README.md) · [Nivel 4 · Operación →](04_Nivel_4_Operacion.md)

<a id="avanzado"></a>

Copilot y agentes, automatización con PowerShell, Microsoft Graph y el MIP SDK, Customer Key y Double Key Encryption, y monitoreo con el SOC. Terminas con una matriz de derechos de uso para Copilot, una decisión documentada sobre claves y una detección de bajadas de etiqueta.

*L400 · 4 módulos · ~20 horas · 25 recursos*

**Módulos de este nivel:** [A1 Copilot y agentes](#a1) · [A2 PowerShell, Graph y SDK](#a2) · [A3 Customer Key y DKE](#a3) · [A4 Monitoreo y SOC](#a4)

<a id="a1"></a>

## A1 · Information Protection para Microsoft 365 Copilot y agentes

*L400 · ~5 h · Origen: Nuevo en esta edición (complementa el módulo 3 de la ruta Ninja de Learn y el blueprint oficial de Copilot)*

Copilot no se salta los permisos: solo resume o cita contenido al que la persona ya tiene acceso. Con contenido cifrado, además, necesita que esa persona tenga los derechos de uso **VIEW y EXTRACT**; el contenido que Copilot genera hereda la etiqueta de mayor prioridad de sus fuentes cuando se admite; Copilot Chat muestra la etiqueta; los agentes no pueden leer archivos con permisos definidos por el usuario; y el contenido con DKE es inaccesible para Copilot. Todo esto está en la arquitectura de protección de datos de Copilot, actualizada el 3 de noviembre de 2026, y convierte las etiquetas en el principal control de datos para la IA.

Hay controles adicionales con licencias distintas: la **DLP para Copilot** que impide procesar archivos y correos etiquetados (nivel E5) y la DLP sobre prompts (disponible para todos los usuarios de Copilot y Copilot Chat), que se profundizan en el programa de DLP; la configuración **BlockContentAnalysisServices**, solo por PowerShell, que bloquea el análisis por servicios conectados con efectos colaterales; y las **etiquetas de contenedor** para cortar la sobreexposición. Para agentes de Microsoft Foundry y apps conectadas a Entra, Purview se licencia con Microsoft 365 E7 o Agent 365, un tema que sigue el programa de DSPM.

Microsoft resume el camino en un blueprint de tres pilares —remediar la sobreexposición, poner guardarraíles con Purview y SharePoint Advanced Management, y cumplir con la regulación de IA— y en una guía detallada para construir una base segura y gobernada antes de ampliar Copilot.

**Por qué importa**

Copilot amplifica lo que tus permisos y etiquetas ya dicen: el contenido sobrecompartido y sin etiqueta se vuelve encontrable en lenguaje natural. Diseñar etiquetas con los derechos de uso correctos, herencia y exclusiones es la diferencia entre un despliegue de Copilot que el CISO puede aprobar y uno que Legal frena. Además, da evidencia medible al comité de gobierno de IA, como la cobertura de etiquetas en los sitios del alcance.

**Qué vas a lograr**

- Explicar cómo Copilot y los agentes respetan permisos, cifrado y derechos de uso (VIEW y EXTRACT).
- Diseñar etiquetas que permitan, limiten o excluyan el uso por Copilot y documentar su efecto.
- Comprobar la herencia de etiquetas en el contenido generado por Copilot.
- Elegir entre DLP para Copilot, BlockContentAnalysisServices, DKE y etiquetas de contenedor según el riesgo.
- Ubicar el licenciamiento de Copilot, E5, E7 y Agent 365 para cada control.

> **Novedad.** Arquitectura de protección de datos de Copilot, actualizada el 3 de noviembre de 2026: Copilot solo usa contenido al que la persona tiene acceso, requiere VIEW y EXTRACT sobre contenido cifrado, el contenido generado hereda la etiqueta de mayor prioridad cuando se admite y los agentes no pueden leer archivos con permisos definidos por el usuario ([arquitectura](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing)). El contenido con DKE no es accesible para Copilot ni en reposo ni en uso ([DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption)).

> **Atención.** BlockContentAnalysisServices se configura solo por PowerShell (`Set-Label -Settings`), impide que Microsoft 365 Copilot y otras experiencias conectadas analicen los archivos con esa etiqueta y se amplió con MC1297982 en mayo de 2026. Efectos colaterales: deja de funcionar la comprobación DLP del cliente en Outlook clásico, las respuestas sugeridas y la predicción de texto ([análisis](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/)).

> **Atención.** Licencias: Copilot Chat muestra las etiquetas, pero la herencia en las apps de Office requiere la licencia de Microsoft 365 Copilot (complemento, incluida en E7). La DLP que impide a Copilot procesar archivos y correos etiquetados requiere Microsoft 365 E5 o A5, Purview Suite, E5 IP&G u Office 365 E5; la DLP sobre prompts está disponible para todos los usuarios de Copilot y Copilot Chat ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). La configuración de esa DLP se profundiza en el programa de DLP de esta serie.

> **Consejo Ninja.** Sigue el blueprint oficial de tres pilares —remediar la sobreexposición, poner guardarraíles con Purview y SharePoint Advanced Management (incluido con la licencia de Copilot) y cumplir con la regulación de IA— ([blueprint](https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance)) y su recorrido detallado, que distingue capacidades fundacionales de E3 y optimizadas de E5 ([base segura y gobernada](https://learn.microsoft.com/en-gb/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot?tabs=dlm%2Caihub)).

**¿Tienes poco tiempo?**

- [Microsoft Copilot data protection architecture (How data is protected and audited in Microsoft 365 and Microsoft Copilot)](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Documentación
- [Secure and govern Microsoft Copilot: Foundational deployment guidance (deployment blueprint)](https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance) · Documentación
- [Microsoft Extends Sensitivity Label Block for Connected Services (BlockContentAnalysisServices)](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/) · Blog
- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog

### Documentación, cursos y credenciales

- [Microsoft Copilot data protection architecture (How data is protected and audited in Microsoft 365 and Microsoft Copilot)](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Explica cómo Copilot respeta etiquetas y cifrado: solo usa contenido al que el usuario tiene acceso, requiere derechos EXTRACT y VIEW sobre contenido cifrado y hereda la etiqueta de mayor prioridad en el contenido generado.
- [Secure and govern Microsoft Copilot: Foundational deployment guidance (deployment blueprint)](https://learn.microsoft.com/en-us/copilot/plan/secure-govern-copilot-foundational-deployment-guidance) · Documentación · Oficial · Nuevo · Microsoft Learn · 3 nov 2026. Blueprint oficial (PDF y PowerPoint) de tres pilares para Copilot: remediar sobreexposición de datos, establecer guardarraíles con Purview y SharePoint Advanced Management y cumplir regulaciones de IA.
- [Configure a secure and governed foundation for Microsoft 365 Copilot](https://learn.microsoft.com/en-gb/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot?tabs=dlm%2Caihub) · Documentación · Oficial · Microsoft Learn. Recorrido detallado del blueprint: evaluar con DSPM y SAM, aplicar Restricted Content Discovery y DLP para Copilot, etiquetar sitios, corregir permisos y monitorear con auditoría.
- [View sensitivity labels in connectors (Power Platform 2026 release wave 1)](https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/view-sensitivity-labels-connectors) · Documentación · Oficial · Nuevo · Microsoft Learn - Power Platform release plan · 27 ago 2026. Plan de lanzamiento para que conectores de Power Platform y Copilot transfieran y muestren etiquetas de confidencialidad, empezando por Copilot Studio (preview nov-2025, GA prevista jun-2026).

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Extends Sensitivity Label Block for Connected Services (BlockContentAnalysisServices)](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/) · Blog · MVP · Nuevo · Tony Redmond · Office 365 for IT Pros · 8 jun 2026. Explica la configuración avanzada BlockContentAnalysisServices (solo PowerShell) que impide que Microsoft 365 Copilot y otras experiencias conectadas analicen archivos con cierta etiqueta, ampliada en MC1297982 (may-2026).
- [How to Deploy Microsoft Purview DLP for Copilot and Generative AI](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/) · Blog · MVP · Nuevo · Nikki Chapple · 20 may 2026. Seis controles DLP prioritarios para Copilot e IA generativa (bloquear prompts sensibles, grounding web, acceso de Copilot a contenido etiquetado, pegado/subida a sitios de IA, subida de archivos etiquetados y protección inline en Edge) con su licencia requerida.
- [Microsoft Purview: DSPM-Copilot Readiness and Data Explorer (roadmap 571157)](https://m365admin.handsontek.net/microsoft-purview-dspm-copilot-readiness-data-explorer/) · Blog · Oficial · Vista previa · Nuevo · Microsoft (republicado) · M365 Admin (HANDS ON tek) · 16 sep 2026. Republica el aviso de Microsoft sobre las experiencias de preparación para Copilot y explorador de datos en DSPM (preview sep-2026, disponibilidad prevista ene-2027). *Nota:* Roadmap ID 571157; fechas sujetas a cambio tras Ignite 2026
- [Securing AI with Microsoft Purview](https://alberthoitingh.com/2025/08/07/securing-ai-with-microsoft-purview/) · Blog · MVP · Legado aún útil · Albert Hoitingh · Albert Hoitingh - Information security and compliance · 7 ago 2025. Arquitectura de ejemplo para agentes en Azure AI Foundry que respetan etiquetas, políticas de protección en Blob/Cosmos DB, DLP y el Purview SDK. *Nota:* Azure AI Foundry ahora se denomina Microsoft Foundry; el Purview SDK estaba en preview

**Manos a la obra**

1. `Laboratorio` Construye la matriz de tus etiquetas: para cada una, el nivel de permisos, si concede VIEW y EXTRACT a las personas previstas y qué podrá hacer Copilot (resumir, citar o nada). Usa la [Taxonomía de ejemplo](00_Programa.md#taxonomia) y la tabla de derechos de uso ([derechos de uso](https://learn.microsoft.com/en-us/purview/rights-management-usage-rights), [arquitectura](https://learn.microsoft.com/en-us/copilot/plan/architecture-data-protection-auditing)).
2. `Laboratorio parcial` Con una persona que tenga licencia de Microsoft 365 Copilot (sandbox de desarrollador o piloto), pide a Copilot que resuma tres documentos: uno cifrado con Coautor, uno cifrado con Visor (sin EXTRACT) y uno sin cifrado; documenta las respuestas y, si usas agentes, repite con un archivo con permisos definidos por el usuario. Limitación: la prueba E5 no trae Copilot, y Copilot Chat muestra las etiquetas pero la herencia en las apps de Office requiere la licencia.
3. `Laboratorio parcial` Pide a Copilot en Word que cree un documento a partir de un archivo Confidencial y otro General y comprueba que el nuevo hereda la etiqueta de mayor prioridad. Limitación: la misma licencia del paso anterior.
4. `Laboratorio parcial` Aplica `BlockContentAnalysisServices` a una etiqueta de prueba con `Set-Label -Settings`, documenta los efectos colaterales en Outlook clásico y luego revierte el ajuste ([análisis](https://office365itpros.com/2026/06/08/blockcontentanalysisservices-label/)). Limitación: comprobar que Copilot deja de analizar esos archivos requiere una licencia de Microsoft 365 Copilot.
5. `Laboratorio parcial` Crea en modo simulación una directiva DLP para la ubicación de Microsoft 365 Copilot que excluya del procesamiento los archivos con la etiqueta Altamente confidencial ([directiva predeterminada de Copilot](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy), [seis controles para IA](https://nikkichapple.com/microsoft-purview-dlp-copilot-genai-setup-guide/)). Limitación: ver el efecto real requiere licencias de Copilot; el diseño de la directiva se profundiza en el programa de DLP.
6. `Solo producción` Piloto de Copilot con etiquetas: un sitio de prueba con contenido sintético etiquetado, personas piloto que ya tienen Copilot y auditoría activa. Empieza con etiquetas sin cifrado, revisa los eventos CopilotInteraction en el explorador de actividades y después agrega cifrado. Forma segura: DLP para Copilot en simulación, sin tocar sitios críticos y con una revisión de sobreexposición en DSPM antes de ampliar.

<a id="a2"></a>

## A2 · Automatización, SDK y APIs

*L400 · ~4 h · Origen: Nuevo en esta edición (guía SC-401: cliente y PowerShell)*

A escala, todo es código. Con **Security & Compliance PowerShell** inventarías y cambias etiquetas y políticas (`Get-Label`, `Set-Label`, `Get-LabelPolicy`); con el SDK de Microsoft Graph lees las etiquetas del tenant; con el módulo del cliente para Windows etiquetas archivos locales; y con `Export-ActivityExplorerData` y `Export-ContentExplorerData` construyes evidencia y series históricas más allá de las ventanas de 30 días del portal.

**Microsoft Graph** ofrece `assignSensitivityLabel` para asignar o quitar etiquetas de archivos de SharePoint y OneDrive —una API protegida y medida, asíncrona, que pide justificación para bajar o quitar y no agrega marcas de contenido— y `extractSensitivityLabels` para leerlas. Para aplicaciones propias o de terceros, el **MIP SDK** (File, Policy y Protection) lee y aplica etiquetas y cifrado en Windows, Linux, macOS, Android e iOS, y admite DKE desde la versión 1.7.

La disciplina es la de cualquier configuración crítica: línea base versionada en un repositorio, registros de aplicación con mínimo privilegio y autenticación por certificado, pruebas antes de cambiar en producción y registro de cada ejecución.

**Por qué importa**

Los clics manuales no escalan a miles de sitios ni a auditorías que piden «todos los cambios de etiquetas del trimestre». La automatización convierte el etiquetado en una configuración repetible, probada y auditable; las API permiten que aplicaciones de negocio y procesos de datos respeten las mismas etiquetas; y las exportaciones programadas construyen la evidencia histórica que el portal no conserva.

**Qué vas a lograr**

- Inventariar y versionar etiquetas y políticas con PowerShell y el SDK de Microsoft Graph.
- Asignar y extraer etiquetas de archivos de SharePoint y OneDrive con Microsoft Graph, conociendo sus costos y límites.
- Exportar datos del explorador de actividades y del explorador de contenido de forma programada y paginada.
- Describir cuándo usar el MIP SDK y qué requisitos tiene una aplicación que lo integra.

> **Atención.** `assignSensitivityLabel` es una API protegida y medida, con cargo: requiere habilitar las API medidas, es asíncrona y pide justificación para bajar o quitar una etiqueta. Office no aplica marcas de contenido a los archivos etiquetados por esta vía, no está disponible en nubes gubernamentales y devuelve el error 423 con DKE ([assignSensitivityLabel](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0)). Para leer, `extractSensitivityLabels` necesita como mínimo Files.Read.All ([extractSensitivityLabels](https://learn.microsoft.com/en-us/graph/api/driveitem-extractsensitivitylabels?view=graph-rest-1.0)).

> **Consejo Ninja.** `Export-ActivityExplorerData` devuelve JSON o CSV paginado con PageCookie ([actividades](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps)); `Export-ContentExplorerData` conviene ejecutarlo con un script por etiqueta o SIT, reconectando la sesión porque el token expira en cerca de una hora, y admite autenticación por certificado con el rol Content Explorer List Viewer ([contenido](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-contentexplorerdata?view=exchange-ps)).

> **Novedad.** El MIP SDK (File, Policy y Protection) funciona en Windows, Linux, macOS, Android e iOS; la documentación, actualizada el 21 de septiembre de 2026, referencia la versión 1.18 y el soporte de Java está en vista previa ([MIP SDK](https://learn.microsoft.com/en-us/information-protection/develop/overview)). Para desarrollar necesitas etiquetas configuradas, una app registrada en Entra ID y solicitar el Information Protection Integration Agreement ([configuración](https://learn.microsoft.com/en-us/information-protection/develop/setup-configure-mip)).

**¿Tienes poco tiempo?**

- [driveItem: assignSensitivityLabel - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0) · Documentación
- [Overview - Microsoft Information Protection SDK](https://learn.microsoft.com/en-us/information-protection/develop/overview) · Documentación
- [Export-ActivityExplorerData (ExchangePowerShell)](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps) · Documentación
- [Primer: Finding Sensitivity Labels with PowerShell](https://office365itpros.com/2026/06/11/sensitivity-label-ps/) · Blog

### Documentación, cursos y credenciales

- [Overview - Microsoft Information Protection SDK](https://learn.microsoft.com/en-us/information-protection/develop/overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 21 sep 2026. Presenta el MIP SDK (File, Policy y Protection SDK) para que aplicaciones de terceros lean y escriban etiquetas y cifrado, con plataformas compatibles (Windows, Linux, macOS, Android, iOS).
- [driveItem: assignSensitivityLabel - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn - Microsoft Graph. API de Graph (protegida y medida/con cargo) para asignar o quitar de forma asíncrona una etiqueta a un archivo de SharePoint/OneDrive, con método de asignación y justificación para bajar o quitar la etiqueta.
- [driveItem: extractSensitivityLabels - Microsoft Graph v1.0](https://learn.microsoft.com/en-us/graph/api/driveitem-extractsensitivitylabels?view=graph-rest-1.0) · Documentación · Oficial · Microsoft Learn - Microsoft Graph. API de Graph para extraer las etiquetas asignadas a un archivo y actualizar sus metadatos en SharePoint/OneDrive, útil para inventarios y automatizaciones.
- [Microsoft Information Protection (MIP) SDK setup and configuration](https://learn.microsoft.com/en-us/information-protection/develop/setup-configure-mip) · Documentación · Oficial · Microsoft Learn. Pasos previos para desarrollar con el MIP SDK: suscripción, etiquetas configuradas, estación de trabajo, registro de la app en Entra ID y solicitud del Information Protection Integration Agreement (IPIA).

### Comunidad: blogs, libros, newsletters y eventos

- [Primer: Finding Sensitivity Labels with PowerShell](https://office365itpros.com/2026/06/11/sensitivity-label-ps/) · Blog · MVP · Nuevo · Tony Redmond · Office 365 for IT Pros · 11 jun 2026. Muestra cómo inventariar etiquetas con PowerShell usando Get-Label (Security & Compliance) y el cmdlet Get-MgSecurityDataSecurityAndGovernanceSensitivityLabel del SDK de Microsoft Graph.

**Manos a la obra**

1. `Laboratorio` Exporta etiquetas y políticas a JSON con `Get-Label` y `Get-LabelPolicy` y con `Get-MgSecurityDataSecurityAndGovernanceSensitivityLabel` del SDK de Graph; guárdalas en un repositorio como línea base y compara dos versiones después de un cambio ([inventario](https://office365itpros.com/2026/06/11/sensitivity-label-ps/)).
2. `Laboratorio` Registra una app de Entra con Files.Read.All y usa `extractSensitivityLabels` para listar las etiquetas de los archivos de una biblioteca de prueba ([extractSensitivityLabels](https://learn.microsoft.com/en-us/graph/api/driveitem-extractsensitivitylabels?view=graph-rest-1.0)).
3. `Laboratorio parcial` Habilita las API medidas con una suscripción de Azure y asigna una etiqueta a un archivo con `assignSensitivityLabel`, incluida una bajada con justificación; verifica que Office no agrega las marcas de contenido ([assignSensitivityLabel](https://learn.microsoft.com/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-1.0)). Limitación: es una API con cargo; úsala sobre pocos archivos y revisa el costo.
4. `Laboratorio` Programa un script diario con autenticación por certificado que ejecute `Export-ActivityExplorerData`, pagine con PageCookie y guarde CSV en un almacenamiento propio ([cmdlet](https://learn.microsoft.com/en-us/powershell/module/exchangepowershell/export-activityexplorerdata?view=exchange-ps)).
5. `Laboratorio` Prepara un entorno de desarrollo con el MIP SDK, lee la etiqueta de un archivo de prueba con un ejemplo de la documentación y documenta los requisitos de registro e IPIA que necesitaría una aplicación de negocio ([MIP SDK](https://learn.microsoft.com/en-us/information-protection/develop/overview), [configuración](https://learn.microsoft.com/en-us/information-protection/develop/setup-configure-mip)).

<a id="a3"></a>

## A3 · Customer Key y Double Key Encryption

*L400 · ~6 h · Origen: Nuevo en esta edición (mapa de capacidades de Information Protection y guía SC-401)*

Son dos respuestas distintas a la pregunta «¿quién controla las claves?». **Customer Key** agrega una capa de cifrado de servicio en reposo con claves raíz del cliente en Azure Key Vault, aplicada con tres tipos de políticas de cifrado (DEP): multicarga (Teams, interacciones de Microsoft 365 Copilot, Exchange, datos de EDM y configuraciones de etiquetas), de buzones de Exchange y de SharePoint y OneDrive. Es transparente para los servicios, que siguen procesando el contenido, y revocar las claves inicia la eliminación criptográfica de los datos. Requiere al menos tantas licencias como usuarios con Exchange o Teams.

**Double Key Encryption (DKE)** cifra con dos claves, una bajo control exclusivo del cliente y otra en Azure, de modo que Microsoft no puede descifrar el contenido. El costo funcional es alto: solo funciona en Microsoft 365 Apps for enterprise para Windows, sin coautoría ni AutoSave; SharePoint y OneDrive no procesan esos archivos; no sirve como etiqueta predeterminada de biblioteca ni en Loop o reuniones; y Copilot no accede al contenido. Microsoft lo reserva para cerca del 5 % de los datos más sensibles y publica un servicio de claves de referencia en GitHub.

Este módulo te ayuda a decidir con criterio: DKE apoya requisitos de custodia o residencia de claves cuando una regulación lo exige, mientras Customer Key protege en reposo sin quitar capacidades. Ambos exigen custodia, respaldo y procedimientos de recuperación probados.

**Por qué importa**

Los reguladores y los directorios preguntan cada vez más quién puede descifrar los datos. Responder con la herramienta correcta evita dos fallas: comprar DKE para todo y perder búsqueda, eDiscovery y Copilot, o prometer un control de claves que Customer Key no da sobre el contenido en uso. Una decisión documentada, con custodia y recuperación probadas, protege a la organización de hallazgos regulatorios y de pérdidas de datos autoinfligidas.

**Qué vas a lograr**

- Diferenciar Customer Key, DKE y el cifrado de servicio predeterminado según quién controla las claves.
- Desplegar el servicio DKE de ejemplo y crear una etiqueta DKE en el laboratorio.
- Documentar el impacto funcional de DKE en coautoría, SharePoint, eDiscovery, DLP y Copilot.
- Diseñar las políticas de cifrado de Customer Key con su runbook de clave de disponibilidad y de revocación.
- Calcular los requisitos de licencias de Customer Key.

> **Atención.** DKE (página actualizada el 27 de octubre de 2026): solo Microsoft 365 Apps for enterprise en Windows; sin coautoría ni AutoSave; SharePoint y OneDrive no procesan los archivos (sin Office web, búsqueda, eDiscovery ni DLP); no sirve como etiqueta predeterminada de biblioteca ni en Loop o reuniones; Outlook no admite Encrypt-Only ni Do Not Forward con DKE; y Copilot no accede al contenido. Microsoft lo recomienda solo para cerca del 5 % de los datos más sensibles ([DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption)).

> **Consejo Ninja.** El servicio de claves de referencia está en [Azure-Samples/DoubleKeyEncryptionService](https://github.com/Azure-Samples/DoubleKeyEncryptionService) y la guía cubre .NET 8, generación de claves, publicación en Azure, registro del almacén, creación de etiquetas y migración desde HYOK ([configurar DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption-setup)). Si pierdes la clave del cliente, el contenido queda inaccesible: documenta custodia, respaldo y prueba de recuperación antes de cualquier uso real.

> **Atención.** Customer Key está incluido en Microsoft 365 E5, A5 y G5, Purview Suite, E5 IP&G y Office 365 E5; el tenant debe tener al menos tantas licencias como usuarios con Exchange o Teams (SharePoint se cuenta aparte) y, si faltan, el cifrado vuelve al cifrado de servicio predeterminado ([descripción del servicio](https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)). Revocar las claves inicia la eliminación criptográfica de los datos ([Customer Key](https://learn.microsoft.com/en-us/purview/customer-key-overview)).

> **Consejo Ninja.** Las políticas de cifrado de Customer Key son de tres tipos: multicarga (Teams, interacciones de Microsoft 365 Copilot, Exchange, datos de EDM y configuraciones de etiquetas), de buzones de Exchange (hasta 50 activas por tenant) y de SharePoint y OneDrive; se administran con Exchange Online PowerShell y Azure PowerShell ([administrar las políticas](https://learn.microsoft.com/en-us/purview/customer-key-manage)).

**¿Tienes poco tiempo?**

- [Double Key Encryption (DKE)](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Documentación
- [Set up Double Key Encryption (DKE)](https://learn.microsoft.com/en-us/purview/double-key-encryption-setup) · Documentación
- [Overview of Service encryption with Microsoft Purview Customer Key](https://learn.microsoft.com/en-us/purview/customer-key-overview) · Documentación
- [Azure-Samples/DoubleKeyEncryptionService](https://github.com/Azure-Samples/DoubleKeyEncryptionService) · GitHub

### Documentación, cursos y credenciales

- [Double Key Encryption (DKE)](https://learn.microsoft.com/en-us/purview/double-key-encryption) · Documentación · Oficial · Nuevo · Microsoft Learn · 27 oct 2026. Explica DKE (una clave bajo control del cliente y otra en Azure), cuándo adoptarlo (solo ~5% de datos altamente sensibles) y qué servicios de Microsoft 365 pierden visibilidad del contenido.
- [Set up Double Key Encryption (DKE)](https://learn.microsoft.com/en-us/purview/double-key-encryption-setup) · Documentación · Oficial · Microsoft Learn. Guía de despliegue del servicio DKE (prerrequisitos .NET 8, clonar el repositorio de GitHub, generar claves, publicar en Azure, registrar el almacén y crear etiquetas DKE) y migración desde HYOK.
- [Overview of Service encryption with Microsoft Purview Customer Key](https://learn.microsoft.com/en-us/purview/customer-key-overview) · Documentación · Oficial · Microsoft Learn. Explica Customer Key como capa adicional de cifrado en reposo con claves raíz del cliente en Azure Key Vault y los tres tipos de políticas de cifrado (multi-workload, buzones de Exchange y SharePoint/OneDrive).
- [Manage Customer Key encryption policies](https://learn.microsoft.com/en-us/purview/customer-key-manage) · Documentación · Oficial · Microsoft Learn. Referencia operativa con los cmdlets para crear, asignar, verificar, deshabilitar y revertir políticas de cifrado de Customer Key y gestionar permisos de Key Vault.

### Laboratorios, GitHub y herramientas

- [Azure-Samples/DoubleKeyEncryptionService](https://github.com/Azure-Samples/DoubleKeyEncryptionService) · GitHub · Oficial · GitHub - Azure-Samples. Código fuente de referencia del servicio de claves de Double Key Encryption que Microsoft publica para desplegarlo on-premises o en Azure.

**Manos a la obra**

1. `Laboratorio parcial` Despliega el servicio DKE de ejemplo en Azure App Service siguiendo la [guía de configuración](https://learn.microsoft.com/en-us/purview/double-key-encryption-setup) y el [repositorio](https://github.com/Azure-Samples/DoubleKeyEncryptionService): genera las claves, registra el almacén y crea la etiqueta PRUEBA-DKE. Limitación: solo Microsoft 365 Apps for enterprise en Windows y sin coautoría; consume créditos y exige custodiar la clave.
2. `Laboratorio parcial` Con la etiqueta DKE, cifra un documento en Word para Windows, súbelo a OneDrive e intenta abrirlo en Office web, buscarlo y encontrarlo con eDiscovery; compara cada resultado con un documento de cifrado estándar ([DKE](https://learn.microsoft.com/en-us/purview/double-key-encryption)). Limitación: la misma del paso anterior.
3. `Laboratorio parcial` Etiqueta con DKE un archivo que no es de Office desde el Explorador de archivos o con PowerShell del cliente y ábrelo con el visor ([cliente para Windows](https://learn.microsoft.com/en-us/purview/information-protection-client)). Limitación: depende del servicio DKE de ejemplo del primer paso y de su clave.
4. `Laboratorio` Redacta un registro de decisión de una página: qué datos (cerca del 5 % como máximo) justifican DKE, cuáles bastan con Customer Key o con el cifrado de etiquetas, qué funciones se pierden en cada caso y qué requisito normativo, validado por Legal, lo exige (módulo O3).
5. `Solo producción` Customer Key requiere el conteo real de licencias y bóvedas de claves en dos suscripciones de Azure. Forma segura: política de cifrado de buzón solo para buzones de prueba, runbook de la clave de disponibilidad y de revocación revisado por el comité de cambios, y nunca revocar claves fuera de un procedimiento de salida aprobado ([administrar las políticas](https://learn.microsoft.com/en-us/purview/customer-key-manage), [Customer Key](https://learn.microsoft.com/en-us/purview/customer-key-overview)).
6. `Solo producción` Piloto de DKE en producción: un grupo mínimo, contenido sintético y equipos con Microsoft 365 Apps for enterprise. Forma segura: respaldo de la clave en dos ubicaciones, prueba de recuperación documentada y una salida definida para descifrar o reetiquetar si se abandona DKE.

<a id="a4"></a>

## A4 · Monitoreo e integración con el SOC

*L400 · ~5 h · Origen: Ruta Ninja de Learn · módulo 3 «Efficiently investigate data risks with Security Copilot in Microsoft Purview» (contexto), ampliado en esta edición*

Las etiquetas generan señales que el SOC necesita: bajadas o eliminación de etiquetas con su justificación, protección quitada, archivos etiquetados que salen de la organización, resultados del auto-etiquetado y hallazgos del escáner. En Purview, el **explorador de actividades** —basado en el registro de auditoría unificado, con cerca de 50 filtros, conjuntos de filtros y hasta 30 días de datos— y los **informes de postura** de Information Protection (vista previa) son el primer lugar para investigar.

Para llevarlas al SOC, el **conector de Microsoft Purview Information Protection** para Sentinel (vista previa) envía los eventos de etiquetado, protección y escáner a la tabla `MicrosoftPurviewInformationProtection` y reemplaza al antiguo conector de AIP. Necesita una licencia con Audit (E3, A3, Business Basic o superior) y la auditoría habilitada, y documenta tipos de registro como `SensitivityLabelAction` y operaciones como `FileSensitivityLabelChanged`, base para reglas de detección y búsquedas.

Security Copilot suma resúmenes y agentes de triage para DLP e Insider Risk dentro de Purview, con consumo de SCU; se profundizan en los programas de Security Copilot y de DLP. Aquí te enfocas en que el SOC entienda la sensibilidad y la use para priorizar.

**Por qué importa**

Bajar la etiqueta de un archivo justo antes de compartirlo fuera es una de las señales tempranas más claras de exfiltración, pero solo si alguien la mira. Enviar los eventos de etiquetas al SOC, con reglas ajustadas y un runbook de triage, convierte Information Protection de un control de cumplimiento en una fuente de detección, y le da al SOC el contexto de sensibilidad para priorizar incidentes de DLP y de riesgo interno.

**Qué vas a lograr**

- Usar el explorador de actividades y los informes de postura para investigar cambios de etiquetas.
- Conectar Information Protection a Microsoft Sentinel y consultar la tabla MicrosoftPurviewInformationProtection.
- Escribir consultas KQL que detecten bajadas o eliminación de etiquetas con justificación.
- Definir con el equipo de DLP un runbook de triage para alertas relacionadas con etiquetas.

> **Atención.** El conector de Microsoft Purview Information Protection para Sentinel sigue en vista previa, reemplaza al conector de AIP (cuya analítica se retiró el 31 de marzo de 2023) y requiere una licencia con Audit (E3, A3, Business Basic o superior) y la auditoría habilitada. Su página aún describe el portal de Azure, aunque Sentinel se opera hoy desde el portal de Defender ([conector](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview)).

> **Consejo Ninja.** Para detecciones, usa los tipos de registro y operaciones del conector —por ejemplo, SensitivityLabelAction, MipAutoLabelSharePointItem y FileSensitivityLabelChanged o FileSensitivityLabelRemoved— ([referencia](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-purview-record-types-activities)) y las columnas LabelName, OldSensitivityLabelId, JustificationText y Operation de la tabla, que admite los planes Basic y Auxiliary ([esquema](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/microsoftpurviewinformationprotection)).

> **Novedad.** El explorador de actividades ofrece cerca de 50 filtros, conjuntos de filtros y hasta 30 días de datos, con Security Copilot integrado en vista previa para generar filtros en lenguaje natural ([explorador de actividades](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)). Los agentes de Security Copilot en Purview (triage de DLP e Insider Risk y postura de DSPM) consumen SCU y se profundizan en el programa de Security Copilot ([agentes](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview)).

**¿Tienes poco tiempo?**

- [Stream data from Microsoft Purview Information Protection to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Documentación
- [Microsoft Purview Information Protection connector reference - audit log record types and activities support in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-purview-record-types-activities) · Documentación
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Documentación

### Documentación, cursos y credenciales

- [Microsoft Purview Information Protection connector reference - audit log record types and activities support in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-purview-record-types-activities) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Lista los tipos de registro (AipDiscover, MipLabel, SensitivityLabelAction, MipAutoLabelSharePointItem, etc.) y operaciones (FileSensitivityLabelApplied/Changed/Removed) que el conector envía a Sentinel.
- [Get started with activity explorer](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer) · Documentación · Oficial · Microsoft Learn. Explorador de actividades sobre contenido etiquetado y sensible basado en el registro de auditoría unificado, con ~50 filtros, conjuntos de filtros y hasta 30 días de datos.
- [Stream data from Microsoft Purview Information Protection to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo habilitar el conector de Microsoft Purview Information Protection en Sentinel para enviar eventos de etiquetado, protección y escáner a la tabla MicrosoftPurviewInformationProtection. *Nota:* El conector sigue en preview; reemplaza al conector de AIP (analytics de AIP retirado el 31-mar-2023); requiere licencia con Audit (E3/A3/Business Basic o superior) y auditoría habilitada…
- [Azure Monitor Logs reference - MicrosoftPurviewInformationProtection](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/microsoftpurviewinformationprotection) · Documentación · Oficial · Microsoft Learn - Azure Monitor. Esquema de columnas de la tabla MicrosoftPurviewInformationProtection (LabelName, OldSensitivityLabelId, JustificationText, Operation, etc.) con soporte de nivel Basic/Auxiliary.
- [Security Copilot agents in Microsoft Purview overview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents-overview) · Documentación · Oficial · Microsoft Learn. Resume los agentes de Security Copilot en Purview: triage de alertas de DLP e IRM y agentes de postura de DSPM y Data Security Investigations (preview), que consumen SCU.
- [Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview) · Documentación · Oficial · Microsoft Learn. Describe las experiencias integradas y standalone de Security Copilot en Purview (resúmenes de alertas DLP/IRM, insights de políticas, DSPM, activity explorer) y cómo habilitar el plugin.
- [Get started with the Microsoft Purview Triage Agent in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-dlp-agent-get-started) · Documentación · Oficial · Microsoft Learn. Despliegue del agente de triage de DLP en los portales de Purview y Defender XDR, con roles requeridos, consumo de SCU y uso de identidad de agente.

**Manos a la obra**

1. `Laboratorio` En el explorador de actividades, crea y guarda un conjunto de filtros para etiquetas cambiadas o eliminadas con justificación; genera tres cambios con cuentas de prueba y verifícalos al día siguiente ([explorador de actividades](https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer)).
2. `Laboratorio` Habilita el conector de Purview Information Protection en un workspace de Sentinel de laboratorio (el del programa de Sentinel) y confirma la llegada de eventos a la tabla MicrosoftPurviewInformationProtection ([conector](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-purview)).
3. `Laboratorio` Escribe una consulta KQL que liste las bajadas de etiqueta por persona en 24 horas con la etiqueta anterior (OldSensitivityLabelId), la nueva (LabelName) y JustificationText, y conviértela en una regla programada o una detección personalizada con umbral ([esquema](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/microsoftpurviewinformationprotection), [tipos de registro](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-purview-record-types-activities)).
4. `Laboratorio` Revisa los informes de postura de Information Protection y guarda en PDF la distribución de etiquetas y la cobertura de auto-etiquetado del mes ([informes](https://learn.microsoft.com/en-us/purview/purview-reports)).
5. `Laboratorio parcial` Si tu tenant tiene capacidad de Security Copilot, genera un filtro del explorador de actividades en lenguaje natural y compáralo con el tuyo ([Security Copilot en Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview)). Limitación: las SCU incluidas con E5 se calculan sobre licencias pagas, así que una prueba de 25 licencias no da capacidad útil.
6. `Solo producción` Regla de bajadas de etiqueta en producción: ejecútala dos semanas como consulta, sin generar incidentes, para medir el volumen real. Forma segura: acuerda con DLP, Legal y Privacidad el umbral y el tratamiento de los datos de las personas, y documenta el runbook de triage antes de activar los incidentes.

<a id="reto-avanzado"></a>

## Reto del nivel

**Copilot listo para el comité.** Presenta la matriz de tus etiquetas con niveles de permisos, VIEW, EXTRACT y comportamiento esperado de Copilot y de los agentes; demuestra (o documenta, si no tienes licencias) la herencia de etiquetas y una DLP para Copilot en simulación; incluye el registro de decisión sobre DKE y Customer Key, la consulta KQL de bajadas de etiqueta funcionando en Sentinel y el script que exporta cada día el explorador de actividades. Formato: diez minutos de exposición y un repositorio con el código y la documentación.

<a id="quiz-avanzado"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-avanzado). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. ¿Qué derechos de uso debe tener una persona para que Copilot use contenido cifrado en su nombre?
   - a) VIEW y EXTRACT
   - b) EDIT y PRINT
   - c) Solo OWNER
   - d) FORWARD y EXPORT

2. Copilot crea un documento a partir de un archivo General y otro Confidencial. Cuando se admite la herencia, ¿qué etiqueta recibe el nuevo contenido?
   - a) La de menor prioridad de las fuentes, General
   - b) Ninguna: el contenido nuevo siempre nace sin etiqueta
   - c) La de mayor prioridad de las fuentes, Confidencial
   - d) Siempre Altamente confidencial, sin importar las fuentes

3. Según la arquitectura de protección de datos de Copilot, ¿qué archivos no pueden leer los agentes?
   - a) Los archivos sin ninguna etiqueta de confidencialidad
   - b) Los archivos con permisos definidos por el usuario
   - c) Los correos internos enviados dentro del tenant
   - d) Los PDF exportados desde Office con etiqueta

4. ¿Cómo se configura BlockContentAnalysisServices y qué efecto colateral tiene?
   - a) En el portal de Purview, como una opción más de la etiqueta y sin efectos colaterales
   - b) En Entra ID, como una directiva de Acceso condicional que bloquea a Copilot
   - c) En el centro de administración de Teams; además desactiva la grabación de reuniones
   - d) Solo por PowerShell; también desactiva la comprobación DLP del cliente en Outlook clásico

5. ¿Qué licencias habilitan la DLP que impide a Copilot procesar archivos y correos etiquetados?
   - a) Microsoft 365 E3
   - b) Microsoft 365 Business Premium sin complementos
   - c) Microsoft 365 E5 o A5, Purview Suite, E5 IP&G u Office 365 E5
   - d) Ninguna: está incluida para todos los usuarios de Copilot Chat

6. ¿Qué describe mejor a assignSensitivityLabel de Microsoft Graph?
   - a) Una API protegida y medida, asíncrona, que pide justificación para bajar o quitar una etiqueta
   - b) Una API gratuita y síncrona que también aplica las marcas de contenido
   - c) Una API disponible solo en nubes gubernamentales y soberanas
   - d) Un cmdlet del cliente de Information Protection para archivos locales

7. ¿Qué buena práctica aplica a Export-ContentExplorerData?
   - a) Un único script para todas las etiquetas, sin reconectar la sesión
   - b) Un script por etiqueta o SIT, reconectando la sesión porque el token expira en cerca de una hora
   - c) Ejecutarlo solo desde el portal de Purview, porque no admite certificados
   - d) Usarlo solo con archivos cifrados con DKE en OneDrive

8. ¿Desde qué versión admite DKE el MIP SDK?
   - a) Desde la 1.0
   - b) Desde la 1.18
   - c) No admite DKE
   - d) Desde la 1.7

9. ¿Qué NO funciona con contenido cifrado con DKE?
   - a) Etiquetar desde el Explorador de archivos
   - b) La coautoría y AutoSave
   - c) Guardar el archivo en SharePoint
   - d) Abrir un PDF con DKE en el visor del cliente

10. ¿Qué exige Customer Key en cuanto a licencias?
   - a) Una licencia por cada administrador que gestiona las claves en Azure Key Vault
   - b) Licencias solo para los usuarios de SharePoint, porque Exchange y Teams se cuentan aparte
   - c) Al menos tantas licencias como usuarios con Exchange o Teams; si faltan, vuelve al cifrado de servicio predeterminado
   - d) Pago por uso por cada clave raíz y por cada política de cifrado creada

11. ¿Qué cubre la política de cifrado multicarga de Customer Key?
   - a) Teams, interacciones de Microsoft 365 Copilot, Exchange, datos de EDM y configuraciones de etiquetas
   - b) Solo los archivos de SharePoint y OneDrive, incluidas sus versiones anteriores
   - c) Solo los buzones de Exchange, con un máximo de 50 políticas activas
   - d) Los endpoints con Windows y los recursos compartidos que rastrea el escáner

12. ¿Para qué proporción de los datos sugiere Microsoft usar DKE?
   - a) Para todos los datos de la organización, por defecto
   - b) Para cerca de la mitad de los datos, los etiquetados como Confidencial
   - c) Para ningún dato en producción: solo para pruebas
   - d) Para cerca del 5 % de los datos más sensibles

13. ¿En qué tabla deja los eventos el conector de Purview Information Protection para Sentinel?
   - a) SecurityEvent
   - b) MicrosoftPurviewInformationProtection
   - c) AzureActivity
   - d) InformationProtectionLogs_CL

14. ¿Qué latencia típica tiene el explorador de actividades?
   - a) Tiempo real, en menos de un minuto
   - b) Hasta siete días
   - c) Entre 60 y 90 minutos
   - d) Treinta días, igual que su retención

15. ¿Qué requisito de licencia y configuración tiene el conector de Purview Information Protection para Sentinel?
   - a) Microsoft 365 E5 o Purview Suite para todas las personas auditadas, sin auditoría
   - b) Teams Premium y la auditoría habilitada en el tenant de Sentinel
   - c) Una licencia de Security Copilot con SCU aprovisionadas en la región del workspace
   - d) Una licencia con Audit (E3, A3, Business Basic o superior) y la auditoría habilitada

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza a los Ninja Training oficiales, a la documentación de Microsoft Learn ni a las certificaciones oficiales. No es asesoría legal: las decisiones sobre datos personales deben validarse con Legal y Privacidad. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

# Nivel 2 · Intermedio · Arquitectura, datos, detección y operación

*Microsoft Sentinel Ninja Training · Edición 2026*

[← Nivel 1 · Inicial](01_Nivel_1_Inicial.md) · [Índice del programa](README.md) · [Nivel 3 · Avanzado →](03_Nivel_3_Avanzado.md)

<a id="intermedio"></a>

Las decisiones de arquitectura y datos que definen costo y cobertura, y el trabajo diario de detección, investigación, búsqueda y automatización esencial. Reconstruye las partes 2 a 4 del Ninja original.

*L300 · 13 módulos · ~76 horas · 258 recursos*

**Módulos de este nivel:** [M1 Workspaces y tenants](#m1) · [M2 Recolección de datos](#m2) · [M3 Logs, niveles y costos](#m3) · [M4 Enriquecimiento](#m4) · [M5 Transformación de logs](#m5) · [M6 Migración](#m6) · [M7 Analítica y detecciones](#m7) · [M8 Workbooks y reportes](#m8) · [M9 Incidentes](#m9) · [M10 Hunting](#m10) · [M11 UEBA](#m11) · [M12 Salud y optimización](#m12) · [M13 Automatización esencial](#m13)

<a id="m1"></a>

## M1 · Arquitectura de workspaces y tenants

*L300 · ~6 h · Origen: Módulo 3 · Workspace and tenant architecture*

La primera decisión de arquitectura es cuántos workspaces usar y dónde. Un único workspace simplifica la operación, la correlación y el costo, pero la residencia de datos, la separación entre tenants, los requisitos regulatorios, la propiedad de los datos o la estructura de un proveedor de servicios llevan a diseños con varios workspaces que deben funcionar como un solo sistema.

En el portal de Defender esto se traduce en un **workspace principal** y workspaces secundarios, en la **gestión multi-inquilino** y en un modelo de permisos que combina Azure RBAC —incluido el acceso por recurso y por tabla— con el **RBAC unificado de Defender**. Este módulo recorre el árbol de decisión oficial, los diseños de referencia y las herramientas para operar varios workspaces y tenants a escala.

**Qué vas a lograr**

- Aplicar el árbol de decisión oficial para diseñar la topología de workspaces.
- Explicar el comportamiento de workspaces principal y secundarios en el portal de Defender.
- Diseñar el control de acceso combinando Azure RBAC, RBAC por recurso y por tabla, y RBAC unificado.
- Elegir entre Azure Lighthouse y la gestión multi-inquilino de Defender según el escenario.

> **Novedad.** En el portal de Defender cada tenant tiene **un workspace principal y workspaces secundarios ilimitados**. Solo el principal se correlaciona con Defender XDR; las detecciones personalizadas y las consultas por API se limitan a él, y los libros muestran solo sus datos ([workspaces en el portal de Defender](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal)).

> **Atención.** Dato clave para MCSA: según la documentación de residencia, los workspaces fuera de Europa e Israel procesan datos de cliente en una región de EE. UU.; en Sudamérica solo figuran Brazil South y Brazil Southeast para el SIEM y no hay región de data lake listada, y el lake debe estar en la misma región que el workspace principal. Valídalo con el cliente antes de diseñar ([residencia de datos](https://learn.microsoft.com/en-us/azure/sentinel/geographical-availability-data-residency)).

> **Novedad.** GDAP para Sentinel, incluso para organizaciones que no son CSP, entró en vista previa pública el 16 de abril de 2026, y en septiembre de 2026 se agregaron roles personalizados de RBAC unificado asignables a grupos GDAP ([GDAP para Sentinel](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/how-granular-delegated-admin-privileges-gdap-allows-sentinel-customers-to-delega/4503123)). Algunas páginas de activación todavía dicen lo contrario: confirma el estado vigente antes de recomendarlo.

> **Novedad.** El RBAC a nivel de fila (Sentinel scoping), en vista previa desde abril de 2026, existe solo en el portal de Defender, requiere Sentinel activado en el RBAC unificado, admite hasta 100 scopes por tenant y etiqueta filas en la ingesta ([scoping](https://learn.microsoft.com/en-us/defender-xdr/scoping)).

> **Atención.** Al activar el RBAC unificado para un workspace, los permisos pasan a gestionarse en Defender; Playbook Operator, Automation Contributor y Workbook Contributor siguen en Azure RBAC y no se admiten entidades de servicio ([activar URBAC](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac)).

> **Consejo Ninja.** Empieza con **un único workspace** y crea más solo ante requisitos concretos: tenants, soberanía, facturación, retención o acceso. Separa la telemetría operativa (Perf, InsightsMetrics, ContainerLog) para que no se facture con precios de Sentinel ([diseño de workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design)).

**¿Tienes poco tiempo?**

- [Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Documentación
- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar
- [What's new in Microsoft Sentinel: September 2026](https://techcommunity.microsoft.com/blog/MicrosoftSentinelBlog/what%E2%80%99s-new-in-microsoft-sentinel-september-2026/4560902) · Blog oficial

### Documentación, cursos y credenciales

- [Microsoft Defender multitenant management](https://learn.microsoft.com/en-us/defender-xdr/mto-overview) · Documentación · Oficial · Nuevo · Microsoft Learn · 10 sep 2026. Vista unificada multi-tenant del portal de Defender para incidentes, alertas, casos, hunting avanzado y reglas de detección personalizadas, incluyendo workspaces de Sentinel incorporados.
- [Multiple Microsoft Sentinel workspaces in the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/workspaces-defender-portal) · Documentación · Oficial · Nuevo · Microsoft Learn · 8 jun 2026. Describe el modelo de un workspace primario (correlacionado con Defender XDR) y secundarios ilimitados por tenant, permisos, cambio de primario, alcance de datos por vista y sincronización bidireccional.
- [Microsoft Defender unified role-based access control (RBAC)](https://learn.microsoft.com/en-us/defender-xdr/manage-rbac) · Documentación · Oficial · Microsoft Learn. Explica el modelo URBAC del portal de Defender, que ya admite Sentinel para workspaces incorporados: las asignaciones se sincronizan con Azure RBAC y URBAC pasa a ser la fuente de permisos al activarse.
- [Transition your Microsoft Sentinel environment to the Defender portal](https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender) · Documentación · Oficial · Microsoft Learn. Guía oficial paso a paso para pasar de Sentinel en el portal de Azure al portal de Defender: planificación, permisos, diferencias de almacenamiento/privacidad, configuración y operación.
- [Design a Log Analytics workspace architecture](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Guía de criterios (tenants, regiones, propiedad de datos, facturación, retención, niveles de compromiso, control de acceso, resiliencia) para decidir entre uno o varios workspaces, partiendo siempre de un único workspace.
- [Prepare for multiple workspaces and tenants in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/prepare-multiple-workspaces) · Documentación · Oficial · Microsoft Learn. Explica cuándo se justifica una arquitectura de varios workspaces/tenants (soberanía, propiedad de datos, varios tenants de Entra, control de acceso, facturación, MSSP) y qué alternativas reducen su número.
- [Activate Microsoft Defender unified role-based access control (URBAC)](https://learn.microsoft.com/en-us/defender-xdr/activate-defender-rbac) · Documentación · Oficial · Microsoft Learn. Pasos para activar URBAC por carga de trabajo, incluida la activación selectiva de workspaces de Sentinel, con roles no soportados y riesgos de errores de sincronización.
- [Manage Microsoft Sentinel workspaces at scale (Azure Lighthouse)](https://learn.microsoft.com/en-us/azure/lighthouse/how-to/manage-sentinel-workspaces) · Documentación · Oficial · Microsoft Learn (Azure Lighthouse). Modelo MSSP con Azure Lighthouse: workspaces en cada tenant cliente gestionados desde el tenant del proveedor, roles delegados, consultas y workbooks entre tenants y protección de propiedad intelectual.
- [Geographical availability and data residency in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/geographical-availability-data-residency) · Documentación · Oficial · Microsoft Learn. Detalla dónde se almacenan y procesan los datos crudos, procesados y de configuración de Sentinel, las regiones soportadas para SIEM y data lake y la retención tras la baja.
- [Configure Microsoft Sentinel scoping (row-level RBAC)](https://learn.microsoft.com/en-us/defender-xdr/scoping) · Documentación · Oficial · Vista previa · Microsoft Learn. Configura scopes de Sentinel en URBAC para dar acceso a subconjuntos de filas etiquetadas en ingesta (por unidad de negocio, región o sensibilidad) sin separar workspaces. *Nota:* Solo en el portal de Defender; requiere Sentinel activado en URBAC; hasta 100 scopes por tenant; aplica a tablas que soportan transformaciones en ingesta (usa DCR). Anunciado en RSAC 2026 (preview 1-abr-2026)
- [Set up Microsoft Defender multitenant management](https://learn.microsoft.com/en-au/unified-secops/mto-requirements) · Documentación · Oficial · Microsoft Learn. Requisitos y pasos para configurar la gestión multi-tenant (B2B o GDAP, permisos por tenant, Lighthouse para consultas cruzadas de Sentinel, límite de tenants).
- [Centrally manage multiple Microsoft Sentinel workspaces with workspace manager (Preview)](https://learn.microsoft.com/en-us/azure/sentinel/workspace-manager) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 30 jul 2026. Publica contenido (reglas, automatizaciones, parsers, hunting, workbooks) desde un workspace central a workspaces miembro con topologías direct-link, co-gestión y N-tier. *Nota:* Aplica solo a Sentinel en el portal de Azure; en el portal de Defender usar gestión multi-tenant y distribución de contenido. Con fin de soporte del portal de Azure (31-mar-2027) tiene vida limitada

### Anuncios y blogs oficiales

- [What's new in Microsoft Sentinel: September 2026](https://techcommunity.microsoft.com/blog/MicrosoftSentinelBlog/what%E2%80%99s-new-in-microsoft-sentinel-september-2026/4560902) · Blog oficial · Empleado de Microsoft · Nuevo · vkokkengada · Microsoft Tech Community - Microsoft Sentinel Blog · 30 sep 2026. Resumen mensual oficial: Case Management en Defender (preview pública desde el 23-sep-2026), roles personalizados URBAC para GDAP, conectores CCF multi-cuenta y más de 500 conectores de datos.
- [New content types supported in multi-tenant content distribution](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/new-content-types-supported-in-multi-tenant-content-distribution/4457948) · Blog oficial · Empleado de Microsoft · tomasbeerthuis · Microsoft Tech Community - Microsoft Sentinel Blog · 29 ene 2026. La distribución de contenido multi-tenant del portal de Defender ahora replica reglas de análisis, reglas de automatización y workbooks de Sentinel, además de reglas de ajuste de alertas, hacia tenants y workspaces destino.
- [How Granular Delegated Admin Privileges (GDAP) allows Sentinel customers to delegate access](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/how-granular-delegated-admin-privileges-gdap-allows-sentinel-customers-to-delega/4503123) · Blog oficial · Empleado de Microsoft · Vista previa · Yossi Basha · Microsoft Tech Community - Microsoft Sentinel Blog · 20 mar 2026. Explica la extensión de GDAP a clientes no-CSP para delegar acceso a Sentinel y Defender desde el portal de Defender mediante un handshake de tres pasos entre tenant gobernante y gobernado. *Nota:* Vista previa pública desde el 16-abr-2026 (actualizado esa fecha). Alternativa/complemento a Azure Lighthouse para MSSP y organizaciones multi-tenant
- [Enable continuous deployment natively with Microsoft Sentinel repositories](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/enable-continuous-deployment-natively-with-microsoft-sentinel/ba-p/2929413) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 3 ('Arquitectura de workspaces y tenants') del skill-up de Learn: blog-oficial «Enable continuous deployment natively with Microsoft Sentinel repositories».

### Webinars, videos y podcasts

- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar · Oficial · Jeremy Tan, Maria de Sousa-Valadas Castano · YouTube – Microsoft Security Community · 16 dic 2025. Segunda parte de la transición a Defender: onboarding, modelos de permisos, conectores, data lake, SOC optimization, custom detections unificadas y multi-workspace/multi-tenant.
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar · Oficial · Neelam Nursee, Naomi Christis · YouTube – Microsoft Security Community · 9 dic 2025. Recorrido de un día en el SOC dentro del portal de Defender: navegación, cola unificada de incidentes, UEBA, TI, watchlists, automatización y case management.
- [Extend Microsoft Sentinel across workspaces and tenants (webinar)](https://youtu.be/hwahlwgJPnE) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube. Material enlazado en el Módulo 3 ('Arquitectura de workspaces y tenants') del skill-up de Learn: webinar «Extend Microsoft Sentinel across workspaces and tenants (webinar)» ofrecido en YouTube, MP4, presentation.

**Manos a la obra**

1. `Laboratorio` Aplica el [árbol de decisión de workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design) a un caso: un banco con operación en tres países y dos tenants de Entra. Documenta cada decisión y su justificación.
2. `Laboratorio` En el laboratorio, conecta un workspace secundario y verifica qué funciones quedan limitadas al principal.
3. `Laboratorio` Activa el RBAC unificado para Sentinel en un workspace de prueba y crea un rol personalizado para analistas.
4. `Laboratorio parcial` Opcional: crea un Sentinel scope para un SOC regional y valida que sus analistas solo vean sus filas.

**¿Quieres profundizar?**

- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar

<a id="m2"></a>

## M2 · Recolección de datos

*L300 · ~8 h · Origen: Módulo 4 · Data collection*

Un SIEM vale lo que valen sus datos: eventos, alertas e información de contexto como inteligencia de amenazas, vulnerabilidades e inventario. Sentinel ofrece cientos de conectores, pero casi todos se reducen a unos pocos **métodos de ingesta**: integraciones de servicio a servicio para Microsoft y Azure; **Azure Monitor Agent** con reglas de recolección de datos (DCR) para Windows, Linux, Syslog y CEF; la **API de ingesta de logs** para fuentes personalizadas; el **Codeless Connector Framework** para APIs de terceros; y conectores para otras nubes como AWS y Google Cloud.

Si entiendes el método, entiendes el conector. Aquí aprenderás a elegir el método adecuado para cada fuente, a desplegarlo con buenas prácticas, a evitar caminos que ya fueron retirados —como el antiguo agente de Log Analytics— y a monitorear que los datos sigan llegando.

**Qué vas a lograr**

- Clasificar cualquier conector según su método de ingesta.
- Desplegar Azure Monitor Agent y reglas de recolección de datos para Windows, Syslog y CEF.
- Ingerir datos personalizados con la API de ingesta de logs.
- Identificar conectores en retiro y su ruta de migración.

> **Qué cambió.** El agente de Log Analytics (MMA/OMS) se retiró el 31 de agosto de 2024; ejecutar MMA y AMA a la vez duplica eventos y costos ([migración a AMA](https://learn.microsoft.com/en-us/azure/sentinel/ama-migrate)).

> **Atención.** La HTTP Data Collector API exige TLS 1.2 desde el 1 de marzo de 2026 y su soporte terminó el 14 de septiembre de 2026; migra a la API de ingesta de logs o a CCF. Las tablas «Custom table (classic)» delatan uso heredado ([migrar logs personalizados](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate)).

> **Novedad.** Microsoft está migrando los conectores basados en Azure Functions al Codeless Connector Framework; en septiembre de 2026 el catálogo superó los 500 conectores y CCF sumó soporte multicuenta en vista previa ([conectores CCF](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/exciting-announcements-new-data-connectors-released-using-the-codeless-connector/4421104)).

> **Atención.** Windows Event Forwarding escribe en la tabla `WindowsEvent`, no en `SecurityEvent`: muchas reglas integradas requieren adaptación o ASIM ([conectores de Windows](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-windows-based)).

> **Consejo Ninja.** Syslog y CEF vía AMA: la DCR define los filtros, el agente recibe del daemon local por TCP 28330, se admiten RFC 3164 y 5424, y los reenviadores fuera de Azure requieren Azure Arc ([Syslog y CEF con AMA](https://learn.microsoft.com/en-us/azure/sentinel/cef-syslog-ama-overview)).

**¿Tienes poco tiempo?**

- [Microsoft Sentinel data connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources) · Documentación
- [Syslog and Common Event Format (CEF) via AMA connectors for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/cef-syslog-ama-overview) · Documentación
- [Migrate from the HTTP Data Collector API to the Logs ingestion API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate) · Documentación

### Documentación, cursos y credenciales

- [Stream data from Microsoft Defender XDR to Microsoft Sentinel in the Azure portal](https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Configura el conector Defender XDR (incidentes y alertas, entidades de AD vía MDI y eventos de hunting avanzado) y cómo verificar la ingesta con SecurityIncident.
- [AMA migration for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/ama-migrate) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Proceso recomendado para migrar del agente Log Analytics (MMA/OMS) a AMA en Sentinel: prueba de concepto, workbook de seguimiento de migración, evitar doble ingesta y desinstalar el agente legado.
- [Microsoft Defender XDR integration with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Documentación · Oficial · Microsoft Learn. Explica cómo SIEM (Sentinel) y XDR (Defender) se integran: cola de incidentes única, sincronización bidireccional, correlación y recolección de eventos de hunting avanzado.
- [Discover and manage Microsoft Sentinel out-of-the-box content (Content hub)](https://learn.microsoft.com/en-us/azure/sentinel/sentinel-solutions-deploy) · Documentación · Oficial · Microsoft Learn. Cómo buscar, instalar, actualizar en lote y habilitar el contenido de soluciones del Content hub desde el portal de Defender (Microsoft Sentinel > Content management > Content hub).
- [Ingest syslog and CEF messages to Microsoft Sentinel with the Azure Monitor Agent](https://learn.microsoft.com/en-us/azure/sentinel/connect-cef-syslog-ama) · Documentación · Oficial · Microsoft Learn. Procedimiento para instalar la solución del Content hub, crear la DCR, desplegar AMA en un reenviador Linux (Azure o Arc), ejecutar el script de instalación y probar la ingesta de Syslog/CEF.
- [Syslog and Common Event Format (CEF) via AMA connectors for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/cef-syslog-ama-overview) · Documentación · Oficial · Microsoft Learn. Explica la arquitectura de recolección Syslog/CEF con AMA (máquina única o reenviador), el papel de las DCR como filtros y cómo evitar duplicados entre tablas Syslog y CommonSecurityLog.
- [Migrate from the HTTP Data Collector API to the Logs ingestion API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Guía para migrar integraciones y tablas 'Custom table (classic)' del HTTP Data Collector API a la Logs ingestion API con DCE/DCR, transformaciones y RBAC por DCR, incluyendo el impacto en conectores de Sentinel que pasan a CCF.
- [Create a pull codeless connector for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/isv/create-codeless-connector) · Documentación · Oficial · Microsoft Learn. Introducción práctica al Codeless Connector Framework (CCF) para conectores pull: tabla de salida, DCR, interfaz y reglas de conexión empaquetadas en una plantilla ARM.
- [Connect Microsoft Sentinel to other Microsoft services with a Windows agent-based data connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-windows-based) · Documentación · Oficial · Microsoft Learn. Cómo crear DCR (GUI o API) para conectores Windows basados en AMA, incluidos Windows Security Events via AMA y Windows Forwarded Events, con filtros XPath en origen.
- [Connect Microsoft Sentinel to Amazon Web Services to ingest AWS service log data](https://learn.microsoft.com/en-us/azure/sentinel/connect-aws) · Documentación · Oficial · Microsoft Learn. Configura el conector AWS S3 (VPC Flow Logs, GuardDuty, CloudTrail, CloudWatch) con script automático que crea proveedor OIDC, rol IAM, bucket S3 y cola SQS.
- [Connect data sources to Microsoft Sentinel by using data connectors](https://learn.microsoft.com/en-us/azure/sentinel/configure-data-connector) · Documentación · Oficial · Microsoft Learn. Procedimiento genérico para habilitar un conector desde el Content hub, configurar retención/tiering por tabla (analytics + espejo o solo lake), habilitar UEBA y verificar los datos.
- [Windows security event sets that can be sent to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/windows-security-event-id-reference) · Documentación · Oficial · Nuevo · Microsoft Learn · 7 ago 2026. Referencia de los conjuntos All, Common, Minimal y Custom (XPath) de eventos de seguridad de Windows, con la lista de Event IDs de cada uno.
- [Connect to Azure, Windows, Microsoft, and Amazon services](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-windows-microsoft-services) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Connect to Azure, Windows, Microsoft, and Amazon services».
- [Connect your data source to the Microsoft Sentinel Data Collector API to ingest data](https://learn.microsoft.com/en-us/azure/sentinel/connect-rest-api-template) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Connect your data source to the Microsoft Sentinel Data Collector API to ingest data».
- [Use Azure Functions to connect Microsoft Sentinel to your data source](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-functions-template) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Use Azure Functions to connect Microsoft Sentinel to your data source».
- [Find your Microsoft Sentinel data connector](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Find your Microsoft Sentinel data connector».
- [Create a custom connector](https://learn.microsoft.com/en-us/azure/sentinel/create-custom-connector) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 4 ('Recolección de datos') del skill-up de Learn: doc «Create a custom connector».
- [Set up your Amazon Web Services (AWS) environment to collect AWS logs to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-aws-configure-environment) · Documentación · Oficial · Microsoft Learn. Detalla la preparación del lado AWS (S3 + SQS, proveedor OIDC, rol asumido con prefijo OIDC_, políticas IAM) y enlaza a los conectores AWS WAF, servicios AWS y EKS.
- [Microsoft Sentinel health tables reference](https://learn.microsoft.com/en-us/azure/sentinel/health-table-reference) · Documentación · Oficial · Microsoft Learn. Esquema de la tabla SentinelHealth y operaciones registradas para conectores, reglas de análisis, reglas de automatización y playbooks.
- [Stream logs to Microsoft Sentinel with Logstash and DCR-based API](https://learn.microsoft.com/en-us/azure/sentinel/connect-logstash-data-connection-rules) · Documentación · Oficial · Vista previa · Microsoft Learn. Configura el plugin oficial de salida de Logstash que envía datos vía Logs Ingestion API a tablas personalizadas o estándar con transformaciones DCR. *Nota:* Plugin microsoft-sentinel-log-analytics-logstash-output-plugin v2.5.0 en public preview; el plugin antiguo usaba el Data Collector API (deprecado). Soporta Logstash 7.x a 9.4

### Anuncios y blogs oficiales

- [Exciting Announcements: New Data Connectors Released Using the Codeless Connector Framework](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/exciting-announcements-new-data-connectors-released-using-the-codeless-connector/4421104) · Blog oficial · Empleado de Microsoft · PrateekTaneja · Microsoft Tech Community - Microsoft Sentinel Blog · 9 jun 2025. Anuncia conectores GA y en preview migrados de Azure Functions a CCF (Confluence, Auth0, Azure DevOps, Box, Proofpoint, SentinelOne, GCP, CrowdStrike FDR) y explica por qué CCF reemplaza al patrón Function App.
- [Forward On-Premises Windows Security Event Logs to Microsoft Sentinel](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/forward-on-premises-windows-security-event-logs-to-microsoft-sentinel/3040784) · Blog oficial · Empleado de Microsoft · Legado aún útil · paulberg · Microsoft Tech Community - Core Infrastructure and Security Blog · 16 dic 2021. Recorrido paso a paso para montar WEF/WEC on-premises (GPO, suscripciones, dimensionamiento) y enviar los eventos a Sentinel con Azure Arc + AMA. *Nota:* El conector 'Windows Forwarded Events' aparecía en preview; hoy se configura desde el portal de Defender y los eventos llegan a WindowsEvent. La guía de dimensionamiento WEC sigue vigente

### Webinars, videos y podcasts

- [Transforming data collection for AI-ready security operations with Microsoft Sentinel (webinar)](https://www.youtube.com/watch?v=QHEtAHGiCpc) · Webinar · Empleado de Microsoft · Krishna Sagar B V; Javier Soriano; David Hoerster · Microsoft Security Community (YouTube) · 11 dic 2025. Webinar sobre la visión de recolección de datos de Sentinel: pipeline, Table Management, conectores on-prem, de primera y de terceros, CCF, normalización y hoja de ruta.
- [Data Collection Scenarios](https://www.youtube.com/watch?v=FStpHl0NRM8) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube · 18 mar 2021. Material enlazado en el Módulo 4 ('Recolección de datos') del skill-up de Learn: webinar «Data Collection Scenarios» ofrecido en YouTube, MP4, presentation.

### Laboratorios, GitHub y herramientas

- [AzLogDcrIngestPS - Log Ingestion API, custom tables v2 and Data Collection Rules (PowerShell module)](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · GitHub · MVP · Morten Knudsen · GitHub (KnudsenMorten). Módulo PowerShell que automatiza la creación/actualización de tablas personalizadas v2, DCR y DCE, valida esquemas y envía datos vía Logs Ingestion API, con videos de migración desde el Data Collector API.
- [oshezaf/sentinelninja (Solutions Analyzer y documentación de conectores)](https://github.com/oshezaf/sentinelninja/tree/main/) · GitHub · Empleado de Microsoft · Ofer Shezaf · GitHub · dic 2025. Repositorio del PM de Sentinel con el Solutions Analyzer, que mapea conectores a las tablas que pueblan, y documentación de conectores generada desde sus definiciones.
- [Windows Event Collection (WEC/WEF) to Microsoft Sentinel — Complete Guide](https://github.com/kcl-ghas-org/sentinel-deploy/blob/main/Windows-WEC-WEF-to-Sentinel.md) · GitHub · Comunidad · kmboland · GitHub (kcl-ghas-org/sentinel-deploy). Guía comunitaria detallada para WEC/WEF: tamaño del log ForwardedEvents, suscripciones, permisos, onboarding Arc y DCR del conector Windows Forwarded Events via AMA.

### Comunidad: blogs, libros, newsletters y eventos

- [Take 3: How I Made My AI Agent Say "This Is Driving Me Crazy!" (and Provided an Exciting Alternative to Sentinel Connectors Docs on the way)](https://www.linkedin.com/pulse/take-3-finally-microsoft-sentinel-has-decent-connector-ofer-shezaf-qdx7c/) · Blog · Empleado de Microsoft · Ofer Shezaf · LinkedIn · 10 dic 2025. Presenta la documentación unificada y actualizada de todos los conectores de Sentinel (aka.ms/sentinel_connector_docs) y lecciones prácticas de codificar con agentes de IA.
- [Kaido Järvemets - Articles (Azure Data Collection Rules: The Complete Guide)](https://docs.kaidojarvemets.com/articles) · Blog · MVP · Kaido Järvemets · kaidojarvemets.com · feb 2026. Artículos sobre Data Collection Rules, Azure Arc y monitoreo con Sentinel.
- [365 by Thijs - Sentinel (Health monitoring y CI/CD)](https://365bythijs.be/category/security/sentinel/) · Blog · MVP · Thijs Lecomte · 365bythijs.be · 13 feb 2026. Blog personal con artículos recientes sobre la función de salud de Sentinel (habilitarla vía CI/CD, fallos de reglas) y la operación de Sentinel como MSSP.

**Manos a la obra**

1. `Laboratorio` Clasifica diez conectores de tu entorno por método de ingesta usando la [referencia de conectores](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources).
2. `Laboratorio` Despliega un reenviador Linux con AMA (con Azure Arc si está fuera de Azure) y el conector Syslog/CEF vía AMA ([configurar](https://learn.microsoft.com/en-us/azure/sentinel/connect-cef-syslog-ama)).
3. `Laboratorio` Habilita Windows Security Events vía AMA con el conjunto Common y compara el volumen con Minimal ([conjuntos de eventos](https://learn.microsoft.com/en-us/azure/sentinel/windows-security-event-id-reference)).
4. `Laboratorio` Envía un log personalizado con la API de ingesta de logs a una tabla propia.
5. `Laboratorio` Activa el libro de salud de recolección y una alerta para cuando un conector deje de enviar datos ([salud de conectores](https://learn.microsoft.com/en-us/azure/sentinel/monitor-data-connector-health)).

**¿Quieres profundizar?**

- [Transforming data collection for AI-ready security operations with Microsoft Sentinel (webinar)](https://www.youtube.com/watch?v=QHEtAHGiCpc) · Webinar
- [AzLogDcrIngestPS - Log Ingestion API, custom tables v2 and Data Collection Rules (PowerShell module)](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · GitHub
- [oshezaf/sentinelninja (Solutions Analyzer y documentación de conectores)](https://github.com/oshezaf/sentinelninja/tree/main/) · GitHub
- [Take 3: How I Made My AI Agent Say "This Is Driving Me Crazy!" (and Provided an Exciting Alternative to Sentinel Connectors Docs on the way)](https://www.linkedin.com/pulse/take-3-finally-microsoft-sentinel-has-decent-connector-ofer-shezaf-qdx7c/) · Blog

<a id="m3"></a>

## M3 · Gestión de logs, niveles de datos y costos

*L300 · ~6 h · Origen: Módulo 5 · Log management*

Después de cuántos workspaces, las grandes preguntas de arquitectura son **qué dato guardar en cada nivel, por cuánto tiempo y a qué costo**. Sentinel distingue hoy entre el **nivel de analítica** —datos de alto valor, consultables al instante por reglas, búsquedas y libros— y el **data lake**, pensado para grandes volúmenes y retención prolongada a bajo costo, consultable con KQL y notebooks.

Las reglas de resumen, los trabajos de búsqueda, los KQL jobs y la retención por tabla completan la caja de herramientas, junto con los modelos de precios y los beneficios incluidos en algunas licencias. Bien usadas, estas piezas reducen la factura sin perder visibilidad; mal usadas, generan puntos ciegos justo donde un atacante se esconde. También verás cómo proteger el acceso a los propios logs.

**Qué vas a lograr**

- Decidir el nivel de almacenamiento adecuado para cada tabla según su valor de detección.
- Configurar retención por tabla, reglas de resumen, trabajos de búsqueda y KQL jobs.
- Estimar y monitorear costos con las herramientas oficiales.
- Proteger el acceso a los datos con RBAC por recurso y por tabla y con Private Link.

> **Novedad.** Dos niveles: **analítica** (detección en tiempo real, búsqueda, alertas) y **data lake** (retención de hasta 12 años, formato abierto, una sola copia y cómputo separado) ([data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)). Desde el 23 de septiembre de 2026 el nivel lake se habilita por tabla en Table management, las consultas interactivas al lago se hacen desde la búsqueda avanzada y la retención de archivo evoluciona a retención en el lago ([novedades](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

> **Atención.** Tras incorporar el data lake, las tablas Auxiliary dejan de verse en la búsqueda avanzada y se consultan en el lago; las tablas personalizadas heredadas (MMA/CLv1) no se reflejan ([conectores y lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-connectors)).

> **Consejo Ninja.** Elige la herramienta correcta: **KQL jobs** sobre el lago (hasta 12 años, admiten joins), **summary rules** (intervalos de 20 minutos a 24 horas) y **search jobs** para datos archivados o anteriores al onboarding ([comparación](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs)).

> **Atención.** Precios de lista publicados en USD (varían por región y acuerdo): analítica con pago por uso 4,30/GB; lago con ingesta 0,05/GB, procesamiento 0,10/GB, consulta 0,005/GB y almacenamiento 0,026/GB-mes. Verifica siempre la [página de precios](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) y la [retención por nivel](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview).

**¿Tienes poco tiempo?**

- [What is Microsoft Sentinel data lake?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview) · Documentación
- [Manage data tiers and retention in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview) · Documentación
- [Compare KQL jobs, summary rules, and search jobs in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs) · Documentación

### Documentación, cursos y credenciales

- [Compare KQL jobs, summary rules, and search jobs in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Tabla comparativa de KQL jobs, summary rules y search jobs (nivel de origen, alcance, joins, frecuencia, lookback, timeout, límites y modelo de precio) con guía de elección.
- [Set up connectors for the Microsoft Sentinel data lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-connectors) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Configuración de retención y tiering por conector (analytics + espejo o solo lake), datos XDR, tablas personalizadas, tablas Auxiliary e ingesta directa al lake.
- [What is Microsoft Sentinel data lake?](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview) · Documentación · Oficial · Microsoft Learn. Describe el data lake de Sentinel: almacenamiento Parquet de copia única, separación de cómputo y almacenamiento, niveles analytics y data lake, retención hasta 12 años, exploración KQL, jobs de promoción y notebooks.
- [Manage data tiers and retention in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/manage-data-overview) · Documentación · Oficial · Microsoft Learn. Explica la gestión de tablas en el portal de Defender: retención analítica (30 días por defecto, hasta 2 años), retención total en el lake (hasta 12 años), nivel solo-lake y tratamiento de tablas XDR.
- [Aggregate Microsoft Sentinel data with summary rules](https://learn.microsoft.com/en-us/azure/sentinel/summary-rules) · Documentación · Oficial · Microsoft Learn. Cómo crear reglas de resumen y desplegar plantillas para agregar datos voluminosos (incluso de niveles baratos) en tablas _CL del nivel analytics, para reportes, ahorro y privacidad.
- [Microsoft Sentinel Pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/) · Documentación · Oficial · Microsoft Security. Página oficial de precios con niveles de análisis (PAYG y compromisos), medidores del data lake y del graph, nivel promocional de 50 GB y el beneficio de hasta 5 MB/usuario/día de ingesta gratuita.
- [Export from Microsoft Sentinel / Log Analytics workspace to Azure Storage and Event Hubs](https://learn.microsoft.com/en-us/cli/azure/monitor/log-analytics/workspace/data-export) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Export from Microsoft Sentinel / Log Analytics workspace to Azure Storage and Event Hubs».
- [Move logs to long-term storage by using Azure Logic Apps](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-export-logic-app) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Move logs to long-term storage by using Azure Logic Apps».
- [Configure data retention and archive policies in Azure Monitor Logs (Preview)](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Configure data retention and archive policies in Azure Monitor Logs (Preview)».
- [Manage access to Log Analytics workspaces (table-level RBAC)](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/manage-access) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Table-level RBAC».
- [Delete customer content from your workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/personal-data-mgmt) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Delete customer content from your workspaces».
- [Use Azure Private Link with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/private-link-security) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Private links».
- [Dedicated workspace cluster](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/logs-dedicated-clusters) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: doc «Dedicated workspace cluster».

### Anuncios y blogs oficiales

- [Microsoft Sentinel data lake is now generally available](https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-sentinel-data-lake-is-now-generally-available/4456342) · Blog oficial · Empleado de Microsoft · vkokkengada · Microsoft Tech Community - Microsoft Security Community Blog · 30 sep 2025. Anuncia la disponibilidad general del data lake de Sentinel y presenta casos de uso (investigaciones de largo plazo, líneas base de comportamiento, enriquecimiento, hunting retrospectivo).
- [Empowering defenders in the era of agentic AI with Microsoft Sentinel](https://www.microsoft.com/en-us/security/blog/2025/09/30/empowering-defenders-in-the-era-of-agentic-ai-with-microsoft-sentinel/) · Blog oficial · Empleado de Microsoft · Vasu Jakkal · Microsoft Security Blog · 30 sep 2025. Anuncio ejecutivo de Sentinel como plataforma agéntica: GA del data lake y vista previa pública de Sentinel graph y del servidor MCP, más el constructor de agentes sin código de Security Copilot.
- [Unlocking value with Microsoft Sentinel data lake](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/unlocking-value-with-microsoft-sentinel-data-lake/4497660) · Blog oficial · Empleado de Microsoft · atennant · Microsoft Tech Community - Microsoft Sentinel Blog · 26 feb 2026. Casos de valor del data lake: base de datos unificada y económica, análisis histórico de hasta 12 años, hunting retrospectivo de IOC y analítica con grafos y agentes.
- [Microsoft Sentinel data lake: Unify signals, cut costs, and power agentic AI](https://www.microsoft.com/en-us/security/blog/2025/07/22/microsoft-sentinel-data-lake-unify-signals-cut-costs-and-power-agentic-ai/) · Blog oficial · Empleado de Microsoft · Legado aún útil · Scott Woodgate; Krishna Kumar Parthasarathy · Microsoft Security Blog · 22 jul 2025. Presenta el data lake de Sentinel en vista previa pública y anuncia la convergencia de las capacidades de MDTI en Defender XDR y Sentinel sin costo adicional. *Nota:* Anuncio de preview (jul-2025); el lake es GA desde sep-2025. Fuente oficial del cambio de licenciamiento de MDTI (desde oct-2025 reportes, perfiles e IoC en Defender XDR). Ver M4
- [Ingest, archive, search, and restore data in Microsoft Sentinel](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/ingest-archive-search-and-restore-data-in-microsoft-sentinel/ba-p/3195126) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: blog-oficial «Ingest, archive, search, and restore data in Microsoft Sentinel».
- [Table-level retention settings](https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/azure-log-analytics-data-retention-by-type-in-real-life/ba-p/1416287) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: blog-oficial «Table-level retention settings».
- [Resource role-based access control (RBAC)](https://techcommunity.microsoft.com/t5/azure-sentinel/controlling-access-to-azure-sentinel-data-resource-rbac/ba-p/1301463) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: blog-oficial «Resource role-based access control (RBAC)».
- [Audit workspace queries and Microsoft Sentinel use by using alerts workbooks and queries](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/auditing-microsoft-sentinel-activities/ba-p/1718328) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 5 ('Gestión de logs') del skill-up de Learn: blog-oficial «Audit workspace queries and Microsoft Sentinel use by using alerts workbooks and queries».

### Webinars, videos y podcasts

- [Microsoft Sentinel data lake (playlist)](https://www.youtube.com/playlist?list=PL3ZTgFEc7LyvM-OlDTB8BDV_aARfmBMG9) · Video · Oficial · Microsoft Security (YouTube). Serie de 8 videos cortos con demos: introducción al lake, consultas KQL, KQL jobs, notebooks, gestión de costos, Sentinel graph y servidor MCP.
- [Microsoft Sentinel Data Lake: Architecture, Cost Optimization, and Use Cases](https://www.youtube.com/watch?v=CrFGMSI125Q) · Video · Comunidad · Christopher Brumm; Marvin Rose · glueckkanja (YouTube). Sesión de partner con demos de tablas y costos del lake, comparación analytics vs. lake (compresión 6:1), KQL jobs, MCP con VS Code, notebooks y Sentinel graph.
- [Microsoft Sentinel | Introduction to Sentinel data lake for Developers (webinar)](https://www.youtube.com/watch?v=oLvM4NVVtpQ) · Webinar · Empleado de Microsoft · James Coliz; Eleanor Falla · Microsoft Security Community (YouTube) · 4 nov 2025. Webinar para desarrolladores/ISV sobre el data lake: datos unificados, analítica avanzada, graph, servidor MCP, agentes y demo en VS Code.

### Laboratorios, GitHub y herramientas

- [Workspace Usage Report (workbook)](https://github.com/clivewatson/KQLpublic/tree/master/KQL/Workbooks/WorkspaceUsage) · GitHub · MVP · Legado aún útil · Clive Watson · GitHub · sep 2022. Workbook para analizar ingesta, uso y costos de los workspaces de Log Analytics/Sentinel por tabla y fuente. *Nota:* Última versión anunciada por el autor: v1.6 (sep-2022); anterior al data lake

### Comunidad: blogs, libros, newsletters y eventos

- [Microsoft Sentinel Cost Estimation and Optimization — The Definitive Guide!](https://charbelnemnom.com/sentinel-cost-estimation-and-optimization/) · Blog · MVP · Nuevo · Charbel Nemnom · charbelnemnom.com · 22 jun 2026. Guía extensa y actualizada sobre todos los medidores de Sentinel (analytics, lake, consultas, notebooks, federación), descuentos (E5, Defender for Servers P2), escenarios de dimensionamiento y estrategias de filtrado y división.
- [The Sentinel Data Lake Got Respecced: What Actually Moved to Fabric](https://www.itprofessor.cloud/sentinel-data-lake-fabric-changes/) · Blog · Comunidad · Nuevo · IT Professor (autor no identificado) · itprofessor.cloud · 1 oct 2026. Explica en lenguaje práctico el cambio del 23-sep-2026: almacenamiento del lake como ajuste de tabla, consultas interactivas en Advanced Hunting y jobs/notebooks/grafos movidos a Microsoft Fabric, con cómo rehacer un KQL job como summary rule.
- [Practical Sentinel: Reviewing and Optimizing costs](https://practical365.com/practical-sentinel-reviewing-and-optimizing-costs/) · Blog · MVP · Legado aún útil · Thijs Lecomte · Practical365 · 22 may 2025. Método práctico para revisar costos: Azure Cost Analysis, workbook de costos del Content hub, detectar tablas no usadas en reglas (LAQueryLogs) y mover datos a niveles más baratos. *Nota:* Escrito antes del GA del data lake: sus recomendaciones sobre Basic/Auxiliary deben leerse hoy como 'nivel data lake'. Estatus MVP de Thijs Lecomte según su perfil público (verificar)
- [Learn Sentinel (blog de Matt Zorich)](https://learnsentinel.blog/author/mzorich/) · Blog · Empleado de Microsoft · Legado aún útil · Matt Zorich · learnsentinel.blog. Blog con guías prácticas de KQL avanzado (mv-expand, mv-apply), detecciones y gestión de datos en Sentinel. *Nota:* Sin publicaciones recientes; conceptos de KQL siguen vigentes
- [Use Sentinel Basic and Archive logs](https://medium.com/@koosg/use-sentinel-basic-and-archive-logs-fae3bb3a6299) · Blog · MVP · Legado aún útil · Koos Goossens · Medium. Serie sobre reducir costos con los niveles Basic y Archive de Log Analytics en Sentinel. *Nota:* Superado en gran parte por el data lake y el nivel Auxiliary; útil como contexto histórico de niveles de datos

**Manos a la obra**

1. `Laboratorio parcial` Con la tabla `Usage`, lista las diez tablas de mayor volumen y clasifícalas por valor de detección.
2. `Laboratorio` Mueve al nivel lake una tabla de alto volumen y bajo valor de detección, y define su retención.
3. `Laboratorio` Crea una [summary rule](https://learn.microsoft.com/en-us/azure/sentinel/summary-rules) que agregue por hora los registros de firewall en una tabla de analítica.
4. `Laboratorio` Ejecuta un KQL job sobre el lago y usa su resultado en una regla.
5. `Laboratorio` Arma una estimación mensual de costos con la página de precios y el beneficio de Microsoft 365 E5; compara dos escenarios.

**¿Quieres profundizar?**

- [Microsoft Sentinel Cost Estimation and Optimization — The Definitive Guide!](https://charbelnemnom.com/sentinel-cost-estimation-and-optimization/) · Blog
- [Practical Sentinel: Reviewing and Optimizing costs](https://practical365.com/practical-sentinel-reviewing-and-optimizing-costs/) · Blog
- [Learn Sentinel (blog de Matt Zorich)](https://learnsentinel.blog/author/mzorich/) · Blog
- [Workspace Usage Report (workbook)](https://github.com/clivewatson/KQLpublic/tree/master/KQL/Workbooks/WorkspaceUsage) · GitHub

<a id="m4"></a>

## M4 · Enriquecimiento: inteligencia de amenazas, watchlists y más

*L300 · ~5 h · Origen: Módulo 6 · Enrichment: Threat intelligence, watchlists, and more*

Un evento aislado dice poco; con contexto, dice mucho. La **inteligencia de amenazas** aporta indicadores y objetos STIX —actores, campañas, infraestructura, relaciones— que se cruzan con tus registros en reglas y búsquedas. Las **watchlists** traen tu propio contexto de negocio —activos críticos, cuentas privilegiadas, empleados que dejaron la organización, rangos de IP autorizados— para priorizar alertas, reducir la fatiga y enriquecer investigaciones.

En el portal de Defender la gestión de inteligencia de amenazas se unificó para SIEM y XDR, y la inteligencia de Microsoft quedó integrada en la plataforma. Además de las watchlists, existen otras formas de búsqueda de contexto —funciones KQL, `externaldata`, tablas personalizadas— con ventajas y límites distintos. Este módulo te enseña a importar, administrar y usar todo ese contexto.

**Qué vas a lograr**

- Importar inteligencia de amenazas con TAXII, la API de carga y los conectores de Microsoft.
- Usar indicadores y objetos STIX en reglas de coincidencia y búsquedas.
- Crear y consumir watchlists para listas de permitidos, activos críticos y enriquecimiento.
- Elegir el mecanismo de búsqueda de contexto adecuado para cada caso.

> **Qué cambió.** Las tablas **ThreatIntelIndicators** y **ThreatIntelObjects** reemplazaron a `ThreatIntelligenceIndicator`, que dejó de recibir datos el 31 de agosto de 2025 y perdió soporte en mayo de 2026: actualiza reglas y libros que la usen ([nuevas tablas de TI](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/table-talk-sentinel%E2%80%99s-new-threatintel-tables-explained/4440273)).

> **Novedad.** Las capacidades de Microsoft Defender Threat Intelligence, incluidas las premium, convergieron en Defender XDR y Sentinel sin costo adicional, y el producto independiente se retiró ([anuncio de convergencia](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991)). La página del conector aún menciona un SKU de API pago: verifica el requisito vigente.

> **Consejo Ninja.** En el portal de Defender la inteligencia de amenazas se gestiona en Intel explorer con objetos STIX, relaciones, TLP y reglas de ingesta para curar feeds ([trabajar con indicadores](https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators)); se importan feeds TAXII 2.0/2.1 y se puede exportar a TAXII 2.1 ([TAXII](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-taxii)).

> **Atención.** Límites de watchlists: 10 millones de elementos activos por workspace, CSV local de hasta 3,8 MB y refresco de la tabla Watchlist cada 12 días; consúltalas con `_GetWatchlist` ([watchlists](https://learn.microsoft.com/en-us/azure/sentinel/watchlists)).

**¿Tienes poco tiempo?**

- [Enable the Microsoft Defender Threat Intelligence data connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-mdti-data-connector) · Documentación
- [Table Talk: Sentinel's New ThreatIntel Tables Explained](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/table-talk-sentinel%E2%80%99s-new-threatintel-tables-explained/4440273) · Blog oficial

### Documentación, cursos y credenciales

- [Enable the Microsoft Defender Threat Intelligence data connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-mdti-data-connector) · Documentación · Oficial · Nuevo · Microsoft Learn · 1 jul 2026. Habilita con un clic los conectores estándar y premium de Defender Threat Intelligence para traer IOC de alta fidelidad de Microsoft a la tabla ThreatIntelIndicators y usarlos en reglas TI map y matching analytics.
- [Use STIX/TAXII to import and export threat intelligence in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-taxii) · Documentación · Oficial · Ninja original · Microsoft Learn. Configura el conector Threat Intelligence - TAXII para importar desde servidores TAXII 2.0/2.1 y el conector TAXII Export para compartir inteligencia con plataformas TAXII 2.1. *Nota:* Incluye la lista de IP del cliente TAXII de Sentinel para allowlisting (p. ej., FS-ISAC). La exportación TAXII es una capacidad reciente frente a la Ninja original
- [Work with Microsoft Sentinel threat intelligence](https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators) · Documentación · Oficial · Microsoft Learn. Gestión de TI en Intel explorer (portal de Defender): crear objetos STIX con relaciones y TLP, reglas de ingesta para curar feeds, búsqueda, etiquetado y exportación.
- [Work with STIX objects and indicators to enhance threat intelligence and threat hunting in Microsoft Sentinel (Preview)](https://learn.microsoft.com/en-us/azure/sentinel/work-with-stix-objects-indicators) · Documentación · Oficial · Vista previa · Microsoft Learn. Consultas KQL para correlacionar indicadores con actores de amenaza y TTP usando ThreatIntelIndicators/ThreatIntelObjects, migrar consultas al nuevo esquema y filtrar filas/columnas antes de la ingesta. *Nota:* La republicación de datos TI ocurre cada 7-10 días (LastUpdateMethod = LogARepublisher); campos largos de Data se truncan a 1.000 caracteres
- [Threat intelligence integration in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/threat-intelligence-integration) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: doc «Threat intelligence integration in Microsoft Sentinel».
- [Understand threat intelligence in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/understand-threat-intelligence) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: doc «Threat intelligence».
- [geo_info_from_ip_address()](https://learn.microsoft.com/en-us/kusto/query/geo-info-from-ip-address-function?view=microsoft-fabric) · Documentación · Oficial · Microsoft Learn (Kusto). Función KQL (válida en Microsoft Sentinel) que devuelve país, estado, ciudad y coordenadas de una IPv4/IPv6 para enriquecer consultas, reglas y transformaciones.
- [Connect your threat intelligence platform to Microsoft Sentinel with the upload API (Preview)](https://learn.microsoft.com/en-us/azure/sentinel/connect-threat-intelligence-upload-api) · Documentación · Oficial · Vista previa · Microsoft Learn. Conecta una TIP o aplicación propia mediante la upload API basada en objetos STIX (registro de app en Entra, rol Sentinel Contributor a nivel workspace) sin necesidad de conector. *Nota:* Sustituye al conector legacy 'Threat Intelligence Platforms' (Graph tiIndicators) y a la Upload Indicators API anterior
- [Create watchlists in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create) · Documentación · Oficial · Vista previa · Microsoft Learn. Crear watchlists desde CSV local (hasta 3,8 MB), desde Azure Storage con URL SAS (hasta 500 MB), manualmente o desde plantillas, y entender su estado y recreación. *Nota:* La carga local es GA; plantillas, carga desde Azure Storage y creación manual siguen en preview. En el portal de Defender: Microsoft Sentinel > Configuration > Watchlist

### Anuncios y blogs oficiales

- [Table Talk: Sentinel's New ThreatIntel Tables Explained](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/table-talk-sentinel%E2%80%99s-new-threatintel-tables-explained/4440273) · Blog oficial · Empleado de Microsoft · neelam_n · Microsoft Tech Community - Microsoft Sentinel Blog · 5 ago 2025. Explica las nuevas tablas STIX ThreatIntelIndicators y ThreatIntelObjects frente a la legacy ThreatIntelligenceIndicator, con fechas de transición, diferencias de esquema, impacto en volumen y consultas de ejemplo.
- [MDTI is Converging into Microsoft Sentinel and Defender XDR](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/mdti-is-converging-into-microsoft-sentinel-and-defender-xdr/4427991) · Blog oficial · Empleado de Microsoft · Mike_Browning · Microsoft Tech Community - Microsoft Defender XDR Blog · 22 jul 2025. Anuncia que las capacidades de Microsoft Defender Threat Intelligence (incluido premium) se integran en Defender XDR y Sentinel sin costo adicional: informes, intel profiles, IoC y TTP en Threat analytics e IoC en case management.
- [Implementing lookups in Microsoft Sentinel.](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/implementing-lookups-in-azure-sentinel/ba-p/1091306) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: blog-oficial «Implementing lookups in Microsoft Sentinel.».
- [Utilize watchlists to drive efficiency during Microsoft Sentinel investigations](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/utilize-watchlists-to-drive-efficiency-during-microsoft-sentinel/ba-p/2090711) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: blog-oficial «Utilize watchlists to drive efficiency during Microsoft Sentinel investigations».
- [Become a Microsoft Defender Threat Intelligence Ninja: The complete level 400 training](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/become-an-mdti-ninja-the-complete-level-400-training/3656965) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community – Microsoft Defender XDR Blog · 26 oct 2022. Ninja de nivel 400 de Defender Threat Intelligence (intel profiles, búsquedas, Graph API, workbooks, playbooks de Sentinel) con knowledge check y certificado actualizados en ago-2023. *Nota:* Lanzado 26-oct-2022 (aka.ms/BecomeAnMDTINinja); actualizado 16-ago-2023. MDTI se integró en Defender XDR/Security Copilot; verificar estado del producto antes de citar. Mapa: -> M4

### Webinars, videos y podcasts

- [Brewing KQL: Smarter Threat Intel Feeds with AI & MISP with Sergio Albea (KQL Cafe, May 2026)](https://www.youtube.com/watch?v=e-mg6XYcCAY) · Video · Comunidad · Nuevo · Gianni Castaldi, Alex Verboon, Sergio Albea · KQL Cafe (YouTube) · 26 may 2026. Episodio sobre evaluación de feeds de TI con KQL e IA, mejoras del portal de advanced hunting y un cambio disruptivo en la función ASIM ImProcessCreate.
- [Threat intelligence in Microsoft Sentinel (Ignite session, 28 min)](https://www.youtube.com/watch?v=RLt05JaOnHc) · Video · Oficial · Legado aún útil · Ninja original · YouTube. Enlace del Módulo 6 ('Enriquecimiento: TI y watchlists') del skill-up de Learn: video «Ignite session».

### Laboratorios, GitHub y herramientas

- [MC1192257 - Microsoft Defender Threat Intelligence: Convergence with Microsoft Defender and Microsoft Sentinel (archivo del Message Center)](https://mc.merill.net/message/MC1192257) · Herramienta · Empleado de Microsoft · Merill Fernando · mc.merill.net (archivo comunitario del Microsoft 365 Message Center) · 22 dic 2025. Copia del aviso MC1192257: la convergencia de MDTI culmina el 1-ago-2026, el producto independiente se retira y desde entonces sus capacidades requieren licencia activa de Defender o Sentinel.

### Comunidad: blogs, libros, newsletters y eventos

- [michalos.net (blog)](https://www.michalos.net/) · Blog · Empleado de Microsoft · Nuevo · Michalis Michalos · michalos.net · oct 2026. Blog sobre SecOps, DFIR e inteligencia de amenazas con KQL en Sentinel y Defender XDR (auditoría, ofuscación de resultados, pilares de TI).

**Manos a la obra**

1. `Laboratorio` Conecta el conector de inteligencia de amenazas de Microsoft y un feed TAXII público; verifica los datos en `ThreatIntelIndicators`.
2. `Laboratorio` Habilita una plantilla de regla de coincidencia de indicadores (TI map) contra registros de inicio de sesión y valida una alerta.
3. `Laboratorio` Crea las watchlists «Usuarios VIP» e «IP de escáneres autorizados» y úsalas en una regla para elevar la severidad o suprimir alertas ([crear watchlists](https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create)).
4. `Laboratorio` Enriquece inicios de sesión con `geo_info_from_ip_address()` y discute sus límites de precisión ([función](https://learn.microsoft.com/en-us/kusto/query/geo-info-from-ip-address-function?view=microsoft-fabric)).

**¿Quieres profundizar?**

- [michalos.net (blog)](https://www.michalos.net/) · Blog
- [MC1192257 - Microsoft Defender Threat Intelligence: Convergence with Microsoft Defender and Microsoft Sentinel (archivo del Message Center)](https://mc.merill.net/message/MC1192257) · Herramienta
- [Brewing KQL: Smarter Threat Intel Feeds with AI & MISP with Sergio Albea (KQL Cafe, May 2026)](https://www.youtube.com/watch?v=e-mg6XYcCAY) · Video

<a id="m5"></a>

## M5 · Transformación de logs

*L300 · ~4 h · Origen: Módulo 7 · Log transformation*

No todo lo que llega merece guardarse tal cual. Las **transformaciones en tiempo de ingesta**, definidas con KQL dentro de reglas de recolección de datos, actúan antes de que el dato se almacene: filtran ruido, eliminan columnas, enmascaran datos personales, normalizan valores, agregan contexto y permiten **dividir un mismo flujo** entre el nivel de analítica y niveles más económicos.

Es una de las palancas más efectivas para controlar costos y mejorar la calidad de los datos, y funciona tanto con conectores basados en Azure Monitor Agent como con la API de ingesta y con la DCR de transformación del workspace para conectores de servicio. Este módulo cubre cuándo transformar, cómo escribir transformaciones seguras y cómo probarlas.

**Qué vas a lograr**

- Explicar dónde actúan las transformaciones de ingesta y qué limitaciones de KQL tienen.
- Crear transformaciones para filtrar, enmascarar y enriquecer datos.
- Dividir datos entre niveles de almacenamiento para optimizar costos.

> **Novedad.** Las transformaciones **filter** y **split** se configuran desde Table management en el portal de Defender sin escribir DCR a mano; split envía lo que cumple la condición al nivel de analítica y el resto solo al lago ([filter y split](https://learn.microsoft.com/en-us/azure/sentinel/transformation-filter-split)). El Training Lab incluye un ejercicio dedicado ([E16](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/Exercises/E16_split_transformation.md)).

> **Consejo Ninja.** Con Sentinel habilitado no se cobra el filtrado hacia tablas de analítica ([transformación de datos](https://learn.microsoft.com/en-us/azure/sentinel/data-transformation)). Toda transformación parte de la tabla virtual `source`, debe producir `TimeGenerated` y las columnas personalizadas en tablas integradas terminan en `_CF` ([crear transformaciones](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations-create)).

> **Novedad.** Las transformaciones multietapa, en vista previa, agregan procesadores declarativos y procesamiento en el agente ([transformaciones](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations)).

**¿Tienes poco tiempo?**

- [Transform data using filter and split in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/transformation-filter-split) · Documentación
- [Microsoft Sentinel Training Lab - Exercise 16: Data Transformation: Split Ingestion by Tier](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/Exercises/E16_split_transformation.md) · Laboratorio

### Documentación, cursos y credenciales

- [Transform data using filter and split in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/transformation-filter-split) · Documentación · Oficial · Microsoft Learn. Configura desde Table management del portal de Defender reglas de filtro (descartar ruido con una condición KQL) y de división (enviar parte de los datos al nivel data lake) sin escribir DCR a mano.
- [Custom data ingestion and transformation in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/data-transformation) · Documentación · Oficial · Microsoft Learn. Marco conceptual de transformaciones en ingesta con DCR (filtrar, enriquecer, normalizar con ASIM, enmascarar datos sensibles), Logs Ingestion API y DCR de transformación del workspace.
- [Transformations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Visión general de las transformaciones en DCR: tablas soportadas, DCR de transformación del workspace, costos y las nuevas transformaciones multi-etapa con procesadores declarativos que pueden ejecutarse en el agente.
- [Create a transformation in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations-create) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Cómo escribir y probar consultas de transformación (tabla virtual source, TimeGenerated obligatorio), agregarlas al JSON de una DCR (transformKql), crear la DCR de workspace y diagnosticar problemas.
- [Sample transformations in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations-samples) · Documentación · Oficial · Microsoft Learn (Azure Monitor). Catálogo de consultas de ejemplo para reducir costos (filtrar filas/columnas), parsear, enviar filas a tablas más baratas, enmascarar datos sensibles, enriquecer y normalizar a ASIM.
- [Transform or customize data at ingestion time in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 7 ('Transformación de logs') del skill-up de Learn: doc «Transform or customize data at ingestion time in Microsoft Sentinel».
- [Data collection rules in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 7 ('Transformación de logs') del skill-up de Learn: doc «Data collection rules».
- [Workspace data transformations for standard logs](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-transformations-workspace) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 7 ('Transformación de logs') del skill-up de Learn: doc «** Workspace data transformations for standard logs**».

### Laboratorios, GitHub y herramientas

- [Microsoft Sentinel Training Lab - Exercise 16: Data Transformation: Split Ingestion by Tier](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/Microsoft-Sentinel-Training-Lab/Exercises/E16_split_transformation.md) · Laboratorio · Empleado de Microsoft · Andreas Kapetaniou · GitHub (Azure/Azure-Sentinel). Ejercicio práctico que crea una regla de división sobre CommonSecurityLog para enviar solo tráfico denegado de Palo Alto al nivel Analytics y el resto al data lake (tabla con sufijo _SPLT).
- [Tutorial: Add a workspace transformation by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-workspace-transformations-portal) · Laboratorio · Oficial · Microsoft Learn (Azure Monitor). Laboratorio guiado que crea la DCR de transformación del workspace para filtrar y enriquecer la tabla LAQueryLogs con una columna personalizada _CF.
- [AzLogDcrIngestPS - Log Ingestion API, custom tables v2 and Data Collection Rules (PowerShell module)](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · GitHub · MVP · Morten Knudsen · GitHub (KnudsenMorten). Módulo PowerShell que automatiza la creación/actualización de tablas personalizadas v2, DCR y DCE, valida esquemas y envía datos vía Logs Ingestion API, con videos de migración desde el Data Collector API.

**Manos a la obra**

1. `Laboratorio` Configura una transformación split para una tabla de firewall: tráfico denegado al nivel de analítica y permitido solo al lago.
2. `Laboratorio` Escribe una DCR de transformación del workspace que elimine columnas ruidosas y pruébala con `datatable` ([ejemplos](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-transformations-samples)).
3. `Laboratorio` Enmascara un campo de correo electrónico en la ingesta y compara el volumen antes y después con `Usage`.

**¿Quieres profundizar?**

- [AzLogDcrIngestPS - Log Ingestion API, custom tables v2 and Data Collection Rules (PowerShell module)](https://github.com/KnudsenMorten/AzLogDcrIngestPS) · GitHub
- [Tutorial: Add a workspace transformation by using the Azure portal](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-workspace-transformations-portal) · Laboratorio

<a id="m6"></a>

## M6 · Migración desde otro SIEM

*L300 · ~5 h · Origen: Módulo 8 · Migration*

En muchos casos —quizás en la mayoría— ya tienes un SIEM y necesitas migrar. Es un buen momento para repensar la implementación, pero también para aprovechar lo construido: casos de uso, reglas, automatización y datos históricos. Microsoft publica una guía de migración por fases y una **experiencia de migración en el portal de Defender** que analiza exportaciones de reglas de otros SIEM y propone equivalentes en Sentinel.

Aquí verás cómo planificar la migración, priorizar casos de uso, traducir detecciones, migrar la automatización, conservar datos históricos y operar en paralelo durante la transición. El objetivo no es replicar el SIEM anterior, sino terminar con un SOC mejor.

**Qué vas a lograr**

- Planificar una migración por fases con criterios de éxito.
- Traducir reglas de detección y automatización al modelo de Sentinel.
- Definir la estrategia para datos históricos y la operación en paralelo.

> **Novedad.** La experiencia de migración de SIEM del portal de Defender llegó a disponibilidad general en RSAC 2026: analiza exportaciones de Splunk o QRadar, recomienda reglas de Sentinel, detecciones nativas de Defender XDR y conectores. Requiere Security Copilot habilitado en el tenant, pero no consume SCU ([migración de SIEM](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration)).

> **Consejo Ninja.** No migres a ciegas: descarta reglas que no generaron alertas en 6 a 12 meses y valida las fuentes antes de habilitar las nuevas ([migrar reglas de Splunk](https://learn.microsoft.com/en-us/azure/sentinel/migration-splunk-detection-rules)).

**¿Tienes poco tiempo?**

- [Migrate to Microsoft Sentinel with the SIEM migration experience](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration) · Documentación
- [What's new in Microsoft Sentinel: RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971) · Blog oficial

### Documentación, cursos y credenciales

- [Migrate to Microsoft Sentinel with the SIEM migration experience](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration) · Documentación · Oficial · Microsoft Learn. Guía de la experiencia de migración SIEM del portal de Defender: exportar detecciones de Splunk (consulta REST) o QRadar (script collector), analizar, mapear a reglas OOTB de Sentinel y detecciones nativas de Defender XDR, y recomendar conectores.
- [Plan your migration to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/migration) · Documentación · Oficial · Microsoft Learn. Punto de partida de la guía de migración: fases, seguimiento con workbook, experiencia de migración SIEM y rutas por origen (ArcSight, Splunk, QRadar) para reglas, SOAR, datos históricos, dashboards y procesos del SOC.
- [Migrate Splunk detection rules to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/migration-splunk-detection-rules) · Documentación · Oficial · Microsoft Learn. Cómo auditar, priorizar y migrar detecciones de Splunk: empezar por la experiencia de migración SIEM, usar plantillas OOTB del Content hub y traducir manualmente con tablas de equivalencia SPL→KQL.
- [Migrate Splunk SOAR automation to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/migration-splunk-automation) · Documentación · Oficial · Microsoft Learn. Criterios para elegir casos de uso SOAR, mapeo de componentes de Splunk SOAR a reglas de automatización, playbooks de Logic Apps y Hybrid Runbook Worker, y buenas prácticas posteriores a la migración.

### Anuncios y blogs oficiales

- [What's new in Microsoft Sentinel: RSAC 2026](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/what%E2%80%99s-new-in-microsoft-sentinel-rsac-2026/4503971) · Blog oficial · Empleado de Microsoft · spalani · Microsoft Tech Community - Microsoft Sentinel Blog · 20 mar 2026. Novedades de RSAC 2026: experiencia de migración SIEM en GA (Splunk/QRadar), generador de playbooks, GDAP, URBAC y RBAC a nivel de fila para Sentinel, y federación de datos con Fabric/ADLS/Databricks.

### Laboratorios, GitHub y herramientas

- [ArcSight and QRadar rule mapping samples](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/RuleMigration/Rule%20Logic%20Mappings.md) · GitHub · Oficial · Legado aún útil · Ninja original · GitHub. Enlace del Módulo 8 ('Migración') del skill-up de Learn: github «ArcSight and QRadar rule mapping samples».

### Comunidad: blogs, libros, newsletters y eventos

- [Hybrid Brothers (blog)](https://hugo.hybridbrothers.com/) · Blog · MVP · Robbe Van den Daele · hybridbrothers.com. Blog de SOC engineering con Defender XDR y Sentinel, incluida una guía práctica de transición de Sentinel al portal Defender.
- [Practical Sentinel: A Practical Look at the Unified SecOps Experience](https://practical365.com/practical-sentinel-a-practical-look-at-the-unified-secops-experience/) · Blog · MVP · Legado aún útil · Thijs Lecomte · Practical365 · 21 may 2024. Análisis temprano de la integración de Sentinel en el portal Defender: beneficios del hunting unificado y limitaciones de la preview. *Nota:* Describe limitaciones de 2024 ya resueltas (multi-workspace, configuración en Defender); útil como contexto de la transición obligatoria antes del 31-mar-2027

**Manos a la obra**

1. `Laboratorio` Ejecuta la [experiencia de migración de SIEM](https://learn.microsoft.com/en-us/azure/sentinel/siem-migration) con una exportación de reglas de ejemplo y revisa sus recomendaciones.
2. `Laboratorio` Arma un plan por fases con criterios de éxito siguiendo la [guía de migración](https://learn.microsoft.com/en-us/azure/sentinel/migration).
3. `Laboratorio` Traduce tres búsquedas SPL a KQL con el [mapeo SPL a KQL](https://github.com/Azure/Azure-Sentinel/blob/master/Tools/RuleMigration/SPL%20to%20KQL.md).
4. `Laboratorio` Define la estrategia de datos históricos y la de automatización ([migrar automatización de Splunk](https://learn.microsoft.com/en-us/azure/sentinel/migration-splunk-automation)).

**¿Quieres profundizar?**

- [Hybrid Brothers (blog)](https://hugo.hybridbrothers.com/) · Blog

<a id="m7"></a>

## M7 · Analítica y detecciones

*L300 · ~10 h · Origen: Módulo 11 · Analytics*

Las reglas de analítica son el corazón de la detección. Puedes partir de plantillas, ajustarlas a tu entorno o escribir reglas propias: **programadas**, **casi en tiempo real (NRT)**, de **anomalías** o basadas en **machine learning**. Pero una regla es mucho más que su consulta: el mapeo de entidades, los detalles personalizados, la agrupación de alertas, la supresión, la severidad dinámica y el mapeo a MITRE ATT&CK determinan si una alerta es accionable o solo ruido.

En la plataforma unificada, las reglas de Sentinel conviven con las **detecciones personalizadas** de Defender, y el **motor de correlación de Defender XDR** agrupa alertas de SIEM y XDR en incidentes. Este módulo cubre los tipos de regla, los patrones clásicos de detección —correlación, agregación, búsquedas en listas, ventanas deslizantes, eventos demorados— y la práctica de ingeniería de detecciones: medir cobertura, ajustar falsos positivos y mejorar continuamente.

**Qué vas a lograr**

- Crear reglas programadas y NRT con mapeo de entidades, detalles y agrupación.
- Entender cómo se generan incidentes en el portal de Defender y el papel del motor de correlación.
- Medir la cobertura frente a MITRE ATT&CK y priorizar brechas.
- Ajustar reglas para reducir falsos positivos sin perder detección.

> **Qué cambió.** Desde el 28 de octubre de 2025, las **detecciones personalizadas** son la experiencia recomendada para crear reglas nuevas sobre datos de Sentinel y Defender XDR; las reglas de analítica existentes siguen funcionando y no hay que migrarlas ([anuncio](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875)). Según la [comparación oficial](https://learn.microsoft.com/en-us/azure/sentinel/compare-analytics-rules-custom-detections), solo las reglas de analítica permiten agrupación personalizada, alertas sin incidente y supresión; solo las detecciones personalizadas ofrecen acciones de respuesta nativas de XDR y NRT por streaming.

> **Qué cambió.** En el portal de Defender, Fusion se desactiva y lo reemplaza el motor de correlación de Defender XDR ([Fusion](https://learn.microsoft.com/en-us/azure/sentinel/fusion)); las reglas «Microsoft incident creation» no aplican, y solo las alertas del workspace principal se correlacionan con Defender ([correlación](https://learn.microsoft.com/en-us/defender-xdr/alerts-incidents-correlation)).

> **Consejo Ninja.** Las reglas NRT de analítica se ejecutan cada minuto con 2 minutos de retraso, con un máximo de 50 por cliente ([reglas NRT](https://learn.microsoft.com/en-us/azure/sentinel/near-real-time-rules)); cada regla admite hasta 10 mapeos de entidades con 3 identificadores cada uno ([mapeo de entidades](https://learn.microsoft.com/en-us/azure/sentinel/map-data-fields-to-entities)).

> **Novedad.** La página de cobertura MITRE ATT&CK (vista previa) está alineada con ATT&CK v18 ([cobertura MITRE](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage)), y la optimización del SOC suma recomendaciones de valor de datos, cobertura por amenaza y etiquetado MITRE asistido por IA ([referencia](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference)).

**¿Tienes poco tiempo?**

- [Feature comparison: Microsoft Sentinel analytics rules and Microsoft Defender custom detections](https://learn.microsoft.com/en-us/azure/sentinel/compare-analytics-rules-custom-detections) · Documentación
- [Custom detections are now the unified experience for creating detections in Microsoft Defender](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875) · Blog oficial
- [Adopting Unified Custom Detections in Microsoft Sentinel via the Defender Portal (webinar)](https://www.youtube.com/watch?v=ZB15mfUk_rU) · Webinar

### Documentación, cursos y credenciales

- [Feature comparison: Microsoft Sentinel analytics rules and Microsoft Defender custom detections](https://learn.microsoft.com/en-us/azure/sentinel/compare-analytics-rules-custom-detections) · Documentación · Oficial · Nuevo · Microsoft Learn · 4 oct 2026. Tabla de paridad entre reglas de análisis de Sentinel y detecciones personalizadas de Defender (MITRE, agrupación, NRT streaming, automatización, salud/auditoría, CI/CD) con capacidades 'planned'.
- [Microsoft Defender XDR integration with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-365-defender-sentinel-integration) · Documentación · Oficial · Microsoft Learn. Explica cómo SIEM (Sentinel) y XDR (Defender) se integran: cola de incidentes única, sincronización bidireccional, correlación y recolección de eventos de hunting avanzado.
- [Threat detection in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/threat-detection) · Documentación · Oficial · Microsoft Learn. Tipos de reglas de análisis (programadas, NRT, anomalías, seguridad de Microsoft, TI, Fusion, ML) y la recomendación de partir de plantillas del Content hub.
- [Alert correlation and incident merging in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/alerts-incidents-correlation) · Documentación · Oficial · Microsoft Learn. Describe la lógica de correlación de alertas y fusión de incidentes del portal de Defender, el papel del espacio de trabajo principal frente a los secundarios y las 'correlaciones recomendadas'.
- [SOC optimization reference (SOC optimization recommendation types)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference) · Documentación · Oficial · Microsoft Learn. Referencia de tipos de recomendaciones de optimización del SOC: valor de datos, cobertura basada en amenazas, etiquetado MITRE con IA (preview), basadas en riesgo (preview) y organizaciones similares.
- [Create custom detection rules in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-rules) · Documentación · Oficial · Microsoft Learn. Guía para crear detecciones personalizadas desde advanced hunting o la lista de reglas: permisos (Defender y Sentinel Contributor), detalles de alerta, enriquecimiento, acciones de respuesta y alcance.
- [Map data fields to entities in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/map-data-fields-to-entities) · Documentación · Oficial · Microsoft Learn. Procedimiento y límites del mapeo de entidades en reglas programadas: hasta 10 mapeos, 3 identificadores por entidad, 500 entidades por alerta y 64 KB.
- [Creación de detecciones y realización de investigaciones mediante Microsoft Sentinel (ruta de aprendizaje SC-200)](https://learn.microsoft.com/es-es/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/) · Curso · Oficial · ES · Microsoft Learn. Ruta oficial en español de ~6,5 h con 8 módulos: analítica, automatización, playbooks, incidentes, UEBA, ASIM, workbooks y gestión de contenido, con ejercicios.
- [View MITRE ATT&CK framework coverage in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/mitre-coverage) · Documentación · Oficial · Vista previa · Microsoft Learn. Uso de la matriz MITRE ATT&CK de Sentinel para ver detecciones activas, simular cobertura con plantillas disponibles y filtrar por escenario de amenaza. *Nota:* La página MITRE sigue en preview; alineada a ATT&CK v18 según la versión actual del documento
- [Automatically create incidents from Microsoft security alerts](https://learn.microsoft.com/en-us/azure/sentinel/create-incidents-from-alerts) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Cómo crear incidentes desde alertas de productos de seguridad de Microsoft con reglas 'Microsoft security' y aclara que no aplica si se usa la integración de Defender XDR o el portal de Defender. *Nota:* En el portal de Defender las reglas de creación de incidentes de Microsoft no aplican: la correlación de Defender XDR crea los incidentes; reemplazar las de productos no integrados (p. ej. Purview IRM) por reglas programadas
- [Microsoft Sentinel built-in SOC-machine learning anomalies](https://learn.microsoft.com/en-us/azure/sentinel/soc-ml-anomalies) · Documentación · Oficial · Nuevo · Ninja original · Microsoft Learn · 14 may 2026. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: doc «Microsoft Sentinel built-in SOC-machine learning anomalies».
- [Quick threat detection with near-real-time (NRT) analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/near-real-time-rules) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Concepto de reglas NRT: ejecución cada minuto sobre tiempo de ingesta con retraso de 2 minutos, límite de 50 reglas y fuentes con latencia menor a 12 horas.
- [Detect threats with built-in analytics rules](https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: doc «Built-in rule templates».
- [Create custom analytics rules to detect threats](https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: doc «Create custom analytics rules to detect threats».
- [Work with near-real-time (NRT) detection analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/create-nrt-rules) · Documentación · Oficial · Microsoft Learn. Procedimiento para ver y crear reglas NRT en los portales Defender y Azure, y qué opciones del asistente no aplican (programación fija de 1 minuto, umbral, agrupación limitada a 30 alertas).
- [Manage existing custom detection rules](https://learn.microsoft.com/en-us/defender-xdr/custom-detection-manage) · Documentación · Oficial · Microsoft Learn. Cómo ver, editar, ejecutar, activar/desactivar y eliminar detecciones personalizadas y analytics rules en la vista unificada, e incluirlas o excluirlas de la correlación.
- [Work with anomaly detection analytics rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/work-with-anomaly-rules) · Documentación · Oficial · Microsoft Learn. Cómo ver plantillas de anomalías, evaluar su calidad en la tabla Anomalies y ajustarlas duplicando reglas en modo Flighting antes de producción.
- [Advanced, multi-stage attack detections (Fusion)](https://learn.microsoft.com/en-us/azure/sentinel/fusion) · Documentación · Oficial · Legado aún útil · Ninja original · Microsoft Learn. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: doc «Advanced, multi-stage attack detections (Fusion)». *Nota:* Fusion queda superado por la correlación de Defender XDR al usar el portal de Defender
- [Configure multistage attack detection (Fusion) rules in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/configure-fusion-rules) · Documentación · Oficial · Legado aún útil · Microsoft Learn. Cómo habilitar, configurar señales de origen y excluir patrones en la regla Fusion del portal de Azure. *Nota:* Útil solo para entornos aún en portal de Azure (soporte hasta 31-mar-2027)

### Anuncios y blogs oficiales

- [Detection and automation, reimagined (Part 3 of 6 - The USX Transition Series)](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/detection-and-automation-reimagined/4527933) · Blog oficial · Empleado de Microsoft · Nuevo · Mohit Kumar (con Lizet Pena, Caroline Mutua, Alvin Kua, Marco Sudahl) · Microsoft Sentinel Blog (Tech Community) · 18 jun 2026. Explica cómo evolucionan reglas, playbooks, workbooks, hunting y gestión de casos al pasar al portal de Defender, incluida la convergencia analytics rules/custom detections y el retiro de Fusion.
- [Custom detections are now the unified experience for creating detections in Microsoft Defender](https://techcommunity.microsoft.com/t5/microsoft-defender-xdr-blog/custom-detections-are-now-the-unified-experience-for-creating/ba-p/4463875) · Blog oficial · Empleado de Microsoft · Noa Nutkevitch, Jeremy Tan · Microsoft Defender XDR Blog (Tech Community) · 28 oct 2025. Anuncio de que las detecciones personalizadas son la experiencia unificada para crear reglas sobre datos de Defender XDR y Sentinel, con FAQ sobre el futuro de las analytics rules.
- [Using lists and the "in" operator](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/azure-sentinel-correlation-rules-active-lists-out-make-list-in/ba-p/1029225) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: blog-oficial «Using lists and the "in" operator».
- [Using the "join" operator](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/azure-sentinel-correlation-rules-the-join-kql-operator/ba-p/1041500) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: blog-oficial «Using the "join" operator».
- [Advanced pattern handling sliding windows](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/handling-sliding-windows-in-azure-sentinel-rules/ba-p/1505394) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: blog-oficial «Advanced pattern handling sliding windows».
- [Blob and File storage investigations](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/microsoft-ignite-2021-blob-and-file-storage-investigations/ba-p/2175138) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 11 ('Analítica') del skill-up de Learn: blog-oficial «Blob and File storage investigations».

### Webinars, videos y podcasts

- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar · Oficial · Jeremy Tan, Maria de Sousa-Valadas Castano · YouTube – Microsoft Security Community · 16 dic 2025. Segunda parte de la transición a Defender: onboarding, modelos de permisos, conectores, data lake, SOC optimization, custom detections unificadas y multi-workspace/multi-tenant.
- [Adopting Unified Custom Detections in Microsoft Sentinel via the Defender Portal (webinar)](https://www.youtube.com/watch?v=ZB15mfUk_rU) · Webinar · Empleado de Microsoft · Noa Nutkevitch, Jeremy Tan · Microsoft Security Community (YouTube) · 5 nov 2025. Webinar sobre la visión, beneficios, cronología de unificación y mejoras recientes de las detecciones personalizadas, con demo y comparación frente a analytics rules.
- [Fusion machine learning detections with scheduled analytics rules](https://www.youtube.com/watch?v=Ee7gBAQ2Dzc) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube. Material enlazado en el Módulo 11 ('Analítica') del skill-up de Learn: webinar «Fusion machine learning detections with scheduled analytics rules» ofrecido en YouTube, MP4, presentation.
- [Fusion machine learning detections for emerging threats and configuration UI](https://www.youtube.com/watch?v=bTDp41yMGdk) · Webinar · Oficial · Legado aún útil · Ninja original · YouTube. Material enlazado en el Módulo 11 ('Analítica') del skill-up de Learn: webinar «Fusion machine learning detections for emerging threats and configuration UI» ofrecido en YouTube, presentation.

### Laboratorios, GitHub y herramientas

- [FalconForceTeam/FalconFriday](https://github.com/FalconForceTeam/FalconFriday) · GitHub · Comunidad · FalconForce (Olaf Hartong y equipo) · FalconForce (GitHub). Consultas de hunting/detección mapeadas a MITRE ATT&CK, cada una documentada con razonamiento, precisión esperada y trade-offs de falsos positivos.
- [FalconForceTeam repositories (KQLAnalyzer, NRT-KQL, TelemetryCollectionManager)](https://github.com/orgs/FalconForceTeam/repositories) · Herramienta · Comunidad · FalconForce · FalconForce (GitHub). Herramientas de ingeniería de detección: KQLAnalyzer (valida KQL contra esquemas de Sentinel/Defender) y documentación propia de sintaxis válida para reglas NRT.
- [AzSentinelQueries](https://github.com/f-bader/AzSentinelQueries) · GitHub · MVP · Fabian Bader · GitHub. Reglas analíticas y consultas de caza para Sentinel publicadas por un MVP especializado en identidad y detección.

### Comunidad: blogs, libros, newsletters y eventos

- [(DxBP) Part 1 - Technical Detection Engineering Best Practices](https://kqlquery.com/posts/dxbp-part1/) · Blog · MVP · Bert-Jan Pals · kqlquery.com · 23 feb 2026. Buenas prácticas técnicas de ingeniería de detección: medir la latencia de ingesta con percentiles, idiomas de logs, identificadores únicos, sensibilidad a mayúsculas, joins y entidades fuertes.

**Manos a la obra**

1. `Laboratorio` Desde una plantilla del Content hub, crea una regla programada con mapeo de entidades y detalles personalizados.
2. `Laboratorio` Recrea la misma lógica como detección personalizada con una acción de respuesta y compárala con la [tabla de paridad](https://learn.microsoft.com/en-us/azure/sentinel/compare-analytics-rules-custom-detections).
3. `Laboratorio` Escribe una regla NRT para un evento crítico, como el alta de un usuario en un grupo privilegiado.
4. `Laboratorio parcial` Revisa las recomendaciones de [optimización del SOC](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) e implementa una de cada tipo.
5. `Laboratorio parcial` Ajusta una regla ruidosa con una watchlist de excepciones y mide la reducción de falsos positivos.

**¿Quieres profundizar?**

- [(DxBP) Part 1 - Technical Detection Engineering Best Practices](https://kqlquery.com/posts/dxbp-part1/) · Blog
- [Part 2: Don’t Get Left Behind: Complete Your Sentinel Move to Defender](https://www.youtube.com/watch?v=0GAxsbzGirw) · Webinar
- [FalconForceTeam/FalconFriday](https://github.com/FalconForceTeam/FalconFriday) · GitHub

<a id="m8"></a>

## M8 · Workbooks, reportes y visualización

*L300 · ~4 h · Origen: Módulo 13 · Workbooks, reporting, and visualization*

Como centro nervioso del SOC, Sentinel debe mostrar lo que recoge y produce. Los **workbooks** son la herramienta nativa para tableros interactivos y, bien diseñados, funcionan como pequeñas aplicaciones de investigación: parámetros, pestañas, consultas a APIs y acciones. Existen decenas de plantillas en el Content hub que conviene conocer y adaptar.

Para reportes ejecutivos, distribución programada o tablas dinámicas, **Power BI** se conecta a los datos de Sentinel; y el portal de Defender suma sus propios informes y paneles. Este módulo cubre cómo construir y adaptar libros y cómo elegir la herramienta de visualización adecuada para cada audiencia.

**Qué vas a lograr**

- Crear y personalizar workbooks con parámetros, pestañas y visualizaciones.
- Elegir entre workbooks, Power BI y los informes del portal de Defender.
- Reutilizar plantillas del Content hub y del repositorio de GitHub.

> **Atención.** En el portal de Defender algunas visualizaciones de libros requieren «Abrir en Azure» y los libros muestran solo los datos del workspace principal ([visualizar datos](https://learn.microsoft.com/en-us/azure/sentinel/monitor-your-data)).

> **Novedad.** El portal de Defender incluye el informe nativo «Unified security summary» con 90 días por defecto y exportación a PDF o CSV ([informe](https://learn.microsoft.com/en-us/defender-xdr/security-summary-report)); para audiencias sin acceso a Sentinel, exporta la consulta a Power BI ([Power BI](https://learn.microsoft.com/en-us/azure/sentinel/powerbi)).

**¿Tienes poco tiempo?**

- [Create a Power BI report from Microsoft Sentinel data](https://learn.microsoft.com/en-us/azure/sentinel/powerbi) · Documentación

### Documentación, cursos y credenciales

- [Create a Power BI report from Microsoft Sentinel data](https://learn.microsoft.com/en-us/azure/sentinel/powerbi) · Documentación · Oficial · Microsoft Learn. Escenario paso a paso: exportar una consulta KQL a M, construir el informe en Power BI Desktop, publicarlo, compartirlo en Teams y programar su actualización.
- [Libros de Microsoft Sentinel de uso común](https://learn.microsoft.com/es-es/azure/sentinel/top-workbooks) · Documentación · Oficial · ES · Microsoft Learn. Lista en español de los workbooks más usados (Analytics Health & Audit, Data collection health monitoring, Incident Overview, Investigation Insights, MITRE ATT&CK, CMMC, Entra ID) y la solución del Content hub que los contiene.
- [Microsoft Defender XDR in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender-portal) · Documentación · Oficial · Microsoft Learn. Describe el portal de Defender (security.microsoft.com) que reúne incidentes, hunting, acciones y análisis de amenazas, y reitera que Sentinel funciona allí con o sin Defender XDR o E5 y que tras el 31-mar-2027 solo estará disponible en ese portal.
- [Highlight security impact and achievements with the unified security summary](https://learn.microsoft.com/en-us/defender-xdr/security-summary-report) · Documentación · Oficial · Microsoft Learn. Informe 'Unified security summary' del portal de Defender (Reports > General) con postura, detección, protección, investigación y uso de Copilot, exportable a PDF/CSV.
- [Azure Workbooks documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: doc «Azure Workbooks documentation».
- [Integrates with Azure Monitor Logs and Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-powerbi) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: doc «Integrates with Azure Monitor Logs and Microsoft Sentinel».
- [Azure Monitor Logs and Microsoft Sentinel as the data source](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-excel) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: doc «Azure Monitor Logs and Microsoft Sentinel as the data source».

### Anuncios y blogs oficiales

- [Investigation Insights Workbook](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/announcing-the-investigation-insights-workbook/ba-p/1816903) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Investigation Insights Workbook».
- [Graph visualization of external Teams collaborations](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/graph-visualization-of-external-teams-collaborations-in-azure/ba-p/1356847) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Graph visualization of external Teams collaborations».
- [Users' travel map workbook](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/how-to-use-azure-sentinel-to-follow-a-users-travel-and-map-their/ba-p/981716) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Users' travel map workbook».
- [Microsoft Sentinel insecure protocols workbook implementation guide](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/azure-sentinel-insecure-protocols-workbook-implementation-guide/ba-p/1197564) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Microsoft Sentinel insecure protocols workbook implementation guide».
- [Azure Sentinel insecure protocols workbook reimagined](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/azure-sentinel-insecure-protocols-workbook-reimagined/ba-p/1558375) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Recent enhancements».
- [Integrate information from any source by using API calls in a workbook](https://techcommunity.microsoft.com/t5/azure-sentinel/using-the-sentinel-api-to-view-data-in-a-workbook/ba-p/1386436) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-oficial «Integrate information from any source by using API calls in a workbook».

### Laboratorios, GitHub y herramientas

- [Workbooks folder (Azure-Sentinel on GitHub)](https://github.com/Azure/Azure-Sentinel/tree/master/Workbooks) · GitHub · Oficial · Legado aún útil · Ninja original · GitHub. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: github «_ Workbooks_ folder».

### Comunidad: blogs, libros, newsletters y eventos

- [Azure Advent Calendar: Azure Monitor workbooks (companion article)](https://www.cloudsma.com/2019/12/azure-advent-calendar-azure-monitor-workbooks/) · Blog · Comunidad · Legado aún útil · Ninja original · cloudsma.com. Enlace del Módulo 13 ('Workbooks, reportes y visualización') del skill-up de Learn: blog-comunidad «Accompanying text».

**Manos a la obra**

1. `Laboratorio` Instala un libro del Content hub y personalízalo con parámetros y pestañas.
2. `Laboratorio` Construye un libro de eficiencia del SOC con métricas de `SecurityIncident`.
3. `Laboratorio` Exporta una consulta a [Power BI](https://learn.microsoft.com/en-us/azure/sentinel/powerbi) y publícala para una audiencia ejecutiva.

<a id="m9"></a>

## M9 · Incidentes e investigación

*L300 · ~6 h · Origen: Módulo 16 · Handling incidents*

Construido el SOC, toca usarlo. Un incidente agrupa alertas, entidades y evidencia relacionadas; tu trabajo es **clasificarlo, investigarlo y responder**. En el portal de Defender los incidentes de Sentinel y de Defender XDR conviven en una sola cola, con historia del ataque, gráfico de incidente, páginas de entidad, tareas, comentarios, acciones de respuesta y, en escenarios compatibles, interrupción automática de ataques.

Este módulo recorre un día en la vida de un analista: priorizar la cola, investigar con el gráfico y las páginas de entidad, documentar con tareas y comentarios, coordinar con el equipo y cerrar con la clasificación correcta. También verás cómo medir la eficiencia del SOC con métricas de incidentes.

**Qué vas a lograr**

- Gestionar la cola de incidentes unificada del portal de Defender.
- Investigar con el gráfico de incidente, las páginas de entidad y la línea de tiempo.
- Documentar con tareas y comentarios y cerrar con clasificaciones precisas.
- Medir la eficiencia del SOC con métricas de incidentes.

> **Novedad.** Los **incident cases** (vista previa) son la experiencia recomendada para gestionar incidentes en Defender: tareas, SLA, campos personalizados, adjuntos, auditoría en la tabla SecurityCaseEvent y sesiones agénticas. Solo existen en el portal de Defender y la experiencia clásica sigue disponible ([gestión de casos](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management)).

> **Consejo Ninja.** En la tabla `SecurityIncident` cada actualización genera un registro nuevo: deduplica con `arg_max()` antes de calcular métricas como MTTR ([métricas del SOC](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics)).

> **Novedad.** La interrupción automática de ataques actúa con 99 % o más de confianza (contener dispositivos o IP, deshabilitar usuarios) y ya cubre escenarios de Okta y AWS en vista previa con un workspace de Sentinel conectado ([interrupción automática](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption)).

> **Atención.** La integración de incidentes con Microsoft Teams sigue en vista previa y solo existe en el portal de Azure ([colaborar en Teams](https://learn.microsoft.com/en-us/azure/sentinel/collaborate-in-microsoft-teams)).

**¿Tienes poco tiempo?**

- [Manage incidents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/manage-incidents) · Documentación
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar

### Documentación, cursos y credenciales

- [Manage incidents in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/manage-incidents) · Documentación · Oficial · Microsoft Learn. Tareas del ciclo de vida del incidente en el portal de Defender: asignar, severidad, etiquetas, estado, resolver, clasificar, comentar, resumir y exportar a PDF.
- [Plan an incident response workflow in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/plan-incident-response) · Documentación · Oficial · Microsoft Learn. Flujo de respuesta (triage, investigación, contención, recuperación, cierre, revisión) con guía por nivel de experiencia y rol (Tier 1/2/3).
- [Case management in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 23 sep 2026. Explica la gestión de casos nativa del portal de Defender (casos de incidente en preview y casos genéricos), con tareas, comentarios, adjuntos, plantillas, SLA y auditoría en la tabla SecurityCaseEvent. *Nota:* Los 'incident cases' son la experiencia recomendada para incidentes (preview); la experiencia clásica sigue disponible. Solo en el portal de Defender
- [Manage incident cases in the Microsoft Defender portal (preview)](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-cases) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo asignar, cambiar severidad/estado, campos personalizados, etiquetas, clasificación/determinación, comentarios, tareas, sesiones agénticas y fusión en casos de incidente. *Nota:* Incluye 'agentic sessions' dentro del caso de incidente
- [Automatic attack disruption in Microsoft Defender](https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption) · Documentación · Oficial · Microsoft Learn. Explica cómo Defender correlaciona señales para contener automáticamente activos comprometidos (contener dispositivo/IP, deshabilitar usuario) con confianza ≥99% y cómo revertir acciones.
- [Manage incident case tasks in the Microsoft Defender portal (preview)](https://learn.microsoft.com/en-us/defender-xdr/manage-incident-case-tasks) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · 23 sep 2026. Uso de tareas en casos de incidente para dividir el trabajo de respuesta, asignar responsables, fechas y notas de cierre. *Nota:* Sustituye funcionalmente a las 'incident tasks' de Sentinel en el nuevo modelo de casos
- [Configure automatic attack disruption in Microsoft Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/configure-attack-disruption) · Documentación · Oficial · Microsoft Learn. Prerrequisitos de licencias, permisos y despliegue para la disrupción automática, incluido el aislamiento automático de dispositivos (preview) y exclusiones.

### Anuncios y blogs oficiales

- [Welcome to the Microsoft Incident Response Ninja Hub](https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/welcome-to-the-microsoft-incident-response-ninja-hub/4243594) · Blog oficial · Oficial · Ninja original · Microsoft Tech Community – Microsoft Security Experts Blog. Hub Ninja del equipo de Microsoft Incident Response con guías, playbooks, casos reales y consejos de hunting. *Nota:* ID 4243594 sugiere 2024. Mapa: -> M9/M10
- [Create Tasks Repository in Microsoft Sentinel](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/create-tasks-repository-in-microsoft-sentinel/4038563) · Blog oficial · Empleado de Microsoft · Legado aún útil · Benjamin Kovacevic · Microsoft Tech Community. Explica cómo crear un repositorio de tareas de incidentes con una watchlist y un playbook para estandarizar la respuesta en Sentinel. *Nota:* Herramienta asociada en Azure-Sentinel/Tools/Tasks-Repository; validar en el portal Defender
- [Why use Jupyter for security investigations?](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/why-use-jupyter-for-security-investigations/ba-p/475729) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: blog-oficial «Why use Jupyter for security investigations?».
- [Security investigation with Azure Sentinel and Jupyter notebooks, part 1](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/security-investigation-with-azure-sentinel-and-jupyter-notebooks/ba-p/432921) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: blog-oficial «Part 1».
- [Security investigation with Azure Sentinel and Jupyter notebooks, part 2](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/security-investigation-with-azure-sentinel-and-jupyter-notebooks/ba-p/483466) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: blog-oficial «Part 2».
- [Security investigation with Azure Sentinel and Jupyter notebooks, part 3](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/security-investigation-with-azure-sentinel-and-jupyter-notebooks/ba-p/561413) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 16 ('Gestión e investigación de incidentes') del skill-up de Learn: blog-oficial «Part 3».

### Webinars, videos y podcasts

- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar · Oficial · Neelam Nursee, Naomi Christis · YouTube – Microsoft Security Community · 9 dic 2025. Recorrido de un día en el SOC dentro del portal de Defender: navegación, cola unificada de incidentes, UEBA, TI, watchlists, automatización y case management.
- [Transition to the Unified SOC Platform: Deep Dive and Interactive Q&A for SOC Professionals](https://www.youtube.com/watch?v=WIM6fbJDkK4) · Webinar · Empleado de Microsoft · Chi Nguyen, Naomi Christis · Microsoft Security Community (YouTube) · 1 abr 2025. Sesión práctica sobre incidentes, correlación, automatización y advanced hunting al pasar de Sentinel en Azure al portal unificado de Defender.

**Manos a la obra**

1. `Laboratorio` Abre un incident case, agrega tareas mediante una regla de automatización, clasifica y cierra; luego verifica el evento en `SecurityCaseEvent` ([gestión de casos](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-case-management)).
2. `Laboratorio` Investiga un incidente del laboratorio con el gráfico y las páginas de entidad, y documenta la línea de tiempo.
3. `Laboratorio parcial` Calcula MTTT y MTTR por severidad con `SecurityIncident` y `arg_max()` ([métricas](https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics)).

**¿Quieres profundizar?**

- [Transition to the Unified SOC Platform: Deep Dive and Interactive Q&A for SOC Professionals](https://www.youtube.com/watch?v=WIM6fbJDkK4) · Webinar

<a id="m10"></a>

## M10 · Hunting: búsqueda proactiva de amenazas

*L300 · ~8 h · Origen: Módulo 17 · Hunting*

Mientras la detección reacciona a alertas, el hunting sale a buscar lo que nadie detectó: es una **búsqueda proactiva** guiada por hipótesis. Sentinel ofrece cientos de consultas de búsqueda mapeadas a tácticas de MITRE ATT&CK, marcadores para conservar evidencia, campañas de búsqueda (hunts) para organizar el trabajo del equipo y la **búsqueda avanzada** del portal de Defender para consultar datos de SIEM y XDR en un mismo lugar.

Pero el hunting es, ante todo, un método: formular una hipótesis, reunir datos, analizarlos, documentar hallazgos y **convertirlos en detecciones**. Este módulo combina herramientas y metodología, con repositorios de consultas de Microsoft y de la comunidad para acelerar el trabajo.

**Qué vas a lograr**

- Planificar y ejecutar una búsqueda basada en hipótesis.
- Usar consultas de búsqueda, marcadores y hunts para organizar el trabajo.
- Consultar datos de Sentinel y Defender XDR desde la búsqueda avanzada.
- Convertir hallazgos de hunting en reglas de detección.

> **Novedad.** Los **hunts** (campañas de búsqueda basadas en hipótesis) funcionan en Defender y en Azure, con marcadores, comentarios y métricas, y permiten crear reglas, incidentes o indicadores ([hunts](https://learn.microsoft.com/en-us/azure/sentinel/hunts)).

> **Atención.** Livestream ya no está disponible: usa KQL jobs, reglas o playbooks ([hunting](https://learn.microsoft.com/en-us/azure/sentinel/hunting)). Los marcadores solo se crean en el portal de Azure; Defender los muestra pero no permite crearlos ([marcadores](https://learn.microsoft.com/en-us/azure/sentinel/bookmarks)).

> **Consejo Ninja.** La búsqueda avanzada unificada requiere como mínimo Microsoft Sentinel Reader; con el data lake incorporado, las tablas Auxiliary se consultan desde la exploración del lago ([búsqueda avanzada en Defender](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender)).

**¿Tienes poco tiempo?**

- [Conduct end-to-end proactive threat hunting in Microsoft Sentinel (Hunts)](https://learn.microsoft.com/en-us/azure/sentinel/hunts) · Documentación
- [Perform threat hunting in Microsoft Sentinel (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) · Curso
- [Bert-JanP/Hunting-Queries-Detection-Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) · GitHub

### Documentación, cursos y credenciales

- [Conduct end-to-end proactive threat hunting in Microsoft Sentinel (Hunts)](https://learn.microsoft.com/en-us/azure/sentinel/hunts) · Documentación · Oficial · Microsoft Learn. Guía para crear 'hunts' basados en hipótesis, ejecutar consultas, guardar marcadores, comentar, crear incidentes/reglas y medir resultados.
- [Perform threat hunting in Microsoft Sentinel (SC-200 learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-perform-threat-hunting-azure-sentinel/) · Curso · Oficial · Microsoft Learn. Ruta de ~2 h 14 min con 4 módulos: conceptos de hunting e hipótesis, consultas, marcadores y hunts, search jobs y notebooks.
- [Keep track of data during hunting with Microsoft Sentinel (bookmarks)](https://learn.microsoft.com/en-us/azure/sentinel/bookmarks) · Documentación · Oficial · Microsoft Learn. Cómo crear, mapear a MITRE/entidades y gestionar marcadores de hunting y llevarlos a incidentes o al gráfico de investigación.

### Anuncios y blogs oficiales

- [SolarWinds post-compromise hunting with Microsoft Sentinel](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/solarwinds-post-compromise-hunting-with-azure-sentinel/ba-p/1995095) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 17 ('Hunting') del skill-up de Learn: blog-oficial «SolarWinds post-compromise hunting with Microsoft Sentinel».
- [Web shell threat hunting with Azure Sentinel](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/web-shell-threat-hunting-with-azure-sentinel/ba-p/2234968) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 17 ('Hunting') del skill-up de Learn: blog-oficial «WebShell hunting».

### Webinars, videos y podcasts

- [Empowering the Modern SOC (Microsoft Sentinel and Microsoft Defender XDR)](https://www.youtube.com/watch?v=bSFcBfHmr1o) · Webinar · Empleado de Microsoft · Benji Kovacevic, Javier Soriano · Microsoft Security Community (YouTube) · 2 dic 2025. Panorama de la experiencia unificada SIEM+XDR para detectar, responder y cazar, con demos del data lake y del grafo de Sentinel y agentes de Security Copilot.
- [Microsoft Sentinel platform – Unified, Graph-enabled, and AI-ready Security (Microsoft Mechanics)](https://www.youtube.com/watch?v=0nNsOrKYxdM) · Video · Empleado de Microsoft · Vandana Mahtani · Microsoft Mechanics (YouTube) · nov 2025. Demo de blast radius, investigación con el servidor MCP de Sentinel, advanced hunting y grafos personalizados en la plataforma Sentinel.
- [Microsoft Secure 2023 Ep01: Threat hunting with Microsoft Sentinel (Learn Live)](https://learn.microsoft.com/en-us/shows/learn-live/microsoft-secure-2023-ep01-threat-hunting-with-microsoft-sentinel) · Video · Empleado de Microsoft · Legado aún útil · Rod Trent, Javier Soriano, Ken Lawson, Benjamin Kovacevic · Microsoft Learn Shows · 28 mar 2023. Sesión Learn Live con demos de consultas de hunting, marcadores y livestream en Sentinel. *Nota:* Grabado en el portal de Azure; livestream ya retirado y hunting ahora en el portal de Defender/Advanced hunting

### Laboratorios, GitHub y herramientas

- [KQL Search - Search engine for KQL Queries](https://www.kqlsearch.com/) · Herramienta · Comunidad · Nuevo · Ugur Koc y comunidad · kqlsearch.com · nov 2026. Buscador comunitario de consultas KQL para Sentinel, Defender y Azure Monitor, filtrable por tabla y autor, con aportes actualizados de la comunidad.
- [Bert-JanP/Hunting-Queries-Detection-Rules](https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Bert-Jan Pals · GitHub (comunidad) · oct 2026. Repositorio muy activo con cientos de consultas KQL de detección, hunting, DFIR, data lake/jobs y operaciones SOC para Defender XDR y Sentinel, organizado por producto y MITRE.
- [reprise99/Sentinel-Queries](https://github.com/reprise99/Sentinel-Queries) · GitHub · Empleado de Microsoft · Legado aún útil · Matt Zorich · GitHub (comunidad) · ene 2026. Colección clásica de consultas KQL para Sentinel con un README que enseña la anatomía de una consulta y fundamentos (tiempo, where, summarize, parse/split). *Nota:* Mayormente sin cambios desde hace años (algunas actualizaciones recientes); el autor fue MVP y hoy trabaja en Microsoft (GHOST)
- [alexverboon/Hunting-Queries-Detection-Rules](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub · MVP · Nuevo · Alex Verboon · GitHub (comunidad) · nov 2026. Repositorio de consultas KQL de hunting, detección y auditoría para Defender, Entra, Copilot/Power Platform, LAPS y Sentinel, con plantilla v2 y metadatos de estado.
- [Threat-Hunting-KQL-Queries (Sergio Albea)](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · GitHub · MVP · Nuevo · Sergio Albea · GitHub · nov 2026. Repositorio de consultas KQL de caza para Defender XDR (correo, identidades, vulnerabilidades) de un MVP de origen español.
- [SlimKQL/Hunting-Queries-Detection-Rules (KQLWizard)](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules) · GitHub · MVP · Steven Lim · GitHub (comunidad). Repositorio de detecciones y hunting KQL para Defender XDR, Sentinel y ADX con actualizaciones muy frecuentes sobre amenazas y CVE recientes.
- [FalconFriday](https://github.com/FalconForceTeam/FalconFriday/blob/main/README.md) · GitHub · MVP · Legado aún útil · FalconForce (Olaf Hartong y equipo) · GitHub - FalconForceTeam. Consultas de caza para Microsoft Defender for Endpoint mapeadas a MITRE ATT&CK para técnicas avanzadas (inyección de procesos, LOLBins, AD CS, AWS). *Nota:* Fecha del último commit no visible; ~880 estrellas; las consultas requieren ajuste al entorno
- [jkerai1/KQL-Queries](https://github.com/jkerai1/KQL-Queries) · GitHub · Comunidad · Jay Kerai · GitHub (comunidad). Consultas KQL prácticas para Defender, Entra, Azure y Office 365 (TVM, dominios de riesgo, RMM, IOC vía externaldata) publicadas también en kqlsearch.com.
- [Threat-Hunting-and-Detection (Cyb3r-Monk)](https://github.com/Cyb3r-Monk/Threat-Hunting-and-Detection) · GitHub · MVP · Mehmet Ergene · GitHub. Consultas KQL avanzadas de caza y detección para Defender XDR y Sentinel.

**Manos a la obra**

1. `Laboratorio` Desde la página de MITRE, elige una técnica sin cobertura y crea un [hunt](https://learn.microsoft.com/en-us/azure/sentinel/hunts) con consultas del Content hub.
2. `Laboratorio` Documenta hallazgos y evidencia, y conviértelos en una regla y un incidente.
3. `Laboratorio` Repite una búsqueda en la búsqueda avanzada combinando una tabla de Sentinel con una de Defender XDR.

**¿Quieres profundizar?**

- [reprise99/Sentinel-Queries](https://github.com/reprise99/Sentinel-Queries) · GitHub
- [alexverboon/Hunting-Queries-Detection-Rules](https://github.com/alexverboon/Hunting-Queries-Detection-Rules) · GitHub
- [Threat-Hunting-KQL-Queries (Sergio Albea)](https://github.com/Sergio-Albea-Git/Threat-Hunting-KQL-Queries) · GitHub
- [SlimKQL/Hunting-Queries-Detection-Rules (KQLWizard)](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules) · GitHub

<a id="m11"></a>

## M11 · UEBA: análisis de comportamiento de usuarios y entidades

*L300 · ~4 h · Origen: Módulo 18 · User and Entity Behavior Analytics (UEBA)*

User and Entity Behavior Analytics (UEBA) construye perfiles de comportamiento de usuarios, hosts, direcciones IP y aplicaciones a lo largo del tiempo y frente a sus pares, para detectar lo que una regla estática no ve: un acceso inusual, un volumen atípico, una actividad fuera de patrón. También estima la sensibilidad de los activos y el posible **radio de impacto** de una cuenta comprometida, lo que ayuda a priorizar.

Sus tablas —**BehaviorAnalytics**, **IdentityInfo**, **UserPeerAnalytics** y **Anomalies**— enriquecen investigaciones, reglas y búsquedas. Este módulo cubre cómo habilitar UEBA, qué fuentes analiza, cómo leer sus resultados y cómo incorporarlos a tus detecciones.

**Qué vas a lograr**

- Habilitar UEBA y seleccionar las fuentes de datos analizadas.
- Interpretar las tablas y puntuaciones de UEBA en investigaciones.
- Usar IdentityInfo y BehaviorAnalytics en reglas y búsquedas.

> **Novedad.** La **capa de behaviors de UEBA** usa IA generativa para resumir registros crudos en comportamientos legibles («quién hizo qué a quién») mapeados a MITRE. Requiere el workspace incorporado a Defender, se activa en un solo workspace por tenant, no requiere licencia adicional y la ingesta se factura ([UEBA behaviors](https://learn.microsoft.com/en-us/azure/sentinel/entity-behaviors-layer)).

> **Novedad.** Algunas fuentes nuevas de UEBA (AWS, GCP, Okta, CEF de terceros, inicios de sesión de identidades administradas y entidades de servicio) se activan solo desde Defender; UEBA no tiene costo de licencia, pero su almacenamiento se factura ([habilitar UEBA](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics)).

> **Novedad.** La página de novedades registra la capa de behaviors en disponibilidad general desde febrero de 2026 y nuevas fuentes (FortiGate, Check Point, Zscaler y GuardDuty) en agosto de 2026 ([novedades de Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/whats-new)).

**¿Tienes poco tiempo?**

- [Translate raw security logs to behavioral insights using UEBA behaviors in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/entity-behaviors-layer) · Documentación
- [Introducing the UEBA Behaviors Layer in Microsoft Sentinel](https://www.youtube.com/watch?v=SqbxmGdMP7c) · Webinar

### Documentación, cursos y credenciales

- [Translate raw security logs to behavioral insights using UEBA behaviors in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/entity-behaviors-layer) · Documentación · Oficial · Nuevo · Microsoft Learn · 2 jul 2026. Describe la capa de 'UEBA behaviors' que resume logs crudos en registros 'quién hizo qué a quién' con mapeo MITRE y roles de entidades (tablas SentinelBehaviorInfo/SentinelBehaviorEntities).
- [Enable User and Entity Behavior Analytics (UEBA) in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics) · Documentación · Oficial · Microsoft Learn. Pasos y permisos para activar UEBA desde Configuración > Microsoft Sentinel > UEBA en Defender, elegir directorios y fuentes de datos y activar anomalías.
- [Microsoft Sentinel User and Entity Behavior Analytics (UEBA) reference](https://learn.microsoft.com/en-us/azure/sentinel/ueba-reference) · Documentación · Oficial · Microsoft Learn. Referencia de fuentes de datos de UEBA (Entra ID, AzureActivity, SecurityEvent, AWS, GCP, Okta, CEF, MDE) y de los enriquecimientos que añade a entidades.

### Anuncios y blogs oficiales

- [UEBA for investigations in your SOC](https://techcommunity.microsoft.com/t5/azure-sentinel/guided-ueba-investigation-scenarios-to-empower-your-soc/ba-p/1857100) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 18 ('UEBA') del skill-up de Learn: blog-oficial «UEBA for investigations in your SOC».

### Webinars, videos y podcasts

- [Introducing the UEBA Behaviors Layer in Microsoft Sentinel](https://www.youtube.com/watch?v=SqbxmGdMP7c) · Webinar · Oficial · Michal Shechter, Taylor Wong · YouTube – Microsoft Security Community · 17 feb 2026. Webinar sobre la nueva capa de Behaviors de UEBA que traduce telemetría cruda en comportamientos legibles, con casos de uso y demo.
- [UEBA behaviors boost: Anomalies on top of behaviors layer](https://www.youtube.com/watch?v=73XRo0U6qDQ) · Video · Oficial · Michal Shechter, Dror Cohen · YouTube – Microsoft Security Community. Introduce detección de anomalías sobre la capa de behaviors de UEBA (primera vez visto, patrones poco comunes, coincidencias de TI) para hunting proactivo.

**Manos a la obra**

1. `Laboratorio parcial` Habilita UEBA y selecciona fuentes ([habilitar UEBA](https://learn.microsoft.com/en-us/azure/sentinel/enable-entity-behavior-analytics)); tras unos días, revisa `BehaviorAnalytics` y las páginas de entidad.
2. `Laboratorio parcial` Si tienes AWS CloudTrail o CEF compatibles, activa la capa de behaviors y consulta comportamientos por táctica y técnica.
3. `Laboratorio` Usa `IdentityInfo` en una regla para elevar la severidad cuando la cuenta afectada sea privilegiada.

**¿Quieres profundizar?**

- [UEBA behaviors boost: Anomalies on top of behaviors layer](https://www.youtube.com/watch?v=73XRo0U6qDQ) · Video

<a id="m12"></a>

## M12 · Salud, auditoría y optimización del SOC

*L300 · ~4 h · Origen: Módulo 19 · Monitoring Microsoft Sentinel's health*

Operar un SIEM incluye asegurarse de que funciona. ¿Llegan los datos de cada conector? ¿Se ejecutan las reglas y los playbooks? ¿Quién cambió qué y cuándo? Las tablas **SentinelHealth** y **SentinelAudit** responden esas preguntas y permiten alertar sobre fallas; la tabla **Heartbeat** y los libros de uso del workspace muestran la salud de agentes e ingesta.

La **optimización del SOC** agrega una mirada proactiva: recomienda cómo aprovechar mejor los datos que ya pagas, qué reglas activar y dónde hay brechas frente a amenazas concretas. Este módulo convierte la operación en un proceso medible y auditable.

**Qué vas a lograr**

- Habilitar y consultar la supervisión de salud y auditoría de Sentinel.
- Crear alertas sobre fallas de conectores, reglas y automatización.
- Aplicar las recomendaciones de optimización del SOC.

> **Consejo Ninja.** `SentinelHealth` no se factura y `SentinelAudit` sí. Consulta con las funciones `_SentinelHealth()` y `_SentinelAudit()`; la salud cubre conectores, reglas de analítica, reglas de automatización y playbooks, y la auditoría cubre reglas de analítica ([salud y auditoría](https://learn.microsoft.com/en-us/azure/sentinel/health-audit)). En Defender se activa en Sistema > Configuración > Microsoft Sentinel ([habilitar](https://learn.microsoft.com/en-us/azure/sentinel/enable-monitoring)).

> **Atención.** Revisa la [disponibilidad por función](https://learn.microsoft.com/en-us/azure/sentinel/feature-availability): por ejemplo, la salud de reglas de analítica figura en vista previa.

**¿Tienes poco tiempo?**

- [Optimize your security operations (SOC optimization)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) · Documentación

### Documentación, cursos y credenciales

- [Optimize your security operations (SOC optimization)](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access) · Documentación · Oficial · Microsoft Learn. Cómo acceder a la página de optimización del SOC, interpretar sus métricas (datos ingeridos, cobertura de amenazas alta/media/baja) y gestionar recomendaciones.
- [Auditing and health monitoring in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/health-audit) · Documentación · Oficial · Microsoft Learn. Explica las tablas SentinelHealth (no facturable) y SentinelAudit (facturable), las funciones _SentinelHealth()/_SentinelAudit() y las preguntas clave de salud del servicio.
- [Monitor the health and audit the integrity of your analytics rules](https://learn.microsoft.com/en-us/azure/sentinel/monitor-analytics-rule-integrity) · Documentación · Oficial · Microsoft Learn. Consultas de ejemplo sobre SentinelHealth/SentinelAudit para detectar reglas auto-deshabilitadas, fallos y cambios no autorizados en reglas de análisis.
- [Turn on auditing and health monitoring for Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/enable-monitoring) · Documentación · Oficial · Microsoft Learn. Cómo activar auditoría y monitoreo de salud desde Configuración (Defender: Sistema > Configuración > Microsoft Sentinel) y verificar las tablas.
- [Monitor the health of your automation rules and playbooks](https://learn.microsoft.com/en-us/azure/sentinel/monitor-automation-health) · Documentación · Oficial · Microsoft Learn. Uso de SentinelHealth para eventos 'Automation rule run' y 'Playbook was triggered', estados y errores comunes con acciones sugeridas.
- [Microsoft Sentinel feature support for Azure commercial/other clouds](https://learn.microsoft.com/en-us/azure/sentinel/feature-availability) · Documentación · Oficial · Microsoft Learn. Tabla de estado (GA/preview/no disponible) por funcionalidad de Sentinel: analítica, contenido, conectores, hunting, incidentes, ML, ASIM, UEBA, SOC optimization.
- [Microsoft Sentinel audit tables reference](https://learn.microsoft.com/en-us/azure/sentinel/audit-table-reference) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 may 2026. Esquema de la tabla SentinelAudit y propiedades extendidas (estado antes/después, llamante, IP) para auditar cambios en reglas.
- [Heartbeat table reference](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/heartbeat) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 19 ('Monitoreo de salud') del skill-up de Learn: doc «Heartbeat table».

### Anuncios y blogs oficiales

- [Get notifications on anomalies](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/data-connector-health-push-notification-alerts/ba-p/1996442) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 19 ('Monitoreo de salud') del skill-up de Learn: blog-oficial «Get notifications on anomalies».
- [Ingestion Cost Alert Playbook](https://techcommunity.microsoft.com/t5/azure-sentinel/ingestion-cost-alert-playbook/ba-p/2006003) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 19 ('Monitoreo de salud') del skill-up de Learn: blog-oficial «Ingestion Cost Alert Playbook».

### Comunidad: blogs, libros, newsletters y eventos

- [365 by Thijs (blog)](https://365bythijs.be/blog/) · Blog · MVP · Thijs Lecomte · 365bythijs.be. Blog con artículos prácticos sobre salud de Sentinel, CI/CD de contenido, fallos de reglas analíticas y SOAR.

**Manos a la obra**

1. `Laboratorio` Activa salud y auditoría, fuerza el fallo de una regla y consulta `_SentinelHealth()` y `_SentinelAudit()` ([salud y auditoría](https://learn.microsoft.com/en-us/azure/sentinel/health-audit)).
2. `Laboratorio` Crea una regla que alerte cuando alguien elimine o deshabilite una regla de analítica.
3. `Laboratorio parcial` Revisa las recomendaciones de optimización del SOC y el indicador de cobertura por amenaza.

**¿Quieres profundizar?**

- [365 by Thijs (blog)](https://365bythijs.be/blog/) · Blog

<a id="m13"></a>

## M13 · Automatización esencial: reglas de automatización y playbooks

*L300 · ~6 h · Origen: Módulo 12 · Implementing SOAR (primera parte)*

En los SIEM modernos, la automatización (SOAR) cubre todo el proceso desde que se dispara un incidente hasta que se resuelve. Las **reglas de automatización** son el punto de partida: de forma centralizada asignan, etiquetan, cambian severidad o estado, suprimen falsos positivos conocidos y deciden cuándo ejecutar playbooks, tanto al crear como al actualizar incidentes y alertas.

Los **playbooks**, construidos sobre Azure Logic Apps, agregan flujos completos: notificar, enriquecer, abrir tickets o contener una amenaza. Este módulo cubre lo esencial —tipos de disparador, permisos que Sentinel necesita, plantillas y primeros playbooks—; el nivel experto profundiza en patrones avanzados, Logic Apps Standard e integración con IA.

**Qué vas a lograr**

- Crear reglas de automatización con condiciones, acciones y orden de ejecución.
- Desplegar playbooks desde plantillas y asignar los permisos necesarios.
- Ejecutar playbooks automáticamente y bajo demanda sobre incidentes, alertas y entidades.

> **Consejo Ninja.** Las reglas de automatización se disparan al crear o actualizar un incidente y al crear una alerta. En Defender, el disparador de alertas aplica solo a alertas de Sentinel; para alertas de Defender XDR existe un disparador ampliado ([reglas de automatización](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules)).

**¿Tienes poco tiempo?**

- [Automation in Microsoft Sentinel: Security orchestration, automation, and response (SOAR)](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation) · Documentación
- [Automate threat response with automation rules](https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules) · Documentación
- [Authenticate playbooks to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel) · Documentación

### Documentación, cursos y credenciales

- [Create and manage Microsoft Sentinel playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/create-playbooks) · Documentación · Oficial · Nuevo · Microsoft Learn · 14 oct 2026. Procedimiento para crear playbooks Consumption (asistente con identidad administrada por defecto) y Standard (logic app + workflow stateful), usar contenido dinámico, custom details y gestionar la pestaña Active playbooks.
- [Automation in Microsoft Sentinel: Security orchestration, automation, and response (SOAR)](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jun 2026. Visión general de SOAR en Sentinel (reglas de automatización + playbooks) y tabla de diferencias de comportamiento de la automatización tras incorporar el workspace al portal de Defender.
- [Monitor the health of your automation rules and playbooks](https://learn.microsoft.com/en-us/azure/sentinel/monitor-automation-health) · Documentación · Oficial · Microsoft Learn. Uso de SentinelHealth para eventos 'Automation rule run' y 'Playbook was triggered', estados y errores comunes con acciones sugeridas.
- [Create and use Microsoft Sentinel automation rules to manage response](https://learn.microsoft.com/en-us/azure/sentinel/create-manage-use-automation-rules) · Documentación · Oficial · Microsoft Learn. Procedimiento para diseñar y crear reglas de automatización (alcance, disparador, condiciones, acciones, orden y expiración) en Defender y Azure.
- [Automate threat response with playbooks in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/automate-responses-with-playbooks) · Documentación · Oficial · Microsoft Learn. Casos de uso de playbooks (enriquecimiento, sincronización bidireccional, orquestación, respuesta) y roles necesarios para crearlos y ejecutarlos.
- [Automate and run Microsoft Sentinel playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automation/run-playbooks) · Documentación · Oficial · Microsoft Learn. Cómo adjuntar playbooks a reglas de análisis o de automatización, ejecutarlos a demanda y conceder a la cuenta de servicio de Sentinel el rol Automation Contributor, incluido el escenario multitenant/MSSP.
- [Authenticate playbooks to Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel) · Documentación · Oficial · Microsoft Learn. Describe los métodos de autenticación del conector de Sentinel (identidad administrada, service principal, usuario de Entra) y cómo asignar a la identidad del playbook el rol Sentinel Responder o Reader en el workspace.
- [Migrate your Microsoft Sentinel alert-trigger playbooks to automation rules](https://learn.microsoft.com/en-us/azure/sentinel/automation/migrate-playbooks-to-automation-rules) · Documentación · Oficial · Microsoft Learn. Explica por qué y cómo mover playbooks invocados desde reglas de análisis ('Alert automation (classic)') a reglas de automatización con disparador 'When alert is created'.
- [Recommended playbook use cases, templates, and examples](https://learn.microsoft.com/en-us/azure/sentinel/automation/playbook-recommendations) · Documentación · Oficial · Microsoft Learn. Catálogo de casos de uso recomendados (enriquecimiento con TI, sincronización con ServiceNow, orquestación por Teams/Slack/correo con botones de aprobación, respuesta a usuario o equipo comprometido, respuesta manual con disparador de entidad) y plantillas sugeridas.
- [Threat response with Microsoft Sentinel playbooks (training module)](https://learn.microsoft.com/en-us/training/modules/threat-response-sentinel-playbooks/) · Curso · Oficial · Microsoft Learn Training. Módulo de 1 h 20 min (ruta SC-200) que explica las capacidades SOAR, el conector de Logic Apps de Sentinel y cómo crear y ejecutar un playbook a demanda, con ejercicios.
- [Monitor and collect diagnostic data for workflows in Azure Logic Apps](https://learn.microsoft.com/en-us/azure/logic-apps/monitor-workflows-collect-diagnostic-data) · Documentación · Oficial · Microsoft Learn. Cómo enviar telemetría de ejecuciones de workflows (disparadores, ejecuciones, acciones) a Log Analytics, Storage o Event Hubs mediante configuración de diagnóstico, en Consumption y Standard.
- [Create basic automation rules with Simple Flows in the Microsoft Defender portal (preview)](https://learn.microsoft.com/en-us/azure/sentinel/automation/create-basic-automation-rules-simple-flows) · Documentación · Oficial · Vista previa · Nuevo · Microsoft Learn · jul 2026. Presenta Simple Flows: acciones prearmadas sin Logic Apps (enviar correo, actualizar caso, añadir tareas, actualizar alerta) y los nuevos disparadores Case created/Case updated en el portal de Defender. *Nota:* Public preview 2026; correos con plantilla fija de Microsoft, sin CC/BCC; máximo 10 tareas por regla; Update Alert solo con disparador Alert created
- [Automation with ISOC in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-automation) · Documentación · Oficial · Vista previa · Microsoft Learn. Resume la automatización del Integrated Security Operations Center (ISOC) en Defender: reglas de automatización, playbooks de Logic Apps, Playbook Generator con IA, perfiles de integración y Enhanced Alert Trigger, con permisos URBAC y límites. *Nota:* Playbooks generados solo en Python, máx. 100 por tenant, 10 min por ejecución, 8M tokens IA/día; reglas enhanced sin orden de prioridad y una acción por regla; hasta 500 reglas activas por tenant
- [Generate playbooks using AI in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/automation/generate-playbook) · Documentación · Oficial · Vista previa · Microsoft Learn. Explica el generador de playbooks SOAR que crea flujos en Python co-escritos en lenguaje natural con el agente de código Cline dentro de un VS Code embebido en el portal de Defender, con perfiles de integración y Enhanced Alert Trigger. *Nota:* Requiere workspace incorporado a Defender y permiso URBAC 'Automation Playbooks'; la versión actual indica que no requiere licencia de Security Copilot ni SCU (versiones anteriores sí exigían capacidad SCU aprovisionada aunque no se facturara)
- [Create and customize Microsoft Sentinel playbooks from templates](https://learn.microsoft.com/en-us/azure/sentinel/automation/use-playbook-templates) · Documentación · Oficial · Vista previa · Microsoft Learn. Cómo instalar plantillas de playbooks desde Content hub o GitHub, filtrarlas por disparador/conectores/entidades y crear una copia editable con el asistente de despliegue. *Nota:* Las plantillas de playbook siguen en PREVIEW; técnicamente son plantillas ARM (workflow + API connections); avisa cuando hay versión nueva de la plantilla
- [Azure Monitor Logs reference - LogicAppWorkflowRuntime](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/logicappworkflowruntime) · Documentación · Oficial · Nuevo · Microsoft Learn · 28 jul 2026. Esquema de la tabla LogicAppWorkflowRuntime (RunId, ActionName, Status, Error, RetryHistory, TrackedProperties) para correlacionar con SentinelHealth y construir alertas de fallos de playbooks.
- [Investigate incidents with Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «Incident investigation».
- [Tutorial: respond to threats with playbooks and automation rules](https://learn.microsoft.com/en-us/azure/sentinel/tutorial-respond-threats-playbook) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «Automated response».
- [Handle false positives in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/false-positives) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «False-positive handling».
- [Automate threat response with playbooks](https://learn.microsoft.com/en-us/azure/sentinel/automate-responses-with-playbooks) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «Logic Apps playbooks».
- [Microsoft Sentinel health tables reference](https://learn.microsoft.com/en-us/azure/sentinel/health-table-reference) · Documentación · Oficial · Microsoft Learn. Esquema de la tabla SentinelHealth y operaciones registradas para conectores, reglas de análisis, reglas de automatización y playbooks.
- [Create incident tasks in Microsoft Sentinel using automation rules](https://learn.microsoft.com/en-us/azure/sentinel/create-tasks-automation-rule) · Documentación · Oficial · Microsoft Learn. Cómo usar reglas de automatización para añadir listas de tareas estandarizadas a incidentes según la regla analítica que los generó.
- [Automatización de la respuesta a amenazas en Microsoft Sentinel con reglas de automatización](https://learn.microsoft.com/es-es/azure/sentinel/automate-incident-handling-with-automation-rules) · Documentación · Oficial · ES · Microsoft Learn. Versión en español (traducción automática) del artículo conceptual sobre reglas de automatización de Sentinel, útil como lectura base para equipos hispanohablantes.
- [Create detections and perform investigations using Microsoft Sentinel (learning path)](https://learn.microsoft.com/en-us/training/paths/sc-200-create-detections-perform-investigations-azure-sentinel/) · Curso · Oficial · Microsoft Learn Training. Ruta de aprendizaje de 8 módulos alineada con SC-200 que incluye analítica, 'Automation in Microsoft Sentinel' (reglas de automatización) y 'Threat response with Microsoft Sentinel playbooks'.
- [Course SC-200T00-A: Defend against cyberthreats with Microsoft's security operations platform](https://learn.microsoft.com/en-us/training/courses/sc-200t00) · Credencial · Oficial · Microsoft Learn Training. Curso de 4 días (disponible en español) que prepara el examen SC-200 e incluye Sentinel, Defender XDR, Security Copilot y automatización con playbooks.
- [Implement automation rules and playbooks in Microsoft Sentinel (training module)](https://learn.microsoft.com/en-us/training/modules/implement-automation-rules-playbooks-sentinel/) · Curso · Oficial · Microsoft Learn Training. Módulo reciente (31 min) que diferencia reglas de automatización y playbooks, crea reglas de triaje/enrutamiento, activa un playbook de Content hub y crea uno propio en Logic Apps.
- [Microsoft Sentinel automation rules reference](https://learn.microsoft.com/en-us/azure/sentinel/automation-rule-reference) · Documentación · Oficial · Microsoft Learn. Referencia de las propiedades de entidad e incidente utilizables como condiciones en reglas de automatización y su correspondencia con la API y con el esquema de alertas.
- [Create automation rules with ISOC in Microsoft Defender (preview)](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-create-automation-rules) · Documentación · Oficial · Vista previa · Microsoft Learn. Describe las reglas de automatización 'enhanced' y 'standard' en el portal de Defender con disparadores de alerta y de caso, y permisos de RBAC unificado. *Nota:* Requiere permisos Unified RBAC 'Automation Rules' y 'Automation Playbooks' (lectura/escritura)
- [Generate playbooks using AI in the Microsoft Defender portal](https://learn.microsoft.com/en-us/defender-xdr/siem-defender-generate-playbooks) · Documentación · Oficial · Vista previa · Microsoft Learn. Procedimiento del Playbook Generator en Defender (modo Plan/Act, prueba con un ID de alerta, activación y uso desde reglas de automatización) para playbooks con entrada de alerta o de caso de incidente. *Nota:* Para casos de incidente, la identidad de Graph necesita SecurityAlert.ReadWrite.All, SecurityIncident.ReadWrite.All y CaseManagement.*; cambios de permisos tardan hasta 2 h
- [What is Azure Logic Apps?](https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-overview) · Documentación · Oficial · Ninja original · Microsoft Learn. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: doc «Logic Apps».
- [Referencia de reglas de automatización de Microsoft Sentinel](https://learn.microsoft.com/es-es/azure/sentinel/automation-rule-reference) · Documentación · Oficial · ES · Microsoft Learn. Versión en español de la referencia de condiciones y propiedades de entidades para reglas de automatización.

### Anuncios y blogs oficiales

- [Automating Microsoft Sentinel: Playbook Fundamentals](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/automating-microsoft-sentinel-playbook-fundamentals/4424475) · Blog oficial · Empleado de Microsoft · Matt Egen · Microsoft Tech Community - Microsoft Sentinel Blog · 16 jul 2025. Tercera entrega de la serie oficial 'Automating Microsoft Sentinel' que explica la estructura de un playbook, sus disparadores (incidente, alerta, entidad), las entidades clave y el catálogo de playbooks de Content hub.
- [Automating Microsoft Sentinel: A blog series on enabling Smart Security](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/automating-microsoft-sentinel-a-blog-series-on-enabling-smart-security/4411356/replies/4416997) · Blog oficial · Empleado de Microsoft · Matt Egen · Microsoft Tech Community - Microsoft Sentinel Blog · 19 may 2025. Primera entrega de la serie oficial sobre automatización de Sentinel: por qué automatizar y panorama de los tipos de automatización (reglas, playbooks, código).
- [Debugging Playbooks](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/debugging-playbooks/4165374/replies/4172865) · Blog oficial · Empleado de Microsoft · Legado aún útil · Gary Bushey · Microsoft Tech Community - Microsoft Sentinel Blog · 12 jun 2024. Guía práctica para depurar playbooks: crear una regla de análisis 'dummy' con datatable, limitar la regla de automatización a esa regla, revisar entradas/salidas de cada paso y re-ejecutar con 'Resubmit'. *Nota:* Gary Bushey (ex-MVP y luego empleado de Microsoft; hoy figura como 'Former Employee'). URL visible corresponde a la vista con respuestas del post; el método sigue vigente aunque las capturas sean del portal de Azure
- [Become a Microsoft Sentinel Automation Ninja!](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-automation-ninja/3563377) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community – Microsoft Sentinel Blog · 1 jul 2022. Ninja temático de automatización (SOAR) en Sentinel que reúne recursos desde la introducción a reglas de automatización y playbooks hasta trucos avanzados. *Nota:* Anunciado 01-jul-2022 en el foro de Security Community. Los playbooks siguen basados en Logic Apps; en el portal de Defender cambian rutas de UI. Mapa: -> M13/X1
- [How to use Microsoft Sentinel for Incident Response, Orchestration and Automation](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/how-to-use-azure-sentinel-for-incident-response-orchestration/ba-p/2242397) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: blog-oficial «How to use Microsoft Sentinel for Incident Response, Orchestration and Automation».
- [A playbook using a watchlist to inform a subscription owner about an alert](https://techcommunity.microsoft.com/t5/microsoft-sentinel-blog/playbooks-amp-watchlists-part-1-inform-the-subscription-owner/ba-p/1768917) · Blog oficial · Oficial · Legado aún útil · Ninja original · Microsoft Tech Community. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: blog-oficial «A playbook using a watchlist to inform a subscription owner about an alert».

### Webinars, videos y podcasts

- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar · Oficial · Neelam Nursee, Naomi Christis · YouTube – Microsoft Security Community · 9 dic 2025. Recorrido de un día en el SOC dentro del portal de Defender: navegación, cola unificada de incidentes, UEBA, TI, watchlists, automatización y case management.
- [Transition to the Unified SOC Platform: Deep Dive and Interactive Q&A for SOC Professionals](https://www.youtube.com/watch?v=WIM6fbJDkK4) · Webinar · Empleado de Microsoft · Chi Nguyen, Naomi Christis · Microsoft Security Community (YouTube) · 1 abr 2025. Sesión práctica sobre incidentes, correlación, automatización y advanced hunting al pasar de Sentinel en Azure al portal unificado de Defender.
- [Microsoft Sentinel | Automated Responses to Threats | Automation Rules | Playbooks | Sentinel SOAR](https://www.youtube.com/watch?v=H57XZfW6_4Y) · Video · Comunidad · Legado aún útil · CyberPlatter · YouTube - CyberPlatter. Capítulo de un curso gratuito en video que explica y demuestra reglas de automatización, playbooks y plantillas de playbooks en Sentinel para principiantes. *Nota:* Grabado sobre la experiencia del portal de Azure; trasladar los pasos a Microsoft Sentinel en el portal de Defender

### Laboratorios, GitHub y herramientas

- [Learning Path 8 - Lab 1 - Exercise 1 - Create a Playbook in Microsoft Sentinel (SC-200 lab)](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/Instructions/Labs/LAB_AK_08_Lab1_Ex01_Playbook_Defender.html) · Laboratorio · Oficial · Microsoft Learning · MicrosoftLearning (GitHub Pages). Laboratorio oficial que, desde el portal de Defender, instala la solución 'Sentinel SOAR Essentials', crea un playbook de tareas de incidente (ransomware) desde plantilla y lo asocia a una regla de automatización por tácticas.
- [MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst (GitHub)](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · GitHub · Oficial · Nuevo · Microsoft Learning · GitHub - MicrosoftLearning · ago 2026. Repositorio fuente de los labs SC-200 (instrucciones, scripts KQL en Allfiles y demos VTD, incluidos data lake, incidentes y SOC optimization en Defender).
- [Microsoft Sentinel GitHub](https://github.com/Azure/Azure-Sentinel) · GitHub · Oficial · Legado aún útil · Ninja original · GitHub. Enlace del Módulo 12 ('Implementación de SOAR') del skill-up de Learn: github «Microsoft Sentinel GitHub».

### Comunidad: blogs, libros, newsletters y eventos

- [The Hidden Reason Your Sentinel Playbook Won't Show Up in Automation Rules (It's Not RBAC)](https://techcommunity.microsoft.com/discussions/microsoftsentinel/the-hidden-reason-your-sentinel-playbook-wont-show-up-in-automation-rules-its-no/4555399) · Blog · Comunidad · Nuevo · Blackfoundry · Microsoft Tech Community - Microsoft Sentinel (discusiones) · 10 sep 2026. Caso real: un playbook creado con el portal en otro idioma generó un nombre de disparador localizado y no aparecía en el selector de reglas de automatización hasta renombrarlo a 'Microsoft_Sentinel_incident'.
- [Use automation/playbooks in Microsoft Sentinel during incident update activity using update triggers](https://jeffreyappel.nl/use-automation-playbooks-in-microsoft-sentinel-during-incident-update-activity-using-update-triggers/) · Blog · MVP · Legado aún útil · Jeffrey Appel · Jeffrey Appel - Microsoft Security blog · 1 jun 2022. Explica el disparador 'When incident is updated' con sus operadores (Changed, Changed from/to, Added) y fuentes de actualización, con ejemplos de notificación y sincronización de tickets. *Nota:* Escrito cuando el disparador estaba en preview (hoy GA) y antes del portal de Defender (cambió 'Microsoft 365 Defender' como valor de Updated by)

**Manos a la obra**

1. `Laboratorio` Crea una regla de automatización que asigne responsable y etiquete los incidentes de alta severidad.
2. `Laboratorio` Crea otra que cierre automáticamente un falso positivo conocido, con fecha de vencimiento.
3. `Laboratorio` Despliega un playbook desde plantilla y ejecútalo bajo demanda sobre un incidente.

**¿Quieres profundizar?**

- [Transition to the Unified SOC Platform: Deep Dive and Interactive Q&A for SOC Professionals](https://www.youtube.com/watch?v=WIM6fbJDkK4) · Webinar
- [Use automation/playbooks in Microsoft Sentinel during incident update activity using update triggers](https://jeffreyappel.nl/use-automation-playbooks-in-microsoft-sentinel-during-incident-update-activity-using-update-triggers/) · Blog
- [Learning Path 8 - Lab 1 - Exercise 1 - Create a Playbook in Microsoft Sentinel (SC-200 lab)](https://microsoftlearning.github.io/SC-200T00A-Microsoft-Security-Operations-Analyst/Instructions/Labs/LAB_AK_08_Lab1_Ex01_Playbook_Defender.html) · Laboratorio
- [Part 1: Stop Waiting, Start Onboarding: Get Sentinel Defender-Ready Today](https://www.youtube.com/watch?v=I5dhz_0LDCI) · Webinar

<a id="reto-intermedio"></a>

## Reto del nivel

**Un caso de uso de punta a punta con costo controlado.** Elige un riesgo concreto (por ejemplo, password spray contra cuentas privilegiadas). Define las fuentes y su nivel de datos (analítica o lago), crea la detección (programada o NRT, y su versión como detección personalizada), agrega excepciones con una watchlist, automatiza el triage con una regla de automatización y un playbook, y mide en un libro el tiempo de triage. Cierra con la estimación de costo mensual del caso de uso y su cobertura en MITRE ATT&CK.

<a id="quiz-intermedio"></a>

## Evaluación del nivel

Responde y compara con [Evaluaciones y respuestas](06_Evaluaciones_y_respuestas.md#eval-intermedio). Con 80 % o más, ¡nivel aprobado! (En la versión web puedes corregir en línea y generar tu certificado).

1. En el portal de Defender, ¿cuál es el modelo de workspaces de Sentinel por tenant?
   - a) Hasta cinco principales
   - b) Uno principal y secundarios ilimitados
   - c) Un único workspace
   - d) Uno principal y diez secundarios

2. Para un workspace en una región de Latinoamérica fuera de Brasil, ¿dónde procesa Sentinel los datos de cliente según la documentación de residencia?
   - a) En la misma región del workspace
   - b) En Brasil
   - c) En una región de EE. UU.
   - d) En Europa

3. Los eventos recolectados con Windows Event Forwarding se escriben en la tabla…
   - a) SecurityEvent
   - b) WindowsEvent
   - c) Event
   - d) CommonSecurityLog

4. ¿Cuál es la situación de la HTTP Data Collector API a noviembre de 2026?
   - a) Recomendada para conectores nuevos
   - b) Fin de soporte el 14 de septiembre de 2026; migrar a Logs Ingestion API o CCF
   - c) Retirada junto con MMA en 2024
   - d) Reemplazada por Logstash

5. Una transformación split configurada en Table management…
   - a) Elimina los datos que no cumplen la condición
   - b) Envía lo que cumple la condición a analítica y el resto solo al data lake
   - c) Solo funciona en el portal de Azure
   - d) Solo aplica a tablas Basic

6. ¿Qué tablas reemplazan a ThreatIntelligenceIndicator?
   - a) ThreatIntelIndicators y ThreatIntelObjects
   - b) TIIndicators_CL
   - c) SecurityIoC
   - d) ThreatIntelligenceIndicatorV2

7. ¿Qué prerrequisito tiene la experiencia de migración de SIEM del portal de Defender?
   - a) Licencia de Splunk Enterprise Security
   - b) Security Copilot habilitado en el tenant, sin consumo de SCU
   - c) Logic Apps Standard
   - d) Un workspace en el portal de Azure

8. ¿Con qué frecuencia y con qué retraso se ejecutan las reglas NRT de analítica?
   - a) Cada 5 minutos, con 5 minutos de retraso
   - b) Cada minuto, con 2 minutos de retraso
   - c) Cada minuto, sin retraso
   - d) Cada 15 minutos, con 2 minutos de retraso

9. Al incorporar un workspace al portal de Defender, ¿qué ocurre con Fusion?
   - a) Sigue activo
   - b) Pasa a vista previa
   - c) Se deshabilita y lo reemplaza la correlación de Defender XDR
   - d) Se convierte en una detección personalizada

10. ¿Qué tabla de supervisión NO se factura?
   - a) SentinelAudit
   - b) SentinelHealth
   - c) Ambas
   - d) Ninguna

11. ¿Por qué se usa arg_max() al calcular métricas con la tabla SecurityIncident?
   - a) Para ordenar por severidad
   - b) Porque cada actualización del incidente crea un registro nuevo
   - c) Para unir con SecurityAlert
   - d) Para reducir costos

12. ¿Dónde se pueden crear marcadores de hunting?
   - a) Solo en el portal de Defender
   - b) En la búsqueda avanzada
   - c) Solo en el portal de Azure
   - d) En ambos portales

13. En 2026, ¿cuál es la experiencia recomendada para gestionar incidentes en el portal de Defender?
   - a) La integración con Teams
   - b) Los incident cases (vista previa)
   - c) Los libros
   - d) Los hunts

---

*Guía de estudio independiente basada en material público. No es una publicación oficial de Microsoft ni reemplaza al Ninja Training oficial, a la documentación de Microsoft Learn o a las certificaciones oficiales. Los contenidos enlazados pertenecen a sus autores. Ante cualquier diferencia, prevalece la documentación oficial en inglés vigente.*

Curaduría: @SCavanna · Principal CSA Security · Microsoft MCSA · Noviembre 2026 · Fuentes verificadas al 6 de noviembre de 2026

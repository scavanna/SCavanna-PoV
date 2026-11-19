# Cobertura multicloud: hasta dónde llega Microsoft fuera de Microsoft

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M03 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Por qué importa

Una organización puede elegir la plataforma de seguridad de Microsoft y tener sus cargas en varias nubes. La pregunta entonces no es si la plataforma es buena, sino **hasta dónde llega**: qué controla en AWS, en Google Cloud, en el centro de datos y en las aplicaciones SaaS de terceros, con qué mecanismo y con qué límite.

## 2. Cómo se verificó

- Se revisó la documentación oficial de Microsoft de las 50 capacidades, con fecha de corte al 15 de noviembre de 2026.
- Para cada capacidad se registró la cobertura en cinco entornos: Azure, AWS, Google Cloud, centro de datos propio y SaaS de terceros.
- Valores: Sí, Parcial, No, No aplica y No confirmado. «No confirmado» significa que la documentación consultada no lo afirma con claridad: no es un «no», es un punto a probar.
- Se excluyeron las vistas previas privadas.

## 3. Resultado general

| Cobertura | Celdas | Proporción |
|---|:--:|:--:|
| Sí | 68 | 27% |
| Parcial | 87 | 35% |
| No confirmado | 64 | 26% |
| No | 5 | 2% |
| No aplica | 26 | 10% |
| Total | 250 | 100% |

Solo 17 de las 50 capacidades tienen los cinco entornos confirmados. La cobertura plena se concentra en Azure; fuera de Azure predomina la cobertura parcial.

## 4. Cobertura por capacidad

| ID | Capacidad | Azure | AWS | Google Cloud | Centro de datos | SaaS de terceros | Estado |
|---|---|:--:|:--:|:--:|:--:|:--:|---|
| MS-IDE-01 | Microsoft Entra ID con Conditional Access | Sí | Parcial | Parcial | Parcial | Sí | mixto: Conditional Access e intensidades de autenticación en disponibilidad general; la orientación de directivas a agentes figura como versión preliminar pública |
| MS-IDE-02 | Microsoft Entra ID Protection | Sí | Parcial | Parcial | Parcial | Parcial | disponibilidad general |
| MS-IDE-03 | Microsoft Entra Privileged Identity Management | Sí | Parcial | No confirmado | No confirmado | Parcial | disponibilidad general |
| MS-IDE-04 | Microsoft Entra ID Governance | Sí | Parcial | Parcial | Sí | Sí | disponibilidad general |
| MS-IDE-05 | Microsoft Entra Workload ID | Sí | Parcial | Parcial | Parcial | Parcial | disponibilidad general |
| MS-IDE-06 | Microsoft Entra Agent ID | Sí | Parcial | Parcial | No confirmado | Parcial | mixto: producto en disponibilidad general; el asistente de creación de blueprints e identidades de agente y la orientación de Conditional Access a agentes en versión preliminar pública |
| MS-IDE-07 | Microsoft Defender for Identity | Parcial | No confirmado | No confirmado | Sí | Parcial | mixto: sensores para Active Directory, AD FS, AD CS y Microsoft Entra Connect en disponibilidad general; integración con Okta en versión preliminar pública |
| MS-END-01 | Microsoft Defender for Endpoint | Sí | Sí | Sí | Sí | No aplica | disponibilidad general |
| MS-END-02 | Microsoft Defender Vulnerability Management | Sí | Sí | Sí | Sí | No aplica | disponibilidad general |
| MS-END-03 | Microsoft Intune | Parcial | No confirmado | No confirmado | Parcial | No aplica | disponibilidad general |
| MS-END-04 | Controles de seguridad de Windows administrados con Intune | Parcial | Parcial | Parcial | Parcial | No aplica | disponibilidad general |
| MS-PRO-01 | Microsoft Defender for Office 365 | No aplica | No aplica | No aplica | Parcial | No confirmado | disponibilidad general |
| MS-PRO-02 | Attack simulation training | No aplica | No aplica | No aplica | Parcial | No confirmado | disponibilidad general |
| MS-DAT-01 | Microsoft Purview Information Protection | Parcial | No confirmado | No | Sí | Sí | mixto: etiquetas de confidencialidad en disponibilidad general; extensión de etiquetas a activos de Microsoft Purview Data Map en versión preliminar pública |
| MS-DAT-02 | Microsoft Purview Data Loss Prevention | No confirmado | No confirmado | No confirmado | Sí | Parcial | mixto: ubicaciones principales en disponibilidad general; aplicaciones conectadas no Microsoft (Box, Dropbox, Google Workspace, Salesforce) y Microsoft 365 Copilot en versión preliminar pública |
| MS-DAT-03 | Microsoft Purview Data Security Posture Management | Parcial | No confirmado | Parcial | No confirmado | Parcial | mixto: la versión actual de DSPM se documenta sin etiqueta de versión preliminar; la integración con orígenes no Microsoft mediante Microsoft Sentinel data lake en versión preliminar pública |
| MS-DAT-04 | Microsoft Purview Insider Risk Management | Parcial | Parcial | No confirmado | Parcial | Parcial | mixto: indicadores integrados de servicios en la nube sin etiqueta de versión preliminar; conector Insider Risk Indicators e indicadores de Risky Agents, Risky AI usage y Risky browsing en versión preliminar pública |
| MS-DAT-05 | Microsoft Purview Data Map y Unified Catalog | Sí | Parcial | Parcial | Sí | Parcial | mixto: disponibilidad general con retiro anunciado (modo de mantenimiento hasta 2027-11-12); etiquetado de activos y algunas directivas en versión preliminar pública |
| MS-DAT-06 | Customer Key y Double Key Encryption | Parcial | No confirmado | No confirmado | Parcial | No | disponibilidad general |
| MS-XDR-01 | Microsoft Defender XDR | Sí | Parcial | No confirmado | Parcial | Parcial | disponibilidad general |
| MS-XDR-02 | Inteligencia de amenazas en el portal de Defender | Parcial | No confirmado | No confirmado | Parcial | Parcial | mixto: Threat analytics y la convergencia de Defender Threat Intelligence en disponibilidad general; la pestaña Indicators en versión preliminar pública |
| MS-SIE-01 | Microsoft Sentinel | Sí | Sí | Sí | Sí | Sí | mixto: SIEM y conectores Amazon Web Services S3 y GCP Pub/Sub en disponibilidad general; estado de Microsoft Sentinel data lake no confirmado en la página abierta; algunas funciones del portal de Defender en versión preliminar pública |
| MS-SIE-02 | Automatización de Microsoft Sentinel | Sí | No confirmado | No confirmado | No confirmado | Sí | disponibilidad general |
| MS-NUB-01 | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Sí | Sí | Parcial | Parcial | Parcial | mixto: disponibilidad general; ingesta de AWS CloudTrail y GCP Cloud Logging, panel de seguridad de AKS y recomendaciones personalizadas en versión preliminar pública |
| MS-NUB-02 | Defender for Servers | Sí | Sí | Parcial | Parcial | No aplica | disponibilidad general |
| MS-NUB-03 | Defender for Containers | Sí | Sí | Sí | Parcial | Parcial | mixto: disponibilidad general; evaluación de vulnerabilidades de nodos EKS y GKE, acciones de respuesta en XDR y protección en tiempo de ejecución en Kubernetes con Arc en versión preliminar pública |
| MS-NUB-04 | Defender for Cloud: servicios de plataforma | Sí | Parcial | No confirmado | No confirmado | No aplica | disponibilidad general en Azure comercial (algunas alertas de bases de datos de Azure en versión preliminar pública) |
| MS-NUB-05 | DevOps security de Defender for Cloud | Sí | No aplica | No aplica | No | Parcial | mixto: DevOps security en disponibilidad general; análisis de código sin agente y «DevOps security posture» de Foundational CSPM en versión preliminar pública |
| MS-NUB-06 | Azure Arc, Azure Policy y Azure Update Manager | No aplica | Sí | Sí | Sí | No aplica | mixto: disponibilidad general; inscripción de máquinas (machine enrollment) en versión preliminar pública |
| MS-APP-01 | Microsoft Defender for Cloud Apps | Sí | Parcial | Parcial | No confirmado | Parcial | mixto: disponibilidad general; SSPM en versión preliminar pública para algunas aplicaciones (NetDocuments, Workplace by Meta, Zoom) |
| MS-EXP-01 | Microsoft Security Exposure Management | Sí | Sí | Sí | Parcial | No confirmado | mixto: conectores de datos de terceros en versión preliminar pública; el estado del producto base no se declara en las páginas abiertas |
| MS-EXP-02 | Microsoft Defender External Attack Surface Management | Parcial | Parcial | Parcial | Parcial | No confirmado | no confirmado: la página no declara el estado ni lleva etiqueta de versión preliminar |
| MS-IAA-01 | Microsoft Agent 365 | Sí | Parcial | Parcial | No confirmado | Parcial | mixto: disponibilidad general para el segmento comercial; la observabilidad de agentes de terceros pertenece al programa de versión preliminar Frontier |
| MS-IAA-02 | Defender for Cloud: postura de IA y Defender for AI Services | Sí | Parcial | No confirmado | No aplica | No confirmado | mixto: postura de IA y Defender for AI Services en disponibilidad general; descubrimiento de agentes de IA en versión preliminar pública |
| MS-IAA-03 | Protecciones de Microsoft Purview para IA generativa | Sí | No confirmado | No confirmado | No confirmado | Parcial | mixto: protecciones generales sin etiqueta de versión preliminar; integraciones con SASE o navegadores de terceros en disponibilidad general o versión preliminar pública según la integración |
| MS-IAA-04 | Controles de seguridad de Microsoft Foundry | Sí | Parcial | Parcial | Parcial | No confirmado | mixto: Prompt Shields y filtros de texto e imagen en disponibilidad general; Groundedness detection y categorías personalizadas en versión preliminar pública; estado del AI Red Teaming Agent no confirmado |
| MS-ASI-01 | Microsoft Security Copilot | Sí | No confirmado | No confirmado | No confirmado | Parcial | mixto: disponibilidad general; inclusión en Microsoft 365 E5 y E7 en despliegue por fases; la página de complementos no Microsoft lleva aviso de versión preliminar |
| MS-RED-01 | Global Secure Access (Entra Internet Access y Private Access) | Sí | Sí | Sí | Sí | Sí | mixto: ambos productos en disponibilidad general; registros de tráfico y despliegue multinube del conector de red privada en versión preliminar pública |
| MS-RED-02 | Azure Firewall, Web Application Firewall y DDoS Protection | Sí | Parcial | Parcial | Parcial | No confirmado | disponibilidad general |
| MS-RED-03 | Segmentación y acceso privado en Azure | Sí | Parcial | Parcial | Parcial | No confirmado | mixto: Network Security Perimeter en disponibilidad general con algunos recursos en versión preliminar pública; Private Link Service Direct Connect en versión preliminar pública; resto en disponibilidad general |
| MS-RED-04 | Microsoft Defender for IoT | No aplica | No aplica | No aplica | Sí | No aplica | mixto: supervisión OT con sensores de red en disponibilidad general; experiencia en el portal de Microsoft Defender en versión preliminar pública |
| MS-RED-05 | Azure Key Vault y Managed HSM | Sí | No confirmado | No confirmado | Parcial | No confirmado | mixto: ambos servicios en disponibilidad general; claves simétricas OCT-HSM en Key Vault Premium en versión preliminar pública |
| MS-RES-01 | Azure Backup | Sí | No confirmado | No confirmado | Sí | No | mixto: disponibilidad general; copia de Azure Database for MySQL Flexible Server y Azure Cosmos DB en versión preliminar pública |
| MS-RES-02 | Azure Site Recovery | Sí | Parcial | No confirmado | Sí | No aplica | mixto: disponibilidad general; replicación desde Azure Extended Zones en versión preliminar pública |
| MS-RES-03 | Microsoft 365 Backup | No aplica | No aplica | No aplica | No aplica | No | disponibilidad general |
| MS-CUM-01 | Microsoft Purview Compliance Manager | Sí | Sí | Sí | No confirmado | Parcial | disponibilidad general |
| MS-CUM-02 | Microsoft Purview Audit y eDiscovery | No confirmado | No confirmado | No confirmado | No confirmado | Parcial | mixto: disponibilidad general; algunas funciones de eDiscovery (consultas KQL en conjuntos de revisión, Query Report) en versión preliminar pública |
| MS-CUM-03 | Microsoft Purview Data Lifecycle Management y Records Management | No confirmado | No confirmado | No confirmado | No confirmado | Parcial | disponibilidad general |
| MS-CUM-04 | Microsoft Purview Communication Compliance e Information Barriers | No confirmado | No confirmado | No confirmado | Parcial | Parcial | disponibilidad general |
| MS-CUM-05 | Microsoft Priva | No confirmado | No confirmado | No confirmado | No confirmado | No confirmado | mixto: Privacy Risk Management en disponibilidad general; situación de Subject Rights Requests y de otras soluciones de Priva no confirmada |

## 5. Qué cubre cada capacidad fuera de Microsoft y con qué límite

| ID | Capacidad | Qué cubre y con qué límite | Fecha de la página | Fuente |
|---|---|---|---|---|
| MS-IDE-01 | Microsoft Entra ID con Conditional Access | Fuera de Microsoft actúa por federación: SSO SAML desde la galería hacia AWS IAM Identity Center y Google Cloud, aplicaciones SaaS integradas y aplicaciones web locales publicadas con Microsoft Entra application proxy (conector de red privada). Límite: solo protege inicios de sesión que pasan por Entra ID; el usuario raíz y las cuentas IAM nativas de AWS o Google Cloud quedan fuera, y en local solo cubre aplicaciones publicadas o integradas. | 2026-04-27 | https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview |
| MS-IDE-02 | Microsoft Entra ID Protection | Calcula riesgo de usuario y de inicio de sesión sobre identidades de Entra ID y lo aplica mediante Conditional Access basado en riesgo a cualquier aplicación federada (AWS, Google Cloud, SaaS, aplicaciones locales publicadas). Límite: no detecta riesgo sobre identidades nativas de AWS IAM, Google Cloud ni Active Directory local; solo ve el inicio de sesión que pasa por Entra ID. | 2025-10-30 | https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection |
| MS-IDE-03 | Microsoft Entra Privileged Identity Management | Gobierna de forma nativa roles de Microsoft Entra, roles de recursos de Azure y pertenencia o propiedad de grupos (PIM for Groups). Hacia AWS y SaaS solo llega indirectamente, activando de forma temporal un grupo asignado a la aplicación (p. ej., grupos mapeados a roles de AWS) con aprovisionamiento SCIM; no administra roles IAM de AWS ni de Google Cloud de forma nativa. | 2026-04-23 | https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure |
| MS-IDE-04 | Microsoft Entra ID Governance | Flujos de ciclo de vida, gestión de derechos (paquetes de acceso) y revisiones de acceso, con aprovisionamiento hacia aplicaciones en la nube y locales mediante SCIM, LDAP y SQL, y aprovisionamiento entrante desde RR. HH. En AWS IAM Identity Center y Google Cloud gobierna la asignación y el aprovisionamiento de usuarios, pero no los permisos internos (conjuntos de permisos de AWS, roles IAM de Google Cloud). | 2026-05-08 | https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview |
| MS-IDE-05 | Microsoft Entra Workload ID | La federación de identidades de carga permite que cargas en AWS (IAM Outbound Identity Federation, EKS), Google Cloud (incluido GKE), Kubernetes local, SPIFFE/SPIRE o GitHub Actions canjeen su token externo por un token de Entra, sin secretos. Límite: solo cubre el acceso de esas cargas a recursos protegidos por Entra; no gobierna las identidades de carga nativas de AWS o Google Cloud. | 2025-04-09 | https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation |
| MS-IDE-06 | Microsoft Entra Agent ID | Cubre agentes construidos fuera de Microsoft (se citan Amazon Bedrock, Google Cloud y n8n) mediante Microsoft Entra ID Auth SDK (sidecar) o federación de identidades de carga. Límite: cada agente externo debe integrarse expresamente; no se documenta un alta automática de agentes de terceros. | 2026-06-24 | https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id |
| MS-IDE-07 | Microsoft Defender for Identity | Sensores en controladores de dominio y en servidores AD FS, AD CS y Microsoft Entra Connect, más señales de Microsoft Entra ID; fuera de Microsoft, un conector por API para Okta (versión preliminar pública). Límite: en Azure solo aporta señales de identidad de Entra ID y no se documentan AWS IAM ni Google Cloud como fuentes. | 2026-07-23 | https://learn.microsoft.com/en-us/defender-for-identity/what-is |
| MS-END-01 | Microsoft Defender for Endpoint | Agente por sistema operativo (Windows 10/11, Windows Server 2012 R2 y posteriores, macOS, Linux, Android, iOS), con independencia de dónde se aloje el servidor. Incorporación automática para máquinas virtuales de Azure y servidores con Azure Arc mediante Defender for Servers; manual o «Direct onboarding» para servidores fuera de Azure. Límite: los servidores requieren licencia aparte. | 2025-11-17 | https://learn.microsoft.com/en-us/defender-endpoint/minimum-requirements |
| MS-END-02 | Microsoft Defender Vulnerability Management | Evalúa vulnerabilidades y configuración de los dispositivos incorporados a Defender for Endpoint (Windows, macOS y Linux, incluido Amazon Linux), sea cual sea su alojamiento. Límite: en Android e iOS/iPadOS solo vulnerabilidades, sin evaluación de configuración; en Windows Server solo compilaciones LTSC. | 2026-09-24 | https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-supported-os |
| MS-END-03 | Microsoft Intune | Administra dispositivos Android, iOS/iPadOS, Linux (Ubuntu LTS, RHEL), macOS, Windows y ChromeOS, además de Cloud PC de Windows 365. Límite: la lista de plataformas no incluye Windows Server, por lo que no administra servidores del centro de datos ni de otras nubes; en Azure solo alcanza escritorios virtuales cliente. | 2026-04-16 | https://learn.microsoft.com/en-us/intune/fundamentals/ref-supported-platforms |
| MS-END-04 | Controles de seguridad de Windows administrados con Intune | Los perfiles de BitLocker, Windows LAPS, App Control for Business y reducción de superficie de ataque se dirigen a la plataforma Windows; la cobertura depende de que el equipo sea un dispositivo Windows administrado, no de dónde se aloje. Límite: los dispositivos con Defender for Endpoint no inscritos en Intune solo reciben Antivirus, Attack Surface Reduction y EDR, y las reglas ASR exigen Microsoft Defender Antivirus como antivirus principal. | 2026-04-15 | https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/manage-policies |
| MS-PRO-01 | Microsoft Defender for Office 365 | Protege correo y colaboración de Microsoft 365: Safe Attachments en correo, SharePoint, OneDrive y Teams, y Safe Links en correo, clientes de Office y Teams. Fuera de Microsoft 365 solo consta que la protección integrada de buzones (antes EOP) se ofrece como suscripción independiente para entornos de correo locales; no se confirma Plan 1/Plan 2 sobre buzones locales ni cobertura de Gmail u otro correo en la nube de terceros. | 2026-05-21 | https://learn.microsoft.com/en-us/defender-office-365/mdo-about |
| MS-PRO-02 | Attack simulation training | Simulaciones de phishing y formación para usuarios con licencia Microsoft 365 E5 o Defender for Office 365 Plan 2. Admite buzones locales con informes reducidos; no se indica compatibilidad con buzones de otros proveedores en la nube. | 2026-07-03 | https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started |
| MS-DAT-01 | Microsoft Purview Information Protection | Tres mecanismos fuera de Microsoft 365: Microsoft Defender for Cloud Apps etiqueta y protege contenido en aplicaciones de terceros (Salesforce, Box, Dropbox); el cliente y el scanner de Microsoft Purview Information Protection cubren repositorios locales; y Data Map (versión preliminar) etiqueta activos de Azure. Límite: en la tabla de Data Map, Google BigQuery, Amazon S3 y Amazon RDS figuran sin etiquetado, aunque otra página incluye AWS RDS entre los activos etiquetables. | 2026-10-29 | https://learn.microsoft.com/en-us/purview/sensitivity-labels |
| MS-DAT-02 | Microsoft Purview Data Loss Prevention | Cubre dispositivos Windows 10/11 y macOS, recursos compartidos de archivos y SharePoint locales (con el scanner de Information Protection) y aplicaciones en la nube de terceros mediante Defender for Cloud Apps; el tráfico web hacia aplicaciones no administradas se controla en Microsoft Edge for Business y en la red mediante integraciones SASE. Límite: las ubicaciones listadas no incluyen almacenes de datos IaaS de Azure, AWS ni Google Cloud. | 2026-06-26 | https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp |
| MS-DAT-03 | Microsoft Purview Data Security Posture Management | Declara cobertura de Microsoft 365, Azure, Fabric y plataformas SaaS e IaaS de terceros (Google Cloud, Snowflake, Databricks) mediante soluciones de socios (Varonis, Cyera, BigID, OneTrust) y Microsoft Sentinel data lake. Límite: las ubicaciones no Microsoft dependen de socios; AWS no se nombra y no se enumeran las aplicaciones de IA de terceros cubiertas. | — | https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about |
| MS-DAT-04 | Microsoft Purview Insider Risk Management | Indicadores integrados para Google Drive, Box y Dropbox y para Amazon S3 y Azure (SQL Server y Storage), que exigen facturación de pago por uso y conectar las aplicaciones en Microsoft Defender; otras fuentes entran con indicadores personalizados y el conector Insider Risk Indicators. Límite: Google Cloud como infraestructura no aparece; en local solo indicadores de dispositivos incorporados y conectores (acceso físico, historiales médicos). | 2026-06-22 | https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-policy-indicators |
| MS-DAT-05 | Microsoft Purview Data Map y Unified Catalog | Examina orígenes de Azure, AWS (Amazon S3 y RDS con clasificación; Redshift solo metadatos), Google BigQuery (sin clasificación, con linaje), bases y archivos locales (SQL Server, Oracle, Teradata, SAP, HDFS) mediante self-hosted integration runtime, y servicios como Snowflake, Salesforce, Tableau y Looker. Límite: la clasificación automática y las directivas se concentran en Azure, y el producto está en retiro. | 2026-10-13 | https://learn.microsoft.com/en-us/purview/data-map-data-sources |
| MS-DAT-06 | Customer Key y Double Key Encryption | Customer Key cifra solo datos en reposo de Microsoft 365 (Exchange, SharePoint, OneDrive, Teams, Windows 365, interacciones de Microsoft 365 Copilot) con claves en Azure Key Vault. DKE mantiene una clave bajo control del cliente en un servicio que puede hospedarse en local o en la nube sin nombrar proveedores. Límite: no protegen datos fuera de Microsoft 365, y el contenido con DKE pierde Copilot, eDiscovery, búsqueda, DLP y coautoría. | 2026-01-15 | https://learn.microsoft.com/en-us/purview/customer-key-overview |
| MS-XDR-01 | Microsoft Defender XDR | Correlaciona de forma nativa solo señales de productos de seguridad Microsoft licenciados (Defender for Endpoint, Office 365, Identity, Cloud Apps, Defender for Cloud, Entra ID Protection, entre otros). Las señales no Microsoft entran por Microsoft Sentinel en el portal de Defender (cola de incidentes unificada): conectores para AWS, Syslog/CEF para orígenes locales y API o conectores personalizados para el resto. | 2026-08-07 | https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender |
| MS-XDR-02 | Inteligencia de amenazas en el portal de Defender | La inteligencia es global y no depende del entorno; el cruce con el entorno propio usa incidentes y alertas de Defender for Endpoint, Identity, Office 365, Cloud Apps y Defender for Cloud, y la exposición solo se calcula sobre dispositivos incorporados. Límite: no se desglosa cómo se reflejan los recursos de AWS o Google Cloud entre los activos afectados. | 2026-11-08 | https://learn.microsoft.com/en-us/defender-xdr/threat-analytics |
| MS-SIE-01 | Microsoft Sentinel | AWS: el conector Amazon Web Services S3 ingiere desde un bucket S3 (cola SQS y rol OIDC) CloudTrail, VPC Flow Logs, GuardDuty y CloudWatch. Google Cloud: conectores GCP Pub/Sub (Audit Logs, Security Command Center, GKE) con federación de identidad de carga. Local mediante Azure Arc y Azure Monitor Agent (Syslog/CEF); SaaS y terceros mediante conectores del Content hub. Límite: cada fuente exige su propio conector, y su coste de ingesta. | 2026-09-10 | https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender |
| MS-SIE-02 | Automatización de Microsoft Sentinel | Los playbooks son flujos de Azure Logic Apps que se integran con sistemas internos y externos; la documentación cita ServiceNow como sistema externo de tickets. Límite: la página no enumera acciones concretas sobre AWS, Google Cloud ni sistemas locales. | 2026-06-28 | https://learn.microsoft.com/en-us/azure/sentinel/automation/automation |
| MS-NUB-01 | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | AWS y Google Cloud se conectan con conectores nativos sin secretos de larga duración: Foundational CSPM da inventario, recomendaciones, secure score y Microsoft cloud security benchmark; Defender CSPM añade rutas de ataque, cumplimiento regulatorio, DSPM y análisis sin agente. Límites: en Google Cloud no hay protección serverless y el descubrimiento de datos sensibles solo cubre Cloud Storage; en local solo recursos con Azure Arc (inventario, recomendaciones, secure score); en SaaS solo GitHub, Azure DevOps, GitLab, Docker Hub y JFrog. | 2026-09-30 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-cloud-security-posture-management |
| MS-NUB-02 | Defender for Servers | Fuera de Azure las máquinas se incorporan con Azure Arc (aprovisionamiento automático en EC2 mediante AWS SSM Agent) más la integración de Defender for Endpoint y el análisis sin agente. Límites: AWS carece de alertas y evaluación de red; Google Cloud además carece de Just-in-time VM access y Cloud security explorer; los servidores locales con Arc no tienen Just-in-time, alertas de red ni evaluación de cifrado de disco. | 2026-06-17 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-servers |
| MS-NUB-03 | Defender for Containers | AKS, EKS y GKE se cubren con el sensor de Defender, acceso a la API de Kubernetes y a los registros (ACR, ECR, Google Artifact Registry y Container Registry). Límites: sin protección en tiempo de ejecución para clústeres privados de EKS ni para GKE de red privada o Autopilot; en Kubernetes con Arc la detección está en versión preliminar y sin rutas de ataque; en SaaS solo los registros Docker Hub y JFrog Artifactory. | 2026-07-01 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/support-matrix-defender-for-containers |
| MS-NUB-04 | Defender for Cloud: servicios de plataforma | En el conector de AWS solo se ofrecen dos planes de este grupo: Defender for SQL (SQL Server en EC2 y RDS Custom for SQL Server, con Azure Arc) y Defender for open-source relational databases (Amazon RDS: Aurora PostgreSQL/MySQL, PostgreSQL, MySQL, MariaDB). Storage, App Service, Key Vault, Resource Manager y APIs no aparecen para AWS; el alcance en Google Cloud no se detalla. | 2026-08-04 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/quickstart-onboard-aws |
| MS-NUB-05 | DevOps security de Defender for Cloud | Protege plataformas DevOps con conectores para Azure DevOps Services, GitHub Enterprise Cloud y GitLab SaaS; no se listan ediciones autoalojadas. Límites: GitLab tiene menos funciones (sin inventario, anotaciones de pull request ni mapeo código-nube, y exige GitLab Ultimate); las rutas de ataque requieren Defender CSPM en una suscripción de Azure o conector de AWS o Google Cloud del mismo inquilino. | 2026-09-18 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/devops-support |
| MS-NUB-06 | Azure Arc, Azure Policy y Azure Update Manager | El agente Azure Connected Machine proyecta en Azure servidores Windows y Linux físicos o virtuales alojados fuera de Azure; sobre ellos se asignan machine configurations para auditar la configuración y se gestionan parches con Azure Update Manager. Arc-enabled Kubernetes admite clústeres certificados por CNCF en AWS, Google Cloud o local, con Azure Policy y GitOps. Límite: requiere conectividad; una máquina desconectada 45 días caduca. | 2026-02-26 | https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview |
| MS-APP-01 | Microsoft Defender for Cloud Apps | Cubre SaaS de terceros con conectores por API, descubrimiento a partir del tráfico de red, SSPM y app governance para aplicaciones OAuth; las capacidades varían por aplicación. AWS: supervisa actividad administrativa y de inicio de sesión y descubre buckets S3, sin SSPM. Google Cloud: solo registros de auditoría Admin Activity, sin SSPM. | 2026-07-03 | https://learn.microsoft.com/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps |
| MS-EXP-01 | Microsoft Security Exposure Management | Azure, AWS y Google Cloud entran a través de Microsoft Defender for Cloud (no hay conectores propios de AWS o GCP en el catálogo). Lo local depende de Defender for Endpoint e Identity o de los conectores externos en versión preliminar (ServiceNow CMDB, Qualys, Rapid7, Tenable, Wiz, Palo Alto Prisma; Armis, Dragos y Forescout para OT). | 2026-07-07 | https://learn.microsoft.com/en-us/security-exposure-management/overview-data-connectors |
| MS-EXP-02 | Microsoft Defender External Attack Surface Management | Descubre desde fuera, sin agente ni conector y a partir de semillas, dominios, bloques IP, hosts, ASN y contactos Whois. Límite: solo ve activos expuestos a Internet, con independencia de la nube donde estén; la página no enumera nubes concretas. | 2026-04-24 | https://learn.microsoft.com/en-us/azure/external-attack-surface-management/overview |
| MS-IAA-01 | Microsoft Agent 365 | El registro incluye agentes de Microsoft, de socios y propios; los de terceros se incorporan con «Connected platforms» (Amazon Bedrock Agents, Google Vertex AI, Salesforce Agentforce, Databricks Genie, Anthropic Claude Managed Agents, Oracle, Snowflake Cortex). Límite: conexión de solo lectura, sincronización manual con credenciales con clave, y la observabilidad de Oracle y Snowflake figura como «Coming soon». | 2026-11-12 | https://learn.microsoft.com/en-us/microsoft-agent-365/overview |
| MS-IAA-02 | Defender for Cloud: postura de IA y Defender for AI Services | La postura descubre cargas de IA en Azure OpenAI, Microsoft Foundry, Azure Machine Learning y Amazon Bedrock mediante los conectores de nube de Defender for Cloud. Límite: la protección frente a amenazas (Defender for AI Services) es solo para Azure, sin soporte en AWS ni Google Cloud. | 2026-06-17 | https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture |
| MS-IAA-03 | Protecciones de Microsoft Purview para IA generativa | ChatGPT Enterprise y Anthropic Claude Enterprise se tratan como «Enterprise AI apps», igual que Microsoft Foundry y las apps registradas en Entra. ChatGPT de consumo, Gemini o DeepSeek solo se cubren como «Other AI apps», con Endpoint DLP en equipos incorporados o Network Data Security vía Global Secure Access o un SASE de terceros. | 2026-05-27 | https://learn.microsoft.com/en-us/purview/ai-microsoft-purview |
| MS-IAA-04 | Controles de seguridad de Microsoft Foundry | Azure AI Content Safety se ofrece como servicio independiente (API) para modelos y agentes fuera de Foundry o repartidos en varias plataformas. Límite: la aplicación debe llamar a la API de un recurso de Azure (no se nombran AWS ni Google Cloud), y el AI Red Teaming Agent no admite agentes ni herramientas ajenos a Foundry o Azure. | 2026-11-06 | https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview |
| MS-ASI-01 | Microsoft Security Copilot | Llega a productos de terceros mediante complementos no Microsoft (p. ej., ServiceNow, Splunk, Netskope, CyberArk, Tanium, Darktrace, Jamf) y complementos personalizados; los agentes de socios se obtienen en Security Store. Límite: esos productos se licencian aparte y no se documentan complementos de AWS ni Google Cloud. | 2026-06-19 | https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion |
| MS-RED-01 | Global Secure Access (Entra Internet Access y Private Access) | Private Access da acceso sin VPN a aplicaciones privadas en entornos híbridos y multinube mediante el cliente Global Secure Access y el conector de red privada de Microsoft Entra; Internet Access protege el tráfico a Internet y SaaS con una puerta de enlace web segura basada en identidad. Límite: el despliegue nativo del conector en otras nubes sigue en versión preliminar. | 2026-04-15 | https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access |
| MS-RED-02 | Azure Firewall, Web Application Firewall y DDoS Protection | Solo protegen recursos externos si el tráfico entra por un servicio de Azure: Azure Front Door admite orígenes locales o de otro proveedor de nube, y DDoS Protection cubre un Application Gateway en Azure con sitios locales detrás. Límite: DDoS Protection solo protege IP públicas en redes virtuales de Azure, y Azure Firewall se describe solo para cargas de Azure. | 2025-09-25 | https://learn.microsoft.com/en-us/azure/frontdoor/origin |
| MS-RED-03 | Segmentación y acceso privado en Azure | Bastion conecta por IP a máquinas locales o de otras nubes alcanzables por ExpressRoute o VPN (SKU Standard o superior), y los puntos de conexión privados son accesibles desde local por VPN o ExpressRoute. Límite: grupos de seguridad de red, Network Security Perimeter y Virtual Network Manager solo gobiernan redes y recursos PaaS de Azure. | 2026-03-11 | https://learn.microsoft.com/en-us/azure/bastion/connect-ip-address |
| MS-RED-04 | Microsoft Defender for IoT | Supervisa redes OT/ICS sin agente mediante sensores de red instalados en las instalaciones del cliente, conectados a la nube, aislados (air-gapped) o híbridos; Azure actúa como plano de gestión. Límite: no protege cargas en AWS, Google Cloud ni SaaS; su ámbito es la planta. | 2026-06-24 | https://learn.microsoft.com/en-us/azure/defender-for-iot/organizations/overview |
| MS-RED-05 | Azure Key Vault y Managed HSM | Fuera de Azure se documentan la importación de claves desde HSM locales (BYOK) y la administración de claves externas de Managed HSM, donde la clave de cifrado de claves permanece en un HSM del cliente. Límite: ambos mecanismos sirven al cifrado en reposo de servicios de Azure; no se describe el consumo desde cargas en AWS o Google Cloud. | 2026-09-22 | https://learn.microsoft.com/en-us/azure/key-vault/general/overview |
| MS-RES-01 | Azure Backup | Fuera de Azure respalda cargas locales mediante agentes: MARS para archivos, carpetas y estado del sistema en Windows, y MABS o System Center DPM para Hyper-V, VMware y aplicaciones. Límite: la documentación solo nombra máquinas locales y de Azure, sin AWS ni Google Cloud, y no incluye aplicaciones SaaS. | 2026-09-16 | https://learn.microsoft.com/en-us/azure/backup/backup-overview |
| MS-RES-02 | Azure Site Recovery | Replica hacia Azure máquinas VMware y Hyper-V, servidores físicos Windows y Linux y Azure Stack, con el dispositivo de replicación y el servicio Mobility. Límite: para AWS la información general solo declara instancias Windows (tratadas como servidores físicos) y Google Cloud no aparece. | 2026-10-15 | https://learn.microsoft.com/en-us/azure/site-recovery/vmware-physical-azure-support-matrix |
| MS-RES-03 | Microsoft 365 Backup | Solo respalda datos de Microsoft 365 (sitios de SharePoint, cuentas de OneDrive y buzones de Exchange Online) dentro del límite de servicio de Microsoft 365. Límite: no cubre SaaS de terceros; los socios pueden construir soluciones sobre Microsoft 365 Backup Storage. | 2026-11-04 | https://learn.microsoft.com/en-us/microsoft-365/backup/backup-overview |
| MS-CUM-01 | Microsoft Purview Compliance Manager | Evalúa Microsoft 365, Azure, AWS y Google Cloud con pruebas automáticas a nivel de recurso mediante la integración con Microsoft Defender for Cloud. Límite: en SaaS solo hay conectores para Salesforce y Zoom (y Corporate Sustainability); el resto se evalúa con plantillas universales y pruebas manuales. | 2025-09-26 | https://learn.microsoft.com/en-us/purview/compliance-manager-multicloud |
| MS-CUM-02 | Microsoft Purview Audit y eDiscovery | eDiscovery alcanza datos de terceros solo cuando se importan a buzones de Microsoft 365 con conectores de datos (nativos o de socios como TeleMessage, 17a-4 y CellTrust). Límite: Audit registra operaciones de servicios de Microsoft y no se confirma auditoría de servicios de terceros. | 2026-06-04 | https://learn.microsoft.com/en-us/purview/archive-third-party-data |
| MS-CUM-03 | Microsoft Purview Data Lifecycle Management y Records Management | Las directivas y etiquetas de retención y la declaración de registros se aplican a datos de terceros solo después de importarlos a buzones de Microsoft 365 mediante conectores de datos. Límite: no gobiernan los datos en su origen (AWS, Google Cloud o la aplicación SaaS). | 2026-06-04 | https://learn.microsoft.com/en-us/purview/archive-third-party-data |
| MS-CUM-04 | Microsoft Purview Communication Compliance e Information Barriers | Communication Compliance analiza comunicaciones de fuentes no Microsoft (Instant Bloomberg, Slack, Zoom, SMS, WhatsApp, entre otras) importadas con conectores de datos, e interacciones con IA generativa de terceros. Límite: Information Barriers solo restringe Microsoft Teams, SharePoint, OneDrive y Planner, sin fuentes de terceros ni correo. | 2025-08-28 | https://learn.microsoft.com/en-us/purview/communication-compliance-channels |
| MS-CUM-05 | Microsoft Priva | La página vigente describe la evaluación de datos personales en Exchange Online, SharePoint Online, OneDrive y Teams, y menciona orígenes registrados en Microsoft Purview sin decir cuáles. Límite: la cobertura fuera de Microsoft 365 no se puede confirmar. | 2026-05-11 | https://learn.microsoft.com/en-us/privacy/priva/priva-overview |

## 6. Cobertura por función

La cobertura de una función es la mejor entre sus capacidades: indica que al menos una capacidad alcanza el entorno.

| ID | Función | Microsoft 365 | Azure | AWS | Google Cloud | Centro de datos | SaaS de terceros | Estado con todos los entornos en el alcance |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| GOB-G2.1 | Marcos, estándares y grilla de propiedad | Sí | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GOB-G2.2 | Políticas, estándares y procedimientos | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| GOB-G3.1 | Requisitos legales, regulatorios y contractuales | Sí | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GOB-G3.2 | Cumplimiento y aseguramiento continuo | Sí | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GOB-G5.1 | Supervisión de la evaluación y el análisis de riesgos | No aplica | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GOB-G5.2 | Supervisión del tratamiento y la aceptación de riesgos | No aplica | Sí | Sí | Sí | Sí | Parcial | Parcial |
| GOB-G6.1 | Comunicación estratégica y reporte a la dirección | Sí | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GES-M1.1 | Programa de seguridad y portafolio de productos-control | Sí | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GES-M2.1 | Activos, datos y protección de datos personales | Sí | Sí | Parcial | Parcial | Sí | Sí | Parcial |
| GES-M2.2 | Gestión de identidades y accesos | Sí | Sí | Parcial | Parcial | Sí | Sí | Parcial |
| GES-M3.1 | Arquitectura de seguridad e ingeniería (Zero Trust) | No aplica | Sí | Sí | Sí | Parcial | Parcial | Parcial |
| GES-M3.2 | Selección, implementación y evaluación de controles | Sí | Sí | Sí | Sí | Sí | Parcial | Parcial |
| GES-M4.1 | Gestión de las operaciones de seguridad | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes | Sí | Sí | Sí | Sí | Sí | Parcial | Parcial |
| GES-M5.1 | Preparación de la respuesta a incidentes | Sí | Sí | Parcial | No confirmado | Parcial | Sí | Requiere complemento o verificación |
| GES-M5.2 | Conducción de la respuesta y aprendizaje | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| GES-M6.1 | Continuidad, recuperación y resiliencia | Sí | Sí | Parcial | No confirmado | Sí | No | Requiere complemento o verificación |
| GES-M6.2 | Nube, tecnologías emergentes y cadena de suministro | Sí | Sí | Sí | Parcial | Parcial | Parcial | Parcial |
| OPE-ID-01 | Inventario y descubrimiento de activos | No aplica | Sí | Sí | Sí | Sí | Parcial | Parcial |
| OPE-ID-02 | Gestión de vulnerabilidades y de la exposición | No aplica | Sí | Sí | Sí | Sí | Parcial | Parcial |
| OPE-ID-03 | Postura de nube y de configuración | Sí | Sí | Sí | Sí | Sí | Parcial | Parcial |
| OPE-ID-04 | Evaluación de riesgo de terceros | Sí | Sí | Parcial | Parcial | Parcial | Parcial | Parcial |
| OPE-ID-05 | Pruebas ofensivas y validación de controles | Sí | Sí | Sí | Sí | Parcial | No confirmado | Requiere complemento o verificación |
| OPE-ID-06 | Descubrimiento y clasificación de datos | Sí | Sí | Parcial | Parcial | Sí | Sí | Parcial |
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes | Sí | Sí | Parcial | Parcial | No confirmado | Parcial | Requiere complemento o verificación |
| OPE-PR-01 | Identidades y accesos de las personas | Sí | Sí | Parcial | Parcial | Sí | Sí | Parcial |
| OPE-PR-02 | Acceso privilegiado | Sí | Sí | Parcial | Parcial | Parcial | Sí | Parcial |
| OPE-PR-03 | Identidades no humanas, de cargas y de agentes | Sí | Sí | Parcial | Parcial | Parcial | Parcial | Parcial |
| OPE-PR-04 | Protección y gestión de dispositivos | No aplica | Sí | Sí | Sí | Sí | No aplica | Cubierta |
| OPE-PR-05 | Protección del correo y la colaboración | Sí | No aplica | No aplica | No aplica | Parcial | No confirmado | Requiere complemento o verificación |
| OPE-PR-06 | Protección de datos | Sí | Parcial | Parcial | No confirmado | Sí | Sí | Requiere complemento o verificación |
| OPE-PR-07 | Seguridad de aplicaciones y del desarrollo | Sí | Sí | Parcial | Parcial | Parcial | Parcial | Parcial |
| OPE-PR-08 | Seguridad de red y segmentación | No aplica | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-PR-09 | Protección de cargas e infraestructura de nube | No aplica | Sí | Sí | Sí | Sí | Parcial | Parcial |
| OPE-PR-10 | Concientización y cultura de seguridad | Sí | No aplica | No aplica | No aplica | Parcial | No confirmado | Requiere complemento o verificación |
| OPE-PR-11 | Protección de sistemas de IA y agentes | Sí | Sí | Parcial | Parcial | Parcial | Parcial | Parcial |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados | No aplica | No aplica | No aplica | No aplica | Sí | No aplica | Cubierta |
| OPE-DE-01 | Monitoreo continuo y gestión de alertas | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-DE-02 | Ingeniería y calidad de la detección | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-DE-03 | Búsqueda proactiva de amenazas | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-DE-04 | Inteligencia de amenazas | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-DE-05 | Gestión de registros y telemetría | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-DE-06 | Observabilidad de IA y agentes | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-RS-01 | Gestión y coordinación de incidentes | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-RS-02 | Análisis e investigación forense | Sí | Sí | Sí | Sí | Sí | Parcial | Parcial |
| OPE-RS-03 | Contención, erradicación y respuesta automatizada | Sí | Sí | Sí | Sí | Sí | Sí | Cubierta |
| OPE-RS-04 | Comunicación y notificación de incidentes | Sí | Sí | Parcial | No confirmado | Parcial | Parcial | Requiere complemento o verificación |
| OPE-RC-01 | Respaldo y restauración | Sí | Sí | No confirmado | No confirmado | Sí | No | Requiere complemento o verificación |
| OPE-RC-02 | Recuperación de servicios críticos | No aplica | Sí | Parcial | No confirmado | Sí | No | Requiere complemento o verificación |
| OPE-RC-03 | Recuperación de la identidad y de la plataforma de control | Sí | Sí | Parcial | Parcial | Sí | Sí | Parcial |

| Estado con todos los entornos en el alcance | Funciones |
|---|:--:|
| Cubierta | 14 |
| Parcial | 26 |
| Requiere complemento o verificación | 10 |
| Sin capacidad asociada | 9 |
| Total | 59 |

En el libro, el estado se recalcula según los entornos que la organización marque en el alcance.

## 7. Dónde hace falta complemento o verificación

### AWS (1)

| ID | Función | Cobertura | Qué queda fuera |
|---|---|---|---|
| OPE-RC-01 | Respaldo y restauración | No confirmado | Respaldo de cargas en AWS, en Google Cloud y en SaaS de terceros. |

### Google Cloud (6)

| ID | Función | Cobertura | Qué queda fuera |
|---|---|---|---|
| GES-M5.1 | Preparación de la respuesta a incidentes | No confirmado | Plan de respuesta, roles, contactos y ejercicios. |
| GES-M6.1 | Continuidad, recuperación y resiliencia | No confirmado | Análisis de impacto, objetivos de recuperación y cargas en otras nubes. |
| OPE-PR-06 | Protección de datos | No confirmado | Datos en almacenes de otras nubes y en aplicaciones sin conector. |
| OPE-RS-04 | Comunicación y notificación de incidentes | No confirmado | Criterios, plazos y registro de notificaciones. |
| OPE-RC-01 | Respaldo y restauración | No confirmado | Respaldo de cargas en AWS, en Google Cloud y en SaaS de terceros. |
| OPE-RC-02 | Recuperación de servicios críticos | No confirmado | Recuperación de servicios alojados en otras nubes. |

### Centro de datos (1)

| ID | Función | Cobertura | Qué queda fuera |
|---|---|---|---|
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes | No confirmado | Agentes y modelos de plataformas no conectadas. |

### SaaS de terceros (6)

| ID | Función | Cobertura | Qué queda fuera |
|---|---|---|---|
| GES-M6.1 | Continuidad, recuperación y resiliencia | No | Análisis de impacto, objetivos de recuperación y cargas en otras nubes. |
| OPE-ID-05 | Pruebas ofensivas y validación de controles | No confirmado | Pruebas de penetración, ejercicios de equipo rojo y validación continua de controles. |
| OPE-PR-05 | Protección del correo y la colaboración | No confirmado | Correo y colaboración fuera de Microsoft 365. |
| OPE-PR-10 | Concientización y cultura de seguridad | No confirmado | Programa de cultura, formación por función y red de referentes. |
| OPE-RC-01 | Respaldo y restauración | No | Respaldo de cargas en AWS, en Google Cloud y en SaaS de terceros. |
| OPE-RC-02 | Recuperación de servicios críticos | No | Recuperación de servicios alojados en otras nubes. |

## 8. Hallazgos de la verificación

1. Microsoft Sentinel es la puerta de entrada documentada de señales de AWS (S3/CloudTrail, GuardDuty, VPC Flow Logs), Google Cloud (Pub/Sub), centro de datos (Arc/AMA, Syslog/CEF) y SaaS a Defender XDR; Defender XDR por sí solo correlaciona solo productos Microsoft licenciados.
2. Microsoft Sentinel deja de tener soporte en Azure portal después de 2027-03-31 y queda solo en el portal de Microsoft Defender.
3. La postura multinube (CSPM, Defender for Servers, Defender for Containers) cubre Azure, AWS y Google Cloud, pero Google Cloud tiene menos funciones que AWS, y el cumplimiento regulatorio y las rutas de ataque exigen Defender CSPM (de pago).
4. Los planes de Defender for Cloud para servicios de plataforma son esencialmente de Azure; en AWS solo constan Defender for SQL y bases relacionales de código abierto en RDS. Defender for AI Services (protección de amenazas de IA) no admite AWS ni Google Cloud.
5. Azure Arc es el requisito común para servidores y Kubernetes fuera de Azure (Defender for Servers, Azure Policy, machine configuration, Update Manager).
6. La identidad llega a AWS, Google Cloud y SaaS por federación (SSO, Conditional Access, aprovisionamiento SCIM); PIM y ID Governance no gobiernan roles IAM nativos de AWS ni de Google Cloud.
7. Microsoft Entra Agent ID y Microsoft Agent 365 aceptan agentes de terceros (Amazon Bedrock, Google Vertex AI, Salesforce, etc.), con integración explícita, sincronización manual y licencia de Agent 365 (requerida también para la postura de agentes desde 2026-07-01).
8. Retiros con fecha: Unified Catalog y gobierno de datos clásico de Purview en mantenimiento hasta 2027-11-12; file policies de Defender for Cloud Apps el 2027-01-06; Azure Front Door (classic) el 2027-03-31; Site Recovery bloqueará Windows sin soporte desde 2027-03-01; páginas independientes de Defender Threat Intelligence retiradas desde 2026-08-01; consola de administración local de Defender for IoT retirada el 2025-01-01.
9. Purview cubre datos de terceros por conectores e importación a Microsoft 365 (eDiscovery, retención, Communication Compliance) o por Defender for Cloud Apps y socios (etiquetas, DLP, DSPM); no gobierna almacenes IaaS de AWS o Google Cloud en origen, salvo Amazon S3 en Insider Risk Management y el escaneo de Data Map (en retiro).
10. La resiliencia fuera de Microsoft es limitada: Azure Backup y Microsoft 365 Backup no declaran AWS, Google Cloud ni SaaS de terceros; Site Recovery solo cita instancias Windows de AWS.
11. Cinco productos tienen guía de operación oficial con cadencias explícitas (Defender for Office 365, Defender for Endpoint, Defender for Identity, Defender for Cloud Apps, Microsoft Sentinel) y Defender XDR las incluye en su guía de integración con el SOC; solo Defender for Identity usa cadencia trimestral.
12. Security Copilot se incluye en Microsoft 365 E5 y E7 (despliegue desde 2025-11-18, 400 SCU al mes por cada 1.000 licencias, hasta 10.000).

## 9. Qué hacer con esto

| Situación | Acción |
|---|---|
| Servidores y clústeres fuera de Azure | Incorporarlos con Azure Arc: es el requisito común para extender la protección, la línea base y la actualización. |
| Señales de AWS, de Google Cloud y de terceros | Ingresarlas por los conectores de Microsoft Sentinel. Defender XDR correlaciona por sí solo solo productos de Microsoft. Presupuestar la ingesta. |
| Identidades | Federar AWS, Google Cloud y las aplicaciones SaaS con Microsoft Entra. Las identidades nativas de esas nubes (cuenta raíz, usuarios locales, cuentas de servicio) se gobiernan con las herramientas de cada nube. |
| Servicios de plataforma de otras nubes | Usar los controles nativos de cada nube e integrar sus hallazgos a la telemetría central. Los planes de Defender for Cloud para servicios de plataforma son casi solo de Azure. |
| Respaldo y recuperación de cargas en otras nubes | Resolverlo fuera de la plataforma: la documentación no confirma esa cobertura. |
| Datos en almacenes de otras nubes | Verificar el conector de cada origen: Purview no gobierna en origen la mayoría de los almacenes de infraestructura de otras nubes. |
| Toda celda «No confirmado» | Probarla en el entorno propio antes de comprometer un resultado clave que dependa de ella, y anotar el resultado en el libro. |

## 10. Lo que no pudo confirmarse

1. PIM: no hay documentación de gobierno nativo de roles de Google Cloud, de AWS IAM ni de Active Directory local, ni anuncio de PIM multinube.
2. Defender for Identity: no se documentan controladores de dominio en VM de AWS o Google Cloud ni proveedores de identidad distintos de Okta.
3. Intune: no se aclara si administra VM Windows cliente en AWS o Google Cloud, ni si BitLocker, Windows LAPS y App Control aplican a Windows Server.
4. Defender for Office 365: no se confirma protección de Plan 1/Plan 2 para buzones locales ni para correo en la nube de terceros.
5. Contradicciones entre páginas oficiales: etiquetado de AWS RDS en Data Map; postura de IA en Google Vertex AI (página de postura frente a matriz multinube).
6. DSPM: no se nombra AWS ni se enumeran las aplicaciones de IA de terceros cubiertas; la página no muestra fecha.
7. Microsoft Sentinel data lake: la página abierta no declara su estado de disponibilidad.
8. Automatización de Sentinel: no se documentan acciones concretas sobre AWS, Google Cloud o sistemas locales.
9. Defender for Cloud: no se detalla qué planes de servicios de plataforma se pueden activar en el conector de Google Cloud.
10. Defender EASM: no se encontró estado ni aviso de retiro; la página de novedades no pudo abrirse.
11. Exposure Management: sin estado ni precio por conector para la disponibilidad general.
12. Azure Backup y Site Recovery: no se aclara el soporte de MARS/MABS en VM de AWS o Google Cloud ni de Site Recovery desde Google Cloud.
13. Azure Key Vault: no se describe el uso desde cargas en AWS o Google Cloud.
14. Microsoft Priva: no hay página oficial abierta con fechas de retiro de Subject Rights Requests, Consent Management, Privacy Assessments y Tracker Scanning; la cobertura fuera de Microsoft 365 no se confirma.
15. Guías de operación: Microsoft Intune y Microsoft Purview (protección de la información y DLP) no tienen guía de operación oficial con cadencias; Defender for Cloud y Microsoft Entra tienen guías sin tabla de cadencias (las secciones de identidad, autenticación y gobierno de la guía de Entra no se abrieron).
16. Zero Trust Workshop: sin página en dominios oficiales admitidos (solo microsoft.github.io).

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

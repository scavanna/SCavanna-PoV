# Catálogo de seguridad Microsoft — edición validada

**Fecha de revisión: 4 de noviembre de 2026.** Revisión íntegra del inventario adjunto: 15 tablas originales, incluidas sus 19 filas Entra, 18 Defender, 20 Purview, 12 Intune, 22 Windows, 15 Defender for Cloud, 29 Azure, 38 etiquetas de mercado, 29 correspondencias consolidadas, 9 servicios, 19 capacidades de la comparación de licencias y 8 relaciones Atlas. Se han corregido nombres, tipos, alcances y fechas. Las categorías Gartner se conservan como etiquetas de trabajo, **no como mercados o participaciones certificados**. **Uso: catálogo funcional, no contrato de licencias.** Fuentes oficiales indexadas en el anexo.

Santiago, para construir un **catálogo del stack de seguridad Microsoft cruzado con Gartner Peer Insights 2026**, conviene separar tres elementos:

1. **Tecnologías y capacidades Microsoft:** qué existe y qué función cumple.
2. **Mercados de Gartner Peer Insights:** cómo se agrupan las soluciones que evalúan los compradores.
3. **Correspondencias:** qué producto o servicio Microsoft cubre cada mercado, de forma completa, parcial o complementaria.

Esto también puede convertirse en una nueva dimensión del grafo del **AI CISO Atlas**: `Technology → ProvidesCapability → MarketCategory`.

La investigación confirma que Microsoft 365 E7 incorpora E5, Copilot, Agent 365 y Entra Suite; pero **no debemos interpretar E7 como una licencia universal de todos los servicios de seguridad de Azure**. [[microsoft.com\]](https://www.microsoft.com/en-us/microsoft-365/enterprise/e7), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

# 1. Inventario de tecnologías de seguridad Microsoft — revisado

## A. Microsoft Entra — Identidad y acceso

Fuentes por entrada: licencias [S01] y perfiles de acceso [S02].

| Tecnología                           | Descripción breve                                            | Disponibilidad orientativa    |
| ------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| Microsoft Entra ID                   | Directorio e identidad empresarial, autenticación y autorización | E3/E5/E7                      |
| Entra ID P1                          | Conditional Access y administración avanzada de identidad    | E3/E5/E7                      |
| Entra ID P2                          | Protección de identidad basada en riesgo y capacidades privilegiadas | E5/E7                         |
| Entra Conditional Access | Políticas de acceso contextual; las basadas en riesgo requieren P2 | P1 en E3/E5/E7; riesgo P2 en E5/E7; agentes requieren Agent 365 |
| Entra ID Protection                  | Detección y respuesta ante riesgos de identidad              | E5/E7                         |
| Entra Privileged Identity Management | Acceso privilegiado just-in-time                             | E5/E7                         |
| Entra ID Governance                  | Ciclo de vida, revisiones y paquetes de acceso               | E7 / Add-on                   |
| Entra Lifecycle Workflows            | Automatización de altas, movimientos y bajas                 | E7 / Add-on                   |
| Entra Entitlement Management | Paquetes y solicitudes de acceso, con funciones diferenciadas por plan | P2/E5 para funciones base; ID Governance/Entra Suite/E7 para ampliaciones |
| Entra Access Reviews | Revisiones de acceso, con funciones diferenciadas por plan | P2/E5 funciones base; ID Governance/Entra Suite/E7 ampliaciones |
| Entra Workload ID | Identidades de cargas de trabajo y principales de servicio; no confundir con identidades administradas Azure | Producto por identidad de carga de trabajo/mes; identidades administradas Azure sin licencia adicional |
| Entra Agent ID | Identidades de agentes; extender controles de seguridad a agentes requiere Agent 365 | Plataforma para clientes Entra; seguridad extendida: Agent 365, incluido en E7 |
| Entra External ID | Identidad externa de clientes y socios | Primeros 50,000 usuarios activos mensuales de funciones principales gratuitos; resto según modelo External ID |
| Entra Verified ID | Credenciales verificables; Face Check es función premium | Funciones básicas incluso con Entra Free; Face Check add-on o Entra Suite/E7 |
| Entra Internet Access | Secure Web Gateway para Internet/SaaS; perfil Microsoft services distinto | Producto independiente o Entra Suite/E7; perfil Microsoft services con P1/P2 |
| Entra Private Access                 | Zero Trust Network Access para aplicaciones privadas         | E7 / Add-on                   |
| Entra Global Secure Access | Nombre unificador de Internet Access y Private Access, no tercer SKU | Derechos por perfil: P1/P2 para servicios Microsoft; suite o SKU para Internet/Private |
| Microsoft Authenticator              | Autenticación multifactor y passwordless                     | Capacidades base y avanzadas  |
| Windows Hello for Business           | Autenticación empresarial resistente al phishing             | Windows / Entra               |

Microsoft documenta Entra ID, Agent ID, ID Governance, External ID, Internet Access, Private Access, Verified ID y Workload ID como componentes diferenciados. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/entra/), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/entra/architecture/deployment-scenario-intro)

## B. Microsoft Defender — Protección y operaciones

Fuentes por entrada: planes [S05], correo [S07], IoT [S09], inteligencia [S12], Copilot [S13] y Experts [S14].

| Tecnología                                            | Descripción breve                                            | Disponibilidad orientativa  |
| ----------------------------------------------------- | ------------------------------------------------------------ | --------------------------- |
| Microsoft Defender XDR                                | Correlación de amenazas entre endpoints, identidades, correo y aplicaciones | E5/E7                       |
| Defender for Endpoint P1                              | Prevención y reducción de superficie de ataque               | E3                          |
| Defender for Endpoint P2                              | EDR, investigación y respuesta avanzadas                     | E5/E7                       |
| Microsoft Defender Antivirus                          | Antivirus y protección antimalware                           | Windows                     |
| Defender Vulnerability Management                     | Evaluación y priorización de vulnerabilidades                | Capacidades base / Add-on   |
| Defender for Office 365 P1 | Protección avanzada de correo y colaboración | Office 365 E3 y Microsoft 365 E3 desde 1 de julio de 2026 |
| Defender for Office 365 P2                            | Investigación, automatización y protección avanzada          | E5/E7                       |
| Exchange Online Protection                            | Protección antispam y antimalware del correo                 | Exchange Online             |
| Defender for Identity                                 | Detección de ataques a identidades híbridas                  | E5/E7                       |
| Defender for Cloud Apps                               | CASB, descubrimiento y control de aplicaciones cloud         | E5/E7                       |
| Defender for IoT | IoT empresarial y OT son modalidades de licencia distintas | E5: cinco dispositivos IoT empresariales por licencia de usuario; OT por sitio; ampliaciones aparte |
| Microsoft Security Exposure Management                | Análisis unificado de exposición y rutas de ataque           | Según capacidades/licencias |
| Microsoft Defender External Attack Surface Management | Descubrimiento de activos expuestos a Internet               | Separado                    |
| Microsoft Defender Threat Intelligence | Inteligencia de amenazas integrada en Defender y Sentinel; SKU independiente retirada | SKU independiente MDTI terminada el 1 de agosto de 2026 |
| Microsoft Security Copilot | Producto de IA de seguridad y operaciones | E5/E7 elegibles: 400 SCU/mes por 1,000 licencias pagadas, máximo 10,000 SCU/mes |
| Defender Experts MDR                                  | Detección y respuesta administradas por expertos             | Servicio separado           |
| Defender Experts Hunting                              | Threat hunting administrado                                  | Servicio separado           |
| Defender Experts Cybersecurity Incident Response      | Preparación y respuesta ante incidentes                      | Servicio separado           |

Microsoft diferencia explícitamente Defender for Endpoint, Office 365, Identity, Cloud Apps, Vulnerability Management, IoT, Sentinel y Defender for Cloud. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender/), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview)

## C. Microsoft Purview — Seguridad, gobierno y cumplimiento de datos

Fuentes por entrada: [S15][S16][S17][S18][S19][S20].

| Tecnología                               | Descripción breve                                     | Disponibilidad orientativa |
| ---------------------------------------- | ----------------------------------------------------- | -------------------------- |
| Purview Information Protection           | Clasificación, etiquetado y cifrado de información    | E3/E5/E7                   |
| Sensitivity Labels                       | Etiquetas de sensibilidad y protección                | E3+                        |
| Automatic Labeling                       | Clasificación y etiquetado automatizado               | E5/E7 / Add-on             |
| Purview Data Loss Prevention             | Prevención de fuga de información                     | E3/E5/E7                   |
| Endpoint DLP                             | Protección de información en dispositivos             | E5/E7 / Add-on             |
| Purview Data Security Posture Management | Visibilidad y evaluación de exposición de datos       | Según oferta y consumo     |
| Purview Data Security Investigations | Investigación de incidentes de datos con análisis de IA | Pago por uso de almacenamiento GB/mes y capacidad de IA; sin licencia empresarial dedicada |
| Purview Insider Risk Management          | Detección e investigación de riesgos internos         | E5/E7                      |
| Purview Information Barriers             | Restricción de colaboración entre grupos              | E5/E7                      |
| Purview Communication Compliance         | Supervisión de comunicaciones sujetas a políticas     | E5/E7                      |
| Purview Audit (Standard) | Registro y búsqueda; retención estándar 180 días | E3/E5/E7; [S19] |
| Purview Audit (Standard) | Registro y búsqueda; retención estándar 180 días | E3/E5/E7; [S19] |
| Purview eDiscovery                       | Investigación y obtención de evidencia electrónica    | E3/E5/E7                   |
| Purview Data Lifecycle Management        | Retención y eliminación de información                | E3/E5/E7                   |
| Purview Records Management               | Gestión avanzada de registros                         | E5/E7                      |
| Purview Compliance Manager               | Evaluación y seguimiento de controles de cumplimiento | Capacidades base / Add-on  |
| Purview Data Map | Mapa de datos/metadatos; distinguir gobierno actual y experiencia clásica | No todo escaneo es consumo facturable; revisar modelo de gobierno |
| Purview Unified Catalog | Curación y gobierno de datos | Activos únicos gobernados/día; calidad/salud mediante DGPU |
| Purview Data Estate Insights | Denominación clásica; usar informes/salud de Unified Catalog para experiencias actuales | Función histórica; no SKU separado |
| Purview Data Security for AI | Conjunto de controles para datos usados por IA; no SKU único | Según control y fuente; interacciones no M365 pueden facturarse por consumo |

**Importante:** Microsoft Purview es una familia que incluye tanto seguridad y cumplimiento de Microsoft 365 como gobierno de datos en Azure y otros entornos. No todos sus componentes están incluidos en E5. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/purview/purview-compliance), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/purview/purview-security), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/purview/purview)

------

# 2. Microsoft Intune y seguridad incorporada en Windows

Estas capacidades son especialmente importantes porque un inventario limitado a productos Defender omitiría controles fundamentales.

## A. Microsoft Intune

Desde julio de 2026 E3 incluye Plan 2, Remote Help y Advanced Analytics; E5/E7 agregan EPM, Cloud PKI y Enterprise Application Management. No implica Suite íntegra. [S21]

| Tecnología                               | Descripción                                          |
| ---------------------------------------- | ---------------------------------------------------- |
| Intune Plan 1                            | Gestión de dispositivos y aplicaciones               |
| Intune Suite                             | Capacidades avanzadas de administración y seguridad  |
| Intune Endpoint Privilege Management     | Administración de elevaciones de privilegios locales |
| Intune Enterprise Application Management | Administración de aplicaciones empresariales         |
| Intune Advanced Analytics                | Análisis avanzado de dispositivos                    |
| Intune Remote Help                       | Asistencia remota administrada                       |
| Intune Cloud PKI                         | Infraestructura de certificados administrada         |
| Intune Mobile Application Management     | Protección de datos en aplicaciones móviles          |
| Intune Compliance Policies               | Evaluación de cumplimiento de dispositivos           |
| Intune Endpoint Security Policies        | Administración de antivirus, firewall y cifrado      |
| Windows Autopilot                        | Aprovisionamiento de dispositivos                    |
| Windows Autopatch                        | Gestión automatizada de actualizaciones              |

Intune es una plataforma Microsoft de administración de endpoints; su participación en un mercado Gartner debe acreditarse por separado. [S21] 

## B. Windows Enterprise — Seguridad integrada

Fuentes por control: Windows Security [S03][S23] y cifrado personal [S24]. El título no implica exclusividad Enterprise ni activación automática.

| Tecnología                          | Función                                                  |
| ----------------------------------- | -------------------------------------------------------- |
| BitLocker                           | Cifrado de unidades                                      |
| BitLocker To Go                     | Cifrado de unidades extraíbles                           |
|  Microsoft Defender Antivirus (antes Windows Defender Antivirus)          | Protección antimalware                                   |
|  Windows Firewall (antes Windows Defender Firewall)           | Firewall del dispositivo                                 |
| Microsoft Defender SmartScreen      | Protección contra sitios y archivos maliciosos           |
| Windows Hello for Business          | Autenticación passwordless                               |
| Credential Guard                    | Aislamiento de secretos y credenciales                   |
| Remote Credential Guard             | Protección de credenciales en conexiones remotas         |
| Virtualization-Based Security       | Aislamiento de componentes críticos                      |
| Hypervisor-Protected Code Integrity | Protección de integridad del código                      |
| App Control for Business            | Control de ejecución de aplicaciones                     |
| AppLocker                           | Restricción de aplicaciones                              |
| Attack Surface Reduction Rules      | Reducción de comportamientos explotables                 |
| Controlled Folder Access            | Protección contra modificaciones no autorizadas          |
| Secure Boot                         | Protección de la cadena de arranque                      |
| Trusted Platform Module             | Protección de claves mediante hardware                   |
| Microsoft Pluton                    | Procesador de seguridad integrado en hardware compatible |
| Windows LAPS                        | Gestión de contraseñas de administrador local            |
| Windows Sandbox                     | Entorno aislado de ejecución                             |
| Windows Security Baselines          | Configuraciones de seguridad recomendadas                |
| Personal Data Encryption | Archivos: Windows 11 22H2+, Enterprise o Education, unión Entra y Windows Hello; carpetas conocidas desde 24H2. [S24] |
| Local Security Authority Protection | Protección del proceso de autenticación                  |

No todas son exclusivas de Windows Enterprise ni están habilitadas automáticamente. Las condiciones dependen de edición, versión, hardware y configuración. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/windows/security/), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol-and-applocker-overview)

------

# 3. Seguridad de Azure

## A. Microsoft Defender for Cloud

Fuente por plan y capacidad: [S25]; protección de IA: [S26]. Foundational CSPM es gratuito; Defender CSPM avanzado. Las dos filas CSPM son un duplicado conceptual; DevOps y Regulatory Compliance son capacidades, no planes independientes.

Defender for Cloud combina **CNAPP, CSPM, DevSecOps y protección de workloads**. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)

| Tecnología / plan                             | Workload protegido                               |
| --------------------------------------------- | ------------------------------------------------ |
| Defender Cloud Security Posture Management | Alias duplicado de Defender CSPM; Foundational CSPM gratuito; Fusionar con Defender CSPM, plan avanzado |
| Defender for Servers Plan 1                   | Servidores y máquinas virtuales                  |
| Defender for Servers Plan 2                   | Protección avanzada de servidores                |
| Defender for Containers                       | Kubernetes y contenedores                        |
| Defender for Storage                          | Cuentas de almacenamiento y objetos              |
| Defender for SQL                              | SQL Server y bases SQL                           |
| Defender for Open-Source Relational Databases | Bases de datos relacionales compatibles          |
| Defender for App Service                      | Aplicaciones alojadas en App Service             |
| Defender for Key Vault                        | Actividades sospechosas sobre secretos y claves  |
| Defender for Resource Manager                 | Operaciones sospechosas de administración        |
| Defender for APIs                             | Protección y visibilidad de APIs                 |
| Defender for AI Services | Amenazas IA admitida; distinto de AI-SPM; tokens de texto, no imagen/audio; Plan Azure; prueba 30 días hasta 75 mil millones de tokens |
| Defender for DevOps | Capacidad DevSecOps, no plan CWPP independiente; Conexiones de repositorios; avanzado según Defender CSPM |
| Defender CSPM                                 | Configuraciones, riesgos y rutas de ataque       |
| Defender for Cloud Regulatory Compliance | Panel de evaluación, no plan ni certificación; Estándares según nivel CSPM |

La documentación actual enumera protecciones para servidores, contenedores, bases de datos, almacenamiento, DevOps, App Service, Key Vault, Resource Manager e IA. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/defender-for-cloud/), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/training/modules/enable-configure-workload-protection-plans/)

## B. Azure — Servicios adicionales de seguridad

Fuentes por servicio: Sentinel [S27], red [S28][S29][S31], claves [S30], gobierno [S33], observabilidad [S34], resiliencia [S36], retirada de Dedicated HSM [S39].

| Tecnología                     | Función                                           |
| ------------------------------ | ------------------------------------------------- |
| Microsoft Sentinel             | SIEM y operaciones de seguridad                   |
| Sentinel SOAR | Función de automatización y playbooks mediante Azure Logic Apps; Facturación Logic Apps aplicable |
| Azure Firewall                 | Firewall administrado de red                      |
| Azure Firewall Premium         | Inspección avanzada y protección de amenazas      |
| Azure Web Application Firewall | Protección de aplicaciones web                    |
| Azure DDoS Protection          | Protección contra ataques DDoS                    |
| Azure Key Vault                | Administración de claves, secretos y certificados |
| Azure Managed HSM | Azure Key Vault Managed HSM: HSM administrado para claves; Servicio Azure independiente |
| Azure Private Link             | Acceso privado a servicios                        |
| Azure Private Endpoint | Interfaz privada de recurso; no desactiva acceso público automáticamente; Recurso Azure |
| Azure Bastion                  | Acceso administrativo seguro a máquinas virtuales |
| Azure Policy                   | Gobierno y cumplimiento de configuraciones        |
| Azure RBAC                     | Control de acceso a recursos                      |
| Azure Monitor                  | Observabilidad y registros                        |
| Azure Monitor Logs             | Almacenamiento y consulta de telemetría           |
| Azure Confidential Computing   | Protección de datos durante procesamiento         |
| Azure Backup                   | Copias de seguridad                               |
| Azure Site Recovery            | Recuperación ante desastres                       |
| Azure Migrate | Descubrimiento y migración; no control continuo de seguridad; Servicio de migración |
| Azure API Management           | Gobierno, autenticación y control de APIs         |
| Azure Front Door | Entrega web global; WAF depende de SKU y política habilitada; Servicio Azure |
| Azure Application Gateway | Proxy HTTP(S) regional; WAF depende de SKU y política habilitada; Servicio Azure |
| Azure Network Security Groups  | Filtrado de tráfico de red                        |
| Azure Virtual Network Manager  | Administración centralizada de redes y reglas     |
| Azure Arc                      | Gobierno y administración de recursos híbridos    |
| Azure Update Manager           | Gestión de actualizaciones                        |
| Azure Attestation              | Verificación de integridad y confianza            |
| Azure Dedicated HSM | Servicio en retirada; no admite nuevos clientes; Soporte a existentes hasta el 31 de julio de 2028 |
| Azure Confidential Ledger      | Registro verificable resistente a alteraciones    |

Estos servicios no deben confundirse con productos de seguridad independientes: algunos son **controles de seguridad integrados en servicios de infraestructura**. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/networking/security/network-security), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/azure/key-vault/general/secure-key-vault)

------

# 4. Categorías Gartner Peer Insights 2026 relevantes para un CISO

Niveles editoriales: DF = capacidad principal; P = parcial; C = complementaria; ND = sin equivalente demostrado. Ninguno certifica participación Gartner.

La siguiente lista conserva **etiquetas de mercado del borrador original** para organizar el stack; la vigencia, denominación oficial y participación de Microsoft **no han sido validadas de forma independiente ante Gartner**. Solo se valida la correspondencia funcional con documentación Microsoft.

No representa un inventario exhaustivo de todo el catálogo de Gartner. Sus mercados cambian, se fusionan o se retiran.

## A. Identidad, acceso y dispositivos

| Categoría del borrador, no mercado Gartner validado | Correspondencia técnica corregida | Nivel editorial | Fuentes Microsoft |
|---|---|---|---|
| Access Management | Entra ID | DF | [S01][S05][S21] |
| Identity Governance and Administration | Entra ID Governance | DF | [S01][S05][S21] |
| Privileged Access Management | Entra PIM; cobertura parcial de PAM completo | P | [S01][S05][S21] |
| Identity Threat Detection and Response | Defender for Identity, Entra ID Protection | P | [S01][S05][S21] |
| Endpoint Protection | Defender for Endpoint | DF | [S01][S05][S21] |
| Endpoint Management Tools | Intune | DF | [S01][S05][S21] |
| Security Awareness Computer-Based Training | Attack Simulation Training: simulaciones y formación de phishing, con Defender for Office 365 P2/E5; no plataforma universal | P | [S01][S05][S21] |

Estas etiquetas proceden del borrador. Los enlaces Gartner del material de origen no constituyen en este catálogo una validación de vigencia ni del reconocimiento de un proveedor. , , , , , 

## B. Operaciones y detección

| Categoría del borrador, no mercado Gartner validado | Correspondencia técnica corregida | Nivel editorial | Fuentes Microsoft |
|---|---|---|---|
| Security Information and Event Management | Sentinel | DF | [S04][S14][S27] |
| Integrated Security Operations Center Solutions | Defender XDR + Sentinel | DF | [S04][S14][S27] |
| Extended Detection and Response — retirada | Defender XDR | DF | [S04][S14][S27] |
| Security Orchestration, Automation and Response — en transición | Sentinel Automation | DF | [S04][S14][S27] |
| Network Detection and Response | Sentinel integra telemetría de red; no constituye sensor NDR autónomo | C | [S04][S14][S27] |
| Managed Detection and Response | Defender Experts MDR | DF | [S04][S14][S27] |
| Co-Managed Security Monitoring Services | Servicios Experts y operación Sentinel según contrato; sin oferta uniforme acreditada | P | [S04][S14][S27] |
| Cybersecurity Incident Response Management | Defender XDR y Sentinel gestionan incidentes; respuesta humana mediante contrato Experts separado | P | [S04][S14][S27] |
| External Attack Surface Management | Defender EASM | DF | [S04][S14][S27] |
| Cyber Asset Attack Surface Management | Security Exposure Management; cobertura parcial | P | [S04][S14][S27] |
| Exposure Assessment Platforms | Security Exposure Management, Defender Vulnerability Management | P | [S04][S14][S27] |
| Adversarial Exposure Validation | No se demuestra una plataforma Microsoft integral equivalente; no equiparar a Attack Simulation Training | ND | [S04][S14][S27] |

SIEM, ISOC, MDR, NDR, ITDR y gestión de exposición son ámbitos funcionales diferentes; las etiquetas y estatus Gartner no se acreditan aquí. , , , , , , , 

## C. Cloud, aplicaciones y redes

| Categoría del borrador, no mercado Gartner validado | Correspondencia técnica corregida | Nivel editorial | Fuentes Microsoft |
|---|---|---|---|
| Cloud-Native Application Protection Platforms | Defender for Cloud | DF | [S02][S25][S29] |
| Cloud Security Posture Management Tools | Defender CSPM | DF | [S02][S25][S29] |
| Security Service Edge | Entra Internet Access + Private Access; Defender for Cloud Apps si se requiere CASB | DF | [S02][S25][S29] |
| SASE Platforms | SSE de Entra; no se demuestra solución SD-WAN integral | P | [S02][S25][S29] |
| Network Security Microsegmentation | Azure NSG, Firewall y segmentación; cobertura parcial | P | [S02][S25][S29] |
| Cloud Web Application and API Protection | WAF en Front Door/Application Gateway + DDoS + Defender for APIs según capa y recursos | P | [S02][S25][S29] |
| AI Application Security | Defender for Cloud AI-SPM + AI threat protection, solo servicios de IA admitidos | P | [S02][S25][S29] |
| AI Usage Control | Entra Internet Access, Purview, Defender for Cloud Apps | P | [S02][S25][S29] |

Microsoft describe Defender for Cloud como CNAPP con CSPM, DevSecOps y CWPP; cualquier equivalencia con un mercado externo es una valoración editorial. , , , , , , 

## D. Datos, cumplimiento y resiliencia

| Categoría del borrador, no mercado Gartner validado | Correspondencia técnica corregida | Nivel editorial | Fuentes Microsoft |
|---|---|---|---|
| Data Loss Prevention | Purview DLP | DF | [S15][S16][S20][S42] |
| Data Security Posture Management | Purview DSPM | DF | [S15][S16][S20][S42] |
| Data Security Platforms | Purview + controles Azure; combinación de productos y planes, no SKU único | P | [S15][S16][S20][S42] |
| Email Security | Defender for Office 365 | DF | [S15][S16][S20][S42] |
| Digital Communications Governance and Archiving Solutions | Purview Communication Compliance + retención + eDiscovery; Audit no es archivo por sí solo | P | [S15][S16][S20][S42] |
| Data and Analytics Governance Platforms | Microsoft Purview Data Governance | DF | [S15][S16][S20][S42] |
| Privacy UX | Sin equivalente integral demostrado por las fuentes Microsoft revisadas | ND | [S15][S16][S20][S42] |
| Microsoft 365 Governance Tools | Capacidades nativas M365; comparar requisitos especializados | P | [S15][S16][S20][S42] |
| Backup and Data Protection Platforms | Azure Backup + Microsoft 365 Backup, alcances y facturación independientes | P | [S15][S16][S20][S42] |
| IT Risk Management | Compliance Manager, Defender for Cloud; cobertura parcial | C | [S15][S16][S20][S42] |
| Security Consulting Services | Servicios Experts, FastTrack y soporte según contrato y elegibilidad | P | [S15][S16][S20][S42] |

DLP, DSPM, correo, backup, archivo de comunicaciones y gobierno tienen requisitos funcionales distintos; este documento no certifica la taxonomía vigente de Gartner. , , , , , 

------

# 5. Correspondencia funcional propuesta: etiquetas del original → Microsoft

Para evitar equivalencias incorrectas, propongo tres niveles:

- **Directa:** Microsoft ofrece una solución claramente alineada con el mercado.
- **Parcial:** cubre capacidades relevantes, pero no necesariamente todos los requisitos.
- **Complementaria:** contribuye al resultado, sin constituir por sí sola una solución del mercado.

| Rótulo del borrador | Solución o capacidad Microsoft | Valoración editorial | Fuente |
|---|---|---|---|
| Endpoint Protection | Defender for Endpoint | Directa funcional | ver categoría desarrollada en sección 4 |
| Endpoint Management Tools | Intune | Directa funcional | ver categoría desarrollada en sección 4 |
| Access Management | Entra ID | Directa funcional | ver categoría desarrollada en sección 4 |
| Identity Governance and Administration | Entra ID Governance | Directa funcional | ver categoría desarrollada en sección 4 |
| Privileged Access Management | Entra PIM | Parcial | ver categoría desarrollada en sección 4 |
| Identity Threat Detection and Response | Defender for Identity + Entra ID Protection, según fuentes | Parcial | [S01][S05] |
| Email Security | Defender for Office 365 | Directa funcional | ver categoría desarrollada en sección 4 |
| Data Loss Prevention | Purview DLP | Directa funcional | ver categoría desarrollada en sección 4 |
| Data Security Posture Management | Purview DSPM actual, según orígenes y controles | Directa funcional, alcance definido | [S17] |
| Data Security Platforms | Purview + Azure | Parcial | ver categoría desarrollada en sección 4 |
| SIEM | Sentinel | Directa funcional | ver categoría desarrollada en sección 4 |
| ISOC | Defender XDR + Sentinel, derechos independientes | Directa funcional | [S04][S27] |
| MDR | Defender Experts MDR | Directa funcional | ver categoría desarrollada en sección 4 |
| NDR | Sentinel + producto/sensor de red integrado | Complementaria | [S27] |
| SOAR | Sentinel Automation | Directa funcional | ver categoría desarrollada en sección 4 |
| CNAPP | Defender for Cloud | Directa funcional | ver categoría desarrollada en sección 4 |
| CSPM | Defender CSPM | Directa funcional | ver categoría desarrollada en sección 4 |
| EASM | Defender EASM | Directa funcional | ver categoría desarrollada en sección 4 |
| CAASM | Security Exposure Management | Parcial | ver categoría desarrollada en sección 4 |
| Exposure Assessment Platforms | Security Exposure Management | Directa funcional | ver categoría desarrollada en sección 4 |
| AEV | No se acredita plataforma Microsoft integral equivalente | Sin equivalencia demostrada | [S44] |
| SSE | Entra Internet Access + Private Access; CASB según necesidad | Directa funcional, alcance SSE | [S02] |
| SASE | SSE de Entra; SD-WAN integral no demostrado | Parcial | [S02] |
| WAAP | Azure WAF + DDoS + Defender for APIs según arquitectura | Parcial | [S29][S25] |
| AI Application Security | Defender for Cloud AI-SPM + amenaza IA admitida | Parcial, servicios admitidos | [S26] |
| AI Usage Control | Entra + Purview + Defender for Cloud Apps | Parcial | ver categoría desarrollada en sección 4 |
| Backup and Data Protection | Azure Backup + Microsoft 365 Backup; facturación separada | Parcial | [S36][S42] |
| IT Risk Management | Compliance Manager + Azure Policy; no GRC integral | Complementaria | [S15][S33] |
| Security Consulting | Servicios Microsoft según programa y contrato | Parcial | [S14][S43] |

**Esta tabla es únicamente un mapeo editorial funcional, no verificación de participación o denominación Gartner.** Los rótulos conservan el texto del original y requieren verificación independiente antes de publicarse como mercados Gartner vigentes.

------

# 6. Servicios de seguridad ofrecidos por Microsoft

Conviene separarlos de los productos tecnológicos.

| Servicio                                         | Descripción                                         | Categoría relacionada           |
| ------------------------------------------------ | --------------------------------------------------- | ------------------------------- |
| Defender Experts MDR                             | SOC administrado y respuesta                        | MDR                             |
| Defender Experts Hunting                         | Búsqueda proactiva de amenazas                      | Threat Hunting / MDR            |
| Defender Experts for Servers                     | Detección y respuesta administrada para servidores  | MDR / CWPP                      |
| Defender Experts Threat Intelligence             | Inteligencia y alertas contextualizadas             | Threat Intelligence             |
| Defender Experts Cybersecurity Incident Response | Preparación, investigación y respuesta a incidentes | Incident Response Services      |
| FastTrack for Microsoft 365 | Guía de adopción según programa y elegibilidad; no MDR | Servicios de adopción / [S43] |
| Microsoft Unified Support                        | Soporte técnico empresarial                         | Servicios de soporte            |
| Microsoft Security Assessment                    | Evaluaciones según programa y elegibilidad          | Security Consulting             |
| Microsoft Security Copilot | Producto de IA: reclasificado fuera de servicios gestionados | Security Copilot / [S13] |

Microsoft documenta Defender Experts como una familia de servicios que incluye MDR, hunting, inteligencia y respuesta a incidentes. MDR se comercializa por separado de las licencias Defender convencionales. [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-overview), [[learn.microsoft.com\]](https://learn.microsoft.com/en-us/defender-xdr/defender-experts/defender-experts-mdr-overview)

------

# 7. Diferencias entre Microsoft 365 E3, E5 y E7

Éste es el resumen que utilizaría como primera aproximación.

| Capacidad | E3 | E5 | E7 |
|---|---|---|---|
| Entra ID P1 | Incluido | Incluido | Incluido |
| Entra ID P2 | No | Incluido | Incluido |
| Defender for Endpoint | P1 | P2, incluye P1 | P2 por E5 |
| Defender for Office 365 | P1 desde 1 de julio de 2026 | P2 | P2 por E5 |
| Defender for Identity | No en E3 base | Incluido | Incluido por E5 |
| Defender for Cloud Apps | No en E3 base | Incluido | Incluido por E5 |
| Defender XDR | Componentes licenciados | Componentes principales E5 | Componentes E5 |
| Purview Information Protection | Funciones base | Funciones avanzadas | Funciones E5 |
| Purview DLP | Exchange, SharePoint y OneDrive base | Cobertura avanzada según ámbito | Funciones E5 |
| Purview Insider Risk Management | No en E3 base | Incluido | Incluido por E5 |
| Purview eDiscovery | Standard | Premium | Premium por E5 |
| Intune | Plan 1 y desde julio 2026 Plan 2, Remote Help y Advanced Analytics | E3 más EPM, Cloud PKI y Enterprise Application Management | Funciones E5 |
| Windows Enterprise | Windows Enterprise E3 | Windows Enterprise E5 | Windows Enterprise E5 por E5 |
| Microsoft Entra Suite | Adquisición separada | Adquisición separada | Incluido |
| Microsoft 365 Copilot | Add-on | Add-on | Incluido |
| Agent 365 | E3 solo no cumple prerrequisitos de compra nueva | Adquisición adicional con requisitos | Incluido |
| Microsoft Sentinel | Azure separado | Azure separado | Azure separado |
| Defender for Cloud | Azure separado | Azure separado | Azure separado |
| Azure Firewall / WAF | Azure separado | Azure separado | Azure separado |
| Security Copilot — añadido | No incluido por E3 base | 400 SCU/mes por 1,000 licencias pagadas; máximo 10,000 SCU/mes | Mismo derecho E5, sujeto a rollout |
| Microsoft 365 Backup — añadido | Pago por uso | Pago por uso | Pago por uso |

Las inclusiones pueden variar por SKU, contrato, país, servicios habilitados y cambios de producto. Microsoft confirma la composición principal de E7 y mantiene comparativas oficiales de planes empresariales. [[microsoft.com\]](https://www.microsoft.com/en-us/security/pricing/enterprise-plans), [[microsoft.com\]](https://www.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-plans-and-pricing), [[microsoft.com\]](https://www.microsoft.com/en-us/microsoft-365/enterprise/compare-microsoft-365-and-office-365)

------

# 8. Cómo incorporaría este catálogo al AI CISO Atlas

Para tu proyecto, evitaría crear una única relación genérica:

```
MicrosoftProduct → GartnerCategory
```

Propongo representar al menos cinco entidades:

1. `Technology`
2. `SecurityCapability`
3. `MarketCategory`
4. `LicenseEntitlement`
5. `ManagedService`

Y relaciones como:

| Relación                     | Significado                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| `PROVIDES_CAPABILITY`        | Una tecnología proporciona una capacidad                    |
| `ALIGNS_WITH_MARKET`         | Una tecnología se corresponde funcionalmente con un mercado |
| `INCLUDED_IN_LICENSE`        | Una capacidad está incluida en un plan determinado          |
| `REQUIRES_ADDON`             | Necesita licencia o consumo adicional                       |
| `DELIVERED_AS_SERVICE`       | Una capacidad se entrega como servicio administrado         |
| `PROTECTS_WORKLOAD`          | Protege un workload específico                              |
| `SUPPORTS_CONTROL_OBJECTIVE` | Contribuye a un objetivo de control                         |
| `MAPS_TO_ATLAS_DOMAIN`       | Se relaciona con un dominio del Atlas                       |

Además, cada relación debería registrar:

- Fuente oficial.
- Fecha de verificación.
- Versión o estado del producto.
- Tipo de correspondencia.
- Nivel de cobertura.
- Restricciones de licencia.

Esto permitiría cruzar después:

**Microsoft Technology × Gartner Category × AI CISO Atlas Domain × NIST Function × License**

------

## 9. Consideraciones para interpretar el catálogo

Hay cuatro distinciones que considero esenciales.

**1. Producto no equivale a mercado.**
 Una plataforma como Defender for Cloud puede participar funcionalmente en CNAPP, CSPM, CWPP y DevSecOps.

**2. Mercado no equivale a capacidad.**
 Gartner puede agrupar varias capacidades en una categoría comercial.

**3. Capacidad no equivale a licencia.**
 Una función puede existir técnicamente, pero requerir un plan adicional.

**4. Correspondencia no equivale a cobertura completa.**
 Por ejemplo, Entra PIM cubre administración de privilegios, pero no necesariamente todos los escenarios de un producto PAM especializado.

------

## Conclusión

Microsoft ofrece un stack de seguridad que abarca:

- Identidad y acceso.
- Endpoint y dispositivos.
- Correo y colaboración.
- Protección y gobierno de datos.
- Seguridad de aplicaciones.
- Seguridad cloud y multicloud.
- Operaciones SOC, SIEM y XDR.
- Exposición y vulnerabilidades.
- Inteligencia de amenazas.
- Seguridad de IA y agentes.
- Continuidad y recuperación.
- Servicios administrados de seguridad.

**La principal conclusión es que Microsoft no debe modelarse como una lista de productos que compiten uno a uno con las categorías Gartner.**

La correspondencia correcta es de muchos a muchos:

**Productos → Capacidades → Categorías de mercado → Objetivos de seguridad.**

Para el AI CISO Atlas, ésta es la estructura que recomiendo adoptar, manteniendo la distinción entre capacidades Microsoft documentadas y correspondencias editoriales no acreditadas por Gartner.

**Limitación de exhaustividad:** este catálogo revisa todas las entradas del documento de entrada a 4 de noviembre de 2026; no certifica denominaciones, vigencia ni participantes de Gartner Peer Insights ni la inclusión de todas las ofertas Microsoft. Para usarla como inventario contractual o matriz definitiva de licenciamiento, cada SKU y correspondencia debe validarse individualmente.

## Anexo A. Fuentes Microsoft

Los códigos de las tablas remiten a documentación oficial; no prueban reconocimiento de mercados Gartner.

- [S01](https://learn.microsoft.com/entra/fundamentals/licensing)
- [S02](https://learn.microsoft.com/entra/global-secure-access/overview-what-is-global-secure-access)
- [S03](https://learn.microsoft.com/windows/security/)
- [S04](https://learn.microsoft.com/defender-xdr/prerequisites)
- [S05](https://learn.microsoft.com/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-defender-service-description)
- [S06](https://learn.microsoft.com/defender-vulnerability-management/defender-vulnerability-management-capabilities)
- [S07](https://learn.microsoft.com/office365/servicedescriptions/office-365-advanced-threat-protection-service-description)
- [S08](https://learn.microsoft.com/partner-center/announcements/2026-july#dlp-in-defender-for-cloud-apps-deprecation)
- [S09](https://learn.microsoft.com/azure/defender-for-iot/organizations/billing)
- [S10](https://learn.microsoft.com/security-exposure-management/prerequisites)
- [S11](https://learn.microsoft.com/azure/external-attack-surface-management/understanding-billable-assets)
- [S12](https://learn.microsoft.com/partner-center/announcements/2026-july#mdti-reaches-end-of-life-august-1,-2026)
- [S13](https://learn.microsoft.com/copilot/security/security-copilot-inclusion)
- [S14](https://learn.microsoft.com/defender-xdr/defender-experts/defender-experts-overview)
- [S15](https://learn.microsoft.com/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)
- [S16](https://learn.microsoft.com/purview/purview-billing-models)
- [S17](https://learn.microsoft.com/purview/data-security-posture-management-learn-about)
- [S18](https://learn.microsoft.com/purview/data-security-investigations-billing)
- [S19](https://learn.microsoft.com/purview/audit-solutions-overview)
- [S20](https://learn.microsoft.com/purview/data-governance-billing)
- [S21](https://learn.microsoft.com/intune/fundamentals/planning-guide#step-3---determine-costs-and-licensing)
- [S22](https://learn.microsoft.com/autopilot/requirements)
- [S23](https://learn.microsoft.com/windows/security/)
- [S24](https://learn.microsoft.com/windows/security/operating-system-security/data-protection/personal-data-encryption)
- [S25](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-cloud-introduction)
- [S26](https://learn.microsoft.com/azure/defender-for-cloud/ai-threat-protection)
- [S27](https://learn.microsoft.com/azure/sentinel/overview)
- [S28](https://learn.microsoft.com/azure/firewall/features-by-sku)
- [S29](https://learn.microsoft.com/azure/web-application-firewall/afds/afds-overview)
- [S30](https://learn.microsoft.com/azure/key-vault/managed-hsm/overview)
- [S31](https://learn.microsoft.com/azure/private-link/private-endpoint-overview)
- [S32](https://learn.microsoft.com/azure/bastion/bastion-overview)
- [S33](https://learn.microsoft.com/azure/governance/policy/overview)
- [S34](https://learn.microsoft.com/azure/azure-monitor/overview)
- [S35](https://learn.microsoft.com/azure/confidential-computing/)
- [S36](https://learn.microsoft.com/azure/backup/backup-overview)
- [S37](https://learn.microsoft.com/azure/api-management/api-management-key-concepts)
- [S38](https://learn.microsoft.com/azure/azure-arc/overview)
- [S39](https://learn.microsoft.com/azure/dedicated-hsm/migration-guide)
- [S40](https://learn.microsoft.com/copilot/plan/compare-copilot-e3-e5-e7)
- [S41](https://learn.microsoft.com/partner-center/announcements/2026-july#new-licensing-prerequisite-for-agent-365)
- [S42](https://learn.microsoft.com/microsoft-365/backup/backup-setup#1-set-up-pay-as-you-go-billing)
- [S43](https://learn.microsoft.com/microsoft-365/fasttrack/introduction)
- [S44](https://learn.microsoft.com/defender-office-365/attack-simulation-training-get-started)

**Términos contractuales:** https://www.microsoft.com/licensing/terms/ . Antes de comprar, verificar SKU, asignación, región y fecha de vigencia.

# Capacidades de Microsoft por función y por licencia

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M02 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Catorce dominios y 50 capacidades

| Dominio | Capacidades | Funciones del núcleo que usan el dominio |
|---|:--:|:--:|
| Identidades | 7 | 8 |
| Dispositivos | 4 | 10 |
| Correo y colaboración | 2 | 3 |
| Datos | 6 | 4 |
| Detección y respuesta | 2 | 14 |
| SIEM y automatización | 2 | 11 |
| Nube | 6 | 15 |
| Aplicaciones y SaaS | 1 | 6 |
| Exposición | 2 | 9 |
| IA y agentes | 4 | 5 |
| Asistencia con IA | 1 | 5 |
| Red e infraestructura | 5 | 5 |
| Resiliencia | 3 | 4 |
| Cumplimiento | 5 | 8 |
| Total | 50 |  |

## 2. Catálogo de capacidades y licencias

Las columnas E3, E5 y E7 indican si la capacidad viene en Microsoft 365 E3, E5 o E7. Son una lectura del catálogo validado el 4 de noviembre de 2026.

| ID | Capacidad | Qué aporta al plan | E3 | E5 | E7 | Licencia: detalle |
|---|---|---|:--:|:--:|:--:|---|
| MS-IDE-01 | Microsoft Entra ID con Conditional Access | Directorio, inicio de sesión único, acceso condicional y autenticación resistente a la suplantación. | Sí | Sí | Sí | Entra ID P1 en E3; P2 en E5 y E7. El acceso condicional basado en riesgo requiere P2 o Entra Suite. |
| MS-IDE-02 | Microsoft Entra ID Protection | Riesgo de usuario y de inicio de sesión, aplicado con acceso condicional. | Parcial | Sí | Sí | Completa con P2 (E5 y E7) o Entra Suite; P1 incluye detecciones básicas. |
| MS-IDE-03 | Microsoft Entra Privileged Identity Management | Privilegios justo a tiempo, con aprobación y vencimiento. | No | Sí | Sí | P2 (E5 y E7) o Entra ID Governance. |
| MS-IDE-04 | Microsoft Entra ID Governance | Ciclo de vida de las identidades, paquetes de acceso y revisiones de acceso. | Adicional | Parcial | Sí | Complemento sobre P1 o P2; incluido en Entra Suite y en E7. P2 trae gestión de derechos y revisiones de acceso básicas. |
| MS-IDE-05 | Microsoft Entra Workload ID | Identidades de cargas de trabajo y federación sin secretos. | Parcial | Parcial | Parcial | Identidades administradas y federación sin costo; Workload ID Premium se licencia por identidad y no viene en ningún paquete. |
| MS-IDE-06 | Microsoft Entra Agent ID | Identidad propia para cada agente de IA. | Parcial | Parcial | Sí | Plataforma disponible para todo cliente de Entra; el acceso condicional, la protección, el gobierno y los controles de red para agentes requieren Agent 365, incluido en E7. |
| MS-IDE-07 | Microsoft Defender for Identity | Detección de ataques a la identidad y postura del directorio local. | No | Sí | Sí | E5 y E7, EMS E5, Defender Suite o por separado. |
| MS-END-01 | Microsoft Defender for Endpoint | Prevención, detección y respuesta en puestos de trabajo, móviles y servidores. | Parcial | Sí | Sí | Plan 1 en E3; Plan 2 en E5 y E7. Los servidores se licencian aparte. |
| MS-END-02 | Microsoft Defender Vulnerability Management | Inventario de software, vulnerabilidades y configuración de los dispositivos. | No | Parcial | Parcial | Funciones básicas incluidas en Defender for Endpoint Plan 2 (E5 y E7); las avanzadas son un complemento. |
| MS-END-03 | Microsoft Intune | Administración, cumplimiento y configuración de dispositivos. | Sí | Sí | Sí | Plan 1 y Plan 2 en E3, E5 y E7 (Plan 2 desde julio de 2026). La mayoría de los componentes de Intune Suite ya viene en esos planes. |
| MS-END-04 | Controles de seguridad de Windows administrados con Intune | Cifrado de disco, reducción de la superficie de ataque, contraseñas de administrador local y control de aplicaciones. | Sí | Sí | Sí | Depende de la edición de Windows y de la licencia de Intune; ver el catálogo validado. |
| MS-PRO-01 | Microsoft Defender for Office 365 | Protección del correo y de la colaboración: adjuntos, vínculos, suplantación e investigación. | No | Sí | Sí | Plan 2 en E5 y E7. E3 incluye solo la protección integrada del buzón. |
| MS-PRO-02 | Attack simulation training | Simulaciones de phishing y formación dirigida. | No | Sí | Sí | Requiere E5 o Defender for Office 365 Plan 2; E3 solo tiene un subconjunto de prueba. |
| MS-DAT-01 | Microsoft Purview Information Protection | Clasificación, etiquetas de confidencialidad y cifrado. | Parcial | Sí | Sí | E3: etiquetado manual, por defecto y obligatorio. E5 y E7: etiquetado automático y funciones avanzadas. |
| MS-DAT-02 | Microsoft Purview Data Loss Prevention | Prevención de pérdida de datos en correo, archivos, chat, dispositivos e IA. | Parcial | Sí | Sí | E3: correo y archivos. E5 y E7: Teams, dispositivos y controles para Copilot. La red y el navegador hacia aplicaciones no administradas se pagan por consumo. |
| MS-DAT-03 | Microsoft Purview Data Security Posture Management | Postura de seguridad de los datos, incluidos los que usa la IA. | Ver licencia | Sí | Sí | La versión vigente unifica DSPM y DSPM for AI desde mayo de 2026 y requiere licencia de soporte; la anterior exigía E5 o Purview Suite. |
| MS-DAT-04 | Microsoft Purview Insider Risk Management | Detección de riesgo interno con privacidad por diseño. | No | Sí | Sí | E5 y E7, Purview Suite o el complemento específico. Los indicadores de fuentes ajenas a Microsoft 365 y de IA se pagan por consumo. |
| MS-DAT-05 | Microsoft Purview Data Map y Unified Catalog | Mapa y catálogo de datos de varias nubes y locales. | Consumo | Consumo | Consumo | Pago por consumo. La documentación indica mantenimiento del catálogo unificado y del gobierno de datos clásico hasta el 12 de noviembre de 2027. |
| MS-DAT-06 | Customer Key y Double Key Encryption | Control de las claves de cifrado por parte de la organización. | No | Sí | Sí | E5 y E7, Purview Suite o complementos equivalentes. |
| MS-XDR-01 | Microsoft Defender XDR | Incidentes unificados, investigación, búsqueda y respuesta automática entre dominios. | Parcial | Sí | Sí | Sin costo adicional con cualquier licencia de Defender que califique; E5 y E7 lo traen completo. |
| MS-XDR-02 | Inteligencia de amenazas en el portal de Defender | Análisis de amenazas e inteligencia integrada a los incidentes y a la búsqueda. | Parcial | Sí | Sí | Integrada en Defender XDR y en Sentinel sin costo adicional; el portal independiente se retiró el 1 de agosto de 2026. |
| MS-SIE-01 | Microsoft Sentinel | Registro central, detección, búsqueda y casos sobre fuentes propias y de terceros. | Consumo | Consumo | Consumo | Pago por consumo de ingesta y de retención. Opera en el portal de Defender; sin soporte en el portal de Azure después del 31 de marzo de 2027. |
| MS-SIE-02 | Automatización de Microsoft Sentinel | Reglas de automatización y cuadernos de respuesta. | Consumo | Consumo | Consumo | No es un producto aparte; los cuadernos de respuesta consumen Azure Logic Apps. |
| MS-NUB-01 | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Postura de Azure, AWS y Google Cloud, rutas de ataque y cumplimiento regulatorio. | Consumo | Consumo | Consumo | Foundational CSPM sin costo; Defender CSPM por recurso facturable. |
| MS-NUB-02 | Defender for Servers | Protección de servidores en cualquier nube y locales. | Consumo | Consumo | Consumo | Consumo en Azure, por servidor. |
| MS-NUB-03 | Defender for Containers | Protección de clústeres, imágenes y registros. | Consumo | Consumo | Consumo | Consumo en Azure. |
| MS-NUB-04 | Defender for Cloud: servicios de plataforma | Protección de almacenamiento, bases de datos, aplicaciones, claves, administración de recursos e interfaces. | Consumo | Consumo | Consumo | Consumo en Azure, por plan. |
| MS-NUB-05 | DevOps security de Defender for Cloud | Postura de repositorios y canalizaciones. | Consumo | Consumo | Consumo | Sin precio propio: básico en Foundational CSPM y avanzado en Defender CSPM. |
| MS-NUB-06 | Azure Arc, Azure Policy y Azure Update Manager | Línea base, configuración y actualización de servidores y clústeres fuera de Azure. | Consumo | Consumo | Consumo | Servicios de Azure; Arc es el requisito para extender los controles fuera de Azure. |
| MS-APP-01 | Microsoft Defender for Cloud Apps | Descubrimiento de aplicaciones, postura de SaaS, gobierno de aplicaciones OAuth y control de sesión. | Parcial | Sí | Sí | Completo en E5 y E7; E3 incluye solo el descubrimiento de aplicaciones. |
| MS-EXP-01 | Microsoft Security Exposure Management | Superficie de ataque, activos críticos, rutas de ataque e iniciativas con puntuación. | Adicional | Sí | Sí | Sin licencia propia: incluido con E5 y E7; en E3, con complementos. Los conectores externos se pagan por consumo. |
| MS-EXP-02 | Microsoft Defender External Attack Surface Management | Descubrimiento de activos expuestos a internet. | Consumo | Consumo | Consumo | Recurso de Azure facturado por activo. |
| MS-IAA-01 | Microsoft Agent 365 | Registro, observabilidad y control de los agentes. | Adicional | Adicional | Sí | Incluido en E7. |
| MS-IAA-02 | Defender for Cloud: postura de IA y Defender for AI Services | Inventario y postura de las cargas de IA, y detección de amenazas en ejecución. | Consumo | Consumo | Consumo | Postura de IA dentro de Defender CSPM; Defender for AI Services por consumo. La postura de agentes requiere Agent 365 desde el 1 de julio de 2026. |
| MS-IAA-03 | Protecciones de Microsoft Purview para IA generativa | Etiquetas, prevención de pérdida de datos, auditoría y retención sobre el uso de IA. | Parcial | Parcial | Sí | Copilot: licencias por usuario; algunas funciones requieren E5. Agentes y aplicaciones conectadas a Entra: E7 y Agent 365. IA fuera de Microsoft 365: por consumo. |
| MS-IAA-04 | Controles de seguridad de Microsoft Foundry | Filtros de contenido, protección ante inyección de instrucciones, evaluaciones y pruebas adversarias. | Consumo | Consumo | Consumo | Servicios de Azure por consumo. |
| MS-ASI-01 | Microsoft Security Copilot | Asistencia con IA y agentes para investigación, respuesta y postura. | Consumo | Sí | Sí | Incluido en E5 y E7: 400 unidades de cómputo por cada 1.000 licencias pagas por mes, hasta 10.000. Sin esas licencias, por capacidad aprovisionada. |
| MS-RED-01 | Global Secure Access (Entra Internet Access y Private Access) | Acceso a internet y a aplicaciones privadas con identidad, sin red privada virtual. | Parcial | Parcial | Sí | Por separado o en Entra Suite, incluida en E7. El perfil de tráfico de Microsoft viene con P1 y P2. |
| MS-RED-02 | Azure Firewall, Web Application Firewall y DDoS Protection | Filtrado de red, protección de aplicaciones web y defensa ante denegación de servicio. | Consumo | Consumo | Consumo | Servicios de Azure por consumo. |
| MS-RED-03 | Segmentación y acceso privado en Azure | Grupos de seguridad de red, vínculos privados, perímetro de seguridad de red y acceso administrativo seguro. | Consumo | Consumo | Consumo | Servicios de Azure. |
| MS-RED-04 | Microsoft Defender for IoT | Supervisión de redes de tecnología operacional. | Adicional | Parcial | Parcial | Tecnología operacional: licencia por sitio. Los dispositivos conectados de la empresa están incluidos en E5 y E7. |
| MS-RED-05 | Azure Key Vault y Managed HSM | Custodia de claves, secretos y certificados. | Consumo | Consumo | Consumo | Servicios de Azure por consumo. |
| MS-RES-01 | Azure Backup | Copias de seguridad con bóveda aislada, eliminación temporal e inmutabilidad. | Consumo | Consumo | Consumo | Servicio de Azure por consumo. |
| MS-RES-02 | Azure Site Recovery | Replicación y conmutación por error hacia Azure. | Consumo | Consumo | Consumo | Servicio de Azure por consumo. |
| MS-RES-03 | Microsoft 365 Backup | Copia y restauración rápida de SharePoint, OneDrive y Exchange Online. | Consumo | Consumo | Consumo | Pago por consumo, por volumen almacenado. |
| MS-CUM-01 | Microsoft Purview Compliance Manager | Evaluaciones por norma, acciones de mejora y puntuación de cumplimiento. | Parcial | Parcial | Parcial | Todos los planes incluyen la plantilla de base; E5 suma tres plantillas; el resto se compra por plantilla. |
| MS-CUM-02 | Microsoft Purview Audit y eDiscovery | Registro de auditoría y búsqueda, preservación y revisión de contenido. | Parcial | Sí | Sí | Estándar en E3; las funciones avanzadas, en E5 y E7. |
| MS-CUM-03 | Microsoft Purview Data Lifecycle Management y Records Management | Retención, eliminación y gestión de registros. | Parcial | Sí | Sí | E3: directivas de retención y etiquetas manuales. E5 y E7: aplicación automática y gestión de registros. |
| MS-CUM-04 | Microsoft Purview Communication Compliance e Information Barriers | Supervisión de comunicaciones y barreras de información. | No | Sí | Sí | E5 y E7 o Purview Suite. |
| MS-CUM-05 | Microsoft Priva | Riesgo de privacidad sobre datos personales. | Adicional | Adicional | Adicional | Complemento sobre E3 o E5. |

### Inclusión por plan

| Inclusión | Microsoft 365 E3 | Microsoft 365 E5 | Microsoft 365 E7 |
|---|:--:|:--:|:--:|
| Sí | 3 | 22 | 27 |
| Parcial | 14 | 8 | 4 |
| No | 8 | 0 | 0 |
| Adicional | 5 | 2 | 1 |
| Consumo | 19 | 18 | 18 |
| Ver licencia | 1 | 0 | 0 |
| Total | 50 | 50 | 50 |

### Qué agrega cada plan

- **De E3 a E5** quedan incluidas 19 capacidades que en E3 no lo estaban o lo estaban en parte: Microsoft Entra ID Protection, Microsoft Entra Privileged Identity Management, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office 365, Attack simulation training, Microsoft Purview Information Protection, Microsoft Purview Data Loss Prevention, Microsoft Purview Data Security Posture Management, Microsoft Purview Insider Risk Management, Customer Key y Double Key Encryption, Microsoft Defender XDR, Inteligencia de amenazas en el portal de Defender, Microsoft Defender for Cloud Apps, Microsoft Security Exposure Management, Microsoft Security Copilot, Microsoft Purview Audit y eDiscovery, Microsoft Purview Data Lifecycle Management y Records Management, Microsoft Purview Communication Compliance e Information Barriers.
- **De E5 a E7** quedan incluidas 5 más: Microsoft Entra ID Governance, Microsoft Entra Agent ID, Microsoft Agent 365, Protecciones de Microsoft Purview para IA generativa, Global Secure Access (Entra Internet Access y Private Access).
- **Por consumo**, en cualquier plan: 18 capacidades de Azure o de pago por uso. Su costo depende del volumen: servidores, recursos, registros ingeridos y almacenamiento.

## 3. Cada función sobre la plataforma

### Gobierno

| ID | Función | Aporte de Microsoft | Capacidades | Evidencia y fuente del dato | Qué queda fuera |
|---|---|---|---|---|---|
| GOB-G1.1 | Contexto, mandato y autoridad del CISO | Fuera de la plataforma | — | Mandato, actas y derechos de decisión: registro propio. | — |
| GOB-G1.2 | Estrategia de seguridad y alineación con el negocio | Fuera de la plataforma | — | Estrategia y hoja de ruta: registro propio. | — |
| GOB-G2.1 | Marcos, estándares y grilla de propiedad | Apoya | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Compliance Manager: evaluaciones por marco. Defender for Cloud: estándares asignados y benchmark. | La grilla de propiedad y la elección de marcos son decisiones de gestión. |
| GOB-G2.2 | Políticas, estándares y procedimientos | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Entra ID con Conditional Access | Asignaciones de Azure Policy, perfiles de Intune y directivas de acceso condicional como expresión técnica de la política. | Repositorio de políticas con dueño y ciclo de revisión. |
| GOB-G3.1 | Requisitos legales, regulatorios y contractuales | Apoya | Microsoft Purview Compliance Manager · Microsoft Purview Data Lifecycle Management y Records Management · Microsoft Purview Communication Compliance e Information Barriers | Compliance Manager: plantillas de normas y mapeo de acciones. Retención, registros y supervisión de comunicaciones para las obligaciones que lo exigen. | Relevamiento legal de las normas aplicables. |
| GOB-G3.2 | Cumplimiento y aseguramiento continuo | Cubre en parte | Microsoft Purview Compliance Manager · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Purview Audit y eDiscovery | Compliance Manager: puntuación y acciones de mejora. Defender for Cloud: cumplimiento regulatorio. Purview Audit: registros. | Auditoría interna, verificación independiente y evidencia de controles fuera de Microsoft. |
| GOB-G4.1 | Gobernanza del riesgo: estructuras y dueños | Fuera de la plataforma | — | Comité, dueños de riesgo y actas: registro propio. | — |
| GOB-G4.2 | Apetito de riesgo: definición y comunicación | Fuera de la plataforma | — | Declaración de apetito y umbrales: registro propio. | — |
| GOB-G5.1 | Supervisión de la evaluación y el análisis de riesgos | Apoya | Microsoft Security Exposure Management · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Exposure Management: iniciativas, métricas y rutas de ataque como insumo del análisis de riesgo. | Registro de riesgos y cuantificación de escenarios. |
| GOB-G5.2 | Supervisión del tratamiento y la aceptación de riesgos | Apoya | Microsoft Defender Vulnerability Management · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Excepciones y exenciones registradas en Defender Vulnerability Management y en Defender for Cloud. | Registro de riesgos aceptados, con dueño y vencimiento. |
| GOB-G6.1 | Comunicación estratégica y reporte a la dirección | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR | Microsoft Secure Score, iniciativas de Exposure Management y tendencias de incidentes como insumo del informe. | El informe a la dirección y su formato. |
| GOB-G6.2 | Liderazgo ético y medición de la efectividad | Fuera de la plataforma | — | Registro propio. | — |

### Gestión

| ID | Función | Aporte de Microsoft | Capacidades | Evidencia y fuente del dato | Qué queda fuera |
|---|---|---|---|---|---|
| GES-M1.1 | Programa de seguridad y portafolio de productos-control | Apoya | Microsoft Security Exposure Management · Microsoft Defender XDR | Microsoft Secure Score y sus acciones por producto; iniciativas de Exposure Management. | Portafolio de productos-control con dueño, objetivo y evidencia. |
| GES-M1.2 | Finanzas, equipo, proveedores y capacitación | Apoya | — | Consumo de los servicios de seguridad en la facturación de Azure y uso de licencias en el centro de administración. Formación: serie Ninja. | Presupuesto, dotación y contratos: registro propio. |
| GES-M2.1 | Activos, datos y protección de datos personales | Cubre en parte | Microsoft Purview Data Map y Unified Catalog · Microsoft Purview Data Security Posture Management · Microsoft Purview Information Protection · Microsoft Priva | Data Map: inventario de orígenes. DSPM: evaluaciones de riesgo de datos. Priva: datos personales en Microsoft 365. | Inventario de activos no digitales y registro de tratamientos de datos personales. |
| GES-M2.2 | Gestión de identidades y accesos | Cubre | Microsoft Entra ID con Conditional Access · Microsoft Entra ID Governance · Microsoft Entra Privileged Identity Management · Microsoft Entra ID Protection | Microsoft Entra: Identity Secure Score, recomendaciones, revisiones de acceso e informes de métodos de autenticación. | Identidades nativas de otras nubes y directorios que no se federan. |
| GES-M3.1 | Arquitectura de seguridad e ingeniería (Zero Trust) | Apoya | Microsoft Security Exposure Management · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Zero Trust Assessment, iniciativas de Exposure Management y rutas de ataque como evidencia de la arquitectura. | Arquitectura objetivo y revisión de diseños. |
| GES-M3.2 | Selección, implementación y evaluación de controles | Apoya | Azure Arc, Azure Policy y Azure Update Manager · Microsoft Intune · Microsoft Purview Compliance Manager | Línea base como código: Azure Policy y configuración de máquinas; perfiles y líneas base de Intune. | Criterios de selección y de evaluación de controles. |
| GES-M4.1 | Gestión de las operaciones de seguridad | Cubre | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot · Automatización de Microsoft Sentinel | Defender XDR y Microsoft Sentinel: cola de incidentes, eficiencia de las operaciones y optimización del SOC. | Modelo operativo, turnos y contrato del servicio gestionado, si lo hay. |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes | Cubre | Microsoft Defender Vulnerability Management · Microsoft Security Exposure Management · Inteligencia de amenazas en el portal de Defender · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Defender Vulnerability Management, Exposure Management y análisis de amenazas. | Activos sin agente y tecnologías fuera del alcance de los sensores. |
| GES-M5.1 | Preparación de la respuesta a incidentes | Cubre en parte | Automatización de Microsoft Sentinel · Microsoft Defender XDR | Cuadernos de respuesta y reglas de automatización; acciones de respuesta de Defender XDR. | Plan de respuesta, roles, contactos y ejercicios. |
| GES-M5.2 | Conducción de la respuesta y aprendizaje | Cubre en parte | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot | Línea de tiempo del incidente, casos y acciones registradas en Defender XDR y en Sentinel. | Dirección del incidente, comunicación y revisión posterior. |
| GES-M6.1 | Continuidad, recuperación y resiliencia | Cubre en parte | Azure Backup · Azure Site Recovery · Microsoft 365 Backup | Azure Backup, Azure Site Recovery y Microsoft 365 Backup: trabajos, simulacros y restauraciones. | Análisis de impacto, objetivos de recuperación y cargas en otras nubes. |
| GES-M6.2 | Nube, tecnologías emergentes y cadena de suministro | Cubre en parte | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender for Cloud Apps · Microsoft Agent 365 · DevOps security de Defender for Cloud | Defender for Cloud: postura por entorno. Defender for Cloud Apps: aplicaciones en uso. Agent 365: agentes. | Riesgo de proveedores y cadena de suministro de software. |

### Operación

| ID | Función | Aporte de Microsoft | Capacidades | Evidencia y fuente del dato | Qué queda fuera |
|---|---|---|---|---|---|
| OPE-ID-01 | Inventario y descubrimiento de activos | Cubre | Microsoft Security Exposure Management · Microsoft Defender for Endpoint · Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Microsoft Defender External Attack Surface Management | Inventario de dispositivos de Defender, inventario de recursos de Defender for Cloud y superficie de ataque de Exposure Management. | Activos sin agente, sin conector o fuera de las nubes conectadas. |
| OPE-ID-02 | Gestión de vulnerabilidades y de la exposición | Cubre | Microsoft Defender Vulnerability Management · Microsoft Security Exposure Management · Defender for Servers · Defender for Containers | Defender Vulnerability Management: exposición, recomendaciones y corrección. Defender for Cloud: evaluación de servidores e imágenes. | Equipos de red, tecnología operacional y aplicaciones propias. |
| OPE-ID-03 | Postura de nube y de configuración | Cubre | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) · Azure Arc, Azure Policy y Azure Update Manager · Microsoft Defender for Cloud Apps · Microsoft Intune | Defender for Cloud: puntuación de seguridad y cumplimiento por entorno. Defender for Cloud Apps: postura de SaaS. | Servicios de otras nubes con cobertura parcial y SaaS sin conector. |
| OPE-ID-04 | Evaluación de riesgo de terceros | Apoya | Microsoft Defender for Cloud Apps · Microsoft Defender External Attack Surface Management | Catálogo de aplicaciones en la nube con puntuación de riesgo; superficie externa de terceros. | Proceso de evaluación de proveedores, cuestionarios y cláusulas. |
| OPE-ID-05 | Pruebas ofensivas y validación de controles | Cubre en parte | Attack simulation training · Microsoft Security Exposure Management · Controles de seguridad de Microsoft Foundry | Simulaciones de phishing, rutas de ataque y pruebas adversarias de modelos. | Pruebas de penetración, ejercicios de equipo rojo y validación continua de controles. |
| OPE-ID-06 | Descubrimiento y clasificación de datos | Cubre | Microsoft Purview Information Protection · Microsoft Purview Data Security Posture Management · Microsoft Purview Data Map y Unified Catalog | Purview: explorador de contenido y de actividad, evaluaciones de DSPM y resultados de los exámenes de Data Map. | Almacenes de datos de otras nubes sin conector o sin clasificación. |
| OPE-ID-07 | Inventario y evaluación de sistemas de IA y agentes | Cubre | Microsoft Agent 365 · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Purview Data Security Posture Management · Microsoft Defender for Cloud Apps | Agent 365: registro de agentes. Defender for Cloud: inventario de cargas de IA. Defender for Cloud Apps: aplicaciones de IA en uso. | Agentes y modelos de plataformas no conectadas. |
| OPE-PR-01 | Identidades y accesos de las personas | Cubre | Microsoft Entra ID con Conditional Access · Microsoft Entra ID Protection · Microsoft Entra ID Governance | Microsoft Entra: métodos de autenticación, registros de inicio de sesión e información de acceso condicional. | Aplicaciones que no se federan e identidades locales de otras nubes. |
| OPE-PR-02 | Acceso privilegiado | Cubre | Microsoft Entra Privileged Identity Management · Microsoft Entra ID con Conditional Access · Segmentación y acceso privado en Azure | Privileged Identity Management: asignaciones aptas y activas, activaciones y revisiones. | Roles nativos de AWS y de Google Cloud, y cuentas privilegiadas locales. |
| OPE-PR-03 | Identidades no humanas, de cargas y de agentes | Cubre | Microsoft Entra Workload ID · Microsoft Entra Agent ID · Microsoft Defender for Cloud Apps · Azure Key Vault y Managed HSM | Entra: identidades de carga y de agente. Defender for Cloud Apps: aplicaciones OAuth. Key Vault: secretos y certificados. | Cuentas de servicio y claves nativas de otras nubes. |
| OPE-PR-04 | Protección y gestión de dispositivos | Cubre | Microsoft Intune · Microsoft Defender for Endpoint · Controles de seguridad de Windows administrados con Intune | Intune: cumplimiento y configuración. Defender for Endpoint: dispositivos incorporados y estado del sensor. | Dispositivos no administrados y plataformas sin soporte. |
| OPE-PR-05 | Protección del correo y la colaboración | Cubre | Microsoft Defender for Office 365 · Attack simulation training | Defender for Office 365: informes de protección, envíos, analizador de configuración y campañas. | Correo y colaboración fuera de Microsoft 365. |
| OPE-PR-06 | Protección de datos | Cubre | Microsoft Purview Information Protection · Microsoft Purview Data Loss Prevention · Microsoft Purview Insider Risk Management · Customer Key y Double Key Encryption | Purview: alertas y coincidencias de prevención de pérdida de datos, cobertura de etiquetas y casos de riesgo interno. | Datos en almacenes de otras nubes y en aplicaciones sin conector. |
| OPE-PR-07 | Seguridad de aplicaciones y del desarrollo | Cubre en parte | DevOps security de Defender for Cloud · Defender for Cloud: servicios de plataforma · Azure Firewall, Web Application Firewall y DDoS Protection · Microsoft Defender for Cloud Apps | DevOps security: hallazgos en repositorios y canalizaciones. Defender for Cloud: interfaces y aplicaciones. | Análisis de código y de dependencias en el repositorio; plataformas de desarrollo autoalojadas. |
| OPE-PR-08 | Seguridad de red y segmentación | Cubre en parte | Global Secure Access (Entra Internet Access y Private Access) · Azure Firewall, Web Application Firewall y DDoS Protection · Segmentación y acceso privado en Azure | Global Secure Access: registros de tráfico. Azure Firewall y grupos de seguridad de red: reglas y registros. | Segmentación en otras nubes y en el centro de datos. |
| OPE-PR-09 | Protección de cargas e infraestructura de nube | Cubre | Defender for Servers · Defender for Containers · Defender for Cloud: servicios de plataforma · Azure Arc, Azure Policy y Azure Update Manager | Defender for Cloud: cobertura de planes, alertas y recomendaciones por carga. | Servicios de plataforma de AWS y de Google Cloud sin plan equivalente. |
| OPE-PR-10 | Concientización y cultura de seguridad | Cubre en parte | Attack simulation training | Attack simulation training: informes de simulación y de formación; mensajes reportados por los usuarios. | Programa de cultura, formación por función y red de referentes. |
| OPE-PR-11 | Protección de sistemas de IA y agentes | Cubre | Controles de seguridad de Microsoft Foundry · Protecciones de Microsoft Purview para IA generativa · Defender for Cloud: postura de IA y Defender for AI Services · Microsoft Entra Agent ID | Foundry: filtros y evaluaciones. Purview: controles sobre el uso de IA. Defender for Cloud: alertas de cargas de IA. | Modelos y agentes alojados en otras plataformas. |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados | Cubre en parte | Microsoft Defender for IoT | Defender for IoT: inventario y alertas de la red de tecnología operacional. | Segmentación industrial, parches y respuesta en planta. |
| OPE-DE-01 | Monitoreo continuo y gestión de alertas | Cubre | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot | Defender XDR y Sentinel: cola de incidentes, tiempos de clasificación y estado de los sensores y de los conectores. | Fuentes sin conector y cobertura horaria del servicio. |
| OPE-DE-02 | Ingeniería y calidad de la detección | Cubre | Microsoft Sentinel · Microsoft Defender XDR | Sentinel: reglas de análisis, optimización del SOC y cobertura frente a técnicas de ataque. Defender XDR: detecciones personalizadas. | Casos de uso propios y pruebas de las detecciones. |
| OPE-DE-03 | Búsqueda proactiva de amenazas | Cubre | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Copilot | Búsqueda avanzada en Defender XDR y consultas de búsqueda en Sentinel. | Hipótesis, calendario de búsquedas y registro de resultados. |
| OPE-DE-04 | Inteligencia de amenazas | Cubre | Inteligencia de amenazas en el portal de Defender · Microsoft Sentinel | Análisis de amenazas en el portal de Defender e indicadores en Sentinel. | Fuentes sectoriales y nacionales de inteligencia. |
| OPE-DE-05 | Gestión de registros y telemetría | Cubre | Microsoft Sentinel · Microsoft Purview Audit y eDiscovery · Azure Arc, Azure Policy y Azure Update Manager | Sentinel: estado de los conectores, volumen de ingesta y retención. Purview Audit: registros de auditoría. | Fuentes sin conector; costo de ingesta y de retención. |
| OPE-DE-06 | Observabilidad de IA y agentes | Cubre en parte | Microsoft Agent 365 · Defender for Cloud: postura de IA y Defender for AI Services · Protecciones de Microsoft Purview para IA generativa · Microsoft Sentinel | Agent 365: actividad de los agentes. Purview: auditoría de las interacciones con IA. Defender for Cloud: alertas de IA. | Trazas de agentes de plataformas no conectadas. |
| OPE-RS-01 | Gestión y coordinación de incidentes | Cubre | Microsoft Defender XDR · Microsoft Sentinel · Automatización de Microsoft Sentinel | Defender XDR y Sentinel: incidentes, casos, asignación y tiempos. | Herramienta de gestión de servicios y coordinación con terceros. |
| OPE-RS-02 | Análisis e investigación forense | Cubre en parte | Microsoft Defender XDR · Microsoft Defender for Endpoint · Microsoft Purview Audit y eDiscovery · Microsoft Security Copilot | Investigación de incidentes, respuesta en vivo en dispositivos, registros de auditoría y preservación de contenido. | Forense de disco y de memoria; cadena de custodia. |
| OPE-RS-03 | Contención, erradicación y respuesta automatizada | Cubre | Microsoft Defender XDR · Automatización de Microsoft Sentinel · Microsoft Defender for Endpoint · Microsoft Entra ID Protection | Centro de actividades: acciones automáticas y manuales; interrupción automática de ataques; cuadernos de respuesta. | Acciones sobre sistemas de otras nubes y locales sin integración. |
| OPE-RS-04 | Comunicación y notificación de incidentes | Apoya | Microsoft Defender XDR · Microsoft Purview Audit y eDiscovery | Línea de tiempo y alcance del incidente como insumo de la notificación. | Criterios, plazos y registro de notificaciones. |
| OPE-RS-05 | Gestión de crisis y ejercicios | Fuera de la plataforma | — | Registro propio de los ejercicios y de sus resultados. | — |
| OPE-RC-01 | Respaldo y restauración | Cubre en parte | Azure Backup · Microsoft 365 Backup | Azure Backup y Microsoft 365 Backup: trabajos, puntos de restauración y restauraciones de prueba. | Respaldo de cargas en AWS, en Google Cloud y en SaaS de terceros. |
| OPE-RC-02 | Recuperación de servicios críticos | Cubre en parte | Azure Site Recovery · Azure Backup | Azure Site Recovery: estado de la replicación y simulacros de conmutación por error. | Recuperación de servicios alojados en otras nubes. |
| OPE-RC-03 | Recuperación de la identidad y de la plataforma de control | Cubre en parte | Microsoft Defender for Identity · Microsoft Entra ID con Conditional Access · Azure Backup | Defender for Identity: postura del directorio local. Entra: cuentas de acceso de emergencia. Azure Backup: copia del estado del sistema. | Procedimiento probado de recuperación del directorio y de la plataforma de control. |
| OPE-RC-04 | Continuidad y operación degradada | Fuera de la plataforma | — | Registro propio. | — |
| OPE-RC-05 | Comunicación de la recuperación y lecciones aprendidas | Fuera de la plataforma | — | Registro propio. | — |

## 4. Cómo leer el mapa

- **Cubre.** La plataforma aporta la capacidad principal. Falta desplegarla, operarla y probarla.
- **Cubre en parte.** Hay una parte que depende de un proceso, de personas o de otra herramienta. La columna «Qué queda fuera» lo dice.
- **Apoya.** La plataforma da datos o evidencia. La función es de gobierno o de gestión.
- **Fuera de la plataforma.** No hay nada que activar: hay que decidir, escribir y sostener.

Tener la licencia no eleva el nivel de evidencia de una función. En la escala del núcleo, una capacidad desplegada sostiene el nivel «Implementado»; el nivel «Probado» exige una prueba, un ejercicio o una revisión independiente.

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

# Puente con el repositorio del autor: guías, acciones, indicadores técnicos y formación

**Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1, revisión 3** · documento M11 · 15 de noviembre de 2026 · @SCavanna

> Propuesta de base. Las capacidades, las licencias y la cobertura se verificaron en fuentes oficiales con fecha de corte al 15 de noviembre de 2026; revalidar después de Microsoft Ignite (17 al 20 de noviembre de 2026).

## 1. Qué es y por qué se agrega

El autor publica en su repositorio `SCavanna-PoV` un conjunto de **23 guías de excelencia operacional** para los productos de seguridad de Microsoft, junto con la serie Ninja Training y un puente que las vincula con el plan del CISO. Todas las guías tienen la misma estructura: la configuración que se hace una vez, las rutinas que se repiten con una cadencia, la respuesta ante un evento, los indicadores técnicos del producto, los roles que intervienen y la correspondencia con NIST CSF 2.0.

Las revisiones anteriores de esta edición usaron borradores de diez de esas guías. La revisión 3 toma el repositorio como referencia vigente y lo incorpora de cuatro maneras:

| Qué se tomó del repositorio | Cantidad | Dónde quedó en esta edición |
|---|:--:|---|
| Guías, con su relación con dominios, funciones, capacidades y programas de formación | 23 | Hoja «Guías del repositorio»; sección 3 |
| Acciones de configuración, de rutina y de respuesta | 833 | Hoja «Acciones de las guías»; secciones 4 y 5 |
| Tareas de riesgo interno y de ciclo de vida de los datos, integradas una por una | 56 leídas; 47 filas nuevas | Hoja «Operación por cadencias»; sección 6 |
| Indicadores técnicos | 184 | Hoja «Indicadores técnicos»; sección 7 y anexo |
| Ejercicios y entorno de práctica de los programas Ninja | 2165 ejercicios en 15 programas | Hoja «Formación»; sección 8; documento M06 «Plan de formación con los Ninja Training» |

**Regla de lectura.** La guía dice qué se configura, qué se repite y qué se hace ante un evento en un producto. El plan dice para qué: qué función cumple, qué resultado clave mueve y qué indicador del CISO cambia. Este documento une las dos cosas. El procedimiento de cada acción (consola, pasos y consultas) está en la guía y no se copió.

## 2. De dónde se leyó

| Dato | Valor |
|---|---|
| Repositorio | SCavanna-PoV · https://github.com/scavanna/SCavanna-PoV |
| Carpeta | `ExcelenciaOperacional_NinjaTraining_KPIsOKRs` |
| Fecha de consolidación | 12 de noviembre de 2026 |
| Fecha de validación de las guías | 11 de noviembre de 2026 |
| Paquete leído | `Repositorio_GitHub_Pages_CISO365_ExcelenciaOperacional_Ninja_2026.zip`, de 311 archivos, localizado en el OneDrive del autor |
| Puente del repositorio | Escrito para el plan 1.0 del CISO 365: 7 fases, 130 actividades y 70 indicadores |

En las páginas públicas del repositorio se confirmaron la carpeta y su estructura. La descarga directa de los archivos no estuvo disponible en el entorno de trabajo, así que el contenido se leyó del paquete. El paquete declara la misma carpeta, las mismas cifras y la misma fecha de consolidación; no se comparó archivo por archivo con el repositorio.

Otras carpetas del repositorio, que no se incorporaron en esta revisión:

| Carpeta | Estado |
|---|---|
| `Ransomware_ExcelenciaOperacional_NinjaTraining_KPIsOKRs` | Programa operativo de resiliencia ante ransomware. No se incorporó en esta revisión. |
| `Ninja_Training_Seguridad_Microsoft_2026` | Serie Ninja Training publicada por separado. No se leyó: se usó la copia de la carpeta principal. |
| `Miscelaneos` | Otros materiales del autor. No se leyó. |

## 3. Las 23 guías

| ID | Guía | Categoría en el repositorio | Licencia según la guía | Configuración puntual | Rutinas periódicas | Respuesta por evento | Indicadores técnicos | En la hoja Operación por cadencias |
|---|---|---|---|:--:|:--:|:--:|:--:|---|
| EO-00 | Marco Maestro de Excelencia Operacional para la Oficina del CISO, SOC Moderno y Gobierno NIST CSF 2.0 | Marco Transversal CISO, SOC y NIST | Asociado a M365 E5 (Marco Arquitectónico y de Gobierno Transversal sobre M365 E5 / E7 y Azure) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-01 | Microsoft Entra ID (Plan 1 / Plan 2 — Core IAM, Conditional Access e Identity Protection / ITDR) | Identidad y Acceso (Microsoft Entra) | Incluido en Microsoft 365 E5 | 8 | 23 | 5 | 8 | Tareas del borrador anterior |
| EO-02 | Microsoft Entra ID Governance (Gobierno de Ciclo de Vida JML, Derechos, Recertificación IA y Agentes) | Identidad y Acceso (Microsoft Entra) | Complemento / Add-on sobre M365 E5 (Incluido en Microsoft Entra Suite / M365 E7) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-03 | Microsoft Defender XDR (Plataforma SecOps Unificada) | SecOps, XDR y SIEM | Incluido en M365 E5 | 8 | 24 | 4 | 8 | Tareas del borrador anterior |
| EO-04 | Microsoft Defender for Endpoint (P1/P2) y Vulnerability Management | SecOps, XDR y SIEM | Incluido en M365 E5 (Plan 2 + MDVM Core) | 8 | 24 | 4 | 8 | Tareas del borrador anterior |
| EO-05 | Microsoft Defender for Office 365 (Plan 1 y Plan 2) | SecOps, XDR y SIEM | Incluido en M365 E5 | 8 | 25 | 4 | 8 | Tareas del borrador anterior |
| EO-06 | Microsoft Defender for Identity (ITDR Híbrido) | SecOps, XDR y SIEM | Incluido en M365 E5 | 8 | 22 | 4 | 8 | Tareas del borrador anterior |
| EO-07 | Microsoft Defender for Cloud Apps (MDA / CASB & SaaS Security) | SecOps, XDR y SIEM | Incluido en M365 E5 | 8 | 24 | 5 | 8 | Tareas del borrador anterior |
| EO-08 | Microsoft Sentinel (SIEM / SOAR Cloud-Native Asociado a M365 E5) | SecOps, XDR y SIEM | Asociado a M365 E5 (Consumo en Azure + Beneficio Data Grant E5) | 8 | 24 | 5 | 8 | Tareas del borrador anterior |
| EO-09 | Microsoft Security Copilot (IA Generativa y Agéntica para SecOps, Identidad, Endpoints y Datos) | SecOps, XDR y SIEM | Incluido con dotación base en M365 E5 (2026) + Consumo elástico por SCUs en Azure | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-10 | Microsoft Intune Plan 1 (Gestión Unificada de Endpoints y Postura en Microsoft 365 E3/E5) | Endpoints, Dispositivos y Plataforma Windows | Incluido en Microsoft 365 E5 | 8 | 23 | 5 | 8 | Tareas del borrador anterior |
| EO-11 | Microsoft Intune Suite (Capacidades Avanzadas de Gestión y Seguridad de Endpoints) | Endpoints, Dispositivos y Plataforma Windows | Complemento / Add-on sobre M365 E5 (Capacidades selectas incluidas en M365 E5 desde 2026 + Suite completa / M365 E7) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-12 | Windows Enterprise Security y Cifrado (Windows 11 Enterprise E3/E5 en Microsoft 365 E5) | Endpoints, Dispositivos y Plataforma Windows | Incluido en Microsoft 365 E5 (Windows 11 Enterprise E5) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-13 | Microsoft Purview Suite (Arquitectura Integral, Gobierno, DSPM, Seguridad para IA y Compliance Manager) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 (y modelo complementario Pay-As-You-Go en Azure) | 8 | 22 | 5 | 8 | Sin tareas en la hoja |
| EO-14 | Microsoft Purview Information Protection (Sensitivity Labels, Clasificación, Cifrado y Scanner) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 | 9 | 25 | 5 | 8 | Tareas del borrador anterior |
| EO-15 | Microsoft Purview Data Loss Prevention (Cloud, Teams, Endpoint DLP, Adaptive Protection y DLP para IA) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 | 9 | 23 | 4 | 8 | Tareas del borrador anterior |
| EO-16 | Microsoft Purview Data Lifecycle Management y Records Management | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 | 8 | 23 | 5 | 8 | Tareas integradas |
| EO-17 | Microsoft Purview Insider Risk Management | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 | 8 | 23 | 5 | 8 | Tareas integradas |
| EO-18 | Microsoft Purview Communication Compliance (Riesgo Conductual, Supervisión Regulatoria e Interacciones IA) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (+ Pay-As-You-Go para fuentes no-M365/IA) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-19 | Microsoft Purview Audit (Standard vs. Premium, Forense Cloud y Retención de 10 Años) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (1 año por defecto; 10-Year Audit Log Retention como Add-on) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-20 | Microsoft Purview eDiscovery (Experiencia Moderna Unificada y Capacidades Premium en M365 E5) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 / Microsoft Purview Suite | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-21 | Microsoft Purview Customer Lockbox, Customer Key y Privileged Access Management (M365 PAM) | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (+ costos Azure Key Vault / Managed HSM para Customer Key) | 8 | 23 | 5 | 8 | Sin tareas en la hoja |
| EO-22 | Microsoft Agent 365 (Plano de Control Empresarial de Identidad, Seguridad, Datos y Gobierno para Agentes de IA) | Gobierno y Seguridad de Agentes IA | Complemento / Add-on sobre M365 E5 (Standalone o incluido en Microsoft 365 E7: The Frontier Suite) | 9 | 24 | 5 | 8 | Sin tareas en la hoja |
|  | Total |  |  | 187 | 536 | 110 | 184 |  |

La licencia es la que declara cada guía. La referencia de esta edición para las licencias es el documento M02 «Capacidades de Microsoft por función y por licencia», que se apoya en el catálogo validado el 4 de noviembre de 2026.

**Una diferencia para revalidar.** La guía EO-11 presenta Intune Suite como un complemento sobre Microsoft 365 E5, con algunas capacidades incluidas desde 2026. El catálogo de esta edición indica que la mayoría de los componentes de Intune Suite ya viene en los planes E3, E5 y E7. Las dos lecturas no coinciden del todo: hasta revalidarlo, esta edición usa su catálogo y deja la diferencia registrada. En las demás guías, la licencia declarada es compatible con el catálogo.

### Relación con el modelo

La relación de cada guía con un dominio de operación, con las funciones del núcleo y con las capacidades de esta edición es una propuesta de esta edición. El dueño de producto y el programa de formación son los que propone el repositorio.

| ID | Guía | Dominio de operación | Funciones del núcleo | Capacidades de esta edición | Dueño de producto propuesto | Programa Ninja principal |
|---|---|---|---|---|---|---|
| EO-00 | Marco Maestro CISO, SOC y NIST | Detección y respuesta | GES-M4.1 Gestión de las operaciones de seguridad · GES-M1.1 Programa de seguridad y portafolio de productos-control · GOB-G2.1 Marcos, estándares y grilla de propiedad · GOB-G6.1 Comunicación estratégica y reporte a la dirección | Microsoft Defender XDR · Microsoft Sentinel · Microsoft Security Exposure Management | Product Owner de Gobierno Ciber, Arquitectura Zero Trust y Operación SOC (Deputy CISO / SecOps Lead) | 2 · Microsoft Defender XDR |
| EO-01 | Microsoft Entra ID | Identidades | GES-M2.2 Gestión de identidades y accesos · OPE-PR-01 Identidades y accesos de las personas · OPE-PR-02 Acceso privilegiado · OPE-RC-03 Recuperación de la identidad y de la plataforma de control | Microsoft Entra ID con Conditional Access · Microsoft Entra ID Protection · Microsoft Entra Privileged Identity Management | Product Owner de Identidad, Autenticación y Acceso Adaptativo (IAM & ITDR Product Owner) | 3 · Microsoft Entra: identidad y agentes |
| EO-02 | Microsoft Entra ID Governance | Identidades | GES-M2.2 Gestión de identidades y accesos · OPE-PR-01 Identidades y accesos de las personas · OPE-PR-02 Acceso privilegiado · OPE-PR-03 Identidades no humanas, de cargas y de agentes | Microsoft Entra ID Governance · Microsoft Entra Privileged Identity Management | Product Owner de Gobierno de Identidades, Ciclo JML y Mínimo Privilegio (IGA Product Owner) | 3 · Microsoft Entra: identidad y agentes |
| EO-03 | Defender XDR | Detección y respuesta | GES-M4.1 Gestión de las operaciones de seguridad · OPE-DE-01 Monitoreo continuo y gestión de alertas · OPE-DE-02 Ingeniería y calidad de la detección · OPE-DE-03 Búsqueda proactiva de amenazas · OPE-RS-01 Gestión y coordinación de incidentes · OPE-RS-03 Contención, erradicación y respuesta automatizada | Microsoft Defender XDR · Inteligencia de amenazas en el portal de Defender · Microsoft Security Exposure Management | Product Owner de Plataforma Unificada XDR, Gestión de Exposición (CTEM) e Incidentes (XDR & CTEM Product Owner) | 2 · Microsoft Defender XDR |
| EO-04 | Defender for Endpoint | Dispositivos | OPE-PR-04 Protección y gestión de dispositivos · OPE-ID-02 Gestión de vulnerabilidades y de la exposición · OPE-RS-02 Análisis e investigación forense · OPE-RS-03 Contención, erradicación y respuesta automatizada | Microsoft Defender for Endpoint · Microsoft Defender Vulnerability Management | Product Owner de Protección, Detección y Vulnerabilidades en Endpoints y Servidores (EDR & MDVM Product Owner) | 2 · Microsoft Defender XDR |
| EO-05 | Defender for Office 365 | Correo y colaboración | OPE-PR-05 Protección del correo y la colaboración · OPE-PR-10 Concientización y cultura de seguridad | Microsoft Defender for Office 365 · Attack simulation training | Product Owner de Seguridad de Correo, Colaboración y Resiliencia Humana Anti-Phishing (MDO Product Owner) | 2 · Microsoft Defender XDR |
| EO-06 | Defender for Identity | Identidades | OPE-DE-01 Monitoreo continuo y gestión de alertas · OPE-PR-02 Acceso privilegiado · OPE-RC-03 Recuperación de la identidad y de la plataforma de control | Microsoft Defender for Identity | Product Owner de Seguridad de Infraestructura de Identidad Híbrida Tier-0 (ITDR Active Directory / MDI Product Owner) | 2 · Microsoft Defender XDR |
| EO-07 | Defender for Cloud Apps | Aplicaciones y SaaS | OPE-ID-03 Postura de nube y de configuración · OPE-ID-04 Evaluación de riesgo de terceros · OPE-ID-07 Inventario y evaluación de sistemas de IA y agentes · OPE-PR-07 Seguridad de aplicaciones y del desarrollo | Microsoft Defender for Cloud Apps | Product Owner de Seguridad SaaS, Gobierno OAuth y Descubrimiento de Shadow IT / Shadow AI (CASB & SSPM Product Owner) | 13 · Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio |
| EO-08 | Microsoft Sentinel | SIEM y automatización | GES-M4.1 Gestión de las operaciones de seguridad · OPE-DE-01 Monitoreo continuo y gestión de alertas · OPE-DE-02 Ingeniería y calidad de la detección · OPE-DE-05 Gestión de registros y telemetría · OPE-RS-03 Contención, erradicación y respuesta automatizada | Microsoft Sentinel · Automatización de Microsoft Sentinel | Product Owner de Plataforma SIEM, Ingeniería de Detección, Data Lake y Automatización SOAR (SIEM & SOAR Product Owner) | 1 · Microsoft Sentinel |
| EO-09 | Microsoft Security Copilot | Detección y respuesta | GES-M4.1 Gestión de las operaciones de seguridad · OPE-DE-01 Monitoreo continuo y gestión de alertas · OPE-DE-03 Búsqueda proactiva de amenazas · OPE-RS-02 Análisis e investigación forense | Microsoft Security Copilot | Product Owner de Operaciones Agénticas en Seguridad y Eficiencia Analítica (Agentic SOC Product Owner) | 4 · Microsoft Security Copilot |
| EO-10 | Microsoft Intune Plan 1 | Dispositivos | OPE-PR-04 Protección y gestión de dispositivos · OPE-ID-03 Postura de nube y de configuración · GES-M3.2 Selección, implementación y evaluación de controles | Microsoft Intune · Controles de seguridad de Windows administrados con Intune | Product Owner de Gestión Unificada, Conformidad y Postura de Dispositivos (UEM & Device Compliance Product Owner) | 3 · Microsoft Entra: identidad y agentes |
| EO-11 | Microsoft Intune Suite | Dispositivos | OPE-PR-04 Protección y gestión de dispositivos · OPE-PR-02 Acceso privilegiado | Microsoft Intune | Product Owner de Mínimo Privilegio en Endpoint, PKI Cloud y Soporte Seguro (Intune Suite Product Owner) | 3 · Microsoft Entra: identidad y agentes |
| EO-12 | Windows Enterprise Security y Cifrado | Dispositivos | OPE-PR-04 Protección y gestión de dispositivos · GES-M3.2 Selección, implementación y evaluación de controles | Controles de seguridad de Windows administrados con Intune | Product Owner de Endurecimiento de Plataforma Windows 11 E5 y Cifrado (Windows Platform Security Product Owner) | 2 · Microsoft Defender XDR |
| EO-13 | Microsoft Purview Suite | Datos | GES-M2.1 Activos, datos y protección de datos personales · OPE-ID-06 Descubrimiento y clasificación de datos · GOB-G3.2 Cumplimiento y aseguramiento continuo | Microsoft Purview Data Security Posture Management · Microsoft Purview Data Map y Unified Catalog · Microsoft Purview Compliance Manager · Protecciones de Microsoft Purview para IA generativa | Product Owner de Arquitectura de Seguridad de Datos, Cumplimiento Continuo y DSPM para IA (Purview Lead / Data Governance PO) | 12 · Purview DSPM y seguridad de datos para IA |
| EO-14 | Purview Information Protection | Datos | OPE-PR-06 Protección de datos · OPE-ID-06 Descubrimiento y clasificación de datos · GES-M2.1 Activos, datos y protección de datos personales | Microsoft Purview Information Protection | Product Owner de Clasificación, Taxonomía de Sensibilidad y Cifrado de Información (MIP Product Owner) | 5 · Purview Information Protection |
| EO-15 | Purview Data Loss Prevention | Datos | OPE-PR-06 Protección de datos | Microsoft Purview Data Loss Prevention | Product Owner de Prevención Unificada de Fuga de Datos en Nube, Endpoint, Red e IA (DLP Product Owner) | 6 · Purview Data Loss Prevention |
| EO-16 | Purview DLCM y Records Management | Datos | GES-M2.1 Activos, datos y protección de datos personales · GOB-G3.1 Requisitos legales, regulatorios y contractuales · GOB-G3.2 Cumplimiento y aseguramiento continuo | Microsoft Purview Data Lifecycle Management y Records Management | Product Owner de Ciclo de Vida Documental, Minimización ROT y Registros Inmutables (DLCM & Records Product Owner) | 9 · Purview Ciclo de vida de los datos y Gestión de registros |
| EO-17 | Purview Insider Risk Management | Datos | OPE-PR-06 Protección de datos · OPE-DE-01 Monitoreo continuo y gestión de alertas · OPE-RS-02 Análisis e investigación forense | Microsoft Purview Insider Risk Management | Product Owner de Gestión de Riesgo Interno con Privacidad por Diseño (Insider Risk Product Owner) | 7 · Purview Insider Risk Management |
| EO-18 | Purview Communication Compliance | — | GOB-G3.1 Requisitos legales, regulatorios y contractuales · GOB-G3.2 Cumplimiento y aseguramiento continuo · GOB-G6.2 Liderazgo ético y medición de la efectividad | Microsoft Purview Communication Compliance e Information Barriers | Product Owner de Cumplimiento de Comunicaciones, Supervisión Regulatoria y Barreras de Información (Comm Compliance PO) | 8 · Purview Communication Compliance e Information Barriers |
| EO-19 | Purview Audit (Premium) | — | OPE-DE-05 Gestión de registros y telemetría · OPE-RS-02 Análisis e investigación forense · GOB-G3.2 Cumplimiento y aseguramiento continuo | Microsoft Purview Audit y eDiscovery | Product Owner de Trazabilidad Forense Inmutable y Telemetría de Auditoría (Purview Audit Product Owner) | 10 · Purview eDiscovery y Audit |
| EO-20 | Purview eDiscovery Premium | — | OPE-RS-02 Análisis e investigación forense · OPE-RS-04 Comunicación y notificación de incidentes · GOB-G3.1 Requisitos legales, regulatorios y contractuales | Microsoft Purview Audit y eDiscovery | Product Owner de Preservación Legal, Investigaciones Digitales y Cadena de Custodia (eDiscovery Product Owner) | 10 · Purview eDiscovery y Audit |
| EO-21 | Customer Lockbox, Customer Key y M365 PAM | — | OPE-PR-06 Protección de datos · OPE-PR-02 Acceso privilegiado · GES-M6.2 Nube, tecnologías emergentes y cadena de suministro | Customer Key y Double Key Encryption | Product Owner de Soberanía Criptográfica, Control de Acceso del Proveedor y PAM M365 (Sovereignty & Lockbox Product Owner) | 5 · Purview Information Protection |
| EO-22 | Microsoft Agent 365 | — | OPE-ID-07 Inventario y evaluación de sistemas de IA y agentes · OPE-PR-11 Protección de sistemas de IA y agentes · OPE-DE-06 Observabilidad de IA y agentes · OPE-PR-03 Identidades no humanas, de cargas y de agentes | Microsoft Agent 365 · Microsoft Entra Agent ID | Product Owner de Gobierno, Identidad, Seguridad y Observabilidad del Parque de Agentes IA (AI & Agent 365 Product Owner) | 13 · Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio |

## 4. Cómo se ubican las guías en el año de cuatro ciclos

El núcleo organiza el año en cuatro ciclos trimestrales: el ciclo 1 ocupa los días 1 a 90 e incluye el diagnóstico; los ciclos 2, 3 y 4 cierran los días 180, 270 y 365. El puente del repositorio ubica cada acción en las fases del plan 1.0. Esta edición traduce esas fases a los ciclos, con la misma equivalencia que usa el núcleo: las fases 1 a 3 corresponden al ciclo 1; la fase 4, al ciclo 2; la fase 5, al ciclo 3; y la fase 6, al ciclo 4.

| Momento de la acción | Ubicación en el plan | Qué significa | Acciones |
|---|---|---|:--:|
| Configuración puntual | Ciclos 1 y 2 | Resultados tempranos en el ciclo 1 e instalación en el ciclo 2 (fases F3 y F4 del plan 1.0). | 187 |
| Rutina periódica | Desde el ciclo 1 | Operación continua desde el diagnóstico (fases F2 a F6). | 444 |
| Rutina periódica | Ciclos 3 y 4 | Pruebas y aseguramiento en los ciclos 3 y 4 (fases F5 y F6). | 92 |
| Respuesta por evento | Ciclos 1 y 3 | Preparación en el ciclo 1 y prueba en el ciclo 3 (fases F1 y F5). | 110 |
| Total |  |  | 833 |

Lectura práctica para un producto que entra en el alcance:

1. **Ciclo 1 (días 1 a 90).** Durante el diagnóstico se decide qué guías aplican y quién es el dueño de cada producto. Se completa la configuración puntual que no admite demora, se preparan las respuestas por evento y arrancan las rutinas diarias y semanales de los productos que protegen los activos críticos.
2. **Ciclo 2 (días 91 a 180).** Se termina la configuración puntual y las rutinas periódicas quedan instaladas, con responsable y evidencia.
3. **Ciclo 3 (días 181 a 270).** Se ensayan las respuestas por evento y empiezan las rutinas de prueba y de aseguramiento.
4. **Ciclo 4 (días 271 a 365).** Se completan las pruebas, se revisa la adopción de cada guía y se prepara el informe del año.

Esta ubicación es un punto de partida. El resultado clave de cada ciclo sigue siendo el del núcleo: una guía se adelanta o se posterga según lo que muestre el diagnóstico.

### Acciones por cadencia

| Cadencia | Acciones |
|---|:--:|
| Única o por cambio | 187 |
| Diaria | 180 |
| Semanal | 141 |
| Mensual | 123 |
| Trimestral | 42 |
| Semestral | 25 |
| Anual | 25 |
| Por evento | 110 |
| Total | 833 |

## 5. Las acciones y su validación

Cada guía declara, acción por acción, si la acción está verificada en la documentación oficial de Microsoft o si es una propuesta de la guía. Esta edición reproduce esa declaración; no la comprobó.

| Momento de la acción | Acciones | Verificadas en la documentación oficial | Propuestas de la guía |
|---|:--:|:--:|:--:|
| Configuración puntual | 187 | 187 | 0 |
| Rutina periódica | 536 | 434 | 102 |
| Respuesta por evento | 110 | 106 | 4 |
| Total | 833 | 727 | 106 |

- **Configuración puntual.** Lo que se hace una vez, o cada vez que cambia el producto o el alcance. Es el trabajo de adopción.
- **Rutina periódica.** Lo que se repite con una cadencia: diaria, semanal, mensual, trimestral, semestral o anual. Es la operación.
- **Respuesta por evento.** Lo que se hace cuando ocurre algo: un incidente, un pedido legal, una baja, una saturación. Se prepara antes y se ensaya.

La hoja «Acciones de las guías» del libro tiene las 833 acciones con su guía, su cadencia, el rol que la ejecuta, la categoría de NIST CSF 2.0, su validación y su ubicación en el plan. Se filtra por guía para obtener la lista de trabajo de un producto.

## 6. Riesgo interno y ciclo de vida de los datos: integración tarea por tarea

Estas dos disciplinas no tenían tareas en el libro. Los dos borradores localizados en OneDrive son documentos de referencia y no traen tareas por cadencia; las tareas se tomaron de las guías 17 y 16 del repositorio.

| Guía | Actividades leídas | Filas nuevas | Equivalentes a una fila que ya estaba |
|---|:--:|:--:|:--:|
| Microsoft Purview Insider Risk Management | 28 | 21 | 7 |
| Microsoft Purview Data Lifecycle Management y Records Management | 28 | 26 | 2 |
| Total | 56 | 47 | 9 |

### Filas nuevas, por cadencia

| Disciplina | Diaria | Semanal | Mensual | Trimestral | Semestral | Anual | Por evento | Total |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Riesgo interno (guía 17) | 6 | 5 | 2 | 2 | 1 | 1 | 4 | 21 |
| Ciclo de vida de los datos (guía 16) | 7 | 6 | 4 | 2 | 1 | 1 | 5 | 26 |
| Total | 13 | 11 | 6 | 4 | 2 | 2 | 9 | 47 |

### Actividades que ya estaban cubiertas

No se agregó una fila: la fila existente recibió la referencia a la guía.

| Referencia | Actividad de la guía | Fila del libro | Tarea del libro |
|---|---|:--:|---|
| IRM D-02 | Triaje priorizado de alertas High Severity y vista del Purview Alert Triage Agent | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| IRM D-05 | Correlación diaria en cola unificada de incidentes de Microsoft Defender XDR | DP-D01 | Triar alertas DLP (High/Medium) e Insider Risk correlacionadas; clasificar y resolver |
| IRM S-04 | Caza proactiva semanal KQL en Microsoft Defender Portal sobre seguridad de datos | DP-W04 | Hunting sobre CloudAppEvents / EmailEvents: egress, descargas masivas, etiquetas degradadas |
| IRM M-02 | Evaluación mensual de Insider Risk Analytics y brechas de cobertura de plantillas | DP-M03 | Revisar políticas de Insider Risk con Privacidad/Legal; casos abiertos |
| IRM M-04 | Renovación preventiva del contexto del Alert Triage Agent (ventana 90 días) y control de SCUs | DP-Q02 | Revisar desempeño y costo de la flota Datos |
| IRM M-05 | Auditoría mensual de los 6 Role Groups, Administrative Units, capacidad forense y comité ejecutivo | DP-Q03 | Recertificar roles de Purview y permisos de agentes |
| IRM AH-04 | Respuesta conjunta SOC ante incidente unificado Defender XDR + Insider Risk Management | ID-A02 | Investigación de insider risk correlacionada con riesgo de identidad |
| DLM D-02 | Auditoría diaria de cambios administrativos en políticas, etiquetas y Set-RegulatoryComplianceUI | GMIP-D-08 | Validación de Cambios Administrativos del Día Anterior |
| DLM M-05 | Auditoría mensual de privilegios RBAC/PIM, límite de revisores y costos Pay-As-You-Go | DP-Q03 | Recertificar roles de Purview y permisos de agentes |

### Qué lleva cada fila nueva

- **Práctica independiente de la plataforma.** Es la del documento 16 del núcleo, «Prácticas de operación: riesgo interno y ciclo de vida de los datos», o una práctica de GM-24 cuando ya existía. Si la organización cambia de herramienta, conserva la práctica y reescribe la tarea.
- **Rol y categoría de NIST CSF 2.0.** Los que declara la guía.
- **Indicador de la tarea.** El indicador técnico de la guía, con la meta que la guía propone. Lo tienen 38 de las 47 filas.
- **Origen.** La guía y el código de la actividad, para llegar al procedimiento.

La lista de las filas nuevas está en el documento M05 «Operación por cadencias: excelencia operacional», en el dominio Datos, y la correspondencia completa de las 56 actividades, en el documento M10 «Guías de excelencia operacional del autor: qué aportan y cómo se incorporaron».

## 7. Indicadores técnicos

Cada guía trae indicadores de operación de su producto, con fórmula, meta, frecuencia y audiencia: son 184 en total, y 183 tienen una meta propuesta por la guía. No reemplazan a los indicadores del CISO: los alimentan. Un indicador técnico responde si el producto está bien operado; un indicador del CISO responde si la función cumple su objetivo.

El puente del repositorio vincula cada indicador técnico con un indicador del CISO. Usa 23 indicadores distintos:

| Indicador del CISO | Nombre | Función | Indicadores técnicos vinculados | De ellos, en una función que esta edición asocia con la guía | Guías |
|---|---|:--:|:--:|:--:|:--:|
| K41 | Cobertura de telemetría y protección de activos críticos | OPE-DE-05 | 32 | 7 | 16 |
| K37 | Datos sensibles clasificados y protegidos | OPE-PR-06 | 22 | 15 | 10 |
| K34 | Accesos privilegiados sin privilegios permanentes (JIT) | OPE-PR-02 | 17 | 11 | 10 |
| K53 | Observabilidad de agentes integrada a la detección | OPE-DE-06 | 17 | 6 | 10 |
| K43 | Técnicas de ataque priorizadas con detección validada | OPE-DE-02 | 13 | 1 | 10 |
| K32 | Escenarios críticos con playbook probado | GES-M5.1 | 12 | 0 | 9 |
| K33 | Autenticación resistente al phishing | OPE-PR-01 | 10 | 3 | 4 |
| K46 | Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo | OPE-ID-02 | 9 | 2 | 7 |
| K11 | Comportamiento seguro: tasa de reporte de phishing | OPE-PR-10 | 8 | 4 | 2 |
| K42 | Tiempo medio de detección (MTTD) | OPE-DE-01 | 8 | 4 | 7 |
| K57 | Obligaciones aplicables mapeadas a controles con evidencia vigente | GOB-G3.2 | 7 | 2 | 4 |
| K52 | Interacciones con IA protegidas contra la fuga de datos | OPE-PR-06 | 5 | 2 | 3 |
| K03 | Decisiones materiales con registro y revisión posterior | GOB-G6.2 | 4 | 0 | 1 |
| K28 | Respaldos inmutables de sistemas críticos con restauración probada | OPE-RC-01 | 4 | 0 | 1 |
| K50 | Agentes con dueño humano y autoridad delegada acotada | GES-M2.2 | 3 | 2 | 3 |
| K05 | Tiempo hasta la decisión ejecutiva en crisis | OPE-RS-05 | 2 | 0 | 1 |
| K09 | Procesos y activos críticos con dueño de riesgo designado | GOB-G4.1 | 2 | 0 | 1 |
| K20 | Tiempo de habilitación segura de iniciativas | GES-M3.1 | 2 | 0 | 1 |
| K27 | Servicios críticos concentrados en un proveedor sin alternativa | GES-M6.2 | 2 | 0 | 1 |
| K35 | Activos conformes a la línea base de configuración segura | OPE-ID-03 | 2 | 1 | 2 |
| K12 | Cobertura de capacidades críticas del equipo de seguridad | GES-M1.2 | 1 | 0 | 1 |
| K44 | Campañas de hunting que mejoran la detección | OPE-DE-03 | 1 | 1 | 1 |
| K49 | Inventario de sistemas de IA y agentes | OPE-ID-07 | 1 | 1 | 1 |
| Total |  |  | 184 | 62 |  |

En 62 de los 184 casos, el indicador del CISO pertenece a una de las funciones que esta edición asocia con la guía. En los demás, el vínculo es más general: muchos indicadores técnicos de productos distintos apuntan a un mismo indicador del CISO. Conviene usar el vínculo como punto de partida y confirmarlo indicador por indicador. La hoja «Indicadores técnicos» marca cada caso.

Cómo usarlos:

1. **Elegir pocos.** Dos o tres indicadores técnicos por guía en el alcance, los que el dueño del producto puede medir desde el primer mes.
2. **Tratar la meta como una propuesta.** Las metas son las de las guías; no son valores de referencia oficiales. La meta propia se fija con la línea base.
3. **Revisarlos en la operación.** Se leen en la revisión semanal de los controles (RT01) y se cierran cada mes (RT05). Al directorio llegan los indicadores del CISO, no los técnicos.
4. **Exigirlos al proveedor.** Si un servicio gestionado opera el producto, los indicadores técnicos de la guía son la base de la evidencia mensual.

## 8. Formación: programas, ejercicios y guías

El repositorio relaciona cada guía con un programa Ninja principal y con programas de apoyo, e informa cuántos ejercicios tiene cada programa y dónde pueden practicarse.

| N.º | Programa | Módulos | Ejercicios | De laboratorio | De laboratorio parcial | Solo en producción | Sin etiqueta | Guías que cubre como programa principal | Guías que apoya |
|:--:|---|:--:|:--:|:--:|:--:|:--:|:--:|---|---|
| 1 | Microsoft Sentinel | 41 | 145 | 105 | 30 | 4 | 6 | EO-08 | EO-00, EO-03, EO-09, EO-19 |
| 2 | Microsoft Defender XDR | 38 | 219 | 157 | 26 | 28 | 8 | EO-00, EO-03, EO-04, EO-05, EO-06, EO-12 | EO-01, EO-07, EO-08, EO-09, EO-10, EO-11 |
| 3 | Microsoft Entra: identidad y agentes | 31 | 163 | 96 | 31 | 29 | 7 | EO-01, EO-02, EO-10, EO-11 | EO-06, EO-07, EO-09, EO-12, EO-21, EO-22 |
| 4 | Microsoft Security Copilot | 30 | 159 | 48 | 76 | 29 | 6 | EO-09 | EO-00, EO-01, EO-02, EO-03, EO-04, EO-05, EO-08, EO-10, EO-11, EO-12, EO-15, EO-22 |
| 5 | Purview Information Protection | 18 | 94 | 55 | 20 | 15 | 4 | EO-14, EO-21 | EO-07, EO-13 |
| 6 | Purview Data Loss Prevention | 18 | 100 | 59 | 19 | 16 | 6 | EO-15 | EO-17 |
| 7 | Purview Insider Risk Management | 18 | 95 | 54 | 19 | 16 | 6 | EO-17 | — |
| 8 | Purview Communication Compliance e Information Barriers | 18 | 81 | 58 | 12 | 7 | 4 | EO-18 | — |
| 9 | Purview Ciclo de vida de los datos y Gestión de registros | 18 | 99 | 64 | 19 | 12 | 4 | EO-16 | EO-20 |
| 10 | Purview eDiscovery y Audit | 18 | 93 | 53 | 21 | 13 | 6 | EO-19, EO-20 | EO-21 |
| 11 | Purview Compliance Manager | 18 | 95 | 57 | 16 | 16 | 6 | — | EO-00, EO-13 |
| 12 | Purview DSPM y seguridad de datos para IA | 18 | 88 | 28 | 36 | 18 | 6 | EO-13 | EO-07, EO-14, EO-22 |
| 13 | Seguridad de Microsoft 365 Copilot, agentes y Copilot Studio | 34 | 219 | 99 | 80 | 32 | 8 | EO-07, EO-22 | EO-02, EO-10, EO-13, EO-14, EO-15, EO-16, EO-17, EO-18, EO-19, EO-20 |
| 14 | Microsoft Defender for Cloud | 41 | 327 | 201 | 81 | 37 | 8 | — | EO-04 |
| 15 | Seguridad de agentes de IA en Microsoft Foundry | 28 | 188 | 130 | 35 | 15 | 8 | — | EO-22 |
|  | Total | 387 | 2165 | 1264 | 521 | 287 | 93 |  |  |

- **De laboratorio.** El ejercicio puede hacerse completo en un entorno de prueba.
- **De laboratorio parcial.** Puede hacerse en un entorno de prueba, con funciones limitadas.
- **Solo en producción.** Necesita un entorno real: conviene acordar antes con qué permisos y con qué datos.
- **Sin etiqueta.** El repositorio no indica el entorno.

Los programas 11, 14 y 15 no son el programa principal de ninguna guía. El plan de formación por rol y por ciclo no cambia: está en el documento M06 «Plan de formación con los Ninja Training».

## 9. Lo que el repositorio no cubre y lo que esta edición no integró

| Tema | Situación | Qué hacer |
|---|---|---|
| Dominio de operación sin guía | Nube: sus 23 tareas provienen solo del plano B de GM-24 | Operar con esas tareas y con la guía oficial de Defender for Cloud |
| Guías sin dominio en la hoja Operación por cadencias | 5: EO-18 Purview Communication Compliance; EO-19 Purview Audit (Premium); EO-20 Purview eDiscovery Premium; EO-21 Customer Lockbox, Customer Key y M365 PAM; EO-22 Microsoft Agent 365 | Usar la lista de acciones de cada guía como lista de trabajo |
| Productos cuyas filas provienen del borrador anterior | 10: EO-01 Microsoft Entra ID (código ENT); EO-03 Defender XDR (código XDR); EO-04 Defender for Endpoint (código MDE); EO-05 Defender for Office 365 (código MDO); EO-06 Defender for Identity (código MDI); EO-07 Defender for Cloud Apps (código MDA); EO-08 Microsoft Sentinel (código SEN); EO-10 Microsoft Intune Plan 1 (código INT); EO-14 Purview Information Protection (código MIP); EO-15 Purview Data Loss Prevention (código DLP) | El procedimiento vigente es el de la guía del repositorio; las filas del libro conservan los títulos del borrador |
| Guías sin filas en la hoja Operación por cadencias | 11 de 23 | Están en los catálogos de acciones y de indicadores técnicos |
| Capacidades de esta edición sin guía | 19 de 50 | Operarlas con la documentación oficial |
| Funciones del núcleo sin guía | 24 de 59 | En su mayoría son funciones de gobierno y de gestión: ninguna guía de producto las reemplaza |

### Capacidades sin guía

| ID | Capacidad | Dominio |
|---|---|---|
| MS-IDE-05 | Microsoft Entra Workload ID | Identidades |
| MS-NUB-01 | Defender for Cloud: postura (Foundational CSPM y Defender CSPM) | Nube |
| MS-NUB-02 | Defender for Servers | Nube |
| MS-NUB-03 | Defender for Containers | Nube |
| MS-NUB-04 | Defender for Cloud: servicios de plataforma | Nube |
| MS-NUB-05 | DevOps security de Defender for Cloud | Nube |
| MS-NUB-06 | Azure Arc, Azure Policy y Azure Update Manager | Nube |
| MS-EXP-02 | Microsoft Defender External Attack Surface Management | Exposición |
| MS-IAA-02 | Defender for Cloud: postura de IA y Defender for AI Services | IA y agentes |
| MS-IAA-04 | Controles de seguridad de Microsoft Foundry | IA y agentes |
| MS-RED-01 | Global Secure Access (Entra Internet Access y Private Access) | Red e infraestructura |
| MS-RED-02 | Azure Firewall, Web Application Firewall y DDoS Protection | Red e infraestructura |
| MS-RED-03 | Segmentación y acceso privado en Azure | Red e infraestructura |
| MS-RED-04 | Microsoft Defender for IoT | Red e infraestructura |
| MS-RED-05 | Azure Key Vault y Managed HSM | Red e infraestructura |
| MS-RES-01 | Azure Backup | Resiliencia |
| MS-RES-02 | Azure Site Recovery | Resiliencia |
| MS-RES-03 | Microsoft 365 Backup | Resiliencia |
| MS-CUM-05 | Microsoft Priva | Cumplimiento |

### Funciones sin guía

| ID | Función |
|---|---|
| GOB-G1.1 | Contexto, mandato y autoridad del CISO |
| GOB-G1.2 | Estrategia de seguridad y alineación con el negocio |
| GOB-G2.2 | Políticas, estándares y procedimientos |
| GOB-G4.1 | Gobernanza del riesgo: estructuras y dueños |
| GOB-G4.2 | Apetito de riesgo: definición y comunicación |
| GOB-G5.1 | Supervisión de la evaluación y el análisis de riesgos |
| GOB-G5.2 | Supervisión del tratamiento y la aceptación de riesgos |
| GES-M1.2 | Finanzas, equipo, proveedores y capacitación |
| GES-M3.1 | Arquitectura de seguridad e ingeniería (Zero Trust) |
| GES-M4.2 | Gestión de amenazas, vulnerabilidades y riesgos emergentes |
| GES-M5.1 | Preparación de la respuesta a incidentes |
| GES-M5.2 | Conducción de la respuesta y aprendizaje |
| GES-M6.1 | Continuidad, recuperación y resiliencia |
| OPE-ID-01 | Inventario y descubrimiento de activos |
| OPE-ID-05 | Pruebas ofensivas y validación de controles |
| OPE-PR-08 | Seguridad de red y segmentación |
| OPE-PR-09 | Protección de cargas e infraestructura de nube |
| OPE-PR-12 | Seguridad de tecnología operacional y dispositivos conectados |
| OPE-DE-04 | Inteligencia de amenazas |
| OPE-RS-05 | Gestión de crisis y ejercicios |
| OPE-RC-01 | Respaldo y restauración |
| OPE-RC-02 | Recuperación de servicios críticos |
| OPE-RC-04 | Continuidad y operación degradada |
| OPE-RC-05 | Comunicación de la recuperación y lecciones aprendidas |

## 10. Cómo adoptarlo

1. **Definir el alcance.** En la hoja «Guías del repositorio», marque qué guías aplican según lo licenciado y lo desplegado. Una guía fuera del alcance no cuenta en el nivel de adopción.
2. **Designar al dueño de cada producto.** Es el rol R22 del núcleo, dueño de producto-control. La guía propone el perfil; la organización pone el nombre.
3. **Completar la configuración puntual.** Filtre la hoja «Acciones de las guías» por la guía y por «Configuración puntual». Registre el porcentaje completado.
4. **Instalar las rutinas.** Asigne cada rutina a un equipo propio, a un proveedor o a un agente, con su evidencia. En riesgo interno y en ciclo de vida de los datos, las rutinas ya son filas de la hoja «Operación por cadencias»; en los demás productos, se usa la lista de acciones de la guía.
5. **Ensayar la respuesta por evento.** Marque «Sí», «Parcial» o «No» según se haya ensayado. El ensayo es la prueba que sostiene el nivel «Probado» de la función.
6. **Elegir los indicadores técnicos** y vincularlos con el indicador del CISO que corresponda (sección 7).
7. **Formar al dueño y a los operadores** con el programa principal de la guía (sección 8).
8. **Revisar en cada cierre de ciclo.** El bloque 9 de la hoja Resumen muestra cuántas guías están en operación, cuántas en adopción y el nivel promedio.

El nivel de adopción de una guía es el promedio de tres datos: la configuración completada, las rutinas en operación y la respuesta por evento ensayada. Una guía se considera en operación cuando alcanza la adopción mínima definida en la hoja Parámetros.

**Si un proveedor opera el producto.** La lista de rutinas de la guía es el anexo del servicio, los indicadores técnicos son la evidencia mensual y el dueño del producto sigue siendo interno. Se aplican las comprobaciones de servicios externalizados del núcleo y la versión externalizada de los resultados clave.

## 11. Límites

- **La relación de cada guía con dominios, funciones y capacidades es una propuesta de esta edición.** El repositorio no la trae.
- **El puente del repositorio se escribió para el plan 1.0.** La ubicación en los cuatro ciclos y el vínculo con los indicadores de la versión 2.0 son una lectura de esta edición, no una afirmación del repositorio.
- **La validación es la que declara cada guía.** Esta edición no comprobó las acciones contra la documentación oficial.
- **Solo dos guías se integraron tarea por tarea.** En las demás, las filas de la hoja Operación por cadencias provienen del borrador anterior o no existen.
- **Las metas de los indicadores técnicos son propuestas de las guías.**
- **El paquete leído no se comparó archivo por archivo con el repositorio público**, y las otras carpetas del repositorio no se leyeron.
- **Microsoft Ignite (17 al 20 de noviembre de 2026) puede cambiar nombres, portales y licencias.** Las guías se validaron antes del evento.
- **Las guías y la serie Ninja Training son trabajos del autor.** No son publicaciones oficiales de Microsoft.

## Anexo. Indicadores técnicos, por guía

### EO-00 · Marco Maestro de Excelencia Operacional para la Oficina del CISO, SOC Moderno y Gobierno NIST CSF 2.0 (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 00-KPI-01 | Velocidad de Reconocimiento y Contención Crítica (MTTA / MTTC P1) | MTTA <= 15 minutos; MTTC <= 60 minutos | Diaria / Semanal | Altitud 3: SOC Manager y Equipo SecOps | K32 Escenarios críticos con playbook probado |
| 00-KPI-02 | Cobertura de Autenticación Resistente a Phishing | 100% en Roles Privilegiados; >= 85% en Usuarios Generales | Mensual | Altitud 2: CISO, IAM Lead y CIO | K33 Autenticación resistente al phishing |
| 00-KPI-03 | Índice de Mitigación de Rutas de Ataque Críticas y Postura (MSEM) | >= 90% rutas críticas mitigadas en SLA; Microsoft Secure Score >= 85% | Semanal / Mensual | Altitud 2: CISO, Cybersecurity Architects y CTO | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 00-KPI-04 | Tasa de Automatización Tier-1 y Precisión de Agentes IA | 60% - 70% automatización Tier-1; >= 95% precisión validada de agentes IA | Semanal / Mensual | Altitud 3 y 2: SOC Manager y CISO | K53 Observabilidad de agentes integrada a la detección |
| 00-KPI-05 | Índice de Cero Privilegio Permanente (Zero Standing Privilege Ratio) | >= 98% vía PIM JIT (< 5 Global Administrators elegibles; solo 2 Break-Glass activas sin uso) | Mensual | Altitud 2: CISO, IAM Lead y Auditoría Interna | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 00-KPI-06 | Efectividad Contractual del MSSP Basada en Resultados (Outcome SLA) | >= 90% precisión de escalamiento; >= 95% cumplimiento SLA en incidentes P1 | Mensual | Altitud 2: CISO, Compras/TPRM y SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 00-KPI-07 | Índice de Sostenibilidad Operativa y Retención del Talento | Holgura operativa >= 15%; Retención anual del equipo >= 88% | Mensual / Trimestral | Altitud 2 y 1: CISO, RRHH y Comité Ejecutivo | K41 Cobertura de telemetría y protección de activos críticos |
| 00-KPI-08 | Alineación al Apetito de Riesgo (FAIR) y Madurez NIST CSF 2.0 | 100% escenarios dentro de tolerancia o con plan financiado; >= 85% subcategorías en Tier 3 (Repeatable) | Trimestral / Anual | Altitud 1: Consejo de Administración (Board), CEO y CFO | K41 Cobertura de telemetría y protección de activos críticos |

### EO-01 · Microsoft Entra ID (Plan 1 / Plan 2 — Core IAM, Conditional Access e Identity Protection / ITDR) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 01-KPI-01 | Adopción de MFA Resistente a Phishing (Passkeys FIDO2 / WHfB / CBA) | 100% en Roles Administrativos; >= 85% en Usuarios Generales | Mensual | CISO, IAM Lead y Auditoría | K33 Autenticación resistente al phishing |
| 01-KPI-02 | Cobertura Efectiva de Conditional Access sobre Inicios Exitosos | >= 99% (única excepción documentada: cuentas Break-Glass sin actividad normal) | Semanal / Mensual | IAM Lead y Conditional Access Administrator | K43 Técnicas de ataque priorizadas con detección validada |
| 01-KPI-03 | Tiempo Medio de Remediación de Identidades en Riesgo Alto (MTTR-Identity) | <= 15 minutos vía auto-remediación CA/XDR; <= 4 horas en casos que requieran triaje manual | Diaria / Semanal | SOC Manager y Analistas ITDR | K53 Observabilidad de agentes integrada a la detección |
| 01-KPI-04 | Índice de Elevación Just-In-Time (Zero Standing Admin Ratio) | 100% humanos vía PIM JIT (< 5 Global Administrators elegibles) | Mensual | CISO, IAM Lead y GRC | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 01-KPI-05 | Tasa Residual de Autenticación Heredada y MFA Telefónico (SMS/Voz) | 0.0% Legacy Auth; < 2% SMS/Voz en fase final de retiro | Mensual | IAM Lead y Cybersecurity Architect | K33 Autenticación resistente al phishing |
| 01-KPI-06 | Higiene de Credenciales de Aplicaciones y Agentes IA Gobernados | >= 95% de conformidad sin secretos eternos ni agentes huérfanos | Semanal / Mensual | Cloud Application Admin y AI & Agent Governance Lead | K50 Agentes con dueño humano y autoridad delegada acotada |
| 01-KPI-07 | Salud y Vigencia de Soporte de Sincronización Híbrida | >= 99.9% ciclos exitosos; >= 3 meses de margen antes del fin de soporte de la versión | Mensual | Hybrid Identity Lead e Infraestructura TI | K33 Autenticación resistente al phishing |
| 01-KPI-08 | Identity Secure Score y Cumplimiento de Simulacro Break-Glass | Identity Secure Score >= 88%; Validación Break-Glass <= 90 días | Mensual / Trimestral | CISO y Comité de Riesgos | K34 Accesos privilegiados sin privilegios permanentes (JIT) |

### EO-02 · Microsoft Entra ID Governance (Gobierno de Ciclo de Vida JML, Derechos, Recertificación IA y Agentes) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 02-KPI-01 | SLA de Revocación Integral Leaver (Offboarding Time-to-Revoke) | < 15 min (bajas urgentes) / < 3 h (bajas programadas) | Diaria / Mensual | CISO, SOC Manager, Internal Audit | K32 Escenarios críticos con playbook probado |
| 02-KPI-02 | Tasa de Onboarding Día-1 Automatizado sin Intervención Manual | >= 98 % | Mensual | CIO, Identity Architect, RR. HH. | K41 Cobertura de telemetría y protección de activos críticos |
| 02-KPI-03 | Tasa de Decisión Explícita en Access Reviews (Efectividad Anti-Rubber-Stamping) | >= 95 % | Trimestral | CISO, GRC, Dueños de Negocio | K53 Observabilidad de agentes integrada a la detección |
| 02-KPI-04 | Índice de Cero Privilegios Permanentes (ZSP Ratio en Roles Críticos) | 100 % | Semanal | CISO, Privileged Role Administrator | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 02-KPI-05 | Cobertura de Aplicaciones Tier-1 y Tier-2 bajo Entitlement Management | >= 90 % | Trimestral | Identity Architect, GRC | K43 Técnicas de ataque priorizadas con detección validada |
| 02-KPI-06 | Higiene de Cuentas Huérfanas (Account Discovery Remediation Rate) | >= 99 % | Semanal | Identity Governance Administrator, Internal Audit | K09 Procesos y activos críticos con dueño de riesgo designado |
| 02-KPI-07 | Cobertura de Patrocinio Humano sobre Guests B2B y Agentes IA | 100 % | Semanal | CISO, AI Governance Lead | K50 Agentes con dueño humano y autoridad delegada acotada |
| 02-KPI-08 | Cumplimiento de Separation of Duties (SoD Zero-Conflict Rate) | 100 % | Semanal | GRC, CFO / SOX Compliance | K09 Procesos y activos críticos con dueño de riesgo designado |

### EO-03 · Microsoft Defender XDR (Plataforma SecOps Unificada) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 03-KPI-01 | Tiempo de reconocimiento / triaje inicial por percentiles (MTTA p50 / p90) | Severidad Crítica/Alta: p50 < 15 min, p90 < 30 min; Media: p90 < 2 horas | Semanal | SOC Lead / SOC Manager | K42 Tiempo medio de detección (MTTD) |
| 03-KPI-02 | Tiempo hasta la primera acción de contención efectiva (MTTC p50 / p90) | Automático (Attack Disruption): < 5 min; Manual en Severidad Alta: p90 < 60 min | Semanal | SOC Manager / CISO | K32 Escenarios críticos con playbook probado |
| 03-KPI-03 | Tiempo de resolución y cierre validado (MTTR p50 / p90) | Severidad Alta: p50 < 6 horas, p90 < 24 horas; Media: p90 < 72 horas | Mensual | SOC Manager / CISO | K05 Tiempo hasta la decisión ejecutiva en crisis |
| 03-KPI-04 | Tasa de falsos positivos por regla y fuente (FP Rate) | Global < 15%; < 10% en reglas personalizadas de severidad Alta | Semanal | Detection Engineer / SOC Lead | K05 Tiempo hasta la decisión ejecutiva en crisis |
| 03-KPI-05 | Tasa de resolución y contención automatizada con control de reversiones | > 50% en severidades Baja/Media con tasa de reversión (Undo) < 2% | Mensual | SOC Manager / CISO | K53 Observabilidad de agentes integrada a la detección |
| 03-KPI-06 | Tasa de conversión de cacerías de amenazas (Hunt-to-Detection Rate) | >= 20% de conversión mensual | Mensual | Threat Hunting Lead / SOC Manager | K44 Campañas de hunting que mejoran la detección |
| 03-KPI-07 | Reducción de rutas de ataque críticas y avance de Security Initiatives (CTEM) | Tendencia decreciente mensual en Choke points críticos; >= 80% de meta en iniciativas priorizadas | Mensual | CISO / Comité de Riesgo / Directorio | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 03-KPI-08 | Cobertura efectiva de sensores XDR multi-dominio | > 98% en endpoints corporativos y 100% en controladores de dominio / infraestructura Tier-0 | Mensual | Security Admin / IT Operations / CISO | K41 Cobertura de telemetría y protección de activos críticos |

### EO-04 · Microsoft Defender for Endpoint (P1/P2) y Vulnerability Management (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 04-KPI-01 | Cobertura efectiva de incorporación MDE (Onboarding Coverage) | >= 98% en estaciones de trabajo/VDI y 100% en servidores críticos | Semanal | Endpoint Security Admin / IT Operations / CISO | K43 Técnicas de ataque priorizadas con detección validada |
| 04-KPI-02 | Tasa de salud activa de sensores EDR y actualidad antimalware | >= 96% sostenido | Diaria | Endpoint Security Admin / SOC Lead | K41 Cobertura de telemetría y protección de activos críticos |
| 04-KPI-03 | Tiempo hasta aislamiento o contención de endpoint comprometido (MTTC-EP p50 / p90) | p50 < 15 minutos; p90 < 45 minutos | Semanal | SOC Lead / CISO | K41 Cobertura de telemetría y protección de activos críticos |
| 04-KPI-04 | Cobertura de las 19 reglas ASR en modo Block | 3/3 Standard protection rules en Block y >= 14 reglas totales en Block en estaciones corporativas | Mensual | Security Architect / CISO | K43 Técnicas de ataque priorizadas con detección validada |
| 04-KPI-05 | Cobertura efectiva de Tamper Protection / Controlled Configuration | >= 99% (permitiendo únicamente ventanas temporales auditadas en Troubleshooting mode) | Semanal | Endpoint Security Admin / GRC | K43 Técnicas de ataque priorizadas con detección validada |
| 04-KPI-06 | Organizational Exposure Score en Defender Vulnerability Management | Exposure Score < 30 (Low exposure) o reducción neta trimestral sostenida | Semanal | Vulnerability Lead / CISO | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 04-KPI-07 | Cumplimiento de SLA de remediación en CVEs Críticos con exploit activo | >= 90% en <= 7 días (<= 48 horas para activos expuestos o críticos) | Semanal | IT Operations / Vulnerability Lead / CISO | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 04-KPI-08 | Adopción del nivel Full Automation en grupos de dispositivos | >= 90% en estaciones de usuario (manteniendo supervisión Semi solo donde sea estrictamente necesario) | Mensual | SOC Manager / Endpoint Security Admin | K35 Activos conformes a la línea base de configuración segura |

### EO-05 · Microsoft Defender for Office 365 (Plan 1 y Plan 2) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 05-KPI-01 | Tiempo medio y p90 de reconocimiento de incidentes MDO (MTTA) | Mediana (p50) < 15 min / p90 < 30 min en severidad Alta | Semanal | SOC Manager | K11 Comportamiento seguro: tasa de reporte de phishing |
| 05-KPI-02 | Tiempo de contencion de campana y clics maliciosos (MTTC-MDO) | p90 < 30 minutos (severidad Alta) / < 2 horas (severidad Media) | Semanal | SOC Manager / CISO | K41 Cobertura de telemetría y protección de activos críticos |
| 05-KPI-03 | Tasa de automatizacion efectiva en AIR y Security Alert Triage Agent | > 80% de automatizacion con < 2% de acciones revertidas | Semanal | SOC Manager | K53 Observabilidad de agentes integrada a la detección |
| 05-KPI-04 | Mensajes maliciosos entregados por System Overrides | Tendencia a 0 (0 reglas ETR con SCL=-1 sin excepcion temporal aprobada) | Semanal | Security Admin / CISO | K11 Comportamiento seguro: tasa de reporte de phishing |
| 05-KPI-05 | Indice de alineacion en Configuration Analyzer (Standard / Strict) | >= 95% de alineacion tecnica y 0 desviaciones sin aprobacion | Mensual | Security Architect / GRC | K11 Comportamiento seguro: tasa de reporte de phishing |
| 05-KPI-06 | Tasa de compromiso en Attack Simulation Training (AST Compromise Rate) | < 6% poblacion general y < 3% en Priority Accounts | Mensual | CISO / Comite de Riesgos | K41 Cobertura de telemetría y protección de activos críticos |
| 05-KPI-07 | Ratio de reporte frente a compromiso humano (Report-to-Compromise Ratio) | > 3:1 con > 95% de finalizacion de capacitacion correctiva en 30 dias | Mensual | CISO / Concientizacion | K11 Comportamiento seguro: tasa de reporte de phishing |
| 05-KPI-08 | Cobertura de autenticacion criptografica DMARC p=reject y DKIM | 100% de dominios corporativos | Trimestral | CISO / Auditoria Interna | K43 Técnicas de ataque priorizadas con detección validada |

### EO-06 · Microsoft Defender for Identity (ITDR Híbrido) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 06-KPI-01 | Cobertura y salud operativa de sensores Tier-0 (Sensor v3.x Health Rate) | 100% de cobertura de instalacion y >= 99,5% de estado saludable | Diaria | Identity Platform Admin / SOC Manager | K43 Técnicas de ataque priorizadas con detección validada |
| 06-KPI-02 | Tiempo de reconocimiento en incidentes criticos de identidad (MTTA-ITDR) | Mediana (p50) < 10 min / p90 < 15 min en severidad Alta | Semanal | SOC Manager | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 06-KPI-03 | Tiempo medio de contencion de identidad hibrida (MTTC-ID) | p90 < 15 minutos (automatica con Attack Disruption o manual asistida) | Semanal | SOC Manager / CISO | K32 Escenarios críticos con playbook probado |
| 06-KPI-04 | Cumplimiento de postura ISPA e Identity Security Initiative | >= 85% con crecimiento mensual sostenido | Mensual | CISO / Identity Architect | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 06-KPI-05 | Volumen residual de autenticaciones heredadas (NTLMv1 y LDAP Simple Bind) | 0 eventos NTLMv1 y reduccion trimestral >= 25% en LDAP Simple Bind hasta llegar a 0 | Mensual | Identity Architect / Lideres de Infraestructura | K41 Cobertura de telemetría y protección de activos críticos |
| 06-KPI-06 | Rutas de ataque criticas abiertas hacia activos Tier-0 (Attack Paths to Tier-0) | 0 rutas criticas con credenciales expuestas o delegaciones explotables | Semanal | CISO / Identity Architect | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 06-KPI-07 | Tasa de falsos positivos en detecciones MDI | < 10% manteniendo 0 exclusiones globales amplias | Mensual | SOC Lead | K41 Cobertura de telemetría y protección de activos críticos |
| 06-KPI-08 | Exposiciones criticas abiertas en infraestructura Tier-0 (Spooler, Unconstrained, ESC1) | Exactamente 0 hallazgos abiertos | Mensual | CISO / Auditoria GRC | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |

### EO-07 · Microsoft Defender for Cloud Apps (MDA / CASB & SaaS Security) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 07-KPI-01 | Tiempo medio de reconocimiento de incidentes CASB (MTTA-CASB) | < 15 minutos (High) / < 60 minutos (Medium) | Semanal | SOC Manager | K42 Tiempo medio de detección (MTTD) |
| 07-KPI-02 | Tiempo medio de contención de amenazas SaaS y OAuth (MTTC-SaaS) | < 30 minutos (severidad Crítica / Alta) | Semanal | SOC Manager / CISO | K41 Cobertura de telemetría y protección de activos críticos |
| 07-KPI-03 | Tasa de falsos positivos en políticas de Defender for Cloud Apps (FPR) | < 15% | Mensual | SOC L3 / Security Admin | K27 Servicios críticos concentrados en un proveedor sin alternativa |
| 07-KPI-04 | Aplicaciones de IA Generativa (Shadow AI) sin clasificación de gobierno | 0 aplicaciones sin clasificar al cierre semanal | Semanal | CISO / GRC | K37 Datos sensibles clasificados y protegidos |
| 07-KPI-05 | Exposición de aplicaciones OAuth de alto privilegio no verificadas o inactivas | 0 aplicaciones pendientes por más de 7 días | Semanal | IAM Lead / CISO | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 07-KPI-06 | Tasa de remediación de recomendaciones SSPM en Secure Score | >= 75% en controles de impacto alto | Mensual | Cloud Security Architect / CISO | K27 Servicios críticos concentrados en un proveedor sin alternativa |
| 07-KPI-07 | Disponibilidad operativa de App Connectors, CAAC y Log Collectors | >= 99,5% | Semanal | Security Admin / SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 07-KPI-08 | Avance de migración de File Policies hacia Microsoft Purview | 100% completado antes del 15 de diciembre de 2026 (retiro oficial: 6 de enero de 2027) | Mensual | Compliance Lead / CISO | K52 Interacciones con IA protegidas contra la fuga de datos |

### EO-08 · Microsoft Sentinel (SIEM / SOAR Cloud-Native Asociado a M365 E5) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 08-KPI-01 | Tiempo medio de triaje / reconocimiento de incidentes (MTTA) | < 15 minutos (Crítico / High) y < 45 minutos (Medium) | Semanal | SOC Manager | K42 Tiempo medio de detección (MTTD) |
| 08-KPI-02 | Tiempo medio de cierre / resolución de incidentes (MTTC / MTTR) | < 4 horas (High) / < 24 horas (Medium) | Semanal / Mensual | SOC Manager / CISO | K32 Escenarios críticos con playbook probado |
| 08-KPI-03 | Tasa de falsos positivos del catálogo de detección (FPR) | < 15% global (< 20% máximo por regla individual antes de tuning obligatorio) | Semanal / Mensual | SOC L3 / Detection Engineer | K41 Cobertura de telemetría y protección de activos críticos |
| 08-KPI-04 | Tasa de éxito de ejecución de Playbooks SOAR (Playbook Success Rate) | >= 98% | Diaria / Semanal | SOAR Engineer / Platform Engineer | K32 Escenarios críticos con playbook probado |
| 08-KPI-05 | Porcentaje de incidentes con enriquecimiento o triaje automatizado | >= 70% | Mensual | SOC Manager | K42 Tiempo medio de detección (MTTD) |
| 08-KPI-06 | Disponibilidad de conectores críticos e integridad de reglas activas | >= 99,5% disponibilidad de conectores y 0 reglas AUTO DISABLED | Diaria / Semanal | Platform Engineer / SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 08-KPI-07 | Cobertura activa sobre técnicas prioritarias de MITRE ATT&CK v18 | >= 80% de las técnicas prioritarias del perfil de amenaza organizacional | Semestral / Mensual | Threat Hunter / CISO | K43 Técnicas de ataque priorizadas con detección validada |
| 08-KPI-08 | Índice de optimización de valor de datos en Analytics Tier (Data Value Efficiency) | >= 95% (reubicando tablas secundarias sin reglas hacia el Sentinel Data Lake) | Mensual | FinOps / Platform Engineer / CISO | K41 Cobertura de telemetría y protección de activos críticos |

### EO-09 · Microsoft Security Copilot (IA Generativa y Agéntica para SecOps, Identidad, Endpoints y Datos) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 09-KPI-01 | Reducción Porcentual de MTTR en Incidentes Asistidos por Security Copilot | >= 30 % | Mensual | CISO, SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 09-KPI-02 | Índice de Aprovechamiento Óptimo de SCUs Incluidas en M365 E5/E7 | 70 % - 92 % | Semanal / Mensual | FinOps, Security Copilot Owner | K41 Cobertura de telemetría y protección de activos críticos |
| 09-KPI-03 | Tasa de Concordancia Analítica de Agentes de Triaje (Defender y Purview) | >= 94 % | Semanal | SOC Manager, Purview Data Security Lead | K53 Observabilidad de agentes integrada a la detección |
| 09-KPI-04 | Continuidad de Autenticación de Agentes Autónomos (Zero Auth-Expiry Downtime) | 100 % | Semanal | Security Administrator, SOC Operations | K53 Observabilidad de agentes integrada a la detección |
| 09-KPI-05 | Adopción de Microsoft Entra Agent ID en Agentes Microsoft Soportados | 100 % | Mensual | Identity Architect, AI Security Engineer | K53 Observabilidad de agentes integrada a la detección |
| 09-KPI-06 | Cobertura de Telemetría Purview Audit y DSPM for AI | 100 % | Mensual | GRC, Internal Audit, Data Security Admin | K41 Cobertura de telemetría y protección de activos críticos |
| 09-KPI-07 | Tiempo Medio de Respuesta ante Alertas XPIADetected / JailbreakDetected | < 30 min | Diaria | SOC L2, AI Security Engineer | K32 Escenarios críticos con playbook probado |
| 09-KPI-08 | Tasa de Calidad Validada en Respuestas y Promptbooks (Looks Right Rate) | >= 90 % | Mensual | SOC L3, Detection Engineering Lead | K12 Cobertura de capacidades críticas del equipo de seguridad |

### EO-10 · Microsoft Intune Plan 1 (Gestión Unificada de Endpoints y Postura en Microsoft 365 E3/E5) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 10-KPI-01 | Dispositivos Noncompliant con sesión corporativa activa | 0 dispositivos | Diaria | SOC Manager / Identity Lead | K33 Autenticación resistente al phishing |
| 10-KPI-02 | Cobertura efectiva de onboarding EDR en flota gestionada | >= 98 % | Diaria | SOC Manager / Endpoint Security Engineer | K43 Técnicas de ataque priorizadas con detección validada |
| 10-KPI-03 | Tasa de cifrado verificado con Recovery Key en custodia | >= 99 % (100 % restante con excepción aprobada <= 90 días) | Semanal / Mensual | CISO / GRC & Auditoría Interna | K37 Datos sensibles clasificados y protegidos |
| 10-KPI-04 | Adherencia limpia a Security Baselines sin conflictos CSP | >= 95 % y 0 conflictos CSP > 7 días | Semanal | Endpoint Security Engineer | K35 Activos conformes a la línea base de configuración segura |
| 10-KPI-05 | Cumplimiento de SLA en Security Tasks críticas y CISA KEV | >= 95 % (100 % KEV con acción iniciada en <= 48h) | Semanal | Vulnerability Management / CISO | K33 Autenticación resistente al phishing |
| 10-KPI-06 | Tasa de adopción de Hotpatch updates sin reinicio (Windows 11 24H2+) | >= 85 % | Mensual | Endpoint Engineering / CIO / CISO | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 10-KPI-07 | Integridad de doble control administrativo (MAA + ITSM) | 100 % (0 cambios no autorizados) | Diaria / Semanal | CISO / Internal Audit | K33 Autenticación resistente al phishing |
| 10-KPI-08 | Higiene de inventario activo y erradicación de Phantom Compliant | < 3 % inactivos y 0 equipos activos en bajas RRHH > 48h | Semanal | Intune Platform Administrator / Identity Lead | K33 Autenticación resistente al phishing |

### EO-11 · Microsoft Intune Suite (Capacidades Avanzadas de Gestión y Seguridad de Endpoints) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 11-KPI-01 | Tasa de Endpoints Windows sin Administradores Locales Permanentes | >= 98 % | Mensual | CISO / Endpoint Engineering Lead | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 11-KPI-02 | Proporción de Elevaciones Gestionadas vs. No Gestionadas (EPM) | >= 99 % (< 1 % Unmanaged) | Semanal | SOC Manager / Endpoint Privilege Manager | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 11-KPI-03 | Tiempo Medio de Resolución de Solicitudes JIT Support Approved (EPM) | <= 30 minutos | Diaria / Semanal | Help Desk Manager / SOC L1-L2 | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 11-KPI-04 | Cumplimiento de Parcheo de Aplicaciones del Enterprise App Catalog (CVEs Críticos/Altos) | >= 95 % en 7 días (>= 99 % en 48 h para 0-day) | Semanal | CISO / Vulnerability Management Lead | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 11-KPI-05 | Tasa de Éxito de Emisión y Renovación SCEP en Microsoft Cloud PKI | >= 99 % | Semanal | PKI Architect / Network Security Lead | K20 Tiempo de habilitación segura de iniciativas |
| 11-KPI-06 | Conformidad de Sesiones Privilegiadas Remote Help Conciliadas con Ticket | 100 % | Semanal | Internal Audit / Help Desk Manager | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 11-KPI-07 | Tasa de Diagnóstico Resuelto con Device Query sin Sesión Interactiva | >= 45 % | Mensual | IT Operations Director / DEX Lead | K20 Tiempo de habilitación segura de iniciativas |
| 11-KPI-08 | Disponibilidad Operativa de Sitios Microsoft Tunnel for MAM | >= 99,9 % | Mensual | Mobility Lead / Infrastructure Manager | K41 Cobertura de telemetría y protección de activos críticos |

### EO-12 · Windows Enterprise Security y Cifrado (Windows 11 Enterprise E3/E5 en Microsoft 365 E5) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 12-KPI-01 | Cobertura Efectiva de Cifrado BitLocker con Clave Escrowed en Entra ID | >= 99,5 % | Semanal | CISO / Endpoint Security Lead | K37 Datos sensibles clasificados y protegidos |
| 12-KPI-02 | Tasa de Transición Completada hacia Certificados Windows UEFI CA 2023 | >= 98 % (100 % en equipos fabricados desde 2024) | Semanal | Windows Platform Architect / CISO | K41 Cobertura de telemetría y protección de activos críticos |
| 12-KPI-03 | Cumplimiento de Aislamiento VBS, HVCI y Credential Guard en Ejecución | >= 97 % | Semanal | Endpoint Security Engineer / SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 12-KPI-04 | Salud de Respaldo y Rotación Vigente en Windows LAPS | >= 99 % | Semanal | Identity Security Lead / Internal Audit | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 12-KPI-05 | Tiempo de Rotación Post-Exposición de Claves BitLocker y Contraseñas LAPS | <= 4 horas | Diaria | SOC Manager / Help Desk Manager | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 12-KPI-06 | Adopción de Inicio de Sesión Sin Contraseña (WHfB + FIDO2) | >= 92 % | Mensual | Identity Architect / CISO | K33 Autenticación resistente al phishing |
| 12-KPI-07 | Cobertura de Políticas App Control for Business en Modo Enforced | >= 90 % (100 % para Vulnerable Driver Blocklist) | Mensual | Endpoint Security Lead / SOC L3 | K46 Vulnerabilidades explotadas y exposiciones críticas remediadas en plazo |
| 12-KPI-08 | Conformidad de Perfiles Activos en Windows Firewall with Advanced Security | >= 99,8 % | Diaria / Semanal | Network Security Lead / SOC L1 | K33 Autenticación resistente al phishing |

### EO-13 · Microsoft Purview Suite (Arquitectura Integral, Gobierno, DSPM, Seguridad para IA y Compliance Manager) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 13-KPI-01 | Cobertura de etiquetado de sensibilidad sobre activos con datos sensibles | >= 90 % en repositorios críticos M365 y Fabric | Mensual | CISO / Chief Data Officer | K37 Datos sensibles clasificados y protegidos |
| 13-KPI-02 | Índice de sitios con oversharing crítico expuestos a IA | < 2 % (0 vínculos Anyone en sitios Highly Confidential) | Semanal | CISO / AI Governance Committee | K52 Interacciones con IA protegidas contra la fuga de datos |
| 13-KPI-03 | Cobertura de políticas Purview sobre agentes IA activos | 100 % | Semanal | AI Governance Lead / CISO | K53 Observabilidad de agentes integrada a la detección |
| 13-KPI-04 | Compliance Score sobre controles gestionados por el cliente | >= 85 % (100 % en controles Preventative mandatory de 27 puntos) | Mensual | GRC / DPO / Comité de Auditoría | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 13-KPI-05 | Tiempo medio de triaje (MTTA) en incidentes convergentes Datos + XDR | <= 30 minutos (High) / <= 4 horas (Medium) | Diaria / Semanal | SOC Manager / CSIRT Lead | K52 Interacciones con IA protegidas contra la fuga de datos |
| 13-KPI-06 | Efectividad operativa de Adaptive Protection y Device Onboarding | 100 % políticas activas y >= 98 % endpoints con onboarding saludable | Semanal | Data Security Lead / Endpoint Security | K37 Datos sensibles clasificados y protegidos |
| 13-KPI-07 | Cumplimiento de segregación jurisdiccional y acceso JIT a contenido | 100 % (0 accesos permanentes a texto plano de archivos/prompts) | Trimestral | DPO / Internal Audit | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 13-KPI-08 | Adherencia presupuestaria FinOps en medidores Purview PAYG y SCUs | <= 100 % (variación no planificada < 10 %) | Semanal / Mensual | FinOps / CIO / CISO | K41 Cobertura de telemetría y protección de activos críticos |

### EO-14 · Microsoft Purview Information Protection (Sensitivity Labels, Clasificación, Cifrado y Scanner) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 14-KPI-01 | Cobertura de Clasificación sobre Datos Sensibles | >= 85 % en entornos Microsoft 365 E5 (>= 70 % en E3) | Mensual | CISO, Comité de Riesgos, Reguladores | K37 Datos sensibles clasificados y protegidos |
| 14-KPI-02 | Tasa de Automatización y Etiquetado por Defecto | >= 65 % con tendencia trimestral creciente | Mensual | Data Security Architect, Dirección de Operaciones | K37 Datos sensibles clasificados y protegidos |
| 14-KPI-03 | Cobertura de Etiquetas de Contenedor en Sitios y Teams | >= 95 % general y 100 % en sitios habilitados para Microsoft 365 Copilot | Semanal | CISO, Collaboration Lead, Gobierno de IA | K37 Datos sensibles clasificados y protegidos |
| 14-KPI-04 | Tiempo Medio de Reconocimiento (MTTA) en Incidentes Críticos de Datos | < 60 minutos (severidad Critical) / < 4 horas (severidad High) | Mensual | SOC Manager, Auditoría Externa, Aseguradoras | K42 Tiempo medio de detección (MTTD) |
| 14-KPI-05 | Tiempo Medio de Contención Criptográfica (MTTC) | < 4 horas (severidad Critical) / < 8 horas (severidad High) | Mensual | CISO, SOC Manager | K32 Escenarios críticos con playbook probado |
| 14-KPI-06 | Tasa de Éxito de Auto-Labeling en Servicio | >= 98 % | Semanal | Information Protection Admin | K37 Datos sensibles clasificados y protegidos |
| 14-KPI-07 | Tasa de Justificación Válida en Bajadas de Etiqueta (Downgrades) | >= 95 % y 100 % de remociones masivas investigadas | Semanal | SOC L2, Insider Risk Management | K37 Datos sensibles clasificados y protegidos |
| 14-KPI-08 | Cumplimiento de Gestión de Cambios Administrativos | 100 % (tolerancia cero a cambios no autorizados) | Mensual | GRC, Auditoría Interna y Regulatoria | K34 Accesos privilegiados sin privilegios permanentes (JIT) |

### EO-15 · Microsoft Purview Data Loss Prevention (Cloud, Teams, Endpoint DLP, Adaptive Protection y DLP para IA) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 15-KPI-01 | Tasa de Verdaderos Positivos (Precisión de Alertas DLP) | >= 75 % | Semanal | SOC Manager, DLP Engineer | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-02 | Cobertura Efectiva de Flota en Endpoint DLP | >= 98 % | Semanal | CISO, Endpoint Security Lead | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-03 | Tiempo Medio de Reconocimiento (MTTA) en Alertas DLP Críticas/Altas | < 30 minutos (Críticas) / < 2 horas (Altas) | Mensual | SOC Manager, Auditoría Externa | K52 Interacciones con IA protegidas contra la fuga de datos |
| 15-KPI-04 | Tiempo Medio de Contención de Exfiltración (MTTC) | < 2 horas (Críticas) / < 6 horas (Altas) | Mensual | CISO, SOC Manager | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-05 | Tasa de Anulación por Usuario (Override Rate) | < 5 % general y 100 % de overrides en reglas altas auditados en 24h | Semanal | DLP Lead, Data Owners | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-06 | Proporción de Políticas en Enforcement Activo vs. Simulación | >= 85 % (cero políticas >30 días en simulación sin decisión) | Mensual | Data Security Architect, CISO | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-07 | Tasa de Prevención en Interacciones IA (Copilot y Shadow AI) | >= 95 % en políticas activas | Mensual | CISO, Comité de Gobierno de IA | K37 Datos sensibles clasificados y protegidos |
| 15-KPI-08 | Cumplimiento de Migración MDCA (2027-01-06) y Control de Cambios | 100 % | Mensual | GRC, Cloud Security Lead, Auditoría | K52 Interacciones con IA protegidas contra la fuga de datos |

### EO-16 · Microsoft Purview Data Lifecycle Management y Records Management (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 16-KPI-01 | Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA) | 100% | Mensual | CISO / Oficial de Cumplimiento | K43 Técnicas de ataque priorizadas con detección validada |
| 16-KPI-02 | Cumplimiento de SLA en Revisiones de Disposición | >= 95% (0 ítems > 30 días) | Semanal / Mensual | Records Manager / Legal | K03 Decisiones materiales con registro y revisión posterior |
| 16-KPI-03 | Completitud de Resguardo Mensual de Proof of Disposal | 100% (12/12 meses) | Mensual | Auditoría Interna / GRC | K41 Cobertura de telemetría y protección de activos críticos |
| 16-KPI-04 | Precisión en Políticas de Auto-Aplicación de Etiquetas | >= 92% | Semanal / Mensual | Records Manager / Data Governance Lead | K37 Datos sensibles clasificados y protegidos |
| 16-KPI-05 | Conciliación de Eventos y Asset ID en Event-Based Retention | >= 99% | Mensual | Records Manager / Dueños de Proceso | K03 Decisiones materiales con registro y revisión posterior |
| 16-KPI-06 | Reducción de Deuda de Retención en Exempleados | Reducción sostenida hasta 0 retenciones infinitas sin causa legal | Mensual / Trimestral | DPO / Oficial de Cumplimiento / FinOps | K41 Cobertura de telemetría y protección de activos críticos |
| 16-KPI-07 | Tasa de Minimización de Datos ROT Pre-IA | >= 85% anual | Mensual | CISO / Líder de Seguridad IA | K03 Decisiones materiales con registro y revisión posterior |
| 16-KPI-08 | Integridad de Cambios Administrativos y Priority Cleanup | 100% | Diaria / Mensual | CISO / SOC Manager / Auditoría Interna | K03 Decisiones materiales con registro y revisión posterior |

### EO-17 · Microsoft Purview Insider Risk Management (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 17-KPI-01 | Tiempo Medio de Triaje de Alertas Críticas (MTTA - High Severity) | <= 4 horas hábiles (100% < 24 h) | Diaria / Semanal | SOC Manager / Líder IRM | K42 Tiempo medio de detección (MTTD) |
| 17-KPI-02 | Tasa de Verdaderos Positivos por Política (Signal-to-Noise Ratio) | >= 65% | Semanal / Mensual | Insider Risk Management Admins / Ingeniería Detección | K37 Datos sensibles clasificados y protegidos |
| 17-KPI-03 | Disponibilidad y Frescura de Conectores Críticos (HR y Endpoints) | >= 99% | Diaria / Mensual | Insider Risk Management Admins / Plataforma | K41 Cobertura de telemetría y protección de activos críticos |
| 17-KPI-04 | Efectividad de Contención Automática (Adaptive Protection) | >= 95% | Mensual | CISO / Arquitecto Zero Trust | K37 Datos sensibles clasificados y protegidos |
| 17-KPI-05 | Tasa de Corrección Conductual Post-Notificación (Notices) | >= 85% | Trimestral / Semestral | Recursos Humanos / Concientización / CISO | K41 Cobertura de telemetría y protección de activos críticos |
| 17-KPI-06 | Cumplimiento de Privacidad, Segregación SoD y Doble Autorización Forense | 100% | Diaria / Mensual | DPO / Auditoría Interna / Legal | K37 Datos sensibles clasificados y protegidos |
| 17-KPI-07 | Tiempo Medio de Escalamiento Defensible a Purview eDiscovery | <= 8 horas | Mensual | General Counsel / Investigadores L3 | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 17-KPI-08 | Continuidad del Alert Triage Agent y Cobertura de Políticas IA / Agentes | 100% | Mensual | SOC Manager / Líder Seguridad IA | K53 Observabilidad de agentes integrada a la detección |

### EO-18 · Microsoft Purview Communication Compliance (Riesgo Conductual, Supervisión Regulatoria e Interacciones IA) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 18-KPI-01 | SLA de Triaje de Alertas de Severidad Alta (LLM >= 4 y Amenazas) | >= 98 % | Diaria / Semanal | Chief Compliance Officer, RR. HH., SOC Manager | K42 Tiempo medio de detección (MTTD) |
| 18-KPI-02 | Cumplimiento de Cuota de Supervisión Regulatoria (SEC / FINRA) | 100 % (0 ítems pendientes > 5 días hábiles) | Semanal / Mensual | Chief Compliance Officer, Auditoría Interna | K37 Datos sensibles clasificados y protegidos |
| 18-KPI-03 | Tasa de Precisión de Políticas (Actionable / True Positive Rate) | >= 65 % (Falsos positivos <= 35 %) | Semanal | Communication Compliance Admin, Lead Analyst | K11 Comportamiento seguro: tasa de reporte de phishing |
| 18-KPI-04 | Cobertura de Supervisión sobre Aplicaciones GenAI y Agentes (Agent 365) | 100 % | Mensual | CISO, AI Governance Lead | K53 Observabilidad de agentes integrada a la detección |
| 18-KPI-05 | Tiempo Medio de Contención de Mensajes Reportados en Teams | <= 4 horas laborales | Semanal | RR. HH., Relaciones Laborales | K32 Escenarios críticos con playbook probado |
| 18-KPI-06 | Salud de Capacidad de Buzones de Supervisión (Review Mailboxes) | 100 % (0 desactivaciones automáticas por saturación) | Semanal | Communication Compliance Admin | K11 Comportamiento seguro: tasa de reporte de phishing |
| 18-KPI-07 | Índice de Integridad de Segregación RBAC y Seudonimización | 100 % | Mensual | Data Protection Officer (DPO), CISO, Auditoría Interna | K11 Comportamiento seguro: tasa de reporte de phishing |
| 18-KPI-08 | Efectividad Pedagógica Post-Notificación (Tasa de No-Reincidencia) | >= 85 % | Trimestral | Chief Compliance Officer, Cultura y Ética, CISO | K11 Comportamiento seguro: tasa de reporte de phishing |

### EO-19 · Microsoft Purview Audit (Standard vs. Premium, Forense Cloud y Retención de 10 Años) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 19-KPI-01 | Cobertura Efectiva del Plan Microsoft 365 Advanced Auditing en Población E5 | 100 % | Semanal | CISO, Purview Admin, Identity Lead | K43 Técnicas de ataque priorizadas con detección validada |
| 19-KPI-02 | Cobertura de Activación de SearchQueryInitiatedExchange en Buzones | 100 % | Semanal | SOC Manager, DFIR Lead | K43 Técnicas de ataque priorizadas con detección validada |
| 19-KPI-03 | Integridad Continua del Pipeline UAL y Cero Bypass No Autorizado | 100 % | Diaria / Mensual | CISO, Internal Audit | K41 Cobertura de telemetría y protección de activos críticos |
| 19-KPI-04 | Porcentaje de Migración a Microsoft Graph AuditLogQuery API (MC1505599) | 100 % antes de Q2 2027 (retiro definitivo 15-oct-2027) | Semanal / Mensual | SecOps Engineering Lead, SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |
| 19-KPI-05 | Tiempo Medio de Triaje ante Estrangulamiento MailItemsAccessed (IsThrottled) | <= 30 minutos | Diaria | SOC Manager, DFIR Lead | K42 Tiempo medio de detección (MTTD) |
| 19-KPI-06 | Conformidad de Retención Regulatoria (1 Año / 10 Años / Data Lake SPN) | 100 % | Mensual / Trimestral | Chief Compliance Officer, Legal, GRC | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 19-KPI-07 | Tasa de Extracciones Forenses Sin Truncamiento (isRecordCountLimitExceeded = false) | 100 % | Mensual | DFIR Lead, General Counsel | K41 Cobertura de telemetría y protección de activos críticos |
| 19-KPI-08 | Salud y Puntualidad del Streaming OfficeActivity hacia Microsoft Sentinel | >= 99,5 % | Diaria / Semanal | SIEM Architect, SOC Manager | K41 Cobertura de telemetría y protección de activos críticos |

### EO-20 · Microsoft Purview eDiscovery (Experiencia Moderna Unificada y Capacidades Premium en M365 E5) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 20-KPI-01 | Efectividad de Aplicación de Holds Legales | >= 99.5 % (remediación de errores en < 24 h) | Semanal | General Counsel / Compliance Officer | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 20-KPI-02 | Tiempo Medio de Congelamiento Probatorio (MTTH) | <= 4 horas en investigaciones críticas | Mensual | CISO / General Counsel | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 20-KPI-03 | Tasa de Acuse de Notificación Legal por Custodios | >= 98 % dentro de 10 días hábiles | Semanal | Legal Operations / DPO | K32 Escenarios críticos con playbook probado |
| 20-KPI-04 | Ratio de Reducción Documental por Analítica (Culling Rate) | >= 45 % en casos con más de 10.000 ítems | Mensual | General Counsel / FinOps Legal | K32 Escenarios críticos con playbook probado |
| 20-KPI-05 | Tiempo de Contención ante Derrame de Datos en IA (Search & Purge) | <= 2 horas | Por incidente / Mensual | CISO / SOC Manager | K32 Escenarios críticos con playbook probado |
| 20-KPI-06 | Cumplimiento de Segregación eDiscovery Administrator | <= 3 cuentas nominales humanas y 0 Service Principals | Mensual | CISO / Auditoría Interna | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 20-KPI-07 | Cumplimiento en Plazo de Solicitudes Regulatorias y DSR | 100 % | Mensual | DPO / Comité de Riesgos | K57 Obligaciones aplicables mapeadas a controles con evidencia vigente |
| 20-KPI-08 | Higiene de Exportaciones y Control de Desvío PAYG | 0 paquetes perdidos y <= 5 % de desvío mensual PAYG | Mensual | FinOps / eDiscovery Administrator | K41 Cobertura de telemetría y protección de activos críticos |

### EO-21 · Microsoft Purview Customer Lockbox, Customer Key y Privileged Access Management (M365 PAM) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 21-KPI-01 | Cobertura de Auditoría Post-Acceso Lockbox (Microsoft Operator) | 100 % en <= 24 h | Por evento / Mensual | CISO / DPO / Auditoría Interna | K43 Técnicas de ataque priorizadas con detección validada |
| 21-KPI-02 | Cobertura Efectiva de Cifrado Customer Key | >= 99.9 % | Semanal | Cloud Security Architect / CISO | K37 Datos sensibles clasificados y protegidos |
| 21-KPI-03 | Incidencias de Fallback No Planificado a la Availability Key | 0 eventos por error operativo | Diaria / Mensual | Cryptography Lead / SOC Manager | K28 Respaldos inmutables de sistemas críticos con restauración probada |
| 21-KPI-04 | Cumplimiento de Inmutabilidad en Bóvedas Criptográficas | 100 % | Mensual | Cryptography Lead / GRC | K28 Respaldos inmutables de sistemas críticos con restauración probada |
| 21-KPI-05 | Margen de Seguridad de Licenciamiento Customer Key | >= 5 % de superávit continuo | Semanal | FinOps / Compliance Officer | K28 Respaldos inmutables de sistemas críticos con restauración probada |
| 21-KPI-06 | Tasa de Aprobación Peer-Review en M365 PAM sin Autoaprobación | 100 % (0 autoaprobaciones) | Mensual | Identity Lead / Auditoría Interna | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 21-KPI-07 | Higiene y No Interactividad de SystemAccounts en M365 PAM | <= 2 cuentas y 100 % no interactivo | Mensual | Identity Lead / SOC Manager | K34 Accesos privilegiados sin privilegios permanentes (JIT) |
| 21-KPI-08 | Tasa de Éxito en Pruebas Trimestrales de Restauración de Claves | 100 % | Trimestral | CISO / Comité de Riesgos | K28 Respaldos inmutables de sistemas críticos con restauración probada |

### EO-22 · Microsoft Agent 365 (Plano de Control Empresarial de Identidad, Seguridad, Datos y Gobierno para Agentes de IA) (8)

| ID | Indicador técnico | Meta de la guía | Frecuencia | Audiencia | Indicador del CISO según el repositorio |
|---|---|---|:--:|---|---|
| 22-KPI-01 | Cobertura de Agentes Gobernados en Microsoft Agent 365 | >= 98 % | Mensual | CISO, CIO, AI Administrator | K53 Observabilidad de agentes integrada a la detección |
| 22-KPI-02 | Tasa de Agentes con Owner y Sponsor Humano Activo | 100 % (0 agentes huérfanos por más de 24 horas) | Diaria | AI Administrator, Entra Agent ID Admin | K50 Agentes con dueño humano y autoridad delegada acotada |
| 22-KPI-03 | Cobertura de Identidad Entra Agent ID y Acceso Condicional | >= 99 % | Mensual | CISO, Entra Agent ID Admin | K53 Observabilidad de agentes integrada a la detección |
| 22-KPI-04 | Tiempo Medio de Contención de Agentes de Alto Riesgo (MTTC-Agent) | <= 30 minutos | Diaria | SOC Manager, CISO | K53 Observabilidad de agentes integrada a la detección |
| 22-KPI-05 | Tasa de Mitigación de Agentes Locales Shadow AI No Autorizados | >= 95 % en menos de 7 días | Semanal | Security Admin, Endpoint Management Lead | K49 Inventario de sistemas de IA y agentes |
| 22-KPI-06 | Cobertura de Gobernanza Granular y Gateway en Servidores MCP | 100 % | Semanal | AI Administrator, Security Admin | K53 Observabilidad de agentes integrada a la detección |
| 22-KPI-07 | Índice de Confiabilidad de Herramientas Agénticas (Tasa de Excepción <= 1 %) | >= 95 % | Semanal | CIO, CAIO, Agent Owners | K53 Observabilidad de agentes integrada a la detección |
| 22-KPI-08 | Puntaje de Cumplimiento Regulatorio de IA y Control de Sobrescompartición | >= 90 % de puntaje y 0 agentes High Risk sin remediación > 7 días | Trimestral | GRC / AI Ethics, Purview Data Security AI Admin, CISO | K53 Observabilidad de agentes integrada a la detección |

---

*Frontier CISO Atlas · Modelo Operativo CISO 365 · edición Microsoft · versión 2.1 · revisión 3 · 15 de noviembre de 2026 · propuesta sujeta a validación · @SCavanna*

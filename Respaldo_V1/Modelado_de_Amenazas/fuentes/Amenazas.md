En la taxonomía formal de gestión de riesgos de ciberseguridad (marcos como ISO/IEC 27005, NIST SP 800-30 y FAIR), el **ransomware se clasifica estrictamente como una amenaza** (específicamente, una técnica de ataque o herramienta maliciosa ejecutada por un actor de amenaza), **no como un riesgo**.

La confusión entre ambos términos suele surgir en la comunicación ejecutiva cuando se abrevia el lenguaje, pero mantener la distinción taxonómica es fundamental para modelar escenarios y asignar presupuesto.

### 1. Desglose taxonómico según marcos estándar

Para que exista un **riesgo**, se requiere la convergencia de múltiples variables. El ransomware ocupa solo uno de los eslabones de esa ecuación:

| **Concepto**                                   | **Definición Formal (NIST / ISO 27005)**                     | **Aplicación al caso del Ransomware**                        |
| ---------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Actor de Amenaza** (*Threat Actor*)          | Entidad con capacidad e intención de causar daño.            | Grupos de cibercrimen organizado, afiliados RaaS (*Ransomware-as-a-Service*), estados-nación. |
| **Amenaza / Evento** (*Threat / Threat Event*) | Cualquier circunstancia o evento con el potencial de impactar adversamente en las operaciones. | **El Ransomware en sí mismo** (el código malicioso) y la acción de cifrado/exfiltración de datos. |
| **Vulnerabilidad** (*Vulnerability*)           | Debilidad en un sistema, proceso o control que puede ser explotada. | Servidores RDP expuestos sin MFA, software sin parches, copias de seguridad inmutables mal configuradas, falta de segmentación. |
| **Activo** (*Asset*)                           | Recurso de valor para la organización que requiere protección. | Bases de datos transaccionales, controladores de dominio, propiedad intelectual, sistemas ERP. |
| **Riesgo** (*Risk*)                            | La probabilidad de que una amenaza explote una vulnerabilidad y el impacto resultante en el negocio. | **La pérdida financiera, operativa o reputacional** derivada de la interrupción de operaciones críticas por el cifrado de sistemas debido a un ataque de ransomware. |

### 2. Formulación correcta en el registro de riesgos

En un registro de riesgos (*Risk Register*) o ante un Comité de Auditoría, listar "Ransomware" en la columna de riesgos es un error metodológico porque impide medir la probabilidad y el impacto de forma granular.

- **Enunciado incorrecto (confunde amenaza con riesgo):** *"Riesgo de Ransomware."*
- **Enunciado correcto (estructura Causa → Evento → Impacto):** *"Riesgo de interrupción prolongada de la cadena de suministro y pérdida de ingresos por [X] millones de dólares, debido al cifrado de los servidores ERP (impacto/evento) mediante un ataque de ransomware (amenaza) que explote credenciales comprometidas sin doble factor de autenticación (vulnerabilidad)."*

### 3. Implicación estratégica en la gestión y gobernanza

Diferenciar ambos conceptos cambia el enfoque de defensa y reporte:

1. **Sobre la amenaza (Ransomware) no tienes control:** No puedes reducir la existencia del ransomware en el ecosistema global ni disuadir directamente a los grupos criminales.
2. **Sobre el riesgo sí tienes control:** El riesgo se gestiona reduciendo la superficie de exposición (mitigando vulnerabilidades como accesos privilegiados o falta de segmentación) y acotando el impacto (implementando respaldos inmutables y planes de continuidad de negocio probados).

Cuando un directorio pregunta *"¿Cuál es nuestro riesgo de ransomware?"*, la respuesta técnica rigurosa consiste en traducir esa inquietud hacia los **escenarios de impacto al negocio** (tiempo máximo de inactividad tolerable, costo por hora de parada operativa y exposición regulatoria por exfiltración) que esa amenaza específica podría desencadenar sobre los activos críticos actuales.







El Ransomware forma parte de una lista de posibles amenazas de ciberseguridad y privacidad, correcto? Cuál es la lista completa que típicamente usan las organizaciones para modelar/estimar/mitigar riesgos?





Efectivamente, el ransomware es solo un ítem dentro de catálogos estructurados de amenazas. En la práctica empresarial madura, las organizaciones no utilizan una única lista universal, sino que combinan **tres taxonomías estándar** según el nivel de abstracción que requiera el análisis: catálogos de **gestión de riesgos y cumplimiento** (ISO/ENISA), catálogos **técnicos y operacionales** (MITRE ATT&CK) y catálogos específicos de **privacidad y protección de datos** (LINDDUN / NIST Privacy).

Para modelar, estimar y mitigar riesgos de forma integral en una organización grande, los marcos de referencia que definen las listas completas son los siguientes:

---

### 1. Catálogos de Amenazas de Ciberseguridad (Nivel Gestión y Riesgo)

Cuando se construye un registro de riesgos corporativo bajo **ISO/IEC 27005** (Anexo A de versiones anteriores / guías de implementación) o se utiliza el mapa de amenazas de la **Agencia de la Unión Europea para la Ciberseguridad (ENISA Threat Landscape)**, las amenazas se agrupan en categorías exhaustivas que cubren tanto ataques deliberados como fallos no maliciosos:

| Categoría de Amenaza                                         | Amenazas Específicas Típicas                                 | Ejemplo de Escenario / Vector                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1. Malware y Código Malicioso**                            | **Ransomware**, Wipers (destructores), Troyanos bancarios, Infostealers, Rootkits, Cryptojacking. | Cifrado de servidores críticos tras intrusión por phishing o explotación perimetral. |
| **2. Ingeniería Social y Compromiso de Identidad**           | Phishing, Spear-phishing, Business Email Compromise (BEC), Credential Stuffing, AitM (Adversary-in-the-Middle). | Robo de tokens de sesión de administradores globales evadiendo MFA tradicional. |
| **3. Ataques a Aplicaciones Web y APIs**                     | Inyección SQL/Código, Cross-Site Scripting (XSS), Broken Object Level Authorization (BOLA), SSRF. | Exfiltración masiva de bases de datos de clientes a través de una API pública mal validada. |
| **4. Denegación de Servicio**                                | DDoS volumétrico, DDoS de capa de aplicación (L7), Ransom DDoS (RDoS). | Indisponibilidad de canales digitales transaccionales o portales de atención crítica. |
| **5. Amenazas Internas (*Insider Threats*)**                 | Abuso de privilegios (malicioso), negligencia operacional, exfiltración previa a desvinculación. | Administrador de bases de datos que descarga información confidencial antes de renunciar. |
| **6. Compromiso de la Cadena de Suministro**                 | Compromiso de proveedores de software (updates maliciosos), brechas en terceros (BPO/SaaS), dependencias Open Source. | Compromiso de un proveedor de soporte TI con acceso VPN directo a la red interna. |
| **7. Explotación de Infraestructura y Configuración**        | Explotación de vulnerabilidades Zero-Day / N-Day, Misconfiguration en Cloud (buckets públicos, IAM excesivo). | Acceso no autorizado a repositorios en la nube por permisos excesivos en roles de servicio. |
| **8. Amenazas Físicas y Ambientales**                        | Robo de dispositivos, sabotaje físico, incendios, inundaciones, cortes prolongados de energía o telecomunicaciones. | Destrucción de un centro de datos local o corte de fibra óptica redundante. |
| **9. Fallos Técnicos y Errores Humanos**                     | Errores de configuración en producción, fallos de hardware, corrupción de datos, pérdida de claves criptográficas. | Borrado accidental de volúmenes de almacenamiento en producción sin respaldo reciente. |
| **10. Intercepción y Manipulación de Información**           | Man-in-the-Middle (MitM), espionaje de red, envenenamiento de DNS/BGP, manipulación de integridad de datos. | Modificación no autorizada de registros financieros o parámetros de sistemas industriales (OT). |
| **11. Amenazas Específicas de IA (OWASP Top 10 for LLMs / MITRE ATLAS)** | Prompt Injection, Data Poisoning, Model Inversion / Extraction, Excessive Agency de agentes autónomos. | Manipulación de un agente de IA corporativo para que ejecute acciones privilegiadas o filtre datos. |

---

### 2. Catálogo Técnico Operacional: MITRE ATT&CK

Mientras que listas como ISO 27005 o ENISA nombran *qué* ocurre a nivel macro (ej. "Ransomware"), los equipos de arquitectura, detección y respuesta (SOC/Blue Team) modelan las amenazas utilizando **MITRE ATT&CK** (*Adversarial Tactics, Techniques, and Common Knowledge*).

ATT&CK no es una lista plana de amenazas, sino una matriz de **14 Tácticas** (el objetivo técnico del atacante en cada fase) desglosadas en más de **200 Técnicas y 400 Subtécnicas**:

1. **Reconnaissance** (Recopilación de información previa).
2. **Resource Development** (Adquisición de infraestructura, cuentas o capacidades).
3. **Initial Access** (Phishing, explotación de aplicaciones públicas, cuentas válidas).
4. **Execution** (PowerShell, scripts, binarios maliciosos).
5. **Persistence** (Creación de cuentas, modificación de registros, tareas programadas).
6. **Privilege Escalation** (Explotación de vulnerabilidades locales, abuso de tokens).
7. **Defense Evasion** (Desactivación de EDR, ofuscación, Living-off-the-Land).
8. **Credential Access** (Volcado de memoria LSASS, Kerberoasting, fuerza bruta).
9. **Discovery** (Enumeración de Active Directory, escaneo de red interna).
10. **Lateral Movement** (Uso de RDP, SMB, WMI, robo de sesiones).
11. **Collection** (Recopilación y empaquetado de datos internos).
12. **Command and Control** (Canales cifrados de comunicación externa, túneles DNS/HTTPS).
13. **Exfiltration** (Transferencia de datos hacia infraestructura del atacante).
14. **Impact** (**Aquí se ubica técnicamente el Ransomware** bajo la técnica *T1486 - Data Encrypted for Impact*, junto con *Service Stop*, *Data Destruction*, etc.).

---

### 3. Catálogo de Amenazas a la Privacidad: Metodología LINDDUN

Cuando el objetivo es modelar riesgos de **privacidad y protección de datos personales** (requerido por regulaciones como GDPR, LGPD o leyes locales de protección de datos, y alineado con **ISO/IEC 27701** y el **NIST Privacy Framework**), las amenazas de ciberseguridad tradicionales son insuficientes, porque una organización puede sufrir una violación de privacidad **sin que exista ningún ciberataque ni brecha de seguridad** (por ejemplo, por recolección excesiva o uso secundario no consentido).

El estándar de referencia en ingeniería de privacidad para listar estas amenazas es **LINDDUN** (análogo a STRIDE en seguridad):

* **L — Linking (Vinculación):** Capacidad de asociar dos o más registros o acciones anónimas para deducir que pertenecen al mismo individuo.
* **I — Identifying (Identificación):** Capacidad de descubrir la identidad real de un sujeto a partir de un conjunto de datos supuestamente anonimizados o seudonimizados.
* **N — Non-repudiation (No repudio):** Imposibilidad de un usuario de negar haber realizado una acción o transacción cuando la privacidad requiere negabilidad plausible (ej. denuncias anónimas o historiales médicos).
* **D — Detecting (Detección):** Capacidad de un tercero de deducir si un registro o individuo existe dentro de una base de datos (ej. ataques de inferencia de membresía en modelos de IA).
* **D — Data Disclosure (Divulgación de datos):** Exposición excesiva, recolección desproporcionada o acceso no autorizado a datos personales (el único punto donde se solapa directamente con la confidencialidad en ciberseguridad).
* **U — Unawareness (Desconocimiento / Falta de transparencia):** Procesamiento de datos sin que el titular comprenda qué datos se recolectan, con qué fin o bajo qué base legal (fallos de consentimiento y control).
* **N — Non-compliance (Incumplimiento normativo):** Tratamiento de datos que viola leyes, políticas internas de retención, transferencia internacional o principios de minimización.

---

### Cómo articulan las organizaciones estas listas en la práctica

En un programa de gobernanza maduro, estas taxonomías operan en cascada:

1. **Para el Directorio y Comité de Riesgos:** Se consolidan las amenazas en **10 a 15 escenarios de riesgo de negocio** (basados en el catálogo ENISA / ISO 27005 + riesgos de incumplimiento LINDDUN), cuantificando pérdida financiera y tolerancia al impacto.
2. **Para Arquitectura y Operaciones (CISO / SOC):** Cada escenario de negocio se mapea contra técnicas específicas de **MITRE ATT&CK** (para validar cobertura de controles preventivos y detectivos) y contra categorías **LINDDUN** durante las Evaluaciones de Impacto en la Privacidad (PIA / DPIA) de nuevos proyectos o despliegues de IA.

### Fuentes de referencia verificables

* **ENISA Threat Landscape:** [https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends](https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends)
* **MITRE ATT&CK Enterprise Matrix:** [https://attack.mitre.org/matrices/enterprise/](https://attack.mitre.org/matrices/enterprise/)
* **LINDDUN Privacy Engineering Framework:** [https://linddun.org/](https://linddun.org/)
* **OWASP Top 10 for Large Language Model Applications:** [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)







Diseña una matriz de gobierno que muestre cómo vincular los escenarios de riesgo ejecutivo (ENISA/ISO 27005) con los controles técnicos (MITRE ATT&CK) y los requisitos de privacidad (LINDDUN).









Para operar un programa de ciberseguridad y privacidad sin silos en una organización de gran escala, el CISO y el DPO (Data Protection Officer) requieren una **estructura de trazabilidad bidireccional**: que permita al Directorio entender el impacto financiero y regulatorio (nivel superior), mientras los equipos de arquitectura, SOC e ingeniería de privacidad ejecutan controles verificables (nivel inferior).

La siguiente matriz articula **6 escenarios de riesgo ejecutivo representativos** (basados en el catálogo de amenazas ENISA / ISO 27005) vinculando en una misma línea:

1. **Capa Ejecutiva (Riesgo de Negocio):** El escenario formulado bajo estructura *Amenaza + Vulnerabilidad + Impacto* y las métricas de apetito/tolerancia.
2. **Capa Técnica Operacional (MITRE ATT&CK):** Las tácticas y técnicas críticas que habilitan el escenario y los controles arquitectónicos de mitigación.
3. **Capa de Privacidad (LINDDUN / ISO 27701):** Las amenazas específicas sobre los datos personales y los controles de protección/cumplimiento regulatorio asociados.

### Matriz Integrada de Gobierno: Riesgo Ejecutivo, Defensa Técnica y Privacidad

| **1. Escenario de Riesgo Ejecutivo (ENISA / ISO 27005)**     | **2. Tácticas y Técnicas Críticas (MITRE ATT&CK)**           | **3. Controles Técnicos Clave (Arquitectura / SOC)**         | **4. Amenazas de Privacidad (LINDDUN)**                      | **5. Controles de Privacidad y Gobernanza (DPO / Legal)**    | **6. KPIs / KRIs de Reporte al Directorio**                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Escenario 1: Extorsión y Parálisis Operativa**  • *Amenaza:* Ransomware con doble extorsión.  • *Impacto:* Detención de operaciones críticas (ERP/OT) y filtración de datos corporativos y de clientes. | • **Initial Access:** Phishing (`T1566`), Valid Accounts (`T1078`).  • **Credential Access:** OS Credential Dumping (`T1003`).  • **Lateral Movement:** Remote Services (`T1021`).  • **Exfiltration:** Exfiltration Over Web Service (`T1567`).  • **Impact:** Data Encrypted for Impact (`T1486`). | • MFA resistente a phishing (FIDO2/Passkeys) en accesos privilegiados y remotos.  • Microsegmentación de red y restricción de movimiento lateral (Tiering).  • EDR/XDR con aislamiento automático de endpoints.  • Respaldos inmutables y aislados (air-gapped). | • **Data Disclosure (D):** Exposición pública de datos sensibles robados en sitios de extorsión.  • **Non-compliance (N):** Incumplimiento de plazos legales de notificación de brechas (ej. 72h GDPR / reguladores locales). | • Clasificación y etiquetado automático de datos personales (DLP/Purview).  • Cifrado en reposo con gestión de claves separada.  • Playbook integrado CISO-DPO-Legal para notificación de brechas y evaluación de daño a titulares. | • **RTO real** validado en simulacros vs. RTO tolerado.  • % de activos Tier-0 con cobertura XDR activa y MFA FIDO2.  • Tiempo medio de contención (MTTC) de intrusiones. |
| **Escenario 2: Compromiso de Identidad y Fraude Corporativo**  • *Amenaza:* Ingeniería social avanzada / Adversary-in-the-Middle (AitM).  • *Impacto:* Toma de control de cuentas ejecutivas, desvío de fondos (BEC) y acceso no autorizado a correo/colaboración. | • **Initial Access:** Spearphishing Link (`T1566.002`).  • **Credential Access:** Steal Web Session Cookie (`T1539`), MFA Interception (`T1111`).  • **Persistence:** Account Manipulation (`T1098`).  • **Collection:** Email Collection (`T1114`). | • Políticas de Acceso Condicional basadas en riesgo de sesión y dispositivo gestionado.  • Protección contra robo de tokens (Token Binding / CAE).  • Reglas de bloqueo de reenvío automático de correo externo.  • Monitoreo de anomalías de identidad (ITDR). | • **Data Disclosure (D):** Acceso a comunicaciones confidenciales con datos personales de empleados o clientes.  • **Linking (L):** Correlación de información extraída de múltiples hilos de correo y repositorios. | • Políticas de retención y purga automática en buzones y plataformas de colaboración.  • Minimización de datos personales compartidos en canales no estructurados.  • Flujos de aprobación fuera de banda para transferencias o cambios de datos bancarios. | • % de identidades privilegiadas protegidas con Acceso Condicional estricto.  • Cantidad de sesiones anómalas bloqueadas automáticamente.  • Tasa de reporte de phishing por empleados. |
| **Escenario 3: Exfiltración Masiva vía Aplicaciones y APIs**  • *Amenaza:* Explotación de vulnerabilidades web o fallos de autorización en APIs.  • *Impacto:* Robo de bases de datos de clientes, multas regulatorias y pérdida de confianza del mercado. | • **Initial Access:** Exploit Public-Facing Application (`T1190`).  • **Discovery:** Network Service Discovery (`T1046`).  • **Collection:** Data from Information Repositories (`T1213`).  • **Exfiltration:** Automated Exfiltration (`T1020`). | • Web Application Firewall (WAF) y API Gateway con inspección de esquemas y rate limiting.  • Pruebas SAST/DAST integradas en pipelines CI/CD.  • Gestión continua de superficie de ataque (EASM) y remediación prioritaria de CVEs críticos. | • **Identifying (I):** Re-identificación de clientes mediante cruce de registros extraídos.  • **Data Disclosure (D):** Filtración masiva de PII (identificadores, datos financieros o de salud).  • **Detecting (D):** Inferencia de pertenencia de usuarios a servicios sensibles. | • Seudonimización y tokenización de identificadores directos en bases de datos transaccionales.  • Evaluación de Impacto en la Privacidad (DPIA) obligatoria antes del despliegue de nuevas APIs externas.  • Principio de minimización en respuestas de API (evitar *over-fetching*). | • Tiempo medio de remediación (MTTR) de vulnerabilidades críticas en activos expuestos.  • % de APIs inventariadas bajo gobierno de API Gateway.  • % de proyectos nuevos con DPIA completada pre-producción. |
| **Escenario 4: Brecha en Cadena de Suministro y Terceros**  • *Amenaza:* Compromiso de proveedor tecnológico (SaaS/BPO) o dependencia de software.  • *Impacto:* Acceso indirecto a la red interna o filtración de datos procesados por terceros. | • **Initial Access:** Supply Chain Compromise (`T1195`), Trusted Relationship (`T1199`).  • **Persistence:** Valid Accounts (`T1078`).  • **Command and Control:** Web Service (`T1102`). | • Arquitectura Zero Trust para terceros (acceso granulado a nivel aplicación, sin VPN de red plana).  • Revisión de integridad de software (SBOM) y firma de código.  • Monitoreo continuo de actividad y volumen de descarga de cuentas de proveedores. | • **Unawareness (U):** Transferencia o subcontratación de procesamiento de datos a cuartos partidos sin conocimiento del titular.  • **Non-compliance (N):** Incumplimiento de cláusulas de transferencia internacional o retención post-contrato. | • Acuerdos de Procesamiento de Datos (DPA) vinculantes con cláusulas de auditoría y notificación.  • Registro actualizado de encargados y subencargados del tratamiento (RoPA).  • Verificación certificada de destrucción de datos al finalizar el contrato. | • % de proveedores críticos con evaluación de riesgo de seguridad y privacidad vigente.  • % de accesos de terceros bajo modelo Zero Trust (sin acceso de red lateral). |
| **Escenario 5: Fuga Interna y Abuso de Privilegios**  • *Amenaza:* Insider malicioso o negligencia operacional.  • *Impacto:* Robo de propiedad intelectual o exposición accidental de repositorios en la nube. | • **Collection:** Data from Local System (`T1005`), Data from Cloud Storage Object (`T1530`).  • **Defense Evasion:** Impair Defenses (`T1562`).  • **Exfiltration:** Exfiltration to Cloud Storage (`T1567.002`), Physical Medium (`T1052`). | • Gestión de Privilegios Just-In-Time (PIM/PAM) con aprobación y grabación de sesiones.  • Políticas de prevención de fuga de datos (DLP) en endpoint, red y nube.  • Gestión de postura de seguridad en la nube (CSPM) para bloquear buckets públicos. | • **Data Disclosure (D):** Acceso interno no autorizado a registros sensibles de clientes o empleados (curiosidad o venta).  • **Non-repudiation (N):** Falta de trazabilidad individualizada en cuentas compartidas. | • Control de acceso basado en atributos/roles (ABAC/RBAC) bajo estricto *Need-to-Know*.  • Prohibición de cuentas genéricas compartidas; auditoría inmutable de acceso a registros sensibles.  • Enmascaramiento dinámico de datos en entornos de soporte y desarrollo. | • % de cuentas administrativas operando bajo modelo Just-In-Time (cero privilegios permanentes).  • Tiempo de revocación de accesos tras desvinculación de personal.  • Incidentes DLP críticos resueltos. |
| **Escenario 6: Manipulación y Fuga en Ecosistemas de IA Generativa**  • *Amenaza:* Prompt Injection, Data Poisoning o Excessive Agency (OWASP LLM / MITRE ATLAS).  • *Impacto:* Ejecución de acciones no autorizadas por agentes autónomos o exposición de datos confidenciales en respuestas. | • **Initial Access / Execution:** LLM Prompt Injection (`AML.T0051`).  • **Privilege Escalation:** Excessive Agency / Tool Misuse.  • **Exfiltration:** LLM Data Leakage (`AML.T0024`).  • **Impact:** Data Poisoning (`AML.T0020`). | • Gateways de seguridad para IA (filtrado de prompts/respuestas y detección de inyecciones).  • Aislamiento de permisos de agentes IA (identidad propia con mínimo privilegio, nunca heredando permisos totales del usuario).  • Sanitización y validación de fuentes de datos RAG. | • **Detecting (D):** Ataques de inferencia de membresía (deducir si los datos de una persona fueron usados para entrenar/ajustar el modelo).  • **Unawareness (U):** Uso de datos personales para entrenamiento sin base legal ni transparencia.  • **Linking (L):** Inferencia de perfiles sensibles no declarados. | • Gobernanza de IA (ISO/IEC 42001): inventario de modelos y casos de uso aprobados.  • Prohibición de entrenamiento de modelos públicos con datos corporativos/personales.  • Evaluación de impacto algorítmico y mecanismos de explicabilidad y rectificación para titulares. | • % de modelos y agentes de IA en producción registrados y auditados.  • Cantidad de intentos de fuga de datos sensibles bloqueados por controles DLP/AI Gateway. |

### Mecanismo de Operación y Gobernanza (Cómo hacer viva la matriz)

Para que esta matriz no sea un documento estático de cumplimiento, debe integrarse en **tres cadencias operativas**:

1. **Ciclo de Diseño de Proyectos (Shift-Left):**
   - Cuando el negocio propone una nueva iniciativa (ej. lanzar una app móvil o integrar un agente de IA), se identifican primero los escenarios aplicables en la **Columna 1**.
   - Arquitectura y Seguridad derivan los requisitos obligatorios de la **Columna 3** (validados contra las técnicas de la **Columna 2**), mientras Privacidad ejecuta los controles de la **Columna 5** (evaluando las amenazas de la **Columna 4**).
2. **Ciclo de Validación Continua (Purple Teaming y Auditoría):**
   - Los ejercicios de simulación de adversarios (Red Team / BAS) utilizan las técnicas específicas de la **Columna 2** (MITRE ATT&CK / ATLAS) para poner a prueba los controles de la **Columna 3**.
   - Si un control técnico falla en bloquear o detectar una técnica (ej. *Steal Web Session Cookie*), el riesgo residual de la **Columna 1** sube automáticamente en el tablero ejecutivo.
3. **Ciclo de Reporte al Directorio (Comité de Riesgos):**
   - El Directorio no recibe métricas técnicas aisladas (como "cantidad de ataques bloqueados por el firewall"), sino la **Columna 1** (exposición financiera y operativa) respaldada por los indicadores de efectividad de control de la **Columna 6**, demostrando cobertura simultánea sobre continuidad operativa (ciberseguridad) y cumplimiento legal (privacidad).









Cómo se modelan las amenazas? Que métodos y marcos de referencia hay?







El **modelado de amenazas (\*Threat Modeling\*)** es una disciplina de ingeniería y gestión de riesgos que permite identificar, enumerar, priorizar y mitigar de manera estructurada los posibles vectores de ataque y fallos de diseño antes de que sean explotados.   

En la práctica profesional, el proceso se estructura en **cuatro preguntas fundamentales** (definidas por el *Threat Modeling Manifesto* de Adam Shostack y referentes de la industria) y se ejecuta mediante distintos **marcos de referencia** según la capa organizacional o técnica que se desee analizar.   

### 1. El Proceso Estándar de Modelado (4 Pasos)

Independientemente de la metodología elegida, todo ejercicio riguroso de modelado sigue esta secuencia lógica:

1. **¿En qué estamos trabajando? (Descomposición del sistema):**

   Se define el alcance, se identifican los activos críticos y se dibujan **Diagramas de Flujo de Datos (DFD)**. El elemento más crítico de este paso es marcar las **fronteras de confianza (\*Trust Boundaries\*)**: todo punto donde los datos o el control cruzan de una zona de menor confianza a una de mayor confianza (ej. de Internet hacia una API, o de un usuario estándar hacia un rol administrativo).   

2. **¿Qué puede salir mal? (Identificación de amenazas):**

   Se recorre cada nodo, flujo de datos y frontera de confianza aplicando un marco taxonómico (como STRIDE, PASTA o LINDDUN) o árboles de ataque para enumerar sistemáticamente cómo un adversario podría comprometer el sistema.   

3. **¿Qué vamos a hacer al respecto? (Priorización y respuesta):**

   Se estima la criticidad de cada amenaza y se define una de las cuatro estrategias formales de tratamiento: **Mitigar** (implementar controles técnicos o de proceso), **Eliminar** (remover la funcionalidad riesgosa), **Transferir** (seguros o acuerdos contractuales con terceros) o **Aceptar** (asumir el riesgo residual bajo aprobación formal de un dueño de negocio).   

4. **¿Hicimos un buen trabajo? (Validación y verificación):**

   Se verifica que los controles diseñados existan en la implementación real mediante revisiones de arquitectura, pruebas de penetración, *Purple Teaming* o simulaciones automatizadas.   

### 2. Métodos y Marcos de Referencia Principales

No existe un marco único para todos los propósitos; se seleccionan según el enfoque (**centrado en el sistema/software**, **centrado en el atacante**, **centrado en el riesgo de negocio** o **centrado en privacidad/IA**):   

| **Método / Marco**                                           | **Enfoque Principal**                                    | **Mecanismo de Operación**                                   | **Caso de Uso Ideal**                                        |
| ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **STRIDE** *(Microsoft)*                                     | Centrado en el software y arquitectura técnica.          | Evalúa cada elemento del DFD contra 6 categorías: **S**poofing (suplantación), **T**ampering (manipulación), **R**epudiation (repudio), **I**nformation Disclosure (divulgación), **D**enial of Service (denegación) y **E**levation of Privilege (elevación de privilegios). | Diseño de aplicaciones, microservicios, APIs y arquitecturas Cloud en ciclos DevSecOps. |
| **PASTA** *(Process for Attack Simulation and Threat Analysis)* | Centrado en el riesgo de negocio y simulación de ataque. | Metodología de **7 etapas** que comienza definiendo objetivos de negocio y cumplimiento, descompone la arquitectura, analiza inteligencia de amenazas reales, modela ataques y cuantifica el impacto financiero. | Entornos corporativos regulados donde se requiere alinear seguridad técnica con impacto financiero. |
| **Árboles de Ataque (\*Attack Trees\*)**                     | Centrado en el atacante (orientado a objetivos).         | Diagramas jerárquicos donde el nodo raíz es el objetivo final del atacante (ej. "Exfiltrar base de datos de clientes") y las ramas desglosan las condiciones lógicas (`AND` / `OR`) necesarias para lograrlo. | Análisis profundo de escenarios críticos de alto impacto, sistemas ciberfísicos (OT) o seguridad financiera. |
| **OCTAVE** *(Carnegie Mellon SEI)*                           | Centrado en activos y operaciones organizacionales.      | Evaluación cualitativa basada en talleres con áreas operativas y directivas para identificar activos críticos, prácticas actuales y riesgos operativos sin depender exclusivamente de auditorías técnicas. | Evaluación de riesgos a nivel organizacional y de procesos de negocio. |
| **VAST** *(Visual, Agile, and Simple Threat)*                | Centrado en escalabilidad Agile / DevOps.                | Separa el modelado en dos vistas automatizables: modelos de procesos de aplicación (para equipos de desarrollo) y modelos de procesos operacionales (para infraestructura/operaciones). | Organizaciones grandes con cientos de equipos de desarrollo ágil que requieren automatización. |
| **TRIKE**                                                    | Centrado en auditoría y gestión de riesgos defensiva.    | Utiliza una matriz CRUD (*Create, Read, Update, Delete*) sobre cada activo y actor para asignar niveles de riesgo aceptable aprobados por los interesados. | Auditorías de seguridad y verificación de cumplimiento de políticas de acceso. |
| **LINDDUN**                                                  | Centrado en ingeniería de privacidad.                    | Análogo a STRIDE pero aplicado a datos personales: evalúa **L**inking, **I**dentifying, **N**on-repudiation, **D**etecting, **D**ata Disclosure, **U**nawareness y **N**on-compliance. | Evaluaciones de Impacto en la Privacidad (DPIA) y cumplimiento normativo (GDPR / LGPD). |
| **MAESTRO / MITRE ATLAS**                                    | Centrado en Inteligencia Artificial y Agentes Autónomos. | **MAESTRO** modela amenazas específicas en sistemas multi-agente (*tool misuse*, envenenamiento de memoria, autonomía excesiva), complementándose con la matriz de tácticas **MITRE ATLAS** para aprendizaje automático. | Despliegue de modelos LLM, arquitecturas RAG y agentes autónomos empresariales. |

### 3. Marcos de Priorización y Cuantificación (El puente hacia el riesgo)

Una vez identificadas las amenazas mediante alguno de los métodos anteriores, las organizaciones utilizan marcos complementarios para estimar su severidad y decidir dónde invertir:   

- **Enfoque Técnico / Cualitativo:**
  - **DREAD** *(Damage, Reproducibility, Exploitability, Affected Users, Discoverability)*: Puntúa cada amenaza del 1 al 10 en cinco dimensiones (aunque ha perdido tracción frente a modelos basados en evidencia por su subjetividad).   
  - **CVSS + EPSS:** Combina la severidad técnica intrínseca de una debilidad (CVSS) con la probabilidad real de explotación observada en internet en los próximos 30 días (EPSS).   
- **Enfoque Ejecutivo / Cuantitativo:**
  - **FAIR (\*Factor Analysis of Information Risk\*):** Traduce las amenazas modeladas en distribuciones probabilísticas de pérdida financiera anualizada (ALE), permitiendo comparar el costo de implementar un control frente a la reducción real de exposición económica.
  - **NIST SP 800-30 / ISO/IEC 27005:** Proveen el marco procedimental formal para integrar los resultados del modelado técnico dentro del registro corporativo de riesgos y el sistema de gestión de seguridad de la información (SGSI).

### Fuentes de referencia verificables

- **OWASP Threat Modeling Cheat Sheet:** https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- **Threat Modeling Manifesto:** https://www.threatmodelingmanifesto.org/
- **NIST SP 800-30 Rev. 1 (Guide for Conducting Risk Assessments):** https://csrc.nist.gov/pubs/sp/800/30/r1/final
- **MITRE ATLAS (Adversarial Threat Landscape for AI Systems):** [https://atlas.mitre.org/](https://www.google.com/search?q=https%3A%2F%2Fatlas.mitre.org%2F)
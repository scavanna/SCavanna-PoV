# Guía Maestra de Excelencia Operacional: Microsoft Sentinel (SIEM / SOAR Cloud-Native Asociado a M365 E5)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `08_Microsoft_Sentinel` |
| **Slug Canónico** | `Microsoft_Sentinel` |
| **Nombre Completo** | Microsoft Sentinel (SIEM / SOAR Cloud-Native Asociado a M365 E5) |
| **Categoría Maestra** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (Modelo de Operación SecOps + 12 Bloques + SOPs + Auditoría NIST CSF 2.0 + Licenciamiento/FinOps) + Revalidado Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Asociado a M365 E5** — Facturado por consumo/compromiso en Azure (no incluido como licencia por usuario en E5), con **Microsoft 365 E5/E7 Data Grant de hasta 5 MB/usuario/día**, fuentes M365 siempre gratuitas y operación unificada con Defender XDR `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://security.microsoft.com` (Unified SecOps Platform — portal primario y único tras el **31 de marzo de 2027**), `https://portal.azure.com` (administración de recursos Azure, IAM/RBAC, Cost Management y Logic Apps; experiencia Sentinel en Azure soportada solo hasta el `2027-03-31`) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, SOC L1, SOC L2, SOC L3 / Detection Engineer, Threat Hunter, Sentinel Platform Engineer, SOAR / Automation Engineer, FinOps / Cloud Architect, GRC & Internal/External Auditors |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Microsoft Zero Trust (Visibility, Automation & Orchestration / TIC 3.0), MITRE ATT&CK Enterprise v18, Open Source Security Events Metadata (OSSEM / ASIM), Microsoft Security Adoption Framework (SAF) |

> **Nota de consolidación documental:** Esta guía unifica orgánicamente las tres vertientes del repositorio maestro (el **Modelo de Operación SecOps** con sus 12 bloques tácticos y SOPs de consola, el marco formal de **Auditoría NIST CSF 2.0** con consultas KQL reproducibles, y el modelo **FinOps / Beneficio Microsoft 365 E5**), corrigiendo la separación detectada en archivos fuente previos. Se aplica estrictamente `[Verificado MS Learn]` para hechos técnicos documentados por Microsoft a noviembre de 2026 y `[Decisión / Propuesta Editorial]` para SLAs, metas cuantitativas de KPIs, matrices RACI y modelos consultivos de madurez.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución del SIEM Clásico a la Plataforma Unificada SecOps & AI-Ready

**Microsoft Sentinel** ha evolucionado desde un SIEM y SOAR nativo de nube hacia una **plataforma integral de datos y operaciones de seguridad** profundamente unificada dentro del **portal de Microsoft Defender (`https://security.microsoft.com`)** `[Verificado MS Learn]`. A noviembre de 2026, Sentinel articula cinco capas tecnológicas convergentes `[Verificado MS Learn]`:

1. **SIEM Cloud-Native Multicloud y Multiplataforma:** Más de **350 conectores out-of-the-box** en el **Content Hub**, recolección moderna mediante **Azure Monitor Agent (AMA)** con **Data Collection Rules (DCR)**, **Logs Ingestion API** y **Codeless Connector Framework (CCF)**, normalización **ASIM** y correlación multi-dominio automática junto con Microsoft Defender XDR `[Verificado MS Learn]`.
2. **Microsoft Sentinel Data Lake Integrado:** Lago de datos de seguridad nativo y totalmente administrado (integrado por defecto en el flujo de onboarding desde el **23 de septiembre de 2026**), con espejo automático desde el nivel Analytics sin doble cargo de ingesta, compresión 6:1, retención económica de hasta **12 años**, consultas KQL interactivas en Advanced Hunting, *KQL jobs*, notebooks Apache Spark y espejo/federación sin copia hacia **Microsoft Fabric OneLake** `[Verificado MS Learn]`.
3. **SOAR Declarativo y Asistido por IA:** Orquestación centralizada mediante **Automation Rules**, gestión de casos (**Case Management**), *Simple Flows* (Preview) y **Playbooks en Azure Logic Apps (Consumption y Standard)** autenticados con **Managed Identity**, complementados por el **generador de playbooks con IA (GA desde mayo de 2026)** y la interrupción automática de ataques (*Automatic Attack Disruption*) de Defender XDR `[Verificado MS Learn]`.
4. **SOC Optimization y Cobertura MITRE ATT&CK v18:** Motor continuo en producción (con acceso UI y API) que recomienda controles frente a brechas de cobertura de amenazas y optimiza el valor financiero por tabla (*Data value optimization*, incluyendo detección de tablas sin uso analítico en 30 días y columnas no utilizadas en preview) `[Verificado MS Learn]`.
5. **Sentinel Graph y Servidor MCP (SOC Agéntico):** Grafo de relaciones de ataque (*Blast radius* e investigación visual sin costo adicional embebida en Defender/Purview, más grafos personalizados en GQL) e interfaz **Model Context Protocol (MCP)** para que **Microsoft Security Copilot** y agentes autónomos consulten telemetría, analicen entidades y ejecuten triaje gobernado `[Verificado MS Learn]`.

### 2.2 Modelo Financiero y Asociación Exacta con Microsoft 365 E5 (FinOps SecOps)

> **Distinción arquitectónica y contractual crítica `[Verificado MS Learn]`:** Microsoft Sentinel **no está incluido como licencia por usuario** dentro de Microsoft 365 E5; requiere una suscripción de Azure donde se factura según el nivel de almacenamiento y volumen de datos ingeridos/procesados (**GB/día**). No obstante, mantiene una **sinergia financiera y técnica directa con Microsoft 365 E5** que reduce sustancialmente el costo total de propiedad (TCO) del SOC:

| Mecanismo / Beneficio Oficial | Alcance Técnico y Financiero Verificado (Noviembre 2026) | Condición de Elegibilidad | Etiqueta |
|---|---|---|---|
| **Microsoft 365 E5 / E7 / A5 / F5 / G5 Data Grant** | Otorga automáticamente hasta **5 MB por usuario licenciado por día** de ingesta gratuita en Microsoft Sentinel (ej. 3.500 usuarios E5 = ~17,5 GB/día; 10.000 usuarios E5 = ~50 GB/día / ~1,5 TB/mes). Cubre: (1) logs de inicio de sesión y auditoría de **Microsoft Entra ID**, (2) logs de descubrimiento Shadow IT de **Defender for Cloud Apps**, (3) logs de **Microsoft Purview Information Protection**, y (4) tablas de **Advanced Hunting de Microsoft Defender XDR** (`Device*`, `Email*`, `Identity*`, `CloudAppEvents`, `AlertEvidence`). Se refleja en la factura Azure bajo medidores `Free Benefit - M365 Defender`. | Clientes EA, EAS o CSP con licencias M365 E7/E5/A5/F5/G5 o E7/E5/A5/F5/G5 Security (*Microsoft Defender Suite*). | `[Verificado MS Learn]` |
| **Fuentes Siempre Gratuitas (Free Data Sources)** | Ingesta a **$0** para todos los clientes de Sentinel: `AzureActivity` (Azure Activity Logs), `SentinelHealth`, `OfficeActivity` (auditoría de SharePoint, Exchange y Teams), e incidentes/alertas de seguridad (`SecurityIncident`, `SecurityAlert`) provenientes de Defender XDR, MDE, MDI, MDO, MDA, Defender for Cloud, Defender for IoT y Entra ID Protection. | Todo workspace activo de Microsoft Sentinel (90 días de retención interactiva incluidos; la retención extendida >90 días sí genera cargo). | `[Verificado MS Learn]` |
| **Consulta Gratuita por 30 Días de Tablas XDR en Portal Unificado** | Al conectar el workspace primario de Sentinel al **portal de Microsoft Defender**, los analistas consultan en `Advanced hunting` los logs crudos de Defender XDR durante **30 días sin necesidad de ingerirlos ni pagarlos** en el nivel Analytics de Sentinel (solo se ingiere lo que requiera retención >30 días o correlación específica). | Workspace de Sentinel incorporado a `https://security.microsoft.com` junto con Defender XDR. | `[Verificado MS Learn]` |
| **UEBA Extendido sobre Datos XDR con M365 E5 (Preview)** | Permite conectar tablas elegibles de Defender XDR (`EntraIdSignInEvents`, `EntraIdSpnSignInEvents`, `EntraIdDirectoryAuditEvents`, `DeviceLogonEvents`) a **Sentinel UEBA** desde el workspace primario sin re-ingerir esos datos first-party en Sentinel (aplican cargos de Log Analytics únicamente por los resultados generados en `BehaviorAnalytics` / `Anomalies`). | Tenant M365 E5 con workspace primario conectado al portal Defender y sincronización de directorio activa. | `[Verificado MS Learn]` |
| **Beneficio Microsoft Defender for Servers Plan 2** | Otorga **500 MB por nodo/día** (consolidados a nivel workspace) para tablas de seguridad de servidores elegibles (`SecurityEvent`, `WindowsEvent`, `SecurityBaseline`, `WindowsFirewall`, `MDCFileIntegrityMonitoringEvents`, etc.). | Defender for Servers Plan 2 activo sobre el mismo workspace de Log Analytics. | `[Verificado MS Learn]` |
| **Prueba Gratuita Inicial (Free Trial)** | Primeros **10 GB/día** gratuitos durante **31 días** (tanto ingesta Log Analytics como análisis Sentinel en nivel Analytics; sujeto a límite de 20 workspaces por tenant; cargos de automatización, Data Lake o BYOML se facturan por separado). | Nuevos workspaces habilitados en Microsoft Sentinel. | `[Verificado MS Learn]` |
| **Modelos de Pago: PAYG vs. Simplified Commitment Tiers** | En el **Analytics tier**, el pago puede ser **Pay-As-You-Go** o **Commitment Tiers simplificados** (unificando medidores de Log Analytics y Sentinel desde **100 GB/día** hacia arriba con descuentos progresivos; permite subir de tier en cualquier momento y bajar cada 31 días). El **Data Lake tier** factura por separado ingesta directa a lago, procesamiento, almacenamiento comprimido (6:1) y datos escaneados por query KQL o cómputo Spark. | Configuración en `Settings > Microsoft Sentinel > Pricing` / Azure Cost Management. | `[Verificado MS Learn]` |

### 2.3 Principios Operativos Oficiales y Alineación Zero Trust

Microsoft fundamenta la operación de Sentinel sobre cinco principios rectores documentados (`incidents-first`, `automation-assisted SOC`, `metrics-driven operations`, `threat-informed defense` con MITRE ATT&CK v18 y `continuous optimization`) articulados con **Zero Trust** `[Verificado MS Learn]`:

- **Verificar explícitamente:** Correlación multi-fuente (identidad + endpoint + SaaS + red + multicloud AWS/GCP + SAP) enriquecida con **Threat Intelligence** (MDTI y STIX/TAXII) y líneas base **UEBA**.
- **Usar privilegio mínimo:** Segregación estricta mediante **Azure RBAC** a nivel Resource Group, **Microsoft Defender Unified RBAC (URBAC)** / Entra ID para el Data Lake, scoping a nivel de fila (Preview), auditoría de consultas (`LAQueryLogs`) y **Managed Identities** en playbooks.
- **Asumir brecha:** Caza proactiva guiada por hipótesis (*Hunts* y *Bookmarks*), reglas casi en tiempo real (**NRT** y **Custom Detection Rules**), grafo de *blast radius* y contención automatizada en segundos mediante SOAR y *Automatic Attack Disruption*.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Transición Obligatoria al Portal de Microsoft Defender (`2027-03-31`)

> **Hito mandatorio de plataforma `[Verificado MS Learn]`:** Microsoft Sentinel se encuentra en disponibilidad general (GA) en `https://security.microsoft.com` (incluso para clientes sin licencias Defender XDR o E5). **Después del 31 de marzo de 2027, Microsoft Sentinel dejará de tener soporte en Azure Portal (`portal.azure.com`) y estará disponible exclusivamente en el portal de Microsoft Defender**, redirigiendo automáticamente a todos los usuarios. Toda nueva innovación (Data Lake integrado, Security Copilot y agentes, Case Management, AI Playbook Generator, Blast Radius Graph y SOC Optimization guiado) aterriza primero o exclusivamente en el portal de Defender.

#### Mapa de Equivalencia de Navegación para Equipos SecOps `[Verificado MS Learn]`

| Función Histórica (Azure Portal) | Ruta Operativa Vigente en Microsoft Defender Portal (`security.microsoft.com`) |
|---|---|
| `General > Logs` | `Investigation & response > Hunting > Advanced hunting` |
| `Threat management > Incidents` | `Investigation & response > Incidents & alerts > Incidents` (Cola unificada SIEM + XDR y *Case management*) |
| `Threat management > Workbooks / Hunting / Notebooks / MITRE ATT&CK` | `Microsoft Sentinel > Threat management > Workbooks / Hunting / Notebooks / MITRE ATT&CK` |
| `Threat management > Entity behavior` | `Assets > Identities` o `Assets > Devices` > pestaña `Sentinel events` (y páginas unificadas de entidad) |
| `Threat management > Threat intelligence` | `Threat intelligence > Intel management` |
| `Content management > Content hub / Repositories` | `Microsoft Sentinel > Content management > Content hub` / `Repositories` |
| `Configuration > Analytics` | `Microsoft Sentinel > Configuration > Analytics` **y** `Investigation & response > Hunting > Custom detection rules` |
| `Configuration > Data connectors / Watchlists / Automation` | `Microsoft Sentinel > Configuration > Data connectors` / `Watchlists` / `Automation` |
| `Configuration > Settings` y Gestión de Tablas/Lago | `System > Settings > Microsoft Sentinel` y `Microsoft Sentinel > Configuration / Data management > Tables` |

### 3.2 Estrategia de Niveles de Datos: Analytics Tier vs. Data Lake Tier

Desde el **23 de septiembre de 2026**, el **Microsoft Sentinel Data Lake** viene integrado en el onboarding estándar sin configuración de facturación separada `[Verificado MS Learn]`:

| Categoría de Dato Oficial | Nivel Recomendado | Características Técnicas y Operativas (Noviembre 2026) | Ejemplos de Fuentes | Etiqueta |
|---|---|---|---|---|
| **Primary Security Data** *(Alto valor inmediato de detección)* | **Analytics Tier** *(con espejo automático al Data Lake)* | **90 días** de retención interactiva gratuita por defecto (extensible hasta 2 años); consultas KQL ilimitadas de alta velocidad sin costo por escaneo; soporta reglas **Scheduled**, **NRT**, **Custom Detection Rules**, **UEBA** y alertas en tiempo real. Los datos ingeridos aquí se espejan automáticamente al Data Lake sin cargo duplicado de ingesta ni procesamiento. | Alertas EDR/XDR, `SigninLogs`, `AuditLogs`, `SecurityEvent` filtrado, feeds TI, `OfficeActivity`, logs críticos de identidad y plano de control cloud. | `[Verificado MS Learn]` |
| **Secondary Security Data** *(Alto volumen, contexto forense e histórico)* | **Data Lake Tier** *(reemplaza gestión heredada Archive / Auxiliary)* | Ingesta y almacenamiento económico de escala petabyte con **compresión uniforme 6:1** y retención total de hasta **12 años**; consultable directamente con KQL interactivo desde `Advanced hunting` (sin restaurar primero), **KQL jobs** programados que promueven resúmenes al nivel Analytics, notebooks Spark (pools de 12, 32 y 80 vCores) y espejo sin copia a **Microsoft Fabric OneLake**. *(Nota: en workspaces no incorporados o planes clásicos aún existen medidores `Basic Logs` y `Auxiliary Logs`).* | Logs verbosos de Firewall/Proxy, NetFlow, DNS de alto volumen, logs de acceso a almacenamiento cloud (S3/Blob), TLS/SSL e IoT. | `[Verificado MS Learn]` |

### 3.3 Componentes Críticos de Ingesta, Normalización y SOAR

- **Recolección moderna y retiro de HTTP Data Collector API (`2026-09-14`) `[Verificado MS Learn]`:** La antigua *HTTP Data Collector API* quedó fuera de soporte después del **14 de septiembre de 2026**. Toda integración personalizada o de terceros debe operar sobre **Azure Monitor Logs Ingestion API** (con **Data Collection Rules - DCR** que permiten transformaciones pre-ingesta `filter` y `split` para enrutar entre Analytics y Data Lake) o el **Codeless Connector Framework (CCF)** (acelerado con el agente constructor en VS Code). Para servidores Windows/Linux y colectores **Syslog/CEF**, el estándar único es **Azure Monitor Agent (AMA)**.
- **Normalización con ASIM (Advanced Security Information Model) `[Verificado MS Learn]`:** Capa alineada con **OSSEM** que proporciona parsers en tiempo de consulta (*query-time*) y normalización en tiempo de ingesta (*ingest-time*, ej. `ASimDnsActivityLogs`, `ASimNetworkSessionLogs`, `ASimAuthenticationEventLogs`, `ASimWebSessionLogs`, `ASimUserManagementActivityLogs`) para escribir detecciones agnósticas del fabricante.
- **Arquitectura SOAR Vigente `[Verificado MS Learn]`:** El vínculo directo de playbooks dentro de reglas analíticas quedó obsoleto en marzo de 2026. El patrón obligatorio es: **Evento (Incidente creado/actualizado, Alerta creada o `Enhanced Alert Trigger` en Defender) -> Automation Rule (orden secuencial controlado, asignación, tags, *Incident tasks*, supresión con expiración o *Simple Flows*) -> Playbook en Azure Logic Apps (Consumption o Standard) autenticado mediante System-Assigned Managed Identity**. Desde julio de 2026, el mapeo de `AccountName` entrega siempre únicamente el prefijo del UPN (`usuario`), separando `UPNSuffix` y `UserPrincipalName`.

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Modelo Dual de Permisos: Azure RBAC (SIEM) + Entra ID / Unified RBAC (Data Lake y Portal Defender)

Microsoft Sentinel combina **Azure RBAC** (recomendado oficialmente asignar a nivel del **Resource Group** que aloja el workspace y los playbooks) con **Microsoft Entra ID RBAC / Microsoft Defender Unified RBAC (URBAC)** para gobernar el acceso transversal en el portal de Defender y el **Sentinel Data Lake** (incluyendo control de acceso a nivel de fila/*scoping* en preview y tabla/recurso) `[Verificado MS Learn]`.

| Rol Técnico Oficial | Plano RBAC / Alcance | Permisos Clave | Estrategia PIM / JIT Recomendada | Responsabilidad en el SOC | Etiqueta |
|---|---|---|---|---|---|
| **Microsoft Sentinel Reader** (+ `Security Reader` en Entra/URBAC) | Azure RBAC (Resource Group) + Entra ID | Ver datos, incidentes, workbooks, recomendaciones y ejecutar consultas interactivas en el workspace y Data Lake; sin permisos de edición. | Permanente sobre grupo de monitoreo L1 o auditores internos/externos con MFA FIDO2 `[Decisión / Propuesta Editorial]`. | Monitoreo de tableros, auditoría GRC y consultas de lectura sin riesgo operativo. | `[Verificado MS Learn]` |
| **Microsoft Sentinel Responder** + **Microsoft Sentinel Playbook Operator** | Azure RBAC (Resource Group de Sentinel y RG de Playbooks) | Todos los permisos de Reader más gestionar incidentes (asignar, cambiar severidad/estado, agregar comentarios/bookmarks) y listar/ejecutar manualmente playbooks. *(Nota: usuarios invitados B2B requieren además `Directory Reader` en Entra ID para asignar incidentes).* | Permanente para analistas en turno o elegible en PIM (8 h) `[Decisión / Propuesta Editorial]`. | Operación diaria de SOC L1 y SOC L2: triaje, investigación, gestión de casos y disparo manual controlado de playbooks. | `[Verificado MS Learn]` |
| **Microsoft Sentinel Contributor** (+ `Security Operator` / `Security Admin` para jobs del Data Lake) | Azure RBAC (Resource Group) + Entra ID / URBAC | Crear y editar reglas analíticas, custom detections, automation rules, watchlists, instalar/actualizar soluciones del Content Hub y programar jobs en el Data Lake. *(Para crear/borrar workbooks añadir `Workbook Contributor`).* | **Elegible (JIT) vía Azure PIM / Entra PIM** (máximo 4 h), requerir ticket de cambio e integración CI/CD (*Sentinel Repositories*) `[Decisión / Propuesta Editorial]`. | Ingeniería de detección (SOC L3), administración del Content Hub, tuning KQL y gestión del ciclo de vida de contenido. | `[Verificado MS Learn]` |
| **Logic App Contributor** | Azure RBAC (Resource Group de Playbooks) | Crear, modificar y depurar flujos de Azure Logic Apps utilizados como playbooks SOAR. | **Elegible (JIT) en Azure PIM** (máx. 4 h) segregado de analistas L1/L2 `[Decisión / Propuesta Editorial]`. | Ingeniería SOAR: desarrollo, manejo de errores y configuración de conexiones con **Managed Identity**. | `[Verificado MS Learn]` |
| **Microsoft Sentinel Automation Contributor** | Azure RBAC (Resource Group de Playbooks — **no para usuarios humanos**) | Rol exclusivo asignado a la cuenta de servicio especial de Microsoft Sentinel (*Azure Security Insights*) mediante `Settings > Playbook permissions` (requiere `Owner` al configurarlo) para permitir que las Automation Rules ejecuten playbooks. | Asignación permanente **solo al Service Principal oficial de Sentinel** acotado exclusivamente al Resource Group de playbooks productivos `[Verificado MS Learn]`. | Habilitación segura de ejecución desatendida de playbooks desde Automation Rules (incluyendo escenarios multitenant Lighthouse). | `[Verificado MS Learn]` |
| **Identidad Administrada de Logic App (`System-Assigned Managed Identity`)** | Azure RBAC sobre Workspace Sentinel y APIs destino | Se le asigna `Microsoft Sentinel Responder` (si actualiza incidentes/watchlists) o `Microsoft Sentinel Reader` (si solo lee) en el workspace, más el permiso Graph/MDE mínimo necesario en el destino. | Sin secretos ni contraseñas; rotación automática administrada por plataforma Azure `[Verificado MS Learn]`. | Autenticación *zero-secret* de cada playbook hacia Microsoft Sentinel, Entra ID, MDE o firewalls. | `[Verificado MS Learn]` |
| **Log Analytics Contributor / Custom URBAC `data (manage)`** | Azure RBAC (Workspace) / Defender Custom URBAC | Configurar conectores de datos, modificar planes de tabla y retención (`Analytics` vs. `Data Lake`), DCRs y tablas personalizadas. | **Elegible (JIT) en PIM** (máx. 4 h) con aprobación de Arquitectura/FinOps `[Decisión / Propuesta Editorial]`. | Ingeniería de plataforma Sentinel, gobierno de costos, retención y onboarding de fuentes. | `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

> Consolida las **6 tareas diarias obligatorias** del **Microsoft Sentinel Operational Guide (`ops-guide`)** oficial con los protocolos de turno del Modelo Operativo SecOps sobre `https://security.microsoft.com` `[Verificado MS Learn]`.

### D-01 — Triaje, Asignación e Investigación Contextual de Incidentes en Cola Unificada
- **Objetivo:** Detectar, priorizar, investigar y contener oportunamente incidentes correlacionados entre Microsoft Sentinel y Microsoft Defender XDR manteniendo bajo el MTTA y MTTC.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 (triaje inicial) / SOC L2 (investigación profunda y contención).
- **Procedimiento paso a paso:**
  1. Filtrar incidentes `New` e `In progress` ordenando por severidad (`Critical / High > Medium > Low`), validando que cuentas privilegiadas o activos críticos (*crown jewels*) reciban elevación inmediata de prioridad aunque la severidad heurística sea Media/Baja `[Verificado MS Learn]`.
  2. Asignar propietario (`Assign to me` o cola L2), cambiar estado a `Active` / `In progress` y completar secuencialmente las **Incident tasks** inyectadas por Automation Rules `[Verificado MS Learn]`.
  3. Analizar el **Attack story**, el grafo interactivo de investigación y el análisis de **Blast radius**, expandiendo nodos (Usuario, Host, IP, Recurso Azure) y consultando **Watchlists** (activos VIP, rangos IP internos, empleados en preaviso) y contexto **UEBA** (`Assets > Identities / Devices > Sentinel events`) `[Verificado MS Learn]`.
  4. Aprovechar **Security Copilot** embebido en el incidente para resumen inicial, decodificación de scripts y generación asistida de consultas KQL cuando el tenant disponga de SCUs (incluidas en M365 E5) `[Verificado MS Learn]`.
  5. Al cerrar, registrar clasificación obligatoria (`True Positive`, `Benign Positive` o `False Positive`) con motivo y comentario estructurado para retroalimentar el tuning y las métricas del SOC `[Verificado MS Learn]`.
- **Evidencia auditable:** Registros en tabla `SecurityIncident` (propietario, tiempos de triaje/cierre, clasificación, etiquetas y comentarios) e historial de tareas completadas.

### D-02 — Caza Proactiva Diaria de Amenazas (*Threat Hunting*) y Gestión de Bookmarks
- **Objetivo:** Descubrir actividad adversaria evasiva (*living-off-the-land*, persistencia sutil, abuso de tokens) no cubierta aún por reglas analíticas programadas.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Threat management > Hunting` y `Investigation & response > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol responsable:** Threat Hunter / SOC L2.
- **Procedimiento paso a paso:**
  1. Ejecutar paquetes de consultas de caza integradas o campañas estructuradas (**Hunts**) filtradas por tácticas MITRE ATT&CK prioritarias (`Initial Access`, `Credential Access`, `Persistence`, `Defense Evasion`, `Lateral Movement`, `Exfiltration`) `[Verificado MS Learn]`.
  2. Ordenar por **Results Delta** para investigar incrementos anómalos respecto a la ejecución anterior y consultar datos tanto del nivel Analytics como del **Data Lake** directamente desde `Advanced hunting` `[Verificado MS Learn]`.
  3. Para todo evento sospechoso relevante, seleccionar la fila y crear un **Bookmark** mapeando obligatoriamente las entidades (`Account`, `Host`, `IP`, `URL`) y documentando notas analíticas (o vincular registros de `BehaviorInfo` a incidentes) `[Verificado MS Learn]`.
  4. Promover hallazgos confirmados mediante `Incident actions > Create new incident` o `Add to existing incident`, y proponer nueva regla de detección si el patrón es repetible `[Verificado MS Learn]`.
- **Evidencia auditable:** Bookmarks registrados (`HuntingBookmark`), campañas en `Hunts` e incidentes promovidos desde caza proactiva.

### D-03 — Supervisión de Salud, Ejecución y Habilitación de Reglas Analíticas y Custom Detections
- **Objetivo:** Impedir brechas de detección causadas por reglas deshabilitadas automáticamente (`AUTO DISABLED`), fallos de sintaxis/esquema o demoras de ejecución.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Analytics` e `Investigation & response > Hunting > Custom detection rules` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 (Detection Engineer) / Platform Engineer.
- **Procedimiento paso a paso:**
  1. Verificar en la lista de reglas que ninguna regla crítica figure con prefijo **AUTO DISABLED** y consultar la tabla `SentinelHealth` filtrando `SentinelResourceType == 'Analytics Rule'` y `Status != 'Success'` `[Verificado MS Learn]`.
  2. Corregir fallos por tiempos de espera agotados (*query timeout*), tablas faltantes o cambios en funciones ASIM, y verificar que las reglas **NRT** y **Custom detection rules** (ruta recomendada para nuevas detecciones unificadas) se ejecuten puntualmente `[Verificado MS Learn]`.
  3. Evaluar plantillas nuevas provenientes de soluciones recién instaladas o actualizadas y habilitarlas tras validar mapeo de entidades `[Verificado MS Learn]`.
- **Evidencia auditable:** Consulta diaria sobre `SentinelHealth` con 0 fallos críticos sin remediación y registro de reglas habilitadas/optimizadas.

### D-04 — Monitoreo de Salud de Data Connectors y Control de Volumen/Límites de Ingesta
- **Objetivo:** Garantizar flujo ininterrumpido de telemetría desde todas las fuentes conectadas y detectar anomalías de volumen (caídas silenciosas o picos de costo inesperados).
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Data connectors` y `Threat management > Workbooks > Data collection health monitoring` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer.
- **Procedimiento paso a paso:**
  1. Confirmar estado `Connected` en conectores críticos (Microsoft Defender XDR, Microsoft Entra ID, Microsoft 365, Azure Activity, firewalls CEF/Syslog, AWS/GCP, SAP) `[Verificado MS Learn]`.
  2. Consultar `SentinelHealth` (`OperationName == 'Data fetch status change'`) y el workbook **Data collection health monitoring** revisando `EPS = 0`, retrasos en `Last log received` o caídas >30 % respecto a la línea base `[Verificado MS Learn]`.
  3. Verificar el consumo diario en GB frente al **Commitment Tier** contratado y asegurarse de no aproximarse a un *Daily Cap* (usando DCRs con transformaciones `filter`/`split` en lugar de *Daily Cap* para no cegar al SOC) `[Verificado MS Learn]`.
- **Evidencia auditable:** Registros de `SentinelHealth`, métricas diarias de tabla `Usage` y alertas automáticas de caída de ingesta.

### D-05 — Verificación de Conectividad y Latidos de Azure Monitor Agent (AMA)
- **Objetivo:** Asegurar que servidores Windows/Linux, controladores y reenviadores Syslog/CEF mantengan comunicación activa hacia el workspace.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Hunting > Advanced hunting` (tabla `Heartbeat`) y `portal.azure.com > Monitor > Data Collection Rules` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / Cloud & Infra Ops.
- **Procedimiento paso a paso:**
  1. Ejecutar consulta KQL sobre la tabla `Heartbeat` filtrando `Category == 'Azure Monitor Agent'` para detectar equipos cuyo `max(TimeGenerated)` supere 1 hora sin mantenimiento programado `[Verificado MS Learn]`.
  2. Priorizar crítica e inmediatamente los **Log Forwarders** Linux de CEF/Syslog (cuya caída deja sin visibilidad múltiples firewalls/proxies simultáneamente).
  3. Diagnosticar estado del servicio (`MonAgentCore.exe` en Windows / `azuremonitoragent` en Linux), asociación DCR y conectividad TLS saliente hacia endpoints de Azure Monitor `[Verificado MS Learn]`.
- **Evidencia auditable:** Reporte diario de agentes silenciosos y tickets de remediación sobre colectores/servidores críticos.

### D-06 — Revisión de Fallos en Playbooks SOAR y Reglas de Automatización
- **Objetivo:** Detectar y corregir errores en flujos automatizados de enriquecimiento, notificación o contención para evitar fallos silenciosos durante incidentes reales.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Automation` y `portal.azure.com > Logic Apps > Runs history` `[Verificado MS Learn]`.
- **Rol responsable:** SOAR / Platform Engineer / SOC L3.
- **Procedimiento paso a paso:**
  1. Consultar la tabla `SentinelHealth` filtrando `SentinelResourceType in ('Automation rule', 'Playbook')` y `Status in ('Failure', 'PartiallySucceeded')` en las últimas 24 horas `[Verificado MS Learn]`.
  2. Abrir `Runs history` de cualquier Logic App fallida e inspeccionar entradas/salidas del paso con error: `401/403` (permisos faltantes en la Managed Identity), `429` (throttling de API), o errores de comparación sobre `AccountName` (verificar que use `Contains`/`Starts with` sobre el prefijo UPN y `UPNSuffix` tras el cambio de julio de 2026) `[Verificado MS Learn]`.
  3. Re-ejecutar manualmente los playbooks críticos fallidos sobre los incidentes abiertos del turno tras corregir la causa `[Verificado MS Learn]`.
- **Evidencia auditable:** Consulta diaria de `SentinelHealth` para automatización e historial `Succeeded` en Azure Logic Apps.

### D-07 — Revisión de Coincidencias de Threat Intelligence e Indicadores Activos
- **Objetivo:** Validar la recepción continua de indicadores STIX/TAXII y MDTI y priorizar cualquier coincidencia de IOC de alta confianza en el entorno.
- **Consola y ruta:** `https://security.microsoft.com > Threat intelligence > Intel management` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L2 / Threat Hunter.
- **Procedimiento paso a paso:**
  1. Confirmar sincronización reciente de conectores de inteligencia de amenazas (plataformas TAXII/STIX, ISAC sectoriales, MISP y feeds nativos de Microsoft) y vigencia de entradas en `ThreatIntelIndicators` / `ThreatIntelligenceIndicator` `[Verificado MS Learn]`.
  2. Revisar alertas generadas por reglas de *TI map* / coincidencia de indicadores contra tráfico de red, DNS, correo e inicios de sesión.
  3. Retroalimentar IOCs confirmados durante investigaciones del día hacia Watchlists o indicadores personalizados de bloqueo en MDE/firewalls `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Estadísticas de ingesta TI y alertas de coincidencia investigadas.

### D-08 — Control de SLA Operativo y Handover Estructurado entre Turnos SOC
- **Objetivo:** Garantizar transferencia limpia de contexto operativo 24x7 sin pérdida de seguimiento sobre incidentes activos, bloqueos pendientes ni degradaciones de conectores.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts` y workbook `Security operations efficiency` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / SOC L2 / Shift Lead.
- **Procedimiento paso a paso:**
  1. Auditar incidentes abiertos próximos a vencer SLA, tareas pendientes en **Case management** y reglas temporales de supresión próximas a expirar `[Verificado MS Learn]`.
  2. Emitir resumen formal de fin de turno detallando: incidentes críticos/altos abiertos, contenciones ejecutadas, conectores/playbooks en observación y campañas de hunting activas `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Bitácora diaria de entrega de turno archivada en el repositorio operativo del SOC.

---

## 6. Cadencia Operativa Semanal

> Integra las **2 actividades semanales oficiales** del `ops-guide` con optimización continua del SOC, tuning analítico y control operacional semanal `[Verificado MS Learn]`.

### S-01 — Ciclo de Vida de Soluciones y Actualizaciones en el Content Hub
- **Objetivo:** Mantener al día conectores CCF, reglas analíticas, parsers ASIM, workbooks, consultas de hunting y playbooks publicados por Microsoft y fabricantes.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Content management > Content hub` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / SOC L3.
- **Procedimiento:** Filtrar el **Content hub** por `Status = Update available`; revisar el archivo `ReleaseNotes.md` de cada solución antes de actualizar; aplicar actualizaciones preservando las reglas personalizadas como clones independientes de las plantillas OOTB (evitando sobrescritura accidental); y evaluar nuevas soluciones relevantes (ej. *Zero Trust TIC 3.0*, *SAP BTP*, soluciones esenciales basadas en **ASIM**) para incorporarlas al backlog de ingeniería `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de versiones actualizadas en Content Hub y tickets de despliegue en control de cambios.

### S-02 — Auditoría Semanal de Integridad y Cambios en Recursos de Microsoft Sentinel
- **Objetivo:** Detectar modificaciones, desactivaciones o eliminaciones no autorizadas sobre reglas analíticas, reglas de automatización, conectores, bookmarks o consultas sensibles.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Hunting > Advanced hunting` (`SentinelAudit`, `AzureActivity`, `LAQueryLogs`) `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / SOC Manager / GRC.
- **Procedimiento:** Ejecutar consultas de auditoría sobre `SentinelAudit` y `AzureActivity` (`Microsoft.SecurityInsights/*`) listando todas las operaciones `Create`, `Update` y `Delete` de los últimos 7 días; revisar `LAQueryLogs` para auditar consultas ejecutadas sobre tablas sensibles; y conciliar cada cambio contra solicitudes aprobadas en el pipeline CI/CD (*Sentinel Repositories*) o ITSM, revirtiendo e investigando cualquier alteración fuera de proceso `[Verificado MS Learn]`.
- **Evidencia auditable:** Reporte semanal de auditoría `SentinelAudit` / `AzureActivity` conciliado con control de cambios.

### S-03 — Revisión y Acción sobre Recomendaciones de SOC Optimization (Cobertura y Valor de Datos)
- **Objetivo:** Maximizar la relación cobertura-costo cerrando brechas de detección frente a amenazas y reubicando tablas sin uso analítico hacia niveles económicos.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Optimization` (SOC optimizations) `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 / Platform Engineer / SOC Manager.
- **Procedimiento:**
  1. Revisar recomendaciones de **cobertura basada en amenazas y riesgos** vinculadas a tácticas MITRE ATT&CK y activar las detecciones faltantes `[Verificado MS Learn]`.
  2. Evaluar recomendaciones de **Data value optimization**: para tablas facturables sin uso por reglas analíticas en los últimos 30 días (excepto tablas usadas por UEBA o TI matching), activar plantillas de detección relevantes o migrar la tabla al **Data Lake tier** (vía `Table management`), y revisar recomendaciones en preview de **columnas no utilizadas** (ej. `ConditionalAccessPolicies` en `SignInLogs` / `AADNonInteractiveUserSignInLogs`) verificando antes requisitos de cumplimiento `[Verificado MS Learn]`.
- **Evidencia auditable:** Exportación semanal (UI o API) del estado de recomendaciones de SOC Optimization (`Open`, `Mitigated`, `Dismissed` con justificación).

### S-04 — Tuning Semanal de Reglas Ruidosas, Mapeo de Entidades y Normalización ASIM
- **Objetivo:** Reducir la tasa de falsos positivos, enriquecer automáticamente cada alerta con entidades accionables y estandarizar consultas multi-fuente.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Analytics` y `Custom detection rules` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 (Detection Engineer) / SOC L2.
- **Procedimiento:** Extraer el Top 5 de reglas con mayor conteo de incidentes cerrados como `False Positive` o `Benign Positive` en la semana; refinar lógica KQL (aplicar filtros de tiempo y evento al inicio del pipeline, exclusiones mediante **Watchlists** auditadas, ajustar umbrales de agrupación), verificar mapeo completo de entidades (`Account`, `Host`, `IP`, `File`, `CloudApplication`) y migrar reglas específicas de fabricante hacia parsers **ASIM** cuando existan múltiples fuentes equivalentes `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Pull requests / commits en `Sentinel Repositories` (Bicep/ARM) y reducción medible de falsos positivos en la semana siguiente.

### S-05 — Mantenimiento de Watchlists, Fuentes UEBA y Reglas de Automatización Temporal
- **Objetivo:** Mantener precisos los datos contextuales que alimentan detecciones, supresiones controladas y puntajes de riesgo de comportamiento.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Watchlists`, `Automation` y `System > Settings > Microsoft Sentinel > UEBA` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L2 / Platform Engineer.
- **Procedimiento:** Actualizar **Watchlists** dinámicas o manuales (activos críticos, servidores de escaneo de vulnerabilidades, subredes VPN, cuentas *break-glass*, usuarios de alto impacto); auditar reglas de automatización de supresión confirmando que todas posean **Expiration date** definida; y verificar estado `Connected` de las fuentes en **UEBA** (incluyendo fuentes XDR conectadas en E5 y nuevas anomalías de firewalls/AWS/GCP incorporadas en 2026) `[Verificado MS Learn]`.
- **Evidencia auditable:** Fechas de última actualización de Watchlists y listado de Automation Rules auditadas.

### S-06 — Comité de Control Operacional Semanal del SOC (Métricas MTTA, MTTR/MTTC y Backlog)
- **Objetivo:** Gobernar el desempeño táctico del SOC, eliminar cuellos de botella entre turnos y priorizar el backlog de ingeniería de detección y SOAR.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Threat management > Workbooks > Security operations efficiency` `[Verificado MS Learn]`.
- **Rol responsable:** SOC Manager / SOC Leads L2-L3 / Platform Engineer.
- **Procedimiento:** Analizar en el workbook oficial **Security operations efficiency** el MTTA, MTTC/MTTR por severidad, distribución de cierres (TP/BP/FP), carga por analista e incidentes mayores de la semana; asignar acciones correctivas con responsable y fecha para todo desvío de SLA `[Verificado MS Learn]`.
- **Evidencia auditable:** Exportación semanal del workbook de eficiencia y minuta de acuerdos operativos.

---

## 7. Cadencia Operativa Mensual

> Desarrolla las **2 tareas mensuales oficiales** del `ops-guide` junto con gobierno FinOps del beneficio M365 E5, ingeniería de contenido como código y reporte ejecutivo `[Verificado MS Learn]`.

### M-01 — Revisión Mensual de Accesos, Roles RBAC/URBAC y Cuentas Inactivas en Sentinel
- **Objetivo:** Hacer cumplir estrictamente el principio de privilegio mínimo tanto en el plano SIEM (Azure RBAC) como en el Data Lake y portal unificado (Entra ID / Defender URBAC).
- **Consola y ruta:** `https://portal.azure.com > Resource Group de Sentinel > Access control (IAM)` y `https://security.microsoft.com > Permissions > Microsoft Defender XDR > Roles` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / IAM Admin / SOC Manager / GRC.
- **Procedimiento:**
  1. Exportar todas las asignaciones de roles en el Resource Group de Sentinel y de Playbooks (`Sentinel Reader`, `Responder`, `Contributor`, `Playbook Operator`, `Logic App Contributor`, `Owner`) recordando que los roles son acumulativos `[Verificado MS Learn]`.
  2. Cruzar con `LAQueryLogs` y registros de inicio de sesión para detectar analistas inactivos (>30 días), bajas/rotaciones del SOC o cuentas con permisos permanentes de escritura que deben pasar a elegibles en **PIM** `[Verificado MS Learn]`.
  3. Auditar los permisos de las **Managed Identities** de los playbooks y el alcance del rol `Microsoft Sentinel Automation Contributor`, revocando todo exceso y archivando evidencia firmada `[Verificado MS Learn]`.
- **Evidencia auditable:** Exportación mensual IAM / URBAC revisada, tickets de revocación ejecutados y acta de recertificación de accesos.

### M-02 — Revisión del Workspace, Niveles de Tablas (`Analytics` vs. `Data Lake`) y Retención Regulatoria
- **Objetivo:** Asegurar que la retención interactiva y total de cada tabla cumpla las exigencias legales/normativas al menor costo posible mediante `Table management`.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration / Data management > Tables` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / GRC / FinOps.
- **Procedimiento:**
  1. Auditar la configuración de retención en **Analytics tier** (90 días incluidos sin cargo adicional) y **Total retention** en el **Data Lake tier** (hasta 12 años) frente a la matriz regulatoria aplicable (PCI-DSS, ISO 27001, SOX, normativas bancarias o de protección de datos locales) `[Verificado MS Learn]`.
  2. Identificar tablas verbosas de datos secundarios que se estén ingiriendo innecesariamente en Analytics y cambiarlas a **Lake-only tier** o implementar reglas **DCR con `filter` y `split`** para enviar solo eventos de alto valor a Analytics y el resto al lago `[Verificado MS Learn]`.
  3. Diseñar **KQL jobs** o *Summary rules* sobre el Data Lake cuando se requiera agregar indicadores históricos hacia tablas ligeras en Analytics `[Verificado MS Learn]`.
- **Evidencia auditable:** Matriz mensual de tablas con tier configurado, días de retención Analytics/Total y validación firmada por GRC.

### M-03 — Conciliación FinOps Mensual: Commitment Tiers, Beneficio M365 E5 (5 MB/usuario/día) y Medidores del Lago
- **Objetivo:** Maximizar el aprovechamiento financiero del *Microsoft 365 E5 Data Grant*, las fuentes gratuitas y los descuentos de capacidad comprometida, evitando sobrecostos.
- **Consola y ruta:** `https://portal.azure.com > Cost Management + Billing > Cost analysis` y `System > Settings > Microsoft Sentinel > Pricing` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / SOC Manager / FinOps.
- **Procedimiento:**
  1. Agrupar costos en **Cost analysis** por `Meter` verificando la aplicación efectiva de los medidores sin cargo (`Free Benefit - M365 Defender Analysis` / `Data Ingestion` de hasta 5 MB/usuario/día y beneficio Defender for Servers P2 de 500 MB/nodo/día) `[Verificado MS Learn]`.
  2. Analizar el volumen diario real de los últimos 30 días en la tabla `Usage` para recalibrar hacia arriba o hacia abajo (permitido cada 31 días) el **Simplified Commitment Tier** (100 GB/día, 200 GB/día, 500 GB/día, 1 TB+) cuando el ahorro supere la tarifa PAYG `[Verificado MS Learn]`.
  3. Auditar el consumo mensual de consultas KQL sobre Data Lake, horas de vCore Spark/Graph, ejecuciones de Azure Logic Apps y consumo de **SCUs** (Security Copilot / MCP Entity Analyzer frente a la dotación incluida en M365 E5) `[Verificado MS Learn]`.
- **Evidencia auditable:** Reporte mensual FinOps del SOC con desglose de GB facturados vs. GB bonificados por M365 E5 y ahorro neto logrado.

### M-04 — Gobierno de Ingeniería de Detección como Código (*Sentinel Repositories*) y Rendimiento KQL
- **Objetivo:** Eliminar deuda técnica en reglas analíticas y custom detections, asegurando versionado Git/Bicep, pruebas y tiempos óptimos de ejecución.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Content management > Repositories` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 (Detection Engineer) / Platform Engineer.
- **Procedimiento:** Sincronizar y auditar que el 100 % de las reglas analíticas personalizadas, **Custom detection rules** (soportadas como código en Bicep en preview desde julio de 2026), Automation Rules (exportables en JSON/ARM) y playbooks estén respaldados en GitHub o Azure DevOps; revisar tiempos de ejecución y carga de consultas programadas optimizando joins y operadores costosos `[Verificado MS Learn]`.
- **Evidencia auditable:** Estado de sincronización exitosa en `Repositories` y reporte de salud de reglas sin errores de rendimiento.

### M-05 — Validación Mensual de Playbooks SOAR Críticos y Permisos de Identidad Administrada
- **Objetivo:** Confirmar mediante pruebas controladas que los flujos automáticos de contención (bloqueo de cuenta Entra ID, aislamiento MDE, bloqueo IP en firewall, creación de ticket ITSM) responden dentro de los objetivos operativos.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Automation` y entorno de prueba `[Verificado MS Learn]`.
- **Rol responsable:** SOAR Engineer / SOC L2.
- **Procedimiento:** Disparar un incidente sintético de prueba para cada familia crítica de playbooks; verificar orden secuencial de ejecución de las Automation Rules (considerando la ventana de 2 minutos para avance entre acciones cuando un playbook tarda más), confirmar éxito de autenticación por **Managed Identity** y comprobar el registro de evidencia en el sistema destino `[Verificado MS Learn]`.
- **Evidencia auditable:** Tasa mensual de éxito de playbooks (`Playbook success rate`) y bitácora de prueba controlada.

### M-06 — Reporte Ejecutivo Mensual de Operaciones de Seguridad y Riesgo al CISO
- **Objetivo:** Traducir la telemetría operativa del SIEM/XDR en indicadores ejecutivos de eficacia, cobertura de amenazas, retorno de inversión y postura de cumplimiento.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Threat management > Workbooks` `[Verificado MS Learn]`.
- **Rol responsable:** SOC Manager / CISO.
- **Procedimiento:** Consolidar tendencias mensuales de MTTA, MTTR/MTTC (promedio, P50 y P95), tasa de automatización SOAR, evolución de cobertura MITRE ATT&CK, cierre de brechas de SOC Optimization y eficiencia presupuestaria (ahorro M365 E5 + Data Lake) para presentación al comité ejecutivo de riesgo `[Verificado MS Learn]`.
- **Evidencia auditable:** Informe ejecutivo mensual PDF/Power BI y acta del comité de seguridad.

---

## 8. Cadencias Trimestral, Semestral y Anual

> Basadas en las guías oficiales de **MITRE ATT&CK Coverage**, **BCDR for Microsoft Sentinel**, **Transición al Portal Defender (`2027-03-31`)** e **Integración de Gobernanza NIST CSF 2.0 (Secure Future Initiative)** `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.

### T-01 (Trimestral) — Ejercicio Tabletop / Purple Team de Cadena de Ataque Multi-Dominio y Validación SOAR
- **Objetivo:** Poner a prueba la detección correlacionada SIEM+XDR, la ejecución de playbooks de contención y la toma de decisiones entre *"clean as you go"* y *"big bang"* ante un adversario activo.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts` y matriz `MITRE ATT&CK` `[Verificado MS Learn]`.
- **Rol responsable:** SOC Manager / Threat Hunter / SOC L3 / IAM & Endpoint Leads / GRC.
- **Procedimiento:** Ejecutar trimestralmente una simulación técnica o ejercicio de mesa (ransomware humano, compromiso de identidad híbrida/federada, abuso de workload identity o ataque sobre SAP/multicloud); verificar qué etapas generaron alertas, cómo agrupó el incidente el motor de correlación de Defender XDR, si los playbooks aislaron activos en tiempo y actualizar detecciones y runbooks con las brechas identificadas `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Informe Purple Team / Tabletop trimestral y tickets cerrados de nuevas detecciones creadas.

### T-02 (Trimestral) — Auditoría de Transición Completa al Portal de Microsoft Defender (Hito `2027-03-31`) y Deprecaciones
- **Objetivo:** Asegurar cero dependencia operativa respecto a experiencias heredadas en Azure Portal antes del retiro definitivo del **31 de marzo de 2027**, así como conectores o APIs obsoletas.
- **Consola y ruta:** `https://security.microsoft.com > System > Settings > Microsoft Sentinel` y `https://portal.azure.com` `[Verificado MS Learn]`.
- **Rol responsable:** Platform Engineer / SOC Manager.
- **Procedimiento:** Verificar que todos los workspaces estén incorporados al portal de Defender, que el 100 % de los runbooks, enlaces en notificaciones Teams/ITSM y entrenamientos del SOC apunten a `security.microsoft.com`, que no quede ningún conector personalizado usando la retirada *HTTP Data Collector API* (post 14-sep-2026) ni endpoints legacy de Graph `/security/alerts` (retirados en oct-2026 en favor de `alerts_v2` / `incidents`), y validar permisos Unified RBAC `[Verificado MS Learn]`.
- **Evidencia auditable:** Checklist trimestral de preparación y modernización de plataforma sin dependencias heredadas.

### SM-01 (Semestral) — Análisis Integral de Brechas de Cobertura MITRE ATT&CK v18
- **Objetivo:** Medir objetivamente la cobertura activa frente a técnicas adversarias prioritarias y planificar el roadmap semestral de ingeniería de detección.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Threat management > MITRE ATT&CK` `[Verificado MS Learn]`.
- **Rol responsable:** Threat Hunter / SOC L3 (Detection Engineer).
- **Procedimiento:** Inspeccionar la matriz nativa **MITRE ATT&CK (alineada a v18)** comparando la cobertura activa actual (reglas Scheduled, NRT y Custom Detections) frente a la **cobertura simulada** disponible en plantillas, soluciones del Content Hub y consultas de hunting; priorizar las técnicas críticas del perfil de amenaza sectorial sin cobertura y convertirlas en backlog comprometido del semestre `[Verificado MS Learn]`.
- **Evidencia auditable:** Exportación comparativa semestral de la matriz MITRE ATT&CK y plan de cierre de brechas aprobado.

### A-01 (Anual) — Autoevaluación Anual de Madurez NIST CSF 2.0, Prueba BCDR del SIEM y Revisión Zero Trust
- **Objetivo:** Evaluar formalmente la madurez del programa SecOps bajo las 6 funciones de NIST CSF 2.0, probar la resiliencia/continuidad del SIEM y actualizar la arquitectura multicloud/federada.
- **Consola y ruta:** `https://security.microsoft.com` y repositorio de código IaC (GitHub / Azure DevOps) `[Verificado MS Learn]`.
- **Rol responsable:** CISO / GRC Lead / Cloud Security Architect / SOC Manager.
- **Procedimiento:**
  1. Ejecutar la autoevaluación anual recomendada por Microsoft (`integrate-nist-2-governance`) registrando brechas en el *Risk Register* corporativo y recopilando el paquete de evidencia anual reproducible por KQL `[Verificado MS Learn]`.
  2. Validar el plan oficial de **Business Continuity and Disaster Recovery (BCDR)** de Sentinel: respaldo íntegro como código (Bicep/ARM) de reglas, workbooks, watchlists y playbooks, residencia de datos y simulacro de contingencia regional `[Verificado MS Learn]`.
  3. Revisar arquitectura de workspaces, espejo/federación con **Microsoft Fabric OneLake** y gobernanza de agentes IA / servidor MCP para el siguiente ejercicio fiscal `[Verificado MS Learn]`.
- **Evidencia auditable:** Informe anual de madurez NIST CSF 2.0, acta de prueba BCDR y documento de arquitectura SecOps actualizado.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

> Alineados con la guía oficial de **Incident Response Overview** y **Unified SIEM + XDR Operations** de Microsoft Learn `[Verificado MS Learn]`.

### AH-01 — Respuesta Mayor Coordinada ante Campaña de Ransomware Humano (*Human-Operated Ransomware*)
- **Disparador:** Incidente crítico multi-etapa (acceso inicial + robo de credenciales + movimiento lateral + evasión defensiva / precifrado `T1486`) o activación de *Automatic Attack Disruption*.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts` y `Action center` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. **Verificación de contención automática (<5 min):** Confirmar en el incidente y en `Action center` qué hosts y cuentas ya fueron contenidos automáticamente por *Attack Disruption* o por Automation Rules de severidad Crítica.
  2. **Contención ampliada por playbooks:** Ejecutar playbooks con Managed Identity para aislar de red en MDE todos los endpoints alcanzados en el *Blast radius*, deshabilitar cuentas comprometidas/revocar sesiones en Entra ID y bloquear IPs/dominios C2 en firewalls perimetrales y NSGs `[Verificado MS Learn]`.
  3. **Decisión táctica de erradicación:** Determinar junto al Incident Commander y SOC L3 si aplica contención *"clean as you go"* (intrusión acotada) o erradicación coordinada *"big bang"* (cuando el adversario posee persistencia amplia en identidad híbrida/administradores) para no alertar prematuramente al actor antes de cerrar todos sus vectores `[Verificado MS Learn]`.
  4. **Caza histórica en Data Lake:** Ejecutar búsqueda sobre el **Sentinel Data Lake** (meses previos) para ubicar el paciente cero, fecha real de intrusión inicial y alcance completo antes de autorizar restauración.
- **Evidencia auditable:** Expediente completo en Case Management, ejecuciones exitosas de Logic Apps, línea de tiempo forense y reporte ejecutivo SBAR.

### AH-02 — Playbook de Contención e Investigación ante Compromiso Crítico de Identidad Híbrida o Workload Identity
- **Disparador:** Incidente de robo de sesión AiTM sobre administrador, abuso de Service Principal / credenciales federadas, *Golden SAML* o anomalía crítica UEBA.
- **Consola y ruta:** `https://security.microsoft.com > Incidents & alerts`, `Assets > Identities` y `https://entra.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Ejecutar playbook de contención de identidad: deshabilitar usuario o Service Principal, revocar todos los *refresh tokens*, invalidar métodos MFA añadidos fraudulentamente y bloquear IPs origen.
  2. Pivotar en `Advanced hunting` correlacionando `SigninLogs` / `EntraIdSignInEvents`, `AADServicePrincipalSignInLogs`, `AuditLogs`, `CloudAppEvents` y `AzureActivity` para auditar persistencia (nuevas apps OAuth, secretos añadidos, asignaciones RBAC en suscripciones Azure o reglas de buzón).
  3. Verificar impacto cruzado mediante el grafo de entidades y *Entity Analyzer* antes de restablecer acceso sobre estación limpia con MFA resistente a phishing.
- **Evidencia auditable:** Registros de revocación en `AuditLogs`, trazas de ejecución del playbook y certificado de limpieza de persistencia.

### AH-03 — Caza de Emergencia (*Emergency Threat Hunt*) y Retro-Búsqueda ante Nuevo Boletín Zero-Day / CVE Crítico
- **Disparador:** Publicación urgente de explotación activa (MSRC, CISA KEV, Microsoft Threat Intelligence) con nuevos IOCs o TTPs.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Hunting > Advanced hunting`, `Threat intelligence > Intel management` y `Microsoft Sentinel > Threat management > Hunts` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Ingerir inmediatamente los IOCs (hashes, IPs, dominios, patrones de URL/User-Agent) en `ThreatIntelIndicators` o una Watchlist de emergencia.
  2. Abrir una campaña en **Hunts** ejecutando consultas KQL tanto sobre el **Analytics tier** (últimos 90 días) como sobre el **Data Lake tier** (hasta 12 meses+) usando esquemas normalizados **ASIM** (`imNetworkSession`, `imDns`, `imWebSession`, `imProcessCreate`) para barrer todas las tecnologías conectadas en una sola consulta `[Verificado MS Learn]`.
  3. Si se confirma actividad benigna, desplegar una **Custom detection rule (NRT o programada)** preventiva; si se hallan coincidencias positivas, promover Bookmarks a incidente crítico e iniciar contención AH-01/AH-02.
- **Evidencia auditable:** Campaña documentada en `Hunts`, consulta retrospectiva ejecutada sobre el lago y regla preventiva desplegada.

### AH-04 — Respuesta ante Interrupción Crítica de Ingesta o Pico Anómalo de Facturación en el SIEM
- **Disparador:** Alerta interna sobre `SentinelHealth` / caída abrupta de EPS en conectores críticos o alerta presupuestaria en Azure Cost Management por pico inesperado de GB/día.
- **Consola y ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Data connectors`, `Data management > Tables` y `portal.azure.com > Monitor > Data Collection Rules` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. **Ante caída de ingesta:** Verificar primero `Azure Service Health` / `M365 Service Health`; inspeccionar `SentinelHealth` para aislar si el fallo es de credenciales expiradas, cambio de red en firewall, saturación de un reenviador AMA Syslog/CEF o migración incompleta de conectores legacy; restablecer el conector y documentar la ventana exacta de brecha de visibilidad para auditoría.
  2. **Ante pico de volumen/costo:** Ejecutar consulta sobre tabla `Usage` y tablas top (`CommonSecurityLog`, `SecurityEvent`, `Syslog`, `AzureDiagnostics`) identificando el host, EventID o extensión CEF (`AdditionalExtensions`) causante del bucle de logs; aplicar transformación `filter` inmediata en la **DCR** o redirigir temporalmente el flujo secundario al **Data Lake tier** sin apagar la visibilidad de seguridad ni activar un *Daily Cap* ciego `[Verificado MS Learn]`.
- **Evidencia auditable:** Diagnóstico en `SentinelHealth` / `Usage`, cambio aplicado en DCR y nota de impacto en expediente de auditoría.

### AH-05 — Investigación Post-Incidente (Post-Mortem) e Institucionalización de Lecciones Aprendidas
- **Disparador:** Cierre de cualquier incidente de severidad Crítica o Alta, o incidente con impacto regulatorio/operacional.
- **Consola y ruta:** `https://security.microsoft.com > Incidents & alerts` (Case Management) y `Microsoft Sentinel > Optimization` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Extraer la cronología íntegra del caso desde `SecurityIncident`, `SecurityAlert` y comentarios del expediente, calculando MTTA, MTTC y MTTR reales frente al objetivo interno.
  2. Identificar brechas en tres ejes: visibilidad de logs (fuente faltante o mal ubicada de tier), lógica de detección (técnica MITRE no cubierta) y automatización (paso manual repetitivo automatizable con playbook).
  3. Crear y rastrear hasta su cierre las acciones correctivas en Git/ITSM: nueva regla analítica/custom detection, actualización de Watchlist, ajuste de playbook y actualización del runbook operativo.
- **Evidencia auditable:** Documento formal de Post-Mortem / RCA vinculado al ID de incidente y commits de mejora desplegados.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL Operativas, de Salud, FinOps y Auditoría

#### Consulta 1 — Salud Integral de Reglas Analíticas, Conectores y Automatización (`SentinelHealth`) `[Verificado MS Learn]`
```kql
// Detecta fallos recientes en reglas analíticas (incl. AUTO DISABLED), conectores de datos y playbooks/automation rules
SentinelHealth
| where TimeGenerated > ago(24h)
| where Status in ("Failure", "PartiallySucceeded")
| summarize Fallos24h = count(), UltimoFalloUTC = max(TimeGenerated), Motivos = make_set(Reason, 5)
    by SentinelResourceType, SentinelResourceName, OperationName
| order by Fallos24h desc, UltimoFalloUTC desc
```

#### Consulta 2 — Monitoreo de Agentes Silenciosos de Azure Monitor Agent (`Heartbeat`) `[Verificado MS Learn]`
```kql
// Identifica servidores y Log Forwarders CEF/Syslog con AMA que dejaron de reportar en la última hora
Heartbeat
| where TimeGenerated > ago(24h)
| where Category == "Azure Monitor Agent"
| summarize UltimoLatidoUTC = max(TimeGenerated), OS = any(OSType), VersionAgente = any(Version) by Computer, _ResourceId
| where UltimoLatidoUTC < ago(1h)
| extend MinutosDesconectado = datetime_diff('minute', now(), UltimoLatidoUTC)
| order by MinutosDesconectado desc
```

#### Consulta 3 — Métricas Ejecutivas del SOC: MTTA, MTTC/MTTR (Promedio, P50, P95) y Tasa de Falsos Positivos `[Verificado MS Learn]`
```kql
// Calcula KPIs oficiales de eficiencia operativa sobre el último registro de cada incidente en 30 días
SecurityIncident
| where TimeGenerated > ago(30d)
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| extend MinutosTriaje = iff(isnotnull(FirstModifiedTime), datetime_diff('minute', FirstModifiedTime, CreatedTime), real(null)),
         HorasCierre = iff(Status == "Closed" and isnotnull(ClosedTime), datetime_diff('minute', ClosedTime, CreatedTime) / 60.0, real(null))
| summarize TotalIncidentes = count(),
            Cerrados = countif(Status == "Closed"),
            MTTA_Min = round(avg(MinutosTriaje), 1),
            MTTC_Promedio_Horas = round(avg(HorasCierre), 2),
            MTTC_P50_Horas = round(percentile(HorasCierre, 50), 2),
            MTTC_P95_Horas = round(percentile(HorasCierre, 95), 2),
            TruePositives = countif(Classification == "TruePositive"),
            FalsePositives = countif(Classification == "FalsePositive"),
            BenignPositives = countif(Classification == "BenignPositive")
    by Severity
| extend TasaFP_Pct = round(todouble(FalsePositives) * 100.0 / iff(Cerrados == 0, 1, Cerrados), 1)
| order by TotalIncidentes desc
```

#### Consulta 4 — Control FinOps de Ingesta Facturable vs. Gratuita por Tabla (`Usage`) `[Verificado MS Learn]`
```kql
// Audita el volumen ingerido en los últimos 30 días separando tablas facturables y gratuitas para optimizar Commitment Tiers y Data Lake
Usage
| where TimeGenerated > ago(30d)
| summarize TotalGB_30d = round(sum(Quantity) / 1024.0, 2),
            PromedioDiario_GB = round(sum(Quantity) / 1024.0 / 30.0, 2)
    by DataType, IsBillable
| order by TotalGB_30d desc
```

#### Consulta 5 — Auditoría de Gobernanza sobre Modificaciones en Reglas y Automatización (`SentinelAudit` / `AzureActivity`) `[Verificado MS Learn]`
```kql
// Rastrea quién creó, modificó o eliminó reglas analíticas o reglas de automatización (evidencia NIST CSF 2.0 GV.OV / PR.AA)
SentinelAudit
| where TimeGenerated > ago(7d)
| where SentinelResourceType in ("Analytics Rule", "Automation rule")
| project TimeGenerated, OperationName, SentinelResourceType, SentinelResourceName, Status, Description, ExtendedProperties
| order by TimeGenerated desc
```

#### Consulta 6 — Detección Agnóstica de Fuente con ASIM: Fuerza Bruta Seguida de Éxito (`_Im_Authentication`) `[Verificado MS Learn]`
```kql
// Utiliza el parser unificado ASIM de autenticación para correlacionar fallos y éxito a través de Entra, Windows, Linux, Okta o VPNs
_Im_Authentication(starttime=ago(2h), endtime=now())
| summarize IntentosFallidos = countif(EventResult == "Failure"),
            IniciosExitosos = countif(EventResult == "Success"),
            Fuentes = make_set(EventProduct, 5),
            PrimerFallo = min(TimeGenerated),
            UltimoExito = maxif(TimeGenerated, EventResult == "Success")
    by TargetUsername, SrcIpAddr
| where IntentosFallidos >= 15 and IniciosExitosos >= 1 and UltimoExito > PrimerFallo
| order by IntentosFallidos desc
```

#### Consulta 7 — Verificación de Coincidencias de Indicadores de Threat Intelligence Activos `[Verificado MS Learn]`
```kql
// Resume el inventario activo de indicadores de inteligencia de amenazas por tipo y nivel de confianza
ThreatIntelligenceIndicator
| where TimeGenerated > ago(14d)
| summarize arg_max(TimeGenerated, *) by IndicatorId
| where Active == true and ExpirationDateTime > now()
| summarize IndicadoresActivos = count() by ThreatType, ConfidenceScore
| order by IndicadoresActivos desc
```

### 10.2 Mecanismos de Verificación Operativa ("Proof of Life" en Entornos con M365 E5)

| Dimensión Verificada | Ruta / Artefacto de Comprobación | Criterio de Validación Auditable | Etiqueta |
|---|---|---|---|
| **Unificación en Portal Defender** | `security.microsoft.com > System > Settings > Microsoft Sentinel` | Workspace primario conectado y cola `Incidents` mostrando incidentes sincronizados SIEM + XDR. | `[Verificado MS Learn]` |
| **Aplicación del Data Grant M365 E5** | `portal.azure.com > Cost Management > Cost analysis` (agrupar por `Meter`) | Presencia activa de medidores `Free Benefit - M365 Defender` descontando hasta 5 MB/usuario/día. | `[Verificado MS Learn]` |
| **Salud de Detección y SOAR** | Tabla `SentinelHealth` habilitada en `Settings > Auditing and health monitoring` | Registros continuos sin fallos persistentes en `Analytics Rule`, `Data connector` y `Playbook`. | `[Verificado MS Learn]` |
| **Gobierno de Niveles de Tablas** | `security.microsoft.com > Microsoft Sentinel > Data management > Tables` | Datos primarios en `Analytics` (90d+) con espejo activo y tablas verbosas secundarias en `Data Lake` (hasta 12 años). | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs del SOC con Microsoft Sentinel

> **Clarificación metodológica verificada:** Microsoft Learn documenta oficialmente **MTTA** (*Mean Time to Acknowledge / Triage*) y **MTTR / MTTC** (*Mean Time to Respond / Closure*) en el workbook *Security operations efficiency* y en *Incident Response Overview*; métricas complementarias como MTTD o porcentajes objetivo específicos (ej. `< 15 min`, `< 4 h`, `> 95 %` éxito en playbooks) se incluyen explícitamente como **propuestas editoriales consultivas** `[Decisión / Propuesta Editorial]`.

| ID | Indicador (KPI) | Definición Ejecutiva | Fórmula en Sentinel (`SecurityIncident` / `SentinelHealth`) | Meta Sugerida | Frecuencia | Audiencia | Naturaleza |
|---|---|---|---|---|---|---|---|
| **KPI-01** | **Tiempo Medio de Triaje / Reconocimiento (MTTA)** | Velocidad desde la creación del incidente en Sentinel/Defender hasta su asignación y cambio de estado inicial. | `avg(FirstModifiedTime - CreatedTime)` | `< 15 min` (Crítico/High) / `< 45 min` (Medium) | Semanal | SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tiempo Medio de Cierre / Resolución (MTTC / MTTR)** | Tiempo integral transcurrido desde la creación del incidente hasta su cierre validado tras contención y remediación. | `avg(ClosedTime - CreatedTime)` (más percentil `P95`) | `< 4 horas` (High) / `< 24 horas` (Medium) | Semanal / Mensual | SOC Manager / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Falsos Positivos por Catálogo Analítico (FPR)** | Porcentaje de incidentes cerrados como `FalsePositive` sobre el total de incidentes cerrados en el período. | `(countif(Classification == 'FalsePositive') / count(Closed)) * 100` | `< 15 %` global (`< 20 %` por regla individual) | Semanal / Mensual | SOC L3 (Detection Eng.) | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tasa de Éxito de Ejecución SOAR (Playbook Success Rate)** | Proporción de ejecuciones de playbooks de Logic Apps invocadas por Automation Rules que finalizan sin errores. | `(Runs_Succeeded / Total_Playbook_Runs) * 100` en `SentinelHealth` | `>= 98 %` | Diaria / Semanal | SOAR / Platform Eng. | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa de Automatización de Incidentes (Auto-Triage / Enrichment)** | Porcentaje de incidentes que reciben enriquecimiento, tareas estandarizadas, asignación o contención automática vía Automation Rules. | `(Incidentes_Con_Accion_SOAR / Total_Incidentes) * 100` | `>= 70 %` de incidentes enriquecidos automáticamente | Mensual | SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Disponibilidad de Conectores Críticos e Integridad de Reglas** | Porcentaje de conectores críticos recibiendo datos dentro de su ventana esperada y reglas activas sin estado `AUTO DISABLED`. | `(Recursos_Saludables / Total_Recursos_Criticos) * 100` | `>= 99,5 %` conectores / `0` reglas `AUTO DISABLED` | Diaria / Semanal | Platform Engineer | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Cobertura Activa de Técnicas MITRE ATT&CK Prioritarias** | Proporción de técnicas ATT&CK v18 definidas como críticas para el negocio que cuentan con al menos una regla activa validada. | `(Tecnicas_Prioritarias_Cubiertas / Total_Tecnicas_Prioritarias) * 100` | `>= 80 %` sobre técnicas prioritarias del sector | Semestral / Mensual | Threat Hunter / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Eficiencia de Valor de Datos y Aprovechamiento Grant M365 E5** | Porcentaje de tablas facturables en Analytics respaldadas por al menos una regla activa (0 tablas huérfanas en SOC Optimization) y captura del beneficio E5. | `(Tablas_Analytics_Con_Deteccion / Total_Tablas_Analytics_Facturables) * 100` | `>= 95 %` tablas Analytics con uso activo | Mensual | FinOps / CISO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional SIEM / SOAR (Niveles 1 a 5)

| Nivel | Estadio | Perfil Operativo Verificable `[Decisión / Propuesta Editorial]` |
|---|---|---|
| **Nivel 1** | **Reactivo / En Portal Heredado** | Operación aún fragmentada en Azure Portal; ingesta PAYG sin separación de tiers ni aprovechamiento consciente del grant E5; playbooks ausentes o con credenciales de usuario; sin auditoría `SentinelHealth`. |
| **Nivel 2** | **Unificado Estandarizado** | Workspace incorporado en `security.microsoft.com`; conectores M365/Entra/Defender y AMA operativos; rutinas diarias `ops-guide` activas; roles Azure RBAC a nivel Resource Group. |
| **Nivel 3** | **Gobernado y Medido** | Separación disciplinada **Analytics tier** vs. **Sentinel Data Lake tier**; Commitment Tier optimizado con M365 E5 Data Grant auditado; Automation Rules + Playbooks con **Managed Identity**; tuning semanal (<15 % FP) y métricas MTTA/MTTC reportadas. |
| **Nivel 4** | **Proactivo, As-Code y Optimizado** | Detecciones y Automation Rules gestionadas en **Sentinel Repositories (CI/CD Bicep)**; normalización **ASIM** multi-fuente; caza guiada por hipótesis (*Hunts*) sobre Data Lake; cierre sistemático de **SOC Optimization** y ejercicios Purple Team trimestrales. |
| **Nivel 5** | **SOC Agéntico y Federado** | Operación aumentada con **Microsoft Security Copilot**, agentes de triaje/caza y herramientas del **Sentinel MCP Server**; análisis relacional en **Sentinel Graph / Fabric OneLake** sin movimiento innecesario de datos; evidencia continua NIST CSF 2.0 audit-ready los 365 días. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

### 12.1 Sentinel como "Outcome Enabler" de NIST CSF 2.0

Bajo **NIST CSWP 29**, Sentinel actúa como **generador continuo de evidencia técnica objetiva, reproducible por KQL e histórica** para demostrar ante auditores internos y externos que los resultados (*outcomes*) de las seis funciones del marco se cumplen de manera sostenida `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome CSWP 29) | Capacidad Habilitadora en Microsoft Sentinel | Evidencia Auditable Reproducible | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OV-03` | El desempeño de la gestión de riesgos de ciberseguridad organizacional se evalúa y revisa para aplicar ajustes necesarios. | Workbook oficial *Security operations efficiency*, métricas históricas en `SecurityIncident` y recomendaciones basadas en riesgo de **SOC Optimization** (UI/API). | Exportación mensual de KPIs (MTTA, MTTC P50/P95, FPR) e historial de cierre de brechas de SOC Optimization. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` / `GV.PO-02` | Roles y políticas se establecen, revisan, actualizan y auditan de forma trazable. | Auditoría inmutable de cambios en `SentinelAudit`, `AzureActivity` y auditoría de consultas en `LAQueryLogs`, junto con versionado en `Sentinel Repositories`. | Reportes semanales de `SentinelAudit` conciliados contra Change Management y logs de `LAQueryLogs`. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-03` / `ID.AM-04` | Se mantienen representaciones de flujos de datos de red y de servicios provistos por terceros/nubes. | Más de 350 conectores en Content Hub, ingesta multicloud (Azure, M365, AWS, GCP, SAP), normalización CEF/ASIM y arquitectura multi-workspace / Data Lake con residencia geográfica definida. | Consultas sobre `Usage` y `CommonSecurityLog` inventariando todas las fuentes activas y documentación de residencia de datos del workspace. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-02` / `ID.RA-05` | Se recibe inteligencia de amenazas y se prioriza el riesgo según amenazas, vulnerabilidades e impacto. | Conectores STIX/TAXII, inteligencia nativa de Microsoft en `ThreatIntelIndicators`, matriz **MITRE ATT&CK v18** y evaluación de brechas en SOC Optimization. | Conteo de indicadores TI activos por confianza, mapa exportado de cobertura MITRE ATT&CK y registro de riesgos derivados. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso se gestionan, aplican y revisan bajo mínimo privilegio y separación de funciones. | Azure RBAC granular en Resource Group, Microsoft Defender Unified RBAC / Entra ID para Data Lake, scoping por fila y autenticación **Managed Identity** en playbooks. | Exportación mensual de IAM/URBAC (M-01), configuración de PIM y verificación de playbooks sin secretos hardcodeados. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-04` | Los registros de auditoría y logs se generan y ponen a disposición para monitoreo continuo y retención conforme a política. | Recolección mediante AMA + DCRs, Logs Ingestion API, separación `Analytics tier` (90d–2y) y `Sentinel Data Lake tier` (hasta 12 años). | Configuración verificada en `Table management` demostrando retención interactiva y de largo plazo alineada a normativa. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-01` / `DE.CM-09` | Las redes, plataformas de cómputo, entornos runtime y sus datos se monitorean continuamente para hallar eventos adversos. | Reglas analíticas **Scheduled**, **NRT**, **Custom Detection Rules**, modelos ML, **UEBA** (`BehaviorAnalytics`, `Anomalies`, `BehaviorInfo`) y monitoreo de salud `SentinelHealth`. | Catálogo exportado de reglas activas sin estado `AUTO DISABLED`, alertas generadas y chequeos continuos en `SentinelHealth`. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-03` / `DE.AE-07` | Se correlaciona información de múltiples fuentes integrando inteligencia de amenazas y contexto conductual; se ejecuta caza proactiva. | Correlación cruzada SIEM + Defender XDR en incidentes unificados, mapeo de entidades, **Sentinel Graph / Blast radius**, **Hunts** y **Bookmarks**. | Expedientes de incidentes multi-fuente, grafo de ataque exportado y campañas documentadas en `Hunts` / `HuntingBookmark`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MA-02` / `RS.CO-02` | Los incidentes son triados, validados, gestionados con propiedad clara y comunicados oportunamente a las partes interesadas. | Cola unificada de incidentes, **Case management** con tareas obligatorias, playbooks automáticos de notificación (Teams/correo) y sincronización bidireccional ITSM. | Muestras auditables de expedientes de incidentes cerrados por severidad, tickets ITSM enlazados y logs de notificación automática. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos para limitar su propagación e impacto en el negocio. | **Automation Rules** + **Playbooks en Logic Apps** que ejecutan bloqueo de usuario Entra ID, aislamiento de host en MDE o bloqueo IP en firewall, más *Automatic Attack Disruption*. | Historial `Runs history` en Logic Apps (`Succeeded`), logs de auditoría en el sistema destino y métrica MTTC. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-01` / `RC.RP-06` | Se ejecuta la recuperación asegurando resiliencia del propio servicio de monitoreo y documentando mejoras post-incidente. | Arquitectura **BCDR** oficial de Microsoft Sentinel (respaldo IaC en repositorios, resiliencia regional/cross-region) y análisis histórico de tendencias MTTR post-incidente. | Repositorio Git sincronizado de contenido Sentinel, acta anual de prueba BCDR e informes post-mortem con mejoras cerradas. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps / Admin / GRC)

| Rol en el SOC | Ruta Curricular Técnica Recomendada | Recursos Oficiales, Comunidad y Certificaciones | Horizonte Sugerido |
|---|---|---|---|
| **SOC L1 (Analista de Triaje)** | Fundamentos de Unified SecOps en `security.microsoft.com`, ciclo de vida de incidentes, grafo de ataque, Watchlists, KQL esencial y uso asistido de Security Copilot. | *Microsoft Sentinel Skill-Up Training* en Learn, *Must Learn KQL* (Rod Trent), *Microsoft Sentinel Training Lab* (17 ejercicios) y examen **SC-200** (*Microsoft Security Operations Analyst Associate*, guía actualizada oct-2026). | Semanas 1 a 4 `[Decisión / Propuesta Editorial]`. |
| **SOC L2 & Threat Hunter** | KQL intermedio/avanzado (series temporales, joins, grafos GQL), UEBA behaviors/anomalies, campañas **Hunts**, caza sobre **Sentinel Data Lake** y playbooks de respuesta a incidentes. | *Become a Microsoft Sentinel Ninja* (Ofer Shezaf), *The Definitive Guide to KQL* (Morowczynski, Trent, Zorich — Microsoft Press), repositorios KQL de Bert-Jan Pals y laboratorios en español de Jorge Castañeda (`d3fend.me`). Certificación: **SC-200**. | Semanas 5 a 14 `[Decisión / Propuesta Editorial]`. |
| **SOC L3 / Detection & Platform Engineer** | Recolección AMA/DCR, transformaciones `filter`/`split`, **Logs Ingestion API**, conectores **CCF**, normalización **ASIM**, **Sentinel Repositories (CI/CD Bicep)**, niveles `Analytics` vs. `Data Lake` y federación con Microsoft Fabric. | Documentación oficial de ASIM, Data Lake y CCF en Learn, acelerador *Sentinel All-in-One* (Javier Soriano), guías de DCR/Data Lake de Morten Knudsen y Clive Watson. Certificaciones: **SC-200** + **AZ-500**. | Semanas 6 a 19 `[Decisión / Propuesta Editorial]`. |
| **SOAR & AI Automation Engineer** | Diseño de **Automation Rules**, `Enhanced Alert Trigger`, **Azure Logic Apps (Consumption/Standard)** con **Managed Identity**, generador de playbooks con IA, **Security Copilot** y **Sentinel MCP Server**. | *Automation Ninja*, publicaciones de Benji Kovacevic en Microsoft Sentinel Blog, *Security Copilot Ninja* (Sean Wasonga) y libro *Exam Ref SC-200 2nd Edition* (abr-2026). | Semanas 12 a 25 `[Decisión / Propuesta Editorial]`. |
| **SOC Manager, FinOps & GRC** | Gobierno de **Simplified Commitment Tiers**, optimización del **M365 E5 Data Grant**, **SOC Optimization**, transición al portal Defender (`2027-03-31`), BCDR y auditoría continua **NIST CSF 2.0**. | *Manage your SOC with incident metrics*, *Plan costs and understand Sentinel pricing*, *Integrate NIST CSF 2.0 governance* y talleres SecOps del *Microsoft Security Adoption Framework (SAF)* (Mark Simos) + **SC-100**. | Continuo / Trimestral `[Decisión / Propuesta Editorial]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos Verificados y Correcciones Aplicadas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Técnica Revalidada | Hallazgo Oficial en Microsoft Learn (Noviembre 2026) | Impacto Aplicado en esta Guía Maestra |
|---|---|---|---|
| 1 | **Consolidación de los tres flujos separados de `MSEOP-MD`** | En el directorio fuente local, el archivo raíz `Sentinel - VC- SecOps` contenía únicamente el mapeo NIST CSF 2.0, mientras el modelo operativo real residía en `Modelo operacion`, los 12 bloques SecOps y `Sentinel OG`, y el detalle financiero en `Sentinel VC Lic`. | Se integraron los tres cuerpos (Operación SecOps + Auditoría NIST CSF 2.0 + FinOps/Beneficio M365 E5) en una arquitectura documental única y coherente. |
| 2 | **Fecha vigente de retiro de Sentinel en Azure Portal (`2027-03-31`)** | Mientras documentos y copias regionales de 2025 citaban el 1 de julio de 2026, Microsoft Learn confirma oficialmente que el soporte de Sentinel en Azure Portal finaliza después del **31 de marzo de 2027**, quedando disponible exclusivamente en `https://security.microsoft.com`. | Actualizado en Portada, Sección 3.1 (incluyendo tabla completa de mapeo de menús Azure -> Defender) y tarea trimestral **T-02**. |
| 3 | **Data Lake integrado por defecto (`2026-09-23`) y Federación con Microsoft Fabric** | Desde el **23 de septiembre de 2026**, el **Sentinel Data Lake** viene integrado en el onboarding de Sentinel sin alta separada, gestionándose desde `Table management` con retención de hasta 12 años, compresión 6:1, consultas KQL interactivas en `Advanced hunting` y espejo sin copia a **Microsoft Fabric OneLake**. | Actualizado en Sección 2, Sección 3.2 y tareas **M-02** / **M-03**, clarificando su relación con los medidores clásicos `Basic` / `Auxiliary` / `Archive`. |
| 4 | **Asociación exacta con M365 E5 / E7 y UEBA extendido** | La página oficial de la oferta verifica elegibilidad para **Microsoft 365 E7, E5, A5, F5, G5** y suites Security (**5 MB/usuario/día** automáticos sobre Entra ID, MDA Shadow IT, Purview IP y tablas Advanced Hunting XDR), además de consulta gratuita por 30 días de tablas XDR en Defender, SCUs incluidas en E5 y la capacidad en preview `extend-ueba` para conectar fuentes XDR a Sentinel UEBA sin re-ingesta. | Documentado con precisión quirúrgica en Sección 2.2, `relacionM365E5` del JSON y tarea mensual **M-03**. |
| 5 | **Retiros e hitos de ingesta, caza y SOAR en 2026** | (a) *HTTP Data Collector API* fuera de soporte tras el **14 de septiembre de 2026** (migración a **Logs Ingestion API** y **CCF**); (b) *Livestream* retirado en favor de **Hunts**, **NRT / Custom Detections** y `Advanced hunting`; (c) playbooks adjuntos directo a reglas analíticas obsoletos desde marzo de 2026 (uso obligatorio de **Automation Rules**); (d) **AI Playbook Generator** en **GA desde mayo de 2026**; (e) cambio de `AccountName` a solo prefijo UPN en julio de 2026; y (f) **Custom Detection Rules as Code** en `Repositories` (Preview, julio 2026). | Se depuraron referencias heredadas a *Livestream* o playbooks directos desde reglas analíticas y se incorporaron todas las prácticas vigentes en D-02, D-06, S-03 y M-04. |
| 6 | **Clarificación sobre KPIs oficiales vs. benchmarks consultivos** | Siguiendo la auditoría interna del propio corpus y Microsoft Learn (`manage-soc-with-incident-metrics`), Microsoft documenta **MTTA** y **MTTR / MTTC** como métricas primarias nativas, sin imponer metas numéricas universales (como *TPR >40 %*). | Se preservaron las fórmulas nativas sobre `SecurityIncident` y se etiquetaron todos los umbrales objetivo como `[Decisión / Propuesta Editorial]`. |

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Arquitectónica |
|---|---|---|
| **Objetivos numéricos de SLA y KPIs** (`MTTA < 15 min`, `MTTC < 4 h`, `FPR < 15 %`, `Playbook Success >= 98 %`, `MITRE >= 80 %`) | `[Decisión / Propuesta Editorial]` | Microsoft provee las tablas y workbooks de medición pero indica que los objetivos cuantitativos dependen de la dotación, severidad y acuerdos de nivel de servicio de cada organización. |
| **Extensión de cadencias a Trimestral, Semestral y Anual** (Purple Team, auditoría de transición al portal Defender, brechas MITRE y evaluación anual CSF 2.0) | `[Decisión / Propuesta Editorial]` | El artículo `ops-guide` oficial de Sentinel cubre frecuencias diaria, semanal y mensual; las actividades de horizonte mayor consolidan guías complementarias de Microsoft (`mitre-coverage`, `integrate-nist-2-governance`, `business-continuity-disaster-recovery`). |
| **Política de elegibilidad JIT en PIM (4 h / 8 h) y segregación de Resource Groups para Playbooks** | `[Decisión / Propuesta Editorial]` | Microsoft recomienda mínimo privilegio y asignación en Resource Group; los tiempos máximos de activación PIM y la separación estricta entre ingeniería SOAR y operación L1/L2 constituyen diseño de gobierno recomendado. |
| **Modelo de Madurez Operacional SIEM / SOAR en 5 niveles** | `[Decisión / Propuesta Editorial]` | Marco consultivo diseñado para evaluar la progresión desde un SIEM reactivo en portal heredado hasta un SOC agéntico unificado sobre Data Lake y Security Copilot. |
| **Mapeo de subcategorías y artefactos probatorios NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Conforme a NIST CSWP 29, el vínculo entre outcomes normativos y consultas KQL/reportes específicos de Sentinel es definido por la organización auditada. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn y Microsoft Azure

1. **REF-01 — Microsoft Sentinel operational guide (`ops-guide`):** `https://learn.microsoft.com/en-us/azure/sentinel/ops-guide` — Guía oficial de tareas operativas diarias, semanales y mensuales recomendadas por Microsoft para equipos SOC.
2. **REF-02 — Microsoft Sentinel in the Microsoft Defender portal:** `https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal` — Comparativa completa de capacidades, equivalencia de menús y confirmación oficial del fin de soporte en Azure Portal tras el **31 de marzo de 2027**.
3. **REF-03 — Plan costs and understand Microsoft Sentinel pricing and billing:** `https://learn.microsoft.com/en-us/azure/sentinel/billing` — Modelo oficial de facturación para Analytics tier (PAYG y Simplified Commitment Tiers), Data Lake tier (compresión 6:1), Sentinel Graph, servidor MCP y fuentes de datos gratuitas.
4. **REF-04 — Microsoft 365 E5 benefit offer with Microsoft Sentinel:** `https://azure.microsoft.com/en-us/pricing/offers/sentinel-microsoft-365-offer/` — Condiciones oficiales del **Data Grant de hasta 5 MB/usuario/día** para clientes M365 E7/E5/A5/F5/G5 y suites Security, con detalle de fuentes y tablas elegibles.
5. **REF-05 — Log retention tiers in Microsoft Sentinel & What is Sentinel data lake?:** `https://learn.microsoft.com/en-us/azure/sentinel/log-plans` y `https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview` — Clasificación oficial de datos primarios vs. secundarios, Analytics tier (90d–2y) y Data Lake tier (hasta 12 años).
6. **REF-06 — Roles and permissions in the Microsoft Sentinel platform:** `https://learn.microsoft.com/en-us/azure/sentinel/roles` — Matriz oficial de roles Azure RBAC para SIEM y Microsoft Entra ID / Defender Unified RBAC para el Data Lake.
7. **REF-07 — Automate threat response in Microsoft Sentinel with automation rules:** `https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules` — Arquitectura oficial de triggers, condiciones, orden secuencial, *Simple Flows* y permisos multitenant de Automation Rules.
8. **REF-08 — Authenticate playbooks to Microsoft Sentinel:** `https://learn.microsoft.com/en-us/azure/sentinel/automation/authenticate-playbooks-to-sentinel` — Configuración paso a paso de **System-Assigned Managed Identity** y roles mínimos requeridos para playbooks en Logic Apps.
9. **REF-09 — SOC optimization recommendations reference:** `https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-reference` — Catálogo oficial de recomendaciones de cobertura y *Data value optimization* (incluyendo columnas no utilizadas en preview).
10. **REF-10 — Normalization and the Advanced Security Information Model (ASIM):** `https://learn.microsoft.com/en-us/azure/sentinel/normalization` — Arquitectura de esquemas y parsers normalizados query-time e ingest-time alineados con OSSEM.
11. **REF-11 — What's new in Microsoft Sentinel:** `https://learn.microsoft.com/en-us/azure/sentinel/whats-new` — Registro oficial verificado a noviembre de 2026 (Data Lake onboarding integrado sep-2026, Fabric OneLake mirroring, Custom Detections as Code jul-2026, AI Playbook Generator GA may-2026, cambio `AccountName` UPN prefix).
12. **REF-12 — Connect data sources to UEBA with Microsoft 365 E5 (Preview):** `https://learn.microsoft.com/en-us/defender-xdr/extend-ueba` — Conexión directa de fuentes de Defender XDR hacia Sentinel UEBA en tenants E5 sin re-ingesta first-party.

### 15.2 Publicaciones Oficiales y Empleados de Microsoft

13. **REF-13 — Microsoft Sentinel Blog — UPDATE: New timeline for transitioning Sentinel experience to Defender portal:** `https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464` — Anuncio oficial del equipo de producto fijando el 31 de marzo de 2027 como fecha de retiro del portal de Azure.
14. **REF-14 — Ofer Shezaf (Principal Product Manager, Microsoft) — Become a Microsoft Sentinel Ninja: The complete level 400 training:** `https://techcommunity.microsoft.com/blog/microsoftsentinelblog/become-a-microsoft-sentinel-ninja-the-complete-level-400-training/1246310` — Programa maestro de formación nivel 400 reorganizado por roles de arquitectura, ingeniería y análisis SOC.
15. **REF-15 — Javier Soriano (Principal Product Manager, Microsoft) — Sentinel All-in-One & Sentinel as Code:** `https://github.com/javiersoriano/sentinel-all-in-one` — Acelerador técnico de despliegue automatizado e infraestructura como código para Microsoft Sentinel.
16. **REF-16 — Benji Kovacevic (Microsoft) — Create Tasks Repository in Microsoft Sentinel (SOAR Automation):** `https://techcommunity.microsoft.com/blog/microsoftsentinelblog/create-tasks-repository-in-microsoft-sentinel/4038563` — Patrones prácticos de estandarización de tareas de incidentes y orquestación SOAR con Automation Rules y Logic Apps.
17. **REF-17 — Rod Trent (Microsoft) — Must Learn KQL & THE PROMPT Newsletter:** `https://github.com/rod-trent/MustLearnKQL` — Serie formativa abierta de referencia para dominar Kusto Query Language orientado a operaciones de seguridad.

### 15.3 Comunidad y MVPs de Seguridad de Microsoft

18. **REF-18 — Bert-Jan Pals (Microsoft Security MVP) — KQL Query & Hunting Repository:** `https://kqlquery.com` — Portal técnico y colección curada de consultas avanzadas de detección, caza y respuesta a incidentes para Sentinel y Defender XDR.
19. **REF-19 — Jorge Castañeda (Microsoft Security MVP, Perú) — Blog Técnico d3fend.me (Español):** `https://blog.d3fend.me/` — Laboratorios reproducibles, priorización de vulnerabilidades e integración práctica de Microsoft Sentinel y Defender XDR en español.
20. **REF-20 — Morten Knudsen (Microsoft MVP) — AMA, DCR, Logs Ingestion API & Sentinel Data Lake:** `https://mortenknudsen.net/` — Artículos de arquitectura profunda sobre recolección moderna con DCR, transformaciones y gestión económica de tablas en el Data Lake.
21. **REF-21 — Clive Watson (Microsoft MVP) — Workspace Usage & Cost Workbooks (GitHub):** `https://github.com/clivewatson/KQLpublic/tree/master/KQL/Workbooks/WorkspaceUsage` — Workbooks comunitarios avanzados para auditoría granular de consumo, latencia y optimización de Log Analytics y Sentinel.

### 15.4 Marcos Normativos y de Gobernanza

22. **REF-22 — NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29):** `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` — Marco oficial basado en outcomes para las 6 funciones de gestión del riesgo cibernético.
23. **REF-23 — Integrate NIST CSF 2.0 governance & Unified SIEM/XDR Zero Trust (Microsoft Learn):** `https://learn.microsoft.com/en-us/security/zero-trust/sfi/integrate-nist-2-governance` y `https://learn.microsoft.com/en-us/security/operations/siem-xdr-overview` — Guías oficiales de Microsoft para autoevaluación de madurez CSF 2.0 e implementación integrada de Sentinel + Defender XDR bajo principios Zero Trust.

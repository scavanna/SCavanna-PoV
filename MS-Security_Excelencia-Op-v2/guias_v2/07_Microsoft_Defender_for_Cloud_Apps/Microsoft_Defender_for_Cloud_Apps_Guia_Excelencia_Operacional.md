# Guía Maestra de Excelencia Operacional: Microsoft Defender for Cloud Apps (MDA / CASB & SaaS Security)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `07_Microsoft_Defender_for_Cloud_Apps` |
| **Slug Canónico** | `Microsoft_Defender_for_Cloud_Apps` |
| **Nombre Completo** | Microsoft Defender for Cloud Apps (MDA / CASB & SaaS Security) |
| **Categoría Maestra** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (12 Bloques SecOps + NIST CSF 2.0 + Licenciamiento) + Revalidado Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Incluido en M365 E5** (también en Microsoft Defender Suite, Microsoft Purview Suite, EMS E5, M365 F5 Security & Compliance y licencia independiente por usuario) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://security.microsoft.com` (Microsoft Defender portal > Cloud apps), `https://entra.microsoft.com` (Conditional Access), `https://purview.microsoft.com` (migración DLP/Auto-labeling), `https://admin.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, SOC L1 (Operator/Monitor), SOC L2 (Incident Responder), SOC L3 (Threat Hunter / Detection Engineer), Cloud/SaaS Security Architect, Security Administrator, Compliance & GRC Lead |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Microsoft Zero Trust Reference Architecture (Applications & Data), MITRE ATT&CK Enterprise v18, CIS Critical Security Controls v8, Microsoft Security Adoption Framework (SAF) |

> **Regla de rigor documental:** Toda afirmación sobre arquitectura, consolas, roles RBAC, tablas KQL, conectores, licenciamiento y fechas de retiro respaldada por documentación pública vigente al 11 de noviembre de 2026 se identifica con `[Verificado MS Learn]`. Los objetivos numéricos de nivel de servicio (SLA/KPI), matrices RACI internas, modelos consultivos de madurez y mapeos interpretativos de evidencia para auditoría se declaran explícitamente con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Tesis Ejecutiva para el CISO y Liderazgo del SOC

La disolución del perímetro de red corporativo trasladó el plano de control crítico hacia la intersección entre **identidad, dispositivo, aplicación SaaS, sesión web e interacciones app-a-app (OAuth)**. **Microsoft Defender for Cloud Apps (MDA)** —históricamente abreviado como MDCA o MCAS— trasciende la definición clásica de un *Cloud Access Security Broker* (CASB) para operar como una plataforma convergente de seguridad SaaS integrada de forma nativa en **Microsoft Defender XDR** (`https://security.microsoft.com`) `[Verificado MS Learn]`.

Defender for Cloud Apps consolida cuatro disciplinas operativas en un único plano de telemetría e intervención `[Verificado MS Learn]`:

1. **CASB Fundamental y Gobernanza de Shadow IT / Shadow AI:** Descubrimiento continuo del uso real de aplicaciones en la nube evaluadas contra un catálogo de **más de 31.000 aplicaciones cloud** calificadas con **más de 90 factores de riesgo** de seguridad y cumplimiento, incluyendo una categoría nativa **Generative AI** con **más de 1.000 aplicaciones de IA generativa** (LLM, asistentes y herramientas SaaS de IA) y bloqueo automático en el endpoint mediante sincronización nativa con **Microsoft Defender for Endpoint (MDE)** `[Verificado MS Learn]`.
2. **SaaS Security Posture Management (SSPM):** Identificación continua de errores de configuración en aplicaciones SaaS conectadas (Microsoft 365, Salesforce, ServiceNow, Okta, GitHub, Box, entre otras), publicando acciones recomendadas directamente en **Microsoft Secure Score** y alimentando el grafo de **Microsoft Security Exposure Management** `[Verificado MS Learn]`.
3. **Protección Avanzada contra Amenazas (UEBA + XDR Inline/API):** Detección comportamental basada en Machine Learning e inteligencia de amenazas de Microsoft, correlacionada automáticamente en incidentes multi-dominio (correo, endpoint, identidad y SaaS) y combinada con controles preventivos en tiempo real mediante **Conditional Access App Control (CAAC)** (proxy inverso `*.mcas.ms` y **protección directa in-browser en Microsoft Edge for Business**) `[Verificado MS Learn]`.
4. **Protección App-to-App y Gobernanza OAuth (App Governance):** Visibilidad profunda, detección de anomalías ML, higiene de privilegios y remediación sobre aplicaciones OAuth registradas en **Microsoft Entra ID, Google Workspace y Salesforce**, neutralizando campañas de *consent phishing*, abuso de tokens, aplicaciones sobre-privilegiadas y rutas de ataque laterales hacia **Microsoft Graph** `[Verificado MS Learn]`.

### 2.2 Posicionamiento en Microsoft Zero Trust (Pilar Aplicaciones y Datos)

Microsoft estructura el despliegue Zero Trust para aplicaciones sobre seis objetivos progresivos que Defender for Cloud Apps materializa operativamente `[Verificado MS Learn]`:

| Principio Zero Trust | Objetivo de Despliegue Microsoft | Materialización Operativa en Defender for Cloud Apps | Etiqueta |
|---|---|---|---|
| **Verificar explícitamente** | Acceso y controles de sesión adaptativos | Integración con Microsoft Entra Conditional Access + CAAC para evaluar identidad, riesgo de sesión, ubicación y postura Intune/MDE en cada transacción web, exigiendo MFA *step-up* o restringiendo descargas en tiempo real. | `[Verificado MS Learn]` |
| **Usar acceso de mínimo privilegio** | Gobernanza OAuth, SSPM y RBAC | Auditoría y revocación de permisos OAuth no utilizados o excesivos en App Governance; endurecimiento SSPM de consolas SaaS; acceso administrativo regido por **Microsoft Defender Unified RBAC (URBAC)**. | `[Verificado MS Learn]` |
| **Asumir brecha** | Detección continua, UEBA y rutas de ataque | Motor UEBA con línea base de 7 días, `Investigation Priority Score`, análisis de *blast radius* en OAuth Attack Paths y caza proactiva sobre la tabla `CloudAppEvents` en Advanced Hunting. | `[Verificado MS Learn]` |

### 2.3 Licenciamiento Enterprise y Prerrequisitos Verificados (Noviembre 2026)

Microsoft Defender for Cloud Apps se licencia **por usuario**; toda persona cuyas sesiones, cuentas o actividades sean protegidas por el servicio requiere una licencia elegible `[Verificado MS Learn]`:

| Plan / Suite de Licenciamiento | Incluye MDA | Alcance y Notas de Arquitectura (Noviembre 2026) | Etiqueta |
|---|---|---|---|
| **Microsoft 365 E5 / A5 / G5** | Sí | Suite integral Enterprise. Incluye MDA completo, **App Governance** sin costo adicional, Entra ID P2, MDE P2, MDO P2, MDI y Microsoft Purview Suite. | `[Verificado MS Learn]` |
| **Microsoft Defender Suite** *(antes M365 E5 Security)* | Sí | Complemento de seguridad avanzada sobre M365 E3; incluye MDA + App Governance, Entra ID P2, MDE P2, MDI y MDO P2. | `[Verificado MS Learn]` |
| **Microsoft Purview Suite** *(antes M365 E5 Compliance)* | Sí | Habilita capacidades de MDA y resulta indispensable para la migración de **File Policies hacia Purview DLP / Auto-labeling** antes del 6 de enero de 2027. | `[Verificado MS Learn]` |
| **Enterprise Mobility + Security (EMS) E5** | Sí | Incluye MDA, Microsoft Entra ID P2, Microsoft Defender for Identity y Microsoft Intune Plan 1. | `[Verificado MS Learn]` |
| **Microsoft 365 F5 Security / F5 Security + Compliance** | Sí | Referido en Service Descriptions actuales como *Microsoft Defender + Purview Suite FLW* para trabajadores de primera línea. | `[Verificado MS Learn]` |
| **Microsoft Defender for Cloud Apps Standalone** | Sí | Licencia independiente por usuario; no exige suite de productividad M365, aunque requiere **Microsoft Entra ID P1** para utilizar Conditional Access App Control. | `[Verificado MS Learn]` |
| **Microsoft 365 E3 / EMS E3 / Business Premium** | No | No incluyen Defender for Cloud Apps completo (O365 Cloud App Security fue retirado/superado); requieren upgrade o add-on. | `[Verificado MS Learn]` |
| **Microsoft Agent 365 / Microsoft 365 E7** | Complementario | Desde el **1 de julio de 2026**, el descubrimiento, postura, detección de amenazas y tabla `AgentsInfo` para agentes de IA de Copilot Studio y Foundry exigen licencia **Microsoft Agent 365** (ver Sección 14). | `[Verificado MS Learn]` |

**Prerrequisitos técnicos indispensables antes de pasar a operación continua `[Verificado MS Learn]`:**
- **Consolidación de consola:** Acceso habilitado en `https://security.microsoft.com` bajo el nodo **Cloud apps** (el portal clásico `portal.cloudappsecurity.com` redirige obligatoriamente desde junio de 2024 sin opción de reversión).
- **Conector Microsoft 365 activo:** En `System > Settings > Cloud apps > Connected apps > App Connectors`, conectar **Microsoft 365** marcando explícitamente `Microsoft 365 activities` y `Microsoft 365 files` para poblar `Activity log` y la tabla KQL `CloudAppEvents`.
- **Integración nativa con Microsoft Defender for Endpoint:** Activar el interruptor en `System > Settings > Cloud apps > Cloud Discovery > Microsoft Defender for Endpoint` para telemetría continua de *Defender-managed endpoints* (Windows y macOS) fuera de la red corporativa y enforcement de bloqueo por indicadores de red.
- **Rangos de direcciones IP corporativas (`IP address ranges`):** Configurar subredes de sedes, salidas NAT, proxies sancionados y concentradores VPN en `System > Settings > Cloud apps > System > IP address ranges` antes de evaluar alertas UEBA de ubicación o *Impossible travel*.
- **Integración de cuentas SaaS con Identity Inventory:** Habilitada automáticamente desde el **15 de octubre de 2026** para tenants elegibles que no emplean los roles heredados `User group admin` o `App/instance admin`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Diagrama de Flujo de Señales y Control (Signal-to-Enforcement Loop)

```
+---------------------------------------------------------------------------------------------------+
|                        FUENTES DE TELEMETRÍA E INTERCEPCIÓN DE TRÁFICO                            |
|  [Endpoints MDE Win/macOS]   [Log Collectors Syslog/FTP & SWG]   [IdP Entra ID / SAML / OIDC]     |
|  [Conectores API SaaS: M365, Salesforce, Google, Box, Okta, AWS]  [Edge for Business / Proxy CAAC]|
+-------------------------------------------------+-------------------------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|             MICROSOFT DEFENDER FOR CLOUD APPS (en https://security.microsoft.com)                 |
|  +-----------------------+ +-----------------------+ +---------------------+ +------------------+ |
|  | Cloud Discovery &     | | Conditional Access    | | Motor UEBA,         | | App Governance & | |
|  | Catálogo >31k Apps    | | App Control (CAAC) &  | | Activity Policies & | | Application      | |
|  | (>1.000 GenAI Apps)   | | Edge In-Browser Prot. | | Malware TI Scanning | | Inventory (OAuth)| |
|  +-----------------------+ +-----------------------+ +---------------------+ +------------------+ |
+----------+-------------------------+-------------------------+------------------------+-----------+
           |                         |                         |                        |
           v                         v                         v                        v
+--------------------+   +-----------------------+   +----------------------+   +-------------------+
| Defender for       |   | Microsoft Purview     |   | Microsoft Defender   |   | Microsoft         |
| Endpoint (MDE)     |   | Information Prot. &   |   | XDR + Exposure Mgmt  |   | Sentinel          |
| Bloqueo/Warn de    |   | DLP (Migración File   |   | Incidentes XDR,      |   | SIEM/SOAR, Data   |
| Apps Unsanctioned  |   | Policies <06-Ene-2027)|   | CloudAppEvents,      |   | Grant E5 (5MB/u/d)|
| en red del equipo  |   | Etiquetas / Cifrado   |   | OAuth Attack Paths   |   | Retención DataLake|
+--------------------+   +-----------------------+   +----------------------+   +-------------------+
```

### 3.2 Componentes Operativos y Modos de Intervención

| Componente Técnico | Función Operativa Principal | Ruta en Consola Vigente (Nov 2026) | Integraciones Clave | Etiqueta |
|---|---|---|---|---|
| **Cloud Discovery & App Catalog** | Analiza logs de tráfico cuatro veces al día contra >31.000 apps y >90 factores de riesgo (SOC 2, ISO 27001, GDPR, cifrado, IA generativa). Soporta *Snapshot reports* y *Continuous reports*. | `security.microsoft.com > Cloud apps > Cloud discovery` y `Cloud app catalog` | MDE, Log Collector Docker (Syslog/FTP), Zscaler, iboss, Menlo, Corrata, Entra Global Secure Access | `[Verificado MS Learn]` |
| **Application Inventory Unificado** | Consolida en dos pestañas (**SaaS apps** y **OAuth apps**) el estado de protección, etiquetas, apps GenAI sin clasificar, apps OAuth sobre-privilegiadas, sin uso (>90 días) y publishers no verificados. | `security.microsoft.com > Assets > Applications` | Cloud Discovery, App Governance, Identity Inventory (Non-human identities) | `[Verificado MS Learn]` |
| **App Connectors (API)** | Conexión out-of-band por API OAuth/REST hacia proveedores SaaS para inventariar cuentas, actividades administrativas/usuario, archivos y postura SSPM. | `security.microsoft.com > System > Settings > Cloud apps > Connected apps > App Connectors` | Microsoft 365, Salesforce (incl. Real-Time Event Monitoring en preview), Google Workspace, Box, Dropbox, Okta, GitHub, Workday, ServiceNow | `[Verificado MS Learn]` |
| **Conditional Access App Control (CAAC)** | Control inline en tiempo real de sesiones basadas en navegador (bloquear descarga, *protect-on-download*, bloquear copiar/pegar/imprimir, escaneo antimalware en subida/bajada, *step-up* MFA). | `entra.microsoft.com > Protection > Conditional Access` + `security.microsoft.com > Cloud apps > Policies > Policy management > Conditional Access` | Microsoft Entra ID (incorporación automática de apps Entra), Okta, AD FS, cualquier IdP SAML 2.0 | `[Verificado MS Learn]` |
| **In-Browser Protection con Edge for Business (Preview)** | Aplica controles de sesión directamente en el perfil de trabajo de Microsoft Edge (Windows 10/11 y macOS) sin redirección por proxy inverso ni sufijo `.mcas.ms`, deshabilitando herramientas de desarrollador. | `security.microsoft.com > System > Settings > Cloud apps > Conditional Access App Control > Edge for Business protection` | Microsoft Edge for Business, Microsoft Entra Conditional Access, Microsoft Purview Browser DLP | `[Verificado MS Learn]` |
| **App Governance (OAuth Security)** | Supervisión de permisos delegados y de aplicación, consumo de datos vía Graph API, sensibilidad de datos accedidos y detección ML de anomalías para apps OAuth. | `security.microsoft.com > Cloud apps > App governance` | Microsoft Entra ID, Google Workspace, Salesforce Connected Apps & ECAs | `[Verificado MS Learn]` |
| **Motor UEBA y Detección de Amenazas** | Perfilado conductual (ventana inicial de aprendizaje de 7 días), `Investigation Priority Score`, atributos `UncommonForUser` / `LastSeenForUser` y políticas de actividad/anomalía. | `security.microsoft.com > Cloud apps > Policies > Policy management > Threat detection` y `Assets > Identities` | Microsoft Defender XDR, Entra ID Protection, Microsoft Threat Intelligence | `[Verificado MS Learn]` |
| **SSPM & OAuth Attack Paths** | Evalúa configuraciones inseguras en apps SaaS conectadas y modela rutas de ataque desde dispositivos vulnerables hacia *Service Principals* con permisos críticos en Graph. | `security.microsoft.com > Exposure management > Recommendations` y `Attack surface > Attack paths` | Microsoft Secure Score, Microsoft Security Exposure Management | `[Verificado MS Learn]` |

> **Advertencia arquitectónica sobre clientes nativos y coexistencia DLP `[Verificado MS Learn]`:**
> 1. Los controles de sesión de CAAC operan exclusivamente sobre sesiones interactivas en navegadores soportados (Edge, Chrome, Firefox, Safari). **La aplicación de escritorio de Microsoft Teams no soporta controles de sesión CAAC**; para evitar evasión de bloqueos de descarga, las políticas de Acceso Condicional deben restringir el acceso desde clientes de escritorio para los usuarios/escenarios acotados y permitir acceso web.
> 2. En dispositivos cubiertos simultáneamente por **Microsoft Purview Endpoint DLP** y una política de sesión de Defender for Cloud Apps sobre el mismo contexto, **Endpoint DLP tiene prioridad**. Asimismo, **File Policies de MDA y políticas equivalentes de Purview DLP no deben coexistir activas** porque generan conflictos de enforcement durante la migración previa al **6 de enero de 2027**.

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Evolución hacia Microsoft Defender Unified RBAC (URBAC)

Desde diciembre de 2025 la integración de permisos de Defender for Cloud Apps en **Microsoft Defender Unified RBAC (URBAC)** está disponible globalmente, y desde **agosto de 2026 viene habilitada por defecto para todos los clientes nuevos** `[Verificado MS Learn]`. En paralelo:
- Los roles granulares heredados de MDA (`App/instance admin`, `User group admin`, `Cloud Discovery global admin` y `Cloud Discovery report admin`) **ya no están disponibles para nuevas configuraciones** por consolidación de plataforma (las asignaciones preexistentes siguen soportadas) `[Verificado MS Learn]`.
- Casi la totalidad de las vistas y acciones de **App Governance** en el portal unificado son gobernadas **únicamente por roles de Microsoft Entra ID** (la excepción es la consulta de la tabla `OAuthAppInfo` en Advanced Hunting, autorizada vía URBAC) `[Verificado MS Learn]`.

### 4.2 Matriz RBAC de Mínimo Privilegio y Elegibilidad PIM

| Rol Técnico Oficial (Entra ID / Defender URBAC / MDA) | Nivel SOC / Función | Permisos Operativos Clave | Estrategia PIM / JIT Recomendada | Responsabilidad Operativa | Etiqueta |
|---|---|---|---|---|---|
| **Security Reader** / **Global Reader** | SOC L1 (Monitor) / Auditoría GRC | Lectura de alertas, incidentes, apps descubiertas, catálogo, políticas, archivos y registro de gobernanza. (`Security Reader` puede generar tokens API propios; `Global Reader` es 100 % solo lectura). | Asignación permanente sobre grupo de seguridad SOC L1 / Auditores con MFA phishing-resistant `[Decisión / Propuesta Editorial]`. | Monitoreo continuo de tableros, verificación de evidencias y auditoría sin riesgo de alteración. | `[Verificado MS Learn]` |
| **Security Operator** | SOC L1 / SOC L2 (Triage & IR) | Todos los permisos de lectura más gestión de alertas/incidentes y configuración de conectores API seleccionados; **no puede** crear/editar políticas ni banear apps globalmente. | Permanente para analistas de turno activo o elegible en Entra PIM (8 h) `[Decisión / Propuesta Editorial]`. | Triaje diario en cola unificada XDR, investigación en `Activity log` y `CloudAppEvents`, escalamiento documentado. | `[Verificado MS Learn]` |
| **Cloud App Security Administrator** | Ingeniería CASB / SaaS Security Admin | Control total circunscrito exclusivamente a Defender for Cloud Apps (políticas, conectores, CAAC, rangos IP, acciones de gobernanza, SIEM agents y administración de roles MDA) sin otorgar control sobre otros workloads Defender. | **Elegible (JIT) vía Microsoft Entra PIM**, máximo 4 horas, requerir MFA FIDO2, justificación y ticket de cambio `[Decisión / Propuesta Editorial]`. | Onboarding de conectores API y apps CAAC, tuning de políticas, etiquetado Sanctioned/Unsanctioned, mantenimiento de salud. | `[Verificado MS Learn]` |
| **Compliance Administrator** / **Compliance Data Administrator** | Gobierno de Datos / DLP & Privacidad | Lectura en MDA, gestión de alertas y administración de políticas de archivos/reportes de descubrimiento; habilitado para ejecutar el asistente **DLP to Purview migration** en conjunto con Security Admin. | Elegible (JIT) vía Entra PIM (4–8 h) con aprobación del Oficial de Cumplimiento/Privacidad `[Decisión / Propuesta Editorial]`. | Gestión de cuarentenas administrativas, informes ejecutivos de Shadow IT y migración de File Policies hacia Microsoft Purview. | `[Verificado MS Learn]` |
| **Security Administrator** | SOC L3 / Lead Security Engineer | Acceso administrativo transversal en Microsoft Defender XDR, incluyendo MDA completo, App Governance, activación de Unified RBAC y Security Exposure Management. | **Estrictamente Elegible (JIT) en Entra PIM** (máx. 4 h), aprobación dual y estación de trabajo privilegiada (PAW) `[Decisión / Propuesta Editorial]`. | Diseño de arquitectura XDR, gobierno de roles URBAC, remediación de OAuth Attack Paths y aprobaciones de alto impacto. | `[Verificado MS Learn]` |
| **Application Administrator** / **Cloud Application Administrator** | IAM / OAuth Remediation | Gestión de registros de aplicaciones, Service Principals, políticas de consentimiento y revocación/deshabilitación definitiva de apps OAuth en Microsoft Entra ID (además de prerrequisito para habilitar Information Protection en MDA). | **Elegible (JIT) en Entra PIM** (máx. 2–4 h) con validación de ticket SOC/IAM `[Decisión / Propuesta Editorial]`. | Contención definitiva de aplicaciones OAuth maliciosas, rotación/revocación de credenciales de apps y políticas de consentimiento. | `[Verificado MS Learn]` |
| **Global Administrator** | Emergencia (Break-Glass) | Acceso irrestricto al tenant completo. Microsoft recomienda explícitamente restringirlo a escenarios de emergencia donde ningún rol específico sea viable. | Solo cuentas *break-glass* excluidas de dependencia circular y monitoreadas con alerta crítica inmediata `[Verificado MS Learn]`. | Uso exclusivo ante contingencia catastrófica de identidad o recuperación del tenant. | `[Verificado MS Learn]` |

### 4.3 Matriz RACI Organizacional por Dominio Operativo

> La siguiente matriz RACI constituye una estructura organizacional recomendada para segregar ejecución técnica, aprobación de riesgo y auditoría interna `[Decisión / Propuesta Editorial]`.

| Dominio / Proceso Operativo | SOC L1 | SOC L2 (IR) | SOC L3 / Hunter | SaaS / MDA Admin | IAM / Entra Admin | GRC / Privacidad | SOC Mgr / CISO |
|---|---|---|---|---|---|---|---|
| Triaje diario de incidentes XDR y alertas CASB | R | A | C | I | I | I | I |
| Investigación UEBA y caza en `CloudAppEvents` | C | R | A | I | C | I | I |
| Revisión diaria de App Governance y revocación OAuth | C | R | C | R | A | I | I |
| Salud de CAAC, Edge In-Browser, Conectores y Colectores | I | I | C | R/A | C | I | I |
| Clasificación Shadow IT / Shadow AI (Unsanction + MDE) | R | C | C | R | I | C | A |
| Remediación SSPM y OAuth Attack Paths | I | C | R | R | C | I | A |
| Migración File Policies a Microsoft Purview (<06-Ene-2027) | I | I | C | R | I | R/A | I |
| Auditoría mensual de acciones admin ("Audit the Auditors") | I | I | C | C | I | R | A |

*(R = Responsible · A = Accountable · C = Consulted · I = Informed)*

---

## 5. Cadencia Operativa Diaria

> Basada en el **Microsoft Defender for Cloud Apps Daily Operational Guide** oficial y enriquecida con flujos de correlación XDR y criterios de escalamiento `[Verificado MS Learn]`.

### D-01 — Triaje de Incidentes y Alertas CASB en Cola Unificada XDR
- **Objetivo:** Detectar y clasificar tempranamente compromisos de cuentas SaaS, robo de sesiones y actividad maliciosa correlacionada entre SaaS, identidad, endpoint y correo.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Filtrar `Status = New, In progress` y `Severity = High, Medium` manteniendo **todas las fuentes de servicio marcadas** para preservar la correlación XDR de alta fidelidad; aplicar filtro secundario `Service source = Microsoft Defender for Cloud Apps` para barrido focalizado CASB `[Verificado MS Learn]`.
  2. Abrir la página del incidente y examinar la pestaña **Attack story** para reconstruir la relación entre usuario, IP origen, dispositivo y aplicación SaaS.
  3. En la pestaña **Evidence and response**, seleccionar cada evidencia > menú de opciones > **Investigate** > **Activity log** o **Go hunt** `[Verificado MS Learn]`.
  4. En la pestaña **Users**, verificar saltos abruptos en el **Investigation Priority Score** y presencia de etiquetas IP (`Corporate VPN`, `Anonymous proxy`, `Tor`).
  5. En **Manage incident**, clasificar como `True positive` (especificando el tipo de amenaza), `False positive` o `Informational, expected activity`, asignar propietario y pasar a `In progress` `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de cambio de estado, propietario, clasificación y comentario estructurado `[UTC Timestamp] - [Analista] - [Acción/Hallazgo]` en el incidente XDR.

### D-02 — Revisión de Detección de Amenazas y Anomalías Comportamentales (UEBA)
- **Objetivo:** Identificar ataques lentos y persistentes (*low-and-slow*), viajes imposibles reales, actividad desde países infrecuentes, descargas masivas o cifrado tipo ransomware en repositorios cloud.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management > Threat detection` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Revisar las coincidencias generadas por **Activity policies** y **Anomaly detection policies** en las últimas 24 horas (`Impossible travel`, `Activity from infrequent country`, `Unusual multiple file download`, `Ransomware activity`, `Suspicious inbox forwarding`) `[Verificado MS Learn]`.
  2. Abrir el **Activity log** vinculado a la alerta y contrastar `UncommonForUser` y `LastSeenForUser` con el perfil histórico del usuario en `Assets > Identities`.
  3. Descartar falsos positivos de red verificando si la IP pertenece a nueva sede o VPN no registrada en `IP address ranges`; si es legítima, abrir tarea de actualización de rangos IP.
  4. Confirmar técnicamente picos de descarga mediante consulta KQL por bloques horarios (`bin(Timestamp, 1h)`) en `CloudAppEvents` antes de suspender usuario o escalar a respuesta a incidentes.
- **Evidencia auditable:** Trazabilidad en `Activity log`, consulta KQL adjunta al caso y actualización del ticket de investigación.

### D-03 — Evaluación Diaria de App Governance y Aplicaciones OAuth Riesgosas
- **Objetivo:** Detectar y contener ataques de *consent phishing*, aplicaciones OAuth con publishers no verificados, privilegios excesivos o extracción anómala vía Microsoft Graph / Google / Salesforce.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > App governance > Overview` y pestañas `Microsoft 365` / `Google` / `Salesforce` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L2 / SaaS Security Admin.
- **Procedimiento paso a paso:**
  1. Revisar en **Overview** los indicadores diarios recomendados por Microsoft: número de apps *Overprivileged* o *Highly privileged*, apps con **Unverified publisher**, volumen de uso de datos por **Graph API**, y conteo de apps que accedieron a archivos con y sin **Sensitivity labels** `[Verificado MS Learn]`.
  2. Filtrar alertas con `Detection source = App Governance` en la cola de alertas XDR (ej. `OAuth App with suspicious Reply URL`, `App with suspicious OAuth scope made graph calls to read email and created inbox rule`).
  3. Inspeccionar permisos delegados y de aplicación críticos (`Mail.ReadWrite`, `MailboxSettings.ReadWrite`, `Files.ReadWrite.All`, `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`).
  4. Ante confirmación de app maliciosa o no autorizada con alto riesgo, ejecutar **Disable app** / **Revoke app** y pivotar con **View in Entra ID** para revocar *refresh tokens* de usuarios afectados `[Verificado MS Learn]`.
- **Evidencia auditable:** Captura/exportación de postura diaria de App Governance y registro de deshabilitación en `Governance log` y `AuditLogs` de Entra ID.

### D-04 — Monitoreo de Alertas y Estado de Conditional Access App Control (CAAC) e In-Browser Protection
- **Objetivo:** Garantizar que los controles preventivos en tiempo real sobre sesiones web (bloqueo de descarga, bloqueo de copia/impresión, inspección de malware) estén operativos y sin bypass.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management > Conditional Access` y `System > Settings > Cloud apps > Connected apps > Conditional Access App Control apps` `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin / SOC L1.
- **Procedimiento paso a paso:**
  1. Revisar alertas diarias disparadas por políticas de acceso y de sesión (intentos de descarga desde dispositivos no administrados, bloqueos de subida de malware, accesos desde clientes nativos no permitidos) `[Verificado MS Learn]`.
  2. Filtrar `Cloud apps > Activity log` por `Source = Access control` y `Source = Session control` para auditar bloqueos efectivos y posibles fricciones operativas `[Verificado MS Learn]`.
  3. Confirmar en `Conditional Access App Control apps` que todas las aplicaciones críticas muestran estado **Connected** (sin errores SAML/OIDC ni certificados vencidos) y verificar la directiva de **Edge for Business protection** (`System > Settings > Cloud apps > Conditional Access App Control > Edge for Business protection`).
- **Evidencia auditable:** Eventos con `AuditSource` igual a `Defender for Cloud Apps session control` / `access control` en `CloudAppEvents` y estado `Connected` verificado.

### D-05 — Descubrimiento de Shadow IT y Gobernanza de Shadow AI (Generative AI)
- **Objetivo:** Visibilizar y controlar la adopción no autorizada de servicios SaaS de alto riesgo y herramientas de IA generativa externas antes de que ocurra fuga de propiedad intelectual o PII.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Cloud discovery > Dashboard` y `Discovered apps` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / SaaS Security Admin.
- **Procedimiento paso a paso:**
  1. Examinar los widgets superiores del **Cloud discovery dashboard** identificando variaciones atípicas en aplicaciones descubiertas, usuarios activos, direcciones IP top y distribución geográfica `[Verificado MS Learn]`.
  2. En la pestaña **Discovered apps**, filtrar aplicaciones nuevas con `Risk score <= 4` y volumen de subida relevante (`Uploaded bytes > 50 MB`) `[Decisión / Propuesta Editorial]`.
  3. Aplicar el filtro **Category = Generative AI** (catálogo de >1.000 apps GenAI) y cruzar con los *insights* de `Assets > Applications > SaaS apps` (`Untagged GenAI apps`, `Untagged high risk apps`) `[Verificado MS Learn]`.
  4. Evaluar atributos de cumplimiento (ausencia de SOC 2, ISO 27001, GDPR, retención de prompts para entrenamiento) y clasificar formalmente como **Sanctioned**, **Unsanctioned** (bloqueo automático en endpoints MDE o modo *Warn and educate*) o etiqueta personalizada bajo monitoreo `[Verificado MS Learn]`.
- **Evidencia auditable:** Historial de etiquetado de aplicaciones en `Governance log` e indicadores URL generados automáticamente en Microsoft Defender for Endpoint.

### D-06 — Revisión Proactiva de Exposición de Archivos e Information Protection
- **Objetivo:** Detectar exposición pública o compartición externa indebida de archivos sensibles en nubes conectadas y gestionar violaciones DLP vigentes.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Files` y `Cloud apps > Policies > Policy management > Information protection` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / Compliance Data Admin.
- **Procedimiento paso a paso:**
  1. Responder diariamente las cuatro verificaciones recomendadas por Microsoft en **Cloud apps > Files**: (a) archivos compartidos públicamente accesibles sin enlace o con enlace anónimo, (b) dominios externos socios con compartición saliente activa, (c) archivos con nombres sensibles expuestos, y (d) archivos corporativos compartidos con cuentas personales (`gmail.com`, `outlook.com`, etc.) `[Verificado MS Learn]`.
  2. Revisar alertas activas de políticas de protección de información (y alertas correlacionadas desde **Microsoft Purview DLP** para las cargas ya migradas).
  3. Ejecutar acciones inmediatas de contención sobre exposiciones críticas: `Remove external users`, `Make private`, `Apply sensitivity label` o `Admin quarantine` `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de remediación sobre el archivo en `Governance log` / `Purview Activity explorer` y reducción de archivos públicos expuestos.

### D-07 — Verificación Rápida de Flujo de Telemetría e Ingesta (`CloudAppEvents`)
- **Objetivo:** Prevenir puntos ciegos silenciosos validando que los conectores API y el pipeline de Advanced Hunting reciben telemetría fresca en las últimas horas.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Hunting > Advanced hunting` y `System > Settings > Cloud apps > Connected apps > App Connectors` `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin / SOC L1.
- **Procedimiento paso a paso:**
  1. Ejecutar consulta de verificación de frescura sobre `CloudAppEvents` agrupando `max(Timestamp)` por `Application` `[Decisión / Propuesta Editorial]`.
  2. Confirmar que Microsoft 365 y las aplicaciones SaaS críticas registran eventos recientes acordes a su ventana de polling API y que no existen alertas del sistema por desconexión de conectores.
  3. Si un conector figura en estado `Error` o sin eventos por más de 4 horas, escalar inmediatamente a administración de plataforma para reautorización OAuth/token `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Resultado de consulta diaria de salud y bitácora de turno del SOC.

### D-08 — Gestión de Escalamiento, Documentación Estructurada y Handover de Turno
- **Objetivo:** Asegurar continuidad 24x7 sin incidentes huérfanos, manteniendo trazabilidad forense apta para auditoría y notificaciones ejecutivas oportunas.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L1 / SOC L2 / SOC Manager.
- **Procedimiento paso a paso:**
  1. Verificar al cierre de cada turno que el 100 % de los incidentes `High` y `Medium` con origen MDA tengan propietario asignado, etiquetas estandarizadas y comentarios auditables `[Decisión / Propuesta Editorial]`.
  2. Escalar a SOC L2/L3 e IAM cualquier caso con sospecha de *token replay*, *consent phishing* con alcance de administrador o exfiltración masiva activa.
  3. Ante incidentes críticos de negocio, emitir resumen ejecutivo bajo estructura **SBAR** (*Situation, Background, Assessment, Recommendation*) utilizando un canal fuera de banda validado si existe sospecha de compromiso en Exchange Online / Teams `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Acta de entrega de turno (*shift handover*), tickets ITSM sincronizados y registro en `Comments` del incidente.

---

## 6. Cadencia Operativa Semanal

> Basada en el **Microsoft Defender for Cloud Apps Weekly Operational Guide** oficial y prácticas avanzadas de postura, higiene OAuth y rutas de ataque `[Verificado MS Learn]`.

### S-01 — Revisión y Remediación de Postura SaaS (SSPM) en Microsoft Secure Score
- **Objetivo:** Identificar y corregir configuraciones inseguras en aplicaciones SaaS conectadas (Microsoft 365, Salesforce, ServiceNow, Okta, GitHub, AWS/GCP multi-instancia) antes de que sean explotadas.
- **Consola y ruta:** `https://security.microsoft.com > Exposure management > Secure Score > Recommended actions` (agrupar por `Product`) `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin / Cloud Security Architect.
- **Procedimiento:** Agrupar acciones recomendadas por producto seleccionando **Microsoft Defender for Cloud Apps** y aplicaciones SaaS conectadas; priorizar según puntaje de impacto, costo de implementación e impacto al usuario (teniendo en cuenta que desde marzo de 2026 ciertas recomendaciones de identidad en apps cloud se contabilizan bajo la categoría *Identity* de Secure Score) `[Verificado MS Learn]`; asignar tareas de remediación a los dueños técnicos de cada plataforma SaaS y verificar la subida de puntaje en la siguiente evaluación.
- **Evidencia auditable:** Exportación semanal de `Recommended actions` filtradas por MDA, tickets de cambio asignados e historial de evolución de Secure Score.

### S-02 — Chequeo Integral de Salud de App Connectors, Log Collectors, SIEM Agents y Tokens API
- **Objetivo:** Auditar preventivamente toda la tubería de recolección e integración para evitar interrupciones de descubrimiento Shadow IT o pérdida de alertas en SIEM.
- **Consola y ruta:** `https://security.microsoft.com > System > Settings > Cloud apps` `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin.
- **Procedimiento:** Verificar las cuatro rutas obligatorias documentadas en la guía semanal de Microsoft Learn `[Verificado MS Learn]`:
  1. `Connected apps > App Connectors`: estado saludable de cada instancia conectada y revisión de privilegios mínimos (ej. conector Workday actualizado en enero de 2026 para requerir únicamente permisos `View`).
  2. `Connected apps > Conditional Access App Control apps`: todas las apps en estado `Connected`.
  3. `Cloud Discovery > Automatic log upload`: colectores Docker/Syslog/FTP en estado `Receiving data` sin caídas de EPS.
  4. `System > API tokens` y `System > SIEM agents`: ausencia de tokens próximos a expirar o innecesarios, y flujo saludable hacia Microsoft Sentinel (conector Defender XDR) o SIEM externo.
- **Evidencia auditable:** Lista de chequeo semanal firmada con capturas o exportación de estado de conectores y registro de rotación de credenciales/tokens.

### S-03 — Auditoría del Governance Log y Control de Calidad de Acciones Automáticas
- **Objetivo:** Confirmar que todas las acciones automáticas y manuales de gobernanza (suspensión de usuario, revocación de app OAuth, bloqueo MDE, cuarentena, etiquetado) finalizaron con éxito y sin impacto indebido al negocio.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Governance log` `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin / Compliance Admin.
- **Procedimiento:** Filtrar los últimos 7 días por `Status = Failed` o `Error`; diagnosticar causas raíz (permisos insuficientes de la cuenta conectora, throttling de API Graph o bloqueo sobre archivo abierto) y re-ejecutar remediación `[Verificado MS Learn]`. Realizar muestreo de calidad sobre al menos 5 acciones automáticas ejecutadas (`Success`) para validar ausencia de falsos positivos disruptivos `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Exportación CSV del `Governance log` semanal y tickets de corrección de acciones fallidas.

### S-04 — Seguimiento de Cambios y Novedades en Message Center y What's New
- **Objetivo:** Anticipar cambios de producto, retiros de funcionalidades, ajustes de esquema KQL o nuevas detecciones antes de que impacten la operación del SOC.
- **Consola y ruta:** `https://admin.microsoft.com > Health > Message center` (filtro `Microsoft Defender for Cloud Apps`) y `https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes` `[Verificado MS Learn]`.
- **Rol responsable:** SaaS Security Admin / Cloud Security Architect.
- **Procedimiento:** Revisar todos los avisos etiquetados como *Plan for change* o *Prevent or fix issues*; evaluar el impacto sobre conectores (ej. mejoras en Salesforce Real-Time Event Monitoring), políticas (ej. retiro de File Policies el 6-ene-2027) o RBAC, y convertir cada cambio aplicable en tarea con responsable y fecha en el tablero de ingeniería del SOC `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro semanal en bitácora de ingeniería SOC vinculando ID de Message Center (`MCxxxxxx`) con tarea de adaptación creada.

### S-05 — Barrido Semanal de Higiene OAuth, Nuevos Grants y Rutas de Ataque (OAuth Attack Paths)
- **Objetivo:** Eliminar aplicaciones OAuth "zombies", sobre-privilegiadas o expuestas como puntos de estrangulamiento (*choke points*) en cadenas de compromiso lateral.
- **Consola y ruta:** `https://security.microsoft.com > Assets > Applications > OAuth apps` y `Exposure management > Attack surface > Attack paths` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 / IAM Admin / SaaS Security Admin.
- **Procedimiento:**
  1. En `Assets > Applications > OAuth apps`, revisar los *actionable insights* nativos: **New apps**, **Highly privileged apps**, **Unused apps** (sin actividad en 90 días, disponible también para Salesforce en preview) y **Apps from external unverified publishers** `[Verificado MS Learn]`.
  2. Revocar o deshabilitar aplicaciones de alto privilegio con uso comunitario raro y publisher no verificado que carezcan de aprobación formal `[Decisión / Propuesta Editorial]`.
  3. En `Exposure management > Attack paths` (y pestaña `Choke points`), filtrar por `Target type = AAD Service principal` / `Microsoft Entra OAuth app`, visualizar el *blast radius* (ej. endpoints con vulnerabilidades críticas donde reside credenciales/acceso a un Service Principal con permisos `Microsoft Graph`) y coordinar remediación dual (endpoint + reducción de permisos de la app) `[Verificado MS Learn]`.
- **Evidencia auditable:** Reporte semanal de apps OAuth revocadas/reducidas y reducción del conteo de Attack Paths activos hacia Service Principals críticos.

### S-06 — Revisión Semanal de Usuarios con Mayor Riesgo Acumulado (UEBA Top Risky Users)
- **Objetivo:** Detectar amenazas internas (*insider threats*) o compromisos silenciosos donde múltiples anomalías menores elevan el riesgo de una identidad sin haber disparado aún un incidente crítico aislado.
- **Consola y ruta:** `https://security.microsoft.com > Assets > Identities` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L2 / SOC L3 (Threat Hunter).
- **Procedimiento:** Ordenar identidades de forma descendente por **Investigation Priority Score**; inspeccionar el Top 10 de usuarios y cuentas de servicio (incluyendo cuentas SaaS integradas automáticamente al *Identity inventory* desde octubre de 2026) `[Verificado MS Learn]`; correlacionar con señales de Microsoft Purview Insider Risk Management y Entra ID Protection, abriendo caza focalizada en `CloudAppEvents` para cualquier usuario con score elevado sostenido durante 7 días `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Registro de revisión de Top 10 usuarios riesgosos y *bookmarks*/casos abiertos cuando corresponda.

---

## 7. Cadencia Operativa Mensual

> Basada en el **Microsoft Defender for Cloud Apps Monthly Operational Guide** oficial complementada con controles de gobierno SOC, auditoría administrativa y cobertura de licencias `[Verificado MS Learn]`.

### M-01 — Evaluación de Efectividad y Tuning de Políticas (Reducción de Falsos Positivos)
- **Objetivo:** Mantener alta relación señal/ruido en las detecciones CASB, eliminando fatiga de alertas y cubriendo nuevos patrones de ataque SaaS.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management` `[Verificado MS Learn]`.
- **Rol responsable:** SOC L3 / SaaS Security Admin.
- **Procedimiento:**
  1. Revisar métricas de verdaderos positivos (TP), benignos positivos (BTP) y falsos positivos (FP) por política; ajustar sensibilidad de detección de anomalías, grupos excluidos (ej. cuentas de simulación de ataque o escáneres autorizados) y actualizar rangos IP corporativos para evitar alertas espurias de *Impossible travel* `[Verificado MS Learn]`.
  2. Evaluar políticas con 0 coincidencias (verificar si el conector fuente sigue activo o el umbral es irreal) y políticas ruidosas (>1.000 coincidencias o >15 % FP `[Decisión / Propuesta Editorial]`), evaluando el nuevo interruptor `Generate alert for blocked app access` (Preview, mayo 2026) cuando las alertas informativas de bloqueo MDE generen ruido innecesario `[Verificado MS Learn]`.
  3. Limpiar alertas antiguas abiertas de los últimos 6 meses agrupando alertas similares, verificando la causa de no atención y ajustando la política subyacente antes de descartar las benignas `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de cambios de políticas en control de cambios y métrica mensual de tasa de FP antes/después del tuning.

### M-02 — Revisión Mensual de Patrones Repetitivos en Activity Log y Auditoría Administrativa ("Audit the Auditors")
- **Objetivo:** Descubrir comportamientos anómalos persistentes por entidad y verificar que el 100 % de las modificaciones administrativas en MDA cuenten con autorización formal.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Activity log` y `Permissions > Cloud Apps > Roles > Export admin activities` `[Verificado MS Learn]`.
- **Rol responsable:** SOC Manager / GRC / SaaS Security Admin.
- **Procedimiento:**
  1. Pivotar `Activity log` por tipo de actividad repetida de una misma entidad en los últimos 30 días (múltiples inicios de sesión fallidos, búsquedas masivas, asignación/borrado de privilegios) para crear nuevas políticas personalizadas de monitoreo `[Verificado MS Learn]`.
  2. Filtrar `Activity type = Administrative activity` y exportar el registro de actividad de administradores (`Export admin activities`) desde `Permissions > Cloud Apps > Roles` `[Verificado MS Learn]`.
  3. Cruzar toda acción crítica (`Disable policy`, `Edit policy`, `Unsanction/Sanction app`, `Dismiss alert`, `Add admin`, `Create API token`) contra tickets aprobados en Change Management; tratar cualquier cambio huérfano como incidente interno `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Archivo CSV exportado de `Export admin activities` firmado y conciliado contra tickets ITSM.

### M-03 — Revisión Mensual de Permisos RBAC, Alcance (`Scoped Deployment`) y Cobertura de Licencias
- **Objetivo:** Garantizar cumplimiento estricto de mínimo privilegio y asegurar que ningún grupo de nuevos empleados o subsidiarias quede excluido del monitoreo de MDA.
- **Consola y ruta:** `https://security.microsoft.com > Permissions > Microsoft Defender XDR > Roles` / `Permissions > Cloud Apps > Roles`, `System > Settings > Cloud apps > System > Scoped deployment` y `https://admin.microsoft.com > Billing > Licenses` `[Verificado MS Learn]`.
- **Rol responsable:** IAM Admin / SaaS Security Admin / GRC.
- **Procedimiento:** Auditar miembros con acceso administrativo directo o *overrides* manuales en MDA, revocando privilegios permanentes en favor de grupos elegibles en Entra PIM; revisar `Scoped deployment` confirmando que los grupos incluidos cubren el 100 % de la población licenciada (recordando que usuarios fuera del alcance configurado **no son monitoreados** por MDA) `[Verificado MS Learn]`.
- **Evidencia auditable:** Matriz mensual de usuarios privilegiados validada y captura de configuración de `Scoped deployment` vs. licencias asignadas.

### M-04 — Ejecución y Seguimiento del Plan de Migración de File Policies a Microsoft Purview
- **Objetivo:** Completar de forma ordenada, probada y sin brechas de protección la transición obligatoria de políticas de archivos de MDA antes de su retiro definitivo el **6 de enero de 2027**.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management > All policies > Migrate` y `https://purview.microsoft.com > Solutions > Data loss prevention > Policies` `[Verificado MS Learn]`.
- **Rol responsable:** Compliance Admin / SaaS Security Admin.
- **Procedimiento:**
  1. Inventariar las **File policies** restantes clasificadas por el asistente oficial en `Can migrate`, `Partial migration` y `Cannot migrate` `[Verificado MS Learn]`.
  2. Ejecutar la migración asistida (que crea las directivas `[Migrated] <nombre> (1P DLP)` en modo `Test with notifications` en Purview) y recrear manualmente en Purview Auto-labeling o Purview DLP para apps conectadas no-Microsoft (Box, Dropbox, Google Workspace, Salesforce — manteniendo activo el App Connector en MDA requerido por Purview) aquellas no cubiertas por la herramienta `[Verificado MS Learn]`.
  3. Validar paridad de coincidencias en modo simulación y **deshabilitar inmediatamente la File Policy original en MDA al activar enforcement en Purview** para impedir conflictos de coexistencia `[Verificado MS Learn]`.
- **Evidencia auditable:** Tabla de avance mensual de políticas migradas, validadas en simulación y dadas de baja controlada en MDA.

### M-05 — Reporte Ejecutivo Mensual de Shadow IT, Shadow AI y Postura SaaS al CISO
- **Objetivo:** Entregar visibilidad cuantitativa a la alta dirección sobre el riesgo del portafolio SaaS, adopción de IA generativa, postura SSPM y eficacia operativa del SOC.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Cloud discovery > Dashboard > Actions > Generate Cloud Discovery executive report` `[Verificado MS Learn]`.
- **Rol responsable:** SOC Manager / Compliance Admin.
- **Procedimiento:** Generar el **Cloud Discovery executive report** en PDF junto con la evolución mensual de Secure Score (pilar Apps/Identity), métricas de apps GenAI gobernadas, apps OAuth riesgosas revocadas y cumplimiento de SLA de incidentes CASB; presentar conclusiones y decisiones requeridas al comité del CISO `[Verificado MS Learn]`.
- **Evidencia auditable:** Reporte ejecutivo PDF archivado y minuta de decisiones del comité mensual de seguridad.

### M-06 — Validación End-to-End del Tejido de Integración y Automatizaciones (Playbooks)
- **Objetivo:** Comprobar que el bucle completo de detección a contención automática entre MDA, Entra ID, MDE, Purview, Sentinel y Power Automate / Logic Apps opera sin degradación.
- **Consola y ruta:** `https://security.microsoft.com > System > Settings > Cloud apps` y portal de Microsoft Sentinel / Power Automate `[Verificado MS Learn]`.
- **Rol responsable:** Cloud Security Architect / SOC L3.
- **Procedimiento:** Verificar estado activo de las integraciones críticas (MDE, Microsoft Purview Information Protection, Entra ID Protection, streaming a Microsoft Sentinel) y ejecutar una prueba controlada sobre un usuario/archivo de laboratorio para medir latencia real de alerta, sincronización de bloqueo URL en MDE y ejecución de playbook de respuesta `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Registro mensual de prueba sintética *end-to-end* con tiempos medidos.

---

## 8. Cadencias Trimestral, Semestral y Anual

> Estas actividades de gobierno estratégico extienden la guía operativa mensual de Microsoft Learn alineándola con **Microsoft Security Adoption Framework (SAF)**, **Zero Trust** y **NIST CSF 2.0** `[Decisión / Propuesta Editorial]`.

### T-01 (Trimestral) — Ejercicio Tabletop y Simulación Técnica de Incidente SaaS / OAuth
- **Objetivo:** Validar en condiciones realistas la coordinación entre SOC, IAM, Legal y dueños de aplicaciones frente a escenarios modernos de compromiso SaaS.
- **Consola y ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts` y entorno controlado de prueba `[Decisión / Propuesta Editorial]`.
- **Rol responsable:** SOC Manager / SOC L2 / IAM Admin / GRC.
- **Procedimiento:** Ejecutar un ejercicio trimestral rotando cuatro vectores críticos: (Q1) *Consent phishing* OAuth con acceso a Graph y reglas de reenvío ocultas, (Q2) robo de cookie de sesión AiTM seguido de descarga masiva en SharePoint/Salesforce, (Q3) infección de ransomware sincronizada vía cliente OneDrive, y (Q4) fuga de código fuente/PII hacia app de Shadow AI no sancionada; cronometrar MTTA y MTTC y actualizar runbooks con las brechas halladas.
- **Evidencia auditable:** Informe de resultados del ejercicio Tabletop/Purple Team y registro de actualización de playbooks.

### T-02 (Trimestral) — Calibración de Métricas de Score de Riesgo y Catálogo de Apps Personalizadas
- **Objetivo:** Alinear la ponderación de los >90 factores de riesgo del catálogo de MDA con el apetito de riesgo y marco regulatorio vigente de la organización (GDPR, PCI-DSS, HIPAA, ISO 27001, normativas locales).
- **Consola y ruta:** `https://security.microsoft.com > System > Settings > Cloud apps > Cloud Discovery > Score metrics` y `Cloud apps > Cloud app catalog` `[Verificado MS Learn]`.
- **Rol responsable:** Compliance Admin / Cloud Security Architect.
- **Procedimiento:** Revisar los pesos asignados a certificaciones regulatorias, soberanía de datos y cláusulas de entrenamiento de modelos IA; auditar sobrescrituras manuales de score (`Override risk score`) asegurando justificación vigente, y dar de alta como *Custom apps* aplicaciones web internas o regionales no presentes por defecto en el catálogo de >31.000 apps `[Verificado MS Learn]`.
- **Evidencia auditable:** Captura de configuración de `Score metrics` e inventario justificado de `Override risk scores`.

### SM-01 (Semestral) — Revisión Arquitectónica de Controles de Sesión, Edge for Business y Coexistencia Global Secure Access
- **Objetivo:** Optimizar la cobertura de controles preventivos inline eliminando fricción innecesaria de proxy inverso y cerrando brechas en clientes nativos o acceso web general.
- **Consola y ruta:** `https://security.microsoft.com > System > Settings > Cloud apps > Conditional Access App Control` y `https://entra.microsoft.com > Global Secure Access` `[Verificado MS Learn]`.
- **Rol responsable:** Cloud Security Architect / IAM Architect.
- **Procedimiento:** Evaluar la ampliación del enforcement de **In-browser protection con Microsoft Edge for Business** (`Enforce access from Edge when possible` o `Allow access only from Edge` en dispositivos no administrados), revisar políticas de bloqueo de clientes de escritorio no soportados (como Teams desktop en escenarios de restricción de descarga) y validar la arquitectura de defensa en profundidad junto con **Microsoft Entra Internet Access (Global Secure Access)** y **Microsoft Agent 365** `[Verificado MS Learn]`.
- **Evidencia auditable:** Documento de revisión arquitectónica semestral aprobado por Arquitectura de Seguridad e IAM.

### A-01 (Anual) — Auditoría Integral de Evidencias NIST CSF 2.0, Higiene de Datos Históricos y Recertificación SOC
- **Objetivo:** Consolidar el paquete anual de aseguramiento regulatorio, depurar datos obsoletos de descubrimiento cuando aplique y recertificar competencias técnicas del personal SecOps.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps` y `System > Settings > Cloud apps > Cloud Discovery > Delete data` `[Verificado MS Learn]`.
- **Rol responsable:** CISO Office / GRC Lead / SOC Manager.
- **Procedimiento:** Ejecutar autoevaluación anual de outcomes NIST CSF 2.0 soportados por MDA con paquete completo de evidencias de 12 meses; evaluar si se requiere depuración controlada de datos antiguos de carga manual en Cloud Discovery (`Delete data`) conforme a las recomendaciones ad-hoc de Microsoft; y verificar el cumplimiento del plan anual de formación y certificación (`SC-200`, `SC-300`, `SC-401`, `SC-100`) del equipo `[Decisión / Propuesta Editorial]`.
- **Evidencia auditable:** Informe anual de auditoría GRC / NIST CSF 2.0 y matriz de certificaciones vigentes del equipo SOC.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

> Basados en el **Microsoft Defender for Cloud Apps Ad-Hoc Operational Guide** oficial y en los playbooks de respuesta a incidentes de Microsoft Security Operations `[Verificado MS Learn]`.

### AH-01 — Playbook de Contención y Forense ante Aplicación OAuth Maliciosa / Consent Phishing
- **Disparador:** Alerta de alta severidad con `Detection source = App Governance` (ej. `App with suspicious OAuth scope made graph calls to read email and created inbox rule` o `OAuth App with suspicious Reply URL`) o hallazgo en hunting.
- **Consola y ruta:** `security.microsoft.com > Cloud apps > App governance`, `entra.microsoft.com > Enterprise applications` y `Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. **Triaje y alcance (<15 min):** Identificar `AppId`, `ServicePrincipalId`, publisher, tipo de consentimiento (`Admin` vs. `User`), scopes concedidos y lista completa de usuarios que consintieron.
  2. **Contención inmediata:** Ejecutar **Disable app** en App Governance (bloquea emisión y uso de tokens en Entra ID) y, si persisten sesiones comprometidas del usuario víctima, ejecutar `Revoke sign-in sessions` y restablecimiento de credenciales en Entra ID `[Verificado MS Learn]`.
  3. **Investigación forense:** Consultar `CloudAppEvents` filtrando por `OAuthAppId` y `ActionType` (`MailItemsAccessed`, `FileDownloaded`, `New-InboxRule`, `Set-InboxRule`, `Add member to role.`) en los últimos 30 días para cuantificar datos leídos o exfiltrados.
  4. **Erradicación y endurecimiento:** Eliminar reglas de reenvío de buzón maliciosas en Exchange Online, rotar secretos/certificados si se trató de una app interna comprometida y endurecer las políticas de consentimiento de usuario en `entra.microsoft.com > Enterprise applications > Consent and permissions` `[Verificado MS Learn]`.
- **Evidencia auditable:** Cronología forense exportada de `CloudAppEvents`, registro de deshabilitación de la app y acta post-incidente.

### AH-02 — Playbook de Respuesta ante Exfiltración Masiva de Datos en Sesión SaaS o Insider Threat
- **Disparador:** Alerta `Unusual multiple file download`, `Data exfiltration to unsanctioned apps` o escalamiento desde Microsoft Purview Insider Risk Management.
- **Consola y ruta:** `security.microsoft.com > Incidents & alerts`, `Cloud apps > Activity log` y `entra.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. **Verificación contextual:** Cruzar en `CloudAppEvents` volumen descargado por hora, sensibilidad de etiquetas (`SensitivityLabelId`), IP/ISP origen, `DeviceType` e indicadores de desvinculación laboral (con autorización de Legal/RR. HH.).
  2. **Contención quirúrgica o total:** Para riesgo moderado/en investigación, incluir al usuario en grupo dinámico sujeto a política CAAC de emergencia (`Block download` y `Block cut/copy/print`); para exfiltración maliciosa confirmada, ejecutar **Suspend user** / bloqueo de inicio de sesión y revocación de sesiones en Entra ID `[Verificado MS Learn]`.
  3. **Contención de canales externos:** Si la subida ocurrió hacia una app SaaS no autorizada, marcar inmediatamente la app como **Unsanctioned** para propagar bloqueo de red a todos los endpoints MDE; revocar enlaces externos creados sobre archivos corporativos (`Remove external users` / `Make private`).
  4. **Preservación legal:** Exportar registros íntegros de `Activity log` y `CloudAppEvents` bajo cadena de custodia y coordinar *Legal Hold* en Microsoft Purview eDiscovery si aplica.
- **Evidencia auditable:** Paquete de evidencias exportado, registro en `Governance log` y reporte RCA.

### AH-03 — Respuesta de Emergencia ante Vulnerabilidad Zero-Day o Brecha en Proveedor SaaS Tercero
- **Disparador:** Boletín de inteligencia de amenazas (MSRC, CISA KEV, vendor advisory) reportando explotación activa en una aplicación SaaS o librería crítica utilizada por terceros.
- **Consola y ruta:** `security.microsoft.com > Cloud apps > Cloud discovery > Discovered apps`, `Assets > Applications` y `Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. **Evaluación de radio de impacto (*blast radius*):** Buscar la aplicación afectada en `Discovered apps` y ejecutar consulta KQL sobre `CloudAppEvents` y `DeviceNetworkEvents` para listar todos los usuarios, endpoints, direcciones IP y volúmenes de datos intercambiados en los últimos 7–30 días.
  2. **Contención preventiva:** Si la app no es crítica o carece de mitigación del fabricante, etiquetarla temporalmente como **Unsanctioned** para bloqueo inmediato vía MDE; si es una app corporativa crítica conectada a Entra ID, aplicar política CAAC de emergencia restringiendo acceso solo a dispositivos administrados cumplidores y bloqueando descargas.
  3. **Ingesta de IOCs:** Registrar rangos IP o indicadores asociados al incidente del proveedor en `System > Settings > Cloud apps > System > IP address ranges` con categoría de riesgo y crear política de actividad de bloqueo/alerta `[Verificado MS Learn]`.
  4. **Retorno controlado:** Mantener el control compensatorio hasta confirmar remediación oficial del proveedor y rotación de tokens API/OAuth involucrados.
- **Evidencia auditable:** Reporte de *blast radius* KQL, cambio de estado de la app y notificación a dueños de negocio.

### AH-04 — Gestión y Resolución Forense de Archivos en Cuarentena Administrativa (`Admin Quarantine`)
- **Disparador:** Archivo retenido en cuarentena administrativa por detección de malware con Microsoft Threat Intelligence o violación severa de política de información, o hallazgo de auditoría de cumplimiento.
- **Consola y ruta:** `https://security.microsoft.com > Cloud apps > Files` (filtro `Quarantined = True`) o sitio de cuarentena controlada de Microsoft Purview DLP `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Verificar en **Microsoft 365 Service health** (`admin.microsoft.com > Health > Service health`) que no exista degradación conocida del servicio antes de diagnosticar anomalías operativas `[Verificado MS Learn]`.
  2. Filtrar archivos en cuarentena administrativa y revisar metadatos, propietario, colaboradores previos y alerta origen sin abrir artefactos sospechosos fuera de un entorno sandbox aislado.
  3. Si se trató de malware, pivotar en Defender XDR para investigar el endpoint y la identidad que subió el archivo; eliminar definitivamente o mantener aislado según retención legal.
  4. Si se valida falso positivo con aprobación escrita de Compliance/Data Owner, restaurar desde cuarentena aplicando etiqueta de sensibilidad adecuada y ajustar la política en Purview DLP `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de revisión de cuarentena, aprobación del Data Owner y trazabilidad en `Governance log`.

### AH-05 — Contención de Abuso o Inyección de Prompts en Agentes de Copilot Studio Conectados
- **Disparador:** Alerta informativa/bloqueo de invocación de herramienta en tiempo real en Defender XDR o detección de actividad anómala de agente conectado a datos corporativos.
- **Consola y ruta:** `https://security.microsoft.com > Incidents & alerts`, `Hunting > Advanced hunting` (`BehaviorInfo` / `AgentsInfo` con Agent 365 o `CloudAppEvents`) y centro de administración de Power Platform `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Verificar el evento bloqueado o alertado identificando el agente involucrado, el usuario invocador, la herramienta/conector invocado y los recursos accedidos.
  2. Auditar si el agente utiliza credenciales privilegiadas del *maker* en lugar de la identidad del usuario final y revisar sus conectores activos.
  3. Coordinar con el Power Platform Administrator / AI Administrator la puesta en cuarentena o desactivación del agente afectado y revocar conexiones OAuth comprometidas.
  4. Nota de alcance licenciatario: verificar disponibilidad de **Microsoft Agent 365** para acceso completo a inventario `AgentsInfo` y reglas unificadas en `Settings > Security for AI > Policies & rules > Real-time protection` vigentes desde el 1 de julio de 2026 `[Verificado MS Learn]`.
- **Evidencia auditable:** Registro de bloqueo/alerta en Defender XDR y cambio de estado del agente en Power Platform / Agent Registry.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Esquema y Prerrequisitos de la Tabla `CloudAppEvents`

La tabla `CloudAppEvents` en **Advanced Hunting** (`security.microsoft.com > Investigation & response > Hunting > Advanced hunting`) consolida eventos enriquecidos de cuentas y objetos en Microsoft 365 y todas las aplicaciones SaaS conectadas a Defender for Cloud Apps `[Verificado MS Learn]`. Campos clave para el SOC:
- `Timestamp`, `ActionType`, `ActivityType`, `Application`, `ApplicationId`, `AppInstanceId`.
- `AccountObjectId`, `AccountId`, `AccountDisplayName`, `AccountType`, `IsAdminOperation`, `IsExternalUser`, `IsImpersonated`.
- `IPAddress`, `IPCategory`, `IPTags`, `IsAnonymousProxy`, `CountryCode`, `City`, `Isp`, `DeviceType`, `OSPlatform`, `UserAgent`, `UserAgentTags`.
- `AuditSource` (`Defender for Cloud Apps access control`, `Defender for Cloud Apps session control`, `Defender for Cloud Apps app connector`), `SessionData`, `OAuthAppId`.
- `LastSeenForUser` y `UncommonForUser` (enriquecimiento UEBA nativo para descartar falsos positivos y cazar anomalías), `ActivityObjects` y `RawEventData` `[Verificado MS Learn]`.

### 10.2 Catálogo de Consultas KQL Operativas y de Verificación ("Proof of Life")

#### Consulta 1 — Health Check Diario de Ingesta SaaS por Aplicación Conectada `[Verificado MS Learn]`
```kql
// Verifica frescura de telemetría en CloudAppEvents por aplicación y origen de auditoría
CloudAppEvents
| where Timestamp > ago(24h)
| summarize Eventos24h = count(), UltimoEventoUTC = max(Timestamp) by Application, AuditSource
| extend MinutosSinDatos = datetime_diff('minute', now(), UltimoEventoUTC)
| order by MinutosSinDatos asc
```

#### Consulta 2 — Detección de Exfiltración: Picos de Descarga de Archivos y Sensibilidad `[Verificado MS Learn]`
```kql
// Basada en la consulta oficial del Ad-Hoc Ops Guide enriquecida con conteo horario
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType == "FileDownloaded"
| extend FileName = tostring(RawEventData.SourceFileName),
         SiteUrl = tostring(RawEventData.SiteUrl),
         FileLabel = tostring(RawEventData.SensitivityLabelId)
| summarize DescargasHora = count(), ArchivosUnicos = dcount(FileName), MuestraArchivos = make_set(FileName, 10)
    by AccountDisplayName, AccountObjectId, Application, IPAddress, IsExternalUser, FileLabel, bin(Timestamp, 1h)
| where DescargasHora >= 50 or IsExternalUser == true
| order by DescargasHora desc
```

#### Consulta 3 — Auditoría de Consentimientos OAuth y Aplicaciones Recién Autorizadas `[Verificado MS Learn]`
```kql
// Identifica otorgamientos de consentimiento a aplicaciones OAuth y quién los ejecutó
CloudAppEvents
| where Timestamp > ago(14d)
| where ActionType == "Consent to application"
| extend TargetAppId = coalesce(OAuthAppId, tostring(RawEventData.AppId)),
         ConsentAction = tostring(RawEventData.ResultStatus)
| project Timestamp, AccountDisplayName, AccountObjectId, IsAdminOperation, TargetAppId, IPAddress, CountryCode, RawEventData
| order by Timestamp desc
```

#### Consulta 4 — Escalamiento de Privilegios en Directorio (`Add member to role.`) `[Verificado MS Learn]`
```kql
// Consulta oficial del Ad-Hoc Operational Guide de Defender for Cloud Apps
CloudAppEvents
| where Timestamp > ago(30d)
| where ActionType in ("Add member to role.")
| extend FirstElement = ActivityObjects[0], SecondElement = ActivityObjects[1]
| extend Type = tostring(FirstElement.ServiceObjectType),
         RoleName = tostring(FirstElement.Name),
         UserAddedName = tostring(SecondElement.Name),
         UserAddedId = tostring(SecondElement.Id)
| project Timestamp, Type, ActionType, RoleName, UserAddedName, UserAddedId, AccountId, AccountDisplayName, IPAddress
| order by Timestamp desc
```

#### Consulta 5 — Investigación Forense de `MailItemsAccessed` Cruzado con `EmailEvents` `[Verificado MS Learn]`
```kql
// Consulta oficial del Ad-Hoc Operational Guide para auditar mensajes accedidos por sesión/OAuth sospechosa
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType == "MailItemsAccessed"
| extend Folders = RawEventData.Folders[0]
| extend MailboxPath = tostring(Folders.Path)
| mv-expand Folders.FolderItems
| extend MessageIDs = tostring(Folders_FolderItems.InternetMessageId)
| join kind=inner (EmailEvents | where Timestamp > ago(14d)) on $left.MessageIDs == $right.InternetMessageId
| project Timestamp, AccountType, AccountDisplayName, AccountObjectId, OAuthAppId, UserAgent, IPAddress, CountryCode, City, MailboxPath, Subject, SenderFromAddress, RecipientEmailAddress
| sort by Timestamp desc
```

#### Consulta 6 — Monitoreo de Controles en Tiempo Real de CAAC (Accesos y Sesiones Bloqueadas) `[Verificado MS Learn]`
```kql
// Audita la efectividad de políticas inline de acceso y sesión (Reverse Proxy y Edge for Business)
CloudAppEvents
| where Timestamp > ago(7d)
| where AuditSource in ("Defender for Cloud Apps session control", "Defender for Cloud Apps access control")
| summarize TotalEventos = count(), UsuariosUnicos = dcount(AccountObjectId)
    by AuditSource, Application, ActionType, DeviceType, OSPlatform
| order by TotalEventos desc
```

#### Consulta 7 — Caza de OAuth Apps Críticas en el Grafo de Exposición (`ExposureGraphNodes` / `ExposureGraphEdges`) `[Verificado MS Learn]`
```kql
// Identifica aplicaciones OAuth / Service Principals con permisos sobre Microsoft Graph y alta criticidad
let RelevantNodes = ExposureGraphNodes
| where NodeLabel == "Microsoft Entra OAuth App" or NodeLabel == "serviceprincipal"
| project NodeId, NodeLabel, NodeName, NodeProperties;
ExposureGraphEdges
| where EdgeLabel == "has permissions to" or EdgeLabel == "can authenticate as"
| make-graph SourceNodeId --> TargetNodeId with RelevantNodes on NodeId
| graph-match (AppRegistration)-[canAuthAs]->(SPN)-[hasPermissionTo]->(Target)
    where AppRegistration.NodeLabel == "Microsoft Entra OAuth App"
      and canAuthAs.EdgeLabel == "can authenticate as"
      and SPN.NodeLabel == "serviceprincipal"
      and SPN.NodeProperties["rawData"]["criticalityLevel"]["criticalityLevel"] == 0
      and hasPermissionTo.EdgeLabel == @"has permissions to"
      and Target.NodeLabel == "Microsoft Entra OAuth App"
      and Target.NodeName == "Microsoft Graph"
| project DisplayName = SPN.NodeProperties["rawData"]["accountDisplayName"],
          Enabled = SPN.NodeProperties["rawData"]["accountEnabled"],
          AppPermissions = hasPermissionTo.EdgeProperties["rawData"]["applicationPermissions"]["permissions"]
```

### 10.3 Mecanismos de Verificación de Uso Efectivo M365 E5 (Auditoría "Proof of Life")

| Capacidad E5 Evaluada | Ruta de Verificación en Consola | Evidencia Inequívoca de Operación Activa ("Proof of Life") | Etiqueta |
|---|---|---|---|
| **Cloud Discovery & MDE Sync** | `Cloud apps > Cloud discovery > Dashboard` | Tráfico actualizado en las últimas 24 h bajo *Defender-managed endpoints* y aplicaciones etiquetadas `Sanctioned` / `Unsanctioned`. | `[Verificado MS Learn]` |
| **Conditional Access App Control** | `Cloud apps > Activity log` (filtro `Source = Session control`) | Eventos continuos de sesión inspeccionada/bloqueada y políticas CA con control de sesión en estado `On` en Entra ID. | `[Verificado MS Learn]` |
| **Edge In-Browser Protection** | `System > Settings > Cloud apps > CAAC > Edge for Business protection` | Interruptor activo y sesiones en perfil corporativo de Edge mostrando candado + maletín sin sufijo `.mcas.ms`. | `[Verificado MS Learn]` |
| **App Governance** | `Cloud apps > App governance > Overview` | Métricas pobladas de apps OAuth en Entra/Google/Salesforce y políticas de App Governance en estado `Enabled`. | `[Verificado MS Learn]` |
| **SSPM en Secure Score** | `Exposure management > Secure Score > Recommended actions` | Recomendaciones visibles agrupadas bajo `Microsoft Defender for Cloud Apps` con historial de variación de puntaje. | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operativos, de Postura y de Gobierno

> Microsoft documenta las métricas de triaje, resolución, Secure Score y riesgo de aplicaciones; los umbrales numéricos objetivo que siguen constituyen **metas referenciales consultivas** que cada CISO debe calibrar según dotación y criticidad del negocio `[Decisión / Propuesta Editorial]`.

| ID | Indicador (KPI) | Definición Ejecutiva | Fórmula de Medición | Meta Sugerida | Frecuencia | Audiencia | Naturaleza |
|---|---|---|---|---|---|---|---|
| **KPI-01** | **Tiempo Medio de Reconocimiento CASB (MTTA-CASB)** | Velocidad desde la generación de un incidente High/Medium con fuente MDA hasta la asignación e inicio de triaje activo. | `Promedio(Timestamp_InProgress - Timestamp_Created)` | `< 15 min` (High) / `< 60 min` (Medium) | Diaria / Semanal | SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tiempo Medio de Contención SaaS / OAuth (MTTC-SaaS)** | Tiempo transcurrido desde la detección de un compromiso confirmado SaaS/OAuth hasta la revocación de app, suspensión de cuenta o bloqueo CAAC. | `Promedio(Timestamp_Contencion_GovernanceLog - Timestamp_Created)` | `< 30 min` (Crítico/High) | Semanal | SOC Manager / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Falsos Positivos en Políticas MDA (FPR)** | Proporción de alertas originadas por políticas de MDA cerradas como `False Positive` respecto al total clasificado en el mes. | `(Alertas_FP / Total_Alertas_Clasificadas) * 100` | `< 15 %` | Mensual | SOC L3 / SaaS Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Exposición de Aplicaciones GenAI sin Clasificar** | Número de aplicaciones de la categoría `Generative AI` descubiertas con tráfico activo que carecen de etiqueta formal (`Sanctioned` / `Unsanctioned`). | `Conteo(DiscoveredApps where Category == 'Generative AI' and Tag == 'Untagged')` | `0 apps` con tráfico > 10 MB sin clasificar | Semanal | CISO / GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Higiene de Aplicaciones OAuth de Alto Privilegio** | Cantidad de aplicaciones OAuth con nivel de privilegio `High` y publisher `Unverified` o sin uso en >90 días pendientes de revisión/revocación. | `Conteo(OAuthApps where Privilege == 'High' and (Publisher == 'Unverified' or Unused90d == true) and Unreviewed)` | `0 apps` sin revisión > 7 días | Semanal | IAM Lead / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Remediación SSPM SaaS** | Porcentaje de recomendaciones de postura SSPM publicadas por MDA en Microsoft Secure Score implementadas dentro del ciclo mensual. | `(Recomendaciones_Completadas / Total_Recomendaciones_MDA_Elegibles) * 100` | `>= 75 %` (controles críticos) | Mensual | Cloud Security Architect | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Disponibilidad de Conectores API y Colectores** | Porcentaje de conectores SaaS, apps CAAC y colectores de logs operando en estado `Connected` / `Receiving data` sin fallos mayores a 4 h. | `(Conectores_Saludables / Total_Conectores_Produccion) * 100` | `>= 99,5 %` | Semanal | SaaS Security Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Avance de Migración File Policies a Purview** | Porcentaje de File Policies históricas de MDA migradas, validadas en simulación en Microsoft Purview y dadas de baja en MDA antes del retiro del 6-ene-2027. | `(FilePolicies_Migradas_Y_Deshabilitadas / Total_FilePolicies_Inventario) * 100` | `100 %` antes de `2026-12-15` | Mensual | Compliance Lead / CISO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional CASB & SaaS Security (Niveles 1 a 5)

| Nivel | Estadio | Características Operativas Verificables `[Decisión / Propuesta Editorial]` |
|---|---|---|
| **Nivel 1** | **Inicial / Ad-Hoc** | Licencia E5 asignada sin operación estructurada; conectores desconectados o limitados a M365 básico; sin rangos IP definidos ni revisión de Shadow IT o OAuth. |
| **Nivel 2** | **Visibilidad Base** | Cloud Discovery activo vía MDE; conectores API en apps principales; triaje reactivo de incidentes High en Defender XDR; inventario inicial de apps GenAI y OAuth. |
| **Nivel 3** | **Gobierno Estandarizado** | Cadencias diaria, semanal y mensual ejecutadas con evidencia; etiquetado Sanctioned/Unsanctioned con bloqueo automático MDE; rangos IP y tuning UEBA (<15 % FP); URBAC + PIM activos; migración de File Policies a Purview en curso. |
| **Nivel 4** | **Control Preventivo Inline** | CAAC e **In-browser protection con Edge for Business** protegiendo sesiones en dispositivos no administrados y externos; remediación continua de SSPM y *OAuth Attack Paths*; ejercicios Tabletop trimestrales. |
| **Nivel 5** | **Optimizado y Adaptativo** | Automatización SOAR end-to-end (Sentinel + Logic Apps), higiene continua *zero-standing OAuth bloat*, gobernanza convergente con Entra Global Secure Access y Agent 365, y auditoría continua NIST CSF 2.0 reproducible por KQL. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

### 12.1 Principio Rector de Auditoría

Conforme a **NIST CSWP 29 (febrero de 2024)**, NIST CSF 2.0 es un marco basado en resultados (*outcomes*), no un listado prescriptivo de herramientas. **Defender for Cloud Apps no "cumple" por sí solo el marco; provee evidencia técnica, continua y verificable** que demuestra la consecución de los outcomes definidos en cada subcategoría `[Decisión / Propuesta Editorial]`. Nota: en CSF 2.0 el antiguo dominio `PR.AC` (CSF 1.1) fue reemplazado oficialmente por **`PR.AA`** (*Identity Management, Authentication, and Access Control*).

### 12.2 Matriz de Auditoría NIST CSF 2.0 (`Function -> Category -> Subcategory -> Evidence`)

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome CSWP 29) | Capacidad Habilitadora en Defender for Cloud Apps | Evidencia Concreta Auditable | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales —incluyendo privacidad— son comprendidos y gestionados. | Cloud Discovery + App Catalog (>90 factores de riesgo regulatorios: GDPR, SOC 2, ISO 27001, HIPAA, propiedad de datos) y reportes ejecutivos. | Exportación PDF del *Cloud Discovery Executive Report* y matriz de evaluación regulatoria del portafolio SaaS/GenAI. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.PO-01` | La política de gestión de riesgos de ciberseguridad se establece, comunica y hace cumplir. | Motor de políticas de descubrimiento (Sanction/Unsanction + bloqueo MDE), políticas de acceso/sesión CAAC y políticas de App Governance. | Inventario exportado de políticas habilitadas y registros de enforcement efectivo en `Governance log`. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad se establecen, comunican y hacen cumplir. | Microsoft Defender Unified RBAC (URBAC), segregación de roles en `Permissions > Cloud Apps > Roles` y elegibilidad JIT en Entra PIM. | Exportación `Export admin activities`, matriz RACI firmada y reporte mensual "Audit the Auditors" (M-02/M-03). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-02` | Se mantienen inventarios de software, servicios y sistemas gestionados por la organización. | `Assets > Applications` (pestañas *SaaS apps* y *OAuth apps*) + integración continua con *Defender-managed endpoints*. | Exportación CSV de aplicaciones SaaS descubiertas y aplicaciones OAuth registradas en Entra ID, Google y Salesforce. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` / `ID.RA-05` | Se identifican vulnerabilidades/configuraciones débiles y se prioriza la respuesta según riesgo inherente. | SSPM integrado en Microsoft Secure Score, scoring 0–10 de apps SaaS y modelado de **OAuth Attack Paths** en Exposure Management. | Historial de puntaje SSPM en Secure Score y reporte semanal de cierre de *choke points* OAuth (S-01 / S-05). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos y autorizaciones se gestionan y aplican bajo mínimo privilegio y separación de funciones. | Conditional Access App Control (acceso adaptativo por postura de dispositivo/riesgo) y revocación de permisos OAuth no usados en App Governance. | Políticas CA en estado `On` enrutando a MDA, logs de acceso controlado y registro de revocación de apps OAuth sobre-privilegiadas. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` / `PR.DS-02` | La confidencialidad, integridad y disponibilidad de datos en reposo y en tránsito están protegidas. | Controles de sesión CAAC e **In-browser protection con Edge for Business** (bloqueo de descarga/copia/impresión, *protect-on-download* con etiquetas Purview, escaneo antimalware) + migración de datos en reposo a Purview DLP. | Eventos de sesión bloqueada/protegida en `CloudAppEvents` (`AuditSource == 'Defender for Cloud Apps session control'`) y políticas Purview DLP activas. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-03` / `DE.CM-06` | La actividad del personal, el uso tecnológico y los servicios de proveedores externos se monitorean continuamente. | Motor UEBA, políticas de detección de anomalías, monitoreo ML de App Governance sobre llamadas a Graph/Salesforce/Google y tabla `CloudAppEvents`. | Políticas de detección activas con coincidencias verificadas, alertas con `Detection source = App Governance` y consultas KQL programadas. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` / `DE.AE-03` | Los eventos adversos se analizan y correlacionan desde múltiples fuentes para comprender la cadena de ataque. | Correlación nativa en incidentes de Microsoft Defender XDR (*Attack story*) uniendo señales de SaaS, identidad, endpoint y correo. | Expedientes de incidentes XDR con múltiples fuentes correlacionadas y enriquecimiento UEBA (`UncommonForUser`). | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MA-02` / `RS.MI-01` | Los reportes de incidentes son triados/validados y los incidentes son contenidos oportunamente. | Triaje diario XDR (D-01) y acciones nativas de contención (`Suspend user`, `Disable/Revoke OAuth app`, `Tag as Unsanctioned`, `Admin quarantine`). | Tiempos MTTA/MTTC medidos, entradas en `Governance log` con `Status = Success` y tickets ITSM asociados. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-06` | Se declara el fin de la recuperación con base en criterios y se completa la documentación post-incidente y mejoras. | Contribución evidencial y analítica (MDA no restaura backups de infraestructura): reconstrucción forense completa en `Activity log` / `CloudAppEvents` y ajuste post-incidente de políticas. | Informe post-mortem (RCA) sustentado en logs de MDA y tickets de cambios preventivos aplicados tras el incidente o ejercicio Tabletop (T-01). | `[Decisión / Propuesta Editorial]` |

### 12.3 Cobertura de Tácticas y Técnicas MITRE ATT&CK Enterprise v18

| Táctica MITRE ATT&CK | Técnicas Principales Cubiertas | Mecanismo de Detección / Contención en MDA | Etiqueta |
|---|---|---|---|
| **Initial Access (`TA0001`)** | `T1078.004` (Cloud Accounts), `T1566` / Phishing de consentimiento OAuth | Anomalías de inicio de sesión SaaS, `Impossible travel`, alertas de App Governance sobre Reply URLs sospechosas y consentimientos anómalos. | `[Verificado MS Learn]` |
| **Persistence (`TA0003`) & Privilege Escalation (`TA0004`)** | `T1098.001` (Additional Cloud Credentials), `T1098.003` (Additional Cloud Roles), `T1528` (Steal Application Access Token) | Detección de adición de credenciales/certificados a apps OAuth seguida de llamadas anómalas, adición a roles privilegiados y monitoreo de abuso de tokens. | `[Verificado MS Learn]` |
| **Collection (`TA0009`)** | `T1114.002` (Remote Email Collection), `T1213` (Data from Information Repositories), `T1530` (Data from Cloud Storage) | Auditoría de `MailItemsAccessed`, descargas masivas anómalas en SharePoint/OneDrive/Box/Salesforce y actividad inusual de apps privilegiadas en Teams/Graph. | `[Verificado MS Learn]` |
| **Exfiltration (`TA0010`)** | `T1567` (Exfiltration Over Web Service), reglas de reenvío externo | Políticas `Data exfiltration to unsanctioned apps`, bloqueo inline de descarga/copia en CAAC / Edge for Business y bloqueo MDE de apps no sancionadas. | `[Verificado MS Learn]` |
| **Impact (`TA0040`)** | `T1486` (Data Encrypted for Impact), `T1496` (Resource Hijacking) | Política `Ransomware activity` sobre sincronización de archivos cifrados en la nube y alerta de App Governance por creación anómala de VMs desde apps OAuth. | `[Verificado MS Learn]` |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps / Admin / GRC)

| Perfil / Rol Objetivo | Competencias Críticas a Desarrollar | Recursos Oficiales y Credenciales Recomendadas | Meta de Habilitación |
|---|---|---|---|
| **SOC L1 (Monitor / Operator)** | Navegación en `security.microsoft.com > Cloud apps`, triaje de incidentes XDR con señales CASB, análisis inicial de `Impossible travel`, lectura de `Cloud discovery dashboard` y `Activity log`. | Ruta oficial de aprendizaje SC-200 en Microsoft Learn, *MDCA Daily Operational Guide* y *Microsoft Defender XDR Ninja Training*. Certificación: **Microsoft Certified: Security Operations Analyst Associate (SC-200)**. | Completar en primeros 30 días de incorporación `[Decisión / Propuesta Editorial]`. |
| **SOC L2 / L3 (Incident Responder & Threat Hunter)** | Consultas KQL avanzadas sobre `CloudAppEvents`, `OAuthAppInfo`, `ExposureGraphNodes`/`Edges`; respuesta forense a *consent phishing*, tuning UEBA y análisis de *OAuth Attack Paths*. | *App Governance Threat Detection Alerts*, *Defender XDR Advanced Hunting*, repositorios KQL comunitarios verificados (Bert-Jan Pals) y *SC-200* + **SC-300** (*Identity and Access Administrator Associate*). | Completar en 60–90 días + 1 Tabletop trimestral `[Decisión / Propuesta Editorial]`. |
| **SaaS Security Admin & Architect** | Onboarding de App Connectors y colectores Docker/SWG, despliegue de CAAC (Entra/SAML/OIDC) e **In-browser protection con Edge for Business**, URBAC, SSPM y coexistencia con Global Secure Access y Agent 365. | *Defender for Cloud Apps Ninja Training*, guía de despliegue Zero Trust para Aplicaciones y certificaciones **SC-300** + **SC-100** (*Cybersecurity Architect Expert*). | Recertificación anual y revisión mensual de *What's new* `[Decisión / Propuesta Editorial]`. |
| **Compliance, DLP & GRC Lead** | Clasificación regulatoria del catálogo SaaS/GenAI, ejecución del asistente **DLP to Purview migration** (<06-ene-2027), gestión de cuarentenas y recolección de evidencias NIST CSF 2.0. | Guía oficial *Migrate file policies to Microsoft Purview*, rutas de protección de IA y datos en Purview y certificación **SC-401** (*Administering Information Security in Microsoft 365*) / **AB-900**. | Antes de ejecutar migración productiva de File Policies `[Decisión / Propuesta Editorial]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos Verificados y Correcciones Aplicadas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Técnica Revalidada | Hallazgo Oficial en Microsoft Learn (Noviembre 2026) | Impacto Aplicado en esta Guía Maestra |
|---|---|---|---|
| 1 | **Retiro de File Policies en MDA** | Microsoft anunció (junio 2026) el retiro definitivo de **File Policies** en Defender for Cloud Apps el **6 de enero de 2027**, proveyendo el asistente **DLP to Purview migration** (`Cloud apps > Policies > Policy management > All policies > Migrate`) hacia Microsoft Purview DLP y Auto-labeling, advirtiendo que ambas políticas no pueden coexistir activas simultáneamente. | Se incorporó la tarea mensual crítica **M-04**, el **KPI-08** y las advertencias arquitectónicas de no coexistencia, reemplazando recomendaciones heredadas de crear nuevas File Policies permanentes en MDA. |
| 2 | **Transición de Agentes de IA hacia Microsoft Agent 365** | Desde el **1 de julio de 2026**, el descubrimiento, postura, detección de amenazas e inventario en Advanced Hunting de agentes de **Copilot Studio** y **Microsoft Foundry** exigen licencia **Microsoft Agent 365** (o M365 E7), depreciando `AIAgentsInfo` en favor de `AgentsInfo` y moviendo alertas de reglas runtime a `BehaviorInfo` (manteniendo sin cambios únicamente la protección runtime previa de Copilot Studio vía MDA para tenants que ya la usaban). | Se corrigió la sección de agentes de IA (que en borradores de marzo 2026 figuraba como preview incluida en MDA con `AIAgentsInfo`), delimitando con precisión la frontera con el módulo `22_Microsoft_Agent_365`. |
| 3 | **Unified RBAC (URBAC) por defecto y baja de roles heredados** | Desde **agosto de 2026**, **Microsoft Defender Unified RBAC** viene habilitado automáticamente para nuevos clientes de MDA. Los roles `App/instance admin`, `User group admin`, `Cloud Discovery global admin` y `Cloud Discovery report admin` ya no admiten nuevas asignaciones; y las vistas de App Governance se rigen exclusivamente por roles de Entra ID (salvo `OAuthAppInfo`). | Se actualizó íntegramente la Sección 4 (RBAC), rutas de consola (`Permissions > Cloud Apps > Roles` y URBAC) y revisión mensual **M-03**. |
| 4 | **Integración automática con Identity Inventory y mejoras OAuth/MDE 2026** | Desde el **15 de octubre de 2026**, la integración de cuentas SaaS de MDA con *Identity inventory* pasó a habilitación automática; en junio de 2026 se sumó **Salesforce Real-Time Event Monitoring** y soporte de Connected Apps / ECAs en App Governance (Preview); y en mayo de 2026 se añadió el toggle para suprimir alertas informativas de bloqueo MDE. | Incorporado en prerrequisitos (Sección 2.3), arquitectura (Sección 3.2) y procedimientos de tuning (M-01 y S-05). |
| 5 | **Consolidación de consolas y nombres vigentes de suites** | Redirección obligatoria irreversible desde `portal.cloudappsecurity.com` hacia `https://security.microsoft.com` activa para todos los clientes; adopción en Service Descriptions de **Microsoft Defender Suite** y **Microsoft Purview Suite** (`purview.microsoft.com` en lugar de `compliance.microsoft.com`), y catálogo con **>1.000 apps Generative AI** dentro de **>31.000 apps**. | Todas las rutas de consola, URLs canónicas (`/defender-cloud-apps/` sin el prefijo obsoleto `/microsoft-365/security/defender-cloud-apps/`) y tablas de licenciamiento fueron normalizadas. |
| 6 | **Corrección taxonómica NIST CSF 2.0** | Borradores previos mezclaban el código `PR.AC` (perteneciente a CSF 1.1) y omitían la numeración oficial de las 106 subcategorías de **NIST CSWP 29**. | Se normalizó todo el mapeo de la Sección 12 y del contrato JSON a códigos oficiales **NIST CSF 2.0** (`PR.AA-05`, `GV.OC-03`, `GV.PO-01`, `GV.RR-02`, `ID.AM-02`, `ID.RA-01`, `PR.DS-01`, `PR.DS-02`, `DE.CM-03`, `DE.AE-02`, `RS.MI-01`, `RC.RP-06`). |

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Arquitectónica |
|---|---|---|
| **Umbrales cuantitativos de KPIs/SLAs** (`MTTA < 15 min`, `MTTC < 30 min`, `FPR < 15 %`, `0 apps GenAI >10 MB sin clasificar`, `>= 75 % SSPM`) | `[Decisión / Propuesta Editorial]` | Microsoft Learn define las métricas operativas pero delega la fijación de metas numéricas en cada organización según dotación 24x7, apetito de riesgo y acuerdos internos. |
| **Matriz RACI y ventanas temporales de activación PIM** (4 h / 8 h, aprobación dual) | `[Decisión / Propuesta Editorial]` | Microsoft recomienda mínimo privilegio y Entra PIM, pero la distribución exacta entre SOC L1/L2/L3, IAM y GRC depende de la estructura orgánica del cliente. |
| **Extensión a cadencias Trimestral, Semestral y Anual** (Tabletops, calibración de `Score metrics`, revisión semestral Edge/GSA) | `[Decisión / Propuesta Editorial]` | El *Operational Guide* oficial de MDA cubre frecuencias Daily, Weekly, Monthly y Ad-hoc; las cadencias trimestral/semestral/anual integran prácticas de Microsoft SAF, Zero Trust y gobierno GRC. |
| **Modelo de Madurez Operacional en 5 niveles** | `[Decisión / Propuesta Editorial]` | Construcción consultiva inspirada en *Zero Trust Deployment Objectives for Applications* y *Azure Well-Architected Security Maturity Model* para orientar hojas de ruta ejecutivas. |
| **Mapeo de evidencias específicas a subcategorías NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Conforme a NIST CSWP 29, el estándar define resultados (*outcomes*) agnósticos de tecnología; la selección de artefactos concretos de MDA como prueba auditable es diseño de gobierno. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn

1. **REF-01 — Microsoft Defender for Cloud Apps overview:** `https://learn.microsoft.com/en-us/defender-cloud-apps/what-is-defender-for-cloud-apps` — Visión general oficial de los cuatro pilares: CASB, SSPM, protección XDR y gobernanza app-to-app.
2. **REF-02 — Microsoft Defender for Cloud Apps operational guide (Overview, Daily, Weekly, Monthly, Ad-hoc):** `https://learn.microsoft.com/en-us/defender-cloud-apps/ops-guide/ops-guide` (subpáginas verificadas: `ops-guide-daily`, `ops-guide-weekly`, `ops-guide-monthly`, `ops-guide-ad-hoc`) — Guía maestra oficial de rutinas SecOps para MDA.
3. **REF-03 — What's new in Microsoft Defender for Cloud Apps:** `https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes` — Registro oficial de novedades verificadas a noviembre de 2026 (Identity inventory auto-enablement oct-2026, Unified RBAC default ago-2026, retiro File Policies jun-2026, Salesforce RTEM).
4. **REF-04 — Migrate file policies to Microsoft Purview:** `https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview` — Guía oficial del retiro de File Policies el 6 de enero de 2027, asistente de migración en 4 pasos y tabla de equivalencias con Purview DLP y Auto-labeling.
5. **REF-05 — Cloud app discovery overview:** `https://learn.microsoft.com/en-us/defender-cloud-apps/set-up-cloud-discovery` — Arquitectura de descubrimiento sobre >31.000 apps y >90 factores de riesgo, integración nativa con MDE, colectores y SWGs.
6. **REF-06 — Conditional Access app control & In-browser protection with Microsoft Edge for Business (Preview):** `https://learn.microsoft.com/en-us/defender-cloud-apps/in-browser-protection` y `https://learn.microsoft.com/en-us/defender-cloud-apps/proxy-intro-aad` — Controles de acceso y sesión en tiempo real vía proxy inverso y protección nativa en el navegador Edge for Business.
7. **REF-07 — App governance in Microsoft Defender for Cloud Apps & OAuth Attack Paths:** `https://learn.microsoft.com/en-us/defender-cloud-apps/app-governance-manage-app-governance` y `https://learn.microsoft.com/en-us/defender-cloud-apps/attack-paths` — Gobernanza OAuth sobre Entra ID, Google Workspace y Salesforce, e integración con Exposure Management.
8. **REF-08 — Configure admin access in Defender for Cloud Apps:** `https://learn.microsoft.com/en-us/defender-cloud-apps/manage-admins` — Referencia oficial de roles Entra ID, Unified RBAC, baja de roles heredados, acceso MSSP B2B y exportación de auditoría administrativa.
9. **REF-09 — CloudAppEvents table in the advanced hunting schema:** `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-cloudappevents-table` — Esquema completo de columnas, prerrequisitos del conector M365 y aplicaciones cubiertas en Advanced Hunting.
10. **REF-10 — Transition Microsoft Copilot Studio and Microsoft Foundry agent security capabilities to Microsoft Agent 365:** `https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/transition-agent-security-to-agent-365` — Transición oficial efectiva el 1 de julio de 2026 hacia Microsoft Agent 365 y migración de `AIAgentsInfo` a `AgentsInfo`.
11. **REF-11 — Microsoft Defender service description (Licensing):** `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-defender-service-description#microsoft-defender-for-cloud-apps` — Detalle oficial de planes y suites que incluyen MDA (M365 E5, Microsoft Defender Suite, Microsoft Purview Suite, EMS E5).

### 15.2 Publicaciones Oficiales y Empleados de Microsoft

12. **REF-12 — Microsoft Security Blog — Microsoft Defender for Cloud Apps Ninja Training:** `https://techcommunity.microsoft.com/blog/microsoft-security-blog/microsoft-defender-for-cloud-apps-ninja-training--june-2022/2751518` — Programa oficial de entrenamiento estructurado por módulos de Shadow IT, políticas, controles de sesión y protección de amenazas.
13. **REF-13 — Microsoft Security Blog — Start secure and stay secure on your AI agent journey with Microsoft Defender:** `https://techcommunity.microsoft.com/blog/microsoft-security-blog/start-secure-and-stay-secure-on-your-ai-agent-journey-with-microsoft-defender/4469430` — Arquitectura oficial de postura y protección en tiempo de ejecución para agentes empresariales en el portal Defender.
14. **REF-14 — Heike Ritter (Microsoft) & Equipos de Producto — Hub "ninja training" en Microsoft Tech Community:** `https://techcommunity.microsoft.com/tag/ninja%20training` — Índice vivo mantenido por empleados de Microsoft con las actualizaciones de los programas Ninja de Defender XDR y workloads asociados.

### 15.3 Comunidad y MVPs de Seguridad de Microsoft

15. **REF-15 — Nikki Chapple (Microsoft MVP) — How to Govern Shadow AI with Microsoft Purview, Defender and DSPM:** `https://nikkichapple.com/govern-shadow-ai-microsoft-purview-defender-dspm/` — Guía práctica de una MVP de Seguridad y Cumplimiento para estructurar descubrimiento, evaluación y bloqueo de Shadow AI combinando Defender for Cloud Apps, MDE y Purview.
16. **REF-16 — Bert-Jan Pals (Microsoft Security MVP) — Hunting-Queries-Detection-Rules:** `https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules` — Repositorio comunitario de referencia con consultas KQL avanzadas de caza y detección sobre `CloudAppEvents` y Microsoft Defender XDR.
17. **REF-17 — Jeffrey Appel (Microsoft Security MVP) — Blog Técnico Defender XDR, MDA & Sentinel:** `https://jeffreyappel.nl/` — Análisis técnicos profundos de arquitectura, novedades mensuales de Defender, retención e investigaciones XDR.

### 15.4 Marcos Normativos y de Arquitectura

18. **REF-18 — NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29):** `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` — Estándar oficial del National Institute of Standards and Technology (febrero de 2024) con las 6 funciones, 22 categorías y 106 subcategorías basadas en resultados.
19. **REF-19 — Secure applications with Zero Trust (Microsoft Learn):** `https://learn.microsoft.com/en-us/security/zero-trust/deploy/applications` — Guía oficial de arquitectura de despliegue Zero Trust para el pilar de Aplicaciones mediante Defender for Cloud Apps y Microsoft Entra.

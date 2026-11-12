# Microsoft Defender for Identity (ITDR Híbrido) — Guía Maestra de Excelencia Operacional

## 1. Portada y Ficha de Control Documental

| Atributo | Valor |
|---|---|
| **Identificador del Módulo** | `06_Microsoft_Defender_for_Identity` |
| **Nombre Oficial** | Microsoft Defender for Identity (ITDR Híbrido) |
| **Categoría** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 (Edición Canónica Consolidada) |
| **Origen y Trazabilidad** | Compilado MSEOP-MD + Revalidado Learn |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5, Microsoft 365 E7, Microsoft 365 A5/G5, Enterprise Mobility + Security E5 (EMS E5/A5), Microsoft Defender Suite (antes M365 E5 Security) y planes F5 Security `[Verificado MS Learn]` |
| **Portales Principales** | `https://security.microsoft.com`, `https://entra.microsoft.com`, `https://admin.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Analistas SOC (L1, L2, L3), Identity Responders, Arquitectos de Identidad Híbrida / Active Directory Tier-0, Security Admins, Auditores GRC |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST SP 800-61 Rev. 3, MITRE ATT&CK Enterprise, Microsoft Zero Trust & Security Adoption Framework (SAF), MCSB v2 |

> **Regla de separación evidencial:** Esta guía etiqueta con `[Verificado MS Learn]` las capacidades técnicas, licencias, requisitos del sensor unificado v3.x, rutas de consola, roles RBAC, tablas KQL y procedimientos oficiales verificados en Microsoft Learn a noviembre de 2026; y con `[Decisión / Propuesta Editorial]` los umbrales cuantitativos de SLA/KPI, ventanas de elevación PIM, modelos de madurez consultivos y mapeos interpretativos hacia resultados (*outcomes*) de NIST CSF 2.0.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust y Microsoft 365 E5

En la empresa híbrida moderna, la identidad constituye el plano de control primario y el objetivo predilecto para escalar privilegios y alcanzar dominancia total sobre la organización. La mayoría de las intrusiones críticas —incluyendo ransomware operado por humanos— explotan configuraciones inseguras heredadas en Active Directory (protocolos NTLMv1, delegaciones Kerberos sin restricciones, plantillas vulnerables en AD CS o cuentas de servicio sobreprivilegiadas) y encadenan saltos laterales entre el directorio local y la nube `[Verificado MS Learn]`.

**Microsoft Defender for Identity (MDI)** es la solución nativa en la nube de **Detección y Respuesta ante Amenazas de Identidad (ITDR)** integrada en **Microsoft Defender XDR**. Protege de extremo a extremo identidades humanas y no humanas (NHI) a través de **Active Directory Domain Services (AD DS)**, **Active Directory Federation Services (AD FS)**, **Active Directory Certificate Services (AD CS)**, **Microsoft Entra Connect**, **Microsoft Entra ID** y proveedores de identidad conectados como **Okta**, **CyberArk Identity** y **SailPoint Identity Security Cloud** `[Verificado MS Learn]`.

### 2.1 Transformación Arquitectónica 2025–2026

Operar MDI con manuales anteriores a 2026 introduce riesgos severos de puntos ciegos y fallos de respuesta. La plataforma experimentó cinco evoluciones estructurales verificadas a noviembre de 2026 `[Verificado MS Learn]`:

1. **Sensor Unificado v3.x:** Integrado en la plataforma de sensor unificado, se activa desde el portal (`Settings > Identities > On-premises > Sensor management`), se actualiza mediante **Windows Update**, opera exclusivamente bajo la cuenta **`LocalSystem`** (eliminando cuentas DSA y gMSA en v3.x) y acota su consumo máximo al **30% de CPU y 1,5 GB de RAM** `[Verificado MS Learn]`. Desde julio de 2026 la migración desde v2.x está en GA (incluyendo Windows Server 2025) y desde octubre de 2026 la activación sin despliegue previo de Defender for Endpoint está en GA para entornos comerciales `[Verificado MS Learn]`.
2. **Remediación Multi-IdP e Interrupción Automática:** Acciones nativas (`Disable`, `Enable`, `Revoke session`, `Mark as compromised`, `Force password change`) sobre AD, Entra ID, Okta, CyberArk, SailPoint y aplicaciones SaaS (Google Workspace, Salesforce, Box), utilizadas también de forma autónoma por **Automatic Attack Disruption** `[Verificado MS Learn]`.
3. **Evolución de Rutas de Movimiento Lateral:** Los mapas clásicos de *Lateral Movement Paths (LMP)* dejaron de actualizarse en mayo de 2025 tras deshabilitarse la recolección remota de administradores locales vía SAM-R (`MC1073068`); hoy se reemplazan operativamente por **Attack Paths en Microsoft Security Exposure Management** y la pestaña **Identity Explorer** (Preview con *Hunting Graph* y *Sentinel Data Lake*) `[Verificado MS Learn]`.
4. **Postura Continua (ISPA), Identity Risk Score e Inventario NHI/IA:** Puntaje de riesgo de identidad de `0 a 100` en GA (junio de 2026), página de **Domain investigation** en GA (julio de 2026), seis categorías de evaluaciones de postura en *Microsoft Secure Score* y visibilidad sobre entidades de servicio utilizadas por **agentes de IA** (`Used by AI agents`) `[Verificado MS Learn]`.
5. **Señales de Riesgo Unificadas:** MDI alimenta el cálculo de riesgo compuesto de usuario en **Microsoft Entra ID Protection**, permitiendo elevar a riesgo alto la combinación de señales en tierra y nube para activar acceso condicional basado en riesgo (`Require risk remediation`, tras el retiro de las directivas de riesgo heredadas el 1 de octubre de 2026) `[Verificado MS Learn]`.

### 2.2 Licenciamiento y Prerrequisitos Técnicos Verificados

- **Licencias habilitantes:** **Microsoft 365 E5**, **Microsoft 365 E7**, **Microsoft Defender Suite** (nombre vigente de *Microsoft 365 E5 Security*), **Enterprise Mobility + Security E5 (EMS E5/A5)**, **Microsoft 365 A5/G5**, **Microsoft 365 F5 Security / F5 Security + Compliance** (sobre base F1/F3 + EMS E3) o licencia independiente de MDI `[Verificado MS Learn]`. (*Office 365 E3/E5* y *Microsoft 365 E3* sin complementos no incluyen MDI).
- **Requisitos técnicos del Sensor v3.x (Noviembre 2026)** `[Verificado MS Learn]`:
  - **Sistema Operativo:** Windows Server 2019, Windows Server 2022 o Windows Server 2025 con la **actualización acumulativa de septiembre de 2026 o posterior** (`KB5122876` para WS2019, `KB5122882` para WS2022, `KB5122871` para WS2025 — versión de sensor `3.0.10+`), sin sensor v2.x instalado (o migrado desde el portal).En nuevos workspaces, la instalación de sensor v2.x se restringe a Windows Server 2016 o anterior `[Verificado MS Learn]`.
  - **Roles de servidor soportados:** Controladores de dominio (AD DS) y servidores dedicados con **AD FS**, **AD CS** o **Microsoft Entra Connect** (desplegar en estos tres últimos exige contar al menos con un sensor v3.x activo en un controlador de dominio) `[Verificado MS Learn]`.
  - **Memoria en máquinas virtuales y plan de energía:** Asignación estática total de RAM (deshabilitar *Dynamic Memory* en Hyper-V y activar *Reserve all guest memory / All locked* en VMware), plan de energía en **High Performance** y sincronización horaria NTP dentro de +/-5 minutos `[Verificado MS Learn]`.
  - **Cuenta de acción obligatoria:** Seleccionar **Automatically use the sensor's local system account** en `Settings > Identities > Microsoft Defender for Identity > Manage action accounts` `[Verificado MS Learn]`.
  - **Auditoría de Windows y RPC:** Habilitar **Automatic Windows event auditing** para sensores v3.x (cubre AD DS, AD FS, AD CS y Entra Connect); desde la versión `3.0.8+` la auditoría RPC en controladores de dominio se activa automáticamente `[Verificado MS Learn]`. Validar prerrequisitos con el script oficial `Test-MdiReadiness.ps1` `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Flujo de Telemetría Híbrida y Capacidades del Sensor Unificado v3.x

```
[Infraestructura Tier-0: AD DS (DCs) · AD FS · AD CS · Microsoft Entra Connect]
       │
       ├──► Inspección profunda de red (Kerberos, NTLM, LDAP, RPC, DNS) + NNR automático
       ├──► Eventos de Seguridad Windows (4624/4625, 4662, 4672, 4776, 8004, AD CS/AD FS)
       └──► Proveedores ETW (Event Tracing for Windows) y auditoría RPC automática (v3.0.8+)
       │
       ▼ [Sensor Unificado MDI v3.x (LocalSystem · <=30% CPU · <=1.5 GB RAM) — Endpoints MDE TLS 443]
[Servicio Cloud Microsoft Defender for Identity (Hasta 1.000 sensores por workspace)]
       │
       ├──► Detecciones AD/Entra/IdP (Alertas Clásicas y Formato Unificado XDR)
       ├──► Identity Inventory (Humanas, NHI, Agentes IA) + Identity Risk Score (0-100)
       ├──► Security Posture Assessments (ISPA en Secure Score) + Domain Investigation
       ├──► Señales de Riesgo Unificadas ──► Microsoft Entra ID Protection (Conditional Access)
       └──► Remediación Directa & Automatic Attack Disruption ──► AD / Entra / Okta / CyberArk / SailPoint
```

**Diferencias operativas clave del Sensor v3.x frente al Sensor Clásico v2.x** `[Verificado MS Learn]`:
- **Identidad del sensor:** v3.x utiliza únicamente `LocalSystem` para consultas LDAP y acciones de remediación en AD; **no utiliza cuentas DSA ni gMSA**. En entornos mixtos (v2.x + v3.x), MDI continúa validando las credenciales DSA/gMSA a nivel de workspace mientras exista esa configuración; una vez migrados el 100% de los sensores a v3.x, se debe eliminar la cuenta DSA/gMSA del portal para evitar falsas alertas de salud `[Verificado MS Learn]`.
- **Conectividad y mantenimiento:** Comparte las mismas URLs de conectividad (*Streamlined* o *Standard*) de Microsoft Defender for Endpoint, prescinde de controladores Npcap externos y del *MDI Sizing Tool*, y recibe actualizaciones mediante paquetes acumulativos de Windows Server `[Verificado MS Learn]`.
- **Limitaciones documentadas de v3.x:** No soporta integración de contabilidad VPN RADIUS, no envía notificaciones por *syslog*, presenta limitaciones con *Azure ExpressRoute* y la activación sin MDE no está soportada temporalmente en nubes gubernamentales `[Verificado MS Learn]`.

### 3.2 Componentes Clave en el Portal Microsoft Defender (`security.microsoft.com`)

| Componente | Función Operativa Principal | Ruta en Portal | Estado Nov 2026 |
|---|---|---|---|
| **Identity Security Dashboard & Coverage** | Vista ejecutiva y táctica con *Top insights*, incidentes de identidad, usuarios Entra en riesgo y evaluación *Coverage & Maturity* multi-IdP | `security.microsoft.com > Identities > Dashboard` | GA / Preview parcial `[Verificado MS Learn]` |
| **Sensor Management & Health Issues** | Pestaña unificada (desde sep-2026) de sensores instalados y servidores elegibles, más monitoreo de alertas de salud globales y por sensor | `Settings > Identities > On-premises > Sensor management` y `Identities > Health issues` | GA `[Verificado MS Learn]` |
| **Identity Inventory (Humanas, NHI y Agentes IA)** | Inventario centralizado con filtros de criticidad, privilegio, cuentas de servicio AD, service principals de Entra y columna `Used by AI agents` | `security.microsoft.com > Assets > Identities` | GA (mejoras NHI/IA en Preview) `[Verificado MS Learn]` |
| **Identity Page, Risk Score e Identity Explorer** | Perfil integral con línea de tiempo de 180 días, **Identity Risk Score (0-100)**, rutas de ataque de Exposure Management e **Identity Explorer** | `Assets > Identities > [Identidad] > Risk score / Attack paths / Identity Explorer` | GA (*Identity Explorer* en Preview con Data Lake) `[Verificado MS Learn]` |
| **Domain Investigation Page** | Investigación de postura por dominio AD: propiedades, salud de sensores, cuentas de servicio, entidades sensibles, GPOs y relaciones de confianza (*trusts*) | `Identities > Domain investigation` (desde activos/alertas de dominio) | GA (julio 2026) `[Verificado MS Learn]` |
| **Security Posture Assessments (ISPA)** | Evaluaciones continuas en 6 categorías (*Hybrid*, *Infrastructure*, *Certificates*, *Group policy*, *Accounts*, *Cloud identities*) en Secure Score | `Exposure management > Secure score > Recommended actions` (filtro *Identity*) | GA `[Verificado MS Learn]` |
| **Entity Tags (Sensitive, Honeytoken, Exchange)** | Clasificación automática y manual de activos Tier-0, roles privilegiados (AD, Entra incluyendo `Agent ID Administrator`, Okta, CyberArk, SailPoint) y cuentas trampa | `Settings > Identities > Entity tags` (`Sensitive`, `Honeytoken`, `Exchange server`) | GA `[Verificado MS Learn]` |
| **Identity Remediation Actions** | Contención directa (`Disable`, `Enable`, `Revoke session`, `Mark as compromised`, `Force password change`) auditada en *Action Center* | `Assets > Identities > [Usuario] > Actions` / `Hunting` / `Action center` | GA `[Verificado MS Learn]` |

### 3.3 Coexistencia de Alertas y Detecciones Modernas 2026

En el portal Defender conviven alertas en formato clásico y alertas nativas en formato unificado Defender XDR (independientemente de si el sensor es v2.x o v3.x) `[Verificado MS Learn]`:
- Las **alertas clásicas** se ajustan mediante **Exclusions** de MDI (`Settings > Identities > Exclusions`), mientras que las **alertas en formato Defender** se ajustan mediante reglas de **Alert tuning** (`Settings > Microsoft Defender XDR > Alert tuning`) `[Verificado MS Learn]`.
- **Catálogo ampliado en 2026:** Además de *Golden Ticket*, *Pass-the-Hash*, *Pass-the-Ticket* y reconocimiento LDAP/SMB, MDI detecta en 2026 abuso de **AD CS (ESC1, ESC8, ESC11 y Certighost CVE-2026-54121)**, escalamiento Kerberos con **Diamond Ticket**, extracción de **DPAPI master key**, **DCSync** unificado, autenticación sospechosa de cuenta **Entra Connect**, uso anómalo de **Temporary Access Pass (TAP)**, registro malicioso de métodos MFA y ataques contra **Okta** y **SailPoint ISC** `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM y JIT)

### 4.1 Modelo Obligatorio Unified RBAC (URBAC) y Scoped Access por Dominio

Desde **marzo de 2025**, los nuevos inquilinos de MDI configuran permisos exclusivamente mediante **Microsoft Defender XDR Unified RBAC (URBAC)** y MDI dejó de crear automáticamente los grupos de seguridad heredados `Azure ATP <workspace> Administrators / Users / Viewers` en Entra ID `[Verificado MS Learn]`. Asimismo, URBAC permite definir **Identity scoping** para restringir la visibilidad de analistas regionales únicamente a dominios específicos de Active Directory `[Verificado MS Learn]`.

### 4.2 Permisos Mínimos Verificados por Función en MDI

| Actividad en MDI | Rol Microsoft Entra ID | Permisos Mínimos en Microsoft Defender Unified RBAC |
|---|---|---|
| Crear workspace / incorporar MDI | `Security Administrator` | N/A (exige `Security Administrator` en el alta inicial) `[Verificado MS Learn]` |
| Ver configuración, alertas y evaluaciones ISPA | `Security Reader` | `Security data basics (read)` + `Security settings (read)` + `System settings (read)` `[Verificado MS Learn]` |
| Gestionar alertas de identidad e investigar | `Security Operator` | `Security data basics (read)` + `Alerts (manage)` `[Verificado MS Learn]` |
| Activar sensores v3.x, configurar etiquetas y ajustes | `Security Administrator` / `Security Operator` | `System settings (Read and manage)` + `Security settings (All permissions)` `[Verificado MS Learn]` |
| Ejecutar acciones de remediación (`Disable`, `Reset`, `Revoke`, `Mark compromised`) | `SOC Identity Responder`, `Security Operator` o roles de Auth/User Admin en Entra | Rol personalizado URBAC con **`Response (manage)`** (más rol Entra aplicable para acciones sobre cuentas Entra ID) `[Verificado MS Learn]` |

> **Nota sobre remediaciones en Entra ID:** MDI ejecuta las acciones en Entra ID mediante la aplicación empresarial administrada *Microsoft Defender for Identity* (`App ID: 60ca1954-583c-4d1f-86de-39d835f3e452`, llamada *Radius Aad Syncer* en tenants antiguos), respetando los límites jerárquicos de roles protegidos de Microsoft Graph `[Verificado MS Learn]`.

### 4.3 Matriz SOC de Separación de Funciones y Elevación JIT en Entra PIM

Los límites horarios y aprobaciones cruzadas constituyen una `[Decisión / Propuesta Editorial]` para resguardar activos Tier-0:

| Nivel SOC / Rol | Rol Técnico Asignado | Estado en Entra PIM | Ventana JIT y Controles | Responsabilidad y Frontera SoD |
|---|---|---|---|---|
| **SOC L1 — Identity Monitor** | Rol URBAC *SOC L1 Identity Analyst* (`Security data basics read` + `Alerts manage`, con *Identity scoping* si aplica) | Activa permanente `[Decisión / Propuesta Editorial]` | MFA resistente a phishing obligatorio | Monitoreo de *Dashboard*, cola de incidentes y *Health issues*; **sin permiso `Response (manage)`** ni modificación de etiquetas/exclusiones `[Decisión / Propuesta Editorial]` |
| **SOC L2 — Identity Responder** | `SOC Identity Responder` / `Security Operator` + URBAC `Response (manage)` | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · MFA FIDO2/Passkey + ticket de incidente `[Decisión / Propuesta Editorial]` | Contención de cuentas (`Disable`, `Revoke session`, `Force password change`, `Mark as compromised`) y clasificación TP/B-TP/FP `[Verificado MS Learn]` |
| **SOC L3 — ITDR Hunter & Lead** | Rol URBAC *SOC L3 ITDR Hunter* + `Custom detections (manage)` | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · MFA resistente a phishing `[Decisión / Propuesta Editorial]` | Caza KQL sobre `Identity*`, diseño de detecciones personalizadas, análisis forense de ataques Kerberos/AD CS y *Alert tuning* `[Verificado MS Learn]` |
| **Identity Platform Admin** | `Security Administrator` (acceso a DCs solo desde **PAW** para tareas de SO/parches) | Elegible en PIM `[Verificado MS Learn]` | Máx. 4 h · Aprobación de líder IAM/SOC + número de cambio `[Decisión / Propuesta Editorial]` | Activación y migración de sensores v3.x, gestión de *Action accounts* (`LocalSystem`), etiquetas *Honeytoken*/*Sensitive* y remediación de salud `[Verificado MS Learn]` |
| **AD Tier-0 Admin (IAM)** | Grupos AD Tier-0 gobernados fuera de cuentas de uso diario | JIT/PAM en directorio local `[Decisión / Propuesta Editorial]` | Máx. 2 h · Exclusivo desde estación **PAW** `[Decisión / Propuesta Editorial]` | Ejecución de doble rotación `krbtgt`, endurecimiento de GPOs/plantillas AD CS y desactivación de *Print Spooler* / NTLMv1; no administra alertas SOC `[Decisión / Propuesta Editorial]` |
| **Auditoría / GRC** | `Security Reader` / `Global Reader` | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · Ventana de auditoría `[Decisión / Propuesta Editorial]` | Verificación independiente de cobertura de sensores, *Identity Secure Score*, historial del *Action Center* y cumplimiento NIST CSF 2.0 `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

> **Propósito:** Asegurar cero puntos ciegos en sensores Tier-0, detectar ataques contra credenciales/Kerberos/AD CS en minutos y ejecutar contención inmediata. Basado en el *Daily Operational Guide* oficial de MDI `[Verificado MS Learn]`.

### D-01 — Revisión Diaria del Identity Security Dashboard y Cobertura ITDR
- **Consola / Ruta:** `https://security.microsoft.com` -> `Identities > Dashboard` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Identity Admin.
- **Procedimiento paso a paso:**
  1. Inspeccionar los tres widgets prescriptivos de la guía diaria oficial: **Top insights**, **Identity related incidents** y **Entra ID users at risk** `[Verificado MS Learn]`.
  2. Verificar el panel **Coverage & Maturity** para detectar caídas abruptas de cobertura en controladores de dominio, servidores AD CS/AD FS/Entra Connect o conectores Okta/CyberArk/SailPoint `[Verificado MS Learn]`.
  3. Escalar de inmediato cualquier anomalía en cuentas etiquetadas como *Sensitive* o con *Identity Risk Score* crítico `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de revisión del dashboard y capturas ante desvíos de umbral.

### D-02 — Triaje Priorizado de Incidentes de Identidad Híbrida en Defender XDR
- **Consola / Ruta:** `https://security.microsoft.com/incidents` (`Investigation & response > Incidents & alerts`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Filtrar `Status = New, In progress` y `Severity = High, Medium, Low` manteniendo **todas las fuentes de servicio marcadas** para preservar la correlación multi-dominio XDR, y aplicando vista específica `Service source = Defender for Identity` para barrido focalizado `[Verificado MS Learn]`.
  2. Otorgar prioridad crítica inmediata (`MTTA < 15 min` `[Decisión / Propuesta Editorial]`) a: actividad en cuentas **Honeytoken**, **DCSync**, **Golden / Diamond Ticket**, abuso **AD CS (ESC1/ESC8/ESC11/Certighost)**, extracción **DPAPI master key**, autenticación sospechosa de cuenta **Entra Connect**, **Pass-the-Hash / Pass-the-Ticket** y registro malicioso de MFA o **TAP** `[Verificado MS Learn]`.
  3. Analizar el *Attack story*, la pestaña *Evidence and response* y *Activity log*; asignar propietario, pasar a `In progress` y al resolver clasificar siempre como `True positive` (especificando amenaza), `False positive` o `Informational, expected activity` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Cola de incidentes exportada, trazabilidad de asignación y clasificación al cierre.

### D-03 — Verificación de Alertas en Cuentas Honeytoken y Cambios en Grupos Sensibles
- **Consola / Ruta:** `https://security.microsoft.com/alerts` y `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Validar ausencia total de inicios de sesión o consultas originadas/dirigidas a usuarios y equipos etiquetados como **Honeytoken** (cualquier evento en una cuenta trampa inactiva constituye compromiso confirmado de alta fidelidad) `[Verificado MS Learn]`.
  2. Verificar todas las alertas y eventos en `IdentityDirectoryEvents` de adición de miembros a grupos **Sensitive** de AD, Entra ID (incluyendo `Global Administrator` y `Agent ID Administrator`), Okta, CyberArk y SailPoint contra tickets aprobados de gestión de cambios `[Verificado MS Learn]`.
- **Evidencia Auditable:** Conciliación diaria de cambios en grupos privilegiados contra sistema ITSM `[Decisión / Propuesta Editorial]`.

### D-04 — Monitoreo y Resolución Prioritaria de Health Issues (Global y Sensor)
- **Consola / Ruta:** `https://security.microsoft.com` -> `Identities > Health issues` (o `Settings > Identities > Deployment > Health issues`) `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Platform Admin / SOC L1.
- **Procedimiento paso a paso:**
  1. Revisar diariamente las pestañas **Global health issues** y **Sensor health issues** filtrando `Status = Open` `[Verificado MS Learn]`.
  2. Tratar cualquier alerta `Sensor service failed to start`, `Sensor stopped communicating` (> 5 min sin señal), `NTLM Auditing is not enabled` o `Directory Services Advanced/Object Auditing not enabled` como un **punto ciego crítico** `[Verificado MS Learn]`.
  3. Verificar si corresponde a v2.x o v3.x: para `Sensor outdated (v3)` coordinar instalación del paquete acumulativo mensual de Windows Server; si persiste alerta de auditoría en v3 pese a GPO correcta, activar *Automatic Windows auditing configuration* en `Settings > Advanced features`; usar `Suppressed` (7 días) únicamente para ventanas de mantenimiento planificadas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `0 Open High/Medium` no justificados en *Health issues* y alertas por correo electrónico activas `[Verificado MS Learn]`.

### D-05 — Ejecución y Auditoría de Acciones de Contención sobre Identidades Comprometidas
- **Consola / Ruta:** `Assets > Identities > [Identidad] > Actions` y `Actions & submissions > Action center` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC Identity Responder.
- **Procedimiento paso a paso:**
  1. Ante confirmación de compromiso o disparo de **Automatic Attack Disruption**, validar en *Action center* que se hayan ejecutado las acciones de contención en todos los directorios vinculados (`Disable`, `Revoke session`, `Mark as compromised`, `Force password change`) `[Verificado MS Learn]`.
  2. Confirmar que cuentas híbridas queden contenidas tanto en Active Directory (ejecutado por el sensor en el DC mediante `LocalSystem`) como en Microsoft Entra ID (vía app administrada MDI) y proveedores terceros conectados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registros de ejecución y estado en `Action center > History` y logs de auditoría de Defender `[Verificado MS Learn]`.

### D-06 — Configuración Táctica de Reglas de Ajuste para B-TP y Falsos Positivos
- **Consola / Ruta:** `Settings > Microsoft Defender XDR > Rules > Alert tuning` y `Settings > Identities > Exclusions` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3.
- **Procedimiento paso a paso:**
  1. Cuando el triaje diario confirme actividades legítimas autorizadas (*Benign True Positives*, como escáneres de vulnerabilidades o herramientas de inventario aprobadas), crear reglas granulares de **Alert tuning** para alertas en formato Defender o exclusiones acotadas por tipo de alerta para alertas clásicas `[Verificado MS Learn]`.
  2. Evitar exclusiones globales de cuentas o subredes completas para no cegar la detección de otras técnicas (ej. *Golden Ticket* o *DCSync* desde el mismo host) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Regla creada con referencia al ticket de validación y alcance mínimo documentado.

### D-07 — Cacería Diaria Rápida (Daily Proactive Hunt) de Anomalías Críticas AD/Híbridas
- **Consola / Ruta:** `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3.
- **Procedimiento paso a paso:**
  1. Ejecutar consultas rápidas de 24 horas buscando: replicaciones de directorio (`Directory Service Replication`) desde equipos que no son DCs ni servidores Entra Connect autorizados, solicitudes anómalas de certificados AD CS y autenticaciones interactivas con cuentas de servicio (`svc_*`) `[Verificado MS Learn]`.
  2. Revisar usuarios con incremento súbito en su **Identity Risk Score** o con señales de riesgo unificadas hacia Entra ID Protection `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de ejecución de consultas base de caza rápida.

### D-08 — Conciliación de Cierre de Turno ITDR
- **Consola / Ruta:** `security.microsoft.com/incidents` y `Identities > Health issues` `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** Shift Lead / SOC L2.
- **Procedimiento paso a paso:**
  1. Verificar que ningún incidente de identidad de severidad `High` permanezca sin contención y que el 100% de los controladores de dominio reporten estado saludable o tengan ticket P1 de infraestructura abierto `[Decisión / Propuesta Editorial]`.
  2. Documentar en el traspaso de turno cuentas contenidas temporalmente pendientes de rehabilitación con TI/RR.HH. `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta de cierre de turno SOC.

---

## 6. Cadencia Operativa Semanal

> **Propósito:** Reducir proactivamente la superficie de ataque de identidad en Secure Score, cazar técnicas silenciosas de reconocimiento/persistencia y vigilar rutas de ataque hacia activos Tier-0 `[Verificado MS Learn]`.

### S-01 — Revisión y Priorización Semanal de Identity Security Posture Assessments (ISPA)
- **Consola / Ruta:** `https://security.microsoft.com/securescore` (`Recommended actions` -> categoría `Identity`) `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / Security Admin.
- **Procedimiento:** Revisar hallazgos actualizados en las 6 categorías oficiales (*Hybrid security*, *Identity infrastructure*, *Certificates*, *Group policy*, *Accounts*, *Cloud identities*); priorizar remediación inmediata de *Print Spooler* habilitado en DCs, delegaciones Kerberos sin restricciones, plantillas vulnerables de AD CS (ESC1–ESC8), credenciales expuestas en texto claro (LDAP Simple Bind), cuentas obsoletas en grupos sensibles y cuenta *Guest* habilitada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Backlog semanal priorizado con tickets asignados a los equipos de AD/PKI/IAM.

### S-02 — Caza Proactiva Semanal del AD Kill-Chain (Reconocimiento, Kerberoasting, AD CS y Spraying)
- **Consola / Ruta:** `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Threat Hunter.
- **Procedimiento:** Ejecutar hipótesis estructuradas sobre 7 días en `IdentityQueryEvents`, `IdentityLogonEvents` e `IdentityDirectoryEvents`: enumeraciones masivas LDAP/SAM-R tipo *BloodHound/SharpHound*, degradación de cifrado Kerberos a RC4 (*Kerberoasting / AS-REP Roasting*), fallos distribuidos de autenticación (*Password Spraying*) y anomalías en cuentas no humanas (`IdentityAccountInfo` / service principals usados por agentes IA) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consultas KQL versionadas, hallazgos investigados y nuevas *Custom detection rules* derivadas.

### S-03 — Análisis de Rutas de Ataque hacia Tier-0 (Exposure Management Attack Paths e Identity Explorer)
- **Consola / Ruta:** `Exposure management > Attack surface > Attack paths` y `Assets > Identities > [Identidad] > Attack paths / Identity Explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / SOC L3.
- **Procedimiento:** Dado que los mapas clásicos de *Lateral Movement Paths* dejaron de actualizarse en mayo de 2025 (`MC1073068`), analizar semanalmente las **Attack paths** modernas hacia controladores de dominio, servidores Entra Connect/AD CS y cuentas Tier-0 (usando además *Identity Explorer* si se cuenta con *Sentinel Data Lake*), priorizando puntos de estrangulamiento (*chokepoints*) como credenciales almacenadas en estaciones no privilegiadas o permisos ACL excesivos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de rutas de ataque críticas hacia activos Tier-0 y acciones de corte ejecutadas.

### S-04 — Auditoría y Erradicación Progresiva de Protocolos Heredados (NTLMv1, LDAP Simple Bind y SMBv1)
- **Consola / Ruta:** `https://security.microsoft.com/v2/advanced-hunting` y reportes ISPA `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Admin / Security Engineer.
- **Procedimiento:** Consultar semanalmente en `IdentityLogonEvents` cualquier autenticación `NTLMv1` y enlaces `LDAP SimpleBind` en texto claro agrupados por dispositivo de origen y aplicación; notificar a los dueños de aplicaciones para migrar a Kerberos / LDAPS (puerto 636/3269) y exigir *LDAP Signing* y *Channel Binding* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tabla semanal decreciente de sistemas emisores de NTLMv1 y LDAP en texto claro.

### S-05 — Seguimiento de Amenazas Emergentes de Identidad y Validación de Reglas Custom
- **Consola / Ruta:** `Threat intelligence > Threat analytics` y `Hunting > Custom detection rules` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Detection Engineer.
- **Procedimiento:** Revisar reportes de *Threat Analytics* sobre vulnerabilidades de Active Directory, Kerberos o AD CS (ej. *Certighost* u otros vectores PKINIT), validar impacto en el entorno y verificar que las reglas de detección personalizada sobre tablas `Identity*` ejecuten sin errores ni exceso de falsos positivos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de validación de reglas de ingeniería de detección.

### S-06 — Verificación del Estado de Migración y Paridad de Sensores v3.x
- **Consola / Ruta:** `Settings > Identities > On-premises > Sensor management` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Platform Admin.
- **Procedimiento:** Auditar que el 100% de los servidores de identidad detectados estén incorporados con sensor **v3.x** actualizado, revisar motivos en el tooltip *Not ready for migration* si restan sensores v2.x, y confirmar que `Manage action accounts` mantenga habilitado *Automatically use the sensor's local system account* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario exportado desde la pestaña unificada *Sensor management*.

---

## 7. Cadencia Operativa Mensual

> **Propósito:** Auditar gobernanza de ajustes, revisar postura integral por dominio AD, asegurar cobertura de identidades no humanas/agentes y reportar reducción de exposición al CISO `[Verificado MS Learn]`.

### M-01 — Revisión Mensual de Alertas Ajustadas (Alert Tuning) y Exclusiones Clásicas
- **Consola / Ruta:** `Settings > Microsoft Defender XDR > Alert tuning` y `Settings > Identities > Exclusions` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Lead / Security Admin.
- **Procedimiento:** Auditar todas las reglas de *Alert tuning* y exclusiones clásicas de MDI conforme al *Monthly Operational Guide*; eliminar reglas sin coincidencias en 30 días, validar que los escáneres o cuentas excluidas sigan autorizadas y confirmar en entornos 100% v3.x que se hayan retirado cuentas DSA/gMSA residuales del portal `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual de depuración de reglas de *Alert tuning* y exclusiones firmada.

### M-02 — Gobernanza de la Iniciativa Identity Security en Exposure Management y Domain Investigation
- **Consola / Ruta:** `Exposure management > Exposure insights > Initiatives > Identity Security` e `Identities > Domain investigation` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / SOC Manager.
- **Procedimiento:** Evaluar el avance mensual frente al puntaje objetivo (*Target score*) de la **Identity Security Initiative**, e inspeccionar la página **Domain investigation** (GA julio 2026) para cada dominio del bosque revisando relaciones de confianza (*trusts*), GPOs riesgosas, desglose de cuentas de servicio y entidades sensibles `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de progreso de la iniciativa *Identity Security* y resumen de postura por dominio AD.

### M-03 — Auditoría de Identidades No Humanas (NHI), Agentes de IA y Etiquetas Entity Tags
- **Consola / Ruta:** `Assets > Identities` (filtro Non-human identities) y `Settings > Identities > Entity tags` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / Security Admin.
- **Procedimiento:** Revisar el inventario de cuentas de servicio de AD y *service principals* de Entra ID (incluyendo la columna `Used by AI agents`), revocar privilegios excesivos o credenciales inactivas, actualizar el etiquetado manual de cuentas/grupos **Sensitive** y rotar/validar la ubicación de las cuentas y equipos **Honeytoken** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación CSV mensual del inventario de identidades privilegiadas/NHI y listado auditado de *Entity tags*.

### M-04 — Auditoría de Roles Unified RBAC, Scoped Access, PIM e Historial del Action Center
- **Consola / Ruta:** `System > Permissions & roles`, `Actions & submissions > Action center > History` y `entra.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / GRC.
- **Procedimiento:** Auditar quiénes poseen permisos `Response (manage)` y roles `SOC Identity Responder` / `Security Administrator`, validar alcances por dominio AD (*Identity scoping*), conciliar el 100% de las acciones manuales ejecutadas sobre identidades en *Action center* contra incidentes documentados y confirmar vigencia de políticas de Conditional Access por riesgo unificado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de gobierno RBAC/PIM y trazabilidad de acciones de contención.

### M-05 — Seguimiento Mensual de Cambios de Plataforma (What's New / Message Center) y Reporte CISO
- **Consola / Ruta:** `admin.microsoft.com > Health > Message center` y `learn.microsoft.com/en-us/defender-for-identity/whats-new` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Platform Admin / SOC Manager.
- **Procedimiento:** Revisar avisos mensuales de MDI y Defender XDR (nuevas alertas XDR, actualizaciones acumulativas requeridas para sensor v3.x, avisos de activación automática de 30 días), convertir cambios en tareas de ingeniería y presentar al CISO el tablero mensual de exposición e incidentes ITDR `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro mensual de evaluación de novedades y presentación ejecutiva al CISO.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral) — Validación Profunda de Configuración de Dominio y Servidores (`Test-MdiReadiness.ps1`)
- **Consola / Ruta:** `Identities > Tools` (Preview) / repositorio oficial GitHub `Test-MdiReadiness` y `admin.microsoft.com > Service health` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Platform Admin / AD Tier-0 Admin.
- **Procedimiento:** Ejecutar trimestralmente `Test-MdiReadiness.ps1` sobre todos los dominios y servidores AD DS, AD FS, AD CS y Entra Connect para certificar políticas de auditoría avanzada, SACLs de objetos, auditoría NTLM (`8004`), auditoría RPC automática, reserva completa de memoria VM y plan de energía *High Performance*; validar además que el proceso corporativo de aprovisionamiento de servidores incluya activación obligatoria del sensor v3.x `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reportes HTML/JSON de `Test-MdiReadiness.ps1` al 100% de cumplimiento y checklist de alta de servidores.

### SM-01 (Semestral) — Ejercicio Purple Team de Historias Completas de Ataque en Directorio Híbrido
- **Consola / Ruta:** Entorno controlado siguiendo *Best Practices before Offensive Security Testing for MDI* `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** Red/Purple Team / SOC L3 / Identity Architect.
- **Procedimiento:** Ejecutar historias de ataque completas de principio a fin (tal como exige la guía oficial de pruebas ofensivas de MDI, evitando técnicas aisladas fuera de contexto): reconocimiento LDAP -> abuso de plantilla AD CS (`ESC1`/`ESC8`) o *Kerberoasting* -> movimiento lateral *Pass-the-Ticket* -> intento *DCSync* o toque de *Honeytoken*; verificar salud previa de sensores, tiempos de generación de alerta, correlación XDR y señales de riesgo unificadas hacia Entra ID `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral Purple Team con matriz MITRE ATT&CK validada, MTTD medido y brechas cerradas.

### A-01 (Anual) — Simulacro Tabletop de Compromiso Tier-0 y Doble Rotación `krbtgt`
- **Consola / Ruta:** Ejercicio ejecutivo y técnico de crisis (SOC, IAM/AD Tier-0, Infraestructura, Legal y CISO) `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO / Incident Response Lead / AD Tier-0 Lead.
- **Procedimiento:** Simular un escenario de dominancia de dominio (*Golden/Diamond Ticket* o compromiso de servidor *Entra Connect* / CA raíz) validando la secuencia de contención masiva, aislamiento de sistemas, procedimiento probado de **doble restablecimiento de la cuenta `krbtgt`** (respetando el intervalo mínimo de replicación de >=10 horas entre ambos resets) y plan de recuperación del bosque AD `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta anual de ejercicio Tabletop y prueba documentada en pre-producción del procedimiento `krbtgt`.

### A-02 (Anual) — Revisión Arquitectónica Anual de Ciclo de Vida de SO, Capacidad y Licencias ITDR
- **Consola / Ruta:** `Settings > Identities > On-premises > Sensor management` y `admin.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Enterprise Identity Architect / CISO.
- **Procedimiento:** Auditar el ciclo de vida de sistemas operativos de todos los controladores de dominio y servidores AD FS/AD CS/Entra Connect (eliminando cualquier Windows Server 2016 remanente que impida sensor v3.x), validar capacidad por workspace (límite de 1.000 sensores), revisar integraciones con IdPs externos (Okta, CyberArk, SailPoint) y conciliar licenciamiento E5 / Defender Suite / EMS E5 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Documento anual de arquitectura ITDR y plan de modernización de infraestructura de identidad.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes

### AH-01 — Playbook ante Ataque Crítico de Dominancia AD (`DCSync`, `Golden Ticket`, `Diamond Ticket`)
- **Disparador:** Alerta de alta severidad `DCSync attack (replication of directory services)`, `Golden Ticket` o `Kerberos privilege escalation using a diamond ticket` `[Verificado MS Learn]`.
- **Secuencia de respuesta:**
  1. **Verificación inmediata (< 10 min `[Decisión / Propuesta Editorial]`):** Confirmar en el *Alert story* e `IdentityDirectoryEvents` el dispositivo origen (`DeviceName` / `IPAddress`) y la cuenta ejecutora; descartar únicamente si corresponde a un controlador de dominio legítimo o servidor *Microsoft Entra Connect* documentado.
  2. **Contención Dual (Identidad + Endpoint):** Aislar inmediatamente el host origen en Defender for Endpoint (`Isolate device`), deshabilitar la cuenta comprometida en AD y Entra ID (`Disable`), revocar sesiones (`Revoke session`) y marcar como comprometida (`Mark as compromised`) `[Verificado MS Learn]`.
  3. **Erradicación Tier-0:** Auditar ACLs del objeto raíz del dominio buscando permisos `Replicating Directory Changes All` inyectados (`AdminSDHolder` / `SIDHistory`); si hubo *Golden* o *Diamond Ticket*, ejecutar el procedimiento coordinado de **doble rotación de contraseña de `krbtgt`** (con separación mínima de 10 horas) y rotación de credenciales de cuentas privilegiadas expuestas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Incidente maestro en Defender XDR, acciones en *Action center* y bitácora firmada de rotación `krbtgt`.

### AH-02 — Playbook ante Explotación de Servicios de Certificados AD CS (`ESC1`, `ESC8`, `ESC11`, `Certighost`)
- **Disparador:** Alertas `Suspicious AD CS misconfigured certificate template abuse (ESC1)`, `machine certificate issuance abuse (ESC8 / ESC11)`, `Potential Certighost (CVE-2026-54121)` o `CA certificate and private key theft` `[Verificado MS Learn]`.
- **Secuencia de respuesta:**
  1. Identificar la plantilla de certificado abusada, el solicitante y el Subject Alternative Name (SAN) suplantado en los detalles de la alerta y eventos PKINIT (`Suspicious Kerberos PKINIT authentication AS-REQ`) `[Verificado MS Learn]`.
  2. Deshabilitar inmediatamente la publicación de la plantilla vulnerable en la entidad emisora (CA), revocar los certificados fraudulentos emitidos (publicando nueva CRL de emergencia) y contener tanto la cuenta solicitante como la identidad privilegiada suplantada `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
  3. Si se detectó robo de clave privada de la CA, activar protocolo mayor de desconfianza y reconstrucción de jerarquía PKI.
- **Evidencia Auditable:** Registro de revocación CRL, plantilla deshabilitada y cierre de la evaluación ISPA de certificados en *Secure Score*.

### AH-03 — Playbook ante Activación de Cuenta o Equipo Honeytoken
- **Disparador:** Cualquier alerta de autenticación, consulta o intento de movimiento lateral involucrando una entidad etiquetada como **Honeytoken** `[Verificado MS Learn]`.
- **Secuencia de respuesta:**
  1. Asumir **intrusión activa confirmada** con prioridad P1 sin esperar segunda señal (las entidades Honeytoken carecen de uso legítimo productivo) `[Verificado MS Learn]`.
  2. Rastrear en `IdentityLogonEvents` y `DeviceNetworkEvents` el host origen exacto mediante atribución NNR, aislar el equipo en MDE, recolectar paquete de investigación forense y contener las cuentas reales activas en ese mismo dispositivo `[Verificado MS Learn]`.
  3. Rotar la contraseña de la cuenta Honeytoken tras concluir la contención del incidente.
- **Evidencia Auditable:** Línea de tiempo forense completa desde el toque del Honeytoken hasta el aislamiento del origen.

### AH-04 — Playbook de Incorporación / Migración Controlada de Servidor Tier-0 a Sensor v3.x o Pérdida de Salud
- **Disparador:** Promoción de un nuevo controlador de dominio / servidor AD FS / AD CS / Entra Connect, migración desde v2.x o alerta crítica de sensor sin comunicación `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Verificar en `Settings > Identities > Microsoft Defender for Identity > Manage action accounts` que esté activo **Automatically use the sensor's local system account** `[Verificado MS Learn]`.
  2. Confirmar SO Windows Server 2019/2022/2025 con actualización acumulativa de septiembre de 2026+, memoria VM totalmente reservada, energía *High Performance* y conectividad HTTPS hacia las URLs de MDE `[Verificado MS Learn]`.
  3. Activar o migrar el sensor desde `Settings > Identities > On-premises > Sensor management` (proceso sin reinicio ni caída de hasta 20 min por DC en migración v2->v3), verificar activación de auditoría automática de Windows/RPC y confirmar estado `Running` con `0 Health issues` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `Running` del sensor v3.x en portal y validación limpia con `Test-MdiReadiness.ps1`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Esquema de Tablas KQL de Identidad en Advanced Hunting (Noviembre 2026)

| Tabla | Estado | Contenido y Propósito en Cacería e Investigación |
|---|---|---|
| `IdentityLogonEvents` | GA | Eventos de autenticación Kerberos, NTLM y LDAP en Active Directory on-premises y servicios conectados `[Verificado MS Learn]` |
| `IdentityQueryEvents` | GA | Consultas realizadas contra objetos de Active Directory (usuarios, grupos, equipos, dominios, SAM-R, LDAP, DNS) `[Verificado MS Learn]` |
| `IdentityDirectoryEvents` | GA | Cambios de directorio y eventos de sistema en controladores de dominio (replicación DCSync, cambios de grupos sensibles, GPOs, servicios, PKI) `[Verificado MS Learn]` |
| `IdentityInfo` | GA | Perfil consolidado de usuarios (roles asignados, departamento, estado, UPN, SID, pertenencia a grupos, nivel de riesgo) `[Verificado MS Learn]` |
| `IdentityAccountInfo` | GA (Feb 2026) | Información detallada de cuentas humanas y no humanas provenientes de múltiples directorios y su vínculo con la identidad propietaria `[Verificado MS Learn]` |
| `IdentityEvents` | Preview | Eventos de actividad e inicio de sesión provenientes de proveedores de identidad cloud externos (ej. Okta) `[Verificado MS Learn]` |
| `EntraIdSignInEvents` / `EntraIdSpnSignInEvents` | GA | Inicios de sesión interactivos, no interactivos, de *service principals* e identidades administradas en Microsoft Entra ID (reemplazó a `AADSignInEventsBeta` en octubre de 2026) `[Verificado MS Learn]` |
| `DisruptionAndResponseEvents` | Preview | Registro de eventos de contención autónoma ejecutados por *Automatic Attack Disruption* sobre cuentas y dispositivos `[Verificado MS Learn]` |

### 10.2 Consultas KQL Operacionales Verificadas

#### KQL-01: Detección de replicación maliciosa de directorio (DCSync) desde orígenes no autorizados
```kql
// Identifica llamadas de replicación AD (DCSync) fuera de DCs conocidos o servidores Entra Connect [Verificado MS Learn]
IdentityDirectoryEvents
| where Timestamp > ago(7d)
| where ActionType == "Directory Service Replication"
| where isnotempty(AccountUpn) or not(AccountName endswith "$")
| project Timestamp, ActionType, AccountDomain, AccountName, AccountUpn, DeviceName, IPAddress, TargetDeviceName, AdditionalFields
| order by Timestamp desc
```

#### KQL-02: Actividad de alta fidelidad sobre cuentas o equipos Honeytoken
```kql
// Cualquier autenticación o consulta asociada a cuentas trampa exige respuesta P1 inmediata [Verificado MS Learn]
let Honeytokens = dynamic(["svc_backup_legacy@contoso.com", "adm_tier0_vault@contoso.com"]);
IdentityLogonEvents
| where Timestamp > ago(24h)
| where AccountUpn in~ (Honeytokens) or TargetAccountUpn in~ (Honeytokens)
| project Timestamp, ActionType, Protocol, LogonType, AccountUpn, DeviceName, IPAddress, TargetDeviceName, FailureReason
```

#### KQL-03: Modificaciones en grupos altamente privilegiados (AD Sensitive Groups)
```kql
// Audita altas y bajas en grupos Tier-0 de Active Directory [Verificado MS Learn]
IdentityDirectoryEvents
| where Timestamp > ago(7d)
| where ActionType has "Group Membership changed"
| extend Details = parse_json(AdditionalFields)
| extend TargetGroup = coalesce(tostring(Details["TO.GROUP"]), tostring(Details.GroupName))
| where TargetGroup in~ ("Domain Admins", "Enterprise Admins", "Schema Admins", "Administrators", "Account Operators", "Backup Operators", "Server Operators", "Print Operators")
| project Timestamp, Actor = AccountUpn, MemberChanged = TargetAccountUpn, TargetGroup, TargetDeviceName, Details
```

#### KQL-04: Reconocimiento masivo LDAP / SAM-R (Patrón BloodHound / SharpHound / ADRecon)
```kql
// Detecta ráfagas de enumeración de objetos y relaciones en Active Directory [Verificado MS Learn]
IdentityQueryEvents
| where Timestamp > ago(7d)
| where ActionType in ("SamR query", "Ldap query")
| summarize TotalQueries = count(), DistinctQueryTypes = dcount(QueryType), SampleQueries = make_set(QueryType, 10)
    by AccountUpn, DeviceName, IPAddress, bin(Timestamp, 1h)
| where TotalQueries > 500 and DistinctQueryTypes >= 3
| order by TotalQueries desc
```

#### KQL-05: Inventario para erradicación de protocolos heredados NTLMv1 y LDAP Simple Bind
```kql
// Identifica aplicaciones y equipos que aún negocian NTLMv1 o exponen credenciales por LDAP sin cifrar [Verificado MS Learn]
IdentityLogonEvents
| where Timestamp > ago(14d)
| extend Info = parse_json(AdditionalFields)
| extend NtlmVersion = tostring(Info.NtlmVersion)
| where (Protocol == "Ntlm" and NtlmVersion == "1") or (Protocol == "Ldap" and LogonType == "SimpleBind")
| summarize EventCount = count(), AffectedAccounts = dcount(AccountUpn)
    by Protocol, LogonType, NtlmVersion, DeviceName, IPAddress, Application
| order by EventCount desc
```

#### KQL-06: Correlación híbrida de cuenta privilegiada con alerta MDI e inicio de sesión riesgoso en Entra ID
```kql
// Une alertas de MDI con inicios de sesión en EntraIdSignInEvents (esquema vigente oct 2026) [Verificado MS Learn]
let MdiAlertUsers = AlertInfo
    | where Timestamp > ago(24h) and DetectionSource == "Microsoft Defender for Identity"
    | join kind=inner (AlertEvidence | where Timestamp > ago(24h) and EntityType == "User") on AlertId
    | distinct AccountUpn, Title, Severity;
EntraIdSignInEvents
| where Timestamp > ago(24h)
| join kind=inner MdiAlertUsers on AccountUpn
| where RiskLevelDuringSignIn in ("medium", "high") or ErrorCode == 0
| project Timestamp, AccountUpn, Title, Severity, Application, IPAddress, Country, RiskLevelDuringSignIn, ConditionalAccessStatus
```

### 10.3 Verificación Técnica con `Test-MdiReadiness.ps1` y Salud de Dominio

```powershell
# Ejecución del validador oficial Test-MdiReadiness.ps1 antes/después de activar sensores v3.x [Verificado MS Learn]
# Fuente oficial: https://github.com/microsoft/Microsoft-Defender-for-Identity/tree/main/Test-MdiReadiness
.\Test-MdiReadiness.ps1 -Path "C:\MDI_Audit" -OpenHtmlReport

# Auditoría rápida en AD de cuentas o servidores no-DC con Unconstrained Delegation [Verificado MS Learn]
Get-ADComputer -Filter {TrustedForDelegation -eq $true -and PrimaryGroupID -ne 516} -Properties TrustedForDelegation,OperatingSystem |
    Select-Object Name,OperatingSystem,TrustedForDelegation
Get-ADUser -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation |
    Select-Object Name,SamAccountName,TrustedForDelegation
```

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales y de Postura ITDR

> Las definiciones se apoyan en telemetría oficial de MDI, *Secure Score* y *Exposure Management* `[Verificado MS Learn]`; las metas cuantitativas son `[Decisión / Propuesta Editorial]`.

| ID | Indicador (KPI) | Fórmula / Método de Cálculo | Meta Sugerida `[Decisión / Propuesta Editorial]` | Frecuencia | Audiencia |
|---|---|---|---|---|---|
| **KPI-01** | **Cobertura y Salud de Sensores Tier-0 (v3.x)** | `(Servidores AD DS, AD FS, AD CS y Entra Connect con sensor activo y 0 Health Issues críticos / Total servidores de identidad) * 100` | 100% de cobertura y >= 99,5% de disponibilidad saludable | Diaria | Identity Admin / SOC Manager |
| **KPI-02** | **MTTA en Incidentes Críticos de Identidad** | `percentiles(FirstModifiedTime - CreatedTime, 50, 90)` sobre incidentes con origen MDI / Entra ID Protection | p50 < 10 min / p90 < 15 min (severidad Alta) | Semanal | SOC Manager |
| **KPI-03** | **Tiempo Medio de Contención de Identidad (MTTC-ID)** | Tiempo desde creación del incidente hasta ejecución de `Disable` / `Revoke session` (manual o vía *Automatic Attack Disruption*) | p90 < 15 minutos en compromisos críticos | Semanal | SOC Manager / CISO |
| **KPI-04** | **Puntaje de Postura ISPA / Identity Security Initiative** | Porcentaje de puntos alcanzados en recomendaciones de identidad en *Secure Score* e iniciativa *Identity Security* | >= 85% y tendencia creciente mensual | Mensual | CISO / Identity Architect |
| **KPI-05** | **Exposición de Protocolos Heredados (NTLMv1 + Simple Bind)** | Conteo mensual de eventos de autenticación `NTLMv1` y `LDAP SimpleBind` en `IdentityLogonEvents` | 0 eventos NTLMv1 y reducción > 25% trimestral de Simple Bind hasta llegar a 0 | Mensual | Identity Architect / TI |
| **KPI-06** | **Rutas de Ataque Críticas hacia Activos Tier-0** | Cantidad de *Attack paths* activas en *Exposure Management* que alcanzan Domain Admins, DCs, AD CS o Entra Connect | 0 rutas críticas explotables con credenciales expuestas | Semanal | CISO / Identity Architect |
| **KPI-07** | **Tasa de Falsos Positivos por Regla en Alertas MDI** | `(Alertas MDI cerradas como False Positive / Total alertas MDI cerradas) * 100` (emparejado con revisión de *Alert tuning*) | < 10% sin exclusiones globales amplias | Mensual | SOC Lead |
| **KPI-08** | **Higiene de Delegaciones y Superficie Tier-0** | Conteo de cuentas/equipos no-DC con *Unconstrained Delegation* + DCs con *Print Spooler* activo + plantillas AD CS ESC1 abiertas | Exactamente 0 en las tres condiciones | Mensual | CISO / Auditoría GRC |

### 11.2 Modelo de Madurez Operacional ITDR (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estado | Características Observables |
|---|---|---|
| **Nivel 1 — Inicial** | Visibilidad fragmentada | Sensores desplegados parcialmente solo en algunos DCs, sensores v2.x desactualizados, *Health issues* abiertos sin dueño, sin cuentas Honeytoken. |
| **Nivel 2 — Básico Gestionado** | Cobertura completa AD DS | 100% de DCs cubiertos, triaje diario de incidentes, alertas de salud monitoreadas, etiquetado básico de grupos sensibles. |
| **Nivel 3 — Intermedio Híbrido** | Sensor unificado v3.x + Postura activa | Migración a **sensor v3.x** (`LocalSystem`) extendida a AD FS, AD CS y Entra Connect; remediaciones directas operativas; revisión mensual de ISPA en *Secure Score*; URBAC + PIM activos. |
| **Nivel 4 — Avanzado Proactivo** | Convergencia ITDR + XDR + Conditional Access | Señales de riesgo unificadas alimentando acceso condicional (`Require risk remediation`), caza semanal KQL, análisis continuo de *Attack paths*, inventario NHI/Agentes IA gobernado y erradicación de NTLMv1. |
| **Nivel 5 — Optimizado / Resiliente** | Dominio Tier-0 endurecido y validado | *Automatic Attack Disruption* validado, conectores multi-IdP (Okta/CyberArk/SailPoint) integrados, ejercicios semestrales Purple Team de historias completas, simulacro anual `krbtgt` y cero rutas críticas abiertas hacia Tier-0. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> Mapeo basado en resultados (*outcomes*) conforme a NIST CSWP 29 con artefactos repetibles y verificables en el portal Microsoft Defender `[Decisión / Propuesta Editorial]`.

### 12.1 Matriz de Evidencia Auditable NIST CSF 2.0

| Función | Subcategoría CSF 2.0 | Resultado Esperado (Outcome) | Capacidad Habilitadora en MDI / XDR | Evidencia Objetiva para Auditoría |
|---|---|---|---|---|
| **GOVERN (GV)** | `GV.RM-02` | Se establecen y comunican objetivos de apetito y tolerancia al riesgo cibernético. | Definición de *Target score* en la iniciativa **Identity Security** de Exposure Management y panel *Coverage & Maturity*. | Captura de meta configurada y reporte histórico de tendencia de 14/30 días. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de seguridad se establecen y hacen cumplir. | **Microsoft Defender Unified RBAC (URBAC)** con *Identity scoping* por dominio AD y elevación JIT en Entra PIM. | Exportación de roles personalizados URBAC, asignaciones con alcance de dominio y logs PIM. |
| **IDENTIFY (ID)** | `ID.AM-05` | Los activos se priorizan según clasificación, criticidad e impacto misional. | **Identity Inventory** (humanas, NHI, servicio AD y `Used by AI agents`), **Identity Risk Score (0-100)** y *Entity tags* (`Sensitive`). | Exportación CSV de `Assets > Identities` y configuración en `Settings > Identities > Entity tags`. |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican, validan y registran vulnerabilidades en activos e infraestructura. | **Security Posture Assessments (ISPA)** en 6 categorías (incluyendo plantillas/CA de AD CS, GPOs y Entra Connect) y **Domain investigation**. | Exportación de acciones recomendadas de identidad en *Secure Score* y vista *Domain investigation*. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen y gestionan bajo mínimo privilegio. | Reducción de rutas en **Attack paths / Identity Explorer**, remoción de cuentas inactivas en grupos sensibles y señales unificadas hacia Conditional Access. | Reporte de reducción de *Attack paths* hacia Tier-0 y políticas de acceso condicional basadas en riesgo. |
| **PROTECT (PR)** | `PR.PS-01` | Se establecen y mantienen prácticas seguras de gestión de configuración de plataformas. | Endurecimiento guiado por ISPA (desactivar *Print Spooler* en DCs, exigir *LDAP Signing*, eliminar *NTLMv1* y *Unconstrained Delegation*) y validación `Test-MdiReadiness.ps1`. | Reportes trimestrales `Test-MdiReadiness.ps1` y consultas KQL con 0 eventos NTLMv1. |
| **DETECT (DE)** | `DE.CM-01` | Las redes y sistemas críticos se monitorean continuamente para detectar eventos adversos. | Sensores unificados **v3.x** en AD DS, AD FS, AD CS y Entra Connect con monitoreo continuo de salud y cuentas trampa **Honeytoken**. | Estado 100% saludable en `Identities > Health issues` y `Sensor management`. |
| **DETECT (DE)** | `DE.AE-03` | Se correlacionan eventos de múltiples fuentes para caracterizar ataques e impacto. | Correlación de alertas AD/Entra/Okta/SailPoint en incidentes XDR con *Attack story* y línea de tiempo de 180 días por identidad. | Exportación de incidentes correlacionados y capturas de *Alert story* en Defender XDR. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes se contienen de forma rápida para impedir la expansión del compromiso. | **Identity Remediation Actions** (`Disable`, `Revoke session`, `Mark as compromised`, `Force password change`) manuales y vía **Automatic Attack Disruption**. | Registros auditables en `Action center > History` y tabla `DisruptionAndResponseEvents`. |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de activos restaurados y se restablece la operación segura. | Rehabilitación controlada de cuentas (`Enable`), verificación post-incidente de ACLs/grupos/certificados y simulacros de rotación `krbtgt` + AAR. | Informes *After-Action Report*, validación limpia de membresías privilegiadas y logs de rehabilitación. |

### 12.2 Cobertura Principal del AD & Hybrid Kill-Chain en MITRE ATT&CK `[Verificado MS Learn]`

| Táctica MITRE | Técnicas Cubiertas | Detecciones y Controles en MDI |
|---|---|---|
| **Reconnaissance / Discovery (`TA0043` / `TA0007`)** | `T1087.002` (Domain Account Discovery), `T1069.002` (Domain Groups), `T1018` (Remote System Discovery) | Alertas de enumeración LDAP, SAM-R, DNS y mapeo de red; caza en `IdentityQueryEvents` |
| **Credential Access (`TA0006`)** | `T1003.006` (DCSync), `T1558.001` (Golden Ticket), `T1558.003` (Kerberoasting), `T1558.004` (AS-REP), `T1649` (Steal/Forge Auth Certificates — ESC1/8/11), `T1555.004` (DPAPI) | Detecciones determinísticas y comportamentales de DCSync, Golden/Diamond Ticket, PKINIT, abuso AD CS y robo de claves DPAPI |
| **Privilege Escalation & Persistence (`TA0004` / `TA0003`)** | `T1098` (Account Manipulation / MFA registration / Sensitive groups), `T1484` (Domain Policy Modification), `T1556` (Modify Auth Process) | Adiciones a grupos sensibles (AD/Entra/Okta), registro malicioso de MFA, abuso de TAP y cambios en GPO/trusts |
| **Lateral Movement (`TA0008`)** | `T1550.002` (Pass-the-Hash / Overpass-the-Hash), `T1550.003` (Pass-the-Ticket), `T1021` (Remote Services sobre DCs) | Reutilización anómala de tickets/hashes, ejecución remota WMI/RPC sobre controladores de dominio y toque de *Honeytokens* |
| **Defense Evasion & Exfiltration (`TA0005` / `TA0010`)** | `T1557` (NTLM Relay / Tampering), `T1562` (Impair Defenses), `T1048.003` (Exfiltration Over DNS) | Degradación de cifrado Kerberos, manipulación NTLM, alertas de salud ante detención de auditoría/sensor y exfiltración sobre DNS |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps, Admin y GRC)

Plan de habilitación progresiva de 30-60-90 días `[Decisión / Propuesta Editorial]` basado en recursos oficiales verificados `[Verificado MS Learn]`:

| Rol | Días 1–30 (Fundamentos) | Días 31–60 (Operación Autónoma) | Días 61–90 (Dominio Avanzado) |
|---|---|---|---|
| **Analista SOC L1** | Módulo Learn *Safeguard your environment with MDI*, operación del *Identity Security Dashboard* (`D-01`) y *Health issues* (`D-04`). | Triaje de incidentes de identidad en XDR (`D-02`), validación de *Honeytokens* y grupos sensibles (`D-03`) y consultas guiadas KQL. | Correlación inicial entre `IdentityLogonEvents` y `EntraIdSignInEvents`. |
| **Analista SOC L2 / Identity Responder** | Todo L1 + anatomía de alertas clásicas vs unificadas, atribuciones NNR y línea de tiempo de 180 días en *Identity page*. | Ejecución segura de **Identity Remediation Actions** (`D-05`) en AD/Entra/IdP, ajuste de alertas B-TP (`D-06`) y preparación **SC-200**. | Ejecución de playbooks críticos `AH-01` (DCSync/Golden Ticket), `AH-02` (AD CS) y `AH-03` (Honeytoken). |
| **Analista SOC L3 / ITDR Hunter** | Esquema completo `Identity*`, `EntraId*`, `ExposureGraph*` y nuevas detecciones 2026 (Diamond Ticket, ESC1/8/11, DPAPI, TAP). | Caza semanal de reconocimiento, Kerberoasting y protocolos inseguros (`S-02`, `S-04`) y análisis de *Attack paths* / *Identity Explorer* (`S-03`). | Diseño de *Custom detection rules*, liderazgo de ejercicios Purple Team de historias completas (`SM-01`) y simulacros `krbtgt` (`A-01`). |
| **Identity Platform / AD Admin** | Arquitectura del **sensor unificado v3.x**, requisitos de parches acumulativos (sep-2026+), memoria VM y cuenta `LocalSystem`. | Despliegue y migración sin caída desde v2.x a v3.x en DCs, AD FS, AD CS y Entra Connect (`S-06`, `AH-04`) y uso de `Test-MdiReadiness.ps1` (`T-01`). | Remediación estructural de hallazgos ISPA en *Secure Score* (`S-01`), gobernanza NHI/Agentes IA (`M-03`) y eliminación de NTLMv1/Simple Bind. |
| **Auditor GRC / CISO Office** | Comprensión de licenciamiento ITDR (E5 / Defender Suite / EMS E5) y modelo de resultados NIST CSF 2.0. | Revisión de permisos URBAC, *Identity scoping*, activaciones PIM y trazabilidad en *Action center* (`M-04`). | Supervisión ejecutiva de la iniciativa *Identity Security* (`M-02`), cobertura multi-IdP y preparación regulatoria ante incidentes Tier-0. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Actualizaciones Aplicadas tras Revalidación en Microsoft Learn (Noviembre 2026)

| Área Revalidada | Estado en Borradores Previos (`MSEOP-MD`) | Estado Oficial Verificado a Noviembre de 2026 (`[Verificado MS Learn]`) |
|---|---|---|
| **Arquitectura y Despliegue del Sensor Unificado v3.x** | Describía mayoritariamente el sensor clásico v2.x (`AATPSensor`, Npcap, `MDI Sizing Tool`, límite 350 sensores). | Consolidado el **sensor v3.x**: activación desde pestaña unificada `Sensor management`, actualización vía **Windows Update** (requiere CU sep-2026+, sensor `3.0.10+`), límite de **30% CPU y 1,5 GB RAM**, auditoría RPC automática desde `3.0.8+`, migración v2->v3 en **GA** (jul-2026, incl. WS2025), activación sin MDE en **GA** (oct-2026 comercial), activación automática con aviso de 30 días y capacidad de **1.000 sensores/workspace**. |
| **Cuentas de Servicio y Action Accounts (`LocalSystem` vs gMSA/DSA)** | Indicaba configurar y rotar cuentas gMSA/DSA como estándar general para todos los sensores. | En **sensor v3.x solo se admite `LocalSystem`** tanto para lectura AD como para remediación (no usa DSA ni gMSA). Documentado el prerrequisito obligatorio pre-migración de seleccionar *Automatically use the sensor's local system account* y la limpieza posterior de DSA/gMSA a nivel workspace tras migrar el 100% de sensores. |
| **Transición de Lateral Movement Paths (LMP)** | Trataba el widget y reporte clásico de *Lateral Movement Paths* como control activo semanal y mensual. | Documentado el aviso oficial **`MC1073068`**: desde mayo de 2025 MDI deshabilitó la recolección remota de administradores locales vía SAM-R, por lo que los mapas clásicos LMP dejaron de actualizarse; sustituidos operativamente por **Attack paths en Exposure Management** e **Identity Explorer** (Preview con *Sentinel Data Lake*). |
| **Remediación Multi-IdP y App Administrada Entra ID** | Limitaba las acciones de respuesta a AD y Entra ID básico. | Actualizado el alcance oficial de **Identity Remediation Actions** a Active Directory (solo sensores en DCs), Microsoft Entra ID (vía app administrada `60ca1954-583c-4d1f-86de-39d835f3e452`), **Okta, CyberArk Identity, SailPoint ISC** y apps SaaS (Google Workspace, Salesforce, Box), integradas con **Automatic Attack Disruption**. |
| **Postura, Risk Score, NHI / Agentes IA y Domain Investigation** | No incluía capacidades liberadas entre abril y octubre de 2026. | Incorporados **Identity Risk Score (0-100)** en GA (jun-2026), **Domain investigation page** en GA (jul-2026), **Coverage & Maturity** (sep-2026), inventario NHI con columna `Used by AI agents` y el rol `Agent ID Administrator` dentro de las etiquetas sensibles automáticas. |
| **Nuevas Detecciones 2026 y Esquema KQL** | Catálogo centrado en alertas clásicas y sin tablas nuevas de 2026. | Añadidas las nuevas alertas XDR de 2026 (**AD CS ESC1/ESC8/ESC11, Certighost CVE-2026-54121, Diamond Ticket, DPAPI master key, TAP sospechoso, MFA malicioso, Okta y SailPoint**), distinción de ajuste (*Exclusions* para clásicas vs *Alert tuning* para formato Defender) y tablas `IdentityAccountInfo` (GA), `IdentityEvents` (Preview) y `EntraIdSignInEvents` (GA oct-2026). |
| **Permisos Unified RBAC y Licenciamiento** | Citaba grupos heredados `Azure ATP` como predeterminados y solo el nombre *M365 E5 Security*. | Documentado que desde marzo de 2025 los nuevos tenants usan exclusivamente **Unified RBAC** (con soporte de *Identity scoping* por dominio AD), retiro de políticas de riesgo heredadas en Entra ID Protection (1-oct-2026) y renombramiento comercial a **Microsoft Defender Suite** (más M365 E7). |

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Técnica y de Gobierno |
|---|---|---|
| **Metas cuantitativas de SLA y KPIs (MTTA p50 < 10 min, MTTC p90 < 15 min, ISPA >= 85%, FP < 10%)** | `[Decisión / Propuesta Editorial]` | Microsoft Learn define los procedimientos de triaje y métricas de exposición, dejando la fijación de SLAs exactos al perfil de riesgo y cobertura horaria de cada SOC. |
| **Ventanas de activación JIT en Entra PIM (2 h Tier-0, 4 h Admin, 8 h L2/L3) y exigencia de estaciones PAW** | `[Decisión / Propuesta Editorial]` | Basado en las arquitecturas de referencia de acceso privilegiado de Microsoft, adaptado como política prescriptiva de separación de funciones para este marco. |
| **Modelo de Madurez ITDR de 5 niveles y plan formativo 30-60-90 días** | `[Decisión / Propuesta Editorial]` | Construcción consultiva propia alineada a *Coverage & Maturity* de Defender, el Microsoft Security Adoption Framework (SAF) y NIST CSF 2.0. |
| **Mapeo de subcategorías y evidencias hacia NIST CSF 2.0 (CSWP 29)** | `[Decisión / Propuesta Editorial]` | Como establece NIST CSWP 29, las herramientas tecnológicas no otorgan cumplimiento automático sino evidencia verificable para sustentar *outcomes* organizacionales. |
| **Frecuencia semestral de ejercicios Purple Team de historias completas y anual de doble rotación `krbtgt` simulada** | `[Decisión / Propuesta Editorial]` | Microsoft documenta las buenas prácticas previas a pruebas ofensivas contra MDI y la recuperación de AD; la cadencia semestral/anual obligatoria es una decisión de gobierno operativo. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
1. **Microsoft Defender for Identity operational guide (Overview)** — Resumen oficial de cadencias diarias, semanales, mensuales y trimestrales/ad-hoc: `https://learn.microsoft.com/en-us/defender-for-identity/ops-guide/ops-guide`
2. **Daily operational guide - Microsoft Defender for Identity** — Guía oficial de tareas diarias (Dashboard, triaje XDR, tuning, hunting y Health issues): `https://learn.microsoft.com/en-us/defender-for-identity/ops-guide/ops-guide-daily`
3. **What's new in Microsoft Defender for Identity** — Registro oficial de novedades verificadas hasta octubre/noviembre de 2026 (sensor v3.x sin MDE GA, activación automática, nuevas alertas AD CS/Kerberos/Entra/Okta, Identity Risk Score, Domain investigation): `https://learn.microsoft.com/en-us/defender-for-identity/whats-new`
4. **Deploy the Microsoft Defender for Identity sensor v3.x** — Requisitos oficiales de SO, parches acumulativos de septiembre de 2026, memoria VM, cuenta `LocalSystem` y auditoría RPC automática: `https://learn.microsoft.com/en-us/defender-for-identity/deploy/deploy-sensor-v3`
5. **Migrate from sensor v2.x to sensor v3.x** — Procedimiento oficial en GA de migración sin tiempo de inactividad desde el portal Defender: `https://learn.microsoft.com/en-us/defender-for-identity/deploy/migrate-to-sensor-v3`
6. **Identity remediation actions in Microsoft Defender** — Acciones de contención en AD, Entra ID (App ID administrada), Okta, CyberArk, SailPoint y apps SaaS, y su uso en *Automatic Attack Disruption*: `https://learn.microsoft.com/en-us/defender-for-identity/remediation-actions`
7. **Microsoft Defender for Identity's security posture assessments** — Las seis categorías oficiales de evaluaciones ISPA en Microsoft Secure Score y requisitos de sensores en AD CS / Entra Connect: `https://learn.microsoft.com/en-us/defender-for-identity/security-assessment`
8. **Defender for Identity entity tags in Microsoft Defender** — Configuración de etiquetas *Sensitive*, *Honeytoken* y *Exchange server*, y roles sensibles por defecto (AD, Entra incluyendo `Agent ID Administrator`, Okta, CyberArk, SailPoint): `https://learn.microsoft.com/en-us/defender-for-identity/entity-tags`
9. **Microsoft Defender for Identity health issues** — Catálogo completo de alertas de salud globales y por sensor (v2.x y v3.x) y pasos de resolución: `https://learn.microsoft.com/en-us/defender-for-identity/health-alerts`
10. **Microsoft Defender for Identity role groups & Unified RBAC** — Permisos mínimos en URBAC, transición desde grupos heredados y *Scoped access* por dominio AD: `https://learn.microsoft.com/en-us/defender-for-identity/role-groups`
11. **Unified risk signals in Microsoft Entra ID Protection** — Composición del riesgo de usuario combinando señales de MDI, MDE, MDCA, Purview y Entra ID: `https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-unified-risk`
12. **Best Practices before Offensive Security Testing for Microsoft Defender for Identity** — Guía oficial para ejecutar pruebas Purple Team mediante historias completas de ataque: `https://learn.microsoft.com/en-us/defender-for-identity/security-testing-best-practices`

### 15.2 Publicaciones Oficiales, Repositorios y Empleados de Microsoft
13. **Microsoft Defender for Identity Tools (`Test-MdiReadiness`)** — Repositorio oficial en GitHub con el script de validación de prerrequisitos y auditoría de dominio: `https://github.com/microsoft/Microsoft-Defender-for-Identity/tree/main/Test-MdiReadiness`
14. **Seamless Migration to the Unified MDI Sensor (V3) — Ronit Litinski (Microsoft Security Community)** — Webinar técnico del equipo de producto explicando la migración desde v2.x al sensor unificado v3.x: `https://www.youtube.com/watch?v=fp_JpsZ3Oos`
15. **Mark Morowczynski (Microsoft GHOST) — Identity & KQL Technical Content** — Publicaciones e investigaciones de respuesta e ingeniería KQL sobre identidad híbrida y Entra ID: `https://markmorow.com/content/`
16. **Welcome to the Microsoft Incident Response Ninja Hub — Emily Liu (Microsoft IR)** — Guías operativas de caza y respuesta ante compromisos de identidad y dominio del equipo Microsoft Incident Response: `https://techcommunity.microsoft.com/blog/microsoft-defender-experts/welcome-to-the-microsoft-incident-response-ninja-hub/4243594/replies/4245146`

### 15.3 Comunidad y MVPs de Seguridad de Microsoft
17. **Christopher Brumm (Microsoft Security MVP) — Identity & ITDR Security Archive** — Análisis profundos sobre seguridad de identidad híbrida, monitoreo ITDR y Microsoft Entra: `https://chris-brumm.com/archive/`
18. **Fabian Bader (Microsoft Security MVP) — Cloudbrothers Blog** — Investigación aplicada sobre Defender for Identity, Defender XDR, detecciones KQL y automatización PowerShell: `https://cloudbrothers.info/en/aboutme/`
19. **Michael Morten Sonne (Microsoft Security MVP) — Unified Identity Signals from Defender** — Guía técnica práctica sobre señales de riesgo unificadas entre MDI y Microsoft Entra ID Protection: `https://blog.sonnes.cloud/entra-id-protection-user-risk-with-unified-identity-signals-from-defender-is-here/`
20. **Thomas Naunheim (Microsoft Security MVP) — Cloud-Architekt Blog & Attack/Defense Playbook** — Investigación avanzada en identidades privilegiadas, identidades de carga de trabajo, agentes e ITDR: `https://www.cloud-architekt.net/blog/`

### 15.4 Marcos Normativos y Estándares de la Industria
21. **NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)** — Especificación oficial de funciones, categorías y resultados (*outcomes*) de ciberseguridad: `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`
22. **NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations** — Guía normativa de gestión y respuesta a incidentes alineada con NIST CSF 2.0: `https://csrc.nist.gov/pubs/sp/800/61/r3/final`

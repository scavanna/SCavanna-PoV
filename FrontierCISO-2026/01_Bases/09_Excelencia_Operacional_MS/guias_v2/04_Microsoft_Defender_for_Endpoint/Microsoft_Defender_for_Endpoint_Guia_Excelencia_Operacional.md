# Microsoft Defender for Endpoint (P1/P2) y Vulnerability Management — Guía Maestra de Excelencia Operacional

## 1. Portada y Ficha de Control Documental

| Atributo de Control | Detalle Documental |
|---|---|
| **Identificador del Módulo** | `04_Microsoft_Defender_for_Endpoint` |
| **Nombre Oficial Revalidado** | Microsoft Defender for Endpoint (P1/P2) y Vulnerability Management |
| **Categoría del Repositorio** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 — Edición Canónica Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (`2026-02-24 - MDE` + Anexo `26w01 - BNA MDE VDI`) + Revalidación activa contra Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **MDE Plan 2** (incluyendo **Defender Vulnerability Management núcleo**) está incluido en Microsoft 365 E5, Microsoft Defender Suite, Microsoft 365 E7 y Windows 10/11 Enterprise E5; **MDE Plan 1** está incluido en Microsoft 365 E3 y Windows Enterprise E3. Servidores y capacidades MDVM premium se licencian por separado `[Verificado MS Learn]` |
| **Portales Operativos Principales** | `https://security.microsoft.com` (Microsoft Defender portal — Endpoints, Exposure management y SecOps unificado), `https://intune.microsoft.com` (políticas de seguridad de endpoint), `https://admin.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Analistas SecOps (Tier 1 / Tier 2 / Tier 3), Incident Responders (DFIR), Endpoint Security Administrators, Administradores Intune/VDI, Security Architects y GRC |
| **Marcos de Referencia Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST SP 800-61 Rev. 3, Microsoft Zero Trust (Endpoints Pillar), CIS Controls v8, MITRE ATT&CK Enterprise y Microsoft Defender for Endpoint Security Operations Guide |

> **Convención obligatoria de evidencia:** Se emplea `[Verificado MS Learn]` exclusivamente para funcionalidades, licencias, rutas de consola, límites técnicos, reglas ASR, tablas KQL y procedimientos documentados por Microsoft a noviembre de 2026. Los acuerdos de nivel de servicio (SLA), metas numéricas de KPIs, matrices RACI, modelos de madurez consultivos y mapeos interpretativos a NIST CSF 2.0 se rotulan explícitamente con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Síntesis Ejecutiva

**Microsoft Defender for Endpoint (MDE)** es la plataforma empresarial unificada de protección de endpoints que integra en un agente sin sobrecarga de sensores adicionales (*built-in* en Windows y multiplataforma en macOS, Linux, iOS y Android) capacidades preventivas pre-brecha, detección y respuesta de endpoints (EDR) post-brecha, investigación y remediación automatizada, caza avanzada de amenazas y gestión continua de vulnerabilidades basada en riesgo (**Microsoft Defender Vulnerability Management — MDVM**) `[Verificado MS Learn]`.

Operado como pilar nativo dentro de **Microsoft Defender XDR** (`https://security.microsoft.com`), MDE aporta señales de salud, cumplimiento y nivel de riesgo del dispositivo en tiempo real a **Microsoft Intune** y **Microsoft Entra Conditional Access**, cerrando el ciclo de verificación explícita de **Zero Trust**: un endpoint comprometido o con controles manipulados puede ser aislado de la red y bloqueado simultáneamente del acceso a recursos corporativos en cuestión de segundos `[Verificado MS Learn]`. En evaluaciones independientes como *MITRE Engenuity ATT&CK Evaluations Enterprise*, la plataforma ha demostrado cobertura de detección a lo largo de todas las fases de la cadena de ataque, respaldando el retorno financiero documentado por Forrester TEI (242 % de ROI a tres años para el ecosistema Microsoft Defender) `[Verificado MS Learn]`.

La revalidación técnica a **noviembre de 2026** introduce actualizaciones críticas que corrigen manuales previos `[Verificado MS Learn]`:
1. **Catálogo vigente de 19 reglas Attack Surface Reduction (ASR):** Se corrige el conteo desactualizado de "13 reglas" presente en borradores previos por las **19 reglas ASR oficiales** documentadas en Microsoft Learn (divididas en **3 Standard protection rules** y **16 Other ASR rules**), incorporando el requisito de aprobación de administrador para *Unblock* en modo *Warn* (plataforma `4.18.26060+`) y las reglas que no admiten modo *Warn*.
2. **Integración de AIR en la pila Antivirus (1 de septiembre de 2026):** Desde el 1 de septiembre de 2026, *Automated Investigation and Response (AIR)* en MDE dejó de ejecutarse como una experiencia de investigación separada o con disparo manual: sus capacidades corren de forma nativa y automática dentro de la pila predeterminada de Microsoft Defender Antivirus (usando escaneo completo bajo demanda cuando se requiere inspección manual), manteniendo los niveles de automatización por *Device group* y la auditoría/aprobación en el *Action Center*.
3. **Convergencia de MDVM bajo Exposure Management:** Las vistas de gestión de vulnerabilidades residen ahora integradas dentro de **Exposure management** en el portal Defender, distinguiendo nítidamente el alcance **Core** (incluido en MDE Plan 2 / M365 E5) frente a las **6 capacidades Premium** del *MDVM Add-on / Standalone* (y *Defender for Servers Plan 2*).

### 2.2 Comparativa de Licenciamiento y Capacidades: AV vs. MDE P1 vs. MDE P2 vs. MDVM Add-on

| Capacidad Técnica | Defender AV (Windows) | MDE Plan 1 (M365 E3 / Win E3) | MDE Plan 2 (M365 E5 / Defender Suite / Win E5) | MDVM Add-on / Standalone (y Defender for Servers P2) | Estado |
|---|---|---|---|---|---|
| **Next-Generation Protection (NGAV + Cloud MAPS + Behavior)** | Incluido (local) | Incluido + gestión central | Incluido + gestión central | Requiere AV activo para bloqueo de apps | `[Verificado MS Learn]` |
| **Attack Surface Reduction (19 reglas ASR en Windows)** | Local (PS/GPO) | Centralizado + telemetría/reportes | Centralizado + telemetría/reportes + KQL | — | `[Verificado MS Learn]` |
| **Device Control (USB, Bluetooth, impresoras) y Host Firewall** | Básico OS | Incluido | Incluido | — | `[Verificado MS Learn]` |
| **Tamper Protection / Controlled Configuration** | Básico | Incluido (empresarial) | Incluido + caza KQL `TamperingAttempt` | — | `[Verificado MS Learn]` |
| **Acciones manuales básicas (Isolate device, Run AV scan, Quarantine, IoCs)** | No | Incluido | Incluido + Contain device/IP/user y Restrict app execution | — | `[Verificado MS Learn]` |
| **EDR profundo (6 meses de timeline de dispositivo + árbol de procesos)** | No | No | **Incluido** | — | `[Verificado MS Learn]` |
| **EDR in Block Mode (coexistencia con AV primario de terceros)** | No | No | **Incluido** | — | `[Verificado MS Learn]` |
| **Remedición automatizada (AIR en pila AV + niveles por Device group)** | No | No | **Incluido** | — | `[Verificado MS Learn]` |
| **Live Response (shell remoto interactivo + Library + scripts)** | No | No | **Incluido** | — | `[Verificado MS Learn]` |
| **Advanced Hunting KQL (30 días de eventos crudos)** | No | No | **Incluido** | — | `[Verificado MS Learn]` |
| **Threat Analytics y Device Discovery (modo Standard activo)** | No | No | **Incluido** | Device Discovery en Standalone | `[Verificado MS Learn]` |
| **MDVM Core** (inventario SW, CVEs, priorización por riesgo, tareas Intune) | No | No | **Incluido** | Incluido en Standalone | `[Verificado MS Learn]` |
| **MDVM Premium** (Baselines CIS/STIG, bloqueo de apps vulnerables, extensiones de navegador, certificados digitales, recursos compartidos de red, hardware/firmware) | No | No | No (requiere Add-on) | **Incluido** | `[Verificado MS Learn]` |

> **Aclaración crítica sobre Servidores `[Verificado MS Learn]`:** Las licencias por usuario (Microsoft 365 E3/E5, Microsoft Defender Suite o MDE P1/P2 standalone de cliente) cubren hasta 5 dispositivos cliente concurrentes por usuario licenciado, pero **no incluyen licenciamiento para Windows Server ni Linux Server**; los servidores deben licenciarse mediante **Microsoft Defender for Servers Plan 1 o Plan 2** (en Microsoft Defender for Cloud) o licencias específicas de servidor, con excepción de hosts multi-sesión de Windows 10/11 Enterprise en Azure Virtual Desktop cubiertos por licencias de usuario elegibles.

**Prerrequisitos técnicos verificados `[Verificado MS Learn]`:**
- Conectividad HTTPS saliente (puerto 443 vía WinHTTP) hacia los endpoints del servicio MDE (preferentemente *Streamlined connectivity* `*.endpoint.security.microsoft.com`, sin inspección TLS/SSL ni proxies autenticados sobre el tráfico del sensor `MsSense.exe`).
- Microsoft Defender Antivirus en **Active mode** con *Real-time protection* y *Cloud-delivered protection* habilitados (requisito indispensable para el funcionamiento de las 19 reglas ASR y del bloqueo de aplicaciones vulnerables; cuando existe un AV primario de terceros y Defender AV pasa a *Passive mode*, habilitar obligatoriamente **EDR in block mode**).
- Versiones de plataforma (`Platform`) y motor (`Engine`) de Microsoft Defender Antivirus con antigüedad no mayor a dos versiones mensuales respecto a la última publicada.
- Integración activa con **Microsoft Intune** (`Settings > Endpoints > General > Advanced features > Microsoft Intune connection = On`) para políticas de cumplimiento y riesgo de dispositivo en Acceso Condicional.

---

## 3. Arquitectura Operativa, Componentes Clave, Reglas ASR y Anexo VDI No Persistente

### 3.1 Componentes Operativos e Integraciones en el Ecosistema

| Componente | Función Operativa | Ruta en `security.microsoft.com` / `intune.microsoft.com` | Integraciones | Estado |
|---|---|---|---|---|
| **Sensor EDR & Timeline de Dispositivo** | Recolección continua de procesos, red, archivos, registro, cargas DLL, inicios de sesión y kernel con retención de **6 meses** en la vista de línea de tiempo del dispositivo y **30 días** en tablas crudas KQL, enriquecida con etiquetas de sensibilidad de Microsoft Purview. | `Assets > Devices > [Dispositivo] > Timeline` | Defender XDR, Purview Information Protection, Microsoft Sentinel | `[Verificado MS Learn]` |
| **Next-Generation Protection + AIR Integrado** | Protección en tiempo real, monitoreo conductual, protección en la nube (MAPS) y capacidades de investigación/remediación automática integradas en la pila AV (desde el 1-sep-2026), gobernadas por niveles de automatización en *Device groups*. | `System > Settings > Endpoints > Rules > Device groups` y `Actions & submissions > Action center` | Action Center, Threat Intelligence, Indicadores IoC | `[Verificado MS Learn]` |
| **Attack Surface Reduction (19 Reglas ASR) + Web/Network Protection** | Endurecimiento pre-ejecución en Windows contra robo de credenciales LSASS, abuso de Office/macros, scripts ofuscados, persistencia WMI, drivers vulnerables (BYOVD), webshells Exchange y reinicio en modo seguro. | `intune.microsoft.com > Endpoint security > Attack surface reduction` y `Reports > Endpoints > Attack surface reduction rules` | Microsoft Intune, Defender Portal, Group Policy, ConfigMgr | `[Verificado MS Learn]` |
| **Tamper Protection & Controlled Configuration** | Bloqueo contra desactivación maliciosa de protección en tiempo real, nube, IOAV, actualizaciones y listas de exclusiones administradas (en Windows activo/pasivo, macOS `Audit`/`Block` y Linux `Audit` Preview), con *Troubleshooting mode* temporal auditado. | `System > Settings > Endpoints > General > Advanced features` / Intune Endpoint Security | MDVM Recommendations, Advanced Hunting (`TamperingAttempt`) | `[Verificado MS Learn]` |
| **Live Response & Investigation Package** | Consola interactiva remota en la nube para triaje forense en vivo, descarga de artefactos en segundo plano (`getfile ... &`), ejecución controlada de scripts desde biblioteca central y recolección de paquete forense completo (Autoruns, Prefetch, Event Logs, SMB, red). | `Assets > Devices > [Dispositivo] > Initiate live response session` / `Collect investigation package` | Unified RBAC (`Basic` / `Advanced live response`), `Library management` | `[Verificado MS Learn]` |
| **Arsenal de Contención de Red e Identidad en Endpoint** | *Isolate device* (total o selectivo conservando Outlook/Teams, más *Isolation exclusions*), *Contain device* (para activos no incorporados), *Contain IP*, *Contain user* / *Proactive user containment*, *Restrict app execution* y *GPO/Safeboot hardening*. | `Assets > Devices > [Dispositivo] > ... (Actions)` y *Automatic Attack Disruption* | Automatic Attack Disruption, Defender for Identity, Entra ID | `[Verificado MS Learn]` |
| **Defender Vulnerability Management (MDVM)** | Descubrimiento continuo sin escáneres externos de software, CVEs, configuraciones inseguras, puntaje de exposición (0-100, menor es mejor), excepciones de CVE y flujo de remediación integrado con *Security Tasks* en Intune. | `Exposure management > Vulnerability management > Dashboard / Weaknesses / Remediation` | Microsoft Security Exposure Management, Microsoft Intune, Defender for Servers | `[Verificado MS Learn]` |
| **Standard Device Discovery** | Sondeo pasivo y activo inteligente desde endpoints Windows incorporados para descubrir estaciones, servidores, impresoras y dispositivos IoT/OT no administrados en subredes corporativas. | `System > Settings > Device discovery` y `Assets > Devices` (`Can be onboarded`) | Inventario de activos, Exposure Graph y flujos de incorporación | `[Verificado MS Learn]` |

### 3.2 Catálogo Oficial Revalidado de las 19 Reglas Attack Surface Reduction (ASR)

> **Corrección documental explícita (Noviembre 2026):** Textos previos del bloque fuente referenciaban "13 reglas ASR". Microsoft Learn documenta oficialmente **19 reglas ASR** exclusivas para Windows, clasificadas en **3 reglas de protección estándar** (recomendadas en modo `Block` de inmediato salvo excepciones documentadas) y **16 reglas adicionales** (que requieren validación previa en modo `Audit`) `[Verificado MS Learn]`.
>
> **Modos y reglas operativas críticas `[Verificado MS Learn]`:**
> - Códigos oficiales de modo: `0 = Disabled/Off` (puede causar conflictos entre políticas), `1 = Block`, `2 = Audit`, `5 = Not configured` (sin conflicto), `6 = Warn` (permite *Unblock* por 24 h, disponible desde Windows 10 1809+, no soportado en Configuration Manager).
> - **Cambio 2026 (Plataforma `4.18.26060+`):** Se requiere **aprobación de administrador** para usar la opción *Unblock* cuando una regla está en modo `Warn`.
> - **Precedencia ante conflictos:** Si MDM (Intune) y Group Policy aplican modos distintos sobre la misma regla, **Group Policy prevalece por defecto** salvo que se habilite `MDMWinsOverGP` (Policy CSP) o *Controlled configuration*.
> - **Exclusiones:** Evitar exclusiones globales; aplicar siempre **exclusiones por regla ASR específica (*Per-ASR rule exclusions*)** mediante Intune o Endpoint Security Policies en el portal Defender. Nótese además que varias reglas críticas (como LSASS, WMI persistence e inyección Office) **no** respetan las exclusiones de archivo/carpeta de Defender Antivirus, aunque todas respetan exclusiones de proceso de Defender AV.

| # | Categoría Oficial | Nombre de la Regla ASR en Microsoft Intune | GUID Oficial | Soporta Warn | Acción KQL (`DeviceEvents`) |
|---|---|---|---|---|---|
| 1 | **Standard protection** | Block abuse of exploited vulnerable signed drivers (Device) | `56a863a9-875e-4185-98a7-b882c64b5ce5` | Sí | `AsrVulnerableSignedDriver*` |
| 2 | **Standard protection** | Block credential stealing from the Windows local security authority subsystem (`lsass.exe`) *(Nota: redundante si LSA Protection + Credential Guard están activos)* | `9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2` | **No** | `AsrLsassCredentialTheft*` |
| 3 | **Standard protection** | Block persistence through WMI event subscription *(probar en Audit si se usa ConfigMgr)* | `e6db77e5-3df2-4cf1-b95a-636979351e5b` | Sí | `AsrPersistenceThroughWmi*` |
| 4 | Other ASR rules | Block Adobe Reader from creating child processes | `7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c` | Sí | `AsrAdobeReaderChildProcess*` |
| 5 | Other ASR rules | Block all Office applications from creating child processes | `d4f940ab-401b-4efc-aadc-ad5f3c50688a` | Sí | `AsrOfficeChildProcess*` |
| 6 | Other ASR rules | Block executable content from email client and webmail | `be9ba2d9-53ea-4cdc-84e5-9b1eeee46550` | Sí | `AsrExecutableEmailContent*` |
| 7 | Other ASR rules | Block executable files from running unless they meet a prevalence, age, or trusted list criterion *(requiere Cloud Protection)* | `01443614-cd74-433a-b99e-2ecdc07bfc25` | Sí | `AsrUntrustedExecutable*` |
| 8 | Other ASR rules | Block execution of potentially obfuscated scripts *(requiere Cloud Protection + AMSI)* | `5beb7efe-fd9a-4556-801d-275e5ffc04cc` | Sí | `AsrObfuscatedScript*` |
| 9 | Other ASR rules | Block JavaScript or VBScript from launching downloaded executable content | `d3e037e1-3eb8-44c8-a917-57927947596d` | Sí | `AsrScriptExecutableDownload*` |
| 10 | Other ASR rules | Block Office applications from creating executable content | `3b576869-a4ec-4529-8536-b80a7769e899` | Sí | `AsrExecutableOfficeContent*` |
| 11 | Other ASR rules | Block Office applications from injecting code into other processes | `75668c1f-73b5-4cf0-bb93-3ecf5cb7cc84` | **No** | `AsrOfficeProcessInjection*` |
| 12 | Other ASR rules | Block Office communication application from creating child processes (Outlook) | `26190899-1602-49e8-8b27-eb1d0a1ce869` | Sí | `AsrOfficeCommAppChildProcess*` |
| 13 | Other ASR rules | Block process creations originating from PSExec and WMI commands *(incompatible con cliente ConfigMgr si se despliega fuera de él)* | `d1e49aac-8f56-4280-b9ba-993a6d77406c` | Sí | `AsrPsexecWmiChildProcess*` |
| 14 | Other ASR rules | Block rebooting machine in Safe Mode | `33ddedf1-c6e0-47cb-833e-de6133960387` | Sí | `AsrSafeModeReboot*` |
| 15 | Other ASR rules | Block untrusted and unsigned processes that run from USB | `b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4` | Sí | `AsrUntrustedUsbProcess*` |
| 16 | Other ASR rules | Block use of copied or impersonated system tools | `c0033c00-d16d-4114-a5a0-dc9b3a7d2ceb` | Sí | `AsrAbusedSystemTool*` |
| 17 | Other ASR rules | Block Webshell creation for Servers *(solo servidores Microsoft Exchange)* | `a8f5898e-1dc8-49a9-9878-85004b8a61e6` | N/A | N/A |
| 18 | Other ASR rules | Block Win32 API calls from Office macros | `92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b` | Sí | `AsrOfficeMacroWin32ApiCalls*` |
| 19 | Other ASR rules | Use advanced protection against ransomware *(requiere Cloud Protection)* | `c1db55ab-c21a-4637-bb3f-a12568109d35` | Sí | `AsrRansomware*` |

### 3.3 Arquitectura y Estándar Operativo para Entornos VDI No Persistentes (AVD, Citrix MCS/PVS, VMware Horizon)

En infraestructuras de escritorios virtuales efímeros o *pooled*, un despliegue convencional de MDE provoca duplicación masiva de registros, tormentas de CPU en el arranque y pérdida de evidencia forense al destruirse la sesión. Todo despliegue VDI no persistente debe cumplir estos 6 controles `[Verificado MS Learn]`:

1. **Prohibición absoluta de incorporar la imagen maestra (*Golden Image*):** Jamás ejecutar el script de onboarding en la imagen base, plantillas internas ni réplicas (ej. `cp-template` / `cp-replica` en VMware Instant Clones), ya que todos los clones heredarían el mismo `senseGuid` y colapsarían bajo una única entrada en el portal `[Verificado MS Learn]`. Si una imagen maestra fue incorporada accidentalmente, ejecutar *offboarding*, verificar `sc query sense` detenido y limpiar los datos de registro bajo `SYSTEM` (`PsExec.exe -s cmd.exe`): borrar `C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection\Cyber\*.*` y las claves `senseGuid`, `senseId` y subvalores asociados bajo `HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection` antes de sellar `[Verificado MS Learn]`.
2. **Modelo *Single Entry for Each Device*:** Descargar el paquete **VDI onboarding scripts for non-persistent endpoints** (`security.microsoft.com > Settings > Endpoints > Onboarding`) y copiar `Onboard-NonPersistentMachine.ps1` junto con `WindowsDefenderATPOnboardingScript.cmd` en `C:\Windows\System32\GroupPolicy\Machine\Scripts\Startup` de la imagen maestra, configurando la GPO de inicio para ejecutar `Onboard-NonPersistentMachine.ps1` **únicamente después de que la VM aprovisionada reciba su nombre de host final y complete su reinicio definitivo** (o mediante script post-sincronización *ClonePrep* en Horizon Instant Clones) `[Verificado MS Learn]`.
3. **Etiquetado e higiene de inventario:** Estampar en registro `HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection\DeviceTagging` (`VDI = NonPersistent`) y activar *Hide potential duplicate device records* en `Settings > Endpoints > Advanced features` `[Verificado MS Learn]`.
4. **Inteligencia de seguridad compartida y optimización de CPU:** Antes de sellar la imagen maestra, ejecutar manualmente la tarea programada *Windows Defender Cache Maintenance*; en entornos de alta densidad (Citrix MCS/PVS, Horizon), configurar un recurso compartido UNC central (`SharedSignaturesPath` / GPO *Define security intelligence location for VDI clients*) con definiciones pre-extraídas cada hora, aleatorizar tareas programadas (`SchedulerRandomizationTime 30`) y limitar `ScanAvgCPULoadFactor` a 25–30 % `[Decisión / Propuesta Editorial]`.
5. **Exclusiones obligatorias de contenedores de perfil (FSLogix y vDisk):** Configurar desde el día 1 exclusiones específicas para discos de perfil `*.VHD` y `*.VHDX` de **FSLogix** (`%TEMP%\*.VHD(X)`, `%Windir%\TEMP\*.VHD(X)`, `%ProgramData%\FSLogix\Cache\*`, `%ProgramData%\FSLogix\Proxy\*` y ruta SMB del perfil) y cachés de escritura de Citrix PVS, evitando pantallas negras y demoras críticas de inicio de sesión `[Verificado MS Learn]`.
6. **Adaptación de Respuesta a Incidentes en máquinas efímeras:** Ante cualquier alerta alta o crítica en un host `VDI=NonPersistent`, el analista SOC L2 debe disparar de inmediato **Collect investigation package** e iniciar sesión **Live Response** (`getfile`, `processes`, `connections`) **antes** de que el usuario cierre sesión o el pool recicle la máquina virtual, manteniendo la telemetría histórica sincronizada en Microsoft Sentinel `[Decisión / Propuesta Editorial]`.

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Segregación de Permisos en Microsoft Defender Unified RBAC para Endpoints y MDVM

| Rol Operativo | Nivel SOC | Permisos Clave en Unified RBAC / Intune | Estrategia PIM / JIT y Segmentación | Responsabilidad Principal | Estado |
|---|---|---|---|---|---|
| **Endpoint SOC Operator** | Tier 1 (L1) | `Security operations > Security data basics (Read)`, `Alerts (Manage)`, `Vulnerability management (Read)`, `Execute query/soft actions`. | Permanente en grupo Entra con alcance restringido a *Device groups* asignados. | Triaje de incidentes de endpoint, clasificación inicial, solicitud de paquetes de investigación y escalamiento sin capacidad de aislar servidores ni usar Live Response. | `[Decisión / Propuesta Editorial]` |
| **Endpoint Incident Responder** | Tier 2 (L2) | Suma `Response (Manage)`, `Execute hard actions`, `Basic live response (Manage)`, `File collection (Manage)`. | Elegible en **Entra ID PIM** (máx. 8 h por guardia, MFA FIDO2/Passkey). | Aislamiento/contención de equipos, aprobación de acciones en Action Center, *Live Response* básico (solo comandos de lectura y `getfile`) y envíos WDSI. | `[Decisión / Propuesta Editorial]` |
| **Senior DFIR & Threat Hunter** | Tier 3 (L3) | Suma `Advanced live response (Manage)` y gestión de *Custom detections*; subida de scripts mediante `Library management`. | Elegible en **Entra ID PIM** (máx. 4 h con ticket de incidente crítico aprobado). | Ejecución remota de scripts firmados (`run`), remediación quirúrgica de entidades (`remediate`), caza KQL avanzada y análisis de artefactos forenses. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Endpoint Security Administrator** | Ingeniería / SecAdmin | `Authorization and settings > Core security settings (Manage)` + rol **Endpoint Security Manager** en Microsoft Intune. | Estricto **JIT en PIM** (máx. 4 h con cambio aprobado en CAB). | Onboarding/offboarding (incluyendo VDI), políticas AV/ASR/Firewall/Device Control, *Tamper Protection* / *Troubleshooting mode*, *Device groups* e indicadores IoC. | `[Verificado MS Learn]` |
| **Vulnerability & Exposure Lead** | Postura / VM | `Security posture > Vulnerability management (Read & Manage)` y `Exposure Management (Manage)` (solicitud de remediación y excepciones CVE). | Asignación controlada por rol; aprobación formal requerida para *CVE exceptions*. | Priorización de CVEs explotados, creación de *Security Tasks* hacia Intune, seguimiento de SLA de parcheo y evaluación de líneas base CIS/STIG. | `[Verificado MS Learn]` |
| **Auditor GRC / Compliance** | Gobierno y Auditoría | Entra ID *Security Reader* o rol URBAC de solo lectura (`Security data basics Read` + `Security posture Read` + `Authorization Read-only`). | Permanente de solo lectura sin acceso a *Live Response* ni *File collection*. | Verificación independiente de cobertura de sensores, efectividad ASR, Tamper Protection y evidencias NIST CSF 2.0. | `[Decisión / Propuesta Editorial]` |

> **Controles críticos de seguridad sobre Live Response `[Verificado MS Learn]`:**
> 1. Habilitar por separado *Live response* para estaciones y *Live response for servers* en `Settings > Endpoints > General > Advanced features`.
> 2. Mantener **deshabilitada** la opción *Allow unsigned script execution* en producción, exigiendo que todo script PowerShell cargado en la biblioteca esté firmado digitalmente por la PKI interna.
> 3. El botón de carga directa de archivos a la biblioteca desde una sesión activa requiere el permiso `Manage Security Settings`; para segregación de funciones, gestione el catálogo de scripts aprobados desde la página dedicada **Library management**.

---

## 5. Cadencia Operativa Diaria

### D-01 — Triaje de Incidentes y Alertas EDR / AV en la Cola Unificada (con Contexto de Sensibilidad de Datos)
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `DE.CM-09`, `DE.AE-02`, `RS.AN-03` | MITRE: Execution / Privilege Escalation / Credential Access (TA0002 / TA0004 / TA0006).
- **Procedimiento:**
  1. Filtrar incidentes de las últimas 24 h con `Service source = Microsoft Defender for Endpoint`, `Severity = High, Medium` y `Status = New, In progress` `[Verificado MS Learn]`.
  2. Priorizar inmediatamente incidentes que involucren etiquetas `VDI=NonPersistent` (por volatilidad de evidencia), activos críticos o dispositivos con columna **Data sensitivity** (etiquetas confidenciales de Microsoft Purview) `[Verificado MS Learn]`.
  3. Inspeccionar el árbol de procesos y la pestaña **Timeline** del dispositivo para distinguir actividad post-brecha real de herramientas administrativas legítimas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Incidentes asignados y documentados dentro del SLA interno (Crítico < 15 min, Alto < 1 h) `[Decisión / Propuesta Editorial]`.

### D-02 — Revisión y Aprobación de Acciones en Action Center (Pila AV/AIR y Remediaciones Manuales)
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Actions & submissions > Action center` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `RS.MI-01`, `RS.MI-02` | MITRE: Execution / Persistence.
- **Procedimiento:**
  1. Revisar la pestaña **Pending** para grupos configurados en *Semi-automation* (ej. controladores de dominio o servidores críticos), aprobando o rechazando acciones de cuarentena de archivos, detención de procesos/servicios o limpieza de registro/tareas programadas antes de la expiración de 7 días `[Verificado MS Learn]`.
  2. Auditar la pestaña **History** validando que los grupos en *Full automation* estén ejecutando remediaciones automáticas de la pila AV/AIR sin afectar software de línea de negocio (usando *Undo* si corresponde) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación diaria de *Action Center* sin acciones críticas pendientes > 4 horas `[Decisión / Propuesta Editorial]`.

### D-03 — Monitoreo Inmediato de Intentos de Manipulación (*Tamper Protection* y Desactivación de Sensor)
- **Consola / Ruta:** `Incidents & alerts > Alerts` y *Advanced hunting* (`ActionType == "TamperingAttempt"`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3.
- **Alineación:** NIST `PR.PS-05`, `DE.CM-09` | MITRE: Defense Evasion — Impair Defenses (T1562.001).
- **Procedimiento:**
  1. Tratar toda alerta *Tamper Protection bypass* o *Tampering with the Microsoft Defender for Endpoint sensor* como posible preludio de ransomware operado por humanos `[Verificado MS Learn]`.
  2. Ejecutar consulta diaria sobre `DeviceEvents | where ActionType == "TamperingAttempt"` para capturar intentos bloqueados que no generaron alerta por sí solos `[Verificado MS Learn]`.
  3. Verificar si el dispositivo tenía *Troubleshooting mode* autorizado por ticket de cambio; en caso contrario, aislar el equipo e investigar la cuenta ejecutora `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de eventos de *tampering* conciliados contra ventanas de mantenimiento aprobadas.

### D-04 — Control Diario de Salud de Sensores EDR y Actualización de Microsoft Defender Antivirus
- **Consola / Ruta:** `security.microsoft.com > Reports > Endpoints > Device health > Sensor health & OS` y `Microsoft Defender Antivirus health` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator.
- **Alineación:** NIST `DE.CM-09`, `PR.PS-02` | MITRE: Defense Evasion.
- **Procedimiento:**
  1. Identificar dispositivos con estado de sensor `Misconfigured`, `Inactive` (> 7 días) o `Impaired communications`, y diagnosticar con **MDE Client Analyzer** cuando persista fallo de comunicación `[Verificado MS Learn]`.
  2. Revisar en **Microsoft Defender Antivirus health** que las versiones de *Platform*, *Engine* y *Security intelligence* estén al día (nunca > 2 versiones atrás) y que los equipos sin AV de terceros operen en **Active mode** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de salud con > 95 % de sensores activos saludables y tickets de remediación para fallos silenciosos `[Decisión / Propuesta Editorial]`.

### D-05 — Gestión Estructurada de Falsos Positivos / Negativos (Marco de 5 Pasos y WDSI)
- **Consola / Ruta:** `Actions & submissions > Submissions` y `https://www.microsoft.com/wdsi/filesubmission` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Administrator.
- **Alineación:** NIST `DE.AE-02`, `RS.IM-01`.
- **Procedimiento:**
  1. Identificar la fuente exacta de detección (`Antivirus`, `EDR`, `ASR`, `Custom TI`, `Custom detection`) `[Verificado MS Learn]`.
  2. Enviar muestras o hashes a Microsoft (`Submissions` o portal WDSI; para detecciones comportamentales sin archivo recolectar `MpSupport.cab` con `MpCmdRun.exe -GetFiles`) `[Verificado MS Learn]`.
  3. Si se requiere mitigación temporal para una aplicación legítima firmada/verificada, priorizar un **Allow Indicator** por hash SHA-256 o una **exclusión por regla ASR específica**, evitando exclusiones amplias de carpeta en el antivirus `[Verificado MS Learn]`.
- **Evidencia Auditable:** ID de envío en *Submissions* y justificación auditada de cualquier indicador *Allow*.

### D-06 — Seguimiento Diario de Amenazas de Alto Impacto en *Threat Analytics* y *Exposure Score*
- **Consola / Ruta:** `Threat intelligence > Threat analytics` y `Exposure management > Vulnerability management > Dashboard` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Vulnerability Lead.
- **Alineación:** NIST `ID.RA-01`, `ID.RA-05` | MITRE: Exploitation for Client Execution (T1203).
- **Procedimiento:**
  1. Revisar en **Threat analytics** la tabla *High-impact threats* ordenada por dispositivos con alertas activas o vulnerables `[Verificado MS Learn]`.
  2. Monitorear saltos súbitos (> 3 puntos) en el **Exposure Score** organizacional (0–100, menor es mejor) causados por nuevas vulnerabilidades zero-day o activos recién descubiertos `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario de variación de *Exposure Score* y alertas tempranas emitidas a Parcheo/IT.

### D-07 — Verificación de Solicitudes de Desbloqueo ASR (*Warn Mode Admin Approval*) y Eventos Bloqueados
- **Consola / Ruta:** `Reports > Endpoints > Attack surface reduction rules` y `Advanced hunting` (`ActionType startswith "Asr"`) `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / SOC L1.
- **Alineación:** NIST `PR.PS-05` | MITRE: Execution / Credential Access.
- **Procedimiento:**
  1. Revisar bloqueos de reglas ASR y solicitudes de desbloqueo temporal (*Unblock* en modo `Warn`, sujetas a aprobación de administrador desde plataforma `4.18.26060+`) `[Verificado MS Learn]`.
  2. Confirmar que las 3 *Standard protection rules* y las reglas críticas de Office/scripts permanezcan en modo `Block` sin regresión accidental a `Audit` por conflicto de GPO `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consulta diaria de eventos ASR y registro de aprobaciones/rechazos de *Unblock*.

### D-08 — Cierre Diario de Guardia, Seguimiento de Dispositivos Aislados y Traspaso de Turno
- **Consola / Ruta:** `Action center > History` (filtro `Isolate device`) + Bitácora SOC `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `RS.CO-02`, `RC.RP-05`.
- **Procedimiento:** Conciliar al cierre de cada turno la nómina de dispositivos actualmente en aislamiento de red o contención, su estado de investigación forense y el contacto con el propietario del activo, transfiriendo formalmente los casos abiertos al turno entrante `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Lista conciliada de equipos aislados y acta de cambio de guardia.

---

## 6. Cadencia Operativa Semanal

### S-01 — Priorización y Emisión de *Security Tasks* para CVEs Críticos con Exploit Activo (MDVM)
- **Consola / Ruta:** `security.microsoft.com > Exposure management > Vulnerability management > Weaknesses` y `Recommendations` `[Verificado MS Learn]`.
- **Rol Responsable:** Vulnerability & Exposure Lead / Endpoint Security Admin.
- **Alineación:** NIST `ID.RA-01`, `PR.PS-02`, `RS.MI-03` | MITRE: Exploitation (T1190, T1203, T1068).
- **Procedimiento:**
  1. Filtrar en **Weaknesses** por `Severity = Critical, High` combinado con `Exploit available = Yes` (y amenazas activas / CISA KEV), ordenando por número de dispositivos expuestos `[Verificado MS Learn]`.
  2. Abrir la recomendación asociada y seleccionar **Request remediation** para generar automáticamente una **Security Task** en Microsoft Intune con fecha límite acorde a criticidad `[Verificado MS Learn]`.
  3. Si existe impedimento inmediato de parcheo, evaluar mitigación compensatoria (regla ASR o *Block vulnerable applications* si se dispone de MDVM Add-on y Defender AV en modo activo) `[Verificado MS Learn]`.
- **Evidencia Auditable:** *Remediation activities* activas en MDVM vinculadas a *Security Tasks* en Intune.

### S-02 — Revisión de Reportes ASR, Web Protection y Progresión Controlada `Audit -> Warn -> Block`
- **Consola / Ruta:** `Reports > Endpoints > Attack surface reduction rules` y `Web protection` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / Security Architect.
- **Alineación:** NIST `PR.PS-01`, `PR.PS-05` | MITRE: Initial Access / Execution / C2.
- **Procedimiento:**
  1. Analizar archivos y procesos legítimos que dispararon eventos `Audited` en las 19 reglas ASR durante la última semana, diseñando únicamente **exclusiones por regla ASR específica** con datos reales del reporte `[Verificado MS Learn]`.
  2. Promover a modo `Warn` o `Block` aquellas reglas que completaron al menos 14–30 días en `Audit` sin impacto operativo no mitigado (recordando que LSASS `9e6c4e1f-...` e inyección Office `75668c1f-...` pasan directo a `Block` al no soportar `Warn`) `[Verificado MS Learn]`.
  3. Revisar en **Web protection report** bloqueos de *SmartScreen*, *Network Protection* e indicadores URL/IP personalizados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Plan semanal de progresión ASR actualizado y reporte de bloqueos web.

### S-03 — Threat Hunting Semanal sobre Telemetría de Endpoint (Procesos, Red, Archivos y Persistencia)
- **Consola / Ruta:** `Investigation & response > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / SOC L3.
- **Alineación:** NIST `DE.CM-09`, `DE.AE-02` | MITRE: Execution / Persistence / Credential Access / Lateral Movement.
- **Procedimiento:**
  1. Ejecutar hipótesis semanales sobre `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceFileEvents`, `DeviceRegistryEvents` y `DeviceImageLoadEvents` buscando abuso de *LOLBins* (`rundll32`, `regsvr32`, `mshta`, `certutil`, `wmic`), tareas programadas anómalas, carga lateral de DLLs y conexiones SMB/RDP inusuales `[Verificado MS Learn]`.
  2. Incluir búsquedas específicas sobre el pool `VDI=NonPersistent` para detectar herramientas de volcado de credenciales o túneles salientes efímeros `[Decisión / Propuesta Editorial]`.
  3. Promover hallazgos confirmados a *Custom detection rules* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consultas guardadas, bitácora de cacería semanal e incidentes/reglas generados.

### S-04 — Higiene de Inventario, *Standard Device Discovery*, Equipos Inactivos y Desduplicación VDI
- **Consola / Ruta:** `System > Settings > Device discovery` y `Assets > Devices` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / IT Operations.
- **Alineación:** NIST `ID.AM-01`, `DE.CM-09`.
- **Procedimiento:**
  1. Confirmar que **Standard discovery** esté activo en subredes corporativas (manteniendo subredes OT/ICS sensibles en lista *Ignore*) y exportar activos `Can be onboarded` para incorporación vía Intune, ConfigMgr o *Defender deployment tool* `[Verificado MS Learn]`.
  2. Conciliar dispositivos `Inactive` (> 30 días sin señal) contra bajas en Active Directory / Intune para ejecutar *offboarding* limpio `[Decisión / Propuesta Editorial]`.
  3. Auditar que los pools VDI no persistentes no estén generando entradas duplicadas por ejecución prematura del script antes del hostname definitivo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación semanal de brechas de onboarding y depuración de dispositivos inactivos.

### S-05 — Revisión de Tendencias de Amenazas en Endpoint, Niveles de Automatización e Higiene de IoCs
- **Consola / Ruta:** `Reports > Endpoints > Threat protection`, `Settings > Endpoints > Rules > Device groups` y `Indicators` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Administrator.
- **Alineación:** NIST `RS.IM-01`, `DE.CM-01`.
- **Procedimiento:**
  1. Analizar histogramas semanales en **Threat protection report** detectando reinfecciones repetidas en un mismo host (señal de persistencia no erradicada) `[Verificado MS Learn]`.
  2. Validar que la mayoría de *Device groups* operen en **Full - remediate threats automatically** (el cual remueve 40 % más muestras de malware de alta confianza según telemetría publicada por Microsoft Learn) `[Verificado MS Learn]`.
  3. Depurar indicadores IoC expirados o sin impactos manteniendo margen seguro bajo el límite del tenant (15.000 indicadores) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semanal de tendencias MDE e inventario depurado de indicadores.

### S-06 — Revisión Semanal de Anuncios en M365 Message Center y Salud de Imágenes Maestras VDI
- **Consola / Ruta:** `admin.microsoft.com > Health > Message center` y pipeline de mantenimiento de imágenes VDI `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / VDI Admin.
- **Alineación:** NIST `GV.OV-02`, `PR.PS-02`.
- **Procedimiento:**
  1. Revisar avisos de *Microsoft 365 Message Center* sobre cambios de MDE, nuevas reglas ASR o actualizaciones del sensor `[Verificado MS Learn]`.
  2. Verificar que el recurso compartido UNC de firmas para VDI no persistente esté actualizando definiciones horariamente (< 24 h de antigüedad) y que en cada mantenimiento de imagen maestra se ejecute *Windows Defender Cache Maintenance* sin dejar `senseGuid` activo `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro semanal de revisión de Message Center y checklist firmada de sellado de imagen maestra VDI.

---

## 7. Cadencia Operativa Mensual

### M-01 — Auditoría Mensual de Dispositivos Excluidos, Exclusiones AV/ASR y Uso de *Troubleshooting Mode*
- **Consola / Ruta:** `intune.microsoft.com > Endpoint security > Antivirus / ASR`, `security.microsoft.com > Endpoints > Configuration management` y *Advanced hunting* `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / Security Architect.
- **Alineación:** NIST `PR.PS-01`, `GV.PO-02` | MITRE: Defense Evasion (T1562.001).
- **Procedimiento:**
  1. Ejecutar la tarea mensual oficial de **revisión de dispositivos excluidos de políticas** y de todas las listas de exclusión de Microsoft Defender Antivirus y ASR `[Verificado MS Learn]`.
  2. Eliminar de inmediato exclusiones peligrosamente amplias (ej. `C:\Users\*`, `C:\Program Files\*`, variables de entorno de usuario o comodines `*.exe` globales), conservando solo exclusiones estrictas documentadas (como contenedores FSLogix `*.VHD(X)` o procesos específicos de Citrix PVS) protegidas por *Tamper Protection* `[Verificado MS Learn]`.
  3. Auditar todos los equipos donde se habilitó **Troubleshooting mode** en el mes confirmando retorno automático a estado protegido con *Tamper Protection* encendido `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz mensual firmada de exclusiones vigentes y bitácora de *Troubleshooting mode*.

### M-02 — Evaluación Integral de Vulnerabilidades, Software Fin de Soporte (EOS) y Líneas Base (MDVM)
- **Consola / Ruta:** `Exposure management > Vulnerability management > Dashboard / Software inventory / Baselines assessment` `[Verificado MS Learn]`.
- **Rol Responsable:** Vulnerability & Exposure Lead / IT Manager.
- **Alineación:** NIST `ID.AM-02`, `PR.PS-02`, `RS.MI-03`.
- **Procedimiento:**
  1. Revisar evolución mensual del **Exposure Score** y del **Microsoft Secure Score for Devices**, midiendo cumplimiento de SLAs de parcheo por severidad `[Verificado MS Learn]`.
  2. Filtrar en **Software inventory** sistemas operativos y aplicaciones en *End of Support* (EOS) o próximos a EOS (< 12 meses) para planificar retiro o reemplazo `[Verificado MS Learn]`.
  3. Revisar *CVE exceptions* vigentes y, si se cuenta con MDVM Add-on / Defender for Servers P2, auditar cumplimiento contra perfiles **CIS / STIG** en *Security baselines assessment*, certificados vencidos y vulnerabilidades de firmware `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual MDVM de exposición, plan EOS y estado de cumplimiento CIS/STIG.

### M-03 — Resolución de Conflictos de Políticas (`GPO vs. Intune`), *EDR in Block Mode* y Versiones de Agente
- **Consola / Ruta:** `security.microsoft.com > Endpoints > Configuration management > Endpoint security policies`, pestaña *Effective settings* en página de dispositivo y `whats-new-in-microsoft-defender-endpoint` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator.
- **Alineación:** NIST `PR.PS-01`, `PR.PS-02`.
- **Procedimiento:**
  1. Revisar las notas mensuales oficiales (*What's new in MDE* y *MDE versions*) verificando que el 100 % del parque Windows, macOS y Linux cumpla la ventana de soporte de versiones de plataforma y motor `[Verificado MS Learn]`.
  2. Auditar políticas en estado `Conflict` o `Error` (recordando que GPO prevalece por defecto sobre MDM si no se aplica `MDMWinsOverGP` o *Controlled configuration*) `[Verificado MS Learn]`.
  3. En cualquier segmento que aún utilice un antivirus primario de terceros con Defender AV en modo pasivo, verificar que **EDR in block mode** esté habilitado y operando correctamente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de conformidad de versiones de motor/plataforma y cero políticas en conflicto no resuelto.

### M-04 — Auditoría de Roles RBAC de Endpoint, Sesiones de *Live Response* y Biblioteca de Scripts
- **Consola / Ruta:** `Permissions > Microsoft Defender XDR > Roles` y `Settings > Endpoints > Live response > Library management` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Administrator / GRC.
- **Alineación:** NIST `PR.AA-05`, `GV.RR-02`.
- **Procedimiento:**
  1. Auditar quién posee los permisos `Basic live response`, `Advanced live response` y `Core security settings (Manage)` en Unified RBAC `[Verificado MS Learn]`.
  2. Revisar el registro de comandos ejecutados (*Command log*) de todas las sesiones de **Live Response** del mes verificando correspondencia con incidentes abiertos `[Verificado MS Learn]`.
  3. Auditar los scripts alojados en **Library management**, confirmando firma digital válida y removiendo utilidades obsoletas `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación de sesiones *Live Response* auditadas e inventario firmado de scripts en biblioteca.

### M-05 — Prueba Mensual de Extremo a Extremo del Pipeline de Detección, Alerta y Contención
- **Consola / Ruta:** `Evaluation & tutorials > Tutorials & simulations` (sobre equipo de prueba dedicado, nunca en producción sin control) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Administrator.
- **Alineación:** NIST `DE.CM-09`, `RS.MA-01`.
- **Procedimiento:** Ejecutar un archivo o script de prueba oficial de Microsoft en una estación de validación controlada para cronometrar toda la cadena: bloqueo/detección local -> aparición de alerta/incidente en `security.microsoft.com` (< 5 min) -> remediación automática en *Action Center* -> sincronización con Microsoft Sentinel (< 15 min) y notificación al SOC `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro mensual de prueba sintética end-to-end con marcas de tiempo medidas.

### M-06 — Generación del *Monthly Security Summary* y Conciliación de Licencias Cliente/Servidor/VDI
- **Consola / Ruta:** `Reports > Endpoints > Monthly Security Summary` y `admin.microsoft.com > Billing > Licenses` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager / Endpoint Admin / CISO.
- **Alineación:** NIST `GV.OV-01`, `ID.AM-01`.
- **Procedimiento:** Generar el PDF ejecutivo **Monthly Security Summary** (amenazas prevenidas, cobertura de sensores, postura de dispositivos, bloqueos ASR/Web y resumen MDVM) y conciliar el parque activo de estaciones, pools VDI y servidores contra las licencias asignadas (M365 E5 / Defender Suite / Windows E5 vs. *Defender for Servers Plan 1/2* y *MDVM Add-on*) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte *Monthly Security Summary* firmado y matriz mensual de cumplimiento de licenciamiento.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 — Simulacro Trimestral de Respuesta Forense en Endpoint y VDI Efímero [Trimestral]
- **Consola / Ruta:** `Evaluation & tutorials > Evaluation lab` + entorno piloto VDI `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3 / VDI Admin.
- **Alineación:** NIST `RS.AN-07`, `RS.MA-04`.
- **Procedimiento:** Ejecutar simulacro práctico cronometrado de ataque sin archivos (*fileless*) o ransomware en laboratorio, midiendo el uso correcto de *Device Timeline*, *Live Response* (incluyendo descarga en segundo plano `getfile ... &`), recolección inmediata de *Investigation package* en máquina VDI antes de cierre de sesión y aislamiento selectivo `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe trimestral del ejercicio con tiempos reales TTD/TTC y ajustes al SOP.

### SM-01 — Ingeniería Semestral del Perímetro ASR (19 Reglas) y Políticas *Device Control* [Semestral]
- **Consola / Ruta:** `intune.microsoft.com > Endpoint security > Attack surface reduction` y `Device control` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Architect / Endpoint Security Administrator.
- **Alineación:** NIST `PR.PS-01`, `PR.DS-05`.
- **Procedimiento:** Evaluar de extremo a extremo el estado de las **19 reglas ASR** por grupo de dispositivos, cruzando los incidentes reales del semestre contra reglas que aún permanezcan en `Audit` o `Not configured`, recertificando una por una todas las exclusiones por regla y auditando políticas de **Device Control** (bloqueo de USB masivo salvo dispositivos cifrados con BitLocker autorizados) `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe semestral del perímetro ASR (`N/19` reglas en `Block` como indicador interno de avance) y recertificación de reglas USB.

### SM-02 — Revisión Semestral de Reglas de Detección Personalizadas, Supresiones/Tuning y Auditoría RBAC [Semestral]
- **Consola / Ruta:** `Hunting > Custom detection rules`, `Settings > Microsoft Defender XDR > Alert tuning` y Purview Unified Audit Log `[Verificado MS Learn]`.
- **Rol Responsable:** Detection Engineer / GRC.
- **Alineación:** NIST `DE.AE-04`, `GV.RR-02`.
- **Procedimiento:** Revalidar todas las reglas KQL personalizadas de endpoint y reglas de *Alert tuning*, retirando supresiones caducas y auditando en el registro unificado cualquier cambio administrativo sensible fuera de horario sobre exclusiones o *Tamper Protection* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Catálogo depurado de detecciones de endpoint y acta semestral de auditoría de privilegios.

### A-01 — Revisión Anual de Arquitectura Multiplataforma MDE, Retención y Ejercicio Full-Scale [Anual]
- **Consola / Ruta:** `security.microsoft.com` + `intune.microsoft.com` + Microsoft Defender for Cloud `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO / Security Architect / SOC Manager.
- **Alineación:** NIST `GV.OV-03`, `RC.IM-02`.
- **Procedimiento:** Evaluar cobertura y madurez anual en Windows, macOS, Linux, iOS, Android y VDI/AVD, validar estrategia de retención (6 meses en Timeline + 30 días en Advanced Hunting + archivo en *Sentinel data lake*), actualizar roadmap de capacidades Microsoft y conducir ejercicio anual de respuesta a incidentes a escala completa `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe anual del programa de seguridad de endpoints aprobado por el CISO.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01 — Contención Inmediata y Forensia en Vivo en Endpoint Comprometido (*Isolate Device* + *Live Response*)
- **Disparador:** Alerta crítica de C2 activo, volcado de credenciales LSASS, ejecución de implante o ransomware en estación o servidor `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Preservación y aislamiento inmediato:** Desde la página del dispositivo (`Assets > Devices > [Dispositivo]`), ejecutar **Collect investigation package** (captura Autoruns, conexiones activas, caché DNS/ARP, Prefetch, tareas programadas, sesiones SMB y registros de seguridad) y acto seguido **Isolate device** (eligiendo *Full isolation* para servidores/ransomware o *Selective isolation* permitiendo Outlook/Teams si se requiere coordinar con el usuario) — **no apagar ni reiniciar el equipo** `[Verificado MS Learn]`.
  2. **Investigación interactiva con Live Response:** Iniciar sesión (`Initiate live response session`), inspeccionar procesos (`processes`), conexiones (`connections`), persistencia (`persistence`, `scheduledtasks`, `services`) e información de binarios sospechosos (`fileinfo <ruta>`), descargando muestras en segundo plano (`getfile "<ruta>" &`) dentro de los límites operativos (máx. 3 GB, timeout de inactividad 30 min) `[Verificado MS Learn]`.
  3. **Remediación y liberación verificada:** Con rol Tier 3 (`Advanced live response`), ejecutar `remediate file <ruta> -auto` o scripts firmados de limpieza (`run <script.ps1>`), escanear con antivirus completo y liberar del aislamiento únicamente cuando se confirme ausencia total de persistencia `[Verificado MS Learn]`.

### AH-02 — Contención de Dispositivos No Incorporados (*Rogue Devices*) y Usuarios Laterales (*Contain Device / IP / User*)
- **Disparador:** Detección de movimiento lateral, escaneo interno o cifrado remoto originado desde una dirección IP o equipo descubierto pero aún sin agente MDE, o mediante una cuenta comprometida `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Bloqueo distribuido desde la flota MDE:** Ejecutar **Contain device** o **Contain IP** sobre el activo no gestionado; todos los endpoints incorporados a MDE aplican automáticamente una política de firewall que bloquea toda comunicación entrante/saliente con ese host/IP `[Verificado MS Learn]`.
  2. **Contención de identidad en capa endpoint:** Si hay credenciales comprometidas usadas vía RDP/SMB/RPC, verificar o activar **Contain user** (bloqueando sesiones entrantes de esa identidad hacia cualquier endpoint MDE) mientras IAM deshabilita la cuenta y rota credenciales `[Verificado MS Learn]`.

### AH-03 — Bloqueo de Emergencia Multi-Motor de Indicadores de Compromiso (IoCs) y Restricción de Ejecución
- **Disparador:** Brote activo de malware nuevo o recepción de boletín urgente de inteligencia (MSTIC, CISA, ISAC) `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Publicación de IoCs:** En `System > Settings > Endpoints > Rules > Indicators`, cargar hashes SHA-256, direcciones IP, URLs/dominios o certificados con acción **Alert and block**, justificación, fuente y fecha de expiración `[Verificado MS Learn]`.
  2. **Modo de bloqueo estricto en segmento afectado:** Sobre servidores o estaciones de alto riesgo bajo ataque activo, activar temporalmente **Restrict app execution** para permitir únicamente ejecutables firmados por Microsoft mientras concluye el análisis forense `[Verificado MS Learn]`.

### AH-04 — Respuesta Forense Acelerada en Escritorios Virtuales Efímeros (VDI No Persistente / AVD)
- **Disparador:** Incidente de severidad Alta o Crítica originado en un dispositivo con etiqueta `VDI=NonPersistent` `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Congelamiento antes de destrucción de sesión:** Coordinar inmediatamente con el equipo VDI (Citrix/Horizon/AVD) para poner el host en modo mantenimiento/drenaje evitando que el cierre de sesión destruya el disco volátil, mientras SOC L2 lanza **Collect investigation package** y **Live Response** inmediato `[Decisión / Propuesta Editorial]`.
  2. **Verificación de la imagen base:** Comprobar mediante *Advanced hunting* (`DeviceFileEvents` / `DeviceProcessEvents`) si el artefacto malicioso provino de la sesión del usuario, del contenedor de perfil FSLogix o de contaminación previa de la imagen maestra; si hay compromiso en el contenedor FSLogix, poner en cuarentena el `.VHDX` afectado y revocar tokens del usuario `[Decisión / Propuesta Editorial]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

Consultas KQL verificadas sobre las tablas oficiales de MDE y MDVM en **Advanced Hunting** (`https://security.microsoft.com/v2/advanced-hunting`) `[Verificado MS Learn]`.

### 10.1 Diagnóstico de Fallos Silenciosos de Sensores EDR y Estado por Plataforma OS (`DeviceInfo`)
```kql
// Tabla principal: DeviceInfo
// Propósito: Detectar endpoints incorporados que dejaron de reportar en las últimas 24h o presentan problemas de sensor
DeviceInfo
| summarize arg_max(Timestamp, *) by DeviceId
| where OnboardingStatus == "Onboarded"
| where Timestamp < ago(24h) or SensorHealthState != "Active"
| project DeviceName, OSPlatform, OSVersion, SensorHealthState, ExposureLevel, Timestamp, PublicIP
| extend HorasSinSenal = datetime_diff('hour', now(), Timestamp)
| order by HorasSinSenal desc
```

### 10.2 Caza de Ejecución Sospechosa de LOLBins y Comandos Ofuscados (`DeviceProcessEvents`)
```kql
// Tabla principal: DeviceProcessEvents
// Propósito: Identificar procesos hijos sospechosos lanzados desde Office o intérpretes con comandos codificados/descargas
DeviceProcessEvents
| where Timestamp > ago(7d)
| where (InitiatingProcessFileName in~ ("winword.exe", "excel.exe", "powerpnt.exe", "outlook.exe", "acrord32.exe")
         and FileName in~ ("powershell.exe", "pwsh.exe", "cmd.exe", "wscript.exe", "cscript.exe", "mshta.exe", "rundll32.exe", "regsvr32.exe"))
     or (FileName in~ ("powershell.exe", "pwsh.exe") and ProcessCommandLine has_any ("-enc", "-EncodedCommand", "FromBase64String", "DownloadString", "Invoke-Mimikatz", "comsvcs.dll"))
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, FileName, ProcessCommandLine, SHA256
| order by Timestamp desc
```

### 10.3 Detección de Barrido de Movimiento Lateral SMB/RDP/WinRM (`DeviceNetworkEvents`)
```kql
// Tabla principal: DeviceNetworkEvents
// Propósito: Detectar estaciones que abren conexiones administrativas hacia múltiples destinos internos en ventana de 1 hora
DeviceNetworkEvents
| where Timestamp > ago(7d)
| where ActionType == "ConnectionSuccess" and RemotePort in (445, 3389, 5985, 5986, 135)
| where RemoteIPType == "Private"
| summarize DestinosUnicos = dcount(RemoteIP), ListaIPs = make_set(RemoteIP, 15) by DeviceId, DeviceName, InitiatingProcessAccountName, InitiatingProcessFileName, bin(Timestamp, 1h)
| where DestinosUnicos >= 10
| order by DestinosUnicos desc
```

### 10.4 Monitoreo de Creación de Ejecutables o Scripts Sospechosos en Rutas de Perfil/Temp (`DeviceFileEvents`)
```kql
// Tabla principal: DeviceFileEvents
// Propósito: Rastrear drop de binarios o scripts descargados desde navegadores o correo en carpetas de usuario
DeviceFileEvents
| where Timestamp > ago(7d)
| where ActionType == "FileCreated"
| where FileName endswith ".exe" or FileName endswith ".dll" or FileName endswith ".ps1" or FileName endswith ".vbs" or FileName endswith ".hta"
| where FolderPath has_any ("\\AppData\\Local\\Temp\\", "\\Downloads\\", "\\Users\\Public\\")
| where InitiatingProcessFileName in~ ("msedge.exe", "chrome.exe", "firefox.exe", "outlook.exe", "teams.exe")
| project Timestamp, DeviceName, InitiatingProcessFileName, FolderPath, FileName, SHA256, FileOriginUrl
| order by Timestamp desc
```

### 10.5 Auditoría de Intentos de Manipulación (*Tamper Protection*) y Estado de las 19 Reglas ASR (`DeviceEvents`)
```kql
// Tabla principal: DeviceEvents
// Propósito: Consolidar intentos de TamperingAttempt y volumen de eventos ASR en Audit, Block y Warn bypass
DeviceEvents
| where Timestamp > ago(14d)
| where ActionType == "TamperingAttempt" or ActionType startswith "Asr"
| summarize
    TotalEventos = count(),
    DispositivosAfectados = dcount(DeviceId),
    ProcesosOrigen = make_set(InitiatingProcessFileName, 10)
    by ActionType
| order by TotalEventos desc
```

### 10.6 Priorización de Dispositivos Expuestos a CVEs Críticos con Exploit Público (`DeviceTvmSoftwareVulnerabilities`)
```kql
// Tablas principales: DeviceTvmSoftwareVulnerabilities + DeviceTvmSoftwareVulnerabilitiesKB
// Propósito: Listar activos afectados por CVEs Críticos con código de exploit verificado para remediación prioritaria
DeviceTvmSoftwareVulnerabilities
| where VulnerabilitySeverityLevel == "Critical"
| join kind=inner (
    DeviceTvmSoftwareVulnerabilitiesKB
    | where IsExploitAvailable == 1
    | project CveId, CvssScore, VulnerabilityDescription, PublishedDate
) on CveId
| summarize
    DispositivosExpuestos = dcount(DeviceId),
    EjemplosHosts = make_set(DeviceName, 10),
    ParchesRecomendados = make_set(RecommendedSecurityUpdate)
    by CveId, CvssScore, SoftwareVendor, SoftwareName
| order by DispositivosExpuestos desc, CvssScore desc
```

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla de KPIs de Seguridad de Endpoints y Gestión de Vulnerabilidades

| ID | Indicador (KPI) | Fórmula / Fuente Técnica | Meta Sugerida | Frecuencia | Audiencia | Estado |
|---|---|---|---|---|---|---|
| **KPI-01** | **Cobertura Efectiva de Onboarding MDE** | `Dispositivos Onboarded / (Onboarded + Can be onboarded en inventario elegible) * 100` | >= 98 % estaciones/VDI; 100 % servidores críticos | Semanal | Endpoint Admin / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Salud Activa del Sensor y Actualidad de Firmas** | `% dispositivos Onboarded con SensorHealthState == 'Active' y definiciones AV < 48 h` | >= 96 % sobre parque encendido | Diaria | Endpoint Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tiempo Medio hasta Aislamiento / Contención de Host (MTTC-EP)** | `percentiles(Timestamp_IsolateOrContain - CreatedTime, 50, 90)` en incidentes Críticos/Altos | p50 < 15 min; p90 < 45 min | Semanal | SOC Lead / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Adopción de las 19 Reglas ASR en Modo `Block`** | `Cantidad de reglas ASR aplicables configuradas en modo Block (código 1) sobre las 19 reglas oficiales` | 3/3 *Standard rules* en `Block`; >= 14/18 reglas aplicables a clientes en `Block` | Mensual | Security Architect | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Cumplimiento de *Tamper Protection* Activo** | `% dispositivos Windows/macOS elegibles con Tamper Protection en modo Enabled/Block` | >= 99 % (excepciones solo en ventana *Troubleshooting mode*) | Semanal | Endpoint Admin / GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Índice de Exposición Organizacional (*Exposure Score*)** | Valor nativo en `Exposure management > Vulnerability management > Dashboard` (0–100, menor es mejor) | Score < 30 (Low exposure) o reducción sostenida trimestral | Semanal | Vulnerability Lead / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **SLA de Remediación de CVEs Críticos con Exploit Activo** | `% instancias CVE Críticas con IsExploitAvailable == 1 cerradas dentro de ventana objetivo` | >= 90 % en <= 7 días (<= 48 h si expuesto a Internet) | Semanal | IT Ops / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Cobertura de *Full Automation* en Device Groups** | `% endpoints estándar cubiertos por grupos con nivel 'Full - remediate threats automatically'` | >= 90 % de estaciones de usuario; 100 % de servidores en *Full* o *Semi* auditado | Mensual | SOC Manager | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional en Seguridad de Endpoints

| Nivel | Estadio | Características Operativas Verificables `[Decisión / Propuesta Editorial]` |
|---|---|---|
| **Nivel 1 — Básico (Solo Antivirus Reactivo)** | Protección basada únicamente en firmas o MDE sin gobernanza operativa. | Reglas ASR sin configurar, *Tamper Protection* parcial, exclusiones AV amplias heredadas, sin uso de *Action Center* ni flujo MDVM. |
| **Nivel 2 — Estandarizado (EPP + EDR Operativo)** | Cobertura > 95 %, *Tamper Protection* al 99 %, las 3 *Standard ASR rules* en `Block` y triaje diario de incidentes MDE. | *Full automation* activo en estaciones estándar; revisión diaria de salud de sensores y *Action Center*; onboarding VDI con *Single entry* sin duplicados. |
| **Nivel 3 — Proactivo (Hardening ASR + MDVM Basado en Riesgo + DFIR)** | >= 14 de las 19 reglas ASR en `Block` con exclusiones estrictamente por regla; ciclo semanal MDVM integrado con *Security Tasks* en Intune y uso experto de *Live Response*. | Caza semanal KQL sobre `DeviceProcessEvents`/`DeviceNetworkEvents`; señales de riesgo MDE conectadas a políticas de Acceso Condicional en Entra ID. |
| **Nivel 4 — Optimizado (Zero Trust Continuo y Resiliencia Autónoma)** | Perímetro preventivo endurecido (*Controlled configuration*, *Device Control*, *Predictive Shielding*), forensia automatizada incluso en VDI efímero y validación trimestral Purple Team. | *Exposure Score* bajo (< 30), cero exclusiones globales injustificadas, MTTC en minutos y evidencias continuas listas para auditoría NIST CSF 2.0. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

| Función NIST CSF 2.0 | Subcategoría | Resultado Esperado (NIST CSF 2.0) | Capacidad MDE (P1/P2) y MDVM + MITRE ATT&CK | Evidencia Auditable | Estado |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.RR-02` | Roles, responsabilidades y autoridades de ciberseguridad establecidos y exigidos. | Segregación en Unified RBAC (`Basic` vs. `Advanced live response`, `Core security settings`) y niveles de automatización por *Device group*. | Exportación de roles URBAC, grupos de dispositivos y bitácora de sesiones *Live Response*. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.OV-01` | Resultados de la estrategia de riesgo revisados para ajustar dirección. | *Monthly Security Summary*, evolución de *Exposure Score* y *Microsoft Secure Score for Devices*. | Informes PDF mensuales de los últimos 90 días y actas de comité de riesgo. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-01` | Se mantienen inventarios de hardware gestionado por la organización. | *Device Inventory* multiplataforma (Windows, macOS, Linux, iOS, Android, VDI) y *Standard Device Discovery*. | Exportación CSV de `Assets > Devices` y reporte de salud de sensores. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-02` | Se mantienen inventarios de software, servicios y sistemas. | `DeviceTvmSoftwareInventory` en MDVM (incluyendo detección de software fin de soporte / EOS y uso real). | Exportación de inventario de software y reporte mensual de activos EOS. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican, validan y registran las vulnerabilidades en los activos. | Evaluación continua en `DeviceTvmSoftwareVulnerabilities` cruzada con explotabilidad (`DeviceTvmSoftwareVulnerabilitiesKB`) y líneas base CIS/STIG (Add-on). | Panel *Weaknesses*, *Security Tasks* en Intune y registro formal de *CVE exceptions*. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-01` | Se establecen y aplican prácticas de gestión de configuración. | *Endpoint security policies* (Intune/Defender), **19 reglas ASR** y pestaña *Effective settings* por dispositivo (mitiga T1003.001, T1566, T1059). | Exportación de políticas ASR, consulta KQL de acciones `Asr*Blocked` y matriz de exclusiones por regla. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-05` | Se previene la instalación y ejecución de software no autorizado. | *Next-Generation Protection*, **Tamper Protection / Controlled Configuration**, **Device Control** (USB) y *Restrict app execution* (mitiga T1562.001, T1091, T1204). | Estado global de *Tamper Protection*, reportes de *Device Control* e historial de *Action Center*. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-09` | El hardware, software, entornos de ejecución y sus datos se monitorean para encontrar eventos potencialmente adversos. | Telemetría profunda del sensor EDR (6 meses en *Device Timeline* y 30 días en `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceFileEvents`, `DeviceEvents`). | Muestras de *Timeline*, consultas guardadas de *Advanced Hunting* y alertas EDR generadas. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para caracterizar actividades de ataque. | Correlación automática de alertas EDR/AV en incidentes XDR, árbol de procesos e informes contextualizados de *Threat Analytics*. | Páginas de incidentes investigados con árbol de ejecución y técnicas ATT&CK asociadas. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos. | **Isolate device** (total/selectivo), **Contain device / IP / user** y *EDR in block mode* (mitiga T1021, T1486). | Exportación de *Action Center > History* mostrando tiempos de aislamiento y contención. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.AN-07` | Los datos y metadatos del incidente se recolectan preservando su integridad y procedencia. | **Collect investigation package** y registro auditable de comandos en sesiones **Live Response** (`Command log`). | Paquetes forenses recolectados con hash y bitácora inmutable del *Command log*. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de los activos restaurados y se confirma el funcionamiento normal. | Verificación de limpieza vía escaneo AV completo, reversión controlada (*Undo* / *Release from isolation*) en *Action Center* y sellado limpio de imágenes VDI. | Registro en *Action Center* de liberación post-erradicación vinculado a validación técnica. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps / Admin / GRC)

| Rol Objetivo | Ruta Oficial y Comunitaria Recomendada (Noviembre 2026) | Certificación Asociada |
|---|---|---|
| **SOC Operator (L1) e Incident Responder (L2)** | *Become a Microsoft Defender for Endpoint Ninja* — Track **SecOps** (Heike Ritter, v45 actualizado ago/sep 2026), *MDE Security Operations Guide* y práctica guiada de *Live Response* y *Action Center*. | **SC-200** (*Security Operations Analyst Associate*) `[Verificado MS Learn]` |
| **Endpoint Security Admin y VDI Engineer** | *MDE Ninja Training* — Track **SecAdmin**, guía oficial de despliegue en **VDI no persistente**, catálogo de las **19 reglas ASR** y guías de optimización de Jeffrey Appel (MVP). | **MD-102** (*Endpoint Administrator*) / **MS-102** + **SC-300** `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Threat Hunter (L3) y Detection Engineer** | Consultas avanzadas sobre tablas `Device*` y `DeviceTvm*`, repositorio **FalconFriday** (Olaf Hartong, MVP) y repositorio de caza KQL de Alex Verboon (MVP). | **SC-200** + validación práctica Purple Team `[Decisión / Propuesta Editorial]` |
| **Vulnerability Lead, Architect y CISO / GRC** | *Become a Microsoft Defender Vulnerability Management Ninja*, integración con *Microsoft Security Exposure Management* y arquitectura Zero Trust de endpoints. | **SC-100** (*Cybersecurity Architect Expert*) `[Verificado MS Learn]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Resumen de Correcciones Aplicadas contra Microsoft Learn MCP (`2026-11-11`)

1. **Corrección mayor del número, GUIDs y modos de reglas Attack Surface Reduction (ASR):** Se corrigió la afirmación desactualizada de "13 reglas ASR" (presente en `MDE- SecOPS pura Bloques 20260309` y `MDE - SecOPS pura VC 20260309`) actualizándola al catálogo oficial vigente de **19 reglas ASR** en Microsoft Learn (`attack-surface-reduction-rules-reference`: 3 *Standard protection rules* + 16 *Other ASR rules*). Se corrigió asimismo la errata en el GUID de la regla de LSASS (`9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2` en lugar de `...e4b0`), se documentaron los 5 códigos de modo (`0, 1, 2, 5, 6`), las 2 reglas que **no admiten modo Warn** (LSASS e inyección de código Office), la precedencia predeterminada de GPO sobre MDM salvo `MDMWinsOverGP`, el requisito de Defender AV en *Active mode* y el cambio de plataforma `4.18.26060` que exige **aprobación de administrador para *Unblock* en modo Warn**, eliminando además porcentajes de eficacia no publicados oficialmente ("80-90%" / "95%") `[Verificado MS Learn]`.
2. **Actualización arquitectónica de AIR en MDE (1 de septiembre de 2026):** Conforme a `learn.microsoft.com/en-us/defender-endpoint/automation-levels`, se registró que desde el **1 de septiembre de 2026** *Automated Investigation and Response (AIR)* dejó de ejecutarse como una experiencia de investigación separada o con inicio manual en MDE, pasando a ejecutarse automáticamente integrada en la pila predeterminada de Microsoft Defender Antivirus (usando escaneo completo bajo demanda cuando se requiere análisis manual), manteniendo los niveles de automatización por *Device group* y el control en *Action Center* `[Verificado MS Learn]`.
3. **Delimitación exacta de licenciamiento MDVM Core vs. Add-on y Servidores:** Se precisó la ubicación actual de *Vulnerability Management* dentro de **Exposure management** en `security.microsoft.com`, separando las 9 capacidades **Core** incluidas en MDE P2 / M365 E5 de las 6 capacidades **Premium** exclusivas del *MDVM Add-on / Standalone* (y *Defender for Servers Plan 2*), así como la exclusión de servidores de las licencias de usuario M365 E5 y el retiro del escaneo autenticado de Windows `[Verificado MS Learn]`.
4. **Revalidación de Tamper Protection, Controlled Configuration y modos en macOS/Linux:** Se documentó la transición de la configuración bajo el nombre **Controlled configuration**, la protección de listas de exclusiones administradas en Windows (incluso en modo pasivo), el uso de *Troubleshooting mode*, los modos `Disabled/Audit/Block` en macOS y el modo `Audit` (Preview) en Linux, más la consulta KQL oficial `ActionType == "TamperingAttempt"` `[Verificado MS Learn]`.
5. **Verificación de capacidades y límites de Live Response (2026):** Se incorporó la descarga de archivos en segundo plano (`getfile <path> &` y `fg <command_id>`), la página centralizada *Library management* y los límites exactos vigentes (50 sesiones concurrentes por tenant, 5 por usuario, 1 por dispositivo, timeout 30 min, `getfile` 3 GB, `library` 250 MB, `putfile` 300 MB en Windows / 10 MB otras plataformas) `[Verificado MS Learn]`.
6. **Consolidación del estándar empresarial para VDI no persistente:** Se integró y validó contra `configure-endpoints-vdi` el modelo *Single entry for each device* (`Onboard-NonPersistentMachine.ps1`), la prohibición de incorporar imágenes maestras y su limpieza como `SYSTEM` con `PsExec.exe`, las exclusiones críticas de contenedores **FSLogix** (`*.VHD`/`*.VHDX`), el uso de firmas pre-extraídas por recurso compartido UNC y la respuesta forense acelerada ante máquinas efímeras `[Verificado MS Learn]`.

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Técnica |
|---|---|---|
| **SLAs de respuesta y parcheo** (ej. MTTC p50 < 15 min, CVEs críticos con exploit <= 7 días / <= 48 h expuestos) | `[Decisión / Propuesta Editorial]` | Microsoft provee priorización dinámica por riesgo y *Exposure Score*, pero cada organización define sus tiempos contractuales de parcheo y contención junto a TI y Negocio. |
| **Indicador interno `N/19` reglas ASR en `Block` y meta >= 14 reglas en estaciones** | `[Decisión / Propuesta Editorial]` | Microsoft recomienda las 3 *Standard rules* en `Block` y pruebas previas en `Audit` para el resto; la métrica fraccional de avance semestral es un indicador consultivo interno, no un score oficial. |
| **Parámetros de tuning de rendimiento VDI** (`ScanAvgCPULoadFactor 25-30 %`, ventana de 30 min) | `[Decisión / Propuesta Editorial]` | Recomendación de arquitectura de campo validada en implementaciones VDI de gran escala (20.000+ asientos) sobre los parámetros soportados de `Set-MpPreference`. |
| **Estructura de roles URBAC por niveles (L1/L2/L3/SecAdmin/VM) y ventanas JIT en PIM** | `[Decisión / Propuesta Editorial]` | Combina permisos reales de Microsoft Defender Unified RBAC e Intune bajo un diseño consultivo de segregación de funciones. |
| **Mapeo de controles de endpoint a subcategorías NIST CSF 2.0 y modelo de madurez de 4 niveles** | `[Decisión / Propuesta Editorial]` | Construcción metodológica auditable basada en los resultados (*outcomes*) del NIST CSF 2.0 Core (CSWP 29) respaldados por evidencias observables de MDE y MDVM. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Corporation — *Microsoft Defender for Endpoint Security Operations Guide* — `https://learn.microsoft.com/en-us/defender-endpoint/mde-sec-ops-guide` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-02:** Microsoft Corporation — *Attack surface reduction (ASR) rules overview & technical reference (19 rules)* — `https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-overview` y `https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-03:** Microsoft Corporation — *Automation levels in automated investigation and remediation capabilities (Sept 1, 2026 AIR update)* — `https://learn.microsoft.com/en-us/defender-endpoint/automation-levels` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-04:** Microsoft Corporation — *Tamper protection overview & Controlled configuration* — `https://learn.microsoft.com/en-us/defender-endpoint/prevent-changes-to-security-settings-with-tamper-protection` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-05:** Microsoft Corporation — *Investigate entities on devices using live response* — `https://learn.microsoft.com/en-us/defender-endpoint/live-response` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-06:** Microsoft Corporation — *Take response actions on a device in Microsoft Defender for Endpoint* — `https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts` (Verificado vía Microsoft Learn, Nov 2026).
- **REF-07:** Microsoft Corporation — *Compare Microsoft Defender Vulnerability Management plans and capabilities* — `https://learn.microsoft.com/en-us/defender-vulnerability-management/defender-vulnerability-management-capabilities` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-08:** Microsoft Corporation — *Onboard non-persistent VDI devices to Microsoft Defender for Endpoint* — `https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-vdi` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-09:** Microsoft Corporation — *Endpoint detection and response (EDR) in block mode* — `https://learn.microsoft.com/en-us/defender-endpoint/edr-in-block-mode` (Verificado vía Microsoft Learn, Nov 2026).
- **REF-10:** Microsoft Corporation — *Understand the advanced hunting schema (`Device*` and `DeviceTvm*` tables)* — `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables` (Verificado vía MCP Microsoft Learn, Nov 2026).

### 15.2 Publicaciones Oficiales y Empleados de Microsoft
- **REF-11:** Heike Ritter (Empleado de Microsoft) — *Become a Microsoft Defender for Endpoint Ninja* (Microsoft Tech Community, versión 45 actualizada ago/sep 2026) — `https://techcommunity.microsoft.com/blog/microsoftdefenderatpblog/become-a-microsoft-defender-for-endpoint-ninja/1515647`
- **REF-12:** Microsoft Core Infrastructure and Security Blog — *MDE for Non-Persistent VDI — Implementation Guide & Best Practices* (Microsoft Tech Community) — `https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/mde-for-non%E2%80%91persistent-vdi-%E2%80%94-implementation-guide--best-practices-/4470439`
- **REF-13:** Microsoft Security Blog — *Microsoft Defender XDR demonstrates 100% detection coverage across all cyberattack stages in the 2024 MITRE ATT&CK Evaluations: Enterprise* — `https://www.microsoft.com/en-us/security/blog/2024/12/11/microsoft-defender-xdr-demonstrates-100-detection-coverage-across-all-cyberattack-stages-in-the-2024-mitre-attck-evaluations-enterprise/`

### 15.3 Comunidad y MVPs de Seguridad de Microsoft
- **REF-14:** Jeffrey Appel (Microsoft Security MVP) — *Microsoft Defender for Endpoint, ASR, VDI & Vulnerability Management Technical Guides* — `https://jeffreyappel.nl/`
- **REF-15:** Olaf Hartong (Microsoft Security MVP, FalconForce) — *FalconFriday: Detection Engineering & KQL Queries for Defender for Endpoint mapped to MITRE ATT&CK* — `https://github.com/FalconForceTeam/FalconFriday/blob/main/README.md`
- **REF-16:** Alex Verboon (Microsoft Security MVP) — *Defender Resource Hub & Hunting-Queries-Detection-Rules* — `https://github.com/alexverboon/Hunting-Queries-Detection-Rules` y `https://defenderresourcehub.info/`

### 15.4 Marcos Normativos y Estándares Abiertos
- **REF-17:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)* — `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`
- **REF-18:** MITRE Corporation — *MITRE ATT&CK Enterprise Matrix & MITRE Engenuity Evaluations* — `https://attack.mitre.org/` y `https://evals.mitre.org/`

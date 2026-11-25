# Guía Maestra de Excelencia Operacional: Microsoft Intune Plan 1 (Gestión Unificada de Endpoints y Postura en Microsoft 365 E3/E5)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `10_Microsoft_Intune_Plan_1` |
| **Slug Canónico** | `Microsoft_Intune_Plan_1` |
| **Nombre Completo** | Microsoft Intune Plan 1 (Gestión Unificada de Endpoints y Postura en Microsoft 365 E3/E5) |
| **Categoría Maestra** | Endpoints, Dispositivos y Plataforma Windows |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (`Intune - VC - SecOps 260310 + Modelo Operacion`, auditorías `revisado 1-3`, Bloques `01/09` a `09/09`, Playbooks `IR-01` a `IR-03`, Licenciamiento y NIST CSF 2.0) + Revalidado Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Incluido en Microsoft 365 E5** (también incluido en Microsoft 365 E3/E7, Enterprise Mobility + Security E3/E5, M365 F1/F3, M365 Business Premium y Education A3/A5) como plano base de Unified Endpoint Management (MDM + MAM) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://intune.microsoft.com` (Microsoft Intune admin center), `https://security.microsoft.com` (Microsoft Defender portal — XDR, ASR, MDVM y Sentinel), `https://entra.microsoft.com` (Conditional Access, PIM y objetos de dispositivo) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, SOC L1, SOC L2, Endpoint Security Engineer, Intune Platform Administrator, Vulnerability Management Analyst, Identity & Access Architect, GRC & Internal/External Auditors |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Microsoft Zero Trust Architecture (Pilar Endpoints), MITRE ATT&CK Enterprise / Mobile, CIS Benchmarks, DISA STIG (referencia de línea base), CISA Known Exploited Vulnerabilities (KEV) |

> **Nota de consolidación y frontera arquitectónica:** Esta guía maestra unifica orgánicamente el modelo operativo SecOps de `MSEOP-MD` (sus revisiones técnicas `revisado 1`, `revisado 2` y `revisado 3`, los nueve bloques operativos `01/09` a `09/09`, los playbooks `IR-01` a `IR-03`, el análisis de licenciamiento y el marco de auditoría NIST CSF 2.0), actualizándolo al estado verificado del servicio al `2026-11-11`. Se delimita explícitamente el alcance de **Microsoft Intune Plan 1** frente al **Módulo `11_Microsoft_Intune_Suite`** (donde se profundizan Endpoint Privilege Management, Microsoft Cloud PKI, Remote Help, Enterprise Application Management, Advanced Analytics, Microsoft Tunnel for MAM y dispositivos especializados) y frente al **Módulo `12_Windows_Enterprise_Security_y_Cifrado`** (donde se abordan a nivel de arquitectura interna de sistema operativo BitLocker profundo, Windows Hello for Business, Virtualization-Based Security / Credential Guard, App Control for Business y Windows LAPS) `[Verificado MS Learn]`. Toda afirmación técnica documentada lleva la etiqueta `[Verificado MS Learn]`, mientras que los SLAs, metas cuantitativas de KPIs, matrices RACI y criterios consultivos llevan `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución de Microsoft Intune Plan 1 como Fuente de Verdad de Postura de Endpoints

En una arquitectura **Zero Trust**, la red corporativa deja de constituir una frontera de confianza implícita y el endpoint verificado se convierte en el perímetro efectivo de acceso `[Verificado MS Learn]`. Desde la perspectiva del Centro de Operaciones de Seguridad (SOC) y de Ingeniería de Seguridad de Endpoints, **Microsoft Intune Plan 1** no se opera simplemente como una herramienta de inventario o distribución de software, sino como la **fuente determinista de verdad sobre la postura de seguridad de dispositivos y aplicaciones** en Windows 11, macOS, iOS/iPadOS, Android (Android Enterprise y AOSP) y escritorios Linux soportados `[Verificado MS Learn]`.

A noviembre de 2026, la excelencia operacional sobre Microsoft Intune Plan 1 descansa sobre cuatro bucles de seguridad convergentes `[Verificado MS Learn]`:

1. **Bucle cerrado de Acceso Condicional basado en Postura y Riesgo EDR:** Intune evalúa continuamente el cumplimiento del dispositivo (*Device Compliance*) frente a requisitos criptográficos, integridad de arranque, versión mínima del sistema operativo y nivel de riesgo calculado dinámicamente por **Microsoft Defender for Endpoint (MDE)**. El estado resultante (`Compliant` o `Noncompliant`) se sincroniza con **Microsoft Entra ID**, donde **Conditional Access** y **Continuous Access Evaluation (CAE)** permiten, restringen o revocan sesiones casi en tiempo real `[Verificado MS Learn]`.
2. **Endurecimiento declarativo mediante Settings Catalog y Security Baselines:** Distribución granular y auditable de configuraciones sobre proveedores CSP de Windows y perfiles declarativos Apple/Android mediante **Settings Catalog** (asistido opcionalmente por *Microsoft Copilot in Intune* cuando existen SCUs habilitadas), **Endpoint Security Policies** y **Security Baselines** actualizadas a 2026 (Windows 11 hasta versión **26H2**, Microsoft 365 Apps **v2512**, Microsoft Edge **v139**, Defender for Endpoint **v24H1** y Windows 365) `[Verificado MS Learn]`.
3. **Protección de datos sin inscripción MDM (MAM / App Protection Policies):** Contenedorización de aplicaciones e identidad laboral en dispositivos personales BYOD mediante **Intune App Protection Policies (APP)** sobre iOS/iPadOS, Android y **Microsoft Edge for Business en Windows** (integrado con el conector Mobile Threat Defense de **Windows Security Center** en Windows 11 23H2+ y *App Protection Conditional Access*) `[Verificado MS Learn]`.
4. **Defensa del plano de control y actualización sin interrupción:** Gobernanza con **Multi Admin Approval (MAA)** para impedir que un único administrador comprometido o script automatizado ejecute borrados masivos, despliegue scripts maliciosos o altere RBAC; segmentación delegada mediante **Scope Tags**; y parcheo convergente mediante **Windows Autopatch** con **Hotpatch updates** sin reinicio en Windows 11 Enterprise 24H2/25H2 `[Verificado MS Learn]`.

### 2.2 Matriz de Licenciamiento, Fronteras Modulares y Prerrequisitos (Noviembre 2026)

| Plano / Licencia | Estado respecto a M365 E5 | Alcance Técnico y Delimitación Modular en el Repositorio Maestro | Etiqueta |
|---|---|---|---|
| **Microsoft Intune Plan 1** *(Alcance de este Módulo 10)* | **Incluido** en M365 E3/E5/E7, EMS E3/E5, M365 F1/F3, Business Premium y Education A3/A5 | Gestión unificada MDM y MAM multiplataforma, *Device Compliance*, *Settings Catalog*, *Security Baselines*, políticas *Endpoint Security* (Antivirus, Firewall MDM, BitLocker/FileVault, ASR, Account Protection / Windows LAPS, EDR onboarding), *Windows Autopatch* (unificado desde abril de 2025 para E3+/A3+/F3/Business Premium), scripts PowerShell/Remediations (con licencia Windows E3/E5 elegible), RBAC, *Scope Tags*, *Multi Admin Approval (MAA)*, *Co-management* con Configuration Manager y *Diagnostics settings* hacia Azure Monitor. | `[Verificado MS Learn]` |
| **Suscripción Device-Only de Intune** | Licencia por dispositivo *(escenarios sin afinidad de usuario)* | Aplicable a quioscos, salas de reuniones, *Windows Autopilot Self-Deploying*, *Android Enterprise Dedicated*, *AOSP userless*, *Apple ADE sin afinidad* y cuentas *DEM*. **Limitación crítica:** no admite *App Protection Policies*, *Conditional Access* basado en usuario ni perfiles de correo/calendario de usuario. | `[Verificado MS Learn]` |
| **Acceso de Administradores sin Licencia (*Unlicensed Admin Access*)** | Activo por defecto en tenants creados después de julio de 2021 *(irreversible al activarlo en previos)* | Permite iniciar sesión en `intune.microsoft.com` y aprobar solicitudes MAA sin asignar licencia Intune al administrador. Soporta hasta **1.000 administradores sin licencia por grupo de seguridad directo** (no admite grupos anidados; propagación de hasta 48 horas). | `[Verificado MS Learn]` |
| **Microsoft Intune Plan 2 y Microsoft Intune Suite** *(Frontera -> Módulo 11)* | **Complemento (Add-on)** sobre Intune Plan 1 *(o incluido en bundles superiores como M365 E7)* | **Intune Plan 2:** *Microsoft Tunnel for MAM*, *Specialty device management* (AR/VR, pantallas inteligentes, salas) y *Firmware Over-the-Air (FOTA)*. **Intune Suite** (incluye Plan 2): *Endpoint Privilege Management (EPM)*, *Microsoft Cloud PKI*, *Remote Help*, *Enterprise Application Management* y *Advanced Analytics*. Operación detallada en `11_Microsoft_Intune_Suite`. | `[Verificado MS Learn]` |
| **Seguridad Nativa de Windows Enterprise y Cifrado** *(Frontera -> Módulo 12)* | Capacidades de SO en Windows 11 Enterprise E3/E5 gestionadas vía CSP | Criptografía profunda de BitLocker y TPM 2.0, *Windows Hello for Business (Cloud Kerberos Trust)*, *Virtualization-Based Security (VBS)* / *Credential Guard*, *App Control for Business* y arquitectura interna de *Windows LAPS*. Operación detallada en `12_Windows_Enterprise_Security_y_Cifrado`. | `[Verificado MS Learn]` |
| **Dependencias Transversales en M365 E5** | Incluidas en M365 E5 *(excepto consumo Azure)* | **Microsoft Entra ID P1/P2** (Conditional Access, CAE, MDM auto-enrollment, PIM); **Microsoft Defender for Endpoint P2** (señal de riesgo en cumplimiento, reportes ASR, Security Tasks de MDVM, Live Response); **Suscripción Azure** para Log Analytics / Storage / Event Hubs y **Microsoft Sentinel**. | `[Verificado MS Learn]` |

### 2.3 Principios Rectores Oficiales y Criterios de Excelencia Operacional

- **Principio 1 — Entrega de instrucción no equivale a enforcement (*Succeeded != Protected*):** Un estado `Succeeded` en un perfil de Intune solo certifica que el agente MDM entregó la configuración al CSP local; la efectividad real de BitLocker, Firewall MDM y reglas ASR debe validarse en reportes dedicados de estado operativo `[Verificado MS Learn]`.
- **Principio 2 — Cumplimiento determinista acoplado a Acceso Condicional y CAE:** Ningún dispositivo corporativo accede a aplicaciones empresariales si no cumple simultáneamente identidad fuerte y estado `Compliant` vigente, reduciendo ventanas de exposición mediante *Continuous Access Evaluation* `[Verificado MS Learn]`.
- **Principio 3 — Doble control administrativo mediante Multi Admin Approval (MAA):** Toda acción destructiva (`Wipe`, `Retire`, `Delete`) y toda modificación de scripts, políticas críticas o roles RBAC exige aprobación explícita de un segundo administrador distinto, tanto en portal como vía Microsoft Graph API `[Verificado MS Learn]`.
- **Principio 4 — Protección centrada en la aplicación (MAM) para BYOD sin fricción de privacidad:** En equipos personales Windows (Edge for Business) y móviles iOS/Android, se protege el contenedor de datos corporativos con *App Protection Policies* y *Selective Wipe* sin inscribir el dispositivo completo en MDM `[Verificado MS Learn]`.
- **Principio 5 — Parcheo continuo sin reinicio (*Hotpatching*) con vía rápida para CISA KEV:** Maximización de *Hotpatch updates* mensuales en Windows 11 Enterprise 24H2+ para sostener cumplimiento rápido sin interrumpir al usuario, reservando despliegues acelerados con reinicio para vulnerabilidades explotadas activamente `[Verificado MS Learn]`.
- **Principio 6 — Observabilidad SIEM consciente de la arquitectura del pipeline:** Separación analítica entre eventos transaccionales casi en tiempo real (`IntuneAuditLogs`, `IntuneOperationalLogs`) y volcados diarios de inventario/cumplimiento (`IntuneDevices`, `IntuneDeviceComplianceOrg`) con deduplicación obligatoria en KQL `[Verificado MS Learn]`.

### 2.4 Las Tres Dimensiones que Consume el SOC sobre Microsoft Intune

Para preservar la eficiencia analítica y evitar solapamientos con soporte técnico, el SOC consume sobre Intune tres vectores específicos `[Decisión / Propuesta Editorial]`:

1. **Señal de Cumplimiento (*Compliance Signal*):** Evalúa si el activo cumple condiciones objetivas de confianza antes y durante la sesión, alimentando el bloqueo determinista en Entra Conditional Access `[Verificado MS Learn]`.
2. **Postura de Configuración Segura (*Security Configuration*):** Verifica el endurecimiento activo del sistema operativo y navegador (Security Baselines, BitLocker/FileVault, Firewall MDM, ASR y LAPS) `[Verificado MS Learn]`.
3. **Integración de Amenazas y Respuesta (*Threat Integration*):** Garantiza cobertura del sensor EDR de MDE, recibe el nivel de riesgo del endpoint para degradar automáticamente su cumplimiento y ejecuta contención remota auditada (`Remote lock`, `Retire`, `App selective wipe`, `Full Wipe`) `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Motores y Superficies de Control en `https://intune.microsoft.com`

| Componente / Motor | Función Operativa Principal | Ruta Exacta en Consola | Integraciones Nativas | Etiqueta |
|---|---|---|---|---|
| **Device Compliance Engine** | Evalúa cumplimiento por setting (cifrado, integridad OS/Play Integrity, versión mínima/máxima de SO, salud de Windows Security y riesgo MDE), aplica *Grace period* y gobierna ajustes globales (*Validity period* y dispositivos sin política asignada). | `intune.microsoft.com > Devices > Compliance` | Microsoft Entra Conditional Access, CAE, Defender for Endpoint | `[Verificado MS Learn]` |
| **Settings Catalog** | Catálogo unificado de configuraciones mapeadas directamente a CSPs de Windows, payloads MDM/DDM de Apple y Android Enterprise, eliminando valores predeterminados ocultos y permitiendo consultas asistidas por Copilot in Intune. | `intune.microsoft.com > Devices > Manage devices > Configuration > Create > Settings catalog` | Windows CSPs, Apple DDM, Android Enterprise, Copilot in Intune | `[Verificado MS Learn]` |
| **Security Baselines** | Instancias versionadas de endurecimiento recomendado por Microsoft: *Windows 10 and later* (**v26H2, v25H2, v24H2**), *Defender for Endpoint* (**v24H1**, no recomendada en VDI/VMs), *M365 Apps* (**v2512**, jun-2026), *Microsoft Edge* (**v139**, abr-2026) y *Windows 365*. | `intune.microsoft.com > Endpoint security > Security baselines` | Windows Security, Microsoft Edge, Defender for Endpoint | `[Verificado MS Learn]` |
| **Endpoint Security Workloads & Conector MDE** | Administración dedicada para SecOps de *Antivirus*, *Disk encryption* (BitLocker/FileVault), *Firewall*, *Endpoint detection and response* (onboarding MDE), *Attack surface reduction (ASR)*, *Account protection* (LAPS) y *Security tasks* de MDVM. | `intune.microsoft.com > Endpoint security` | Microsoft Defender XDR, Defender Vulnerability Management, Entra ID | `[Verificado MS Learn]` |
| **Windows Autopatch & Hotpatch Updates** | Gestión automatizada en anillos de actualizaciones de Windows, M365 Apps, Edge y Teams (activación unificada desde abril de 2025 para E3+/A3+/F3/Business Premium) y parches mensuales de seguridad sin reinicio (*Hotpatch*) en Windows 11 Enterprise 24H2+. | `intune.microsoft.com > Devices > Manage updates > Windows updates > Quality updates` | Windows Update, Endpoint Analytics, Defender Vulnerability Management | `[Verificado MS Learn]` |
| **App Protection Policies (MAM) & Windows MAM** | Controles DLP a nivel aplicación (bloqueo de copia/impresión/guardado externo, cifrado org, PIN, *Conditional Launch* y *Selective Wipe*) sobre iOS 17+, Android y **Microsoft Edge for Business en Windows** con conector MTD de Windows Security Center (Win 11 23H2+). | `intune.microsoft.com > Apps > Protection` y `Tenant administration > Connectors and tokens > Windows Security Center` | Microsoft Entra App Protection Conditional Access, Purview Endpoint/Browser DLP | `[Verificado MS Learn]` |
| **Multi Admin Approval (MAA) & Scope Tags** | Políticas de acceso de doble aprobación para *Apps*, *Compliance policies*, *Configuration policies* (Settings Catalog), *Device actions* (`Wipe`, `Retire`, `Delete`), *RBAC*, *Scripts* (con soporte de *Change Review Agent*) y *Tenant Configuration*. | `intune.microsoft.com > Tenant administration > Multi Admin Approval` y `Roles > Scope tags` | Microsoft Graph API (delegated & app-auth), Intune Audit Logs | `[Verificado MS Learn]` |
| **Diagnostics Settings (Exportación Azure Monitor)** | Canalización continua de `AuditLogs`, `OperationalLogs`, `DeviceComplianceOrg` e `IntuneDevices` hacia Log Analytics, Azure Storage o Event Hubs. | `intune.microsoft.com > Reports > Diagnostics settings` | Azure Monitor Log Analytics, Microsoft Sentinel, Event Hubs | `[Verificado MS Learn]` |

### 3.2 Hitos de Plataforma, Retiros y Reglas Arquitectónicas Críticas (2025–2027)

1. **Fin de soporte de Windows 10 (`2025-10-14`) `[Verificado MS Learn]`:**
   - Windows 10 alcanzó su fin de soporte el 14 de octubre de 2025 y permanece en Intune solo como *allowed version* sin garantía sobre nuevas funcionalidades `[Verificado MS Learn]`.
   - Todo dispositivo sin cobertura formal de Extended Security Updates (ESU) debe quedar bloqueado por política de versión mínima hacia Windows 11 24H2/25H2 `[Decisión / Propuesta Editorial]`.
2. **Arquitectura y calendario de Hotpatch en Windows 11 Enterprise 24H2+ `[Verificado MS Learn]`:**
   - El calendario anual se divide en **4 meses Baseline con reinicio obligatorio (enero, abril, julio y octubre)** y **8 meses Hotpatch sin reinicio** (febrero-marzo, mayo-junio, agosto-septiembre y noviembre-diciembre) `[Verificado MS Learn]`.
   - Exige obligatoriamente **Virtualization-based Security (VBS)** activo (`VirtualizationBasedTechnology` CSP) y estar en la versión Baseline vigente `[Verificado MS Learn]`.
   - Exclusivamente en equipos **Arm64**, exige deshabilitar el uso de binarios híbridos CHPE (`DisableCHPE` / `HotPatchRestrictions=1`); además, las actualizaciones de seguridad de **Microsoft 365 Apps de 32 bits en Windows Arm finalizan en diciembre de 2026** `[Verificado MS Learn]`.
3. **Transición a Apple Declarative Device Management (DDM) `[Verificado MS Learn]`:**
   - Con la deprecación de comandos MDM heredados de actualización de software en **Apple OS 26** (iOS 26, iPadOS 26 y macOS 26), las políticas de actualización deben migrarse a **DDM en Settings Catalog** (*Software Update* / *Software Update Enforce Latest*) `[Verificado MS Learn]`.
   - Las políticas de protección y configuración de aplicaciones MAM exigen **iOS/iPadOS 17.x o posterior** `[Verificado MS Learn]`.
4. **Consolidación en Android Enterprise y AOSP tras fin de Device Administrator `[Verificado MS Learn]`:**
   - Intune finalizó el soporte de *Android device administrator* en dispositivos con GMS en diciembre de 2024 `[Verificado MS Learn]`.
   - La administración basada en usuario requiere **Android 10.0+** (*Personally-owned Work Profile*, *Corporate-owned Work Profile*, *Fully Managed* y *AOSP user-based*) y los escenarios sin usuario requieren **Android 8.0+** (*Android Enterprise Dedicated* y *AOSP userless*, soportando desde octubre de 2026 en la release `2610` *referenced apps* por nombre de paquete en AOSP) `[Verificado MS Learn]`.
5. **Deprecación de Dual Scan en Windows Update `[Verificado MS Learn]`:**
   - La directiva clásica *Dual Scan* ha sido deprecada y sustituida por la política **Scan source** en Windows Autopatch / Windows Update `[Verificado MS Learn]`.
6. **Asimetría de latencia y duplicación en el pipeline hacia Log Analytics `[Verificado MS Learn]`:**
   - `AuditLogs` y `OperationalLogs` se envían inmediatamente en lotes de ~5 minutos, pero `DeviceComplianceOrg` e `IntuneDevices` se exportan una vez cada 24 horas (ventana de **hasta 48 horas**) y pueden **duplicar hasta el 100% de los registros** en 24h, obligando a deduplicar en KQL mediante `summarize arg_max()` `[Verificado MS Learn]`.

### 3.3 Topología Funcional de Señales e Integración Cross-Workload

```
+-----------------------------------------------------------------------------------+
|                        PLANO DE IDENTIDAD Y ACCESO (ENTRA ID)                     |
|   Conditional Access + Continuous Access Evaluation (CAE) + App Protection CA     |
+-----------------------------------------+-----------------------------------------+
                                          ^
                   Estado Compliant /     |     Salud App + MTD
                     Noncompliant         |   (Mobile & Edge Win)
                                          |
+----------------------+     +------------+-------------+     +---------------------+
|  DEFENDER XDR / MDE  | <-> |  MICROSOFT INTUNE PLAN 1 | --> |  SENTINEL / MONITOR |
| - Nivel Riesgo Host  |     | - Device Compliance      |     | - IntuneAuditLogs   |
| - Reglas ASR (1121)  |     | - Settings Catalog & DDM |     | - OperationalLogs   |
| - MDVM Security Tasks|     | - Security Baselines     |     | - ComplianceOrg     |
| - Isolate / LiveResp |     | - Autopatch + Hotpatch   |     | - IntuneDevices     |
+----------+-----------+     | - Multi Admin Approval   |     +---------------------+
           ^                 +------------+-------------+
           |                              |
           | Señales Endpoint DLP / IRM   | MDM (CSP/DDM) & MAM (APP)
           v                              v
+----------+-----------+     +------------+-----------------------------------------+
|  MICROSOFT PURVIEW   |     | FLOTA CORPORATIVA Y BYOD                             |
| - Endpoint/Edge DLP  |     | Win 11 24H2+, macOS, iOS/iPadOS 17+, Android 10+/AOSP|
| - Adaptive Protection|     +------------------------------------------------------+
+----------------------+
```

### 3.4 Anatomía Técnica de Evaluación y Diagnóstico de Estados en Intune

Para diagnosticar correctamente desviaciones en la flota, el analista SecOps debe interpretar con exactitud los cuatro estados por ajuste (*Per-setting status*) `[Verificado MS Learn]` y la taxonomía operativa de fallos `[Decisión / Propuesta Editorial]`:

- **`Not compliant` `[Verificado MS Learn]`:** El valor reportado por el dispositivo incumple explícitamente el umbral exigido por la política (ej. cifrado desactivado, firewall apagado o build inferior al mínimo).
- **`Not applicable` `[Verificado MS Learn]`:** El CSP o ajuste no puede aplicarse en esa edición/plataforma o carece de un prerrequisito físico de hardware (ej. BitLocker con requisito TPM 2.0 en un equipo sin chip TPM); en activos con acceso a datos sensibles debe auditarse como posible excepción de seguridad `[Decisión / Propuesta Editorial]`.
- **`Error` `[Verificado MS Learn]`:** Fallo en la comunicación o ejecución del proveedor CSP en el sistema operativo.
- **`Conflict` `[Verificado MS Learn]`:** Dos o más perfiles (ej. *Security Baseline* frente a *Settings Catalog* o política heredada) intentan escribir valores divergentes sobre el mismo URI OMA-URI / CSP; exige depurar la configuración redundante.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Diseño RBAC de Mínimo Privilegio, Scope Tags y Reglas Anti-Deadlock de MAA

La administración segura de Intune exige combinar **roles de Microsoft Entra ID**, **roles RBAC propios de Intune** (integrados y personalizados), segmentación de visibilidad por **Scope Tags** y políticas de acceso de **Multi Admin Approval (MAA)** `[Verificado MS Learn]`.

> **Reglas operativas críticas de Multi Admin Approval (MAA) `[Verificado MS Learn]`:**
> - **Cobertura interactiva y programática:** MAA intercepta tanto acciones interactivas en `intune.microsoft.com` como llamadas automatizadas **application-authenticated (app-auth)** en Microsoft Graph API (permitiendo excluir hasta **50 Enterprise Applications** por política bajo revisión periódica).
> - **Requisitos estrictos del grupo aprobador:** El grupo aprobador debe ser un **grupo de seguridad** con membresía directa (listas de distribución, grupos Microsoft 365 y grupos anidados fallan silenciosamente) y debe estar **asignado directamente como Member group de al menos un rol RBAC de Intune** con permiso `Read` sobre el recurso protegido; si no lo está, Intune remueve periódicamente a sus integrantes.
> - **Prevención de interbloqueo (*Deadlock*) en políticas de tipo `Role`:** Activar MAA para el tipo `Role` exige doble aprobación para cualquier cambio ulterior sobre roles y asignaciones RBAC (incluidas las que el propio MAA necesita). Configure y valide primero todas las asignaciones RBAC antes de activar la política MAA de tipo `Role` `[Verificado MS Learn]`.
> - **Expiración de solicitudes:** Una vez enviada o aprobada, si el solicitante original no pulsa **Complete** dentro de **3 días**, la solicitud pasa a estado `Expired` `[Verificado MS Learn]`.

| Rol Oficial / Personalizado | Plano RBAC | Equipo / Función Operativa | Permisos Clave Otorgados | Estrategia PIM / JIT y Controles Compensatorios | Etiqueta |
|---|---|---|---|---|---|
| **Intune Read Only Operator** | Intune RBAC integrado | SOC L1 / Analista de Monitoreo y Auditores GRC | Lectura completa de dispositivos, estado de cumplimiento, perfiles, líneas base, reportes y `Audit logs`, sin permisos de escritura ni acciones remotas. | Asignación acotada por *Scope Tags* cuando aplique; uso seguro para guardias diarias `D-01` a `D-07` y revisiones de auditoría. | `[Verificado MS Learn]` |
| **Endpoint Security Manager** | Entra ID / Intune RBAC integrado | SOC L2 / Endpoint Security Engineer | Administración del nodo `Endpoint security` (Security Baselines, Antivirus, Disk Encryption, Firewall, ASR, EDR onboarding, Security Tasks) y políticas de cumplimiento. | **Elegible en Entra ID PIM** (duración máxima 4 horas `[Decisión / Propuesta Editorial]`), MFA phishing-resistant y justificación obligatoria con ticket. | `[Verificado MS Learn]` |
| **Custom Role — SecOps Endpoint Responder** | Intune Custom RBAC | SOC L2 / Incident Response Team | Permisos granulares: `ManagedDevices/Read`, `RemoteTasks/RemoteLock`, `RemoteTasks/SyncDevice`, `RemoteTasks/LocateDevice`, `RemoteTasks/RotateBitLockerKeys`; `RemoteTasks/Wipe` y `RemoteTasks/Retire` sujetos a **MAA**. | Activación JIT en PIM restringida a incidentes activos `[Decisión / Propuesta Editorial]`; ejecución de `Wipe`/`Retire` bloqueada sin segunda firma en **MAA** `[Verificado MS Learn]`. | `[Decisión / Propuesta Editorial]` |
| **Policy and Profile Manager** | Intune RBAC integrado | Microinformática / Endpoint Engineering | Creación y asignación de perfiles de configuración de productividad (Wi-Fi, VPN, certificados SCEP/PKCS), filtros de asignación e inscripción corporativa dentro de sus *Scope Tags*. | Elegible vía PIM for Groups (máximo 8 horas `[Decisión / Propuesta Editorial]`); cambios sobre *Settings Catalog* y *Scripts* gobernados por **MAA** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Application Manager** | Intune RBAC integrado | Equipo de Aplicaciones y Movilidad | Gestión de aplicaciones gestionadas, políticas de configuración de apps y políticas **App Protection (MAM)** más *App selective wipe*. | Elegible vía PIM; despliegues de *Apps* sujetos a aprobación cruzada en **MAA** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Custom Role — MAA Access Policy Admin & Approver** | Intune Custom RBAC | Security Lead / Change Advisory Board | Gestión de políticas de acceso MAA (`Create/Read/Update/Delete access policy`) o pertenencia directa al grupo de seguridad aprobador con permiso `<Recurso>/Read`. | Segregación nativa: ningún administrador (ni siquiera Global Admin) puede aprobar su propia solicitud en Intune `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Intune Administrator** *(Intune Service Administrator)* | Microsoft Entra ID | Arquitecto Principal de Plataforma *(Tier 3)* | Control total sobre Intune, conectores tenant-wide (MDE, APNs, Android Enterprise, Windows Security Center), *Diagnostics settings* y licenciamiento de administradores. | **Estrictamente elegible en Entra ID PIM** (máximo 2 horas, aprobación dual, Authentication Context desde PAW) `[Decisión / Propuesta Editorial]`. Prohibido en operación rutinaria `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

### 4.2 Matriz RACI Consultiva entre Ciberseguridad / SOC y Microinformática `[Decisión / Propuesta Editorial]`

| Dominio de Gobierno y Operación | Ciberseguridad / SOC | Microinformática / TI | Identidad (Entra) |
|---|---|---|---|
| Políticas de *Device Compliance*, *Grace Period* y *Validity Period* | **A / R** | C | C |
| Políticas de Acceso Condicional (`Compliant` / `App Protection`) y CAE | C | I | **A / R** |
| Políticas *Endpoint Security* (AV, BitLocker, Firewall MDM, ASR, Onboarding MDE) | **A / R** | C | I |
| *Security Baselines* (evaluación de versiones, análisis de diff y control de conflictos) | **A / R** | C / S | I |
| Inscripción Autopilot / ADE / Android Enterprise y perfiles Wi-Fi / VPN / Impresión | C | **A / R** | C |
| *Windows Autopatch* y *Hotpatching* (anillos regulares vs. aceleración por CISA KEV) | C *(A en KEV)* | **A / R** | I |
| Certificados SCEP/PKCS, APNs y conectores de plataforma | C *(auditoría)* | **A / R** *(operación)* | C |
| Aprobaciones *Multi Admin Approval (MAA)* y vigilancia de `IntuneAuditLogs` | **A / R** | R *(solicitante)* | C |
| Ejecución de Playbooks `IR-01`, `IR-02`, `IR-03` y gestión de excepciones de riesgo | **A / R** | S | S |

### 4.3 Gobierno Formal de Excepciones de Seguridad en Endpoints `[Decisión / Propuesta Editorial]`

Cuando una estación o lote de hardware no pueda cumplir un control obligatorio (por ejemplo, incompatibilidad temporal con una regla ASR o falta de TPM 2.0 en equipos próximos a retiro), toda excepción en grupos de exclusión de Intune exige documentar siete atributos auditables `[Decisión / Propuesta Editorial]`:
1. Identificadores exactos (`DeviceId`, `DeviceName`, `UPN` y propietario del activo).
2. Control específico exceptuado (ajuste de BitLocker, perfil Firewall o GUID de regla ASR).
3. Causa técnica verificada e imposibilidad de remediación inmediata.
4. Controles compensatorios activos (segmentación de red, restricción de aplicaciones sensibles en Conditional Access o monitoreo reforzado en MDE).
5. Aprobación formal del Security Manager / CISO Office.
6. Fecha estricta de caducidad máxima (**<= 90 días**, sin prórroga automática).
7. Plan vinculado de cierre definitivo (recambio de hardware o actualización de aplicación).

---

## 5. Cadencia Operativa Diaria

### D-01 — Detección de Dispositivos Noncompliant con Sesión Activa en Entra ID
- **Objetivo:** Identificar dispositivos activos en estado `Noncompliant` que conservan sesiones autenticadas exitosas sobre recursos corporativos, detectando brechas en Acceso Condicional o abusos de *Grace Period* `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Compliance > Monitor > Noncompliant devices` + `https://entra.microsoft.com > Identity > Monitoring & health > Sign-in logs` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 (detección) / SOC L2 (escalamiento) `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.AA-05` / Initial Access (`TA0001`), Valid Accounts (`T1078`).
- **Procedimiento:**
  1. Filtrar en Intune `Compliance state = Noncompliant` con `Last check-in < 24h`, separando vistas por sistema operativo (`Windows`, `macOS`, `iOS/iPadOS`, `Android`).
  2. Clasificar el ajuste incumplido (*Noncompliant setting*) en Categoría A crítica (cifrado desactivado, nivel de riesgo MDE `High`, antivirus/EDR inactivo, jailbreak/root) frente a Categoría B administrativa (versión mínima de SO pendiente) `[Decisión / Propuesta Editorial]`.
  3. Ejecutar correlación por `DeviceId` y `UPN` contra `SigninLogs` de las últimas 24 horas verificando si ocurrieron inicios de sesión con `ResultType == 0` una vez vencido el *Grace period*.
  4. Si se confirma sesión activa en un equipo `Noncompliant` fuera de gracia, abrir incidente prioritario por *Potential Conditional Access Bypass* e involucrar al equipo de Identidad para corregir exclusiones en la política CA.
  5. Documentar cada hallazgo Categoría A en ITSM asignando remediación inmediata a SecOps o Microinformática según la matriz RACI `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario CSV / resultado de Consulta KQL 2 adjunto al parte de turno SOC `[Decisión / Propuesta Editorial]`.

### D-02 — Verificación del Conector Defender for Endpoint, Cobertura EDR y Estado Antivirus
- **Objetivo:** Asegurar la continuidad del enlace bidireccional Intune <-> MDE y eliminar brechas de onboarding EDR o agentes antimalware degradados antes del procesamiento diario de alertas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Endpoint security > Overview`, `Endpoint security > Microsoft Defender for Endpoint` y `Reports > Microsoft Defender Antivirus` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-09` / Defense Evasion (`T1562` Impair Defenses).
- **Procedimiento:**
  1. Confirmar en `Endpoint security > Microsoft Defender for Endpoint` que `Connection status` sea **Enabled** y que la última sincronización tenga menos de 24 horas `[Verificado MS Learn]`.
  2. Escalar como incidente crítico inmediato cualquier estado `Inactive` o error de sincronización, pues interrumpe el marcado automático de no cumplimiento por nivel de riesgo MDE `[Decisión / Propuesta Editorial]`.
  3. Cotejar el contador de *Devices onboarded to Microsoft Defender for Endpoint* frente al total de dispositivos inscritos por plataforma, asignando perfil de onboarding EDR a todo equipo faltante `[Verificado MS Learn]`.
  4. Revisar `Antivirus agent status` y `Detected malware`, forzando actualización de inteligencia de seguridad o sincronización en equipos con protección en tiempo real desactivada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/log de salud del conector MDE y listado diario de remediación sobre endpoints sin sensor activo `[Verificado MS Learn]`.

### D-03 — Auditoría de Cambios Administrativos y Gestión de Solicitudes Multi Admin Approval (MAA)
- **Objetivo:** Conciliar toda modificación de políticas de seguridad o ejecución de acciones remotas contra tickets aprobados de cambio y procesar con trazabilidad la bandeja de **Multi Admin Approval** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Tenant administration > Audit logs` y `Tenant administration > Multi Admin Approval > All requests` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Security Administrator `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-01`, `GV.RR-02` / Account Manipulation (`T1098`).
- **Procedimiento:**
  1. Consultar `Audit logs` de las últimas 24 horas filtrando `Category` en `Compliance`, `DeviceConfiguration`, `DeviceSecurity`, `Role`, `Enrollment` y operaciones `Wipe`, `Retire`, `Delete` `[Verificado MS Learn]`.
  2. Verificar que el campo `Actor` corresponda a cuentas humanas nominales con activación PIM vigente o a Service Principals autorizados y documentados en ITSM `[Decisión / Propuesta Editorial]`.
  3. Revisar en `Multi Admin Approval > All requests` (o `Admin tasks`) solicitudes en estado `Needs approval` o `Approved` próximas a vencer su ventana de **3 días** `[Verificado MS Learn]`.
  4. En solicitudes de scripts de Windows PowerShell, inspeccionar la columna **Agent Response** generada por el *Change Review Agent* cuando esté habilitado antes de emitir aprobación `[Verificado MS Learn]`.
  5. Escalar de inmediato al playbook `AH-03` (`IR-03`) cualquier cambio crítico sin ticket aprobado o intento no autorizado de excluir aplicaciones en políticas MAA.
- **Evidencia Auditable:** Bitácora diaria de conciliación `IntuneAuditLogs` <-> ITSM y registro de aprobaciones/rechazos MAA `[Verificado MS Learn]`.

### D-04 — Control Diario de Errores y Conflictos en Perfiles de Security Baselines
- **Objetivo:** Detectar desviaciones tempranas, fallos de CSP y colisiones entre perfiles de **Security Baselines** y políticas de **Settings Catalog** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Endpoint security > Security baselines > [Perfil] > Monitor` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.PS-01` / Defense Evasion (`TA0005`).
- **Procedimiento:**
  1. Inspeccionar los paneles de monitoreo de las líneas base activas (*Windows 10 and later*, *Defender for Endpoint*, *Microsoft 365 Apps* y *Microsoft Edge*) `[Verificado MS Learn]`.
  2. Filtrar los estados `Conflict` y `Error` en la vista *Per-setting status* para determinar si una modificación reciente introdujo parámetros contradictorios sobre un mismo CSP `[Verificado MS Learn]`.
  3. Identificar qué políticas compiten en la vista de detalle del dispositivo afectado y eliminar el ajuste duplicado en la política secundaria para restablecer determinismo `[Verificado MS Learn]`.
  4. Registrar tickets de infraestructura cuando un ajuste (ej. VBS / Credential Guard) falle globalmente en un modelo específico de hardware por configuración de firmware BIOS/UEFI `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Captura o exportación de *Per-setting status* con seguimiento de conflictos abiertos `[Verificado MS Learn]`.

### D-05 — Correlación de Incidentes de Microsoft Defender XDR con Postura del Endpoint en Intune
- **Objetivo:** Enriquecer cada incidente activo de severidad alta o media en Defender XDR con el contexto de cumplimiento, cifrado y última sincronización del endpoint en Intune `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` + `https://intune.microsoft.com > Devices > All devices` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2 `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `RS.AN-03` / Execution (`TA0002`), Credential Access (`TA0006`).
- **Procedimiento:**
  1. Seleccionar en la cola unificada de incidentes XDR aquellos con severidad `High` o `Medium` que involucren entidades de tipo dispositivo `[Verificado MS Learn]`.
  2. Consultar para cada host involucrado su estado en Intune (`Compliant`/`Noncompliant`), fecha de último check-in, propiedad (`Corporate`/`Personal`) y políticas aplicadas `[Verificado MS Learn]`.
  3. Confirmar la custodia de la clave de recuperación BitLocker/FileVault antes de escalar acciones de contención destructiva `[Verificado MS Learn]`.
  4. Documentar en el expediente XDR si una degradación previa de postura actuó como factor contribuyente y activar `AH-01` (`IR-01`) ante compromiso confirmado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Notas estructuradas de postura Intune registradas dentro del incidente en `security.microsoft.com` `[Verificado MS Learn]`.

### D-06 — Vigilancia de Inscripciones Diarias (Enrollments) y Restricciones de Plataforma
- **Objetivo:** Detectar inscripciones no autorizadas, abusos de cuentas *Device Enrollment Manager (DEM)* o fallos anómalos en controles que bloquean dispositivos personales en MDM `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > All devices` y `Devices > Monitor > Enrollment failures` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.AM-01`, `PR.AA-05` / Initial Access (`TA0001`).
- **Procedimiento:**
  1. Listar dispositivos inscritos en las últimas 24 horas validando propiedad (`Corporate` vs. `Personal`), plataforma y correspondencia con altas formales en TI/RRHH `[Decisión / Propuesta Editorial]`.
  2. Auditar inscripciones efectuadas mediante cuentas *Device Enrollment Manager (DEM)* verificando que correspondan exclusivamente a quioscos o equipos compartidos autorizados `[Verificado MS Learn]`.
  3. Verificar que `Enrollment device platform restrictions` continúen rechazando inscripciones MDM personales no permitidas `[Verificado MS Learn]`.
  4. Revisar `Enrollment failures` descartando fallos sistémicos de Autopilot, Apple ADE o Managed Google Play `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de altas de inventario verificadas y resumen de `IntuneOperationalLogs` `[Verificado MS Learn]`.

### D-07 — Monitoreo de Alertas de Windows Autopatch y Bloqueos de App Protection (MAM)
- **Objetivo:** Atender tempranamente alertas de salud de actualizaciones (incluyendo elegibilidad de *Hotpatch*) y bloqueos por riesgo en aplicaciones protegidas por MAM `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Manage updates > Windows updates > Monitor` y `Apps > Monitor > App protection status` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / SOC L1 `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.PS-02`, `PR.DS-02` / Collection (`TA0009`).
- **Procedimiento:**
  1. Revisar alertas operativas activas en **Windows Autopatch**, prestando atención inmediata a la alerta `Hotpatch – VBS not running` en estaciones Windows 11 24H2/25H2 `[Verificado MS Learn]`.
  2. Inspeccionar en `App protection status` usuarios o dispositivos bloqueados por *Conditional Launch* en iOS, Android o **Microsoft Edge for Business en Windows** tras detección de amenaza en Windows Security Center o MTD `[Verificado MS Learn]`.
  3. Confirmar la finalización efectiva de las órdenes de `App selective wipe` emitidas en las últimas 24 horas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura diaria de alertas Autopatch y estado de acciones en `App selective wipe` `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01 — Análisis de Tendencias Organizacionales de Cumplimiento y Cobertura Conditional Access
- **Objetivo:** Identificar degradaciones estructurales semana contra semana por sistema operativo o departamento y asegurar que Conditional Access cubra la totalidad de aplicaciones críticas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Reports > Device compliance > Organizational` + `https://entra.microsoft.com > Protection > Conditional Access > Insights and reporting` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / Identity Architect `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.OV-03`, `PR.AA-05` / Valid Accounts (`T1078`).
- **Procedimiento:**
  1. Generar el reporte organizacional de cumplimiento comparando la variación porcentual respecto a la semana previa por plataforma y unidad organizativa `[Verificado MS Learn]`.
  2. Investigar toda caída superior al 5% en un segmento `[Decisión / Propuesta Editorial]`, determinando si obedece a un *Quality/Feature update*, expiración de certificados o nueva regla de cumplimiento.
  3. Contrastar en *Conditional Access Insights and reporting* inicios de sesión a aplicaciones críticas donde no se evaluó `Require device to be marked as compliant` ni `Require app protection policy`, cerrando brechas de alcance `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semanal de tendencia de cumplimiento y cobertura CA `[Verificado MS Learn]`.

### S-02 — Gobernanza Semanal de Reglas Attack Surface Reduction (ASR): Detecciones y Modo Block
- **Objetivo:** Evaluar telemetría de auditoría/bloqueo ASR para promover reglas desde `Audit` hacia `Block` y controlar desviaciones o exclusiones excesivas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Reports > Attack surface reduction rules` + `https://intune.microsoft.com > Endpoint security > Attack surface reduction` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.PS-01`, `DE.CM-09` / Execution (`T1059`, `T1204`), Credential Access (`T1003.001`).
- **Procedimiento:**
  1. Analizar en `Detections` los eventos `Audited` y `Blocked` de los últimos 7 días sobre reglas críticas (robo de credenciales en LSASS, procesos hijos desde Office, scripts ofuscados, WMI/PSExec y ejecución desde USB no confiable) `[Verificado MS Learn]`.
  2. En `Configuration`, identificar endpoints con reglas críticas en `Off` o `Audit` no autorizados y contrastar eventos locales (`1121` Block, `1122` Audit y `1129` en `Microsoft-Windows-Windows Defender/Operational`) `[Verificado MS Learn]`.
  3. Validar que cualquier paso temporal a `Audit` o exclusión puntual cuente con ticket aprobado, justificación en el perfil y fecha de revisión `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación semanal de configuración ASR y registro auditado de exclusiones vigentes `[Verificado MS Learn]`.

### S-03 — Procesamiento Semanal de Security Tasks (Defender Vulnerability Management -> Intune)
- **Objetivo:** Ejecutar de extremo a extremo el flujo de remediación de vulnerabilidades priorizadas desde MDVM hacia Intune dentro de los acuerdos internos de nivel de servicio `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Endpoint security > Security tasks` y `https://security.microsoft.com > Exposure management / Vulnerability management > Remediation` `[Verificado MS Learn]`.
- **Rol Responsable:** Vulnerability Management Analyst / Endpoint Engineering `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.RA-01`, `PR.PS-02` / Exploitation for Client Execution (`T1203`).
- **Procedimiento:**
  1. Revisar todas las `Security tasks` pendientes en Intune priorizando vulnerabilidades incluidas en **CISA KEV**, exploits activos confirmados y CVSS >= 9.0 `[Verificado MS Learn]`.
  2. Aceptar la tarea en Intune y asignar el despliegue de parche de aplicación, perfil de mitigación en *Settings Catalog* o actualización de sistema operativo sobre anillo piloto y producción `[Verificado MS Learn]`.
  3. Marcar `Complete` únicamente tras verificar la reducción efectiva de equipos expuestos en el portal de Microsoft Defender `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tablero semanal de *Security tasks* procesadas y cumplimiento de SLA interno `[Verificado MS Learn]`.

### S-04 — Auditoría de Privilegios RBAC, Activaciones PIM, Scope Tags y Políticas MAA
- **Objetivo:** Verificar que ningún administrador opere con permisos permanentes innecesarios ni existan configuraciones que debiliten o bloqueen **Multi Admin Approval** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Tenant administration > Roles` + `Multi Admin Approval > Access policies` + `https://entra.microsoft.com > Identity governance > Privileged Identity Management` `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Platform Administrator / GRC Lead `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.RR-02`, `PR.AA-05` / Valid Accounts (`T1078.004`).
- **Procedimiento:**
  1. Revisar asignaciones activas y elegibles de `Global Administrator`, `Intune Administrator` y `Endpoint Security Manager`, erradicando asignaciones permanentes humanas salvo cuentas *Break Glass* `[Decisión / Propuesta Editorial]`.
  2. Confirmar que cada administrador delegado posea únicamente los **Scope Tags** de su región o unidad organizativa `[Verificado MS Learn]`.
  3. Verificar que los grupos aprobadores de **MAA** sean grupos de seguridad directos vinculados a un rol RBAC de Intune (evitando vaciamiento automático de miembros) y auditar las aplicaciones empresariales excluidas (tope de 50 por política) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación semanal de roles RBAC, historial de activaciones PIM y lista de exclusiones MAA `[Verificado MS Learn]`.

### S-05 — Vigilancia de Certificados (APNs, SCEP/PKCS), Tokens ABM/VPP y Conectores del Tenant
- **Objetivo:** Evitar interrupciones sistémicas de administración o acceso de red anticipando vencimientos de certificados y degradaciones de conectores externos `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Tenant administration > Connectors and tokens` y `Devices > Monitor > Certificates` `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Platform Administrator `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.AA-02`, `DE.CM-09` / Impair Defenses (`T1562`).
- **Procedimiento:**
  1. Verificar estado y días restantes del **Apple MDM Push certificate (APNs)**, tokens *Apple Automated Device Enrollment (ADE/ABM)*, tokens *Volume Purchase Program (VPP)*, enlace *Managed Google Play* y conectores NDES / PKCS `[Verificado MS Learn]`.
  2. Activar alerta preventiva interna cuando reste menos de **45 días** para cualquier token Apple (verificando resguardo del Apple ID corporativo original del APNs) o **30 días** para certificados SCEP/PKCS `[Decisión / Propuesta Editorial]`.
  3. Investigar certificados de dispositivo en estado `Error` o `Revoked` coordinando remediación inmediata con el equipo de infraestructura PKI `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de estado de `Connector status` y reporte de certificados próximos a expirar `[Verificado MS Learn]`.

### S-06 — Limpieza de Inventario Inactivo, Control de "Phantom Compliant" y Conciliación Entra ID
- **Objetivo:** Depurar activos inactivos que distorsionan métricas de cobertura y eliminar el riesgo de dispositivos de ex-colaboradores o silenciosos que conservan estado `Compliant` aparente `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Organize devices > Device cleanup rules` + `https://entra.microsoft.com > Identity > Devices > All devices` `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Platform Administrator / Identity Administrator `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.AM-01`, `PR.AA-05` / Valid Accounts (`T1078`).
- **Procedimiento:**
  1. Ejecutar filtro sobre dispositivos con `Compliance state = Compliant` y `Last check-in > 10 días` (*Phantom Compliant*) para validar si corresponden a ausencias justificadas o equipos apagados/extraviados que requieren bloqueo preventivo `[Decisión / Propuesta Editorial]`.
  2. Cruzar bajas semanales de RRHH (cuentas deshabilitadas en Entra ID) contra dispositivos que permanezcan inscritos en Intune, disparando recupero físico o `Retire`/`Wipe` `[Decisión / Propuesta Editorial]`.
  3. Revisar los equipos procesados por **Device cleanup rules** (30–90 días) y deshabilitar o depurar sus objetos correspondientes en Microsoft Entra ID para evitar objetos huérfanos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de higiene de inventario Intune <-> Entra ID y bajas ejecutadas `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01 — Auditoría Profunda de Enforcement Real: BitLocker/FileVault, Firewall MDM y ASR
- **Objetivo:** Confirmar mensualmente que los tres pilares preventivos del endpoint estén efectivamente activos en el sistema operativo y no solo entregados (`Succeeded`) por el canal MDM `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Monitor > Encryption report`, `Reports > Firewall > MDM Firewall status for Windows 10 and later` y `https://security.microsoft.com > Reports > Attack surface reduction rules` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.DS-01`, `PR.PS-01` / Data from Local System (`T1005`), Lateral Movement (`TA0008`).
- **Procedimiento:**
  1. **BitLocker y FileVault:** Auditar *Encryption report* exigiendo `Encrypted`, `TPM 2.0` y comprobando que el 100% de dispositivos cifrados posea **Recovery Key custodiada** en Microsoft Entra ID / Intune; tratar errores `Compatible TPM not found` mediante plan de renovación de hardware y excepción formal `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  2. **Firewall MDM:** Verificar en *MDM Firewall status* que ningún equipo figure `Disabled`, `Temporarily Disabled` ni `Limited`, e investigar aquellos con `Target = Group Policy` para eliminar colisiones GPO en equipos Hybrid Joined (validando en diagnósticos locales la ruta `HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\Mdm\FirewallRules` en lugar de confiar únicamente en `wf.msc`) `[Verificado MS Learn]`.
  3. **ASR y Registro de Excepciones:** Contrastar estado local (`Get-MpPreference`) en hosts con discrepancias y revocar toda excepción vencida (> 90 días) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe mensual del Tridente de Hardening y libro de excepciones de seguridad al día `[Decisión / Propuesta Editorial]`.

### M-02 — Calibración Mensual de Políticas de Cumplimiento, Ventanas de Gracia y Versiones de SO
- **Objetivo:** Mantener actualizados los criterios de *Device Compliance* frente a nuevos lanzamientos de sistemas operativos y auditar parámetros globales críticos del tenant `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Compliance > Compliance policy settings` y `Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / SOC Manager `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.AA-05`, `ID.RA-01` / Initial Access (`TA0001`).
- **Procedimiento:**
  1. Verificar que `Mark devices with no compliance policy assigned as` permanezca en **Not compliant** y que el `Compliance status validity period` no supere el umbral corporativo aprobado (7–14 días `[Decisión / Propuesta Editorial]`) `[Verificado MS Learn]`.
  2. Actualizar builds mínimos permitidos para Windows 11 (24H2/25H2), macOS, iOS/iPadOS (17+) y Android (10+) tras el cierre mensual de los anillos de actualización `[Verificado MS Learn]`.
  3. Analizar en *Conditional Access Insights* bloqueos por incumplimiento para mejorar plantillas de notificación preventiva al usuario antes del vencimiento del *Grace period* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Configuración exportada de *Compliance policy settings* y tabla actualizada de builds mínimos `[Verificado MS Learn]`.

### M-03 — Evaluación y Adopción Controlada de Nuevas Versiones de Security Baselines
- **Objetivo:** Incorporar de forma segura nuevas versiones GA de **Security Baselines** evitando interrupciones productivas, colisiones CSP y efectos de *tattooing* `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Endpoint security > Security baselines` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / Microinformática `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.PS-01` / Defense Evasion (`TA0005`).
- **Procedimiento:**
  1. Revisar nuevas instancias GA publicadas (ej. Windows **v26H2**, M365 Apps **v2512**, Edge **v139**, MDE **v24H1**), respetando la directriz oficial de no desplegar versiones *Preview* en producción ni aplicar la baseline de MDE sobre escritorios virtuales VDI/VMs `[Verificado MS Learn]`.
  2. Exportar y analizar línea por línea las diferencias de settings antes de actualizar cualquier perfil, validando un perfil nuevo sobre anillo piloto durante 7 a 14 días `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Documentar valores explícitos de reversión para configuraciones propensas a *tattooing* antes de retirar asignaciones antiguas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz comparativa de versión de baseline y acta de aprobación de paso a producción `[Verificado MS Learn]`.

### M-04 — Revisión Ejecutiva de Microsoft Secure Score (Device) y Plan de Mejora Continua
- **Objetivo:** Evaluar la progresión mensual de controles preventivos de endpoints en **Microsoft Secure Score** y priorizar mejoras estructurales `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Exposure management > Secure score` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / CISO `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.OV-03`, `ID.IM-01` / Multiple Tactics.
- **Procedimiento:**
  1. Extraer el puntaje actual, porcentaje alcanzado y tendencia de 90 días para la categoría **Device**, junto con la comparativa sectorial (*Similar organizations*) `[Verificado MS Learn]`.
  2. Seleccionar tres a cinco *Improvement actions* de mayor impacto técnico factibles de implementar vía Intune Plan 1 en el mes siguiente `[Decisión / Propuesta Editorial]`.
  3. Auditar las acciones marcadas como *Risk accepted* o *Resolved through third party* confirmando respaldo documental vigente `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte ejecutivo mensual de *Secure Score (Device)* presentado al CISO `[Verificado MS Learn]`.

### M-05 — Gobernanza Mensual de Windows Autopatch y Elegibilidad de Hotpatch Updates
- **Objetivo:** Auditar la tasa de convergencia mensual de actualizaciones de calidad y eliminar barreras técnicas que impidan aplicar **Hotpatch updates** sin reinicio en Windows 11 Enterprise `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Manage updates > Windows updates` y `Reports > Windows updates > Hotpatch quality update report` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Engineering / Vulnerability Management Analyst `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.PS-02` / Exploitation for Privilege Escalation (`T1068`).
- **Procedimiento:**
  1. Verificar tasas de cumplimiento por anillo de despliegue de **Windows Autopatch** (`Test`, `First`, `Fast`, `Broad`) a los 7, 14 y 21 días desde Patch Tuesday `[Decisión / Propuesta Editorial]`.
  2. Auditar el **Hotpatch quality update report** en los ocho meses anuales de hotpatch, identificando equipos relegados a LCU con reinicio por no tener **VBS en ejecución** o no estar en la *Baseline update* trimestral vigente `[Verificado MS Learn]`.
  3. En flotas con procesadores Arm64, auditar la aplicación de `DisableCHPE` y la erradicación de Microsoft 365 Apps de 32 bits antes del fin de soporte de seguridad en diciembre de 2026 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación mensual del *Hotpatch quality update report* y plan de remediación de equipos inelegibles `[Verificado MS Learn]`.

### M-06 — Verificación Mensual del Pipeline de Telemetría hacia Log Analytics y Microsoft Sentinel
- **Objetivo:** Garantizar la integridad, continuidad, costo controlado y correcta deduplicación de las cuatro tablas de Intune en el SIEM `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Reports > Diagnostics settings` + `https://security.microsoft.com > Investigation & response > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Detection Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-01`, `ID.IM-02` / Defense Evasion (`T1562.008`).
- **Procedimiento:**
  1. Validar en `Diagnostics settings` que las cuatro fuentes (`AuditLogs`, `OperationalLogs`, `DeviceComplianceOrg`, `IntuneDevices`) continúen activas hacia el workspace primario de Log Analytics / Sentinel `[Verificado MS Learn]`.
  2. Ejecutar la Consulta KQL 1 comprobando latencia normal en `IntuneAuditLogs`/`IntuneOperationalLogs` y recepción de snapshots diarios dentro del umbral oficial de 24 a 48 horas para `IntuneDeviceComplianceOrg`/`IntuneDevices` `[Verificado MS Learn]`.
  3. Auditar reglas analíticas y workbooks sobre `IntuneDevices` o `IntuneDeviceComplianceOrg` asegurando el uso de `summarize arg_max()` frente a duplicados del exportador diario `[Verificado MS Learn]`.
- **Evidencia Auditable:** Resultado mensual de auditoría KQL de ingesta, volumen y reglas activas en Sentinel `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 — Ejecución de Meses Baseline de Hotpatching y Auditoría de Modernización Apple DDM / Android AOSP
- **Cadencia:** Trimestral (enero, abril, julio y octubre) `[Verificado MS Learn]`.
- **Objetivo:** Asegurar la instalación exitosa de las cuatro actualizaciones acumulativas *Baseline* anuales (con reinicio obligatorio) en Windows 11 Enterprise y certificar la migración plena a protocolos modernos móviles.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Manage updates > Windows updates` y `Devices > Manage devices > Configuration` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Engineering / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Supervisar el cumplimiento del reinicio obligatorio en los meses *Baseline* (**enero, abril, julio y octubre**) y programar en esos mismos meses cualquier salto de versión anual (*Feature update*, ej. 24H2 a 25H2) para preservar continuidad de hotpatch `[Verificado MS Learn]`.
  2. Confirmar que el 100% de dispositivos Apple OS 26 reciba políticas declarativas **DDM** desde *Settings Catalog*, retirando políticas MDM heredadas deprecadas `[Verificado MS Learn]`.
  3. Auditar el inventario Android y Windows verificando cero dispositivos en *Android device administrator* y reducción programada de excepciones Windows 10 con ESU `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte trimestral de convergencia de *Baseline update* y auditoría de versiones de plataforma `[Verificado MS Learn]`.

### T-02 — Access Reviews Trimestrales, Auditoría MAM (BYOD / Edge) y Backup Declarativo en Git vía Graph API
- **Cadencia:** Trimestral `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Recertificar privilegios administrativos y grupos aprobadores MAA, validar endurecimiento MAM y generar copia de respaldo versionada de todas las políticas de Intune `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Identity governance > Access reviews` + `https://intune.microsoft.com > Apps > Protection` + Microsoft Graph PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Lead / Intune Platform Administrator `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Ejecutar *Access Reviews* trimestrales sobre miembros elegibles de `Intune Administrator`, `Endpoint Security Manager`, cuentas `DEM` y grupos de seguridad aprobadores de **Multi Admin Approval** `[Verificado MS Learn]`.
  2. Auditar las configuraciones de *Data Protection* y *Health Checks (Conditional Launch)* en políticas **App Protection (MAM)** de iOS, Android y **Microsoft Edge for Business en Windows** `[Verificado MS Learn]`.
  3. Exportar mediante Microsoft Graph API a archivos JSON firmados en repositorio Git privado todas las políticas de Compliance, Settings Catalog, Security Baselines, Endpoint Security, App Protection, Enrollment Restrictions y Scope Tags para garantizar restauración ante `IR-03` `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Actas cerradas de *Access Reviews* en Entra ID y etiqueta trimestral del respaldo JSON en Git.

### SM-01 — Simulacro Semestral Integrado de Respuesta a Incidentes (`IR-01`, `IR-02`, `IR-03`) y Revisión RACI
- **Cadencia:** Semestral `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Validar en condiciones realistas los tiempos de contención, doble aprobación **MAA** y recuperación de políticas entre SOC, Identidad y Microinformática.
- **Consola y Ruta:** Entorno controlado en `https://intune.microsoft.com`, `https://security.microsoft.com` y `https://entra.microsoft.com`.
- **Rol Responsable:** SOC Manager / Incident Response Lead / Intune Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Ejecutar ejercicio práctico de `IR-01` e `IR-02` sobre equipos de laboratorio validando aislamiento MDE, consulta previa de BitLocker Recovery Key, flujo de solicitud y aprobación **MAA** para `Wipe` y registro de cadena de custodia.
  2. Ejercitar `IR-03` restaurando una política crítica eliminada en entorno de prueba a partir del respaldo JSON trimestral vía Microsoft Graph API.
  3. Actualizar y firmar semestralmente la matriz RACI y los acuerdos internos de SLA entre Ciberseguridad y Operaciones de TI.
- **Evidencia Auditable:** Informe ejecutivo de simulacro semestral con métricas MTTA/MTTC medidas y matriz RACI refrendada `[Decisión / Propuesta Editorial]`.

### A-01 — Ceremonia Anual de Renovación APNs / ABM / VPP y Revisión Estratégica de Arquitectura UEM
- **Cadencia:** Anual `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Renovar de forma segura las credenciales anuales de gestión Apple y revisar la hoja de ruta anual frente a capacidades avanzadas del ecosistema (*Intune Suite* / Windows Enterprise).
- **Consola y Ruta:** `https://intune.microsoft.com > Tenant administration > Connectors and tokens` `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Platform Administrator / CISO Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Ejecutar con al menos 30–45 días de margen la renovación anual del **Apple MDM Push certificate (APNs)** empleando estrictamente la cuenta corporativa custodia original en el portal de Apple para preservar el identificador de tópico y evitar re-inscripción masiva `[Verificado MS Learn]`.
  2. Renovar los tokens anuales de **Apple Business Manager (ADE)** y **Volume Purchase Program (VPP)** comprobando sincronización exitosa `[Verificado MS Learn]`.
  3. Realizar evaluación arquitectónica anual determinando qué brechas residuales (privilegios locales, CA cloud o catálogo Win32 curado) ameritan adoptar capacidades de `11_Microsoft_Intune_Suite` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Certificado APNs y tokens ABM/VPP renovados por 365 días en `Connectors and tokens` `[Verificado MS Learn]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01 — Playbook IR-01: Respuesta a Dispositivo Corporativo Comprometido (Malware / Ransomware)
- **Disparador:** Incidente o alerta `High` en Microsoft Defender XDR indicando ejecución de malware activo, robo de credenciales (LSASS/tokens) o actividad de ransomware en un endpoint inscrito en Intune `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Assets > Devices` + `https://intune.microsoft.com > Devices > All devices` + `https://entra.microsoft.com > Users` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 (contención inicial) -> SOC L2 / IR Team (investigación y remediación) -> Approver MAA (autorización de Wipe) `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Contención inmediata:** Aislar de red el dispositivo en MDE (`Isolate device`, manteniendo activo únicamente el canal hacia Defender; considerar que el aislamiento bloquea red pero no detiene cifrado local ya en curso) y ejecutar `Revoke sessions` del usuario en Entra ID `[Verificado MS Learn]`.
  2. **Precondición obligatoria en Intune:** Consultar estado de cumplimiento, última conexión y confirmar en `Encryption report` / Entra ID que la **BitLocker Recovery Key** (o FileVault key) esté efectivamente en custodia antes de cualquier acción irreversible `[Verificado MS Learn]`.
  3. **Preservación forense y alcance lateral:** Recolectar *Investigation package* y artefactos críticos vía **MDE Live Response**, auditar `IntuneAuditLogs` del host y buscar propagación lateral en Sentinel / Advanced Hunting `[Verificado MS Learn]`.
  4. **Erradicación o Full Wipe con MAA:** Si la amenaza fue contenida sin persistencia, ejecutar escaneo completo, verificar remediación total y liberar aislamiento. Si existe persistencia, ransomware o rootkit, solicitar `Wipe` en Intune, aprobarlo con un segundo administrador vía **Multi Admin Approval (MAA)**, completar la acción y re-aprovisionar limpio mediante Windows Autopilot `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete forense MDE, solicitud/aprobación MAA en `IntuneAuditLogs`, restablecimiento de credenciales/MFA y post-mortem en ITSM `[Verificado MS Learn]`.

### AH-02 — Playbook IR-02: Pérdida, Robo Físico o Desvinculación No Cooperativa de Dispositivo
- **Disparador:** Reporte de pérdida o robo por el usuario, alerta de acceso geográfico anómalo o baja laboral inmediata de riesgo notificada por RRHH `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > All devices > [Dispositivo]` y `https://entra.microsoft.com > Users` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2 + Approver MAA (para Full Wipe) + DPO (si no existía cifrado) `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Bloqueo inmediato reversible:** Ejecutar `Remote lock` (registrando PIN en cadena de custodia cuando aplique), activar `Locate device` si está soportado y habilitado (Windows 10/11 e iOS/iPadOS supervisado; no soportado en Android MDM) y revocar refresh tokens en Entra ID `[Verificado MS Learn]`.
  2. **Evaluación de exposición:** Comprobar en `Encryption report` si el disco estaba `Encrypted`. Si el dispositivo extraviado carecía de cifrado verificado y almacenaba datos personales o confidenciales, notificar de inmediato al DPO / Legal para evaluar brecha notificable `[Decisión / Propuesta Editorial]`.
  3. **Ejecución proporcional de borrado:**
     - **Equipos personales BYOD / Android Work Profile:** Ejecutar `Retire` o `App selective wipe` preservando información personal del propietario `[Verificado MS Learn]`.
     - **Equipos corporativos (Windows, macOS, iOS ADE, Android Fully Managed):** Ejecutar `Wipe` completo autorizado por **MAA**, monitorear `Device action status` hasta salir de `Pending`, revocar certificados SCEP/PKCS en la CA y eliminar el objeto huérfano en Entra ID `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro auditable de `Remote lock` / `Wipe` en `IntuneAuditLogs`, cadena de custodia CSV y baja de certificados/objeto Entra `[Verificado MS Learn]`.

### AH-03 — Playbook IR-03: Compromiso de Cuenta Administrativa o Alteración Masiva en Intune
- **Disparador:** Alerta de compromiso sobre un `Intune Administrator` / `Endpoint Security Manager` en Entra ID Protection, ráfaga de borrados o modificaciones no autorizadas en `IntuneAuditLogs`, o manipulación de políticas **MAA** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Identity > Users / PIM` + `https://intune.microsoft.com > Tenant administration > Audit logs` y `Multi Admin Approval` `[Verificado MS Learn]`.
- **Rol Responsable:** Incident Response Team + Identity Lead + Intune Platform Architect + CISO `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Contención del plano administrativo:** Revocar todas las sesiones, desactivar elevaciones activas en **Entra ID PIM** y deshabilitar temporalmente la cuenta de administrador o Service Principal comprometido (considerando la ventana residual de access tokens si una app no soporta CAE) `[Verificado MS Learn]`.
  2. **Auditoría forense de impacto:** Extraer en Microsoft Sentinel el historial íntegro de `IntuneAuditLogs` del actor durante los últimos 7 días, identificando cambios en *Compliance*, *Security Baselines*, *Scripts*, *Apps*, *Enrollment restrictions*, *Scope Tags*, *Roles* o exclusiones de **MAA** `[Verificado MS Learn]`.
  3. **Rechazo en MAA y reconstrucción desde código:** Rechazar/cancelar toda solicitud pendiente en `Multi Admin Approval > All requests`. Dado que Intune no ofrece *rollback* nativo automático, re-importar las políticas legítimas desde el respaldo JSON en Git mediante Microsoft Graph API y ejecutar sincronización masiva sobre los dispositivos afectados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Cronología forense exportada de `IntuneAuditLogs`, commits de restauración Graph aplicados y rotación completa de credenciales/MFA `[Verificado MS Learn]`.

### AH-04 — Despliegue Acelerado de Emergencia ante Vulnerabilidad Zero-Day / CISA KEV
- **Disparador:** Inclusión de una vulnerabilidad crítica de Windows, navegador o componente base en el catálogo **CISA KEV** o boletín de explotación activa Zero-Day `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Devices > Manage updates > Windows updates > Quality updates` + `Endpoint security > Attack surface reduction` `[Verificado MS Learn]`.
- **Rol Responsable:** Vulnerability Management Analyst + Endpoint Engineering + SOC Manager `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. Cuantificar la exposición exacta mediante *Security tasks* de MDVM o consulta KQL en `DeviceTvmSoftwareVulnerabilities` `[Verificado MS Learn]`.
  2. Desplegar política de **Expedited quality update** en Intune / Windows Autopatch anulando diferimientos estándar de anillos y fijando plazo estricto de reinicio cuando el parche requiera reinicio `[Verificado MS Learn]`.
  3. Activar simultáneamente controles compensatorios inmediatos (reglas ASR en `Block` o bloqueo en Firewall MDM) y elevar el nivel mínimo de parche requerido en *Device Compliance* tras vencer la ventana de emergencia `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de cambio de emergencia, reporte de convergencia Autopatch/Expedited a 72 horas y cierre de *Security task* `[Verificado MS Learn]`.

### AH-05 — Contención y Selective Wipe MAM en BYOD Móvil y Microsoft Edge for Business en Windows
- **Disparador:** Infección detectada en equipo personal no inscrito en MDM, alerta de salud de Windows Security Center / MTD sobre sesión MAM o finalización contractual de proveedor externo `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Apps > App selective wipe` y `Apps > Protection` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Application Security Administrator `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. Crear solicitud de **App selective wipe** para el usuario y dispositivo afectado, eliminando exclusivamente datos organizacionales, tokens y contenedores cifrados en iOS, Android y el perfil laboral de **Microsoft Edge for Business en Windows** `[Verificado MS Learn]`.
  2. Verificar que la política de *Health Checks (Conditional Launch)* junto con el conector de **Windows Security Center** bloquee re-ingresos mientras la amenaza local persista en el dispositivo personal `[Verificado MS Learn]`.
  3. Revocar sesiones en Entra ID forzando una nueva evaluación de *App Protection Conditional Access* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Confirmación `Deleted` en `App selective wipe` y evento registrado en `IntuneAuditLogs` `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL (Sentinel / Log Analytics / XDR) y Microsoft Graph PowerShell

#### Consulta 1 — Salud de Ingesta y Control de Ventanas Asimétricas en Tablas de Intune (KQL Sentinel / Log Analytics) `[Verificado MS Learn]`
```kql
// Distingue tablas transaccionales near-real-time (IntuneAuditLogs, IntuneOperationalLogs)
// de tablas de exportación diaria 24h-48h (IntuneDeviceComplianceOrg, IntuneDevices)
union IntuneAuditLogs, IntuneOperationalLogs, IntuneDeviceComplianceOrg, IntuneDevices
| where TimeGenerated > ago(72h)
| summarize LastEventUTC = max(TimeGenerated),
            HoursSinceLastIngestion = round(datetime_diff("minute", now(), max(TimeGenerated)) / 60.0, 2),
            TotalRecords72h = count()
            by TableName = Type
| extend ExpectedSLAPipeline = iff(TableName in ("IntuneAuditLogs", "IntuneOperationalLogs"), "< 1h (Lotes ~5m)", "24h - 48h (Snapshot Diario)")
| extend PipelineHealth = case(
    TableName in ("IntuneAuditLogs", "IntuneOperationalLogs") and HoursSinceLastIngestion > 2, "ALERTA: Retraso en tabla transaccional",
    TableName in ("IntuneDeviceComplianceOrg", "IntuneDevices") and HoursSinceLastIngestion > 48, "ALERTA: Snapshot diario fuera de ventana 48h",
    "OK"
)
| order by HoursSinceLastIngestion desc
```

#### Consulta 2 — Dispositivos Noncompliant con Sesiones Exitosas en Entra ID (Deduplicada) (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Aplica summarize arg_max() obligatorio para eliminar duplicados (hasta 100% en 24h) del export diario
let LatestNonCompliant = IntuneDeviceComplianceOrg
    | where TimeGenerated > ago(48h)
    | summarize arg_max(TimeGenerated, *) by DeviceId
    | where ComplianceState != "Compliant" and isnotempty(UPN);
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType == 0
| extend SignInDeviceId = tostring(DeviceDetail.deviceId)
| join kind=inner LatestNonCompliant on $left.SignInDeviceId == $right.DeviceId
| summarize SuccessfulSignIns = count(),
            TargetApps = make_set(AppDisplayName, 10),
            LastAccessUTC = max(TimeGenerated)
            by UPN, DeviceName, OS, ComplianceState, ConditionalAccessStatus
| order by LastAccessUTC desc
```

#### Consulta 3 — Dispositivos Corporativos "Compliant" Sin Cifrado Verificado (Brecha de Política) (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Detecta equipos corporativos marcados Compliant cuyo estado de cifrado reportado no es Encrypted
IntuneDevices
| where TimeGenerated > ago(48h)
| summarize arg_max(TimeGenerated, *) by DeviceId
| where Ownership == "Corporate" and CompliantState == "Compliant"
| where StorageTotal > 0
| where EncryptionState != "Encrypted" and EncryptionStatusString != "Encrypted"
| project SnapshotUTC = TimeGenerated, DeviceName, OS, OSVersion, UPN, CompliantState, EncryptionStatusString, LastContact
| order by LastContact desc
```

#### Consulta 4 — Auditoría de Wipes, Cambios en Políticas Críticas y Multi Admin Approval (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Monitorea operaciones remotas destructivas, cambios de seguridad/RBAC y flujo Multi Admin Approval
IntuneAuditLogs
| where TimeGenerated > ago(24h)
| where OperationName has_any ("Wipe", "Retire", "Delete", "CompliancePolicy", "SecurityBaseline", "DeviceSecurity", "Role", "AccessPolicy", "MultiAdminApproval")
| project TimeGenerated, OperationName, Category, ResultType, InitiatedBy = Identity, TargetResources, Properties
| order by TimeGenerated desc
```

#### Consulta 5 — Detección de Riesgo "Phantom Compliant" por Silencio Prolongado (> 10 Días) (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Identifica dispositivos que siguen figurando Compliant por Validity Period sin hacer check-in en >10 días
IntuneDevices
| where TimeGenerated > ago(48h)
| summarize arg_max(TimeGenerated, *) by DeviceId
| where CompliantState == "Compliant"
| extend LastContactUTC = todatetime(LastContact)
| extend DaysWithoutCheckIn = datetime_diff("day", now(), LastContactUTC)
| where DaysWithoutCheckIn > 10
| project DeviceName, UPN, OS, Ownership, CompliantState, LastContactUTC, DaysWithoutCheckIn
| order by DaysWithoutCheckIn desc
```

#### Consulta 6 — Correlación en Defender XDR: Endpoints con Alertas High y Telemetría ASR (KQL Advanced Hunting) `[Verificado MS Learn]`
```kql
// Cruza máquinas con alertas High en Defender XDR frente a bloqueos/auditorías ASR recientes
let HighAlertHosts = AlertInfo
    | where Timestamp > ago(72h) and Severity == "High"
    | join kind=inner (AlertEvidence | where EntityType == "Machine") on AlertId
    | distinct DeviceId, DeviceName, Title;
HighAlertHosts
| join kind=leftouter (
    DeviceEvents
    | where Timestamp > ago(7d) and ActionType startswith "Asr"
    | summarize AsrBlocks7d = countif(ActionType endswith "Blocked"),
                AsrAudits7d = countif(ActionType endswith "Audited") by DeviceId
) on DeviceId
| project DeviceName, HighAlertTitle = Title, AsrBlocks7d = coalesce(AsrBlocks7d, 0), AsrAudits7d = coalesce(AsrAudits7d, 0)
```

#### Consulta 7 — Extracción Automatizada App-Only de Dispositivos Noncompliant vía Microsoft Graph PowerShell `[Verificado MS Learn]`
```powershell
# Requiere App Registration con permiso Application: DeviceManagementManagedDevices.Read.All y certificado en almacén seguro
Connect-MgGraph -TenantId $env:TENANT_ID -ClientId $env:APP_ID -CertificateThumbprint $env:CERT_THUMBPRINT -NoWelcome

$devices = Get-MgDeviceManagementManagedDevice `
    -Filter "complianceState eq 'noncompliant'" `
    -Property "id,deviceName,userPrincipalName,operatingSystem,osVersion,lastSyncDateTime,isEncrypted,managedDeviceOwnerType" `
    -All

$devices | Select-Object DeviceName, UserPrincipalName, OperatingSystem, OSVersion, IsEncrypted, ManagedDeviceOwnerType, LastSyncDateTime,
    @{Name="DaysSinceLastSync"; Expression = { [math]::Round(((Get-Date).ToUniversalTime() - $_.LastSyncDateTime.ToUniversalTime()).TotalDays, 1) }} |
    Sort-Object DaysSinceLastSync |
    Export-Csv -Path ".\Intune_NonCompliant_Audit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation -Encoding UTF8
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*) `[Verificado MS Learn]`

| Componente / Control Verificado | Consola y Ruta Exacta | Criterio Objetivo de Operatividad (*Proof of Life*) |
|---|---|---|
| **Conector Defender for Endpoint** | `intune.microsoft.com > Endpoint security > Microsoft Defender for Endpoint` | `Connection status = Enabled`, última sincronización `< 24h` y evaluación de riesgo activa en políticas de cumplimiento. |
| **Cifrado y Custodia de Claves** | `intune.microsoft.com > Devices > Monitor > Encryption report` | Dispositivos corporativos en `Encrypted`, `TPM 2.0` y claves de recuperación visibles en Entra ID / Intune. |
| **Enforcement Real de Firewall MDM** | `intune.microsoft.com > Reports > Firewall > MDM Firewall status` | `Firewall status = Enabled` en los tres perfiles de red y `Target = MDM` (sin colisión involuntaria de GPO). |
| **Multi Admin Approval (MAA)** | `intune.microsoft.com > Tenant administration > Multi Admin Approval > Access policies` | Políticas activas cubriendo `Device actions`, `Scripts`, `Compliance policies`, `Configuration policies`, `Apps` y `RBAC`. |
| **Windows Autopatch + Hotpatch** | `intune.microsoft.com > Reports > Windows updates > Hotpatch quality update report` | Flota Windows 11 Enterprise 24H2/25H2 con VBS en ejecución recibiendo parches mensuales sin reinicio en meses hotpatch. |
| **MAM en Móviles y Edge Windows** | `intune.microsoft.com > Apps > Monitor > App protection status` | Usuarios BYOD sincronizando estado de salud de aplicación y conector *Windows Security Center* operativo. |
| **Exportación SIEM (4 Tablas)** | `intune.microsoft.com > Reports > Diagnostics settings` + Consulta KQL 1 | Las 4 categorías marcadas y eventos fluyendo dentro de las ventanas documentadas (`< 1h` y `24h–48h`). |

### 10.3 Guía Rápida de Verificación Local en Endpoint (Registry y Event Viewer) `[Verificado MS Learn]`

Cuando exista discrepancia entre el reporte de consola en Intune y el comportamiento observado en un equipo Windows 11, el analista de Nivel 2 valida tres fuentes locales autoritativas `[Verificado MS Learn]`:
- **Reglas de Firewall MDM en Registro:** `HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\Mdm\FirewallRules` (las reglas desplegadas vía CSP MDM no siempre aparecen en el complemento clásico `wf.msc`) `[Verificado MS Learn]`.
- **Eventos de Reglas ASR:** Visor de eventos en `Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational`, filtrando Event IDs `1121` (acción bloqueada), `1122` (acción auditada) y `1129` `[Verificado MS Learn]`.
- **Elegibilidad Local de Hotpatch:** Visor de eventos filtrando `AllowRebootlessUpdates` (`1` = inscrito en política hotpatch con `vbsState: 2`) y verificación de `Virtualization-based security = Running` en `msinfo32` `[Verificado MS Learn]`.

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operativos y Ejecutivos `[Decisión / Propuesta Editorial]`

> **Aclaración de gobierno:** Microsoft suministra la telemetría y los reportes nativos, pero **no prescribe umbrales porcentuales ni SLAs universales obligatorios**. Los siguientes ocho KPIs constituyen metas consultivas recomendadas para formalizar acuerdos internos de nivel de servicio entre Ciberseguridad / SOC y Microinformática `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Medición | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Dispositivos Noncompliant con Sesión Activa** | `Count(Dispositivos Noncompliant fuera de Grace Period con SignIn exitoso en Entra ID en 24h)` | `0 dispositivos` | Diaria | SOC Manager / Identity Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cobertura Efectiva de Sensor EDR en Flota Gestionada** | `(Dispositivos inscritos en Intune con sensor MDE activo / Total dispositivos corporativos elegibles en Intune) * 100` | `>= 98 %` | Diaria | SOC Manager / Endpoint Security | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Cifrado de Disco Verificado con Recovery Key en Custodia** | `(Equipos corporativos Windows/macOS Encrypted + Recovery Key custodiada / Total equipos corporativos) * 100` | `>= 99 %` *(resto con excepción vigente <= 90d)* | Semanal / Mensual | CISO / Auditoría Interna | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Adherencia Limpia a Security Baselines (Sin Conflictos CSP)** | `(Dispositivos sin estados Error ni Conflict en perfiles Security Baselines / Total dispositivos asignados) * 100` | `>= 95 %` y `0 conflictos` > 7 días | Semanal | Endpoint Security Engineer | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Velocidad de Cierre de Security Tasks Críticas y CISA KEV** | `(Security Tasks MDVM->Intune Críticas o CISA KEV remediadas en <= 7 días / Total generadas) * 100` | `>= 95 %` *(100% KEV con acción en <= 48h)* | Semanal | Vulnerability Mgmt / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Elegibilidad y Adopción de Hotpatch (Win 11 24H2+)** | `(Equipos Windows 11 Enterprise aplicando Hotpatch sin reinicio / Total flota Windows 11 Enterprise) * 100` | `>= 85 %` | Mensual | Endpoint Engineering / CIO | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Trazabilidad de Doble Control (MAA + Ticket ITSM)** | `(Acciones Wipe/Retire y cambios críticos con aprobación MAA + ticket ITSM / Total operaciones auditadas) * 100` | `100 %` (`0 cambios huérfanos`) | Diaria / Semanal | CISO / GRC & Auditores | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Índice de Higiene de Inventario (*Anti-Phantom Compliant*)** | `(Dispositivos con Last check-in > umbral limpieza o asignados a bajas de RRHH / Total inventario Intune) * 100` | `< 3 %` inactivos y `0` en bajas > 48h | Semanal | Intune Admin / Identity | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio de Madurez | Descripción de Capacidades y Disciplina Operativa |
|---|---|---|
| **Nivel 1** | **Inicial / Ad-Hoc** | Inscripción parcial, coexistencia desordenada de GPOs y perfiles heredados con conflictos frecuentes, uso habitual de *Global Administrator*, sin integración con Defender for Endpoint ni envío de registros a SIEM. |
| **Nivel 2** | **Repetible Básico** | Políticas elementales de *Device Compliance* enlazadas a Acceso Condicional para un subconjunto de apps; cifrado evaluado solo por estado `Succeeded` del perfil; sin protección MAM en BYOD ni controles *Multi Admin Approval*. |
| **Nivel 3** | **Definido e Integrado** | Uso estandarizado de *Settings Catalog* y *Security Baselines* GA, bucle cerrado activo con nivel de riesgo de MDE, roles RBAC mínimos con Entra ID PIM y *Scope Tags*, reglas de limpieza y exportación de las 4 tablas hacia Sentinel con deduplicación KQL. |
| **Nivel 4** | **Gestionado Cuantitativamente** | **Multi Admin Approval (MAA)** obligatorio en acciones destructivas, scripts, políticas y RBAC; MAM activo en móviles y *Edge for Business* en Windows; cadencias diarias/semanales/mensuales auditadas por KPIs y playbooks `IR-01` a `IR-03` ejercitados. |
| **Nivel 5** | **Optimizado y Resiliente** | Cobertura superior al 85% de **Hotpatch updates** sin reinicio en Windows 11 24H2+, **Apple DDM** y **Android Enterprise/AOSP** modernos al 100%, respaldo trimestral automatizado como código en Git vía Graph API, CAE casi en tiempo real y revisión asistida por *Change Review Agent*. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota metodológica:** El mapeo a las **seis funciones oficiales de NIST CSF 2.0 (CSWP 29)** constituye una estructura probatoria consultiva para auditorías internas y regulatorias basada en controles técnicos verificables de Intune Plan 1 `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría | Resultado de Seguridad (CSWP 29) | Capacidad Habilitadora en Microsoft Intune Plan 1 (+ E5) | Táctica / Técnica MITRE ATT&CK | Evidencia Auditable Reproducible | Etiqueta |
|---|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OC-03` | Requisitos legales, regulatorios y de privacidad sobre datos y dispositivos gestionados e integrados. | Políticas **App Protection (MAM)** y *App selective wipe* en iOS, Android y Edge for Business que segregan datos corporativos sin tomar control MDM del dispositivo personal. | Collection (`TA0009`) | Configuraciones exportadas de `Apps > Protection` y logs de *App selective wipe*. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Roles, responsabilidades y autoridades de seguridad establecidos y reforzados técnicamente. | Roles RBAC personalizados en Intune, partición por *Scope Tags*, activación JIT en *Entra ID PIM* y políticas de doble aprobación **Multi Admin Approval (MAA)**. | Valid Accounts (`T1078`) / Account Manipulation (`T1098`) | Capturas de *Access policies* MAA, asignaciones PIM y actas de *Access Reviews* (`T-02`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-01` | Inventarios precisos de hardware y endpoints administrados mantenidos continuamente. | Inventario central `All devices`, distinción `Corporate`/`Personal`, *Device cleanup rules* y exportación diaria a `IntuneDevices` conciliada con Entra ID. | Hardware Additions / Rogue Assets (`TA0001`) | Consulta KQL deduplicada sobre `IntuneDevices` y reporte semanal `S-06`. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` | Vulnerabilidades en endpoints identificadas, validadas y registradas para mitigación. | Flujo nativo de **Security Tasks** desde Defender Vulnerability Management hacia Intune y políticas de versión mínima de sistema operativo. | Exploitation for Client Execution (`T1203`) | Registro de `Endpoint security > Security tasks` cerradas en SLA (`S-03`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Derechos de acceso y autorizaciones regidos por postura verificada y mínimo privilegio. | Evaluación continua de *Device Compliance* (con riesgo MDE) y *App Protection* exigida por **Microsoft Entra Conditional Access** y **CAE**. | Initial Access (`TA0001`) / Lateral Movement (`TA0008`) | Consulta KQL 2 demostrando `0` inicios de sesión exitosos desde equipos no conformes. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-01` | Prácticas de gestión de configuración de seguridad establecidas y mantenidas. | **Settings Catalog**, **Security Baselines** vigentes (Windows v26H2, Office v2512, Edge v139, MDE v24H1) y **Apple DDM**. | Defense Evasion (`TA0005`) | Reportes *Per-setting status* sin conflictos y respaldo trimestral JSON en Git (`T-02`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-02` | Software mantenido, actualizado y reemplazado conforme al riesgo de exposición. | **Windows Autopatch**, **Hotpatch updates** sin reinicio (Win 11 24H2+) y despliegues acelerados *Expedited updates* ante **CISA KEV**. | Exploitation for Privilege Escalation (`T1068`) | *Hotpatch quality update report* (`M-05`) y actas trimestrales de *Baseline updates* (`T-01`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` | Confidencialidad e integridad de datos en reposo protegidas criptográficamente. | Perfiles `Endpoint security > Disk encryption` (BitLocker TPM 2.0 y FileVault) con custodia verificada (*Key escrow*) en Entra ID / Intune. | Data from Local System (`T1005`) | Exportación mensual de `Devices > Monitor > Encryption report` (`M-01`). | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-01` | Redes y flujos de administración monitoreados para detectar actividad no autorizada. | Supervisión de *MDM Firewall status*, eventos de reglas **ASR** y correlación en Sentinel de cambios críticos en `IntuneAuditLogs`. | Command and Control (`TA0011`) / Execution (`TA0002`) | Consulta KQL 4 y reglas analíticas activas en Microsoft Sentinel sobre `IntuneAuditLogs`. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-09` | Hardware y software de cómputo monitoreados frente a anomalías e inactivación de sensores. | Onboarding automatizado del sensor EDR de **Defender for Endpoint** y evaluación de salud de **Windows Security Center** en MAM. | Impair Defenses (`T1562`) | Estado `Enabled` del conector MDE (`D-02`) y reporte `Antivirus agent status`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Incidentes contenidos rápidamente para impedir propagación o exfiltración. | Ejecución coordinada de `IR-01` e `IR-02`: aislamiento MDE + revocación de sesiones + `Remote lock`, `Retire`, `App selective wipe` y `Full Wipe` bajo **MAA**. | Lateral Movement (`TA0008`) / Exfiltration (`TA0010`) | Trazas en `IntuneAuditLogs`, aprobaciones MAA y bitácora firmada de cadena de custodia. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-02` | Acciones de recuperación validadas y ejecutadas para restaurar la operación confiable. | Playbook `IR-03` (re-importación declarativa de políticas desde Git vía Graph API tras abuso administrativo) y re-aprovisionamiento limpio vía **Windows Autopilot**. | System Wipe / Defacement (`T1485`) | Evidencia del simulacro semestral `SM-01` y verificación post-inscripción Autopilot. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

### 13.1 Matriz Curricular por Rol Operativo

| Rol Operativo | Certificaciones y Rutas Oficiales Microsoft Learn (Vigentes Nov-2026) | Recursos Técnicos Complementarios (Blogs Ingeniería, GitHub y Comunidad MVP) | Práctica Obligatoria en Entorno de Prueba |
|---|---|---|---|
| **SOC L1 / SOC L2** | Ruta oficial *Protect endpoints with Microsoft Intune* y certificación **SC-200** (*Security Operations Analyst Associate*) `[Verificado MS Learn]`. | Playbooks oficiales de respuesta a incidentes de Microsoft (`learn.microsoft.com/security/operations/incident-response-playbooks`) `[Verificado MS Learn]`. | Correlación KQL `Noncompliant` + `SigninLogs`, validación previa de Recovery Key y ejecución de `IR-01` / `IR-02`. |
| **Endpoint Security Engineer** | Certificación **MD-102** (*Microsoft 365 Certified: Endpoint Administrator Associate*) + módulos de *Security Baselines*, *ASR* y *Windows Autopatch Hotpatch* `[Verificado MS Learn]`. | Blog oficial *Microsoft Intune Customer Success* (Tech Community) y proyecto comunitario MVP *OpenIntuneBaseline* como referencia de arquitectura `[Verificado MS Learn]`. | Resolución de conflictos CSP en *Settings Catalog*, promoción de reglas ASR a `Block` y despliegue de *Hotpatch* con VBS activo. |
| **Intune Platform Administrator** | Certificaciones **MD-102** y **MS-102** (*Microsoft 365 Certified: Administrator Expert*) + guías de *Multi Admin Approval*, *Apple DDM* y *Android AOSP* `[Verificado MS Learn]`. | Repositorio oficial **Microsoft Graph PowerShell Intune Samples** (`github.com/microsoft/mggraph-intune-samples`) y exportación declarativa con *Microsoft365DSC* `[Verificado MS Learn]`. | Configuración de políticas MAA evitando interbloqueo en `Role`, scripts App-Only con certificado en Key Vault y respaldo JSON. |
| **Identity Architect & GRC Auditor** | Certificación **SC-300** (*Identity and Access Administrator Associate*) — *Device Compliance* y *App Protection Conditional Access* + CAE `[Verificado MS Learn]`. | Publicación oficial **NIST CSF 2.0 (CSWP 29)** y referencia de tablas Azure Monitor (`IntuneAuditLogs`, `IntuneDevices`) `[Verificado MS Learn]`. | Validación de Acceso Condicional en BYOD con Edge for Business y auditoría trimestral de evidencias KQL deduplicadas. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Incorporadas tras Revalidación en Microsoft Learn MCP (`2026-11-11`)

| # | Estado en Material Base (`MSEOP-MD`) | Hallazgo Verificado en Microsoft Learn al `2026-11-11` | Corrección Aplicada en la Guía Definitiva v2.0 |
|---|---|---|---|
| **1** | Se exigía un KPI uniforme de latencia `< 15 minutos` para las cuatro tablas de Intune en Sentinel. | Solo `IntuneAuditLogs` e `IntuneOperationalLogs` se envían de inmediato en lotes de ~5 minutos; `IntuneDeviceComplianceOrg` e `IntuneDevices` se exportan **una vez cada 24h (ventana de hasta 48h)** y el pipeline puede **duplicar hasta el 100% de registros** en 24h `[Verificado MS Learn]`. | Se corrigió la cadencia mensual `M-06`, la Consulta KQL 1 y se añadió `summarize arg_max(TimeGenerated, *) by DeviceId` en todas las consultas sobre tablas diarias. |
| **2** | Los playbooks `IR-01` a `IR-03` dependían solo de autorización procedimental en ticket antes de un `Wipe` o cambio RBAC. | **Multi Admin Approval (MAA)** impone doble aprobación técnica nativa sobre *Apps*, *Compliance*, *Settings Catalog*, *Device actions* (`Wipe`, `Retire`, `Delete`), *RBAC*, *Scripts* (con *Change Review Agent*) y *Tenant Configuration*, incluyendo llamadas app-auth en Graph API `[Verificado MS Learn]`. | Se integró MAA en arquitectura, matriz RBAC (incluyendo la regla oficial anti-deadlock para políticas `Role` y requisitos del grupo aprobador), `D-03` y playbooks `AH-01` a `AH-03`. |
| **3** | Parcheo descrito únicamente con *Update rings* clásicos y sin reflejar fin de soporte de Windows 10 ni parches sin reinicio. | **Windows Autopatch** unificó el despliegue de actualizaciones (abril 2025), incorporó **Hotpatch updates** sin reinicio en Windows 11 24H2+ (requiriendo VBS y desactivar CHPE en Arm64; EOS de Office 32-bit en Arm en dic-2026), mientras **Windows 10 alcanzó fin de soporte el 14-oct-2025** `[Verificado MS Learn]`. | Se incorporaron controles operativos de Autopatch y Hotpatching en `D-07`, `M-05`, `T-01` y `KPI-06`, además del control sobre Windows 10 como *allowed version*. |
| **4** | Gestión móvil sin reflejar la deprecación de actualizaciones MDM en Apple ni la evolución post Device Administrator en Android. | Intune finalizó soporte de **Android Device Administrator** en GMS en diciembre de 2024 (consolidando Android Enterprise 10+ y **AOSP**, con *referenced apps* desde la release `2610` de oct-2026), y **Apple OS 26** deprecó actualizaciones MDM clásicas exigiendo **Apple DDM** en *Settings Catalog* `[Verificado MS Learn]`. | Se actualizaron estándares móviles en Sección 3.2 y validación trimestral en `T-01`. |
| **5** | Cobertura MAM enfocada solo en iOS/Android, sin abordar estaciones Windows personales BYOD. | **Data Protection for Windows MAM** con **Microsoft Edge for Business**, *App Protection Conditional Access* y el conector MTD de **Windows Security Center** (Windows 11 23H2+) están disponibles en GA `[Verificado MS Learn]`. | Se incorporó Windows MAM con Edge for Business en arquitectura, monitoreo diario `D-07`, revisión trimestral `T-02` y playbook `AH-05`. |
| **6** | Referencias genéricas a *Security Baselines* y asunción de equivalencia directa con cumplimiento CIS/NIST. | Existen instancias específicas vigentes Windows **v26H2/25H2/24H2**, M365 Apps **v2512** (jun-2026), Edge **v139** (abr-2026) y MDE **v24H1** (no recomendada en VDI/VMs); además, Microsoft aclara oficialmente que **no constituyen mapeo 1:1 ni certificación CIS/NIST automática** `[Verificado MS Learn]`. | Se documentaron las versiones exactas a nov-2026, la advertencia sobre VDI/VMs y la precisión normativa en Sección 3.1 y `M-03`. |
| **7** | Límites difusos entre capacidades incluidas en M365 E3/E5 y capacidades avanzadas comercializadas aparte. | Microsoft divide formalmente **Intune Plan 1** (incluido en M365 E3/E5), **Intune Plan 2** y **Microsoft Intune Suite**, además de reglas específicas para licencias *Device-only* y *Unlicensed admin access* (tope de 1.000 admins por grupo directo) `[Verificado MS Learn]`. | Se delimitó con exactitud el alcance en Sección 2.2 articulando la conexión con los Módulos `11` y `12`. |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas `[Decisión / Propuesta Editorial]`

| # | Elemento Consultivo / Diseño Editorial | Justificación Arquitectónica y de Gobierno |
|---|---|---|
| **1** | **Metas numéricas en `KPI-01` a `KPI-08` y SLAs internos (<= 7 días para tareas críticas / KEV)** | Microsoft no establece metas cuantitativas universales; definir umbrales medibles habilita contratos internos de nivel de servicio entre el CISO y Operaciones de TI. |
| **2** | **Clasificación de incumplimientos en Categoría A (seguridad crítica) vs. Categoría B (administrativa) y control de *Phantom Compliant* (> 10 días)** | Evita que el SOC trate con idéntica urgencia un equipo con BitLocker desactivado y sesión activa frente a una demora menor de versión móvil, y visibiliza equipos silenciosos cubiertos por el *Validity Period*. |
| **3** | **Matriz RACI entre Ciberseguridad / SOC, Microinformática e Identidad** | Elimina zonas grises de responsabilidad sobre consolas compartidas, otorgando *Accountability* de postura y respuesta a Ciberseguridad y de ciclo de vida/soporte a Microinformática. |
| **4** | **Ventanas JIT en Entra ID PIM (2h Intune Admin / 4h Endpoint Security Manager) y respaldo trimestral JSON en Git vía Graph API** | Reduce drásticamente la ventana de exposición de sesiones privilegiadas y compensa la ausencia de función nativa de *rollback* masivo en Intune frente a incidentes `IR-03`. |
| **5** | **Mapeo de auditoría a 12 subcategorías de NIST CSF 2.0 y modelo de madurez de 5 niveles** | Estructura evidencia técnica reproducible en un marco aceptado por auditoría interna, reguladores y comités ejecutivos de riesgo. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn (`[Verificado MS Learn]`)
- **REF-01:** *Microsoft Intune licensing (Plan 1, Plan 2, Intune Suite, Device-only & Unlicensed Admins)* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/licenses`
- **REF-02:** *Microsoft Intune advanced capabilities (Plan 2 and Intune Suite)* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/advanced-capabilities`
- **REF-03:** *Operating systems and browsers supported by Microsoft Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/supported-devices-browsers`
- **REF-04:** *What's new in Microsoft Intune (Service release 2610 — October 2026)* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/whats-new`
- **REF-05:** *Use compliance policies to set rules for devices you manage with Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/protect/device-compliance-get-started`
- **REF-06:** *Use the Intune settings catalog to configure settings* — `https://learn.microsoft.com/en-us/intune/intune-service/configuration/settings-catalog`
- **REF-07:** *Use security baselines to help secure Windows devices (v26H2, v25H2, Office v2512, Edge v139, MDE v24H1)* — `https://learn.microsoft.com/en-us/intune/intune-service/protect/security-baselines`
- **REF-08:** *Configure Microsoft Defender for Endpoint in Microsoft Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/protect/mde-security-integration`
- **REF-09:** *Use access policies to require Multi Admin Approval in Microsoft Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/multi-admin-approval`
- **REF-10:** *Role-based access control (RBAC) and Scope Tags with Microsoft Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/role-based-access-control`
- **REF-11:** *What is Windows Autopatch?* — `https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-overview`
- **REF-12:** *Hotpatch updates in Windows Autopatch (Windows 11 Enterprise 24H2/25H2)* — `https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/manage/windows-autopatch-hotpatch-updates`
- **REF-13:** *Data Protection for Windows MAM (Microsoft Edge for Business & Windows Security Center MTD)* — `https://learn.microsoft.com/en-us/intune/intune-service/apps/protect-mam-windows`
- **REF-14:** *Send Intune log data to Azure Storage, Event Hubs, or Log Analytics* — `https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/review-logs-using-azure-monitor`
- **REF-15:** *Retire or wipe devices using Microsoft Intune* — `https://learn.microsoft.com/en-us/intune/intune-service/remote-actions/devices-wipe`

### 15.2 Blogs Oficiales de Ingeniería Microsoft, Repositorios y Marcos Normativos
- **REF-16:** *Support tip: Move to Declarative Device Management (DDM) for Apple software updates* — Benjamin Flamm, Microsoft Intune Customer Success Blog (`https://techcommunity.microsoft.com/blog/intunecustomersuccess/support-tip-move-to-declarative-device-management-for-apple-software-updates/4432177`)
- **REF-17:** *Hotpatch efficiency unlocked: Smaller update size* — Windows IT Pro Blog, Microsoft Tech Community (`https://techcommunity.microsoft.com/blog/windows-itpro-blog/hotpatch-efficiency-unlocked-smaller-update-size/4460681`)
- **REF-18:** *Microsoft Graph PowerShell Intune Samples (Official GitHub Repository)* — Microsoft (`https://github.com/microsoft/mggraph-intune-samples`)
- **REF-19:** *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* — National Institute of Standards and Technology (`https://doi.org/10.6028/NIST.CSWP.29`)

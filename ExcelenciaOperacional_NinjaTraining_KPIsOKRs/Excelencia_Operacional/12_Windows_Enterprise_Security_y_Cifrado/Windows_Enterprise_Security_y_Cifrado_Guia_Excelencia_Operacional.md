# Guía Maestra de Excelencia Operacional: Windows Enterprise Security y Cifrado (Windows 11 Enterprise E3/E5 en Microsoft 365 E5)

## 1. Portada y Ficha de Control Documental

| Campo Documental | Detalle Oficial Consolidado |
| :--- | :--- |
| **Identificador del Módulo** | `12_Windows_Enterprise_Security_y_Cifrado` |
| **Slug Canónico** | `Windows_Enterprise_Security_y_Cifrado` |
| **Nombre Completo** | Windows Enterprise Security y Cifrado (Endurecimiento de Silicio, Criptografía, Identidad Local y Control de Ejecución en Windows 11 Enterprise) |
| **Categoría Maestra** | Endpoints, Dispositivos y Plataforma Windows |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 (Windows 11 Enterprise E5) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://intune.microsoft.com`, `https://entra.microsoft.com`, `https://security.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Windows Platform Architect, Endpoint Security Engineer, SOC L1/L2/L3, Identity Engineer, Help Desk Lead, GRC / Internal Audit `[Decisión / Propuesta Editorial]` |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), MITRE ATT&CK Enterprise v18, Microsoft Windows 11 Security Baselines (24H2 / 25H2 / 26H2), Estándar Secured-core PC `[Verificado MS Learn]` |

> **Nota de Consolidación y Alcance Operacional (Corte 11 de noviembre de 2026):** Esta guía establece el modelo de excelencia operacional para los controles nativos de seguridad de plataforma, cifrado multicapa, raíz de confianza en silicio, aislamiento por virtualización, protección de credenciales/cuentas locales y control de aplicaciones integrados en **Windows 11 Enterprise E3/E5** (versiones soportadas **24H2, 25H2 y 26H2**, tras el fin de soporte definitivo de Windows 10 el **14 de octubre de 2025**) `[Verificado MS Learn]`. Aborda con profundidad operativa cuatro dominios críticos gobernados desde Microsoft Intune y Microsoft Entra ID y telemetrizados en Microsoft Defender XDR / Microsoft Sentinel: (1) **BitLocker Drive Encryption** y **Personal Data Encryption (PDE)**; (2) **Secured-core PC**, **TPM 2.0**, **Pluton**, **VBS/HVCI** y la transición obligatoria 2025–2026 de certificados **UEFI Secure Boot (2011 hacia Windows UEFI CA 2023)**; (3) **Credential Guard**, **LSA Protection (`RunAsPPL`)**, **Windows LAPS** con *Automatic Account Management* y **Windows Hello for Business (Cloud Kerberos Trust & Passwordless Experience)**; y (4) **App Control for Business** (sucesor oficial de WDAC), **Smart App Control**, **Administrator Protection** y **Windows Firewall with Advanced Security** `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026

En una arquitectura **Zero Trust**, ningún agente EDR ni control de identidad en nube es suficiente si el firmware UEFI, el gestor de arranque, el kernel del sistema operativo, el subsistema LSASS o el disco físico del endpoint pueden ser subvertidos por debajo de la capa de visibilidad del agente. La evolución de amenazas entre 2023 y 2026 —marcada por *bootkits* UEFI como BlackLotus (`CVE-2023-24932`), ataques *Bring Your Own Vulnerable Driver (BYOVD)* para deshabilitar sensores EDR desde el kernel, robo de tokens de sesión y explotación silenciosa de sesiones con privilegios administrativos— llevó a Microsoft a rediseñar profundamente la seguridad nativa de **Windows 11 Enterprise** `[Verificado MS Learn]`.

A corte **11 de noviembre de 2026**, el panorama operativo de seguridad Windows está definido por cinco transformaciones estructurales verificadas:

1. **Fin de soporte de Windows 10 (14 de octubre de 2025) y consolidación en Windows 11 24H2 / 25H2 / 26H2:** Con Windows 10 fuera de soporte estándar, **Windows 11 Enterprise** constituye la plataforma obligatoria para recibir innovaciones arquitectónicas como *Windows LAPS Automatic Account Management*, *Personal Data Encryption (PDE) for Known Folders*, ampliación de auto-cifrado BitLocker en OOBE/Autopilot (eliminando las antiguas barreras de Modern Standby/HSTI y DMA en 24H2+) y las herramientas de la *Windows Resiliency Initiative* (**Quick Machine Recovery [QMR]**, *Point-in-time restore*, *Cloud rebuild* y *Post-quantum security APIs*) añadidas a Windows Enterprise E3/E5 `[Verificado MS Learn]`.
2. **Transición crítica de certificados UEFI Secure Boot (Expiración Junio 2026 -> `Windows UEFI CA 2023`):** Los certificados fundacionales de Secure Boot emitidos en 2011 (`Microsoft Corporation UEFI CA 2011`, `Microsoft Windows Production PCA 2011` y `Microsoft Corporation KEK CA 2011`) iniciaron su vencimiento en **junio de 2026** `[Verificado MS Learn]`. La migración controlada de toda la flota hacia la jerarquía **2023** (`Windows UEFI CA 2023`, `Microsoft UEFI CA 2023`, `Microsoft Corporation KEK 2K CA 2023` y gestor de arranque firmado 2023) es una prioridad operativa ineludible para conservar protección pre-OS frente a nuevos *bootkits* y evitar fallos de arranque o bucles de recuperación BitLocker `[Verificado MS Learn]`.
3. **Defensa activa por defecto en silicio y memoria:** En equipos modernos y **Secured-core PC**, **Virtualization-Based Security (VBS)**, **HVCI (Memory Integrity)**, **Credential Guard** y **LSA Protection (`RunAsPPL`)** vienen habilitados por defecto en Windows 11 Enterprise, complementados por **Kernel-mode Hardware-enforced Stack Protection** (pilas sombra en hardware CET/PAC) y el procesador de seguridad **Microsoft Pluton** integrado en el SoC `[Verificado MS Learn]`.
4. **Cifrado en doble capa (Volumen + Archivo vinculado a identidad):** **BitLocker** protege el volumen en reposo frente al robo físico con el equipo apagado, mientras que **Personal Data Encryption (PDE)** en Windows 11 22H2+/24H2 cifra archivos individuales y carpetas conocidas (`Desktop`, `Documents`, `Pictures`) vinculando las claves criptográficas al inicio de sesión con **Windows Hello for Business** y descartándolas al cerrar sesión `[Verificado MS Learn]`.
5. **Reemplazo de WDAC por *App Control for Business* y llegada de *Administrator Protection*:** Microsoft unificó el control de integridad de código bajo la marca oficial **App Control for Business**, e introdujo **Administrator Protection** (disponible vía `KB5120998` y activado por defecto en las *Windows Security Baselines* de octubre de 2026 para Windows 11 24H2/25H2/26H2), que emite tokens administrativos aislados Just-In-Time desde un perfil oculto generado por el sistema previa autenticación Windows Hello `[Verificado MS Learn]`.

### 2.2 Matriz Detallada de Licenciamiento y Capacidades en Microsoft 365 E5

| Licencia / Suscripción | Derechos y Capacidades de Seguridad Windows Incluidos | Rol de Gestión y Monitoreo Asociado |
| :--- | :--- | :--- |
| **Windows 11 Enterprise E3** *(Incluido en Microsoft 365 E3, E5 y E7)* | BitLocker y BitLocker To Go gestionados, Credential Guard y Remote Credential Guard, App Control for Business, Personal Data Encryption (PDE), Windows LAPS, Windows Hello for Business, Administrator Protection, System Guard, Quick Machine Recovery (QMR), Cloud rebuild, Point-in-time restore, Post-quantum APIs y Windows Autopatch (incluyendo *Secure Boot status report*) `[Verificado MS Learn]`. | Políticas desplegadas desde **Microsoft Intune Plan 1** y claves escrowed en **Microsoft Entra ID** `[Verificado MS Learn]`. |
| **Windows 11 Enterprise E5** *(Incluido en Microsoft 365 E5 y Microsoft 365 E7)* | Todo lo incluido en Windows 11 Enterprise E3 **más** integración nativa completa con **Microsoft Defender for Endpoint Plan 2** (telemetría kernel XDR, Advanced Hunting a 30 días, Live Response, evaluación continua de postura **Defender Vulnerability Management** sobre BIOS/Secure Boot/VBS/BitLocker/LAPS y detección de exploits en memoria) `[Verificado MS Learn]`. | Caza de amenazas, incidentes unificados y postura de hardware en `https://security.microsoft.com` `[Verificado MS Learn]`. |
| **Microsoft Entra ID P1 / P2** *(Incluido en M365 E3 / E5)* | Almacenamiento cifrado y rotación de claves BitLocker y contraseñas Windows LAPS en objetos de dispositivo Entra, **Cloud Kerberos Trust** para WHfB, Temporary Access Pass (TAP) para *Web Sign-in*, Acceso Condicional basado en `DeviceCompliance` y `AuditLogs` `[Verificado MS Learn]`. | Gobierno de identidad de dispositivo, RBAC personalizado y PIM en `https://entra.microsoft.com` `[Verificado MS Learn]`. |
| **Microsoft Intune Plan 1** *(Incluido en M365 E3 / E5)* | Nodos de **Endpoint security** (*Disk encryption* para BitLocker y PDE, *Account protection* para WHfB y Windows LAPS, *App Control for Business*, *Firewall*, *Security baselines*) y evaluación criptográfica `DeviceHealthAttestation` `[Verificado MS Learn]`. | Orquestación declarativa MDM/CSP en `https://intune.microsoft.com` `[Verificado MS Learn]`. |

### 2.3 Principios Rectores Oficiales y Alineación Zero Trust

1. **Raíz de confianza verificable desde el silicio hasta la nube:** Exigir hardware **TPM 2.0**, **UEFI Secure Boot** actualizado a certificados **2023**, **System Guard Secure Launch** y atestación de salud antes de conceder acceso mediante Acceso Condicional `[Verificado MS Learn]`.
2. **Defensa criptográfica en profundidad (Volumen + Carpeta de Usuario + Portátiles Extraíbles):** Combinar **BitLocker XTS-AES 256** silencioso o con PIN pre-arranque y **BitLocker To Go** con **Personal Data Encryption (PDE)** enlazado a Windows Hello for Business `[Verificado MS Learn]`.
3. **Custodia de secretos de recuperación bajo privilegio mínimo estricto:** Escrowed obligatorio de claves BitLocker y contraseñas Windows LAPS en Microsoft Entra ID antes de activar la protección, bloqueando la auto-lectura por usuarios estándar cuando el modelo de amenaza lo exija y auditando cada consulta en `AuditLogs` `[Verificado MS Learn]`.
4. **Aislamiento por virtualización innegociable para credenciales e integridad de kernel:** Imponer **VBS**, **HVCI**, **Kernel-mode Hardware-enforced Stack Protection**, **Credential Guard** y **LSA Protection (`RunAsPPL`)** sin desactivaciones permanentes por drivers obsoletos `[Verificado MS Learn]`.
5. **Autenticación sin contraseñas y cuentas locales efímeras:** Desplegar **Windows Hello for Business** con *Cloud Kerberos Trust* y *Passwordless experience*, gobernando cuentas de emergencia locales exclusivamente mediante **Windows LAPS** con rotación automática post-autenticación `[Verificado MS Learn]`.
6. **Confianza explícita en ejecución binaria y elevación administrativa:** Reemplazar listas negras reactivas por políticas de **App Control for Business** (incluyendo bloqueo de drivers vulnerables) y tokens efímeros aislados mediante **Administrator Protection** o EPM `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional y Componentes de Plataforma Windows 11 Enterprise

| Componente / Motor Nativo | Función Operativa Principal | Consola y Ruta de Gobierno (`intune.microsoft.com` / `entra.microsoft.com`) | Integraciones y Telemetría Clave |
| :--- | :--- | :--- | :--- |
| **1. BitLocker Drive Encryption & BitLocker To Go** | Cifrado de volúmenes de sistema operativo, unidades fijas y extraíbles mediante **XTS-AES 128/256 bits**, protectores TPM 2.0 o TPM + PIN, habilitación silenciosa para usuarios estándar y rotación automática de contraseñas de recuperación `[Verificado MS Learn]`. | `Intune > Endpoint security > Disk encryption > BitLocker` y `Devices > Monitor > Encryption report` | `BitLocker CSP`, Microsoft Entra ID (`bitlockerRecoveryKey` máx. 200 claves/equipo), Device Compliance, Entra `AuditLogs` `[Verificado MS Learn]`. |
| **2. Personal Data Encryption (PDE)** | Cifrado a nivel de archivo (Windows 11 22H2+) y de carpetas conocidas `Desktop`, `Documents` y `Pictures` (Windows 11 24H2+) vinculando las claves criptográficas a **Windows Hello for Business** y descartándolas al cerrar sesión `[Verificado MS Learn]`. | `Intune > Endpoint security > Disk encryption > Personal Data Encryption` (o Settings Catalog > `PDE`) | `PersonalDataEncryption CSP`, Windows Hello for Business, coexistencia aditiva sobre BitLocker `[Verificado MS Learn]`. |
| **3. UEFI Secure Boot (Certificados 2023), TPM 2.0, System Guard y Pluton** | Verificación criptográfica de firmware y gestor de arranque con transición activa a **Windows UEFI CA 2023**, raíz de confianza en **TPM 2.0 / Microsoft Pluton**, arranque medido dinámico (**System Guard Secure Launch / DRTM**) y protección **Kernel DMA** `[Verificado MS Learn]`. | `Intune > Settings Catalog > Secure Boot` y `Reports > Windows quality updates > Secure Boot status` (Autopatch) | `SecureBoot CSP` (`EnableSecurebootCertificateUpdates = 22852`), Microsoft Azure Attestation, System Event Log (`1808`, `1801`, `1795`) `[Verificado MS Learn]`. |
| **4. Virtualization-Based Security (VBS), HVCI y Kernel Stack Protection** | Creación del *Virtual Secure Mode (VSM)* mediante el hipervisor de Windows para aislar páginas ejecutables del kernel (**HVCI / Memory Integrity**) y proteger direcciones de retorno en hardware (**Kernel-mode Hardware-enforced Stack Protection**) `[Verificado MS Learn]`. | `Intune > Endpoint security > Account protection / Security baselines` y Settings Catalog > `Device Guard` | Hipervisor Windows, Intel CET / Arm PAC, Defender Vulnerability Management, `DeviceEvents` `[Verificado MS Learn]`. |
| **5. Credential Guard, Remote Credential Guard y LSA Protection (`RunAsPPL`)** | Aislamiento de secretos NTLM, TGTs Kerberos y credenciales de dominio en `LsaIso.exe` sobre VBS (**Credential Guard**), redirección Kerberos sin exponer credenciales en RDP (**Remote Credential Guard**) y ejecución de `lsass.exe` como proceso protegido PPL `[Verificado MS Learn]`. | `Intune > Endpoint security > Account protection` y Settings Catalog > `Local Security Authority` / `Device Guard` | VBS, Active Directory / Entra Kerberos, Defender for Endpoint (`DeviceEvents` / bloqueo de volcado LSASS) `[Verificado MS Learn]`. |
| **6. Windows LAPS (Local Administrator Password Solution)** | Gestión nativa en el sistema operativo (`laps.dll`, `lapscsp.dll`) de cuentas locales de emergencia con respaldo cifrado directo a **Microsoft Entra ID**, **Automatic Account Management** con sufijo aleatorio en 24H2+ y rotación automática post-uso `[Verificado MS Learn]`. | `Entra > Devices > Device settings` y `Intune > Endpoint security > Account protection > Windows LAPS` | `LAPS CSP`, Microsoft Graph (`DeviceLocalCredential.Read.All`), Event Log `Microsoft-Windows-LAPS/Operational` (`10029`), Entra `AuditLogs` `[Verificado MS Learn]`. |
| **7. Windows Hello for Business (WHfB) & Passwordless Experience** | Autenticación multifactor resistente a phishing respaldada por claves asimétricas en TPM 2.0, modelo **Cloud Kerberos Trust** para SSO híbrido simplificado, **Web Sign-in** con TAP y ocultamiento del proveedor de contraseñas (`EnablePasswordlessExperience`) `[Verificado MS Learn]`. | `Intune > Devices > Enrollment > Windows Hello for Business` y `Endpoint security > Account protection` | Microsoft Entra Kerberos, TPM 2.0, Temporary Access Pass (TAP), Personal Data Encryption `[Verificado MS Learn]`. |
| **8. App Control for Business, Smart App Control, Administrator Protection y Windows Firewall** | Control de integridad de binarios, scripts y drivers en kernel/usuario (**App Control for Business**, antes WDAC), reputación IA (**Smart App Control**), elevación JIT con token aislado y Windows Hello (**Administrator Protection**) y microsegmentación local (**Windows Firewall**) `[Verificado MS Learn]`. | `Intune > Endpoint security > App Control for Business / Firewall` y Settings Catalog > `Local Policies Security Options` | Intelligent Security Graph (ISG), Managed Installer (IME), ETW `Microsoft-Windows-LUA` (`15031`/`15032`), CodeIntegrity (`3076`/`3077`) `[Verificado MS Learn]`. |

### 3.2 Desglose Técnico Profundo de los Cuatro Dominios de Endurecimiento

#### 3.2.1 Dominio 1 — BitLocker Drive Encryption y Gobierno del Ciclo de Vida de Claves
- **Algoritmos y alcance de volúmenes:** Microsoft recomienda cifrado **XTS-AES** (128 bits o **256 bits** para máxima fortaleza regulatoria; XTS-AES no es compatible con unidades extraíbles que deban leerse en versiones legadas anteriores a Windows 10 1511, donde se emplea `AES-CBC`) cubriendo unidades de sistema operativo, unidades fijas de datos y unidades extraíbles mediante **BitLocker To Go** con bloqueo de escritura en medios USB no cifrados `[Verificado MS Learn]`.
- **Habilitación silenciosa vs. Pre-boot PIN y mejoras en Windows 11 24H2:**
  - En **Windows 11 24H2+**, Microsoft eliminó los antiguos prerrequisitos de *Modern Standby / HSTI* y de interfaces *DMA* para el cifrado automático durante OOBE/Autopilot, ampliando drásticamente los equipos que se cifran de forma nativa con solo disponer de TPM y UEFI Secure Boot `[Verificado MS Learn]`.
  - Para **Silent BitLocker** en Intune (`Endpoint security > Disk encryption > BitLocker`, evitando *Settings Catalog* porque carece de todos los controles de autenticación de arranque TPM para habilitación silenciosa confiable), se exige: `Require Device Encryption = Enabled`, `Allow Warning For Other Disk Encryption = Disabled` (tras auditar ausencia de cifradores de terceros para evitar pérdida de datos), `Allow Standard User Encryption = Enabled` y `Configure TPM startup PIN/key = Do not allow` `[Verificado MS Learn]`.
  - Para flotas de **alto riesgo físico** (ejecutivos, viajeros internacionales, defensa), se despliega un perfil separado exigiendo **TPM 2.0 + Startup PIN** pre-arranque (incompatible con habilitación silenciosa, pues requiere que el usuario defina el PIN; toda modificación de PIN queda registrada con **Event ID 789** en `Microsoft-Windows-BitLocker-API/Management`) `[Verificado MS Learn]`.
  - El tipo de cifrado predeterminado en modo silencioso es *Used space only* en equipos *Modern Standby (S0 Low Power Idle)* y *Full disk encryption* en equipos no-Modern Standby (verificable con `powercfg /a` y `manage-bde -status c:`), pudiendo forzarse *Full encryption* mediante `Enforce drive encryption type on operating system drives` `[Verificado MS Learn]`.
- **Escrow, límite de 200 claves, rotación y privilegio mínimo en Entra ID:**
  - Debe configurarse `Save BitLocker recovery information to Microsoft Entra ID = Enabled` y `Store recovery information in Microsoft Entra ID before enabling BitLocker = Required` `[Verificado MS Learn]`.
  - **Límite crítico:** Microsoft Entra ID admite un **máximo de 200 claves de recuperación BitLocker por objeto de dispositivo**; al alcanzarse dicho tope, el cifrado silencioso falla porque no puede respaldar nuevas claves antes de cifrar `[Verificado MS Learn]`.
  - **Advertencia operativa sobre borrado en Intune:** Eliminar el objeto de Intune de un dispositivo Microsoft Entra joined protegido con BitLocker dispara una sincronización que **remueve los protectores de clave del volumen de sistema operativo**, dejando BitLocker en estado **suspendido** `[Verificado MS Learn]`.
  - **Rotación automática y remota:** Habilitar `Client-driven recovery password rotation` permite rotar automáticamente la contraseña de recuperación tras un uso local o disparar la acción remota `BitLocker key rotation` desde Intune (requiere permiso RBAC `Remote tasks > Rotate BitLockerKeys`) `[Verificado MS Learn]`.
  - **Restricción de auto-servicio y auditoría:** En `entra.microsoft.com > Devices > Device settings`, el conmutador *Restrict users from recovering the BitLocker key(s) for their owned devices* (`allowedToReadBitlockerKeysForOwnedDevice = false` en Graph) impide que usuarios estándar lean la clave de su propio equipo y eludan controles administrativos; todo acceso administrativo o de usuario genera el evento auditable `Read BitLocker key` bajo la categoría `KeyManagement` en `AuditLogs` `[Verificado MS Learn]`.

#### 3.2.2 Dominio 2 — Secured-core PC y la Renovación Crítica de Certificados UEFI Secure Boot (2011 -> 2023)
- **Arquitectura Secured-core PC y Microsoft Pluton:** Un **Secured-core PC** combina protecciones de hardware, firmware y núcleo habilitadas de fábrica: **TPM 2.0** o procesador criptográfico integrado en el silicio **Microsoft Pluton** (eliminando el bus físico expuesto entre CPU y TPM discreto), **System Guard Secure Launch** (que utiliza *Dynamic Root of Trust for Measurement [DRTM]* para arrancar en un estado limpio independiente de código UEFI potencialmente comprometido y supervisa *System Management Mode [SMM]*), **Kernel DMA Protection** (IOMMU contra ataques físicos Thunderbolt/PCIe), **VBS**, **HVCI** y **Kernel-mode Hardware-enforced Stack Protection** `[Verificado MS Learn]`.
- **Transición obligatoria de certificados UEFI Secure Boot (Vencimiento Junio 2026):**
  - Los certificados Secure Boot originales de 2011 comenzaron a expirar en **junio de 2026**. Si un endpoint no recibe los nuevos certificados **2023** y el nuevo gestor de arranque firmado por **Windows UEFI CA 2023**, Windows puede seguir iniciando pero **pierde la capacidad de validar y aplicar futuras protecciones de seguridad sobre componentes de arranque temprano** (como mitigaciones posteriores a `CVE-2023-24932`), o sufrir errores de validación Secure Boot y bucles de recuperación BitLocker en firmwares antiguos `[Verificado MS Learn]`.
  - **Mecanismos oficiales de despliegue:**
    1. **Microsoft Intune (Settings Catalog > categoría `Secure Boot`):** Tres directivas dedicadas: `Enable SecureBoot Certificate Updates` (CSP `./Device/Vendor/MSFT/Policy/Config/SecureBoot/EnableSecurebootCertificateUpdates` con valor habilitado `22852`), `Configure Microsoft Update Managed Opt In` (opt-in a *Controlled Feature Rollout*, requiere telemetría diagnóstica) y `Configure High Confidence Opt-Out` `[Verificado MS Learn]`.
    2. **Registro de Windows / GPO:** Clave `HKLM\SYSTEM\CurrentControlSet\Control\SecureBoot\AvailableUpdates = 0x5944` (equivalente decimal `22852`) o GPO `Computer Configuration > Administrative Templates > Windows Components > Secure Boot > Enable Secure Boot certificate deployment` `[Verificado MS Learn]`.
    3. **Windows Configuration System (WinCS CLI):** Herramienta para clientes unidos a dominio en Windows 11 23H2/24H2/25H2 (`Feature_AllKeysAndBootMgrByWinCS`, clave `F33E0C8E002`) `[Verificado MS Learn]`.
    - *Regla de oro oficial:* Actualizar primero el **firmware UEFI/BIOS del OEM**, probar en grupo piloto multi-OEM con BitLocker activo, **no mezclar métodos de despliegue en el mismo equipo** y prever ~48 horas y uno o más reinicios para completar la secuencia `[Verificado MS Learn]`.
  - **Señales exactas de monitoreo y diagnóstico:**
    - Informe nativo en **Windows Autopatch**: `Intune > Reports > Windows quality updates > Reports > Secure Boot status` `[Verificado MS Learn]`.
    - Clave de estado en registro: `HKLM\SYSTEM\CurrentControlSet\Control\SecureBoot\Servicing\UEFICA2023Status` debe alcanzar el valor `"Updated"`, sin existencia de `UEFICA2023Error` `[Verificado MS Learn]`.
    - Eventos en `Windows Logs > System`: **Event ID 1808** confirma aplicación exitosa de los certificados 2023 en el firmware; **Event ID 1801** indica certificados aún pendientes; **Event ID 1795** (o `AvailableUpdates` atascado en `0x4104` sin limpiar el bit `0x0004` de KEK) indica fallo al entregar certificados al firmware UEFI, requiriendo actualización BIOS del fabricante `[Verificado MS Learn]`.

#### 3.2.3 Dominio 3 — Protección de Credenciales, Windows LAPS (24H2+) y Windows Hello for Business
- **Credential Guard y LSA Protection (`RunAsPPL`):** Desde Windows 11 22H2 Enterprise, **Credential Guard** está habilitado por defecto en sistemas que cumplen requisitos de hardware, aislando secretos derivados en VBS fuera del alcance incluso de malware con privilegios `SYSTEM`, mientras que **Remote Credential Guard** protege sesiones RDP redirigiendo solicitudes Kerberos al host origen sin enviar credenciales al equipo remoto `[Verificado MS Learn]`. Complementariamente, **LSA Protection (`RunAsPPL`)** ejecuta `lsass.exe` como *Protected Process Light*, impidiendo inyección de DLLs no firmadas por Microsoft y bloqueando volcados de memoria (`T1003.001`) `[Verificado MS Learn]`.
- **Windows LAPS nativo y *Automatic Account Management*:** Integrado directamente en el sistema operativo (`laps.dll`, `lapscsp.dll` con ciclo de evaluación cada 1 hora o inmediato vía `Invoke-LapsPolicyProcessing`), respalda contraseñas o *passphrases* doblemente cifradas directamente al objeto de dispositivo en **Microsoft Entra ID** vía HTTPS (`BackupDirectory = 1`, sin depender de Microsoft Entra Connect) `[Verificado MS Learn]`.
  - En **Windows 11 24H2+** (y Windows Server 2025+), incorpora **Automatic Account Management** (`AutomaticAccountManagementEnabled = 1`, `AutomaticAccountManagementEnableAccount`, `AutomaticAccountManagementNameOrPrefix` <= 14 caracteres y `AutomaticAccountManagementRandomizeName = 1` que añade un sufijo aleatorio de 6 dígitos en cada rotación) `[Verificado MS Learn]`.
  - Sus valores predeterminados incluyen `PasswordAgeDays = 30`, `PasswordLength = 14`, `PasswordComplexity = 4`, `PostAuthenticationResetDelay = 24` horas (recomendándose reducir a 4–8 horas en producción `[Decisión / Propuesta Editorial]`) y `PostAuthenticationActions = 3` (*Reset password and sign out* al expirar la ventana de gracia) `[Verificado MS Learn]`.
  - En Microsoft Graph, la lectura se segrega entre `DeviceLocalCredential.ReadBasic.All` (solo metadatos de fechas para compliance) y `DeviceLocalCredential.Read.All` (texto claro mediante `Get-LapsAADPassword -IncludePasswords` o consola Intune/Entra) `[Verificado MS Learn]`.
- **Windows Hello for Business (WHfB) y *Passwordless Experience*:** El modelo **Cloud Kerberos Trust** simplifica radicalmente el SSO híbrido a recursos Active Directory on-premises sin requerir PKI compleja de certificados de usuario (el primer uso en equipos *Hybrid Joined* requiere línea de vista a un DC; en *Entra Joined* opera de inmediato hacia la nube) `[Verificado MS Learn]`. Combinado con **Web Sign-in** (para aprovisionamiento inicial con *Temporary Access Pass [TAP]*) y la directiva **Enable passwordless experience** (`EnablePasswordlessExperience` CSP en Windows 11 24H2+), oculta el proveedor de contraseñas en inicio de sesión, bloqueo, UAC y `RunAs`, eliminando el hábito y la superficie de phishing de contraseñas `[Verificado MS Learn]`.

#### 3.2.4 Dominio 4 — App Control for Business, Smart App Control, PDE, Administrator Protection y Firewall
- **App Control for Business (antes WDAC):** Nombre canónico vigente del motor de integridad de código empresarial de Windows `[Verificado MS Learn]`. Permite desplegar políticas base (`DefaultWindows`, `AllowMicrosoft`) y múltiples políticas suplementarias combinando confianza criptográfica, **Managed Installer** (Intune Management Extension) e **Intelligent Security Graph (ISG)**, junto con la **Microsoft Vulnerable Driver Blocklist** `[Verificado MS Learn]`.
  - *Advertencia crítica de despliegue en equipos con HVCI:* Debido a un comportamiento documentado en Microsoft Learn, las **nuevas políticas Base firmadas** de App Control **deben activarse mediante script acompañado de reinicio del sistema** en equipos con *Memory Integrity (HVCI)* activo (en lugar de empujarlas inicialmente sin reinicio por MDM); las actualizaciones posteriores a políticas base firmadas ya activas, políticas sin firmar y políticas suplementarias sí pueden desplegarse directamente por MDM `[Verificado MS Learn]`.
- **Smart App Control:** Diseñado principalmente para instalaciones limpias sin gestión empresarial compleja de App Control, evalúa procesos, scripts y macros web con IA en nube; en entornos corporativos gobernados con Intune, **App Control for Business** es el control determinista empresarial recomendado `[Verificado MS Learn]`.
- **Personal Data Encryption (PDE):** En Windows 11 24H2+, **PDE for Known Folders** cifra automáticamente `Desktop`, `Documents` y `Pictures` usando claves protegidas por Windows Hello for Business `[Verificado MS Learn]`. Para alcanzar máxima seguridad criptográfica contra extracción forense en memoria, Microsoft Learn recomienda endurecer complementariamente el endpoint **deshabilitando volcados de memoria de kernel/live dumps, volcados de usuario (WER) y la hibernación** `[Verificado MS Learn]`.
- **Administrator Protection en Windows 11:** Disponible desde `KB5120998` y **habilitado por defecto en las líneas base de seguridad de Windows 11 (24H2, 25H2 y 26H2) desde octubre de 2026** `[Verificado MS Learn]`. Al iniciar sesión, incluso un usuario administrador recibe un token desprivilegiado; cuando se requiere elevar, Windows solicita autorización interactiva integrada con **Windows Hello** y genera un token administrativo aislado usando una **cuenta oculta separada por perfil creada por el sistema**, destruyendo el token apenas finaliza el proceso `[Verificado MS Learn]`.
  - Se configura en Intune Settings Catalog (`Local Policies Security Options > User Account Control Type Of Admin Approval Mode` y `User Account Control Behavior Of the Elevation Prompt for Administrator Protection`, requiere reinicio) y se monitorea vía ETW `Microsoft-Windows-LUA` (`{93c05d69-51a3-485e-877f-1806a8731346}`) con **Event ID 15031** (*Elevation Approved*) y **Event ID 15032** (*Elevation Denied/Fail*) `[Verificado MS Learn]`.
  - **Exclusiones obligatorias documentadas en Learn:** **No habilitar Administrator Protection** en **Windows 365 Cloud PCs**, **Azure Virtual Desktop (AVD) session hosts**, dispositivos gestionados con flujos **Windows LAPS** incompatibles o estaciones de virtualización pesada Hyper-V/WSL compartido sin validar aislamiento de perfiles (además de vigilar `KB5124010` frente al error RDP no-admin `0xC000000D`) `[Verificado MS Learn]`. En la flota general de usuarios finales, la práctica recomendada sigue siendo operar como **Standard User + Intune EPM**, reservando *Administrator Protection* para estaciones de desarrolladores o administradores locales excepcionales `[Decisión / Propuesta Editorial]`.
- **Windows Firewall with Advanced Security:** Gobernado desde `Intune > Endpoint security > Firewall` sobre los tres perfiles (`Domain`, `Private`, `Public`) bloqueando conexiones entrantes no solicitadas, auditando desactivaciones mediante el informe `MDM devices running Windows 10 or later with firewall off` (alimentado por `DeviceStatus CSP`) y evitando conflictos de fusión (*rule merging*) con GPOs heredadas `[Verificado MS Learn]`.

### 3.3 Matriz de Integraciones Cruzadas con el Ecosistema Microsoft 365 E5 / E7

| Servicio del Ecosistema | Integración Operativa con Windows Enterprise Security | Resultado de Seguridad Verificable |
| :--- | :--- | :--- |
| **Microsoft Entra ID & Conditional Access** | Escrow cifrado de claves BitLocker y Windows LAPS; **Cloud Kerberos Trust** para WHfB; evaluación de cumplimiento (`Require BitLocker`, `Secure Boot`, `Code Integrity`) antes de emitir tokens OAuth/PRT `[Verificado MS Learn]`. | Bloquea en tiempo real el acceso a M365 y apps corporativas desde equipos sin cifrado o con arranque comprometido `[Verificado MS Learn]`. |
| **Microsoft Intune & Windows Autopatch** | Despliegue declarativo de perfiles `Disk encryption`, `Account protection`, `App Control for Business`, `Firewall`, `Security baselines` y monitoreo del **Secure Boot status report** (certificados 2023) `[Verificado MS Learn]`. | Convergencia de políticas sin dependencia de red corporativa ni controladores de dominio locales `[Verificado MS Learn]`. |
| **Microsoft Defender XDR & Vulnerability Management** | Telemetría en `DeviceEvents`, `DeviceProcessEvents`, `DeviceNetworkEvents` y evaluación continua de configuración de BIOS, Secure Boot, VBS/HVCI, Credential Guard, BitLocker y LAPS en *Security recommendations* `[Verificado MS Learn]`. | Correlaciona intentos de volcado LSASS, drivers vulnerables bloqueados y brechas de firmware en un único incidente XDR `[Verificado MS Learn]`. |
| **Microsoft Sentinel** | Correlación SIEM en `security.microsoft.com` cruzando `AuditLogs` de Entra ID (`Read BitLocker key`, `Recover device local administrator password`) con `SigninLogs` e inicios de sesión locales `DeviceLogonEvents` `[Verificado MS Learn]`. | Detecta abuso interno o exfiltración masiva de claves de recuperación y contraseñas de administrador local `[Decisión / Propuesta Editorial]`. |
| **Microsoft Purview & Windows Resiliency** | Protección complementaria **Purview Endpoint DLP** sobre datos desencriptados en sesión activa de usuario PDE, más recuperación acelerada ante fallos masivos con **Quick Machine Recovery (QMR)** `[Verificado MS Learn]`. | Asegura tanto confidencialidad contra exfiltración lógica como resiliencia operativa ante incidentes de arranque a gran escala `[Verificado MS Learn]`. |

### 3.4 Matriz Canónica de Registros de Eventos Locales y Señales Diagnósticas de Windows 11

Para el diagnóstico forense local, la recolección mediante **Azure Monitor Agent (AMA) / Data Collection Rules (DCR)** hacia Microsoft Sentinel y la correlación con **Microsoft Defender for Endpoint**, los equipos de ingeniería y SOC deben dominar las siguientes fuentes exactas del sistema operativo verificadas en Microsoft Learn `[Verificado MS Learn]`:

| Subsistema de Seguridad | Canal de Registro / Proveedor ETW o Clave de Registro | Identificadores de Evento / Valores Clave | Interpretación Operativa Inmediata |
| :--- | :--- | :--- | :--- |
| **BitLocker Drive Encryption** | `Microsoft-Windows-BitLocker-API/Management` | **Event ID 789** (modificación de PIN pre-arranque); **Event ID 854** (WinRE no configurado bloqueando cifrado silencioso) `[Verificado MS Learn]`. | Audita cambios de PIN por el usuario y explica fallos silenciosos cuando falta la partición de recuperación `[Verificado MS Learn]`. |
| **UEFI Secure Boot (`2023 CAs`)** | `Windows Logs > System` y `HKLM\SYSTEM\CurrentControlSet\Control\SecureBoot\Servicing` | **Event ID 1808** (certificados 2023 aplicados); **Event ID 1801** (pendiente); **Event ID 1795** (error de entrega a firmware); `UEFICA2023Status = Updated` `[Verificado MS Learn]`. | Confirma cierre exitoso de la migración pre-junio 2026 o exige actualizar BIOS/UEFI del OEM (`1795` / `0x4104`) `[Verificado MS Learn]`. |
| **Windows LAPS** | `Microsoft-Windows-LAPS/Operational` | **Event ID 10029** (actualización exitosa de contraseña cifrada en Microsoft Entra ID); ciclo nativo de evaluación cada 60 minutos `[Verificado MS Learn]`. | Evidencia local irrefutable de que el dispositivo rotó y persistió su credencial local en Entra ID `[Verificado MS Learn]`. |
| **LSA Protection (`RunAsPPL`)** | `Microsoft-Windows-Wininit/Operational` y `Microsoft-Windows-CodeIntegrity/Operational` | **Event ID 12** (`LSASS.exe` iniciado como proceso protegido PPL); **Event IDs 3033 / 3063** (DLL bloqueada/auditada por no estar firmada para LSA) `[Verificado MS Learn]`. | Verifica activación real de `RunAsPPL` tras reinicio e identifica agentes antiguos incompatibles `[Verificado MS Learn]`. |
| **App Control for Business** | `Microsoft-Windows-CodeIntegrity/Operational` y `Microsoft-Windows-AppLocker/MSI and Script` | **Event ID 3076** (ejecución permitida solo por modo *Audit*); **Event ID 3077** (ejecución bloqueada en modo *Enforced*); **8028 / 8029** (scripts/MSI) `[Verificado MS Learn]`. | Base primaria para construir políticas suplementarias antes de conmutar de *Audit* a *Enforced* `[Verificado MS Learn]`. |
| **Administrator Protection** | Proveedor ETW `Microsoft-Windows-LUA` (`{93c05d69-51a3-485e-877f-1806a8731346}`) | **Event ID 15031** (*Elevation Approved* con SID, ruta, cuenta aislada y método Windows Hello); **Event ID 15032** (*Elevation Denied/Fail/Timeout*) `[Verificado MS Learn]`. | Trazabilidad completa de elevaciones JIT sobre cuentas administradoras desprivilegiadas en Windows 11 `[Verificado MS Learn]`. |
| **TPM Health Attestation (24H2+)** | Tarea programada `Tpm-PreAttestationHealthCheck` y carpeta `%WinDir%\Logs\MeasuredBoot` | Archivo diagnóstico JSON consolidando estado de TPM 2.0, PCRs, Secure Boot y BitLocker previo a la atestación remota `[Verificado MS Learn]`. | Acelera la resolución de falsos negativos de cumplimiento en políticas `Require BitLocker / Secure Boot` `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Un fallo frecuente en auditorías empresariales consiste en permitir que todos los usuarios estándar lean sus propias claves BitLocker en `myaccount.microsoft.com` (habilitado por defecto en Entra ID) o que roles amplios consulten sin control contraseñas en texto claro de **Windows LAPS** `[Verificado MS Learn]`. En Microsoft Entra ID, por defecto solo `Global Administrator`, `Cloud Device Administrator` e `Intune Administrator` pueden leer contraseñas LAPS en texto claro, mientras que `Cloud Device Administrator`, `Helpdesk Administrator` y `Global Administrator` poseen `microsoft.directory/bitlockerKeys/key/read` `[Verificado MS Learn]`. El diseño de excelencia exige roles personalizados acotados por **Administrative Units (AUs)** y activación **PIM JIT**:

| Rol Oficial / Personalizado | Plano RBAC | Permisos Clave Verificados | Estrategia PIM / JIT Sugerida | Responsabilidad Operativa y Segregación de Funciones |
| :--- | :--- | :--- | :--- | :--- |
| **Endpoint Security Manager** *(Rol integrado Intune)* | Intune RBAC | Gestión integral del nodo `Endpoint security` en Intune: perfiles BitLocker, PDE, Account Protection (WHfB/LAPS), App Control for Business, Firewall, Security Baselines y rotación remota de claves BitLocker `[Verificado MS Learn]`. | **Elegible en PIM (máx. 4 h)** con MFA resistente a phishing y ticket de cambio `[Decisión / Propuesta Editorial]`. | Autoría y despliegue de políticas criptográficas, integridad de código y endurecimiento de endpoints Windows `[Verificado MS Learn]`. |
| **BitLocker Recovery Reader (Custom Entra Role por AU)** *(Rol personalizado Entra ID)* | Microsoft Entra RBAC (Scoped a Administrative Units) | Permiso exclusivo `microsoft.directory/bitlockerKeys/key/read` y `microsoft.directory/devices/standard/read` restringido a la unidad administrativa regional correspondiente `[Verificado MS Learn]`. | **Elegible en PIM (máx. 2 h)** exigiendo número de ticket de usuario verificado `[Decisión / Propuesta Editorial]`. | Entrega puntual de claves de recuperación BitLocker tras validar identidad del empleado, disparando rotación posterior `[Decisión / Propuesta Editorial]`. |
| **Windows LAPS Credential Operator (Custom Entra Role)** *(Rol personalizado Entra ID)* | Microsoft Entra RBAC / Graph | Permiso sensible `DeviceLocalCredential.Read.All` acotado por unidad administrativa para soporte de emergencia N2/N3 `[Verificado MS Learn]`. | **Elegible en PIM (máx. 1 h)** con aprobación de líder de turno y justificación obligatoria `[Decisión / Propuesta Editorial]`. | Recuperación excepcional de contraseña local de emergencia LAPS cuando el equipo está aislado de red o falla Entra auth `[Verificado MS Learn]`. |
| **Windows LAPS & BitLocker Compliance Auditor (Custom Reader)** *(Rol personalizado Entra / Graph)* | Microsoft Entra RBAC / Graph | Permisos de metadatos sin secretos: `DeviceLocalCredential.ReadBasic.All` y `microsoft.directory/bitlockerKeys/metadata/read` `[Verificado MS Learn]`. | **Asignación activa de solo lectura** para reportes automatizados y GRC `[Decisión / Propuesta Editorial]`. | Verificar fechas de respaldo y expiración de contraseñas LAPS y presencia de protectores BitLocker sin acceder jamás al secreto en claro `[Verificado MS Learn]`. |
| **Help Desk Operator** *(Rol integrado Intune)* | Intune RBAC | Ejecución de tareas remotas operativas incluyendo sincronización y **Rotate BitLockerKeys**, visualización de estado de cumplimiento y reportes de cifrado `[Verificado MS Learn]`. | **Activo en turno o elegible PIM 8 h** acotado por *Scope Tags* `[Decisión / Propuesta Editorial]`. | Forzar rotación remota de claves BitLocker y sincronización de políticas sin capacidad de modificar baselines de seguridad `[Verificado MS Learn]`. |
| **Policy and Profile Manager** *(Rol integrado Intune)* | Intune RBAC | Gestión de *Device compliance policies* (`Require BitLocker`, `Require Secure Boot`, `Require Code Integrity`), perfiles *Settings Catalog* (`Secure Boot`, `Administrator Protection`) y filtros `[Verificado MS Learn]`. | **Elegible en PIM (máx. 4 h)** segregado de quienes leen secretos en Entra ID `[Decisión / Propuesta Editorial]`. | Mantenimiento de políticas de cumplimiento, transición de certificados UEFI 2023 y líneas base de configuración `[Verificado MS Learn]`. |
| **Security Administrator / Security Reader** *(Roles Microsoft Entra / Defender XDR)* | Defender Unified RBAC + Entra | Visibilidad de recomendaciones de postura en Defender Vulnerability Management, Advanced Hunting (`DeviceEvents`, `AuditLogs`) y gestión de incidentes XDR `[Verificado MS Learn]`. | `Security Reader` activo en SOC L1/L2; `Security Administrator` **elegible PIM (4 h)** `[Decisión / Propuesta Editorial]`. | Detección, caza de amenazas sobre LSASS/App Control y respuesta a incidentes de exposición de credenciales `[Verificado MS Learn]`. |
| **Cloud Device Administrator** *(Rol integrado Microsoft Entra)* | Microsoft Entra RBAC | Habilitación global de Windows LAPS y restricción de lectura BitLocker en `Device settings`, baja/deshabilitación de objetos de dispositivo en Entra ID `[Verificado MS Learn]`. | **Elegible en PIM (máx. 2 h)** con aprobación dual para cambios en `Device settings` `[Decisión / Propuesta Editorial]`. | Gobierno del ciclo de vida de identidades de dispositivos y parámetros globales de LAPS/BitLocker en Entra ID `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

### D-01: Monitoreo Diario de Estado de Cifrado BitLocker y Fallos de Habilitación Silenciosa
- **Objetivo:** Asegurar que el 100 % de los equipos aprovisionados completen el cifrado silencioso y respalden sus protectores en Microsoft Entra ID sin degradar su estado de cumplimiento `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Monitor** > **Encryption report** y **Endpoint security** > **Disk encryption** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer / Help Desk L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar en **Encryption report** todos los dispositivos Windows con `Encryption readiness = Ready` pero `Encrypted = No` o con estado de perfil `Error` / `Conflict` `[Verificado MS Learn]`.
  2. Verificar las causas raíz documentadas: presencia de directiva conflictiva que exija PIN/clave TPM de arranque bloqueando el modo silencioso, partición **WinRE** no configurada, Secure Boot desactivado o alcance del tope de **200 claves BitLocker** en el objeto Entra `[Verificado MS Learn]`.
  3. Resolver conflictos de políticas y disparar sincronización remota sobre los dispositivos remediados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación diaria del `Encryption report` y tickets de remediación para equipos no cifrados > 24 h desde enrolamiento `[Decisión / Propuesta Editorial]`.

### D-02: Auditoría Diaria de Accesos a Claves BitLocker y Contraseñas de Windows LAPS en `AuditLogs`
- **Objetivo:** Detectar accesos no autorizados, exfiltración masiva o falta de rotación posterior sobre secretos críticos de recuperación local `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > **Monitoring & health** > **Audit logs** (y correlación KQL en `https://security.microsoft.com`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar actividades de las últimas 24 horas bajo categoría `KeyManagement` (`Read BitLocker key`) y `Device` (`Recover device local administrator password`) `[Verificado MS Learn]`.
  2. Validar que cada lectura provenga de un operador con activación PIM vigente y ticket ITSM asociado; generar incidente de alta severidad si un mismo actor consulta >= 5 claves/contraseñas en una ventana corta `[Decisión / Propuesta Editorial]`.
  3. Confirmar que tras toda entrega manual de una clave BitLocker se haya ejecutado la acción remota `BitLocker key rotation` en Intune `[Verificado MS Learn]`.
- **Evidencia Auditable:** Trazas conciliadas en `AuditLogs` y confirmaciones de rotación post-exposición `[Verificado MS Learn]`.

### D-03: Vigilancia Diaria de Errores de Actualización de Certificados UEFI Secure Boot (`2023`)
- **Objetivo:** Detectar fallos de entrega de los certificados **Windows UEFI CA 2023** al firmware UEFI antes de que provoquen pérdida de protección pre-arranque o incidencias de inicio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Windows quality updates** > pestaña **Reports** > **Secure Boot status** `[Verificado MS Learn]`.
- **Rol Responsable:** Windows Platform Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar la columna **Alerts** y **Certificate status** en el *Secure Boot status report* de Windows Autopatch identificando dispositivos con fallos recientes `[Verificado MS Learn]`.
  2. Correlacionar mediante Advanced Hunting o Device Query la presencia en el registro de `UEFICA2023Error` distinto de cero, `AvailableUpdates` bloqueado en `0x4104` (fallo de actualización KEK) o eventos de sistema **Event ID 1795** y **Event ID 1801** `[Verificado MS Learn]`.
  3. Pausar la aplicación de la política en el modelo de placa base OEM afectado y priorizar el despliegue previo de la actualización de BIOS/UEFI del fabricante `[Verificado MS Learn]`.
- **Evidencia Auditable:** Lista diaria de dispositivos con alerta en *Secure Boot status report* y paquete de firmware OEM asignado `[Verificado MS Learn]`.

### D-04: Triaje Diario de Eventos de **App Control for Business** y Bloqueo de Drivers Vulnerables
- **Objetivo:** Distinguir bloqueos legítimos de aplicaciones de línea de negocio frente a intentos reales de ejecución de malware o carga de drivers vulnerables (*BYOVD*) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > **Investigation & response** > **Hunting** > **Advanced hunting** (`DeviceEvents`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Consultar eventos de integridad de código (`AppControlCodeIntegrityPolicyAudited` / `AppControlCodeIntegrityPolicyBlocked` y drivers bloqueados equivalentes a Event IDs `3076` y `3077` de `Microsoft-Windows-CodeIntegrity/Operational`) de las últimas 24 horas `[Verificado MS Learn]`.
  2. Investigar como incidente potencial todo intento de carga de driver firmado conocido como vulnerable (*Microsoft Vulnerable Driver Blocklist*) o ejecutable no firmado en rutas temporales `[Verificado MS Learn]`.
  3. Documentar falsos positivos de herramientas internas firmadas para su inclusión controlada en la revisión semanal de políticas suplementarias `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Consulta diaria ejecutada y triaje de bloqueos de código/drivers registrado en cola SOC `[Decisión / Propuesta Editorial]`.

### D-05: Monitoreo Diario de Respaldo y Rotación Post-Autenticación en **Windows LAPS**
- **Objetivo:** Garantizar que ningún equipo Windows quede con contraseña local estática o sin respaldo vigente en Microsoft Entra ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Account protection** y **Reports** > **Device configuration** `[Verificado MS Learn]`.
- **Rol Responsable:** Identity & Endpoint Operations L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar fallos de aplicación del perfil de **Windows LAPS** en `Account protection` (ej. cuenta personalizada inexistente cuando se usa modo manual sin haberla creado con `Accounts CSP`) `[Verificado MS Learn]`.
  2. Verificar que los dispositivos donde ayer se recuperó la contraseña local hayan ejecutado efectivamente su **Post-authentication action** (`Reset password and sign out`) y registrado un nuevo respaldo exitoso (**Event ID 10029**) con marca de tiempo actualizada en Entra ID `[Verificado MS Learn]`.
  3. En equipos donde la rotación automática post-uso no se haya reflejado por desconexión prolongada, programar rotación forzada (`Reset-LapsPassword` / acción remota) al reconectar `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `Succeeded` del perfil Windows LAPS y actualización de `PasswordUpdateTime` verificada vía Graph Basic `[Verificado MS Learn]`.

### D-06: Detección y Remediación de Endpoints con **Windows Firewall** Desactivado
- **Objetivo:** Impedir que endpoints corporativos operen en redes públicas o corporativas con perfiles de firewall deshabilitados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Firewall** > **MDM devices running Windows 10 or later with firewall off** `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Endpoint Operations L1 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Consultar el reporte nativo alimentado por `DeviceStatus CSP` para listar cualquier dispositivo con Firewall apagado en perfiles Domain, Private o Public `[Verificado MS Learn]`.
  2. Cruzar los dispositivos detectados con alertas de `Tampering` o desactivación de defensas (`T1562.004`) en Microsoft Defender XDR `[Verificado MS Learn]`.
  3. Forzar sincronización de la política `Endpoint security > Firewall` o aislar preventivamente el host si coexisten señales de intrusión `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario en cero dispositivos (o tickets de remediación inmediata abiertos) `[Decisión / Propuesta Editorial]`.

### D-07: Caza Diaria de Ataques contra **Credential Guard** y **LSA Protection (`RunAsPPL`)**
- **Objetivo:** Identificar procesos maliciosos o herramientas ofensivas intentando leer la memoria de `lsass.exe` o extraer tickets Kerberos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > **Investigation & response** > **Incidents & alerts** y **Advanced hunting** `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Threat Hunter `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar alertas e eventos `DeviceEvents` / `SecurityEvent` de acceso bloqueado a `lsass.exe` protegido por `RunAsPPL` y auditorías de drivers/plug-ins LSA rechazados por falta de firma Microsoft (`Event IDs 3033 / 3063`) `[Verificado MS Learn]`.
  2. Verificar que el proceso atacante haya sido contenido y que el host mantenga activos **Credential Guard** y **LSA Protection** sin degradación de registro `[Verificado MS Learn]`.
  3. Escalar a respuesta a incidentes cualquier intento de acceso a memoria LSASS independientemente de que haya sido bloqueado preventivamente (indicador de post-explotación activa `T1003.001`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Expedientes de investigación SOC sobre eventos de acceso bloqueado a LSASS `[Decisión / Propuesta Editorial]`.

### D-08: Supervisión de **Windows Hello for Business** y **Personal Data Encryption (PDE)**
- **Objetivo:** Resolver incidencias de registro de claves TPM en WHfB que impidan el inicio de sesión sin contraseña o el cifrado automático de archivos en PDE `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Account protection** y **Disk encryption** (`Personal Data Encryption`) `[Verificado MS Learn]`.
- **Rol Responsable:** Help Desk L2 / Identity Operations `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar errores de aplicación en los perfiles de **Windows Hello for Business** (*Cloud Kerberos Trust*) y **Personal Data Encryption** `[Verificado MS Learn]`.
  2. En dispositivos *Hybrid Joined* recién aprovisionados donde falle el primer desbloqueo con PIN de WHfB, verificar conectividad inicial de línea de vista hacia un controlador de dominio con el objeto *Microsoft Entra Kerberos* publicado `[Verificado MS Learn]`.
  3. Confirmar que usuarios que requieran recuperación de acceso reciban un **Temporary Access Pass (TAP)** de un solo uso para *Web Sign-in* sin reactivar contraseñas permanentes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tasa diaria de éxito de perfiles WHfB y PDE sin degradaciones a contraseña `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Gobernanza Semanal por Anillos de la Renovación **Windows UEFI CA 2023**
- **Objetivo:** Completar ordenadamente la actualización de certificados Secure Boot 2023 y del gestor de arranque firmado 2023 en el 100 % del parque Windows `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Windows quality updates** > **Secure Boot status** y **Devices** > **Configuration** `[Verificado MS Learn]`.
- **Rol Responsable:** Windows Platform Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Analizar en el **Secure Boot status report** el porcentaje de equipos con `Certificate status = Up to date` (`UEFICA2023Status = Updated` y **Event ID 1808**) frente a los pendientes por familia y modelo de placa base OEM `[Verificado MS Learn]`.
  2. Validar que los dispositivos de anillos piloto con `Enable SecureBoot Certificate Updates` habilitado (`22852` / `0x5944`) hayan completado sus reinicios tras 48 horas sin disparar prompts de recuperación BitLocker `[Verificado MS Learn]`.
  3. Expandir progresivamente la asignación de la política a los siguientes anillos de producción manteniendo un único método de despliegue (Intune CSP, sin mezclar GPO/WinCS en los mismos hosts) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tablero semanal de progreso hacia `Windows UEFI CA 2023` desglosado por fabricante y modelo `[Verificado MS Learn]`.

### S-02: Auditoría Semanal de Postura **Secured-core PC** (TPM 2.0, System Guard, VBS, HVCI y Stack Protection)
- **Objetivo:** Detectar equipos donde protecciones de silicio o virtualización hayan quedado desactivadas por cambios de BIOS o incompatibilidad de drivers `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > **Vulnerability management** > **Recommendations** y `https://intune.microsoft.com` > **Devices** > **Compliance** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar en **Defender Vulnerability Management** recomendaciones activas sobre `Turn on Virtualization Based Security`, `Turn on Memory Integrity (HVCI)`, `Enable Secure Boot`, `Kernel DMA Protection` y `Hardware-enforced Stack Protection` `[Verificado MS Learn]`.
  2. Para equipos que no puedan activar HVCI o Kernel Stack Protection por drivers de terceros incompatibles, inventariar el driver bloqueante (`.sys`) y gestionar actualización con el OEM/proveedor `[Verificado MS Learn]`.
  3. Revisar fallos de atestación de salud TPM (incluyendo en Windows 11 24H2+ el archivo diagnóstico JSON generado por la tarea `Tpm-PreAttestationHealthCheck` en la carpeta `MeasuredBoot`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de cobertura VBS/HVCI/Secured-core y plan de reemplazo de drivers legados `[Decisión / Propuesta Editorial]`.

### S-03: Ciclo Semanal de Políticas Suplementarias y Promoción *Audit -> Enforced* en **App Control for Business**
- **Objetivo:** Evolucionar las políticas de integridad de código sin bloquear herramientas legítimas firmadas de negocio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **App Control for Business** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer + Application Packaging Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Consolidar los eventos de auditoría (`Event ID 3076`) recolectados en la semana desde grupos piloto de negocio `[Verificado MS Learn]`.
  2. Generar o actualizar políticas **Supplemental** en el *App Control Wizard* autorizando certificados de editores internos verificados o rutas gestionadas por *Managed Installer* (IME), evitando reglas permisivas por ruta escribible `[Verificado MS Learn]`.
  3. Recordar que si se despliega una **nueva política Base firmada** en equipos con HVCI activo, debe aplicarse vía script con reinicio programado; las políticas suplementarias pueden asignarse directamente desde Intune `[Verificado MS Learn]`.
- **Evidencia Auditable:** Repositorio versionado en Git de archivos `.xml`/`.cip` de App Control y registro de cambios aprobado `[Decisión / Propuesta Editorial]`.

### S-04: Higiene de Claves BitLocker en Entra ID (Límite de 200 Claves, Rotación y `BitLocker To Go`)
- **Objetivo:** Prevenir fallos de cifrado por agotamiento del límite de claves en objetos Entra y auditar el control sobre almacenamiento USB extraíble `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > **Devices** > **All devices** y Microsoft Graph PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Identity & Endpoint Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar consulta automatizada de metadatos BitLocker (`microsoft.directory/bitlockerKeys/metadata/read`) identificando objetos de dispositivo que acumulen > 150 claves históricas (acercándose al límite duro de **200 claves por dispositivo**) para planificar reprovisionamiento limpio antes de que falle el respaldo `[Verificado MS Learn]`.
  2. Auditar en Defender XDR eventos de montaje de unidades USB y bloqueos de escritura en medios no cifrados impuestos por **BitLocker To Go** `[Verificado MS Learn]`.
  3. Confirmar que ningún administrador haya borrado objetos en Intune sin seguir el procedimiento de baja, evitando dejar volúmenes activos con BitLocker suspendido `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de salud de llaves escrowed en Entra ID (< 150 claves/dispositivo) y cumplimiento de `BitLocker To Go` `[Decisión / Propuesta Editorial]`.

### S-05: Auditoría Semanal de **Administrator Protection** (Eventos ETW `15031`/`15032` y Exclusiones)
- **Objetivo:** Controlar las elevaciones aprobadas con Windows Hello en estaciones que utilicen *Administrator Protection* y asegurar que no se aplique a plataformas incompatibles `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Configuration** (Settings Catalog > `Local Policies Security Options`) `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar la telemetría recolectada de los eventos **15031** (*Elevation Approved*) y **15032** (*Elevation Denied/Fail*) del proveedor `Microsoft-Windows-LUA` en los grupos donde *Administrator Protection* está habilitado `[Verificado MS Learn]`.
  2. Auditar los filtros de asignación (*Assignment Filters*) en Intune garantizando la exclusión estricta de **Windows 365 Cloud PCs**, **Azure Virtual Desktop session hosts** y equipos con flujos **Windows LAPS** o RDP no-admin afectados `[Verificado MS Learn]`.
  3. Verificar que los usuarios que experimentan elevaciones repetitivas legítimas sean migrados preferentemente al modelo de usuario estándar con reglas acotadas de **Intune Endpoint Privilege Management** `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Verificación de filtros de exclusión en Intune y resumen semanal de eventos `15031`/`15032` `[Decisión / Propuesta Editorial]`.

### S-06: Gobernanza de Reglas y Fusión (*Rule Merging*) en **Windows Firewall with Advanced Security**
- **Objetivo:** Evitar aperturas accidentales de puertos entrantes derivadas de la combinación no controlada de reglas locales, GPO y múltiples perfiles de Intune `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Firewall** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Network Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar las políticas `Windows Firewall Rules` verificando que para perfiles `Public` (y `Private` en teletrabajo) esté deshabilitada la fusión de reglas locales creadas por usuarios/instaladores cuando se exija aislamiento estricto (*Shields Up*) `[Verificado MS Learn]`.
  2. Revisar en Defender XDR `DeviceNetworkEvents` puertos en escucha (`Inbound` aceptados) no contemplados en la matriz corporativa de microsegmentación de estaciones (ej. SMB 445, WinRM 5985/5986 o RDP 3389 expuestos lateralmente entre clientes) `[Decisión / Propuesta Editorial]`.
  3. Depurar reglas duplicadas entre GPO heredadas y perfiles nativos de Intune Endpoint Security `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal de reglas entrantes permitidas en endpoints y cero puertos de administración lateral abiertos a subredes de usuarios `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Conciliación Mensual contra **Windows 11 Security Baselines** (24H2 / 25H2 / 26H2)
- **Objetivo:** Alinear la postura técnica de la flota con las actualizaciones de las líneas base oficiales de seguridad de Microsoft sin introducir regresiones operativas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Security baselines** > **Security Baseline for Windows 10 and later** `[Verificado MS Learn]`.
- **Rol Responsable:** Windows Platform Architect + Security Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Comparar la versión desplegada del baseline contra la última revisión publicada por Microsoft (incluyendo los nuevos valores predeterminados de octubre de 2026 para Windows 11 24H2/25H2/26H2, donde *Administrator Protection* y endurecimientos UAC/BitLocker se actualizan por defecto) `[Verificado MS Learn]`.
  2. Evaluar explícitamente conflictos conocidos entre el baseline y otros perfiles: por ejemplo, que el baseline no habilite `TPM startup PIN` sobre grupos asignados a **Silent BitLocker**, ni active *Administrator Protection* sobre Cloud PCs, AVD o equipos LAPS `[Verificado MS Learn]`.
  3. Desplegar los ajustes validados en anillo piloto durante 14 días antes de actualizar producción `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Matriz mensual de desviaciones documentadas respecto al *Windows 11 Security Baseline* `[Decisión / Propuesta Editorial]`.

### M-02: Auditoría Mensual de Endurecimiento de **Personal Data Encryption (PDE)** contra Exposición en Memoria/Disco
- **Objetivo:** Garantizar que las claves criptográficas de PDE no queden expuestas en archivos de hibernación ni volcados de memoria `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Disk encryption** (`Personal Data Encryption`) y **Devices** > **Configuration** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar cobertura efectiva de **PDE for Known Folders** (`Desktop`, `Documents`, `Pictures`) en dispositivos Windows 11 24H2+ asignados a perfiles ejecutivos, I+D, legal y finanzas `[Verificado MS Learn]`.
  2. Auditar la aplicación de las cuatro recomendaciones oficiales de endurecimiento de Microsoft Learn para PDE: (a) deshabilitar *kernel-mode crash dumps y live dumps*; (b) deshabilitar *Windows Error Reporting (WER) / user-mode crash dumps*; (c) deshabilitar *hibernación* (`hiberfil.sys`); y (d) exigir reautenticación inmediata al reanudar desde *connected standby* `[Verificado MS Learn]`.
  3. Confirmar en pruebas muestrales que al cerrar sesión el usuario, los archivos protegidos resulten criptográficamente inaccesibles para cualquier otra cuenta en el mismo equipo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de cumplimiento del perfil PDE y políticas complementarias de bloqueo de dumps/hibernación `[Verificado MS Learn]`.

### M-03: Revisión Mensual de Adopción **Passwordless Experience** y **Cloud Kerberos Trust**
- **Objetivo:** Eliminar progresivamente el uso de contraseñas en el inicio de sesión e interacciones UAC de Windows 11 `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Account protection** y `https://entra.microsoft.com` > **Monitoring & health** > **Sign-in logs** `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Security Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Medir en `SigninLogs` y `DeviceLogonEvents` el porcentaje de inicios de sesión en Windows realizados con **Windows Hello for Business** o llaves de seguridad FIDO2 frente a contraseñas tradicionales `[Verificado MS Learn]`.
  2. Ampliar mensualmente los grupos cubiertos por la política **Enable passwordless experience** (`EnablePasswordlessExperience` CSP) y **Web Sign-in** en Windows 11 24H2+ una vez confirmado el enrolamiento WHfB del usuario `[Verificado MS Learn]`.
  3. Auditar la salud del objeto **Microsoft Entra Kerberos** en los controladores de dominio Active Directory (rotación regular de claves Kerberos cada 30 días) para escenarios *Cloud Kerberos Trust* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Indicador mensual de inicios de sesión *passwordless* en Windows y registro de rotación de clave *Microsoft Entra Kerberos* `[Verificado MS Learn]`.

### M-04: Higiene Mensual de **Windows LAPS Automatic Account Management** y Cuentas Locales
- **Objetivo:** Asegurar que todas las cuentas de emergencia locales usen nombres aleatorizados, rotación activa y cero contraseñas compartidas en la flota `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Account protection** (`Windows LAPS` y `Local user group membership`) `[Verificado MS Learn]`.
- **Rol Responsable:** Identity & Endpoint Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar en endpoints Windows 11 24H2+ la aplicación correcta de **Automatic Account Management** (`AutomaticAccountManagementEnabled = 1` y `AutomaticAccountManagementRandomizeName = 1` con prefijo <= 14 caracteres + 6 dígitos aleatorios) `[Verificado MS Learn]`.
  2. Auditar con política `Local user group membership` (Acción `Replace` o `Update` controlada) que el grupo local `Administrators` contenga únicamente `SID S-1-5-32-544` con la cuenta gestionada por LAPS y los grupos SID de roles Entra autorizados, erradicando cuentas locales manuales `[Verificado MS Learn]`.
  3. Verificar mediante Graph (`DeviceLocalCredential.ReadBasic.All`) que el 99 %+ de dispositivos activos posean `PasswordExpirationTime` futura válida (< 30 días de antigüedad) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de frescura de respaldo Windows LAPS y auditoría de membresía local `Administrators` `[Verificado MS Learn]`.

### M-05: Control Mensual de Erradicación de Sistemas Fuera de Soporte y Estándar Criptográfico XTS-AES 256
- **Objetivo:** Impedir deuda técnica de sistemas Windows 10 post-EOS (14-oct-2025) o volúmenes cifrados con algoritmos antiguos (`AES-CBC 128`) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Compliance** y **Devices** > **Device query** `[Verificado MS Learn]`.
- **Rol Responsable:** Windows Platform Lead + GRC `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar la política de cumplimiento de Intune verificando versión mínima de sistema operativo exigida (Windows 11 23H2/24H2+ con nivel de parche mensual vigente), marcando como `Non-compliant` cualquier instalación residual de Windows 10 no cubierta por ESU aprobada `[Verificado MS Learn]`.
  2. Consultar métodos de cifrado reportados en la flota (`XTS-AES 256` vs. `XTS-AES 128` o `AES-CBC`) planificando recifrado gradual durante reprovisionamiento Autopilot hacia **XTS-AES 256** `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe mensual de distribución de versiones OS y algoritmos de cifrado activos en flota `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Recertificación de Permisos de Lectura BitLocker / LAPS y Configuración Tenant en Entra ID
- **Objetivo:** Auditar la configuración de privilegio mínimo sobre los secretos locales más sensibles almacenados en Microsoft Entra ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > **Devices** > **Device settings** e **Identity governance** > **Access reviews** `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Lead + Cloud Device Administrator `[Verificado MS Learn]`.
- **Procedimiento Paso a Paso:**
  1. Verificar en `Devices > Device settings` que `Enable Microsoft Entra Local Administrator Password Solution (LAPS)` esté en **Yes** y que `Restrict users from recovering the BitLocker key(s) for their owned devices` permanezca en **Yes** (`allowedToReadBitlockerKeysForOwnedDevice = false`) salvo para poblaciones explícitamente exceptuadas con Acceso Condicional estricto `[Verificado MS Learn]`.
  2. Ejecutar *Access Reviews* trimestrales sobre todo usuario y aplicación registrada en Entra ID que posea `DeviceLocalCredential.Read.All` o `microsoft.directory/bitlockerKeys/key/read`, confirmando alcance limitado a *Administrative Units* `[Verificado MS Learn]`.
  3. Auditar que ninguna aplicación de automatización utilice secretos de cliente expirables donde pueda usar certificados o *Managed Identity*, y degradar cuentas de reporte a `DeviceLocalCredential.ReadBasic.All` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/JSON de `authorizationPolicy` y cierre al 100 % de *Access Reviews* sobre permisos BitLocker y LAPS `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Simulacro de Recuperación BitLocker, Rotación Remota y **Quick Machine Recovery (QMR)**
- **Objetivo:** Validar de extremo a extremo que la organización puede recuperar endpoints bloqueados en pre-arranque o caídas masivas sin comprometer la seguridad criptográfica `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **All devices** > **Recovery keys** / **BitLocker key rotation** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Engineering + Help Desk Lead + Business Continuity `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. En equipos representativos de laboratorio, forzar entrada en recuperación BitLocker, activar PIM del rol `BitLocker Recovery Reader`, recuperar la clave de 48 dígitos, desbloquear el volumen y verificar generación inmediata de `Read BitLocker key` en `AuditLogs` `[Verificado MS Learn]`.
  2. Ejecutar `BitLocker key rotation` desde Intune y comprobar que la clave anterior quede invalidada y una nueva clave de recuperación aparezca escrowed en Entra ID `[Verificado MS Learn]`.
  3. Probar los flujos empresariales de **Quick Machine Recovery (QMR)** y *Point-in-time restore* en Windows 11 Enterprise para validar resiliencia ante incidentes de actualización o controladores defectuosos que impidan el arranque masivo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta de simulacro trimestral con tiempos de recuperación medidos y validación de rotación criptográfica `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Ejercicio Purple Team sobre Credenciales, Kernel, App Control y Acceso Físico/Pre-Boot
- **Objetivo:** Someter a prueba real las defensas nativas de Windows 11 Enterprise y las reglas de detección de Defender XDR / Sentinel `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > **Investigation & response** > **Hunting** `[Verificado MS Learn]`.
- **Rol Responsable:** Purple Team + SOC L3 + Windows Platform Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar pruebas controladas de: (a) extracción de memoria `lsass.exe` contra **Credential Guard** y **RunAsPPL** (`T1003.001`); (b) carga de driver vulnerable conocido (*BYOVD*, `T1068`) contra **HVCI** y **Microsoft Vulnerable Driver Blocklist**; (c) ejecución de binarios no firmados y scripts contra **App Control for Business** (`T1218`); y (d) intentos de elevación silenciosa contra **Administrator Protection** (`T1548.002`) `[Verificado MS Learn]`.
  2. Validar que en un equipo apagado o con sesión cerrada, tanto **BitLocker** como **Personal Data Encryption (PDE)** impidan acceso offline a archivos en `Desktop`/`Documents`/`Pictures` `[Verificado MS Learn]`.
  3. Documentar tiempos de detección en `security.microsoft.com` y cerrar cualquier brecha de visibilidad telemétrica `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe técnico Purple Team semestral mapeado a MITRE ATT&CK v18 y plan de mejora cerrado `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión Anual de Estándares de Adquisición **Secured-core PC (Pluton / UEFI 2023)** y Criptografía Post-Cuántica
- **Objetivo:** Garantizar que toda compra o renovación de hardware corporativo incorpore las máximas garantías de silicio y criptografía moderna de Windows 11 `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Comités de Arquitectura Empresarial, Compras TI e `https://intune.microsoft.com` `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO + Windows Platform Architect + IT Procurement `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Actualizar el pliego técnico obligatorio de adquisición OEM exigiendo certificación **Secured-core PC**, procesador de seguridad **Microsoft Pluton** (o TPM 2.0 certificado), **Kernel DMA Protection**, compatibilidad total con **System Guard Secure Launch** y certificados **Windows UEFI CA 2023** preinstalados de fábrica `[Verificado MS Learn]`.
  2. Evaluar la adopción de las nuevas **Post-quantum security APIs** incorporadas en Windows Enterprise (anunciadas en la hoja de ruta 2026) para aplicaciones internas de larga vida criptográfica `[Verificado MS Learn]`.
  3. Auditar las llaves maestras de recuperación de emergencia (*Data Recovery Agents [DRA]* si se emplean) y políticas de retención criptográfica `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Estándar anual de homologación de hardware firmado por el CISO y auditoría de flota Secured-core `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook de Respuesta ante Robo o Extravío Físico de Portátil Corporativo
- **Disparador:** Notificación del empleado, Seguridad Física o RR. HH. reportando sustracción o pérdida de un portátil Windows 11 corporativo `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **All devices** y `https://entra.microsoft.com` > **Users** / **Devices** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Consultar inmediatamente en Intune (`Encryption report` y detalles del objeto) y en Entra ID la última confirmación de estado **BitLocker Encrypted = Yes**, algoritmo activo (`XTS-AES`), presencia de protector **TPM + PIN** (si es activo VIP) y cobertura de **Personal Data Encryption (PDE)** `[Verificado MS Learn]`.
  2. Enviar de inmediato la acción remota **Wipe** (con opción de retener estado de enrolamiento o bloqueo completo según política forense) o **Remote Lock** / deshabilitación del dispositivo en Microsoft Entra ID `[Verificado MS Learn]`.
  3. En Microsoft Entra ID, ejecutar **Revoke sign-in sessions** sobre el usuario afectado para invalidar Primary Refresh Tokens (PRT) y deshabilitar credenciales comprometidas; revocar certificados SCEP del equipo si utiliza Cloud PKI `[Verificado MS Learn]`.
  4. **Evaluación regulatoria de brecha de datos:** Documentar con evidencia inmutable (reporte de cumplimiento BitLocker + timestamp de clave escrowed en Entra ID + política PDE) que el almacenamiento estaba cifrado íntegramente antes del extravío, insumo probatorio esencial para GRC/Legal ante normativas de notificación de brechas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Paquete probatorio PDF/JSON de cifrado previo + log de comando `Wipe` + revocación de sesiones en `AuditLogs` `[Decisión / Propuesta Editorial]`.

### AH-02: Playbook de Rotación de Emergencia por Exposición de Clave BitLocker o Contraseña Windows LAPS
- **Disparador:** Entrega de una clave BitLocker o contraseña LAPS durante soporte de emergencia, sospecha de compromiso de cuenta de un operador Help Desk o detección de lectura anómala en `AuditLogs` `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **All devices** > `[Dispositivo]` > **BitLocker key rotation** / **Rotate local admin password** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Si el disparador es actividad anómala de un administrador, revocar al instante su sesión activa y asignaciones PIM en Microsoft Entra ID `[Verificado MS Learn]`.
  2. Identificar mediante consulta KQL en `AuditLogs` el listado exacto de dispositivos cuyas claves BitLocker (`Read BitLocker key`) o contraseñas LAPS (`Recover device local administrator password`) fueron leídas durante la ventana de compromiso `[Verificado MS Learn]`.
  3. Disparar sobre cada equipo afectado la acción remota **BitLocker key rotation** en Intune y la rotación de contraseña **Windows LAPS** (o `Reset-LapsPassword` vía Live Response / script remediación, cuidando no exceder umbrales de *throttling* de Entra ID) `[Verificado MS Learn]`.
  4. Verificar que todos los equipos registren una nueva clave/contraseña con fecha posterior al incidente (`Event ID 10029` para LAPS y nuevo `Key ID` BitLocker en Entra ID) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Lista de dispositivos impactados conciliada al 100 % con nuevos identificadores/timestamps de secretos rotados `[Verificado MS Learn]`.

### AH-03: Playbook de Remediación ante Fallo de Actualización `Windows UEFI CA 2023` o Bucle de Recuperación BitLocker
- **Disparador:** Aparición de **Event ID 1795**, `UEFICA2023Error` distinto de cero, `AvailableUpdates` bloqueado en `0x4104` o solicitud inesperada de clave BitLocker tras actualización de firmware/arranque `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Windows quality updates** > **Secure Boot status** y **Devices** > **All devices** > **Recovery keys** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Detener inmediatamente el despliegue de `Enable SecureBoot Certificate Updates` hacia nuevos dispositivos del mismo modelo de placa base (`System board model` en *Secure Boot status report*) `[Verificado MS Learn]`.
  2. Si el usuario se encuentra en pantalla azul de recuperación BitLocker, validar su identidad, proporcionarle la clave de recuperación escrowed en Entra ID para completar el arranque y rotar la clave posteriormente `[Verificado MS Learn]`.
  3. En equipos con **Event ID 1795** o bloqueo en `0x4104` (error al inyectar KEK/DB en NVRAM UEFI), obtener y desplegar la actualización oficial de BIOS/UEFI del OEM (suspendiendo BitLocker por 1 reinicio durante el flasheo UEFI si el instalador del fabricante no lo gestiona automáticamente) `[Verificado MS Learn]`.
  4. Una vez actualizado el firmware, reanudar el despliegue de certificados 2023 y confirmar `UEFICA2023Status == "Updated"` y **Event ID 1808** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Confirmación de versión BIOS corregida, `UEFICA2023Status = Updated` y cierre de alerta en Autopatch `[Verificado MS Learn]`.

### AH-04: Playbook de Contención Inmediata de Driver Vulnerable (*BYOVD*) o Binario 0-Day con **App Control for Business**
- **Disparador:** Inteligencia de amenazas o incidente activo del SOC detectando uso de un driver firmado vulnerable no incluido aún en la lista estándar o un binario malicioso propagándose en la red `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **App Control for Business** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Capturar el hash SHA-256, atributos de archivo y huella del certificado firmante del driver `.sys` o ejecutable malicioso desde Microsoft Defender XDR `[Verificado MS Learn]`.
  2. Construir una actualización de política con reglas explícitas `Deny` en **App Control for Business** (aplicando a modo kernel y modo usuario según corresponda) `[Verificado MS Learn]`.
  3. Desplegar con prioridad de emergencia sobre toda la flota gestionada y forzar sincronización MDM, verificando en `DeviceEvents` la transición inmediata a eventos de bloqueo (`3077`) en cualquier intento ulterior de ejecución `[Verificado MS Learn]`.
- **Evidencia Auditable:** Política `.cip` de bloqueo desplegada y registros de bloqueo efectivo en Defender XDR `[Verificado MS Learn]`.

### AH-05: Playbook de Reversión Controlada ante Fallo Crítico por **Administrator Protection** o **HVCI**
- **Disparador:** Bloqueo operativo severo en aplicaciones críticas que requieren acceso cruzado entre perfiles o aparición del error de inicio de sesión remoto RDP `0xC000000D` tras activar *Administrator Protection* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Configuration** (Settings Catalog > `Local Policies Security Options`) `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Verificar primero si el equipo afectado cuenta con la actualización acumulativa correctiva (`KB5124010` o posterior) que resuelve incidencias conocidas de iconos del menú Inicio y extensiones Edge bajo *Administrator Protection* `[Verificado MS Learn]`.
  2. Si se trata del fallo documentado de RDP no-administrativo (`0xC000000D`) o de un entorno no soportado (Cloud PC, AVD, host LAPS), mover el dispositivo al grupo de exclusión y revertir la política `User Account Control: Configure type of Admin Approval Mode` a `Legacy Admin Approval Mode (Default)` vía Intune `[Verificado MS Learn]`.
  3. Ejecutar reinicio controlado del endpoint (obligatorio para que el cambio de *Administrator Protection* surta efecto) y migrar al usuario al modelo estándar sin admin local gobernado por **Intune EPM** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Ticket de cambio de emergencia con fecha de expiración de excepción y verificación post-reinicio `[Decisión / Propuesta Editorial]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Microsoft Graph y PowerShell Operativo

#### Consulta 1 — Microsoft Sentinel / Entra `AuditLogs` (KQL): Auditoría de Lecturas de Claves BitLocker y Contraseñas Windows LAPS
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` / Log Analytics (`AuditLogs`) `[Verificado MS Learn]`.
- **Propósito:** Detectar toda recuperación de claves BitLocker (`Read BitLocker key`) o contraseñas de administrador local Windows LAPS en el tenant, alertando picos de consultas por un mismo operador `[Verificado MS Learn]`.
```kql
// Auditoria unificada de lectura de secretos locales (BitLocker + Windows LAPS) en Microsoft Entra ID
AuditLogs
| where TimeGenerated > ago(7d)
| where Category == "KeyManagement" and OperationName has "BitLocker"
   or OperationName has_any ("Recover device local administrator password", "Update device local administrator password")
| extend ActorUPN = tostring(InitiatedBy.user.userPrincipalName),
         ActorApp = tostring(InitiatedBy.app.displayName),
         ActorIP  = tostring(InitiatedBy.user.ipAddress),
         TargetDevice = tostring(TargetResources[0].displayName)
| project TimeGenerated, Category, OperationName, Result, ActorUPN, ActorApp, ActorIP, TargetDevice, CorrelationId
| order by TimeGenerated desc
```

#### Consulta 2 — Microsoft Defender XDR Advanced Hunting (KQL): Eventos de Integridad de Código **App Control for Business** y Drivers Bloqueados
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` (`DeviceEvents`) `[Verificado MS Learn]`.
- **Propósito:** Monitorear ejecuciones bloqueadas o auditadas por políticas de **App Control for Business** y la lista de bloqueo de drivers vulnerables de Microsoft `[Verificado MS Learn]`.
```kql
// Monitoreo de bloqueos y auditorias de App Control for Business (antes WDAC) y drivers en kernel
DeviceEvents
| where Timestamp > ago(7d)
| where ActionType in ("AppControlCodeIntegrityPolicyBlocked", "AppControlCodeIntegrityPolicyAudited",
                       "AppControlCIScriptBlocked", "AppControlCIScriptAudited")
| project Timestamp, DeviceName, ActionType, FileName, FolderPath, SHA256, InitiatingProcessFileName, InitiatingProcessAccountName, AdditionalFields
| summarize EventsCount = count(), AffectedDevices = dcount(DeviceName) by ActionType, FileName, FolderPath, SHA256
| order by EventsCount desc
```

#### Consulta 3 — Microsoft Defender XDR Advanced Hunting (KQL): Detección de Intentos de Volcado o Acceso a Memoria `lsass.exe` (`RunAsPPL` / Credential Guard)
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` (`DeviceEvents` / `DeviceProcessEvents`) `[Verificado MS Learn]`.
- **Propósito:** Cazar herramientas de robo de credenciales (`T1003.001`) bloqueadas o detectadas al interactuar con `lsass.exe` protegido por **LSA Protection** y **Credential Guard** `[Verificado MS Learn]`.
```kql
// Caza de intentos sospechosos de apertura o volcado sobre LSASS.exe
DeviceEvents
| where Timestamp > ago(7d)
| where FileName =~ "lsass.exe" or ActionType has_any ("Lsass", "CredentialGuard", "ProtectedProcess")
| where InitiatingProcessFileName !in~ ("MsMpEng.exe", "SenseIR.exe", "MsSense.exe", "csrss.exe", "wininit.exe", "svchost.exe", "werfault.exe")
| project Timestamp, DeviceName, ActionType, InitiatingProcessAccountName, InitiatingProcessFileName, InitiatingProcessFolderPath, InitiatingProcessCommandLine, InitiatingProcessSHA256
| order by Timestamp desc
```

#### Consulta 4 — Intune Multi-Device `Device query` / PowerShell Inventario: Verificación de Transición **Windows UEFI CA 2023** (`UEFICA2023Status` y Eventos `1808`/`1801`/`1795`)
- **Plataforma / Ruta:** Script de remediación/diagnóstico PowerShell en Intune o sesión remota sobre endpoints Windows 11 `[Verificado MS Learn]`.
- **Propósito:** Auditar localmente en registro y visor de eventos el estado exacto de migración hacia los certificados **Windows UEFI CA 2023** antes/después del vencimiento de junio de 2026 `[Verificado MS Learn]`.
```powershell
# Verificacion oficial del estado de actualizacion de certificados Secure Boot 2023
$sbServicing = Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot\Servicing' -ErrorAction SilentlyContinue
$sbRoot      = Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecureBoot' -ErrorAction SilentlyContinue
$sbEvents    = Get-WinEvent -FilterHashtable @{LogName='System'; Id=1808,1801,1795} -MaxEvents 5 -ErrorAction SilentlyContinue

[PSCustomObject]@{
    SecureBootEnabled  = Confirm-SecureBootUEFI -ErrorAction SilentlyContinue
    UEFICA2023Status   = $sbServicing.UEFICA2023Status
    UEFICA2023Error    = $sbServicing.UEFICA2023Error
    AvailableUpdates   = ('0x{0:X4}' -f $sbRoot.AvailableUpdates)
    LastSecureBootEvt  = ($sbEvents | Select-Object -First 1 -ExpandProperty Id)
}
```

#### Consulta 5 — Microsoft Graph PowerShell: Verificación de Restricción de Auto-Lectura BitLocker y Auditoría Básica Sin Secretos de **Windows LAPS**
- **Plataforma / Ruta:** Microsoft Graph PowerShell SDK (`Policy.Read.All`, `DeviceLocalCredential.ReadBasic.All`, `BitlockerKey.ReadBasic.All`) `[Verificado MS Learn]`.
- **Propósito:** Comprobar que los usuarios estándar tengan bloqueada la auto-recuperación de claves BitLocker (`allowedToReadBitlockerKeysForOwnedDevice == false`) y auditar metadatos de rotación LAPS sin exponer contraseñas en claro `[Verificado MS Learn]`.
```powershell
Connect-MgGraph -Scopes "Policy.Read.All", "Device.Read.All", "DeviceLocalCredential.ReadBasic.All", "BitlockerKey.ReadBasic.All"

# 1. Auditar politica global del tenant sobre auto-lectura de claves BitLocker por propietarios no-admin
$authPolicy = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/policies/authorizationPolicy"
$authPolicy.defaultUserRolePermissions | Select-Object allowedToReadBitlockerKeysForOwnedDevice

# 2. Auditar metadatos de respaldo Windows LAPS (sin leer contrasenas en texto claro)
$lapsMeta = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/directory/deviceLocalCredentials?`$select=id,deviceName,lastBackupDateTime,refreshDateTime"
$lapsMeta.value | Select-Object deviceName, lastBackupDateTime, refreshDateTime
```

#### Consulta 6 — Microsoft Defender Vulnerability Management Advanced Hunting (KQL): Brechas de Configuración en BitLocker, Secure Boot y VBS/HVCI
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` (`DeviceTvmSecureConfigurationAssessment`) `[Verificado MS Learn]`.
- **Propósito:** Obtener en una sola consulta KQL todos los endpoints corporativos que incumplen controles críticos de hardware y cifrado en Windows 11 `[Verificado MS Learn]`.
```kql
// Evaluacion continua de postura en Defender Vulnerability Management sobre controles Windows 11
DeviceTvmSecureConfigurationAssessment
| where IsApplicable == 1 and IsCompliant == 0
| where ConfigurationId has_any ("bitlocker", "secureboot", "credentialguard", "hvci", "lsa", "laps", "firewall")
   or ConfigurationSubcategory in ("Encryption", "Hardware Security", "Credential Protection", "Application Control")
| summarize NonCompliantDevices = dcount(DeviceId) by ConfigurationId, ConfigurationSubcategory
| order by NonCompliantDevices desc
```

#### Consulta 7 — Trazado Local ETW y Diagnóstico de **Administrator Protection** (`Microsoft-Windows-LUA` Eventos `15031` y `15032`)
- **Plataforma / Ruta:** Consola administrativa / script diagnóstico en Windows 11 24H2/25H2+ con `KB5120998` `[Verificado MS Learn]`.
- **Propósito:** Capturar eventos de elevación aprobada (`15031`) o rechazada/expirada (`15032`) generados por el token aislado de **Administrator Protection** `[Verificado MS Learn]`.
```powershell
# Iniciar sesion de trazado ETW sobre el proveedor oficial Microsoft-Windows-LUA ({93c05d69-51a3-485e-877f-1806a8731346})
logman start AdminProtectionTrace -p "{93c05d69-51a3-485e-877f-1806a8731346}" -o "C:\ProgramData\Microsoft\AdminProtectionTrace.etl" -ets

# Tras reproducir o auditar elevaciones, detener la sesion y filtrar Event IDs 15031 (Approved) y 15032 (Denied/Fail)
logman stop AdminProtectionTrace -ets
Get-WinEvent -Path "C:\ProgramData\Microsoft\AdminProtectionTrace.etl" -Oldest | Where-Object { $_.Id -in 15031, 15032 } | Select-Object TimeCreated, Id, Message
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Control de Plataforma Windows 11 | Indicador Técnico de *Proof of Life* | Comando / Ruta de Verificación Rápida | Estado Esperado en Producción |
| :--- | :--- | :--- | :--- |
| **BitLocker Drive Encryption** | `Conversion Status: Fully Encrypted` (o *Used Space Only* en S0), método `XTS-AES 256` y clave escrowed en Entra ID (< 200 claves/equipo) `[Verificado MS Learn]`. | `manage-bde -status c:` e `Intune > Devices > Monitor > Encryption report` `[Verificado MS Learn]`. | `Protection Status: Protection On`, clave respaldada en Entra y `allowedToReadBitlockerKeysForOwnedDevice = false` `[Verificado MS Learn]`. |
| **UEFI Secure Boot (`2023 CAs`)** | `Confirm-SecureBootUEFI == True`, `UEFICA2023Status == "Updated"`, ausencia de `UEFICA2023Error` y **Event ID 1808** `[Verificado MS Learn]`. | `Intune > Reports > Windows quality updates > Secure Boot status` `[Verificado MS Learn]`. | 100 % de equipos compatibles actualizados a `Windows UEFI CA 2023` sin errores `1795`/`1801` `[Verificado MS Learn]`. |
| **Secured-core, VBS, HVCI y Credential Guard** | `VirtualizationBasedSecurityStatus = 2` (Running) con `SecurityServicesRunning` incluyendo Credential Guard (`1`) y HVCI (`2`) `[Verificado MS Learn]`. | `Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard` `[Verificado MS Learn]`. | VBS, HVCI, Kernel Stack Protection y Credential Guard en ejecución activa `[Verificado MS Learn]`. |
| **LSA Protection (`RunAsPPL`)** | Proceso `lsass.exe` ejecutándose como *Protected Process Light* (**Event ID 12** en `Microsoft-Windows-Wininit`) `[Verificado MS Learn]`. | Visor de eventos `Wininit` y `Defender Vulnerability Management` `[Verificado MS Learn]`. | `RunAsPPL` activo bloqueando inyección de código no firmado y volcados LSASS `[Verificado MS Learn]`. |
| **Windows LAPS (Entra ID + 24H2 AAM)** | Binarios `laps.dll`/`lapscsp.dll` procesando cada hora, **Event ID 10029** en `Microsoft-Windows-LAPS/Operational` y `refreshDateTime` futura `[Verificado MS Learn]`. | `Get-LapsAADPassword` (metadatos) y `Endpoint security > Account protection` `[Verificado MS Learn]`. | Respaldo cifrado activo en Entra ID, cuenta aleatorizada (24H2+) y rotación automática post-uso `[Verificado MS Learn]`. |
| **WHfB + Personal Data Encryption (PDE)** | Estado `NgcPrerequisiteCheck = Pass` en `dsregcmd /status` y carpetas `Desktop`/`Documents`/`Pictures` protegidas por PDE `[Verificado MS Learn]`. | `dsregcmd /status` e `Intune > Endpoint security > Disk encryption (PDE)` `[Verificado MS Learn]`. | *Cloud Kerberos Trust* operativo, *Passwordless experience* activo y claves PDE descartadas al cerrar sesión `[Verificado MS Learn]`. |
| **App Control, Administrator Protection y Firewall** | Políticas `.cip` cargadas en `C:\Windows\System32\CodeIntegrity\CiPolicies\Active`, perfiles Firewall `On` y exclusiones Cloud PC/AVD respetadas `[Verificado MS Learn]`. | `citool.exe -lp` (en 22H2+) e `Intune > Endpoint security > Firewall` `[Verificado MS Learn]`. | Políticas Base + Supplemental activas, *Vulnerable Driver Blocklist* activa y cero equipos con Firewall apagado `[Verificado MS Learn]`. |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales (`KPI-01` a `KPI-08`)

> Todos los umbrales porcentuales, tiempos de rotación y metas operativas siguientes constituyen criterios consultivos de excelencia operacional `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Cobertura Efectiva de Cifrado BitLocker con Clave Escrowed en Entra ID** | `(Endpoints Windows corporativos cifrados con BitLocker + clave activa en Entra ID / Total endpoints Windows activos) * 100` | `>= 99,5 %` | Semanal | CISO / Endpoint Security Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tasa de Transición Completada a Certificados `Windows UEFI CA 2023`** | `(Endpoints Windows con UEFICA2023Status == 'Updated' y Event ID 1808 / Total endpoints Windows con Secure Boot) * 100` | `>= 98 %` (100 % en hardware 2024+) | Semanal | Windows Platform Architect / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Cumplimiento de Aislamiento VBS, HVCI y Credential Guard Activos** | `(Endpoints Windows 11 con VBS + HVCI + Credential Guard en estado Running / Total endpoints Windows 11) * 100` | `>= 97 %` | Semanal | Endpoint Security Engineer / SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Salud de Respaldo y Rotación Vigente en Windows LAPS (Entra ID)** | `(Endpoints Windows con respaldo LAPS exitoso en Entra ID y expiración <= 30 días / Total endpoints en alcance LAPS) * 100` | `>= 99 %` | Semanal | Identity Security Lead / Internal Audit | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo de Rotación Post-Exposición de Claves BitLocker / Contraseñas LAPS** | `Tiempo transcurrido entre evento 'Read BitLocker key' o 'Recover LAPS password' y confirmación de nuevo secreto en Entra ID` | `<= 4 horas` | Diaria | SOC Manager / Help Desk Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Adopción de Inicio de Sesión Sin Contraseña (WHfB + Passwordless Experience)** | `(Inicios de sesión interactivos en Windows 11 autenticados con WHfB o FIDO2 / Total inicios de sesión interactivos) * 100` | `>= 92 %` | Mensual | Identity Architect / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Cobertura de Políticas **App Control for Business** en Modo *Enforced*** | `(Endpoints Windows gobernados por política App Control for Business en modo Enforced / Total endpoints Windows corporativos) * 100` | `>= 90 %` (`100 %` con Vulnerable Driver Blocklist) | Mensual | Endpoint Security Lead / SOC L3 | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Tasa de Endpoints con Perfiles de Windows Firewall Íntegramente Activos** | `(Endpoints Windows con perfiles Domain, Private y Public activos / Total endpoints Windows gestionados en Intune) * 100` | `>= 99,8 %` | Diaria / Semanal | Network Security Lead / SOC L1 | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de 5 Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Verificables |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Reactivo** | Cifrado BitLocker inconsistente o con claves guardadas localmente; usuarios estándar pueden leer sus claves BitLocker en el portal web; cuentas de administrador local con contraseña idéntica o LAPS heredado sin respaldo en Entra ID; presencia residual de Windows 10 post-EOS; certificados Secure Boot 2011 sin inventariar. |
| **Nivel 2** | **Básico / Gestionado** | Silent BitLocker desplegado desde Intune con escrow en Entra ID; Windows Firewall activo por política; VBS y Credential Guard en configuración predeterminada del OS pero sin monitoreo de desviaciones; inicio de inventario del *Secure Boot status report*. |
| **Nivel 3** | **Definido / Endurecido** | Flota 100 % en Windows 11 Enterprise 24H2/25H2+; auto-lectura BitLocker restringida (`allowedToReadBitlockerKeysForOwnedDevice = false`) con RBAC por Administrative Units; Windows LAPS nativo respaldado en Entra ID con rotación post-uso; WHfB con *Cloud Kerberos Trust* desplegado; despliegue por anillos de **Windows UEFI CA 2023** avanzado; *App Control for Business* en modo *Audit* + lista de bloqueo de drivers vulnerables *Enforced*. |
| **Nivel 4** | **Gestionado Cuantitativamente** | `UEFICA2023Status = Updated` >= 98 %; **Personal Data Encryption (PDE)** activo en carpetas conocidas para roles sensibles con hibernación y memory dumps deshabilitados; **Windows LAPS Automatic Account Management** con nombres aleatorizados; **App Control for Business** en modo *Enforced* con Managed Installer e ISG; alertas SIEM correlacionando cada lectura de clave BitLocker/LAPS. |
| **Nivel 5** | **Optimizado / Silicio Zero Trust** | Renovación de parque 100 % **Secured-core PC con Microsoft Pluton** y certificados UEFI 2023 de fábrica; experiencia **100 % Passwordless** (`EnablePasswordlessExperience` activo); **Administrator Protection** aplicado selectivamente en perfiles técnicos junto con Intune EPM en usuarios estándar; simulacros trimestrales con **Quick Machine Recovery (QMR)** y validación Purple Team semestral. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

El mapeo siguiente cubre íntegramente las **6 funciones de NIST CSF 2.0 (CSWP 29)** enlazando controles verificados de Windows 11 Enterprise con artefactos de auditoría reproducibles `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Subcategoría Oficial | Descripción del Resultado (CSWP 29) | Capacidad Habilitadora en Windows 11 Enterprise + MITRE ATT&CK | Evidencia Auditable Reproducible |
| :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OV-01` | Los resultados de la estrategia de gestión de riesgos de ciberseguridad se revisan para informar y ajustar políticas. | Conciliación mensual contra **Windows 11 Security Baselines (24H2 / 25H2 / 26H2)** en Intune y seguimiento ejecutivo de cobertura criptográfica y de silicio `[Verificado MS Learn]`. | Reporte mensual de desviaciones del *Security Baseline* y tablero ejecutivo de `KPI-01` a `KPI-08` `[Decisión / Propuesta Editorial]`. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades se establecen, comunican y aplican. | Bloqueo tenant-wide de auto-lectura de claves BitLocker (`allowedToReadBitlockerKeysForOwnedDevice = false`) y segregación en Entra RBAC + Administrative Units entre `DeviceLocalCredential.ReadBasic.All` y `Read.All` (`T1078`) `[Verificado MS Learn]`. | Salida JSON de `authorizationPolicy`, definiciones de roles custom Entra y cierre trimestral de *Access Reviews* `[Verificado MS Learn]`. |
| **IDENTIFY (ID)** | `ID.AM-01` | Se mantienen inventarios de hardware y firmware gestionados por la organización. | Inventario detallado de fabricantes/placas base, versión TPM 2.0 / Pluton y estado de certificados UEFI 2011 vs. **2023** mediante el **Secure Boot status report** de Windows Autopatch `[Verificado MS Learn]`. | Exportación del *Secure Boot status report* con columnas opcionales de modelo de placa y versión de firmware `[Verificado MS Learn]`. |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican, validan y registran las vulnerabilidades y brechas de configuración en los activos. | Evaluación continua en **Microsoft Defender Vulnerability Management** (`DeviceTvmSecureConfigurationAssessment`) sobre BIOS, Secure Boot, VBS, HVCI, Credential Guard, BitLocker y LAPS `[Verificado MS Learn]`. | Consulta KQL reproducible sobre `DeviceTvmSecureConfigurationAssessment` y plan de cierre mensual `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.DS-01` | Se protege la confidencialidad, integridad y disponibilidad de los datos en reposo. | Cifrado de volumen **BitLocker XTS-AES 256** (con TPM 2.0 / PIN pre-boot y **BitLocker To Go**) combinado con **Personal Data Encryption (PDE) for Known Folders** vinculado a Windows Hello (`T1005`, `T1052`) `[Verificado MS Learn]`. | `Encryption report` de Intune, claves escrowed en Entra ID y perfil activo de *Personal Data Encryption* + bloqueo de dumps/hibernación `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.AA-03` | Los usuarios, servicios y hardware son autenticados de manera robusta. | **Windows Hello for Business** con claves respaldadas en TPM 2.0, **Cloud Kerberos Trust**, **Web Sign-in** con TAP, **Enable passwordless experience** y atestación de salud **System Guard** (`T1556`, `T1110`) `[Verificado MS Learn]`. | Políticas `Account protection` activas y métricas de inicios de sesión sin contraseña en Entra `SigninLogs` `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso y credenciales privilegiadas locales incorporan mínimo privilegio y rotación continua. | **Windows LAPS** con respaldo cifrado en Entra ID, *Automatic Account Management* (nombres aleatorizados en 24H2+), *Post-authentication actions* y elevación JIT con token aislado en **Administrator Protection** (`T1078.003`, `T1548.002`) `[Verificado MS Learn]`. | Eventos `10029` de LAPS, metadatos `deviceLocalCredentials` en Graph y política de *Administrator Protection* con exclusiones verificadas `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.PS-01` | Se establecen y aplican prácticas de gestión de configuración y control de ejecución. | **App Control for Business** (políticas Base + Supplemental, Managed Installer, ISG y *Microsoft Vulnerable Driver Blocklist*), **VBS / HVCI**, **Credential Guard** y **LSA Protection (`RunAsPPL`)** (`T1003.001`, `T1068`, `T1218`) `[Verificado MS Learn]`. | Políticas `.cip` desplegadas en `Endpoint security > App Control for Business` y estado `Win32_DeviceGuard` en ejecución `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.PS-02` | El software y firmware se mantienen y actualizan acorde al riesgo. | Renovación controlada hacia **Windows UEFI CA 2023** (`EnableSecurebootCertificateUpdates = 22852` / `0x5944`) y actualizaciones previas de firmware OEM antes/después del vencimiento de junio de 2026 (`T1542.003`) `[Verificado MS Learn]`. | Registros `UEFICA2023Status = Updated` y **Event ID 1808** en System Event Log `[Verificado MS Learn]`. |
| **DETECT (DE)** | `DE.CM-03` | Se monitorean accesos a credenciales, elevaciones y desactivaciones de defensas para detectar eventos adversos. | Correlación KQL de `AuditLogs` (`Read BitLocker key`, `Recover device local administrator password`), bloqueos de `lsass.exe` / App Control en `DeviceEvents`, trazas `15031`/`15032` de *Administrator Protection* y reporte de **Windows Firewall** apagado `[Verificado MS Learn]`. | Reglas de detección activas en Microsoft Defender XDR / Sentinel y reportes diarios conciliados `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.MI-02` | Los incidentes se erradican y mitigan revocando secretos expuestos y bloqueando artefactos maliciosos. | Rotación remota inmediata `BitLocker key rotation`, reseteo forzado `Reset-LapsPassword`, comando `Wipe` ante robo físico y bloqueo de emergencia de drivers/binarios en **App Control for Business** `[Verificado MS Learn]`. | Logs de rotación post-exposición en Entra/Intune y políticas suplementarias `Deny` aplicadas `[Verificado MS Learn]`. |
| **RECOVER (RC)** | `RC.RP-03` | La integridad de los activos de restauración y arranque se verifica durante la recuperación operativa. | Desbloqueo controlado con claves de recuperación BitLocker auditadas, remediación de fallos UEFI `1795`/`0x4104` y recuperación a escala con **Quick Machine Recovery (QMR)** y *Point-in-time restore* `[Verificado MS Learn]`. | Actas de simulacros trimestrales de recuperación BitLocker/QMR y verificación de re-cifrado posterior `[Decisión / Propuesta Editorial]`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta de Formación Oficial Microsoft Learn | Comunidad Técnica / Empleados Microsoft y MVPs | Certificación Vigente (Nov 2026) |
| :--- | :--- | :--- | :--- |
| **Windows Platform & Security Architect** | *Windows 11 Security Book* en Microsoft Learn (Silicon-assisted security, Advanced credential protection, Application and driver control, PDE) y *Secure Boot playbook for certificates expiring in 2026* `[Verificado MS Learn]`. | Michael Niehaus (*Out of Office Hours — BitLocker 24H2 & Secure Boot*), Rudy Ooms (*Call4Cloud — TPM Attestation & LAPS PAA*) `[Verificado MS Learn]`. | **Microsoft Certified: Cybersecurity Architect Expert (SC-100)** + **MD-102** `[Verificado MS Learn]`. |
| **Endpoint Security Engineer (Intune)** | Rutas Learn de *Encrypt Windows devices with BitLocker & PDE using Intune*, *Deploy App Control for Business policies using MDM* y *Manage Firewall with Endpoint Security* `[Verificado MS Learn]`. | Peter van der Woude (*All about Microsoft Intune*) y Joery Van den Bosch (*IntuneStuff — Windows LAPS & Intune*) `[Verificado MS Learn]`. | **Microsoft 365 Certified: Endpoint Administrator Associate (MD-102)** `[Verificado MS Learn]`. |
| **Identity & Access Engineer** | Guías oficiales de *Windows Hello for Business Cloud Kerberos Trust*, *Passwordless experience* y *Windows LAPS with Microsoft Entra ID* `[Verificado MS Learn]`. | Documentación de ingeniería de Microsoft Entra ID y comunidad MVP de identidad `[Verificado MS Learn]`. | **Microsoft Certified: Identity and Access Administrator Associate (SC-300)** `[Verificado MS Learn]`. |
| **SOC L2 / L3 & Threat Hunter** | Caza avanzada en Microsoft Defender XDR sobre `DeviceEvents`, `DeviceTvmSecureConfigurationAssessment` y auditoría `KeyManagement` en Microsoft Sentinel `[Verificado MS Learn]`. | Investigación MSRC / Microsoft Threat Intelligence sobre *bootkits* UEFI (`CVE-2023-24932`) y *BYOVD* `[Verificado MS Learn]`. | **Microsoft Certified: Security Operations Analyst Associate (SC-200)** `[Verificado MS Learn]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Verificaciones Técnicas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Verificada | Hallazgo Técnico Oficial a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **Expiración de certificados UEFI Secure Boot 2011 en junio de 2026 y migración a `Windows UEFI CA 2023`** | Confirmado en Microsoft Learn (*Update Secure Boot Certificates for Windows Devices*, actualizado may-2026) y *Windows IT Pro Blog*: los certificados de 2011 expiran desde **junio de 2026**. Se verificó el CSP `EnableSecurebootCertificateUpdates = 22852` (`AvailableUpdates = 0x5944`), WinCS (`F33E0C8E002`), clave `UEFICA2023Status == "Updated"`, **Secure Boot status report** en Windows Autopatch y eventos `1808` (éxito), `1801` (pendiente) y `1795` / `0x4104` (error de firmware/KEK) `[Verificado MS Learn]`. | Convertido en cadencia diaria `D-03`, semanal `S-01`, consulta PowerShell #4 y playbook de contingencia `AH-03`. |
| **2** | **Administrator Protection en Windows 11 (`KB5120998` y Baselines Oct-2026)** | Confirmado en Learn (actualizado **13 de octubre de 2026**): disponible vía `KB5120998` y **habilitado por defecto con la actualización de seguridad de octubre de 2026 en los Security Baselines de Windows 11 26H2, 25H2 y 24H2**. Usa cuenta oculta separada por perfil con autorización Windows Hello, eventos ETW `15031`/`15032` en `Microsoft-Windows-LUA` y **no está soportado** en Cloud PCs, AVD session hosts ni hosts gestionados con LAPS (además de incidencia RDP `0xC000000D` post-`KB5124010`) `[Verificado MS Learn]`. | Incorporado con sus exclusiones obligatorias en Sección 3.2.4, `S-05`, `M-01`, consulta #7 y playbook de reversión `AH-05`. |
| **3** | **Renombre oficial de WDAC a *App Control for Business* y regla de activación con HVCI** | Microsoft consolidó oficialmente el nombre **App Control for Business** en Learn e Intune, documentando una advertencia crítica: en sistemas con *Memory Integrity (HVCI)* activo, las **nuevas políticas Base firmadas** deben desplegarse por script y activarse con reinicio del sistema (no por push MDM directo sin reinicio) `[Verificado MS Learn]`. | Reflejado en terminología canónica de todo el módulo y en el procedimiento semanal `S-03`. |
| **4** | **BitLocker en Windows 11 24H2+, límite de 200 claves en Entra ID y suspensión por borrado en Intune** | Se verificó: (a) eliminación de requisitos Modern Standby/HSTI y DMA para auto-cifrado OOBE en Windows 11 24H2; (b) límite de **200 claves BitLocker por dispositivo** en Entra ID; (c) limitación de *Settings Catalog* para Silent BitLocker (usar `Endpoint security > Disk encryption`); y (d) que borrar un objeto en Intune remueve protectores del volumen OS dejando BitLocker suspendido `[Verificado MS Learn]`. | Incorporado en Sección 3.2.1, `D-01` y `S-04`. |
| **5** | **Personal Data Encryption (PDE) for Known Folders y endurecimiento de memoria** | En Windows 11 24H2+, **PDE for Known Folders** cifra `Desktop`, `Documents` y `Pictures` vinculando claves a Windows Hello for Business; Learn recomienda explícitamente deshabilitar volcados kernel/live/user y la hibernación para proteger claves PDE en RAM `[Verificado MS Learn]`. | Documentado en `D-08` y auditoría mensual `M-02`. |
| **6** | **Windows LAPS Automatic Account Management en Windows 11 24H2+** | Confirmado soporte exclusivo en Windows 11 24H2+ / Server 2025+ para `AutomaticAccountManagementEnabled` y `AutomaticAccountManagementRandomizeName` (prefijo <= 14 caracteres + sufijo aleatorio de 6 dígitos en cada rotación) y valores predeterminados (`PostAuthenticationActions = 3`, `PasswordAgeDays = 30`) `[Verificado MS Learn]`. | Integrado en Sección 3.2.3 y revisión mensual `M-04`. |
| **7** | **Fin de soporte de Windows 10 (14-oct-2025) y Windows Resiliency Initiative (QMR)** | Confirmado EOS de Windows 10 el **14 de octubre de 2025** e inclusión en Windows Enterprise E3/E5 de **Quick Machine Recovery (QMR)**, *Cloud rebuild*, *Point-in-time restore* y *Post-quantum security APIs* `[Verificado MS Learn]`. | Incorporado en Sección 2, `M-05` y simulacro trimestral `T-02`. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Definido | Tipo | Justificación Arquitectónica y Operativa |
| :--- | :--- | :--- | :--- |
| **1** | **Activación de `Restrict users from recovering the BitLocker key(s) for their owned devices = Yes` por defecto corporativo** | `Propuesta Editorial` | En Entra ID el valor predeterminado es `No` (permitiendo auto-servicio). En entornos Zero Trust E5 donde los usuarios son estándar (sin admin local), impedir que el usuario obtenga su clave de recuperación evita acceso offline al volumen para alterar el sistema operativo o extraer datos `[Decisión / Propuesta Editorial]`. |
| **2** | **Posicionamiento complementario: Standard User + Intune EPM para flota general vs. *Administrator Protection* para excepciones técnicas** | `Propuesta Editorial` | Aunque *Administrator Protection* endurece cuentas con rol de administrador local, mantener a la población general como usuario estándar gobernado por EPM (y usar Windows LAPS en la cuenta local de emergencia de forma segregada) ofrece menor superficie de ataque y evita las incompatibilidades documentadas con LAPS, Cloud PC y AVD `[Decisión / Propuesta Editorial]`. |
| **3** | **Estandarización en XTS-AES 256 bits para unidades OS/fijas y reducción de `PostAuthenticationResetDelay` de LAPS a 4–8 horas** | `Propuesta Editorial` | Mientras los valores predeterminados admiten XTS-AES 128 y 24 horas de retardo en LAPS, exigir XTS-AES 256 en despliegues nuevos y acotar la ventana post-uso de LAPS a 4–8 h minimiza exposición criptográfica y de credenciales sin afectar soporte `[Decisión / Propuesta Editorial]`. |
| **4** | **Umbrales de `KPI-01` a `KPI-08` (ej. rotación post-exposición `<= 4 h`, cobertura BitLocker `>= 99,5 %`) y ventanas PIM (1 h a 4 h)** | `Propuesta Editorial` | Metas cuantitativas de nivel bancario/reguladas diseñadas para convertir capacidades técnicas de Windows 11 Enterprise en SLAs auditables por el SOC y GRC `[Decisión / Propuesta Editorial]`. |
| **5** | **Modelo de madurez de 5 niveles y mapeo probatorio sobre las 6 funciones de NIST CSF 2.0** | `Propuesta Editorial` | Marco estructurado para guiar la transición desde cifrado básico hacia estaciones *Secured-core PC* con Pluton, *Passwordless* total y resiliencia QMR `[Decisión / Propuesta Editorial]`. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Encrypt Windows devices with BitLocker and Personal Data Encryption using Intune*: `https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/encrypt-bitlocker-windows` `[Verificado MS Learn]`
- **REF-02:** Microsoft Learn — *Disk encryption policy for endpoint security in Microsoft Intune*: `https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/disk-encryption` `[Verificado MS Learn]`
- **REF-03:** Microsoft Learn — *Personal Data Encryption (PDE) Overview (Known Folders & Windows Hello integration)*: `https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/personal-data-encryption/` `[Verificado MS Learn]`
- **REF-04:** Microsoft Learn — *Personal Data Encryption Settings, Configuration and Memory Dump Hardening*: `https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/personal-data-encryption/configure` `[Verificado MS Learn]`
- **REF-05:** Microsoft Learn — *Update Secure Boot Certificates for Windows Devices (2011 Expiration in June 2026 to 2023 CAs)*: `https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/update-secure-boot-certificates` `[Verificado MS Learn]`
- **REF-06:** Microsoft Learn — *Secure Boot status report in Windows Autopatch*: `https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/monitor/secure-boot-status-report` `[Verificado MS Learn]`
- **REF-07:** Microsoft Learn — *Policy CSP - SecureBoot (`EnableSecurebootCertificateUpdates = 22852`)*: `https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-secureboot` `[Verificado MS Learn]`
- **REF-08:** Microsoft Learn — *Windows 11 Security Book: Silicon-assisted security (VBS, HVCI, Kernel DMA & Secured-core PC)*: `https://learn.microsoft.com/en-us/windows/security/book/hardware-security-silicon-assisted-security` `[Verificado MS Learn]`
- **REF-09:** Microsoft Learn — *System Guard: How a hardware-based root of trust helps protect Windows*: `https://learn.microsoft.com/en-us/windows/security/hardware-security/how-hardware-based-root-of-trust-helps-protect-windows` `[Verificado MS Learn]`
- **REF-10:** Microsoft Learn — *Credential Guard overview & Default Enablement in Windows 11*: `https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/` `[Verificado MS Learn]`
- **REF-11:** Microsoft Learn — *Windows 11 Security Book: Advanced credential protection (LSA Protection, Credential Guard & Remote Credential Guard)*: `https://learn.microsoft.com/en-us/windows/security/book/identity-protection-advanced-credential-protection` `[Verificado MS Learn]`
- **REF-12:** Microsoft Learn — *Get started with Windows LAPS and Microsoft Entra ID*: `https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-scenarios-azure-active-directory` `[Verificado MS Learn]`
- **REF-13:** Microsoft Learn — *Configure Policy Settings & Automatic Account Management for Windows LAPS (24H2+)*: `https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-management-policy-settings` `[Verificado MS Learn]`
- **REF-14:** Microsoft Learn — *Windows Hello for Business Cloud Kerberos Trust Deployment Guide*: `https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust` `[Verificado MS Learn]`
- **REF-15:** Microsoft Learn — *Deploy App Control for Business policies using Mobile Device Management (Intune)*: `https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/deploy-appcontrol-policies-using-intune` `[Verificado MS Learn]`
- **REF-16:** Microsoft Learn — *Administrator Protection in Windows 11 (Architecture, CSP, ETW Events 15031/15032 & Exclusions)*: `https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/` `[Verificado MS Learn]`
- **REF-17:** Microsoft Learn — *Manage firewall settings with endpoint security policies in Microsoft Intune*: `https://learn.microsoft.com/en-us/intune/device-configuration/endpoint-security/firewall` `[Verificado MS Learn]`

### Blogs Oficiales, Empleados Microsoft, MVPs y Marcos Normativos
- **REF-18:** Windows IT Pro Blog (Microsoft) — *Secure Boot playbook for certificates expiring in 2026 (`0x5944`, Event IDs 1808/1801/1795 & WinCS)*: `https://techcommunity.microsoft.com/blog/windows-itpro-blog/secure-boot-playbook-for-certificates-expiring-in-2026/4469235` `[Verificado MS Learn]`
- **REF-19:** Michael Niehaus (*Out of Office Hours*) & Rudy Ooms (*Call4Cloud*) — *BitLocker auto-encryption in Windows 11 24H2 & TPM Pre-Attestation Health Check in 24H2*: `https://oofhours.com/2025/05/02/bitlocker-auto-encrypts-more-systems-with-windows-11-24h2/` y `https://call4cloud.nl/category/attestation-and-compliance-series/`
- **REF-20:** NIST — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)*: `https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20`

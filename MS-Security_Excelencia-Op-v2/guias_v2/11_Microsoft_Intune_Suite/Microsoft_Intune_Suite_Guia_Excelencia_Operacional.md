# Guía Maestra de Excelencia Operacional: Microsoft Intune Suite (Capacidades Avanzadas de Gestión y Seguridad de Endpoints)

## 1. Portada y Ficha de Control Documental

| Campo Documental | Detalle Oficial Consolidado |
| :--- | :--- |
| **Identificador del Módulo** | `11_Microsoft_Intune_Suite` |
| **Slug Canónico** | `Microsoft_Intune_Suite` |
| **Nombre Completo** | Microsoft Intune Suite (Capacidades Avanzadas sobre Intune Plan 1 y Microsoft 365 E5 / E7) |
| **Categoría Maestra** | Endpoints, Dispositivos y Plataforma Windows |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Complemento / Add-on sobre M365 E5 (Capacidades selectas incluidas en M365 E5 desde julio/agosto de 2026 + Suite completa / M365 E7) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://intune.microsoft.com`, `https://security.microsoft.com`, `https://entra.microsoft.com`, `https://admin.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Endpoint Engineering Lead, SOC L1/L2/L3, Help Desk Manager, PKI Architect, Vulnerability Management Lead, GRC / Internal Audit `[Decisión / Propuesta Editorial]` |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), MITRE ATT&CK Enterprise v18, Principios Microsoft Zero Trust, DISA STIG Audit Baseline `[Verificado MS Learn]` |

> **Nota de Consolidación y Alcance Operacional (Corte 11 de noviembre de 2026):** Esta guía operacionaliza las capacidades avanzadas que extienden **Microsoft Intune Plan 1** dentro del centro de administración `https://intune.microsoft.com`: **Endpoint Privilege Management (EPM)**, **Microsoft Cloud PKI**, **Enterprise Application Management (EAM)**, **Remote Help**, **Intune Advanced Analytics** y **Microsoft Tunnel for Mobile Application Management (MAM)**, junto con su integración agéntica con **Microsoft Security Copilot in Intune** `[Verificado MS Learn]`. Refleja con precisión contractual y técnica la actualización comercial de Microsoft efectiva desde el **1 de julio de 2026** (desplegada a tenants elegibles existentes hacia el **1 de agosto de 2026**), mediante la cual los clientes de **Microsoft 365 E5** reciben incluidos sin costo adicional los seis pilares operativos aquí documentados, preservándose el SKU **Microsoft Intune Suite** y los complementos individuales para escenarios de licenciamiento independiente, Frontline, Educación o adopción selectiva sobre planes base `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026

Históricamente, las organizaciones con **Microsoft Intune Plan 1** debían mantener un mosaico fragmentado de herramientas de terceros para cubrir brechas críticas de seguridad y operaciones en endpoints: agentes externos de gestión de privilegios (PAM/PEDM de escritorio), infraestructura local Active Directory Certificate Services (AD CS) con servidores NDES e Intune Certificate Connector, empaquetadores externos de parches Win32, software de control remoto no integrado con Acceso Condicional y agentes adicionales de consulta forense en tiempo real. Dicha fragmentación incrementaba el costo total de propiedad (TCO), ampliaba la superficie de ataque en modo kernel/usuario —en un contexto donde Microsoft Digital Defense Report documentó que el 79 % de los ataques de ransomware involucraron abuso de herramientas de administración remota en endpoints— y rompía la trazabilidad unificada del SOC `[Verificado MS Learn]`.

**Microsoft Intune Suite** consolida estas funciones directamente sobre la arquitectura nativa de Microsoft Intune, Microsoft Entra ID y Microsoft Defender XDR `[Verificado MS Learn]`. Durante 2026 se materializaron dos hitos comerciales y arquitectónicos decisivos que redefinen la planificación presupuestaria y operativa del CISO:

1. **Inclusión de capacidades avanzadas de Intune en Microsoft 365 E3 y Microsoft 365 E5 (Julio–Agosto 2026):** Anunciado oficialmente por Microsoft el 4 de diciembre de 2025 y efectivo desde el **1 de julio de 2026** (con aprovisionamiento automático en tenants existentes hacia el **1 de agosto de 2026**), **EMS E3 / Microsoft 365 E3** incorporó **Intune Remote Help**, **Intune Advanced Analytics** e **Intune Plan 2** (*Microsoft Tunnel for MAM*, *Specialty device management* y *Firmware Over-The-Air [FOTA]*). De forma acumulativa, **Microsoft 365 E5** incorporó todas las capacidades anteriores **más** **Intune Endpoint Privilege Management (EPM)**, **Microsoft Cloud PKI**, **Intune Enterprise Application Management (EAM)** y **Microsoft Security Copilot** `[Verificado MS Learn]`.
2. **Disponibilidad General de Microsoft 365 E7 ("The Frontier Suite", 1 de mayo de 2026) y Agentes de Security Copilot en Intune:** Microsoft 365 E7 unifica Microsoft 365 E5 (incluyendo las capacidades avanzadas de Intune y Security Copilot), Microsoft Entra Suite, Microsoft 365 Copilot y **Microsoft Agent 365** `[Verificado MS Learn]`. En paralelo, Intune integró agentes especializados de Security Copilot —destacando **Vulnerability Remediation Agent** y **Change Review Agent**— que correlacionan señales de Defender Vulnerability Management, Entra ID y Threat Intelligence para asistir decisiones de parcheo y aprobaciones administrativas `[Verificado MS Learn]`.

### 2.2 Matriz Detallada de Licenciamiento y Prerrequisitos (Corte Noviembre 2026)

| Plan / SKU Comercial | Capacidades Avanzadas de Intune Incluidas | Estado para Clientes M365 E5 (Post Julio/Agosto 2026) | Escenario de Uso Recomendado |
| :--- | :--- | :--- | :--- |
| **Microsoft Intune Plan 1** (Base MDM/MAM; $8 USD/usuario/mes standalone; incluido en M365 E3/E5/F1/F3/Business Premium/A3/A5) | Gestión base MDM/MAM, Endpoint Security (BitLocker, LAPS, Firewall, ASR), Autopilot, Endpoint Analytics base. No incluye capacidades avanzadas de Suite `[Verificado MS Learn]`. | Base obligatoria incluida en M365 E5 `[Verificado MS Learn]`. | Prerrequisito fundacional obligatorio para cualquier capacidad de Plan 2 o Intune Suite `[Verificado MS Learn]`. |
| **Microsoft Intune Plan 2** ($4 USD/usuario/mes add-on; incluido en EMS E3 / M365 E3 / M365 E5 desde CY26 Q3) | **Microsoft Tunnel for MAM**, **Specialty device management** (AR/VR, salas de reuniones, pantallas inteligentes) y **Firmware Over-The-Air (FOTA)** para Android/Zebra `[Verificado MS Learn]`. | **Incluido sin costo adicional** en EMS E3, M365 E3 y M365 E5 desde julio/agosto 2026 `[Verificado MS Learn]`. | Organizaciones con BYOD móvil no enrolado (MAM Tunnel) o dispositivos especializados/frontline `[Verificado MS Learn]`. |
| **EMS E3 / Microsoft 365 E3** (Actualización CY26 Q3) | Intune Plan 1 + **Intune Plan 2** + **Remote Help** + **Intune Advanced Analytics** `[Verificado MS Learn]`. | Subconjunto incluido automáticamente en M365 E5 `[Verificado MS Learn]`. | Clientes E3 que requieren soporte remoto RBAC, Device Query KQL y BYOD Tunnel, pudiendo adquirir EPM/Cloud PKI/EAM como add-on `[Verificado MS Learn]`. |
| **Microsoft 365 E5** (Actualización CY26 Q3) | Todo lo de M365 E3/Plan 2 **más** **Endpoint Privilege Management (EPM)**, **Microsoft Cloud PKI**, **Enterprise Application Management (EAM)** y **Microsoft Security Copilot** `[Verificado MS Learn]`. | **Incluido en la suscripción M365 E5** (aprovisionado automáticamente en el tenant) `[Verificado MS Learn]`. | Estándar empresarial recomendado para eliminar administradores locales, retirar AD CS/NDES y automatizar parcheo de terceros `[Decisión / Propuesta Editorial]`. |
| **Microsoft 365 E7 (The Frontier Suite)** (GA 1-may-2026; $99 USD/usuario/mes) | Incluye Microsoft 365 E5 completo (con todas las capacidades avanzadas de Intune + Security Copilot), Microsoft Entra Suite, Microsoft 365 Copilot y Microsoft Agent 365 `[Verificado MS Learn]`. | Nivel superior integrador sobre M365 E5 `[Verificado MS Learn]`. | Organizaciones que gobiernan de extremo a extremo identidades humanas, endpoints, red Zero Trust (SSE) y agentes IA `[Verificado MS Learn]`. |
| **Microsoft Intune Suite (Add-on SKU)** ($10 USD/usuario/mes) o **Add-ons individuales** ($2–$5 USD/usuario/mes) | Unifica Intune Plan 2 + EPM + Cloud PKI + EAM + Remote Help + Advanced Analytics. Evaluable mediante prueba gratuita de 90 días (máx. 250 usuarios + 30 días de gracia) en `Tenant administration > Intune add-ons` `[Verificado MS Learn]`. | No requerido para usuarios ya cubiertos por M365 E5 post CY26 Q3; vigente para usuarios con Intune Plan 1 standalone, F3, Business Premium o Educación `[Verificado MS Learn]`. | Cobertura de poblaciones mixtas (trabajadores de primera línea F1/F3, contratistas o tenants sin M365 E5 completo) `[Decisión / Propuesta Editorial]`. |

**Prerrequisitos técnicos transversales verificados:**
- **Sistemas operativos y fin de soporte de Windows 10:** EPM y Enterprise App Catalog operan sobre Windows de 64 bits (x64 y Arm64, incluyendo Windows 11 22H2/23H2/24H2/25H2+, Windows 365 y AVD single-session para EPM). El **14 de octubre de 2025** Windows 10 alcanzó su fin de soporte (*End of Support*); aunque Intune permite aún su enrolamiento como versión tolerada, no se garantiza funcionalidad completa, por lo que Windows 11 Enterprise es la base operativa exigible `[Verificado MS Learn]`.
- **Conectividad sin inspección TLS/SSL en endpoints críticos:** EPM requiere línea de vista directa sin inspección SSL hacia los endpoints de servicio de Intune/MMP-C, y Single-Device `Device query` junto con *Remote launch* de Remote Help dependen estrictamente de **Windows Push Notification Services (WNS)** activo `[Verificado MS Learn]`.
- **Propiedad corporativa e inventario:** `Device query` (individual y multi-dispositivo) y *Unattended remote sign-in* de Remote Help exigen que el dispositivo esté marcado como `Corporate` en Intune; además, `Device query for multiple devices` en Windows requiere desplegar previamente una política de **Properties catalog** `[Verificado MS Learn]`.

### 2.3 Principios Rectores y Alineación Zero Trust

1. **Erradicación del administrador local permanente (Verify Explicitly & Least Privilege):** Operar el 100 % de los usuarios finales como usuarios estándar en Windows, otorgando elevación Just-In-Time (JIT) aislada en cuenta virtual únicamente a binarios aprobados en EPM con validación criptográfica de hash o certificado `[Verificado MS Learn]`.
2. **Confianza criptográfica cloud-native sin deuda de infraestructura heredada:** Sustituir o descargar jerarquías locales AD CS, servidores NDES y conectores mediante **Microsoft Cloud PKI** con claves respaldadas en **Azure Managed HSM** (sin requerir suscripción Azure adicional) y distribución automática de AIA y CRL `[Verificado MS Learn]`.
3. **Higiene continua de aplicaciones de terceros guiada por riesgo de explotación:** Combinar el catálogo preempaquetado de **Enterprise Application Management** (con SLO de 24 horas para el 80–90 % de actualizaciones) con **Defender Vulnerability Management** y el **Vulnerability Remediation Agent** para cerrar CVEs explotados antes de que sean vector de intrusión `[Verificado MS Learn]`.
4. **Asistencia remota autenticada, condicionada y auditada de extremo a extremo:** Prohibir herramientas de soporte remoto no gobernadas, exigiendo **Remote Help** con autenticación Microsoft Entra ID intratenant, directivas de Acceso Condicional, alertas visuales de incumplimiento y segregación RBAC estricta `[Verificado MS Learn]`.
5. **Observabilidad proactiva y telemetría KQL en vivo antes de interrumpir al usuario:** Resolver diagnósticos L1/L2 y cazar desviaciones de flota con **Intune Advanced Analytics** (*Anomalies*, *Device timeline* y *Device query* individual/multi-dispositivo) antes de escalar a sesiones interactivas `[Verificado MS Learn]`.
6. **Micro-conectividad sin enrolamiento invasivo para BYOD (Assume Breach):** Garantizar acceso por aplicación a recursos privados en iOS/iPadOS y Android no enrolados mediante **Microsoft Tunnel for MAM**, **Strict Tunnel Mode** en Edge y bloqueo dinámico ante detección de *root* por Microsoft Defender `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional y Motores de Servicio

Microsoft Intune Suite extiende el plano de control de `https://intune.microsoft.com` mediante seis subsistemas nativos acoplados con la arquitectura de configuración declarativa de Windows (*Windows Declared Configuration / WinDC* y *Microsoft Management Platform - Cloud / MMP-C*), el agente *Intune Management Extension (IME)*, los servicios en nube de registro SCEP/HSM y la plataforma de datos de Endpoint Analytics `[Verificado MS Learn]`:

| Componente / Subsistema | Función Operativa Principal | Consola y Ruta Exacta (`intune.microsoft.com`) | Integraciones Nativas Clave |
| :--- | :--- | :--- | :--- |
| **1. Endpoint Privilege Management (EPM)** | Elevación JIT de procesos y ajustes de sistema (ej. configuración de red IPv4/IPv6/DNS offline) para usuarios estándar mediante cuenta virtual aislada (o *Elevate as current user* por compatibilidad), reglas *Automatic*, *User confirmed*, *Support approved* y *Deny*, control de procesos hijos y módulo local `EpmTools` `[Verificado MS Learn]`. | `Endpoint security > Endpoint Privilege Management` | Windows Declared Configuration (WinDC), Microsoft Defender TI vía Copilot in Intune, Entra ID, Intune RBAC `[Verificado MS Learn]`. |
| **2. Microsoft Cloud PKI** | Servicio PKI gestionado en nube (hasta 3 CAs por tenant en producción respaldadas por Azure Managed HSM: Root + Issuing en nube o *Bring Your Own CA* [BYOCA]), autoridad de registro SCEP en nube, endpoints públicos AIA/CDP y renovación/revocación de certificados hoja en Windows, macOS, iOS y Android `[Verificado MS Learn]`. | `Tenant administration > Cloud PKI` y `Devices > Configuration > SCEP / Trusted certificate` | Azure Managed HSM, Microsoft Entra CBA (autenticación resistente a phishing), Wi-Fi empresarial 802.1X y VPN `[Verificado MS Learn]`. |
| **3. Enterprise Application Management (EAM)** | Catálogo hospedado por Microsoft (`*.manage.microsoft.com`) de más de 1.000 aplicaciones Win32 (`.exe`/`.msi`) con comandos de instalación, códigos de retorno y reglas de detección preconfiguradas, soportando *Auto-update* (en asignaciones *Required*) y *Guided update supersedence* `[Verificado MS Learn]`. | `Apps > Windows > Add > Enterprise App Catalog app` y `Apps > Enterprise App Catalog apps with updates` | Intune Management Extension (IME), Windows Autopilot (ESP y Device Preparation DPP), Defender Vulnerability Management `[Verificado MS Learn]`. |
| **4. Remote Help** | Soporte remoto autenticado en Entra ID para Windows, macOS y Android con controles RBAC (*View screen*, *Take full control*, *Elevation*, *Unattended control* en Android dedicado y *Unattended remote sign-in* en sesión Windows separada), *Remote launch*, chat auditable y Web App *view-only* `[Verificado MS Learn]`. | `Tenant administration > Remote Help` y `Devices > All devices > [Dispositivo] > New remote assistance session` | Microsoft Entra Conditional Access, WNS, Intune Compliance Warnings, Intune Audit Logs `[Verificado MS Learn]`. |
| **5. Intune Advanced Analytics — Anomalies & Health** | Detección estadística/IA de anomalías de cuelgues de aplicaciones y errores de detención (BSOD) con grupos de correlación, informes de *Battery health*, *Resource performance*, *Device timeline*, segmentación por *Device scopes* y evaluación **DISA STIG Audit Baseline** `[Verificado MS Learn]`. | `Reports > Endpoint analytics > Anomalies / Battery health / Resource performance` | Windows Telemetry, Scope Tags de Intune, flujos ITSM de remediación proactiva `[Verificado MS Learn]`. |
| **6. Intune Advanced Analytics — Device Query (Single & Multi-Device)** | Motor KQL en tiempo real por dispositivo sobre WNS (entidades vivas `Process`, `WindowsRegistry`, `WindowsService`, `Certificate`, `LocalGroup`, etc.) y consulta KQL transversal multi-dispositivo (Windows, macOS, iOS, Android Enterprise) con exportación de hasta 50.000 filas y acción directa *Add all items to a group* `[Verificado MS Learn]`. | `Devices > Windows > [Dispositivo] > Device Query` y `Devices > Device query` | Properties Catalog Policy, Windows Push Notification Services (WNS), Microsoft Entra Security Groups, Copilot NL-to-KQL `[Verificado MS Learn]`. |
| **7. Microsoft Tunnel for Mobile Application Management (MAM)** | Extensión del gateway contenedorizado Linux de Microsoft Tunnel hacia dispositivos BYOD iOS/iPadOS y Android **no enrolados** en MDM, habilitando micro-VPN por aplicación, *Strict Tunnel Mode* e *Identity switch* en Microsoft Edge `[Verificado MS Learn]`. | `Tenant administration > Microsoft Tunnel Gateway` y `Apps > App configuration / App protection policies` | Microsoft Defender for Endpoint en Android (detección de *root* con corte inmediato de túnel), Intune App SDK, MSAL, Entra CA `[Verificado MS Learn]`. |
| **8. Security Copilot & Agents in Intune** | Asistencia generativa y agentes autónomos supervisados (*Vulnerability Remediation Agent* y *Change Review Agent* para *Multi Admin Approval* de scripts PowerShell) operando bajo identidad agéntica delegada `[Verificado MS Learn]`. | `Agents > Vulnerability Remediation Agent / Change Review Agent` e icono Copilot en `intune.microsoft.com` | Microsoft Security Copilot (SCUs), Defender Vulnerability Management, Entra ID Protection, Microsoft Threat Intelligence `[Verificado MS Learn]`. |

### 3.2 Desglose Técnico Profundo de los Seis Pilares Operativos

#### 3.2.1 Pilar 1 — Endpoint Privilege Management (EPM): Motor WinDC, Cuenta Virtual y Matriz de Reglas
- **Arquitectura del cliente y aprovisionamiento bajo demanda:** Intune aprovisiona los binarios locales del agente EPM (`C:\Program Files\Microsoft EPM Agent`) exclusivamente cuando el endpoint recibe una *Windows elevation settings policy* cuya intención explícita es habilitar EPM `[Verificado MS Learn]`. La distribución de políticas se apoya en el canal **Windows Declared Configuration (WinDC)** / **MMP-C**, cuyos documentos pueden inspeccionarse localmente mediante `Get-DeclaredConfiguration` y `Get-DeclaredConfigurationAnalysis` del módulo `EpmTools` `[Verificado MS Learn]`.
- **Tipos de políticas y configuración reutilizable:**
  - *Windows elevation settings policy*: política de ámbito de dispositivo (incluso si se asigna a grupos de usuarios) que define la activación del agente, el envío de telemetría diagnóstica (`Diagnostic data` / `Reporting scope`) y la respuesta de elevación predeterminada (`Deny`, `Require support approval` o `Require user confirmation`) `[Verificado MS Learn]`.
  - *Windows elevation rules policy*: define ejecutables específicos, requisitos de validación de identidad o justificación, argumentos permitidos, comportamiento de procesos hijos y modo de elevación `[Verificado MS Learn]`.
  - *Reusable settings groups*: repositorios centralizados de certificados de editor (`.cer`) referenciables por múltiples reglas para evitar duplicación y simplificar la rotación de certificados de proveedores `[Verificado MS Learn]`.
- **Comparativa operativa de comportamientos de elevación en EPM:**
  - `Automatic`: eleva silenciosamente sin intervención del usuario; debe acotarse con hash o certificado + `File path` inmutable en directorios protegidos del sistema `[Verificado MS Learn]`.
  - `User confirmed`: requiere invocación explícita mediante clic derecho *Run with elevated access* y admite exigir `Windows authentication` (reautenticación de credenciales/WHfB) y `Business justification` registrada en auditoría `[Verificado MS Learn]`.
  - `Elevate as current user`: ejecuta el proceso elevado bajo el token de la propia cuenta del usuario conectado en lugar de la cuenta virtual aislada de EPM, preservando variables de entorno y rutas de perfil de usuario tras exigir autenticación Windows; incrementa la superficie de ataque sobre datos del usuario y debe limitarse a excepciones documentadas de compatibilidad `[Verificado MS Learn]`.
  - `Support approved`: retiene la elevación hasta que un operador autorizado apruebe la solicitud en `intune.microsoft.com`, notificando al endpoint para permitir la ejecución durante la ventana aprobada `[Verificado MS Learn]`.
  - `Deny`: bloquea de manera absoluta la elevación del archivo y prevalece sobre cualquier otra regla en el dispositivo `[Verificado MS Learn]`.
- **Gobernanza de procesos hijos (*Child process behavior*):** Toda regla EPM permite configurar tres niveles sobre subprocesos engendrados por el binario elevado: `Deny all` (máxima seguridad, impide lanzar subprocesos elevados), `Require rule to elevate` (cada subproceso debe coincidir con su propia regla EPM) y `Allow all child processes to run elevated` (mayor riesgo de escape mediante *LOLBins* o cuadros de diálogo `Abrir/Guardar`) `[Verificado MS Learn]`.
- **Elevación de ajustes del sistema (*System settings*):** EPM permite delegar ajustes específicos del sistema operativo (como configuración de adaptadores de red IPv4, IPv6 y servidores DNS mediante interfaz acotada integrada con Company Portal, funcional incluso sin conectividad de red previa cuando la política ya reside en el equipo) sin otorgar acceso administrativo completo a Windows Settings `[Verificado MS Learn]`.

#### 3.2.2 Pilar 2 — Microsoft Cloud PKI: Flujo Criptográfico SCEP, Azure mHSM y Modelos de Despliegue
- **Flujo transaccional SCEP de extremo a extremo (pasos `A1` a `A5`):**
  1. `A1`: El dispositivo enrolado en Intune realiza check-in y recibe los perfiles *Trusted certificate* (CA Raíz y Emisora) junto con el perfil *SCEP certificate* específico de su plataforma (Windows, macOS, iOS/iPadOS o Android) `[Verificado MS Learn]`.
  2. `A2`: El dispositivo genera localmente el par de claves (la clave privada **nunca abandona el dispositivo**) y construye el *Certificate Signing Request (CSR)*, enviándolo junto con el desafío SCEP cifrado y firmado con claves RA de Intune hacia el URI de Cloud PKI SCEP `[Verificado MS Learn]`.
  3. `A3`: El *Cloud PKI SCEP validation service* (Autoridad de Registro en nube) verifica que la solicitud provenga de un dispositivo gestionado legítimo y que el challenge no haya sido alterado y coincida exactamente con los atributos esperados del perfil SCEP; cualquier discrepancia rechaza la solicitud `[Verificado MS Learn]`.
  4. `A4`: Tras validar el CSR, la Autoridad de Registro solicita la firma a la *Cloud PKI Issuing CA* (cuyas claves de firma/cifrado RSA 2048/3072/4096 con SHA-256/384/512 residen en **Azure Managed HSM**) `[Verificado MS Learn]`.
  5. `A5`: El certificado hoja firmado (PKCS#7) se entrega silenciosamente al almacén criptográfico del dispositivo `[Verificado MS Learn]`.
- **Coexistencia de modelos Cloud Root CA y BYOCA:** Un mismo tenant puede combinar jerarquías de dos niveles 100 % en nube (*Cloud PKI Root CA + Issuing CA*) con emisoras **Bring Your Own CA (BYOCA)** subordinadas a una PKI privada existente (AD CS o terceros de N niveles), siempre respetando el tope global de **3 CAs por tenant** `[Verificado MS Learn]`. En ambos modelos, los *relying parties* (RADIUS/NPS, concentradores VPN y **Microsoft Entra CBA**) deben confiar en la cadena pública descargada desde `Tenant administration > Cloud PKI` y tener visibilidad HTTP hacia los puntos **AIA** y **CDP (CRL)** hospedados por Intune `[Verificado MS Learn]`.

#### 3.2.3 Pilar 3 — Enterprise Application Management (EAM): Flujo de Ingestión, Validación y Parcheo
- **Pipeline gestionado por Microsoft:** Cada aplicación Win32 (`.exe` o `.msi`) del catálogo atraviesa cuatro fases: (1) *Ingestion* desde la fuente del fabricante; (2) *Automated Validation* (meta SLO: **80–90 % disponible en consola dentro de 24 horas**); (3) *Manual Validation* para instaladores complejos (meta SLO: **<= 7 días**, o meta acelerada de **48 horas** en aplicaciones críticas de alto uso); y (4) *Catalog Availability* servida desde almacenamiento de Microsoft en `*.manage.microsoft.com` mediante *Intune Management Extension (IME)* (sin depender de `winget`) `[Verificado MS Learn]`.
- **Integración con aprovisionamiento moderno:** Las aplicaciones del catálogo empresarial pueden seleccionarse como aplicaciones bloqueantes tanto en la *Enrollment Status Page (ESP)* de Windows Autopilot clásico como en perfiles de *Windows Autopilot Device Preparation (DPP)* `[Verificado MS Learn]`.
- **Matriz de decisión operativa entre modos de actualización EAM:**
  - *Self-updating apps*: aplicaciones con actualizador nativo del proveedor (ej. navegadores); Intune verifica que la versión instalada sea igual o superior a la versión mínima objetivo `[Verificado MS Learn]`.
  - *Auto-update for Enterprise App Catalog apps*: aplicable solo a asignaciones `Required`; actualiza automáticamente al publicarse nueva versión en el catálogo sin crear nuevos objetos, ideal para utilidades estándar tolerantes a despliegue directo `[Verificado MS Learn]`.
  - *Guided update supersedence*: crea un nuevo objeto de aplicación con relación de *supersedence* preconfigurada desde `Apps > Enterprise App Catalog apps with updates`, obligatorio para asignaciones `Available` y recomendado para software crítico que exige anillos piloto y control de cambio `[Verificado MS Learn]`.

#### 3.2.4 Pilar 4 — Remote Help: Matriz Multi-Plataforma y Sesiones Desatendidas
- **Controles transversales de confianza:** Tanto el *Helper* como el *Sharer* deben iniciar sesión con cuentas Microsoft Entra ID de la **misma organización** (no se admiten sesiones B2B entre tenants distintos), bajo evaluación de Acceso Condicional (MFA, ubicación, cumplimiento) y visualización previa de *Compliance warnings* si el endpoint destino incumple directivas `[Verificado MS Learn]`.
- **Capacidades específicas por sistema operativo:**
  - *Windows*: soporta *View screen*, *Take full control*, *Elevation* (ingreso de credenciales administrativas en avisos UAC; si el usuario final cierra una sesión donde hubo elevación, Windows cierra automáticamente la sesión del usuario por seguridad), *Remote launch* vía notificación push, *Web app for sharers* (solo vista cuando no puede instalarse el cliente) y **Unattended control: Remote sign-in** (crea una sesión Windows separada y autenticada con las credenciales del helper en PCs físicos corporativos gestionados por Intune, sin requerir usuario presente) `[Verificado MS Learn]`.
  - *macOS*: soporta cliente nativo, *Web app for sharers* (*view-only*), chat multilingüe continuo y Acceso Condicional `[Verificado MS Learn]`.
  - *Android*: soporta asistencia atendida y **Unattended control** sobre dispositivos enrolados como *Android Enterprise dedicated devices (COSU)* `[Verificado MS Learn]`.

#### 3.2.5 Pilar 5 — Intune Advanced Analytics: Esquema de Entidades `Device query` y Analítica Proactiva
- **Diferencia arquitectónica entre Single-Device y Multi-Device `Device query`:**
  - *Single-Device `Device query`*: interroga en tiempo real un dispositivo Windows corporativo vivo a través de **WNS**, exponiendo 21 entidades operativas y forenses (`BiosInfo`, `Certificate`, `Cpu`, `DiskDrive`, `EncryptableVolume`, `FileInfo`, `LocalGroup`, `LocalUserAccount`, `LogicalDrive`, `MemoryInfo`, `OsVersion`, `Process`, `SystemEnclosure`, `SystemInfo`, `Tpm`, `WindowsAppCrashEvent`, `WindowsDriver`, `WindowsEvent`, `WindowsQfe`, `WindowsRegistry`, `WindowsService`) y permitiendo disparar acciones remotas inmediatas `[Verificado MS Learn]`.
  - *Multi-Device `Device query`*: ejecuta KQL sobre el inventario recolectado en la plataforma de datos de Intune a través de Windows (con política *Properties catalog* desplegada), macOS, iOS/iPadOS y Android Enterprise (`COSU`, `COBO`, `COPE`), exponiendo entidades normalizadas (`Apple Auto Setup Admin Accounts`, `Apple Device States`, `Apple Update Settings`, `Battery`, `Bios Info`, `Bluetooth`, `Cellular`, `CPU`, `Device Storage`, `Disk Drive`, `Encryptable Volume`, `Local AI Agent`, `Logical Drive`, `Memory Info`, `Network Adapter`, `Os Version`, `Shared iPad`, `Sim Info`, `System Enclosure`, `SystemInfo`, `Time`, `Tpm`, `Video Controller`, `Windows Qfe`) vinculadas a la entidad `Device` (`DeviceId`, `EntraDeviceId`, `SerialNumber`, `OSVersion`, `Ownership`, `PrimaryUserId`, `LastSeenDateTime`) `[Verificado MS Learn]`.

#### 3.2.6 Pilar 6 — Microsoft Tunnel for MAM: Arquitectura BYOD en Android vs. iOS/iPadOS
- **En Android BYOD no enrolado:** Requiere instalar *Company Portal* (sin exigir inicio de sesión ni enrolamiento MDM) y la app **Microsoft Defender for Endpoint**, que actúa como proveedor del túnel VPN (soportando *Per-App VPN* y *Device-wide VPN*, *Auto-launch* y corte inmediato de conexión si detecta que el teléfono está *rooted*, elevando el riesgo a `High`) `[Verificado MS Learn]`.
- **En iOS/iPadOS BYOD no enrolado:** No requiere *Company Portal* ni *Defender for Endpoint*; el túnel *Per-App VPN* se establece directamente mediante la integración del **Intune App SDK + MSAL + Tunnel for MAM SDK for iOS** (con soporte de certificados raíz privados para confianza hacia servidores internos) `[Verificado MS Learn]`.
- **Protección en Microsoft Edge for Business (ambas plataformas):** Soporta *Identity switch* (conecta el túnel al usar perfil corporativo y lo desconecta al cambiar a perfil personal o navegación *InPrivate*) y **Strict Tunnel Mode** (bloquea todo tráfico web corporativo si el túnel VPN cae hasta que se restablezca) `[Verificado MS Learn]`.

### 3.3 Consideraciones Arquitectónicas Críticas y Límites de Servicio (2026–2027)

1. **Precedencia determinista de conflictos en reglas EPM:** Cuando múltiples reglas aplican a un mismo ejecutable en un dispositivo, el agente EPM evalúa estrictamente en este orden: (1) las reglas `Deny` ganan siempre; (2) las reglas asignadas a **usuario** prevalecen sobre las asignadas a **dispositivo**; (3) las reglas con **hash de archivo** definido se consideran siempre las más específicas; (4) sin hash, gana la regla con mayor cantidad de atributos definidos; y (5) en caso de empate residual, aplica el orden `User confirmed` > `Elevate as current user` > `Support approved` > `Automatic` `[Verificado MS Learn]`.
2. **Aislamiento de cuenta virtual vs. `Elevate as current user` en EPM:** Por diseño de seguridad, EPM eleva procesos mediante una **cuenta virtual** aislada del perfil del usuario estándar para impedir que malware en contexto de usuario manipule datos del perfil elevado. El modo `Elevate as current user` conserva rutas y variables del usuario activo (exigiendo autenticación Windows), pero amplía la superficie de exposición y debe restringirse exclusivamente a instaladores/herramientas heredadas incompatibles con cuentas virtuales `[Verificado MS Learn]`.
3. **Inmutabilidad de claves de prueba y límite de capacidad en Cloud PKI:** Cada tenant de Intune admite un **máximo de 3 autoridades certificadoras (CAs)** sumando Cloud PKI Root CA, Cloud PKI Issuing CA y BYOCA Issuing CA `[Verificado MS Learn]`. Las CAs creadas durante una **prueba gratuita (trial)** utilizan claves respaldadas por software (`System.Security.Cryptography.RSA`) y **no pueden convertirse posteriormente a claves Azure Managed HSM** tras adquirir o activar la licencia definitiva; por tanto, toda CA creada en fase de prueba debe descartarse y recrearse en producción `[Verificado MS Learn]`. Además, Cloud PKI está soportado en nube pública y GCC High, pero no en DoD ni ofrece opción de residencia de datos específica a corte noviembre de 2026 `[Verificado MS Learn]`.
4. **Compromisos operativos entre *Auto-update* y *Guided Update Supersedence* en EAM:** La función *Auto-update* actualiza automáticamente aplicaciones `Required` sin crear nuevos objetos ni relaciones de supersedence, pero **no soporta anillos de despliegue escalonado (rollout rings)**, **no provee rollback automático** y presenta hasta **1 hora de caché de catálogo** en caso de revocación de una versión maliciosa `[Verificado MS Learn]`. Para software crítico de negocio o agentes sensibles, debe mantenerse *Guided update supersedence* con anillos piloto `[Decisión / Propuesta Editorial]`.
5. **Sintaxis actualizada de `join` y límites en `Device query`:** En `Device query for multiple devices`, las uniones basadas en `on Device.DeviceId` dejaron de estar soportadas y deben escribirse como `| join LogicalDrive on Device` (u omitiendo `on` sobre la entidad `Device`). En consulta individual en vivo, el límite de despacho es de **15 consultas por minuto**, entrada máxima de **2.048 caracteres** y salida truncada a **128 KB** `[Verificado MS Learn]`.
6. **Ausencia de algoritmos FIPS en Microsoft Tunnel:** El gateway Microsoft Tunnel (incluido Tunnel for MAM) **no utiliza algoritmos validados FIPS**, aspecto que GRC debe registrar formalmente si existen cargas reguladas federales `[Verificado MS Learn]`.

### 3.4 Matriz de Integraciones Cruzadas con el Ecosistema Microsoft Security y M365 E5 / E7

| Plataforma del Ecosistema | Punto de Integración Técnica con Microsoft Intune Suite | Valor Operativo Conjunto para CISO y SOC |
| :--- | :--- | :--- |
| **Microsoft Entra ID & Entra Suite** | Emisión SCEP de **Cloud PKI** hacia **Microsoft Entra Certificate-Based Authentication (CBA)** resistente a phishing; directivas de Acceso Condicional sobre **Remote Help** y **Tunnel for MAM**; creación directa de grupos de seguridad Entra desde resultados de **Multi-Device `Device query`** `[Verificado MS Learn]`. | Cierra el ciclo identidad-dispositivo impidiendo accesos desde equipos no conformes o con certificados revocados `[Verificado MS Learn]`. |
| **Microsoft Defender XDR & Vulnerability Management** | Telemetría de CVEs alimentando **Enterprise Application Management** y el **Vulnerability Remediation Agent**; evaluación de inteligencia de amenazas sobre ejecutables en **EPM**; detección de *root* en Android por **Defender for Endpoint** cortando sesiones activas de **Tunnel for MAM** `[Verificado MS Learn]`. | Prioriza parches por riesgo real de explotación y bloquea privilegios o túneles ante señales de compromiso XDR `[Verificado MS Learn]`. |
| **Microsoft Sentinel (Unified SecOps Platform)** | Ingesta de `IntuneAuditLogs` y `IntuneOperationalLogs` mediante Diagnostic Settings hacia Log Analytics / Data Lake en `security.microsoft.com` (aprovechando retención y correlación con `SigninLogs` y `DeviceProcessEvents`) `[Verificado MS Learn]`. | Permite reglas analíticas SIEM sobre elevaciones EPM anómalas, sesiones desatendidas Remote Help y revocaciones PKI `[Decisión / Propuesta Editorial]`. |
| **Microsoft Purview Suite** | Coexistencia de **Intune App Protection Policies (MAM)** con políticas de **Purview Endpoint DLP / Insider Risk Management**; protección de exfiltración en portapapeles y almacenamiento en BYOD conectado vía **Tunnel for MAM** `[Verificado MS Learn]`. | Impide fuga de datos sensibles durante soporte remoto o acceso micro-VPN desde dispositivos personales `[Decisión / Propuesta Editorial]`. |
| **Microsoft Security Copilot & Agent 365** | Consultas NL-to-KQL en `Device query`, análisis de riesgo de solicitudes EPM, **Vulnerability Remediation Agent**, **Change Review Agent** (evaluación de scripts PowerShell en *Multi Admin Approval*) e inventario de `Local AI Agent` en endpoints corporativos `[Verificado MS Learn]`. | Acelera triaje L1/L2, reduce errores humanos en aprobaciones críticas y extiende visibilidad hacia agentes IA locales `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Conforme a las buenas prácticas oficiales de Microsoft Intune, las operaciones diarias **nunca** deben ejecutarse con `Global Administrator` ni `Intune Administrator` permanentes; deben delegarse mediante roles integrados y personalizados de **Intune RBAC** acotados por **Scope Tags** y activados JIT en **Microsoft Entra Privileged Identity Management (PIM)** mediante grupos asignables a roles (*Role-assignable groups*) `[Verificado MS Learn]`. Asimismo, se recomienda verificar que `Allow access to unlicensed admins` esté habilitado en tenants anteriores a julio de 2021 (habilitado por defecto en tenants posteriores, hasta 1.000 administradores sin licencia directa por grupo de seguridad plano, sin anidamiento) `[Verificado MS Learn]`.

| Rol Oficial / Personalizado | Plano RBAC | Permisos Clave Verificados | Estrategia PIM / JIT Sugerida | Responsabilidad Operativa y Segregación de Funciones |
| :--- | :--- | :--- | :--- | :--- |
| **Intune Administrator** *(Rol Microsoft Entra)* | Entra ID + Intune Global | Lectura/escritura completa en datos y auditoría de Intune, habilitación tenant-wide de Remote Help, Cloud PKI root/issuing CAs, Multi Admin Approval y agentes Copilot `[Verificado MS Learn]`. | **Elegible en PIM (máx. 2 h)** con MFA resistente a phishing (FIDO2/WHfB), justificación de ticket y aprobación dual `[Decisión / Propuesta Editorial]`. | Gobierno estructural del tenant, alta/baja de CAs de producción y cambios globales sometidos a *Multi Admin Approval* `[Verificado MS Learn]`. |
| **Intune Role Administrator** *(Rol integrado Intune)* | Intune RBAC | Único rol nativo de Intune autorizado para crear roles personalizados de Intune y asignar permisos y Scope Tags a otros administradores `[Verificado MS Learn]`. | **Elegible en PIM (máx. 2 h)** segregado de quienes aprueban elevaciones o emiten certificados `[Decisión / Propuesta Editorial]`. | Mantenimiento de roles personalizados (Cloud PKI, Remote Help, Device Query) e higiene trimestral RBAC `[Verificado MS Learn]`. |
| **Endpoint Privilege Manager** *(Rol integrado Intune)* | Intune RBAC | Todos los derechos sobre `Endpoint Privilege Management Policy Authoring` (Create, Update, Delete, Assign, View Reports) y `Endpoint Privilege Management Elevation Requests` `[Verificado MS Learn]`. | **Elegible en PIM (máx. 4 h)** para ingeniería de políticas; separado de mesa de ayuda L1 `[Decisión / Propuesta Editorial]`. | Diseño y ciclo de vida de políticas de configuración y reglas de elevación EPM, certificados reutilizables y exclusiones `Deny` `[Verificado MS Learn]`. |
| **EPM Elevation Approver (Custom SOC/L2 Role)** *(Rol personalizado Intune)* | Intune RBAC | `Endpoint Privilege Management Elevation Requests`: *View elevation requests* y *Modify elevation requests* + `Endpoint Privilege Management Policy Authoring`: *Read / View Reports* `[Verificado MS Learn]`. | **Activo en turno SOC/L2** mediante grupo PIM de 8 h con MFA obligatoria `[Decisión / Propuesta Editorial]`. | Aprobación o rechazo JIT de solicitudes `Support approved` sin capacidad de crear reglas `Automatic` permanentes `[Decisión / Propuesta Editorial]`. |
| **Cloud PKI Authority Operator (Custom PKI Role)** *(Rol personalizado Intune)* | Intune RBAC | Permisos granulares de Cloud PKI: *Read CAs*, *Create certificate authorities* (restringido a L3 PKI) y *Revoke issued leaf certificates*, acotados por *Scope Tags* `[Verificado MS Learn]`. | *Read/Revoke* elegible 4 h para SecOps/PKI; *Create CA* bloqueado tras cambio CAB `[Decisión / Propuesta Editorial]`. | Monitoreo de certificados emitidos, revocación de emergencia de certificados hoja comprometidos y gestión de perfiles SCEP `[Verificado MS Learn]`. |
| **Remote Help Tiered Operator (Custom L1 vs. L2/L3 Roles)** *(Roles personalizados Intune)* | Intune RBAC | Permisos `Remote Help app`: L1 solo *View screen* y *Remote launch*; L2 agrega *Take full control* y *Elevation*; L3/Field Ops restringido agrega *Unattended control* `[Verificado MS Learn]`. | L1 activo en turno; L2/L3 **Elegible en PIM (máx. 4 h)** para *Elevation* y *Unattended control* `[Decisión / Propuesta Editorial]`. | Asistencia remota con privilegio mínimo escalonado, impidiendo que N1 tome control desatendido o introduzca credenciales UAC `[Decisión / Propuesta Editorial]`. |
| **Device Query & Analytics Hunter (Custom SecOps Role)** *(Rol personalizado Intune)* | Intune RBAC | `Managed Devices/Query` (obligatorio para Single-Device Query), `Managed devices/Read` y `Organization/Read` (para Multi-Device Query y Advanced Analytics) `[Verificado MS Learn]`. | **Activo en turno para SOC L2 / Threat Hunters** con revisión trimestral `[Decisión / Propuesta Editorial]`. | Ejecución de consultas KQL en tiempo real e inventario transversal de flota sin permisos de borrado ni modificación de políticas `[Verificado MS Learn]`. |
| **Application Manager** *(Rol integrado Intune)* | Intune RBAC | Gestión de aplicaciones móviles y administradas, publicación desde **Enterprise App Catalog**, configuración de *Auto-update* y *Guided update supersedence* `[Verificado MS Learn]`. | **Elegible en PIM (máx. 4 h)** durante ventanas de empaquetado y parcheo `[Decisión / Propuesta Editorial]`. | Despliegue y actualización de aplicaciones Win32 empresariales en coordinación con Vulnerability Management `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

### D-01: Triaje y Resolución JIT de Solicitudes `Support approved` en Endpoint Privilege Management
- **Objetivo:** Procesar las solicitudes de elevación puntual enviadas por usuarios estándar sin otorgar permisos locales permanentes, validando legitimidad de negocio y reputación de amenaza `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Endpoint Privilege Management** > pestaña **Elevation requests** `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1/L2 / EPM Elevation Approver `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola de solicitudes en estado `Pending` y verificar el usuario solicitante, el dispositivo corporativo, la justificación de negocio ingresada y la ruta completa del ejecutable `[Verificado MS Learn]`.
  2. Invocar **Copilot in Intune** sobre la solicitud para evaluar el hash SHA-256, el editor firmante y la inteligencia de amenazas de Microsoft Defender antes de decidir `[Verificado MS Learn]`.
  3. Rechazar (`Deny`) de inmediato cualquier solicitud originada en carpetas modificables por el usuario (`Downloads`, `AppData\Local\Temp`, recursos de red) o correspondiente a intérpretes de alto riesgo (`powershell.exe`, `cmd.exe`, `mshta.exe`) no autorizados `[Verificado MS Learn]`.
  4. Aprobar (`Approve`) únicamente binarios verificados registrando el número de ticket ITSM en el campo de motivo; notificar al usuario que dispone de la ventana aprobada para reintentar *Run with elevated access* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de aprobación/rechazo en `Tenant administration > Audit logs` (categoría `EndpointPrivilegeManagement`) vinculado al ticket ITSM (SLA objetivo: < 30 minutos en horario hábil) `[Decisión / Propuesta Editorial]`.

### D-02: Monitoreo de Anomalías Críticas en Intune Advanced Analytics
- **Objetivo:** Detectar tempranamente picos estadísticos de pantallas azules (stop errors) o cierres inesperados de aplicaciones provocados por parches, drivers o agentes defectuosos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Endpoint analytics** > **Anomalies** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Operations L2 / Problem Management `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar anomalías de severidad `High` y `Medium` generadas en las últimas 24 horas y analizar los *Device correlation groups* calculados por el motor analítico (modelo de hardware, versión de driver, actualización KB o versión de aplicación común) `[Verificado MS Learn]`.
  2. Seleccionar una muestra de dispositivos afectados y revisar **Device timeline** para correlacionar el inicio exacto del fallo con eventos de instalación o reinicio `[Verificado MS Learn]`.
  3. Si la anomalía coincide con un despliegue reciente de aplicación o driver, pausar el anillo siguiente y abrir incidente preventivo en Problem Management antes de que escale el volumen de tickets en Service Desk `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación diaria de anomalías activas y ticket preventivo con grupo de dispositivos correlacionado `[Decisión / Propuesta Editorial]`.

### D-03: Supervisión de Sesiones Activas, *Compliance Warnings* y Elevaciones en Remote Help
- **Objetivo:** Asegurar que toda sesión de asistencia remota cumpla las políticas de acceso condicional y auditar intervenciones sobre equipos no conformes o con elevación UAC `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Remote Help** > pestaña **Monitor** y **Remote Help sessions** `[Verificado MS Learn]`.
- **Rol Responsable:** Help Desk Lead / SOC L1 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar el panel de sesiones de las últimas 24 horas identificando helper, sharer, dispositivo destino, duración y modalidad (`View screen`, `Full control`, `Elevation` o `Unattended`) `[Verificado MS Learn]`.
  2. Auditar específicamente las sesiones conectadas hacia dispositivos con advertencia de *Non-compliant* verificando que el operador no haya expuesto credenciales privilegiadas sin contención previa `[Verificado MS Learn]`.
  3. Cruzar las sesiones con elevación o modo desatendido contra tickets abiertos válidos en la plataforma ITSM; escalar cualquier sesión huérfana como posible abuso interno (`T1219`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Trazas de sesión en el monitor de Remote Help y eventos correspondientes en `Tenant administration > Audit logs` `[Verificado MS Learn]`.

### D-04: Verificación Operativa de Gateways y Salud de Microsoft Tunnel for MAM
- **Objetivo:** Garantizar disponibilidad continua del acceso micro-VPN para dispositivos BYOD iOS y Android y detectar bloqueos por dispositivos comprometidos o *rooteados* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Microsoft Tunnel Gateway** > pestañas **Health status** y **Servers** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Network / Mobility Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Confirmar estado `Online` de todos los nodos contenedorizados Linux en cada *Site* y validar métricas de check-in, uso de CPU/memoria, latencia y vigencia del certificado TLS (< 30 días a expirar dispara renovación) `[Verificado MS Learn]`.
  2. Revisar en Defender XDR / Intune eventos de dispositivos Android bloqueados automáticamente en el túnel por detección de *root* (riesgo `High`) `[Verificado MS Learn]`.
  3. Validar que ninguna directiva de configuración de Microsoft Edge haya desactivado accidentalmente *Strict Tunnel Mode* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/log de estado saludable de *Tunnel Sites* y registro de incidentes por caída o certificado próximo a vencer `[Verificado MS Learn]`.

### D-05: Revisión Diaria de Actualizaciones de Seguridad en Enterprise App Catalog y Agente de Vulnerabilidades
- **Objetivo:** Aprovechar el SLO de 24 horas del catálogo empresarial para parchear rápidamente vulnerabilidades críticas en software de terceros `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Apps** > **Enterprise App Catalog apps with updates** y **Agents** > **Vulnerability Remediation Agent** `[Verificado MS Learn]`.
- **Rol Responsable:** Application Manager / Vulnerability Management Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Consultar el mosaico **Enterprise App Catalog apps with updates** para identificar aplicaciones aprovisionadas cuya `Latest available version` supere la `Provisioned version` `[Verificado MS Learn]`.
  2. Ejecutar o revisar las recomendaciones priorizadas del **Vulnerability Remediation Agent** en Intune (alimentado por Microsoft Defender Vulnerability Management) para detectar CVEs con exploit activo o alto impacto `[Verificado MS Learn]`.
  3. Para aplicaciones críticas de seguridad (navegadores, visores PDF, compresores, clientes VPN/colaboración) con CVE crítico/alto, iniciar de inmediato el flujo de **Guided update supersedence** hacia el anillo piloto 0 o confirmar la ejecución de *Auto-update* `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Lista de nuevas versiones detectadas y registro de creación de paquete *supersedence* o validación de *Auto-update* `[Verificado MS Learn]`.

### D-06: Control de Emisión SCEP y Salud de Servicios en Microsoft Cloud PKI
- **Objetivo:** Detectar fallos de aprovisionamiento de certificados cliente (Wi-Fi, VPN, Entra CBA) que puedan interrumpir la conectividad Zero Trust de los usuarios `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Cloud PKI** y **Devices** > **Monitor** > **Certificates** `[Verificado MS Learn]`.
- **Rol Responsable:** PKI Operations / Endpoint L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar que todas las autoridades certificadoras configuradas (Root CA, Issuing CA o BYOCA Issuing CA) se encuentren en estado `Active` y que sus endpoints CDP (CRL) y AIA respondan correctamente `[Verificado MS Learn]`.
  2. Revisar en el informe de certificados las solicitudes SCEP fallidas en las últimas 24 horas (errores de validación de challenge RA o desajustes de atributos Subject/SAN) `[Verificado MS Learn]`.
  3. Remediar asignaciones de perfiles *Trusted certificate* faltantes antes de que se despliegue el perfil SCEP dependiente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Panel de estado de Cloud PKI (actualizado cada 24 h) sin errores masivos de emisión SCEP `[Verificado MS Learn]`.

### D-07: Diagnóstico Táctico en Vivo mediante Single-Device `Device query`
- **Objetivo:** Resolver incidentes operativos y alertas del SOC consultando el estado real del dispositivo en segundos mediante KQL sin interrumpir al usuario con sesiones de control remoto `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Windows** > `[Seleccionar Dispositivo]` > **Monitor** > **Device Query** `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Help Desk L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ante un ticket escalado o alerta de comportamiento anómalo en un endpoint conectado (con WNS operativo), abrir **Device Query** sobre el dispositivo `[Verificado MS Learn]`.
  2. Ejecutar consultas KQL acotadas (respetando el límite de 15 consultas/minuto) sobre `Process`, `WindowsService`, `WindowsRegistry`, `Certificate`, `LocalGroup` o `WindowsEvent` (apoyándose en Copilot in Intune para traducir lenguaje natural a KQL cuando se requiera) `[Verificado MS Learn]`.
  3. Si se confirma el hallazgo (ej. servicio detenido o configuración corrupta), lanzar directamente una acción remota de remediación o reinicio desde la misma vista sin requerir sesión interactiva `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consulta ejecutada y resultado adjunto en el expediente del incidente/ticket `[Decisión / Propuesta Editorial]`.

### D-08: Auditoría Diaria de Cambios Privilegiados y *Multi Admin Approval* con Change Review Agent
- **Objetivo:** Garantizar trazabilidad de cambios sensibles sobre políticas EPM, CAs, Remote Help y scripts PowerShell evaluados con IA `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Audit logs** y **Tenant administration** > **Multi Admin Approval** (`Change Review Agent`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Governance Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar los registros de auditoría de las últimas 24 horas por categorías `EndpointPrivilegeManagement`, `CloudPKI`, `RemoteHelp` y `Role` `[Verificado MS Learn]`.
  2. Para solicitudes pendientes de *Multi Admin Approval* sobre scripts de PowerShell en Windows, consultar el análisis contextual de riesgo generado por el **Change Review Agent** (señales combinadas de Defender Vulnerability Management, Entra ID y Threat Intelligence) antes de otorgar la segunda firma administrativa `[Verificado MS Learn]`.
  3. Abrir investigación inmediata ante cualquier creación de regla EPM `Automatic` sin ruta de archivo restringida o revocación no documentada en Cloud PKI `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación filtrada de `Audit logs` y dictamen registrado en solicitudes de *Multi Admin Approval* `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Análisis de *Managed vs. Unmanaged Elevations* y Refinamiento de Reglas EPM
- **Objetivo:** Reducir progresivamente a cero las elevaciones no gestionadas (*Run as administrator* remanente) y transformar solicitudes `Support approved` legítimas repetitivas en reglas precisas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Endpoint security** > **Endpoint Privilege Management** > **Elevation report** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Privilege Manager `[Verificado MS Learn]`.
- **Procedimiento Paso a Paso:**
  1. Analizar la proporción semanal de **Managed elevations** frente a **Unmanaged elevations**; todo equipo que aún registre elevaciones no gestionadas indica presencia de cuentas administrativas locales pendientes de erradicar `[Verificado MS Learn]`.
  2. Identificar aplicaciones que acumulen múltiples solicitudes `Support approved` legítimas para una misma *persona* de usuario (ej. desarrolladores o ingenieros de campo) `[Verificado MS Learn]`.
  3. Extraer atributos exactos y cadena de certificados con `Get-FileAttributes` del módulo PowerShell `EpmTools` y crear reglas `User confirmed` exigiendo **Windows authentication** + **Business justification**, ruta de directorio protegido (`C:\Program Files\...`) y control estricto de procesos hijos (`Deny all` o `Require rule to elevate`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semanal de tendencia de elevaciones y registro de cambios CAB de nuevas reglas EPM `[Decisión / Propuesta Editorial]`.

### S-02: Ejecución del Ciclo Semanal de Actualizaciones en Enterprise Application Management
- **Objetivo:** Mantener actualizado el parque de aplicaciones Win32 de terceros minimizando regresiones operativas mediante anillos controlados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Apps** > **Enterprise App Catalog apps with updates** `[Verificado MS Learn]`.
- **Rol Responsable:** Application Manager `[Verificado MS Learn]`.
- **Procedimiento Paso a Paso:**
  1. Revisar todas las aplicaciones del catálogo empresarial con actualizaciones pendientes no críticas acumuladas en la semana `[Verificado MS Learn]`.
  2. Para aplicaciones gestionadas por anillos, ejecutar **Guided update supersedence**, verificar comandos, códigos de retorno y reglas de detección preconfiguradas, y asignar primero al anillo Piloto (10 % de flota durante 72 horas) antes de promover a Producción `[Decisión / Propuesta Editorial]`.
  3. Para aplicaciones con **Auto-update** habilitado (asignación `Required`), auditar el informe de instalación por dispositivo verificando ausencia de bucles o conflictos de carrera (*race conditions*) con paquetes LOB preexistentes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de cumplimiento de versiones de aplicaciones del catálogo empresarial >= 95 % `[Decisión / Propuesta Editorial]`.

### S-03: Caza Transversal de Flota y Agrupación Dinámica con `Device query for multiple devices`
- **Objetivo:** Auditar proactivamente desviaciones de higiene técnica en toda la flota corporativa (Windows, macOS, iOS, Android Enterprise) y alimentar grupos de remediación `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Device query** `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar el catálogo semanal de consultas KQL multi-dispositivo: volúmenes sin protección (`EncryptableVolume | where ProtectionStatus != "PROTECTED" | join LogicalDrive on Device`), chips TPM deshabilitados (`Tpm | where Enabled != true`), parches QFE faltantes (`WindowsQfe`) e inventario de `Local AI Agent` `[Verificado MS Learn]`.
  2. Seleccionar **Add all items to a group** sobre los resultados anómalos para poblar directamente un grupo de seguridad de Microsoft Entra destinado a scripts de remediación o políticas de restricción `[Verificado MS Learn]`.
  3. Exportar resultados detallados a `.csv` (hasta 50.000 registros) para seguimiento de cierre con ingeniería de plataforma `[Verificado MS Learn]`.
- **Evidencia Auditable:** Archivo `.csv` exportado y membresía auditada del grupo de remediación generado desde `Device query` `[Verificado MS Learn]`.

### S-04: Supervisión de Ciclo de Vida Criptográfico y CRL en Microsoft Cloud PKI
- **Objetivo:** Prevenir interrupciones de autenticación Wi-Fi/VPN/CBA por certificados próximos a expirar y confirmar la frescura de las listas de revocación `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Cloud PKI** > seleccionar cada Issuing CA > **View all certificates** `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud PKI Authority Operator `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar en el dashboard de cada CA emisora el conteo de certificados `Active`, `Expired` y `Revoked`, filtrando certificados hoja que expiran en los próximos 30 días sin renovación SCEP completada `[Verificado MS Learn]`.
  2. Verificar que la publicación automática de la CRL (validez de 7 días con refresco cada 3,5 días) esté vigente y accesible desde los *relying parties* (controladoras Wi-Fi RADIUS/NPS, concentradores VPN y Microsoft Entra CBA) `[Verificado MS Learn]`.
  3. Identificar dispositivos dados de baja o estancados (> 45 días sin check-in) que conserven certificados activos y proceder a su revocación preventiva `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte semanal de certificados emitidos/revocados y validación HTTP de descarga del punto CDP `[Verificado MS Learn]`.

### S-05: Auditoría de Sesiones *Unattended Remote Sign-In* y Acceso No Enrolado en Remote Help
- **Objetivo:** Fiscalizar el uso de capacidades de alto privilegio en Remote Help para descartar accesos fuera de ventana autorizada `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Remote Help** > **Settings** y **Remote Help sessions** `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Internal Controls Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar el 100 % de las sesiones semanales de tipo **Unattended control: Remote sign-in** (Windows físico corporativo) y **Unattended control** (Android Enterprise dedicado), validando correspondencia 1:1 con órdenes de trabajo aprobadas `[Verificado MS Learn]`.
  2. Confirmar en `Settings` que la opción *Allow Remote Help to unenrolled devices* permanezca `Disabled` por defecto (o estrictamente controlada si existe excepción temporal aprobada) `[Verificado MS Learn]`.
  3. Verificar que las directivas de Acceso Condicional exijan MFA resistente a phishing y dispositivo conforme a todos los *Helpers* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz semanal de conciliación sesiones desatendidas vs. tickets ITSM (meta: 100 % conciliado) `[Decisión / Propuesta Editorial]`.

### S-06: Optimización de Salud de Batería, Rendimiento de Recursos y Arranque por *Device Scopes*
- **Objetivo:** Reducir fricción digital y reemplazar preventivamente hardware degradado antes de fallos críticos en usuarios clave `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Endpoint analytics** > **Battery health**, **Resource performance** y **Startup performance** `[Verificado MS Learn]`.
- **Rol Responsable:** Digital Employee Experience (DEX) Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Segmentar los informes por **Device scopes** (región, unidad de negocio o Scope Tag) e identificar modelos portátiles con capacidad máxima de carga < 60 % de la capacidad de diseño y alto conteo de ciclos `[Verificado MS Learn]`.
  2. Revisar en **Resource performance** y **Startup performance** procesos de terceros o GPOs heredadas que degraden CPU/RAM o añadan > 15 segundos al inicio de sesión `[Verificado MS Learn]`.
  3. Generar lista proactiva de reemplazo de batería/RAM o ajuste de configuración antes de que el usuario abra reclamo `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte DEX semanal por *Device scope* y órdenes preventivas de mantenimiento emitidas `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Conciliación Mensual de Vulnerabilidades de Aplicaciones (Defender TVM + EAM + Copilot Agent)
- **Objetivo:** Cerrar la brecha entre descubrimiento de vulnerabilidades en software de terceros y cobertura efectiva desde el catálogo de Enterprise App Management `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > **Vulnerability management** > **Software inventory** y `https://intune.microsoft.com` > **Agents** > **Vulnerability Remediation Agent** `[Verificado MS Learn]`.
- **Rol Responsable:** Vulnerability Management Lead + Application Manager `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar el **Vulnerability Remediation Agent** tras verificar permisos de su identidad agéntica con *Run Readiness Check* y extraer el ranking mensual de vulnerabilidades priorizadas por riesgo de brecha `[Verificado MS Learn]`.
  2. Cruzar el top 30 de aplicaciones vulnerables en el tenant contra las aplicaciones disponibles en el **Enterprise App Catalog**; migrar paquetes Win32 manuales hacia el catálogo gestionado siempre que exista equivalencia `[Decisión / Propuesta Editorial]`.
  3. Para aplicaciones de negocio ausentes del catálogo público y sin muro de pago, registrar o votar solicitud formal en el **Microsoft Feedback Portal** bajo la categoría *Enterprise App Management (Intune add-on)* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual de remediación TVM-Intune y porcentaje de aplicaciones críticas cubiertas por EAM `[Decisión / Propuesta Editorial]`.

### M-02: Higiene y Endurecimiento de Reglas de Elevación en Endpoint Privilege Management
- **Objetivo:** Prevenir acumulación de privilegios excesivos (*privilege creep*) en políticas de elevación de Windows `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Endpoint Privilege Management** > **Policies** y **Reusable settings** `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Privilege Manager + Security Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar todas las reglas configuradas con comportamiento `Automatic` o `Elevate as current user`, exigiendo justificación técnica vigente o degradándolas a `User confirmed` sobre cuenta virtual `[Verificado MS Learn]`.
  2. Verificar que el 100 % de las reglas basadas en certificado de editor (*Reusable settings*) incluyan restricción explícita de `File path` hacia directorios protegidos y nombres de binario específicos, evitando que un certificado corporativo o de proveedor permita elevar cualquier ejecutable firmado por ese mismo editor `[Verificado MS Learn]`.
  3. Confirmar que la respuesta predeterminada en *Windows elevation settings policy* continúe fijada en `Deny` o `Require support approval` sin conflictos entre políticas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario mensual firmado de reglas EPM y cero conflictos en *Elevation settings policy* `[Decisión / Propuesta Editorial]`.

### M-03: Auditoría de Postura BYOD y Controles en Microsoft Tunnel for MAM
- **Objetivo:** Validar que el acceso sin enrolamiento MDM mantenga aislamiento estricto de datos corporativos y resiliencia de infraestructura `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Microsoft Tunnel Gateway** y **Apps** > **App protection policies** `[Verificado MS Learn]`.
- **Rol Responsable:** Mobility Security Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar que los servidores Linux host del contenedor Microsoft Tunnel tengan aplicados parches mensuales de sistema operativo, motor de contenedores (Docker/Podman) y última imagen del gateway distribuida por Microsoft `[Verificado MS Learn]`.
  2. Auditar las directivas MAM (App Protection + App Configuration) asociadas a iOS y Android confirmando bloqueo de copia/pegado hacia apps personales, cifrado de datos de aplicación, requisito de PIN/biometría y **Strict Tunnel Mode** + *Identity switch* activos en Microsoft Edge `[Verificado MS Learn]`.
  3. En Android, validar que la integración con Microsoft Defender for Endpoint siga exigiendo estado de riesgo bajo/medio antes de establecer túnel `[Verificado MS Learn]`.
- **Evidencia Auditable:** Checklist mensual de parches de nodos Linux Tunnel y conformidad de políticas MAM `[Decisión / Propuesta Editorial]`.

### M-04: Gobierno de Licenciamiento M365 E3/E5/E7, Add-ons y Consumo SCU de Security Copilot
- **Objetivo:** Evitar sobrecostos por licencias duplicadas tras la inclusión de julio/agosto de 2026 y garantizar disponibilidad de unidades de cómputo (SCUs) para Copilot y sus agentes en Intune `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Tenant status** / **Intune add-ons** y `https://admin.microsoft.com` > **Billing** > **Licenses** `[Verificado MS Learn]`.
- **Rol Responsable:** IT FinOps + Intune Service Owner `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Conciliar asignaciones de licencias verificando que los usuarios cubiertos por **Microsoft 365 E5** o **M365 E7** no mantengan asignados SKUs add-on redundantes de EPM, Cloud PKI, EAM, Remote Help o Advanced Analytics, reasignando o reduciendo dichos add-ons hacia poblaciones F3/Business Premium si aplica `[Verificado MS Learn]`.
  2. Vigilar el vencimiento de cualquier suscripción trial activa (90 días + 30 días de gracia, máx. 250 usuarios) para evitar pérdida abrupta de visibilidad en consola `[Verificado MS Learn]`.
  3. Auditar el consumo mensual de **Security Compute Units (SCUs)** por consultas NL-to-KQL y ejecuciones del *Vulnerability Remediation Agent* y *Change Review Agent* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual FinOps de optimización de licencias Intune y utilización de SCUs `[Decisión / Propuesta Editorial]`.

### M-05: Evaluación Mensual de Cumplimiento contra *DISA STIG Audit Baseline*
- **Objetivo:** Medir objetivamente la desviación de endurecimiento técnico de los endpoints Windows corporativos frente al estándar STIG integrado en Advanced Analytics `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Reports** > **Endpoint analytics** / nodo de cumplimiento **STIG audit baseline** `[Verificado MS Learn]`.
- **Rol Responsable:** GRC / Endpoint Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar los resultados de auditoría del **STIG audit baseline** provisto por Intune Advanced Analytics identificando controles fallidos por categoría de sistema operativo `[Verificado MS Learn]`.
  2. Clasificar desviaciones entre brechas reales de política (a corregir en Settings Catalog / Endpoint Security) y excepciones operativas documentadas `[Decisión / Propuesta Editorial]`.
  3. Presentar la tendencia mensual de conformidad en el comité operativo de seguridad de endpoints `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte mensual exportado del *STIG audit baseline* y registro de excepciones vigentes `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Recertificación de Roles RBAC Granulares, *Scope Tags* y Administradores Sin Licencia
- **Objetivo:** Auditar el principio de mínimo privilegio administrativo en todas las capacidades avanzadas de Intune Suite `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Roles** > **All roles** y `https://entra.microsoft.com` > **Identity governance** > **Access reviews** `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Role Administrator + Identity Governance Lead `[Verificado MS Learn]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar campaña trimestral de *Access Reviews* sobre los grupos PIM asignados a `Endpoint Privilege Manager`, `EPM Elevation Approver`, `Cloud PKI Authority Operator`, `Remote Help Tiered Operator`, `Device Query & Analytics Hunter` y `Application Manager` `[Decisión / Propuesta Editorial]`.
  2. Verificar que los grupos de administradores sin licencia directa de Intune (*Unlicensed admins*) no superen los **1.000 miembros por grupo de seguridad** y carezcan de grupos anidados `[Verificado MS Learn]`.
  3. Validar que cada CA de Cloud PKI, política EPM y ámbito de Remote Help posea los **Scope Tags** regionales o departamentales correctos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Certificación trimestral de *Access Reviews* completada al 100 % y revocación de accesos obsoletos `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Simulacro de Revocación SCEP y Verificación de Cadena Cloud PKI / BYOCA
- **Objetivo:** Comprobar empíricamente que la revocación de un certificado hoja en Microsoft Cloud PKI bloquea de forma efectiva el acceso a Wi-Fi, VPN y Microsoft Entra CBA `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Cloud PKI** `[Verificado MS Learn]`.
- **Rol Responsable:** PKI Architect + Network Security Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. En un dispositivo de laboratorio representativo (Windows y móvil), emitir un certificado SCEP desde la CA emisora de Cloud PKI (y BYOCA si coexiste) y autenticar contra Wi-Fi 802.1X, VPN y Entra CBA `[Verificado MS Learn]`.
  2. Ejecutar la acción **Revoke** sobre el certificado hoja en Cloud PKI, verificando la actualización inmediata de la CRL publicada en el CDP hospedado por Intune `[Verificado MS Learn]`.
  3. Confirmar el rechazo efectivo de autenticación en todos los *relying parties* (ajustando cachés CRL en RADIUS/VPN si retienen listas vencidas) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe de prueba trimestral con marcas de tiempo de revocación, número de serie en CRL y denegación de acceso verificada `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Ejercicio Purple Team sobre Superficie de Privilegios, Soporte Remoto y BYOD Tunnel
- **Objetivo:** Validar controles preventivos y capacidad de detección del SOC frente a técnicas adversarias dirigidas contra EPM, Remote Help y Tunnel for MAM `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` y `https://security.microsoft.com` > **Investigation & response** > **Hunting** `[Verificado MS Learn]`.
- **Rol Responsable:** Red/Purple Team + SOC L3 Detection Engineering `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Simular en entorno controlado intentos de escape de procesos hijos desde aplicaciones elevadas por EPM (*LOLBins*, secuestro de DLL en rutas no protegidas o abuso de argumentos de línea de comandos) `[Verificado MS Learn]`.
  2. Simular inicio de sesión remoto no autorizado mediante Remote Help (*Unattended remote sign-in*) y verificar generación de alertas correlacionadas entre `IntuneAuditLogs` y `DeviceLogonEvents` en Defender XDR / Sentinel `[Decisión / Propuesta Editorial]`.
  3. En móvil Android de prueba, simular estado *rooted* y confirmar que Microsoft Defender marque el riesgo en `High` y corte inmediatamente las sesiones activas de Microsoft Tunnel for MAM `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe Purple Team semestral con matriz MITRE ATT&CK (`T1548`, `T1219`, `T1078`) y ajustes aplicados en reglas EPM y detecciones SIEM/XDR `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión Arquitectónica Anual de Jerarquía Cloud PKI y Hoja de Ruta de Retiro AD CS/NDES
- **Objetivo:** Gobernar la capacidad estructural (máximo 3 CAs mHSM por tenant), vigencia criptográfica de CAs raíz/emisoras y reducción de infraestructura PKI on-premises `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Cloud PKI** `[Verificado MS Learn]`.
- **Rol Responsable:** PKI Architect + Enterprise Security Architect + CISO `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar las fechas de expiración de las CAs Raíz y Emisoras de Cloud PKI / BYOCA, algoritmos de firma/hash (RSA 3072/4096 y SHA-384/SHA-512 recomendados para nuevas CAs) y ocupación del límite de **3 CAs por tenant** `[Verificado MS Learn]`.
  2. Confirmar que ninguna CA heredada creada durante fases de *trial* (claves por software) siga activa en producción `[Verificado MS Learn]`.
  3. Evaluar qué plantillas remanentes en AD CS / NDES / Intune Certificate Connector pueden migrarse hacia Cloud PKI para descomisionar servidores locales `[Verificado MS Learn]`.
- **Evidencia Auditable:** Documento anual de arquitectura PKI firmado por el CISO y plan de retiro de servidores NDES `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Respuesta ante Revocación de Versión Maliciosa o CVE 0-Day en Enterprise App Catalog
- **Disparador:** Notificación oficial de Microsoft en Intune Admin Center por retiro de versión comprometida en el Enterprise App Catalog o publicación de CVE 0-day activamente explotado en aplicación de terceros `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Device query** y **Apps** > **Windows** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Recordar que cuando Microsoft retira una versión maliciosa del catálogo (con hasta 1 hora de caché) o cuando opera *Auto-update*, **Intune no ejecuta desinstalación ni rollback automático**; la remediación en dispositivos afectados es responsabilidad del cliente `[Verificado MS Learn]`.
  2. Ejecutar inmediatamente `Device query for multiple devices` (y Advanced Hunting `DeviceTvmSoftwareInventory` en Defender XDR) para identificar todos los endpoints con la versión exacta comprometida y usar **Add all items to a group** para crear un grupo de contención `[Verificado MS Learn]`.
  3. Crear una regla **Deny** de emergencia en **Endpoint Privilege Management** por hash/certificado/versión para impedir que el instalador o binario afectado pueda elevarse `[Verificado MS Learn]`.
  4. Desplegar un paquete Win32 de desinstalación (`Uninstall` intent), *Guided update supersedence* hacia versión limpia o script de remediación proactiva sobre el grupo de contención, verificando erradicación mediante `Device query` individual `[Verificado MS Learn]`.
- **Evidencia Auditable:** Grupo de impacto, regla `Deny` EPM aplicada y tasa de erradicación verificada >= 99 % en 24 horas `[Decisión / Propuesta Editorial]`.

### AH-02: Contención de Emergencia ante Abuso de Regla de Elevación o Compromiso de Editor en EPM
- **Disparador:** Alerta de Defender for Endpoint / Sentinel detectando ejecución maliciosa hija o abuso de una aplicación elevada mediante Endpoint Privilege Management `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Endpoint security** > **Endpoint Privilege Management** > **Policies** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Aislar el dispositivo afectado en Microsoft Defender XDR si existe actividad adversaria activa y consultar con Single-Device `Device query` (o `EpmTools`: `Get-ElevationRules`, `Get-Policies`) qué regla específica permitió la elevación `[Verificado MS Learn]`.
  2. Crear y asignar con prioridad inmediata una regla EPM con `Elevation type = Deny` apuntando al hash SHA-256 o certificado afectado (recordando que `Deny` prevalece siempre sobre cualquier otra regla de usuario o dispositivo) `[Verificado MS Learn]`.
  3. Sincronizar políticas en la flota objetivo y auditar en el `Elevation report` todos los demás equipos donde se haya ejecutado esa regla en los últimos 30 días para ampliar el alcance forense del SOC `[Verificado MS Learn]`.
- **Evidencia Auditable:** Regla `Deny` desplegada, log de sincronización y reporte de alcance histórico en `Elevation report` `[Verificado MS Learn]`.

### AH-03: Revocación Inmediata de Certificados SCEP en Cloud PKI por Robo o Compromiso de Dispositivo
- **Disparador:** Reporte de robo/extravío de portátil o móvil corporativo, o confirmación de compromiso de identidad de dispositivo por el SOC `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Tenant administration** > **Cloud PKI** > `[Issuing CA]` > **View all certificates** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Localizar todos los certificados hoja `Active` asociados al dispositivo o usuario afectado en cada Issuing CA de Cloud PKI `[Verificado MS Learn]`.
  2. Seleccionar **Revoke**, elegir el código de motivo RFC 5280 (`Key Compromise` o `Cessation of Operation`) y confirmar la acción; verificar que Cloud PKI actualice instantáneamente la CRL en el punto CDP `[Verificado MS Learn]`.
  3. En paralelo, ejecutar `Wipe` / `Retire` o deshabilitar el objeto de dispositivo en Microsoft Entra ID y revocar sesiones de usuario (`Revoke sign-in sessions`) para invalidar tokens PRT existentes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Entrada de revocación en `Tenant administration > Audit logs` y estado `Revoked` visible en Cloud PKI `[Verificado MS Learn]`.

### AH-04: Investigación Forense en Vivo con `Device query` durante Incidente de Seguridad Activo
- **Disparador:** Necesidad del SOC L2/L3 de inspeccionar persistencia en registro, servicios, tareas, procesos o cuentas locales en uno o múltiples endpoints corporativos sin desplegar agentes adicionales `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **Windows** > `[Dispositivo]` > **Device Query** y **Devices** > **Device query** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Sobre el host investigado, ejecutar consultas KQL en vivo en `Process`, `WindowsService`, `WindowsRegistry` (rutas `Run`/`RunOnce` compatibles), `LocalGroup` y `Certificate` para confirmar indicadores de compromiso `[Verificado MS Learn]`.
  2. Recordar la limitación de seguridad documentada: si el usuario local posee permisos de administrador, podría alterar artefactos del cliente devueltos por `Device query`; contrastar siempre con telemetría kernel de Microsoft Defender for Endpoint `[Verificado MS Learn]`.
  3. Pivotar hacia `Device query for multiple devices` para medir prevalencia del artefacto en el resto del inventario corporativo y exportar evidencia `.csv` firmada para la cadena de custodia `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consultas KQL ejecutadas y exportación `.csv` incorporada al expediente del incidente en `security.microsoft.com` `[Decisión / Propuesta Editorial]`.

### AH-05: Recuperación Remota Segura vía Remote Help *Unattended Remote Sign-In*
- **Disparador:** Incidente operativo crítico o degradación de agente en un PC físico corporativo Windows donde no hay usuario presente y se requiere intervención interactiva auditada sin revelar contraseñas locales LAPS al usuario `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com` > **Devices** > **All devices** > `[Dispositivo]` > **New remote assistance session** > **Remote Help** > **Initiate unattended control** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Activar en PIM el rol personalizado con permiso *Unattended control* asociando el número de incidente crítico `[Decisión / Propuesta Editorial]`.
  2. Desde el registro del dispositivo físico corporativo en Intune, lanzar **New remote assistance session > Remote Help** e iniciar **Unattended remote sign-in**, autenticándose con las credenciales corporativas del administrador en una sesión Windows independiente y auditada `[Verificado MS Learn]`.
  3. Ejecutar la remediación requerida, cerrar formalmente la sesión seleccionando **Leave** y verificar el registro completo de inicio/fin en los logs de auditoría de Remote Help `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de sesión desatendida en Remote Help correlacionado con activación PIM e incidente crítico `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Device Query y PowerShell / Graph

#### Consulta 1 — Intune Multi-Device `Device query` (KQL): Detección de Flota con Discos No Protegidos o TPM Deshabilitado
- **Plataforma / Ruta:** `intune.microsoft.com > Devices > Device query` `[Verificado MS Learn]`.
- **Propósito:** Identificar dispositivos corporativos con volúmenes sin protección criptográfica cruzando `EncryptableVolume` y `LogicalDrive` mediante la sintaxis vigente `on Device` `[Verificado MS Learn]`.
```kql
// Intune Device query for multiple devices (KQL oficial soportado a nov-2026)
// Nota: Joins con 'on Device.DeviceId' estan retirados; usar siempre 'on Device'
EncryptableVolume
| where ProtectionStatus != "PROTECTED"
| join LogicalDrive on Device
| project Device, DriveLetter, ProtectionStatus, EncryptionMethod, VolumeType, FreeSpaceBytes, SizeBytes
```

#### Consulta 2 — Intune Single-Device `Device query` (KQL en Tiempo Real sobre WNS): Auditoría de Administradores Locales y Procesos Sospechosos
- **Plataforma / Ruta:** `intune.microsoft.com > Devices > Windows > [Dispositivo] > Device Query` `[Verificado MS Learn]`.
- **Propósito:** Verificar en vivo membresías residuales del grupo local `Administrators` durante el despliegue de EPM para erradicar elevaciones no gestionadas (*unmanaged elevations*) `[Verificado MS Learn]`.
```kql
// Intune Single-device Device Query en vivo (requiere permiso RBAC Managed Devices/Query y WNS activo)
// Importante: usar comillas simples en operadores contains / startswith en el editor Device Query
LocalGroup
| where GroupName contains 'Administrators'
| project GroupName, GroupSid, Members, MemberCount
```

#### Consulta 3 — Intune Multi-Device `Device query` (KQL): Degradación Severa de Salud de Batería en Flota Portátil
- **Plataforma / Ruta:** `intune.microsoft.com > Devices > Device query` `[Verificado MS Learn]`.
- **Propósito:** Detectar equipos portátiles cuya capacidad de carga completa haya caído por debajo del 60 % de la capacidad de diseño para reemplazo preventivo DEX `[Verificado MS Learn]`.
```kql
// Intune Device query for multiple devices - Salud preventiva de baterias
Battery
| project Device, Manufacturer, Model, SerialNumber, CycleCount, DesignedCapacity, FullChargedCapacity,
          FullChargedCapacityPercent = (FullChargedCapacity * 100) / DesignedCapacity
| where FullChargedCapacityPercent < 60
| order by FullChargedCapacityPercent asc
```

#### Consulta 4 — Microsoft Sentinel / Log Analytics (KQL sobre `IntuneAuditLogs`): Auditoría de Acciones Críticas en EPM, Cloud PKI y Remote Help
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` / Log Analytics (`IntuneAuditLogs`) `[Verificado MS Learn]`.
- **Propósito:** Auditar creaciones/modificaciones de políticas EPM, revocaciones/creaciones en Cloud PKI y cambios de configuración en Remote Help ejecutados por administradores `[Verificado MS Learn]`.
```kql
// Requiere conector Diagnostic Settings de Intune enviando AuditLogs a Log Analytics / Sentinel
IntuneAuditLogs
| where TimeGenerated > ago(7d)
| where Category in ("EndpointPrivilegeManagement", "CloudPKI", "RemoteHelp", "Role")
   or OperationName has_any ("Elevation", "CertificateAuthority", "Revoke", "RemoteHelp")
| extend Actor = tostring(parse_json(Identity).Upn)
| project TimeGenerated, Category, OperationName, ResultType, Actor, TargetDisplayNames, Properties
| order by TimeGenerated desc
```

#### Consulta 5 — Microsoft Defender XDR Advanced Hunting (KQL sobre `DeviceProcessEvents`): Caza de Procesos Hijos Riesgosos Nacidos de Elevación EPM
- **Plataforma / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Propósito:** Detectar abuso o escape desde aplicaciones elevadas por el agente EPM que lancen shells, intérpretes de scripts o herramientas de descarga (*LOLBins*) `[Decisión / Propuesta Editorial]`.
```kql
// Correlacion en Defender XDR de procesos lanzados por el servicio/agente EPM hacia interpretes sensibles
DeviceProcessEvents
| where Timestamp > ago(7d)
| where InitiatingProcessFileName has_any ("EpmService.exe", "EpmAgent", "epm")
   or InitiatingProcessFolderPath startswith @"C:\Program Files\Microsoft EPM Agent"
| where FileName in~ ("powershell.exe", "pwsh.exe", "cmd.exe", "mshta.exe", "rundll32.exe", "regsvr32.exe", "certutil.exe", "wscript.exe")
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, InitiatingProcessCommandLine, FileName, ProcessCommandLine, SHA256
| order by Timestamp desc
```

#### Consulta 6 — PowerShell Local (`EpmTools`): Diagnóstico de Políticas WinDC y Extracción de Atributos/Certificados para Reglas EPM
- **Plataforma / Ruta:** PowerShell x64 en endpoint Windows gestionado con EPM (`C:\Program Files\Microsoft EPM Agent\EpmTools\EpmCmdlets.dll`) `[Verificado MS Learn]`.
- **Propósito:** Diagnosticar recepción efectiva de políticas WinDC de EPM y extraer el hash y certificados Publisher/CA exactos de un ejecutable antes de publicar una regla `[Verificado MS Learn]`.
```powershell
# Importar modulo oficial EpmTools (en Windows on Arm64 usar Windows PowerShell x64)
Import-Module 'C:\Program Files\Microsoft EPM Agent\EpmTools\EpmCmdlets.dll'

# Verificar estado efectivo de ClientSettings y analisis de documentos WinDC procesados
Get-ClientSettings
Get-DeclaredConfigurationAnalysis

# Extraer atributos de archivo y certificados Publisher/CA para construir regla EPM segura
Get-FileAttributes -FilePath 'C:\Program Files\VendorApp\Updater.exe' -CertOutputPath 'C:\ProgramData\Microsoft\EPMCerts'
```

#### Consulta 7 — Microsoft Graph PowerShell: Inventario de Políticas EPM y Autoridades Cloud PKI vía Graph Beta
- **Plataforma / Ruta:** Microsoft Graph PowerShell SDK (`DeviceManagementConfiguration.Read.All`) `[Verificado MS Learn]`.
- **Propósito:** Auditar programáticamente las políticas de configuración declarativa de EPM y las autoridades certificadoras dadas de alta en el tenant para evidencia GRC `[Verificado MS Learn]`.
```powershell
Connect-MgGraph -Scopes "DeviceManagementConfiguration.Read.All", "DeviceManagementManagedDevices.Read.All"

# Listar politicas de configuracion en Intune vinculadas a Endpoint Privilege Management
$epmPolicies = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/deviceManagement/configurationPolicies?`$filter=technologies eq 'mdm,endpointPrivilegeManagement'"
$epmPolicies.value | Select-Object id, name, lastModifiedDateTime, isAssigned

# Consultar autoridades certificadoras registradas en Microsoft Cloud PKI
$cloudCAs = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/deviceManagement/cloudCertificationAuthority"
$cloudCAs.value | Select-Object id, commonName, cloudCertificationAuthorityType, certificationAuthorityStatus, validityEndDateTime
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Pilar de Intune Suite | Indicador Técnico de *Proof of Life* | Método de Verificación Rápida | Estado Esperado en Producción |
| :--- | :--- | :--- | :--- |
| **Endpoint Privilege Management** | Carpeta `C:\Program Files\Microsoft EPM Agent`, menú contextual *Run with elevated access* y telemetría en `Elevation report` `[Verificado MS Learn]`. | Ejecutar `Get-ClientSettings` en `EpmTools` y verificar `Elevation report` con datos < 24 h `[Verificado MS Learn]`. | Agente activo, respuesta por defecto `Deny` o `Support approved` y cero conflictos de política `[Verificado MS Learn]`. |
| **Microsoft Cloud PKI** | CA Raíz/Emisora en estado `Active` con claves **Azure Managed HSM** (no trial software keys) y emisión SCEP exitosa `[Verificado MS Learn]`. | Revisar `Tenant administration > Cloud PKI` y probar URL HTTP de descarga de CRL/AIA `[Verificado MS Learn]`. | <= 3 CAs HSM activas, CRL refrescada cada 3,5 días y tasa de éxito SCEP >= 98 % `[Verificado MS Learn]`. |
| **Enterprise Application Management** | Aplicaciones desplegadas desde el catálogo hospedado `*.manage.microsoft.com` y reporte de actualizaciones poblado `[Verificado MS Learn]`. | Abrir `Apps > Enterprise App Catalog apps with updates` y `Managed Apps` por dispositivo `[Verificado MS Learn]`. | Catálogo sincronizado con aplicaciones críticas en última versión o en anillo piloto vigente `[Decisión / Propuesta Editorial]`. |
| **Remote Help** | Tenant habilitado, RBAC escalonado, Acceso Condicional MFA activo y sesiones registradas en monitor/auditoría `[Verificado MS Learn]`. | Revisar `Tenant administration > Remote Help > Monitor` y `Audit logs` `[Verificado MS Learn]`. | 100 % de sesiones autenticadas en Entra ID y soporte a equipos no enrolados deshabilitado `[Verificado MS Learn]`. |
| **Intune Advanced Analytics** | Informes `Anomalies`, `Battery health`, `Device timeline` activos y `Device query` individual/multi-dispositivo respondiendo `[Verificado MS Learn]`. | Ejecutar consulta KQL de prueba en `Devices > Device query` y sobre un host Windows con WNS activo `[Verificado MS Learn]`. | Properties catalog desplegado en Windows y consultas KQL respondiendo sin error de WNS `[Verificado MS Learn]`. |
| **Microsoft Tunnel for MAM** | Nodos Linux `Online`, apps móviles iOS/Android conectando sin enrolamiento MDM y *Strict Tunnel Mode* activo `[Verificado MS Learn]`. | Verificar `Tenant administration > Microsoft Tunnel Gateway > Health status` `[Verificado MS Learn]`. | Gateways saludables con TLS vigente y bloqueo automático de equipos Android *rooteados* `[Verificado MS Learn]`. |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales (`KPI-01` a `KPI-08`)

> Todos los umbrales numéricos, metas porcentuales y ventanas SLA siguientes constituyen objetivos de excelencia operacional sugeridos `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Tasa de Endpoints Windows sin Administradores Locales Permanentes** | `(Endpoints Windows corporativos operando 100 % como Standard User con EPM / Total endpoints Windows corporativos) * 100` | `>= 98 %` | Mensual | CISO / Endpoint Engineering Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Proporción de Elevaciones Gestionadas vs. No Gestionadas (EPM)** | `(Managed elevations registradas en EPM / Total de elevaciones Managed + Unmanaged) * 100` | `>= 99 %` (`< 1 %` Unmanaged) | Semanal | SOC Manager / Endpoint Privilege Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tiempo Medio de Resolución de Solicitudes JIT `Support approved` (EPM)** | `Promedio(Timestamp decisión Approve/Deny - Timestamp envío de solicitud por usuario) en horario hábil` | `<= 30 minutos` | Diaria / Semanal | Help Desk Manager / SOC L1-L2 | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Cumplimiento de Parcheo de Aplicaciones del Enterprise App Catalog (CVEs Críticos/Altos)** | `(Dispositivos actualizados a la versión parcheada del catálogo dentro de 7 días / Dispositivos con la app instalada) * 100` | `>= 95 %` en 7 días (`>= 99 %` en 48 h para 0-day) | Semanal | CISO / Vulnerability Management Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa de Éxito de Emisión y Renovación SCEP en Microsoft Cloud PKI** | `(Certificados hoja SCEP emitidos o renovados sin error / Total de solicitudes CSR procesadas por Cloud PKI RA) * 100` | `>= 99 %` | Semanal | PKI Architect / Network Security Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Conformidad de Sesiones Remote Help Auditadas y Conciliadas con Ticket** | `(Sesiones Remote Help con Elevation o Unattended vinculadas a ticket ITSM válido / Total sesiones privilegiadas Remote Help) * 100` | `100 %` | Semanal | Internal Audit / Help Desk Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tasa de Resolución en Primer Contacto mediante `Device query` sin Control Remoto** | `(Tickets de diagnóstico L1/L2 resueltos con Device Query + acción remota / Total tickets de diagnóstico elegibles) * 100` | `>= 45 %` | Mensual | IT Operations Director / DEX Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Disponibilidad y Salud Criptográfica de Nodos Microsoft Tunnel for MAM** | `(Tiempo operativo de sitios Microsoft Tunnel con TLS vigente y sin fallos de salud / Tiempo total del mes) * 100` | `>= 99,9 %` | Mensual | Mobility Lead / Infrastructure Manager | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de 5 Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Verificables |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Fragmentado** | Usuarios Windows conservan permisos de administrador local; soporte remoto mediante herramientas no integradas a Entra ID; empaquetado Win32 manual reactivo; AD CS/NDES local sin monitoreo centralizado; licencias M365 E5 desaprovechadas tras julio/agosto de 2026. |
| **Nivel 2** | **Básico / Piloto** | EPM desplegado en modo auditoría/reporte en grupos piloto; Remote Help habilitado a nivel tenant pero con roles RBAC amplios; primeras aplicaciones migradas al Enterprise App Catalog; uso esporádico de Single-Device `Device query`. |
| **Nivel 3** | **Definido / Estandarizado** | Usuarios estándar impuestos en la flota general con reglas EPM `User confirmed` / `Support approved` y respuesta por defecto `Deny`; Cloud PKI en producción con claves Azure mHSM emitiendo SCEP para Wi-Fi/VPN; *Guided update supersedence* semanal en EAM; RBAC escalonado en Remote Help. |
| **Nivel 4** | **Gestionado Cuantitativamente** | `Unmanaged elevations` < 1 %; *Multi-device Device query* automatizado con *Add all items to a group* para remediación continua; Cloud PKI integrado con Microsoft Entra CBA resistente a phishing; Tunnel for MAM con *Strict Tunnel Mode* y bloqueo por riesgo MDE en BYOD; KPIs auditados semanalmente. |
| **Nivel 5** | **Optimizado / Agéntico Zero Trust** | Operación aumentada con Security Copilot (*Vulnerability Remediation Agent* priorizando EAM, *Change Review Agent* auditando scripts en *Multi Admin Approval* y evaluación de amenazas en solicitudes EPM); descomisionamiento completo de NDES heredado; ejercicios Purple Team semestrales y conformidad continua STIG. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

El mapeo siguiente cubre las **6 funciones de NIST CSF 2.0 (CSWP 29)** vinculando capacidades oficiales de Microsoft Intune Suite con evidencia auditable reproducible `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Subcategoría Oficial | Descripción del Resultado (CSWP 29) | Capacidad Habilitadora en Microsoft Intune Suite + MITRE ATT&CK | Evidencia Auditable Reproducible |
| :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OV-03` | El desempeño de la gestión de riesgos de ciberseguridad se evalúa y revisa para realizar ajustes. | Conciliación mensual de adopción de capacidades M365 E5 / Intune Suite, auditoría *STIG audit baseline* en Advanced Analytics y seguimiento de KPIs `[Verificado MS Learn]`. | Informe mensual ejecutivo de KPIs y exportación de conformidad *STIG audit baseline* `[Decisión / Propuesta Editorial]`. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad se establecen, comunican y aplican. | Segregación RBAC granular en Intune (`Endpoint Privilege Manager`, `Help Desk Operator`, roles custom Cloud PKI/Remote Help/Device Query), *Scope Tags* y *Multi Admin Approval* con *Change Review Agent* (`T1078`) `[Verificado MS Learn]`. | Configuración exportada de roles Intune RBAC, logs de *Multi Admin Approval* y certificaciones trimestrales de *Access Reviews* `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.AM-01` | Se mantienen inventarios de hardware gestionado por la organización. | Inventario transversal con `Device query for multiple devices` (`Cpu`, `BiosInfo`, `Tpm`, `Battery`, `SystemEnclosure`, `Local AI Agent`) en Windows, macOS, iOS y Android Enterprise `[Verificado MS Learn]`. | Exportación `.csv` (hasta 50.000 registros) de `Device query` y política activa de *Properties catalog* `[Verificado MS Learn]`. |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican, validan y registran las vulnerabilidades en los activos. | Correlación continua entre **Enterprise Application Management**, **Defender Vulnerability Management** y el **Vulnerability Remediation Agent** (`T1190`, `T1203`) `[Verificado MS Learn]`. | Sugerencias registradas del *Vulnerability Remediation Agent* y vista *Enterprise App Catalog apps with updates* `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.AA-03` | Los usuarios, servicios y hardware son autenticados. | Emisión de certificados hoja SCEP desde **Microsoft Cloud PKI** (claves en Azure Managed HSM o BYOCA) para Wi-Fi 802.1X, VPN y **Microsoft Entra CBA** (`T1556`, `T1539`) `[Verificado MS Learn]`. | Jerarquía Cloud PKI activa en `Tenant administration > Cloud PKI`, perfiles SCEP asignados y CRL vigente `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen e incorporan el principio de mínimo privilegio y separación de funciones. | **Endpoint Privilege Management (EPM)**: eliminación de administradores locales, elevación JIT en cuenta virtual aislada, validación de hash/certificado/ruta y control de procesos hijos (`T1548.002`, `T1068`) `[Verificado MS Learn]`. | Políticas *Elevation settings* (`Deny` / `Support approved`) y *Elevation rules* junto con el *Elevation report* `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.PS-02` | El software se mantiene, reemplaza y elimina de forma acorde al riesgo. | Despliegue y actualización ágil desde el **Enterprise App Catalog** mediante *Guided update supersedence* por anillos o *Auto-update* (SLO de 24 h para el 80–90 % de actualizaciones) `[Verificado MS Learn]`. | Reporte *Managed Apps* y registros de despliegue de paquetes *supersedence* en Intune `[Verificado MS Learn]`. |
| **PROTECT (PR)** | `PR.IR-01` | Las redes y entornos son protegidos contra accesos lógicos no autorizados y usos indebidos. | **Microsoft Tunnel for MAM** para BYOD iOS/Android sin enrolamiento MDM, *Strict Tunnel Mode* en Microsoft Edge y corte automático ante detección de *root* por Defender en Android (`T1133`) `[Verificado MS Learn]`. | Configuración de *Tunnel Sites*, políticas de configuración de Edge y políticas de protección MAM `[Verificado MS Learn]`. |
| **DETECT (DE)** | `DE.AE-03` | Se correlaciona información de múltiples fuentes para detectar eventos adversos o anomalías. | Motor de **Anomalies** en Intune Advanced Analytics (grupos de correlación de BSODs y cierres de aplicaciones) y correlación KQL de `IntuneAuditLogs` + `DeviceProcessEvents` en Sentinel/Defender XDR `[Verificado MS Learn]`. | Reportes de anomalías con grupos de correlación y reglas analíticas activas sobre `IntuneAuditLogs` `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.CM-03` | Las actividades del personal y el uso de tecnología son monitoreados para encontrar eventos potencialmente adversos. | Auditoría integral de sesiones **Remote Help** (incluyendo *Elevation*, *Unattended remote sign-in* y *Compliance warnings*) y reporte de *Managed vs. Unmanaged elevations* en EPM (`T1219`) `[Verificado MS Learn]`. | Registros en `Tenant administration > Remote Help > Monitor` y `Tenant administration > Audit logs` `[Verificado MS Learn]`. |
| **RESPOND (RS)** | `RS.AN-03` | Se realiza análisis para establecer qué ha ocurrido durante un incidente y la causa raíz. | Inspección forense en tiempo real con Single-Device `Device query` (WNS) sobre `Process`, `WindowsService`, `WindowsRegistry` y `WindowsEvent`, más barrido de flota en Multi-Device `Device query` `[Verificado MS Learn]`. | Consultas KQL ejecutadas y evidencia `.csv` adjunta al expediente de respuesta a incidentes `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.RP-03` | La integridad de copias de seguridad y otros activos de restauración se verifica antes de usarlos para la recuperación. | Revocación inmediata de certificados hoja comprometidos en **Cloud PKI**, bloqueo `Deny` en **EPM** y remediación remota auditada mediante **Remote Help Unattended Remote Sign-In** sobre PCs físicos corporativos `[Verificado MS Learn]`. | Trazas de revocación en CRL, confirmación de sesión desatendida cerrada y verificación post-recuperación con `Device query` `[Decisión / Propuesta Editorial]`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta de Formación Oficial Microsoft Learn / Ninja | Comunidad Técnica / MVPs de Referencia | Certificación Vigente (Nov 2026) |
| :--- | :--- | :--- | :--- |
| **Endpoint Engineering Lead / Intune Admin** | Ruta *Explore the Microsoft Intune Suite* en Microsoft Learn; documentación oficial de EPM, Cloud PKI y Enterprise App Management; *Microsoft Intune Ninja Training* `[Verificado MS Learn]`. | Peter van der Woude (*All about Microsoft Intune — Intune Suite series*), Rudy Ooms (*Call4Cloud — EPM & WinDC internals*) `[Verificado MS Learn]`. | **Microsoft 365 Certified: Endpoint Administrator Associate (MD-102)** `[Verificado MS Learn]`. |
| **PKI & Identity Security Architect** | Módulos oficiales de *Microsoft Cloud PKI deployment models (Cloud Root vs. BYOCA)* y *Microsoft Entra Certificate-Based Authentication (CBA)* `[Verificado MS Learn]`. | Niklas Tinner (*Oceanleaf — Cloud PKI architecture*), Joery Van den Bosch (*IntuneStuff*) `[Verificado MS Learn]`. | **Microsoft Certified: Identity and Access Administrator Associate (SC-300)** + **Cybersecurity Architect Expert (SC-100)** `[Verificado MS Learn]`. |
| **SOC L1 / L2 & Threat Hunter** | Guías oficiales de *Device query (single & multiple devices)*, sintaxis KQL en Intune, *Security Copilot in Intune* y caza sobre `IntuneAuditLogs` `[Verificado MS Learn]`. | Jannik Reinhard y Sander Rozemuller (automatización Graph/KQL en Intune Suite) `[Verificado MS Learn]`. | **Microsoft Certified: Security Operations Analyst Associate (SC-200)** `[Verificado MS Learn]`. |
| **Help Desk Lead & DEX Specialist** | Guías operativas de *Remote Help* (RBAC, Acceso Condicional, *Unattended remote sign-in*) e *Intune Advanced Analytics* (*Anomalies*, *Device timeline*, *Battery health*) `[Verificado MS Learn]`. | Simon Skotheimsvik y Jeroen Burgerhout (operación de Intune Suite y Windows 365) `[Verificado MS Learn]`. | **MD-102: Endpoint Administrator Associate** `[Verificado MS Learn]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Verificaciones Técnicas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Verificada | Hallazgo Técnico Oficial a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **Inclusión de capacidades de Intune Suite en M365 E3 y M365 E5 (CY26 Q3)** | Confirmado en Microsoft Intune Blog oficial (4-dic-2025 y 18-jun-2026) y páginas de licenciamiento: desde el **1 de julio de 2026** (despliegue a clientes existentes hacia el **1 de agosto de 2026**), **EMS E3 / M365 E3** incluye *Remote Help*, *Advanced Analytics* e *Intune Plan 2* (*Tunnel for MAM*, *Specialty devices*, *FOTA*); **Microsoft 365 E5** añade además **Endpoint Privilege Management**, **Microsoft Cloud PKI**, **Enterprise Application Management** y **Microsoft Security Copilot** `[Verificado MS Learn]`. | Documentado con exactitud en Portada, Sección 2.2 y cadencia FinOps `M-04` para evitar compras duplicadas de add-ons en poblaciones E5. |
| **2** | **Lanzamiento de Microsoft 365 E7 y reorganización documental de Intune Learn** | **Microsoft 365 E7 ("The Frontier Suite")** alcanzó GA el **1 de mayo de 2026** integrando M365 E5, Entra Suite, M365 Copilot y Agent 365. Además, Microsoft migró las rutas canónicas de Learn hacia `/en-us/intune/epm/`, `/en-us/intune/cloud-pki/`, `/en-us/intune/remote-help/`, `/en-us/intune/advanced-analytics/` y `/en-us/intune/app-management/deployment/` `[Verificado MS Learn]`. | Todas las referencias y enlaces se actualizaron a las URLs canónicas vigentes en noviembre de 2026. |
| **3** | **Nuevas capacidades EPM: `Elevate as current user`, ajustes de red y precedencia** | EPM incorporó el tipo de elevación **Elevate as current user** (junto a *Automatic*, *User confirmed*, *Support approved* y *Deny*), soporte de ajustes de sistema (como configuración de red IPv4/IPv6/DNS vía Company Portal incluso offline) y reglas deterministas de resolución de conflictos `[Verificado MS Learn]`. | Incorporado en Sección 3 y en la revisión mensual `M-02` para restringir `Elevate as current user` solo a excepciones de compatibilidad. |
| **4** | **Límites arquitectónicos e inmutabilidad de claves en Microsoft Cloud PKI** | Se verificó el límite estricto de **3 CAs por tenant**, validez CRL de **7 días** con refresco cada **3,5 días**, respaldo en **Azure Managed HSM** para licencias pagas/incluidas e imposibilidad de convertir claves software creadas durante un *trial* hacia HSM `[Verificado MS Learn]`. | Reflejado como advertencia crítica de arquitectura en Sección 3.2 y auditoría anual `A-01`. |
| **5** | **Auto-update vs. Guided Update Supersedence y SLOs en EAM** | Documentación actualizada el **3 de noviembre de 2026** confirma **Auto-update** para asignaciones `Required` en Enterprise App Catalog (sin anillos, sin rollback automático y con caché de hasta 1 h ante revocaciones) y SLO de **24 horas** para el 80–90 % de actualizaciones `[Verificado MS Learn]`. | Incorporado en Sección 3.2, cadencia semanal `S-02` y playbook de emergencia `AH-01`. |
| **6** | **Remote Help *Unattended Remote Sign-In* y Device Query Multi-Dispositivo** | Remote Help soporta **Unattended control: Remote sign-in** (sesión Windows separada y autenticada en PCs físicos corporativos); `Device query for multiple devices` soporta Windows, macOS, iOS y Android Enterprise con acción directa **Add all items to a group** y retiro de `on Device.DeviceId` en favor de `on Device` `[Verificado MS Learn]`. | Reflejado en `S-03`, `S-05`, `AH-05` y en las consultas KQL verificadas de la Sección 10. |
| **7** | **Agentes de Security Copilot en Intune (Preview / GA 2026)** | Intune incorpora en el nodo `Agents` el **Vulnerability Remediation Agent** y el **Change Review Agent** (evaluación asistida por IA de scripts PowerShell bajo *Multi Admin Approval*) `[Verificado MS Learn]`. | Integrado en `D-05`, `D-08` y `M-01`. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Definido | Tipo | Justificación Arquitectónica y Operativa |
| :--- | :--- | :--- | :--- |
| **1** | **SLAs operativos y umbrales numéricos de `KPI-01` a `KPI-08`** | `Propuesta Editorial` | Microsoft Learn documenta los SLOs del catálogo EAM (24 h / 7 días) y límites técnicos, pero no impone SLAs internos al cliente (como `<= 30 min` para aprobar EPM o `>= 98 %` de usuarios estándar). Se establecen metas exigentes alineadas a Zero Trust `[Decisión / Propuesta Editorial]`. |
| **2** | **Segregación de roles personalizados (EPM Approver vs. Policy Author, L1/L2/L3 Remote Help)** | `Propuesta Editorial` | Aunque el rol integrado `Endpoint Privilege Manager` agrupa autoría y aprobación, separar quién aprueba solicitudes JIT diarias de quién crea reglas permanentes `Automatic` mitiga abuso interno y satisface auditoría SOX/ISO/NIST `[Decisión / Propuesta Editorial]`. |
| **3** | **Política híbrida en EAM (*Guided Supersedence* para apps críticas vs. *Auto-update* para utilidades)** | `Propuesta Editorial` | Dado que *Auto-update* carece de anillos de despliegue y rollback automático, usar *Guided update supersedence* con anillo piloto de 72 h en agentes/herramientas críticas equilibra velocidad de parcheo y estabilidad operativa `[Decisión / Propuesta Editorial]`. |
| **4** | **Ventanas máximas de activación PIM (2 h a 4 h) y conciliación 100 % de sesiones desatendidas** | `Propuesta Editorial` | Microsoft recomienda PIM y RBAC de mínimo privilegio pero deja la duración de activación a criterio de gobierno del cliente; acotar a 2–4 h reduce drásticamente la ventana de exposición de tokens administrativos `[Decisión / Propuesta Editorial]`. |
| **5** | **Modelo de madurez de 5 niveles y mapeo probatorio NIST CSF 2.0** | `Propuesta Editorial` | Estructura consultiva diseñada para permitir a CISOs y auditores internos evaluar progresión desde administración tradicional hacia operaciones Zero Trust asistidas por agentes IA `[Decisión / Propuesta Editorial]`. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Microsoft Intune advanced capabilities (Intune Suite & Add-ons overview)*: `https://learn.microsoft.com/en-us/intune/fundamentals/advanced-capabilities` `[Verificado MS Learn]`
- **REF-02:** Microsoft Learn — *Microsoft Intune Licensing Plans and Options (Plan 1, Plan 2, Intune Suite, Unlicensed Admins)*: `https://learn.microsoft.com/en-us/intune/fundamentals/licensing` `[Verificado MS Learn]`
- **REF-03:** Microsoft Learn — *Plan and Prepare for Endpoint Privilege Management (EPM) Deployment*: `https://learn.microsoft.com/en-us/intune/epm/deployment-planning` `[Verificado MS Learn]`
- **REF-04:** Microsoft Learn — *Microsoft Cloud PKI for Microsoft Intune (Architecture, mHSM, CRL & Limits)*: `https://learn.microsoft.com/en-us/intune/cloud-pki/` `[Verificado MS Learn]`
- **REF-05:** Microsoft Learn — *Deployment models for Microsoft Intune Cloud PKI (Cloud Root vs. BYOCA)*: `https://learn.microsoft.com/en-us/intune/cloud-pki/deployment-models` `[Verificado MS Learn]`
- **REF-06:** Microsoft Learn — *Configure Microsoft Cloud PKI root and issuing CA for Microsoft Intune*: `https://learn.microsoft.com/en-us/intune/cloud-pki/configure-ca` `[Verificado MS Learn]`
- **REF-07:** Microsoft Learn — *Microsoft Intune Enterprise Application Management (Catalog, SLOs & Auto-update)*: `https://learn.microsoft.com/en-us/intune/app-management/deployment/enterprise-app-management` `[Verificado MS Learn]`
- **REF-08:** Microsoft Learn — *Guided Update Supersedence for Enterprise App Management*: `https://learn.microsoft.com/en-us/intune/app-management/deployment/update-enterprise-supersedence` `[Verificado MS Learn]`
- **REF-09:** Microsoft Learn — *Use Remote Help to Assist Users Authenticated by your Organization*: `https://learn.microsoft.com/en-us/intune/remote-help/` `[Verificado MS Learn]`
- **REF-10:** Microsoft Learn — *Advanced Analytics Overview in Microsoft Intune*: `https://learn.microsoft.com/en-us/intune/advanced-analytics/` `[Verificado MS Learn]`
- **REF-11:** Microsoft Learn — *Device Query (Single-Device Real-Time KQL)*: `https://learn.microsoft.com/en-us/intune/advanced-analytics/device-query` `[Verificado MS Learn]`
- **REF-12:** Microsoft Learn — *Device Query for Multiple Devices (Fleet-Wide KQL & Group Creation)*: `https://learn.microsoft.com/en-us/intune/advanced-analytics/device-query-multiple-devices` `[Verificado MS Learn]`
- **REF-13:** Microsoft Learn — *Learn about using Microsoft Tunnel with Mobile Application Management (MAM)*: `https://learn.microsoft.com/en-us/intune/device-security/microsoft-tunnel/mam` `[Verificado MS Learn]`
- **REF-14:** Microsoft Learn — *Security Copilot Agents in Intune: Vulnerability Remediation Agent & Change Review Agent*: `https://learn.microsoft.com/en-us/intune/copilot/agents/manage-vulnerability-remediation-agent` y `https://learn.microsoft.com/en-us/intune/copilot/agents/change-review-agent` `[Verificado MS Learn]`

### Blogs Oficiales y Empleados Microsoft
- **REF-15:** Microsoft Intune Blog — *Microsoft 365 adds advanced Microsoft Intune solutions at scale (E3 & E5 Packaging Update)*: `https://techcommunity.microsoft.com/blog/microsoftintuneblog/microsoft-365-adds-advanced-microsoft-intune-solutions-at-scale/4474272` `[Verificado MS Learn]`
- **REF-16:** Lior Bela (Microsoft) — *IT experts weigh in: Advanced Intune capabilities coming to Microsoft 365 E3 and E5 (Effective July 1 / August 1, 2026)*: `https://techcommunity.microsoft.com/blog/microsoftintuneblog/it-experts-weigh-in-advanced-intune-capabilities-coming-to-microsoft-365-e3-and-/4516898` `[Verificado MS Learn]`

### Comunidad Técnica y MVPs de Seguridad / Endpoint Management
- **REF-17:** Peter van der Woude (Microsoft MVP) — *All about Microsoft Intune: Microsoft Intune Suite Series (EPM, Cloud PKI & Remote Help Web App)*: `https://petervanderwoude.nl/post/category/microsoft-intune-suite/`
- **REF-18:** Rudy Ooms (Microsoft MVP, Call4Cloud) — *Manage system settings with Endpoint Privilege Management & WinDC Internals*: `https://call4cloud.nl/manage-system-settings-with-endpoint-privilege-management/`

### Marcos Normativos
- **REF-19:** NIST — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)*: `https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20`

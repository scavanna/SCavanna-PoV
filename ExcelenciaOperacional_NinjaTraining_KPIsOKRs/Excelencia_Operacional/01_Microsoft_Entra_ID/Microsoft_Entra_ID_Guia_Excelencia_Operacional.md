# Guía Maestra de Excelencia Operacional: Microsoft Entra ID (Plan 1 / Plan 2 — Core IAM, Conditional Access e Identity Protection / ITDR)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `01_Microsoft_Entra_ID` |
| **Slug Canónico** | `Microsoft_Entra_ID` |
| **Nombre Completo** | Microsoft Entra ID (Plan 1 / Plan 2 — Core IAM, Conditional Access e Identity Protection / ITDR) |
| **Categoría Maestra** | Identidad y Acceso (Microsoft Entra) |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (*Entra - SecOPS pura VC*, *12 Bloques Modelo de Operación*, *Auditoría Licenciamiento Entra ID P2*, *Mapeo Evidencias NIST CSF 2.0* y *Links Validados*) + *Ninja Training Entra Identidad y Agentes 2026* + Revalidado Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Incluido en Microsoft 365 E5** — **Microsoft Entra ID Plan 2 (P2)** está incluido nativamente en **Microsoft 365 E5**, **Microsoft 365 E7**, **Microsoft Defender Suite** *(antes M365 E5 Security)* y **EMS E5** *(NO incluido en Microsoft Purview Suite / antes E5 Compliance)* `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://entra.microsoft.com` (Microsoft Entra Admin Center), `https://security.microsoft.com` (Unified SecOps Platform: ITDR, Automatic Attack Disruption y `EntraIdSignInEvents`), `https://portal.azure.com` (Azure Monitor Alerts, Log Analytics y suscripciones) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Identity & Access Management (IAM) Lead, Conditional Access Architect, SOC Manager, SOC L1 / L2 / L3 (ITDR), Threat Hunter, Hybrid Identity Engineer, GRC & Internal/External Auditors |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29 — foco primario `PR.AA`, `DE.CM`, `RS.MI`, `GV.PO`, `GV.RR`), NIST SP 800-63B (AAL2/AAL3 Phishing-Resistant MFA), Microsoft Zero Trust Architecture, Microsoft Security Adoption Framework (SAF), MITRE ATT&CK Enterprise v18 |

> **Nota de alcance modular y consolidación:** Este módulo gobierna las operaciones de seguridad y administración nuclear de **Microsoft Entra ID Plan 1 y Plan 2**: directiva unificada de métodos de autenticación, **Passkeys (FIDO2)**, **External MFA (EAM)**, motor **Conditional Access** (**Token Protection**, **Continuous Access Evaluation - CAE**, **Authentication Strengths**, políticas gestionadas por Microsoft), **Microsoft Entra ID Protection (ITDR)** integrado con **Defender XDR** (*Automatic Attack Disruption*), **PIM operativo** para roles privilegiados administrativos/SOC, protección de **Workload Identities**, cuentas **Break-Glass**, sincronización híbrida (**Entra Connect Sync v2.6.x / Cloud Sync**) y base operativa de **Microsoft Entra Agent ID**. Los procesos integrales de gobierno de ciclo de vida (*Joiner-Mover-Leaver* / *Lifecycle Workflows*), catálogos de *Entitlement Management (Access Packages)* y campañas corporativas amplias de *Access Reviews* se desarrollan de forma dedicada y enlazada en el **Módulo `02_Microsoft_Entra_ID_Governance`**, mientras que el gobierno extendido transversal de agentes autónomos conecta con el **Módulo `22_Microsoft_Agent_365`**. Todo hecho técnico oficial lleva `[Verificado MS Learn]` y todo umbral consultivo, SLA o criterio de madurez lleva `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 La Identidad como Plano de Control Primario en la Era de Ataques AiTM y Agentes Autónomos

En la arquitectura empresarial moderna, **la identidad constituye el plano de control primario de defensa** sobre el cual descansan el acceso a aplicaciones SaaS, infraestructura multicloud, endpoints, datos sensibles y agentes de inteligencia artificial `[Verificado MS Learn]`. Los adversarios contemporáneos ya no intentan vulnerar perímetros de red: inician sesión empleando credenciales robadas, kits de phishing *Adversary-in-the-Middle (AiTM)* que interceptan cookies de sesión post-MFA, abuso de consentimientos OAuth, compromiso de principales de servicio o manipulación de agentes autónomos `[Verificado MS Learn]`.

A noviembre de 2026, **Microsoft Entra ID** ha consolidado cinco transformaciones estructurales que redefinen la operación diaria de IAM y del SOC de Identidad (ITDR) `[Verificado MS Learn]`:

1. **Fin definitivo de políticas heredadas MFA/SSPR y consolidación en Authentication Methods (`2025-09-30`):** A partir del **30 de septiembre de 2025**, Microsoft retiró la administración de métodos en las antiguas consolas separadas de MFA por tenant y SSPR, centralizando el control granular por grupos en la directiva unificada **Authentication methods** (`Migration Complete`) `[Verificado MS Learn]`.
2. **Estándar Passwordless y Phishing-Resistant con Passkeys (FIDO2):** Soporte nativo para **device-bound passkeys** (llaves de seguridad FIDO2 y **Microsoft Authenticator** en iOS/Android con atestación FIDO MDS opcional) y **synced passkeys** (Apple iCloud Keychain y Google Password Manager, logrando inicios de sesión **14 veces más rápidos** —3 segundos frente a 69 segundos—), complementado desde noviembre de 2026 (**MC1450133**) por la capacidad de registrar passkeys directamente como primer factor MFA `[Verificado MS Learn]`.
3. **Defensa contra robo y repetición de tokens (Token Protection + CAE Estricto):** Vinculación criptográfica de tokens de sesión al dispositivo mediante **Primary Refresh Tokens (PRT)** en **Token Protection** y reevaluación casi en tiempo real con **Continuous Access Evaluation (CAE)** en modalidad **Strictly enforce location policies** validando la IP vista directamente por el proveedor del recurso `[Verificado MS Learn]`.
4. **Convergencia ITDR con Microsoft Defender XDR y Automatic Attack Disruption:** Fusión nativa de señales de **Entra ID Protection** con endpoints, correo y SaaS en `https://security.microsoft.com`, consultables en la tabla en disponibilidad general **`EntraIdSignInEvents`** (que reemplazó a `AADSignInEventsBeta` el **19 de octubre de 2026**) y capaces de ejecutar revocación automática de sesiones y suspensión de cuentas con **>= 99% de confianza SNR** `[Verificado MS Learn]`.
5. **Extensión del perímetro a identidades no humanas y agentes IA (Entra Agent ID):** Incorporación de constructos nativos (*Agent Identity Blueprints*, identidades de agente y *Agent Users*) gobernados con **Conditional Access for agents** e **ID Protection for agents** (`Risky agents`) en articulación con **Microsoft Agent 365** y **Microsoft 365 E7** `[Verificado MS Learn]`.

### 2.2 Matriz Auditable de Licenciamiento Microsoft Entra ID (Corte Noviembre 2026)

Para evitar hallazgos de incumplimiento contractual o errores en auditorías **NIST CSF 2.0**, es imperativo distinguir con exactitud qué suites incluyen **Microsoft Entra ID Plan 2 (P2)** y qué capacidades requieren complementos adicionales `[Verificado MS Learn]`:

| Licencia / Suite Comercial | Nivel Entra ID Incluido | Capacidades Clave Habilitadas en este Módulo (`01`) | Aclaración Crítica para Auditoría y Compras | Etiqueta |
|---|---|---|---|---|
| **Microsoft 365 E5** *(Full Suite)* y **Microsoft 365 E7** *(Frontier Suite)* | **Entra ID Plan 2 (P2)** *(E7 añade además Entra Suite + Agent 365)* | Todas las funciones P1 + **Entra ID Protection** (`Risky users`, `Risky sign-ins`, políticas CA basadas en riesgo), **Token Protection**, **PIM** (JIT para roles Entra, Azure y Grupos) y exportación/caza en **`EntraIdSignInEvents`**. | Cumple íntegramente los requisitos técnicos de `PR.AA`, `DE.CM` y `RS.MI` sobre identidades humanas; **E7** extiende además la cobertura completa a red SSE y agentes IA. | `[Verificado MS Learn]` |
| **Microsoft Defender Suite** *(antes Microsoft 365 E5 Security)* y **EMS E5** | **Entra ID Plan 2 (P2)** | Habilita exactamente las mismas capacidades de **Entra ID P2** (ID Protection, Risk-based CA, Token Protection, PIM y telemetría XDR de identidad). | Vía óptima de *step-up* sobre M365 E3 cuando se requiere seguridad avanzada de identidad y XDR. | `[Verificado MS Learn]` |
| **Microsoft Purview Suite** *(antes Microsoft 365 E5 Compliance)* | **NINGUNO** *(No incluye Entra ID P1 ni P2)* | **Ninguna capacidad de Entra ID.** Cubre exclusivamente seguridad de datos, auditoría, eDiscovery y cumplimiento Purview. | **Advertencia formal de auditoría:** `M365 E3 + Microsoft Purview Suite` **NO otorga Entra ID P2**; no habilita ID Protection, Risk-based CA ni PIM. | `[Verificado MS Learn]` |
| **Microsoft 365 E3**, **M365 Business Premium** y **EMS E3** | **Entra ID Plan 1 (P1)** | **Conditional Access** (ubicación, dispositivo, aplicación), **Authentication Strengths**, **CAE** estándar, **External MFA (EAM)**, grupos dinámicos, SSPR con *writeback*, Cloud Sync / Connect Sync y App Proxy. | **No incluye** políticas de riesgo automatizadas (ID Protection), **Token Protection**, **PIM** ni la tabla avanzada `EntraIdSignInEvents` en XDR. | `[Verificado MS Learn]` |
| **Microsoft Entra Workload ID Premium** *(Add-on por identidad de workload)* | Complemento para *Service Principals / Apps* | Políticas de **Conditional Access para workload identities**, detección de **`Risky workload identities`** y revisiones de acceso de principales de servicio. | Las identidades humanas P2 no licencian automáticamente aplicaciones empresariales autónomas; se licencia por carga de trabajo protegida. | `[Verificado MS Learn]` |
| **Microsoft Agent 365** *(Add-on sobre E5 o incluido en M365 E7)* | Complemento para **Agentes IA** sobre **Entra Agent ID** | Extiende **Conditional Access for agents**, **ID Protection for agents** (`Risky agents`) y gobierno de ciclo de vida sobre identidades de agentes. | La plataforma base **Entra Agent ID** (creación de *blueprints* e identidades) está disponible para todos los clientes Entra; las políticas avanzadas de seguridad exigen **Agent 365** o **M365 E7**. | `[Verificado MS Learn]` |
| **Microsoft Entra ID Governance / Microsoft Entra Suite** *(Add-on)* | Complemento IGA avanzado y SSE *(Módulo `02`)* | *Lifecycle Workflows* JML, *Entitlement Management* avanzado, recomendaciones ML en *Access Reviews*, *Verified ID* premium y *Global Secure Access*. | Gobernado operativamente en el **Módulo `02_Microsoft_Entra_ID_Governance`**. | `[Verificado MS Learn]` |

### 2.3 Principios Rectores Oficiales de Operaciones de Seguridad de Identidad

1. **Autenticación resistente a phishing por diseño (*Phishing-Resistant MFA Everywhere*):** Erradicar progresivamente métodos vulnerables a intercepción o ingeniería social (SMS, llamadas de voz, OTP y notificaciones push simples) exigiendo **Authentication Strengths** resistentes a phishing (**Passkeys FIDO2**, **Windows Hello for Business** o **CBA multifactor**) para el 100% de roles administrativos y flujos sensibles `[Verificado MS Learn]`.
2. **Evaluación explícita y continua de cada sesión (*Conditional Access + CAE + Token Protection*):** Tratar cada emisión y renovación de token como una decisión explícita que combina identidad, riesgo, cumplimiento de dispositivo, aplicación y ubicación vista por el recurso, vinculando los tokens de sesión al silicio del dispositivo `[Verificado MS Learn]`.
3. **Cero privilegios permanentes (*Zero Standing Privileges vía PIM*):** Ningún administrador humano posee roles privilegiados activos permanentes; toda elevación es **Eligible en PIM**, acotada en horas, justificada y auditada, manteniendo exclusivamente dos o más cuentas **Break-Glass** cloud-only de emergencia `[Verificado MS Learn]`.
4. **Detección y disrupción integrada ITDR-XDR (*Assume Breach*):** Correlacionar señales offline y en tiempo real de **Entra ID Protection** con telemetría de endpoints y correo en **Defender XDR** para interrumpir ataques AiTM y compromisos de cuenta en segundos `[Verificado MS Learn]`.
5. **Paridad de gobierno para identidades no humanas (*Workloads & AI Agents*):** Aplicar a aplicaciones OAuth, principales de servicio y agentes de **Entra Agent ID** controles equivalentes de mínimo privilegio, credenciales libres de secretos estáticos (*Workload Identity Federation* / certificados), patrocinio humano y monitoreo de riesgo `[Verificado MS Learn]`.
6. **Resiliencia híbrida y trato Tier-0 a la sincronización:** Operar **Password Hash Synchronization (PHS)** como respaldo criptográfico universal, mantener actualizado **Entra Connect Sync v2.6.x / Cloud Sync** dentro de la ventana estricta de soporte de 12 meses y proteger los servidores de sincronización como activos de plano de control Tier-0 `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Flujo Arquitectónico Integrado de Autenticación, Decisión y Respuesta ITDR

```
[Usuario / Workload / Agente IA]
       |
       v  1. Credencial primaria / Passkey FIDO2 / WHfB / CBA / External MFA (OIDC)
+---------------------------------------------------------------------------------------+
|              DIRECTIVA UNIFICADA AUTHENTICATION METHODS (Migration Complete)          |
+---------------------------------------------------------------------------------------+
       |
       v  2. Señales en tiempo real: User/Sign-in/Workload/Agent Risk + Intune Device + IP
+---------------------------------------------------------------------------------------+
|                        MOTOR MICROSOFT ENTRA CONDITIONAL ACCESS                       |
|  - Grant Controls: Authentication Strengths (Phishing-Resistant MFA) / Compliant Dev  |
|  - Session Controls: Token Protection (PRT Bound) + CAE (Strictly Enforce Location)   |
+---------------------------------------------------------------------------------------+
       |                                                   |
       | Token emitido (CAE + PRT)                         | Eventos y Detecciones de Riesgo
       v                                                   v
[Recursos M365 / Azure / SaaS / MCP]          +-----------------------------------------+
  (Reevaluación CAE: IP seen by resource)     |  MICROSOFT DEFENDER XDR + SENTINEL      |
                                              |  - EntraIdSignInEvents (GA oct-2026)    |
                                              |  - Automatic Attack Disruption (>=99%)  |
                                              |    -> Revoke Session & Suspend in Entra |
                                              +-----------------------------------------+
```

### 3.2 Componentes Técnicos Nucleares e Hitos 2025–2026

#### A. Directiva Unificada Authentication Methods, Passkeys (FIDO2) y External MFA (EAM)
- **Convergencia obligatoria completada (`2025-09-30`) `[Verificado MS Learn]`:** Las directivas heredadas de MFA y SSPR quedaron inhabilitadas para gestión de métodos desde el **30 de septiembre de 2025** (exceptuando temporalmente las preguntas de seguridad en SSPR heredado y el conteo de métodos requeridos para restablecimiento). Toda organización debe encontrarse en estado **`Migration Complete`** dentro de `Entra ID > Authentication methods > Policies`. Se debe vigilar la limitación técnica de **20 KB de tamaño máximo de política**, consolidando grupos de destino y migrando cualquier asignación individual residual a grupos de seguridad `[Verificado MS Learn]`.
- **Passkeys (FIDO2) — Device-Bound vs. Synced Passkeys `[Verificado MS Learn]`:**
  - **Device-bound passkeys:** La clave privada nunca abandona el autenticador físico (**llaves FIDO2** o **Microsoft Authenticator** en iOS/Android). Soportan **atestación criptográfica** contra el *FIDO Metadata Service (MDS)* mediante *Passkey profiles*, siendo el estándar recomendado para administradores y entornos altamente regulados `[Verificado MS Learn]`.
  - **Synced passkeys:** Claves generadas en HSM local y sincronizadas cifradas mediante proveedores como **Apple iCloud Keychain** o **Google Password Manager**. No soportan atestación (si se activa `Enforce attestation`, las synced passkeys quedan excluidas), pero ofrecen adopción masiva sin fricción (**99% de éxito en registro** y autenticación en **3 segundos**) para población general en reemplazo de SMS y códigos OTP `[Verificado MS Learn]`.
  - **Endurecimiento obligatorio del registro (MC1450133 — Noviembre 2026) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:** Al habilitarse el registro directo de passkeys como primer método MFA sin exigir un método previo alternativo, es obligatorio proteger en Conditional Access la acción de usuario **`Register security information`**, exigiendo **Temporary Access Pass (TAP)** de un solo uso, dispositivo conforme o red corporativa verificada para impedir que un atacante con una contraseña robada registre su propia passkey.
- **External Authentication Methods (EAM / External MFA) y Retiro de Custom Controls `[Verificado MS Learn]`:** Con la disponibilidad general de **External MFA** basado en OIDC (`Entra ID > Authentication methods > Policies > External authentication methods`), los antiguos **Custom Controls** de Conditional Access quedaron obsoletos: **desde septiembre de 2026 no se permite crear ni editar Custom Controls, y su retiro total ocurre a inicios de 2027** `[Verificado MS Learn]`.

#### B. Conditional Access Avanzado: Token Protection, CAE Estricto, Authentication Strengths y Políticas Gestionadas
- **Token Protection (`Require token protection for sign-in sessions`) `[Verificado MS Learn]`:** Disponible de forma general (GA) para aplicaciones nativas en **Windows**, **iOS/iPadOS** (16.0+ con plugin SSO empresarial) y **macOS** (14.0+ con Platform SSO / plugin SSO) accediendo a **Exchange Online, SharePoint Online y Microsoft Teams** (más **Azure Virtual Desktop y Windows 365** en Windows), y en **Preview** para aplicaciones web seleccionadas que acceden a **Azure Resource Manager** (`Windows Azure Service Management API`). Exige que el acceso utilice tokens criptográficamente atados al dispositivo (como el **PRT**), neutralizando la reproducción del token desde otra máquina `[Verificado MS Learn]`.
- **Continuous Access Evaluation (CAE) — *Strictly enforce location policies* (Preview) `[Verificado MS Learn]`:** Revoca sesiones casi en tiempo real ante eventos críticos (cuenta deshabilitada, cambio de contraseña, revocación de sesión, riesgo elevado) y, al activar `Strictly enforce location policies` en controles de sesión, bloquea inmediatamente el acceso si la **`IP address (seen by resource)`** reportada por Exchange, SharePoint, Teams o Graph no pertenece a las *Named Locations* autorizadas. Requiere conocer con exactitud las IPs públicas de salida (sin *split-tunnel* no inventariado ni tráfico hacia apps no-M365 detrás de Global Secure Access sin restauración de IP origen), validándose previamente con el Workbook oficial *Continuous Access Evaluation Insights* `[Verificado MS Learn]`.
- **Authentication Strengths y Microsoft-managed Policies `[Verificado MS Learn]`:** Las fortalezas de autenticación permiten exigir métodos exactos según sensibilidad del recurso (*MFA*, *Passwordless MFA*, *Phishing-resistant MFA* o combinaciones personalizadas; nunca deben combinarse en una misma regla con el control clásico `Require multifactor authentication`). Adicionalmente, Microsoft despliega **Microsoft-managed Conditional Access policies** en estado `Report-only` y las activa automáticamente tras **no menos de 45 días** si permanecen sin modificar `[Verificado MS Learn]`.

#### C. Microsoft Entra ID Protection (ITDR), Defender XDR y Tabla `EntraIdSignInEvents`
- **Detecciones de Riesgo Multi-Entidad `[Verificado MS Learn]`:** Evalúa en tiempo real y offline usuarios humanos (`anomalousToken`, `leakedCredentials`, `mcasImpossibleTravel`, `passwordSpray`, `attackerInTheMiddle`, `attemptedPrtAccess` desde MDE), principales de servicio (`Risky workload identities`) y agentes autónomos (`Risky agents`, con **Learning Mode** para suprimir falsos positivos iniciales y detecciones específicas como `earlyLifeMaliciousActivity`, `entraDirectoryReconnaissance`, `suspiciousCredentialUsage`, `signInSpike` y `unfamiliarResourceAccess`) `[Verificado MS Learn]`.
- **Automatic Attack Disruption en Identidad `[Verificado MS Learn]`:** Cuando Defender XDR correlaciona un ataque activo con confianza **>= 99% SNR**, ejecuta automáticamente `Revoke user session` y `Suspend user in Entra` sobre cuentas nativas de nube o sincronizadas (empleando la aplicación administrada por Microsoft `Microsoft Defender for Identity`, App ID `60ca1954-583c-4d1f-86de-39d835f3e452`, además de deshabilitar en AD on-premises si hay sensores MDI y contener al usuario en endpoints MDE) `[Verificado MS Learn]`.
- **Esquema Vigente en Advanced Hunting (`2026-10-19`) `[Verificado MS Learn]`:** Para clientes con licencia **Entra ID P2**, toda caza en `security.microsoft.com` debe utilizar **`EntraIdSignInEvents`** (que depreció y migró automáticamente a `AADSignInEventsBeta` el **19 de octubre de 2026**), `EntraIdSpnSignInEvents` y `EntraIdDirectoryAuditEvents`, empleando la columna `EntraIdDeviceId` en lugar de la heredada `AadDeviceId` `[Verificado MS Learn]`.

#### D. Cuentas Break-Glass, Sincronización Híbrida (v2.6.x / Cloud Sync) y Entra Agent ID
- **Cuentas de Acceso de Emergencia (Break-Glass) `[Verificado MS Learn]`:** Al menos **dos cuentas cloud-only (`*.onmicrosoft.com`)**, asignadas como **permanentes activas** al rol `Global Administrator` (nunca elegibles en PIM), excluidas de políticas CA que bloqueen el acceso (las políticas `Report-only` no requieren exclusión), operadas únicamente desde estaciones **PAW**, protegidas obligatoriamente con credenciales sin contraseña resistentes a phishing (**Passkey FIDO2 en llave física** o **Certificate-Based Authentication - CBA**) distintas del método habitual de los administradores, almacenadas en bóvedas ignífugas separadas, monitoreadas con alerta **Severidad 0 - Critical** y probadas **al menos cada 90 días** `[Verificado MS Learn]`.
- **Sincronización Híbrida Moderna `[Verificado MS Learn]`:**
  - **Microsoft Entra Connect Sync v2.6.x:** Cada versión caduca exactamente **12 meses después del lanzamiento de la versión posterior** (por ejemplo, la versión `2.6.92.0` se publicó el **23 de septiembre de 2026**, mientras que `2.5.79.0` quedó fuera de soporte el **23 de octubre de 2026**). Desde la rama `2.5.76.0+` / `2.6.x`, la autenticación basada en identidad de aplicación hacia Entra ID es la opción predeterminada en GA y el registro de auditoría de acciones administrativas en Windows Event Log está en GA `[Verificado MS Learn]`.
  - **Microsoft Entra Cloud Sync:** Servicio de aprovisionamiento gestionado desde la nube con agentes ligeros en alta disponibilidad, soporte para bosques AD desconectados, **Password Hash Synchronization (PHS)** y sincronización de objetos de equipo hacia Entra ID para *Hybrid Join* `[Verificado MS Learn]`.
- **Microsoft Entra Agent ID `[Verificado MS Learn]`:** Extiende el motor Conditional Access a tres patrones distintos de sujeto de token: (1) **On-Behalf-Of (OBO)** delegado (el sujeto evaluado es el usuario humano); (2) **Autonomous App-Only** (el sujeto es la identidad del agente o su *Agent Identity Blueprint*); y (3) **Agent User** (cuenta de usuario digital dedicada vinculada al agente, que debe segmentarse explícitamente bajo `Agents > Agent users` en Conditional Access porque las reglas dirigidas a `Users` humanos no aplican a *Agent Users*) `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Microsoft Entra ID exige erradicar el uso operativo de `Global Administrator` delegando tareas cotidianas en roles nativos de mínimo privilegio bajo **Privileged Identity Management (PIM)** `[Verificado MS Learn]`:

| Rol Oficial Microsoft Entra ID | Nivel / Función Operativa | Permisos Clave Otorgados | Configuración PIM / JIT Recomendada | Segregación de Funciones (SoD) y Límites | Etiqueta |
|---|---|---|---|---|---|
| **Global Administrator** *(Solo Break-Glass y <=4 Elegibles)* | Tier-0 Crítico / Emergencia Extrema | Control absoluto sobre todos los servicios administrativos de Entra ID, suscripciones elevables de Azure y cargas M365. | **0 activos humanos** (solo las **>=2 cuentas Break-Glass** `*.onmicrosoft.com` permanentes activas con FIDO2/CBA). Humanos (`< 5`): **Eligible**, máximo **1–2 horas**, **aprobación dual**, justificación y *Authentication Context* FIDO2. | Prohibido su uso para operaciones diarias de IAM, correo, soporte o seguridad; alerta inmediata en cada activación. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Privileged Role Administrator** | Tier-0 Gobierno RBAC y PIM | Administración de asignaciones de roles en Entra ID, configuración de políticas **PIM** y concesión de consentimiento administrativo de APIs. | **Eligible en PIM**, máximo **2 horas**, requiere **aprobación por par distinto**, ticket de cambio y *Phishing-resistant MFA*. | Quien solicita elevar este rol no puede auto-aprobarse; auditado diariamente en `D-04`. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Conditional Access Administrator** | Ingeniería Zero Trust (`PR.AA`) | Creación, edición, paso a `Report-only` / `On` y exclusiones en políticas de **Conditional Access**, *Named Locations* y *Authentication Strengths*. | **Eligible en PIM**, máximo **4 horas**, requiere MFA resistente a phishing + número de cambio CAB aprobado. | Segregado de `Authentication Policy Administrator` y de la propiedad de las cuentas Break-Glass para evitar bloqueos o auto-exclusiones. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Authentication Policy Administrator** | Ingeniería de Credenciales (`PR.AA`) | Gestión de la directiva unificada **Authentication methods**, perfiles de **Passkeys (FIDO2)**, **External MFA (EAM)** y campañas de registro. | **Eligible en PIM**, máximo **4 horas**, requiere MFA resistente a phishing y validación previa en grupo piloto. | No puede modificar políticas de Conditional Access ni restablecer credenciales de Global/Privileged Admins. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Security Administrator** / **Security Operator** | Operaciones SOC de Identidad — ITDR (`DE` / `RS`) | Investigación en **Entra ID Protection**, ejecución de `Confirm compromise`, `Confirm safe`, `Dismiss risk` sobre usuarios, workloads y agentes (`Risky agents`). | `Security Operator` para analistas SOC L2 (**Eligible 8 horas** por turno); `Security Administrator` restringido a SOC Lead/L3 (**Eligible 4 horas**). | Permite contener riesgo de identidad sin otorgar permisos para crear usuarios ni alterar asignaciones de roles de directorio. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Authentication Administrator** vs. **Privileged Authentication Administrator** | Mesa de Ayuda Segura / Respuesta a Incidentes | Emisión de **Temporary Access Pass (TAP)**, restablecimiento de contraseñas y revocación/re-registro de métodos MFA (`Require re-register MFA`). | Helpdesk usa exclusivamente `Authentication Administrator` (acotado por **Administrative Units**, **Eligible 8h**). `Privileged Authentication Administrator` (afecta admins) reservado a IR Tier-0 (**Eligible 2h con aprobación**). | Impide que compromisos en Helpdesk escalen hacia cuentas privilegiadas (`Admin Protection`). | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Application Administrator** / **Cloud Application Administrator** | Gobierno de Apps OAuth y Workload Identities | Gestión de registros de aplicaciones (*App Registrations*), *Enterprise Applications*, certificados/federación de credenciales y URIs de redirección. | Preferir `Cloud Application Administrator` (no gestiona Application Proxy) **Eligible 4 horas** o delegación por propietario/Custom Role; vigilar que agregar secretos a apps con permisos altos equivale a escalar privilegios. | Prohibido conceder `Directory.ReadWrite.All` o `RoleManagement.ReadWrite.Directory` sin aprobación de `Privileged Role Administrator`. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Hybrid Identity Administrator** | Ingeniería de Sincronización Híbrida | Configuración y mantenimiento de **Microsoft Entra Connect Sync v2.6.x**, **Cloud Sync**, agentes PTA y **PHS**. | **Eligible en PIM**, máximo **4 horas**, autenticación FIDO2 desde **PAW**; acceso local a servidores Entra Connect restringido a Tier-0. | Segregado de la administración cotidiana de usuarios on-premises de unidades de negocio. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Triaje y Remediación Prioritaria de Usuarios e Inicios de Sesión en Riesgo Alto (Entra ID Protection)
- **Objetivo:** Investigar y contener en menos de 4 horas todo usuario o inicio de sesión marcado en riesgo `High` que no haya completado remediación automática `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `ID Protection` > `Risky users` y `Risky sign-ins` `[Verificado MS Learn]`.
- **Rol Responsable:** Analista SOC L1 / L2 (`Security Operator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Filtrar `Risky users` por `Risk state == At risk` y `Risk level == High`, ordenando por hora de última detección `[Verificado MS Learn]`.
  2. Inspeccionar en la pestaña `Risk detections` el disparador exacto (`leakedCredentials`, `anomalousToken`, `attackerInTheMiddle`, `attemptedPrtAccess`, `mcasImpossibleTravel`, `unfamiliarFeatures`) `[Verificado MS Learn]`.
  3. Correlacionar actividad posterior en `Sign-in logs` (`Interactive` y `Non-interactive user sign-ins`) y `Audit logs` buscando registro sospechoso de métodos MFA, creación de reglas de reenvío en buzón o consentimiento OAuth `[Verificado MS Learn]`.
  4. Si se confirma compromiso, ejecutar **`Confirm user compromised`**, revocar sesiones (`Revoke sessions`) y disparar el Playbook `AH-02`; si se verifica falso positivo legítimo por canal out-of-band seguro, documentar ticket y marcar `Confirm user safe` o `Dismiss user risk` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación diaria de `Risky users` con cero cuentas `High` abiertas sin acción superadas 4 horas (`DE.CM-03`, `RS.MI-01`) `[Decisión / Propuesta Editorial]`.

### D-02: Monitoreo Diario de Identidades No Humanas en Riesgo (Workload Identities y Agentes IA)
- **Objetivo:** Detectar compromisos de secretos/certificados en principales de servicio y comportamientos maliciosos tempranos en agentes autónomos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `ID Protection` > `Risky workload identities` y `Risky agents` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 (ITDR) + Application / Agent Security Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar entradas activas en `Risky workload identities` (credenciales filtradas en GitHub/repositorios, IPs maliciosas o cambios sospechosos en propiedades de aplicación) `[Verificado MS Learn]`.
  2. Revisar el reporte **`Risky agents`** y la pestaña `Agent detections` en `Risk detections` buscando eventos `earlyLifeMaliciousActivity`, `entraDirectoryReconnaissance`, `suspiciousCredentialUsage`, `signInSpike` o `unfamiliarResourceAccess` `[Verificado MS Learn]`.
  3. Ejecutar inmediatamente `Confirm compromise` (que activa el bloqueo por **Conditional Access for agents / workload identities**) o `Disable` sobre la entidad comprometida y contactar al propietario o *Sponsor* registrado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de colas `Risky workload identities` y `Risky agents` conciliadas y trazas en `EntraIdSpnSignInEvents` (`PR.AA-05`, `DE.CM-03`) `[Verificado MS Learn]`.

### D-03: Vigilancia de Cuentas de Emergencia (Break-Glass) y Asignaciones Directas Fuera de PIM
- **Objetivo:** Asegurar que ninguna cuenta Break-Glass haya sido utilizada sin autorización formal y que ningún rol privilegiado se haya asignado eludiendo **PIM** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Monitoring & health` > `Sign-in logs` / `Audit logs` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Confirmar ausencia de disparos en la regla de alerta crítica **Severidad 0** configurada en Azure Monitor / Sentinel sobre los `ObjectId` de las cuentas Break-Glass (`*.onmicrosoft.com`) `[Verificado MS Learn]`.
  2. Verificar en `Audit logs` (`Category == RoleManagement`) que todo evento `Add member to role` provenga exclusivamente de `MS-PIM` o corresponda a una solicitud aprobada en CAB `[Verificado MS Learn]`.
  3. Revisar cualquier modificación de métodos de autenticación o contraseñas sobre cuentas con roles administrativos (`Admin registered security info` / `Reset password (by admin)`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consulta diaria en `AuditLogs` y `SigninLogs` con resultado cero anomalías no justificadas (`PR.AA-01`, `PR.AA-05`) `[Verificado MS Learn]`.

### D-04: Detección Diaria de Password Spray, Bloqueos MFA con Contraseña Válida y Legacy Auth
- **Objetivo:** Identificar ataques activos de fuerza bruta distribuida, contraseñas ya vulneradas contenidas únicamente por MFA e intentos de autenticación heredada `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Monitoring & health` > `Sign-in logs` y `https://security.microsoft.com` > `Advanced hunting` (`EntraIdSignInEvents`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / L2 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Analizar picos de error **`50126`** (*Invalid username or password*) originados desde una misma IP o rango ASN contra múltiples `AccountUpn` distintos (indicador clásico de *Password Spray*) `[Verificado MS Learn]`.
  2. Filtrar eventos con código **`500121`** (*Authentication failed during strong authentication request*) o reportes de fraude MFA: **el atacante ya posee la contraseña válida del usuario** y fue frenado por MFA, por lo que se debe forzar cambio inmediato de contraseña `[Verificado MS Learn]`.
  3. Auditar cualquier intento con clientes de autenticación heredada (`Exchange ActiveSync`, `IMAP4`, `POP3`, `Authenticated SMTP`, `Other clients`) verificando que hayan resultado bloqueados con código **`53003`** por Conditional Access `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte diario KQL de tendencias `50126`/`500121`/Legacy Auth y tickets de restablecimiento preventivo emitidos (`DE.AE-02`, `PR.AA-03`) `[Verificado MS Learn]`.

### D-05: Supervisión de Acciones de Identidad Ejecutadas por Automatic Attack Disruption
- **Objetivo:** Auditar todas las suspensiones de cuentas y revocaciones de sesión disparadas automáticamente por **Microsoft Defender XDR** sobre **Entra ID** y **Active Directory** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Incidents` (etiqueta `Attack Disruption`) y `Action center` > `History` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / L3 `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Inspeccionar cada incidente donde `Automatic Attack Disruption` ejecutó `Suspend user in Entra`, `Revoke user session` o `Disable user` (vía `Microsoft Defender for Identity`) `[Verificado MS Learn]`.
  2. Reconstruir el vector de entrada (comúnmente enlace AiTM en correo, infostealer en endpoint no gestionado o compromiso de token OAuth) `[Verificado MS Learn]`.
  3. Completar la limpieza integral (eliminación de métodos MFA fraudulentos, reglas de buzón y persistencia OAuth) antes de rehabilitar la cuenta y exigir re-registro presencial o vía TAP verificado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Historial del `Action center` conciliado con el cierre forense del expediente de incidente (`RS.MI-01`, `RC.RP-05`) `[Verificado MS Learn]`.

### D-06: Auditoría Diaria de Elevaciones PIM Fuera de Horario o con Patrones Anómalos
- **Objetivo:** Detectar uso abusivo o sospechoso de roles elegibles en **Privileged Identity Management** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity governance` > `Privileged Identity Management` > `Microsoft Entra roles` > `Resource audit` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 + Identity Security Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar activaciones completadas (`Add member to role completed (PIM activation)`) ocurridas fuera del horario laboral estándar (ej. 20:00 a 07:00) o en días inhábiles sin guardia ni ventana de mantenimiento `[Decisión / Propuesta Editorial]`.
  2. Contrastar la IP, país y dispositivo empleado en la activación PIM contra la línea base habitual del administrador en `EntraIdSignInEvents` `[Verificado MS Learn]`.
  3. Escalar de inmediato cualquier activación desde IP anónima/proxy o con justificación genérica inválida `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario revisado de `PIM Resource audit` con validación de tickets de respaldo (`PR.AA-05`, `DE.CM-03`) `[Verificado MS Learn]`.

### D-07: Vigilancia Diaria de Consentimientos OAuth Sensibles, Nuevos Secretos de Apps y Redirect URIs
- **Objetivo:** Prevenir persistencia silenciosa mediante aplicaciones OAuth maliciosas (*Illicit Consent Grant*) o inyección de credenciales secundarias en registros de aplicaciones existentes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Monitoring & health` > `Audit logs` (`Category == ApplicationManagement`) y `https://security.microsoft.com` > `Cloud apps` > `OAuth apps` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 + Application Security Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Auditar eventos `Consent to application` y `Add app role assignment to service principal` que otorguen permisos críticos (`Mail.ReadWrite`, `Files.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`, `Application.ReadWrite.All`, `Directory.ReadWrite.All`) `[Verificado MS Learn]`.
  2. Revisar eventos `Update application – Certificates and secrets management` ejecutados fuera de pipelines autorizados o sobre aplicaciones multi-tenant / *Agent Identity Blueprints* `[Verificado MS Learn]`.
  3. Verificar modificaciones en `Redirect URIs` (`Update application`) para descartar redirecciones hacia dominios externos no controlados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora diaria de altas de permisos/secretos de aplicaciones validada contra cambios autorizados (`PR.AA-05`, `DE.CM-09`) `[Verificado MS Learn]`.

### D-08: Verificación Diaria de Salud de Sincronización Híbrida (Entra Connect Sync / Cloud Sync y PHS)
- **Objetivo:** Garantizar continuidad e integridad en la sincronización de identidades, bajas de personal y hashes de contraseñas (**PHS**) entre Active Directory y Entra ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Hybrid management` > `Microsoft Entra Connect` > `Connect Sync` / `Cloud Sync` / `Microsoft Entra Connect Health` `[Verificado MS Learn]`.
- **Rol Responsable:** Hybrid Identity Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Verificar que el último ciclo de sincronización de directorio y de **Password Hash Synchronization** se haya ejecutado dentro de la ventana normal (< 30 minutos para delta sync; < 2 minutos para PHS) sin errores de exportación `[Verificado MS Learn]`.
  2. Confirmar que las cuentas deshabilitadas en Active Directory por desvinculación laboral reflejen `AccountEnabled == false` en Entra ID sin demora `[Decisión / Propuesta Editorial]`.
  3. Revisar alertas en `Connect Health` y eventos administrativos en el servidor de sincronización para descartar modificaciones no autorizadas en reglas de filtrado o *sync rules* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `Healthy` en `Microsoft Entra Connect Health` y cero errores críticos de aprovisionamiento sin resolver > 24h (`PR.AA-01`, `PR.IR-01`) `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Optimización de Políticas Conditional Access, Modo Report-Only y Políticas Administradas por Microsoft
- **Objetivo:** Evaluar brechas de cobertura (`notApplied`), promover políticas desde `Report-only` y gobernar activamente las **Microsoft-managed Conditional Access policies** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Conditional Access` > `Policies` e `Insights and reporting` `[Verificado MS Learn]`.
- **Rol Responsable:** Conditional Access Administrator + Cybersecurity Architect `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Analizar en el Workbook **`Conditional Access Insights and Reporting`** todos los inicios de sesión de los últimos 7 días donde `Conditional Access status == Not applied` para cerrar huecos de cobertura en aplicaciones o poblaciones `[Verificado MS Learn]`.
  2. Evaluar el impacto simulado de políticas en estado `Report-only` (mínimo 7 días de observación antes de pasar a `On`) y revisar recomendaciones del *Conditional Access Optimization Agent* `[Verificado MS Learn]`.
  3. Inspeccionar cualquier nueva **Microsoft-managed policy** creada automáticamente en `Report-only` para personalizarla o activarla ordenadamente antes de que se cumpla el plazo mínimo de **45 días** de auto-habilitación por Microsoft `[Verificado MS Learn]`.
- **Evidencia Auditable:** Instantánea semanal del Workbook *Insights and Reporting* y exportación JSON de políticas CA vigentes (`GV.PO-02`, `PR.AA-03`) `[Verificado MS Learn]`.

### S-02: Seguimiento de Adopción de Passkeys (FIDO2) y Endurecimiento del Registro de Credenciales
- **Objetivo:** Acelerar la migración desde MFA tradicional hacia **Passkeys (FIDO2)** asegurando que el flujo de registro no pueda ser abusado por atacantes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Authentication methods` > `Activity` / `Registration campaign` `[Verificado MS Learn]`.
- **Rol Responsable:** Authentication Policy Administrator `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Medir en `Authentication methods > Activity` el porcentaje de usuarios capaces de autenticar sin contraseña y con métodos resistentes a phishing (`FIDO2 security key / passkey`, `Windows Hello for Business`, `CBA`) frente a métodos débiles (`SMS`, `Voice`) `[Verificado MS Learn]`.
  2. Auditar que la política de Conditional Access dirigida a la acción de usuario **`Register security information`** esté activa (`On`), exigiendo **Temporary Access Pass (TAP)**, dispositivo conforme o ubicación corporativa confiable (mitigación crítica ante el registro directo de passkeys de noviembre de 2026) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Excluir en políticas de *Authentication Strength* el principal de servicio `Microsoft Authenticator Credential Registration` cuando corresponda para evitar bucles de registro en dispositivos móviles `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Gráfico semanal de adopción de métodos fuertes en `Activity` y validación de política CA de registro seguro (`PR.AA-02`, `PR.AA-03`) `[Verificado MS Learn]`.

### S-03: Validación Semanal de Continuous Access Evaluation (CAE Estricto) y Token Protection
- **Objetivo:** Ampliar la protección contra repetición de tokens sin generar bloqueos accidentales por discrepancias de enrutamiento de red o incompatibilidad de clientes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Monitoring & health` > `Workbooks` (*Continuous Access Evaluation Insights*) y `Sign-in logs` `[Verificado MS Learn]`.
- **Rol Responsable:** Conditional Access Administrator + Network Security Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Consultar en `Sign-in logs` y en el Workbook **`Continuous Access Evaluation Insights`** las discrepancias entre la IP vista por Entra ID y la columna **`IP address (seen by resource)`** antes y después de aplicar `Strictly enforce location policies` `[Verificado MS Learn]`.
  2. Actualizar los rangos IPv4/IPv6 de egreso corporativo conocidos dentro de `Named locations` y verificar que no se enruten aplicaciones no-M365 sin restauración de IP origen bajo modo estricto `[Verificado MS Learn]`.
  3. Evaluar registros interactivos y no interactivos de políticas piloto de **Token Protection** en Windows, macOS e iOS/iPadOS para expandir progresivamente los grupos en aplicación activa `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal del Workbook *CAE Insights* sin bloqueos falsos no resueltos y cobertura actualizada de *Token Protection* (`PR.AA-03`, `PR.IR-01`) `[Verificado MS Learn]`.

### S-04: Revisión Semanal de Patrones de Uso PIM en Roles del SOC e Administradores de Identidad
- **Objetivo:** Identificar sobre-asignación de roles, activaciones repetitivas mal dimensionadas o cuentas elegibles inactivas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity governance` > `Privileged Identity Management` > `Microsoft Entra roles` > `Assignments` / `Resource audit` `[Verificado MS Learn]`.
- **Rol Responsable:** Privileged Role Administrator / Identity Lead `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Detectar administradores que activan un rol de alto privilegio 3 o más veces al día para tareas que podrían resolverse con un rol de lectura o menor privilegio (ej. usar `Security Reader` en lugar de elevar `Security Administrator`) `[Decisión / Propuesta Editorial]`.
  2. Verificar que el 100% de las elevaciones a roles críticos hayan requerido `Phishing-resistant MFA` mediante *Authentication Context* en Conditional Access `[Verificado MS Learn]`.
  3. Remover elegibilidad PIM a colaboradores que cambiaron de puesto durante la semana (en coordinación con flujos *Mover* del Módulo `02`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación semanal de activaciones PIM y ajustes de mínimo privilegio aplicados (`PR.AA-05`, `GV.RR-02`) `[Verificado MS Learn]`.

### S-05: Higiene Semanal de Registros de Aplicaciones, Secretos por Expirar y Agent Identity Blueprints
- **Objetivo:** Reducir la superficie de ataque de identidades no humanas eliminando secretos de texto plano, URIs colgantes y agentes no patrocinados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Applications` > `App registrations` y `Agent ID` `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud Application Administrator + AI & Agent Governance Lead `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Identificar aplicaciones cuyos certificados o secretos venzan en los próximos 30 días o superen los 180 días de vida útil, exigiendo migración hacia **Workload Identity Federation** o certificados alojados en Azure Key Vault `[Decisión / Propuesta Editorial]`.
  2. Auditar `Redirect URIs` en aplicaciones activas buscando dominios expirados (*dangling URIs*), esquemas HTTP inseguros o comodines no permitidos `[Verificado MS Learn]`.
  3. Revisar los **Agent Identity Blueprints** y cuentas *Agent User* en **Entra Agent ID** asegurando que tengan políticas explícitas de **Conditional Access for agents** aplicadas por blueprint o *Custom Security Attributes* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal de credenciales de apps y *Agent Blueprints* auditados sin secretos eternos ni URIs inseguras (`ID.AM-02`, `PR.AA-01`) `[Verificado MS Learn]`.

### S-06: Ejecución Semanal de Pruebas Continuas de Postura como Código sobre Entra ID (Maester)
- **Objetivo:** Detectar automáticamente regresiones de seguridad en configuración de tenant, Conditional Access, métodos de autenticación y roles administrativos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Pipeline automatizado GitHub Actions / Azure DevOps ejecutando **Maester** contra Microsoft Graph API de solo lectura `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** Identity Security Engineer `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar el conjunto semanal de aserciones automatizadas de **Maester** (CISA ScubaGear + Entra baselines + reglas personalizadas de exclusiones CA y cuentas Break-Glass) empleando una *Managed Identity* con permisos mínimos de lectura `[Decisión / Propuesta Editorial]`.
  2. Comparar el resultado contra la ejecución de la semana anterior para detectar cualquier prueba que haya pasado de `Pass` a `Fail` `[Decisión / Propuesta Editorial]`.
  3. Abrir ticket automático de remediación para cualquier desviación no aprobada en CAB `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte HTML/JSON semanal firmado de pruebas Maester archivado como evidencia continua de control (`GV.OV-03`, `ID.IM-02`) `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Remediación Mensual de Alertas de Seguridad PIM y Control Estricto de Global Administrators
- **Objetivo:** Mantener cero alertas de configuración abiertas en **PIM** y asegurar el límite máximo de administradores globales `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity governance` > `Privileged Identity Management` > `Microsoft Entra roles` > `Alerts` `[Verificado MS Learn]`.
- **Rol Responsable:** Privileged Role Administrator + GRC Auditor `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar y llevar a estado resuelto todas las alertas nativas de PIM: `Roles don't require multifactor authentication for activation`, `There are too many global administrators`, `Roles are being assigned outside of Privileged Identity Management`, `Potential stale accounts in a privileged role` y `Roles are being activated too frequently` `[Verificado MS Learn]`.
  2. Verificar que existan **menos de 5 usuarios humanos elegibles** para `Global Administrator` y que únicamente las cuentas **Break-Glass** posean asignación permanente activa `[Verificado MS Learn]`.
  3. Confirmar la ejecución de revisiones periódicas de acceso sobre roles privilegiados (articuladas en detalle con el **Módulo `02_Microsoft_Entra_ID_Governance`**) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura y exportación CSV mensual de alertas PIM en cero y matriz de titulares `Global Administrator` (`PR.AA-05`, `GV.RR-02`) `[Verificado MS Learn]`.

### M-02: Auditoría Mensual de la Directiva Unificada Authentication Methods y Retiro de Controles Heredados
- **Objetivo:** Verificar la pureza post-migración de `Authentication methods`, la reducción de métodos telefónicos y la ausencia de *Custom Controls* obsoletos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Authentication methods` > `Policies` y `Conditional Access` > `Custom controls` `[Verificado MS Learn]`.
- **Rol Responsable:** Authentication Policy Administrator `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Confirmar que el estado global permanezca en **`Migration Complete`** (obligatorio post `2025-09-30`), que el tamaño total de grupos incluidos/excluidos esté holgadamente por debajo del límite técnico de **20 KB** y que no queden usuarios individuales apuntados directamente `[Verificado MS Learn]`.
  2. Revisar el alcance residual de `SMS`, `Voice calls` y `Email OTP`, reduciendo mensualmente los grupos de excepción hacia **Passkeys (FIDO2)** o **Microsoft Authenticator** con coincidencia numérica y contexto geográfico/aplicación `[Verificado MS Learn]`.
  3. Si la organización integra un proveedor MFA externo, verificar que opere 100% sobre **External MFA (EAM)** en GA y que no subsista ningún **Custom Control** heredado antes de su retiro definitivo a inicios de 2027 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación mensual de configuración JSON de `Authentication methods policy` y conteo cero de *Custom Controls* activos (`PR.AA-02`, `GV.PO-02`) `[Verificado MS Learn]`.

### M-03: Ciclo Mensual de Actualización y Endurecimiento Tier-0 de Entra Connect Sync v2.6.x / Cloud Sync
- **Objetivo:** Evitar caer fuera de soporte por la regla estricta de retiro a 12 meses de **Microsoft Entra Connect Sync** y auditar la postura Tier-0 de la infraestructura híbrida `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Hybrid management` > `Microsoft Entra Connect` y servidores Tier-0 de sincronización `[Verificado MS Learn]`.
- **Rol Responsable:** Hybrid Identity Administrator `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Contrastar la versión instalada de **Microsoft Entra Connect Sync** contra el historial oficial de lanzamientos en Microsoft Learn (ej. rama `2.6.92.0+` vigente a nov-2026), planificando actualización en servidor *Staging Mode* al menos 90 días antes de su fecha de fin de soporte de 12 meses `[Verificado MS Learn]`.
  2. Confirmar que la conexión hacia Entra ID utilice **autenticación basada en identidad de aplicación** (estándar GA en `2.5.76.0+` / `2.6.x`) y que la auditoría de acciones administrativas en Event Log de Windows esté activa y recolectada en Sentinel vía AMA `[Verificado MS Learn]`.
  3. Evaluar cargas candidatas para migración progresiva desde Entra Connect Sync hacia **Microsoft Entra Cloud Sync** con múltiples agentes activos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro mensual de versión instalada vs. matriz oficial de soporte Microsoft y estado de agentes Cloud Sync (`PR.PS-02`, `PR.IR-01`) `[Verificado MS Learn]`.

### M-04: Revisión Mensual de Identity Secure Score y Rutas de Ataque de Identidad en Exposure Management
- **Objetivo:** Cerrar brechas estructurales de postura de identidad y romper caminos de movimiento lateral híbrido nube-on-premises `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Identity Secure Score` y `https://security.microsoft.com` > `Exposure management` > `Attack paths` `[Verificado MS Learn]`.
- **Rol Responsable:** IAM Lead + Cybersecurity Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Evaluar todas las acciones de mejora pendientes en **Identity Secure Score** y su impacto en el puntaje global de seguridad `[Verificado MS Learn]`.
  2. Filtrar en **Exposure Management** rutas de ataque híbridas donde una cuenta sincronizada con privilegios en AD on-premises posea también roles privilegiados en la nube (violación de aislamiento entre planos) `[Verificado MS Learn]`.
  3. Verificar que el 100% de las cuentas administrativas de Entra ID sean **exclusivamente cloud-only**, separadas de las cuentas cotidianas de productividad y sincronización AD `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual exportado de *Identity Secure Score* y remediación de cuentas administrativas híbridas detectadas (`ID.RA-05`, `ID.IM-01`) `[Verificado MS Learn]`.

### M-05: Conciliación Mensual de Licenciamiento Entra ID P2, Workload ID y Agent 365
- **Objetivo:** Garantizar cumplimiento estricto de licenciamiento para todos los usuarios, principales de servicio y agentes protegidos por políticas avanzadas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Billing` > `Licenses` y `Monitoring & health` > `Usage & insights` `[Verificado MS Learn]`.
- **Rol Responsable:** IAM Lead + FinOps Analyst `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Verificar que todo usuario incluido en políticas basadas en riesgo de Conditional Access, Token Protection o PIM posea licencia activa **Entra ID P2** (vía **M365 E5**, **M365 E7**, **Microsoft Defender Suite** o standalone) y que `UsageLocation` esté poblado sin errores de asignación `[Verificado MS Learn]`.
  2. Confirmar cobertura de licencias **Microsoft Entra Workload ID Premium** para principales de servicio sujetos a políticas CA o monitoreo de riesgo `[Verificado MS Learn]`.
  3. Validar licencias **Microsoft Agent 365** (o **M365 E7**) para habilitar **Conditional Access for agents** e **ID Protection for agents** en producción `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de conciliación de licencias de identidad sin errores de aprovisionamiento (`GV.OC-03`, `GV.RR-03`) `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Simulacro Obligatorio de Cuentas Break-Glass (Cada <= 90 Días) y Custodia Física
- **Objetivo:** Cumplir el requisito oficial de Microsoft de validar al menos cada 90 días la operatividad de las cuentas de emergencia, sus credenciales **FIDO2 / CBA** y el disparo de alertas críticas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Estación **PAW** dedicada + `https://entra.microsoft.com` + `https://portal.azure.com` (`Monitor > Alerts`) `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Lead + SOC Manager + Custodios Autorizados `[Verificado MS Learn]`.
- **Procedimiento Operativo Numerado:**
  1. Notificar previamente al equipo de monitoreo del SOC la ventana exacta del ejercicio trimestral controlado `[Verificado MS Learn]`.
  2. Retirar de las ubicaciones físicas seguras e ignífugas separadas las llaves de seguridad **FIDO2** (o certificados **CBA**) y autenticar ambas cuentas `*.onmicrosoft.com` desde una **PAW** empleando rutas de red redundantes independientes `[Verificado MS Learn]`.
  3. Verificar que ninguna política nueva de Conditional Access bloquee el inicio de sesión, que ningún usuario haya registrado métodos personales/SSPR sobre las cuentas y que se dispare en minutos la alerta **Severidad 0 - Critical** hacia todos los canales de notificación del SOC `[Verificado MS Learn]`.
  4. Revisar la lista de personal autorizado (rotando combinaciones de cajas fuertes si algún administrador dejó el rol o la organización) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta trimestral firmada de validación Break-Glass (`<= 90 días`) adjuntando el evento en `SigninLogs` y la notificación de alerta recibida por el SOC (`PR.AA-01`, `PR.IR-01`) `[Verificado MS Learn]`.

### T-02 (Trimestral): Ejercicio Purple Team de Identidad (Simulación AiTM, Robo de PRT y Abuso OAuth)
- **Objetivo:** Validar empíricamente la eficacia de **Phishing-resistant MFA**, **Token Protection**, **CAE**, **Entra ID Protection** y **Automatic Attack Disruption** frente a ataques modernos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Entorno controlado de pruebas en `https://entra.microsoft.com` y `https://security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Purple Team + Conditional Access Administrator `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar pruebas controladas con cuentas de laboratorio intentando: (a) phishing reverso **AiTM** contra cuentas con Passkey FIDO2 vs. cuentas con MFA estándar; (b) reproducción de token fuera del dispositivo protegido por **Token Protection** y fuera de la IP autorizada en **CAE estricto**; y (c) solicitud de consentimiento OAuth no autorizado `[Decisión / Propuesta Editorial]`.
  2. Medir la generación de detecciones en `Risk detections`, telemetría en `EntraIdSignInEvents` y tiempos reales de bloqueo/contención `[Verificado MS Learn]`.
  3. Ajustar políticas de Conditional Access y reglas KQL de caza para cerrar cualquier brecha observada `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe trimestral *Identity Purple Team* con matriz de técnicas MITRE ATT&CK probadas y remediaciones aplicadas (`ID.IM-02`, `DE.AE-02`) `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Prueba de Resiliencia de Autenticación, Contingencia CA y Revisión Cross-Tenant B2B
- **Objetivo:** Asegurar continuidad operativa ante fallas de servicios dependientes y auditar todas las relaciones de confianza con tenants externos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Conditional Access` y `External Identities` > `Cross-tenant access settings` `[Verificado MS Learn]`.
- **Rol Responsable:** IAM Lead + Enterprise Cybersecurity Architect `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Revisar y probar en `Report-only` las **políticas de Conditional Access de contingencia** pre-creadas (deshabilitadas en operación normal) diseñadas para mantener acceso seguro ante degradación de un método primario o proveedor externo `[Verificado MS Learn]`.
  2. Si aún subsiste federación AD FS/terceros para algún dominio, probar el plan documentado de conmutación de emergencia hacia **Password Hash Synchronization (PHS)** `[Verificado MS Learn]`.
  3. Auditar todas las organizaciones configuradas en **`Cross-tenant access settings`** (inbound/outbound trust para MFA, dispositivos conformes y B2B Direct Connect), revocando confianzas con socios inactivos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta semestral de prueba de resiliencia de acceso e inventario depurado de relaciones *Cross-tenant* (`PR.IR-01`, `GV.SC-07`) `[Verificado MS Learn]`.

### A-01 (Anual): Auditoría Arquitectónica Anual Zero Trust de Identidad y Mapeo Probatorio NIST CSF 2.0
- **Objetivo:** Evaluar integralmente la arquitectura de **Microsoft Entra ID** contra el **Microsoft Zero Trust Assessment** y los resultados de `PR.AA` en **NIST CSF 2.0** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Herramienta **Microsoft Zero Trust Assessment** + `https://entra.microsoft.com` + `https://purview.microsoft.com` (`Compliance Manager`) `[Verificado MS Learn]`.
- **Rol Responsable:** IAM Lead + Enterprise Cybersecurity Architect + GRC Lead `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo Numerado:**
  1. Ejecutar el módulo de Identidad del **Microsoft Zero Trust Assessment** e inspeccionar el 100% de las configuraciones de tenant (`User settings`, restricciones de creación de tenants por usuarios, consentimiento de apps, configuración B2B y métodos de autenticación) `[Verificado MS Learn]`.
  2. Recertificar el paquete completo de evidencias de auditoría para las subcategorías `PR.AA-01` a `PR.AA-06`, `DE.CM-03` y `RS.MI-01` `[Decisión / Propuesta Editorial]`.
  3. Actualizar el plan anual de modernización (eliminación total de contraseñas residuales, adopción de **Entra Suite** / **Agent 365** y descomisionamiento de AD FS heredado si existiera) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte anual oficial *Zero Trust Assessment (Identity Pillar)* y dossier consolidado de auditoría NIST CSF 2.0 (`GV.OV-01`, `ID.IM-03`, `PR.AA`) `[Verificado MS Learn]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook de Respuesta ante Robo de Token de Sesión / Adversary-in-the-Middle (AiTM)
- **Disparador:** Detecciones `attackerInTheMiddle`, `anomalousToken`, `tokenIssuerAnomaly`, `attemptedPrtAccess` o inicio de sesión válido con token MFA satisfecho desde proxy/IP anónima seguido de actividad sospechosa `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com` > `Incidents` / `Advanced hunting` y `https://entra.microsoft.com` > `ID Protection` / `Users` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. **Revocar inmediatamente todos los tokens de actualización y sesiones activas** del usuario desde el portal (`Revoke sessions`) o vía Microsoft Graph (`POST /v1.0/users/{id}/revokeSignInSessions`), recordando que cambiar la contraseña o deshabilitar la cuenta por sí solo no invalida instantáneamente tokens de acceso no-CAE en vuelo si no se revocan sesiones `[Verificado MS Learn]`.
  2. Marcar al usuario con **`Confirm user compromised`** en **Entra ID Protection** para elevar su riesgo a `High` y activar bloqueos inmediatos de Conditional Access y **CAE** en proveedores compatibles (Exchange, SharePoint, Teams, Graph) `[Verificado MS Learn]`.
  3. Auditar `AuditLogs` y `EntraIdSignInEvents` por `SessionId` y `CorrelationId` para identificar si el atacante registró un nuevo método MFA/Passkey, un dispositivo Entra Registered o concedió permisos a una app OAuth durante el secuestro de sesión `[Verificado MS Learn]`.
  4. Auditar el buzón en Exchange Online eliminando reglas ocultas de reenvío (`Inbox rules` / `ForwardingSmtpAddress`) empleadas para fraude BEC `[Verificado MS Learn]`.
  5. Requerir registro limpio de **Passkey (FIDO2)** mediante **TAP** verificado por identidad antes de rehabilitar el acceso normal `[Verificado MS Learn]`.
- **Evidencia Auditable:** Traza de ejecución de `revokeSignInSessions`, evento `Confirm user compromised`, limpieza de persistencia documentada y migración de la cuenta a MFA resistente a phishing (`RS.MI-01`, `RS.AN-03`) `[Verificado MS Learn]`.

### AH-02: Playbook de Contención Estricta ante Compromiso Confirmado de Cuenta de Usuario o Administrador
- **Disparador:** Confirmación de credenciales robadas (`leakedCredentials` validado como activo), *takeover* de cuenta o alerta de compromiso de administrador `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com` > `Identity` > `Users` > `All users` y `https://security.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada (Orden Crítico Obligatorio):**
  1. **Bloquear el inicio de sesión:** Establecer `Account enabled = No` en Entra ID (y deshabilitar en AD on-premises si la cuenta es híbrida) `[Verificado MS Learn]`.
  2. **Revocar sesiones activas:** Ejecutar `Revoke sessions` / `revokeSignInSessions` para invalidar tokens de actualización y disparar eventos de revocación **CAE** `[Verificado MS Learn]`.
  3. **Purgar métodos MFA y dispositivos sospechosos:** Ejecutar `Require re-register multifactor authentication`, eliminar métodos de autenticación no reconocidos y deshabilitar dispositivos añadidos durante la intrusión `[Verificado MS Learn]`.
  4. **Invalidar credenciales:** Restablecer contraseña (si la cuenta aún posee contraseña) por canal seguro fuera de banda y confirmar que ningún cambio de contraseña malicioso se haya replicado vía *writeback* `[Verificado MS Learn]`.
  5. **Investigar radio de impacto (*Blast Radius*):** Auditar 72 horas previas en `EntraIdSignInEvents`, `AuditLogs`, `CloudAppEvents` y `OfficeActivity` (especialmente si el usuario tenía roles elegibles en **PIM**, verificando si llegó a elevar alguno) `[Verificado MS Learn]`.
  6. **Recuperación controlada:** Emitir un **Temporary Access Pass (TAP)** de un solo uso tras validar identidad por videollamada/presencial para registrar credencial resistente a phishing y recién entonces restablecer `Account enabled = Yes` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Secuencia completa registrada en `AuditLogs` con marcas temporales de bloqueo, revocación, limpieza MFA y expediente forense cerrado (`RS.MI-01`, `RC.RP-05`) `[Verificado MS Learn]`.

### AH-03: Playbook de Investigación y Mitigación de Ataques de Password Spray / Credential Stuffing
- **Disparador:** Alerta `Password Spray` en **Entra ID Protection**, pico súbito de errores `50126` / `50053` (*Account locked*) en `EntraIdSignInEvents` o eventos AD FS `411` / `342` / `516` `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com` > `Advanced hunting` y `https://entra.microsoft.com` > `Protection` > `Conditional Access` / `Authentication methods` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Identificar la infraestructura origen (IPs, proxies residenciales, User-Agents y protocolos empleados) consultando `EntraIdSignInEvents` en las últimas 24–48 horas `[Verificado MS Learn]`.
  2. Determinar de inmediato si **alguna cuenta autenticó exitosamente (`ErrorCode == 0`)** o **falló recién en el desafío MFA (`ErrorCode == 500121`)** desde esas mismas IPs o infraestructura: cualquier cuenta en ambos grupos tiene su contraseña comprometida `[Verificado MS Learn]`.
  3. Contener de inmediato las cuentas alcanzadas ejecutando `AH-02` sobre los éxitos (`0`) y forzando cambio inmediato de contraseña + verificación MFA resistente a phishing sobre los bloqueados por MFA (`500121`) `[Verificado MS Learn]`.
  4. Verificar que **Smart Lockout** y **Microsoft Entra Password Protection** (incluyendo agentes DC on-premises) estén activos, bloquear protocolos legacy si existiera algún hueco y bloquear rangos IP dedicados maliciosos en `Named locations` (o `Set-AdfsProperties -AddBannedIps` si aún opera AD FS) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Lista auditada de cuentas impactadas (`0` y `500121`), cambios de credenciales ejecutados y bloqueo aplicado (`DE.AE-02`, `RS.MI-01`) `[Verificado MS Learn]`.

### AH-04: Playbook de Erradicación de Illicit Consent Grant, App OAuth o Agente IA Malicioso
- **Disparador:** Alerta de aplicación OAuth sospechosa en **Defender for Cloud Apps / XDR**, consentimiento inesperado a permisos `.ReadWrite.All` / `Mail.*` o detección de compromiso en un *Service Principal* / *Agent Identity Blueprint* `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com` > `Identity` > `Applications` > `Enterprise applications` y `https://security.microsoft.com` > `Cloud apps` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. En `Enterprise applications` > `<App sospechosa>` > `Properties`, establecer inmediatamente **`Enabled for users to sign-in? = No`** (deshabilitar el *Service Principal* sin borrarlo inicialmente para preservar evidencia e impedir que un usuario vuelva a re-consentirla) `[Verificado MS Learn]`.
  2. Revocar todas las concesiones de permisos delegados (`OAuth2PermissionGrants`) y permisos de aplicación (`AppRoleAssignments`) asociados mediante Microsoft Graph PowerShell `[Verificado MS Learn]`.
  3. Auditar en `EntraIdSpnSignInEvents`, `CloudAppEvents` y **Purview Audit** todos los datos (correos, archivos SharePoint/OneDrive, directorio) accedidos por el `AppId` durante el período de exposición `[Verificado MS Learn]`.
  4. Endurecer la política de consentimiento de usuario (`User consent settings`) restringiendo el consentimiento únicamente a aplicaciones verificadas de bajo impacto o exigiendo flujo formal de **Admin Consent Workflow** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `AccountEnabled = false` del *Service Principal*, script/log de revocación de `OAuth2PermissionGrants` e informe de alcance de datos accedidos (`PR.AA-05`, `RS.MI-01`) `[Verificado MS Learn]`.

### AH-05: Playbook de Emergencia ante Bloqueo Administrativo o Caída de Federación (Uso Break-Glass)
- **Disparador:** Bloqueo masivo accidental causado por una política de Conditional Access mal configurada, caída crítica de infraestructura federada on-premises o pérdida total de aprobadores activos en PIM `[Verificado MS Learn]`.
- **Consola y Ruta:** Caja fuerte ignífuga + **PAW** + `https://entra.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Obtener autorización verbal/escrita fuera de banda del CISO (o ejecutivo suplente designado) e informar al SOC antes de iniciar sesión para correlacionar la alerta **Severidad 0** `[Verificado MS Learn]`.
  2. Extraer bajo custodia dual la credencial resistente a phishing (**llave física FIDO2** o **CBA**) de la primera cuenta Break-Glass (`*.onmicrosoft.com`) e iniciar sesión desde una **PAW** `[Verificado MS Learn]`.
  3. Revertir exclusivamente la causa del bloqueo (ej. pasar la política de Conditional Access conflictiva a `Report-only`/`Off`, activar la conmutación de emergencia a **PHS** o restaurar aprobadores de PIM), verificando que un administrador nominal recupere el acceso `[Verificado MS Learn]`.
  4. Cerrar inmediatamente la sesión Break-Glass, resguardar todos los registros `SigninLogs` y `AuditLogs` y convocar en menos de 48 horas al equipo **Post-Mortem** para auditar la intervención y actualizar controles preventivos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro completo de acciones ejecutadas por la cuenta Break-Glass y dictamen firmado de revisión Post-Mortem (`PR.AA-01`, `RC.RP-01`) `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL y Microsoft Graph PowerShell Listas para Producción

#### Consulta 1: Detección de Password Spray y Contraseñas Vulneradas Contenidas por MFA (`EntraIdSignInEvents`)
- **Plataforma / Tabla Principal:** Microsoft Defender XDR Advanced Hunting (`EntraIdSignInEvents`, tabla oficial en GA que reemplazó a `AADSignInEventsBeta` el `2026-10-19`) `[Verificado MS Learn]`.
- **Propósito:** Identificar en una sola consulta IPs ejecutando *Password Spray* (`50126`) y advertir si lograron adivinar contraseñas válidas que chocaron contra MFA (`500121`) o autenticaron con éxito (`0`).
```kql
// Detecta Password Spray en EntraIdSignInEvents y alerta si hubo aciertos de contraseña (0 o 500121)
EntraIdSignInEvents
| where Timestamp > ago(4h)
| where ErrorCode in (0, 50126, 500121, 50053)
| summarize FailedSpray = countif(ErrorCode == 50126),
            LockedAccounts = countif(ErrorCode == 50053),
            ValidPwdBlockedByMFA = countif(ErrorCode == 500121),
            SuccessfulLogons = countif(ErrorCode == 0),
            TargetedUsers = dcountif(AccountUpn, ErrorCode == 50126),
            CompromisedCandidates = make_set_if(AccountUpn, ErrorCode in (0, 500121), 25)
            by IPAddress, Country
| where TargetedUsers >= 8 and FailedSpray >= 20
| order by ValidPwdBlockedByMFA desc, SuccessfulLogons desc, FailedSpray desc
```

#### Consulta 2: Caza de Posible Robo de Token / AiTM y Discrepancias de Ubicación CAE
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`SigninLogs` + `AADNonInteractiveUserSignInLogs`) `[Verificado MS Learn]`.
- **Propósito:** Correlacionar sesiones con riesgo medio/alto o uso de un mismo `OriginalRequestId` / sesión desde múltiples países o direcciones IP en ventanas cortas.
```kql
// Identifica sesiones que cambian abruptamente de IP/País tras satisfacer autenticación inicial
union SigninLogs, AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| where ResultType == "0"
| extend Country = tostring(LocationDetails.countryOrRegion)
| summarize DistinctIPs = dcount(IPAddress),
            DistinctCountries = dcount(Country),
            IPList = make_set(IPAddress, 10),
            Countries = make_set(Country, 5),
            MaxRisk = make_set(RiskLevelDuringSignIn, 5),
            FirstSeen = min(TimeGenerated),
            LastSeen = max(TimeGenerated)
            by UserPrincipalName, CorrelationId, AppDisplayName
| where DistinctCountries > 1 or (DistinctIPs >= 3 and tostring(MaxRisk) has_any ("medium", "high"))
| order by DistinctCountries desc, DistinctIPs desc
```

#### Consulta 3: Alerta Crítica de Cualquier Actividad en Cuentas Break-Glass y Asignaciones Fuera de PIM
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`SigninLogs` + `AuditLogs`) `[Verificado MS Learn]`.
- **Propósito:** Monitorear uso exitoso o fallido de cuentas de emergencia `*.onmicrosoft.com` y detectar elevaciones directas de roles que omitan `MS-PIM`.
```kql
// Reemplazar con los ObjectId reales de las cuentas Break-Glass del tenant
let BreakGlassObjectIds = dynamic(["00aa00aa-bb11-cc22-dd33-44ee44ee44ee", "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"]);
let BreakGlassSignIns = SigninLogs
| where TimeGenerated > ago(24h)
| where UserId in (BreakGlassObjectIds) or UserPrincipalName has_any ("bg-admin", "emergency")
| project TimeGenerated, AlertType = "USO CUENTA BREAK-GLASS (SEV-0)", Actor = UserPrincipalName, Target = AppDisplayName, Detail = strcat("IP: ", IPAddress, " | Result: ", ResultType);
let DirectRoleAssignments = AuditLogs
| where TimeGenerated > ago(24h)
| where Category == "RoleManagement" and OperationName == "Add member to role"
| where tostring(InitiatedBy.app.displayName) != "MS-PIM"
| project TimeGenerated, AlertType = "ROL ASIGNADO FUERA DE PIM", Actor = tostring(InitiatedBy.user.userPrincipalName), Target = tostring(TargetResources[0].displayName), Detail = tostring(TargetResources[1].userPrincipalName);
union BreakGlassSignIns, DirectRoleAssignments
| order by TimeGenerated desc
```

#### Consulta 4: Medición de Adopción de Métodos Resistentes a Phishing (Passkeys FIDO2, WHfB, CBA) vs. Métodos Débiles
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`SigninLogs`) `[Verificado MS Learn]`.
- **Propósito:** Producir evidencia objetiva para `KPI-02` y `PR.AA-02` clasificando autenticaciones reales según nivel de resistencia al phishing.
```kql
// Clasifica los métodos MFA utilizados en inicios exitosos de los últimos 30 días
SigninLogs
| where TimeGenerated > ago(30d) and ResultType == "0"
| mv-expand AuthDetail = parse_json(AuthenticationDetails)
| extend AuthMethod = tostring(AuthDetail.authenticationMethod)
| where isnotempty(AuthMethod) and AuthMethod != "Previously satisfied"
| extend StrengthTier = case(
    AuthMethod in ("FIDO2 security key", "Passkey (device-bound)", "Passkey (synced)", "Windows Hello for Business", "X.509 Certificate (Multi-Factor)"), "1 - Phishing-Resistant (AAL3/FIDO2)",
    AuthMethod in ("PhoneAppNotification", "Passwordless phone sign-in", "Microsoft Authenticator app"), "2 - Strong MFA (App)",
    AuthMethod in ("Text message", "SMS", "Voice call", "One-time passcode"), "3 - Phishable / Legacy MFA (Migrar)",
    "4 - Single Factor / Otro")
| summarize SignInCount = count(), DistinctUsers = dcount(UserPrincipalName) by StrengthTier, AuthMethod
| order by StrengthTier asc, SignInCount desc
```

#### Consulta 5: Detección de Consentimientos OAuth Peligrosos e Inyección de Secretos en Aplicaciones
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`AuditLogs`) `[Verificado MS Learn]`.
- **Propósito:** Detectar ataques de *Illicit Consent Grant* y persistencia mediante adición de secretos/certificados en registros de aplicaciones.
```kql
// Vigila concesiones de permisos Graph de alto impacto y cambios en credenciales de aplicaciones
AuditLogs
| where TimeGenerated > ago(7d)
| where Category == "ApplicationManagement"
| where OperationName in ("Consent to application", "Add app role assignment to service principal", "Add OAuth2PermissionGrant", "Update application – Certificates and secrets management")
| extend Actor = coalesce(tostring(InitiatedBy.user.userPrincipalName), tostring(InitiatedBy.app.displayName)),
         TargetApp = tostring(TargetResources[0].displayName),
         ModifiedProps = tostring(TargetResources[0].modifiedProperties)
| where OperationName has "Certificates and secrets" or ModifiedProps has_any ("Mail.ReadWrite", "Files.ReadWrite.All", "Directory.ReadWrite.All", "RoleManagement.ReadWrite.Directory", "Application.ReadWrite.All")
| project TimeGenerated, OperationName, Actor, TargetApp, Result, ModifiedProps
| order by TimeGenerated desc
```

#### Consulta 6: Evaluación de Cobertura Conditional Access y Bloqueos de Autenticación Heredada
- **Plataforma / Tabla Principal:** Microsoft Sentinel (`SigninLogs`) `[Verificado MS Learn]`.
- **Propósito:** Identificar brechas donde `ConditionalAccessStatus == "notApplied"` y confirmar el bloqueo (`53003`) de clientes legacy.
```kql
// Audita estado de aplicación de Conditional Access y eventuales escapes de autenticación heredada
SigninLogs
| where TimeGenerated > ago(14d)
| extend IsLegacyClient = ClientAppUsed !in ("Browser", "Mobile Apps and Desktop clients", "")
| summarize TotalEvents = count(),
            DistinctUsers = dcount(UserPrincipalName),
            BlockedByCA_53003 = countif(ResultType == "53003"),
            SuccessfulSignIns = countif(ResultType == "0")
            by ConditionalAccessStatus, IsLegacyClient, ClientAppUsed
| order by IsLegacyClient desc, TotalEvents desc
```

#### Consulta 7: Auditoría de Estado de Migración Authentication Methods, Passkeys y Cuentas Admin vía Microsoft Graph PowerShell
- **Plataforma / Tabla Principal:** Microsoft Graph PowerShell (`policies/authenticationMethodsPolicy` y `roleManagement/directory`) `[Verificado MS Learn]`.
- **Propósito:** Extraer evidencia directa de configuración para auditoría NIST CSF 2.0 (`Migration Complete`, estado de FIDO2/Passkeys y conteo de asignaciones activas vs. elegibles de Global Admin).
```powershell
# Requiere Microsoft.Graph y rol Global Reader / Security Reader
Connect-MgGraph -Scopes "Policy.Read.All", "RoleManagement.Read.Directory" -NoWelcome

# 1. Verifica estado Migration Complete y métodos habilitados en la directiva unificada
$authPolicy = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/policies/authenticationMethodsPolicy"
Write-Output ("Estado Migración Auth Methods: " + $authPolicy.policyMigrationState)
$authPolicy.authenticationMethodConfigurations | Select-Object id, state | Format-Table -AutoSize

# 2. Audita asignaciones Permanentes Activas vs Elegibles PIM para Global Administrator
$gaRoleId = "62e90394-69f5-4237-9190-012177145e10"
$activeGA = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignmentScheduleInstances?`$filter=roleDefinitionId eq '$gaRoleId'").value
$eligibleGA = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/roleManagement/directory/roleEligibilityScheduleInstances?`$filter=roleDefinitionId eq '$gaRoleId'").value
Write-Output ("Global Admins Activos (solo Break-Glass): " + $activeGA.Count + " | Elegibles PIM (<5): " + $eligibleGA.Count)
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life") de Microsoft Entra ID

| Control Crítico de Identidad | Estado Operativo Esperado ("Proof of Life") | Ruta de Verificación en Consola | Etiqueta |
|---|---|---|---|
| **Directiva Authentication Methods** | `policyMigrationState == migrationComplete`; métodos `FIDO2 / Passkey` y `Microsoft Authenticator` activos; `Custom Controls` en cero. | `entra.microsoft.com` > `Protection` > `Authentication methods` > `Policies` | `[Verificado MS Learn]` |
| **Conditional Access Zero Trust** | Bloqueo 100% de *Legacy Auth*; `Phishing-resistant MFA` exigido a todos los roles admin; acción `Register security information` protegida con TAP/Compliant Device; políticas `User Risk = High` y `Sign-in Risk = Medium/High` activas. | `entra.microsoft.com` > `Protection` > `Conditional Access` > `Policies` | `[Verificado MS Learn]` |
| **Token Protection y CAE** | CAE activo con *Named Locations* depuradas y piloto/producción de *Strictly enforce location* + **Token Protection** aplicado sobre Exchange, SharePoint y Teams. | `entra.microsoft.com` > `Conditional Access` > `Session controls` / Workbook CAE | `[Verificado MS Learn]` |
| **Privileged Identity Management (PIM)** | `< 5` `Global Administrators` elegibles; 0 administradores humanos permanentes; alertas de seguridad de PIM revisadas y en cero. | `entra.microsoft.com` > `Identity governance` > `PIM` > `Alerts` | `[Verificado MS Learn]` |
| **Cuentas Break-Glass** | >= 2 cuentas cloud-only `*.onmicrosoft.com` con **Passkey FIDO2 / CBA**, excluidas de políticas CA de bloqueo, con alerta Severidad 0 verificada en los últimos 90 días. | `entra.microsoft.com` > `Users` + `portal.azure.com` > `Monitor > Alerts` | `[Verificado MS Learn]` |
| **ITDR en Defender XDR + Híbrido** | Tabla `EntraIdSignInEvents` recibiendo eventos, **Automatic Attack Disruption** activo, **PHS** habilitado y **Entra Connect Sync v2.6.x** dentro de los 12 meses de soporte. | `security.microsoft.com` > `Advanced hunting` + `entra.microsoft.com` > `Entra Connect` | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de 8 KPIs Operativos y Ejecutivos de Identidad

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Adopción de MFA Resistente a Phishing (Passkeys FIDO2 / WHfB / CBA)** | `(Usuarios activos autenticando con FIDO2, WHfB o CBA / Total de usuarios activos) * 100` | `100%` Administradores · `>= 85%` Usuarios Generales | Mensual | CISO, IAM Lead y Auditoría | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cobertura Efectiva de Conditional Access sobre Inicios Exitosos** | `(Inicios de sesión interactivos y no interactivos con ConditionalAccessStatus == "success" / Total inicios exitosos) * 100` | `>= 99%` (excluyendo solo cuentas Break-Glass sin actividad) | Semanal / Mensual | IAM Lead y Conditional Access Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tiempo Medio de Remediación de Identidades en Riesgo Alto (MTTR-Identity)** | `Mediana(RemediationTimestamp - RiskDetectionTimestamp)` para usuarios, workloads y agentes en riesgo `High` | `<= 15 min` vía auto-remediación CA/XDR · `<= 4 horas` casos manuales | Diaria / Semanal | SOC Manager y Analistas ITDR | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Índice de Elevación Just-In-Time (Zero Standing Admin Ratio)** | `(Sesiones con roles administrativos de Entra iniciadas vía activación PIM / Total sesiones administrativas) * 100` | `100%` humanos vía PIM JIT (`< 5` Global Admins elegibles) | Mensual | CISO, IAM Lead y GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa Residual de Autenticación Heredada y MFA Telefónico (SMS/Voz)** | `(Inicios exitosos usando protocolos Legacy o SMS/Voz / Total inicios exitosos) * 100` | `0.0%` Legacy Auth · `< 2%` SMS/Voz en transición final | Mensual | IAM Lead y Cybersecurity Architect | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Higiene de Credenciales de Aplicaciones y Agentes IA Gobernados** | `(Apps y Agent Blueprints usando Federación/Certificados vigentes <=180d y Sponsor activo / Total identidades no humanas) * 100` | `>= 95%` sin secretos expirados ni agentes huérfanos | Semanal / Mensual | App Security & Agent Governance Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Salud y Vigencia de Sincronización Híbrida (Connect Sync / Cloud Sync)** | `% ciclos PHS/Sync exitosos en SLA` y `Meses restantes de soporte de la versión instalada de Entra Connect v2.x` | `>= 99.9%` ciclos exitosos · `>= 3 meses` margen antes de fin de soporte | Mensual | Hybrid Identity Lead e Infraestructura | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Identity Secure Score y Cumplimiento de Pruebas Break-Glass** | `Puntaje porcentual alcanzado en Identity Secure Score` y `Días desde el último simulacro Break-Glass documentado` | `Identity Secure Score >= 88%` · Prueba Break-Glass `<= 90 días` | Mensual / Trimestral | CISO y Comité de Riesgos | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de Cinco Niveles para Microsoft Entra ID

| Nivel | Estado del Plano de Autenticación y Acceso | Privilegios, Híbrido e Identidades No Humanas | Detección y Respuesta ITDR (SOC) | Etiqueta |
|---|---|---|---|---|
| **Nivel 1 — Inicial** | Contraseñas + MFA por usuario heredado o SMS; autenticación legacy permitida; sin Conditional Access estructurado. | Múltiples `Global Administrators` permanentes; cuentas admin sincronizadas desde AD; Entra Connect desactualizado; sin cuentas Break-Glass formales. | Logs de Entra retenidos solo 7–30 días sin integración SIEM/XDR; sin monitoreo de riesgo ni playbooks de identidad. | `[Decisión / Propuesta Editorial]` |
| **Nivel 2 — Básico Gestionado** | Migración completada a `Authentication methods`; bloqueo de Legacy Auth; políticas CA base exigiendo MFA estándar. | Inicio de adopción de **PIM** en roles principales; 2 cuentas Break-Glass creadas pero sin pruebas trimestrales sistemáticas; PHS habilitado. | Exportación de `SigninLogs` y `AuditLogs` a Sentinel; revisión reactiva manual de `Risky users` sin políticas automáticas de riesgo. | `[Decisión / Propuesta Editorial]` |
| **Nivel 3 — Definido Zero Trust** *(Meta Base E5)* | **Authentication Strengths** exigiendo `Phishing-resistant MFA` al 100% de admins; acción `Register security info` protegida con TAP; políticas CA basadas en riesgo de usuario y sesión activas. | **100% humanos Eligible en PIM** (`< 5` GA); admins 100% cloud-only; Break-Glass con **FIDO2/CBA** probadas cada <=90 días; Entra Connect v2.6.x vigente. | Integración activa con **Defender XDR** (`EntraIdSignInEvents`), **Automatic Attack Disruption** habilitado y playbooks probados para AiTM y Password Spray. | `[Decisión / Propuesta Editorial]` |
| **Nivel 4 — Avanzado y Resistente a Robo de Tokens** | Despliegue amplio de **Passkeys (FIDO2)** (device-bound y synced) en usuarios; **Token Protection** activo en apps nativas M365 y **CAE** con *Strictly enforce location* en redes conocidas. | Gobierno estricto de `Workload Identities` con federación libre de secretos; servidores híbridos aislados en Tier-0 o migrados a **Cloud Sync** HA; pruebas semanales con **Maester**. | Caza proactiva semanal de sesiones anómalas y abuso OAuth; ejercicios *Purple Team* trimestrales midiendo MTTC en minutos. | `[Decisión / Propuesta Editorial]` |
| **Nivel 5 — Adaptativo y Agéntico** | Operación 100% *Passwordless* empresarial; acceso adaptativo continuo uniendo señales de **Purview Adaptive Protection**, red **Global Secure Access** y riesgo en tiempo real. | Gobierno integral de **Microsoft Entra Agent ID** (*Agent Blueprints*, *Custom Security Attributes*, *Sponsors*) licenciado con **Agent 365 / M365 E7**; gestión de políticas CA 100% *Policy-as-Code*. | Respuesta autónoma calibrada sobre humanos, principales de servicio y agentes IA (`Risky agents`) con remediación verificada y cero deuda de privilegios. | `[Decisión / Propuesta Editorial]` |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

La siguiente matriz documenta 11 subcategorías oficiales de **NIST CSF 2.0 (CSWP 29)** cubriendo las **6 funciones (`GV`, `ID`, `PR`, `DE`, `RS`, `RC`)** con artefactos de evidencia directa en **Microsoft Entra ID** `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Subcategoría (CSWP 29) | Resultado Esperado | Capacidad Habilitadora en Microsoft Entra ID (`01`) | Evidencia Auditable Reproducible | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.PO-01` | Se establecen, comunican y aplican políticas y procedimientos para gestionar riesgos de ciberseguridad. | Motor **Conditional Access**, directiva unificada **Authentication methods** (`Migration Complete`) y políticas gestionadas como código. | Exportación JSON/Maester fechada de políticas de Conditional Access y `authenticationMethodsPolicy` activas. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de seguridad son establecidos, aplicados y revisados. | Delegación granular con **Microsoft Entra RBAC**, *Administrative Units* y **Privileged Identity Management (PIM)**. | Reporte CSV de asignaciones PIM demostrando separación de funciones, `< 5` Global Admins elegibles y 0 admins humanos permanentes. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-02` | Se mantienen inventarios de software, servicios, aplicaciones e identidades no humanas. | Registro de **Enterprise Applications**, **App Registrations**, *Service Principals* y **Microsoft Entra Agent ID** (*Blueprints*). | Inventario exportado de aplicaciones OAuth, identidades de carga de trabajo y agentes con propietario/*Sponsor* asignado. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-05` | Amenazas, vulnerabilidades, probabilidades e impactos se integran para priorizar el riesgo. | **Entra ID Protection**, **Identity Secure Score** y rutas de ataque de identidad en **Exposure Management** *(MITRE Valid Accounts T1078)*. | Reporte mensual de *Identity Secure Score* e informe de cierre de rutas de ataque híbridas hacia cuentas privilegiadas. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-01` | Las identidades y credenciales son emitidas, gestionadas, verificadas, revocadas y auditadas. | Ciclo de credenciales con **TAP**, **Passkeys (FIDO2)**, sincronización **Entra Connect v2.6.x / Cloud Sync** y cuentas **Break-Glass**. | Registros `AuditLogs` de emisión/revocación de credenciales y actas trimestrales (`<=90d`) de validación Break-Glass. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-02` | Las identidades son verificadas y vinculadas a credenciales acordes al contexto de riesgo. | **Passkey profiles** con atestación FIDO MDS, **CBA**, **WHfB** y protección de `Register security information` en Conditional Access *(MITRE Modify Authentication Process T1556)*. | Configuración exportada de perfiles FIDO2 y política CA que exige TAP o dispositivo conforme para registrar credenciales. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-03` | Los usuarios, servicios y hardware son autenticados de forma segura y continua. | **Authentication Strengths** (*Phishing-resistant MFA*), **Token Protection** (PRT) y **CAE** (*Strictly enforce location*) *(MITRE Steal Application Access Token T1528 / Web Session Cookie T1539)*. | `SigninLogs` / `EntraIdSignInEvents` evidenciando `AuthenticationRequirement == multiFactorAuthentication`, bloqueo Legacy Auth (`53003`) y evaluación CAE. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los derechos de acceso y autorizaciones aplican mínimo privilegio y segregación de funciones. | **PIM JIT** (aprobación dual, expiración horaria, MFA FIDO2), gobernanza de consentimiento OAuth y **Conditional Access for agents**. | Historial `PIM Resource audit`, alertas PIM en cero y configuración restrictiva de *User consent settings*. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-03` | La actividad del personal y los accesos de identidades/servicios se monitorean para detectar eventos adversos. | Detecciones en tiempo real y offline de **Entra ID Protection** (`Risky users`, `Risky workload identities`, `Risky agents`) e ingesta en **`EntraIdSignInEvents`**. | Reporte de `Risk detections` (90 días) y reglas analíticas activas sobre Password Spray, AiTM y elevaciones fuera de horario. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos oportunamente para frenar su propagación. | Políticas CA basadas en riesgo (`High -> Block`), **Automatic Attack Disruption** (`Suspend user in Entra` + `Revoke user session`) y API `revokeSignInSessions`. | Bitácora del `Action center` en Defender XDR y `AuditLogs` demostrando suspensión y revocación inmediata ante AiTM. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de cuentas y accesos restaurados antes de retornar a operación normal. | Flujo de limpieza MFA (`Require re-register MFA`), reemisión controlada con **TAP**, desbloqueo verificado y revisión **Post-Mortem** Break-Glass. | Registros `AuditLogs` de re-registro limpio de credenciales resistentes a phishing y actas de recuperación de cuenta. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Rutas Oficiales en Microsoft Learn | Ninja Trainings, Herramientas y Comunidad MVP (2026) | Certificaciones Vigentes Recomendadas | Meta de Acreditación | Etiqueta |
|---|---|---|---|---|---|
| **IAM Lead & Conditional Access Admin** | **Microsoft Entra SecOps Guide**, **Plan phishing-resistant passwordless deployment**, **Token Protection & CAE** | *Microsoft Entra Identity & Agents Ninja Training 2026*, *Entra.News* y **Maester** (Merill Fernando), blog de Jan Bakker | **SC-300: Microsoft Identity and Access Administrator Associate** | `SC-300` activa en primeros 90 días + laboratorio práctico de políticas como código. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **SOC Analysts L1 / L2 / L3 (ITDR)** | **Investigate risk with Microsoft Entra ID Protection**, **Token Theft / Password Spray / App Consent IR Playbooks** | *Microsoft Defender XDR Ninja Training*, *Microsoft Sentinel Ninja Training*, blog de Jeffrey Appel | **SC-200: Microsoft Security Operations Analyst Associate** | Dominio práctico de `EntraIdSignInEvents` y ejecución trimestral de playbooks `AH-01` a `AH-04`. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Identity & Zero Trust Architect** | **Microsoft Security Adoption Framework (SAF)**, **MCRA (Junio 2026)**, **Microsoft Entra Agent ID Architecture** | Publicaciones de Alex Simons, Mark Simos y Thomas Naunheim (arquitectura Enterprise Scale / Tiering en Entra) | **SC-100: Microsoft Cybersecurity Architect Expert** (con base `SC-300`) | Certificación `SC-100` vigente y liderazgo de la auditoría anual Zero Trust (`A-01`). | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Hybrid Identity Engineer** | **Microsoft Entra Connect Sync v2.x & Cloud Sync Documentation**, **Protect Tier-0 Hybrid Identity** | Guías de migración AD -> Cloud Sync y pruebas de postura híbrida en Maester 2.2+ | **SC-300** + **AZ-800 / AZ-801** (Seguridad híbrida Windows Server AD) | Ejecución semestral de pruebas de conmutación en *Staging Mode* y salud PHS. | `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Actualizaciones Verificadas contra Microsoft Learn MCP al `2026-11-11`

| # | Componente Revalidado | Estado en Fuentes Previas (`MSEOP-MD` Mar 2026) | Estado Oficial Verificado al `2026-11-11` y Corrección Aplicada | Etiqueta |
|---|---|---|---|---|
| **1** | **Convergencia obligatoria a Authentication Methods Policy** | Algunos listados previos aún citaban rutas antiguas de configuración MFA por usuario y SSPR separado. | Confirmado en MS Learn que desde el **30 de septiembre de 2025** ya no se pueden gestionar métodos en las directivas heredadas MFA/SSPR; se exige estado **`Migration Complete`**, vigilancia del tope de **20 KB** y consolidación en grupos. | `[Verificado MS Learn]` |
| **2** | **Cuentas Break-Glass con MFA Resistente a Phishing Obligatorio** | Un bloque previo de `MSEOP-MD` indicaba solo "contraseñas largas y aleatorias en bóveda física" para cuentas Break-Glass. | Actualizado conforme a la guía oficial vigente de Microsoft Learn: las cuentas de emergencia deben cumplir MFA obligatorio registrando **Passkey (FIDO2)** (recomendado) o **Certificate-Based Authentication (CBA)**, operando desde **PAW** y validándose cada **<= 90 días**. | `[Verificado MS Learn]` |
| **3** | **External MFA (EAM) en GA y retiro de Custom Controls** | No se detallaba el calendario de bloqueo y retiro de controles personalizados en Conditional Access. | Incorporado que **External MFA** está en GA y que desde **septiembre de 2026** no se permite crear ni editar **Custom Controls**, con retiro total programado para **inicios de 2027**. | `[Verificado MS Learn]` |
| **4** | **Deprecación de `AADSignInEventsBeta` por `EntraIdSignInEvents`** | Guías previas usaban `SigninLogs` exclusivamente o referenciaban la tabla beta `AADSignInEventsBeta`. | Verificado que el **19 de octubre de 2026** `AADSignInEventsBeta` quedó deprecada y migró automáticamente a **`EntraIdSignInEvents`** (con `EntraIdDeviceId`), incorporada en la arquitectura y consultas KQL. | `[Verificado MS Learn]` |
| **5** | **Passkeys (FIDO2) Device-Bound, Synced y Flujo MC1450133** | Solo se mencionaban llaves físicas FIDO2 y Authenticator tradicional sin distinguir *synced passkeys*. | Documentada la distinción oficial entre **device-bound passkeys** (con atestación MDS) y **synced passkeys** (iCloud/Google, 14x más rápidas, sin atestación), más el endurecimiento del registro directo de noviembre de 2026 (**MC1450133**) protegiendo `Register security information`. | `[Verificado MS Learn]` |
| **6** | **Alcance exacto de Token Protection y CAE Estricto** | Se citaban CAE y Token Protection de forma genérica sin detallar plataformas ni restricciones de red. | Precisada disponibilidad GA de **Token Protection** en apps nativas Windows/iOS/macOS (Preview web ARM) y el modo **CAE Strictly enforce location policies** basado en `IP address (seen by resource)` y el Workbook oficial *CAE Insights*. | `[Verificado MS Learn]` |
| **7** | **Ciclo de soporte de Microsoft Entra Connect Sync v2.6.x** | No se especificaba la caducidad rodante de 12 meses ni las versiones vigentes de finales de 2026. | Incorporada la rama vigente **`2.6.92.0` (23-sep-2026)**, la regla estricta de fin de soporte a **12 meses** del build siguiente (ej. retiro de `2.5.79.0` el `2026-10-23`) y autenticación por identidad de aplicación en GA. | `[Verificado MS Learn]` |
| **8** | **Incorporación de Microsoft Entra Agent ID y Renombres de Suites** | Ausencia de gobierno operativo de agentes IA en Entra y mención exclusiva a *E5 Security / E5 Compliance*. | Añadidos **Microsoft Entra Agent ID**, **Conditional Access for agents** (OBO, autónomo y *Agent User*), **ID Protection for agents** (`Risky agents`), **Microsoft Agent 365 / M365 E7** y el renombre a **Microsoft Defender Suite** / **Microsoft Purview Suite**. | `[Verificado MS Learn]` |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas

| Elemento Definido en esta Guía | Clasificación | Justificación Arquitectónica y Operativa |
|---|---|---|
| **Separación limpia de alcance entre Módulo `01` (Core IAM, CA & ITDR) y Módulo `02` (IGA)** | `Propuesta Editorial` | Evita duplicidades documentales al concentrar en `01` el plano de autenticación, acceso condicional, PIM táctico de roles privilegiados y detección/respuesta ITDR, reservando JML *Lifecycle Workflows*, *Access Packages* y campañas amplias de *Access Reviews* para `02_Microsoft_Entra_ID_Governance`. |
| **Protección obligatoria de `Register security information` con TAP o Dispositivo Conforme** | `Propuesta Editorial` | Cierra la ruta de ataque donde un adversario que robó una contraseña aprovecha la simplificación de registro de passkeys (nov-2026) para persistir con su propia credencial resistente a phishing. |
| **Umbrales cuantitativos de KPIs y ventanas PIM (<=4h Ingeniería, <=2h Tier-0 con aprobación dual)** | `Propuesta Editorial` | Microsoft provee los controles configurables en PIM e ID Protection; fijar `< 5` Global Admins, ventanas de 2 a 4 horas y remediación de riesgo alto en `< 4 horas` traduce Zero Trust en metas auditables. |
| **Automatización semanal de pruebas de postura como código con Maester** | `Propuesta Editorial` | Complementa las consolas nativas con verificación continua independiente en CI/CD para detectar inmediatamente exclusiones indebidas o deriva en Conditional Access. |
| **Modelo de Madurez de Cinco Niveles hasta Operación 100% Passwordless y Agéntica** | `Propuesta Editorial` | Ofrece una hoja de ruta progresiva y realista para organizaciones que parten desde MFA híbrido tradicional hacia Passkeys FIDO2, Token Protection y gobierno de agentes en Entra Agent ID. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn y Licenciamiento
- **REF-01:** *Microsoft Entra Security Operations (SecOps) Guide* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/architecture/security-operations-introduction`). Guía arquitectónica oficial de monitoreo y detección en cuentas de usuario, cuentas privilegiadas, PIM, aplicaciones, dispositivos e infraestructura `[Verificado MS Learn]`.
- **REF-02:** *Manage authentication methods & Migrate legacy MFA and SSPR policies* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-methods-manage`). Fin de administración en políticas heredadas el `2025-09-30`, estado `Migration Complete` y límite de 20 KB `[Verificado MS Learn]`.
- **REF-03:** *Authentication methods in Microsoft Entra ID — Passkeys (FIDO2)* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-passkeys-fido2`). Especificación oficial de *device-bound passkeys*, *synced passkeys* y atestación FIDO MDS `[Verificado MS Learn]`.
- **REF-04:** *Migrate from custom controls to external MFA in Conditional Access* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/conditional-access/how-to-migrate-custom-controls-external-mfa`). Disponibilidad general de External MFA, bloqueo de Custom Controls en septiembre de 2026 y retiro a inicios de 2027 `[Verificado MS Learn]`.
- **REF-05:** *Token Protection in Microsoft Entra Conditional Access* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection`). Disponibilidad GA en apps nativas Windows/iOS/macOS y Preview web ARM mediante vinculación PRT `[Verificado MS Learn]`.
- **REF-06:** *Strictly enforce location policies using Continuous Access Evaluation (CAE)* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation-strict-enforcement`). Bloqueo inmediato basado en `IP address (seen by resource)` y Workbook *CAE Insights* `[Verificado MS Learn]`.
- **REF-07:** *Conditional Access authentication strengths & Microsoft-managed policies* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths` y `https://learn.microsoft.com/en-us/entra/identity/conditional-access/managed-policies`). Fortalezas resistentes a phishing y ventana de 45 días de políticas gestionadas por Microsoft `[Verificado MS Learn]`.
- **REF-08:** *Manage emergency access accounts in Microsoft Entra ID (Break-Glass)* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access`). Exigencia de Passkey FIDO2 o CBA, custodia física, alertas Severidad 0 y pruebas cada <=90 días `[Verificado MS Learn]`.
- **REF-09:** *Automatic attack disruption in Microsoft Defender XDR & EntraIdSignInEvents Schema* — Microsoft Learn (`https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption` y `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-aadsignineventsbeta-table`). Suspensión automática de cuentas comprometidas y transición el `2026-10-19` hacia `EntraIdSignInEvents` `[Verificado MS Learn]`.
- **REF-10:** *Microsoft Entra Connect Sync: Version release history & Cloud Sync* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-version-history` y `https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync`). Historial de builds `2.6.92.0` (sep-2026), política de retiro a 12 meses y aprovisionamiento Cloud Sync `[Verificado MS Learn]`.
- **REF-11:** *What is Microsoft Entra Agent ID?, Conditional Access for agents & ID Protection for agents* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id`, `https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id` y `https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents`). Seguridad integral para agentes autónomos y relación con **Microsoft Agent 365** `[Verificado MS Learn]`.
- **REF-12:** *Microsoft Incident Response Playbooks: Token Theft, Password Spray & App Consent Grant* — Microsoft Learn (`https://learn.microsoft.com/en-us/security/operations/token-theft-playbook`, `https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-password-spray` y `https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-app-consent`). Playbooks oficiales de respuesta a incidentes de identidad `[Verificado MS Learn]`.
- **REF-13:** *Microsoft Entra Licensing Fundamentals & Subscription Suites Guidance* — Microsoft Learn (`https://learn.microsoft.com/en-us/entra/fundamentals/licensing` y `https://www.microsoft.com/licensing/guidance/subscription-suites`). Evidencia contractual de inclusión de Entra ID P2 en M365 E5/E7 y *Microsoft Defender Suite* `[Verificado MS Learn]`.

### Blogs Oficiales y Empleados de Microsoft
- **REF-14:** Alex Simons (CVP, Microsoft Identity & Network Access) — *Microsoft Entra Blog — Announcing Microsoft Entra Agent ID & Identity Innovations* (`https://techcommunity.microsoft.com/t5/microsoft-entra-blog/bg-p/Identity`). Hoja de ruta oficial de autenticación passwordless, Passkeys y era agéntica `[Verificado MS Learn]`.
- **REF-15:** Merill Fernando (Principal Product Manager, Microsoft Entra) — *Entra.News & Maester Automated Microsoft Security Testing* (`https://entra.news` y `https://maester.dev`). Referencia técnica comunitaria y oficial sobre Conditional Access, protección de agentes y pruebas continuas en PowerShell `[Verificado MS Learn]`.
- **REF-16:** Mark Simos (Principal Lead Cybersecurity Architect, Microsoft) — *Zero Trust Identity & Access Reference Architecture in MCRA / SAF* (`https://learn.microsoft.com/en-us/security/adoption/mcra`). Diseño de aislamiento privilegiado y acceso adaptativo dentro del ecosistema Microsoft `[Verificado MS Learn]`.

### Comunidad MVP de Seguridad e Identidad Microsoft
- **REF-17:** Jan Bakker (Microsoft Security & Entra MVP) — *How to secure passkey registration in Entra ID (MC1450133) & Conditional Access Guides* (`https://janbakker.tech/how-to-secure-passkey-registration-in-entra-id/`). Mejores prácticas operativas de noviembre de 2026 para blindar el registro de Passkeys y evitar bucles de políticas `[Verificado MS Learn]`.
- **REF-18:** Thomas Naunheim & Daniel Chronlund (Microsoft Security MVPs) — *Enterprise-Scale Identity Tiering, Workload Identities & Conditional Access Frameworks* (`https://www.cloud-architekt.net` y `https://danielchronlund.com`). Referencias de la comunidad experta sobre modelo de niveles administrativos en Entra ID y diseño de Conditional Access `[Verificado MS Learn]`.

### Marcos Normativos
- **REF-19:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)* (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`) y *NIST SP 800-63B Digital Identity Guidelines* (`https://pages.nist.gov/800-63-3/sp800-63b.html`). Estándares normativos para `PR.AA` y niveles de aseguramiento de autenticación resistentes a phishing (AAL2/AAL3) `[Verificado MS Learn]`.
- **REF-20:** MITRE Corporation — *MITRE ATT&CK Enterprise Matrix v18 (Credential Access, Valid Accounts T1078, Steal Web Session Cookie T1539, Steal Application Access Token T1528)* (`https://attack.mitre.org`). Taxonomía adversaria empleada para mapear reglas KQL y ejercicios *Purple Team* de identidad `[Verificado MS Learn]`.

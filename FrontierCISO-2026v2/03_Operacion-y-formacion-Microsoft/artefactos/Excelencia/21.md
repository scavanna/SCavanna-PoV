# Guía Maestra de Excelencia Operacional: Microsoft Purview Customer Lockbox, Customer Key y Privileged Access Management (M365 PAM)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Definición Oficial |
| :--- | :--- |
| **Identificador del Módulo** | `21_Customer_Lockbox_Customer_Key_y_M365_PAM` |
| **Slug Canónico** | `Customer_Lockbox_Customer_Key_y_M365_PAM` |
| **Nombre Completo** | Microsoft Purview Customer Lockbox, Customer Key y Privileged Access Management (M365 PAM) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` `[Verificado MS Learn]` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (+ costos de consumo en dos suscripciones Azure para Azure Key Vault Premium HSM o Azure Key Vault Managed HSM al desplegar Customer Key) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://admin.microsoft.com` (Customer Lockbox & Privileged Access), `https://purview.microsoft.com` (Audit & Compliance Manager), `https://portal.azure.com` (Key Vault / Managed HSM / Azure Lockbox), `https://intune.microsoft.com` (Windows 365 Cloud PC Encryption) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Cloud Security Architect, Cryptography & PKI Lead, Identity & Privileged Access Lead, Exchange & SharePoint Platform Leads, Compliance Officer / DPO, SOC L2/L3, Internal Audit / GRC |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Microsoft Cloud Security Benchmark v2 (`PA-8`, `DP-4`, `PA-1`), MITRE ATT&CK Enterprise v18, FIPS 140-2 Level 3 / FIPS 140-3, ISO/IEC 27001:2022, HIPAA, FedRAMP, GDPR (Schrems II / Soberanía), DORA, SEC / FINRA |

> **Nota de Consolidación Arquitectónica (Noviembre 2026):** Este documento consolida en un estándar único de ingeniería y gobierno los **tres pilares de soberanía operativa, control criptográfico de servicio y privilegio administrativo cero permanente (*Zero Standing Privileges* — ZSP)** de **Microsoft Purview Suite** (anteriormente *Microsoft 365 E5 Compliance*, renombrado el 1 de octubre de 2025) `[Verificado MS Learn]`: **(1) Microsoft Purview Customer Lockbox**, **(2) Microsoft Purview Customer Key** (incluyendo soporte consolidado para **Windows 365 Cloud PCs**, interacciones de **Microsoft 365 Copilot**, **Azure Key Vault Managed HSM** y *Customer Key Onboarding Service*) y **(3) Microsoft Purview Privileged Access Management (M365 PAM)** `[Verificado MS Learn]`. Asimismo, incorpora la transición obligatoria de auditoría desde `Search-UnifiedAuditLog` (cuyo retiro definitivo fue anunciado en octubre de 2026 mediante MC1505599 para el **15 de octubre de 2027**) hacia **Microsoft Graph `auditLog/queries`** e ingesta nativa en Microsoft Sentinel `[Verificado MS Learn]`. Toda afirmación documental oficial lleva la etiqueta `[Verificado MS Learn]` y todo criterio consultivo, SLA interno, meta de KPI o diseño de control lleva la etiqueta `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 La Tríada de Soberanía y Confianza Cero sobre el Plano de Servicio y Datos

Incluso cuando una organización endurece sus identidades con Microsoft Entra ID y etiqueta sus documentos con Microsoft Purview Information Protection, subsisten tres vectores críticos de riesgo regulatorio y sistémico en la nube pública `[Decisión / Propuesta Editorial]`:
1. **Acceso excepcional del proveedor cloud durante incidentes de soporte:** ¿Cómo garantizar contractual y técnicamente que ningún ingeniero de Microsoft acceda al contenido del cliente sin autorización explícita caso por caso? -> Resuelto por **Microsoft Purview Customer Lockbox** `[Verificado MS Learn]`.
2. **Custodia criptográfica de claves raíz en reposo y salida regulada del servicio:** ¿Cómo controlar en HSM propios las claves raíz que cifran buzones, sitios, chats, Windows 365 Cloud PCs e interacciones de M365 Copilot sin sacrificar las capacidades nativas de IA, búsqueda, DLP y eDiscovery? -> Resuelto por **Microsoft Purview Customer Key** `[Verificado MS Learn]`.
3. **Abuso o compromiso de administradores internos con roles amplios en el sustrato M365:** ¿Cómo exigir aprobación por pares *Just-in-Time* a nivel de un **cmdlet o tarea específica** de Exchange Online (ej. crear reglas de transporte o conectores de correo) más allá de la activación de un rol completo de directorio en Entra PIM? -> Resuelto por **Microsoft Purview Privileged Access Management (M365 PAM)** `[Verificado MS Learn]`.

### 2.2 Matriz Detallada de Licenciamiento y Costos Asociados (Noviembre 2026)

Cada usuario que se beneficia de estas capacidades requiere licencia elegible conforme a los *Product Terms* y la *Microsoft Purview Service Description* vigente a noviembre de 2026 `[Verificado MS Learn]`:

| Pilar Tecnológico | Licencias M365 / Purview que Incluyen el Derecho | Regla Exacta de Conteo y Validación de Licencias | Costos Adicionales de Infraestructura Azure |
| :--- | :--- | :--- | :--- |
| **Microsoft Purview Customer Lockbox** | Microsoft 365 E5 / A5 / G5, Office 365 E5 / A5 / G5, **Microsoft Purview Suite** (EDU/GOV/FLW), Defender + Purview Suite FLW, M365 E5/A5/F5/G5 Insider Risk Management `[Verificado MS Learn]` | Control habilitado a nivel de tenant; cubre Exchange Online, SharePoint, OneDrive, Teams, Windows 365 e interacciones M365 Copilot `[Verificado MS Learn]` | Ninguno para M365. *(Nota: **Customer Lockbox for Microsoft Azure** es independiente y exige plan de soporte Azure >= **Developer**)* `[Verificado MS Learn]` |
| **Customer Key — Multi-Workload DEP (MDEP)** | Microsoft 365 E5 / A5 / G5, Office 365 E5 / A5 / G5, **Microsoft Purview Suite** (EDU/GOV/FLW), M365 E5/A5/F5/G5 Information Protection & Governance `[Verificado MS Learn]` | El tenant debe poseer al menos tantas licencias elegibles de Customer Key como usuarios tengan licencia de **Exchange o Teams (el mayor de ambos)**. Microsoft valida periódicamente; si faltan licencias, revierte al cifrado administrado por Microsoft `[Verificado MS Learn]` | **Sí:** 2 suscripciones Azure de pago con **Azure Key Vault Premium (HSM)** o **Azure Key Vault Managed HSM** `[Verificado MS Learn]` |
| **Customer Key — Exchange Mailbox DEPs** | Mismas SKUs que Customer Key `[Verificado MS Learn]` | Cada buzón de usuario asignado a una DEP debe tener licencia elegible persistente (buzones compartidos, de grupo y carpetas públicas no exigen licencia separada si los usuarios cumplen) `[Verificado MS Learn]` | Consumo de operaciones criptográficas `wrapKey`/`unwrapKey` y llaves HSM en dos regiones Azure `[Verificado MS Learn]` |
| **Customer Key — SharePoint & OneDrive DEP** | Mismas SKUs que Customer Key `[Verificado MS Learn]` | El total de licencias Customer Key en el tenant debe ser **>= total de usuarios con licencia SharePoint** `[Verificado MS Learn]` | Consumo en Azure Key Vault Premium o Managed HSM `[Verificado MS Learn]` |
| **Microsoft Purview Privileged Access Management (M365 PAM)** | Microsoft 365 E5 / A5 / G5, Office 365 E5 / A5 / G5, **Microsoft Purview Suite**, M365 E5/A5/F5/G5 Insider Risk Management `[Verificado MS Learn]` | Control a nivel de organización (hasta **30 políticas de acceso privilegiado** activas actualmente por organización) `[Verificado MS Learn]` | Ninguno `[Verificado MS Learn]` |

### 2.3 Principios Rectores Oficiales y Alineación Zero Trust

1. **Cero Acceso Permanente del Proveedor y del Administrador (*Zero Standing Privileges*):** Ningún ingeniero de soporte de Microsoft posee acceso continuo al contenido del cliente (Lockbox) ni ningún administrador interno debe mantener capacidad permanente de ejecutar tareas críticas sin aprobación acotada en el tiempo (M365 PAM + Entra PIM) `[Verificado MS Learn]`.
2. **Separación Estricta de Custodia Criptográfica (*Dual-Subscription & Dual-Custodian Root Keys*):** En Customer Key, cada política de cifrado de datos (DEP) exige dos claves raíz alojadas en **dos suscripciones de Azure de pago distintas** y regiones separadas dentro del mismo tenant Entra, administradas por equipos independientes para impedir pérdida o sabotaje unilateral `[Verificado MS Learn]`.
3. **Inmutabilidad Antidestrucción Accidental (*Soft Delete 90d + Purge Protection + No Key Expiry*):** Todo Azure Key Vault o Managed HSM de Customer Key exige *Soft Delete* (90 días) y *Purge Protection* desde su creación, claves RSA sin fecha de expiración y **prohibición absoluta de borrar o deshabilitar versiones históricas de claves** `[Verificado MS Learn]`.
4. **Cifrado de Servicio Compatible con Productividad e IA (Customer Key vs. DKE):** Utilizar Customer Key para cumplir mandatos regulatorios de control de claves raíz preservando **Microsoft 365 Copilot, eDiscovery, DLP, antimalware e indexación**, reservando **Double Key Encryption (DKE)** exclusivamente para el ~5 % de activos ultra-secretos que deban permanecer opacos incluso al servicio `[Verificado MS Learn]`.
5. **Defensa en Profundidad Rol + Tarea (Entra PIM + M365 PAM):** Emplear Microsoft Entra PIM para gobernar la activación JIT de roles de directorio y complementar con M365 PAM para exigir revisión por pares (*peer-review*) sobre cmdlets específicos de alto impacto en el sustrato de Exchange Online `[Verificado MS Learn]`.
6. **Trazabilidad Forense Inmutable de Extremo a Extremo:** Auditar en Purview Audit y SIEM cada decisión Lockbox (`Set-AccessToCustomerDataRequest`), cada comando ejecutado por `Microsoft Operator`, cada *fallback* a la `Availability Key` (`CustomerKeyServiceEncryption`) y cada elevación de tarea en M365 PAM `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Pilar 1: Arquitectura de Microsoft Purview Customer Lockbox (M365 vs. Azure)

Cuando un incidente de soporte no puede resolverse mediante telemetría automatizada y un ingeniero de Microsoft necesita acceder temporalmente al contenido del tenant, el flujo **Customer Lockbox** interpone al cliente como aprobador final obligatorio `[Verificado MS Learn]`:

1. **Secuencia de Flujo Verificada:** Ticket abierto por el cliente -> evaluación del ingeniero de soporte -> solicitud en herramienta interna Lockbox de Microsoft -> aprobación obligatoria de un **Microsoft Support Manager** (distinto del solicitante) -> notificación por correo electrónico a los `Global Administrators` y miembros del rol **`Customer Lockbox access approver`** `[Verificado MS Learn]`.
2. **Control Anti-Phishing por Diseño:** Microsoft **nunca incluye enlaces en los correos de notificación de Customer Lockbox** que pidan iniciar sesión en Microsoft 365; el aprobador debe navegar manualmente a `https://admin.microsoft.com > Support > Customer Lockbox Requests` `[Verificado MS Learn]`.
3. **Ventanas Temporales Duras:**
   - **Expiración de cola:** Si el cliente rechaza o no responde en **12 horas**, la solicitud expira automáticamente y no se concede acceso `[Verificado MS Learn]`.
   - **Duración máxima del acceso:** Una vez aprobada, los permisos preaprobados de cmdlets otorgados al ingeniero duran como máximo **4 horas** (o el tiempo menor solicitado) y se revocan automáticamente `[Verificado MS Learn]`.
4. **Cobertura de Cargas e IA:** Cubre **Exchange Online, SharePoint Online, OneDrive for Business, Microsoft Teams y Windows 365**, además de **todas las interacciones de Microsoft 365 Copilot** a través de la cobertura del sustrato de Exchange Online `[Verificado MS Learn]`. Customer Lockbox **nunca otorga acceso a claves criptográficas** del cliente y no aplica a requerimientos judiciales externos (*subpoenas*) ni a eventos extremos de *break-glass* de disponibilidad global auditados bajo SOC 2 `[Verificado MS Learn]`.

#### 3.1.1 Matriz Comparativa: Customer Lockbox for Microsoft 365 vs. Customer Lockbox for Microsoft Azure

| Dimensión Arquitectónica | Customer Lockbox for Microsoft 365 (Purview) | Customer Lockbox for Microsoft Azure |
| :--- | :--- | :--- |
| **Prerrequisito de Licenciamiento / Plan** | Microsoft 365 E5 / Purview Suite / E5 Insider Risk Management `[Verificado MS Learn]` | Plan de soporte de Azure nivel **Developer** o superior `[Verificado MS Learn]` |
| **Consola de Habilitación y Operación** | `https://admin.microsoft.com > Settings > Org Settings > Security & Privacy > Customer Lockbox` y `Support > Customer Lockbox Requests` `[Verificado MS Learn]` | `https://portal.azure.com` > módulo **Customer Lockbox for Microsoft Azure** (`Administration`) `[Verificado MS Learn]` |
| **Cargas de Trabajo Cubiertas** | Exchange Online, SharePoint, OneDrive, Teams, Windows 365 e interacciones **Microsoft 365 Copilot** `[Verificado MS Learn]` | +40 servicios IaaS/PaaS/IA: Azure VMs, Storage, SQL DB/MI, AKS, Key Vault/AIP, Log Analytics, **Azure OpenAI**, **Foundry Tools**, Entra Diagnostics `[Verificado MS Learn]` |
| **Roles Autorizados para Aprobar** | `Customer Lockbox access approver` o `Global Administrator` `[Verificado MS Learn]` | Recursos de suscripción: `Owner` o `Azure Customer Lockbox Approver for Subscription` (no soporta asignación en Management Group; **roles PIM elegibles deben activarse antes** de que inicie la solicitud). Tenant: `Global Administrator` `[Verificado MS Learn]` |
| **Tiempo de Expiración sin Respuesta** | **12 horas** `[Verificado MS Learn]` | **4 días** `[Verificado MS Learn]` |
| **Trazabilidad de Auditoría** | Purview Audit: actividad `Set-AccessToCustomerDataRequest` (`BOXServiceAccount@...`) y acciones bajo usuario `Microsoft Operator` `[Verificado MS Learn]` | Suscripción: **Azure Activity Logs** (`Create/Approve/Deny Lockbox Request`, `Lockbox Request Expiry`). Tenant: **Microsoft Entra Audit Log** (`Service = Access Reviews`) `[Verificado MS Learn]` |
| **Control de Referencia MCSB** | Controles Purview / SOC 1 SSAE 18 `[Verificado MS Learn]` | **MCSB v2 `PA-8`**: *Determine access process for cloud provider support* `[Verificado MS Learn]` |

---

### 3.2 Pilar 2: Arquitectura de Microsoft Purview Customer Key (Service Encryption BYOK)

**Customer Key** agrega una capa de cifrado de servicio en el nivel de aplicación sobre el cifrado físico base de Microsoft (BitLocker + Distributed Key Manager en centros de datos M365 y Azure Storage Server-Side Encryption SSE en discos de Windows 365 Cloud PCs, donde BitLocker no está soportado) `[Verificado MS Learn]`.

#### 3.2.1 Diseño de Claves Raíz: Azure Key Vault Premium vs. Azure Key Vault Managed HSM

| Característica de Diseño | Opción A: Azure Key Vault (Premium SKU) | Opción B: Azure Key Vault Managed HSM |
| :--- | :--- | :--- |
| **Nivel de Aseguramiento Criptográfico** | HSM multitenant validado; usar **Premium SKU** para producción (Standard SKU solo para pruebas) `[Verificado MS Learn]` | HSM **single-tenant** totalmente gestionado con validación **FIPS 140-2 Level 3** `[Verificado MS Learn]` |
| **Cantidad Total de Instancias para Cubrir las 3 Cargas (MDEP, EXO y SPO)** | **6 Key Vaults en total** (3 pares separados: 2 para Multi-workload, 2 para Exchange y 2 para SharePoint/OneDrive) en 2 suscripciones de pago `[Verificado MS Learn]` | **Solo 2 instancias Managed HSM en total** (1 en cada una de las 2 suscripciones Azure de pago), reutilizables por todas las cargas `[Verificado MS Learn]` |
| **Tipo y Longitud de Clave Soportada** | Claves **RSA** respaldadas por HSM de hasta **4.096 bits** (curvas elípticas EC **no soportadas**; **sin fecha de expiración**) `[Verificado MS Learn]` | Claves **RSA-HSM** únicamente (sin fecha de expiración para el servicio de onboarding) `[Verificado MS Learn]` |
| **Modelo de Control de Acceso y Rol para M365** | **Azure RBAC** (recomendado; migrar fuera de *legacy access policies*): rol `Key Vault Crypto Service Encryption User` (`wrapKey`, `unwrapKey`, `get`) `[Verificado MS Learn]` | **Managed HSM Local RBAC**: rol `Managed HSM Crypto Service Encryption User` (`wrapKey`, `unwrapKey`, `get`) `[Verificado MS Learn]` |
| **Protección Antidestrucción Obligatoria** | `Soft delete` (**90 días**) + `Purge protection` habilitados al crear el baúl + Firewall con *Allow Trusted Microsoft Services* `[Verificado MS Learn]` | `Soft delete` activo de fábrica + **obligatorio activar `Purge protection` al aprovisionar** + *Allow Trusted Microsoft Services* `[Verificado MS Learn]` |

#### 3.2.2 Principales de Servicio Oficiales y los Tres Tipos de Data Encryption Policies (DEPs)

Antes del alta mediante el módulo oficial `M365CustomerKeyOnboarding` (`New-CustomerKeyOnboardingRequest -OnboardingMode Validate|Enable`), deben estar registrados en el tenant los principales de servicio oficiales `[Verificado MS Learn]`:
- **Customer Key Onboarding App:** `19f7f505-34aa-44a4-9dcc-6a768854d2ea` `[Verificado MS Learn]`
- **M365DataAtRestEncryption (Multi-workload):** `c066d759-24ae-40e7-a56f-027002b5d3e4` `[Verificado MS Learn]`
- **Office 365 Exchange Online:** `00000002-0000-0ff1-ce00-000000000000` `[Verificado MS Learn]`
- **Office 365 SharePoint Online:** `00000003-0000-0ff1-ce00-000000000000` `[Verificado MS Learn]`

| Tipo de Política DEP | Cmdlets Oficiales de Creación / Asignación | Alcance Exacto de Datos Cifrados y Reglas Operativas |
| :--- | :--- | :--- |
| **1. Multi-Workload DEP (`Scenario: MDEP`)** | `New-M365DataAtRestEncryptionPolicy` y `Set-M365DataAtRestEncryptionPolicyAssignment` `[Verificado MS Learn]` | Solo **1 DEP asignada a la vez por tenant**. Cifra: **(a) Windows 365 Cloud PCs** (Enterprise y Frontline Dedicated/Shared: discos, snapshots e imágenes; requiere activar en `intune.microsoft.com > Tenant administration > Cloud PC encryption type` tras 3-4 h, re-cifrando y reiniciando hasta 20.000 Cloud PCs por lote); **(b) Microsoft Teams** (chats, media, grabaciones en storage Teams, notificaciones); **(c) Interacciones de Microsoft 365 Copilot**; **(d) Purview Information Protection** (esquemas/reglas/salts EDM y configuración de etiquetas); **(e) Exchange** (señales y buzones sin DEP individual); y **(f) Exportaciones directas de Purview eDiscovery** (CMK preview) `[Verificado MS Learn]`. |
| **2. Exchange Mailbox DEPs (`Scenario: EXO`)** | `New-DataEncryptionPolicy` y `Set-Mailbox -DataEncryptionPolicy` / `Set-MailUser` `[Verificado MS Learn]` | Hasta **50 DEPs activas por tenant** (1 DEP por buzón). Cifra `UserMailbox`, `MailUser` (híbrido/pre-migración), `Group`, `PublicFolder` y `Shared` mailboxes `[Verificado MS Learn]`. **Único tipo de DEP que soporta el flujo regulado de *Data Purge Path*** al salir del servicio `[Verificado MS Learn]`. |
| **3. SharePoint & OneDrive DEP** | `Register-SPODataEncryptionPolicy` y `Update-SPODataEncryptionPolicy` (SharePoint PowerShell) `[Verificado MS Learn]` | **1 DEP por ubicación geográfica (Geo)** en tenants single-geo o multi-geo `[Verificado MS Learn]`. Jerarquía de claves: `Customer Keys -> Tenant Intermediate Key (TIK) -> Site Keys -> Blob Keys -> File chunks` en Azure Blob Storage (cubre archivos SharePoint, OneDrive y archivos de Teams guardados en SPO; no cubre metadatos/listas en SQL, gobernados por Lockbox) `[Verificado MS Learn]`. |

#### 3.2.3 Arquitectura de la Availability Key y Peligro Catastrófico de Purge

1. **Funcionamiento de la Availability Key:** Al crear una DEP, Microsoft 365 genera automáticamente una tercera clave raíz (**Availability Key**: AES-256 para Exchange/MDEP y RSA-2048 para SharePoint/OneDrive), protegida en almacenes internos aislados a los que ni el cliente ni los ingenieros de Microsoft tienen acceso interactivo directo `[Verificado MS Learn]`.
   - En **Exchange y Multi-workload**, si fallan ambas claves del cliente por **errores sistémicos transitorios** (timeout o caída regional de Key Vault), el servicio recurre automáticamente a la Availability Key y registra en Purview Audit un evento `RecordType: CustomerKeyServiceEncryption`, `Activity: Fallback to availability key` `[Verificado MS Learn]`. En cambio, ante errores de **Acceso Denegado** (permisos removidos o clave borrada), **las solicitudes de usuario fallan sin fallback** (aunque procesos internos como indexación o eDiscovery pueden usarla hasta que sea destruida) `[Verificado MS Learn]`.
   - En **SharePoint y OneDrive**, la Availability Key **no se usa para disponibilidad transitoria**; solo se activa mediante solicitud explícita de recuperación ante Microsoft Support `[Verificado MS Learn]`.
2. **Riesgo Catastrófico de Destrucción Criptográfica (*Data Shredding* vs. Rollback):**
   - **Prohibición absoluta en rotación:** Nunca se deben eliminar ni deshabilitar versiones anteriores de claves asociadas a Exchange, Multi-workload o SharePoint (los respaldos de restauración de SharePoint dependen de versiones históricas de claves). Al reemplazar claves con `-Replace`, debe esperarse **mínimo 24 horas antes de deshabilitar** la clave antigua y **24 a 48 horas adicionales** antes de cualquier acción ulterior `[Verificado MS Learn]`.
   - **Data Purge Path regulado:** Revocar permisos `wrapKey`/`unwrapKey`, ejecutar `Set-DataEncryptionPolicy <ID> -PermanentDataPurgeRequested` y firmar legalmente el *Data Purge eDocument* destruye la DEP, marca los buzones para borrado permanente y elimina la Availability Key, dejando los datos **criptográficamente irrecuperables para siempre** `[Verificado MS Learn]`. Este flujo **solo existe para DEPs de buzones Exchange al abandonar completamente el servicio** (no está soportado en Multi-workload DEPs ni en SharePoint/OneDrive DEPs; si solo se desea volver a claves administradas por Microsoft sin borrar datos, debe seguirse el flujo de *Rollback* conservando intactos los Key Vaults durante el re-cifrado) `[Verificado MS Learn]`.

#### 3.2.4 Comparativa Arquitectónica Exacta: Customer Key vs. Double Key Encryption (DKE — Módulo 14)

| Criterio Técnico y Operativo | Microsoft Purview Customer Key (BYOK de Servicio) | Microsoft Purview Double Key Encryption (DKE — BYOK/HYOK de Ítem) |
| :--- | :--- | :--- |
| **Capa de Aplicación del Cifrado** | Cifrado en reposo a nivel de carga/contenedor mediante **Data Encryption Policies (DEPs)** `[Verificado MS Learn]` | Cifrado a nivel de archivo/correo individual mediante **Sensitivity Labels** (MIP) `[Verificado MS Learn]` |
| **Custodia y Visibilidad de Claves** | 2 claves raíz del cliente en Azure Key Vault / Managed HSM + 1 Availability Key gestionada por el código de servicio de M365 `[Verificado MS Learn]` | 1 clave en Azure RMS + **1 clave bajo custodia exclusiva del cliente** en el servicio web DKE (on-premises o nube propia); Microsoft nunca ve la segunda clave `[Verificado MS Learn]` |
| **Volumen Objetivo de Datos** | **100 % de los datos en reposo** de las cargas licenciadas en el tenant `[Verificado MS Learn]` | Solo el **~5 % de datos ultra-sensibles** ("joyas de la corona" / *Top Secret*) `[Verificado MS Learn]` |
| **Compatibilidad con Microsoft 365 Copilot** | **Totalmente compatible** (e incluso cifra las interacciones de M365 Copilot en reposo vía MDEP) `[Verificado MS Learn]` | **Incompatible:** Copilot no puede acceder ni razonar sobre contenido cifrado con DKE ni en reposo ni en uso `[Verificado MS Learn]` |
| **Compatibilidad con eDiscovery, DLP e Indexación** | **Totalmente compatible** (el cliente autoriza al servicio a usar las claves para búsqueda, DLP, eDiscovery y antimalware) `[Verificado MS Learn]` | **Incompatible:** SharePoint/OneDrive no indexan archivos DKE; no operan eDiscovery, Content Search, DLP en nube ni reglas de transporte sobre adjuntos DKE `[Verificado MS Learn]` |
| **Experiencia Colaborativa (Web, Coautoría, Loop, Teams)** | Transparente al usuario final en todas las apps web, móviles y de escritorio `[Verificado MS Learn]` | Solo apps Office de escritorio en Windows; **deshabilita Office Web Apps, Coautoría, AutoSave, Loop y cifrado de reuniones/chats Teams** `[Verificado MS Learn]` |

#### 3.2.5 Reglas Oficiales de Validación del Servicio `M365CustomerKeyOnboarding`

Al ejecutar `New-CustomerKeyOnboardingRequest -OnboardingMode Validate`, el servicio audita nueve invariantes técnicas cuyo cumplimiento continuo previene incidentes severos `[Verificado MS Learn]`:

| Regla de Validación Oficial (`RuleName`) | Condición Técnica Auditada por Microsoft 365 | Acción de Remediación en Caso de Fallo |
| :--- | :--- | :--- |
| `OrganizationHasRequiredServicePlan` | El tenant posee planes de servicio elegibles para Customer Key en Exchange `[Verificado MS Learn]` | Asignar licencias Microsoft 365 E5 / Purview Suite / E5 IP&G `[Verificado MS Learn]` |
| `EligibleLicenseCount` | El volumen de licencias elegibles cubre el máximo entre usuarios Exchange y Teams para MDEP `[Verificado MS Learn]` | Incrementar licencias Customer Key asignadas en el tenant `[Verificado MS Learn]` |
| `KeyNeverExpires` | Las claves RSA/RSA-HSM carecen de fecha de expiración (`Expires == null`) `[Verificado MS Learn]` | Crear claves sin fecha de expiración (o fijar `12/31/9999` solo en método legado) `[Verificado MS Learn]` |
| `KeyOperationsSupported` | Las claves soportan las operaciones `wrapKey`, `unwrapKey` y `get` para el Service Principal M365 `[Verificado MS Learn]` | Asignar rol `Key Vault / Managed HSM Crypto Service Encryption User` `[Verificado MS Learn]` |
| `RecoveryLevel` | El nivel de recuperación reporta `Recoverable` (con protección contra purga) `[Verificado MS Learn]` | Verificar `Soft Delete` (90 días) + `Purge Protection` habilitados `[Verificado MS Learn]` |
| `SubscriptionInRequestOrganization` | Ambas suscripciones Azure pertenecen al mismo tenant de Microsoft Entra `[Verificado MS Learn]` | Asociar las suscripciones al directorio corporativo correcto `[Verificado MS Learn]` |
| `SubscriptionsCountPerScenario` | La solicitud incluye exactamente dos suscripciones para el escenario evaluado `[Verificado MS Learn]` | Proveer `Subscription1` y `Subscription2` válidas `[Verificado MS Learn]` |
| `SubscriptionUniquePerScenario` | Los GUID de ambas suscripciones son estrictamente diferentes entre sí `[Verificado MS Learn]` | Aprovisionar una segunda suscripción de pago independiente `[Verificado MS Learn]` |
| `VaultExistsinSubscription` | Cada Key Vault o instancia Managed HSM existe efectivamente en la suscripción declarada `[Verificado MS Learn]` | Corregir el cruce entre URI de clave e ID de suscripción `[Verificado MS Learn]` |

---

### 3.3 Pilar 3: Arquitectura de Microsoft Purview Privileged Access Management (M365 PAM) y Sinergia con Entra PIM

**Microsoft Purview Privileged Access Management (M365 PAM)** opera directamente sobre el **sustrato de Microsoft 365** y el *Exchange Management runspace* para eliminar privilegios administrativos permanentes a nivel de **tarea (`Task` / cmdlet)** `[Verificado MS Learn]`:

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ CAPA 1: MICROSOFT ENTRA PRIVILEGED IDENTITY MANAGEMENT (Entra PIM) — Nivel de Identidad / Rol     │
│   - Gobierna activación JIT de roles completos de directorio (ej. Exchange Admin, Security Admin) │
│   - Otorga acceso amplio a múltiples tareas durante la ventana activa                             │
└───────────────────────────────────────────────┬───────────────────────────────────────────────────┘
                                                │ (Defensa en Profundidad Complementaria)
                                                ▼
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ CAPA 2: MICROSOFT PURVIEW PRIVILEGED ACCESS MANAGEMENT (M365 PAM) — Nivel de Tarea / Cmdlet       │
│   - Intercepta en el Exchange Management Runspace y Sustrato M365 la ejecución de cmdlets críticos│
│   - Políticas (máx. 30 por org): Task (ej. Exchange\New-TransportRule), Role o Role Group         │
│   - Solicitud (New-ElevatedAccessRequest, expira en 24h) -> Aprobación Manual/Auto por grupo      │
│   - Ventana JIT acotada (4 horas por defecto) + Auditoría completa de cada ejecución              │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### 3.3.1 Comparativa Exacta: Microsoft Purview PAM vs. Microsoft Entra PIM

| Dimensión de Control | Microsoft Purview Privileged Access Management (M365 PAM) | Microsoft Entra Privileged Identity Management (Entra PIM) |
| :--- | :--- | :--- |
| **Granularidad Primaria del Control** | **Nivel de Tarea (`Task` / cmdlet individual)** dentro de Exchange Online / sustrato M365 (también soporta *Role* y *Role Group* del sustrato) `[Verificado MS Learn]` | **Nivel de Rol de Directorio, Grupo de Seguridad o Recurso Azure RBAC** (habilita todas las acciones contenidas en el rol) `[Verificado MS Learn]` |
| **Plano Técnico de Intercepción** | Sustrato de Microsoft 365 y *Exchange Management Runspace* `[Verificado MS Learn]` | Plano de identidad Microsoft Entra ID y Azure Resource Manager `[Verificado MS Learn]` |
| **Ejemplo de Caso de Uso Crítico** | Permitir administración rutinaria pero exigir aprobación por pares para ejecutar `Exchange\New-InboundConnector`, `Exchange\New-TransportRule`, `Exchange\New-MoveRequest` o `Exchange\Add-MailboxPermission` `[Verificado MS Learn]` | Elevar temporalmente a un ingeniero al rol `Exchange Administrator` o `Compliance Administrator` durante un turno de cambio `[Verificado MS Learn]` |
| **Límites y Ventanas Temporales** | Hasta **30 políticas** por organización; solicitud pendiente expira en **24 horas**; aprobación válida por la duración solicitada (**4 horas por defecto**) `[Verificado MS Learn]` | Políticas por rol/grupo configurables (ej. 1 a 8 horas) con MFA, Authentication Context y Access Reviews `[Verificado MS Learn]` |
| **Exclusiones para Automatización** | Parámetro explícito `-SystemAccounts` en `Enable-ElevatedAccessControl` para excluir cuentas de servicio estrictamente auditadas `[Verificado MS Learn]` | Asignaciones permanentes (*Active*) excepcionales o identidades gestionadas de carga de trabajo `[Verificado MS Learn]` |

#### 3.3.2 Catálogo Recomendado de Tareas (`Task`) Prioritarias para las 30 Políticas de M365 PAM `[Decisión / Propuesta Editorial]`

Dado que Microsoft Purview PAM admite actualmente hasta **30 políticas por organización** enfocadas en el ámbito `Exchange`, se recomienda asignar aprobación **Manual** obligatoria sobre las siguientes familias de tareas de alto impacto `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:

| Categoría de Riesgo | Tareas / Cmdlets en `New-ElevatedAccessApprovalPolicy` | Riesgo Mitigado (MITRE ATT&CK) |
| :--- | :--- | :--- |
| **Exfiltración por Flujo de Correo y Conectores** | `Exchange\New-TransportRule`, `Exchange\Set-TransportRule`, `Exchange\New-InboundConnector`, `Exchange\Set-InboundConnector`, `Exchange\New-OutboundConnector`, `Exchange\Set-OutboundConnector` | Evita desvío silencioso de correos corporativos hacia servidores externos (`T1114.003`) |
| **Acceso Delegado y Lectura de Buzones VIP** | `Exchange\Add-MailboxPermission`, `Exchange\Add-RecipientPermission`, `Exchange\Set-Mailbox` (reenvío SMTP), `Exchange\Search-Mailbox`, `Exchange\New-MoveRequest` | Impide lectura encubierta o movimiento no autorizado de buzones ejecutivos (`T1098.002`) |
| **Escalamiento RBAC Interno en Exchange** | `Exchange\New-ManagementRoleAssignment`, `Exchange\Add-RoleGroupMember`, `Exchange\New-RoleGroup` | Bloquea creación de puertas traseras administrativas en el sustrato Exchange (`T1098`) |
| **Soberanía Criptográfica y Journalización** | `Exchange\New-DataEncryptionPolicy`, `Exchange\Set-DataEncryptionPolicy`, `Exchange\New-M365DataAtRestEncryptionPolicy`, `Exchange\Set-M365DataAtRestEncryptionPolicyAssignment`, `Exchange\New-JournalRule`, `Exchange\Set-JournalRule` | Impide alteración unilateral de políticas Customer Key, purgas criptográficas o copia oculta de journaling (`T1485`) |

### 3.4 Integraciones Cruzadas del Ecosistema

- **Microsoft Intune & Windows 365:** Integración directa de la Multi-workload DEP de Customer Key con `intune.microsoft.com > Tenant administration > Cloud PC encryption type` para cifrar discos, instantáneas e imágenes de Cloud PCs `[Verificado MS Learn]`.
- **Microsoft Purview eDiscovery:** Extensión de Customer Key (MDEP) para cifrar con claves del cliente (**CMK preview**) los paquetes de exportación directa de investigaciones legales `[Verificado MS Learn]`.
- **Microsoft Defender for Cloud Apps & Microsoft Sentinel:** Como Customer Lockbox no posee alertas nativas personalizables más allá del correo de solicitud, Microsoft recomienda configurar políticas de alerta en **Defender for Cloud Apps** y reglas KQL en **Microsoft Sentinel** sobre `Set-AccessToCustomerDataRequest`, `Microsoft Operator`, `CustomerKeyServiceEncryption` y cmdlets `*-ElevatedAccess*` `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Reglas Innegociables de Segregación de Funciones (SoD) Criptográfica y Privilegiada

1. **Separación de Custodios entre Suscripción Azure 1 y Suscripción Azure 2 (Customer Key):** Microsoft recomienda explícitamente asignar administradores distintos a cada una de las dos suscripciones y grupos de recursos de Customer Key, usando roles **Key Vault Administrator** (que por diseño en el plano de datos RBAC de Customer Key gestiona claves sin borrarlas accidentalmente) separados de **Key Vault Contributor** `[Verificado MS Learn]`.
2. **Aprobadores Lockbox sin Rol `Global Administrator` Permanente:** Delegar la aprobación cotidiana de solicitudes de soporte de Microsoft en el rol específico **`Customer Lockbox access approver`** para mantener el número de `Global Administrators` en el mínimo absoluto `[Verificado MS Learn]`.
3. **Aprobadores M365 PAM independientes del Solicitante:** Los miembros del *mail-enabled security group* aprobador de M365 PAM pueden revisar y aprobar solicitudes vía PowerShell sin necesitar `Global Administrator` ni `Role Management` (para aprobar desde la interfaz web de `admin.microsoft.com` se requiere el rol `Exchange Administrator`) `[Verificado MS Learn]`.

### 4.2 Matriz Oficial de Roles RBAC y Estrategia PIM / JIT

| Rol Oficial | Plano de Control | Permisos Clave Otorgados | Estrategia PIM / JIT Recomendada | Segregación de Funciones (SoD) |
| :--- | :--- | :--- | :--- | :--- |
| **Customer Lockbox Access Approver** | Microsoft 365 Admin Center / Entra ID `[Verificado MS Learn]` | Habilitar/deshabilitar Customer Lockbox y aprobar, denegar o cancelar solicitudes (`Set-AccessToCustomerDataRequest`) `[Verificado MS Learn]` | Asignado a comité ejecutivo CISO/DPO/Legal (elegible en PIM con activación <= 1 h ante recepción de correo de notificación) `[Decisión / Propuesta Editorial]` | Separado de los administradores operativos que abrieron el ticket de soporte con Microsoft `[Decisión / Propuesta Editorial]` |
| **Azure Customer Lockbox Approver for Subscription** | Azure RBAC (Suscripción) `[Verificado MS Learn]` | Aprobar o rechazar solicitudes de **Customer Lockbox for Microsoft Azure** acotadas a recursos de esa suscripción `[Verificado MS Learn]` | Asignación activa sobre grupo dedicado de seguridad CISO/Cloud Governance *(nota: en Azure Lockbox el rol debe estar activo antes de iniciarse la solicitud)* `[Verificado MS Learn]` | Sin permisos de escritura sobre Key Vaults productivos ni cargas de datos `[Decisión / Propuesta Editorial]` |
| **Key Vault / Managed HSM Crypto Custodian (Sub 1 & Sub 2)** | Azure RBAC / Managed HSM Local RBAC `[Verificado MS Learn]` | `Key Vault Administrator` / `Managed HSM Administrator` (`create`, `backup`, `restore`, `get`, `list`) sobre **una sola** de las dos suscripciones de Customer Key `[Verificado MS Learn]` | Elegible en Azure PIM (máximo 2 h, aprobación dual y MFA FIDO2) `[Decisión / Propuesta Editorial]` | **Regla de Dos Personas:** el Custodio de la Suscripción 1 tiene prohibido tener permisos en la Suscripción 2 y viceversa `[Verificado MS Learn]` |
| **Key Vault RBAC Security Officer** | Azure RBAC (`Key Vault Contributor` / `Role Based Access Control Administrator`) `[Verificado MS Learn]` | Asignar `Key Vault Crypto Service Encryption User` a los Service Principals oficiales de M365 (`M365DataAtRestEncryption`, `EXO`, `SPO`) `[Verificado MS Learn]` | Elegible en Azure PIM (máximo 1 h bajo cambio aprobado) `[Decisión / Propuesta Editorial]` | Sin permisos de plano de datos para crear, respaldar o restaurar material criptográfico `[Verificado MS Learn]` |
| **Customer Key Policy Administrator (EXO / MDEP / SPO)** | Exchange Online PowerShell / SharePoint PowerShell / Intune `[Verificado MS Learn]` | `Compliance Administrator` / `Exchange Administrator` / `SharePoint Administrator` para crear, asignar y refrescar DEPs (`*-M365DataAtRestEncryptionPolicy`, `*-DataEncryptionPolicy`, `*-SPODataEncryptionPolicy`) `[Verificado MS Learn]` | Elegible en Entra PIM + protegido adicionalmente con políticas de aprobación en **M365 PAM** `[Decisión / Propuesta Editorial]` | No posee acceso a las suscripciones Azure donde residen los Key Vaults / Managed HSM `[Verificado MS Learn]` |
| **M365 PAM Policy Administrator** | Microsoft 365 Admin Center / Exchange PowerShell `[Verificado MS Learn]` | `Global Administrator` requerido para habilitar `Enable-ElevatedAccessControl` y crear/borrar políticas `New/Remove-ElevatedAccessApprovalPolicy` `[Verificado MS Learn]` | Estricto JIT en Entra PIM (máximo 1 h con aprobación cruzada del CISO) `[Decisión / Propuesta Editorial]` | No debe pertenecer al grupo aprobador cotidiano de tareas operativas de Exchange `[Decisión / Propuesta Editorial]` |
| **M365 PAM Approver Group Member** | Mail-Enabled Security Group en Exchange / M365 `[Verificado MS Learn]` | Ejecutar `Approve-ElevatedAccessRequest` y `Deny-ElevatedAccessRequest` en PowerShell (o en `admin.microsoft.com` si posee `Exchange Administrator`) `[Verificado MS Learn]` | Membresía nominal auditada de líderes SecOps / Arquitectura; prohibida la autoaprobación `[Decisión / Propuesta Editorial]` | Separado de los ingenieros de mensajería que solicitan elevación con `New-ElevatedAccessRequest` `[Verificado MS Learn]` |
| **Purview Audit Reader / SecOps Analyst** | Microsoft Purview Portal / Microsoft Sentinel `[Verificado MS Learn]` | `View-Only Audit Logs` / `Audit Reader` y consulta en Sentinel sobre `OfficeActivity` y `AzureDiagnostics` de Key Vault `[Verificado MS Learn]` | Activo en lectura para monitoreo continuo 24x7 del SOC `[Decisión / Propuesta Editorial]` | Cero permisos de modificación sobre Lockbox, DEPs, Key Vaults o políticas PAM `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Revisión, Validación Cruzada y Decisión sobre Solicitudes de Customer Lockbox (M365 y Azure)
- **Objetivo:** Evaluar dentro de la ventana de **12 horas** (M365) o **4 días** (Azure) cualquier solicitud de acceso de soporte de Microsoft garantizando validación explícita del ticket antes de aprobar `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Support > Customer Lockbox Requests` y `https://portal.azure.com > Customer Lockbox for Microsoft Azure > Pending Requests` `[Verificado MS Learn]`.
- **Rol Responsable:** Customer Lockbox Access Approver / CISO Duty Officer.
- **Procedimiento Paso a Paso:**
  1. Ante una alerta de correo Lockbox, **nunca hacer clic en enlaces externos sospechosos** (recordando que Microsoft jamás incluye enlaces de inicio de sesión en correos de M365 Lockbox) e ingresar directamente al portal oficial `[Verificado MS Learn]`.
  2. Verificar el **Service Request Number**, el servicio afectado, la duración solicitada (máximo 4 h en M365) y confirmar con el ingeniero interno dueño del ticket que el problema sigue abierto y requiere inspección de contenido `[Verificado MS Learn]`.
  3. Aprobar o rechazar en consola (o vía `Set-AccessToCustomerDataRequest`), documentando el motivo en la bitácora del SOC `[Verificado MS Learn]`.
- **Evidencia Auditable:** Evento `Set-AccessToCustomerDataRequest` en Purview Audit o `Approve/Deny Lockbox Request` en Azure Activity Log `[Verificado MS Learn]`.

### D-02: Auditoría Forense Post-Aprobación de Acciones Ejecutadas por `Microsoft Operator`
- **Objetivo:** Auditar el 100 % de los comandos y accesos realizados por el ingeniero de Microsoft durante las 4 horas posteriores a cualquier solicitud Customer Lockbox aprobada `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Search` y Microsoft Sentinel (`OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Compliance Officer.
- **Procedimiento Paso a Paso:**
  1. Filtrar registros de auditoría donde `User` / `UserIds` sea exactamente **`Microsoft Operator`** dentro de la ventana de 4 horas posterior a la aprobación `[Verificado MS Learn]`.
  2. Verificar dirección IP de origen, operaciones ejecutadas y correspondencia estricta con el alcance del ticket de soporte `[Verificado MS Learn]`.
  3. Adjuntar el extracto CSV/JSON de las acciones de `Microsoft Operator` al cierre del incidente interno `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte exportado de Purview Audit filtrado por `Microsoft Operator` y `Set-AccessToCustomerDataRequest` `[Verificado MS Learn]`.

### D-03: Gestión y Aprobación Peer-Review de Solicitudes JIT en Microsoft Purview PAM
- **Objetivo:** Procesar las solicitudes de elevación de tareas críticas de Exchange Online antes de su expiración automática de **24 horas**, aplicando principio de cuatro ojos y duración mínima `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Settings > Org Settings > Security & Privacy > Privileged access > Manage access policies and requests` o Exchange Online PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** M365 PAM Approver Group Member.
- **Procedimiento Paso a Paso:**
  1. Revisar solicitudes en estado `Pending` con `Get-ElevatedAccessRequest` verificando el cmdlet exacto solicitado (ej. `Exchange\New-TransportRule`, `Exchange\New-InboundConnector`), la razón (`-Reason`) y el ticket ITSM asociado `[Verificado MS Learn]`.
  2. Validar que la ventana solicitada (`-DurationHours`) sea proporcional al cambio (recomendado 1 a 2 horas, máximo estándar 4 horas) y que el aprobador no sea el mismo ingeniero solicitante `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Ejecutar `Approve-ElevatedAccessRequest -RequestId <GUID> -Comment '<Ticket y justificación>'` o `Deny-ElevatedAccessRequest` (y revocar anticipadamente con **Revoke** en consola si el mantenimiento concluye antes) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de solicitud, aprobación y ejecución del cmdlet en el *Exchange Management runspace* dentro de Purview Audit `[Verificado MS Learn]`.

### D-04: Monitoreo Diario de Eventos de Fallback a la Availability Key (`CustomerKeyServiceEncryption`)
- **Objetivo:** Detectar de inmediato cualquier degradación, fallo de red o error de permisos en Azure Key Vault / Managed HSM que dispare el uso de emergencia de la Availability Key `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` (`RecordType: CustomerKeyServiceEncryption`) y Microsoft Sentinel `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Cryptography & PKI Lead.
- **Procedimiento Paso a Paso:**
  1. Consultar eventos con `RecordType == "CustomerKeyServiceEncryption"` y `Activity == "Fallback to availability key"` en las cargas `Exchange` y `M365DataAtRestEncryption` `[Verificado MS Learn]`.
  2. Si existe algún evento, inspeccionar `DEP ID`, `Policy ID` y los logs diagnósticos (`AuditEvent`) de ambos Azure Key Vaults / Managed HSM para distinguir entre fallo transitorio de plataforma y denegación de permisos (`AccessDenied`) `[Verificado MS Learn]`.
  3. Escalar a prioridad P1 si se detecta cualquier error `403 Forbidden` o `KeyNotFound` en cualquiera de las dos bóvedas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Consulta diaria limpia sobre `CustomerKeyServiceEncryption` y `AzureDiagnostics` de Key Vault `[Verificado MS Learn]`.

### D-05: Vigilancia en Tiempo Real de Operaciones en el Plano de Control y Datos de Key Vaults / Managed HSM
- **Objetivo:** Detectar intentos no autorizados de cambio de permisos RBAC, modificación de firewall, deshabilitación de claves o eliminación sobre las bóvedas de Customer Key `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` / Microsoft Sentinel (`AzureActivity` + `AzureDiagnostics`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2.
- **Procedimiento Paso a Paso:**
  1. Revisar alertas analíticas sobre operaciones `KeyDelete`, `KeyUpdate`, `VaultDelete`, `VaultPatch` o cambios de `roleAssignments` en las dos suscripciones dedicadas a Customer Key `[Decisión / Propuesta Editorial]`.
  2. Verificar que únicamente los principales `c066d759-24ae-40e7-a56f-027002b5d3e4`, `00000002-0000-0ff1-ce00-000000000000` y `00000003-0000-0ff1-ce00-000000000000` ejecuten `KeyWrap` y `KeyUnwrap` `[Verificado MS Learn]`.
  3. Bloquear y escalar cualquier acceso interactivo fuera de ventana de cambio aprobada `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Panel de salud SIEM de operaciones criptográficas `KeyWrap`/`KeyUnwrap` `[Decisión / Propuesta Editorial]`.

### D-06: Auditoría de Uso de Cuentas Excluidas (`-SystemAccounts`) en M365 PAM
- **Objetivo:** Vigilar que las cuentas de automatización excluidas en `Enable-ElevatedAccessControl -SystemAccounts` no sean utilizadas interactivamente ni ejecuten tareas fuera de su script autorizado `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Microsoft Sentinel (`OfficeActivity` + `SigninLogs`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Identity Lead.
- **Procedimiento Paso a Paso:**
  1. Correlacionar todas las ejecuciones de cmdlets Exchange realizadas por las cuentas listadas en `-SystemAccounts` contra sus IPs de origen y horarios programados `[Decisión / Propuesta Editorial]`.
  2. Confirmar ausencia total de inicios de sesión interactivos humanos sobre dichas cuentas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Alerta SIEM sin violaciones sobre el grupo vigilado de `SystemAccounts` `[Decisión / Propuesta Editorial]`.

### D-07: Verificación de Estado de Cifrado en Nuevos Aprovisionamientos de Windows 365 Cloud PCs
- **Objetivo:** Confirmar que los nuevos Cloud PCs Enterprise y Frontline aprovisionados operen bajo la política activa de Customer Key sin errores en Intune `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com > Tenant administration > Cloud PC encryption type` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint / Windows 365 Admin.
- **Procedimiento Paso a Paso:**
  1. Revisar el estado de cifrado en `Cloud PC encryption type` confirmando que se mantenga seleccionado **Microsoft Purview Customer Key** sin notificaciones de fallo `[Verificado MS Learn]`.
  2. Verificar en `Get-M365DataAtRestEncryptionPolicyAssignment` que la Multi-workload DEP continúe activa a nivel de tenant `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado saludable en Intune Admin Center (`Cloud PC encryption type`) `[Verificado MS Learn]`.

### D-08: Correlación Diaria de Tickets de Soporte Abiertos vs. Cola de Solicitudes Lockbox en Azure y M365
- **Objetivo:** Asegurar que ninguna solicitud legítima de soporte P1 expire por inacción (12 h en M365 / 4 días en Azure) y detectar cualquier solicitud huérfana sin ticket interno `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Support` y `https://portal.azure.com > Help + support / Customer Lockbox` `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud Governance / Service Desk Lead.
- **Procedimiento Paso a Paso:**
  1. Cruzar diariamente los casos severos abiertos con Microsoft Support contra las bandejas de solicitudes pendientes de Customer Lockbox en M365 y Azure `[Verificado MS Learn]`.
  2. Confirmar que los aprobadores elegibles para **Customer Lockbox for Microsoft Azure** hayan activado previamente su rol en PIM cuando se prevea escalamiento a ingeniería de plataforma (dado que Azure Lockbox no reconoce activaciones posteriores al inicio de la solicitud) `[Verificado MS Learn]`.
  3. Verificar que las notificaciones alternas de correo de Azure Lockbox estén operativas para suscripciones críticas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de conciliación ITSM vs. Customer Lockbox M365/Azure `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Validación de Estado de Políticas DEP en Multi-Workload, Exchange y SharePoint/OneDrive
- **Objetivo:** Comprobar que todas las políticas de cifrado (MDEP, buzones Exchange y Geo SharePoint) permanezcan en estado `Enabled` / `Registered` y que los buzones nuevos reciban su DEP `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell y SharePoint Online Management Shell `[Verificado MS Learn]`.
- **Rol Responsable:** Customer Key Policy Administrator.
- **Procedimiento Paso a Paso:**
  1. Ejecutar `Get-M365DataAtRestEncryptionPolicy` y `Get-M365DataAtRestEncryptionPolicyAssignment` para validar la política multi-carga `[Verificado MS Learn]`.
  2. Ejecutar `Get-DataEncryptionPolicy` y auditar una muestra o el total de buzones nuevos/migrados con `Get-Mailbox | fl DataEncryptionPolicy` y `Get-MailboxStatistics <Mailbox> | fl IsEncrypted,DataEncryptionPolicyID`, asignando DEP a buzones pendientes (preferiblemente con `Set-MailUser` antes de migrar buzones híbridos) `[Verificado MS Learn]`.
  3. Ejecutar `Get-SPODataEncryptionPolicy` confirmando estado **`Registered`** al 100 % `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salidas semanales de `Get-M365DataAtRestEncryptionPolicyAssignment`, `Get-DataEncryptionPolicy` y `Get-SPODataEncryptionPolicy` `[Verificado MS Learn]`.

### S-02: Ejecución No Destructiva del Customer Key Onboarding Service en Modo `Validate`
- **Objetivo:** Detectar preventivamente cualquier desviación de configuración en suscripciones, permisos RBAC, expiración de claves o *Purge Protection* sin alterar el entorno productivo `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell (`M365CustomerKeyOnboarding`) `[Verificado MS Learn]`.
- **Rol Responsable:** Cryptography & PKI Lead.
- **Procedimiento Paso a Paso:**
  1. Ejecutar `New-CustomerKeyOnboardingRequest` con `-OnboardingMode Validate` para los escenarios `MDEP` y `EXO` `[Verificado MS Learn]`.
  2. Confirmar que `$request.ValidationResult` devuelva **`Success`** y que `$request.FailedValidations` esté vacío (validando reglas `OrganizationHasRequiredServicePlan`, `EligibleLicenseCount`, `KeyNeverExpires`, `KeyOperationsSupported`, `RecoveryLevel`, `SubscriptionUniquePerScenario`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Objeto JSON/texto de `$request.PassedValidations` con resultado `Success` `[Verificado MS Learn]`.

### S-03: Conciliación de Cobertura de Políticas M365 PAM sobre Cmdlets de Alto Riesgo
- **Objetivo:** Asegurar que las hasta **30 políticas de acceso privilegiado** cubran las tareas más sensibles de exfiltración y persistencia en Exchange Online y que el control global siga activo `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Settings > Org Settings > Security & Privacy > Privileged access` y Exchange Online PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Identity & Privileged Access Lead.
- **Procedimiento Paso a Paso:**
  1. Verificar que **Require approvals for privileged tasks** permanezca habilitado en el centro de administración `[Verificado MS Learn]`.
  2. Auditar con `Get-ElevatedAccessApprovalPolicy` que estén protegidos como mínimo los cmdlets críticos: `Exchange\New-TransportRule`, `Exchange\Set-TransportRule`, `Exchange\New-InboundConnector`, `Exchange\New-OutboundConnector`, `Exchange\Add-MailboxPermission`, `Exchange\New-ManagementRoleAssignment`, `Exchange\Search-Mailbox` y `Exchange\Set-DataEncryptionPolicy` `[Decisión / Propuesta Editorial]`.
  3. Revisar solicitudes expiradas (> 24 h) o denegadas en la semana para identificar cuellos de botella operativos o intentos indebidos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salida exportada de `Get-ElevatedAccessApprovalPolicy` y reporte semanal de `Get-ElevatedAccessRequest` `[Verificado MS Learn]`.

### S-04: Verificación Continua de Habilitación de Customer Lockbox (M365 y Azure)
- **Objetivo:** Confirmar que ningún administrador global haya desactivado accidental o maliciosamente el interruptor de Customer Lockbox en M365 o Azure `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Settings > Org Settings > Security & Privacy > Customer Lockbox` y `https://portal.azure.com > Customer Lockbox` `[Verificado MS Learn]`.
- **Rol Responsable:** Compliance Officer / Cloud Governance.
- **Procedimiento Paso a Paso:**
  1. Comprobar que la casilla **Require approval for all data access requests** esté marcada en M365 Admin Center `[Verificado MS Learn]`.
  2. Comprobar que el módulo **Administration** de Customer Lockbox for Microsoft Azure esté habilitado y que las suscripciones críticas cuenten con aprobadores activos (`Azure Customer Lockbox Approver for Subscription`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/telemetría de cumplimiento MCSB `PA-8` en Microsoft Defender for Cloud y Compliance Manager `[Verificado MS Learn]`.

### S-05: Revisión de Latencia y Salud de Azure Key Vaults / Managed HSM en Regiones Emparejadas
- **Objetivo:** Prevenir indisponibilidades simultáneas revisando métricas de latencia REST, disponibilidad (> 99.9 %) y configuración de firewall de confianza `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > Key vaults / Managed HSMs > Monitoring > Metrics & Networking` `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud Security Architect.
- **Procedimiento Paso a Paso:**
  1. Revisar métricas `ServiceApiLatency`, `Availability` y códigos HTTP `4xx`/`5xx` en todos los Key Vaults / Managed HSM de las Suscripciones 1 y 2 `[Decisión / Propuesta Editorial]`.
  2. Confirmar en `Networking` que, si el firewall está activo, la opción **Allow Trusted Microsoft Services to bypass this firewall** siga marcada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de Azure Monitor sobre los recursos criptográficos de Customer Key `[Decisión / Propuesta Editorial]`.

### S-06: Conciliación Semanal de Margen de Licenciamiento Elegible para Customer Key
- **Objetivo:** Impedir que el crecimiento orgánico de usuarios Exchange, Teams o SharePoint deje al tenant por debajo del umbral de licencias Customer Key (lo cual provocaría reversión automática al cifrado administrado por Microsoft) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Billing > Licenses` `[Verificado MS Learn]`.
- **Rol Responsable:** M365 Licensing Admin + Compliance Officer.
- **Procedimiento Paso a Paso:**
  1. Verificar la regla oficial de **Multi-workload DEP**: `Licencias Customer Key >= Máximo(Usuarios con licencia Exchange, Usuarios con licencia Teams)` `[Verificado MS Learn]`.
  2. Verificar la regla oficial de **SharePoint DEP**: `Licencias Customer Key >= Usuarios con licencia SharePoint` `[Verificado MS Learn]`.
  3. Disparar compra o reasignación preventiva si el margen libre cae por debajo del 5 % `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Hoja de control semanal de ratios de licenciamiento Customer Key `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Recertificación de Aprobadores Lockbox, Grupo Aprobador PAM, `SystemAccounts` y Custodios HSM
- **Objetivo:** Validar el principio de mínimo privilegio y separación estricta de funciones en los tres pilares `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Microsoft Entra ID (`Access Reviews`), `https://admin.microsoft.com` y Azure RBAC `[Verificado MS Learn]`.
- **Rol Responsable:** CISO / Identity Governance Lead.
- **Procedimiento Paso a Paso:**
  1. Auditar quiénes poseen el rol `Customer Lockbox access approver` en M365 y `Azure Customer Lockbox Approver for Subscription` en Azure (recordando activar roles elegibles o usar asignación directa en el grupo dedicado de Azure Lockbox) `[Verificado MS Learn]`.
  2. Auditar los miembros del *mail-enabled security group* aprobador de M365 PAM (confirmando que sea efectivamente un grupo de seguridad habilitado para correo y no una lista de distribución estándar) y validar cada cuenta en `-SystemAccounts` `[Verificado MS Learn]`.
  3. Comprobar mediante Azure RBAC que ningún administrador posea permisos simultáneos sobre la Suscripción 1 y la Suscripción 2 de Customer Key `[Verificado MS Learn]`.
- **Evidencia Auditable:** Campaña mensual de *Entra Access Reviews* completada y matriz SoD firmada `[Decisión / Propuesta Editorial]`.

### M-02: Verificación de Integridad de Backups Offline/Online de Claves Raíz (`Backup-AzKeyVaultKey`)
- **Objetivo:** Garantizar la existencia y legibilidad de copias de respaldo cifradas online y offline de cada clave raíz RSA/RSA-HSM ante pérdida catastrófica `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell y bóveda física/offline de custodia criptográfica `[Verificado MS Learn]`.
- **Rol Responsable:** Cryptography & PKI Lead (Custodios Sub 1 y Sub 2 por separado).
- **Procedimiento Paso a Paso:**
  1. Inventariar las versiones actuales e históricas de todas las claves con `Get-AzKeyVaultKey -VaultName <Vault> -IncludeVersions` (o `-HsmName`) `[Verificado MS Learn]`.
  2. Confirmar que cada clave y versión creada posea su archivo generado con `Backup-AzKeyVaultKey` resguardado tanto en almacenamiento inmutable online como en custodia offline segregada `[Verificado MS Learn]`.
  3. Verificar que ninguna clave tenga fecha de expiración configurada (`Expires == null`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual de verificación de custodia dual de backups de claves con hashes SHA-256 `[Decisión / Propuesta Editorial]`.

### M-03: Auditoría y Migración de Modelo de Permisos Legacy Access Policies hacia Azure RBAC
- **Objetivo:** Asegurar que el 100 % de los Key Vaults de Customer Key operen bajo **Azure role-based access control (Azure RBAC)** y no bajo políticas de acceso heredadas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > Key vaults > Settings > Access configuration` `[Verificado MS Learn]`.
- **Rol Responsable:** Key Vault RBAC Security Officer.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar `Get-AzKeyVault` verificando `EnableRbacAuthorization == True`, `EnableSoftDelete == True` (`SoftDeleteRetentionInDays == 90`) y `EnablePurgeProtection == True` `[Verificado MS Learn]`.
  2. Si existiera algún baúl histórico con *Vault access policy*, ejecutar la secuencia oficial: remover políticas heredadas (`Remove-AzKeyVaultAccessPolicy`), cambiar a *Azure role-based access control* y asignar `Key Vault Crypto Service Encryption User` a la aplicación M365 correspondiente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de Azure Policy confirmando 100 % RBAC, Soft Delete 90d y Purge Protection `[Verificado MS Learn]`.

### M-04: Validación de Reglas de Alerta en Defender for Cloud Apps, Sentinel y Transición Graph `AuditLogQuery`
- **Objetivo:** Comprobar el disparo efectivo de alertas ante eventos Lockbox, Customer Key y M365 PAM, preparando los playbooks para el retiro de `Search-UnifiedAuditLog` (15-oct-2027) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` (Defender for Cloud Apps / Sentinel) y Microsoft Graph `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Detection Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar que la política de alerta en **Microsoft Defender for Cloud Apps** para `Set-AccessToCustomerDataRequest` y `Microsoft Operator` esté habilitada (supliendo la ausencia de alerta nativa post-aprobación en M365 Admin Center) `[Verificado MS Learn]`.
  2. Validar consultas sobre `Microsoft Graph security/auditLog/queries` (GA en octubre de 2026) reemplazando progresivamente scripts heredados basados en `Search-UnifiedAuditLog` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Prueba mensual de reglas analíticas en Sentinel y catálogo de scripts migrados a Graph `[Decisión / Propuesta Editorial]`.

### M-05: Conciliación Financiera de Suscripciones Dedicadas de Customer Key y Protección de Suscripción
- **Objetivo:** Evitar suspensiones administrativas o de facturación en las dos suscripciones Azure de pago dedicadas exclusivamente a Customer Key `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > Subscriptions & Cost Management` `[Verificado MS Learn]`.
- **Rol Responsable:** FinOps Lead + Cloud Governance.
- **Procedimiento Paso a Paso:**
  1. Confirmar que ambas suscripciones sigan vinculadas a un acuerdo empresarial de pago activo (Enterprise Agreement / MCA) sin métodos de pago próximos a vencer `[Verificado MS Learn]`.
  2. Verificar mediante Azure Policy que **ninguna carga de trabajo ajena a Customer Key** haya sido desplegada en esas dos suscripciones dedicadas `[Verificado MS Learn]`.
  3. Confirmar la existencia de `CanNotDelete` Resource Locks sobre los grupos de recursos y Key Vaults / Managed HSM `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Estado de suscripción activa, cumplimiento Azure Policy de aislamiento y bloqueo `CanNotDelete` `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Simulacro de Mesa y Técnico de Flujos Customer Lockbox y Elevación M365 PAM
- **Objetivo:** Entrenar a los aprobadores ejecutivos y al SOC en el manejo de solicitudes Lockbox (incluyendo detección de ingeniería social) y elevaciones JIT de emergencia en M365 PAM `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` y Exchange Online PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + Identity Lead + SOC Manager.
- **Procedimiento Paso a Paso:**
  1. Ejecutar una solicitud real controlada en M365 PAM (`New-ElevatedAccessRequest` para un cmdlet de prueba), aprobarla por pares (`Approve-ElevatedAccessRequest`), ejecutar la tarea, revocar anticipadamente el permiso y verificar la traza completa en Purview Audit `[Verificado MS Learn]`.
  2. Simular en ejercicio de mesa la recepción de un correo falso de Customer Lockbox con enlace de inicio de sesión para validar que los aprobadores identifiquen el intento de phishing y verifiquen directamente en `admin.microsoft.com > Support > Customer Lockbox Requests` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe trimestral del ejercicio con tiempos de respuesta y capturas de auditoría `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Prueba de Restauración de Clave Raíz en Entorno Aislado (`Restore-AzKeyVaultKey`)
- **Objetivo:** Comprobar empíricamente que los archivos `.backup` de claves raíz pueden restaurarse sin errores en una bóveda de contingencia `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell (Key Vault / Managed HSM de laboratorio aislado) `[Verificado MS Learn]`.
- **Rol Responsable:** Cryptography & PKI Lead.
- **Procedimiento Paso a Paso:**
  1. Seleccionar un Key Vault / HSM de validación sin clave preexistente con el mismo nombre (ya que `Restore-AzKeyVaultKey` falla si ya existe una clave con idéntico nombre) `[Verificado MS Learn]`.
  2. Ejecutar `Restore-AzKeyVaultKey -VaultName <TestVault> -InputFile <BackupFile>` verificando la restauración íntegra de versiones y metadatos `[Verificado MS Learn]`.
  3. Destruir la copia temporal del laboratorio tras documentar la prueba exitosa `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora trimestral de prueba de restauración criptográfica firmada `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Revisión de Arquitectura Criptográfica y Re-cifrado de Lotes Windows 365 / CMK eDiscovery
- **Objetivo:** Evaluar la cobertura total de Customer Key frente a nuevas cargas de trabajo M365, lotes adicionales de Windows 365 (> 20.000 Cloud PCs) y exportaciones CMK de eDiscovery `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com`, `https://purview.microsoft.com` y Exchange/SPO PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud Security Architect + Endpoint Lead + Compliance Lead.
- **Procedimiento Paso a Paso:**
  1. Si la flota supera los **20.000 Windows 365 Cloud PCs** (límite por ejecución), verificar que todos los lotes hayan completado su re-cifrado en horarios de mantenimiento (recordando que el proceso reinicia y desconecta temporalmente cada Cloud PC) `[Verificado MS Learn]`.
  2. Revisar la postura combinada de Customer Key frente a etiquetas con **Double Key Encryption (DKE)** para asegurar que ningún repositorio colaborativo o de M365 Copilot haya sido bloqueado inadvertidamente por uso excesivo de DKE `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral de postura criptográfica M365 y cobertura Windows 365 `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Ceremonia Anual Gobernada de Rotación de Claves Customer Key (Solo si la Política lo Exige)
- **Objetivo:** Ejecutar de forma segura la rotación periódica de claves raíz (`Method 1: Update existing key + Refresh`) cuando la normativa interna o sectorial exija rotación anual, preservando todas las versiones previas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell, Exchange Online PowerShell y SharePoint Online Management Shell `[Verificado MS Learn]`.
- **Rol Responsable:** Cryptography & PKI Lead (Custodios Sub 1 y Sub 2) + Customer Key Policy Admin.
- **Procedimiento Paso a Paso:**
  1. Confirmar la necesidad normativa (Microsoft advierte rotar claves de Customer Key **únicamente** cuando las políticas de seguridad/cumplimiento lo exijan) `[Verificado MS Learn]`.
  2. En cada bóveda, generar una **nueva versión de la misma clave** sin fecha de expiración usando `Add-AzKeyVaultKey -VaultName <Vault> -Name <KeyName> -Destination HSM -KeyOps @('wrapKey','unwrapKey') -NotBefore (Get-Date)` y ejecutar de inmediato `Backup-AzKeyVaultKey` `[Verificado MS Learn]`.
  3. Refrescar las DEPs en Exchange y Multi-workload ejecutando `Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Refresh` y `Set-DataEncryptionPolicy -Identity <Policy> -Refresh` `[Verificado MS Learn]`.
  4. En SharePoint y OneDrive, rotar **una sola clave a la vez**: ejecutar `Update-SPODataEncryptionPolicy <SPOAdminSiteUrl> -KeyVaultName <Name> -KeyName <Name> -KeyVersion <Version> -KeyType Primary`, monitorear con `Get-SPODataEncryptionPolicy` hasta que pase de `Rolling` a **`Registered`** al 100 %, y recién entonces repetir para `Secondary` `[Verificado MS Learn]`.
  5. **Verificar estrictamente que ninguna versión anterior de las claves haya sido deshabilitada ni eliminada** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta de ceremonia criptográfica anual con salidas `Registered` y respaldos offline actualizados `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook ante Posible Compromiso de Clave Raíz en Azure Key Vault / Managed HSM (`Replace Method`)
- **Disparador:** Sospecha fundada o confirmación de exposición de credenciales de administración de una suscripción/bóveda de Customer Key o reestructuración mayor `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell + Exchange Online PowerShell + SharePoint PowerShell `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Contener el plano de identidad revocando sesiones en Entra ID del administrador comprometido **sin deshabilitar ni borrar aún la clave activa en Key Vault** (deshabilitarla prematuramente provocaría caída inmediata del acceso de usuarios) `[Verificado MS Learn]`.
  2. Crear claves completamente nuevas (`RSA` / `RSA-HSM`, sin expiración, con Soft Delete + Purge Protection) y respaldarlas con `Backup-AzKeyVaultKey`, verificando permisos RBAC para los principales de M365 `[Verificado MS Learn]`.
  3. Ejecutar reemplazo con el parámetro `-Replace` proporcionando **ambos URIs**: `Set-M365DataAtRestEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>` y `Set-DataEncryptionPolicy -Identity <Policy> -Replace -AzureKeyIDs <KeyURI1>,<KeyURI2>`; en SharePoint ejecutar `Update-SPODataEncryptionPolicy` secuencialmente (una clave a la vez hasta `Registered`) `[Verificado MS Learn]`.
  4. **Respetar los tiempos obligatorios de guarda:** esperar **mínimo 24 horas** tras completar el reemplazo antes de deshabilitar la clave comprometida, y **24 a 48 horas adicionales** antes de cualquier acción posterior (conservando siempre las claves históricas requeridas por backups de SharePoint) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado actualizado de DEPs con nuevos URIs y registro cronológico de espera >= 24 h / 48 h `[Verificado MS Learn]`.

### AH-02: Playbook de Recuperación de Emergencia mediante la Availability Key ante Pérdida Total de Claves del Cliente
- **Disparador:** Pérdida simultánea o inaccesibilidad permanente e irrecuperable de ambos Key Vaults / claves raíz del cliente `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Microsoft Support + Azure PowerShell + Exchange / SharePoint PowerShell `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Para **Exchange y Multi-workload**: aprovisionar dos nuevas claves Customer Key en dos suscripciones Azure válidas, crear una nueva DEP (`New-DataEncryptionPolicy` / `New-M365DataAtRestEncryptionPolicy`) y asignarla a los buzones o al tenant; la Availability Key protege y permite re-cifrar los datos en segundo plano (hasta **72 horas**) `[Verificado MS Learn]`.
  2. Para **SharePoint y OneDrive**: abrir un ticket crítico con **Microsoft Support** solicitando explícitamente activar la Availability Key para recuperación (aprobando la solicitud Customer Lockbox correspondiente si aplica), crear dos nuevas claves y una nueva DEP de SharePoint/OneDrive y re-incorporar el servicio (~**4 horas** típicas tras la activación según cantidad de sitios) `[Verificado MS Learn]`.
  3. Auditar en Purview Audit los registros `CustomerKeyServiceEncryption` (`Fallback to availability key`) generados durante la contingencia `[Verificado MS Learn]`.
- **Evidencia Auditable:** Ticket de soporte Microsoft, confirmación de nueva DEP activa y logs de auditoría `[Verificado MS Learn]`.

### AH-03: Playbook de Rechazo de Emergencia o Auditoría de Solicitud Sospechosa de Customer Lockbox
- **Disparador:** Recepción de una solicitud Customer Lockbox sin ticket de soporte correlacionado, con alcance excesivo o notificación por correo anómala `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Support > Customer Lockbox Requests` / PowerShell `Set-AccessToCustomerDataRequest` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Si el correo recibido contiene un hipervínculo que solicita credenciales de inicio de sesión en Microsoft 365, clasificarlo inmediatamente como **phishing** (Microsoft nunca incluye enlaces de sign-in en notificaciones M365 Lockbox) y reportarlo en Microsoft Defender for Office 365 `[Verificado MS Learn]`.
  2. Si la solicitud existe realmente en `admin.microsoft.com > Support > Customer Lockbox Requests` pero carece de validación del dueño interno del servicio, seleccionar **Deny** inmediatamente (o ejecutar `Set-AccessToCustomerDataRequest` para denegar/cancelar) `[Verificado MS Learn]`.
  3. Contactar a Microsoft Support citando el número de Service Request para exigir aclaración formal del motivo de escalamiento `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro `Set-AccessToCustomerDataRequest` con `ApprovalDecision = Deny` en Purview Audit `[Verificado MS Learn]`.

### AH-04: Playbook de Revocación Inmediata de Elevación Activa en M365 PAM (`Revoke` / Compromiso Admin)
- **Disparador:** Alerta de compromiso de identidad (Entra ID Identity Protection / Defender XDR) o conducta anómala de un administrador que cuenta con una ventana activa aprobada en M365 PAM `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Settings > Org Settings > Security & Privacy > Privileged access > Manage access policies and requests` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ingresar a `Manage access policies and requests`, filtrar por estado **Approved**, seleccionar la solicitud activa del administrador afectado y pulsar **Revoke** para cortar de inmediato la autorización en el *Exchange Management runspace* `[Verificado MS Learn]`.
  2. En paralelo, revocar tokens de sesión en Microsoft Entra ID y desactivar cualquier rol activo en Entra PIM `[Decisión / Propuesta Editorial]`.
  3. Auditar todos los cmdlets ejecutados durante los minutos en que la ventana estuvo activa y revertir cualquier regla de transporte o conector malicioso creado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Estado revocado de la solicitud PAM y traza forense de comandos en `OfficeActivity` `[Verificado MS Learn]`.

### AH-05: Playbook Regulado de Salida Definitiva del Servicio y Destrucción Criptográfica (*Data Purge Path*) vs. Rollback Seguro
- **Disparador:** Decisión corporativa aprobada por Directorio de (A) regresar a claves gestionadas por Microsoft conservando los datos (*Rollback*), o (B) abandonar definitivamente Exchange Online destruyendo criptográficamente todos los buzones (*Data Purge Path*) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Azure PowerShell + Exchange Online PowerShell + Firma Legal Ejecutiva con Microsoft Support `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. **Control de Puerta Crítico:** Verificar qué escenario se solicita. Si la organización **continúa operando en Microsoft 365**, **PROHIBIDO ejecutar Data Purge Path**: para regresar a Microsoft-managed keys (*Rollback*), conservar los Key Vaults activos y con permisos intactos, ejecutar `Set-Mailbox -Identity <mailbox> -DataEncryptionPolicy $null` en Exchange o abrir ticket de Rollback ante Microsoft Support para Multi-workload / SharePoint (preview, no soportado en Gallatin/GCC-H/DoD) `[Verificado MS Learn]`.
  2. Si y solo si la organización **sale completamente de Exchange Online** y requiere *crypto-shredding* regulado (recordando que **purgar Multi-workload DEPs o SharePoint DEPs NO está soportado**): consolidar todos los buzones a purgar en una DEP de Exchange `[Verificado MS Learn]`.
  3. Remover los permisos `wrapKey` y `unwrapKey` de `Office 365 Exchange Online` en ambos Azure Key Vaults `[Verificado MS Learn]`.
  4. Ejecutar `Set-DataEncryptionPolicy <Policy ID> -PermanentDataPurgeRequested -PermanentDataPurgeReason <Reason> -PermanentDataPurgeContact <ContactName>` `[Verificado MS Learn]`.
  5. Solicitar a Microsoft Support el **Data Purge eDocument**, hacerlo firmar electrónicamente por el representante legal ejecutivo autorizado y remitirlo para que Microsoft verifique autenticidad, elimine la DEP, marque los buzones para eliminación permanente y **destruya irreversiblemente la Availability Key** `[Verificado MS Learn]`.
- **Evidencia Auditable:** *Data Purge eDocument* firmado legalmente y confirmación auditable bajo SOC 2 SSAE 18 de destrucción de DEP y Availability Key `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Microsoft Graph y PowerShell

#### Consulta 1: Microsoft Sentinel (KQL) — Decisiones Customer Lockbox y Auditoría Completa de `Microsoft Operator`
- **Plataforma / Tabla:** Microsoft Sentinel / Defender XDR (`OfficeActivity`) `[Verificado MS Learn]`.
```kusto
// Detecta aprobaciones/rechazos de Customer Lockbox M365 y toda acción posterior de ingenieros Microsoft
OfficeActivity
| where TimeGenerated > ago(30d)
| where Operation =~ "Set-AccessToCustomerDataRequest"
    or UserId =~ "Microsoft Operator"
    or UserId startswith "BOXServiceAccount@"
| project TimeGenerated, UserId, Operation, ClientIP, ResultStatus, OfficeWorkload, Parameters
| sort by TimeGenerated desc
```

#### Consulta 2: Microsoft Sentinel (KQL) — Alerta Crítica de Fallback a la Availability Key en Customer Key
- **Plataforma / Tabla:** Microsoft Sentinel (`OfficeActivity` — `CustomerKeyServiceEncryption`) `[Verificado MS Learn]`.
```kusto
// Alerta cuando Exchange o Multi-workload recurren a la Availability Key por fallos en ambos Key Vaults
OfficeActivity
| where TimeGenerated > ago(7d)
| where RecordType =~ "CustomerKeyServiceEncryption" or Operation =~ "Fallback to availability key"
| project TimeGenerated, OfficeWorkload, Operation, OrganizationId, Parameters
| sort by TimeGenerated desc
```

#### Consulta 3: Microsoft Sentinel (KQL) — Vigilancia de Operaciones Sensibles en Azure Key Vaults / Managed HSM de Customer Key
- **Plataforma / Tabla:** Microsoft Sentinel (`AzureDiagnostics`) `[Verificado MS Learn]`.
```kusto
// Detecta borrados, cambios de políticas/RBAC o fallos HTTP 403/404 en los Key Vaults de Customer Key
AzureDiagnostics
| where TimeGenerated > ago(7d)
| where ResourceProvider =~ "MICROSOFT.KEYVAULT"
| where OperationName in ("KeyDelete", "KeyPurge", "KeyUpdate", "VaultDelete", "VaultPatch", "RoleAssignmentCreate", "RoleAssignmentDelete")
    or ResultSignature != "OK" and httpStatusCode_d >= 400
| project TimeGenerated, Resource, OperationName, CallerIPAddress, identity_claim_appid_g, identity_claim_upn_s, httpStatusCode_d, ResultDescription
| sort by TimeGenerated desc
```

#### Consulta 4: Microsoft Sentinel (KQL) — Auditoría de Políticas, Solicitudes y Aprobaciones en M365 PAM
- **Plataforma / Tabla:** Microsoft Sentinel (`OfficeActivity`) `[Verificado MS Learn]`.
```kusto
// Monitorea todo el ciclo de vida de Microsoft Purview Privileged Access Management (M365 PAM)
OfficeActivity
| where TimeGenerated > ago(14d)
| where Operation has_any (
    "Enable-ElevatedAccessControl",
    "Disable-ElevatedAccessControl",
    "New-ElevatedAccessApprovalPolicy",
    "Remove-ElevatedAccessApprovalPolicy",
    "New-ElevatedAccessRequest",
    "Approve-ElevatedAccessRequest",
    "Deny-ElevatedAccessRequest"
)
| project TimeGenerated, UserId, Operation, ClientIP, ResultStatus, Parameters
| sort by TimeGenerated desc
```

#### Consulta 5: Microsoft Graph PowerShell — Búsqueda Moderna en Purview Audit (`auditLog/queries`) Sustituyendo `Search-UnifiedAuditLog`
- **Plataforma / Tabla:** Microsoft Graph PowerShell (`security/auditLog/queries` — GA Octubre 2026) `[Verificado MS Learn]`.
```powershell
# Reemplaza Search-UnifiedAuditLog (retiro anunciado para 15-oct-2027) para auditar Lockbox y PAM
Connect-MgGraph -Scopes "AuditLogsQuery.Read.All"
$body = @{
    displayName = "Audit_Lockbox_and_PAM_7d"
    filterStartDateTime = (Get-Date).AddDays(-7).ToUniversalTime().ToString("o")
    filterEndDateTime   = (Get-Date).ToUniversalTime().ToString("o")
    operationFilters    = @("Set-AccessToCustomerDataRequest", "New-ElevatedAccessRequest", "Approve-ElevatedAccessRequest")
}
Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries" -Body ($body | ConvertTo-Json)
```

#### Consulta 6: Azure & Exchange/SPO PowerShell — Verificación Integral No Destructiva de Customer Key
- **Plataforma / Tabla:** Azure PowerShell (`M365CustomerKeyOnboarding`), Exchange Online y SharePoint PowerShell `[Verificado MS Learn]`.
```powershell
# Valida recursos Customer Key sin realizar cambios y verifica estado de DEPs en las tres cargas
$req = New-CustomerKeyOnboardingRequest -Organization "<TenantGUID>" -Scenario MDEP `
    -Subscription1 "<Sub1>" -KeyIdentifier1 "<KeyURI1>" `
    -Subscription2 "<Sub2>" -KeyIdentifier2 "<KeyURI2>" -OnboardingMode Validate
$req | Select-Object ID, ValidationResult, FailedValidations
Get-M365DataAtRestEncryptionPolicyAssignment
Get-DataEncryptionPolicy | Select-Object Name, Enabled, PolicyState
Get-SPODataEncryptionPolicy
```

#### Consulta 7: Exchange Online PowerShell — Inventario de Políticas y Solicitudes Activas de M365 PAM
- **Plataforma / Tabla:** Exchange Online PowerShell `[Verificado MS Learn]`.
```powershell
# Lista todas las políticas de aprobación configuradas (máx. 30) y las solicitudes recientes en M365 PAM
Connect-ExchangeOnline
Get-ElevatedAccessApprovalPolicy | Format-Table Name, Task, ApprovalType, ApproverGroup -AutoSize
Get-ElevatedAccessRequest | Select-Object RequestId, Requestor, Task, RequestStatus, DurationHours, CreatedTime
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Pilar / Componente | Método de Verificación Rápida | Estado Esperado ("Proof of Life") |
| :--- | :--- | :--- |
| **Customer Lockbox M365** | `admin.microsoft.com > Settings > Org Settings > Security & Privacy > Customer Lockbox` `[Verificado MS Learn]` | `Require approval for all data access requests = Checked` y rol `Customer Lockbox access approver` poblado `[Verificado MS Learn]` |
| **Customer Lockbox Azure** | `portal.azure.com > Customer Lockbox for Microsoft Azure > Administration` `[Verificado MS Learn]` | Módulo habilitado con plan Azure Support >= `Developer` y aprobadores activos en suscripciones `[Verificado MS Learn]` |
| **Customer Key Onboarding & Vaults** | `New-CustomerKeyOnboardingRequest -OnboardingMode Validate` `[Verificado MS Learn]` | `ValidationResult = Success`, `SoftDelete = 90d`, `PurgeProtection = True`, `Expires = null` y RBAC activo `[Verificado MS Learn]` |
| **DEPs Multi-Workload, EXO y SPO** | `Get-M365DataAtRestEncryptionPolicyAssignment` + `Get-SPODataEncryptionPolicy` `[Verificado MS Learn]` | MDEP asignada, buzones con `IsEncrypted = True` y SharePoint en estado `Registered` (100 %) `[Verificado MS Learn]` |
| **Windows 365 Cloud PC Customer Key** | `intune.microsoft.com > Tenant administration > Cloud PC encryption type` `[Verificado MS Learn]` | Tipo de cifrado establecido en `Microsoft Purview Customer Key` completado sin alertas `[Verificado MS Learn]` |
| **Microsoft Purview PAM** | `Get-ElevatedAccessApprovalPolicy` y `admin.microsoft.com > Privileged access` `[Verificado MS Learn]` | `Require approvals for privileged tasks = On`, grupo aprobador *mail-enabled security* y políticas Manual activas `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs de Excelencia Operacional

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Clasificación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Cobertura de Auditoría Post-Acceso Lockbox (`Microsoft Operator`)** | `(Solicitudes Lockbox aprobadas con revisión forense firmada de logs Microsoft Operator / Total solicitudes aprobadas) * 100` | `100 %` en <= 24 h del cierre | Por evento / Mensual | CISO / DPO / Auditoría Interna | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cobertura de Cifrado Customer Key en Buzones y Sitios Elegibles** | `(Buzones elegibles con DEP activa + Sitios SPO en estado Registered) / Total activos en alcance * 100` | `>= 99.9 %` | Semanal | Cloud Security Architect / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Eventos de Fallback No Planificado a la Availability Key** | `Conteo de eventos RecordType == CustomerKeyServiceEncryption (Fallback to availability key)` | `0 eventos` por error de configuración/permisos | Diaria / Mensual | Cryptography Lead / SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Cumplimiento de Inmutabilidad en Bóvedas Criptográficas** | `(Key Vaults / Managed HSM con Soft Delete 90d + Purge Protection + Azure RBAC + Claves sin expiración / Total bóvedas) * 100` | `100 %` | Mensual | Cryptography Lead / GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Margen de Seguridad de Licenciamiento Customer Key** | `((Licencias Customer Key asignadas - Máx(Usuarios EXO, Teams, SPO)) / Máx(Usuarios EXO, Teams, SPO)) * 100` | `>= 5 %` de holgura positiva continua | Semanal | FinOps / Compliance Officer | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Aprobación Peer-Review en M365 PAM sin Autoaprobación** | `(Solicitudes PAM aprobadas por un par distinto del solicitante con ticket válido / Total solicitudes aprobadas) * 100` | `100 %` (0 autoaprobaciones) | Mensual | Identity Lead / Auditoría Interna | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Minimización de Cuentas Excluidas (`SystemAccounts`) en M365 PAM** | `Conteo de cuentas en parámetro -SystemAccounts y % sin inicios de sesión interactivos` | `<= 2 cuentas` y `100 %` no interactivo | Mensual | Identity Lead / SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Éxito en Pruebas Trimestrales de Restauración de Backups de Claves** | `(Claves raíz probadas exitosamente con Restore-AzKeyVaultKey en laboratorio / Total claves raíz activas) * 100` | `100 %` | Trimestral | CISO / Comité de Riesgos | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Observables |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Exposición Implícita** | Customer Lockbox desactivado; cifrado únicamente con claves gestionadas por Microsoft; administradores Exchange permanentes sin Entra PIM ni M365 PAM. |
| **Nivel 2** | **Básico / Controles Parciales** | Customer Lockbox M365 activado pero aprobado por `Global Administrators` sin revisar logs de `Microsoft Operator`; Entra PIM desplegado sin protección granular de cmdlets en M365 PAM. |
| **Nivel 3** | **Definido / Soberanía Estandarizada** | Customer Lockbox M365 y Azure habilitados con aprobadores dedicados y alertas Defender for Cloud Apps; Customer Key operativo en Azure Key Vault Premium con Azure RBAC y 2 suscripciones; M365 PAM protegiendo top cmdlets de Exchange. |
| **Nivel 4** | **Gestionado / Cero Privilegio Permanente** | Despliegue consolidado en **Azure Key Vault Managed HSM** (FIPS 140-2 Level 3, 2 instancias) cubriendo MDEP (Teams, M365 Copilot, Windows 365 Cloud PCs), Exchange y SharePoint; monitoreo SIEM diario de `CustomerKeyServiceEncryption` y custodia dual auditada. |
| **Nivel 5** | **Optimizado / Resiliencia Criptográfica Verificada** | Validación semanal automatizada `M365CustomerKeyOnboarding -OnboardingMode Validate`, pruebas trimestrales `Restore-AzKeyVaultKey`, extensión CMK a exportaciones de eDiscovery, consultas Graph `auditLog/queries` y coexistencia calibrada con DKE para activos *Top Secret*. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

| Función NIST CSF 2.0 | Subcategoría Oficial (CSWP 29) | Táctica / Técnica MITRE ATT&CK Relacionada | Capacidad Habilitadora en Lockbox, Customer Key y M365 PAM | Evidencia Auditable Reproducible `[Decisión / Propuesta Editorial]` |
| :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.SC-07` (Los riesgos planteados por proveedores y terceros son comprendidos y gestionados) | `T1199` (Trusted Relationship) | **Customer Lockbox** (M365 y Azure MCSB `PA-8`) impide el acceso unilateral de ingenieros del proveedor al contenido del cliente sin autorización explícita | Configuración activa de Lockbox e historial de solicitudes aprobadas/denegadas con Service Request ID |
| **GOVERN (GV)** | `GV.RR-02` (Roles, responsabilidades y autoridades establecidos y aplicados) | `T1078.004` (Valid Accounts: Cloud Accounts) | Separación de custodios entre Suscripción Azure 1 y Suscripción Azure 2 en **Customer Key**, rol `Customer Lockbox access approver` y grupo aprobador en **M365 PAM** | Matriz RBAC de suscripciones Azure, membresía de grupos aprobadores y campañas Entra Access Reviews |
| **IDENTIFY (ID)** | `ID.AM-05` (Los recursos se priorizan según clasificación, criticidad y valor de negocio) | `T1530` (Data from Cloud Storage) | Segmentación arquitectónica entre el 95 % de cargas protegidas con **Customer Key** (MDEP, EXO, SPO, Windows 365, Copilot) y el ~5 % ultra-secreto con **DKE** | Inventario de DEPs (`Get-M365DataAtRestEncryptionPolicy`, `Get-DataEncryptionPolicy`, `Get-SPODataEncryptionPolicy`) |
| **IDENTIFY (ID)** | `ID.RA-06` (Las respuestas al riesgo se eligen, priorizan, planifican y siguen) | `T1098` (Account Manipulation) | Validación preventiva de configuración criptográfica mediante `New-CustomerKeyOnboardingRequest -OnboardingMode Validate` | Reporte semanal `PassedValidations` sin reglas fallidas en `M365CustomerKeyOnboarding` |
| **PROTECT (PR)** | `PR.AA-05` (Permisos de acceso y autorizaciones gestionados por mínimo privilegio y separación de funciones) | `T1098.002` (Additional Email Delegate Permissions) | Defensa en profundidad **Entra PIM + M365 PAM**: aprobación manual JIT a nivel de cmdlet (`New-ElevatedAccessRequest` / `Approve-ElevatedAccessRequest`, máx. 4 h default) | Salida de `Get-ElevatedAccessApprovalPolicy` y registros de aprobación por pares en Purview Audit |
| **PROTECT (PR)** | `PR.DS-01` (Confidencialidad, integridad y disponibilidad de datos en reposo protegidas) | `T1565` (Data Manipulation) | Cifrado de servicio con **Customer Key** sobre **Azure Key Vault Premium HSM / Managed HSM** (FIPS 140-2 L3) con `Soft Delete` (90d) y `Purge Protection` | Propiedades de bóvedas en Azure Resource Graph, estado `Registered` en SPO y estado CMK en Windows 365 |
| **DETECT (DE)** | `DE.CM-03` (Actividades del personal y operadores externos monitoreadas para detectar eventos adversos) | `T1114.003` (Email Forwarding Rule) | Auditoría inmutable de acciones ejecutadas por **`Microsoft Operator`** tras Lockbox y de cmdlets elevados ejecutados en el *Exchange Management runspace* | Alertas activas en Microsoft Defender for Cloud Apps y consultas KQL sobre `OfficeActivity` |
| **DETECT (DE)** | `DE.CM-09` (Hardware, software y entornos de ejecución monitoreados para detectar anomalías) | `T1498` / Degradación criptográfica | Telemetría de **Fallback to availability key** (`RecordType: CustomerKeyServiceEncryption`) y logs `AzureDiagnostics` de Key Vault / Managed HSM | Reglas analíticas en Microsoft Sentinel para `CustomerKeyServiceEncryption` y errores HTTP >= 400 en Key Vault |
| **RESPOND (RS)** | `RS.MI-01` (Incidentes contenidos de forma oportuna) | `T1078` (Valid Accounts) | Acción inmediata **Deny** en solicitudes Lockbox sospechosas y acción **Revoke** en consola sobre aprobaciones activas de **M365 PAM** ante compromiso de cuenta | Evento `ApprovalDecision = Deny` en Purview Audit y registro de revocación anticipada en M365 PAM |
| **RESPOND (RS)** | `RS.MI-02` (Incidentes erradicados) | `T1552` (Unsecured Credentials / Compromised Keys) | Reemplazo controlado de claves raíz comprometidas mediante `Set-DataEncryptionPolicy -Replace` y `Set-M365DataAtRestEncryptionPolicy -Replace` | Registro de ejecución de `-Replace` respetando ventanas de 24 h / 48 h antes de deshabilitar claves previas |
| **RECOVER (RC)** | `RC.RP-03` (Integridad de copias de seguridad y activos verificada antes de la restauración) | `T1490` (Inhibit System Recovery) | Respaldo offline/online con `Backup-AzKeyVaultKey`, validación con `Restore-AzKeyVaultKey` y recuperación de emergencia asistida por la **Availability Key** | Actas trimestrales de restauración en laboratorio y procedimiento documentado de recuperación con Availability Key |
| **RECOVER (RC)** | `RC.CO-03` (Actividades de salida, recuperación y cumplimiento comunicadas de forma auditable) | N/A (Salida regulada / *Exit Strategy*) | Proceso formal auditado bajo SOC 2 de **Data Purge Path** (firma de *Data Purge eDocument* y destrucción de Availability Key al salir de Exchange) o *Rollback* controlado | Documentación de *Exit Strategy* aprobada por Directorio e informes SOC 1 / SOC 2 del Service Trust Portal |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta Oficial Microsoft Learn / Certificaciones Vigentes (Nov 2026) | Recursos Oficiales, Guías Interactivas y Comunidad MVP | Laboratorio Práctico Obligatorio `[Decisión / Propuesta Editorial]` |
| :--- | :--- | :--- | :--- |
| **Cryptography & Cloud Security Architect** | Módulo *Understand Microsoft 365 encryption* + Certificaciones **SC-401** (*Information Security Administrator*) y **AZ-500** (*Azure Security Technologies*) `[Verificado MS Learn]` | Documentación oficial de *Customer Key Onboarding Service*, *Managed HSM* y *Availability Key* + comparativas Purview/Copilot de **Joanne Klein** `[Verificado MS Learn]` | Aprovisionar 2 bóvedas de prueba con Soft Delete + Purge Protection, ejecutar `New-CustomerKeyOnboardingRequest -OnboardingMode Validate` y probar `Backup/Restore-AzKeyVaultKey`. |
| **Identity & Exchange Privileged Admin** | Módulo *Implement privileged access management* + Certificación **SC-300** (*Identity and Access Administrator*) `[Verificado MS Learn]` | Guía interactiva *Monitor and control administrator tasks with privileged access management* + análisis técnico en profundidad de M365 PAM por **Vasil Michev** (*Practical365*) `[Verificado MS Learn]` | Configurar `Enable-ElevatedAccessControl` en tenant de laboratorio, proteger `Exchange\New-TransportRule` y completar el ciclo `New/Approve-ElevatedAccessRequest` + `Revoke`. |
| **CISO / Compliance Officer / Lockbox Approver** | Documentación *Customer Lockbox requests* (M365) + *Customer Lockbox for Microsoft Azure* + Control **MCSB v2 `PA-8`** `[Verificado MS Learn]` | Informes de aseguramiento **SOC 1 / SOC 2 SSAE 18** en *Microsoft Service Trust Portal* + guía práctica de **Michael Morten Sonne** (MVP) `[Verificado MS Learn]` | Auditar con Graph `auditLog/queries` y Sentinel los registros simulados de `Set-AccessToCustomerDataRequest` y `Microsoft Operator`. |
| **Endpoint / Windows 365 Administrator** | Guía oficial *Set up Microsoft Purview Customer Key for Windows 365 Cloud PCs* `[Verificado MS Learn]` | Documentación de Windows 365 Enterprise y Frontline en Microsoft Learn `[Verificado MS Learn]` | Validar en entorno piloto la transición de cifrado en `Tenant administration > Cloud PC encryption type` midiendo el impacto del reinicio automático del Cloud PC. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Verificadas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Técnica | Hallazgo Verificado a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **Cobertura de Customer Lockbox M365 sobre Windows 365 y M365 Copilot** | Microsoft Learn confirma que Customer Lockbox soporta **Exchange Online, SharePoint, OneDrive, Teams y Windows 365**, y que **todas las interacciones de Microsoft 365 Copilot** están cubiertas a través de Exchange Online `[Verificado MS Learn]`. | Se incorporó la cobertura completa de Copilot y Windows 365 y las ventanas exactas (12 h de expiración y 4 h máximas de acceso). |
| **2** | **Distinción Exacta con Customer Lockbox for Microsoft Azure (MCSB `PA-8`)** | En Azure Lockbox se exige plan de soporte >= *Developer*, la cola expira en **4 días** (no 12 h), la pestaña *History* del portal fue retirada (se audita en Activity Log / Entra Audit Log) y los roles PIM elegibles deben estar **activos antes** de que inicie la solicitud `[Verificado MS Learn]`. | Se construyó la tabla comparativa detallada `3.1.1` y la advertencia operativa sobre PIM en Azure Lockbox en `M-01`. |
| **3** | **Simplificación Arquitectónica con Managed HSM (2 Instancias vs. 6 Key Vaults)** | Mientras Azure Key Vault estándar/premium exige 3 pares (**6 Key Vaults**) para cubrir MDEP, Exchange y SharePoint, **Azure Key Vault Managed HSM** (FIPS 140-2 Level 3) requiere únicamente **2 instancias en total** (una por suscripción) `[Verificado MS Learn]`. | Se documentaron ambas topologías en `3.2.1` recomendando Managed HSM para despliegues corporativos multcarga de alta seguridad. |
| **4** | **Alcance Ampliado de Multi-Workload DEP (MDEP) y Lote de 20.000 Cloud PCs** | La MDEP cifra Windows 365 Cloud PCs (Enterprise y Frontline Dedicated/Shared, con re-cifrado y reinicio en lotes de hasta **20.000 Cloud PCs** desde Intune), Teams, interacciones M365 Copilot, EDM/etiquetas MIP y exportaciones directas CMK de eDiscovery `[Verificado MS Learn]`. | Se integraron los procedimientos exactos en `D-07`, `SM-01` y la matriz de DEPs `3.2.2`. |
| **5** | **Restricción Estricta del Data Purge Path (Solo Exchange Mailbox DEPs)** | Microsoft Learn advierte que la purga criptográfica permanente (`-PermanentDataPurgeRequested` + *Data Purge eDocument*) **solo está soportada para DEPs de buzones Exchange al salir del servicio**, y **NO está soportada en Multi-workload DEPs ni en SharePoint/OneDrive DEPs** `[Verificado MS Learn]`. | Se incorporó un control de puerta crítico en `AH-05` diferenciando *Rollback* seguro vs. *Data Purge Path* irreversible. |
| **6** | **Frontera Funcional Exacta entre Customer Key y Double Key Encryption (DKE)** | Actualizado en Learn (octubre 2026): **DKE** inhabilita Microsoft 365 Copilot (tanto en reposo como en uso en versiones actuales de Office), eDiscovery, DLP en SharePoint/OneDrive, Office Web, coautoría, AutoSave, Loop y Teams meetings/chat `[Verificado MS Learn]`. | Se documentó la matriz comparativa `3.2.4` para evitar despliegues erróneos de DKE sobre repositorios colaborativos o de IA. |
| **7** | **Límites Actuales de M365 PAM y Transición de Auditoría a Graph (`MC1505599`)** | M365 PAM mantiene un tope de **30 políticas** por organización enfocadas en Exchange, expiración de solicitud a las **24 h** y ventana aprobada por defecto de **4 h**; además, se incorpora Graph `auditLog/queries` (GA oct-2026) ante el retiro de `Search-UnifiedAuditLog` el 15-oct-2027 `[Verificado MS Learn]`. | Se reflejaron los límites reales en `3.3.1`, `S-03` y la consulta moderna Graph en `10.1`. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Diseñado | Clasificación | Justificación Arquitectónica y de Gobierno |
| :--- | :--- | :--- | :--- |
| **1** | **Catálogo Priorizado de Cmdlets Críticos para las 30 Políticas de M365 PAM (`S-03`)** | `Propuesta Editorial` | Dado el límite técnico actual de 30 políticas por organización, concentrarlas en reglas de transporte, conectores, permisos de buzón, asignaciones RBAC y `Set-DataEncryptionPolicy` maximiza la reducción de riesgo de exfiltración y sabotaje. |
| **2** | **Holgura Mínima >= 5 % en Licencias Elegibles de Customer Key (`S-06`, `KPI-05`)** | `Propuesta Editorial` | Como Microsoft valida periódicamente los conteos de licencias y revierte al cifrado por defecto si faltan licencias frente a usuarios de Exchange/Teams/SharePoint, mantener un colchón del 5 % previene reversiones accidentales en altas masivas. |
| **3** | **Alertamiento Obligatorio en Defender for Cloud Apps y Sentinel para Lockbox (`D-02`, `M-04`)** | `Propuesta Editorial` | Suple la ausencia documentada de alertas nativas post-aprobación en el portal de Microsoft 365 y asegura revisión forense del 100 % de sesiones `Microsoft Operator`. |
| **4** | **Pruebas Trimestrales de Restauración `Restore-AzKeyVaultKey` en Bóveda Aislada (`T-02`)** | `Propuesta Editorial` | Garantiza que los respaldos exigidos por Microsoft Learn sean verificadamente restaurables antes de enfrentar un desastre real y valida el requisito de nombre libre de clave. |
| **5** | **Mapeo Integrado a las 6 Funciones de NIST CSF 2.0 y Modelo de Madurez de 5 Niveles** | `Propuesta Editorial` | Articula los tres pilares de soberanía dentro de un marco auditable unificado para comités de riesgo, reguladores financieros y auditores externos. |

---

## 15. Directorio de Referencias Públicas Verificadas

| ID | Título del Recurso | URL Verificada | Tipo de Fuente | Autor / Entidad | Comentario de Verificación (Nov 2026) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REF-01** | Customer Lockbox requests (Microsoft Purview) | `https://learn.microsoft.com/en-us/purview/customer-lockbox-requests` | Microsoft Learn | Microsoft Corporation | Flujo completo M365 Lockbox, soporte Windows 365 y M365 Copilot, expiración 12 h, acceso máx. 4 h y auditoría `Microsoft Operator`. |
| **REF-02** | Customer Lockbox for Microsoft Azure | `https://learn.microsoft.com/en-us/azure/security/fundamentals/customer-lockbox-overview` | Microsoft Learn | Microsoft Corporation | Plan Developer, +40 servicios Azure (incluyendo OpenAI y Foundry), expiración 4 días, requisito PIM activo y control MCSB `PA-8` (jul-2026). |
| **REF-03** | Overview of Service encryption with Microsoft Purview Customer Key | `https://learn.microsoft.com/en-us/purview/customer-key-overview` | Microsoft Learn | Microsoft Corporation | Arquitectura en capas sobre BitLocker/DKM y SSE, y alcance exacto de las 3 categorías de DEPs (MDEP, Exchange y SharePoint). |
| **REF-04** | What is Microsoft 365 service encryption? | `https://learn.microsoft.com/en-us/purview/microsoft-365-service-encryption` | Microsoft Learn | Microsoft Corporation | Comparativa entre claves gestionadas por Microsoft y claves gestionadas por el cliente (Customer Key). |
| **REF-05** | Set up Customer Key (Azure Key Vault & Managed HSM) | `https://learn.microsoft.com/en-us/purview/customer-key-set-up` | Microsoft Learn | Microsoft Corporation | 2 suscripciones de pago, 6 Key Vaults vs. 2 Managed HSM, Soft Delete 90d + Purge Protection, RBAC y `M365CustomerKeyOnboarding`. |
| **REF-06** | Manage Customer Key encryption policies | `https://learn.microsoft.com/en-us/purview/customer-key-manage` | Microsoft Learn | Microsoft Corporation | Cmdlets oficiales de DEPs, verificación de estado, migración a Azure RBAC, *Rollback* y *Data Purge Path* exclusivo de Exchange (jun-2026). |
| **REF-07** | Learn about the availability key for Customer Key | `https://learn.microsoft.com/en-us/purview/customer-key-availability-key-understand` | Microsoft Learn | Microsoft Corporation | Almacenamiento aislado, disparadores de fallback (errores de sistema vs. Access Denied) y auditoría `CustomerKeyServiceEncryption` (may-2026). |
| **REF-08** | Roll or rotate a Customer Key or an availability key | `https://learn.microsoft.com/en-us/purview/customer-key-availability-key-roll` | Microsoft Learn | Microsoft Corporation | Métodos `-Refresh` y `-Replace`, rotación secuencial en SharePoint, tiempos de espera 24h/48h y prohibición de borrar claves antiguas (jun-2026). |
| **REF-09** | Set up Microsoft Purview Customer Key for Windows 365 Cloud PCs | `https://learn.microsoft.com/en-us/windows-365/enterprise/purview-customer-key` | Microsoft Learn | Microsoft Corporation | Configuración en Intune Admin Center (`Cloud PC encryption type`), reinicio automático y límite de 20.000 Cloud PCs por ejecución (mar-2026). |
| **REF-10** | Double Key Encryption (DKE) | `https://learn.microsoft.com/en-us/purview/double-key-encryption` | Microsoft Learn | Microsoft Corporation | Arquitectura de doble llave a nivel de ítem (~5 % de datos) e incompatibilidades con Copilot, eDiscovery, DLP web y coautoría (oct-2026). |
| **REF-11** | Learn about privileged access management (Microsoft Purview) | `https://learn.microsoft.com/en-us/purview/privileged-access-management` | Microsoft Learn | Microsoft Corporation | Arquitectura en el sustrato M365 y *Exchange Management runspace*, límite de 30 políticas y relación con Entra PIM y Lockbox (jun-2026). |
| **REF-12** | Get started with privileged access management | `https://learn.microsoft.com/en-us/purview/privileged-access-management-configuration` | Microsoft Learn | Microsoft Corporation | Paso a paso y cmdlets `Enable-ElevatedAccessControl`, `New-ElevatedAccessApprovalPolicy` y `New/Approve/Deny-ElevatedAccessRequest`. |
| **REF-13** | Microsoft Purview service description | `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description` | Microsoft Learn | Microsoft Corporation | Reglas contractuales exactas de licenciamiento para Customer Key (MDEP, EXO, SPO), Customer Lockbox y Microsoft Purview Suite (nov-2026). |
| **REF-14** | Microsoft Cloud Security Benchmark v2 — Privileged Access (`PA-8`) | `https://learn.microsoft.com/en-us/security/benchmark/azure/mcsb-v2-privileged-access` | Microsoft Learn | Microsoft Corporation | Control normativo oficial de Microsoft para gobernar el acceso de soporte del proveedor cloud mediante Customer Lockbox. |
| **REF-15** | Audit log activities in Microsoft Purview | `https://learn.microsoft.com/en-us/purview/audit-log-activities` | Microsoft Learn | Microsoft Corporation | Catálogo canónico de operaciones auditadas en el registro unificado de Microsoft Purview (actualizado nov-2026). |
| **REF-16** | Privileged Access Management in Office 365 — Deep Dive | `https://practical365.com/privileged-access-management-in-office-365/` | MVP Seguridad | Vasil Michev (M365 MVP) | Guía técnica independiente sobre grupos aprobadores *mail-enabled security*, tareas JEA/JIT y consideraciones prácticas de M365 PAM. |
| **REF-17** | What is Customer Lockbox in Microsoft 365, and how to use it? | `https://blog.sonnes.cloud/what-is-customer-lockbox-in-microsoft-365-and-how-to-use-it/` | MVP Seguridad | Michael Morten Sonne (Security MVP) | Revisión operativa del flujo de activación, aprobación y auditoría de Microsoft Purview Customer Lockbox. |
| **REF-18** | Protect and manage Microsoft 365 Copilot with Microsoft Purview | `https://joannecklein.com/category/microsoft-purview/` | MVP Seguridad | Joanne Klein (Purview MVP) | Prácticas recomendadas de gobierno de información, Customer Key, Customer Lockbox y retención en entornos Microsoft 365 Copilot. |
| **REF-19** | The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29) | `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` | Marco Normativo | National Institute of Standards and Technology (NIST) | Estándar rector para el mapeo de subcategorías `GV`, `ID`, `PR`, `DE`, `RS` y `RC` sobre soberanía, criptografía y acceso privilegiado. |

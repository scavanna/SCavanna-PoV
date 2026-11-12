# Guía Maestra de Excelencia Operacional: Microsoft Purview Audit (Standard vs. Premium, Forense Cloud y Retención de 10 Años)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
| :--- | :--- |
| **Identificador del Módulo** | `19_Purview_Audit_Premium` |
| **Slug Canónico** | `Purview_Audit_Premium` |
| **Nombre Completo** | Microsoft Purview Audit (Standard vs. Premium, Forense Cloud y Retención de 10 Años) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` `[Verificado MS Learn]` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (1 año por defecto; 10-Year Audit Log Retention como Add-on) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (`Solutions > Audit`), `https://security.microsoft.com`, `https://graph.microsoft.com/v1.0/security/auditLog/queries` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, DFIR / Incident Responder, Threat Hunter, Purview Compliance Admin, Exchange & Collaboration Admin, Legal / eDiscovery Lead, GRC / Internal Audit |
| **Marcos Normativos Alineados** | NIST CSF 2.0 (`GV, ID, PR, DE, RS, RC`), MITRE ATT&CK v18 (Cloud / M365) y MITRE ATLAS, CISA M-24-04 / SCuBA, SEC Rule 17a-4, HIPAA, PCI-DSS v4.0, DORA, ISO/IEC 27001:2022, Ley 21.719 (Chile) |

> **Nota de consolidación arquitectónica (Noviembre 2026):** Esta guía documenta con precisión forense la arquitectura vigente de **Microsoft Purview Audit** a corte `2026-11-11`, incorporando: (1) la ampliación de retención de **Audit (Standard)** de 90 a **180 días** (17-oct-2023) y la liberación en 2024 de los eventos `MailItemsAccessed`, `Send`, `SearchQueryInitiatedExchange` y `SearchQueryInitiatedSharePoint` hacia licencias Standard bajo la iniciativa **Secure Future Initiative (SFI) / CISA**; (2) el valor diferencial irremplazable de **Audit (Premium)** en Microsoft 365 E5 / **Microsoft Purview Suite** (**1 año de retención por defecto** para Entra ID, Exchange, OneDrive y SharePoint, hasta **50 políticas personalizadas**, retención de **10 años con add-on**, metadatos forenses enriquecidos como `SensitivityLabel` en `MailItemsAccessed` y `AppAccessContext` en Teams, y **doble ancho de banda dedicado** en Office 365 Management Activity API); (3) la auditoría nativa de **Microsoft 365 Copilot** (`CopilotInteraction`, `XPIADetected`, `JailbreakDetected`) y agentes autónomos de **Microsoft Agent 365** (GA mayo de 2026); y (4) el hito crítico de **`MC1505599` (octubre de 2026)**: disponibilidad general (GA) de la API **`AuditLogQuery` de Microsoft Graph** (`security/auditLog/queries`, hasta 1 millón de registros por consulta) y **retiro definitivo del cmdlet `Search-UnifiedAuditLog` el 15 de octubre de 2027** `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

En cualquier investigación de intrusión moderna —desde compromisos de correo empresarial (**BEC**) y robo de tokens de sesión (*AiTM*) hasta campañas de espionaje de actores de nación-estado (*Midnight Blizzard / Nobelium*, *Storm-0558*)—, la diferencia entre una notificación regulatoria masiva de brecha de datos y una contención quirúrgica demostrable reside en la completitud, profundidad y retención del **Unified Audit Log (UAL)** de **Microsoft Purview Audit** `[Verificado MS Learn]`. Sin registros granulares de acceso a elementos (`MailItemsAccessed`) y consultas de búsqueda del atacante (`SearchQueryInitiatedExchange` / `SearchQueryInitiatedSharePoint`), el equipo DFIR está obligado legalmente bajo marcos como HIPAA, GDPR o SEC a asumir el peor escenario: que **el 100 % de los datos del buzón o sitio fueron exfiltrados** `[Verificado MS Learn]`.

Dentro de una arquitectura **Zero Trust** basada en Microsoft 365 E5, **Purview Audit (Premium)** constituye la fuente de verdad probatoria (*System of Record*) para más de un centenar de tipos de registro (`AuditLogRecordType`), alimentando en paralelo búsquedas forenses asíncronas de largo plazo (1 a 10 años en Purview) y detección en tiempo cuasi-real en **Microsoft Sentinel** (`OfficeActivity`, ingesta gratuita) y **Microsoft Defender XDR** (`CloudAppEvents`) `[Verificado MS Learn]`.

### 2.1 Comparativa Forense Exhaustiva: Audit (Standard) vs. Audit (Premium) vs. 10-Year Add-on

| Capacidad Técnica / Forense | Audit (Standard) (M365 E3 / Business) | Audit (Premium) (M365 E5 / Purview Suite) | Add-on 10-Year Audit Log Retention | Estado y Verificación |
| :--- | :--- | :--- | :--- | :--- |
| **Activación por defecto del pipeline UAL** | Sí (`UnifiedAuditLogIngestionEnabled = True`) | Sí + requiere activar el plan de servicio **Microsoft 365 Advanced Auditing** por usuario | Requiere licencia base E5 / Audit (Premium) + licencia add-on por usuario | GA `[Verificado MS Learn]` |
| **Retención predeterminada de registros** | **180 días** para todas las cargas (ampliado desde 90 días el 17-oct-2023) | **1 año (365 días)** por defecto para `AzureActiveDirectory`, `Exchange`, `OneDrive` y `SharePoint`; **180 días** para el resto de cargas | Hasta **10 años** mediante política personalizada explícita (no retroactiva a eventos previos) | GA `[Verificado MS Learn]` |
| **Políticas personalizadas de retención de auditoría** | No soportado | Sí, hasta **50 políticas** por tenant (`7d, 30d, 6m, 9m, 1y`) por servicio, operación o usuario con prioridad `1` a `10000` | Habilita duraciones de **3, 5, 7 y 10 años** en políticas personalizadas para usuarios con el add-on | GA `[Verificado MS Learn]` |
| **Retención de entidades no humanas (Service Principals, Apps, Sistema)** | 180 días | Período fijo no configurable de **1 año** | **Fijo en 1 año** (las políticas personalizadas de 10 años **no aplican** a entidades no-usuario) | GA `[Verificado MS Learn]` |
| **Eventos `MailItemsAccessed`, `Send`, `SearchQueryInitiatedExchange/SPO`** | **Sí** (expandidos a Standard entre feb–jun 2024 vía Roadmap 380690 / SFI, sin metadatos Premium) | **Sí**, con retención de 1 año por defecto y propiedades forenses enriquecidas (*Intelligent Insights*) | Retenidos hasta 10 años bajo política personalizada | GA `[Verificado MS Learn]` |
| **Intelligent Insights (Propiedades Forenses Exclusivas)** | No incluido | **`SensitivityLabel`** en `MailItemsAccessed`; **`AppAccessContext`**, `ParticipantInfo`, `ParticipatingDomainInformation`, `IsJoinedFromLobby` y `ArtifactShared` en 14 operaciones de **Microsoft Teams** | Retenidos según política aplicable al usuario E5 + add-on | GA `[Verificado MS Learn]` |
| **Auditoría de Copilot y Agentes (`CopilotInteraction`, Agent 365)** | Incluida sin costo adicional para apps IA de Microsoft y Agent 365 (180 días); **Pay-As-You-Go** para apps IA no-Microsoft (`AIAppInteraction`, 180 días) | Retenida hasta **1 año** mediante política personalizada para cargas Microsoft elegibles | Retenible hasta **10 años** para actividades generadas por usuarios licenciados | GA `[Verificado MS Learn]` |
| **Ancho de banda en Office 365 Management Activity API (SIEM)** | Línea base inicial de `2.000 req/min` escalada dinámicamente nivel estándar | Cuota dedicada a nivel de tenant con **~2x el ancho de banda dinámico** respecto a organizaciones no-E5 | Igual que Audit (Premium) | GA `[Verificado MS Learn]` |
| **Búsqueda asíncrona Portal y API Microsoft Graph `AuditLogQuery`** | Soportado (hasta 10 trabajos concurrentes/admin, exportación Graph hasta 1M registros) | Soportado sobre toda la ventana histórica retenida (1 año en bloques de consulta de hasta 180 días) | Soportado sobre hasta 10 años (consultando rangos de hasta 180 días por trabajo) | GA (oct-2026) `[Verificado MS Learn]` |

### 2.2 Licenciamiento Elegible y Prerrequisitos Críticos

**Licencias que otorgan derechos de Microsoft Purview Audit (Premium) `[Verificado MS Learn]`:**
- Microsoft 365 E5 / E7 / A5 / G5 o Office 365 E5 / A5 / G5.
- **Microsoft Purview Suite** (denominación vigente desde el 1 de octubre de 2025 para *Microsoft 365 E5 Compliance*) o Microsoft 365 F5 Compliance / F5 Security + Compliance.
- Add-on independiente **Microsoft 365 E5 eDiscovery and Audit**.
- Para retención superior a 1 año (`3, 5, 7 o 10 años`): **Microsoft 365 10-Year Audit Log Retention** add-on asignado a cada usuario generador del evento además de su licencia E5/Purview Suite.
- Para auditoría de interacciones de usuarios con aplicaciones GenAI **no-Microsoft** (`AIAppInteraction` / carga `AIApp`): suscripción de Azure asociada a **Microsoft Purview Pay-As-You-Go** (cobro por número de registros de auditoría ingeridos, con retención fija de 180 días) `[Verificado MS Learn]`.

**Prerrequisitos técnicos de activación verificados `[Verificado MS Learn]`:**
1. Confirmar `UnifiedAuditLogIngestionEnabled = True` ejecutando `Get-AdminAuditLogConfig` **exclusivamente desde Exchange Online PowerShell** (en Security & Compliance PowerShell la propiedad devuelve siempre `False` aunque la auditoría esté activa).
2. Confirmar que el plan de aplicación **Microsoft 365 Advanced Auditing** esté marcado en la licencia de cada usuario E5 (comienza a emitir *Intelligent Insights* en un plazo de hasta 24 horas).
3. Habilitar explícitamente **`SearchQueryInitiated`** en los buzones Exchange Online (`Set-Mailbox -AuditOwner @{Add="SearchQueryInitiated"}`), dado que **`SearchQueryInitiatedSharePoint` viene habilitado por defecto pero `SearchQueryInitiatedExchange` NO viene activo de fábrica**.
4. Habilitar la auditoría en el portal de administración de **Microsoft Fabric / Power BI** para que los eventos `PowerBIAudit` fluyan al registro unificado.

### 2.3 Principios Rectores de Excelencia Operacional

1. **Presunción de Compromiso Acotada por Evidencia Determinista (`[Verificado MS Learn]`):** Utilizar `MailItemsAccessed` (`Bind` vs. `Sync`), `SensitivityLabel` y `SearchQueryInitiated` para delimitar matemáticamente qué elementos y etiquetas de sensibilidad fueron expuestos durante un incidente BEC, evitando tanto sub-notificaciones ilegales como sobre-notificaciones catastróficas.
2. **Inmutabilidad en el Momento de Ingesta (*Pipeline-Time Lifetime Assignment*) (`[Verificado MS Learn]`):** Diseñar y desplegar licencias Audit (Premium), el plan *Advanced Auditing* y las políticas de retención de 1 a 10 años **antes** de que ocurra el incidente, pues el tiempo de vida del registro se sella al ingresar al pipeline y ningún cambio posterior de licencia o política actúa retroactivamente sobre logs previos.
3. **Arquitectura Dual: Retención Probatoria en Purview + Detección Tiempo Real en SIEM (`[Verificado MS Learn]`):** No usar búsquedas manuales de Purview como motor de alertamiento en vivo (latencia típica de 60 a 90 minutos en cargas centrales); transmitir continuamente vía Office 365 Management Activity API hacia **Microsoft Sentinel** (`OfficeActivity`) y reservar Purview Audit (1 a 10 años) como bóveda forense de cumplimiento e investigación histórica.
4. **Migración Proactiva a Búsqueda Asíncrona y Microsoft Graph `AuditLogQuery` (`MC1505599`) (`[Verificado MS Learn]`):** Erradicar toda dependencia operativa del cmdlet síncrono `Search-UnifiedAuditLog` antes de su retiro inapelable el **15 de octubre de 2027**, estandarizando la automatización DFIR sobre `POST /v1.0/security/auditLog/queries` con permisos granulares por carga (`AuditLogsQuery-<Workload>.Read.All`) y soporte de hasta 1 millón de eventos por consulta.
5. **Vigilancia Continua contra Evasión Forense (*Anti-Tampering & Anti-Throttling*) (`[Verificado MS Learn]`):** Auditar diariamente cualquier cambio en `UnifiedAuditLogIngestionEnabled`, `AuditDisabled`, `MailboxAuditBypassAssociation`, pérdida de `DefaultAuditSet` o activación de estrangulamiento `IsThrottled = True` (> 1.000 `MailItemsAccessed` en 24 h), tratando cada uno como alerta de alta severidad SOC.
6. **Observabilidad Completa sobre IA Generativa y Agentes Autónomos (`[Verificado MS Learn]`):** Auditar sistemáticamente operaciones `CopilotInteraction`, `ConnectedAIAppInteraction`, `AIAppInteraction` y actividades de **Microsoft Agent 365** (humano-a-agente, agente-a-humano, agente-a-herramienta y agente-a-agente), rastreando `AccessedResources`, `SensitivityLabelId`, `JailbreakDetected` y `XPIADetected`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Pipeline de Auditoría Unificada, Latencias y Reglas de Retención

Cuando un usuario, administrador, agente de IA o principal de servicio ejecuta una operación auditada en docenas de servicios de Microsoft 365, el evento ingresa al pipeline de **Microsoft Purview Audit**:
- **Disponibilidad típica de búsqueda (`[Verificado MS Learn]`):** Para servicios centrales (**Exchange Online, SharePoint Online, OneDrive y Microsoft Teams**), los registros suelen estar disponibles entre **60 y 90 minutos** después del evento (aunque Microsoft no establece un SLA contractual rígido ante contingencias de infraestructura).
- **Asignación del tiempo de expiración (`[Verificado MS Learn]`):** En el instante en que el pipeline indexa el evento, calcula su fecha de expiración evaluando: (1) las políticas personalizadas de retención activas ordenadas por **Priority** (`1` = máxima prioridad a `10000` = mínima prioridad); y (2) si ninguna política personalizada coincide, la política predeterminada según la licencia del usuario que generó el evento.
- **Advertencia crítica sobre precedencia de políticas personalizadas (`[Verificado MS Learn]`):** Toda política personalizada creada por la organización **prevalece sobre la política predeterminada de 1 año**. Si un administrador crea por error una política personalizada para `Exchange` con duración de `30 Days` o `6 Months`, reducirá la retención por debajo del año predeterminado de E5. Asimismo, si crea políticas mediante `New-UnifiedAuditLogRetentionPolicy` con `RecordTypes` u `Operations` no expuestos en la interfaz web, dichas políticas solo podrán editarse desde PowerShell (`Set-UnifiedAuditLogRetentionPolicy`) `[Verificado MS Learn]`.

### 3.2 Componentes Técnicos y Motores Clave

| Componente / Motor | Función Operativa Detallada | Ruta / Interfaz Oficial | Integraciones Clave |
| :--- | :--- | :--- | :--- |
| **Unified Audit Log (UAL) Pipeline** | Captura centralizada de miles de operaciones de usuario, administrador y agentes a través de más de 150 `AuditLogRecordType` con esquema común indexado y carga JSON específica en `AuditData`. | `purview.microsoft.com > Solutions > Audit` | Microsoft Entra ID, Exchange, SharePoint, OneDrive, Teams, Copilot, Fabric, Defender, Purview `[Verificado MS Learn]` |
| **Motor de Búsqueda Asíncrona en Portal Purview (New Search)** | Trabajos de búsqueda en segundo plano (sin mantener navegador abierto), retenidos **30 días**, hasta **10 trabajos simultáneos por cuenta admin** (máx. **1 sin filtros**), ventana máxima de **180 días por consulta** y exportación CSV. *(Classic Search retirado el 30-nov-2023)*. | `purview.microsoft.com > Solutions > Audit > Search` | Administrative Units, Excel Power Query (expansión de JSON `AuditData`) `[Verificado MS Learn]` |
| **Microsoft Graph `AuditLogQuery` API (GA Octubre 2026)** | Interfaz programática estratégica (`v1.0`) que reemplaza a `Search-UnifiedAuditLog` (retiro 15-oct-2027), con soporte de hasta **1 millón de registros por consulta**, bandera `isRecordCountLimitExceeded`, filtro libre `keywordFilter` sobre `auditData` no indexado y permisos RBAC por carga de trabajo. | `https://graph.microsoft.com/v1.0/security/auditLog/queries` (`Microsoft.Graph.Security`) | Playbooks SOAR (Azure Logic Apps), scripts DFIR Python/PowerShell, aplicaciones GRC `[Verificado MS Learn]` |
| **Motor de Políticas de Retención de Auditoría (1 a 10 Años)** | Política predeterminada inmutable de 1 año (`AzureActiveDirectory, Exchange, OneDrive, SharePoint`) más hasta **50 políticas personalizadas** (`7d` a `10y`) por carga, operación o usuario con prioridad numérica `1–10000`. | `purview.microsoft.com > Solutions > Audit > Audit retention policies` | Licenciamiento M365 E5 / Purview Suite y 10-Year Audit Log Retention add-on `[Verificado MS Learn]` |
| **Exchange Online Mailbox Auditing (`DefaultAuditSet`)** | Auditoría activada por defecto a nivel organizacional (`AuditDisabled = False`) clasificando acciones por `Owner`, `Delegate` y `Admin` sobre buzones de usuario, compartidos y Grupos M365, incluyendo `MailItemsAccessed`, `Send`, `AttachmentAccess`, `UpdateInboxRules` y `HardDelete`. | Exchange Online PowerShell (`Get-OrganizationConfig`, `Get-Mailbox`, `Set-Mailbox`) | Microsoft Defender for Office 365, Purview eDiscovery `[Verificado MS Learn]` |
| **Audit (Premium) Intelligent Insights** | Generación de telemetría forense exclusiva para usuarios con plan *Microsoft 365 Advanced Auditing*: etiqueta `SensitivityLabel` en `MailItemsAccessed` y contexto de acceso de aplicaciones (`AppAccessContext`), participantes externos y lobby en 14 eventos de Microsoft Teams. | `AuditData` JSON en Purview Audit / Graph / Management Activity API | Purview Information Protection (MIP), Microsoft Teams, Defender for Cloud Apps `[Verificado MS Learn]` |
| **Auditoría de IA Generativa y Agentes (`Copilot` & `Agent 365`)** | Registro automático de `CopilotInteraction`, `ConnectedAIAppInteraction`, `AIAppInteraction` (PAYG) y actividades de instancias **Microsoft Agent 365** (humano-agente, agente-herramienta, agente-agente), capturando `AccessedResources`, `SensitivityLabelId`, `JailbreakDetected`, `XPIADetected` y `DLPEvaluationDeferred`. | `purview.microsoft.com > Solutions > Audit` y `DSPM > Activity explorer` | Microsoft 365 Copilot, Copilot Studio, Microsoft Agent 365, Security Copilot, Fabric `[Verificado MS Learn]` |
| **Office 365 Management Activity API (Alta Velocidad)** | Streaming REST continuo hacia SIEM con cuota dedicada por tenant (~2x ancho de banda dinámico sobre la base de 2.000 req/min para organizaciones E5/A5/G5), superando el límite de 1 año fijo de entidades no-usuario mediante archivo externo en Data Lake. | `https://manage.office.com/api/v1.0/{tenant_id}/activity/feed` | **Microsoft Sentinel** (`OfficeActivity` Analytics + Data Lake 12 años), Defender XDR `[Verificado MS Learn]` |

### 3.3 Anatomía Forense Profunda de Eventos Críticos para Respuesta a Incidentes (BEC, Nación-Estado e IA)

#### A. `MailItemsAccessed`: Diferenciación `Bind` vs. `Sync`, Deduplicación y Mitigación de *Throttling* (> 1.000 eventos / 24 h)
`MailItemsAccessed` audita el acceso real a datos de correo en todos los protocolos (**POP, IMAP, MAPI, EWS, Exchange ActiveSync y REST/Graph**) incluso cuando el atacante no marca el mensaje como leído `[Verificado MS Learn]`:
- **Operación `Bind` (`MailAccessType = Bind`):** Acceso individual a mensajes específicos (ej. abrir correo en OWA, lectura selectiva vía Graph/REST o vista previa). Agrega todos los accesos ocurridos en intervalos de **2 minutos** dentro de un solo registro (propiedad `OperationCount`) listando el **`InternetMessageId`** exacto de cada correo en la colección `Folders`, y en **Audit (Premium)** adjunta el **`SensitivityLabel`** de cada ítem `[Verificado MS Learn]`. Para reducir ruido, Exchange deduplica accesos `Bind` repetidos al mismo mensaje dentro de ventanas de **1 hora** (salvo que cambie `ClientIPAddress`, `ClientInfoString`, `ParentFolder`, `Logon_type`, `MailAccessType`, `MailboxUPN`, `User` o `SessionId`) `[Verificado MS Learn]`.
- **Operación `Sync` (`MailAccessType = Sync`):** Registrada cuando clientes de escritorio Outlook (Windows/Mac) sincronizan carpetas completas hacia almacenamiento local (con deduplicación horaria). Registra la carpeta sincronizada en lugar de cada correo leído offline; **regla forense obligatoria:** si un evento `Sync` ocurre bajo la misma `ClientIPAddress`, `ClientInfoString` o `SessionId` atribuida al atacante, el equipo DFIR debe declarar **comprometida la totalidad de los correos contenidos en las carpetas sincronizadas** `[Verificado MS Learn]`.
- **Estrangulamiento Crítico (`IsThrottled = True` al superar 1.000 registros en 24 h):** Si un buzón genera **más de 1.000 registros de auditoría `MailItemsAccessed` en menos de 24 horas** (patrón típico de exfiltración automatizada masiva vía EWS/Graph por actores como *Midnight Blizzard / Nobelium* o scripts BEC), Exchange Online detiene la generación de nuevos registros `MailItemsAccessed` para ese buzón durante **24 horas**, marcando `IsThrottled = True` en `OperationProperties`, y reanuda automáticamente el registro tras cumplirse las 24 horas `[Verificado MS Learn]`. Operativamente, detectar `IsThrottled = True` exige: (1) disparar alerta crítica de exfiltración en Sentinel/Defender XDR; (2) revocar sesiones de inmediato (`Revoke-MgUserSignInSession`); y (3) asumir compromiso total del buzón durante la ventana estrangulada `[Decisión / Propuesta Editorial]`.

#### B. `SearchQueryInitiatedExchange` y `SearchQueryInitiatedSharePoint`: Reconstrucción de la Intención del Atacante
Una vez dentro de una cuenta comprometida, el adversario casi invariablemente utiliza la barra de búsqueda de Outlook/OWA o SharePoint/OneDrive para localizar credenciales, transferencias bancarias, contratos M&A o secretos criptográficos `[Verificado MS Learn]`:
- **`SearchQueryInitiatedSharePoint`** (configurado como `SharepointSearchQueryInitiated`): **Habilitado por defecto**; captura el texto exacto buscado por el usuario en SharePoint Online y OneDrive `[Verificado MS Learn]`.
- **`SearchQueryInitiatedExchange`** (acción de buzón `SearchQueryInitiated`): **Deshabilitado por defecto**; debe habilitarse explícitamente por buzón mediante `Set-Mailbox <Identity> -AuditOwner @{Add="SearchQueryInitiated"}` ejecutado en el **bosque regional (Multi-Geo forest)** donde reside el buzón `[Verificado MS Learn]`.
- **Implicación operativa crítica de `DefaultAuditSet` (`[Verificado MS Learn]`):** Al personalizar `AuditOwner` con `@{Add="SearchQueryInitiated"}`, Exchange Online retira el valor `Owner` de la propiedad `DefaultAuditSet` de ese buzón, lo que significa que futuras acciones nuevas lanzadas por Microsoft para `Owner` no se agregarán solas a menos que el equipo de plataforma ejecute gobernanza periódica sobre la lista `AuditOwner` `[Verificado MS Learn]`.

#### C. `CopilotInteraction`, `XPIADetected`, `JailbreakDetected` y `Microsoft Agent 365`
Para investigaciones de seguridad de IA en 2026, Purview Audit registra automáticamente sin pasos adicionales `[Verificado MS Learn]`:
- **Tipos de registro e identidad de aplicación:** `CopilotInteraction` (`Workload = Copilot` para M365 Copilot, Cowork, Security Copilot, Fabric Copilot, Copilot Studio y Foundry), `ConnectedAIAppInteraction` (`Workload = ConnectedAIApp` para apps IA empresariales en Entra/Azure AI) y `AIAppInteraction` (`Workload = AIApp` vía DLP de red/navegador bajo Pay-As-You-Go) `[Verificado MS Learn]`.
- **Trazabilidad forense de recursos e inyecciones:** El arreglo **`AccessedResources`** detalla cada archivo, correo o sitio leído/modificado por Copilot para construir la respuesta (`ID`, `Name`, `SiteUrl`, **`SensitivityLabelId`**, `Action`, `PolicyDetails`, `Status`) e incluye el booleano **`XPIADetected`** (*Cross-Prompt Injection Attack* detectado desde un documento o correo malicioso leído por la IA), mientras que **`Messages`** incluye **`JailbreakDetected`** sobre el prompt del usuario, y **`DLPEvaluationDeferred`** (`1=Prompt, 2=Response, 4=Grounding, 8=WebGrounding`) documenta evaluaciones DLP diferidas `[Verificado MS Learn]`.
- **Agentes autónomos (`AgentId`, `AgentName`, `AgentVersion` y Agent 365):** Toda instancia creada en **Microsoft Agent 365** nace con auditoría habilitada de fábrica cubriendo interacciones **humano-a-agente, agente-a-humano, agente-a-herramientas y agente-a-agente** `[Verificado MS Learn]`.

### 3.4 Catálogo Completo de Propiedades Exclusivas de Audit (Premium) y Esquema Forense IA

| Carga de Trabajo | Actividad / Operación Auditada | Propiedades Forenses Clave en `AuditData` | Disponibilidad por Licencia |
| :--- | :--- | :--- | :--- |
| **Exchange Online** | `MailItemsAccessed` (`Bind` y `Sync`) | `SensitivityLabel` (GUID de etiqueta MIP del correo accedido), `InternetMessageId`, `MailAccessType`, `SessionId`, `ClientInfoString`, `ClientIPAddress`, `OperationCount`, `IsThrottled` | Evento base en Standard/Premium; **`SensitivityLabel` exclusivo de Audit (Premium)** `[Verificado MS Learn]` |
| **Exchange Online** | `AttachmentAccess`, `Send`, `SendAs`, `SendOnBehalf`, `UpdateInboxRules`, `HardDelete` | Identificadores de adjunto vía Graph, remitente real vs. suplantado, parámetros de reglas de ocultamiento/reenvío y purga de *Recoverable Items* | Standard (180 d) / **Premium (1 año por defecto, hasta 10 años con add-on)** `[Verificado MS Learn]` |
| **Exchange & SharePoint** | `SearchQueryInitiatedExchange`, `SearchQueryInitiatedSharePoint` | `QueryText` / términos literales buscados, alcances consultados, `ClientInfoString`, `ClientIPAddress` | Standard (180 d) / **Premium (1 año por defecto)**; *Exchange requiere activación explícita por buzón* `[Verificado MS Learn]` |
| **Microsoft Teams** | `MessageSent`, `MessageUpdated` | **`AppAccessContext`**, **`ParticipantInfo`**, **`ParticipatingDomainInformation`** (dominios federados/externos involucrados) | **Propiedades exclusivas de Audit (Premium)** `[Verificado MS Learn]` |
| **Microsoft Teams** | `MeetingParticipantDetail` | **`IsJoinedFromLobby`**, **`ArtifactShared`** (archivos/pantallas compartidas en la reunión) | **Propiedades exclusivas de Audit (Premium)** `[Verificado MS Learn]` |
| **Microsoft Teams** | `ChatCreated`, `ChatRetrieved`, `ChatUpdated`, `MessageRead`, `MessagesListed`, `MessageHostedContentRead`, `MessageHostedContentsListed`, `MessageCreatedNotification`, `MessageUpdatedNotification`, `MessageDeletedNotification`, `SubscribedToMessages` | **`AppAccessContext`** (identifica qué aplicación OAuth/Graph leyó o se suscribió vía webhook a mensajes y contenidos alojados de Teams) | **Propiedades exclusivas de Audit (Premium)** `[Verificado MS Learn]` |
| **Copilot & IA Microsoft** | `CopilotInteraction` (`Workload = Copilot`) | `AccessedResources` (`ID, SiteUrl, Name, Type, Action, Status, PolicyDetails`, **`SensitivityLabelId`**, **`XPIADetected`**), `Messages` (`ID, IsPrompt`, **`JailbreakDetected`**), `AgentId`, `AgentName`, `AgentVersion`, `AISystemPlugin`, `AppHost`, `AppIdentity`, `ModelTransparencyDetails`, `DLPEvaluationDeferred` | Incluido en Standard (180 d); **retenible 1 a 10 años con políticas personalizadas Audit (Premium)** `[Verificado MS Learn]` |
| **Apps IA Conectadas y Externas** | `ConnectedAIAppInteraction` (`ConnectedAIApp`), `AIAppInteraction` (`AIApp`) | Mismo esquema común de recursos, host y detección de riesgos para apps registradas en Entra/Azure AI o detectadas en navegador/red | Requiere **Microsoft Purview Pay-As-You-Go** (retención fija de **180 días**, cobro por registro ingerido) `[Verificado MS Learn]` |

### 3.5 Comparativa Arquitectónica de Interfaces de Consulta y Extracción (Transición `MC1505599` 2026–2027)

| Interfaz / API | Caso de Uso Primario | Límites Operativos Verificados | Comportamiento de Búsqueda por Palabra Clave | Estado a Noviembre 2026 |
| :--- | :--- | :--- | :--- | :--- |
| **Portal Purview Audit Search (`New Search`)** | Investigaciones interactivas humanas por analistas DFIR, Legal y GRC. | Máx. **10 trabajos concurrentes** por cuenta admin (máx. **1 sin filtros**); rango máx. **180 días por trabajo**; trabajos retenidos **30 días**; cuenta aproximada > 100.000 resultados. | **Keyword Search** busca **únicamente en propiedades indexadas** del esquema común (no dentro del JSON crudo de `AuditData`) `[Verificado MS Learn]`. | **GA — Activo** (*Classic Search retirado el 30-nov-2023*) `[Verificado MS Learn]` |
| **Microsoft Graph `AuditLogQuery` API (`v1.0/security/auditLog/queries`)** | Automatización forense DFIR, playbooks SOAR, extracciones probatorias masivas y scripts PowerShell/Python. | Exporta hasta **1.000.000 de registros por consulta**; expone booleano autoritativo **`isRecordCountLimitExceeded`**; permisos granulares por servicio (`AuditLogsQuery-<Workload>.Read.All`). | **`keywordFilter`** busca texto libre **en el contenido no indexado de `auditData`** (incluyendo `AppAccessContext`); para campos indexados usar `operationFilters`, `userPrincipalNameFilters`, etc. `[Verificado MS Learn]`. | **GA desde octubre de 2026 (`MC1505599`) — Vía recomendada** `[Verificado MS Learn]` |
| **Office 365 Management Activity API** | Ingesta continua y permanente en tiempo cuasi-real hacia SIEM (**Microsoft Sentinel**) y archivo Data Lake. | Línea base inicial de **2.000 req/min** por tenant; escalado dinámico con **~2x ancho de banda** en tenants E5/A5/G5 con Audit (Premium). Retiene sus propios feeds hasta 7 días en tránsito para recolección continua. | Entrega el payload JSON íntegro hacia Log Analytics (`OfficeActivity`) permitiendo KQL libre sobre todo el evento `[Verificado MS Learn]`. | **GA — Estándar para ingesta SIEM continua** `[Verificado MS Learn]` |
| **Cmdlet `Search-UnifiedAuditLog` (Exchange Online PowerShell)** | Scripts heredados síncronos creados antes de octubre de 2026. | Limitaciones severas de escalabilidad, timeouts de sesión y paginación en grandes volúmenes (`SessionCommand ReturnLargeSet` <= 50.000). | No recibirá nuevas mejoras funcionales `[Verificado MS Learn]`. | **Deprecado — Retiro definitivo el 15 de octubre de 2027 (`MC1505599`)** `[Verificado MS Learn]` |

### 3.6 Integraciones Transversales con el Ecosistema de Seguridad y Gobierno Microsoft

1. **Microsoft Sentinel (`OfficeActivity` + Data Lake de 12 Años):** Ingesta gratuita de eventos de Exchange, SharePoint y Teams en el *Analytics tier* de Sentinel para correlación NRT/Scheduled con UEBA, y retención económica de hasta 12 años en **Sentinel Data Lake** (cubriendo especialmente logs de *service principals* y aplicaciones más allá del límite fijo de 1 año en Purview Audit) `[Verificado MS Learn]`.
2. **Microsoft Defender XDR (`CloudAppEvents`):** Proyecta eventos de UAL e *Intelligent Insights* durante 30 días en *Advanced Hunting*, permitiendo correlacionar en una sola consulta KQL telemetría de endpoint (`DeviceEvents`), identidad (`IdentityLogonEvents`) y correo (`MailItemsAccessed` / `IsThrottled`) `[Verificado MS Learn]`.
3. **Microsoft Purview Insider Risk Management y Communication Compliance:** Consume señales de auditoría de descarga, compartición, impresión, uso de IA y auditoría de privilegios de revisores (`SupervisoryReviewTag`, `SupervisionPolicyUpdated`) `[Verificado MS Learn]`.
4. **Microsoft Purview eDiscovery (Standard y Premium) y DSPM:** Mientras Purview Audit demuestra *quién accedió a qué recurso y cuándo* (`AccessedResources`, `InternetMessageId`), **eDiscovery** recupera el *contenido literal* de los correos, documentos o conversaciones `Copilot activity`, y **DSPM > Activity explorer** visualiza gráficamente las interacciones de usuarios y agentes de **Agent 365** `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

El acceso al registro de auditoría unificado expone metadatos altamente sensibles de toda la organización (términos buscados por ejecutivos, asuntos de correos, rutas de archivos confidenciales, prompts de IA y direcciones IP), por lo que debe gobernarse bajo **mínimo privilegio estricto, segmentación por cargas de trabajo en Microsoft Graph y unidades administrativas** `[Verificado MS Learn]`.

### 4.1 Matriz Oficial de Roles RBAC en Purview, Exchange y Microsoft Graph

| Rol / Permiso Oficial | Plano de Control | Permisos Clave Otorgados | Restricciones y Segregación | Estrategia PIM / JIT Recomendada |
| :--- | :--- | :--- | :--- | :--- |
| **Audit Reader** (asigna rol *View-Only Audit Logs*) | Purview Role Group (`purview.microsoft.com > Settings > Roles and scopes > Role groups`) | Ejecutar búsquedas asíncronas en el portal de Purview Audit, ver trabajos completados y exportar resultados a CSV (soportando acotamiento por **Administrative Units**). | **No puede** habilitar/deshabilitar la ingesta UAL ni crear o modificar políticas de retención de auditoría `[Verificado MS Learn]`. | Rol estándar para analistas DFIR, SOC L2, Threat Hunters y Auditoría Interna mediante membresía con vencimiento o activación JIT de 8 h `[Decisión / Propuesta Editorial]`. |
| **Audit Manager** (asigna roles *View-Only Audit Logs* + *Audit Logs*) | Purview Role Group + Exchange Admin Center | Buscar y exportar el registro de auditoría **y** gestionar configuraciones globales de auditoría del tenant (como habilitar/deshabilitar la ingesta UAL en EAC/EXO). | **No otorga por sí solo** permisos para crear políticas de retención de auditoría si carece de *Organization Configuration* `[Verificado MS Learn]`. | Restringido a <= 3 ingenieros sénior de Plataforma Purview en modo elegible **Entra PIM for Groups** (máx. 4 h JIT, aprobación y MFA FIDO2) `[Decisión / Propuesta Editorial]`. |
| **Organization Configuration** | Purview Role Group / Rol RBAC | Crear, editar y eliminar **Audit log retention policies** (hasta 50 políticas personalizadas de 7 días a 10 años) en el portal de Purview o Security & Compliance PowerShell. | Separado de los roles de búsqueda operativa diaria para evitar que un investigador reduzca maliciosamente la retención `[Verificado MS Learn]`. | Exclusivo para arquitectura de gobierno Purview bajo cambio controlado (CAB) y activación JIT de 2 h `[Decisión / Propuesta Editorial]`. |
| **Exchange Administrator** (con *Audit Logs* en EAC) | Microsoft Entra ID / Exchange Online RBAC | Verificar `UnifiedAuditLogIngestionEnabled`, gestionar `AuditDisabled`, `Set-Mailbox -AuditOwner` (`SearchQueryInitiated`), `DefaultAuditSet` y auditar `MailboxAuditBypassAssociation`. | No requiere acceso de lectura al contenido de buzones ni casos legales `[Verificado MS Learn]`. | Elegible en **Microsoft Entra PIM** (máx. 4 h JIT con MFA resistente a phishing) `[Decisión / Propuesta Editorial]`. |
| **Permisos Granulares Graph `AuditLogsQuery-<Workload>.Read.All`** | Microsoft Graph API v1.0 (Delegated & Application) | Consulta programática de mínimo privilegio limitada a una sola carga: `AuditLogsQuery-Entra.Read.All`, `AuditLogsQuery-Exchange.Read.All`, `AuditLogsQuery-SharePoint.Read.All`, `AuditLogsQuery-OneDrive.Read.All`, `AuditLogsQuery-Endpoint.Read.All`, `AuditLogsQuery-CRM.Read.All`. | Impide que un script o conector de un equipo específico lea eventos de otras cargas de trabajo no autorizadas `[Verificado MS Learn]`. | Preferir siempre estos permisos granulares sobre `AuditLogsQuery.Read.All` en automatizaciones SOAR y scripts departamentales `[Decisión / Propuesta Editorial]`. |
| **Permiso Global Graph `AuditLogsQuery.Read.All`** | Microsoft Graph API v1.0 (Delegated & Application) | Crear trabajos `POST /security/auditLog/queries`, consultar estado y descargar hasta 1 millón de registros por consulta a través de todas las cargas de Microsoft 365. | Alto privilegio de lectura transversal; prohibido asignar secretos de cliente de larga duración sin rotación o Managed Identity / certificados `[Decisión / Propuesta Editorial]`. | Reservado para la identidad administrada / certificado del motor central DFIR del SOC `[Decisión / Propuesta Editorial]`. |
| **Permiso `ActivityFeed.Read` / `ActivityFeed.ReadDlp`** | Office 365 Management Activity API | Suscripción continua de alto ancho de banda (cuota dedicada E5) para ingesta SIEM de eventos generales y eventos DLP hacia Microsoft Sentinel (`OfficeActivity`). | Exclusivo para conectores nativos SIEM; no utilizar para consultas interactivas humanas ad-hoc `[Verificado MS Learn]`. | Gobernado mediante conector administrado de Microsoft Sentinel en el portal Defender `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

### D-01: Verificación Diaria de Integridad del Pipeline de Auditoría y Detección Anti-Tampering
- **Objetivo:** Confirmar que la ingesta global de Purview Audit y la auditoría de buzones por defecto permanecen intactas y que ningún actor haya intentado deshabilitarlas o añadir cuentas en bypass `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-AdminAuditLogConfig`, `Get-OrganizationConfig`, `Get-MailboxAuditBypassAssociation`) y `security.microsoft.com > Incidents & alerts` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Purview Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar diariamente mediante automatización en Exchange Online PowerShell que `UnifiedAuditLogIngestionEnabled` sea `True` y que `AuditDisabled` en `Get-OrganizationConfig` sea `False`.
  2. Auditar en tiempo real en Microsoft Sentinel (`OfficeActivity`) cualquier aparición de operaciones críticas de manipulación: `Set-AdminAuditLogConfig`, `Set-OrganizationConfig` (cambio en `AuditDisabled`), `Set-MailboxAuditBypassAssociation`, `Remove-UnifiedAuditLogRetentionPolicy` o `Set-UnifiedAuditLogRetentionPolicy`.
  3. Confirmar que el número de cuentas con `AuditBypassEnabled = True` sea exactamente `0` (o coincida estrictamente con cuentas de servicio documentadas y aprobadas por el CISO).
- **Evidencia Auditable:** Registro diario automatizado de estado saludable del pipeline y cero alertas de manipulación `T1562.008` `[Verificado MS Learn]`.

### D-02: Caza Diaria de Estrangulamiento `MailItemsAccessed` (`IsThrottled = True`) como Indicador de Exfiltración
- **Objetivo:** Detectar buzones que hayan superado los **1.000 registros `MailItemsAccessed` en menos de 24 horas**, identificando tempranamente raspado masivo de correo vía Graph/EWS/IMAP o sincronizaciones maliciosas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` (`CloudAppEvents` / `OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Threat Hunter.
- **Procedimiento Paso a Paso:**
  1. Ejecutar la consulta diaria sobre eventos `MailItemsAccessed` extrayendo `IsThrottled` dentro de `OperationProperties`, `MailAccessType` (`Bind` vs. `Sync`), `ClientInfoString`, `ClientIPAddress` y `AppId`.
  2. Separar sincronizaciones legítimas de primera configuración de Outlook en equipos corporativos gestionados en Intune frente a accesos desde IPs anómalas, aplicaciones OAuth desconocidas o tokens en riesgo en Entra ID.
  3. Ante cualquier buzón con `IsThrottled = True` no justificado, abrir incidente P1 y activar el playbook `AH-01` asumiendo pérdida de visibilidad `MailItemsAccessed` por 24 horas en ese buzón.
- **Evidencia Auditable:** Ejecución diaria del job de caza y tickets de triaje cerrados sobre cada evento `IsThrottled = True` `[Verificado MS Learn]`.

### D-03: Monitoreo de Salud y Latencia del Conector `OfficeActivity` hacia Microsoft Sentinel (Alta Velocidad E5)
- **Objetivo:** Verificar que el flujo continuo desde Office 365 Management Activity API hacia Microsoft Sentinel opere sin pérdida de eventos ni errores de *throttling* HTTP 429 `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Data connectors > Microsoft 365` y tabla `SentinelHealth` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Platform / SIEM Engineer.
- **Procedimiento Paso a Paso:**
  1. Consultar en Log Analytics / Advanced Hunting el tiempo transcurrido desde el último registro ingerido en `OfficeActivity` para `Exchange`, `SharePoint` y `MicrosoftTeams` (alertando si supera los 120 minutos).
  2. Verificar en `SentinelHealth` que no existan fallos de autorización ni agotamiento de cuota en la API (aprovechando la cuota dedicada a nivel de tenant de Audit Premium).
- **Evidencia Auditable:** Dashboard de salud de ingesta SIEM con disponibilidad continua >= 99,9 % `[Decisión / Propuesta Editorial]`.

### D-04: Detección Diaria de Ataques *Prompt Injection* (`XPIADetected` / `JailbreakDetected`) y Acceso IA a Datos Críticos
- **Objetivo:** Inspeccionar los registros de auditoría `CopilotInteraction`, `ConnectedAIAppInteraction` y `AIAppInteraction` en busca de banderas de ataque o lectura masiva de archivos con etiquetas *Highly Confidential* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` / API Microsoft Graph `security/auditLog/queries` / Defender XDR `CloudAppEvents` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / AI Security Analyst.
- **Procedimiento Paso a Paso:**
  1. Filtrar eventos de las últimas 24 horas donde `AccessedResources` contenga `XPIADetected == true` (inyección indirecta desde documento/correo externo) o `Messages` contenga `JailbreakDetected == true`.
  2. Cruzar los valores `SensitivityLabelId` dentro de `AccessedResources` contra el catálogo de etiquetas críticas de Purview Information Protection para detectar recolección acelerada de propiedad intelectual asistida por Copilot o agentes de **Agent 365**.
  3. Revisar casos con `DLPEvaluationDeferred != 0` (`Prompt=1, Response=2, Grounding=4, WebGrounding=8`) junto con `DLPEvaluationDeferredReason` para detectar fallos de evaluación DLP en tiempo real.
- **Evidencia Auditable:** Bitácora diaria de eventos de seguridad de IA auditados y escalados a SOC/Communication Compliance `[Verificado MS Learn]`.

### D-05: Vigilancia de Reglas Ocultas de Buzón (`UpdateInboxRules`), Reenvíos y Delegaciones (`SendAs` / `FullAccess`)
- **Objetivo:** Detectar mecanismos clásicos de persistencia y exfiltración silenciosa en compromisos BEC registrados en Exchange Online `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` (`OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / L2.
- **Procedimiento Paso a Paso:**
  1. Revisar alertas y eventos de `New-InboxRule`, `Set-InboxRule`, `UpdateInboxRules` (especialmente reglas que mueven correos a carpetas *RSS Subscriptions*, *Notes* o *Junk* o reenvían al exterior), `Add-MailboxPermission` (`FullAccess`), `Add-RecipientPermission` (`SendAs`) y `UpdateFolderPermissions`.
  2. Correlacionar inmediatamente el `SessionId` y `ClientIPAddress` con registros `MailItemsAccessed` y `SearchQueryInitiatedExchange` del mismo usuario.
- **Evidencia Auditable:** Cola diaria de eventos de persistencia de correo conciliada al 100 % `[Verificado MS Learn]`.

### D-06: Seguimiento de Trabajos Asíncronos de Búsqueda Forense en Curso (`Audit Search Jobs` y Graph Queries)
- **Objetivo:** Supervisar el estado (`Queued`, `In Progress`, `Completed` / `succeeded`, `failed`) y límites de conteo de las búsquedas forenses activas de casos legales o DFIR `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Search` y `GET /v1.0/security/auditLog/queries` `[Verificado MS Learn]`.
- **Rol Responsable:** DFIR Lead / Audit Reader.
- **Procedimiento Paso a Paso:**
  1. Verificar que ningún analista mantenga bloqueado su tope de **10 trabajos concurrentes** (o el límite de **1 búsqueda sin filtros**) con trabajos obsoletos.
  2. Para consultas ejecutadas vía Microsoft Graph `AuditLogQuery`, validar la propiedad autoritativa **`isRecordCountLimitExceeded`**: si devuelve `true` (superando el millón de registros por consulta), particionar inmediatamente el rango horario en sub-ventanas más cortas para evitar truncamiento probatorio.
  3. Exportar y resguardar en bóveda forense los resultados de trabajos próximos a cumplir **30 días** desde su creación antes de que el portal los purgue automáticamente.
- **Evidencia Auditable:** Verificación `isRecordCountLimitExceeded == false` en todas las extracciones probatorias de casos abiertos `[Verificado MS Learn]`.

### D-07: Monitoreo de Accesos de Aplicaciones OAuth de Terceros en Teams y Correo (`AppAccessContext`)
- **Objetivo:** Aprovechar las propiedades exclusivas de **Audit (Premium)** (`AppAccessContext` en Teams y `AttachmentAccess` / `MailItemsAccessed` en Exchange) para detectar aplicaciones OAuth maliciosas o sobreprivilegiadas leyendo chats o adjuntos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` y `purview.microsoft.com > Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Cloud App Security Analyst.
- **Procedimiento Paso a Paso:**
  1. Analizar operaciones de Teams (`ChatRetrieved`, `MessagesListed`, `MessageRead`, `MessageHostedContentRead`) e identificar valores `ClientAppId` / `AADSessionId` dentro de `AppAccessContext` que no pertenezcan al catálogo corporativo aprobado.
  2. Revisar picos de la operación predeterminada `AttachmentAccess` (acceso a adjuntos vía Microsoft Graph API) realizada bajo contexto de aplicación (`Admin` / impersonación).
- **Evidencia Auditable:** Registro diario de validación de aplicaciones con acceso de lectura a mensajería y correo `[Verificado MS Learn]`.

### D-08: Supervisión de Operaciones de Agentes Autónomos Registrados en Microsoft Agent 365
- **Objetivo:** Auditar las acciones autónomas ejecutadas por instancias de **Microsoft Agent 365** (agente-a-herramienta y agente-a-agente) sobre repositorios corporativos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` (`Agent 365 activities`) y `DSPM > Activity explorer > AI activities` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Security Analyst / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Filtrar actividades de auditoría generadas por identidades de agentes (`AgentId`, `AgentName`, `AgentVersion`) buscando accesos denegados por políticas (`PolicyDetails`, `Status = failure`) o lecturas fuera del horario/alcance habitual del flujo de negocio.
  2. Escalar anomalías al propietario del agente y al equipo de Entra Agent ID para ajuste de permisos de mínimo privilegio.
- **Evidencia Auditable:** Reporte diario de anomalías operativas de agentes autónomos sin incidentes abiertos `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Reconciliación de Asignación del Plan `Microsoft 365 Advanced Auditing` en Usuarios E5 y Nuevas Altas
- **Objetivo:** Evitar brechas silenciosas donde usuarios con licencia E5 o Purview Suite tengan desmarcado el plan de servicio **Microsoft 365 Advanced Auditing**, perdiendo la retención de 1 año y los *Intelligent Insights* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Microsoft Graph PowerShell (`Get-MgUserLicenseDetail`) / `admin.microsoft.com > Users > Active users` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity & Licensing Admin + Purview Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Ejecutar script semanal contra Microsoft Graph listando todos los usuarios activos con SKU M365 E5 / E7 / Purview Suite / E5 Audit add-on cuyo `ServicePlans` tenga el plan de *Advanced Auditing* deshabilitado.
  2. Auditar igualmente que el 100 % de custodios regulados (ejecutivos, finanzas, tesorería, administradores privilegiados) tengan asignado el **10-Year Audit Log Retention add-on** si les aplica política decenal.
  3. Remediación automática vía grupos de licenciamiento en Microsoft Entra ID (recordando que la activación tarda hasta 24 h en surtir efecto y no es retroactiva).
- **Evidencia Auditable:** Reporte semanal de conformidad de licenciamiento E5 / 10-Year Add-on al 100 % `[Verificado MS Learn]`.

### S-02: Gobernanza Semanal de Habilitación de `SearchQueryInitiatedExchange` en Nuevos Buzones (Single y Multi-Geo)
- **Objetivo:** Garantizar que todos los buzones de usuario creados en la última semana tengan habilitada la acción `SearchQueryInitiated` para no perder visibilidad de búsquedas del atacante en incidentes BEC `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-Mailbox`, `Set-Mailbox -AuditOwner @{Add="SearchQueryInitiated"}`) `[Verificado MS Learn]`.
- **Rol Responsable:** Exchange Online Admin / Purview Engineer.
- **Procedimiento Paso a Paso:**
  1. Identificar buzones creados o migrados en los últimos 7 días y consultar su ubicación (`MailboxLocations` en entornos Multi-Geo) y su lista `AuditOwner`.
  2. Conectarse al bosque regional correspondiente de Exchange Online y ejecutar `Set-Mailbox <UPN> -AuditOwner @{Add="SearchQueryInitiated"}` sobre los buzones objetivo definidos por la matriz de riesgo corporativa.
  3. Verificar que al personalizar `AuditOwner` se preserven intactas todas las demás acciones críticas predeterminadas (`MailItemsAccessed`, `Send`, `HardDelete`, `SoftDelete`, `Update`, `UpdateInboxRules`, `UpdateFolderPermissions`, `UpdateCalendarDelegation`, `ApplyRecord`).
- **Evidencia Auditable:** Salida semanal de verificación de `AuditOwner` incluyendo `SearchQueryInitiated` y el conjunto base completo `[Verificado MS Learn]`.

### S-03: Auditoría de Prioridades e Integridad de las Políticas de Retención de Auditoría (Límite de 50 Políticas)
- **Objetivo:** Verificar que ninguna política personalizada de retención esté acortando accidentalmente la retención de 1 año por defecto de `AzureActiveDirectory`, `Exchange`, `OneDrive` o `SharePoint` `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Audit retention policies` y Security & Compliance PowerShell (`Get-UnifiedAuditLogRetentionPolicy`) `[Verificado MS Learn]`.
- **Rol Responsable:** Purview Compliance Admin (`Organization Configuration`).
- **Procedimiento Paso a Paso:**
  1. Ejecutar `Get-UnifiedAuditLogRetentionPolicy | Sort-Object Priority | FL Priority,Name,RecordTypes,Operations,UserIds,RetentionDuration` (dado que esto incluye políticas creadas por PowerShell cuyos tipos de registro no son editables en UI).
  2. Verificar que el conteo total se mantenga holgadamente bajo el máximo de **50 políticas por tenant** y que ninguna política de alta prioridad (`Priority` cercano a `1`) establezca duraciones menores a `OneYear` sobre cargas críticas salvo mandato explícito de minimización.
- **Evidencia Auditable:** Instantánea semanal firmada de la tabla de políticas de retención y sus prioridades `[Verificado MS Learn]`.

### S-04: Seguimiento del Plan de Retiro de `Search-UnifiedAuditLog` hacia Microsoft Graph `AuditLogQuery` (`MC1505599`)
- **Objetivo:** Rastrear e inventariar semanalmente cualquier invocación remanente al cmdlet heredado `Search-UnifiedAuditLog` para asegurar 0 % de dependencia antes del retiro definitivo del **15 de octubre de 2027** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Registros de ejecución de cmdlets Exchange (`AdminAuditLog` / `SecurityComplianceCenterEOPCmdlet`) y repositorios DevSecOps `[Verificado MS Learn]`.
- **Rol Responsable:** SecOps Automation Engineer / Purview Lead.
- **Procedimiento Paso a Paso:**
  1. Identificar cuentas de servicio, runbooks de Azure Automation, scripts locales o herramientas de terceros que aún ejecuten `Search-UnifiedAuditLog`.
  2. Refactorizar cada flujo hacia **Microsoft Graph `AuditLogQuery` API v1.0** (`POST /security/auditLog/queries` o `New-MgSecurityAuditLogQuery`) asignando permisos de mínimo privilegio por servicio (`AuditLogsQuery-Exchange.Read.All`, etc.).
- **Evidencia Auditable:** Tendencia semanal decreciente de llamadas a `Search-UnifiedAuditLog` rumbo a cero `[Verificado MS Learn]`.

### S-05: Control FinOps Semanal de Ingesta Pay-As-You-Go por Auditoría de Aplicaciones IA No-Microsoft (`AIAppInteraction`)
- **Objetivo:** Supervisar el volumen y costo de registros de auditoría facturados por consumo en Azure para interacciones de empleados con aplicaciones GenAI externas no-Microsoft `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > Cost Management + Billing` y `purview.microsoft.com > Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** Purview Admin + FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Revisar el medidor de Azure de **Audit solutions** (número de registros de auditoría procesados para `AIAppInteraction` / `ConnectedAIAppInteraction` elegibles en PAYG, retenidos por 180 días).
  2. Detectar aplicaciones *Shadow AI* ruidosas que disparen miles de eventos desde el navegador; coordinar con Defender for Cloud Apps / Endpoint DLP el bloqueo de apps no autorizadas para reducir riesgo y costo simultáneamente.
- **Evidencia Auditable:** Informe semanal FinOps de registros PAYG de auditoría IA y acciones de bloqueo de Shadow AI `[Verificado MS Learn]`.

### S-06: Caza Proactiva Semanal sobre Consultas Sospechosas (`SearchQueryInitiatedExchange` / `SPO`)
- **Objetivo:** Detectar actores internos o cuentas comprometidas buscando términos de alto riesgo (`"password"`, `"credenciales"`, `"secret"`, `"SWIFT"`, `"indemnización"`, `"confidencial"`) en buzones y sitios SharePoint `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` (`CloudAppEvents` / `OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / SOC L3.
- **Procedimiento Paso a Paso:**
  1. Ejecutar consulta KQL semanal sobre `SearchQueryInitiatedExchange` y `SearchQueryInitiatedSharePoint` buscando coincidencias con diccionarios de palabras sensibles de credenciales, tesorería y propiedad intelectual.
  2. Correlacionar usuarios con alta frecuencia de búsquedas sensibles frente a inicios de sesión riesgosos en Entra ID (`SigninLogs`) y alertas de Insider Risk Management.
- **Evidencia Auditable:** Reporte semanal de caza de amenazas con hallazgos investigados `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Auditoría de `DefaultAuditSet`, Acciones Personalizadas y Limitaciones Multi-Geo en Exchange Online
- **Objetivo:** Verificar en toda la flota de buzones de usuario, compartidos y Grupos M365 que ningún cambio administrativo haya dejado buzones sin acciones críticas de auditoría `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-Mailbox | Select DefaultAuditSet, AuditOwner, AuditDelegate, AuditAdmin`) `[Verificado MS Learn]`.
- **Rol Responsable:** Exchange Online Admin + Purview Engineer.
- **Procedimiento Paso a Paso:**
  1. Auditar todos los buzones donde `DefaultAuditSet` no sea `Admin, Delegate, Owner`. Si la personalización fue intencional (para incluir `SearchQueryInitiated` o `MailboxLogin`), validar contra una plantilla maestra que ninguna acción nueva publicada por Microsoft falte en `AuditOwner`, `AuditDelegate` o `AuditAdmin`; si fue accidental, restaurar con `Set-Mailbox -DefaultAuditSet Admin,Delegate,Owner`.
  2. En arquitecturas **Multi-Geo**, auditar asignaciones de permisos sobre buzones compartidos (`Shared Mailboxes`) entre regiones distintas, documentando el control compensatorio necesario dado que **Exchange no registra en el log del buzón compartido las acciones delegadas cross-geo** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de higiene de auditoría de buzones con 100 % de cumplimiento de plantilla base `[Verificado MS Learn]`.

### M-02: Verificación de Archivo Externo en Sentinel Data Lake para Entidades No-Usuario (> 1 Año)
- **Objetivo:** Cubrir la limitación arquitectónica de Purview Audit donde los registros de **entidades no humanas** (*service principals*, aplicaciones, eventos de sistema) tienen una retención fija no configurable de **1 año** (incluso con add-on de 10 años) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Microsoft Sentinel > Data management > Tables` (`OfficeActivity`, `AuditLogs`, `AADServicePrincipalSignInLogs`) `[Verificado MS Learn]`.
- **Rol Responsable:** SIEM Architect + GRC Lead.
- **Procedimiento Paso a Paso:**
  1. Verificar que las tablas de actividad de aplicaciones, principales de servicio y administración en **Microsoft Sentinel Data Lake** mantengan configurada su política de retención de largo plazo (de 2 a 12 años según exigencia regulatoria SEC/DORA/PCI).
  2. Ejecutar una consulta de prueba sobre registros de principales de servicio con antigüedad > 366 días en el Data Lake para certificar recuperabilidad forense.
- **Evidencia Auditable:** Prueba mensual exitosa de consulta histórica (> 1 año) sobre entidades no-usuario en Sentinel Data Lake `[Verificado MS Learn]`.

### M-03: Recertificación Mensual de Roles `Audit Manager`, `Audit Reader`, `Organization Configuration` y Apps Graph
- **Objetivo:** Auditar quién tiene capacidad de leer el registro unificado o alterar su retención, verificando el uso de **Administrative Units** y permisos granulares de Graph `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and scopes > Role groups` y `https://entra.microsoft.com > Applications > Enterprise applications` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Admin + CISO Office.
- **Procedimiento Paso a Paso:**
  1. Revisar miembros de *Audit Manager*, *Audit Reader* y *Organization Configuration* en Purview y roles *Audit Logs / View-Only Audit Logs* en Exchange Admin Center, verificando que investigadores regionales estén acotados a su **Administrative Unit**.
  2. Auditar todas las aplicaciones registradas en Entra ID con permisos de aplicación `AuditLogsQuery.Read.All` o `AuditLogsQuery-*.Read.All`, revocando aquellas sin propietario activo o que no usen certificados / Managed Identity.
- **Evidencia Auditable:** Acta mensual de certificación de privilegios de auditoría y aplicaciones Graph `[Verificado MS Learn]`.

### M-04: Auditoría de Cobertura de Cargas Secundarias (Power BI / Fabric, Dynamics 365, Defender, Purview)
- **Objetivo:** Confirmar que los interruptores específicos por servicio (como el portal de administración de Power BI / Microsoft Fabric) sigan enviando telemetría al registro unificado `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://app.powerbi.com/admin-portal` y `purview.microsoft.com > Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** Purview Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Ejecutar una consulta mensual de conteo por `RecordType` / `Workload` (`PowerBIAudit`, `CRM`, `MicrosoftTeams`, `CopilotInteraction`, `MIPLabel`, `ComplianceDLPSharePoint`, `ComplianceDLPExchange`, `DLPEndpoint`).
  2. Investigar cualquier caída abrupta a cero en cargas habilitadas corporativamente.
- **Evidencia Auditable:** Matriz mensual *Proof of Life* de ingesta activa por `AuditLogRecordType` `[Verificado MS Learn]`.

### M-05: Auditoría Interna de Consultas Ejecutadas sobre Purview Audit ("Auditing the Auditors")
- **Objetivo:** Supervisar qué búsquedas de auditoría ejecutaron los propios administradores e investigadores para prevenir espionaje interno sobre ejecutivos o temas confidenciales `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Search` (historial de 30 días de trabajos) y registros de auditoría de consultas `[Verificado MS Learn]`.
- **Rol Responsable:** Internal Audit / DPO.
- **Procedimiento Paso a Paso:**
  1. Revisar en el **Search job dashboard** la columna **Search performed by**, los criterios de usuarios buscados y las búsquedas sin filtros ejecutadas en los últimos 30 días, además de las llamadas registradas a `security/auditLog/queries`.
  2. Validar una muestra aleatoria del 15 % contra números de ticket de incidente SOC, caso de RR. HH. o requerimiento legal válido.
- **Evidencia Auditable:** Informe mensual de control interno sobre uso legítimo de herramientas de auditoría `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Prueba de Recuperación Forense Histórica a 1 Año y 10 Años (Validación de Extremo a Extremo)
- **Objetivo:** Comprobar empíricamente que los registros cubiertos por la política predeterminada de 1 año y por las políticas personalizadas de **3, 5, 7 y 10 años** son efectivamente recuperables y exportables sin corrupción `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Search` y API Microsoft Graph `POST /v1.0/security/auditLog/queries` `[Verificado MS Learn]`.
- **Rol Responsable:** DFIR Lead + Legal / Compliance Officer.
- **Procedimiento Paso a Paso:**
  1. Seleccionar una ventana histórica de hace 11 meses (para usuarios E5 estándar) y ventanas > 12 meses (para custodios con add-on de 10 años), recordando respetar el máximo de **180 días de rango por cada trabajo de búsqueda** `[Verificado MS Learn]`.
  2. Ejecutar la extracción mediante Microsoft Graph `AuditLogQuery`, descargar los registros (`GET .../records`), transformar la columna JSON `AuditData` y verificar integridad de campos clave (`SensitivityLabel` en `MailItemsAccessed`, `AccessedResources` en `CopilotInteraction`).
- **Evidencia Auditable:** Evidencia trimestral de recuperación exitosa de logs históricos (> 180 días y > 1 año) `[Verificado MS Learn]`.

### T-02 (Trimestral): Revisión de Capacidad, Tiempos de Ejecución y Cuotas de API (`Management Activity API` y `Graph`)
- **Objetivo:** Optimizar el rendimiento de consultas masivas (que en tenants grandes pueden tardar hasta 48 h si no se acotan) y validar márgenes de ancho de banda de ingesta SIEM `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Microsoft Sentinel` y telemetría de API Graph `[Verificado MS Learn]`.
- **Rol Responsable:** SIEM / SecOps Architect.
- **Procedimiento Paso a Paso:**
  1. Analizar los tiempos promedio de finalización (`Search time`) de los trabajos de auditoría del trimestre e instruir a los analistas en acotar siempre `recordTypeFilters`, `operationFilters` y `userPrincipalNameFilters`.
  2. Verificar la relación entre crecimiento de licencias E5 del tenant y la cuota dinámica asignada en Office 365 Management Activity API.
- **Evidencia Auditable:** Reporte trimestral de desempeño y optimización de consultas forenses `[Verificado MS Learn]`.

### SM-01 (Semestral): Simulacro DFIR de Compromiso BEC / Nación-Estado con Reconstrucción de Alcance de Brecha
- **Objetivo:** Entrenar y medir la capacidad del SOC y Legal para determinar exactamente qué correos, archivos y etiquetas de sensibilidad accedió un atacante simulado empleando exclusivamente Purview Audit (Premium) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit`, Microsoft Graph `AuditLogQuery` y `security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + SOC Manager + DFIR Lead + General Counsel.
- **Procedimiento Paso a Paso:**
  1. Simular en un buzón y sitio de prueba E5 una intrusión controlada: inicio de sesión desde IP de laboratorio, ejecución de 3 búsquedas en OWA (`SearchQueryInitiatedExchange`) y SharePoint (`SearchQueryInitiatedSharePoint`), apertura individual `Bind` de 5 correos (2 de ellos con etiqueta *Highly Confidential*), un `Prompt` en Copilot accediendo a un documento etiquetado (`CopilotInteraction`) y creación de una regla de reenvío (`UpdateInboxRules`).
  2. El equipo DFIR debe reconstruir la línea de tiempo exacta por `SessionId`, listar los 5 `InternetMessageId` comprometidos, identificar cuáles tenían `SensitivityLabel` crítico y demostrar matemáticamente que los miles de correos restantes del buzón **no fueron accedidos**.
- **Evidencia Auditable:** Informe pericial simulado admisible ante regulador (HIPAA / GDPR / SEC / CSIRT) `[Verificado MS Learn]`.

### A-01 (Anual): Revisión Anual de Matriz Regulatoria de Retención de Logs (180 Días vs. 1 Año vs. 10 Años vs. Data Lake)
- **Objetivo:** Alinear la arquitectura corporativa de retención de auditoría con nuevas leyes, contratos de clientes críticos y normativas sectoriales (DORA, PCI-DSS v4.0, SEC 17a-4, CISA M-24-04, Ley 21.719 de Chile) `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Audit retention policies` y `Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + Chief Compliance Officer + General Counsel + FinOps Lead.
- **Procedimiento Paso a Paso:**
  1. Revisar qué poblaciones requieren asignación del add-on **10-Year Audit Log Retention** en Purview (búsqueda nativa en el portal/Graph) frente a qué cargas se retienen en **Microsoft Sentinel Data Lake** (incluyendo entidades no humanas > 1 año).
  2. Aprobar el presupuesto anual de licencias add-on de 10 años, medidores PAYG de auditoría IA no-Microsoft y almacenamiento Data Lake.
- **Evidencia Auditable:** Política Corporativa Anual de Retención de Registros de Auditoría aprobada por el Comité de Riesgos `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook Forense ante Compromiso de Cuenta / BEC (`MailItemsAccessed`, `Bind` vs. `Sync`, `IsThrottled`)
- **Disparador:** Alerta confirmada de robo de sesión AiTM, credencial comprometida en Entra ID, regla maliciosa de buzón o envío fraudulento BEC `[Verificado MS Learn]`.
- **Consola y Ruta:** Microsoft Graph `POST /v1.0/security/auditLog/queries`, `purview.microsoft.com > Solutions > Audit` y Exchange Online PowerShell `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. **Contención inmediata:** Deshabilitar cuenta o rotar credenciales, revocar todas las sesiones y refresh tokens (`Revoke-MgUserSignInSession -UserId <UPN>`), auditar dispositivos MFA registrados, revocar consentimientos OAuth maliciosos e inspeccionar reenvíos SMTP y reglas ocultas (`Get-InboxRule -Mailbox <UPN> -IncludeHidden`) `[Verificado MS Learn]`.
  2. **Acotamiento de ventana y sesión:** Identificar en Entra Sign-in Logs las direcciones `ClientIPAddress`, `AppId` y ventanas UTC exactas del actor malicioso.
  3. **Evaluación de `Sync` y `IsThrottled`:** Consultar vía Graph `AuditLogQuery` todas las operaciones `MailItemsAccessed` del usuario afectado. Verificar primero si existe algún registro con `MailAccessType = Sync` bajo la IP/sesión del atacante o si se disparó `IsThrottled = True` (> 1.000 eventos en 24 h): de ser así, declarar comprometida la totalidad de la carpeta/buzón sincronizado o la ventana de 24 h estrangulada `[Verificado MS Learn]`.
  4. **Extracción quirúrgica `Bind` y etiquetas MIP:** Si el atacante operó solo mediante `Bind` sin *throttling*, extraer todos los `InternetMessageId` y su propiedad `SensitivityLabel` (Audit Premium) asociados al `SessionId` / `ClientIPAddress` malicioso para determinar con exactitud milimétrica qué correos e información regulada (PII/PHI/Financiera) fueron expuestos `[Verificado MS Learn]`.
  5. **Reconstrucción de búsquedas y envíos:** Consultar `SearchQueryInitiatedExchange`, `SearchQueryInitiatedSharePoint`, `Send`, `SendAs`, `SendOnBehalf` y `HardDelete` en el mismo rango para conocer qué buscó, qué envió y qué intentó borrar el atacante `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete JSON/CSV inmutable de `AuditLogQuery` con hash SHA-256 adjunto al informe legal de alcance de brecha `[Decisión / Propuesta Editorial]`.

### AH-02: Investigación Forense de Exfiltración o Reconocimiento Asistido por IA (`CopilotInteraction` y Agent 365)
- **Disparador:** Incidente donde un atacante con cuenta comprometida o un *insider* malicioso utilizó Microsoft 365 Copilot o un agente autónomo para resumir y localizar secretos corporativos a velocidad de máquina `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Solutions > Audit` (`CopilotInteraction`, `ConnectedAIAppInteraction`, `AIAppInteraction`) y `Solutions > eDiscovery` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ejecutar consulta en Graph `AuditLogQuery` filtrando por el `userPrincipalNameFilters` del usuario (o identidad de la instancia de **Agent 365**) y `operationFilters = ["CopilotInteraction", "ConnectedAIAppInteraction", "AIAppInteraction"]`.
  2. Desempaquetar en cada registro el arreglo **`AccessedResources`** para obtener la lista completa de documentos SharePoint/OneDrive, correos y chats de Teams que Copilot leyó como *grounding* (`SiteUrl`, `Name`, `SensitivityLabelId`, `Action`), así como `AISystemPlugin` utilizados y banderas `XPIADetected` / `JailbreakDetected` `[Verificado MS Learn]`.
  3. Si se requiere inspeccionar el texto literal del prompt y la respuesta entregada al atacante, escalar a **Purview eDiscovery** ejecutando una colección sobre el buzón del usuario con la condición `Type = Copilot activity` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario completo de `AccessedResources` etiquetados y exportación legal desde eDiscovery `[Verificado MS Learn]`.

### AH-03: Respuesta Crítica ante Desactivación de Auditoría o Manipulación de Bypass (`Audit Tampering`)
- **Disparador:** Detección de `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $false`, `Set-OrganizationConfig -AuditDisabled $true`, `Set-MailboxAuditBypassAssociation -AuditBypassEnabled $true` o borrado de políticas de retención `[Verificado MS Learn]`.
- **Consola y Ruta:** Exchange Online PowerShell, Microsoft Entra ID y `security.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. **Restauración inmediata del control:** Ejecutar `Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true`, `Set-OrganizationConfig -AuditDisabled $false` y revertir cualquier `Set-MailboxAuditBypassAssociation -AuditBypassEnabled $false` `[Verificado MS Learn]`.
  2. Aislar y revocar sesiones de la cuenta administrativa que ejecutó el cambio, tratándola como compromiso de privilegios Tier-0 hasta demostrar lo contrario.
  3. Reconstruir la actividad ocurrida durante la ventana ciega apoyándose en fuentes independientes inmutables: **Entra ID Sign-in/Audit Logs**, **Message Trace**, **Defender for Endpoint / CloudAppEvents** y logs de red.
- **Evidencia Auditable:** Comandos de restauración verificados e informe de incidente mayor de seguridad `[Verificado MS Learn]`.

### AH-04: Extracción Forense Histórica Multi-Anual (Hasta 10 Años) ante Litigio o Inspección Regulatoria
- **Disparador:** Requerimiento formal de regulador (SEC, FINRA, Superintendencia, Autoridad de Protección de Datos) o litigio judicial que exige trazas de auditoría de entre 1 y 10 años atrás `[Verificado MS Learn]`.
- **Consola y Ruta:** API Microsoft Graph `POST /v1.0/security/auditLog/queries` y **Microsoft Sentinel Data Lake** `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Dividir el periodo multianual solicitado en bloques consecutivos de **máximo 180 días** cada uno (límite técnico por consulta de búsqueda en Purview Audit) y lanzar hasta **10 trabajos en paralelo** por cuenta autorizada `[Verificado MS Learn]`.
  2. Verificar en cada lote completado que `status == "succeeded"` e **`isRecordCountLimitExceeded == false`**; si algún semestre excede el millón de registros, subdividirlo en bloques mensuales o semanales `[Verificado MS Learn]`.
  3. Para actividades de principales de servicio o aplicaciones con antigüedad mayor a 1 año (no cubiertas por políticas de 10 años de Purview), extraer los registros complementarios desde **Microsoft Sentinel Data Lake** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Cadena de custodia documentada con archivos exportados, metadatos de consulta e integridad criptográfica `[Decisión / Propuesta Editorial]`.

### AH-05: Incorporación de Emergencia de Custodios de Alto Riesgo a Retención de 10 Años y Auditoría Profunda
- **Disparador:** Fusión/adquisición (M&A), investigación interna incipiente o designación de nuevos ejecutivos/administradores Tier-0 `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `admin.microsoft.com` (Licencias), `purview.microsoft.com > Solutions > Audit > Audit retention policies` y Exchange Online PowerShell `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Asignar inmediatamente a los usuarios objetivo la licencia E5 / Purview Suite (verificando el check **Microsoft 365 Advanced Auditing**) y el add-on **10-Year Audit Log Retention** `[Verificado MS Learn]`.
  2. Incluir a los usuarios en una política personalizada de retención de auditoría con `Duration = 10 Years` y alta prioridad numérica (ej. `Priority = 10`), recordando que protege todos los eventos generados **a partir de ese momento** `[Verificado MS Learn]`.
  3. Habilitar en sus buzones tanto `SearchQueryInitiated` como `MailboxLogin` en `AuditOwner` (`Set-Mailbox -AuditOwner @{Add="SearchQueryInitiated","MailboxLogin"}`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Confirmación de licencia, política `TenYears` aplicada y salida `AuditOwner` verificada `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas Microsoft Graph `AuditLogQuery`, PowerShell y KQL

#### Consulta 1: Búsqueda Forense Asíncrona de `MailItemsAccessed` y Búsquedas vía Microsoft Graph `AuditLogQuery` v1.0 (GA Oct-2026)
Estándar oficial de automatización que reemplaza a `Search-UnifiedAuditLog` (retiro 15-oct-2027 según `MC1505599`), soportando hasta 1 millón de registros y permiso granular `AuditLogsQuery-Exchange.Read.All` `[Verificado MS Learn]`.
```powershell
# Plataforma: Microsoft Graph PowerShell SDK v1.0 (Permisos: AuditLogsQuery-Exchange.Read.All, AuditLogsQuery-SharePoint.Read.All)
Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "AuditLogsQuery-Exchange.Read.All", "AuditLogsQuery-SharePoint.Read.All"

$forensicQuery = @{
    "@odata.type"            = "#microsoft.graph.security.auditLogQuery"
    displayName              = "BEC-Forensic-MailItemsAccessed-SearchQuery"
    filterStartDateTime      = (Get-Date).AddDays(-14).ToUniversalTime().ToString("o")
    filterEndDateTime        = (Get-Date).ToUniversalTime().ToString("o")
    userPrincipalNameFilters = @("ejecutivo.afectado@contoso.com")
    operationFilters         = @("MailItemsAccessed", "Send", "SendAs", "UpdateInboxRules", "SearchQueryInitiatedExchange", "SearchQueryInitiatedSharePoint")
}
$job = Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries" -Body ($forensicQuery | ConvertTo-Json -Depth 5)
Write-Output "Query ID: $($job.id) | Status: $($job.status)"

# Una vez que status == 'succeeded', verificar truncamiento y recuperar registros paginados:
# $status = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries/$($job.id)"
# if ($status.isRecordCountLimitExceeded) { Write-Warning "Límite de 1M excedido: dividir ventana temporal!" }
# $records = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries/$($job.id)/records"
```

#### Consulta 2: Detección KQL de Estrangulamiento `MailItemsAccessed` (`IsThrottled == true`) y Exfiltración `Sync` / `Bind`
Detecta en Defender XDR / Sentinel cuándo un buzón supera los 1.000 eventos `MailItemsAccessed` en menos de 24 horas o sufre sincronización masiva sospechosa `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting (Tabla: CloudAppEvents)
CloudAppEvents
| where Timestamp > ago(24h)
| where ActionType == "MailItemsAccessed"
| extend OpProps = parse_json(tostring(RawEventData.OperationProperties))
| mv-apply Prop = OpProps on (
    summarize
        MailAccessType = take_anyif(tostring(Prop.Value), tostring(Prop.Name) == "MailAccessType"),
        IsThrottled    = take_anyif(tostring(Prop.Value), tostring(Prop.Name) == "IsThrottled")
)
| extend SessionId = tostring(RawEventData.SessionId), ClientInfo = tostring(RawEventData.ClientInfoString)
| where IsThrottled =~ "True" or MailAccessType =~ "Sync"
| project Timestamp, AccountDisplayName, IPAddress, CountryCode, MailAccessType, IsThrottled, ClientInfo, SessionId
| sort by Timestamp desc
```

#### Consulta 3: Auditoría Forense de `CopilotInteraction` para Detectar `XPIADetected`, `JailbreakDetected` y Etiquetas Sensibles
Inspecciona en Sentinel / Log Analytics los recursos accedidos por Microsoft 365 Copilot y agentes IA, alertando ante ataques de inyección cruzada (XPIA) o *jailbreak* `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Sentinel (Tabla: OfficeActivity o exportación AuditData)
OfficeActivity
| where TimeGenerated > ago(7d)
| where Operation in ("CopilotInteraction", "ConnectedAIAppInteraction", "AIAppInteraction")
| extend Data = parse_json(AuditData)
| extend AgentId = tostring(Data.AgentId), AppHost = tostring(Data.AppHost), AppIdentity = tostring(Data.AppIdentity)
| mv-expand Msg = Data.Messages
| extend JailbreakDetected = tobool(Msg.JailbreakDetected)
| mv-expand Res = Data.AccessedResources
| extend ResourceName = tostring(Res.Name), SensitivityLabelId = tostring(Res.SensitivityLabelId), XPIADetected = tobool(Res.XPIADetected)
| where JailbreakDetected == true or XPIADetected == true or isnotempty(SensitivityLabelId)
| project TimeGenerated, UserId, Operation, AppHost, AppIdentity, AgentId, ResourceName, SensitivityLabelId, JailbreakDetected, XPIADetected
```

#### Consulta 4: Verificación Integral del Pipeline UAL, `AuditDisabled`, `Bypass` y Habilitación de `SearchQueryInitiated` (EXO PowerShell)
Ejecuta las comprobaciones oficiales de Microsoft Learn en Exchange Online PowerShell (nunca evaluar `UnifiedAuditLogIngestionEnabled` desde SCC PowerShell) `[Verificado MS Learn]`.
```powershell
# Plataforma: Exchange Online PowerShell
Connect-ExchangeOnline -ShowBanner:$false

# 1. Estado global UAL y Mailbox Auditing on by default
$ual = (Get-AdminAuditLogConfig).UnifiedAuditLogIngestionEnabled
$mbxAuditDisabled = (Get-OrganizationConfig).AuditDisabled
$bypassedUsers = @(Get-MailboxAuditBypassAssociation -ResultSize Unlimited | Where-Object { $_.AuditBypassEnabled -eq $true })

Write-Output "UAL Ingestion Enabled (Esperado True): $ual"
Write-Output "Org Mailbox AuditDisabled (Esperado False): $mbxAuditDisabled"
Write-Output "Cuentas en Audit Bypass (Esperado 0): $($bypassedUsers.Count)"

# 2. Habilitar SearchQueryInitiatedExchange preservando acciones existentes en un buzón crítico
Set-Mailbox -Identity "cfo@contoso.com" -AuditOwner @{Add="SearchQueryInitiated"}
Get-Mailbox -Identity "cfo@contoso.com" | Select-Object UserPrincipalName, DefaultAuditSet, AuditOwner
```

#### Consulta 5: Creación y Auditoría de Políticas de Retención de 10 Años en Security & Compliance PowerShell
Audita la jerarquía de prioridades (`1` a `10000`) de las hasta 50 políticas personalizadas y despliega retención de 10 años para Teams y Copilot `[Verificado MS Learn]`.
```powershell
# Plataforma: Security & Compliance PowerShell (Connect-IPPSSession - Rol: Organization Configuration)
Connect-IPPSSession

# Listar todas las políticas personalizadas en orden real de procesamiento (Priority menor = mayor precedencia)
Get-UnifiedAuditLogRetentionPolicy | Sort-Object Priority |
    Format-Table Priority, Name, RetentionDuration, RecordTypes, Operations, UserIds -AutoSize

# Crear política de 10 años para usuarios licenciados con 10-Year Audit Log Retention add-on
New-UnifiedAuditLogRetentionPolicy -Name "Retencion-10Y-Teams-Ejecutivos" `
    -Description "Retención regulatoria de 10 años para Microsoft Teams en custodios E5 + Add-on 10Y" `
    -RecordTypes MicrosoftTeams -RetentionDuration TenYears -Priority 50
```

#### Consulta 6: Caza KQL de Términos Sensibles Buscados por Atacantes (`SearchQueryInitiatedExchange` / `SPO`)
Revela búsquedas internas sospechosas ejecutadas en Outlook/OWA o SharePoint Online durante reconocimientos post-compromiso `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Sentinel / Defender Unified SecOps (Tabla: OfficeActivity)
OfficeActivity
| where TimeGenerated > ago(14d)
| where Operation in ("SearchQueryInitiatedExchange", "SearchQueryInitiatedSharePoint")
| extend Details = parse_json(AuditData)
| extend QueryText = coalesce(tostring(Details.QueryText), tostring(Details.SearchQueryText))
| where QueryText has_any ("password", "contraseña", "secret", "token", "swift", "wire", "confidencial", "keyvault")
| project TimeGenerated, UserId, Operation, QueryText, ClientIP, UserAgent = tostring(Details.ClientInfoString)
| sort by TimeGenerated desc
```

#### Consulta 7: Detección en Tiempo Real de Manipulación del Sistema de Auditoría (`Anti-Tampering` — KQL)
Genera incidente de severidad crítica si cualquier administrador apaga la auditoría, activa bypass o altera políticas de retención `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Sentinel Analytics Rule (Tabla: OfficeActivity)
OfficeActivity
| where TimeGenerated > ago(1d)
| where Operation in (
    "Set-AdminAuditLogConfig",
    "Set-MailboxAuditBypassAssociation",
    "Remove-UnifiedAuditLogRetentionPolicy",
    "Set-UnifiedAuditLogRetentionPolicy"
) or (Operation == "Set-OrganizationConfig" and AuditData has "AuditDisabled")
| project TimeGenerated, UserId, Operation, ClientIP, Parameters, AuditData
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Control Operativo a Verificar | Comando / Método Oficial | Resultado Esperado ("Proof of Life") | Frecuencia |
| :--- | :--- | :--- | :--- |
| **Ingesta Global UAL Activa** | `Get-AdminAuditLogConfig \| FL UnifiedAuditLogIngestionEnabled` (en EXO PowerShell) | `UnifiedAuditLogIngestionEnabled : True` `[Verificado MS Learn]` | Diaria |
| **Mailbox Auditing por Defecto** | `Get-OrganizationConfig \| FL AuditDisabled` (en EXO PowerShell) | `AuditDisabled : False` `[Verificado MS Learn]` | Diaria |
| **Cero Cuentas en Bypass** | `Get-MailboxAuditBypassAssociation \| Where {$_.AuditBypassEnabled -eq $true}` | `0` cuentas no autorizadas `[Verificado MS Learn]` | Diaria |
| **Plan `Advanced Auditing` E5** | Verificar `ServicePlans` de usuarios E5 en Microsoft Graph (`Get-MgUserLicenseDetail`) | `100 %` de usuarios E5 con **Microsoft 365 Advanced Auditing** habilitado `[Verificado MS Learn]` | Semanal |
| **Captura de `SensitivityLabel` en Correo** | Inspeccionar `AuditData` de un evento `MailItemsAccessed` de usuario E5 sobre correo etiquetado | Propiedad `SensitivityLabel` presente con el GUID de la etiqueta MIP `[Verificado MS Learn]` | Mensual |
| **Habilitación `SearchQueryInitiated`** | `Get-Mailbox <VIP> \| Select -Expand AuditOwner` | Contiene explícitamente `SearchQueryInitiated` junto al set base completo `[Verificado MS Learn]` | Semanal |
| **Migración post-`Search-UnifiedAuditLog`** | Auditar invocaciones a `Search-UnifiedAuditLog` vs. `POST /v1.0/security/auditLog/queries` | `100 %` de automatizaciones productivas operando sobre Microsoft Graph `AuditLogQuery` `[Verificado MS Learn]` | Semanal |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales

> **Nota de validación:** Las metas porcentuales, umbrales de tiempo y frecuencias recomendadas constituyen estándares consultivos de excelencia etiquetados como `[Decisión / Propuesta Editorial]`.

| ID | Indicador Clave (KPI) | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Cobertura Efectiva del Plan `Advanced Auditing` en Población E5** | `(Usuarios E5/Purview Suite con plan Microsoft 365 Advanced Auditing activo / Total usuarios licenciados E5/Purview Suite) * 100` | `100 %` | Semanal | CISO, Purview Admin, Identity Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cobertura Forense de `SearchQueryInitiatedExchange`** | `(Buzones en alcance con SearchQueryInitiated habilitado en AuditOwner sin pérdida de acciones base / Total buzones en alcance) * 100` | `100 %` (Ejecutivos/VIPs/Toda la flota) | Semanal | SOC Manager, DFIR Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Disponibilidad e Integridad del Pipeline UAL y Bypass** | `(Días con UnifiedAuditLogIngestionEnabled=True, AuditDisabled=False y 0 bypasses no aprobados / Total días del mes) * 100` | `100 %` | Diaria / Mensual | CISO, Internal Audit | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Avance de Migración a Microsoft Graph `AuditLogQuery` (`MC1505599`)** | `(Scripts, playbooks e integraciones migradas a Graph AuditLogQuery v1.0 / Total integraciones que consultan Purview Audit) * 100` | `100 %` (antes de Q2 2027; retiro duro 15-oct-2027) | Semanal / Mensual | SecOps Engineering Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo Medio de Triaje ante Estrangulamiento `MailItemsAccessed` (`IsThrottled`)** | `Promedio(Hora de inicio de triaje SOC - Hora de evento MailItemsAccessed con IsThrottled=True)` | `<= 30 minutos` | Diaria | SOC Manager, DFIR Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Conformidad de Retención Regulatoria (1 Año / 10 Años / Data Lake SPN)** | `(Custodios regulados con licencia + política 10Y activa + tablas SPN en Sentinel Data Lake > 1Y / Total ámbito regulado) * 100` | `100 %` | Mensual / Trimestral | Chief Compliance Officer, Legal, GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tasa de Completitud Sin Truncamiento en Extracciones Forenses Graph** | `(Consultas Graph AuditLogQuery cerradas con isRecordCountLimitExceeded == false / Total consultas probatorias DFIR/Legal) * 100` | `100 %` | Mensual | DFIR Lead, Legal Counsel | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Latencia y Salud del Streaming `OfficeActivity` hacia Sentinel** | `(Intervalos horarios con ingesta OfficeActivity activa y latencia <= 90 min / Total horas del mes) * 100` | `>= 99,5 %` | Diaria / Semanal | SIEM Architect, SOC Manager | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Caracterización Operativa en Microsoft Purview Audit |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Por Defecto** | Opera solo con Audit (Standard) a 180 días; sin verificación de `Advanced Auditing` en licencias E5; `SearchQueryInitiatedExchange` apagado; búsquedas manuales ad-hoc dependientes de `Search-UnifiedAuditLog`. |
| **Nivel 2** | **Básico / Habilitado E5** | Plan *Microsoft 365 Advanced Auditing* habilitado en usuarios E5 (1 año por defecto en Entra, Exchange, OneDrive, SharePoint); roles *Audit Reader* y *Audit Manager* separados, pero sin políticas personalizadas para Teams/Copilot ni alertas anti-tampering. |
| **Nivel 3** | **Definido / Forense Proactivo** | `SearchQueryInitiatedExchange` desplegado sistemáticamente; políticas personalizadas de retención de 1 año extendidas a `MicrosoftTeams`, `CopilotInteraction` y `PowerBIAudit`; streaming `OfficeActivity` activo en Sentinel con reglas contra `AuditDisabled`, `Bypass` e `IsThrottled = True`. |
| **Nivel 4** | **Gestionado / Regulatorio y Automatizado** | Retención de **10 años** desplegada en poblaciones reguladas junto con archivo > 1 año de entidades no-usuario en **Sentinel Data Lake**; 100 % de automatización migrada a **Microsoft Graph `AuditLogQuery` v1.0** con permisos granulares por carga; auditoría diaria de `XPIADetected`/`JailbreakDetected` en IA. |
| **Nivel 5** | **Optimizado / Ciber-Resiliente** | Simulacros semestrales BEC/Nación-Estado demostrando delimitación exacta de brecha por `InternetMessageId` y `SensitivityLabel`; gobernanza continua de instancias autónomas **Microsoft Agent 365**; auditoría independiente mensual (*Auditing the Auditors*) y pruebas trimestrales certificadas de recuperación decenal. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota metodológica:** El mapeo probatorio entre capacidades de Microsoft Purview Audit (Premium) y las 6 funciones de **NIST CSF 2.0 (CSWP 29)** se documenta como `[Decisión / Propuesta Editorial]` respaldada en controles técnicos verificados.

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (NIST CSF 2.0) | Capacidad Habilitadora en Purview Audit (Premium) | Técnica MITRE ATT&CK / ATLAS | Evidencia Auditable Reproducible |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OC-03` | Los mandatos legales y regulatorios de conservación probatoria y notificación de brechas se gestionan formalmente. | Retención de **1 año por defecto** (E5), hasta **50 políticas personalizadas** y add-on de **10 años** complementado con Sentinel Data Lake para entidades no humanas. | N/A (Cumplimiento Regulatorio SEC / HIPAA / DORA) | Salida de `Get-UnifiedAuditLogRetentionPolicy` y matriz anual firmada de retención `[Decisión / Propuesta Editorial]`. |
| **GOVERN (GV)** | `GV.RR-02` | Se segregan responsabilidades entre administración de auditoría, configuración de retención y lectura forense. | Separación entre `Organization Configuration`, `Audit Manager`, `Audit Reader`, **Administrative Units** y permisos Graph por carga (`AuditLogsQuery-<Workload>.Read.All`). | `T1078.004` (Cloud Accounts) | Acta mensual de recertificación de grupos de roles Purview y permisos de apps Entra `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.AM-03` | Las representaciones de flujos de comunicación, accesos de aplicaciones y agentes de IA autorizados se mantienen actualizadas. | Propiedad `AppAccessContext` en Teams, `AttachmentAccess` en Graph e inventario auditado de `AppIdentity` y `AgentId` (**Agent 365**). | `T1528` (Steal Application Access Token) | Reporte mensual de aplicaciones OAuth y agentes con actividad en UAL `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.RA-05` | Las amenazas, vulnerabilidades y exposición de activos críticos informan la priorización del riesgo. | Enriquecimiento exclusivo **`SensitivityLabel`** en `MailItemsAccessed` y `SensitivityLabelId` en `AccessedResources` de `CopilotInteraction`. | `T1114.002` (Remote Email Collection) | Consultas forenses cruzando accesos con GUIDs de etiquetas *Highly Confidential* `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.PS-04` | Se generan registros de auditoría adecuados y se protegen contra modificación o desactivación no autorizada. | `UnifiedAuditLogIngestionEnabled = True`, `AuditDisabled = False`, monitoreo de `MailboxAuditBypassAssociation` e inmutabilidad de los registros ingeridos. | `T1562.008` (Impair Defenses: Disable or Modify Cloud Logs) | Salida diaria de verificación EXO PowerShell y regla NRT/Scheduled en Sentinel `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.AA-05` | El acceso a los propios repositorios de logs se restringe bajo mínimo privilegio y alcance regional. | Acotamiento por **Administrative Units** en búsquedas de Purview y reemplazo de `Search-UnifiedAuditLog` por permisos granulares `AuditLogsQuery-*`. | `T1098` (Account Manipulation) | Configuración de AU y auditoría mensual *Auditing the Auditors* `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.CM-01` | Los servicios en la nube y redes colaborativas se monitorean continuamente para detectar actividad anómala. | Streaming continuo de alta velocidad (~2x cuota en E5) vía **Office 365 Management Activity API** hacia `OfficeActivity` en Sentinel. | `T1078` / `T1114` | Métricas de salud en `SentinelHealth` y latencia sostenida <= 90 min `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.AE-03` | Se correlaciona información de múltiples fuentes para detectar reconocimiento interno, raspado masivo o ataques contra IA. | Detección de `IsThrottled = True` (> 1.000 `MailItemsAccessed`/24h), cazas sobre `SearchQueryInitiatedExchange/SPO` y banderas `XPIADetected` / `JailbreakDetected`. | `T1530` / `AML.T0051` (Data from Cloud Storage / XPIA) | Alertas generadas por reglas analíticas y reportes semanales de Threat Hunting `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.AN-03` | Se ejecuta análisis forense para establecer qué ocurrió, la causa raíz y el alcance exacto del compromiso. | Metodología oficial de investigación `MailItemsAccessed` diferenciando `Sync` vs. `Bind` (`InternetMessageId`), `SessionId` y recursos accedidos por Copilot. | `T1114.002` / `T1567` (BEC & Exfiltration) | Paquetes JSON/CSV extraídos vía Microsoft Graph `AuditLogQuery` sin truncamiento (`isRecordCountLimitExceeded == false`) `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.MI-01` | Se contienen sesiones comprometidas, reglas ocultas de persistencia y abusos de agentes autónomos. | Playbook integrado de revocación `Revoke-MgUserSignInSession`, limpieza de `Get-InboxRule -IncludeHidden` y restauración inmediata ante *audit tampering*. | `T1564.008` (Email Hiding Rules) | Trazas de ejecución de playbooks `AH-01`, `AH-02` y `AH-03` `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de los activos restaurados y de los controles de monitoreo antes de normalizar la operación. | Restauración certificada de `DefaultAuditSet = Admin, Delegate, Owner` (más `SearchQueryInitiated`) y verificación tras cese de ventana `IsThrottled` de 24 h. | N/A (Restauración de Telemetría Post-Incidente) | Salida post-incidente de `Get-Mailbox` y validación de ingesta normalizada `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.CO-03` | Se comunica con precisión demostrable el alcance de exposición a reguladores, clientes y partes interesadas. | Prueba pericial basada en `MailItemsAccessed` y `SensitivityLabel` que demuestra qué elementos exactos fueron o **no fueron** accedidos hasta 10 años atrás. | N/A (Defensa Regulatoria y Notificación de Brecha) | Informe pericial de cierre y resultados trimestrales de recuperación histórica `T-01` `[Decisión / Propuesta Editorial]`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta de Aprendizaje Oficial y Recursos Recomendados (Vigentes a Nov-2026) | Credencial / Validación Práctica |
| :--- | :--- | :--- |
| **DFIR Analyst / SOC L2-L3 / Threat Hunter** | - Módulo MS Learn: *Investigate threats by using audit features in Microsoft Defender XDR and Microsoft Purview (Standard and Premium)* `[Verificado MS Learn]`.<br>- Guía oficial MS Learn: *Use MailItemsAccessed to investigate compromised accounts* y *Respond to a compromised email account in Microsoft Defender for Office 365* `[Verificado MS Learn]`.<br>- Referencia API: *Microsoft Graph security auditLogQuery resource type (v1.0)* `[Verificado MS Learn]`. | **Microsoft Certified: Security Operations Analyst Associate (SC-200)** + simulacro práctico semestral `SM-01` de reconstrucción BEC `[Verificado MS Learn]`. |
| **Purview Compliance Admin / Platform Engineer** | - Documentación MS Learn: *Learn about auditing solutions in Microsoft Purview*, *Manage audit log retention policies* y *Manage mailbox auditing* `[Verificado MS Learn]`.<br>- *Microsoft Purview eDiscovery and Audit Ninja Training* actualizado al portal Purview 2026 `[Verificado MS Learn]`. | **Microsoft Certified: Information Security Administrator Associate (SC-401)** + **Applied Skills APL-5007** (para ecosistema eDiscovery/retención conexo) `[Verificado MS Learn]`. |
| **AI Security & Governance Specialist** | - Documentación MS Learn: *Audit logs for Copilot and AI applications* (`CopilotInteraction`, `AccessedResources`, `XPIADetected`) y *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365* `[Verificado MS Learn]`. | Laboratorio interno de trazabilidad forense de prompts, *grounding* y agentes autónomos `[Decisión / Propuesta Editorial]`. |
| **Legal / eDiscovery & GRC Auditor** | - Documentación MS Learn: *Search the audit log* y *Export, configure, and view audit log records* (transformación Power Query de `AuditData`) `[Verificado MS Learn]`.<br>- Marco *Electronic Discovery Reference Model (EDRM 2.0, 2026)* y guía CISA M-24-04 `[Verificado MS Learn]`. | Ejecución trimestral certificada de extracción multianual (`T-01`) y control *Auditing the Auditors* (`M-05`) `[Decisión / Propuesta Editorial]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Verificadas contra Microsoft Learn MCP al `2026-11-11`

| # | Área Técnica | Hallazgo Verificado a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **GA de Graph `AuditLogQuery` y Retiro de `Search-UnifiedAuditLog` (`MC1505599`)** | El 12 de octubre de 2026 Microsoft anunció la disponibilidad general (GA) de **Microsoft Graph `AuditLogQuery` API** (`v1.0/security/auditLog/queries`, exportando hasta 1 millón de registros por consulta con permisos granulares por carga) y el **retiro definitivo de `Search-UnifiedAuditLog` el 15 de octubre de 2027** sin opción de prórroga por tenant `[Verificado MS Learn]`. | Toda la automatización en Sección 10, cadencia `S-04` y `KPI-04` se estructuran sobre Graph `AuditLogQuery` v1.0. |
| **2** | **Ampliación de Audit (Standard) a 180 Días y 4 Eventos Forenses (SFI / Roadmap 380690)** | Desde el 17 de octubre de 2023 Audit (Standard) retiene 180 días (antes 90), y entre febrero y junio de 2024 Microsoft liberó `MailItemsAccessed`, `Send`, `SearchQueryInitiatedExchange` y `SearchQueryInitiatedSharePoint` a usuarios Standard; sin embargo, **Audit (Premium)** conserva la exclusividad de **1 año por defecto**, políticas personalizadas hasta **10 años**, **`SensitivityLabel` en `MailItemsAccessed`**, **`AppAccessContext` en Teams** y **~2x ancho de banda API** `[Verificado MS Learn]`. | Reflejado con rigor exacto en la tabla comparativa de Sección 2.1 evitando afirmaciones obsoletas pre-2024. |
| **3** | **Asimetría de Activación entre `SearchQueryInitiatedSharePoint` y `Exchange`** | Microsoft Learn (`audit-get-started`) confirma que **`SearchQueryInitiatedSharePoint` está habilitado por defecto**, pero **`SearchQueryInitiatedExchange` debe habilitarse explícitamente por buzón** (`Set-Mailbox -AuditOwner @{Add="SearchQueryInitiated"}`) en el bosque regional del buzón, lo cual además retira `Owner` de `DefaultAuditSet` `[Verificado MS Learn]`. | Incorporados procedimientos semanales `S-02` y mensuales `M-01` para evitar perder búsquedas en OWA/Outlook o nuevas acciones por defecto. |
| **4** | **Regla Fija de 1 Año para Entidades No-Usuario y No-Retroactividad** | MS Learn (`audit-solutions-overview`) documenta que las actividades de **entidades no humanas** (*service principals*, apps, eventos de sistema) se retienen por un **período fijo no configurable de 1 año** (las políticas de 10 años no les aplican) y que el tiempo de vida se fija al ingresar al pipeline sin efecto retroactivo `[Verificado MS Learn]`. | Creado control mensual `M-02` para retener logs de principales de servicio > 1 año en **Microsoft Sentinel Data Lake** (hasta 12 años). |
| **5** | **Trampa Crítica de `Get-AdminAuditLogConfig` en SCC PowerShell y Multi-Geo** | En Security & Compliance PowerShell, `UnifiedAuditLogIngestionEnabled` devuelve siempre `False` incluso cuando la auditoría está encendida (debe consultarse en **Exchange Online PowerShell**); además, en entornos Multi-Geo no se registran acciones delegadas cross-geo en el log de buzones compartidos `[Verificado MS Learn]`. | Advertencia explícita incorporada en prerrequisitos, `D-01`, `M-01` y Consulta 4. |
| **6** | **Esquema Forense de IA (`CopilotInteraction`, `XPIADetected`, PAYG y Agent 365)** | MS Learn (`audit-copilot` y `ai-agent-365`, actualizados may–ago 2026) confirma auditoría automática en Audit Standard para apps IA de Microsoft y agentes de **Microsoft Agent 365** (incluyendo humano-agente, agente-herramienta y agente-agente), banderas **`XPIADetected`** y **`JailbreakDetected`**, máscara de bits **`DLPEvaluationDeferred`** y facturación **Pay-As-You-Go** (180 días) para `AIAppInteraction` de terceros `[Verificado MS Learn]`. | Integrado en `D-04`, `D-08`, `S-05`, `AH-02` y Consulta 3. |
| **7** | **Mecánica de Estrangulamiento `MailItemsAccessed` (> 1.000 en 24 h)** | Superar 1.000 registros `MailItemsAccessed` en menos de 24 horas activa `IsThrottled = True` y suspende su registro en ese buzón por 24 horas `[Verificado MS Learn]`. | Operacionalizado como detección diaria de exfiltración (`D-02`, Consulta 2) y regla de presunción en `AH-01`. |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas

| # | Elemento Editorial | Clasificación | Justificación Arquitectónica y Operativa |
| :--- | :--- | :--- | :--- |
| **1** | **Estrategia híbrida Purview Audit 10-Year (usuarios) + Sentinel Data Lake (Service Principals > 1 año)** | `[Decisión / Propuesta Editorial]` | Resuelve de forma arquitectónica la limitación oficial de 1 año fijo en entidades no-usuario dentro de Purview Audit para organizaciones sujetas a mandatos de 3 a 10 años. |
| **2** | **Fecha límite interna Q2 2027 para completar el 100 % de migración a Graph `AuditLogQuery`** | `[Decisión / Propuesta Editorial]` | Otorga un colchón seguro de 4 meses de pruebas paralelas antes del apagado definitivo de `Search-UnifiedAuditLog` el 15 de octubre de 2027 (`MC1505599`). |
| **3** | **Habilitación proactiva de `SearchQueryInitiatedExchange` con auditoría compensatoria mensual de `DefaultAuditSet`** | `[Decisión / Propuesta Editorial]` | Permite capturar qué buscó un atacante en el buzón sin quedar desprotegido ante nuevas acciones de buzón que Microsoft añada en el futuro al conjunto predeterminado. |
| **4** | **Catálogo de 8 KPIs (`KPI-01` a `KPI-08`), SLA de 30 min ante `IsThrottled` y Modelo de Madurez de 5 niveles** | `[Decisión / Propuesta Editorial]` | Traduce capacidades de logging pasivo en disciplina operativa medible para el SOC y GRC. |
| **5** | **Control mensual *Auditing the Auditors* (`M-05`) y mapeo completo a las 6 funciones de NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Asegura gobernanza ética sobre quién consulta el registro unificado y alinea la evidencia forense con auditorías internacionales. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Learn about auditing solutions in Microsoft Purview (Standard vs. Premium & 10-Year Retention)*: `https://learn.microsoft.com/en-us/purview/audit-solutions-overview` `[Verificado MS Learn]`
- **REF-02:** Microsoft Learn — *Get started with auditing solutions (Roles, Advanced Auditing Service Plan & SearchQueryInitiated)*: `https://learn.microsoft.com/en-us/purview/audit-get-started` `[Verificado MS Learn]`
- **REF-03:** Microsoft Learn — *Manage audit log retention policies (Default 1-Year, Custom Policies up to 50 & 10-Year Add-on)*: `https://learn.microsoft.com/en-us/purview/audit-log-retention-policies` `[Verificado MS Learn]`
- **REF-04:** Microsoft Learn — *Manage mailbox auditing (DefaultAuditSet, Actions, Bypass & Multi-Geo)*: `https://learn.microsoft.com/en-us/purview/audit-mailboxes` `[Verificado MS Learn]`
- **REF-05:** Microsoft Learn — *Use MailItemsAccessed to investigate compromised accounts (Bind vs. Sync & Deduplication)*: `https://learn.microsoft.com/en-us/purview/audit-log-investigate-accounts` `[Verificado MS Learn]`
- **REF-06:** Microsoft Learn — *Search the audit log (Asynchronous Search Jobs, 10 Concurrent Limit & 180-Day Range)*: `https://learn.microsoft.com/en-us/purview/audit-search` `[Verificado MS Learn]`
- **REF-07:** Microsoft Learn — *Audit logs for Copilot and AI applications (CopilotInteraction, AccessedResources, XPIADetected, PAYG)*: `https://learn.microsoft.com/en-us/purview/audit-copilot` `[Verificado MS Learn]`
- **REF-08:** Microsoft Learn — *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365*: `https://learn.microsoft.com/en-us/purview/ai-agent-365` `[Verificado MS Learn]`
- **REF-09:** Microsoft Learn — *auditLogQuery resource type — Microsoft Graph v1.0*: `https://learn.microsoft.com/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-1.0` `[Verificado MS Learn]`
- **REF-10:** Microsoft Learn — *Create auditLogQuery (`POST /security/auditLog/queries` & Service-Level Permissions) — Microsoft Graph v1.0*: `https://learn.microsoft.com/en-us/graph/api/security-auditcoreroot-post-auditlogqueries?view=graph-rest-1.0` `[Verificado MS Learn]`
- **REF-11:** Microsoft Learn — *Audit log activities (Complete Catalog of Audited Operations)*: `https://learn.microsoft.com/en-us/purview/audit-log-activities` `[Verificado MS Learn]`
- **REF-12:** Microsoft Learn — *Microsoft services that support auditing (`AuditLogRecordType` mapping)*: `https://learn.microsoft.com/en-us/purview/audit-supported-services` `[Verificado MS Learn]`
- **REF-13:** Microsoft Learn — *Respond to a compromised email account in Microsoft 365 (Defender for Office 365 BEC Playbook)*: `https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account` `[Verificado MS Learn]`
- **REF-14:** Microsoft Learn — *Office 365 Management Activity API reference (High-Bandwidth Tenant Throttling)*: `https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference` `[Verificado MS Learn]`
- **REF-15:** Microsoft Learn — *Learn about Microsoft Purview billing models (Pay-As-You-Go Non-Microsoft AI Audit Records)*: `https://learn.microsoft.com/en-us/purview/purview-billing-models` `[Verificado MS Learn]`

### 15.2 Blogs Oficiales Microsoft, Repositorios Oficiales y Message Center
- **REF-16:** Microsoft 365 Message Center Archive (Merill Fernando, Microsoft) — *MC1505599: Microsoft Purview Audit: AuditLogQuery API generally available and Search-UnifiedAuditLog retiring (Oct 15, 2027)*: `https://mc.merill.net/message/MC1505599` `[Verificado MS Learn]`
- **REF-17:** Microsoft Official Hunting Repository — *MailItemsAccessed Throttling (>1,000 events in 24h) [Nobelium]*: `https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/master/Exfiltration/MailItemsAccessed%20Throttling%20%5BNobelium%5D.md` `[Verificado MS Learn]`
- **REF-18:** Exchange Team Blog (Microsoft Tech Community) — *Contextualizing attacker activity within sessions in Exchange Online (`SessionId`)*: `https://techcommunity.microsoft.com/t5/exchange-team-blog/contextualizing-attacker-activity-within-sessions-in-exchange/ba-p/608801` `[Verificado MS Learn]`

### 15.3 Marcos Normativos y Directrices Forenses Cloud
- **REF-19:** NIST — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* y *CISA Cloud Security Technical Reference Architecture / M-24-04 Logging Guidance*: `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` `[Verificado MS Learn]`

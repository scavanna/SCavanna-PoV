# Microsoft Defender for Office 365 (Plan 1 y Plan 2) — Guía Maestra de Excelencia Operacional

## 1. Portada y Ficha de Control Documental

| Atributo | Valor |
|---|---|
| **Identificador del Módulo** | `05_Microsoft_Defender_for_Office_365` |
| **Nombre Oficial** | Microsoft Defender for Office 365 (Plan 1 y Plan 2) |
| **Categoría** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 (Edición Canónica Consolidada) |
| **Origen y Trazabilidad** | Compilado MSEOP-MD + Revalidado Learn |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Relación con Microsoft 365 E5** | Incluido íntegramente (Plan 2) en Microsoft 365 E5, Office 365 E5, Microsoft 365 A5/G5 y Microsoft Defender Suite (antes M365 E5 Security). Plan 1 incluido en Microsoft 365 E3 y Office 365 E3 desde julio de 2026 `[Verificado MS Learn]` |
| **Portales Principales** | `https://security.microsoft.com`, `https://admin.exchange.microsoft.com`, `https://purview.microsoft.com`, `https://entra.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Analistas SOC (L1, L2, L3), Incident Responders, Messaging & Collaboration Security Engineers, Identity/Security Admins, Auditores GRC |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST SP 800-61 Rev. 3, MITRE ATT&CK Enterprise, Microsoft Zero Trust & Security Adoption Framework (SAF), CIS Controls v8 |

> **Regla de separación evidencial:** En esta guía se distingue explícitamente mediante `[Verificado MS Learn]` todo comportamiento técnico, requisito de licencia, ruta de consola, tabla KQL, permiso RBAC y recomendación oficial verificada en Microsoft Learn a noviembre de 2026; y mediante `[Decisión / Propuesta Editorial]` los umbrales numéricos de SLA/KPI, matrices RACI organizacionales, modelos de madurez consultivos y mapeos interpretativos de resultados hacia NIST CSF 2.0.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust y Microsoft 365 E5

Microsoft Defender for Office 365 (MDO) constituye la plataforma nativa de protección, detección, investigación automatizada, respuesta y resiliencia humana para el plano de correo electrónico y colaboración empresarial (Exchange Online, Microsoft Teams, SharePoint Online, OneDrive for Business y aplicaciones de Microsoft 365) dentro de **Microsoft Defender XDR** `[Verificado MS Learn]`.

El correo electrónico y la mensajería colaborativa continúan representando el vector de acceso inicial predominante en campañas de robo de credenciales (Adversary-in-the-Middle / AiTM), fraude financiero mediante Business Email Compromise (BEC), distribución de código malicioso evasivo (HTML Smuggling, códigos QR maliciosos / *quishing*, cargas útiles con retardo o *time-bomb URLs*) e inyección de instrucciones (*prompt injection*) dirigida a asistentes de IA `[Verificado MS Learn]`. Operar MDO como un filtro perimetral aislado es insuficiente: la excelencia operacional exige integrarlo como fuente primaria de señal dentro de la cola unificada de incidentes de Defender XDR y Microsoft Sentinel `[Verificado MS Learn]`.

### 2.1 Arquitectura en Capas Acumulativas: EOP, MDO Plan 1 y MDO Plan 2

Microsoft estructura la defensa de colaboración en tres niveles acumulativos `[Verificado MS Learn]`:

| Nivel | Propósito Operativo | Capacidades Verificadas a Noviembre de 2026 | Estado en Licenciamiento Empresarial |
|---|---|---|---|
| **Exchange Online Protection (EOP)** | Higiene perimetral y autenticación base | Filtrado antispam y antimalware por reputación/firmas, autenticación SPF/DKIM/DMARC/ARC, *Secure by Default* (cuarentena obligatoria para malware y phishing de alta confianza), ZAP básico en correo `[Verificado MS Learn]` | Incluido en toda suscripción con buzones en Exchange Online `[Verificado MS Learn]` |
| **MDO Plan 1** | Prevención avanzada pre-entrega y *time-of-click* | *Safe Attachments* (detonación sandbox en correo, SPO, ODB y Teams), *Safe Links* (*time-of-click* en correo, Teams y apps Office), anti-phishing con ML, protección de suplantación (usuario/dominio), *Preset Security Policies* (Standard/Strict), *Real-time detections*, **ZAP para Microsoft Teams**, cuarentena administrada de Teams y reportes de usuarios en Teams (incorporados a P1 en enero-febrero de 2026) `[Verificado MS Learn]` | Incluido en **Microsoft 365 Business Premium** y, desde **julio de 2026**, incluido en **Microsoft 365 E3 y Office 365 E3** (además de complemento independiente) `[Verificado MS Learn]` |
| **MDO Plan 2** | Plataforma completa SOC-ready y XDR-ready | Todo Plan 1 más *Threat Explorer*, *Automated Investigation and Response (AIR)* con auto-remediación de clústeres maliciosos, *Campaign Views*, *Attack Simulation Training (AST)*, tablas completas de *Advanced Hunting* (incluyendo `MessageEvents` y `CallActivityEvents`), expulsión administrativa de usuarios en chats de Teams y elegibilidad para *Safe Documents* `[Verificado MS Learn]` | Incluido en **Microsoft 365 E5**, **Microsoft 365 E7**, **Office 365 E5**, **Microsoft 365 A5/G5**, **Microsoft Defender Suite** (nombre vigente de M365 E5 Security) o complemento MDO Plan 2 `[Verificado MS Learn]` |

> **Nota crítica de licenciamiento (Noviembre 2026):** *Safe Documents* requiere específicamente **Microsoft 365 E5** o **Microsoft Defender Suite** (no se incluye en la licencia independiente de MDO Plan 2 ni en Office 365 E5). Asimismo, las organizaciones en Microsoft 365 E3 disponen desde julio de 2026 de MDO Plan 1 (*Real-time detections*), pero carecen de *Threat Explorer*, *AIR* y campañas completas de *Attack Simulation Training*, capacidades indispensables para un SOC empresarial maduro `[Verificado MS Learn]`.

### 2.2 Posicionamiento en los Tres Principios de Zero Trust

1. **Verificar explícitamente (*Verify Explicitly*):** Validación criptográfica y compuesta del remitente (`SPF`, `DKIM`, `DMARC`, `ARC` y `compauth`), detonación dinámica previa a la entrega en *Safe Attachments*, evaluación en tiempo de clic de cada URL en correo, documentos y Teams mediante *Safe Links*, y clasificación contextual asistida por modelos de lenguaje (LLM/SLM) para ataques BEC sin enlaces ni adjuntos `[Verificado MS Learn]`.
2. **Usar acceso de mínimo privilegio (*Use Least Privilege Access*):** Gobernanza del equipo SecOps mediante **Microsoft Defender Unified RBAC (URBAC)** (predeterminado para nuevas organizaciones MDO P2 desde julio de 2026), separación estricta de permisos de previsualización de contenido y purga de buzones (*Search and Purge*), y elevación temporal Just-in-Time (JIT) con **Microsoft Entra Privileged Identity Management (PIM)** `[Verificado MS Learn]`.
3. **Asumir brecha (*Assume Breach*):** Purga retroactiva automatizada mediante **Zero-hour Auto Purge (ZAP)** en correo (ventana de 48 horas) y Microsoft Teams, investigaciones automatizadas **AIR** con remediación a escala organizacional por clústeres de similitud, contención coordinada con Entra ID y Defender for Endpoint ante robo de tokens, y trazabilidad forense completa en *Advanced Hunting* `[Verificado MS Learn]`.

### 2.3 Prerrequisitos Técnicos y Operativos Obligatorios

- **Autenticación de correo en dominios propios:** Configuración validada de registros DNS `SPF`, firma `DKIM` de 2048 bits habilitada por dominio personalizado, política `DMARC` en progresión hacia `p=reject` con buzones de reportes `rua`, y configuración de *Trusted ARC Sealers* únicamente cuando existan intermediarios legítimos que modifiquen mensajes en tránsito `[Verificado MS Learn]`.
- **Auditoría unificada activa:** El registro de auditoría de Microsoft Purview debe encontrarse habilitado (activo por defecto), siendo requisito técnico obligatorio para la ejecución de **AIR** en MDO Plan 2 `[Verificado MS Learn]`.
- **Protección de colaboración activada:** Habilitación explícita de *Safe Attachments for SharePoint, OneDrive, and Microsoft Teams* y del interruptor **Zero-hour auto purge (ZAP)** en `Settings > Email & collaboration > Microsoft Teams protection` `[Verificado MS Learn]`.
- **Configuración de reportes de usuario (Outlook y Teams):** Destino configurado hacia *Microsoft and my reporting mailbox* tanto para correo (`security.microsoft.com/securitysettings/userSubmission`) como en la página independiente de Microsoft Teams (`security.microsoft.com/securitysettings/teamsUserSubmission`, separada desde septiembre de 2026) `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Flujo Secuencial de Inspección y Ciclo Operativo de Cinco Capas

```
[Tráfico Entrante / Interno / Colaboración Teams-SPO-ODB]
       │
       ▼
[1. Perímetro y Autenticación EOP] ──► Reputación IP/Dominio · SPF/DKIM/DMARC/ARC · CompAuth · Antimalware por firmas
       │
       ▼
[2. Prevención Zero-Day MDO P1/P2] ──► Safe Attachments (Sandbox / Dynamic Delivery) · Safe Links (URLs + QR Codes)
       │
       ▼
[3. Inteligencia Anti-Phishing/IA] ──► User/Domain Impersonation · Mailbox Intelligence · LLM BEC · Prompt Injection · Mail Bombing
       │
       ▼
[4. Protección Post-Entrega]       ──► ZAP Correo (48h) · ZAP Teams (Chats internos / Canales estándar y compartidos) · Reclasificación URL
       │
       ▼
[5. Detección, AIR y Respuesta XDR]──► Threat Explorer · AIR Auto-remediation Clusters · Security Alert Triage Agent · Defender XDR / Sentinel
```

El modelo operativo del SOC sobre MDO se organiza en cinco capas funcionales `[Verificado MS Learn]`:

1. **PREVENT:** Controles preventivos gobernados por *Preset Security Policies* (`Standard` y `Strict`), *Built-in protection*, autenticación DMARC/DKIM/SPF y bloqueo táctico en *Tenant Allow/Block List (TABL)* `[Verificado MS Learn]`.
2. **DETECT:** Correlación nativa en incidentes de Defender XDR, *Real-time detections* / *Threat Explorer*, *Campaign Views*, detecciones de *Mail Bombing* e inyección de prompts, y reportes de usuarios `[Verificado MS Learn]`.
3. **INVESTIGATE:** Análisis profundo con *Threat Explorer*, *Email entity page* (con resumen generativo de Security Copilot), *Teams message entity panel*, *Teams call entity panel* y cacería KQL sobre 30 días en *Advanced Hunting* (o retención extendida en Microsoft Sentinel) `[Verificado MS Learn]`.
4. **RESPOND:** *AIR* con auto-remediación de clústeres de URLs y archivos, aprobación controlada en *Action Center*, *Soft/Hard Delete*, bloqueo de dominios/remitentes externos en Teams, expulsión de usuarios en chats de Teams y revocación de sesiones en Entra ID `[Verificado MS Learn]`.
5. **IMPROVE:** *Configuration Analyzer* (y herramienta PowerShell `ORCA`), *Policy What-If insights* (BCL, spoof e impersonation), *Microsoft Secure Score* y ciclos continuos de *Attack Simulation Training* `[Verificado MS Learn]`.

### 3.2 Componentes Técnicos Clave Verificados (Noviembre 2026)

| Componente | Función Operativa Principal | Ruta en Portal | Disponibilidad |
|---|---|---|---|
| **Preset Security Policies (Standard / Strict)** | Aplica y mantiene actualizados automáticamente los perfiles recomendados por Microsoft para antispam, antimalware, anti-phishing, Safe Links y Safe Attachments, evitando deriva de configuración | `security.microsoft.com/presetSecurityPolicies` | MDO P1 / P2 `[Verificado MS Learn]` |
| **Safe Attachments & Dynamic Delivery** | Detona adjuntos desconocidos en hipervisor aislado antes de la entrega; *Dynamic Delivery* entrega el cuerpo con marcador mientras finaliza el escaneo; extiende protección asíncrona a SPO, ODB y Teams | `security.microsoft.com/safeattachmentv2` | MDO P1 / P2 `[Verificado MS Learn]` |
| **Safe Links (Correo, Teams y Apps Office)** | Verificación síncrona en tiempo de clic de URLs (incluyendo URLs extraídas de códigos QR) con advertencias casi en tiempo real en Teams hasta 48h post-entrega | `security.microsoft.com/safelinksv2` | MDO P1 / P2 `[Verificado MS Learn]` |
| **Zero-hour Auto Purge (ZAP) en Correo y Teams** | Purga retroactiva (48h) de malware, phishing y spam en buzones Exchange Online (incluyendo *Deleted Items* y buzones en *Hold*), y cuarentena automática de malware y phishing de alta confianza en chats internos y canales estándar/compartidos de Teams | `security.microsoft.com/securitysettings/teamsProtectionPolicy` | Correo: EOP+ / Teams: MDO P1 y P2 `[Verificado MS Learn]` |
| **Threat Explorer y Campaign Views** | Búsqueda interactiva de 30 días (filtros por URL de QR, tecnología de detección como *Mail bombing*, veredictos, overrides), visualización Sankey de campañas y ejecución directa de *Take action* | `security.microsoft.com/threatexplorer` / `security.microsoft.com/campaigns` | MDO P2 (*Real-time detections* en P1) `[Verificado MS Learn]` |
| **Automated Investigation & Response (AIR)** | Ejecuta playbooks organizacionales ante alertas, ZAP, clics o envíos de usuario; auto-aprueba la remediación de clústeres de similitud maliciosos (URL/archivo) y cierra alertas sin amenaza | `security.microsoft.com/airinvestigation` / `security.microsoft.com/action-center` | MDO P2 `[Verificado MS Learn]` |
| **Priority Account Protection** | Etiqueta hasta 250 cuentas críticas (alta dirección, finanzas, tesorería) aplicando heurísticas específicas contra BEC ejecutivo, filtros de incidentes dedicados e informes de flujo prioritario | `security.microsoft.com/securitysettings/userTags` | MDO P1 / P2 (heurísticas avanzadas en P2) `[Verificado MS Learn]` |
| **Attack Simulation Training (AST)** | Simulación de técnicas reales (Credential Harvest, Malware Attachment, Link in Attachment, Link to Malware, Drive-by URL, OAuth Consent Grant, How-to Guide y códigos QR) con asignación adaptativa de formación | `security.microsoft.com/attacksimulator` | MDO P2 / M365 E5 `[Verificado MS Learn]` |

### 3.3 Integraciones con el Ecosistema Microsoft Security y Agentes IA

- **Microsoft Defender XDR:** Correlación nativa de alertas e investigaciones AIR de MDO con *Defender for Endpoint*, *Defender for Identity*, *Defender for Cloud Apps* y *Microsoft Entra ID Protection* en un único incidente multi-dominio, alimentando **Automatic Attack Disruption** ante compromisos de alta confianza `[Verificado MS Learn]`.
- **Microsoft Sentinel:** Ingesta sin cargo adicional de alertas e incidentes XDR, e ingesta configurable de tablas crudas (`EmailEvents`, `EmailAttachmentInfo`, `EmailUrlInfo`, `EmailPostDeliveryEvents`, `UrlClickEvents`, `MessageEvents`, `CallActivityEvents`) mediante el conector de Defender XDR en el portal unificado `[Verificado MS Learn]`.
- **Microsoft Entra ID:** Correlación con registros de inicio de sesión (`EntraIdSignInEvents`), revocación de sesiones ante clics permitidos en campañas AiTM y gobierno PIM para administradores y analistas con permisos de purga `[Verificado MS Learn]`.
- **Microsoft Purview:** Integración con auditoría unificada (`MailItemsAccessed`, `New-InboxRule`), retenciones legales (*Litigation Hold* compatible con cuarentena ZAP) y búsquedas de contenido multi-buzón en `purview.microsoft.com` `[Verificado MS Learn]`.
- **Microsoft Security Copilot y Agentes Autónomos:**
  - **Security Alert Triage Agent** (evolución del *Phishing Triage Agent*, GA para correo reportado por usuarios): clasifica autónomamente envíos de usuarios con razonamiento transparente consumiendo Security Compute Units (SCU; Microsoft 365 E5 incluye 400 SCU/mes por cada 1.000 licencias pagas, hasta 10.000 SCU). **Requisito crítico:** requiere URBAC activo y deshabilitar la regla integrada de *Alert tuning* `Auto-Resolve - Email reported by user as malware or phish` `[Verificado MS Learn]`.
  - **Resumen generativo en Email Entity Page:** Disponible desde abril de 2026 mediante la acción *Copilot* para sintetizar encabezados, autenticación, detonación y contexto de campaña `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM y JIT)

### 4.1 Transición Obligatoria a Microsoft Defender Unified RBAC (URBAC)

Desde **julio de 2026 (MC1246006)**, **Microsoft Defender Unified RBAC (URBAC)** es el modelo de permisos predeterminado para todas las organizaciones nuevas de MDO Plan 2 y el modelo recomendado por Microsoft para organizaciones existentes `[Verificado MS Learn]`.

Aspectos críticos de diseño verificados en Microsoft Learn `[Verificado MS Learn]`:
1. Al activar URBAC para *Email & collaboration*, la página heredada `https://security.microsoft.com/emailandcollabpermissions` deja de estar disponible en el portal Defender; por ello, los roles personalizados deben diseñarse o importarse **antes** de activar URBAC.
2. URBAC gobierna el portal `security.microsoft.com`, pero **no reemplaza** los permisos de Exchange Online PowerShell ni los roles específicos de *Attack Simulation Training* en Entra ID.
3. El rol `Security Operator` de Microsoft Entra ID **no** concede por sí solo permisos para administrar *Tenant Allow/Block List* si no se usa URBAC o el grupo de roles `Security Operator` de Exchange Online (`Tenant AllowBlockList Manager`).

### 4.2 Permisos Clave en URBAC y Roles Complementarios

| Capacidad Operativa | Permiso Granular URBAC (Portal Defender) | Rol Equivalente Entra ID / Exchange Online / Purview |
|---|---|---|
| Leer metadatos y encabezados de correo y Teams (`EmailEvents`, `MessageEvents`, `UrlClickEvents`) | `Security operations > Raw data (email & collaboration) > Email & collaboration metadata (read)` | `Security Reader` / `Security Operator` `[Verificado MS Learn]` |
| Previsualizar y descargar mensajes asociados exclusivamente a alertas | `Security operations > Raw data (email & collaboration) > Email & collaboration content: Emails associated with alerts (read)` (añadido en abril de 2026) | Rol `Preview` acotado `[Verificado MS Learn]` |
| Previsualizar y descargar cualquier mensaje en Threat Explorer / Email Entity Page | `Security operations > Raw data (email & collaboration) > Email & collaboration content (read)` | Rol `Preview` (asignado por defecto a `Data Investigator` y `eDiscovery Manager`) `[Verificado MS Learn]` |
| Iniciar AIR, aprobar/rechazar acciones pendientes y remediar/purgar mensajes | `Security operations > Security data > Email & collaboration advanced actions (manage)` | Rol `Search and Purge` (en `Data Investigator` u `Organization Management`) `[Verificado MS Learn]` |
| Gestionar políticas de amenazas MDO y *Preset Security Policies* | `Authorization and settings > Security settings > Email & collaboration (manage)` | `Security Administrator` `[Verificado MS Learn]` |
| Administrar entradas en *Tenant Allow/Block List (TABL)* | Permisos de configuración de seguridad en URBAC | `Security Administrator` o rol `Tenant AllowBlockList Manager` en Exchange Online `[Verificado MS Learn]` |
| Crear, programar y revisar campañas de *Attack Simulation Training* | *No soportado en URBAC a nov 2026* | `Attack Simulation Administrator` / `Attack Payload Author` (Entra ID) `[Verificado MS Learn]` |

### 4.3 Matriz RBAC, Separación de Funciones (SoD) y Política PIM/JIT

Los tiempos máximos de activación PIM y la distribución por nivel SOC constituyen una `[Decisión / Propuesta Editorial]` alineada con el principio de mínimo privilegio de Microsoft (`pim-in-mdo-configure`):

| Nivel / Función | Rol Técnico Recomendado | Asignación en Entra PIM | Duración JIT y Aprobación | Responsabilidad y Límite de Separación de Funciones (SoD) |
|---|---|---|---|---|
| **SOC Tier 1 (L1 — Monitor & Triage)** | Rol URBAC custom *SOC L1 Email Analyst* (`Alerts manage` + `Email & collaboration metadata read`) | Activa permanente (sin acceso a cuerpo de correo ni purga) `[Decisión / Propuesta Editorial]` | N/A | Triaje inicial de incidentes, revisión de encabezados y escalamiento; **prohibido** descargar correos o ejecutar *Hard Delete* `[Decisión / Propuesta Editorial]` |
| **SOC Tier 2 (L2 — Responder)** | Rol URBAC custom *SOC L2 Collaboration Responder* (+ `Emails associated with alerts read` + `TABL`) | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · MFA resistente a phishing + justificación `[Decisión / Propuesta Editorial]` | Investigación en *Threat Explorer*, envíos a Microsoft, liberación validada de cuarentena, bloqueo táctico en TABL `[Verificado MS Learn]` |
| **SOC Tier 3 (L3 — Hunter & IR)** | Rol URBAC custom *SOC L3 Purge & Hunter* (`Email & collaboration content read` + `Email & collaboration advanced actions manage`) | Elegible en PIM (máx. 3-5 analistas titulares) `[Decisión / Propuesta Editorial]` | Máx. 4 h · MFA resistente a phishing + aprobación cruzada de SOC Lead `[Decisión / Propuesta Editorial]` | Cacería avanzada KQL, aprobación de purgas masivas (`Soft/Hard Delete`), expulsión de chats en Teams y contención BEC `[Verificado MS Learn]` |
| **Ingeniería / SecAdmin** | `Security Administrator` + `Exchange Recipient/Transport Admin` (solo para reglas ETR) | Elegible en PIM `[Verificado MS Learn]` | Máx. 4 h · MFA resistente a phishing + número de cambio `[Decisión / Propuesta Editorial]` | Configuración de *Preset Policies*, DMARC/DKIM/SPF, *Configuration Analyzer* y *User Tags*; sin auto-aprobación PIM `[Decisión / Propuesta Editorial]` |
| **Concientización / Riesgo Humano** | `Attack Simulation Administrator` / `Attack Payload Author` | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · Justificación de campaña `[Decisión / Propuesta Editorial]` | Diseño y ejecución de simulaciones AST sin privilegios sobre políticas productivas de filtrado `[Verificado MS Learn]` |
| **Auditoría / GRC / Privacidad** | `Global Reader` o `Security Reader` | Elegible en PIM `[Decisión / Propuesta Editorial]` | Máx. 8 h · Ticket de auditoría `[Decisión / Propuesta Editorial]` | Verificación independiente de políticas, métricas, *Action Center History* y campo `ApproverUpn` en solo lectura `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

> **Propósito:** Detectar compromisos post-clic, aprobar remediaciones pendientes antes de que aumente el tiempo de exposición y retroalimentar los modelos de detección. Las actividades provienen del *MDO Security Operations Guide* `[Verificado MS Learn]`; los SLAs objetivo son `[Decisión / Propuesta Editorial]`.

### D-01 — Triaje Priorizado de la Cola Unificada de Incidentes MDO/XDR
- **Consola / Ruta:** `https://security.microsoft.com/incidents` (`Investigation & response > Incidents & alerts > Incidents`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Filtrar `Status = New, In progress`, `Severity = High, Medium` y verificar incidentes con alertas originadas por *Microsoft Defender for Office 365* correlacionadas con Entra ID y MDE `[Verificado MS Learn]`.
  2. Aplicar estrictamente el **orden oficial de precedencia de triaje de Microsoft Learn** `[Verificado MS Learn]`:
     1) *A potentially malicious URL click was detected* (riesgo inminente de compromiso activo);
     2) *User restricted from sending email* (posible cuenta comprometida enviando spam/BEC);
     3) *Suspicious email sending patterns detected*;
     4) *Email reported by user / Multiple users reported email as malware or phish*;
     5) *Email messages containing malicious file/URL/campaign removed after delivery* (ZAP ejecutado);
     6) *Phish delivered due to an ETR override / Junk Mail disabled / IP allow policy*;
     7) *Malware or Phish not zapped because ZAP is disabled*.
  3. Asignar propietario, cambiar estado a `In progress` (meta MTTA < 15 min High / < 45 min Medium `[Decisión / Propuesta Editorial]`) y clasificar obligatoriamente al cierre (`True positive` con tipo de amenaza o `False positive`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación CSV de cola de incidentes, marca temporal de asignación, clasificación documentada y registro en `SecurityIncident`.

### D-02 — Revisión y Aprobación de Investigaciones AIR en Action Center
- **Consola / Ruta:** `https://security.microsoft.com/action-center/pending` y `https://security.microsoft.com/airinvestigation` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / SOC L3.
- **Procedimiento paso a paso:**
  1. Verificar que los clústeres de similitud maliciosos (URL y archivo) hayan sido auto-remediados correctamente en la pestaña `History` `[Verificado MS Learn]`.
  2. Inspeccionar la pestaña `Pending` para acciones que requieren validación humana (ej. purga de mensajes fuera de auto-remediación, desactivación de reenvío externo) antes de su expiración semanal `[Verificado MS Learn]`.
  3. Validar evidencia de detonación, encabezados `Authentication-Results` y alcance de destinatarios; aprobar (`Soft delete` por defecto) o rechazar si corresponde a falso positivo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial en `Action Center > History` y registro del campo `ApproverUpn` en la tabla `EmailPostDeliveryEvents` (incorporado en octubre de 2026) `[Verificado MS Learn]`.

### D-03 — Gestión de Envíos de Usuarios (Correo y Microsoft Teams) y Triaje Agéntico
- **Consola / Ruta:** `https://security.microsoft.com/reportsubmission?viewid=user` (`Actions & submissions > Submissions > User reported` y pestaña `User reported Teams messages`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Revisar las clasificaciones autónomas emitidas por el **Security Alert Triage Agent** (si Security Copilot está activo) y auditar una muestra diaria para retroalimentar su precisión `[Verificado MS Learn]`.
  2. Filtrar mensajes de correo y elementos de Teams (mensajes con contexto de +/-15 mensajes, llamadas 1:1/grupales y reuniones reportadas) con resultado *Should have been blocked* o sin veredicto `[Verificado MS Learn]`.
  3. Ejecutar *Submit to Microsoft for analysis* para falsos negativos o falsos positivos y accionar *Mark as and notify* (notificación localizada automáticamente según idioma de Outlook del usuario desde julio de 2026) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de envíos en portal *Submissions*, ID de análisis de Microsoft y trazas de notificación al usuario.

### D-04 — Administración de falsos positivos en Cuarentena (Email y Teams)
- **Consola / Ruta:** `https://security.microsoft.com/quarantine` (`Email & collaboration > Review > Quarantine > Email` y pestaña `Teams messages`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. Revisar solicitudes de liberación (*Release requests*); recordar que los destinatarios finales **nunca** pueden liberar por sí mismos mensajes clasificados como *Malware* o *High confidence phishing*, ni mensajes de Teams cuarentenados por ZAP `[Verificado MS Learn]`.
  2. Inspeccionar `compauth`, `SPF/DKIM/DMARC`, URLs y adjuntos mediante rol `Preview` / permiso URBAC correspondiente `[Verificado MS Learn]`.
  3. Si se confirma legítimo, ejecutar *Release message* marcando *Report message to Microsoft for analysis* (lo cual crea entrada temporal de 45 días tras último uso en TABL sin abrir brechas permanentes) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Detalle de quién liberó el mensaje en el panel de resumen de cuarentena y registro en `EmailPostDeliveryEvents` `[Verificado MS Learn]`.

### D-05 — Verificación y Desbloqueo Controlado de Entidades Restringidas
- **Consola / Ruta:** `https://security.microsoft.com/restrictedentities` (`Email & collaboration > Review > Restricted entities`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2.
- **Procedimiento paso a paso:**
  1. Identificar buzones restringidos automáticamente para envío saliente por volumen anómalo o spam (frecuente síntoma de BEC o token robado) `[Verificado MS Learn]`.
  2. Antes de desbloquear, ejecutar lista de verificación obligatoria: revocación de sesiones en Entra ID, restablecimiento de credenciales/MFA, eliminación de reglas de bandeja (`ForwardTo` / `RedirectTo`) y conectores ilícitos `[Verificado MS Learn]`.
  3. Desbloquear la cuenta confirmando mitigaciones e informar que la restitución del envío demora hasta 60 minutos; monitorear el buzón por 24 horas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de desbloqueo en *Restricted entities*, ticket de incidente vinculado y auditoría de buzón limpia.

### D-06 — Revisión Diaria de Campañas con Entrega Efectiva en Buzón
- **Consola / Ruta:** `https://security.microsoft.com/campaigns` (`Email & collaboration > Review > Campaigns`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2.
- **Procedimiento paso a paso:**
  1. Filtrar campañas de las últimas 24 horas donde existan mensajes en `Inbox` no purgados aún por ZAP o AIR `[Verificado MS Learn]`.
  2. Analizar el diagrama Sankey de flujo (IPs -> dominios -> veredicto -> clics permitidos vs bloqueados) `[Verificado MS Learn]`.
  3. Ejecutar purga masiva (`Soft delete`) de remanentes y agregar indicadores tácticos (URLs, hashes SHA256, dominios) en *Tenant Allow/Block List* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe descargado de campaña (*Download threat report*) y acciones completadas en *Action Center* `[Verificado MS Learn]`.

### D-07 — Validación de Acciones Post-Entrega ZAP y Clics Previos a la Purga
- **Consola / Ruta:** `https://security.microsoft.com/threatexplorer` y `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento paso a paso:**
  1. En *Threat Explorer* (vista *All email*), filtrar `Additional action = ZAP` en las últimas 24 horas, y cruzar con `EmailPostDeliveryEvents` y `MessagePostDeliveryEvents` `[Verificado MS Learn]`.
  2. Cruzar los `NetworkMessageId` / `TeamsMessageId` purgados con la tabla `UrlClickEvents` buscando eventos `ActionType == "ClickAllowed"` ocurridos **antes** de que ZAP neutralizara el mensaje `[Verificado MS Learn]`.
  3. Escalar inmediatamente a protocolo de contención de identidad cualquier usuario con clic permitido previo a ZAP `[Verificado MS Learn]`.
- **Evidencia Auditable:** Resultado de consulta KQL diaria de cruce ZAP vs `UrlClickEvents` archivado en el bitácora de turno `[Decisión / Propuesta Editorial]`.

### D-08 — Detección Temprana de Compromiso BEC, Mail Bombing y Reglas de Reenvío
- **Consola / Ruta:** `https://security.microsoft.com/threatexplorer` y `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2.
- **Procedimiento paso a paso:**
  1. Revisar en *Threat Explorer* detecciones clasificadas por filtros LLM de BEC, *Prompt injection* y ataques de *Mail bombing* (`Detection technology = Mail bombing`, precursor habitual de llamadas fraudulentas por Teams/vishing) `[Verificado MS Learn]`.
  2. Verificar alertas y eventos `CloudAppEvents` / auditoría Exchange de creación de reglas de bandeja con reenvío externo o borrado silencioso de correos financieros `[Verificado MS Learn]`.
  3. Ante confirmación de sospecha en cuenta ejecutiva (*Priority account*), activar de inmediato el Playbook `AH-02` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de revisión de detecciones BEC/Mail Bombing y alertas tratadas en el turno.

### D-09 — Higiene de Cierre de Turno y Handover Operacional SOC
- **Consola / Ruta:** `https://security.microsoft.com/incidents` y `https://security.microsoft.com/action-center/pending` `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** SOC L1 / SOC L2 / Shift Lead.
- **Procedimiento paso a paso:**
  1. Confirmar cero incidentes de severidad `High` en estado `New` sin analista asignado y cero acciones críticas de AIR próximas a vencer en `Pending` `[Decisión / Propuesta Editorial]`.
  2. Documentar en el acta de traspaso de turno campañas activas, entradas temporales agregadas a TABL y disputas de veredicto abiertas ante Microsoft (`Dispute submission`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora formal de entrega de turno firmada en herramienta ITSM/SOC `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

> **Propósito:** Ejecutar cacería proactiva, eliminar deriva de configuración, ajustar inteligencia de suplantación y evaluar amenazas emergentes `[Verificado MS Learn]`.

### S-01 — Análisis Semanal de Tendencias de Detección y Flujo de Correo
- **Consola / Ruta:** `https://security.microsoft.com/reports/TPSAggregateReportATP` y `https://security.microsoft.com/mailflowStatusReport?viewid=type` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Security Admin.
- **Procedimiento:** Comparar volúmenes semanales de malware, phishing de alta confianza, phishing por suplantación, spam y correo legítimo, así como anomalías de volumen saliente o picos de ZAP. Investigar variaciones superiores al 20% semanal `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación semanal de *Threat Protection Status Report* y *Mailflow Status Report* `[Verificado MS Learn]`.

### S-02 — Revisión de Threat Analytics y Bloqueo Proactivo de Campañas Emergentes
- **Consola / Ruta:** `https://security.microsoft.com/threatanalytics3` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Threat Hunter.
- **Procedimiento:** Analizar informes nuevos de analistas de Microsoft sobre campañas de phishing, AiTM, abuso de códigos QR o explotación en herramientas colaborativas; revisar *Related incidents*, verificar puntaje de exposición de configuraciones recomendadas y ejecutar las consultas KQL asociadas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de boletines *Threat Analytics* evaluados y consultas ejecutadas.

### S-03 — Revisión de Usuarios Más Atacados (Top Targeted Users) y Etiquetas Priority Accounts
- **Consola / Ruta:** `https://security.microsoft.com/threatexplorer` (pestaña `Top targeted users`) y `https://security.microsoft.com/securitysettings/userTags` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Security Admin.
- **Procedimiento:** Identificar los 20 buzones con mayor volumen de intentos de phishing y malware durante los últimos 7 días; incorporar nuevos ejecutivos, roles críticos de tesorería o blancos recurrentes a la etiqueta **Priority account** (respetando el límite de 250 cuentas y usando etiquetas personalizadas adicionales si se supera) y asegurar su inclusión en la política preestablecida **Strict** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Lista actualizada de *Priority accounts* e informe *Email issues for priority accounts* `[Verificado MS Learn]`.

### S-04 — Caza Proactiva (Threat Hunting) en Correo, Códigos QR y Microsoft Teams
- **Consola / Ruta:** `https://security.microsoft.com/threatexplorer` y `https://security.microsoft.com/v2/advanced-hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Threat Hunter.
- **Procedimiento:** Ejecutar hipótesis semanales sobre: 1) mensajes entregados en `Inbox` con adjuntos `.html`, `.htm`, `.iso`, `.lnk`, `.one` o PDFs con URLs de códigos QR; 2) enlaces externos compartidos en chats/reuniones de Teams (`MessageEvents`, `MessageUrlInfo`) y llamadas externas sospechosas (`CallActivityEvents`); 3) clics permitidos hacia dominios recién registrados `[Verificado MS Learn]`. Ejecutar *Take action* directamente desde *Advanced Hunting* (disponible desde finales de 2025) cuando se detecten amenazas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Consultas guardadas en *Shared queries* y registro de hallazgos/remediaciones.

### S-05 — Auditoría de Deriva de Configuración (Configuration Analyzer y ORCA)
- **Consola / Ruta:** `https://security.microsoft.com/configurationAnalyzer` y módulo PowerShell `ORCA` (`Get-ORCAReport`) `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin.
- **Procedimiento:** Evaluar desviaciones respecto a las líneas base **Standard** y **Strict** recomendadas por Microsoft; corregir cualquier debilitamiento no autorizado o documentar formalmente la excepción con fecha de caducidad `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/exportación del panel *Configuration Analyzer* con cero desvíos críticos no aprobados.

### S-06 — Curación de Spoof Intelligence e Impersonation Insights
- **Consola / Ruta:** `https://security.microsoft.com/spoofintelligence` y `https://security.microsoft.com/impersonationinsight` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / Messaging Engineer.
- **Procedimiento:** Revisar remitentes detectados suplantando dominios internos o externos en los últimos 7 días; bloquear dominios maliciosos y exigir a los propietarios de aplicaciones/proveedores legítimos que corrijan sus registros SPF/DKIM/DMARC en lugar de depender indefinidamente de entradas *Allowed to spoof* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de decisiones sobre remitentes suplantados y tickets de corrección DNS remitidos a propietarios de negocio.

### S-07 — Auditoría de Reglas de Transporte (ETR) y Sobrescrituras de Detección (System Overrides)
- **Consola / Ruta:** `https://security.microsoft.com/reports/TPSMessageOverrideReportATP` y `https://admin.exchange.microsoft.com/#/transportrules` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / Messaging Team.
- **Procedimiento:** Analizar correos maliciosos entregados por culpa de *overrides* (`Exchange transport rule`, `IP allow policy`, `User safe sender`, `Admin submission allow`); auditar reglas ETR buscando `Set SCL to -1` o reenvíos externos masivos y eliminar reglas sin aprobación vigente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de *System overrides* con plan de saneamiento y exportación de reglas de transporte activas.

---

## 7. Cadencia Operativa Mensual

> **Propósito:** Gobernar postura, afinar políticas con telemetría histórica, medir resiliencia humana y asegurar controles auditables de privilegio `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.

### M-01 — Revisión de Postura en Microsoft Secure Score (Email & Collaboration)
- **Consola / Ruta:** `https://security.microsoft.com/securescore` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / SOC Manager.
- **Procedimiento:** Filtrar acciones recomendadas por producto *Defender for Office 365*, evaluar la variación mensual de puntaje, priorizar controles pendientes de alto impacto y actualizar el plan de cierre de brechas con propietarios y fechas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación mensual de *Microsoft Secure Score* y tendencia de 30/90 días.

### M-02 — Ajuste Fino de Políticas Anti-Phishing y Anti-Spam con Policy What-If Insights
- **Consola / Ruta:** `https://security.microsoft.com/antiphishing` y `https://security.microsoft.com/antispam` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / Security Architect.
- **Procedimiento:** Utilizar *Policy what-if insights* para simular con datos históricos reales el impacto antes de modificar umbrales BCL (incluyendo entrega opcional a carpeta *Promotions* en Preview), suplantación o impersonación; validar umbrales de phishing avanzado (nivel 2 en Standard, 3-4 en Strict) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Capturas de evaluación *What-If* previas al cambio y registro de control de cambios aprobado.

### M-03 — Higiene Mensual de Tenant Allow/Block List (Correo y Dominios Externos Teams)
- **Consola / Ruta:** `https://security.microsoft.com/tenantAllowBlockList` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / SOC L2.
- **Procedimiento:** Auditar todas las pestañas (*Domains & addresses*, *Spoofed senders*, *URLs*, *Files*, *IPv4/IPv6* y dominios/direcciones bloqueadas para **Microsoft Teams**); verificar que las entradas *Allow* derivadas de envíos mantengan la caducidad predeterminada de **45 días tras el último uso** (`45 days after last used date`) y revocar entradas *Spoofed senders* sin expiración que ya hayan corregido DMARC `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación mensual de TABL y bitácora de depuración de excepciones.

### M-04 — Ejecución y Medición del Programa Mensual de Attack Simulation Training (AST)
- **Consola / Ruta:** `https://security.microsoft.com/attacksimulator` `[Verificado MS Learn]`.
- **Rol Responsable:** Attack Simulation Administrator / SOC Manager.
- **Procedimiento:** Revisar resultados de *Simulation Automations* del mes (incluyendo payloads con códigos QR, OAuth Consent y Credential Harvest), comparar *Actual Compromise Rate* contra *Predicted Compromise Rate*, medir tasa de reporte de usuarios y asignar *Training Campaigns* obligatorias a reincidentes (*Repeat Offenders*) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de cobertura, tasa de compromiso, tasa de reporte y porcentaje de finalización de entrenamiento.

### M-05 — Auditoría Mensual de Permisos URBAC, Grupos Search & Purge y Activaciones PIM
- **Consola / Ruta:** `https://security.microsoft.com/securitypermissions` y `https://entra.microsoft.com` (PIM Audit) `[Verificado MS Learn]`.
- **Rol Responsable:** Security Admin / GRC.
- **Procedimiento:** Verificar que no existan asignaciones permanentes no autorizadas en roles con permisos de purga o lectura masiva de contenido (`Email & collaboration content (read)` / `Search and Purge`); auditar el historial de activaciones PIM del mes contra tickets de incidentes reales y cruzar con el campo `ApproverUpn` en `EmailPostDeliveryEvents` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de revisión de accesos privilegiados y log de activaciones PIM.

### M-06 — Respaldo Versionado de Políticas MDO/EXO y Validación de Conectores Sentinel
- **Consola / Ruta:** Exchange Online PowerShell (`ExchangeOnlineManagement`) y portal Defender / Sentinel `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** Security Engineer / Platform Engineer.
- **Procedimiento:** Exportar mediante script automatizado las configuraciones actuales (`Get-AntiPhishPolicy`, `Get-SafeLinksPolicy`, `Get-SafeAttachmentPolicy`, `Get-HostedContentFilterPolicy`, `Get-MalwareFilterPolicy`, `Get-TeamsProtectionPolicy`, `Get-DkimSigningConfig`, `Get-TransportRule`) a un repositorio Git privado con control de integridad, y verificar la ingesta continua de tablas `Email*` y `Message*` en Microsoft Sentinel `[Verificado MS Learn]`.
- **Evidencia Auditable:** Commit mensual firmado en repositorio de respaldo y consulta de latencia de ingesta en Sentinel.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral) — Auditoría Integral de Autenticación de Dominios (SPF, DKIM, DMARC `p=reject` y ARC)
- **Consola / Ruta:** DNS Público, `https://security.microsoft.com/dkimv2` y reportes agregados DMARC `[Verificado MS Learn]`.
- **Rol Responsable:** Messaging Security Architect / Security Admin.
- **Procedimiento:** Auditar todos los dominios y subdominios corporativos (incluyendo dominios estacionados o sin envío de correo, publicando `v=spf1 -all` y `v=DMARC1; p=reject;`), rotar claves DKIM de 2048 bits según calendario criptográfico, avanzar dominios restantes de `p=none`/`p=quarantine` a `p=reject` y validar *Trusted ARC Sealers* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz trimestral de cumplimiento DNS/DMARC por dominio al 100%.

### T-02 (Trimestral) — Calibración de Reglas de Alert Tuning y Desempeño del Security Alert Triage Agent
- **Consola / Ruta:** `https://security.microsoft.com/securitysettings/defender/alert_suppression` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Lead / Detection Engineer.
- **Procedimiento:** Auditar reglas integradas y personalizadas de *Alert tuning*; confirmar que `Auto-Resolve - Email reported by user as malware or phish` permanezca deshabilitada cuando opere el *Security Alert Triage Agent*, revisar precisión de veredictos del agente y retirar reglas de supresión obsoletas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta trimestral de gobierno de *Alert tuning* e IA agéntica en el SOC `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral) — Recalibración de Cobertura Preset Security Policies (Standard vs Strict) y Cuarentena
- **Consola / Ruta:** `https://security.microsoft.com/presetSecurityPolicies` y `https://security.microsoft.com/quarantinePolicies` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Architect / CISO Office.
- **Procedimiento:** Evaluar la ampliación de la cobertura de la política **Strict** desde ejecutivos hacia áreas de alto riesgo (Finanzas, Compras, RR.HH., TI y Administradores), y auditar las políticas de notificación de cuarentena asegurando ausencia de permisos de liberación de usuario para phishing y malware `[Verificado MS Learn]`.
- **Evidencia Auditable:** Documento semestral de arquitectura de políticas firmado por CISO Office `[Decisión / Propuesta Editorial]`.

### A-01 (Anual) — Ejercicio Tabletop Multi-Dominio de BEC Ejecutivo, Quishing y Abuso de Teams
- **Consola / Ruta:** Ejercicio interdisciplinario (SOC, TI, Tesorería, Legal, Comunicaciones y Dirección) `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO / Incident Response Manager.
- **Procedimiento:** Ejecutar simulación de mesa inspirada en NIST SP 800-61 Rev. 3 combinando phishing AiTM por código QR, robo de sesión, creación de reglas ocultas de buzón, *Mail bombing* distractivo y contacto fraudulento por llamada externa de Microsoft Teams; medir tiempos de decisión financiera, contención técnica y comunicación regulatoria `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe *After-Action Report (AAR)* con brechas detectadas y actualización de playbooks.

### A-02 (Anual) — Revisión Anual de Licenciamiento (E3 P1 vs E5 P2 / Defender Suite), SCU y Hoja de Ruta
- **Consola / Ruta:** `https://admin.microsoft.com` y `https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO / Enterprise Security Architect.
- **Procedimiento:** Conciliar asignación de licencias MDO P1 (incluidas en E3) vs MDO P2 (E5 / Defender Suite), validar elegibilidad de *Safe Documents*, proyectar consumo de SCU de Security Copilot para agentes de triaje y alinear el roadmap anual con las capacidades liberadas por Microsoft `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe anual de gobierno de capacidades, cobertura de licencias y plan anual del SOC.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes

### AH-01 — Playbook de Respuesta a Campaña Masiva de Phishing / AiTM / Quishing (Outbreak)
- **Disparador:** Alerta de campaña activa, pico de reportes de usuarios o detección de múltiples clics permitidos en `UrlClickEvents` `[Verificado MS Learn]`.
- **Fases operativas (alineadas al Phishing Investigation Playbook del SAF)** `[Verificado MS Learn]`:
  1. **Alcance (< 15 min `[Decisión / Propuesta Editorial]`):** En *Threat Explorer* / *Campaign Views*, filtrar por dominio remitente, hash SHA256 o URL (incluyendo filtro de URL en código QR) para cuantificar entregados en `Inbox` y clics permitidos en `UrlClickEvents`.
  2. **Contención de Mensajería (< 30 min `[Decisión / Propuesta Editorial]`):** Bloquear URL, hash y dominio en *Tenant Allow/Block List* (propagación en 5-10 min) y ejecutar *Take action > Purge (Soft delete)* desde *Threat Explorer* o *Advanced Hunting*.
  3. **Contención de Identidades Expuestas:** Para todo usuario con `ActionType == "ClickAllowed"` o inicio de sesión sospechoso en `EntraIdSignInEvents`, revocar sesiones activas, marcar cuenta como comprometida (`Mark as compromised`) y auditar métodos MFA recién registrados.
  4. **Erradicación y Post-Incidente:** Iniciar investigación AIR manual sobre variantes residuales, verificar que no existan ETRs ni *overrides* que permitieron el ingreso y emitir lecciones aprendidas.
- **Evidencia Auditable:** Línea de tiempo del incidente en Defender XDR, entradas TABL con referencia al caso y log de purga con `ApproverUpn`.

### AH-02 — Playbook de Cuenta de Correo Comprometida y Fraude BEC
- **Disparador:** Alerta *User restricted from sending email*, *Suspicious email sending patterns*, regla de reenvío externo o reporte de fraude de pago `[Verificado MS Learn]`.
- **Secuencia oficial verificada (`responding-to-a-compromised-email-account`)** `[Verificado MS Learn]`:
  1. **Deshabilitar la cuenta en Entra ID** (acción preferida por Microsoft mientras se investiga para impedir reconexión del atacante).
  2. **Revocar todas las sesiones y tokens activos** (`Revoke-MgUserSignInSession` o acción directa desde el portal Defender).
  3. **Auditar persistencia de identidad:** Eliminar dispositivos MFA, aplicaciones OAuth con consentimiento ilícito o delegaciones de buzón (`FullAccess`, `SendAs`, `SendOnBehalf`) agregadas por el adversario.
  4. **Limpiar persistencia en buzón:** Inspeccionar con `Get-InboxRule -IncludeHidden` y `Get-Mailbox | Select Forwarding*`; eliminar reglas de borrado/ocultamiento o reenvío externo.
  5. **Análisis forense de alcance:** Revisar `MailItemsAccessed` en Purview Audit, rastrear correos salientes fraudulentos enviados por el atacante mediante *Message Trace* / `EmailEvents` y alertar a clientes/proveedores o tesorería si hubo instrucción de cambio bancario.
  6. **Rehabilitación controlada:** Restablecer contraseña robusta, exigir MFA resistente a phishing (FIDO2/Passkey), habilitar la cuenta y retirar de *Restricted entities* si aplicaba.
- **Evidencia Auditable:** Lista de verificación completada con timestamps, exportación de reglas eliminadas y registro en *Action Center*.

### AH-03 — Playbook de Ataque Colaborativo en Microsoft Teams (Mensajes, Enlaces y Llamadas Externas)
- **Disparador:** Reporte de usuario en Teams (mensaje, llamada scam o reunión sospechosa), alerta de clic en Teams o campaña de *Mail bombing* seguida de contacto por Teams `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Abrir el **Teams message entity panel** o **Teams call entity panel** desde la alerta/incidente e inspeccionar metadatos y los +/-15 mensajes contextuales si hubo reporte de usuario `[Verificado MS Learn]`.
  2. Ejecutar caza en `MessageEvents`, `MessageUrlInfo`, `MessagePostDeliveryEvents` y `CallActivityEvents` para identificar todos los usuarios contactados por el dominio o UPN externo `[Verificado MS Learn]`.
  3. **Contención directa en Teams (capacidades 2026):** Bloquear el dominio o dirección del remitente externo en `Tenant Allow/Block List > Domains & addresses` para Teams (corta chats nuevos, invitaciones y elimina mensajes previos sincronizando con Teams Admin Center) y, si un actor malicioso o cuenta interna comprometida permanece en una conversación, usar **Remove users from Teams chats** (MDO P2) `[Verificado MS Learn]`.
  4. Si un usuario ejecutó archivos descargados desde el enlace de Teams, aislar el equipo en Defender for Endpoint.
- **Evidencia Auditable:** Registro de bloqueo de dominio externo en TABL, acción de remoción de chat y resultados de consulta en `CallActivityEvents` / `MessageEvents`.

### AH-04 — Purga Quirúrgica de Contenido Sensible o Malicioso Multi-Buzón
- **Disparador:** Necesidad de eliminar mensajes específicos más allá de los límites interactivos estándar o con criterios complejos de contenido `[Verificado MS Learn]`.
- **Secuencia operativa:**
  1. Para campañas dentro de los últimos 30 días y <= 100 mensajes seleccionados en vista directa (o purga masiva por filtro), priorizar `Take action > Purge` desde *Threat Explorer* con aprobación en *Action Center* `[Verificado MS Learn]`.
  2. Cuando el escenario requiera búsqueda histórica (> 30 días) o criterios documentales en `https://purview.microsoft.com`, activar rol `Data Investigator` + `Search and Purge` vía PIM, validar muestra previa, aplicar preferentemente `Soft delete` y exigir doble control para `Hard delete` `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Ticket de autorización firmada, consulta exacta ejecutada y registro de auditoría en Purview / `EmailPostDeliveryEvents`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Esquema de Tablas KQL de MDO en Advanced Hunting y Sentinel (Noviembre 2026)

| Tabla | Estado | Contenido y Uso Operacional Verificado |
|---|---|---|
| `EmailEvents` | GA | Metadatos de entrega, bloqueo, autenticación (`AuthenticationDetails`), dirección, `ThreatTypes` y `DetectionMethods` (incluye *Mail bombing*) de todo correo entrante, saliente e intra-org (30 días nativos) `[Verificado MS Learn]` |
| `EmailUrlInfo` | GA | URLs extraídas de mensajes de correo electrónico (incluyendo códigos QR inspeccionados) `[Verificado MS Learn]` |
| `EmailAttachmentInfo` | GA | Metadatos de archivos adjuntos en correos (`SHA256`, `FileName`, `FileType`, veredicto de malware) `[Verificado MS Learn]` |
| `EmailPostDeliveryEvents` | GA | Eventos posteriores a la entrega: ZAP, remediaciones AIR, purgas manuales y liberaciones; incluye desde **octubre de 2026** la columna **`ApproverUpn`** `[Verificado MS Learn]` |
| `UrlClickEvents` | GA | Clics evaluados por *Safe Links* en correo, Microsoft Teams y aplicaciones de Office (`ClickAllowed`, `ClickBlocked`, `UrlChain`, `IPAddress`) `[Verificado MS Learn]` |
| `MessageEvents` | GA | Mensajes enviados y recibidos en Microsoft Teams en el momento de la entrega `[Verificado MS Learn]` |
| `MessagePostDeliveryEvents` | GA | Eventos de seguridad posteriores a la entrega en Microsoft Teams (ej. ZAP para Teams, reportes y remediaciones) `[Verificado MS Learn]` |
| `MessageUrlInfo` | GA | URLs enviadas dentro de mensajes de Microsoft Teams `[Verificado MS Learn]` |
| `MessageContents` | GA | Fragmentos de mensajes de Microsoft Teams y metadatos asociados (sujeto a permisos granulares URBAC) `[Verificado MS Learn]` |
| `CallActivityEvents` | GA (Oct 2026) | Actividades registradas durante llamadas y reuniones de Microsoft Teams para investigar llamadas de ingeniería social o participantes sospechosos `[Verificado MS Learn]` |
| `CampaignInfo` | Preview | Metadatos de campañas de correo correlacionadas por MDO `[Verificado MS Learn]` |
| `FileMaliciousContentInfo` | Preview | Archivos maliciosos detectados por MDO en SharePoint Online, OneDrive for Business y Microsoft Teams `[Verificado MS Learn]` |

### 10.2 Consultas KQL Operacionales Verificadas

#### KQL-01: Usuarios que hicieron clic permitido en una URL antes de que ZAP o AIR purgara el correo
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting / Microsoft Sentinel [Verificado MS Learn]
let PurgedEmails = EmailPostDeliveryEvents
    | where Timestamp > ago(7d)
    | where ActionType has_any ("ZAP", "Manual remediation", "Phish ZAP", "Malware ZAP")
    | where ActionResult == "Success"
    | project PurgeTime = Timestamp, NetworkMessageId, RecipientEmailAddress, ActionType, ApproverUpn;
UrlClickEvents
| where Timestamp > ago(7d)
| where Workload == "Email" and ActionType == "ClickAllowed"
| join kind=inner PurgedEmails on NetworkMessageId
| where Timestamp < PurgeTime
| project ClickTime = Timestamp, PurgeTime, AccountUpn, Url, IPAddress, ActionType, ApproverUpn, NetworkMessageId
| order by ClickTime desc
```

#### KQL-02: Auditoría de gobernanza de remediaciones post-entrega y aprobadores (`ApproverUpn` — Oct 2026)
```kql
// Audita todas las acciones manuales o aprobadas sobre buzones usando el nuevo campo ApproverUpn [Verificado MS Learn]
EmailPostDeliveryEvents
| where Timestamp > ago(30d)
| where isnotempty(ApproverUpn)
| summarize TotalMessages = count(), DistinctRecipients = dcount(RecipientEmailAddress)
    by ApproverUpn, ActionType, Action, ActionResult
| order by TotalMessages desc
```

#### KQL-03: Detección de ataques combinados Mail Bombing seguidos de llamadas externas en Microsoft Teams
```kql
// Correlaciona inundación de correo (Mail bombing) con llamadas externas de Teams (CallActivityEvents - Oct 2026) [Verificado MS Learn]
let MailBombedUsers = EmailEvents
    | where Timestamp > ago(24h)
    | where DetectionMethods has "Mail bombing" or EmailActionPolicy has "Mail bombing"
    | summarize BombCount = count(), FirstBomb = min(Timestamp) by RecipientEmailAddress;
CallActivityEvents
| where Timestamp > ago(24h)
| mv-expand Participant = parse_json(Participants)
| extend ParticipantUpn = tostring(Participant.Upn)
| join kind=inner MailBombedUsers on $left.ParticipantUpn == $right.RecipientEmailAddress
| where Timestamp between (FirstBomb .. (FirstBomb + 4h))
| project Timestamp, FirstBomb, ParticipantUpn, BombCount, CallId, ActivityType
```

#### KQL-04: Cacería de mensajes con URLs clicadas en Microsoft Teams y post-entrega ZAP Teams
```kql
// Correlaciona mensajes de Teams, URLs incluidas, eventos post-entrega y clics en Safe Links [Verificado MS Learn]
MessagePostDeliveryEvents
| where Timestamp > ago(7d)
| join kind=inner (MessageUrlInfo | where Timestamp > ago(7d)) on TeamsMessageId
| join kind=inner (UrlClickEvents | where Timestamp > ago(7d) and Workload == "Teams") on Url
| project Timestamp, TeamsMessageId, SenderEmailAddress, Url, ActionType, IsClickedThrough
```

#### KQL-05: Correos de phishing entregados en Inbox por culpa de Overrides (ETR, Safe Senders, IP Allow)
```kql
// Identifica brechas de configuración donde MDO detectó amenaza pero un override forzó la entrega [Verificado MS Learn]
EmailEvents
| where Timestamp > ago(7d)
| where DeliveryLocation in ("Inbox", "Folder")
| where ThreatTypes has_any ("Phish", "Malware")
| where isnotempty(OrgLevelAction) or isnotempty(UserLevelAction)
| summarize DeliveredThreats = count(), AffectedUsers = dcount(RecipientEmailAddress)
    by ThreatTypes, OrgLevelAction, OrgLevelPolicy, UserLevelAction, SenderFromDomain
| order by DeliveredThreats desc
```

#### KQL-06: Cacería de posibles vectores HTML Smuggling o archivos contenedores riesgosos entregados
```kql
// Detecta adjuntos de alto riesgo de evasión entregados sin bloqueo inicial [Verificado MS Learn]
EmailAttachmentInfo
| where Timestamp > ago(7d)
| where FileType in~ ("html", "htm", "iso", "vhd", "vhdx", "lnk", "one", "svg")
| join kind=inner (
    EmailEvents
    | where Timestamp > ago(7d)
    | where EmailDirection == "Inbound" and DeliveryLocation == "Inbox"
) on NetworkMessageId
| project Timestamp, SenderFromAddress, RecipientEmailAddress, Subject, FileName, FileType, SHA256, NetworkMessageId
```

### 10.3 Verificación de Configuración por PowerShell (Exchange Online Management)

```powershell
# Verificación de estado de ZAP para Teams, Preset Security Policies y DKIM [Verificado MS Learn]
Connect-ExchangeOnline

# 1. Confirmar ZAP para Teams activo y sin exclusiones excesivas
Get-TeamsProtectionPolicy | Format-List Name,ZapEnabled,HighConfidencePhishQuarantineTag,MalwareQuarantineTag
Get-TeamsProtectionPolicyRule | Format-List Name,ExceptIfSentTo,ExceptIfSentToMemberOf,ExceptIfRecipientDomainIs

# 2. Verificar reglas activas de Preset Security Policies (Standard y Strict)
Get-EOPProtectionPolicyRule | Select-Object Name,State,SentTo,SentToMemberOf
Get-ATPProtectionPolicyRule | Select-Object Name,State,SentTo,SentToMemberOf

# 3. Auditar estado de firma DKIM en todos los dominios
Get-DkimSigningConfig | Select-Object Domain,Enabled,Status,Selector1KeySize,Selector2KeySize
```

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales y Ejecutivos

> **Nota metodológica:** Reportar siempre **mediana (p50) y percentil 90 (p90)** en lugar de promedios simples, y emparejar cada métrica de velocidad con una métrica de calidad (ej. reversiones o reaperturas) para evitar incentivos perversos. Los umbrales numéricos son `[Decisión / Propuesta Editorial]`.

| ID | Indicador (KPI) | Fórmula / Método de Cálculo | Meta Sugerida `[Decisión / Propuesta Editorial]` | Frecuencia | Audiencia |
|---|---|---|---|---|---|
| **KPI-01** | **MTTA de Incidentes MDO (Mediana y p90)** | `percentiles(FirstModifiedTime - CreatedTime, 50, 90)` sobre incidentes MDO en `SecurityIncident` | p50 < 15 min / p90 < 30 min (High) | Semanal | SOC Manager |
| **KPI-02** | **MTTC de Campañas y Clics Maliciosos** | Tiempo desde alerta de clic/campaña hasta purga de buzón (`EmailPostDeliveryEvents`) + revocación de sesión | p90 < 30 min (High) / < 2 h (Medium) | Semanal | SOC Manager / CISO |
| **KPI-03** | **Tasa de Automatización Efectiva (AIR + Triage Agent)** | `(Investigaciones resueltas/auto-remediadas por AIR o Agente sin reversión / Total investigaciones MDO) * 100` | > 80% con < 2% de acciones revertidas | Semanal | SOC Manager |
| **KPI-04** | **Exposición por System Overrides** | Total de mensajes con veredicto `Phish`/`Malware` entregados en `Inbox` debido a ETR, IP Allow o Safe Senders | Tendencia a 0 (0 ETR con `SCL = -1` sin excepción vigente) | Semanal | Security Admin / CISO |
| **KPI-05** | **Alineación en Configuration Analyzer** | `(Controles alineados a Standard/Strict / Total controles evaluados en Configuration Analyzer) * 100` | >= 95% (100% de desvíos justificados) | Mensual | Security Architect / GRC |
| **KPI-06** | **Tasa de Compromiso en Simulaciones (AST Compromise Rate)** | `(Usuarios que entregaron credenciales o abrieron payload simulado / Usuarios evaluados) * 100` | < 6% global / < 3% en *Priority Accounts* | Mensual | CISO / Comité de Riesgo |
| **KPI-07** | **Ratio Señal/Compromiso Humano (Report-to-Click Ratio)** | `Usuarios que reportaron la simulación / Usuarios que cayeron en la simulación` | > 3:1 y *Training Completion* > 95% en 30 días | Mensual | CISO / RR.HH. |
| **KPI-08** | **Cobertura DMARC `p=reject` en Dominios Propios** | `(Dominios corporativos activos y estacionados con DMARC p=reject y DKIM 2048-bit / Total dominios) * 100` | 100% de dominios corporativos | Trimestral | CISO / Auditoría |

### 11.2 Modelo de Madurez Operacional MDO (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estado | Características Observables en Tecnología, Procesos y Personas |
|---|---|---|
| **Nivel 1 — Inicial** | Perimetral reactivo | Solo EOP por defecto, DMARC en `none` o inexistente, reglas ETR heredadas con `SCL=-1`, sin triaje diario estructurado ni simulaciones AST. |
| **Nivel 2 — Básico Gestionado** | Prevención estándar | MDO Plan 1 activo (ej. base M365 E3), *Preset Policy Standard* desplegada, ZAP en correo y Teams habilitado, revisión básica de cuarentena. |
| **Nivel 3 — Intermedio XDR** | Operaciones SOC estructuradas | MDO Plan 2 desplegado, *Preset Policy Strict* en *Priority Accounts*, URBAC y PIM activos, *AIR* operando con revisión diaria en *Action Center*, *Configuration Analyzer* mensual. |
| **Nivel 4 — Avanzado Proactivo** | Cacería multi-canal e integración SIEM | Hunting semanal KQL sobre `Email*`, `UrlClickEvents`, `Message*` y `CallActivityEvents`, conectores Sentinel activos, campañas AST automatizadas mensuales, DMARC `p=reject` al 100%. |
| **Nivel 5 — Optimizado / Agéntico** | Excelencia operacional demostrable | *Security Alert Triage Agent* gobernado con muestreo de calidad, auto-remediación de clústeres + *Automatic Attack Disruption*, respaldo de políticas como código, *Tabletop* anuales y KPIs p50/p90 auditables ante el Directorio. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota metodológica:** Conforme a NIST CSWP 29, el CSF 2.0 define **resultados esperados (*outcomes*)** y no controles prescriptivos. El siguiente mapeo vincula capacidades verificadas de MDO con los resultados del CSF 2.0 y sus evidencias objetivas `[Decisión / Propuesta Editorial]`.

### 12.1 Matriz de Evidencia Auditable NIST CSF 2.0

| Función | Subcategoría CSF 2.0 | Resultado Esperado (Outcome) | Capacidad Habilitadora en MDO | Evidencia Objetiva para Auditoría |
|---|---|---|---|---|
| **GOVERN (GV)** | `GV.PO-01` | Se establecen, comunican y aplican políticas de gestión de riesgos de ciberseguridad. | *Preset Security Policies* (`Standard`/`Strict`), políticas de cuarentena restringida y gobierno de excepciones TABL (45 días). | Exportación de `Get-EOPProtectionPolicyRule` / `Get-ATPProtectionPolicyRule` y reporte *Configuration Analyzer*. |
| **GOVERN (GV)** | `GV.RR-02` | Se definen, asignan y auditan roles, responsabilidades y autoridades de ciberseguridad. | Modelo **Unified RBAC (URBAC)** con separación entre metadatos, previsualización y purga + activación JIT en Entra PIM. | Matriz de roles URBAC en `security.microsoft.com/securitypermissions` y logs de activación PIM + `ApproverUpn`. |
| **IDENTIFY (ID)** | `ID.AM-05` | Los activos se priorizan según clasificación, criticidad e impacto al negocio. | **Priority Account Protection** (etiquetado de C-Suite, finanzas y roles de alto impacto hasta 250 cuentas). | Listado exportado en `security.microsoft.com/securitysettings/userTags` y asignación a política *Strict*. |
| **IDENTIFY (ID)** | `ID.RA-03` | Se identifican y registran amenazas internas y externas relevantes para la organización. | *Threat Explorer*, *Campaign Views*, *Threat Analytics* y *Predicted Compromise Rate* en AST. | Informes descargados de campañas dirigidas y actas semanales de revisión de *Threat Analytics*. |
| **PROTECT (PR)** | `PR.PS-01` | Se establecen y mantienen prácticas de gestión de configuración seguras. | Autenticación SPF/DKIM/DMARC/ARC, *Safe Attachments*, *Safe Links* (correo, Teams y Office) y bloqueo de dominios externos en Teams. | Reporte `ORCA`, registros DNS publicados con `p=reject` y exportación mensual versionada de políticas XML. |
| **PROTECT (PR)** | `PR.AT-01` | El personal recibe concientización y capacitación para desempeñar tareas de forma segura. | **Attack Simulation Training (AST)** con simulaciones realistas (incluyendo QR y OAuth) y entrenamiento adaptativo automático. | Historial de campañas ejecutadas, tasas de compromiso/reporte y registros de capacitación completada. |
| **DETECT (DE)** | `DE.CM-01` | Las redes y servicios de comunicación se monitorean para detectar eventos potencialmente adversos. | Detección continua en correo y Teams (ML, LLM BEC, *Prompt injection*, *Mail bombing*, *Safe Links* time-of-click). | Consultas KQL auditadas sobre `EmailEvents`, `UrlClickEvents`, `MessageEvents` y `CallActivityEvents`. |
| **DETECT (DE)** | `DE.AE-03` | Se correlaciona información de múltiples fuentes para analizar eventos adversos. | Correlación automática de alertas MDO + envíos de usuario + clics URL con Entra ID y MDE en incidentes XDR. | Captura/exportación de incidentes multi-dominio en `security.microsoft.com/incidents`. |
| **RESPOND (RS)** | `RS.AN-03` | Se ejecuta análisis para establecer qué ocurrió durante un incidente y su causa raíz. | Investigaciones automatizadas **AIR**, *Email entity page* (con resumen Copilot) y *Teams message/call entity panels*. | Grafos y resultados exportados de investigaciones en `security.microsoft.com/airinvestigation`. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes se contienen para evitar la propagación de sus efectos. | **ZAP** en correo y Teams, auto-remediación de clústeres en AIR, expulsión de usuarios en chats de Teams y bloqueo táctico TABL. | Registros en `EmailPostDeliveryEvents`, `MessagePostDeliveryEvents` y `Action Center > History`. |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de los activos restaurados y se reanuda la operación normal de forma segura. | Rehabilitación controlada de buzones comprometidos, validación en *Restricted entities* y liberación auditada de falsos positivos. | Checklist firmado de rehabilitación BEC (`AH-02`) y logs de desbloqueo en `restrictedentities`. |
| **RECOVER (RC)** | `RC.IM-01` | Las lecciones aprendidas de incidentes y ejercicios mejoran los procesos y controles futuros. | *Post-Incident Reviews*, recalibración de políticas con *What-If insights* y diseño de nuevas campañas AST basadas en ataques reales. | Informes AAR de incidentes/tabletop y trazabilidad de cambios de política posteriores. |

### 12.2 Cobertura Principal en MITRE ATT&CK Enterprise `[Verificado MS Learn]`

| Táctica MITRE | Técnicas Cubiertas | Mecanismo MDO / XDR |
|---|---|---|
| **Initial Access (`TA0001`)** | `T1566.001` (Spearphishing Attachment), `T1566.002` (Spearphishing Link), `T1566.003` (Spearphishing via Service / Teams) | *Safe Attachments*, *Safe Links*, protección de URLs/archivos y bloqueo de dominios externos en Teams |
| **Execution (`TA0002`)** | `T1204.001` (Malicious Link), `T1204.002` (Malicious File) | Reescritura y bloqueo en tiempo de clic (`UrlClickEvents`) y detonación dinámica en sandbox |
| **Defense Evasion (`TA0005`)** | `T1027.006` (HTML Smuggling), `T1656` (Impersonation) | Heurísticas de sandbox, *User/Domain Impersonation*, *Mailbox Intelligence* y filtros LLM BEC |
| **Credential Access (`TA0006`)** | `T1539` (Steal Web Session Cookie / AiTM), `T1528` (Steal Application Access Token) | Detección de phishing AiTM/QR + correlación con Entra ID Protection y *Simulations OAuth* |
| **Persistence / Collection (`TA0003` / `TA0009`)** | `T1098.002` (Additional Email Delegate Permissions), `T1114.003` (Email Forwarding Rule) | Alertas de reglas de reenvío externo, *AIR Compromised User Playbook* y auditoría `MailItemsAccessed` |
| **Lateral Movement (`TA0008`)** | `T1534` (Internal Spearphishing en correo y chats internos de Teams) | Escaneo intra-organizacional en `EmailEvents`, `MessageEvents` y **ZAP para Teams** |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps, Admin y GRC)

Plan estructurado de incorporación técnica de 30-60-90 días `[Decisión / Propuesta Editorial]` respaldado en rutas oficiales verificadas `[Verificado MS Learn]`:

| Rol | Días 1–30 (Fundamentos) | Días 31–60 (Operación Autónoma) | Días 61–90 (Dominio Avanzado) |
|---|---|---|---|
| **Analista SOC L1** | Fundamentos MDO Ninja, arquitectura EOP/P1/P2, triaje en cola XDR (`D-01`) y cuarentena (`D-04`). | Gestión de *User Submissions* en correo y Teams (`D-03`), verificación ZAP (`D-07`) y KQL esencial sobre `EmailEvents` y `UrlClickEvents`. | Detección temprana de *Mail bombing* y BEC (`D-08`), validación de veredictos del *Security Alert Triage Agent*. |
| **Analista SOC L2** | Todo L1 + operación de **AIR** y *Action Center* (`D-02`), *Restricted entities* (`D-05`) y *Campaign Views* (`D-06`). | Investigación interactiva en *Threat Explorer*, uso de *Take action*, administración táctica de TABL (correo y Teams). | Ejecución completa de los playbooks de contención `AH-01`, `AH-02` (BEC) y `AH-03` (Teams) y preparación certificación **SC-200**. |
| **Analista SOC L3 / Hunter** | Dominio del esquema completo `Email*`, `Message*`, `CallActivityEvents` y correlación con `EntraIdSignInEvents` y `Device*`. | Cacería semanal por hipótesis (`S-04`), creación de *Custom Detection Rules* con acciones automatizadas y purgas controladas (`AH-04`). | Liderazgo de incidentes mayores multi-dominio, calibración de *Alert tuning* (`T-02`) y ejercicios Purple Team / Tabletop (`A-01`). |
| **Security Admin / Engineer** | Plan oficial de 8 pasos MDO: autenticación SPF/DKIM/DMARC/ARC, *Preset Security Policies* (`Standard`/`Strict`) y *Priority Accounts*. | Migración y diseño de roles mínimos en **Unified RBAC (URBAC)**, configuración PIM/JIT, ZAP para Teams y *Configuration Analyzer* / `ORCA`. | Ajuste basado en *Policy What-If insights* (`M-02`), automatización de respaldos PowerShell (`M-06`), gestión de AST (`M-04`) e integración Sentinel. |
| **Auditor GRC / CISO Office** | Comprensión diferencial MDO P1 (E3) vs MDO P2 (E5 / Defender Suite) y metodología *Outcome-based* de NIST CSF 2.0. | Verificación de evidencias en solo lectura (`Global Reader`/`Security Reader`), trazabilidad `ApproverUpn` y control de SoD/PIM (`M-05`). | Evaluación anual de madurez operacional, gobierno de agentes de IA en el SOC y reporte de reducción de riesgo al Directorio. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Actualizaciones Aplicadas tras Revalidación en Microsoft Learn (Noviembre 2026)

| Área Revalidada | Estado en Borradores Previos (`MSEOP-MD`) | Estado Oficial Verificado a Noviembre de 2026 (`[Verificado MS Learn]`) |
|---|---|---|
| **Licenciamiento MDO Plan 1 en E3 y Defender Suite** | Indicaba que Microsoft 365 E3 / Office 365 E3 solo incluían EOP y usaba únicamente el nombre *M365 E5 Security*. | Desde **julio de 2026**, **MDO Plan 1 está incluido en Microsoft 365 E3 y Office 365 E3**. El complemento de seguridad E5 se denomina actualmente **Microsoft Defender Suite** (y existe *Microsoft 365 E7* GA mayo 2026). *Safe Documents* exige M365 E5 o Defender Suite. |
| **Modelo de Permisos Unified RBAC (URBAC)** | Basado principalmente en grupos de roles heredados de *Email & collaboration* (`security.microsoft.com/emailandcollabpermissions`). | Desde **julio de 2026 (MC1246006)**, **URBAC es el modelo predeterminado** para nuevas organizaciones MDO Plan 2; activar URBAC deshabilita la página heredada. En abril de 2026 se añadió el permiso granular `Emails associated with alerts (read)`. AST mantiene roles en Entra ID. |
| **Auto-remediación en AIR vs Aprobación Humana** | Un bloque afirmaba que *"ninguna acción en AIR ocurre automáticamente y todas requieren aprobación humana"*, mientras otro citaba clústeres. | **AIR en MDO Plan 2 permanece plenamente vigente** (el cambio del 1-sep-2026 solo afectó a MDE) y **aprueba automáticamente la remediación de clústeres de similitud maliciosos (URLs y archivos)**, además de cerrar automáticamente alertas donde no se hallan amenazas. |
| **Protección de Microsoft Teams (ZAP, Bloqueo Externo y Reportes)** | Asignaba ZAP para Teams exclusivamente a MDO Plan 2 y listaba tablas `Message*` en Preview. | Desde **enero-febrero de 2026**, **ZAP para Teams, cuarentena administrada de Teams y reportes de usuarios en Teams están disponibles desde MDO Plan 1**. Se añadió bloqueo directo de dominios/remitentes externos de Teams en TABL (ene-2026), expulsión de usuarios de chats en GA (abr-2026, P2), página separada `teamsUserSubmission` (sep-2026) y reporte de llamadas/reuniones (mar-oct 2026). |
| **Nuevas Tablas y Columnas KQL (Octubre 2026)** | Solo incluía 4 tablas de correo y 3 de Teams en Preview. | `MessageEvents`, `MessagePostDeliveryEvents`, `MessageUrlInfo` y `MessageContents` están en **GA**; en **octubre de 2026** se incorporaron la tabla **`CallActivityEvents`** (GA) y el campo **`ApproverUpn`** en `EmailPostDeliveryEvents`. |
| **Agentes de Security Copilot y Nuevas Detecciones** | No reflejaba el cambio de nombre del agente ni detecciones de IA/inundación. | Incorporado el **Security Alert Triage Agent** (antes *Phishing Triage Agent*, GA para correo con requisito de desactivar la regla de *Alert tuning* de auto-resolución), resumen Copilot en *Email entity page* (abr-2026), protección contra **Prompt injection** (jul-2026) y detección de **Mail bombing**. |
| **Portales y Retención TABL** | Citaba `compliance.microsoft.com` y retención manual genérica de 30 días en Allow List. | Actualizado al portal unificado **Microsoft Purview (`https://purview.microsoft.com`)** y documentado el vencimiento predeterminado oficial de **45 días tras la última fecha de uso** (`45 days after last used date`) para entradas *Allow* originadas en envíos. |

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Técnica y de Gobierno |
|---|---|---|
| **Metas numéricas de SLA y KPIs (ej. MTTA p50 < 15 min, MTTC p90 < 30 min, AST < 6%)** | `[Decisión / Propuesta Editorial]` | Microsoft Learn define los flujos de triaje y métricas operativas, pero establece que cada organización debe fijar sus objetivos cuantitativos según dotación 24x7, volumen y apetito de riesgo. |
| **Duraciones máximas de activación JIT en Entra PIM (4 h para Purge/Admin, 8 h para L2) y tope de titulares** | `[Decisión / Propuesta Editorial]` | Microsoft recomienda explícitamente usar PIM con MDO (`pim-in-mdo-configure`), pero la cantidad exacta de horas y aprobadores cruzados constituye una política interna de gobierno de acceso privilegiado. |
| **Modelo de Madurez Operacional de 5 niveles y plan de capacitación 30-60-90 días** | `[Decisión / Propuesta Editorial]` | Estructura consultiva diseñada para medir evolución progresiva del SOC combinando la escalera de protección de MDO con prácticas del Microsoft Security Adoption Framework (SAF) y SOC-CMM. |
| **Mapeo de subcategorías y artefactos de evidencia hacia NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | NIST CSF 2.0 evalúa *outcomes* organizacionales; la correspondencia entre funciones técnicas de MDO y subcategorías específicas de CSWP 29 es un mapeo de arquitectura de auditoría. |
| **Periodicidad exacta de respaldos PowerShell XML y ejercicios Tabletop anuales** | `[Decisión / Propuesta Editorial]` | Buenas prácticas de resiliencia operativa e ingeniería de plataforma para garantizar reversibilidad ante cambios accidentales o maliciosos de configuración. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
1. **Microsoft Defender for Office 365 Security Operations Guide** — Guía oficial maestra de actividades diarias, semanales, mensuales y ad-hoc del SOC: `https://learn.microsoft.com/en-us/defender-office-365/mdo-sec-ops-guide`
2. **What's new in Microsoft Defender for Office 365** — Registro oficial de novedades verificadas hasta octubre/noviembre de 2026 (`CallActivityEvents`, `ApproverUpn`, Teams reporting, URBAC, P1 en E3, Prompt Injection): `https://learn.microsoft.com/en-us/defender-office-365/defender-for-office-365-whats-new`
3. **Preset security policies in cloud organizations** — Configuración y precedencia de *Built-in protection*, *Standard* y *Strict*: `https://learn.microsoft.com/en-us/defender-office-365/preset-security-policies`
4. **Microsoft Defender for Office 365 support for Microsoft Teams** — Matriz oficial de protección de Teams por licencia, ZAP para Teams y PowerShell `*-TeamsProtectionPolicy`: `https://learn.microsoft.com/en-us/defender-office-365/mdo-support-teams-about`
5. **Zero-hour auto purge (ZAP) in Microsoft Defender for Office 365** — Funcionamiento técnico de ZAP en Exchange Online (48h) y Microsoft Teams: `https://learn.microsoft.com/en-us/defender-office-365/zero-hour-auto-purge`
6. **Automated investigation and response (AIR) in Microsoft Defender for Office 365 Plan 2** — Flujo de AIR, auto-remediación de clústeres, permisos URBAC e interacción con Alert Tuning y Triage Agent: `https://learn.microsoft.com/en-us/defender-office-365/air-about`
7. **Email authentication in cloud organizations** — Arquitectura interdependiente de SPF, DKIM, DMARC, ARC e implicit/composite authentication (`compauth`): `https://learn.microsoft.com/en-us/defender-office-365/email-authentication-about`
8. **Microsoft Defender for Office 365 permissions in the Microsoft Defender portal** — Modelo Unified RBAC (MC1246006) y roles de colaboración: `https://learn.microsoft.com/en-us/defender-office-365/mdo-portal-permissions`
9. **Respond to a compromised cloud email account** — Procedimiento oficial de respuesta y remediación ante compromisos BEC: `https://learn.microsoft.com/en-us/defender-office-365/responding-to-a-compromised-email-account`
10. **Phishing investigation playbook (Microsoft Security Adoption Framework)** — Playbook operativo moderno de investigación de phishing (SAF SecOps): `https://learn.microsoft.com/en-us/security/zero-trust/security-operations-playbook-phishing`
11. **Microsoft Defender for Office 365 Service Description** — Matriz contractual oficial de capacidades EOP vs Plan 1 vs Plan 2: `https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description`
12. **Understand the advanced hunting schema** — Referencia oficial de tablas KQL (`Email*`, `UrlClickEvents`, `Message*`, `CallActivityEvents`): `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables`

### 15.2 Publicaciones Oficiales y Empleados de Microsoft
13. **Introducing the Microsoft Defender for Office 365 Security Operations Guide** — Blog oficial del equipo de producto MDO en Microsoft Tech Community: `https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/introducing-the-microsoft-defender-for-office-365-security-operations-guide/3638250`
14. **Microsoft Ignite: Transforming phishing response with agentic innovation** — Blog oficial de MDO sobre la evolución agéntica del triaje de phishing (*Security Alert Triage Agent*): `https://techcommunity.microsoft.com/blog/MicrosoftDefenderforOffice365Blog/microsoft-ignite-2025-transforming-phishing-response-with-agentic-innovation/4470791`
15. **Become a Microsoft Defender for Office 365 Ninja** — Entrenamiento oficial curado por el equipo de ingeniería de MDO (`ang31a`, Microsoft Tech Community): `https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/become-a-microsoft-defender-for-office-365-ninja--june-2022/2187392`
16. **Matt Zorich (`reprise99`, Microsoft GHOST) — Sentinel & Defender KQL Queries** — Repositorio de consultas KQL de caza e investigación en M365, correo e identidad: `https://github.com/reprise99/Sentinel-Queries`

### 15.3 Comunidad y MVPs de Seguridad de Microsoft
17. **Bert-Jan Pals (Microsoft Security MVP) — Hunting Queries and Detection Rules** — Repositorio comunitario de referencia con consultas KQL para `EmailEvents`, `UrlClickEvents` y detección de campañas en Defender XDR: `https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules`
18. **Jeffrey Appel (Microsoft Security MVP) — Microsoft Security & Defender XDR Blog** — Análisis técnicos profundos de novedades mensuales de Defender XDR, MDO y automatización de respuesta: `https://jeffreyappel.nl/`
19. **Jorge Castañeda (Microsoft Security MVP, LATAM) — Blog d3fend.me** — Laboratorios reproducibles y prácticas operativas en español sobre Defender XDR y Microsoft Sentinel: `https://blog.d3fend.me/`

### 15.4 Marcos Normativos y Estándares de la Industria
20. **NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)** — Marco normativo oficial basado en funciones, categorías y resultados (*outcomes*): `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`
21. **MITRE ATT&CK Enterprise — Technique T1566 (Phishing)** — Taxonomía de técnicas adversarias de acceso inicial por correo y servicios de colaboración: `https://attack.mitre.org/techniques/T1566/`

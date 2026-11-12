# Microsoft Defender XDR (Plataforma SecOps Unificada) — Guía Maestra de Excelencia Operacional

## 1. Portada y Ficha de Control Documental

| Atributo de Control | Detalle Documental |
|---|---|
| **Identificador del Módulo** | `03_Microsoft_Defender_XDR` |
| **Nombre Oficial Revalidado** | Microsoft Defender XDR (Plataforma SecOps Unificada) |
| **Categoría del Repositorio** | SecOps, XDR y SIEM |
| **Versión Documental** | 2.0 — Edición Canónica Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (`2026-02-24 - XDR`) + Revalidación activa contra Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | Incluido de forma nativa y completa en Microsoft 365 E5, Microsoft Defender Suite (antes M365 E5 Security) y Microsoft 365 E7 `[Verificado MS Learn]` |
| **Portales Operativos Principales** | `https://security.microsoft.com` (Microsoft Defender portal — experiencia unificada XDR + SIEM + Exposure Management + Security Copilot), `https://entra.microsoft.com`, `https://admin.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager / Lead, Analistas SecOps (Tier 1 / Tier 2 / Tier 3), Threat Hunters, Detection Engineers, Ingenieros de Plataforma SecOps, Auditores Internos/Externos y GRC |
| **Marcos de Referencia Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST SP 800-61 Rev. 3 (abril 2025), Microsoft Zero Trust Reference Architecture, Microsoft Security Adoption Framework (SAF — SecOps Discipline 2026), MITRE ATT&CK Enterprise y Microsoft Cloud Security Benchmark (MCSB) v2 |

> **Convención obligatoria de evidencia:** Este documento separa rigurosamente los hechos técnicos verificables en fuentes primarias mediante la etiqueta `[Verificado MS Learn]` respecto de umbrales de nivel de servicio (SLA), metas cuantitativas de KPI, matrices RACI sugeridas, modelos de madurez consultivos y mapeos interpretativos de auditoría, los cuales se identifican explícitamente con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Síntesis Ejecutiva para Dirección y Liderazgo SOC

**Microsoft Defender XDR** (anteriormente *Microsoft 365 Defender*) constituye el plano operacional unificado de prevención pre-brecha y detección, investigación y respuesta extendida post-brecha del ecosistema de seguridad de Microsoft `[Verificado MS Learn]`. A diferencia de las aproximaciones XDR basadas exclusivamente en agregación de registros mediante conectores externos, Defender XDR correlaciona de forma nativa y en tiempo real la telemetría de sensores de endpoints, identidades híbridas y en la nube, correo electrónico y herramientas colaborativas, aplicaciones SaaS/OAuth, postura de exposición y señales de seguridad de datos, consolidando cientos de alertas individuales en **incidentes unificados** con narrativa completa de ataque (*Attack Story*) `[Verificado MS Learn]`.

Entre 2025 y noviembre de 2026 la plataforma experimentó una transformación arquitectónica decisiva que obliga a actualizar cualquier manual operativo anterior a 2025 `[Verificado MS Learn]`:

1. **Convergencia de la Plataforma SecOps Unificada en `security.microsoft.com`:** Microsoft Sentinel opera de forma generalmente disponible dentro del portal de Microsoft Defender (incluso para clientes sin licencia E5), habilitando automáticamente el conector de Defender XDR y compartiendo gestión de casos, búsqueda avanzada sobre el *Microsoft Sentinel data lake* y permisos en **Unified RBAC**. Microsoft estableció el **31 de marzo de 2027** como fecha definitiva de retiro del soporte de Microsoft Sentinel en el portal de Azure (`portal.azure.com`), redirigiendo toda operación SIEM y XDR al portal de Defender `[Verificado MS Learn]`.
2. **Contención Autónoma a Velocidad de Máquina (*Automatic Attack Disruption* y *Predictive Shielding*):** Frente a campañas de ransomware operado por humanos, robo de tokens AiTM y compromiso de correo empresarial (BEC), Defender XDR interrumpe el ataque en segundos con un umbral de confianza (relación señal-ruido) igual o superior al **99 %**, aislando dispositivos, conteniendo usuarios/IPs, revocando sesiones en Entra ID, deshabilitando cuentas en Active Directory y aplicando endurecimiento predictivo (*Safeboot hardening*, *GPO hardening*, *Proactive user containment*), con soporte en vista previa para Okta y AWS IAM vía conectores de Sentinel `[Verificado MS Learn]`.
3. **Gestión Continua de Exposición a Amenazas (CTEM) e IA Agéntica:** Con la disponibilidad general de **Microsoft Security Exposure Management** (grafo de exposición empresarial, rutas de ataque híbridas on-prem a nube y gestión de activos críticos) y la inclusión de capacidad base de **Microsoft Security Copilot** en clientes elegibles con licencias pagas de Microsoft 365 E5 (400 SCU mensuales por cada 1.000 licencias pagas, hasta 10.000 SCU/mes) junto con agentes especializados como el *Security Alert Triage Agent*, el SOC evoluciona desde el triaje reactivo de alertas hacia una operación proactiva y asistida por IA con supervisión humana (*human-in-the-loop*) `[Verificado MS Learn]`.

Desde la perspectiva financiera y de gobierno ejecutivo, el estudio independiente *Total Economic Impact (TEI)* elaborado por Forrester Research para Microsoft documenta un retorno de inversión (ROI) del **242 % a tres años** derivado de la consolidación de consolas puntuales, la reducción de horas operativas en niveles L1/L2 y la disminución del impacto económico de brechas materiales `[Verificado MS Learn]`. Para toda organización que ya posee licencias Microsoft 365 E5 o Microsoft Defender Suite, el imperativo ejecutivo no es la adquisición de nuevas herramientas superpuestas, sino la operacionalización disciplinada de las capacidades ya licenciadas `[Decisión / Propuesta Editorial]`.

### 2.2 Posicionamiento en los Tres Principios de Zero Trust

| Principio Zero Trust | Materialización Operativa en Microsoft Defender XDR | Estado de Validación |
|---|---|---|
| **Verificar explícitamente (*Verify Explicitly*)** | Correlación continua de señales multi-dominio (identidad en Entra ID y Active Directory, salud/riesgo del dispositivo en MDE, telemetría de correo/Teams en MDO, sesiones SaaS/OAuth en MDCA y contexto de sensibilidad de datos en Purview) antes y después de cada decisión de acceso o respuesta. | `[Verificado MS Learn]` |
| **Usar privilegio mínimo (*Use Least Privilege*)** | Adopción de **Microsoft Defender Unified RBAC (URBAC)** con segregación granular entre permisos de consulta, acciones blandas y acciones duras; activación Just-In-Time (JIT) mediante Microsoft Entra Privileged Identity Management (PIM) sin depender del rol *Global Administrator*. | `[Verificado MS Learn]` |
| **Asumir brecha (*Assume Breach*)** | Contención automática en curso mediante *Automatic Attack Disruption* y *Predictive Shielding*, caza proactiva por hipótesis sobre 30 días de telemetría cruda en *Advanced Hunting* (ampliable en *Sentinel data lake*) y modelado preventivo de puntos de estrangulamiento (*Choke points*) en *Exposure Management*. | `[Verificado MS Learn]` |

### 2.3 Licenciamiento Enterprise y Prerrequisitos Verificados (Noviembre 2026)

No existe una licencia aislada denominada comercialmente "SKU Microsoft Defender XDR"; la experiencia XDR unificada emerge al contar con al menos una carga de trabajo elegible, alcanzando su cobertura y correlación multi-dominio completa cuando convergen las cargas Plan 2 `[Verificado MS Learn]`:

| Vehículo de Licenciamiento | Cobertura Defender XDR | Detalle de Componentes y Cambios Vigentes a Noviembre 2026 | Estado |
|---|---|---|---|
| **Microsoft 365 E5** | Completa y nativa | Incluye MDE Plan 2 (con MDVM núcleo), MDI, MDO Plan 2, Defender for Cloud Apps, Entra ID P2, Exposure Management completo, Automatic Attack Disruption e inclusión de 400 SCU/mes por cada 1.000 licencias pagas de E5 (máx. 10.000 SCU/mes) para Security Copilot. elegible a vista previa de ISOC si no tiene workspace activo de Sentinel. | `[Verificado MS Learn]` |
| **Microsoft Defender Suite** *(antes M365 E5 Security)* | Completa (complemento sobre M365 E3) | Nombre actual adoptado en 2025 para el add-on de seguridad avanzada sobre Microsoft 365 E3. Habilita MDE P2, MDI, MDO P2, Defender for Cloud Apps, Entra ID P2, Attack Disruption y Exposure Management completo. | `[Verificado MS Learn]` |
| **Microsoft 365 E7** *(GA mayo 2026)* | Completa + IA y Gobernanza extendida | Incluye la totalidad de Microsoft 365 E5 más Microsoft 365 Copilot, Microsoft Agent 365 y Microsoft Entra Suite. | `[Verificado MS Learn]` |
| **Microsoft 365 E3** | Parcial (sin XDR completo) | Incluye MDE Plan 1 y, desde el **1 de julio de 2026**, incorpora **Defender for Office 365 Plan 1**. No incluye EDR avanzado, Advanced Hunting multi-dominio, MDI, MDCA ni correlación completa de Attack Disruption; accede únicamente a Secure Score básico en postura. | `[Verificado MS Learn]` |
| **Cargas complementarias facturadas por separado** | Extensión SIEM, Servidores y Postura Premium | **Microsoft Sentinel** (consumo Azure en Analytics y Data Lake tiers; ingesta de alertas/incidentes XDR sin cargo adicional), **Defender for Servers Plan 1/Plan 2** (servidores no cubiertos por licencias de usuario M365 E5), **Defender Vulnerability Management Add-on** (capacidades premium de baselines/firmware/certificados) y **Microsoft Entra Workload ID Premium**. | `[Verificado MS Learn]` |

**Prerrequisitos técnicos indispensables para la operación `[Verificado MS Learn]`:**
- Incorporación del workspace primario de Microsoft Sentinel al portal Defender (`System > Settings > Microsoft Sentinel`) o validación de elegibilidad ISOC (evitando desconectar un workspace productivo de Sentinel únicamente para probar ISOC).
- Activación planificada de **Microsoft Defender Unified RBAC** (`Permissions > Microsoft Defender XDR > Roles`) por cada carga de trabajo soportada y por workspace de Sentinel.
- Despliegue del sensor **Defender for Identity v3.x** (ejecutándose como `LocalSystem` y actualizado vía Windows Update) en controladores de dominio, AD FS y AD CS, habilitando el enterprise application administrado por Microsoft (`60ca1954-583c-4d1f-86de-39d835f3e452`) para acciones de contención híbrida.
- Definición explícita de activos críticos (dispositivos VIP, Tier-0/controladores de dominio, grupos privilegiados) y listas de exclusión de contención automática (*Attack Disruption exclusions*) para infraestructura cuya desconexión súbita implique riesgo físico u operacional inaceptable.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Diagrama Lógico de Flujo de Señales y Plano Unificado SecOps

```
+---------------------------------------------------------------------------------------------------+
|                         SENSORES Y CARGAS DE TRABAJO NATIVAS Y EXTENDIDAS                         |
+-------------------+-------------------+--------------------+------------------+-------------------+
| Endpoints & VDI   | Identidad Hibrida | Colaboracion/Email | SaaS, OAuth y    | Datos, Nube e IA  |
| Defender for      | Defender for ID   | Defender for       | Shadow IT        | Purview Suite,    |
| Endpoint P2 +     | (v3.x) + Entra ID | Office 365 P2      | Defender for     | Defender for Cloud|
| MDVM Core/Add-on  | Protection (P2)   | (Email/Teams/SPO)  | Cloud Apps       | y AgentsInfo      |
+---------+---------+---------+---------+---------+----------+--------+---------+---------+---------+
          |                   |                   |                   |                   |
          +-------------------+-------------------+-------------------+-------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                   PLANO OPERACIONAL UNIFICADO: MICROSOFT DEFENDER PORTAL                          |
|                                  https://security.microsoft.com                                   |
|                                                                                                   |
|  1. CORRELACION E INCIDENTES        2. CAZA Y DETECCION UNIFICADA   3. RESPUESTA Y CONTENCION     |
|  - Incident Queue & Incident Cases  - Advanced Hunting (KQL)        - Action Center unificado     |
|  - Attack Story + Queue Assistant   - Custom Detection Rules (NRT)  - Automatic Attack Disruption |
|  - Alert Tuning (antes Suppression) - Hunting Graph (Data Lake)     - AIR (MDO y pila AV en MDE)  |
|                                                                     - Predictive Shielding        |
|  4. EXPOSICION PREVENTIVA (CTEM)    5. SIEM INTEGRADO               6. IA AGENTICA Y GOBIERNO     |
|  - Security Exposure Management     - Microsoft Sentinel en portal  - Security Copilot embebido   |
|  - Attack Paths & Choke Points        Defender (fin Azure: 03/2027) - Security Alert Triage Agent |
|  - Critical Assets & Initiatives    - Sentinel Data Lake + SOAR     - Unified RBAC (URBAC)        |
+---------------------------------------------------------------------------------------------------+
```

### 3.2 Catálogo de Componentes Operativos y Rutas Verificadas

| Componente | Función Operativa en el Ciclo SecOps | Ruta en `security.microsoft.com` | Integraciones Clave | Estado |
|---|---|---|---|---|
| **Incident Queue & Incident Cases** | Consolidación automática de alertas multi-dominio en una única historia de ataque con puntaje de priorización explicable (0-100) y gestión de casos con tareas, SLA y auditoría en `SecurityCaseEvent` (Preview). | `Investigation & response > Incidents & alerts > Incidents` | MDE, MDI, MDO, MDCA, Purview, Defender for Cloud, Sentinel | `[Verificado MS Learn]` |
| **Automatic Attack Disruption & Predictive Shielding** | Contención en tiempo real (confianza >= 99 %) a nivel de incidente (`Contain user`, `Contain device`, `Contain IP`, `Isolate device`, `Disable user`, `Suspend user in Entra`) y endurecimiento proactivo (`Safeboot hardening`, `GPO hardening`, `Proactive user containment`). | `System > Settings > Microsoft Defender XDR > Automated response > Attack disruption` | MDE, MDI, Entra ID, Active Directory, MDCA, Okta/AWS vía Sentinel (Preview) | `[Verificado MS Learn]` |
| **Action Center Unificado** | Punto único de gobierno para aprobar o rechazar remediaciones pendientes, auditar el historial de ejecuciones automáticas/manuales y revertir (*Undo*) acciones de contención o cuarentena. | `Investigation & response > Actions & submissions > Action center` | AIR MDO, pila AV/AIR MDE, Attack Disruption, Live Response | `[Verificado MS Learn]` |
| **Advanced Hunting & Custom Detections** | Motor KQL sobre hasta 30 días de telemetría cruda XDR (y tablas de *Sentinel data lake*), con experiencia unificada de reglas de detección personalizadas (incluyendo frecuencia *Continuous / NRT* en tabla única) y *Hunting graph*. | `Investigation & response > Hunting > Advanced hunting` / `Custom detection rules` | Todas las tablas XDR, Exposure Graph, tablas de Microsoft Sentinel | `[Verificado MS Learn]` |
| **Alert Tuning** *(evolución de Alert Suppression)* | Motor de reducción de ruido para ocultar, resolver automáticamente o reclasificar alertas ruidosas como comportamientos (*behaviors*), incluyendo selección por fuente de detección y ajuste de reglas integradas. | `System > Settings > Microsoft Defender XDR > Alert tuning` | Cola de alertas e incidentes XDR y reglas integradas | `[Verificado MS Learn]` |
| **Microsoft Security Exposure Management (MSEM)** | Plataforma CTEM con grafo empresarial (`ExposureGraphNodes` / `ExposureGraphEdges`), mapa de superficie de ataque, rutas de ataque híbridas (on-prem/cloud, DACLs y *Choke points*), gestión de activos críticos e iniciativas medibles. | `Exposure management > Overview / Attack surface > Attack paths / Critical assets / Initiatives` | MDE, MDVM, MDI, Entra ID, Defender for Cloud (Azure/AWS/GCP), conectores externos | `[Verificado MS Learn]` |
| **Microsoft Sentinel en Defender Portal & ISOC** | Experiencia SIEM/SOAR convergente con sincronización bidireccional automática de incidentes, *Automation rules*, *Playbooks* (Logic Apps), *SOC Optimization* y almacenamiento en *Sentinel data lake* (o vista previa *ISOC* para clientes elegibles sin workspace Sentinel). | `Microsoft Sentinel` (menú lateral en `security.microsoft.com`) | Más de 300 conectores SIEM/multi-nube, Azure Logic Apps, Repositorios CI/CD | `[Verificado MS Learn]` |
| **Microsoft Security Copilot & Agentes en XDR** | Resumen contextual de incidentes, análisis de scripts/archivos, asistente KQL en lenguaje natural y triaje autónomo supervisado mediante *Security Alert Triage Agent* (GA para phishing; identidad y nube en Preview). | Panel lateral en `Incidents`, `Advanced hunting` y configuración de agentes | Telemetría XDR, Threat Intelligence, Entra ID, Purview, Intune | `[Verificado MS Learn]` |

---

## 4. Modelo de Gobierno, Roles SOC y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Arquitectura de Microsoft Defender Unified RBAC (URBAC)

Microsoft Defender Unified RBAC centraliza la administración de permisos de MDE, MDVM, MDI, MDO, MDCA, Defender for Cloud, Exposure Management y Microsoft Sentinel dentro de `security.microsoft.com > Permissions > Microsoft Defender XDR > Roles` `[Verificado MS Learn]`. Aspectos técnicos mandatorios de su diseño:

- **Cuatro categorías de permisos `[Verificado MS Learn]`:**
  1. *Security operations*: acceso a datos de seguridad (`Security data basics`, `Alerts`, `Response`, `Basic/Advanced live response`, `File collection`, `Email & collaboration quarantine / advanced actions`, `Automation rules`, `Playbooks`, `Integrations`) y acceso a datos crudos de correo/colaboración. Incorpora además la jerarquía granular de ejecución y aprobación: **`Execute query actions`**, **`Execute soft actions`**, **`Execute hard actions`**, **`Approve soft actions`** y **`Approve hard actions`**.
  2. *Security posture*: lectura y administración de *Vulnerability Management* y *Exposure Management* (Secure Score, iniciativas, rutas de ataque y activos críticos).
  3. *Authorization and settings*: administración de políticas de seguridad (*Core security settings*), configuración del sistema y el permiso crítico **`Authorization`**, que permite delegar la gestión de roles URBAC sin otorgar roles globales en Entra ID.
  4. *Data operations (Preview)*: control de permisos sobre colecciones de datos y analítica avanzada en *Microsoft Sentinel data lake*.
- **Reglas de activación y alcance `[Verificado MS Learn]`:** Para que URBAC entre en vigor en inquilinos existentes, cada carga de trabajo debe activarse explícitamente (en inquilinos nuevos de MDE/MDI desde 2025 y MDO P2 desde julio de 2026 ya viene activo por defecto). Microsoft Sentinel se activa **por workspace** (requiere *Security Administrator* en Entra ID más *Subscription Owner* o *User Access Administrator + Sentinel Contributor*). En URBAC, el rol *Global Administrator* **no concede permisos automáticos de lectura/operación sobre workspaces de Sentinel** a menos que se asigne explícitamente.

### 4.2 Diseño de Roles SOC y Segregación de Funciones (SoD)

La siguiente distribución operacional traduce los permisos verificados de URBAC en una estructura por niveles que impide que un mismo operador configure políticas, ejecute contenciones destructivas sin supervisión y audite sus propios cambios `[Decisión / Propuesta Editorial]`:

| Rol Funcional SOC | Nivel / Tier | Rol Entra ID / Permisos URBAC Requeridos | Estrategia PIM / JIT y Alcance (Scoping) | Responsabilidad Operativa | Estado |
|---|---|---|---|---|---|
| **Analista de Monitoreo y Triaje** | Tier 1 (L1) | Rol custom URBAC `SOC-Tier1-Triage`: `Security data basics (Read)`, `Alerts (Manage)`, `Execute query actions`, `Execute soft actions`. | Asignación permanente a grupo Entra dedicado con alcance por *Device groups* / fuentes asignadas; MFA obligatorio. | Monitoreo 24x7 de cola de incidentes, triaje inicial, comentarios, etiquetado y escalamiento sin capacidad de aislar activos ni borrar correos. | `[Decisión / Propuesta Editorial]` |
| **Analista de Respuesta a Incidentes** | Tier 2 (L2) | Rol custom URBAC `SOC-Tier2-Responder` (o equivalente *Security Operator*): suma `Response (Manage)`, `Execute hard actions`, `Basic live response`, `File collection`, `Email & collaboration quarantine/advanced actions`. | Elegible en **Entra ID PIM** (máximo 8 h por turno, MFA resistente a phishing FIDO2/Passkey y justificación de turno). | Contención activa (aislamiento de equipos, purga de phishing, aprobación de acciones pendientes en Action Center), Live Response básico y coordinación SOAR. | `[Decisión / Propuesta Editorial]` |
| **Threat Hunter / Analista Forense Senior** | Tier 3 (L3) y Detection Eng. | Rol custom URBAC `SOC-Tier3-Hunter`: suma `Advanced live response (Manage)`, `Custom detections (Manage)`, `Exposure Management (Read)`, `Data operations (Read)` sobre Data Lake. | Elegible en **Entra ID PIM** con aprobación dual o ticket de incidente mayor para `Advanced live response` (máx. 4 h). | Caza proactiva por hipótesis KQL, forensia profunda con ejecución de scripts firmados en Live Response, ingeniería de detecciones y Purple Team. | `[Decisión / Propuesta Editorial]` |
| **Ingeniero de Plataforma SecOps** | Ingeniería / Admin | Entra ID *Security Administrator* o rol custom URBAC `SecOps-Platform-Admin` con `Core security settings (Manage)`, `Automation rules/Playbooks/Integrations (Manage)`, `Exposure Management (Manage)`. | Estricto **JIT vía PIM** (máx. 4 h, aprobación de cambio CAB/SOC Lead y autenticación fuerte). | Configuración de conectores XDR/Sentinel, niveles de automatización, exclusiones de Attack Disruption, políticas MDO/MDE/MDI/MDCA y mantenimiento SOAR. | `[Verificado MS Learn]` |
| **Administrador de Autorización RBAC** | Gobierno IAM / SecAdmin | Rol custom URBAC con permiso `Authorization (Manage)` acotado o Entra ID *Security Administrator*. | Elegible en **PIM** con revisión de acceso mensual y alerta en SIEM ante cada alta/modificación de rol. | Creación, importación y auditoría de roles personalizados URBAC sin utilizar cuentas *Global Administrator*. | `[Verificado MS Learn]` |
| **Auditor / GRC / Privacidad (DPO)** | Gobierno y Auditoría | Entra ID *Security Reader* o rol custom URBAC `GRC-Audit-ReadOnly`: `Security data basics (Read)`, `Security posture (Read)`, `Authorization (Read-only)` **sin** permiso `Email & collaboration content (Read)`. | Asignación de solo lectura; acceso a contenido de mensajes restringido exclusivamente a flujo formal de eDiscovery/Legal. | Verificación de evidencias NIST CSF 2.0, seguimiento de Secure Score e iniciativas de exposición, preservando la privacidad de las comunicaciones. | `[Decisión / Propuesta Editorial]` |

### 4.3 Matriz RACI de Actividades Críticas del SOC

> Nota: Matriz organizacional de referencia (`R` = Responsable ejecutor, `A` = Aprobador final, `C` = Consultado, `I` = Informado) `[Decisión / Propuesta Editorial]`.

| Actividad Crítica | SOC L1 | SOC L2 | SOC L3 / Hunter | Ing. SecOps | IT Ops / IAM | GRC / Legal | SOC Lead / CISO |
|---|---|---|---|---|---|---|---|
| Triaje continuo y clasificación inicial de incidentes | **R** | C | I | — | — | — | **A** (SOC Lead) |
| Aprobación/rechazo de acciones pendientes en Action Center | C | **R** | C | — | I (si servidor) | — | **A** (SOC Lead) |
| Investigación multi-dominio, contención manual y reversión (*Undo*) | I | **R** | C | — | C | I | **A** (SOC Lead) |
| Respuesta mayor, forensia avanzada y *Advanced Live Response* | I | C | **R** | C | C | C | **A** (CISO) |
| Caza proactiva semanal y publicación de *Custom Detection Rules* | I | C | **R** | C | — | — | **A** (SOC Lead) |
| Ajuste de *Alert Tuning* y exclusiones de *Attack Disruption* | — | C | C | **R** | C | I | **A** (CISO) |
| Priorización de *Attack Paths* y activos críticos en Exposure Mgmt | — | I | C | **R** | **R** (parcheo) | C | **A** (CISO) |
| Gobierno de Unified RBAC, revisiones de acceso y reporte ejecutivo | — | — | — | **R** | C | **R** | **A** (CISO) |

---

## 5. Cadencia Operativa Diaria

> **Propósito:** Garantizar detección temprana, validación humana de contenciones automáticas, higiene de colas sin acumulación (*backlog*) y continuidad de señal en todo el plano XDR+SIEM.

### D-01 — Triaje Priorizado de la Cola Unificada de Incidentes y Casos
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` (o vista *Case management* si está habilitada) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `DE.CM-01`, `DE.AE-02`, `RS.AN-03` | MITRE: Multi-táctica (TA0001–TA0011).
- **Procedimiento:**
  1. Filtrar horizonte de **últimas 24 horas** (72 horas al inicio de semana), `Severity = High, Medium` y `Status = New, In progress` `[Verificado MS Learn]`.
  2. Ordenar por puntaje de priorización del **Queue Assistant** (0–100) e inspeccionar la etiqueta **`Attack Disruption`** o activos críticos coronados por *Exposure Management* `[Verificado MS Learn]`.
  3. Abrir el **Attack story** y el grafo de incidente para correlacionar entidades de correo, identidad, endpoint y aplicaciones cloud antes de actuar sobre alertas individuales `[Verificado MS Learn]`.
  4. Revisar el razonamiento del **Security Alert Triage Agent** (si está activo) validando su veredicto antes de aceptar cierres sugeridos `[Verificado MS Learn]`.
  5. Asignar propietario (*Assign to*), pasar estado a `In progress`, etiquetar contexto operativo y cumplir objetivo interno de reconocimiento (MTTA < 15 min para Crítico/Alto; < 60 min para Medio) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de actividad del incidente (*Comments & history* / tabla `SecurityCaseEvent` o `SecurityIncident` en Sentinel) con propietario, marca temporal y clasificación de cierre obligatoria.

### D-02 — Supervisión, Aprobación y Auditoría del Action Center (AIR y Attack Disruption)
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Actions & submissions > Action center` (`https://security.microsoft.com/action-center`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 (revisión) / SOC L2 (aprobación y reversión).
- **Alineación:** NIST `RS.MA-01`, `RS.MI-01`, `RC.RP-01` | MITRE: Execution / Lateral Movement (TA0002 / TA0008).
- **Procedimiento:**
  1. Abrir la pestaña **Pending** y ordenar por severidad y tipo de acción (*Isolate device*, *Quarantine file*, *Soft/Hard delete email*, *Disable user*) `[Verificado MS Learn]`.
  2. Inspeccionar el grafo de investigación asociado: elegir **Approve** ante amenaza confirmada, **Reject** ante falso positivo de negocio (documentando motivo) o **Go hunt** ante ambigüedad `[Verificado MS Learn]`.
  3. Auditar la pestaña **History** filtrando por proveedor *Attack disruption* y acciones automáticas de las últimas 24 h para descartar impacto colateral sobre cuentas ejecutivas o servidores críticos; ejecutar **Undo** / *Release from containment* solo tras validar erradicación `[Verificado MS Learn]`.
  4. Mantener cero acciones críticas pendientes con antigüedad mayor a 4 horas (recordando que las acciones pendientes expiran automáticamente a los 7 días) `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación CSV del historial del *Action Center* con usuario aprobador, timestamp y estado final.

### D-03 — Monitoreo de Detecciones de Identidad Híbrida (ITDR) y Usuarios Riesgosos
- **Consola / Ruta:** `security.microsoft.com > Identities > Dashboard` e `entra.microsoft.com > Protection > Identity Protection > Risky users` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `DE.CM-03`, `PR.AA-01` | MITRE: Credential Access / Defense Evasion (TA0006 / TA0005 — T1550, T1078).
- **Procedimiento:**
  1. Revisar en el panel **ITDR** usuarios con nivel de riesgo alto, señales unificadas de riesgo de identidad (Entra + MDI + MDE + MDCA + Purview) e intentos de acceso a cuentas *Honeytoken* `[Verificado MS Learn]`.
  2. Correlacionar alertas de robo de sesión (*Anomalous token*, *Adversary-in-the-middle*, *Pass-the-Hash*, *DCSync*) con `EntraIdSignInEvents` e `IdentityLogonEvents` `[Verificado MS Learn]`.
  3. Verificar la salud operativa de los sensores **Defender for Identity v3.x** en `System > Settings > Identities > Sensors` y `Health issues`, escalando de inmediato cualquier sensor desconectado en controladores de dominio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Alertas ITDR gestionadas, bitácora de remediación de riesgo en Entra ID y estado saludable de sensores MDI.

### D-04 — Revisión de Campañas Activas de Correo, Colaboración y Phishing Entregado
- **Consola / Ruta:** `security.microsoft.com > Email & collaboration > Investigations > Explorer` y `Campaigns` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `DE.CM-01`, `RS.MI-02` | MITRE: Initial Access (TA0001 — T1566.001, T1566.002).
- **Procedimiento:**
  1. Inspeccionar en **Campaigns** y **Threat Explorer** mensajes maliciosos o de phishing cuya acción de entrega final haya sido `Delivered` (no purgados aún por ZAP) y cruzar clics de usuarios en `UrlClickEvents` `[Verificado MS Learn]`.
  2. Revisar envíos reportados por usuarios en `Actions & submissions > Submissions > User reported` (y clasificaciones del *Security Alert Triage Agent*) `[Verificado MS Learn]`.
  3. Ejecutar purga masiva (*Soft delete* o *Hard delete*) sobre mensajes maliciosos confirmados y pivotar hacia las sesiones de usuarios que hicieron clic con veredicto permitido `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de remediación de correo en *Action Center* y métricas diarias de mensajes reportados/purgados.

### D-05 — Verificación de Integridad del Pipeline SIEM y Sincronización Bidireccional con Sentinel
- **Consola / Ruta:** `security.microsoft.com > System > Settings > Microsoft Sentinel` y `Investigation & response > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / SOC L1.
- **Alineación:** NIST `DE.CM-01`, `PR.PS-04` | MITRE: Defense Evasion (TA0005 — T1562).
- **Procedimiento:**
  1. Comprobar que el workspace primario de Microsoft Sentinel conectado al portal Defender figure en estado **Connected** y sin errores en `SentinelHealth` `[Verificado MS Learn]`.
  2. Ejecutar consulta diaria de *heartbeat* multi-dominio verificando volumen mayor a cero y ausencia de caídas bruscas en `DeviceEvents`, `IdentityLogonEvents`, `EmailEvents`, `CloudAppEvents` y `SecurityIncident` `[Verificado MS Learn]`.
  3. Confirmar latencia de sincronización de incidentes inferior a 15 minutos entre XDR y Sentinel `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Resultado diario de consulta KQL de salud de ingesta y estado de conectores.

### D-06 — Gestión Estructurada de Falsos Positivos, Falsos Negativos y Envíos a Microsoft
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Actions & submissions > Submissions` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Alineación:** NIST `DE.AE-02`, `RS.AN-03` | MITRE: Multi-táctica.
- **Procedimiento:**
  1. Ante falsos positivos confirmados o muestras evasivas (falsos negativos), enviar el artefacto (*Email*, *URL*, *Email attachment*, *File* o *File hash*) a Microsoft mediante **Submit to Microsoft for analysis** `[Verificado MS Learn]`.
  2. Clasificar rigurosamente cada incidente/alerta resuelto como `True positive`, `Informational, expected activity` (`Benign positive`) o `False positive` con nota técnica obligatoria `[Verificado MS Learn]`.
  3. Escalar patrones repetitivos de ruido legítimo a Ingeniería de Detecciones para crear reglas precisas en **Alert tuning** (nunca deshabilitar detectores globales) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial auditable en la pestaña *Submissions* y justificación en el cierre del incidente.

### D-07 — Revisión Diaria de Amenazas Críticas Inminentes (*Threat Analytics* y *Resolve Now*)
- **Consola / Ruta:** `security.microsoft.com > Threat intelligence > Threat analytics` y `Exposure management > Overview (Resolve Now)` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Threat Hunter L3.
- **Alineación:** NIST `ID.RA-01`, `DE.AE-07` | MITRE: Initial Access / Exploitation (T1190, T1203).
- **Procedimiento:**
  1. Revisar tarjetas **High-impact threats** y nuevos informes de analistas de Microsoft sobre vulnerabilidades 0-day o campañas activas de ransomware/extorsión `[Verificado MS Learn]`.
  2. Verificar en la sección **Resolve Now** de *Exposure Management* si existen activos críticos expuestos a Internet afectados por CVEs con explotación activa `[Verificado MS Learn]`.
  3. Emitir alerta temprana y solicitud de mitigación urgente a IT Operations cuando se detecten dispositivos o identidades impactados `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario de revisión de boletines críticos y tickets de mitigación de emergencia generados.

### D-08 — Higiene de Cola (*Queue Hygiene*) y Traspaso Formal entre Turnos (*Shift Handover*)
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` + Sistema ITSM / Bitácora SOC `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** SOC L1 / SOC Lead de turno.
- **Alineación:** NIST `RS.CO-02`, `GV.OV-01` | MITRE: N/A (Gobernanza operativa).
- **Procedimiento:**
  1. Verificar al cierre de cada guardia que existan **cero incidentes High/Critical en estado `New` sin propietario asignado** `[Decisión / Propuesta Editorial]`.
  2. Documentar en la minuta estructurada de cambio de turno: (a) incidentes críticos abiertos y próxima acción requerida, (b) activos actualmente contenidos por *Attack Disruption* o aislamiento manual, (c) acciones pendientes en *Action Center*, y (d) degradaciones de conectores o avisos urgentes del M365 Message Center `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta de *Shift Handover* firmada por analista saliente y entrante, más comentarios trazables en incidentes activos.

---

## 6. Cadencia Operativa Semanal

> **Propósito:** Reducir sistemáticamente la fatiga de alertas, descubrir amenazas evasivas mediante caza basada en hipótesis y cerrar rutas críticas de exposición.

### S-01 — Caza Proactiva de Amenazas Multi-Dominio Basada en Hipótesis (*Threat Hunting*)
- **Consola / Ruta:** `security.microsoft.com > Investigation & response > Hunting > Advanced hunting` y `Microsoft Sentinel > Hunting > Hunts` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter (SOC L3).
- **Alineación:** NIST `DE.AE-02`, `DE.CM-09` | MITRE: Persistence / Lateral Movement / Command and Control (TA0003 / TA0008 / TA0011).
- **Procedimiento:**
  1. Formular al menos 2 hipótesis semanales ancladas en informes recientes de *Threat Analytics* o tácticas MITRE ATT&CK prevalentes en el sector `[Decisión / Propuesta Editorial]`.
  2. Ejecutar consultas KQL correlacionando tablas multi-dominio (`EmailEvents` + `UrlClickEvents` + `EntraIdSignInEvents` + `DeviceProcessEvents` + `CloudAppEvents`) y explorar relaciones mediante **Hunting graph** `[Verificado MS Learn]`.
  3. Registrar la cacería en **Hunts** (hipótesis, consultas, marcadores, conclusión), abrir incidente ante hallazgos positivos y promover patrones repetibles a *Custom detection rules* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro cerrado de *Hunt* en el portal Defender (incluyendo hipótesis descartadas) y nuevas reglas creadas.

### S-02 — Ingeniería de Detecciones y Ajuste de Ruido (*Custom Detections* y *Alert Tuning*)
- **Consola / Ruta:** `Investigation & response > Hunting > Custom detection rules` y `System > Settings > Microsoft Defender XDR > Alert tuning` `[Verificado MS Learn]`.
- **Rol Responsable:** Detection Engineer / SOC L3.
- **Alineación:** NIST `DE.AE-04`, `DE.CM-06` | MITRE: Multi-táctica.
- **Procedimiento:**
  1. Identificar las 5 reglas (integradas o personalizadas) con mayor tasa de falsos positivos en los últimos 7 días `[Decisión / Propuesta Editorial]`.
  2. Refinar las consultas KQL de *Custom detection rules* (incluyendo reglas *Continuous / NRT*) o configurar condiciones acotadas en **Alert tuning** seleccionando entidad y fuente de detección exacta `[Verificado MS Learn]`.
  3. Si las reglas se gestionan como código en *Sentinel Repositories*, aplicar el cambio vía pull request con revisión de pares y verificar nombres vigentes de tablas (ej. migración a `EntraIdSignInEvents`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de modificaciones en *Alert tuning* / repositorio Git y reducción medida de FP por regla.

### S-03 — Análisis y Remediación de Rutas de Ataque (*Attack Paths*) y *Choke Points*
- **Consola / Ruta:** `security.microsoft.com > Exposure management > Attack surface > Attack paths` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / Security Architect.
- **Alineación:** NIST `ID.RA-05`, `PR.PS-01` | MITRE: Privilege Escalation / Lateral Movement (TA0004 / TA0008).
- **Procedimiento:**
  1. Revisar la pestaña **Overview** y **Choke points** para localizar nodos cuello de botella donde convergen múltiples rutas de ataque hacia activos críticos (incluyendo rutas híbridas on-prem a nube y permisos DACL) `[Verificado MS Learn]`.
  2. Priorizar las rutas de nivel de riesgo *High* explotables externamente y extraer las recomendaciones accionables de mitigación `[Verificado MS Learn]`.
  3. Asignar tickets de remediación a propietarios de infraestructura/identidad y rastrear la disminución semanal de rutas activas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Captura/exportación de *Choke points* y tickets ITSM asociados.

### S-04 — Revisión de Aplicaciones OAuth, Shadow IT y Riesgo de Agentes de IA
- **Consola / Ruta:** `security.microsoft.com > Cloud apps > OAuth apps` / `Cloud discovery` y tabla `AgentsInfo` / `OAuthAppInfo` en *Advanced hunting* `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Ingeniero de Plataforma SecOps.
- **Alineación:** NIST `ID.AM-02`, `PR.AA-05` | MITRE: Persistence / Collection (T1098.003, T1528).
- **Procedimiento:**
  1. Auditar nuevas aplicaciones OAuth registradas o consentidas durante la semana con privilegios altos (`Mail.ReadWrite`, `Directory.ReadWrite.All`, `Files.ReadWrite.All`) y puntuaciones bajas de cumplimiento en *Cloud app catalog* `[Verificado MS Learn]`.
  2. Consultar las tablas `AgentsInfo` y `EntraIdSpnSignInEvents` para detectar identidades de carga de trabajo o agentes de IA anómalos `[Verificado MS Learn]`.
  3. Revocar consentimientos ilícitos y bloquear aplicaciones no sancionadas conforme a política corporativa `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de gobernanza OAuth/Shadow IT y acciones de revocación registradas.

### S-05 — Seguimiento Semanal de Microsoft Secure Score, Iniciativas de Exposición y Configuración MDO
- **Consola / Ruta:** `Exposure management > Initiatives` / `Secure score` y `Email & collaboration > Policies & rules > Threat policies > Configuration analyzer` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / GRC.
- **Alineación:** NIST `GV.OV-01`, `PR.PS-01` | MITRE: Defense Evasion / Initial Access.
- **Procedimiento:**
  1. Evaluar la variación de 7 y 14 días en **Microsoft Secure Score** y en las **Security initiatives** activas (Endpoint, Identity, Cloud, Zero Trust, Ransomware protection) `[Verificado MS Learn]`.
  2. Ejecutar **Configuration analyzer** en Defender for Office 365 verificando desviaciones respecto a los perfiles recomendados *Standard* y *Strict* `[Verificado MS Learn]`.
  3. Planificar el despliegue controlado de al menos las 3 recomendaciones de mayor impacto pendiente `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación de tendencia de *Secure Score* / *Initiatives* y reporte sin desvíos críticos en *Configuration analyzer*.

### S-06 — Revisión Semanal de Post-Incident Review (PIR), SLAs por Percentiles y Message Center
- **Consola / Ruta:** `admin.microsoft.com > Health > Message center`, `learn.microsoft.com/en-us/defender-xdr/whats-new` y Workbook *Security operations efficiency* `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Lead / Ingeniero de Plataforma SecOps.
- **Alineación:** NIST `RS.IM-01`, `GV.OV-03` | MITRE: N/A.
- **Procedimiento:**
  1. Conducir revisión post-incidente (PIR) de la totalidad de incidentes *High/Critical* cerrados en la semana, validando causa raíz, tiempo de contención y tasa de reapertura `[Decisión / Propuesta Editorial]`.
  2. Calcular mediana (p50) y percentil 90 (p90) de MTTA, MTTC y MTTR evitando promedios distorsionados por casos atípicos `[Decisión / Propuesta Editorial]`.
  3. Revisar anuncios de **Microsoft 365 Message Center** (filtro *Microsoft Defender XDR* / *Microsoft Sentinel*) y páginas *What's new*, convirtiendo deprecaciones de tablas/APIs o nuevas capacidades en tareas del backlog técnico `[Verificado MS Learn]`.
- **Evidencia Auditable:** Actas PIR semanales, tablero de métricas p50/p90 y backlog de cambios de plataforma actualizado.

---

## 7. Cadencia Operativa Mensual

> **Propósito:** Consolidar el gobierno de accesos, optimizar costos/valor de telemetría, auditar exclusiones críticas y presentar resultados medibles de reducción de riesgo a la alta dirección.

### M-01 — Auditoría Mensual de Microsoft Defender Unified RBAC y Activaciones PIM
- **Consola / Ruta:** `security.microsoft.com > Permissions > Microsoft Defender XDR > Roles` y `entra.microsoft.com > Identity governance > Privileged Identity Management` `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador de Autorización RBAC / GRC.
- **Alineación:** NIST `PR.AA-05`, `GV.RR-02` | MITRE: Valid Accounts (T1078.004).
- **Procedimiento:**
  1. Exportar todos los roles personalizados e importados en **Unified RBAC**, revisando asignaciones de usuarios/grupos y alcances de fuentes de datos / *Device groups* `[Verificado MS Learn]`.
  2. Auditar que ningún analista L1 posea `Execute hard actions` ni `Advanced live response`, y eliminar asignaciones huérfanas o de personal desvinculado `[Decisión / Propuesta Editorial]`.
  3. Revisar el historial mensual de activaciones JIT en Entra ID PIM para *Security Administrator* y roles de respuesta avanzada, verificando ticket justificativo válido `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación de configuración URBAC, registro de auditoría PIM y acta mensual de certificación de privilegios.

### M-02 — Revisión de Activos Críticos, Exclusiones de Attack Disruption y Listas Allow/Block
- **Consola / Ruta:** `Exposure management > Critical asset management`, `Settings > Microsoft Defender XDR > Automated response > Attack disruption` y `Email & collaboration > Policies & rules > Threat policies > Tenant Allow/Block Lists` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / Security Architect.
- **Alineación:** NIST `ID.AM-05`, `PR.PS-01` | MITRE: Defense Evasion (T1562.001).
- **Procedimiento:**
  1. Actualizar las reglas de clasificación en **Critical asset management** asegurando que nuevos servidores de negocio, aplicaciones críticas y cuentas VIP reciban el nivel de criticidad adecuado `[Verificado MS Learn]`.
  2. Auditar exhaustivamente la lista de activos excluidos de **Automatic Attack Disruption** (usuarios, dispositivos, IPs), revocando cualquier exclusión temporal sin riesgo operativo vigente `[Verificado MS Learn]`.
  3. Depurar entradas expiradas o innecesarias en *Tenant Allow/Block Lists* (MDO), indicadores *Allow* (MDE) y exclusiones de identidad (MDI) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario firmado de excepciones y exclusiones vigentes con propietario y fecha de caducidad.

### M-03 — Optimización del SOC, Valor de Ingesta y Retención en Sentinel Data Lake
- **Consola / Ruta:** `security.microsoft.com > Microsoft Sentinel > SOC optimization` y `System > Settings > Microsoft Sentinel > Tables` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / SOC Lead.
- **Alineación:** NIST `GV.RM-06`, `DE.CM-01` | MITRE: Cobertura por escenario de amenaza.
- **Procedimiento:**
  1. Analizar recomendaciones de **SOC optimization** en dos ejes: brechas de cobertura frente a escenarios de amenaza y valor de detección por tabla facturable en los últimos 30 días `[Verificado MS Learn]`.
  2. Ajustar el nivel de almacenamiento (*Analytics tier* vs. *Data lake tier*) y períodos de retención de tablas XDR y SIEM desde el portal Defender, garantizando retención normativa sin sobrecostos por tablas sin uso analítico ni forense `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de *SOC optimization* y registro de cambios de retención por tabla.

### M-04 — Auditoría de Automatizaciones SOAR, Playbooks y Gobierno de Agentes Security Copilot
- **Consola / Ruta:** `Microsoft Sentinel > Configuration > Automation` y panel de agentes de *Security Copilot* en `security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps.
- **Alineación:** NIST `RS.MA-01`, `GV.PO-02` | MITRE: Automated Response.
- **Procedimiento:**
  1. Auditar la tasa de éxito y fallos de ejecución de *Automation rules* y *Playbooks* (Logic Apps), verificando identidades administradas, cuotas de API (`alerts_v2` / `incidents` / `runHuntingQuery`) y latencia `[Verificado MS Learn]`.
  2. Evaluar métricas de precisión, consumo de **SCU** (dentro de la dotación E5 o capacidad aprovisionada) y tasa de acuerdo analista-agente del **Security Alert Triage Agent** `[Verificado MS Learn]`.
  3. Validar mediante prueba controlada que todo flujo de contención automatizada cuente con su procedimiento de reversión operativo `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora mensual de salud SOAR, reporte de consumo SCU y muestreo de calidad agéntica.

### M-05 — Evaluación de Cobertura de Sensores XDR en Todos los Dominios
- **Consola / Ruta:** `Assets > Devices` (`Onboarding status = Can be onboarded`), `Settings > Identities > Sensors` y `Cloud apps > Connected apps` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Plataforma SecOps / IT Operations.
- **Alineación:** NIST `ID.AM-01`, `DE.CM-09` | MITRE: Unprotected Assets.
- **Procedimiento:**
  1. Cruzar el inventario corporativo (CMDB / Entra ID / Active Directory) contra activos incorporados a MDE, controladores de dominio/AD FS/AD CS cubiertos por **MDI sensor v3.x** y conectores de aplicaciones SaaS en MDCA `[Verificado MS Learn]`.
  2. Exportar dispositivos descubiertos por *Standard Device Discovery* en estado `Can be onboarded` y emitir tickets de incorporación con meta > 98 % de cobertura `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Conciliación mensual de cobertura XDR por dominio y plan de cierre de brechas.

### M-06 — Comité Ejecutivo Mensual de Excelencia SecOps y Reporte de Resultados al CISO
- **Consola / Ruta:** `Reports > Security report` (*Monthly Security Summary*), `Exposure management > Overview` y Tablero Ejecutivo Power BI / Workbook `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Lead / GRC / CISO.
- **Alineación:** NIST `GV.OV-01`, `GV.RM-07` | MITRE: Cobertura estratégica.
- **Procedimiento:**
  1. Consolidar reporte ejecutivo centrado en **resultados de riesgo** (reducción en puntaje de iniciativas de exposición, rutas críticas cerradas, incidentes contenidos automáticamente por *Attack Disruption*, mediana/p90 de MTTA/MTTC/MTTR y aprovechamiento de licencias E5) `[Decisión / Propuesta Editorial]`.
  2. Revisar formalmente las excepciones de riesgo (*Risk accepted* / *Exemptions* en Exposure Management) próximas a vencer `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete ejecutivo mensual aprobado por el CISO y acta del Comité de Seguridad.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 — Ejercicio Trimestral de Mesa (*Tabletop*) y Emulación de Adversario (*Purple Team*) [Trimestral]
- **Consola / Ruta:** `security.microsoft.com > Evaluation & tutorials` (en entorno de laboratorio aislado) + Playbooks SecOps del SAF `[Verificado MS Learn]`.
- **Rol Responsable:** CSIRT Lead / SOC L3 / CISO.
- **Alineación:** NIST `RS.MA-04`, `RC.RP-02`, `ID.IM-02`.
- **Procedimiento:** Ejecutar un ejercicio trimestral rotando los escenarios críticos del SAF (Ransomware operado por humanos, robo de token AiTM, compromiso OAuth/aplicación maliciosa, BEC financiero) con participación de SOC, TI, Legal, Comunicaciones y Negocio; complementar en laboratorio con pruebas controladas de técnicas MITRE ATT&CK para verificar que las reglas realmente disparen alertas y contenciones `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe *After-Action Report* (AAR) con tiempos medidos y brechas de detección registradas como tareas.

### SM-01 — Evaluación Semestral de Cobertura MITRE ATT&CK y Salud de Ingeniería de Detecciones [Semestral]
- **Consola / Ruta:** `Microsoft Sentinel > Threat management > MITRE ATT&CK` y `Hunting > Custom detection rules` `[Verificado MS Learn]`.
- **Rol Responsable:** Detection Engineering Lead / SOC L3.
- **Alineación:** NIST `DE.AE-08`, `ID.RA-03`.
- **Procedimiento:** Contrastar la matriz **MITRE ATT&CK** en el portal Defender contra el modelo de amenazas de la organización, retirando reglas obsoletas (> 90 días sin valor ni vigencia) y priorizando nuevas detecciones sobre técnicas validadas sin cobertura probada `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Línea base semestral de cobertura ATT&CK validada y catálogo depurado de reglas.

### SM-02 — Revisión Semestral de Arquitectura Unified SecOps, Migración de Portal y Runbooks [Semestral]
- **Consola / Ruta:** `security.microsoft.com` (configuración global XDR, Sentinel, URBAC y APIs) `[Verificado MS Learn]`.
- **Rol Responsable:** Security Architect / SOC Manager.
- **Alineación:** NIST `GV.OV-02`, `PR.IR-01`.
- **Procedimiento:** Validar el estado de transición total al portal Defender antes del hito obligatorio del **31 de marzo de 2027** (retiro de Sentinel en Azure Portal), auditar la migración completa desde APIs heredadas retiradas (`/security/alerts` retirada en oct 2026; APIs legacy de búsqueda avanzada con corte en feb 2027) hacia Microsoft Graph Security API (`alerts_v2`, `incidents`, `runHuntingQuery`), y actualizar todos los SOP/runbooks versionados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe de revisión arquitectónica semestral y repositorio de runbooks firmado.

### A-01 — Evaluación Anual de Madurez del SOC (NIST CSF 2.0 / SOC-CMM) y Revisión Integral del Programa [Anual]
- **Consola / Ruta:** Evidencias consolidadas de `security.microsoft.com`, Purview Audit y marco NIST CSF 2.0 / SOC-CMM `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** CISO / GRC / Auditoría Externa.
- **Alineación:** NIST `GV.OV-03`, `ID.IM-01`, `RC.IM-02`.
- **Procedimiento:** Ejecutar evaluación anual basada en evidencias (no autopercepción) sobre las 6 funciones de NIST CSF 2.0 y los dominios del marco de excelencia SOC (estrategia, roles, visibilidad, triaje, respuesta, ingeniería de detección, hunting, automatización/IA, exposición y bienestar del equipo), complementada con ejercicio Red Team anual y presentación de hoja de ruta y ROI M365 E5 al Directorio `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Dossier anual de auditoría NIST CSF 2.0, reporte Red Team y plan estratégico anual aprobado por el Board.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

> Basados en los playbooks públicos de la disciplina SecOps del *Microsoft Security Adoption Framework (SAF)* actualizados en 2026 y en *NIST SP 800-61 Rev. 3* `[Verificado MS Learn]`. **Regla crítica:** Antes de ejecutar contenciones disruptivas masivas, preservar evidencia volátil y confirmar el mecanismo de reversión.

### AH-01 — Playbook ante Ransomware Operado por Humanos (*Human-Operated Ransomware*) y *Attack Disruption*
- **Disparador:** Incidente crítico con etiqueta **`Attack Disruption`**, alertas de volcado de credenciales, desactivación de controles (*Tampering*), movimiento lateral SMB/WMI/RDP o cifrado incipiente `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Verificación inmediata de contención automática (0–15 min):** Abrir el incidente en `security.microsoft.com`, revisar el banner amarillo de *Automatic Attack Disruption* y confirmar en el grafo qué hosts e identidades ya fueron aislados/suspendidos (`Isolate device`, `Contain device`, `Contain IP`, `Contain user`, `Disable user`) `[Verificado MS Learn]`.
  2. **Ampliación quirúrgica del cerco:** Aislar manualmente (`Isolate device` — sin apagar el equipo para no destruir artefactos en RAM) cualquier servidor o estación puente identificada en el *Attack story*, aplicar `Restrict app execution` en segmentos en riesgo y verificar desconexión/inmutabilidad de copias de seguridad `[Verificado MS Learn]`.
  3. **Contención de privilegios Tier-0:** Suspender cuentas administrativas comprometidas en Active Directory y Entra ID, revocar tokens de actualización, rotar credenciales afectadas (y evaluar doble rotación de `krbtgt` si hubo compromiso de dominio tipo *DCSync* / *Golden Ticket*) `[Verificado MS Learn]`.
  4. **Erradicación y liberación controlada:** Analizar persistencia (tareas programadas, servicios, WMI, GPOs) con *Live Response* y *Advanced Hunting*; solo tras validar ausencia de implantes y parchar el vector inicial, ejecutar **Release from containment** / **Undo** desde el *Action Center* con monitoreo reforzado de 72 h `[Verificado MS Learn]`.

### AH-02 — Playbook ante Robo de Token de Sesión / Phishing *Adversary-in-the-Middle* (AiTM)
- **Disparador:** Alerta *Anomalous token*, *Unfamiliar sign-in properties*, acceso sospechoso al *Primary Refresh Token (PRT)* en MDE o clic permitido en `UrlClickEvents` seguido de inicio de sesión desde infraestructura proxy `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Corte inmediato de sesión e identidad:** Ejecutar acción **Mark user as compromised** y **Revoke user session** / **Suspend user in Entra** desde el panel de usuario del incidente (o vía playbook `Revoke-AADSignInSessions`) — cambiar únicamente la contraseña **no** invalida tokens de sesión ya robados si no se revocan los *refresh tokens* `[Verificado MS Learn]`.
  2. **Auditoría de persistencia post-acceso:** Inspeccionar en `CloudAppEvents` y registros de auditoría de Entra ID si el atacante registró nuevos métodos MFA/dispositivos, creó reglas de bandeja de entrada ocultas en Exchange Online o consintió aplicaciones OAuth `[Verificado MS Learn]`.
  3. **Remediación y endurecimiento:** Eliminar métodos MFA fraudulentos y reglas de reenvío/borrado, aislar el endpoint si hubo robo local de PRT y migrar al usuario afectado a una política de Acceso Condicional con MFA resistente a phishing (Passkey/FIDO2) y protección de inicio de sesión basada en riesgo `[Verificado MS Learn]`.

### AH-03 — Playbook ante Compromiso de Correo Empresarial (BEC) y Campaña Masiva de Phishing
- **Disparador:** Alerta de creación de reglas sospechosas de reenvío/ocultamiento, envío masivo desde buzón interno (*User restricted from sending email*) o campaña activa multi-buzón en MDO `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Contención de cuenta y buzón:** Deshabilitar temporalmente la cuenta en Entra ID, revocar sesiones activas y verificar delegaciones de buzón y conectores de transporte en Exchange Online `[Verificado MS Learn]`.
  2. **Retro-caza y purga global:** Buscar en *Threat Explorer* y en `EmailEvents` / `EmailUrlInfo` todos los mensajes internos y externos enviados o recibidos de la campaña en los últimos 30 días, ejecutando **Hard delete** masivo y bloqueando remitentes/dominios/URLs en *Tenant Allow/Block List* `[Verificado MS Learn]`.
  3. **Notificación antifraude:** Alertar de inmediato a Tesorería/Finanzas y Legal si el hilo involucró cambio de cuentas bancarias o facturas (*payment diversion*) `[Decisión / Propuesta Editorial]`.

### AH-04 — Playbook ante Concesión Ilícita de Consentimiento y Aplicación OAuth Comprometida
- **Disparador:** Evento `Consent to application` con `IsAdminConsent=True` no autorizado, alerta *Risky application detected* o actividad anómala de *Service Principal* en `EntraIdSpnSignInEvents` / `GraphAPIAuditEvents` `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Deshabilitación sin destrucción forense:** Deshabilitar el *Service Principal* (`accountEnabled = false` en *Enterprise applications*) **sin borrar el objeto** para preservar los registros de auditoría e identificadores `[Verificado MS Learn]`.
  2. **Revocación de permisos y credenciales:** Revocar concesiones OAuth (`oauth2PermissionGrants` / roles de aplicación), rotar/eliminar secretos y certificados comprometidos de la aplicación y bloquear la app en Defender for Cloud Apps `[Verificado MS Learn]`.
  3. **Alcance de exfiltración:** Auditar en `GraphAPIAuditEvents` y `CloudAppEvents` todos los buzones, archivos de SharePoint/OneDrive o directorios leídos por el `AppId` comprometido para evaluación de impacto regulatorio `[Verificado MS Learn]`.

### AH-05 — Respuesta Rápida ante Vulnerabilidad Crítica Emergente (*Zero-Day* / Explotación Activa)
- **Disparador:** Publicación urgente en *Threat Analytics* o boletín CISA KEV / MSRC con CVSS >= 9.0 o explotación in-the-wild `[Verificado MS Learn]`.
- **Secuencia Operativa:**
  1. **Dimensionamiento en minutos:** Consultar el informe de *Threat Analytics* y ejecutar consulta de grafo sobre `ExposureGraphNodes` / `ExposureGraphEdges` + `DeviceTvmSoftwareVulnerabilities` para listar activos expuestos a Internet o con ruta hacia activos críticos `[Verificado MS Learn]`.
  2. **Controles compensatorios inmediatos:** Desplegar indicadores de bloqueo (IoCs), reglas ASR pertinentes o reglas de detección personalizada KQL mientras TI despliega el parche de emergencia (meta editorial < 48 h para activos expuestos) `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

Todas las consultas siguientes utilizan tablas y columnas oficiales del esquema de **Advanced Hunting** de Microsoft Defender XDR y de **Microsoft Sentinel** verificadas a noviembre de 2026 `[Verificado MS Learn]`.

### 10.1 Salud Diaria del Pipeline Multi-Dominio XDR (Heartbeat de Sensores)
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Propósito: Confirmar recepción continua de telemetría en los 4 dominios XDR + Entra ID en las últimas 24h
union withsource=TablaOrigen
    (DeviceEvents | where Timestamp > ago(24h)),
    (IdentityLogonEvents | where Timestamp > ago(24h)),
    (EntraIdSignInEvents | where Timestamp > ago(24h)),
    (EmailEvents | where Timestamp > ago(24h)),
    (CloudAppEvents | where Timestamp > ago(24h))
| summarize TotalEventos = count(), UltimoEvento = max(Timestamp) by TablaOrigen
| extend MinutosSinDatos = datetime_diff('minute', now(), UltimoEvento)
| order by MinutosSinDatos desc
```

### 10.2 Auditoría de Correlación Multi-Fuente y Tácticas MITRE ATT&CK en Incidentes/Alertas
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Tablas: AlertInfo + AlertEvidence
// Propósito: Evidenciar correlación nativa entre múltiples productos Defender (ej. para auditoría NIST DE.AE-03)
AlertInfo
| where Timestamp > ago(30d)
| join kind=inner (
    AlertEvidence
    | where Timestamp > ago(30d)
    | summarize Entidades = make_set(EntityType), RolesEvidencia = make_set(EvidenceRole) by AlertId
) on AlertId
| summarize
    TotalAlertas = dcount(AlertId),
    FuentesServicio = make_set(ServiceSource),
    Categorias = make_set(Category),
    TecnicasMITRE = make_set(AttackTechniques),
    TiposEntidad = make_set(Entidades)
    by Severity
| order by TotalAlertas desc
```

### 10.3 Seguimiento de Eventos de Contención Automática (*Automatic Attack Disruption*)
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Tabla: DisruptionAndResponseEvents (Preview)
// Propósito: Auditar activos contenidos automáticamente por Attack Disruption o Predictive Shielding
DisruptionAndResponseEvents
| where Timestamp > ago(7d)
| project Timestamp, ActionType, ReportId, AccountName, AccountDomain, DeviceName, RemoteIP, AdditionalFields
| order by Timestamp desc
```

### 10.4 Correlación Cross-Domain de Phishing Entregado + Clic en Safe Links + Inicio de Sesión Riesgoso (AiTM)
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Tablas: EmailEvents + UrlClickEvents + EntraIdSignInEvents
// Propósito: Detectar usuarios que recibieron correo externo, hicieron clic permitido y registraron sesión riesgosa
let ClicsSospechosos = UrlClickEvents
    | where Timestamp > ago(7d)
    | where ActionType in ("ClickAllowed", "UrlErrorPage") and IsClickedThrough == true
    | project ClickTime = Timestamp, AccountUpn = tolower(AccountUpn), Url, NetworkMessageId;
EmailEvents
| where Timestamp > ago(7d) and EmailDirection == "Inbound" and DeliveryAction == "Delivered"
| project EmailTime = Timestamp, Recipient = tolower(RecipientEmailAddress), SenderFromAddress, Subject, NetworkMessageId
| join kind=inner ClicsSospechosos on NetworkMessageId
| join kind=inner (
    EntraIdSignInEvents
    | where Timestamp > ago(7d)
    | where RiskLevelDuringSignIn in (50, 100) or ErrorCode == 0
    | project SignInTime = Timestamp, AccountUpn = tolower(AccountUpn), IPAddress, Country, Application, SessionId
) on AccountUpn
| where SignInTime between (ClickTime .. (ClickTime + 2h))
| project EmailTime, ClickTime, SignInTime, AccountUpn, SenderFromAddress, Subject, Url, IPAddress, Country, Application
```

### 10.5 Consulta del Grafo de Exposición Empresarial (*ExposureGraphNodes* y *ExposureGraphEdges*)
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting (Exposure Management)
// Tablas: ExposureGraphNodes + ExposureGraphEdges | Operadores: make-graph, graph-match
// Propósito: Identificar endpoints con vulnerabilidades RCE que pueden autenticar hacia activos críticos (criticidad < 4 / alta)
let NodosRelevantes = ExposureGraphNodes
    | extend Criticidad = toint(NodeProperties.rawData.criticalityLevel.criticalityLevel),
             TieneRCE = isnotnull(NodeProperties.rawData.vulnerableToRCE)
    | where NodeLabel == "device" or NodeLabel == "identity" or Criticidad > 0;
ExposureGraphEdges
| make-graph SourceNodeId --> TargetNodeId with NodosRelevantes on NodeId
| graph-match (Origen)-[Relacion*1..3]->(ActivoCritico)
    where Origen.TieneRCE == true and toint(ActivoCritico.NodeProperties.rawData.criticalityLevel.criticalityLevel) <= 2
| project DispositivoExpuesto = Origen.NodeName, ActivoDestino = ActivoCritico.NodeName, EtiquetaDestino = ActivoCritico.NodeLabel
```

### 10.6 Cálculo Reproducible de Métricas SOC por Percentiles (p50 y p90) en Microsoft Sentinel
```kql
// Plataforma: Microsoft Sentinel / Defender Portal (Workspace Logs)
// Tabla: SecurityIncident (deduplicación obligatoria con arg_max por IncidentNumber)
// Propósito: Medir mediana (p50) y percentil 90 (p90) de MTTA y MTTR por severidad evitando sesgos de promedios
SecurityIncident
| where TimeGenerated > ago(30d)
| summarize arg_max(TimeGenerated, *) by IncidentNumber
| where Status == "Closed"
| extend MTTA_Min = datetime_diff('minute', FirstModifiedTime, CreatedTime),
         MTTR_Horas = round(datetime_diff('minute', ClosedTime, CreatedTime) / 60.0, 2)
| summarize
    TotalCerrados = count(),
    MTTA_p50_Min = percentile(MTTA_Min, 50),
    MTTA_p90_Min = percentile(MTTA_Min, 90),
    MTTR_p50_Horas = percentile(MTTR_Horas, 50),
    MTTR_p90_Horas = percentile(MTTR_Horas, 90),
    TasaFP_Pct = round(100.0 * countif(Classification == "FalsePositive") / count(), 1)
    by Severity
| order by TotalCerrados desc
```

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operativos y Estratégicos

> **Regla metodológica:** Microsoft documenta las columnas de métricas en `SecurityIncident` y el workbook *Security operations efficiency* `[Verificado MS Learn]`, pero advierte que cada organización debe fijar sus umbrales objetivo según dotación y criticidad; por tanto, todas las metas cuantitativas siguientes constituyen `[Decisión / Propuesta Editorial]`. Se recomienda reportar siempre **mediana (p50) y percentil 90 (p90)** emparejando cada métrica de velocidad con un contrapeso de calidad.

| ID | Indicador (KPI) | Fórmula / Fuente Técnica | Meta Sugerida | Frecuencia | Audiencia | Contrapeso de Calidad / Estado |
|---|---|---|---|---|---|---|
| **KPI-01** | **Tiempo de Triaje / Reconocimiento (MTTA p50/p90)** | `percentiles(FirstModifiedTime - CreatedTime, 50, 90)` en `SecurityIncident` (excluir toques automáticos SOAR) | Crítico/Alto: p50 < 15 min, p90 < 30 min; Medio: p90 < 2 h | Semanal | SOC Lead | Emparejar con calidad de clasificación inicial `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tiempo hasta Primera Contención (MTTC p50/p90)** | `Timestamp_PrimeraAccionContencion` (*Action Center* / `DisruptionAndResponseEvents`) - `CreatedTime` | Crítico/Alto: p50 < 15 min (con Attack Disruption), manual p90 < 60 min | Semanal | SOC Lead / CISO | Emparejar con tasa de acciones revertidas (*Undo*) `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tiempo de Resolución y Cierre (MTTR p50/p90)** | `percentiles(ClosedTime - CreatedTime, 50, 90)` en `SecurityIncident` (publicar definición explícita) | Alto: p50 < 6 h, p90 < 24 h; Medio: p90 < 72 h | Mensual | SOC Manager / CISO | Emparejar con tasa de reapertura (< 5 %) `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tasa de Falsos Positivos por Regla (FP Rate)** | `100 * countif(Classification == 'FalsePositive') / count()` sobre incidentes cerrados | Global < 15 %; ninguna regla custom > 20 % sostenido | Semanal | Detection Eng. | Auditar cierres *Undetermined* para evitar ocultamiento `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa de Contención y Resolución Automatizada** | % incidentes/acciones resueltos vía *Attack Disruption*, *AIR* o playbooks/agentes sobre total elegible | > 50 % en severidad Baja/Media; 100 % de detectores Attack Disruption activos | Mensual | SOC Lead / CISO | Monitorear `% Acciones Revertidas` (< 2 %) `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Conversión de Threat Hunting** | `Hunts que generan Custom Detection, mejora de postura o incidente real / Total Hunts cerrados` | >= 20 % de sesiones de caza convertidas en control duradero | Mensual | SOC L3 / Lead | Valorar también hipótesis documentadas descartadas `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Reducción de Rutas de Ataque Críticas (CTEM)** | Variación mensual de *Attack paths* de riesgo alto hacia activos críticos y puntaje de *Security initiatives* | Reducción neta mensual de *Choke points* críticos; iniciativas en meta | Mensual | CISO / Comité Riesgo | Basado en `Exposure management` `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Cobertura Validada MITRE ATT&CK** | `Técnicas prioritarias del modelo de amenazas con regla activa + prueba Purple Team exitosa / Total técnicas prioritarias` | >= 75 % sobre técnicas prioritarias del sector | Semestral | Security Architect / CISO | Contar solo técnicas probadas con telemetría real `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional del SOC sobre Defender XDR

Modelo consultivo en cuatro estadios alineado con la disciplina SecOps del SAF, SOC-CMM y NIST CSF 2.0 `[Decisión / Propuesta Editorial]`:

| Nivel de Madurez | Perfil Operativo | Características Verificables en Defender XDR |
|---|---|---|
| **Nivel 1 — Reactivo (Silos de Alertas)** | Operación en consolas fragmentadas, triaje manual alerta por alerta, RBAC heredado por producto, sin automatización activa. | MTTA p90 > 4 h; alta fatiga de falsos positivos (> 35 %); *Action Center* no revisado diariamente; Sentinel operado aún separado del portal Defender. |
| **Nivel 2 — Gestionado y Correlacionado (XDR Integrado)** | Operación centralizada sobre **incidentes** en `security.microsoft.com`, *Unified RBAC* activado, *Automatic Attack Disruption* y *AIR* activos, Sentinel incorporado al portal Defender. | Cobertura de sensores > 95 %; cadencias diarias y semanales documentadas con evidencia; métricas p50/p90 medidas; cero backlog crítico sin dueño al cierre de guardia. |
| **Nivel 3 — Proactivo y Orientado a Exposición (CTEM + Detection-as-Code)** | Caza semanal por hipótesis en *Advanced Hunting*, detecciones gestionadas como código con *Alert tuning*, priorización continua de *Attack paths* / *Choke points* en *Exposure Management* y Purple Team periódico. | Conversión de hunts >= 20 %; FP por regla < 15 %; reducción sostenida de rutas de ataque híbridas hacia activos críticos; playbooks del SAF ensayados trimestralmente. |
| **Nivel 4 — Optimizado y Agéntico Supervisado (*AI-Augmented SOC*)** | Integración gobernada de *Security Copilot* y agentes especializados (*Security Alert Triage Agent*) con identidad, permisos mínimos y supervisión humana muestreada; optimización continua de *Sentinel data lake* y reportes ejecutivos de resultados de negocio. | MTTC en minutos ante ataques complejos; reversión probada en el 100 % de automatizaciones; evaluación anual independiente sobre NIST CSF 2.0 sin brechas materiales. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Principio rector de auditoría:** NIST CSF 2.0 audita **resultados (*outcomes*)** a nivel de Subcategoría; Microsoft Defender XDR aporta las capacidades técnicas (`[Verificado MS Learn]`) y los artefactos observables de cumplimiento. La correspondencia consolidada siguiente se sustenta en *Microsoft Cloud Security Benchmark (MCSB) v2* y el *NIST CSF 2.0 Core (CSWP 29)* `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría | Resultado Esperado (NIST CSF 2.0) | Capacidad Microsoft Defender XDR + MITRE ATT&CK | Evidencia Auditable en `security.microsoft.com` | Estado |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad están establecidos, comunicados y aplicados. | **Microsoft Defender Unified RBAC** (roles granulares por carga de trabajo y separación query/soft/hard actions) + activación JIT en Entra ID PIM. | Exportación de roles/asignaciones URBAC, bitácora de activaciones PIM y matriz RACI firmada. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.OV-01` | Los resultados de la estrategia de gestión de riesgos de ciberseguridad se revisan para informar y ajustar la dirección. | **Microsoft Secure Score**, **Exposure Management Initiatives** y *Monthly Security Summary* presentados al CISO/Directorio. | Histórico de 90 días de Secure Score e iniciativas, más actas del comité mensual. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-03` | Se mantienen representaciones de las comunicaciones de red autorizadas y los flujos de datos internos y externos. | Inventario multi-dominio de entidades en `AlertEvidence`, catálogo de apps SaaS/OAuth en MDCA y grafo `ExposureGraphNodes` / `ExposureGraphEdges`. | Exportación de consulta KQL sobre `ExposureGraphNodes` y catálogo de aplicaciones conectadas/descubiertas. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-05` | Las amenazas, vulnerabilidades, probabilidades e impactos se utilizan para comprender el riesgo e informar la priorización. | **Exposure Management Attack Paths & Choke Points**, **Critical Asset Management** y **Threat Analytics** contextualizado al inquilino. | Reporte de rutas de ataque híbridas priorizadas, lista de *Choke points* y tarjetas de mitigación de Threat Analytics. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen en políticas, se gestionan y revisan bajo mínimo privilegio y separación de funciones. | Control de permisos en **Unified RBAC** (incluyendo restricción de contenido de correo y `Advanced live response`) y políticas de sesión en MDCA. | Revisión mensual certificada de permisos URBAC y políticas de acceso/sesión activas. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.PS-01` | Se establecen y aplican prácticas de gestión de configuración de seguridad. | *Configuration Analyzer* (MDO), recomendaciones de *Secure Score*, gestión de políticas de seguridad de endpoint y *Predictive Shielding* (*GPO/Safeboot hardening* — T1562, T1484). | Reporte de *Configuration Analyzer*, estado de políticas efectivas y exenciones documentadas en Exposure Management. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-01` | Las redes y los servicios de red se monitorean para encontrar eventos potencialmente adversos. | Monitoreo continuo 24x7 y correlación nativa de señales de endpoint, identidad, correo y SaaS en la cola de incidentes XDR y workspace de Sentinel (TA0001–TA0011). | Exportación de cola de incidentes del período auditado y consulta diaria de integridad de telemetría. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender mejor las actividades asociadas. | Narrativa *Attack Story*, grafo de incidente, **Advanced Hunting (KQL)** y mapeo de técnicas MITRE ATT&CK en `AlertInfo` / `AlertEvidence`. | Muestra auditada de incidentes con grafo de ataque, técnicas ATT&CK identificadas y bitácora de cacerías (*Hunts*). | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-03` | La información se correlaciona a partir de múltiples fuentes. | Motor de fusión multi-dominio de Defender XDR + sincronización bidireccional con **Microsoft Sentinel** en el portal Defender. | Consulta KQL sobre `AlertInfo`/`AlertEvidence` demostrando incidentes con `array_length(Sources) > 1`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MA-01` | El plan de respuesta a incidentes se ejecuta en coordinación con terceros relevantes una vez declarado un incidente. | Gestión unificada de casos/incidentes, *Automation rules*, *Playbooks* SOAR y soporte de *Security Copilot* / *Defender Experts MDR*. | Exportación de incidentes Críticos/Altos cerrados con línea de tiempo completa y trazabilidad de aprobaciones. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos. | **Automatic Attack Disruption** (aislamiento de equipos, contención de usuario/IP, deshabilitación en AD/Entra, bloqueo OAuth — T1486, T1550) y remediaciones supervisadas en **Action Center**. | Exportación CSV de *Action Center > History* y registros en `DisruptionAndResponseEvents`. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-05` | Se verifica la integridad de los activos restaurados, se restauran los sistemas y se confirma el funcionamiento normal. | Flujo auditado de liberación controlada (**Release from containment** / **Undo** en *Action Center*) tras verificar erradicación; complementado con Azure Backup / M365 Backup para restauración de datos. | Registro de liberación en *Action Center* vinculado a validación forense previa al retorno a producción. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol (SecOps / Admin / GRC)

| Rol Objetivo | Ruta Oficial y Comunitaria Recomendada (Edición Noviembre 2026) | Certificación / Validación |
|---|---|---|
| **Analista SOC Tier 1 y Tier 2** | *Microsoft Defender XDR Ninja Training* (Fundamentals & Intermediate — actualizado oct 2026 por Heike Ritter), ruta oficial *SC-200: Mitigate threats using Microsoft Defender XDR* en Microsoft Learn y práctica en laboratorio con simulaciones de ataque. | **Microsoft Certified: Security Operations Analyst Associate (SC-200)** — temario actualizado en oct 2026 `[Verificado MS Learn]` |
| **Threat Hunter (L3) y Detection Engineer** | Nivel *Expert* del Defender XDR Ninja, *Microsoft Incident Response Ninja Hub* (Emily Liu, v21 oct 2026), repositorios comunitarios KQL de Bert-Jan Pals, Olaf Hartong (*FalconFriday*) y Matt Zorich, más consultas de grafo en *Exposure Management*. | **SC-200** + validación práctica de detección como código en *Sentinel Repositories* `[Verificado MS Learn]` / `[Decisión / Propuesta Editorial]` |
| **Ingeniero de Plataforma SecOps y Automatización** | Guías oficiales de transición de Sentinel al portal Defender, activación de *Microsoft Defender Unified RBAC*, configuración de *Automatic Attack Disruption* y gobierno de agentes de *Security Copilot*. | **SC-200** + **SC-300** (para integración IAM/PIM) `[Decisión / Propuesta Editorial]` |
| **SOC Manager, Security Architect y GRC / CISO** | Disciplina pública *Establish a security operations discipline* del **Microsoft Security Adoption Framework (SAF)** en Learn (2026), *MCRA* (junio 2026), *NIST CSF 2.0* y *11 Strategies of a World-Class Cybersecurity Operations Center* (MITRE). | **Microsoft Certified: Cybersecurity Architect Expert (SC-100)** `[Verificado MS Learn]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Resumen de Hallazgos y Correcciones Aplicadas contra Microsoft Learn MCP (`2026-11-11`)

1. **Convergencia obligatoria al portal Defender y nueva fecha de retiro de Sentinel en Azure Portal:** Se actualizó la arquitectura SIEM+XDR incorporando la disponibilidad general de Microsoft Sentinel en `security.microsoft.com` (con activación automática del conector Defender XDR) y la fecha vigente de fin de soporte de Sentinel en el portal de Azure el **31 de marzo de 2027** (corrigiendo referencias previas que citaban julio de 2026), además de documentar la vista previa de **ISOC** (septiembre 2026) para clientes E5/Defender Suite/E7 sin workspace activo de Sentinel `[Verificado MS Learn]`.
2. **Actualización integral de Licenciamiento 2025–2026:** Se incorporó el renombre oficial de *Microsoft 365 E5 Security* a **Microsoft Defender Suite**, la disponibilidad general de **Microsoft 365 E7** (mayo 2026), la inclusión de **Defender for Office 365 Plan 1** en Microsoft 365 E3 (julio 2026) y la dotación incluida de **Security Copilot en Microsoft 365 E5** (400 SCU/mes por cada 1.000 licencias pagas, hasta 10.000 SCU/mes) junto con el *Security Alert Triage Agent* `[Verificado MS Learn]`.
3. **Profundización técnica de Microsoft Defender Unified RBAC (URBAC):** Se añadieron las 4 categorías exactas de permisos (*Security operations*, *Security posture*, *Authorization and settings*, *Data operations [Preview]*), los nuevos niveles granulares de ejecución/aprobación (`Execute/Approve query, soft, hard actions`), la activación por workspace en Sentinel y la regla crítica según la cual *Global Administrator* no concede acceso automático a datos de workspaces de Sentinel `[Verificado MS Learn]`.
4. **Incorporación de Microsoft Security Exposure Management (MSEM) y su grafo KQL:** Se integró la operación continua de *Attack paths* híbridos (incluyendo análisis DACL y *Choke points*), *Critical asset management*, *Security initiatives* y las tablas `ExposureGraphNodes` y `ExposureGraphEdges` con operadores `make-graph` y `graph-match` `[Verificado MS Learn]`.
5. **Actualización de Automatic Attack Disruption, Predictive Shielding y Esquema Advanced Hunting:** Se verificó el umbral de confianza >= 99 %, el catálogo completo de acciones automáticas (incluyendo *Predictive shielding*: `Safeboot hardening`, `GPO hardening`, `Proactive user containment`, e integraciones en Preview con Okta y AWS IAM), la tabla `DisruptionAndResponseEvents`, el reemplazo de `AADSignInEventsBeta` por `EntraIdSignInEvents` (octubre 2026), la nueva tabla `AgentsInfo`, la migración de *Alert suppression* a **Alert tuning** y el retiro de APIs heredadas (`/security/alerts`) `[Verificado MS Learn]`.
6. **Depuración de términos no oficiales:** Se eliminó como capacidad nativa el término *"Defender Boxed"* presente en borradores previos de `MSEOP-MD` (al tratarse de un empaquetado consultivo de partners inexistente en Microsoft Learn), reemplazándolo por artefactos nativos verificados (*Monthly Security Summary*, *Security operations efficiency workbook* e *Initiatives* de Exposure Management) `[Verificado MS Learn]`.

### 14.2 Declaración Explícita de Decisiones y Propuestas Editoriales

| Elemento en la Guía | Clasificación | Justificación Técnica y de Gobierno |
|---|---|---|
| **Metas numéricas de SLA y KPIs** (ej. MTTA p50 < 15 min, MTTR Alto p90 < 24 h, FP < 15 %) | `[Decisión / Propuesta Editorial]` | Microsoft Learn provee el esquema `SecurityIncident` y el workbook de métricas, pero establece que los umbrales dependen del apetito de riesgo, dotación 24x7 y criticidad de activos de cada organización. |
| **Perfiles de roles personalizados URBAC por Tier (L1/L2/L3/GRC) y Matriz RACI** | `[Decisión / Propuesta Editorial]` | Microsoft publica los permisos atómicos en Unified RBAC y roles funcionales en el SAF; la combinación específica de permisos y ventanas PIM (4 h / 8 h) es diseño consultivo de mínimo privilegio. |
| **Periodicidad exacta de tareas tácticas y estratégicas** (ej. al menos 2 hipótesis de caza/semana, tabletop trimestral) | `[Decisión / Propuesta Editorial]` | La guía oficial *SecOps Tasks* define cadencias base (diaria/semanal/mensual/según necesidad); la estructuración codificada (`D-01`..`A-01`) estandariza la auditabilidad operativa. |
| **Modelo de Madurez Operacional de 4 niveles (L1 a L4)** | `[Decisión / Propuesta Editorial]` | Microsoft no publica un modelo normativo único de madurez SOC; se sintetiza a partir de prácticas públicas del SAF, SOC-CMM y NIST CSF 2.0. |
| **Mapeo detallado a subcategorías NIST CSF 2.0 (incluyendo `GOVERN`)** | `[Decisión / Propuesta Editorial]` | Construido combinando mapeos públicos de *MCSB v2* con el texto oficial del *NIST CSF 2.0 Core (CSWP 29)*; NIST audita resultados (*outcomes*), mientras Defender XDR provee evidencias técnicas. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Corporation — *What is Microsoft Defender XDR?* — `https://learn.microsoft.com/en-us/defender-xdr/microsoft-365-defender` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-02:** Microsoft Corporation — *Integrating Microsoft Defender XDR into your security operations (SecOps tasks)* — `https://learn.microsoft.com/en-us/defender-xdr/integrate-microsoft-365-defender-secops-tasks` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-03:** Microsoft Corporation — *Microsoft Defender unified role-based access control (RBAC) & Permissions reference* — `https://learn.microsoft.com/en-us/defender-xdr/custom-permissions-details` y `https://learn.microsoft.com/en-us/defender-xdr/manage-rbac` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-04:** Microsoft Corporation — *Automatic attack disruption in Microsoft Defender* — `https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-05:** Microsoft Corporation — *What is Microsoft Security Exposure Management? & Enterprise exposure graph schemas* — `https://learn.microsoft.com/en-us/security-exposure-management/microsoft-security-exposure-management` y `https://learn.microsoft.com/en-us/security-exposure-management/schemas-operators` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-06:** Microsoft Corporation — *Understand the advanced hunting schema in Microsoft Defender XDR* — `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-schema-tables` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-07:** Microsoft Corporation — *Microsoft Sentinel in the Microsoft Defender portal & Transition guide* — `https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal` y `https://learn.microsoft.com/en-us/azure/sentinel/move-to-defender` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-08:** Microsoft Corporation — *ISOC in Microsoft Defender (preview)* — `https://learn.microsoft.com/en-us/defender-xdr/isoc-overview` (Verificado vía MCP Microsoft Learn, Nov 2026).
- **REF-09:** Microsoft Corporation — *Establish a security operations discipline (Microsoft Security Adoption Framework - SAF)* — `https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-security-operations` (Verificado en corpus curado / Learn, Nov 2026).
- **REF-10:** Microsoft Corporation — *Manage your SOC better with incident metrics in Microsoft Sentinel* — `https://learn.microsoft.com/en-us/azure/sentinel/manage-soc-with-incident-metrics` (Verificado en corpus curado / Learn, Nov 2026).

### 15.2 Publicaciones Oficiales y Empleados de Microsoft
- **REF-11:** Heike Ritter (Empleado de Microsoft) — *Become a Microsoft Defender XDR Ninja* (Microsoft Tech Community, actualizado oct 2026) — `https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/become-a-microsoft-defender-ninja/1789376`
- **REF-12:** Rob Lefferts (CVP, Microsoft Threat Protection) — *Reimagining the SOC for the agentic era in Microsoft Defender* (Microsoft Security Blog, sep 2026) — `https://www.microsoft.com/en-us/security/blog/2026/09/23/reimagining-the-soc-for-the-agentic-era-in-microsoft-defender/`
- **REF-13:** Microsoft Sentinel Product Team — *Update: New timeline for transitioning Sentinel experience to Defender portal (March 31, 2027)* (Microsoft Tech Community) — `https://techcommunity.microsoft.com/blog/microsoftsentinelblog/update-new-timeline-for-transitioning-sentinel-experience-to-defender-portal/4490464`
- **REF-14:** Microsoft Security Blog — *Microsoft Defender delivered 242% return on investment over three years (Forrester TEI)* — `https://www.microsoft.com/en-us/security/blog/2025/09/18/microsoft-defender-delivered-242-return-on-investment-over-three-years/`
- **REF-15:** Emily Liu (Empleado de Microsoft) — *Welcome to the Microsoft Incident Response Ninja Hub* (Microsoft Tech Community, v21 oct 2026) — `https://techcommunity.microsoft.com/blog/microsoft-defender-experts/welcome-to-the-microsoft-incident-response-ninja-hub/4243594/replies/4245146`

### 15.3 Comunidad y MVPs de Seguridad de Microsoft
- **REF-16:** Bert-Jan Pals (Microsoft Security MVP) — *KQL Query Blog & Hunting-Queries-Detection-Rules Repository* — `https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules` y `https://kqlquery.com`
- **REF-17:** Jeffrey Appel (Microsoft Security MVP) — *Microsoft Defender XDR, MDE & Sentinel Data Lake Technical Blog* — `https://jeffreyappel.nl/`
- **REF-18:** Jorge Castañeda (Microsoft Security MVP, Perú) — *Blog d3fend.me: Laboratorios reproducibles Defender XDR + Sentinel y priorización de exposición en español* — `https://blog.d3fend.me/`

### 15.4 Marcos Normativos y Estándares Abiertos
- **REF-19:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)* — `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`
- **REF-20:** National Institute of Standards and Technology (NIST) — *NIST SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile* — `https://csrc.nist.gov/pubs/sp/800/61/r3/final`
- **REF-21:** MITRE Corporation (Carson Zimmerman et al.) — *11 Strategies of a World-Class Cybersecurity Operations Center* y *MITRE ATT&CK Enterprise Matrix* — `https://www.mitre.org/sites/default/files/2022-04/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf` y `https://attack.mitre.org/`

# Guía Maestra de Excelencia Operacional: Microsoft Purview Data Loss Prevention (Cloud, Teams, Endpoint DLP, Adaptive Protection y DLP para IA)

## 1. Portada y Ficha de Control Documental

| Campo | Valor |
|---|---|
| **Identificador del Módulo** | `15_Purview_Data_Loss_Prevention` |
| **Slug Canónico** | `Purview_Data_Loss_Prevention` |
| **Nombre Completo** | Microsoft Purview Data Loss Prevention (Cloud, Teams, Endpoint DLP, Adaptive Protection y DLP para IA) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado limpio desde subcarpetas válidas de `MSEOP-MD\Purview DLP` (`0427 Purview DLP Bloques SecOps\Claude - Compilado final (Limpio)`, `Actúa como Principal Cloud Security Architect v6`, `DLP NIST VC`, `Purview DLP - VC LIC`; descartando explícitamente la carpeta obsoleta `NO`) + Cruce `Ninja Training 2026 (06_Purview_DLP)` + Revalidado contra Microsoft Learn MCP |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (Teams DLP, Endpoint DLP, Adaptive Protection, DLP para Microsoft 365 Copilot/GenAI, Fabric/Power BI y triaje unificado en Defender XDR; DLP básico para Exchange, SharePoint y OneDrive en M365 E3) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com`, `https://security.microsoft.com`, `https://intune.microsoft.com`, `https://portal.azure.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Data Security Architect, DLP Engineer / Admin, SOC Manager, SOC L1, SOC L2, SOC L3 / Detection Engineer, Endpoint Engineer (MDE/Intune), Insider Risk Analyst, GRC / Legal & Privacy |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Arquitectura Zero Trust de Microsoft (Pilar Data), MITRE ATT&CK Enterprise, Microsoft Cloud Security Benchmark (MCSB v2) |

> **Nota de Consolidación Limpia y Trazabilidad (Noviembre 2026):** Esta guía consolida de forma limpia y depurada los artefactos vigentes de `MSEOP-MD\Purview DLP` ubicados en `0427 Purview DLP Bloques SecOps` (`Claude - Compilado final (Limpio)` y `Principal Cloud Security Architect v6`), `DLP NIST VC` y `Purview DLP - VC LIC`, **excluyendo deliberadamente la carpeta `NO`** (`0420 Purview DLP` y borradores descartados previos) para evitar arrastrar rutas o métricas obsoletas `[Decisión / Propuesta Editorial]`. Todo el contenido técnico ha sido contrastado con `Ninja_Training_Seguridad_Microsoft_2026\06_Purview_DLP` y revalidado contra Microsoft Learn al `2026-11-11`, etiquetando rigurosamente los hechos verificables del producto con `[Verificado MS Learn]` y los criterios consultivos, SLAs, metas de KPIs y mapeos de auditoría con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026

Microsoft Purview Data Loss Prevention (DLP) es el plano de aplicación en tiempo real (*enforcement plane*) de la estrategia de seguridad de datos de Microsoft `[Verificado MS Learn]`. Mientras que **Purview Information Protection (Módulo 14)** establece la clasificación y el cifrado persistente mediante etiquetas, Purview DLP inspecciona profundamente el contenido y el contexto de cada transacción para prevenir la compartición accidental o exfiltración maliciosa a través de aplicaciones empresariales, correo, mensajería colaborativa, endpoints Windows/macOS, navegadores corporativos, espacios analíticos y asistentes de IA generativa `[Verificado MS Learn]`.

A noviembre de 2026, seis capacidades revalidadas definen el estándar de excelencia operacional en Purview DLP:

1. **Arquitectura unificada sin agentes adicionales en Endpoint DLP:** Endpoint DLP opera de manera nativa (*built-in*) en **Windows 10, Windows 11**, versiones soportadas de Windows Server y **macOS (las tres versiones mayores más recientes)** aprovechando el onboarding unificado con Microsoft Defender for Endpoint / Microsoft Intune, incorporando **Just-in-Time (JIT) protection** para bloquear egresos mientras concluye la evaluación de clasificación y **Evidence Collection** hacia Azure Blob Storage gestionado por el cliente o almacenamiento administrado por Microsoft `[Verificado MS Learn]`.
2. **Protección nativa de interacciones con Microsoft 365 Copilot, Copilot Chat y Cowork:** La ubicación **Microsoft 365 Copilot and Copilot Chat** permite bloquear prompts que contengan *Sensitive Information Types (SITs)*, impedir que Copilot procese archivos o correos con determinadas **Sensitivity Labels** como fuente de *grounding* y bloquear búsquedas web externas (`Performing Web Searches`) cuando el prompt incluye datos confidenciales `[Verificado MS Learn]`.
3. **Bloqueo inline contra Shadow AI en Microsoft Edge for Business:** Las políticas DLP para aplicaciones cloud no administradas e *Inline web traffic* aplican control nativo en **Microsoft Edge for Business** sobre Windows 10/11 gestionados por Intune para impedir pegado, escritura o carga de datos corporativos hacia sitios GenAI públicos (**OpenAI ChatGPT, Google Gemini, DeepSeek, Microsoft Copilot público**), bloqueando la apertura de navegadores no protegidos (como Firefox o Chrome sin la extensión de Purview) `[Verificado MS Learn]`.
4. **Defensa dinámica centrada en el comportamiento con Adaptive Protection:** La integración nativa con **Microsoft Purview Insider Risk Management** ajusta automáticamente el rigor de las reglas DLP en **Exchange Online, Microsoft Teams y Devices** según el nivel de riesgo dinámico del usuario (`Elevated`, `Moderate`, `Minor`), aplicando bloqueo estricto solo a usuarios riesgosos sin frenar la productividad del resto de la organización `[Verificado MS Learn]`.
5. **Consolidación obligatoria de File Policies de Defender for Cloud Apps (`2027-01-06`):** Con el retiro definitivo de las *File Policies* de Microsoft Defender for Cloud Apps el **6 de enero de 2027**, toda protección basada en archivos sobre SharePoint, OneDrive y nubes conectadas (Google Workspace, Box, Dropbox, Salesforce) se consolida en Purview DLP mediante el asistente **DLP to Purview migration tool** `[Verificado MS Learn]`.
6. **Operación unificada en Microsoft Defender XDR y cambio crítico de Alert Tuning (Octubre 2026):** Desde principios de octubre de 2026, una regla integrada de *Alert tuning* en `security.microsoft.com` convierte por defecto las señales DLP en *behaviors* (`BehaviorInfo` / `BehaviorEntities`) en lugar de alertas en la cola de incidentes; los SOC que centralizan el triaje DLP en la cola unificada de incidentes de Defender XDR deben deshabilitar explícitamente dicha regla en `Settings > Microsoft Defender XDR > Alert tuning` `[Verificado MS Learn]`.

### 2.2 Matriz Exacta de Licenciamiento E3 vs. E5 / Microsoft Purview Suite

| Ubicación / Capacidad de Purview DLP | Microsoft 365 E3 / Office 365 E3 | Office 365 E5 | Microsoft 365 E5 / Microsoft Purview Suite (ex E5 Compliance) | M365 E5 Info Protection & Governance | Observaciones Técnicas y Operativas |
|---|---|---|---|---|---|
| **DLP para Exchange Online, SharePoint Online y OneDrive** (incluye archivos en Teams alojados en SPO/OD) | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Incluye *Single-event alerts* y *Policy Tips* en Outlook/Web/Office `[Verificado MS Learn]`. |
| **Teams DLP (Mensajes de chat 1:1, grupales y canales estándar, privados y compartidos)** | No `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | En canales requiere ámbito de grupos M365 o grupos de seguridad (no cuentas individuales) `[Verificado MS Learn]`. |
| **Endpoint DLP** (Windows 10/11, Windows Server y macOS; JIT, USB, Impresión, Portapapeles, Red, RDP, Edge, Evidence Collection) | No `[Verificado MS Learn]` | No (requiere SKU M365 / Purview Suite) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sin agente adicional; el almacenamiento de evidencias en Azure Storage del cliente genera consumo Azure Blob `[Verificado MS Learn]`. |
| **Adaptive Protection** (Integración dinámica con niveles de riesgo de Insider Risk Management) | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Requiere licencia Insider Risk Management (M365 E5 / Purview Suite / IRM) `[Verificado MS Learn]` | Aplica condición `Insider risk level for Adaptive Protection is` en Exchange, Teams y Devices `[Verificado MS Learn]`. |
| **DLP para Microsoft 365 Copilot, Copilot Chat y Cowork** (SITs en prompts, bloqueo por etiquetas y búsqueda web) | No `[Verificado MS Learn]` | Parcial (requiere E5/Purview Suite + licencia M365 Copilot donde aplique) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Incluye política predeterminada en simulación *Protect sensitive M365 Copilot interactions* `[Verificado MS Learn]`. |
| **DLP Inline en Microsoft Edge for Business hacia apps IA no gestionadas** | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí (requiere dispositivos Windows 10/11 en Intune; red vía PAYG/SASE según alcance) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | No soporta tenants con *Multi-admin approval* habilitado en Microsoft Intune `[Verificado MS Learn]`. |
| **DLP para Microsoft Fabric y Power BI workspaces** | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí (sobre capacidades Fabric F2+/P1+) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Evalúa modelos semánticos y artefactos soportados; diferencia `Member` vs. `Guest` `[Verificado MS Learn]`. |
| **Alertas agregadas por volumen/umbral e investigación de incidentes DLP en Defender XDR** | No (solo evento único en Purview) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Revisar estado de la regla *Alert tuning* introducida en octubre de 2026 en Defender XDR `[Verificado MS Learn]`. |

### 2.3 Principios Rectores y Alineación Zero Trust

1. **Defensa multicapa en el punto exacto de trabajo (`Layered Data Protection`):** Combinar políticas cloud (Exchange, SharePoint, OneDrive, Teams, Fabric), controles nativos en el sistema operativo (**Endpoint DLP**) e inspección inline en el navegador (**Edge for Business**) para eliminar puntos ciegos cuando el archivo cruza el límite de descarga `[Verificado MS Learn]`.
2. **Clasificación como señal y DLP como ejecutor (`Label + SIT Enforcement`):** Consumir directamente las **Sensitivity Labels**, SITs, **EDM (100M filas)** y clasificadores entrenables de Purview Information Protection para evitar duplicar reglas de detección `[Verificado MS Learn]`.
3. **Fricción proporcional al riesgo del usuario (`Adaptive Protection`):** Sustituir bloqueos estáticos indiscriminados por respuestas graduadas (`Block`, `Block with override` con justificación auditable, `Audit + Policy Tip`) gobernadas dinámicamente por el nivel de riesgo de Insider Risk Management `[Verificado MS Learn]`.
4. **Despliegue seguro mediante simulación y telemetría previa (`Simulation-First Rollout`):** Ejecutar toda nueva regla DLP en `Run the policy in simulation mode` (activando *Policy Tips* progresivamente) antes de habilitar bloqueo duro en producción `[Verificado MS Learn]`.
5. **Protección en tiempo de evaluación (`Zero-Gap con Just-in-Time Protection`):** Activar **Endpoint DLP JIT protection** para impedir que archivos recién creados o pendientes de reclasificación sean exfiltrados por USB, red, impresión o navegador durante los segundos de evaluación `[Verificado MS Learn]`.
6. **Convergencia SecOps y cadena de custodia forense (`Unified XDR Triage & Evidence`):** Correlacionar alertas y comportamientos DLP con telemetría de endpoint, identidad e IA en `security.microsoft.com`, respaldados por captura íntegra del archivo coincidente (*Evidence Collection*) para investigación legal `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Anatomía Funcional de Evaluación y Aplicación

Purview DLP divide su cobertura arquitectónica en dos grandes dominios definidos en Microsoft Learn: **(1) Enterprise applications & devices** (Exchange Online, SharePoint Online, OneDrive, Microsoft Teams chat & channels, Devices Windows/macOS, On-premises repositories, Microsoft Fabric & Power BI workspaces, Microsoft 365 Copilot & Copilot Chat y Managed cloud apps) e **(2) Inline web traffic** (protección en **Microsoft Edge for Business** y capa de red para aplicaciones cloud no administradas como ChatGPT, Google Gemini, DeepSeek y más de 35.000 apps del catálogo) `[Verificado MS Learn]`. Toda coincidencia genera telemetría primero en el **Microsoft 365 Unified Audit Log**, alimentando en paralelo **Activity Explorer**, la consola de **Alerts** de Purview y el motor de incidentes/caza avanzada de **Microsoft Defender XDR** `[Verificado MS Learn]`.

El flujo interno de evaluación sigue cinco etapas deterministas que el equipo de ingeniería DLP y el SOC deben comprender para diagnosticar latencias o falsos negativos `[Verificado MS Learn]`:

1. **Extracción profunda de texto y metadatos:** El motor DLP no ejecuta un escaneo superficial de cadenas; extrae flujo textual, propiedades documentales, cabeceras de correo, metadatos de etiquetas de sensibilidad (GUID inmutable), tipos MIME reales y contexto de compartición (`Internal` vs. `External / Guest`) `[Verificado MS Learn]`.
2. **Evaluación contra clasificadores primarios y evidencia corroborativa:** Compara el contenido extraído contra expresiones regulares, diccionarios, funciones de validación (ej. algoritmo Luhn), proximidad de caracteres (por defecto 300 caracteres), tablas hasheadas **Exact Data Match (EDM)**, **Named Entities** y **Trainable Classifiers** `[Verificado MS Learn]`.
3. **Evaluación contextual y conductual:** Incorpora condiciones ambientales como el destino de egreso en el dispositivo (USB, impresora, recurso SMB, sesión RDP, dominio web en Edge), el alcance del contenedor en SharePoint/Teams o el nivel dinámico `Elevated / Moderate / Minor` proveniente de **Adaptive Protection** `[Verificado MS Learn]`.
4. **Resolución de precedencia y aplicación de la acción más restrictiva:** Las políticas y reglas se evalúan según su orden explícito de prioridad (`Priority 0, 1, ...`); cuando múltiples políticas independientes (por ejemplo, una política base de Endpoint DLP y la política predeterminada de Adaptive Protection) alcanzan al mismo usuario y actividad, prevalece la acción más restrictiva (`Block` sobre `Block with override`, y esta sobre `Audit`) `[Verificado MS Learn]`.
5. **Emisión de telemetría, Policy Tip y recolección de evidencia:** De forma síncrona o cuasi-real se muestra la notificación educativa (*Policy Tip* o *toast* nativo en Windows/macOS), se almacena copia íntegra del archivo coincidente en **Evidence Collection** (si la regla lo exige) y se registra el evento en el **Unified Audit Log**, propagándose a `Activity Explorer`, `Alerts` y `security.microsoft.com` `[Verificado MS Learn]`.

### 3.2 Tabla de Componentes Operativos y Rutas Vigentes

| Componente / Motor | Función Operativa Principal | Consola y Ruta Oficial (Nov 2026) | Integraciones Clave | Estado |
|---|---|---|---|---|
| **Motor de Políticas Cloud M365 (EXO, SPO, OD, Teams)** | Inspecciona correo en tránsito, documentos compartidos externamente y mensajes de Teams (1:1, grupales y canales estándar, privados y compartidos) bloqueando en segundos y mostrando *Policy Tips*. | `purview.microsoft.com > Solutions > Data Loss Prevention > Policies` | Exchange Online, SharePoint Online, OneDrive, Microsoft Teams | `[Verificado MS Learn]` |
| **Endpoint DLP Nativo (Windows 10/11, Server & macOS)** | Monitorea y restringe sin agente adicional copia a USB, impresión, portapapeles, recursos SMB, RDP, Bluetooth, apps restringidas y navegadores no permitidos. | `purview.microsoft.com > Settings > Data Loss Prevention > Endpoint settings` | Microsoft Defender for Endpoint, Microsoft Intune, Windows / macOS | `[Verificado MS Learn]` |
| **Endpoint DLP Just-in-Time (JIT) Protection** | Audita o bloquea actividades de egreso sobre *JIT candidate files* (no evaluados o con *stale classification*) mientras termina la clasificación, aplicando acción *fallback* configurable. | `purview.microsoft.com > Settings > Data Loss Prevention > Endpoint settings > Just-in-time protection` | Endpoint DLP (Windows 10/11 y macOS) | `[Verificado MS Learn]` |
| **Evidence Collection (Matched Items Storage)** | Guarda copia completa del archivo coincidente en dispositivos Windows (GA) y macOS (Preview) hacia Azure Storage del cliente o almacenamiento administrado por Microsoft. | `purview.microsoft.com > Settings > Data Loss Prevention > Endpoint settings > Setup evidence collection` | Azure Blob Storage, Activity Explorer, Purview Data Security Investigations | `[Verificado MS Learn]` |
| **DLP para Microsoft 365 Copilot, Copilot Chat y Cowork** | Bloquea prompts con SITs, excluye archivos/correos con etiquetas sensibles del *grounding* y desactiva búsquedas web externas cuando el prompt contiene datos confidenciales. | `purview.microsoft.com > Solutions > Data Loss Prevention > Policies` (ubicación *Microsoft 365 Copilot and Copilot Chat*) | Microsoft 365 Copilot, Copilot Chat, Cowork, Sensitivity Labels | `[Verificado MS Learn]` |
| **Browser DLP en Microsoft Edge for Business (Shadow AI)** | Bloquea inline escritura, pegado o subida de datos sensibles hacia sitios GenAI no administrados (ChatGPT, Gemini, DeepSeek) e impide ejecutar navegadores desprotegidos. | `purview.microsoft.com > Solutions > Data Loss Prevention` + `DSPM for AI` | Microsoft Edge for Business, Microsoft Intune, Extensión Purview para Chrome | `[Verificado MS Learn]` |
| **Adaptive Protection Engine** | Consume en tiempo real los niveles de riesgo `Elevated`, `Moderate` y `Minor` de Insider Risk Management como condición dinámica en reglas de Exchange, Teams y Devices. | `purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection` | Microsoft Purview Insider Risk Management | `[Verificado MS Learn]` |
| **DLP para Microsoft Fabric, Power BI y Nubes Conectadas** | Detecta datos sensibles en espacios de trabajo Fabric/Power BI y reemplaza las File Policies de Defender for Cloud Apps (retiro `2027-01-06`) en nubes SaaS. | `purview.microsoft.com > Solutions > Data Loss Prevention > Policies` y asistente *DLP to Purview migration* | Microsoft Fabric / OneLake, Google Workspace, Box, Dropbox, Salesforce | `[Verificado MS Learn]` |
| **Cola Unificada de Incidentes y Hunting en Defender XDR** | Correlaciona alertas/comportamientos DLP con XDR/SIEM, ejecuta acciones de remediación in-situ, resúmenes con Security Copilot y caza en `CloudAppEvents`, `DeviceEvents`, `DataSecurityEvents` y `BehaviorInfo`. | `security.microsoft.com > Incidents & alerts > Incidents` y `Settings > Microsoft Defender XDR > Alert tuning` | Microsoft Defender XDR, Microsoft Sentinel, Security Copilot | `[Verificado MS Learn]` |

### 3.3 Consideraciones Arquitectónicas Críticas (Revalidación Noviembre 2026)

- **Regla integrada de Alert Tuning en Defender XDR (Octubre 2026):** Microsoft activó a inicios de octubre de 2026 una regla integrada que reclasifica señales DLP como *behaviors* (visibles en `BehaviorInfo` y `BehaviorEntities`) sin crear alertas en la cola de incidentes de Defender XDR. Si el modelo operativo del SOC exige triaje directo de alertas DLP en `security.microsoft.com > Incidents`, es obligatorio desactivar dicha regla en `Settings > Microsoft Defender XDR > Alert tuning` `[Verificado MS Learn]`.
- **Alcance multi-tenant en Teams DLP:** En **Shared Channels** (basados en Entra B2B Direct Connect), los mensajes de cada participante se evalúan contra las políticas DLP de su propio *home tenant*. En cambio, en chats externos (*external access*), la evaluación depende de que el tenant propio haya sido el iniciador (*hosting tenant*) del hilo `[Verificado MS Learn]`. Además, para proteger mensajes en canales de Teams, la política debe dirigirse a grupos M365 o grupos de seguridad, nunca solo a cuentas individuales `[Verificado MS Learn]`.
- **Precedencia Endpoint DLP vs. Edge Inline DLP y limitación Intune:** Cuando coinciden usuario, contexto y acción en un dispositivo Windows 10/11, la política de **Endpoint DLP** tiene precedencia sobre la política inline de **Edge for Business**. Asimismo, la protección inline de apps no gestionadas en Edge crea políticas automáticas en Intune y no es compatible con tenants que tengan activado *Multi-admin approval* en Intune `[Verificado MS Learn]`.

### 3.4 Matriz Técnica de Controles de Egreso en Endpoint DLP y Navegadores

| Canal de Egreso Local / Web | Plataforma Soportada | Modos de Acción Disponibles | Comportamiento con Just-in-Time (JIT) Protection | Requisito Operativo Clave |
|---|---|---|---|---|
| **Medios USB extraíbles** (`Copy to removable USB device`) | Windows 10/11 y macOS `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Bloquea copia mientras concluye evaluación de clasificación `[Verificado MS Learn]`. | Definir grupos de dispositivos USB corporativos autorizados por `VID/PID` o número de serie `[Verificado MS Learn]`. |
| **Impresión local, red o PDF virtual** (`Print`) | Windows 10/11 y macOS `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Retiene/bloquea impresión hasta obtener veredicto de política `[Verificado MS Learn]`. | Configurar grupos de impresoras corporativas de confianza vs. impresoras domésticas o virtuales `[Verificado MS Learn]`. |
| **Portapapeles** (`Copy to clipboard`) | Windows 10/11 y macOS `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | `JIT Audit` por defecto para evitar fricción al copiar/pegar en edición `[Verificado MS Learn]`. | Complementar con bloqueo de pegado (*Block paste*) en Edge for Business hacia dominios IA no gestionados `[Verificado MS Learn]`. |
| **Recursos compartidos de red SMB** (`Copy to network share`) | Windows 10/11 y macOS `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Bloquea transferencia a rutas UNC no excluidas durante evaluación JIT `[Verificado MS Learn]`. | Mantener lista blanca explícita de servidores SMB corporativos gobernados `[Verificado MS Learn]`. |
| **Escritorio Remoto y Bluetooth** (`RDP` / `Bluetooth app`) | Windows 10/11 `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Cubierto nativamente por bloqueo de egreso JIT `[Verificado MS Learn]`. | Impedir redirección de unidades/portapapeles hacia sesiones RDP no administradas `[Decisión / Propuesta Editorial]`. |
| **Aplicaciones restringidas** (`Access by unallowed apps`) | Windows 10/11 y macOS `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Impide lectura del archivo sensible por ejecutables en lista restringida `[Verificado MS Learn]`. | Incluir clientes personales de sincronización cloud, mensajería no corporativa y herramientas CLI de subida `[Decisión / Propuesta Editorial]`. |
| **Dominios cloud / GenAI y navegadores no permitidos** | Edge for Business (nativo) y Chrome (con extensión Purview) `[Verificado MS Learn]` | `Audit`, `Block with override`, `Block` | Bloquea subida a dominios restringidos durante evaluación JIT `[Verificado MS Learn]`. | En modo `Block`, Windows impide abrir Firefox u otros navegadores sin extensión actualizada `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

La administración y operación de Purview DLP debe segregarse estrictamente en `purview.microsoft.com > Settings > Roles and scopes > Role groups` y `security.microsoft.com` (Unified RBAC), respetando **Administrative Units** (cuyo alcance fluye automáticamente hacia las alertas DLP en el portal de Microsoft Defender) `[Verificado MS Learn]`.

| Rol / Role Group Oficial | Plano RBAC | Permisos Clave | Estrategia PIM / JIT Recomendada | Responsabilidad Operativa y Segregación de Funciones | Estado |
|---|---|---|---|---|---|
| **DLP Compliance Management** | Purview Portal | Crea, edita, simula y activa políticas DLP, configura *Endpoint DLP settings*, *JIT protection*, grupos de impresoras/USB y gestiona alertas DLP (acceso *DLP only* en Defender). | **Eligible (JIT máx. 4 h)** con MFA phishing-resistant y ticket de cambio aprobado `[Decisión / Propuesta Editorial]`. | Ingeniería y tuning de políticas DLP; segregado de la descarga de evidencias confidenciales `[Verificado MS Learn]`. |
| **View-Only DLP Compliance Management** | Purview Portal / Defender | Visualiza políticas DLP, reglas, reportes y alertas DLP (incluyendo vista *DLP only* en Defender XDR e inspección de Adaptive Protection) sin permiso de modificación. | Asignación activa acotada o **Eligible (JIT 8 h)** para SOC L1, GRC y Auditoría `[Decisión / Propuesta Editorial]`. | Monitoreo continuo, auditoría de configuración y verificación independiente `[Verificado MS Learn]`. |
| **Information Protection Analyst / Investigator** | Purview Portal / Defender | Triaje, cambio de estado e investigación de alertas DLP en Purview y Defender XDR sin alterar políticas globales. | **Eligible (JIT 8 h por turno SOC)** con MFA resistente a phishing `[Decisión / Propuesta Editorial]`. | Operación diaria de triaje L1/L2, análisis de justificaciones de *override* y escalamiento `[Verificado MS Learn]`. |
| **Security Operator / Manage Alerts (Defender Unified RBAC)** | Microsoft Defender XDR | Gestiona incidentes multi-dominio (DLP + Endpoint + Identity + Office 365), ejecuta acciones de remediación sobre archivos/dispositivos y caza en `CloudAppEvents` / `DeviceEvents`. | **Eligible (JIT 8 h por turno)** en `security.microsoft.com` `[Decisión / Propuesta Editorial]`. | Correlación cruzada XDR y contención integral cuando una alerta DLP coincide con compromiso o exfiltración activa `[Verificado MS Learn]`. |
| **Data Classification Content Viewer** | Purview Portal (Rol sensible) | Permite previsualizar el texto coincidente en la pestaña *Sensitive info types / Source* y previsualizar archivos capturados por *Endpoint DLP Evidence Collection*. | **Eligible estricto (JIT máx. 2 h)** con aprobación dual (Legal/Privacidad + SOC Lead) `[Decisión / Propuesta Editorial]`. | Confirmación puntual de verdaderos positivos sin necesidad de descargar el archivo completo al equipo del analista `[Verificado MS Learn]`. |
| **Data Classification Content Download** | Purview Portal (Rol crítico) | Autoriza descargar una copia íntegra de los archivos originales capturados como evidencia desde dispositivos Windows/macOS (*Evidence Collection*). | **Eligible excepcional (JIT máx. 1 h)** con aprobación dual obligatoria y número de caso forense/legal `[Decisión / Propuesta Editorial]`. | Extracción forense estrictamente controlada hacia custodia legal; auditado semanalmente `[Verificado MS Learn]`. |
| **Insider Risk Management Admin** | Purview Portal | Configura indicadores de riesgo, umbrales de niveles `Elevated / Moderate / Minor` y vinculación de **Adaptive Protection** con DLP. | **Eligible (JIT máx. 4 h)** segregado del equipo de TI general por controles de seudonimización `[Decisión / Propuesta Editorial]`. | Gobernanza conjunta con RR. HH. y Legal de los perfiles de riesgo que alimentan reglas adaptativas DLP `[Verificado MS Learn]`. |
| **Intune / Endpoint Security Administrator** | Microsoft Intune / Defender | Ejecuta onboarding de dispositivos Windows/macOS, despliega políticas sincronizadas de Microsoft Edge for Business y mantiene versiones antimalware requeridas por JIT. | **Eligible (JIT máx. 4 h)** `[Decisión / Propuesta Editorial]`. | Garantizar cobertura de onboarding, exclusiones aprobadas y cumplimiento del navegador corporativo `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

### D-01: Verificación diaria de onboarding de endpoints, salud de telemetría y regla Alert Tuning en Defender XDR
- **Objetivo:** Confirmar que los endpoints Windows 10/11 y macOS reportan telemetría DLP activa, que el almacenamiento de *Evidence Collection* responde sin cuota agotada y que la configuración de *Alert tuning* en Defender XDR no oculte involuntariamente alertas críticas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Device onboarding`, `Settings > Data Loss Prevention > Endpoint settings` y `https://security.microsoft.com > Settings > Microsoft Defender XDR > Alert tuning` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Endpoint Security Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar en `Device onboarding` y `DeviceHealthStatus` que no existan caídas abruptas en el número de dispositivos Windows/macOS reportando políticas Endpoint DLP sincronizadas `[Verificado MS Learn]`.
  2. Comprobar que el estado de la regla integrada de *Alert tuning* para señales DLP en Defender XDR (vigente desde octubre de 2026) coincida con el diseño aprobado del SOC (deshabilitada si se triaja por incidentes/alertas, o monitoreada vía `BehaviorInfo` si se mantiene activa) `[Verificado MS Learn]`.
  3. Validar conectividad y uso diario del contenedor de **Evidence Collection** (Azure Storage propio o administrado por Microsoft) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Check diario de cobertura de dispositivos, estado de *Alert tuning* y salud del repositorio de evidencias (NIST CSF 2.0: `DE.CM-06`) `[Decisión / Propuesta Editorial]`.

### D-02: Auditoría de cambios administrativos en políticas DLP, exclusiones y grupos restringidos
- **Objetivo:** Detectar en menos de 24 horas cualquier creación, desactivación, cambio a modo simulación o adición de exclusiones de ruta/aplicación/USB no autorizada en políticas DLP `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Audit > Search` y `Advanced Hunting` (`CloudAppEvents` / `OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / GRC Analyst.
- **Procedimiento Paso a Paso:**
  1. Consultar operaciones administrativas de las últimas 24 horas: `New-DlpCompliancePolicy`, `Set-DlpCompliancePolicy`, `Remove-DlpCompliancePolicy`, `New-DlpComplianceRule`, `Set-DlpComplianceRule`, `Remove-DlpComplianceRule` y cambios en *Endpoint settings* `[Verificado MS Learn]`.
  2. Verificar que toda modificación cuente con ticket ITSM aprobado y sesión elegible en Entra PIM `[Decisión / Propuesta Editorial]`.
  3. Prestar atención crítica a exclusiones de rutas de carpetas, dominios cloud permitidos o dispositivos USB agregados a listas blancas `[Verificado MS Learn]`.
  4. Escalar cualquier cambio no autorizado al playbook `AH-04` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario de cambios administrativos DLP conciliado 1:1 con gestión de cambios (NIST CSF 2.0: `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

### D-03: Triaje unificado de incidentes y alertas DLP por severidad en Microsoft Defender XDR
- **Objetivo:** Investigar, clasificar y contener dentro de SLA los incidentes que agrupan alertas DLP o correlacionan señales DLP con amenazas de endpoint, identidad o correo `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents & alerts > Incidents` (filtro `Service/detection sources = Microsoft Data Loss Prevention`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola de incidentes por `Microsoft Data Loss Prevention` ordenando por severidad (`High`, `Medium`, `Low`) y priorizando incidentes multi-fuente correlacionados con Defender for Endpoint, Entra ID o Insider Risk `[Verificado MS Learn]`.
  2. Utilizar **Summarize** de Security Copilot (si está habilitado) e inspeccionar el *Alert story*, los SITs/etiquetas coincidentes y los eventos previos del usuario mediante el botón **Go Hunt** `[Verificado MS Learn]`.
  3. Clasificar cada alerta como Verdadero Positivo (ejecutar remediación o escalar a `AH-01`/`AH-02`), Falso Positivo (registrar regla y SIT causante para `S-01`) o Excepción de Negocio Válida `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Expedientes de incidentes clasificados en Defender XDR con tiempos de reconocimiento MTTA (NIST CSF 2.0: `DE.AE-02`, MITRE: `Exfiltration / T1048`) `[Decisión / Propuesta Editorial]`.

### D-04: Revisión diaria de eventos "Block with Override" y justificaciones de negocio declaradas
- **Objetivo:** Auditar el 100% de anulaciones realizadas por usuarios finales (*User overrides*) en políticas de alta sensibilidad para detectar evasión deliberada de controles en Exchange, SharePoint, Teams o Endpoint `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Activity explorer` (filtro `Enforcement mode` / `Overridden`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / DLP Analyst.
- **Procedimiento Paso a Paso:**
  1. Filtrar `Activity explorer` en las últimas 24 horas por actividades donde el usuario anuló un bloqueo (`Block with override`) o reportó falso positivo `[Verificado MS Learn]`.
  2. Evaluar la validez de la justificación escrita frente al destinatario externo, dominio web o medio USB utilizado `[Decisión / Propuesta Editorial]`.
  3. Revocar compartición (`Unshare` en SharePoint/OneDrive) o notificar al gerente directo cuando la anulación carezca de sustento de negocio válido, y evaluar al usuario para perfilado de riesgo `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario de auditoría de *overrides* y acciones correctivas aplicadas (NIST CSF 2.0: `PR.DS-05`, MITRE: `Exfiltration / T1567`) `[Decisión / Propuesta Editorial]`.

### D-05: Monitoreo de intentos de exfiltración física y local en Endpoint DLP (USB, Impresión, Red, RDP, JIT)
- **Objetivo:** Detectar intentos concentrados de extracción de archivos confidenciales por canales físicos/locales y vigilar activaciones de **Just-in-Time (JIT) protection** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Activity explorer` y `DeviceEvents` en `https://security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2.
- **Procedimiento Paso a Paso:**
  1. Revisar eventos bloqueados y auditados en `Devices` correspondientes a copia en USB extraíble, impresión local/virtual, copia a recursos de red SMB, transferencia por RDP, Bluetooth y portapapeles `[Verificado MS Learn]`.
  2. Auditar eventos con `JIT triggered = true` verificando si ocurrieron fallos de evaluación que dispararon la acción *fallback* `[Verificado MS Learn]`.
  3. Identificar usuarios con >= 3 intentos bloqueados de egreso en 24 horas y cruzar con estado de desvinculación laboral o nivel en **Adaptive Protection** (`AH-01`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Resumen diario de bloqueos Endpoint DLP y telemetría JIT (NIST CSF 2.0: `DE.CM-01`, MITRE: `Exfiltration Over Physical Medium / T1052`) `[Decisión / Propuesta Editorial]`.

### D-06: Supervisión de bloqueos en Microsoft 365 Copilot y pegado/subida hacia GenAI no gestionada (Shadow AI)
- **Objetivo:** Vigilar intentos de introducir datos regulados/etiquetados en prompts de Microsoft 365 Copilot o de pegar/cargar información corporativa en sitios GenAI públicos desde **Microsoft Edge for Business** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Activity explorer`, `Alerts` y `Solutions > DSPM for AI` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / AI Security Analyst.
- **Procedimiento Paso a Paso:**
  1. Revisar coincidencias de políticas sobre la ubicación **Microsoft 365 Copilot and Copilot Chat** (prompts bloqueados con SITs, archivos con etiqueta restringida excluidos del *grounding* y búsquedas web bloqueadas) `[Verificado MS Learn]`.
  2. Inspeccionar eventos bloqueados o auditados en **Edge for Business** (y extensión de Chrome) hacia aplicaciones IA no administradas (ChatGPT, Gemini, DeepSeek, etc.) y bloqueos de apertura de navegadores no permitidos `[Verificado MS Learn]`.
  3. Escalar a `AH-03` cualquier carga exitosa detectada en reglas que aún estuvieran en auditoría/simulación involucrando código fuente, credenciales o PII masiva `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario de eventos DLP en Copilot y Shadow AI en navegadores (NIST CSF 2.0: `DE.CM-09`, MITRE: `Exfiltration Over Web Service / T1567`) `[Decisión / Propuesta Editorial]`.

### D-07: Vigilancia de actividad DLP sobre usuarios en nivel "Elevated" de Adaptive Protection
- **Objetivo:** Priorizar la supervisión sobre las alertas y bloqueos generados por usuarios clasificados dinámicamente en riesgo elevado por Insider Risk Management `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection` y `security.microsoft.com` (`DataSecurityEvents`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 + Insider Risk Analyst (bajo controles de privacidad).
- **Procedimiento Paso a Paso:**
  1. Revisar alertas DLP vinculadas a reglas con condición `Insider risk level for Adaptive Protection is Elevated` en Exchange, Teams y Devices `[Verificado MS Learn]`.
  2. Verificar que los bloqueos automáticos sin opción de *override* se hayan aplicado efectivamente ante intentos de compartición externa o copia local `[Verificado MS Learn]`.
  3. Coordinar con el analista autorizado de Insider Risk Management si la persistencia de intentos amerita apertura de caso formal (`AH-01`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de efectividad de bloqueos adaptativos sobre perfiles de alto riesgo (NIST CSF 2.0: `PR.AA-05`, `DE.AE-02`) `[Decisión / Propuesta Editorial]`.

### D-08: Control de SLAs de incidentes DLP pendientes y cierre del tablero operativo diario
- **Objetivo:** Garantizar que ningún incidente de fuga potencial supere su ventana máxima de atención/contención y consolidar indicadores de turno `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents & alerts > Incidents` y tablero SOC `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Shift Lead.
- **Procedimiento Paso a Paso:**
  1. Auditar la antigüedad de todos los incidentes DLP en estado `Active` o `In progress` frente al SLA interno (Críticos: MTTA <30 min, MTTC <2 h; Altos: MTTA <2 h, MTTC <6 h) `[Decisión / Propuesta Editorial]`.
  2. Reasignar o escalar inmediatamente casos próximos a incumplimiento `[Decisión / Propuesta Editorial]`.
  3. Emitir reporte de cierre diario con conteo de bloqueos efectivos, *overrides*, alertas pendientes y salud de endpoints `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta diaria de entrega de turno y snapshot de cola DLP en SLA (NIST CSF 2.0: `RS.MA-01`) `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Tuning semanal de reglas DLP, umbrales de instancia/confianza y reducción de falsos positivos
- **Objetivo:** Elevar la tasa de verdaderos positivos (>75%) ajustando condiciones, recuentos de instancias, niveles de confianza y excepciones acotadas sin abrir brechas de exfiltración `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** DLP Engineer / SOC L3.
- **Procedimiento Paso a Paso:**
  1. Agrupar los falsos positivos documentados en `D-03` y `D-04` identificando las 5 reglas y SITs con mayor ruido semanal `[Decisión / Propuesta Editorial]`.
  2. Separar reglas en niveles graduados por volumen de registros (ej. 1–9 instancias: auditoría + *Policy Tip*; >=10 instancias o confianza *High*: bloqueo duro o alertas agregadas) `[Decisión / Propuesta Editorial]`.
  3. Ajustar dominios asociados de negocio legítimos o grupos de excepción temporal con fecha de caducidad `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de tuning de reglas y comparativa de reducción de falsos positivos (NIST CSF 2.0: `ID.IM-03`) `[Decisión / Propuesta Editorial]`.

### S-02: Evaluación y graduación de políticas DLP en modo Simulación hacia Enforcement
- **Objetivo:** Validar resultados de políticas en `Run the policy in simulation mode` (incluyendo la política predeterminada de Microsoft 365 Copilot) antes de habilitar bloqueo activo `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** DLP Engineer + Data Owners.
- **Procedimiento Paso a Paso:**
  1. Revisar coincidencias simuladas de los últimos 7 a 14 días verificando impacto sobre flujos críticos de negocio `[Verificado MS Learn]`.
  2. Activar primero `Show policy tips while in simulation mode` para educar a usuarios y medir reclamos de falsos positivos `[Verificado MS Learn]`.
  3. Promover a `Turn the policy on right away` aquellas políticas que alcancen precisión validada superior al 90% con aprobación del dueño del proceso `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta de paso a producción desde simulación firmada por Data Owner y DLP Lead (NIST CSF 2.0: `PR.DS-05`) `[Decisión / Propuesta Editorial]`.

### S-03: Revisión de higiene de Endpoint DLP (sincronización de políticas, exclusiones, impresoras/USB y navegadores)
- **Objetivo:** Asegurar paridad de protección en toda la flota Windows 10/11 y macOS, versiones antimalware compatibles con JIT y sincronización de políticas de **Microsoft Edge for Business** en Intune `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Data Loss Prevention > Endpoint settings` y `https://intune.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Engineer (Intune/MDE) + DLP Admin.
- **Procedimiento Paso a Paso:**
  1. Identificar endpoints incorporados en MDE/Intune cuyas políticas DLP presenten estado desactualizado o error de sincronización (incluyendo validación de errores `Resync` en políticas de apps no gestionadas para Edge) `[Verificado MS Learn]`.
  2. Auditar las listas de *File path exclusions*, *Unallowed apps*, *Unallowed browsers*, grupos de dispositivos USB (VID/PID/Serial) y grupos de impresoras autorizadas `[Verificado MS Learn]`.
  3. Confirmar despliegue actualizado de la *Microsoft Purview extension* en Google Chrome donde dicho navegador esté permitido `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de salud y cumplimiento de Endpoint DLP e Intune Edge sync (NIST CSF 2.0: `PR.PS-01`) `[Decisión / Propuesta Editorial]`.

### S-04: Auditoría de gobernanza y accesos sobre archivos capturados en Evidence Collection
- **Objetivo:** Verificar que todo acceso de previsualización o descarga de archivos originales recolectados como evidencia desde endpoints esté estrictamente justificado, y controlar el consumo de almacenamiento `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Data Loss Prevention > Endpoint settings > Setup evidence collection > View Usage` y `Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC Lead / Privacy Officer Liaison.
- **Procedimiento Paso a Paso:**
  1. Auditar todas las activaciones PIM y eventos de los roles `Data Classification Content Viewer` y `Data Classification Content Download` ocurridos en la semana `[Verificado MS Learn]`.
  2. Cotejar cada descarga de evidencia contra un expediente de incidente o investigación en **Data Security Investigations** `[Verificado MS Learn]`.
  3. Revisar la gráfica de consumo en `View Usage` (almacenamiento administrado por Microsoft) o las métricas/políticas de retención lifecycle en el Azure Storage Account gestionado por el cliente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semanal de cadena de custodia de evidencias y métricas de almacenamiento (NIST CSF 2.0: `PR.AA-05`, `PR.DS-01`) `[Decisión / Propuesta Editorial]`.

### S-05: Calibración conjunta de perfiles Adaptive Protection con Insider Risk Management
- **Objetivo:** Validar que la distribución de usuarios en niveles `Elevated`, `Moderate` y `Minor` produzca mitigación efectiva en DLP sin sobre-bloqueo ni sub-cobertura `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection` `[Verificado MS Learn]`.
- **Rol Responsable:** Insider Risk Admin + DLP Engineer.
- **Procedimiento Paso a Paso:**
  1. Revisar conteo semanal de usuarios asignados dinámicamente a cada nivel de riesgo y el volumen de reglas DLP disparadas por nivel `[Verificado MS Learn]`.
  2. Confirmar que en **Devices** se encuentre habilitado *Advanced classification scanning and protection* o condiciones válidas de tipo de archivo para que las reglas adaptativas actúen correctamente `[Verificado MS Learn]`.
  3. Ajustar umbrales de puntuación en Insider Risk si se observa exceso de falsas elevaciones operativas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Resumen semanal anonimizado de desempeño de Adaptive Protection (NIST CSF 2.0: `DE.AE-04`) `[Decisión / Propuesta Editorial]`.

### S-06: Verificación de cobertura DLP en Teams (Shared Channels), Microsoft Fabric y Power BI
- **Objetivo:** Auditar brechas de alcance en canales de Teams (asegurando asignación por grupos y no por usuarios sueltos) y atender coincidencias DLP sobre modelos semánticos en Microsoft Fabric / Power BI `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Policies` y portal de administración de **Microsoft Fabric** `[Verificado MS Learn]`.
- **Rol Responsable:** DLP Engineer + Fabric/Teams Admin.
- **Procedimiento Paso a Paso:**
  1. Auditar las políticas que incluyen `Teams chat and channel messages` verificando que el alcance de canales utilice Microsoft 365 Groups o grupos de seguridad (ya que cuentas individuales solo cubren chats 1:1/grupales y no canales) `[Verificado MS Learn]`.
  2. Revisar alertas y *Policy Tips* disparados sobre *workspaces* de **Microsoft Fabric y Power BI**, confirmando restricción de acceso a usuarios `Guest` cuando corresponda `[Verificado MS Learn]`.
- **Evidencia Auditable:** Checklist semanal de alcance Teams DLP y reporte de coincidencias atendidas en Fabric/Power BI (NIST CSF 2.0: `PR.DS-05`) `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Avance y decomiso en la migración obligatoria desde Defender for Cloud Apps File Policies (`2027-01-06`)
- **Objetivo:** Ejecutar y verificar por etapas la migración de todas las *File Policies* heredadas de Defender for Cloud Apps hacia Purview DLP antes de su retiro definitivo el **6 de enero de 2027** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management` y herramienta **DLP to Purview migration** `[Verificado MS Learn]`.
- **Rol Responsable:** DLP Engineer + Cloud App Security Admin.
- **Procedimiento Paso a Paso:**
  1. Ejecutar evaluación en el asistente *DLP to Purview migration*, clasificando las políticas activas en `Can migrate`, `Partial migration` y `Cannot migrate` para SharePoint, OneDrive y nubes no-Microsoft soportadas (Google Workspace, Box, Dropbox, Salesforce) `[Verificado MS Learn]`.
  2. Migrar y desplegar por fases en Purview DLP validando paridad de detección y remediación en modo simulación `[Verificado MS Learn]`.
  3. Desactivar y documentar la baja de las *File Policies* equivalentes en Defender for Cloud Apps para evitar alertas duplicadas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz mensual de progreso hacia el hito `2027-01-06` y actas de decomiso (NIST CSF 2.0: `GV.RM-02`) `[Decisión / Propuesta Editorial]`.

### M-02: Pruebas sintéticas mensuales extremo a extremo de vectores de exfiltración (Purple Team DLP)
- **Objetivo:** Comprobar empíricamente con archivos semilla no productivos que los controles de bloqueo operen según diseño en correo, enlaces anónimos, Teams externo, USB, impresión, Edge/GenAI y Microsoft 365 Copilot `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** Estaciones de prueba Windows 11 y macOS gestionadas + cuentas de prueba E5 / Copilot `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** SOC L3 / QA Security Engineer + DLP Engineer.
- **Procedimiento Paso a Paso:**
  1. Ejecutar batería controlada de 8 pruebas sintéticas: (a) correo externo con SIT/EDM, (b) vínculo externo en SharePoint/OneDrive, (c) mensaje en chat externo de Teams iniciado en el tenant, (d) copia a USB no autorizado con JIT activo, (e) impresión no autorizada, (f) pegado de datos sensibles en ChatGPT/Gemini vía Edge for Business, (g) intento de abrir navegador no permitido, y (h) prompt con SIT / archivo *Highly Confidential* en Microsoft 365 Copilot `[Verificado MS Learn]`.
  2. Confirmar bloqueo efectivo, aparición de *Policy Tip*, captura de archivo en *Evidence Collection* y llegada del evento a `CloudAppEvents` / `DeviceEvents` / `Incidents` en menos de 15 minutos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de pruebas sintéticas Purple Team DLP con capturas y IDs de eventos (NIST CSF 2.0: `PR.DS-05`, `DE.CM-01`) `[Decisión / Propuesta Editorial]`.

### M-03: Exportación histórica de métricas DLP, análisis de reincidencia y reporte ejecutivo CISO
- **Objetivo:** Consolidar series históricas mayores a 30 días, evaluar los 8 KPIs maestros del programa e identificar departamentos con mayor fricción o reincidencia `[Verificado MS Learn]`.
- **Consola y Ruta:** PowerShell (`Export-ActivityExplorerData`), `purview.microsoft.com > Data Loss Prevention > Overview / Reports` y tablero Power BI `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager + DLP Lead.
- **Procedimiento Paso a Paso:**
  1. Consolidar las exportaciones de `Activity explorer` y métricas de incidentes de Defender XDR para calcular `KPI-01` a `KPI-08` `[Decisión / Propuesta Editorial]`.
  2. Identificar las unidades de negocio con mayor tasa de *Policy Tips* ignorados o anulaciones (*overrides*) para dirigir campañas específicas de concientización `[Decisión / Propuesta Editorial]`.
  3. Presentar al CISO el volumen de exfiltraciones prevenidas y el estado de madurez por vector `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte ejecutivo mensual DLP y dataset histórico archivado (NIST CSF 2.0: `GV.OV-01`) `[Decisión / Propuesta Editorial]`.

### M-04: Conciliación mensual de línea base de políticas DLP y auditoría de deriva (Configuration Drift)
- **Objetivo:** Garantizar que el conjunto completo de políticas, prioridades de evaluación y configuraciones globales de Endpoint DLP no haya sufrido alteraciones no documentadas `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** Security & Compliance PowerShell (`Get-DlpCompliancePolicy`, `Get-DlpComplianceRule`) y `purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC / Internal Audit Liaison.
- **Procedimiento Paso a Paso:**
  1. Exportar a JSON/XML todas las políticas, reglas, prioridades de ejecución y configuraciones de endpoint del tenant `[Verificado MS Learn]`.
  2. Comparar contra la línea base aprobada del mes previo verificando especialmente orden de prioridad de reglas y estado `Enable` `[Verificado MS Learn]`.
  3. Purgar exclusiones temporales de usuarios o dispositivos cuya vigencia haya expirado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Snapshot mensual versionado de políticas DLP y acta de conciliación 100% contra ITSM (NIST CSF 2.0: `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

### M-05: Actualización del catálogo de dominios GenAI / nube no gestionados y revisión de novedades Purview
- **Objetivo:** Mantener actualizadas las políticas inline de **Microsoft Edge for Business** / DSPM for AI frente a nuevos servicios emergentes de IA generativa y almacenamiento personal `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM for AI`, `Data Loss Prevention > Endpoint settings > Restricted cloud service domains` y `What's new in Microsoft Purview` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Data Security Architect + DLP Admin.
- **Procedimiento Paso a Paso:**
  1. Cruzar el descubrimiento de *Shadow AI* de Defender for Cloud Apps y DSPM for AI con la lista de dominios restringidos en Endpoint DLP y políticas de colección en Edge for Business `[Verificado MS Learn]`.
  2. Incorporar nuevos dominios de LLMs públicos o repositorios de archivos anónimos detectados en la red `[Decisión / Propuesta Editorial]`.
  3. Evaluar anuncios mensuales en *What's new in Microsoft Purview* para planificar adopción de capacidades que pasen de Preview a GA `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro actualizado de dominios GenAI/cloud gobernados y bitácora de novedades Purview (NIST CSF 2.0: `ID.RA-01`) `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Racionalización arquitectónica de políticas DLP, límites de escala y alineación regulatoria
- **Objetivo:** Consolidar políticas redundantes, verificar alineación con la taxonomía de etiquetas del Módulo 14 y actualizar cobertura frente a cambios normativos (PCI-DSS 4.0, GDPR, HIPAA, Ley 21.719 Chile, LFPDPPP México) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Policies` y `Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Architect + Legal & Privacy + DLP Lead.
- **Procedimiento Paso a Paso:**
  1. Auditar la matriz global de políticas por ubicación consolidando reglas fragmentadas para optimizar rendimiento de evaluación en clientes Office y endpoints `[Verificado MS Learn]`.
  2. Validar que cada nueva etiqueta de sensibilidad o esquema EDM creado en el trimestre esté incorporado en las políticas DLP correspondientes (incluyendo la ubicación *Microsoft 365 Copilot and Copilot Chat*) `[Verificado MS Learn]`.
  3. Confirmar con Legal y Privacidad la cobertura de categorías regulatorias aplicables en Compliance Manager `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz maestra trimestral de cobertura DLP vs. regulaciones aprobada por Legal y Arquitectura (NIST CSF 2.0: `GV.PO-02`) `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Certificación de accesos (Access Reviews) sobre roles DLP y descarga de evidencias
- **Objetivo:** Recertificar en Microsoft Entra ID Governance a todos los integrantes elegibles de roles administrativos de DLP y, con rigor máximo, de visualización/descarga de evidencias `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Identity governance > Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Admin + CISO Delegate.
- **Procedimiento Paso a Paso:**
  1. Ejecutar *Access Reviews* trimestrales sobre `DLP Compliance Management`, `Data Classification Content Viewer`, `Data Classification Content Download` y operadores con `Manage Alerts` `[Verificado MS Learn]`.
  2. Aplicar revocación automática ante falta de aprobación explícita del propietario del control `[Verificado MS Learn]`.
  3. Auditar permisos RBAC sobre el Azure Storage Account utilizado para *Customer-managed Evidence Collection* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte certificado de *Access Reviews* en Entra ID y revisión de ACLs de Azure Storage (NIST CSF 2.0: `PR.AA-05`) `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Ejercicio integral de respuesta ante exfiltración multi-canal (Insider + GenAI + USB)
- **Objetivo:** Poner a prueba la coordinación en vivo entre SOC, DLP, Insider Risk, Endpoint y Legal ante un escenario combinado de robo de propiedad intelectual `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://security.microsoft.com`, `https://purview.microsoft.com` (`Data Security Investigations` / `Insider Risk`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager + Insider Risk Lead + Legal / RR. HH.
- **Procedimiento Paso a Paso:**
  1. Ejecutar simulacro donde un usuario de prueba intenta extraer datos sensibles sucesivamente por correo, Teams externo, subida a IA no gestionada en navegador y USB extraíble `[Decisión / Propuesta Editorial]`.
  2. Medir tiempos de correlación en Defender XDR, elevación automática en **Adaptive Protection**, recolección e inspección de evidencia en **Data Security Investigations** y aislamiento/bloqueo `[Verificado MS Learn]`.
  3. Documentar brechas operativas y actualizar playbooks ad-hoc `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe de resultados del simulacro semestral con métricas MTTA/MTTC y plan de acción (NIST CSF 2.0: `RC.IM-02`) `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión estratégica anual de arquitectura DLP, retención de evidencias y privacidad laboral
- **Objetivo:** Revalidar ante CISO, Legal, Privacidad y Representación Laboral/RR. HH. la proporcionalidad, avisos de privacidad (*Policy Tips*), retención de evidencias y arquitectura global de prevención de fuga de datos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** Gobierno corporativo + `purview.microsoft.com` + Azure Storage Lifecycle Management `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + General Counsel / DPO + Data Security Architect.
- **Procedimiento Paso a Paso:**
  1. Revisar políticas de retención y purga automática de los archivos almacenados en **Evidence Collection** conforme a normativas laborales y de protección de datos personales de cada país `[Decisión / Propuesta Editorial]`.
  2. Revalidar el diseño de seudonimización e integración con Insider Risk Management y **Adaptive Protection** `[Verificado MS Learn]`.
  3. Aprobar el plan anual de evolución tecnológica (cobertura de red SASE/SSE, agentes IA con Agent 365 y optimización de costos) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta anual de aprobación de arquitectura y privacidad de Purview DLP firmada por CISO y DPO (NIST CSF 2.0: `GV.OC-03`, `GV.RM-01`) `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Contención e investigación ante exfiltración activa confirmada en Endpoint o Nube
- **Disparador:** Alerta DLP de severidad `High` con intentos reiterados de extracción de activos críticos (USB, subida web, correo personal) o coincidencia correlacionada en un incidente de Defender XDR con actividad maliciosa `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents & alerts > Incidents` y `https://purview.microsoft.com > Solutions > Data Security Investigations` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2/L3 + DLP Investigator.
- **Secuencia Operativa:**
  1. Abrir el incidente en Defender XDR y usar acciones de remediación nativas: si es archivo en SharePoint/OneDrive ejecutar **Unshare** o aplicar etiqueta cifrante; si es dispositivo comprometido o en fuga crítica, abrir la tarjeta del dispositivo y aislarlo o restringir ejecución de apps en Defender for Endpoint `[Verificado MS Learn]`.
  2. Solicitar elevación JIT de `Data Classification Content Viewer` para verificar en *Activity Explorer / Evidence Collection* el alcance exacto de los archivos involucrados, agregando el lote en **Purview Data Security Investigations** `[Verificado MS Learn]`.
  3. Si se trata de una cuenta comprometida externamente, revocar sesiones y bloquear cuenta en Microsoft Entra ID; si corresponde a empleado activo sospechoso, coordinar elevación inmediata a `Elevated risk` para aplicar bloqueo total vía **Adaptive Protection** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de acciones in-situ en Defender XDR, hash/evidencia preservada y cronología del incidente (NIST CSF 2.0: `RS.MI-01`, MITRE: `Exfiltration / T1048`).

### AH-02: Respuesta inmediata ante exposición accidental en Microsoft Teams o compartición anónima en SharePoint
- **Disparador:** Envío de credenciales, secretos o datos regulados en canales/chats con invitados externos (cuando la regla estaba solo en auditoría o hubo *override* indebido) o creación de enlace externo sobre documento sensible `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents` y SharePoint / Teams Admin `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1/L2 + Collaboration Admin.
- **Secuencia Operativa:**
  1. Ejecutar acción inmediata **Unshare** desde la página de alerta DLP en Defender XDR (o PowerShell SharePoint) para invalidar vínculos externos y accesos de invitados al archivo `[Verificado MS Learn]`.
  2. Si se expuso una credencial, clave API o secreto en un chat externo donde nuestro tenant no era el *hosting tenant* (o antes del bloqueo), rotar inmediatamente el secreto comprometido en el sistema origen `[Verificado MS Learn]`.
  3. Aplicar etiqueta de sensibilidad con cifrado Azure RMS al documento para revocar lectura futura fuera del perímetro `[Verificado MS Learn]`.
- **Evidencia Auditable:** Constancia de revocación de enlaces compartidos, rotación de secretos si aplica y re-etiquetado del archivo (NIST CSF 2.0: `RS.MI-02`, MITRE: `Exfiltration Over Web Service / T1567`).

### AH-03: Contención ante volcado de datos sensibles en herramientas GenAI públicas o prompts críticos
- **Disparador:** Detección de carga de archivos confidenciales o pegado de PII/propiedad intelectual hacia un servicio GenAI no administrado (por ej. desde dispositivo recién incorporado o regla en modo auditoría) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM for AI`, `Data Loss Prevention > Activity explorer` y `Microsoft Defender for Cloud Apps` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / AI Security Analyst + Legal.
- **Secuencia Operativa:**
  1. Identificar en `Activity explorer` y `Evidence Collection` el texto contextual o archivo exacto transmitido, el usuario, el dispositivo y el dominio GenAI receptor `[Verificado MS Learn]`.
  2. Cambiar de inmediato la acción sobre ese dominio a **Block** en la política de **Edge for Business** / Endpoint DLP y bloquear el dominio en Defender for Endpoint Network Indicators (Web Content Filtering / Custom Indicators) si representa riesgo severo `[Verificado MS Learn]`.
  3. Si el volcado incluyó claves, tokens o código propietario, activar rotación de credenciales y evaluación de impacto con Legal/Privacidad `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Captura de evidencia contextual, regla actualizada a bloqueo y evaluación de impacto documentada (NIST CSF 2.0: `RS.MI-01`, MITRE: `Exfiltration / T1567.002`).

### AH-04: Rollback operativo de emergencia ante bloqueo masivo por falso positivo crítico de negocio
- **Disparador:** Regla DLP recién activada o modificada que bloquea erróneamente procesos transaccionales críticos (facturación masiva, intercambio regulatorio bancario, compilación de desarrollo en endpoint) `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Loss Prevention > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** DLP Engineer + SOC Incident Commander.
- **Secuencia Operativa:**
  1. Cambiar la regla específica afectada (no toda la suite DLP del tenant) a `Run the policy in simulation mode` o habilitar temporalmente `Allow override with business justification` mientras se corrige la condición `[Verificado MS Learn]`.
  2. Si el bloqueo ocurre por latencia de **Endpoint DLP JIT protection** sobre una ruta de software transaccional local, agregar exclusivamente la ruta verificada a las exclusiones de JIT (*JIT file path exclusions*, que mantienen la protección DLP normal fuera de la espera JIT) `[Verificado MS Learn]`.
  3. Tener presente los tiempos de replicación (~1 hora hacia cargas cloud/Teams y ciclo de sincronización en endpoints) para comunicar expectativas reales a mesa de ayuda `[Verificado MS Learn]`.
- **Evidencia Auditable:** Ticket de emergencia ITSM, cambio acotado de regla y post-mortem de validación de simulación (NIST CSF 2.0: `RC.RP-01`).

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL y PowerShell Operativas

#### Consulta 1 — Caza de coincidencias y anulaciones (Overrides) DLP en servicios Cloud y Copilot (`CloudAppEvents`) `[Verificado MS Learn]`
```kql
// Lista eventos DLP recientes en Exchange, SharePoint, OneDrive, Teams y M365 Copilot incluyendo overrides
CloudAppEvents
| where Timestamp > ago(24h)
| where ActionType has "DlpRuleMatch" or ActionType in ("DLPRuleUndo", "DlpInfo")
| extend Raw = parse_json(RawEventData)
| extend PolicyName = tostring(Raw.PolicyDetails[0].PolicyName)
| extend RuleName = tostring(Raw.PolicyDetails[0].Rules[0].RuleName)
| extend Actions = tostring(Raw.PolicyDetails[0].Rules[0].Actions)
| extend OverrideReason = tostring(Raw.ExceptionInfo)
| project Timestamp, AccountDisplayName, Application, ActionType, PolicyName, RuleName, Actions, OverrideReason, IPAddress
| order by Timestamp desc
```

#### Consulta 2 — Monitoreo de señales DLP reclasificadas como Behaviors tras Octubre 2026 (`BehaviorInfo` + `BehaviorEntities`) `[Verificado MS Learn]`
```kql
// Permite cazar señales DLP en Defender XDR incluso cuando la regla integrada de Alert Tuning (oct-2026) está activa
BehaviorInfo
| where Timestamp > ago(24h)
| where ServiceSource has "Data Loss Prevention" or DetectionSource has "DLP"
| join kind=leftouter (
    BehaviorEntities
    | where Timestamp > ago(24h)
    | project BehaviorId, EntityType, AccountUpn, FileName, FolderPath, RemoteUrl
) on BehaviorId
| project Timestamp, BehaviorId, Title, Category, Severity, AccountUpn, FileName, RemoteUrl, AttackTechniques
| order by Timestamp desc
```

#### Consulta 3 — Detección de intentos de exfiltración física y web en Endpoint DLP (`DeviceEvents`) `[Verificado MS Learn]`
```kql
// Identifica bloqueos y auditorías de Endpoint DLP por USB, impresión, portapapeles, red, RDP o subida en navegador
DeviceEvents
| where Timestamp > ago(24h)
| where ActionType startswith "Dlp" or ActionType in (
    "FileCopiedToRemovableMedia", "FilePrinted", "ClipBoardCopied",
    "FileCopiedToNetworkShare", "FileUploadedToCloud", "FileCopiedOverRdp")
| summarize TotalEventos = count(), Acciones = make_set(ActionType, 10),
            Archivos = make_set(FileName, 10), Destinos = make_set(RemoteUrl, 5)
  by InitiatingProcessAccountUpn, DeviceName
| where TotalEventos >= 3
| order by TotalEventos desc
```

#### Consulta 4 — Correlación de violaciones de seguridad de datos y uso riesgoso de IA (`DataSecurityEvents`) `[Verificado MS Learn]`
```kql
// Analiza actividades de riesgo en la tabla DataSecurityEvents (requiere opt-in de Insider Risk hacia Defender XDR)
DataSecurityEvents
| where Timestamp > ago(7d)
| where isnotempty(RiskyAIUsageAppCategory) or isnotempty(SequenceCorrelationId)
| project Timestamp, AccountUpn, ActionType, RiskyAIUsageAppCategory,
          RiskyAIUsageSensitivityLabelsInfo, FileName, SequenceCorrelationId
| order by Timestamp desc
```

#### Consulta 5 — Auditoría diaria de cambios administrativos sobre políticas y reglas DLP (`OfficeActivity` / Audit) `[Verificado MS Learn]`
```kql
// Registra toda creación, modificación o eliminación de políticas y reglas DLP en el tenant
OfficeActivity
| where TimeGenerated > ago(24h)
| where Operation in ("New-DlpCompliancePolicy", "Set-DlpCompliancePolicy", "Remove-DlpCompliancePolicy",
                      "New-DlpComplianceRule", "Set-DlpComplianceRule", "Remove-DlpComplianceRule")
| project TimeGenerated, UserId, Operation, Parameters, ClientIP
| order by TimeGenerated desc
```

#### Consulta 6 — Auditoría de inventario de políticas DLP, modo de ejecución y ubicaciones (PowerShell) `[Verificado MS Learn]`
```powershell
# Conectar a Security & Compliance PowerShell e inventariar estado (Enable vs Test) y ubicaciones de políticas DLP
Connect-IPPSSession
Get-DlpCompliancePolicy | Select-Object Name, Mode, Workload, Priority,
    ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation,
    EndpointDlpLocation, ThirdPartyAppDlpLocation, WhenChanged |
    Sort-Object Priority | Format-Table -AutoSize
```

#### Consulta 7 — Auditoría de reglas con Override habilitado o severidad de alerta desactivada (PowerShell) `[Verificado MS Learn]`
```powershell
# Detectar reglas DLP en producción que permiten anulación de usuario o no generan reporte de incidente
Get-DlpComplianceRule | Where-Object { $_.Disabled -eq $false } |
    Select-Object Name, ParentPolicyName, BlockAccess, BlockAccessScope,
                  NotifyAllowOverride, ReportSeverityLevel |
    Export-Csv -Path ".\AuditExports\DLP_Rules_Posture_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation -Encoding utf8
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Componente / Control DLP | Señal de "Proof of Life" Verificable | Superficie / Comando de Verificación | Estado Esperado |
|---|---|---|---|
| **Políticas Core (EXO, SPO, OD, Teams, Devices, Copilot)** | Estado `Enable` (no estancadas indefinidamente en `TestWithoutNotifications`) `[Verificado MS Learn]` | `Get-DlpCompliancePolicy` / `Data Loss Prevention > Policies` | `Mode = Enable` |
| **Regla Alert Tuning DLP en Defender XDR (Oct 2026)** | Configurada explícitamente según decisión del SOC `[Verificado MS Learn]` | `security.microsoft.com > Settings > Microsoft Defender XDR > Alert tuning` | Documentada / Validada |
| **Endpoint DLP Onboarding & JIT Protection** | Equipos Windows 10/11 y macOS reportando políticas activas y eventos `JIT triggered` `[Verificado MS Learn]` | `Settings > Device onboarding` + `Activity explorer` | `>= 98 %` flota activa `[Decisión / Propuesta Editorial]` |
| **Evidence Collection Storage** | Copia íntegra accesible para `Content Viewer` en pruebas sintéticas `[Verificado MS Learn]` | `Endpoint settings > Setup evidence collection > View Usage` | Operativo y dentro de cuota |
| **Microsoft Edge for Business Inline DLP** | Bloqueo activo sobre sitios GenAI no gestionados y bloqueo de navegadores no permitidos `[Verificado MS Learn]` | Prueba sintética `M-02` + sincronización Intune sin error `Resync` | `Synced / Enforced` |
| **Migración File Policies Defender for Cloud Apps** | Cero File Policies críticas pendientes tras transición a Purview antes de `2027-01-06` `[Verificado MS Learn]` | Asistente *DLP to Purview migration* | `100 %` migradas pre `2027-01-06` `[Decisión / Propuesta Editorial]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales

> **Nota de Transparencia:** Las métricas y umbrales siguientes son propuestas consultivas para medir eficacia preventiva y desempeño del SOC, y por tanto se etiquetan íntegramente como `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Tasa de Verdaderos Positivos (Precisión de Alertas DLP)** | `(Alertas DLP clasificadas como VP / Total de alertas DLP triajadas en el periodo) × 100` | `>= 75 %` | Semanal | SOC Manager, DLP Engineer | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cobertura Efectiva de Flota en Endpoint DLP** | `(Endpoints Windows 10/11 y macOS con políticas DLP sincronizadas / Total de endpoints elegibles) × 100` | `>= 98 %` | Semanal | CISO, Endpoint Security Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tiempo Medio de Reconocimiento (MTTA — Alertas DLP High/Critical)** | `Promedio(Timestamp Inicio Triaje − Timestamp Creación Alerta DLP)` | `< 30 min` (Críticas) / `< 2 horas` (Altas) | Mensual | SOC Manager, Auditoría Externa | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tiempo Medio de Contención de Exfiltración (MTTC)** | `Promedio(Timestamp Unshare, Aislamiento o Bloqueo − Timestamp Reconocimiento)` | `< 2 horas` (Críticas) / `< 6 horas` (Altas) | Mensual | CISO, SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa de Anulación de Usuario (Override Rate) e Invalidez** | `(Eventos con User Override ejecutado / Total de eventos con Policy Tip de bloqueo) × 100` | `< 5 %` general (`100 %` de overrides críticos auditados en 24h) | Semanal | DLP Lead, Data Owners | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Proporción de Políticas en Enforcement Activo vs. Simulación** | `(Políticas productivas en modo Enable / Total de políticas DLP diseñadas) × 100` | `>= 85 %` (ninguna política >30 días estancada en simulación sin decisión) | Mensual | Data Security Architect | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tasa de Prevención en Interacciones IA (Copilot y Shadow AI)** | `(Intentos con SITs/Labels bloqueados en M365 Copilot + Edge GenAI / Total de intentos riesgosos detectados en IA) × 100` | `>= 95 %` en bloqueo activo | Mensual | CISO, Comité de Gobierno IA | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Avance de Migración de File Policies MDCA y Control de Cambios** | `100% cambios con ticket ITSM` y `% de File Policies MDCA migradas a Purview antes de 2027-01-06` | `100 %` | Mensual | GRC, Cloud Security Lead | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Verificables |
|---|---|---|
| **Nivel 1** | **Inicial / Solo Auditoría** | Políticas creadas por plantilla predeterminada en modo simulación permanente; alcance limitado a correo o SharePoint básico; alto volumen de ruido no revisado por el SOC. |
| **Nivel 2** | **Base / Cloud Enforcement (E3)** | Bloqueo activo con *Policy Tips* calibrados sobre Exchange Online, SharePoint Online y OneDrive; revisión periódica de alertas individuales y control básico de compartición externa. |
| **Nivel 3** | **Integrado / Omnicanal E5 (Teams + Endpoint DLP)** | Cobertura activa en **Teams chats y canales** y **Endpoint DLP** sin agentes en Windows/macOS (USB, impresión, portapapeles, red, RDP), **JIT protection** habilitado, *Evidence Collection* operativo y migración de File Policies de MDCA completada. |
| **Nivel 4** | **Convergente / XDR + IA Protegida** | Triaje unificado en **Microsoft Defender XDR** (con gobierno explícito de *Alert tuning* y caza KQL en `CloudAppEvents`/`DeviceEvents`/`BehaviorInfo`), políticas en **Microsoft 365 Copilot / Cowork** y bloqueo inline de **Shadow AI en Edge for Business** + **Microsoft Fabric / Power BI**. |
| **Nivel 5** | **Adaptativo / Zero Trust Dinámico** | **Adaptive Protection** ajustando controles en tiempo real según niveles de **Insider Risk Management**, investigación asistida por IA en **Data Security Investigations** y **Security Copilot**, pruebas sintéticas Purple Team mensuales (`M-02`) y evidencia continua NIST CSF 2.0. |

### 11.3 Señales de Alerta Temprana de Degradación Operativa `[Decisión / Propuesta Editorial]`

| Señal Anticipatoria | Condición Observada | Riesgo Subyacente | Acción Correctiva Inmediata |
|---|---|---|---|
| **Silencio súbito en cola de incidentes DLP** | Caída a cero de alertas DLP en `security.microsoft.com` tras actualización de plataforma o cambio administrativo. | Activación inadvertida de la regla integrada de *Alert tuning* (oct-2026) o desactivación accidental de severidad de incidentes. | Ejecutar `D-01` y `Consulta KQL 2` sobre `BehaviorInfo` para verificar flujo real de señales. |
| **Incremento semanal de Override Rate > 10%** | Los usuarios anulan sistemáticamente un bloqueo en correo, SharePoint o Endpoint con textos repetitivos. | Regla calibrada con umbral demasiado bajo o proceso legítimo de negocio no contemplado que genera fatiga. | Activar tuning urgente `S-01` con el Data Owner y auditar muestra en `D-04`. |
| **Desincronización de políticas Edge en Intune** | Aparición de estado de error / `Resync` requerido en políticas para aplicaciones cloud no administradas. | Los dispositivos Windows dejan de aplicar bloqueo inline sobre sitios GenAI no gestionados. | Ejecutar remediación `S-03` con permisos de aplicaciones no gestionadas e Intune Admin. |
| **Aumento de fallos Fallback en Endpoint JIT** | Crecimiento de eventos donde la evaluación JIT agota tiempo y aplica acción de contingencia. | Exclusiones faltantes sobre directorios de compilación/bases locales o versión desactualizada del cliente antimalware. | Revisar `D-05`, versiones MDE y exclusiones exclusivas de ruta JIT (`AH-04`). |
| **Acumulación de políticas > 45 días en Simulación** | Políticas diseñadas que permanecen indefinidamente en `TestWithoutNotifications`. | Falsa sensación de cobertura ante auditoría sin reducción efectiva del riesgo de fuga. | Exigir decisión de graduación o descarte en `S-02` y seguimiento en `M-03`. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome CSWP 29) | Capacidad Habilitadora en Microsoft Purview DLP | Evidencia Auditable Reproducible y MITRE ATT&CK | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.PO-01` | La política para gestionar riesgos cibernéticos y de fuga de información se establece con base en contexto regulatorio y estratégico. | Traducción de políticas corporativas y regulatorias en reglas DLP multicanal sobre etiquetas de sensibilidad, SITs y EDM `[Verificado MS Learn]`. | Matriz maestra `T-01` y exportación `Get-DlpCompliancePolicy`. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.OV-03` | El desempeño de la gestión de riesgos cibernéticos es evaluado y revisado continuamente. | Auditoría de cambios administrativos (`Set-DlpComplianceRule`), control de deriva mensual y gobernanza de privacidad anual `[Verificado MS Learn]`. | Conciliación al 100% en `D-02` / `M-04` y acta anual `A-01`. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` | Las exposiciones y vectores de fuga sobre activos críticos son identificados y validados. | Simulaciones previas de políticas DLP, descubrimiento de Shadow AI en navegador e inventario de File Policies heredadas (hito `2027-01-06`) `[Verificado MS Learn]`. | Actas de simulación `S-02`, catálogo GenAI `M-05` y avance `M-01`. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.IM-03` | Las mejoras se identifican a partir de la ejecución de procesos operativos, monitoreo y pruebas. | Afinamiento semanal de reglas por falsos positivos y batería mensual de pruebas sintéticas Purple Team DLP `[Verificado MS Learn]`. | Bitácora `S-01` e informes mensuales de pruebas `M-02`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos, autorizaciones y restricciones contextuales se aplican bajo mínimo privilegio dinámico. | **Adaptive Protection** ajustando restricciones DLP según nivel `Elevated/Moderate/Minor` y RBAC estricto sobre descarga de evidencias `[Verificado MS Learn]`. | Registros `D-07` / `S-05`, *Access Reviews* `T-02` y auditoría `S-04` — MITRE `T1078`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-02` | La confidencialidad de los datos en tránsito a través de correo, colaboración y red web está protegida. | Bloqueo/cifrado en Exchange Online, eliminación en segundos en **Teams DLP** y bloqueo inline en **Microsoft Edge for Business** hacia apps GenAI no gestionadas `[Verificado MS Learn]`. | Eventos de bloqueo en `Activity explorer` y pruebas `M-02` — MITRE `T1048`, `T1567`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-05` | Las fugas de datos (*data leaks*) se previenen activamente en puntos finales, aplicaciones e IA. | **Endpoint DLP** con **JIT protection** (USB, impresión, portapapeles, red, RDP) y **DLP para Microsoft 365 Copilot / Cowork** (prompts, etiquetas y búsqueda web) `[Verificado MS Learn]`. | Configuraciones activas en Endpoint/Copilot y métricas `KPI-02`, `KPI-07` — MITRE `T1052`, `T1567.002`. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-01` | Los entornos cloud, endpoints y navegadores se monitorean continuamente para detectar intentos de exfiltración. | Telemetría unificada en `CloudAppEvents`, `DeviceEvents`, `DataSecurityEvents`, `BehaviorInfo` y **Activity Explorer** `[Verificado MS Learn]`. | Ejecución diaria de `D-04`, `D-05` y `D-06` con consultas KQL 1 a 4. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Las señales potencialmente adversas se correlacionan para comprender el alcance de un ataque o abuso interno. | Agrupación y correlación de alertas DLP con señales de Defender for Endpoint, Office 365, Entra ID y Sentinel en `security.microsoft.com` `[Verificado MS Learn]`. | Expedientes de incidentes correlacionados en `D-03` y resúmenes Security Copilot. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.AN-03` | Se realiza análisis forense sustentado en evidencia íntegra para establecer qué ocurrió y qué datos se vieron afectados. | **Evidence Collection** de archivos originales hacia Azure Storage / almacenamiento Microsoft e investigación agregada en **Data Security Investigations** `[Verificado MS Learn]`. | Cadena de custodia auditada en `S-04` e informes del playbook `AH-01`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes de fuga de datos se contienen rápidamente en origen y destino. | Acciones de remediación in-situ en Defender XDR (**Unshare**, eliminación, etiquetado, aislamiento de host) y elevación en Adaptive Protection `[Verificado MS Learn]`. | Ejecución documentada de `AH-01`, `AH-02`, `AH-03` y cumplimiento `KPI-04`. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.IM-02` | Los procesos de respuesta y políticas preventivas se fortalecen tras incidentes y ejercicios. | Rollback controlado `AH-04` ante falsos positivos masivos y simulacro semestral multi-canal `SM-01` `[Verificado MS Learn]`. | Informe semestral `SM-01` y actualizaciones de reglas post-incidente. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Destinatario | Nivel | Recursos Oficiales Microsoft Learn y Certificaciones (Nov 2026) | Comunidad Técnica y Ninja Trainings | Competencia Operativa Habilitada |
|---|---|---|---|---|
| **SOC L1 / DLP Analyst** | Nivel 1 (Fundamentos y Triaje) | Ruta oficial *Safeguard sensitive data with Microsoft Purview ninja training scenarios* y módulo *Investigate data loss prevention alerts with Microsoft Defender XDR* `[Verificado MS Learn]`. | Guías operativas de alertas y auditoría en M365.FM (Mirko Peters, MVP). | Ejecución consistente de `D-01` a `D-04` (triaje en Defender XDR, auditoría de *overrides* y validación de telemetría). |
| **DLP Engineer / Collaboration & Fabric Admin** | Nivel 2 (Ingeniería de Políticas) | Certificación oficial **Exam SC-401 (Information Security Administrator Associate)** + Credencial aplicada **SC-5003** + documentación de *Teams DLP*, *Fabric DLP* y migración MDCA `[Verificado MS Learn]`. | Análisis técnico en *Office 365 for IT Pros* (Tony Redmond, MVP) y diseño de políticas Purview (Joanne Klein, MVP). | Diseño, simulación, tuning y migración de políticas cloud, Teams, Fabric y salida de File Policies MDCA (`S-01`, `S-02`, `S-06`, `M-01`). |
| **Endpoint Security / SOC L2-L3 Engineer** | Nivel 3 (Endpoint, JIT, Forense y KQL) | Módulos Learn *Implement endpoint data loss prevention with Microsoft Purview*, *Endpoint DLP JIT protection*, *Evidence collection* y *Edge for Business DLP* `[Verificado MS Learn]`. | Referencia oficial *Layered data protection across endpoint, browser, and network* (`aka.ms/purviewlayeredprotection`, Nick-MSFT) y laboratorios KQL (Jorge Castañeda, MVP). | Operación avanzada de Endpoint DLP, JIT, custodia de evidencias, caza en `DeviceEvents`/`BehaviorInfo` y playbooks `AH-01` a `AH-04`. |
| **CISO / Data & AI Security Architect** | Nivel 4 (Gobierno Adaptativo e IA) | Documentación oficial *Purview DLP for Microsoft 365 Copilot, Copilot Chat, and Cowork* (oct-2026) y *Adaptive Protection* `[Verificado MS Learn]`. | Sesiones de *Shadow AI & Data Security* (Nikki Chapple, MVP) y resúmenes mensuales CISO/CDO (Albert Hoitingh, MVP). | Gobierno de **Adaptive Protection**, protección de IA generativa y agentes, comité ejecutivo mensual (`M-03`) y revisión anual de privacidad (`A-01`). |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Hallazgos Verificados contra Microsoft Learn (`2026-11-11`)

| # | Aspecto Auditado / Consolidado (`MSEOP-MD\Purview DLP`) | Hallazgo / Estado Vigente a Noviembre de 2026 (`[Verificado MS Learn]`) | Impacto Aplicado en la Guía |
|---|---|---|---|
| **1** | Depuración estructural del repositorio origen `MSEOP-MD\Purview DLP` | Consolidación limpia tomando exclusivamente los compilados validados en `0427 Purview DLP Bloques SecOps` (`Claude - Compilado final (Limpio)` y `Architect v6`), `DLP NIST VC` y `Purview DLP - VC LIC`, **ignorando y descartando en su totalidad la carpeta `NO`**. | Documentado en Portada, Sección 14 y contrato JSON. |
| **2** | Cambio crítico de comportamiento de alertas DLP en Microsoft Defender XDR (Octubre 2026) | `dlp-investigate-alerts-defender` confirma que a inicios de **octubre de 2026** entró en vigor una regla integrada de *Alert tuning* que convierte señales DLP en *behaviors* (`BehaviorInfo` / `BehaviorEntities`) sin crear alertas en la cola de incidentes, salvo que el administrador desactive la regla en `Settings > Microsoft Defender XDR > Alert tuning`. | Incorporado en Secciones 2, 3, `D-01`, Consulta KQL 2 y *Proof of Life*. |
| **3** | Ampliación de DLP para Microsoft 365 Copilot, Copilot Chat y Cowork | `dlp-microsoft365-copilot-location-learn-about` (actualizado el `2026-10-27`) documenta soporte para **Microsoft 365 Copilot, Copilot Chat y Cowork**, añadiendo bloqueo de búsquedas web externas (`Performing Web Searches`) cuando prompts contienen SITs, además de bloqueo de prompts con SITs, exclusión de archivos/correos por etiqueta y política predeterminada en simulación. | Actualizado en Secciones 2, 3, `D-06`, `M-02` y matriz E5. |
| **4** | Protección inline contra Shadow AI en Microsoft Edge for Business | `dlp-browser-dlp-learn` (`2026-09-15`) y `dlp-create-policy-block-to-ai-via-edge` confirman bloqueo inline en Edge for Business (Windows 10/11 en Intune) hacia ChatGPT, Gemini y DeepSeek, bloqueo de navegadores no protegidos, precedencia de Endpoint DLP sobre políticas inline de Edge e incompatibilidad con *Multi-admin approval* en Intune. | Incorporado en Secciones 2, 3, `D-06`, `S-03` y `M-05`. |
| **5** | Retiro de File Policies en Microsoft Defender for Cloud Apps (`2027-01-06`) y alcance del asistente | `migrate-file-policies-to-purview` (`2026-08-28`) fija el retiro definitivo en **6 de enero de 2027** y confirma que la herramienta *DLP to Purview migration* soporta SharePoint, OneDrive y cargas DLP no-Microsoft (Google Workspace, Box, Dropbox, Salesforce). | Incorporada actividad mensual dedicada `M-01` y `KPI-08`. |
| **6** | Endpoint DLP Just-in-Time (JIT) Protection y Evidence Collection | `endpoint-dlp-learn-about-jit` y `dlp-copy-matched-items-get-started` (jun-2026) verifican soporte JIT en Windows 10/11 y macOS (3 últimas versiones), recolección de archivos originales en Azure Storage del cliente o almacenamiento Microsoft, roles `Data Classification Content Viewer` / `Content Download` e integración con **Data Security Investigations**. | Reflejado en Secciones 3, 4, `D-05`, `S-04` y `AH-01`. |
| **7** | Reglas de alcance multi-tenant y por grupos en Microsoft Teams DLP | `dlp-microsoft-teams` precisa que los canales (estándar, privados y compartidos) solo quedan cubiertos al asignar políticas a grupos (no a usuarios individuales), que en *Shared Channels* rige el tenant del remitente y en chats *external access* rige el tenant iniciador del hilo. | Añadida validación explícita en Sección 3.3, `S-06` y `AH-02`. |
| **8** | Nomenclatura de licencias **Microsoft Purview Suite** y tabla `DataSecurityEvents` | Renombre oficial de *M365 E5 Compliance* a **Microsoft Purview Suite** (oct-2025), precisión de que Office 365 E5 puro no incluye Endpoint DLP y requisito de *opt-in* desde Insider Risk Management para poblar `DataSecurityEvents` en Advanced Hunting (`2026-09-01`). | Actualizado en Sección 2.2 y Consulta KQL 4. |

### 14.2 Decisiones y Propuestas Editoriales Explícitas

| # | Elemento en la Guía | Clasificación | Justificación Arquitectónica y Operativa |
|---|---|---|---|
| **1** | Consolidación limpia excluyendo la carpeta `NO` y organización en 27 actividades operacionales (`D`, `S`, `M`, `T`, `SM`, `A`, `AH`) | `[Decisión / Propuesta Editorial]` | Asegura trazabilidad documental limpia sobre los compilados validados y estructura un ciclo operativo completo para el SOC. |
| **2** | Ventanas de SLA más estrictas para DLP (MTTA < 30 min y MTTC < 2 h en severidad crítica) respecto a alertas informativas | `[Decisión / Propuesta Editorial]` | Una alerta DLP de alta severidad suele representar una exfiltración en curso o inminente, exigiendo contención más veloz. |
| **3** | Metas cuantitativas de los 8 KPIs (`>=75%` precisión VP, `>=98%` cobertura Endpoint DLP, `<5%` tasa de override) | `[Decisión / Propuesta Editorial]` | Provee umbrales objetivos de gestión de ruido, cobertura real de flota y control de excepciones para reporte ejecutivo. |
| **4** | Segregación estricta en Entra PIM de `Data Classification Content Download` (JIT máx. 1 h con aprobación dual) | `[Decisión / Propuesta Editorial]` | Los archivos capturados por *Evidence Collection* contienen por definición información altamente sensible o regulada, requiriendo custodia forense reforzada. |
| **5** | Batería mensual de 8 pruebas sintéticas Purple Team DLP (`M-02`), modelo de madurez de 5 niveles y mapeo de 12 subcategorías NIST CSF 2.0 | `[Decisión / Propuesta Editorial]` | Sustituye la confianza declarativa en la consola por verificación empírica continua con evidencia reproducible ante auditores. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Learn about data loss prevention (Enterprise applications & devices and Inline web traffic)*: `https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp`
- **REF-02:** Microsoft Learn — *Learn about Endpoint data loss prevention (Windows 10/11 & macOS)*: `https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about`
- **REF-03:** Microsoft Learn — *Learn about Microsoft Purview Data Loss Prevention just-in-time (JIT) protection*: `https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about-jit`
- **REF-04:** Microsoft Learn — *Get started with collecting files that match data loss prevention policies from devices (Evidence collection)*: `https://learn.microsoft.com/en-us/purview/dlp-copy-matched-items-get-started`
- **REF-05:** Microsoft Learn — *Learn about using Microsoft Purview DLP to protect interactions with Microsoft 365 Copilot, Copilot Chat, and Cowork* (actualizado 27-oct-2026): `https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about`
- **REF-06:** Microsoft Learn — *Learn about Data Loss Prevention for Cloud Apps in Microsoft Edge for Business* (actualizado 15-sep-2026): `https://learn.microsoft.com/en-us/purview/dlp-browser-dlp-learn`
- **REF-07:** Microsoft Learn — *Help prevent sharing via Microsoft Edge for Business to unmanaged AI apps from managed devices*: `https://learn.microsoft.com/en-us/purview/dlp-create-policy-block-to-ai-via-edge`
- **REF-08:** Microsoft Learn — *Learn about Adaptive Protection in Data Loss Prevention*: `https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn`
- **REF-09:** Microsoft Learn — *Data loss prevention and Microsoft Teams (Chats, Private & Shared Channels)*: `https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams`
- **REF-10:** Microsoft Learn — *Get started with data loss prevention policies for Microsoft Fabric and Power BI*: `https://learn.microsoft.com/en-us/purview/dlp-powerbi-get-started`
- **REF-11:** Microsoft Learn — *Investigate data loss prevention alerts with Microsoft Defender XDR (incluye nota Alert Tuning oct-2026)*: `https://learn.microsoft.com/en-us/defender-xdr/dlp-investigate-alerts-defender`
- **REF-12:** Microsoft Learn — *DataSecurityEvents table in the advanced hunting schema*: `https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-datasecurityevents-table`
- **REF-13:** Microsoft Learn — *Migrate file policies to Microsoft Purview (Retiro 6 de enero de 2027)*: `https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview`
- **REF-14:** Microsoft Learn — *Microsoft Purview service description (DLP & Purview Suite licensing)* (actualizado 09-nov-2026): `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description`

### Blogs Oficiales y Empleados de Microsoft
- **REF-15:** Nick-MSFT (Microsoft Purview Blog) — *Close the gaps: layered data protection with Microsoft Purview across endpoint, browser, and network* (ago-2026): `https://techcommunity.microsoft.com/blog/microsoft-purview-blog/close-the-gaps-layered-data-protection-with-microsoft-purview-across-endpoint-br/4550997`
- **REF-16:** Microsoft Learn Training — *Safeguard sensitive data with Microsoft Purview ninja training scenarios*: `https://learn.microsoft.com/en-us/training/paths/purview-ninja-safeguard-data/`

### Comunidad Técnica y MVPs de Seguridad / Microsoft 365
- **REF-17:** Nikki Chapple (Dual Microsoft MVP, M365 & Security) — *Preventing Data Leakage from Generative AI Apps & Shadow AI (2026)*: `https://nikkichapple.com/speaking-engagements-2026/`
- **REF-18:** Tony Redmond (Microsoft MVP) — *Office 365 for IT Pros — Purview Data Loss Prevention & Compliance Analysis*: `https://office365itpros.com/category/microsoft-information-protection/`
- **REF-19:** Albert Hoitingh (Microsoft MVP) — *Things to Know About Microsoft Purview — DLP, Network & Agent 365 Updates (sep-2026)*: `https://alberthoitingh.com/2026/09/04/things-to-know-about-microsoft-purview-september-2026/`

### Marcos Normativos y Arquitectónicos
- **REF-20:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)*: `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`

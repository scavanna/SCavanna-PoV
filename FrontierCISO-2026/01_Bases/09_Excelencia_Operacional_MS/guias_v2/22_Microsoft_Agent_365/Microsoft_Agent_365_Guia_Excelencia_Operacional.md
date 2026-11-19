# Guía Maestra de Excelencia Operacional: Microsoft Agent 365 (Plano de Control Empresarial de Identidad, Seguridad, Datos y Gobierno para Agentes de IA)

## 1. Portada y Ficha de Control Documental

| Campo de Control | Valor Oficial |
| :--- | :--- |
| **Identificador del Módulo** | `22_Microsoft_Agent_365` |
| **Orden en Repositorio Maestro** | `22` |
| **Slug Canónico** | `Microsoft_Agent_365` |
| **Nombre Completo Oficial** | Microsoft Agent 365 (Plano de Control Empresarial de Identidad, Seguridad, Datos y Gobierno para Agentes de IA) `[Verificado MS Learn]` |
| **Categoría Maestra** | `Gobierno y Seguridad de Agentes IA` |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | `Nuevo desde Microsoft Learn MCP (Nov 2026)` |
| **Relación con Microsoft 365 E5** | `Complemento / Add-on sobre M365 E5 (Standalone o incluido en Microsoft 365 E7: The Frontier Suite)` `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://admin.microsoft.com`, `https://entra.microsoft.com`, `https://security.microsoft.com`, `https://purview.microsoft.com`, `https://intune.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, CIO, Chief AI Officer (CAIO), AI Administrator, Identity Architect, SOC Manager, Analistas SOC L2/L3, Purview Data Security AI Admin, Agent Sponsors / Propietarios de Negocio, GRC y Ética de IA `[Decisión / Propuesta Editorial]` |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST AI Risk Management Framework (AI RMF 1.0) y NIST AI 600-1 (GenAI Profile), OWASP Top 10 for LLM Applications (2025) y OWASP Top 10 for Agentic Applications (2026: `ASI01`–`ASI10`), MITRE ATT&CK v18 y MITRE ATLAS (`AML.T0051`, `AML.T0054`, `AML.T0043`, `AML.T0057`) `[Decisión / Propuesta Editorial]` |

> **Nota de Consolidación y Vigencia (Corte 11 de noviembre de 2026):** Esta guía operacional incorpora de forma íntegra la arquitectura en disponibilidad general (GA desde el **1 de mayo de 2026**) de **Microsoft Agent 365** y **Microsoft 365 E7: The Frontier Suite**, la convergencia del registro empresarial de agentes hacia el **Microsoft 365 Admin Center**, la arquitectura de objetos de **Microsoft Entra Agent ID** (`agentIdentityBlueprint`, `agentIdentity`, `agentUser`), el gobierno de gateways **Model Context Protocol (MCP)** (Azure AI Gateway y LiteLLM), la protección en tiempo de ejecución de **Microsoft Defender** (con migración obligatoria a la tabla `AgentsInfo` tras el retiro de `AIAgentsInfo` el 1 de julio de 2026) y la observabilidad de postura de datos y riesgo interno (`Risky Agents`) en **Microsoft Purview** `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica hacia la Empresa Agéntica (Ignite 2025 a Noviembre 2026)

La proliferación acelerada de agentes de inteligencia artificial capaces de razonar sobre contexto organizacional, invocar herramientas externas, comunicarse con otros agentes y ejecutar acciones autónomas ha transformado radicalmente la superficie de ataque corporativa. Presentado inicialmente en **Microsoft Ignite (18 de noviembre de 2025)** dentro del programa *Frontier*, anunciado comercialmente el **9 de marzo de 2026** y lanzado en **disponibilidad general (GA) para clientes comerciales el 1 de mayo de 2026**, **Microsoft Agent 365** constituye el plano de control empresarial unificado (*Enterprise Control Plane for AI Agents*) de Microsoft para observar, gobernar y asegurar todo el parque de agentes de IA sin reconstruir la infraestructura de seguridad existente `[Verificado MS Learn]`.

Bajo la premisa arquitectónica de gobernar a los actores no humanos con el mismo rigor de identidad, mínimo privilegio y cumplimiento aplicado a los empleados humanos, Microsoft Agent 365 extiende de forma nativa los cuatro pilares del stack de seguridad empresarial —**Microsoft Entra**, **Microsoft Defender**, **Microsoft Purview** y **Microsoft Intune**— sobre agentes construidos en plataformas Microsoft (**Microsoft Copilot Studio**, **Microsoft Foundry**, **Microsoft Copilot Agent Builder**, **SharePoint**, **Microsoft 365 Agents Toolkit**), agentes preintegrados e *Agent Factories* de partners del ecosistema (**Adobe, ServiceNow, Workday, Salesforce, Box, Canva, Celonis, Egnyte, Genspark, Kasisto, Kore.ai, Manus, n8n, NVIDIA, Sophos, Zendesk, Zensai**), nubes de terceros sincronizadas (**Amazon Bedrock** y **Google Cloud / Vertex AI**) y agentes locales ejecutados en dispositivos endpoint (**OpenClaw, Claude Desktop/Code, ChatGPT Desktop, Ollama Desktop**) `[Verificado MS Learn]`. Adicionalmente, desde el **1 de octubre de 2026**, Microsoft Agent 365 cumple todos los controles **FedRAMP High** evaluados por su asesor independiente de tercera parte (con autorización final de agencia pendiente) `[Verificado MS Learn]`.

### 2.2 Modelo de Licenciamiento, Relación con Microsoft 365 E5 / E7 y Prerrequisitos Técnicos

Microsoft Agent 365 NO viene incluido como derecho completo dentro de la suscripción estándar de **Microsoft 365 E5**, sino que opera como un **complemento (*Add-on*) por usuario** diseñado para potenciar las inversiones existentes de identidad, XDR, DLP y gestión de endpoints de clientes E5, o bien se adquiere integrado dentro de **Microsoft 365 E7: The Frontier Suite** `[Verificado MS Learn]`.

| Modalidad / SKU | Precio Público de Lista (USD) | Alcance y Capacidades Habilitadas | Relación con Microsoft 365 E5 y Prerrequisitos |
| :--- | :--- | :--- | :--- |
| **Capacidades Base en Suscripciones M365 (E3 / E5 / Business / Edu / FLW)** | Incluido en plan base | Inventario básico en Agent Registry (`admin.microsoft.com`), acciones básicas (publicar, desplegar, bloquear, eliminar, aprobar, reasignar owner, fijar), reglas simples basadas en condiciones y sincronización básica de metadatos externos `[Verificado MS Learn]`. | También incluye sin costo adicional la creación base de identidades en Entra Agent ID y la *Default Agent Identity Inactivity Lifecycle Policy* (60/90/455 días) `[Verificado MS Learn]`. |
| **Microsoft Agent 365 (Standalone Add-on)** | **USD $15 / usuario / mes** (compromiso anual, GA 1-may-2026) `[Verificado MS Learn]` | Desbloquea observabilidad avanzada (*Agent Map*, telemetría de uso/ROI), *Security Policy Templates*, gobierno tenant-wide de herramientas y servidores MCP, APIs Graph de registro, *Conditional Access* e *ID Protection* para agentes, *Access Packages* y ciclos de vida por sponsor en Entra, controles de red SASE para agentes, Purview *DSPM AI Observability*, respeto de etiquetas de sensibilidad, DLP, *Insider Risk Management* (`Risky Agents`), Audit/eDiscovery/DLM sobre interacciones de agentes, postura/detección/bloqueo runtime en Defender y bloqueo de agentes locales Shadow AI en Intune `[Verificado MS Learn]`. | **Funciona de forma óptima con Microsoft 365 E5 como prerrequisito** (o M365 E5/A5/Business Premium, o Microsoft Defender Suite + Microsoft Purview Suite + Entra ID P1/P2). Cada licencia cubre a toda persona que administra, patrocina (*sponsors*) o utiliza agentes que trabajan en su nombre `[Verificado MS Learn]`. |
| **Microsoft 365 E7: The Frontier Suite** | **USD $99 / usuario / mes** (disponible con y sin Teams, GA 1-may-2026) `[Verificado MS Learn]` | Suite insignia *Intelligence + Trust* que unifica en un solo SKU: **Microsoft 365 E5** completo + **Microsoft 365 Copilot** (impulsado por *Work IQ* y *Copilot Cowork*) + **Microsoft Agent 365** + **Microsoft Entra Suite** (Entra ID Governance, Internet Access, Private Access, Verified ID Face Check) `[Verificado MS Learn]`. | Consolida la protección de empleados humanos y agentes autónomos a un costo inferior a la adquisición *à la carte* de sus componentes individuales `[Verificado MS Learn]`. |
| **Auditoría Purview de IA de Terceros No Conectada (Pay-As-You-Go)** | Medidor de consumo Azure PAYG | Retención de 180 días para registros `AIAppInteraction` y ciertos escenarios `ConnectedAIAppInteraction` de aplicaciones IA no Microsoft fuera del ecosistema nativo; las apps Microsoft, Copilot Studio y Foundry se incluyen en *Audit Standard* `[Verificado MS Learn]`. | Requiere vincular suscripción de Azure para facturación PAYG en Microsoft Purview cuando se auditan sitios GenAI externos vía red/navegador `[Verificado MS Learn]`. |

**Prerrequisitos Técnicos Obligatorios de Despliegue `[Verificado MS Learn]`:**
1. Al menos una licencia activa elegible de **Microsoft Agent 365** o **Microsoft 365 E7** en el tenant y aceptación expresa de los términos del servicio por un **Global Administrator** en `https://admin.microsoft.com` antes de que fluya telemetría desde Microsoft Foundry o agentes de terceros.
2. En **Microsoft Defender** (`security.microsoft.com > Settings > Security for AI > Get started`), activar la recopilación de seguridad para agentes IA y conectar el **Microsoft 365 connector** con al menos los componentes *Microsoft Entra ID Management events*, *Microsoft 365 activities* y *Microsoft Entra Users and groups*.
3. Para agentes locales y detección de **Shadow AI**, inscripción de endpoints Windows en **Microsoft Intune**, **Microsoft Defender for Endpoint** en modo activo, licencia **Microsoft 365 E5/E7**, inscripción en el programa *Frontier* (mientras las funciones Shadow AI permanezcan en preview) y habilitación recomendada de **Global Secure Access (Internet Access traffic forwarding)** para poblar telemetría de red, usuarios y actividad reciente.
4. Para inspección de herramientas en pasarelas externas, despliegue del tier **AI Gateway en Azure API Management** (con token delegado de usuario Entra ID) o proxy empresarial **LiteLLM** registrado en Entra ID.

#### Desglose Oficial de Disponibilidad de Capacidades por Plan y Nube Gubernamental (GCC) `[Verificado MS Learn]`

De acuerdo con la *Service Description* oficial de Microsoft Agent 365 (actualizada en octubre de 2026), la frontera funcional exacta entre suscripciones base de Microsoft 365 y el licenciamiento de **Microsoft Agent 365 / Microsoft 365 E7** es la siguiente:

| Capacidad Oficial de Microsoft Agent 365 | Consola Primaria | Incluido en M365 Base (E3/E5/Bus/Edu/FLW) | Requiere M365 E7 / G7 o Agent 365 | Disponible en GCC |
| :--- | :--- | :---: | :---: | :---: |
| Inventario de agentes de toda la organización en el Agent Registry | M365 Admin Center | Sí | Sí | Sí |
| Acciones básicas de gobierno (publicar, desplegar, bloquear, eliminar, aprobar, asignar usuarios/grupos, reasignar owner, fijar) | M365 Admin Center | Sí | Sí | Sí |
| Automatización de acciones de ciclo de vida mediante reglas basadas en condiciones | M365 Admin Center | Sí | Sí | Sí |
| Sincronización de agentes y metadatos desde plataformas externas no gestionadas hacia el registro | M365 Admin Center | Sí | Sí | Sí |
| Plantillas de políticas (*Policy templates*) aplicando controles personalizados a agentes | M365 Admin Center | No | Sí | Sí |
| Observabilidad y monitoreo de actividad de agentes (visualización Agent Map y telemetría) | M365 Admin Center | No | Sí | Sí |
| Control a escala de tenant sobre qué herramientas y servidores MCP pueden invocar los agentes | M365 Admin Center | No | Sí | Sí |
| Acceso mediante Microsoft Graph API al registro de agentes, metadatos y acciones de gobierno | Microsoft Graph | No | Sí | No |
| *Access packages* para agentes que definen el alcance temporal de permisos | Microsoft Entra | No | Sí | Sí |
| Políticas integradas de ciclo de vida en Entra impulsadas por *sponsors* humanos | Microsoft Entra | No | Sí | Sí |
| *Conditional Access* e *Identity Protection* para agentes (extendiendo políticas de usuario y riesgo) | Microsoft Entra | No | Sí | Sí |
| Monitoreo y bloqueo de tráfico de red malicioso o no conforme para agentes en dispositivos y Copilot Studio | Microsoft Entra (GSA) | No | Sí | No |
| Registros de auditoría (*Audit*) y *eDiscovery* (*content search*, *hold* y exportación) de interacciones de agentes | Microsoft Purview | No | Sí | No |
| *Data Lifecycle Management* (retención y eliminación) para datos e interacciones generadas por agentes | Microsoft Purview | No | Sí | No |
| Detección de interacciones no conformes (*Communication Compliance*) y evaluaciones IA en *Compliance Manager* | Microsoft Purview | No | Sí | No |
| *Data Security Posture Management (DSPM)* con *AI Observability* para visibilidad profunda de interacciones | Microsoft Purview | No | Sí | No |
| Extensión de *Insider Risk Management* a agentes (`Risky Agents`) para detectar actividades anómalas | Microsoft Purview | No | Sí | No |
| Herencia/respeto de etiquetas de sensibilidad (*Sensitivity labels*) por parte de los agentes | Microsoft Purview | No | Sí | No |
| *Data Loss Prevention (DLP)* para bloquear el acceso y compartición de contenido sensible por agentes | Microsoft Purview | No | Sí | No |
| Sincronización de agentes locales *Shadow AI* detectados en endpoints | Microsoft Defender | No | Sí | No |
| Postura de seguridad de agentes (configuraciones erróneas, exposición y mapa de relaciones agente-dispositivo-MCP) | Microsoft Defender | No | Sí | No |
| Detección de actividad sospechosa, generación de alertas y bloqueo en tiempo de ejecución de herramientas | Microsoft Defender | No | Sí | No |
| Recolección unificada de logs de observabilidad Agent 365 e investigación/caza (*Advanced Hunting*) | Microsoft Defender | No | Sí | Sí |
| Cumplimiento de dispositivo (*Device compliance*) para Acceso Condicional de agentes | Microsoft Intune | No | Sí | Sí |
| Entorno controlado por políticas para ejecución de agentes (*Windows 365 for Agents*) | Microsoft Intune | No | Sí | No |
| Bloqueo de agentes locales no autorizados en endpoints gestionados (`A365 - Block OpenClaw`) | Microsoft Intune | No | Sí | No |

### 2.3 Principios Rectores y Posicionamiento Zero Trust para Agentes IA

Microsoft Agent 365 materializa los tres pilares de **Zero Trust** (*Verify Explicitly*, *Use Least Privilege Access*, *Assume Breach*) sobre sistemas agénticos mediante seis principios rectores verificables:

1. **Visibilidad Total y Registro Único Convergente (Zero Blind Spots):** Todo agente primera parte, de partners, multi-nube o local (*Shadow AI*) debe converger en el **Agent Registry** del Microsoft 365 Admin Center antes de interactuar con datos corporativos, bloqueando o poniendo en cuarentena cualquier agente no autorizado `[Verificado MS Learn]`.
2. **Identidad Agéntica de Primera Clase y Responsabilidad Humana Ineludible (*Human Accountability*):** Ningún agente debe operar con credenciales estáticas compartidas ni *service principals* genéricos sin gobierno; cada agente recibe un **Microsoft Entra Agent ID** vinculado a un *Blueprint* y respaldado obligatoriamente por un **Owner** técnico y un **Sponsor** humano de negocio con traspaso automático de responsabilidad ante bajas laborales `[Verificado MS Learn]`.
3. **Mínimo Privilegio Dinámico y Bloqueo Duro de Permisos Críticos:** Los agentes solo obtienen acceso acotado temporalmente mediante **Access Packages** en Entra ID Governance, están sujetos a la prohibición técnica en plataforma de más de 50 permisos críticos de Microsoft Graph (como `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory` o `Files.ReadWrite.All` app-only) y ven restringidas individualmente las herramientas de escritura/borrado en servidores MCP `[Verificado MS Learn]`.
4. **Evaluación Explícita de Contexto y Riesgo en Tiempo Real (*Verify Explicitly*):** Cada adquisición o intercambio de token (flujo delegado *On-Behalf-Of*, *App-only* autónomo o cuenta *Agent User*) es evaluada por **Conditional Access para Agentes** e **ID Protection (`riskyAgents`)**, aplicando restricciones de red SASE mediante **Global Secure Access** `[Verificado MS Learn]`.
5. **Protección de Datos por Diseño y Cumplimiento Auditable de Extremo a Extremo:** Los agentes respetan los derechos de uso `VIEW` y `EXTRACT` de **Sensitivity Labels**, son inspeccionados por **DLP** e **Insider Risk Management (`Risky Agents`)**, y toda interacción humano-agente, agente-herramienta y agente-agente queda registrada en **Purview Audit** y preservable en **eDiscovery** `[Verificado MS Learn]`.
6. **Defensa Profunda en Tiempo de Ejecución (*Assume Breach* en el Bucle Agéntico):** Se asume que todo agente expuesto a contenido externo puede sufrir *Indirect Prompt Injection (XPIA)* o secuestro de objetivo; **Microsoft Defender** evalúa la postura continuamente e intercepta en tiempo real invocaciones maliciosas de herramientas, exfiltración de secretos y dominios inseguros antes de su ejecución `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Los Cinco Pilares Arquitectónicos Oficiales de Microsoft Agent 365

De acuerdo con la arquitectura oficial de Microsoft Learn y los anuncios fundacionales de ingeniería, Microsoft Agent 365 articula el control empresarial a través de **cinco pilares arquitectónicos interconectados** (sintetizados ejecutivamente en las capacidades *Observe, Govern, Secure*) `[Verificado MS Learn]`:

```text
+---------------------------------------------------------------------------------------------------+
|                           PLANO DE CONTROL: MICROSOFT AGENT 365                                   |
|                    (Microsoft 365 Admin Center - https://admin.microsoft.com)                     |
+-------------------+-------------------+-------------------+-------------------+-------------------+
|  1. REGISTRY      | 2. ACCESS CONTROL | 3. VISUALIZATION  | 4. INTEROPERA-    |  5. SECURITY &    |
|  (Inventario y    |    E IDENTIDAD    |  & OBSERVABILITY  |    BILITY         |  DATA GOVERNANCE  |
|   Ciclo de Vida)  | (Entra Agent ID)  | (Telemetria/Mapa) | (Work IQ & MCP)   | (Defender/Purview)|
+-------------------+-------------------+-------------------+-------------------+-------------------+
| - All Agents      | - Blueprints      | - Agent Overview  | - Work IQ MCP     | - Defender Assets |
| - Shadow AI       | - Agent Identity  | - Agent Map       |   (10 tools GA)   |   & AgentsInfo    |
| - Registry Sync   | - Agent User      | - Single Agent    | - Tools Registry  | - Real-time Block |
|   (AWS / GCP /    | - Sponsors/Owners |   Map (>1% exc.)  | - Granular MCP    |   (XPIA/Secrets)  |
|    Foundry)       | - Cond. Access    | - Active Users &  |   Tool Toggle     | - Purview DSPM    |
| - Quarantine /    |   (OBO/App/User)  |   Agent Run-Time  | - Azure AI GW &   |   AI Observability|
|   Block / 30d Del | - riskyAgents     | - OpenTelemetry   |   LiteLLM GW      | - Labels/DLP/IRM  |
| - Policy Templates| - Inactivity Pol. |   -> CloudAppEvts | - A2A & Win365    |   Risky Agents    |
+-------------------+-------------------+-------------------+-------------------+-------------------+
```

1. **Pilar 1 — Registry (Inventario Unificado, Ciclo de Vida y Descubrimiento de Shadow Agents):** Tras la convergencia arquitectónica ejecutada entre abril y mayo de 2026, el **Agent Registry** en `admin.microsoft.com > Agents > All agents > Registry` reemplazó al registro previo de Microsoft Entra como única fuente de verdad del inventario organizacional `[Verificado MS Learn]`. Consolida cuatro orígenes de publicación (*Microsoft agents*, *External partner-built agents*, *Published by your org* y *Shared by creator*) y diez tipologías técnicas (`MCS DA`, `MCS CEA`, `MCS BP`, `Foundry LOB`, `Foundry non-LOB`, `Foundry hosted`, `Agent Builder`, `SharePoint`, `Agent Toolkit` y `Agent instance` instrumentada con Agent 365 SDK) `[Verificado MS Learn]`. Incorpora **Registry Sync** (preview) con **Amazon Bedrock** y **Google Cloud (Vertex AI)**, panel en vivo de **Agents without owners**, cuarentena/bloqueo organizacional, borrado suave (*soft-delete*) con retención de **30 días**, arranque/parada de infraestructura Azure para agentes Foundry, activación mediante **Security Policy Templates** (con asignación automática de licencia) y la vista dedicada **Shadow AI** (`Agents > Shadow AI`) que combina Defender for Endpoint, Intune y Global Secure Access para detectar agentes locales no gestionados (OpenClaw, ChatGPT Desktop, Claude Desktop, Ollama Desktop, Poe Desktop, Claw/ZeroClaw, OpenCode) y desplegar políticas de bloqueo en Intune como `A365 - Block OpenClaw` `[Verificado MS Learn]`.
2. **Pilar 2 — Access Control e Identidad (`Microsoft Entra Agent ID`):** Proporciona en `entra.microsoft.com` una arquitectura de identidad específica para agentes compuesta por cuatro recursos de Microsoft Graph: `agentIdentityBlueprint` (plantilla que define configuración y permisos OAuth delegados heredables), `agentIdentityBlueprintPrincipal` (presencia del blueprint en el tenant), `agentIdentity` (identidad principal de autenticación tipo *service principal*) y `agentUser` (subtipo opcional de cuenta de usuario con `idtyp=user`, buzón, chat de Teams y calendario para *digital workers* o *Autopilots*) `[Verificado MS Learn]`. Establece relaciones administrativas obligatorias (`owner`, `sponsor`, `manager`) con transferencia automática de patrocinio al gerente cuando el sponsor causa baja; extiende **Conditional Access** a los tres patrones OAuth (delegado *On-Behalf-Of*, autónomo *App-only* y *Agent-user*) incluyendo atributos de seguridad personalizados y condición de entorno para **Windows 365 for Agents**; incorpora **ID Protection (`riskyAgents` y `agentRiskDetections`)** con *Learning Mode*; automatiza el ciclo de vida mediante **Access Packages** con expiración y la **Default Agent Identity Inactivity Lifecycle Policy** (60 días notificación, 90 días deshabilitación, 455 días eliminación); bloquea en plataforma más de 50 permisos críticos de Microsoft Graph; e inspecciona el tráfico saliente con **Global Secure Access (Secure Web and AI Gateway)** `[Verificado MS Learn]`.
3. **Pilar 3 — Visualization & Observability:** Ofrece en `admin.microsoft.com > Agents > Overview` métricas ejecutivas de impacto (*Total agents*, *Active users*, *Agent run-time* en horas trabajadas durante 30 días, *Registry sync*, *Agents without owners*, *Unmanaged agents* y tarjetas de *Agents at risk* con recuento agregado de señales High/Medium/Low procedentes de Defender, Entra y Purview, con latencia máxima de hasta 1 hora respecto a los portales de origen) `[Verificado MS Learn]`. Complementa las listas tabulares con el **Agent Map** (`Agents > All Agents > Map`), que agrupa visualmente el parque por clúster de plataforma constructora y permite filtrar por estado, canal, sesiones, horas asistidas y tasa de excepciones (disponible para tenants con menos de 4.000 usuarios/agentes en métricas de uso), y el **Single Agent Map (Preview)**, que traza las conexiones ponderadas entre un agente, sus top 50 usuarios y sus top 50 herramientas, resaltando automáticamente toda herramienta con **tasa de excepción > 1 %** `[Verificado MS Learn]`. Bajo el capó, el Agent 365 SDK emite telemetría OpenTelemetry consultable en `CloudAppEvents` (`InvokeAgent`, `InferenceCall`, `ExecuteToolBySDK`, `ExecuteToolByGateway`, `ExecuteToolByMCPServer`) `[Verificado MS Learn]`.
4. **Pilar 4 — Interoperability:** Conecta de forma gobernada a los agentes con el contexto del trabajo en Microsoft 365 a través de **Work IQ** y el servidor **Work IQ MCP** (disponible en GA con 10 herramientas genéricas dinámicas, reemplazando para nuevos proyectos a los servidores MCP legacy por aplicación como Mail, Calendar o Word) `[Verificado MS Learn]`. Desde `admin.microsoft.com > Agents > Tools`, los administradores gobiernan plugins, *skills*, conectores, servidores MCP alojados por Microsoft, servidores *Bring Your Own (BYO) MCP* y pasarelas **Tools Gateway** conectadas a **Azure AI Gateway (Azure API Management)** o **LiteLLM** `[Verificado MS Learn]`. Incluye **control granular por herramienta individual** dentro de servidores MCP compatibles (permitiendo desactivar herramientas de escritura, borrado o pagos mientras se mantienen activas las de lectura), interoperabilidad multi-agente **Agent-to-Agent (A2A)** autenticada con Entra Agent ID y ejecución aislada en **Windows 365 for Agents** (Cloud PCs dedicados a cargas agénticas administrados por Intune) `[Verificado MS Learn]`.
5. **Pilar 5 — Security & Data Governance Integrada con Microsoft Defender y Microsoft Purview:**
   - **En Microsoft Defender (`security.microsoft.com`):** Centraliza el inventario de seguridad y la postura en `Assets > AI agents` y en la tabla de Advanced Hunting `AgentsInfo` (sucesora oficial de `AIAgentsInfo`, retirada el 1 de julio de 2026), mapeando rutas de exposición desde agentes locales y cloud hacia dispositivos, servidores MCP, identidades y recursos críticos `[Verificado MS Learn]`. Ejecuta detección cuasi en tiempo real de intentos de *jailbreak*, *Indirect Prompt Injection (XPIA)*, reconocimiento de LLM, propagación maliciosa, fuga de secretos y evasión, correlacionándolos en incidentes XDR con respuesta coordinada e interrupción automática cuando confluyen señales de compromiso, además de **Real-time protection (`Settings > Security for AI > Policies & rules > Real-time protection`)** capaz de bloquear en línea invocaciones de herramientas ante *Malicious content propagation*, *Secret exfiltration*, *Evasion techniques* y *Unsafe email domain*, registrando los eventos en `BehaviorInfo` y fragmentos redactados en *Prompt evidence collection* `[Verificado MS Learn]`.
   - **En Microsoft Purview (`purview.microsoft.com`):** Habilita automáticamente auditoría, clasificación de datos y evaluaciones regulatorias en **Compliance Manager** al crear instancias de Agent 365 `[Verificado MS Learn]`. Proporciona la página **DSPM > AI observability** (exclusiva de la versión actual de DSPM, no soportada en *DSPM classic*), exige derechos explícitos `VIEW` y `EXTRACT` a las instancias de agentes para leer archivos cifrados con **Sensitivity Labels** (advirtiendo operativamente que el contenido nuevo generado por Agent 365 no hereda de forma automática la etiqueta del archivo fuente), aplica **Inline DLP** en prompts de Copilot Studio y políticas **DLP** sobre canales Teams, SharePoint, OneDrive y correo, ejecuta por defecto la política **`Risky Agents` (preview) en Insider Risk Management** (compartiendo el nivel de riesgo con DSPM y M365 Admin Center), supervisa ética conductual en **Communication Compliance**, gobierna retención/borrado en **Data Lifecycle Management** y soporta investigaciones legales completas en **Audit** (`XPIADetected`, `JailbreakDetected`) y **eDiscovery** `[Verificado MS Learn]`.

### 3.2 Matriz de Componentes Técnicos, Rutas de Consola e Integraciones

| Componente Técnico | Función Operativa Principal | Consola y Ruta Exacta | Integraciones Clave del Ecosistema |
| :--- | :--- | :--- | :--- |
| **Agent Registry & Lifecycle Engine** | Inventario convergente de agentes primera/tercera parte, activación con plantillas, bloqueo, *soft-delete* (30 días), *Agents without owners* y *Registry Sync* multi-nube `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > All agents > Registry / Requests` | Copilot Studio, Microsoft Foundry, AWS Bedrock, Google Vertex AI, Agent Store `[Verificado MS Learn]` |
| **Shadow AI Discovery & Endpoint Blocking** | Detección de agentes locales no autorizados (OpenClaw, Claude, ChatGPT Desktop, Ollama) y despliegue de políticas de bloqueo Intune (`A365 - Block OpenClaw`) `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > Shadow AI` e `intune.microsoft.com` | Defender for Endpoint, Microsoft Intune, Entra Global Secure Access `[Verificado MS Learn]` |
| **Agent Overview, Agent Map & Single Agent Map** | Telemetría ejecutiva de usuarios activos, *Agent run-time*, señales agregadas *Agents at risk*, clústeres por plataforma y grafo de herramientas con excepción >1 % `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > Overview` y `Agents > All Agents > Map` | Agent 365 SDK (OpenTelemetry), Defender, Entra ID Protection, Purview IRM `[Verificado MS Learn]` |
| **Tools Registry, Work IQ MCP & Tools Gateway** | Gobierno de plugins, *skills*, servidores MCP (Work IQ MCP y BYO), apagado granular de herramientas individuales y conexión de pasarelas Azure AI Gateway y LiteLLM `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > Tools` y `Agents > Settings > Gateways` | Work IQ API, Azure API Management (AI Gateway), LiteLLM, Defender Guardrails `[Verificado MS Learn]` |
| **Microsoft Entra Agent ID & Conditional Access** | Identidades `agentIdentityBlueprint`, `agentIdentity` y `agentUser`, evaluación *Conditional Access* (OBO, App-Only, Agent-User) y bloqueo de permisos Graph críticos `[Verificado MS Learn]`. | `entra.microsoft.com > Agent ID` y `Protection > Conditional Access` | Microsoft Graph, Custom Security Attributes, Windows 365 for Agents `[Verificado MS Learn]` |
| **Entra ID Protection (`riskyAgents`) & ID Governance** | Detección conductual de agentes riesgosos (*Learning Mode*, 8 tipos de evento), *Access Packages*, gestión de *Sponsors* y política de inactividad 60/90/455 días `[Verificado MS Learn]`. | `entra.microsoft.com > ID Protection > Risky agents` e `ID Governance` | Portales `myaccount.microsoft.com` y `myaccess.microsoft.com`, Log Analytics / Sentinel `[Verificado MS Learn]` |
| **Entra Global Secure Access (Secure Web & AI Gateway)** | Proxy SASE para tráfico HTTP, conectores personalizados y conectores MCP de agentes Copilot Studio y dispositivos endpoint `[Verificado MS Learn]`. | `entra.microsoft.com > Global Secure Access` y Power Platform Admin Center | Copilot Studio Environments, Threat Intelligence & Web Content Filtering `[Verificado MS Learn]` |
| **Microsoft Defender Security for AI Agents** | Postura y rutas de ataque (`Assets > AI agents`), caza KQL (`AgentsInfo`, `CloudAppEvents`, `BehaviorInfo`), detección XPIA/jailbreak y bloqueo en tiempo real `[Verificado MS Learn]`. | `security.microsoft.com > Assets > AI agents` y `Settings > Security for AI` | Defender XDR Incidents, Defender for Endpoint, Microsoft Sentinel `[Verificado MS Learn]` |
| **Microsoft Purview Data Security & Compliance for Agents** | *DSPM AI Observability*, respeto de etiquetas (`VIEW`+`EXTRACT`), DLP inline/canales, política *Risky Agents* en IRM, Audit, eDiscovery, DLM y Compliance Manager `[Verificado MS Learn]`. | `purview.microsoft.com > DSPM > AI observability`, `DLP`, `IRM`, `Audit` | Microsoft 365 Admin Center Risk Signals, Defender XDR, Exchange/SharePoint/Teams `[Verificado MS Learn]` |

### 3.3 Hitos Técnicos, Transiciones Arquitectónicas y Consideraciones de Soberanía (2026–2027)

- **Convergencia del Agent Registry (Abril–Mayo 2026):** Las APIs legacy de registro de agentes en Microsoft Graph (`agentRegistry`, `agentCardManifest`, `agentInstance`, `agentCollection`) quedaron deprecadas a favor de las capacidades convergentes de **Microsoft Agent 365** en `admin.microsoft.com` y las APIs de gestión de paquetes Copilot/Agent 365, manteniendo en Entra exclusivamente el plano de identidad y acceso `[Verificado MS Learn]`.
- **Retiro de la tabla `AIAgentsInfo` el 1 de julio de 2026:** En Advanced Hunting de Microsoft Defender XDR, toda regla de detección personalizada, workbook o consulta de caza debe utilizar exclusivamente la tabla **`AgentsInfo`** (empleando `summarize arg_max(Timestamp, *) by AgentId`), dado que `AIAgentsInfo` dejó de ser accesible tras el 1 de julio de 2026 `[Verificado MS Learn]`.
- **Riesgo de membresía dinámica de cuentas `agentUser` (Agosto 2026):** Debido a que `agentUser` es un subtipo del recurso `user` con `userType == "Member"`, las reglas dinámicas amplias heredadas (p. ej. `(user.objectId -ne null) -and (user.userType -eq "Member")`) incluyen inadvertidamente a los agentes usuario, asignándoles licencias y permisos grupales. Es imperativo añadir la cláusula `-and (user.agentIdentityBlueprintId -eq null)` (usando `null` sin comillas, nunca `""`) en los grupos dinámicos exclusivos de humanos `[Verificado MS Learn]`.
- **Transición hacia Work IQ MCP:** Las herramientas MCP específicas por carga de trabajo en vista previa (Mail, Calendar, SharePoint, OneDrive, Teams, User, Word) se conservan únicamente por retrocompatibilidad; todo nuevo desarrollo agéntico debe conectarse al endpoint unificado **Work IQ MCP** `[Verificado MS Learn]`.
- **Diferencia de Residencia de Datos entre Foundry y Agent 365:** Mientras que **Microsoft Foundry** almacena datos y logs en la **región de Azure** del recurso, **Microsoft Agent 365** almacena inventario, analítica y gobierno en la **geografía de almacenamiento del tenant de Microsoft Entra**. Para cargas sujetas a soberanía estricta regional, los recursos individuales de Foundry pueden excluirse (*opt-out*) mediante `agent365Config` `[Verificado MS Learn]`.

### 3.4 Taxonomía Técnica de Agentes, Plantilla de Seguridad Predefinida y Señales de Riesgo Entra

#### Tipologías Oficiales de Agentes Gestionables en Microsoft 365 Admin Center `[Verificado MS Learn]`

| Código / Tipo de Agente | Denominación Oficial | Descripción Arquitectónica y Alcance de Gobierno |
| :--- | :--- | :--- |
| `MCS DA` | Microsoft Copilot Studio Declarative Agent | Agente declarativo creado mediante instrucciones en lenguaje natural en Copilot Studio; publicable por canal con aprobación administrativa `[Verificado MS Learn]`. |
| `MCS CEA` | Microsoft Copilot Studio Custom Engine Agent | Agente de motor personalizado con orquestación precisa, conectores y modelos propios en Copilot Studio; puede generar entradas separadas *Shared by creator* y *Published by your org* `[Verificado MS Learn]`. |
| `MCS BP` | Microsoft Copilot Studio Business Process Agent | Agente orientado a secuencias autónomas de tareas, decisiones y flujos de procesos empresariales `[Verificado MS Learn]`. |
| `Foundry LOB` | Microsoft Foundry Line-of-Business Agent | Agente interno desarrollado sobre Microsoft Foundry para un proceso específico de negocio; soporta *Start and stop* de infraestructura Azure desde M365 Admin Center `[Verificado MS Learn]`. |
| `Foundry non-LOB` | Microsoft Foundry Non-LOB Agent | Agente creado en Microsoft Foundry de propósito transversal no atado a un flujo único de negocio `[Verificado MS Learn]`. |
| `Foundry hosted` | Microsoft Foundry Hosted Agent / Autopilot | Agente alojado y ejecutado dentro de Foundry; permite publicar *Autopilots* con cuenta propia `agentUser` e instrumentar telemetría con Agent 365 SDK `[Verificado MS Learn]`. |
| `Agent Builder` | Copilot Agent Builder Declarative Agent | Agente declarativo ligero creado directamente por usuarios dentro de la experiencia de Microsoft 365 Copilot; soporta múltiples propietarios (`Add/Remove owner`) `[Verificado MS Learn]`. |
| `SharePoint` | SharePoint Declarative Agent | Agente declarativo anclado a bibliotecas y sitios de conocimiento organizacional en SharePoint Online `[Verificado MS Learn]`. |
| `Agent Toolkit` | Microsoft 365 Agents Toolkit Agent | Agente pro-code desarrollado con Microsoft 365 Agents Toolkit (anteriormente Teams Toolkit) `[Verificado MS Learn]`. |
| `Agent instance` | Agent 365 SDK Extended Instance | Instancia extendida mediante el **Microsoft Agent 365 SDK** (incluidos agentes de terceros y *Agent Factories* como Kore.ai, Kasisto o n8n), dotada de identidad Entra, observabilidad completa, cobertura MCP y sistema de plantillas IT `[Verificado MS Learn]`. |

#### Las 12 Políticas Incluidas en la Plantilla Predefinida de Microsoft (Default Security Template) `[Verificado MS Learn]`

Al activar o cargar un agente en `admin.microsoft.com > Agents > All agents`, la **Default template** aplica asignación automática de licencia e invoca doce políticas transversales predefinidas:

1. **Microsoft Entra — Identity Protection:** Detecta amenazas de identidad marcando actividades anómalas que involucran agentes (`riskyAgents`) `[Verificado MS Learn]`.
2. **Microsoft Entra — Network visibility:** Habilita visibilidad de red en Global Secure Access sobre los recursos externos accedidos por el agente `[Verificado MS Learn]`.
3. **Microsoft Entra — Lifecycle management for agents:** Aplica políticas escalables de ciclo de vida e inactividad sobre los Entra Agent IDs `[Verificado MS Learn]`.
4. **SharePoint — Restrict external sharing of sites and content:** Restringe que agentes específicos compartan contenido de sitios SharePoint y OneDrive con invitados externos `[Verificado MS Learn]`.
5. **SharePoint — Access control for sites and OneDrive:** Delimita mediante grupos M365 y grupos de seguridad Entra qué sitios puede consultar el agente (*Restricted Access Control*) `[Verificado MS Learn]`.
6. **SharePoint — Content permissions insights:** Habilita reportes de gobierno de acceso a datos (*DAG reports*) sobre sitios expuestos `[Verificado MS Learn]`.
7. **SharePoint — Agent access insights:** Monitorea qué agentes acceden a cada sitio de SharePoint Online y OneDrive `[Verificado MS Learn]`.
8. **Microsoft Purview — Audit enabled:** Registra trazas completas de auditoría para observabilidad forense `[Verificado MS Learn]`.
9. **Microsoft Purview — Know your data policy:** Aplica clasificación e inspección contra fugas de datos sensibles y *oversharing* `[Verificado MS Learn]`.
10. **Microsoft Purview — AI compliance assessment:** Incorpora el agente a la evaluación continua contra regulaciones de IA en Compliance Manager `[Verificado MS Learn]`.
11. **Microsoft Defender — Investigation and advanced hunting:** Genera alertas cuasi en tiempo real y habilita caza KQL sobre la actividad del agente `[Verificado MS Learn]`.
12. **Microsoft Defender — Real-time protection for Microsoft Agent 365 (Preview):** Inspecciona y bloquea comportamientos maliciosos de herramientas durante el tiempo de ejecución `[Verificado MS Learn]`.

#### Detecciones de Riesgo en Entra ID Protection y Permisos Graph Bloqueados por Diseño `[Verificado MS Learn]`

Microsoft Entra ID Protection evalúa continuamente ocho tipos de eventos de riesgo (`riskEventType`) sobre la actividad autónoma del agente (suprimiendo falsos positivos iniciales mediante **Learning Mode**, salvo `earlyLifeMaliciousActivity`):
- `adminConfirmedAgentCompromised`: Confirmación administrativa explícita de compromiso del agente `[Verificado MS Learn]`.
- `earlyLifeMaliciousActivity`: Agente recién creado que exhibe de inmediato múltiples patrones de ataque `[Verificado MS Learn]`.
- `entraDirectoryReconnaissance`: Operaciones sospechosas de enumeración o reconocimiento de directorio en Entra ID `[Verificado MS Learn]`.
- `failedAccessAttempt`: Intentos fallidos repetidos contra recursos no autorizados (indicativo de *token replay*) `[Verificado MS Learn]`.
- `threatIntelligenceAccount`: Actividad coincidente con indicadores de inteligencia de amenazas internos y externos de Microsoft `[Verificado MS Learn]`.
- `signInSpike`: Incremento abrupto de autenticaciones respecto a la línea base histórica del agente `[Verificado MS Learn]`.
- `suspiciousCredentialUsage`: Adición de credenciales nuevas a un `agentIdentityBlueprint` seguida de su uso efectivo `[Verificado MS Learn]`.
- `unfamiliarResourceAccess`: Acceso a recursos sensibles ajenos al patrón habitual y propósito del agente `[Verificado MS Learn]`.

Adicionalmente, Microsoft Entra bloquea de forma inmutable en plataforma la concesión a identidades de agentes de permisos de alto impacto en Microsoft Graph, incluyendo entre más de 50 permisos prohibidos: `AgentIdentity.Create*`, `AgentIdentityBlueprint.Create*`, `Application.ReadWrite.All`, `AppRoleAssignment.ReadWrite.All`, `BitlockerKey.Read.All`, `Chat.Read.All` / `Chat.ReadWrite.All` (aplicación), `CustomSecAttributeAssignment.ReadWrite.All`, `DelegatedPermissionGrant.ReadWrite.All`, `Directory.AccessAsUser.All`, `Directory.ReadWrite.All`, `Domain.ReadWrite.All`, `EntitlementManagement.ReadWrite.All`, `Files.Read.All` / `Files.ReadWrite.All` (aplicación), `Group.ReadWrite.All`, `GroupMember.ReadWrite.All`, `LifecycleManagement.ReadWrite.All`, `Policy.ReadWrite.*`, `PrivilegedAccess.ReadWrite.*`, `RoleManagement.ReadWrite.Directory`, `Sites.FullControl.All`, `Sites.Read.All` / `Sites.ReadWrite.All` (aplicación), `User.DeleteRestore.All`, `User.EnableDisableAccount.All`, `User.ReadWrite.All` y `UserAuthenticationMethod.ReadWrite.All` `[Verificado MS Learn]`.

#### Ecosistema de Partners Preintegrados, AI Teammates y Agent Factories `[Verificado MS Learn]`

Microsoft Agent 365 opera como plano de control abierto para agentes SaaS empresariales (**ServiceNow, Workday, Salesforce, SAP, Adobe**) y distingue en su catálogo de lanzamiento dos modelos de integración directa sin desarrollo personalizado `[Verificado MS Learn]`:

| Categoría de Ecosistema | Ejemplos Oficiales Verificados | Modelo de Identidad, Observabilidad y Gobierno |
| :--- | :--- | :--- |
| **Ready-to-deploy Partner Agents** | **Adobe** (Marketing Agent), **Box**, **Canva**, **Celonis** (gemelo digital de procesos y ROI), **Achievers**, **Cornerstone**, **Coursera**, **Figma**, **Gloat**, **Lucid**, **Miro** (con Work IQ), **Rox**, **Sophos**, **Zoho**, además de conectores empresariales **ServiceNow**, **Workday** y **Salesforce** `[Verificado MS Learn]`. | Desplegables desde `admin.microsoft.com > Agents > All agents > Registry`, registrados en el inventario unificado y con telemetría completa de observabilidad hacia Purview y Defender `[Verificado MS Learn]`. |
| **AI Teammates (Programa Frontier)** | **Genspark** (*super agent* multi-modelo con Work IQ y aprobación *human-in-the-loop*), **Egnyte** (gobierno de contenido), **Manus**, **Zendesk** y **Zensai** `[Verificado MS Learn]`. | Participan con acceso propio (`agentUser`) en conversaciones 1:1 y grupales de Microsoft Teams bajo políticas de Entra, Purview y Defender `[Verificado MS Learn]`. |
| **Agent Factories (Fábricas de Agentes)** | **Kasisto (KAI)** (banca y servicios financieros regulados, con Work IQ), **Kore.ai** (flujos conversacionales LOB), **n8n** (automatización de flujos con Work IQ) y **NVIDIA** `[Verificado MS Learn]`. | Cada agente creado en la fábrica recibe automáticamente un **Microsoft Entra Agent ID** gobernado, aparece en el Agent Registry y hereda controles de identidad, cumplimiento y observabilidad desde su nacimiento `[Verificado MS Learn]`. |
| **Sincronización Multi-Nube y Marcos Open-Source** | **Amazon Bedrock**, **Google Cloud (Vertex AI / Gemini Enterprise Agent Platform)** y agentes SDK sobre **LangChain, CrewAI, OpenAI, Anthropic, Cursor, Perplexity y Vercel** `[Verificado MS Learn]`. | Descubrimiento sin código mediante **Registry Sync** (Bedrock / Google Cloud) o incorporación individual con **Agent 365 CLI / Agent 365 SDK** emitiendo telemetría OpenTelemetry `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

El gobierno de Microsoft Agent 365 exige una segregación estricta de funciones entre administración del plano de control en M365, gobierno de identidades y acceso condicional en Entra, operaciones de amenazas en Defender, protección de datos en Purview y patrocinio responsable por las unidades de negocio. De acuerdo con Microsoft Learn, el rol **Global Administrator** debe reservarse exclusivamente para escenarios de emergencia o para operaciones puntuales que aún lo exigen técnicamente (como la aceptación inicial de términos de Agent 365 o la conexión inicial de **Azure AI Gateway** y **LiteLLM** en `Agents > Settings > Gateways`, donde `AI Administrator` no está soportado) `[Verificado MS Learn]`. Asimismo, un `AI Administrator` NO tiene permisos para crear políticas de Conditional Access ni Access Packages en Entra, y un `Global Administrator` por sí solo NO puede abrir alertas de Purview Insider Risk Management sin contar con el rol `IRM Analyst` o `IRM Investigator` `[Verificado MS Learn]`.

### 4.1 Matriz RBAC Recomendada de Mínimo Privilegio y Estrategia PIM / JIT

| Rol Operativo / Persona | Rol(es) Oficial(es) en Entra / Defender / Purview | Permisos Clave y Alcance Técnico | Estrategia PIM / JIT Recomendada | Segregación de Funciones (SoD) |
| :--- | :--- | :--- | :--- | :--- |
| **1. AI Administrator** | `AI Administrator` (Entra ID) `[Verificado MS Learn]` | Autoridad tenant-wide en `admin.microsoft.com > Agents` para ver insights, Agent Map, aprobar activaciones, aplicar *Policy Templates*, gestionar ciclo de vida, aprobar servidores MCP y otorgar consentimiento a solicitudes MCP `[Verificado MS Learn]`. | **Elegible en PIM**; activación JIT máximo `4 horas`, MFA resistente al phishing (Passkey/FIDO2), justificación con ticket y aprobación de par `[Decisión / Propuesta Editorial]`. | No puede crear políticas de *Conditional Access* ni *Access Packages* en Entra, ni conectar gateways Azure AI / LiteLLM `[Verificado MS Learn]`. |
| **2. Agent Registry Admin** | `AI Administrator` (para acciones) + `AI Reader` (para monitoreo diario continuo) `[Verificado MS Learn]` | Operación cotidiana del **Agent Registry**: revisión de solicitudes pendientes, inventario multi-nube, gestión de *Agents without owners*, fijado en Agent Store, exportación CSV y carga de paquetes `.zip` `[Verificado MS Learn]`. | `AI Reader` asignado activo permanente para visibilidad sin riesgo; elevación JIT a `AI Administrator` por `2 horas` solo al ejecutar cambios en el registro `[Decisión / Propuesta Editorial]`. | Separado de la aprobación de riesgos de identidad (`Security Admin`) y de las investigaciones de datos (`Purview Admin`) `[Decisión / Propuesta Editorial]`. |
| **3. Entra Agent ID Admin** | `Agent ID Administrator` + `Conditional Access Administrator` + `Lifecycle Workflows Administrator` `[Verificado MS Learn]` | Gestión de `agentIdentityBlueprint`, `agentIdentity` y `agentUser`, configuración de *Conditional Access* para agentes, *Access Packages* y políticas de ciclo de vida / inactividad en `entra.microsoft.com` `[Verificado MS Learn]`. | **Elegible en PIM**; activación JIT máximo `4 horas` con *Authentication Context* exigiendo PAW/dispositivo conforme Intune y aprobación dual para cambios CA `[Decisión / Propuesta Editorial]`. | No despliega agentes en canales de negocio ni modifica reglas DLP/IRM en Purview `[Decisión / Propuesta Editorial]`. |
| **4. Security Admin** | `Security Administrator` (Entra ID / Microsoft Defender Unified RBAC) `[Verificado MS Learn]` | Habilitación de *Security for AI* y conector M365 en Defender, creación de reglas de bloqueo en *Real-time protection*, gestión de `Risky Agents` en Entra ID Protection y bloqueo de *Shadow AI* con `Intune Administrator` `[Verificado MS Learn]`. | **Elegible en PIM**; activación JIT máximo `4 horas` con MFA FIDO2 y registro de cambio para reglas de bloqueo en producción `[Decisión / Propuesta Editorial]`. | No actúa como *Owner* ni *Sponsor* de agentes de líneas de negocio para evitar conflicto de interés `[Decisión / Propuesta Editorial]`. |
| **5. Purview Data Security AI Admin** | `Compliance Administrator` / `Data Security AI Admin` + grupo de rol Purview `Insider Risk Management Investigators` / `Analysts` `[Verificado MS Learn]` | Operación de `DSPM > AI observability`, políticas DLP inline y por canal sobre instancias de agentes, investigación de alertas `Risky Agents` en IRM, Communication Compliance, DLM y búsquedas Audit/eDiscovery `[Verificado MS Learn]`. | Roles de lectura analítica activos bajo seudonimización por defecto; elevación JIT (`4 horas`) para modificar políticas DLP o exportar evidencias eDiscovery con aprobación legal `[Decisión / Propuesta Editorial]`. | Ni siquiera el `Global Administrator` accede a alertas IRM de agentes sin pertenecer explícitamente a `IRM Analyst` o `IRM Investigator` `[Verificado MS Learn]`. |
| **6. Agent Sponsor / Business Owner** | Relación administrativa `sponsor` y `owner` sobre objetos Entra Agent ID (sin rol de directorio privilegiado) `[Verificado MS Learn]` | Responsable humano de negocio en `myaccount.microsoft.com` y `myaccess.microsoft.com`: solicita/renueva *Access Packages* del agente, responde notificaciones de inactividad (60 días) y habilita/deshabilita sus agentes `[Verificado MS Learn]`. | Cuenta estándar protegida por MFA resistente al phishing; el `sponsor` no puede restaurar agentes deshabilitados/eliminados por política (requiere `owner` o admin) `[Verificado MS Learn]`. | Un agente crítico en producción debe tener al menos dos *Sponsors* humanos distintos del desarrollador (*maker*) `[Decisión / Propuesta Editorial]`. |
| **7. SOC L2/L3** | `Security Operator` (Entra / Defender XDR) `[Verificado MS Learn]` | Triaje de incidentes XDR con entidades de agentes, caza avanzada KQL (`AgentsInfo`, `CloudAppEvents`, `BehaviorInfo`, `AlertEvidence`) y acciones de respuesta sobre `Risky Agents` (*Confirm compromise*, *Disable*) `[Verificado MS Learn]`. | Activo en turno SOC para `Security Reader`; elevación PIM rápida (`8 horas` de guardia sin bloqueador manual pero con MFA fuerte) a `Security Operator` `[Decisión / Propuesta Editorial]`. | Puede contener/deshabilitar un agente comprometido, pero no modificar plantillas globales ni aprobar servidores MCP `[Decisión / Propuesta Editorial]`. |
| **8. GRC / AI Ethics** | `AI Reader` + `Security Reader` + `Compliance Manager Assessor` / `Reports Reader` `[Verificado MS Learn]` | Visibilidad integral de solo lectura sobre inventario Agent 365, riesgos agregados, métricas de adopción y ejecución de evaluaciones regulatorias de IA en Purview Compliance Manager `[Verificado MS Learn]`. | Asignación permanente de solo lectura revisada trimestralmente mediante Entra Access Reviews `[Decisión / Propuesta Editorial]`. | Estricta segregación de auditoría: cero permisos de escritura (`Install`, `Approve`, `Block` o edición de políticas) `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

### D-01: Triaje Matutino de la Tarjeta Agents at Risk y Señales Agregadas Multi-Plataforma
- **Alineación Normativa:** NIST CSF 2.0 `DE.CM-03` / NIST AI RMF `MEASURE-2.7` / OWASP Agentic `ASI10:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Identificar y priorizar todos los agentes con señales de riesgo activas detectadas en las últimas 24 horas a través de Microsoft Defender, Microsoft Entra y Microsoft Purview `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Overview` (tarjeta **Agents at risk**) y `Agents` > `All agents` > `Registry` (mosaico **Agents at risk** y columna **Risks**) `[Verificado MS Learn]`.
- **Rol Responsable:** `Agent Registry Admin` (`AI Reader`) en coordinación con `SOC L2/L3` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Acceder a `admin.microsoft.com > Overview` e inspeccionar la tarjeta **Agents at risk**, que destaca los tres agentes con mayor recuento agregado de señales entre plataformas Microsoft y terceros conectados `[Verificado MS Learn]`.
  2. Seleccionar **View agents** para abrir `Agents > All agents > Registry` prefiltrado y ordenado por nivel de riesgo (considerando que el conteo en M365 Admin Center puede presentar hasta 1 hora de desfase respecto a los portales de seguridad) `[Verificado MS Learn]`.
  3. Hacer clic sobre el contador numérico de la columna **Risks** en cada agente con severidad **High** o **Medium** para desplegar el panel **Risk details**, verificando la descripción individual, el conteo de **Occurrences** y la agrupación por instancia `[Verificado MS Learn]`.
  4. Seguir los *deep links* de atribución de plataforma hacia Microsoft Defender, Microsoft Entra o Microsoft Purview IRM según permisos RBAC y abrir ticket de contención prioritaria para toda señal High en menos de 30 minutos `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación CSV fechada de la vista filtrada de agentes en riesgo y tickets de seguimiento vinculados en ITSM/SecOps `[Decisión / Propuesta Editorial]`.

### D-02: Investigación y Respuesta a Alertas Cuasi en Tiempo Real y Bloqueos Runtime en Microsoft Defender
- **Alineación Normativa:** NIST CSF 2.0 `DE.AE-02`, `RS.MI-01` / OWASP Agentic `ASI01:2026`, `ASI02:2026` / MITRE ATLAS `AML.T0051.001` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Contener ataques activos dirigidos a agentes gestionados (intentos de *Indirect Prompt Injection / XPIA*, *jailbreak*, propagación de contenido malicioso, exfiltración de secretos o dominios de correo inseguros) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Incidents & alerts` > `Incidents` y `Assets` > `AI agents` > pestaña `Agents` (columna **Active alerts**) `[Verificado MS Learn]`.
- **Rol Responsable:** `SOC L2/L3` (`Security Operator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Filtrar la cola unificada de incidentes en Defender XDR por entidades de tipo agente IA (recordando que para agentes Foundry solo están soportados los agentes publicados, no los de *playground*) y revisar el grafo de incidente (*Attack Story* y *Blast Radius*) `[Verificado MS Learn]`.
  2. Inspeccionar la evidencia redactada del prompt (*Prompt evidence collection*) adjunta a la alerta para distinguir pruebas benignas de ataques reales XPIA, reconocimiento de LLM o evasión codificada `[Verificado MS Learn]`.
  3. Correlacionar en Advanced Hunting las tablas `AlertInfo`, `AlertEvidence`, `BehaviorInfo` y `CloudAppEvents` para verificar si una regla de *Real-time protection* o *Prompt Shields* bloqueó la acción o si el agente ejecutó invocaciones downstream `[Verificado MS Learn]`.
  4. Si se confirma manipulación maliciosa, bloquear el agente en `admin.microsoft.com` o deshabilitar su identidad en Entra y escalar de inmediato al Playbook `AH-01` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Expediente de incidente cerrado/clasificado en Defender XDR con comentarios de triaje y consulta KQL adjunta `[Verificado MS Learn]`.

### D-03: Revisión Diaria del Reporte Risky Agents en Microsoft Entra ID Protection
- **Alineación Normativa:** NIST CSF 2.0 `DE.CM-03`, `PR.AA-05` / OWASP Agentic `ASI03:2026` / MITRE ATT&CK `T1078.004` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Detectar y remediar compromisos de identidad en agentes autónomos (picos de inicio de sesión, uso sospechoso de credenciales nuevas en blueprints, acceso a recursos no familiares o reconocimiento de directorio) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Identity Protection` > `Risky agents` y `Risk detections` > pestaña `Agent detections` `[Verificado MS Learn]`.
- **Rol Responsable:** `SOC L2/L3` / `Security Admin` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Filtrar el reporte **Risky agents** por nivel de riesgo `High` y `Medium` (teniendo en cuenta que en flujos delegados *On-Behalf-Of* el riesgo se atribuye al usuario humano y este reporte evalúa actividad autónoma del agente fuera de *Learning Mode*) `[Verificado MS Learn]`.
  2. Analizar en la pestaña `Agent detections` los eventos `riskEventType` de los últimos 90 días (`earlyLifeMaliciousActivity`, `entraDirectoryReconnaissance`, `suspiciousCredentialUsage`, `unfamiliarResourceAccess`, `signInSpike`, `failedAccessAttempt`, `threatIntelligenceAccount`) `[Verificado MS Learn]`.
  3. Contactar al `Sponsor` u `Owner` registrado en los detalles del agente si se sospecha un cambio operativo no documentado `[Verificado MS Learn]`.
  4. Ejecutar **Confirm compromise** (que eleva el riesgo a High y dispara el bloqueo automático por Conditional Access) o **Disable** ante actividad maliciosa confirmada; usar **Confirm safe** (para suprimir falsos positivos similares) o **Dismiss risk** (para positivos benignos puntuales) solo tras validación documentada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registros de auditoría de Entra ID y entradas en `agentRiskDetections` (retenidas hasta 90 días en el portal y exportadas al SIEM) `[Verificado MS Learn]`.

### D-04: Monitoreo de Alertas de la Política Risky Agents en Purview Insider Risk Management
- **Alineación Normativa:** NIST CSF 2.0 `DE.CM-03`, `PR.DS-01` / OWASP Agentic `ASI06:2026` / MITRE ATLAS `AML.T0057` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Supervisar interacciones de agentes con datos confidenciales, generación de respuestas sensibles, prompts riesgosos o navegación hacia sitios web de riesgo `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Solutions` > `Insider Risk Management` > `Alerts` (política **Risky Agents** y plantilla **Risky AI usage**) `[Verificado MS Learn]`.
- **Rol Responsable:** `Purview Data Security AI Admin` (miembro de `IRM Investigators` o `IRM Analysts`, sin ámbito de unidad administrativa ya que las AU no están soportadas para alertas de agentes) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Revisar en la cola de alertas de IRM todas las detecciones nuevas generadas por la política predeterminada **Risky Agents** sobre agentes de Copilot Studio, Microsoft Foundry y P4AI SDK `[Verificado MS Learn]`.
  2. Inspeccionar las cuatro señales nativas de la política (*Risky prompts*, *Agents generating sensitive responses*, *Agents accessing sensitive data* y *Accessing risky websites*) `[Verificado MS Learn]`.
  3. Evaluar la secuencia de acceso a materiales protegidos (considerando que para usuarios invitados solo se muestran indicadores de tipos de información sensible y no el cuerpo completo de prompts/respuestas) `[Verificado MS Learn]`.
  4. Confirmar la alerta, abrir caso formal en IRM cuando proceda y verificar que el nivel de riesgo actualizado fluya hacia `DSPM > AI observability` y `admin.microsoft.com` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de triaje de alertas en Purview Insider Risk Management y sincronización del score de riesgo hacia DSPM `[Verificado MS Learn]`.

### D-05: Evaluación y Aprobación Gobernada de Solicitudes de Activación de Agentes
- **Alineación Normativa:** NIST CSF 2.0 `GV.RR-02`, `PR.AA-05` / NIST AI RMF `GOVERN-1.3` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Garantizar que ningún agente personalizado o de terceros pase a producción sin revisión de arquitectura, asignación de audiencia mínima y aplicación obligatoria de una **Security Policy Template** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `All agents` > pestaña `Requests` (estado **Allow activation**) `[Verificado MS Learn]`.
- **Rol Responsable:** `AI Administrator` (elevado vía PIM) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Seleccionar cada solicitud pendiente en la pestaña **Requests** y auditar su descripción, publicador, `Owner`, `Sponsor` de negocio, orígenes de datos conectados (*Embedded knowledge* o *Fine-tuned models*) y herramientas declaradas `[Verificado MS Learn]`.
  2. Abrir el asistente de activación y acotar la audiencia exclusivamente a los usuarios solicitantes y grupos de seguridad requeridos (evitando *Everyone* salvo agentes corporativos transversales aprobados por el comité de IA) `[Verificado MS Learn]`.
  3. Aplicar la plantilla **Default template** (con sus 12 políticas de Entra, SharePoint, Purview y Defender más asignación automática de licencia) o una **Custom template** con restricciones adicionales de compartición externa `[Verificado MS Learn]`.
  4. Revisar rigurosamente los permisos OAuth solicitados, otorgar *Grant admin consent* si cumplen mínimo privilegio y pulsar **Finish** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Evento de activación y consentimiento administrativo en el Unified Audit Log de Microsoft Purview y Microsoft Entra `[Verificado MS Learn]`.

### D-06: Revisión de Solicitudes de Servidores MCP Remotos y Acceso a Plugins
- **Alineación Normativa:** NIST CSF 2.0 `GV.SC-07`, `PR.AA-05` / OWASP Agentic `ASI02:2026`, `ASI04:2026` / MITRE ATLAS `AML.T0043` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Impedir la incorporación de servidores **Model Context Protocol (MCP)** o plugins no verificados que expongan herramientas destructivas o canales de exfiltración `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Tools` > pestaña `Requests (preview)` `[Verificado MS Learn]`.
- **Rol Responsable:** `AI Administrator` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Inspeccionar las solicitudes pendientes tanto de registro de servidores MCP remotos por desarrolladores como de usuarios que pulsaron *Request access* sobre plugins bloqueados por política `[Verificado MS Learn]`.
  2. Validar el publicador, endpoint de transporte, alcances OAuth requeridos en Entra y el catálogo exacto de herramientas declaradas por el servidor MCP `[Verificado MS Learn]`.
  3. Confirmar que el servidor MCP transite por **Azure AI Gateway** o **LiteLLM** cuando exponga sistemas críticos o APIs externas `[Verificado MS Learn]`.
  4. Si se aprueba un servidor MCP con capacidades mixtas, acceder inmediatamente después a `Agents > Tools > Registry > [MCP Server] > Tools` y deshabilitar (`Disabled`) las herramientas individuales de alto riesgo (escritura masiva, eliminación o pagos) antes de que se propague a Copilot Studio (hasta 30 minutos) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de solicitudes aprobadas/rechazadas en `Agents > Tools` y registro de consentimiento OAuth en Entra ID `[Verificado MS Learn]`.

### D-07: Remediación Diaria de Agentes Huérfanos (Agents Without Owners)
- **Alineación Normativa:** NIST CSF 2.0 `GV.RR-02`, `ID.AM-02` / NIST AI RMF `GOVERN-2.1` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Eliminar brechas de responsabilidad (*accountability gaps*) generadas en tiempo real cuando los creadores de agentes compartidos son eliminados de la organización `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Overview` o `Agents` > `All agents` > `Registry` (tarjeta de filtro **Agents without owners**) `[Verificado MS Learn]`.
- **Rol Responsable:** `Agent Registry Admin` (`AI Administrator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Hacer clic en la tarjeta **Agents without owners** (cuyo contador se actualiza automáticamente en tiempo real ante cada *hard delete* de usuario en Entra ID) para aislar los agentes compartidos sin propietario `[Verificado MS Learn]`.
  2. Cruzar cada agente con su volumen de sesiones de los últimos 30 días y su departamento origen `[Decisión / Propuesta Editorial]`.
  3. Si el agente respalda un flujo vigente de negocio, ejecutar **Assign a new owner** (y añadir un propietario secundario en agentes *Agent Builder* mediante **Add an owner**) `[Verificado MS Learn]`.
  4. Si no existe patrocinador válido o el agente carece de uso legítimo, aplicar **Block** inmediato o **Delete agent** (*soft-delete* con ventana de recuperación de 30 días) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Conteo diario de la tarjeta **Agents without owners** mantenido en `0` al cierre de guardia y traza de auditoría de reasignación o borrado `[Decisión / Propuesta Editorial]`.

### D-08: Supervisión de Eventos de Bloqueo DLP sobre Prompts e Interacciones de Agentes
- **Alineación Normativa:** NIST CSF 2.0 `PR.DS-01`, `DE.CM-03` / OWASP LLM `LLM02:2025` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Detectar intentos de procesamiento o compartición de información regulada (PII, PCI, propiedad intelectual) en interacciones humano-agente y agente-humano, así como diagnosticar evaluaciones DLP diferidas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Data Loss Prevention` > `Alerts` y `DSPM` > `Activity explorer` > pestaña `AI activities` `[Verificado MS Learn]`.
- **Rol Responsable:** `Purview Data Security AI Admin` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Revisar las alertas DLP disparadas por políticas que incluyen explícitamente instancias de agentes o grupos de seguridad de agentes sobre Teams, SharePoint, OneDrive y Exchange, así como **Inline DLP** en prompts de Copilot Studio `[Verificado MS Learn]`.
  2. Notificar proactivamente al `Agent Owner` cuando una política DLP bloquee a su agente (dado que la instancia del agente no es consciente por sí misma de la acción de bloqueo DLP y los flujos posteriores pueden fallar silenciosamente) `[Verificado MS Learn]`.
  3. Verificar mediante búsqueda en registros de auditoría que no existan tasas anómalas del bitmask `DLPEvaluationDeferred` (`1=Prompt`, `2=Response`, `4=Grounding`, `8=WebGrounding`) ni errores `Timeout` / `Service Unavailable` en `DLPEvaluationDeferredReason` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Alertas DLP resueltas en Purview y notificación documentada al propietario del agente afectado `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Descubrimiento y Bloqueo de Agentes Locales No Gestionados (Shadow AI)
- **Alineación Normativa:** NIST CSF 2.0 `ID.AM-02`, `RS.MI-01` / OWASP Agentic `ASI05:2026`, `ASI10:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Identificar agentes autónomos y asistentes de escritorio instalados sin aprobación en endpoints corporativos y aplicar controles de bloqueo mediante Microsoft Intune `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Shadow AI` y `https://intune.microsoft.com` > `Devices` > `Configuration` `[Verificado MS Learn]`.
- **Rol Responsable:** `Security Admin` en conjunto con `Intune Administrator` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Abrir la página **Shadow AI (Frontier)** y revisar las detecciones sobre el catálogo soportado (**OpenClaw, ChatGPT Desktop, Ollama Desktop, Poe Desktop, Claw/ZeroClaw, OpenCode, Claude Desktop**) `[Verificado MS Learn]`.
  2. Inspeccionar en el panel **Details** los mosaicos **Detections** (dispositivos y usuarios únicos), **Total traffic** (FQDNs únicos, peticiones, volumen enviado/recibido vía Global Secure Access) y la pestaña **Detected devices** (nombre, modelo, sistema operativo y *Last Seen*) `[Verificado MS Learn]`.
  3. Para agentes locales no autorizados con bloqueo soportado (como OpenClaw), ir a **Security policies** > **Block** > **Apply Policies** para generar y propagar automáticamente la política Intune `A365 - Block OpenClaw` (15 minutos a 8 horas de convergencia en equipos Windows inscritos) `[Verificado MS Learn]`.
  4. Para asistentes locales con detección pero sin bloqueo directo aún en la página Shadow AI, aplicar políticas complementarias de AppLocker / WDAC en Intune y reglas de filtrado FQDN en Global Secure Access `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Estado de aplicación de la política `A365 - Block OpenClaw` en Microsoft Intune y reducción semanal de endpoints con agentes Shadow AI activos `[Verificado MS Learn]`.

### S-02: Evaluación de Postura de Seguridad y Rutas de Exposición de Agentes en Microsoft Defender
- **Alineación Normativa:** NIST CSF 2.0 `ID.RA-01`, `PR.IP-01` / NIST AI RMF `MAP-4.1` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Remediar configuraciones inseguras, autenticación débil y rutas de ataque desde agentes hacia activos críticos de nube o datos sensibles `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Assets` > `AI agents` > pestaña `Agents` > `[Seleccionar Agente]` > `Open Agent page` > `Security recommendations` `[Verificado MS Learn]`.
- **Rol Responsable:** `Security Admin` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Filtrar el inventario de **AI agents** en Defender por **Risk level** (`High`, `Medium`) y revisar las columnas **Risk indicators** y **Recommendations** `[Verificado MS Learn]`.
  2. Abrir el mapa de relaciones de superficie de ataque en la página del agente (dispositivo donde corre el agente, servidores MCP conectados, identidades asociadas y recursos cloud AWS/Azure/M365 alcanzables) para priorizar según criticidad del activo `[Verificado MS Learn]`.
  3. Verificar que los agentes con herramientas sensibles no operen tras **Power Platform Firewall** en modo activo de una forma que bloquee las acciones administrativas desde M365 Admin Center sin procedimiento alternativo documentado `[Verificado MS Learn]`.
  4. Extraer los **Remediation steps** y asignarlos con SLA de 7 días para severidad alta a los equipos propietarios en Copilot Studio, Microsoft Foundry o endpoints `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Tendencia semanal de recomendaciones cerradas en Defender Security for AI y consulta de validación sobre `AgentsInfo` `[Verificado MS Learn]`.

### S-03: Revisión de Sobrescompartición y Riesgos de Datos en Purview DSPM AI Observability
- **Alineación Normativa:** NIST CSF 2.0 `ID.RA-01`, `PR.DS-01` / NIST AI 600-1 *Data Privacy* / OWASP LLM `LLM02:2025` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Mitigar riesgos de *data oversharing*, exfiltración y brechas de cobertura de etiquetado o DLP en instancias activas de agentes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Solutions` > `DSPM` (versión actual, no *DSPM classic*) > `AI observability` `[Verificado MS Learn]`.
- **Rol Responsable:** `Purview Data Security AI Admin` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Analizar en **AI observability** el listado de todos los agentes con actividad en los últimos 30 días, priorizados por el nivel de riesgo calculado por Insider Risk Management `[Verificado MS Learn]`.
  2. Examinar las tres categorías principales de actividad riesgosa (*oversharing*, *exfiltration* y *unethical behavior*) y abrir la ficha individual de los agentes críticos (verificando estado Entra-enabled, fecha de creación, `owner`, `agent user ID` y agente padre) `[Verificado MS Learn]`.
  3. Confirmar que los archivos confidenciales accedidos por instancias de agentes hayan sido explícitamente compartidos con ellas y que las etiquetas con cifrado otorguen expresamente `VIEW` y `EXTRACT` a las instancias autorizadas (ya que *All authenticated users* no es suficiente) `[Verificado MS Learn]`.
  4. Aplicar las recomendaciones integradas de Purview y coordinar con SharePoint Admins la restricción de sitios sensibles (*Restricted Access Control* en SharePoint Advanced Management) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/reporte de postura en `DSPM > AI observability` y registro de políticas remediales aplicadas `[Verificado MS Learn]`.

### S-04: Caza Proactiva de Amenazas (Threat Hunting) sobre Telemetría Agéntica e Invocaciones MCP
- **Alineación Normativa:** NIST CSF 2.0 `DE.AE-02`, `DE.CM-03` / OWASP Agentic `ASI01:2026`, `ASI02:2026` / MITRE ATLAS `AML.T0051`, `AML.T0054` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Detectar patrones anómalos de ejecución de herramientas, intentos sutiles de XPIA en documentos de *grounding* y cadenas laterales agente-a-agente que no hayan disparado bloqueos preventivos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com` > `Investigation & response` > `Hunting` > `Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** `SOC L2/L3` (*Threat Hunter*) `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Ejecutar el paquete semanal de consultas KQL correlacionando `AgentsInfo` (último snapshot con `arg_max`), `CloudAppEvents` (`InvokeAgent`, `InferenceCall`, `ExecuteToolBySDK`, `ExecuteToolByGateway`, `ExecuteToolByMCPServer`) y `BehaviorInfo` `[Verificado MS Learn]`.
  2. Cruzar registros del Unified Audit Log (`CopilotInteraction`, `ConnectedAIAppInteraction`) donde `AccessedResources` contenga `XPIADetected == true` o `Messages` contenga `JailbreakDetected == true` `[Verificado MS Learn]`.
  3. Auditar en `NetworkAccessGenerativeAIInsights` cualquier tráfico no autorizado hacia dominios externos de modelos o herramientas MCP fuera de pasarela `[Verificado MS Learn]`.
  4. Promover los hallazgos recurrentes a reglas personalizadas de bloqueo en `Settings > Security for AI > Policies & rules > Real-time protection` o *Custom Detection Rules* en Defender XDR `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora semanal de *Threat Hunting* con resultados de consultas KQL y nuevas reglas promovidas `[Decisión / Propuesta Editorial]`.

### S-05: Gobierno Semanal de Plugins, Skills, Servidores MCP y Pasarelas Tools Gateway
- **Alineación Normativa:** NIST CSF 2.0 `PR.AA-05`, `GV.SC-07` / OWASP Agentic `ASI02:2026`, `ASI04:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Auditar la higiene del catálogo de herramientas disponibles para agentes y asegurar que toda invocación MCP transite por gateways protegidos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Tools` > `Registry / Plugins` y `Agents` > `Settings` > `Gateways` `[Verificado MS Learn]`.
- **Rol Responsable:** `AI Administrator` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Revisar en `Agents > Settings > Agent and plugin access` que solo permanezcan habilitadas las categorías de publicadores aprobadas (*Microsoft*, *your organization*, *certified external publishers*) `[Verificado MS Learn]`.
  2. Verificar el estado operativo de las conexiones en `Agents > Settings > Gateways` (**Azure AI Gateway** con política *Agent 365 tool threat protection* activa bajo token delegado y **LiteLLM** con `litellm-enterprise-api` y *Agent 365 Guardrails*) `[Verificado MS Learn]`.
  3. Auditar en `Agents > Tools > Registry` los servidores MCP activos y verificar los selectores individuales (`Enabled`/`Disabled`) de herramientas críticas, confirmando además que ningún proyecto nuevo utilice servidores MCP legacy por aplicación en lugar de **Work IQ MCP** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal de herramientas y servidores MCP aprobados y estado de salud de gateways `[Decisión / Propuesta Editorial]`.

### S-06: Análisis Visual de Topología y Tasa de Excepciones (>1 %) en Agent Map y Single Agent Map
- **Alineación Normativa:** NIST CSF 2.0 `ID.AM-02`, `DE.CM-03` / OWASP Agentic `ASI08:2026 Cascading Failures` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Detectar degradación operativa, fallos recurrentes en herramientas invocadas y concentraciones de agentes no gestionados por plataforma `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `All Agents` > `Map` y vista **All connections** (*Single Agent Map*) `[Verificado MS Learn]`.
- **Rol Responsable:** `Agent Registry Admin` (`AI Administrator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Abrir **Agent Map**, revisar los cuatro indicadores maestros (*Total agents*, *Agents at risk*, *Agents without owners*, *Unmanaged agents*) y aplicar el filtro **Usage > Exception rate: Has exceptions (>0%)** `[Verificado MS Learn]`.
  2. Para los agentes críticos de negocio con excepciones, abrir **All connections** en **Single Agent Map (preview)** (ventana de 7 y 30 días) e identificar las líneas resaltadas hacia herramientas con **tasa de excepción > 1 %** entre los top 50 usuarios y top 50 herramientas `[Verificado MS Learn]`.
  3. Notificar al `Owner` técnico para corregir credenciales expiradas, esquemas MCP rotos o *throttling* de APIs antes de que provoquen fallos en cascada `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación Excel desde Agent Map y tickets correctivos por herramientas con excepción >1 % `[Verificado MS Learn]`.

### S-07: Supervisión de Conducta y Cumplimiento Regulatorio en Purview Communication Compliance
- **Alineación Normativa:** NIST CSF 2.0 `GV.OC-03`, `DE.CM-03` / NIST AI 600-1 *Harmful Bias & Toxic Content* / OWASP Agentic `ASI09:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Revisar alertas de comunicaciones inapropiadas, acoso, filtración regulatoria o respuestas no éticas en interacciones agente-humano y humano-agente `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Solutions` > `Communication Compliance` > `Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** `Purview Data Security AI Admin` / Oficial de Cumplimiento `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Revisar las coincidencias semanales en políticas de IA generativa sobre canales Microsoft Teams y Exchange Online que incluyan instancias de Agent 365 `[Verificado MS Learn]`.
  2. Clasificar cada alerta bajo controles de seudonimización por defecto, verificando si una desviación responde a mal uso del usuario o a desalineación de las instrucciones del sistema (`Instructions`) del agente `[Verificado MS Learn]`.
  3. Escalar ajustes de *system prompt* o barandillas de seguridad al propietario del agente cuando se observe generación impropia `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro auditable de revisiones y resoluciones en Purview Communication Compliance `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Conciliación Multi-Nube (Registry Sync con AWS Bedrock, Google Vertex AI y Foundry)
- **Alineación Normativa:** NIST CSF 2.0 `ID.AM-02`, `GV.SC-04` / NIST AI RMF `MAP-3.4` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Garantizar paridad del 100 % entre los agentes desplegados en nubes de desarrollo y el inventario gobernado en Microsoft Agent 365, eliminando la brecha de *Unmanaged agents* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Overview` (métrica **Registry sync**) y `Agents` > `All agents` > `Registry` (filtro **Platform**) `[Verificado MS Learn]`.
- **Rol Responsable:** `AI Administrator` en coordinación con Cloud Platform Admins `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Verificar el estado saludable de los conectores de **Registry sync** con **Amazon Bedrock**, **Google Cloud (Vertex AI)** y recursos **Microsoft Foundry** `[Verificado MS Learn]`.
  2. Aislar los agentes contabilizados bajo **Unmanaged agents** e instrumentarlos con el **Microsoft Agent 365 SDK** (o incorporarlos individualmente con **Agent 365 CLI**) y un **Microsoft Entra Agent ID**, o detener su infraestructura subyacente (*Start and stop* para agentes Foundry) si carecen de aprobación `[Verificado MS Learn]`.
  3. Confirmar que los *agent identity blueprints* creados previamente en Entra estén explícitamente registrados en el Agent 365 Registry para visibilidad unificada `[Verificado MS Learn]`.
  4. Revisar las entradas múltiples esperadas por diseño (*Shared by creator* vs. *Published by your org*) en agentes de Copilot Studio para evitar desajustes de auditoría `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de conciliación de inventario multi-nube y exportación maestra CSV del Agent Registry `[Verificado MS Learn]`.

### M-02: Auditoría de Grupos Dinámicos para Cuentas agentUser y Consumo de Licencias
- **Alineación Normativa:** NIST CSF 2.0 `PR.AA-01`, `PR.AA-05` / OWASP Agentic `ASI03:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Prevenir que cuentas de usuario de agentes (`agentUser`) coincidan con reglas dinámicas amplias de usuarios humanos, heredando inadvertidamente licencias E5/E7/Copilot, sitios SharePoint o permisos de aplicaciones `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Identity` > `Groups` > `All groups` (filtro *Dynamic user*) y API Graph `POST /beta/groups/evaluateDynamicMembership` `[Verificado MS Learn]`.
- **Rol Responsable:** `Entra Agent ID Admin` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Auditar todas las reglas de grupos dinámicos de usuarios que otorguen licencias, acceso a aplicaciones empresariales, membresía de Teams o alcance de Acceso Condicional `[Verificado MS Learn]`.
  2. Verificar que toda regla destinada exclusivamente a personas incluya la exclusión explícita `-and (user.agentIdentityBlueprintId -eq null)` o valide `user.identityParentId` (confirmando que nunca se haya escrito `-eq ""`, lo cual evalúa a falso y vacía el grupo) `[Verificado MS Learn]`.
  3. Cuando se creen grupos dinámicos dedicados a agentes de un blueprint concreto, confirmar que se utilice el `appId` del blueprint (no su `objectId`) en `user.agentIdentityBlueprintId -eq "<blueprint app ID>"` `[Verificado MS Learn]`.
  4. Inspeccionar la propiedad `assignedLicenses` de todos los objetos `agentUser` existentes para revocar asignaciones grupales innecesarias y validar la conciliación de cupos de licencias Microsoft Agent 365 / E7 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de validación con `evaluateDynamicMembership` y listado limpio de licencias asignadas a cuentas `agentUser` `[Verificado MS Learn]`.

### M-03: Revisión de Políticas de Acceso Condicional para Agentes y Controles de Red Global Secure Access
- **Alineación Normativa:** NIST CSF 2.0 `PR.AA-05`, `PR.IR-01` / OWASP Agentic `ASI01:2026`, `ASI03:2026` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Asegurar cobertura sin brechas en los tres patrones de autenticación de agentes y en el reenvío de tráfico de red SASE `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `Protection` > `Conditional Access` > `Policies` y `Global Secure Access` `[Verificado MS Learn]`.
- **Rol Responsable:** `Entra Agent ID Admin` (`Conditional Access Administrator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Auditar y simular con la API/herramienta **What If** (`conditionalaccessroot-evaluate`) las políticas separadas requeridas para cada sujeto de token (recordando que una política sobre `Users` no cubre a `Agent Users`, y una política sobre `Agent Identities` o `Blueprints` tampoco cubre a `Agent Users`) `[Verificado MS Learn]`.
  2. Confirmar que existan políticas activas que bloqueen agentes con riesgo `High` en ID Protection (`https://aka.ms/CreateAgentRiskPolicy`), exijan atributos de seguridad personalizados aprobados (`Custom Security Attributes`) y requieran dispositivo conforme en sesiones de **Windows 365 for Agents** (*Agent execution environments*) `[Verificado MS Learn]`.
  3. Auditar que ningún agente en producción eluda Entra ID autenticándose mediante API keys estáticas directas contra recursos corporativos `[Verificado MS Learn]`.
  4. Verificar en Power Platform Admin Center y Global Secure Access que todos los entornos productivos de Copilot Studio reenvíen su tráfico HTTP, conectores personalizados y conectores MCP al proxy de **Secure Web and AI Gateway** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Resultados documentados de simulaciones *What If* y reporte mensual de tráfico filtrado en `NetworkAccessGenerativeAIInsights` `[Verificado MS Learn]`.

### M-04: Gobierno de Agentes Inactivos (60/90/455 Días) y Continuidad de Sponsors en Entra ID Governance
- **Alineación Normativa:** NIST CSF 2.0 `PR.AA-01`, `GV.RR-02` / NIST AI RMF `MANAGE-2.4` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Evitar la persistencia indefinida de identidades agénticas en desuso y garantizar que todo agente conserve al menos un patrocinador humano activo `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `ID Governance` > `Lifecycle Workflows` > `Lifecycle Policies` > `Agent ID (Preview)` `[Verificado MS Learn]`.
- **Rol Responsable:** `Entra Agent ID Admin` (`Lifecycle Workflows Administrator` / `Agent ID Administrator`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Verificar que la **Default Agent Identity Inactivity Lifecycle Policy** (60 días notificación a owners/sponsors, 90 días deshabilitación, 455 días eliminación) y las políticas personalizadas de mayor prioridad sigan habilitadas y con buzón *fallback* grupal configurado `[Verificado MS Learn]`.
  2. Revisar las justificaciones de exclusión (`All Agent IDs except selected`) para agentes estacionales (p. ej. cierre fiscal anual), exigiendo revalidación documental `[Verificado MS Learn]`.
  3. Auditar las ejecuciones de *Lifecycle Workflows* de traspaso automático de patrocinio hacia el manager cuando un `sponsor` dejó la compañía `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de ejecuciones de políticas de inactividad y listado de 100 % de identidades de agentes con `sponsor` vigente `[Verificado MS Learn]`.

### M-05: Revisión Ejecutiva de Adopción, Horas Asistidas (Agent Run-Time), ROI y Retiro de Agentes sin Valor
- **Alineación Normativa:** NIST CSF 2.0 `GV.OV-03`, `ID.AM-02` / NIST AI RMF `MEASURE-1.1` `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Medir el retorno de negocio real del parque de agentes, optimizar licenciamiento y retirar ordenadamente agentes redundantes o sin adopción `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com` > `Agents` > `Overview` y `Reports` > `Usage` > `Microsoft 365 Copilot agents` `[Verificado MS Learn]`.
- **Rol Responsable:** `AI Administrator` junto con CAIO / Líderes de Unidad de Negocio `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Consolidar las métricas hero de 30 días: **Active users** (usuarios únicos con interacción prompt-respuesta) y **Agent run-time** (total de horas trabajadas por agentes ejecutando herramientas y respuestas) `[Verificado MS Learn]`.
  2. Identificar en **Agent Map** los agentes con filtro `No sessions` durante dos meses consecutivos y coordinar su desinstalación o *soft-delete* (y bloqueos a nivel tenant para agentes especiales como *Researcher* y *Analyst* donde el panel *Edit users* está deshabilitado cuando aplique restricción global) `[Verificado MS Learn]`.
  3. Ajustar la lista de agentes fijados (**Manage pinned agents**, máximo 3 visibles con prioridad alta por canal) según impacto medible y calidad operativa `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual del Comité de Gobierno de IA con tablero de adopción, ROI y bajas ejecutadas `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Certificación de Access Packages, Permisos Heredables de Blueprints y Atestación por Sponsors
- **Objetivo:** Recertificar el principio de mínimo privilegio sobre grupos de seguridad, roles de Entra y permisos OAuth delegados/aplicación asignados a agentes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com` > `ID Governance` > `Entitlement management` > `Access packages` y `Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** `Entra Agent ID Admin` y `Agent Sponsors` (a través de `https://myaccess.microsoft.com`) `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Ejecutar campañas trimestrales de **Access Reviews** sobre todos los paquetes de acceso asignados a `agentIdentity` y `agentUser`, exigiendo aprobación expresa del `sponsor` humano para renovar y dejando expirar automáticamente los no justificados `[Verificado MS Learn]`.
  2. Auditar en `agentIdentityBlueprint` los permisos OAuth heredables preautorizados y verificar la ausencia de credenciales secretas de larga duración o claves API fuera de Entra ID `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reportes cerrados de campañas de Access Reviews en Entra ID Governance con decisiones firmadas por cada Sponsor `[Verificado MS Learn]`.

### T-02 (Trimestral): Evaluación Regulatoria de IA en Purview Compliance Manager y Políticas de Retención DLM
- **Objetivo:** Medir y demostrar el cumplimiento normativo del ecosistema agéntico frente a regulaciones internacionales de IA y políticas de retención documental `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` > `Solutions` > `Compliance Manager` > `Assessments` (plantillas **Assessments for AI regulations**) y `Data Lifecycle Management` `[Verificado MS Learn]`.
- **Rol Responsable:** `GRC / AI Ethics` y `Purview Data Security AI Admin` `[Verificado MS Learn]`.
- **Procedimiento Operativo:**
  1. Revisar el puntaje de cumplimiento de todas las instancias de Agent 365 incorporadas automáticamente a las evaluaciones de regulaciones de IA (EU AI Act, ISO/IEC 42001, NIST AI RMF / NIST AI 600-1) `[Verificado MS Learn]`.
  2. Validar que las políticas de **Data Lifecycle Management** retengan y depuren conforme a tabla de plazos legales las interacciones agente-humano y humano-agente en Teams, SharePoint, OneDrive y buzones Exchange `[Verificado MS Learn]`.
  3. Verificar controles compensatorios de etiquetado automático o DLP sobre ubicaciones donde los agentes depositan archivos generados (dado que el contenido nuevo de Agent 365 no hereda automáticamente la etiqueta del ítem fuente) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe de evaluación exportado desde Purview Compliance Manager y matriz de políticas DLM activas `[Verificado MS Learn]`.

### SM-01 (Semestral): Ejercicio de AI Red Teaming y Validación Adversaria (OWASP Agentic Top 10 y MITRE ATLAS)
- **Objetivo:** Validar empíricamente la eficacia de los bloqueos en tiempo real de Microsoft Defender, Prompt Shields, DLP inline y Conditional Access frente a ataques agénticos avanzados `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Entorno preproductivo conectado a `https://security.microsoft.com` (`Settings > Security for AI > Real-time protection`) y **AI Red Teaming Agent** en Microsoft Foundry `[Verificado MS Learn]`.
- **Rol Responsable:** Equipo de Red Team / `Security Admin` / `SOC L2/L3` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Ejecutar campañas controladas cubriendo las amenazas del **OWASP Top 10 for Agentic Applications (2026)** (`ASI01 Agent Goal Hijack`, `ASI02 Tool Misuse`, `ASI03 Identity & Privilege Abuse`, `ASI04 Agentic Supply Chain`, `ASI06 Memory & Context Poisoning`, `ASI07 Insecure Inter-Agent Communication`) y técnicas **MITRE ATLAS** (`AML.T0051.001`, `AML.T0054`, `AML.T0043`, `AML.T0057`) `[Decisión / Propuesta Editorial]`.
  2. Verificar la interceptación efectiva en `BehaviorInfo`, la generación de alertas con `XPIADetected`/`JailbreakDetected` y los tiempos reales de detección y contención del SOC `[Verificado MS Learn]`.
  3. Ajustar reglas personalizadas de *Real-time protection*, permisos MCP y exclusiones tras el ejercicio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe técnico semestral de AI Red Teaming con tasa de bloqueo en tiempo real y plan de remediación cerrado `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión Arquitectónica Integral del Plano de Control Agent 365, Soberanía y Licenciamiento E5/E7
- **Objetivo:** Alinear la arquitectura empresarial de gobierno agéntico con la evolución anual de negocio, presupuesto FinOps (Agent 365 standalone vs. Microsoft 365 E7) y exigencias de residencia de datos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com`, `https://entra.microsoft.com`, `https://security.microsoft.com`, `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO, CIO, `AI Administrator`, `Entra Agent ID Admin` y FinOps `[Decisión / Propuesta Editorial]`.
- **Procedimiento Operativo:**
  1. Recertificar las **Security Policy Templates** predeterminadas y personalizadas aplicadas en la activación de agentes `[Verificado MS Learn]`.
  2. Evaluar el punto de equilibrio financiero y funcional entre mantener **Microsoft 365 E5 + Agent 365 standalone ($15/u/m) + complementos** frente a consolidar usuarios intensivos en **Microsoft 365 E7: The Frontier Suite ($99/u/m)** `[Decisión / Propuesta Editorial]`.
  3. Auditar la matriz de residencia geográfica de datos entre regiones Azure de **Microsoft Foundry** (incluyendo opciones *opt-out* en `agent365Config`) y la geografía del tenant de **Microsoft Entra** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Documento anual de Arquitectura de Referencia y Gobierno de Agentes IA firmado por CISO y CIO `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook de Respuesta ante Secuestro de Objetivo de Agente (Agent Goal Hijack / Indirect Prompt Injection - XPIA)
- **Disparador:** Alerta de alta severidad en Microsoft Defender por *Indirect Prompt Injection (XPIA)*, *malicious content propagation* o *evasion techniques*, o hallazgo `XPIADetected == true` en auditoría Purview `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Incidents & alerts`, `https://admin.microsoft.com > Agents > All agents` y `https://purview.microsoft.com > Audit` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Contener inmediatamente el radio de explosión ejecutando **Block** sobre el agente en `admin.microsoft.com > Agents > All agents` (o creando regla inmediata de bloqueo en `Defender > Settings > Security for AI > Real-time protection` si el ataque afecta una clase específica de herramientas) `[Verificado MS Learn]`.
  2. Inspeccionar en Defender el snippet de **Prompt evidence collection** y consultar `CloudAppEvents` y `AccessedResources` en Purview Audit para identificar exactamente el documento, correo o página externa contaminada que inyectó la instrucción oculta `[Verificado MS Learn]`.
  3. Aislar/poner en cuarentena el archivo o correo malicioso origen y auditar todas las invocaciones de herramientas (`ExecuteToolByGateway`, `ExecuteToolByMCPServer`, `ExecuteToolBySDK`) ejecutadas por el agente en la ventana de compromiso `[Verificado MS Learn]`.
  4. Revertir acciones no autorizadas, reforzar validaciones de herramientas MCP/instrucciones del agente y desbloquear únicamente tras prueba de no regresión `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Línea de tiempo forense KQL, archivo origen en cuarentena y registro de bloqueo/desbloqueo en el expediente XDR `[Decisión / Propuesta Editorial]`.

### AH-02: Playbook de Contención ante Compromiso de Microsoft Entra Agent ID o Credencial Sospechosa en Blueprint
- **Disparador:** Detección `suspiciousCredentialUsage`, `entraDirectoryReconnaissance`, `earlyLifeMaliciousActivity` o `threatIntelligenceAccount` en Entra ID Protection, o correlación en *Automatic Attack Disruption* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Protection > Identity Protection > Risky agents` y `Agent ID > Agent blueprints` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Seleccionar el agente en **Risky agents** y ejecutar **Confirm compromise** (activando de inmediato las políticas de Acceso Condicional basadas en riesgo con evaluación continua CAE donde aplique) y **Disable** para cortar todo nuevo inicio de sesión `[Verificado MS Learn]`.
  2. Inspeccionar los registros de auditoría de directorio de Entra ID sobre el `agentIdentityBlueprint` y `agentIdentity` para identificar quién añadió credenciales nuevas, modificó permisos heredables o alteró `owners`/`sponsors` `[Verificado MS Learn]`.
  3. Eliminar toda credencial no autorizada del blueprint, revocar asignaciones de *Access Packages* activas y verificar la cuenta administrativa o de desarrollador que originó el cambio por posible compromiso upstream `[Verificado MS Learn]`.
  4. Rotar credenciales federadas/certificados legítimos y ejecutar **Confirm safe** únicamente tras validación conjunta de SecOps e Identity Engineering `[Verificado MS Learn]`.
- **Evidencia Auditable:** Evento `adminConfirmedAgentCompromised`, log de eliminación de credenciales en `AuditLogs` y cierre de incidente `[Verificado MS Learn]`.

### AH-03: Playbook de Emergencia ante Servidor MCP Malicioso o Abuso de Herramienta Conectada (Supply Chain / Tool Misuse)
- **Disparador:** Compromiso reportado en un proveedor externo MCP/plugin, comportamiento anómalo en Azure AI Gateway / LiteLLM o abuso masivo de una herramienta de escritura/exfiltración `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Agents > Tools > Registry` y `https://security.microsoft.com > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Si el abuso se circunscribe a una operación puntual de un servidor MCP legítimo, acudir a `Agents > Tools > Registry > [MCP Server] > Tools` y desactivar (`Disabled`) la herramienta específica con efecto inmediato en el *Agent 365 Tooling Gateway*; si el servidor completo es sospechoso, pulsar **Block** para bloquear el servidor MCP y sus plugins/conectores dependientes en todo el tenant `[Verificado MS Learn]`.
  2. Consultar la tabla `AgentsInfo` (`where isnotempty(McpServers)`) y `CloudAppEvents` para enumerar todos los agentes, usuarios y sesiones que invocaron dicho servidor MCP durante los últimos 30 días `[Verificado MS Learn]`.
  3. Revocar el consentimiento OAuth de la aplicación empresarial asociada al servidor MCP en `entra.microsoft.com` y bloquear sus FQDNs en **Global Secure Access** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `Blocked` del servidor MCP en el registro, revocación de *service principal* en Entra y listado KQL de sesiones impactadas `[Verificado MS Learn]`.

### AH-04: Playbook de Mitigación ante Exfiltración de Datos Sensibles o Sobrescompartición Agéntica
- **Disparador:** Alerta crítica de `Secret exfiltration` en Defender Real-time protection, alerta de exfiltración en Purview `Risky Agents` (IRM) o exposición de documentos confidenciales detectada en `DSPM > AI observability` `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > DSPM > AI observability`, `Data Loss Prevention` y `https://admin.microsoft.com > Agents > All agents` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Bloquear temporalmente el agente implicado o incluir su instancia/grupo de seguridad en una política **Purview DLP** en modo `Block` inmediato sobre Teams, SharePoint, OneDrive y correo `[Verificado MS Learn]`.
  2. Extraer desde Purview Audit (`AccessedResources`) todos los archivos con `SensitivityLabelId` accedidos o creados por el agente durante el incidente `[Verificado MS Learn]`.
  3. Restringir el acceso al sitio SharePoint afectado mediante políticas de *SharePoint Advanced Management*, verificar que las etiquetas cifradas críticas no concedan `VIEW` + `EXTRACT` a instancias de agentes no autorizadas y aplicar etiquetado/cifrado retroactivo a cualquier archivo derivado sin etiqueta heredada `[Verificado MS Learn]`.
  4. Si se expusieron secretos (API keys o tokens), rotarlos de inmediato en Azure Key Vault / Entra ID `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte de ítems sensibles auditados en Purview, rotación de secretos confirmada y actualización de política DLP/SAM `[Verificado MS Learn]`.

### AH-05: Playbook de Preservación Legal (Legal Hold) e Investigación Forense en Purview eDiscovery sobre Agentes
- **Disparador:** Requerimiento regulatorio, litigio, auditoría externa o investigación interna formal que involucre decisiones o comunicaciones ejecutadas por un agente de IA `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases` y `Audit` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Abrir un caso formal en **Purview eDiscovery** e identificar como custodios/orígenes tanto los buzones de los usuarios involucrados como la cuenta de instancia del agente (`agentUser` / identidad auditable del agente) `[Verificado MS Learn]`.
  2. Aplicar una retención legal (*eDiscovery Hold*) sobre buzones Exchange, sitios SharePoint, OneDrive y canales Teams vinculados para impedir cualquier purga automática por políticas DLM `[Verificado MS Learn]`.
  3. Ejecutar una búsqueda de contenido utilizando el constructor de consultas `Add condition > Type > Contains any of > Copilot activity` para recuperar todos los pares prompt-respuesta e interacciones agente-humano / humano-agente almacenados `[Verificado MS Learn]`.
  4. Volcar los resultados a un **Review set** para revisión legal privilegiada y exportar de forma paralela los registros inmutables de `Audit` (`CopilotInteraction`, `ConnectedAIAppInteraction`) con cadena de custodia `[Verificado MS Learn]`.
- **Evidencia Auditable:** Caso de eDiscovery con *Hold* activo, paquete exportado desde el *Review set* y hash de registros de auditoría `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas Operativas (KQL, Microsoft Graph y PowerShell)

#### Consulta 1 — Inventario Activo y Postura de Agentes en Defender XDR (Tabla `AgentsInfo`) `[Verificado MS Learn]`
Propósito: Obtener la instantánea más reciente de cada agente no eliminado tras la migración obligatoria desde `AIAgentsInfo` (retirada el 1-jul-2026), identificando agentes publicados sin `EntraAgentId`, sin guardrails o con servidores MCP conectados.

```kusto
// Plataforma: Microsoft Defender XDR Advanced Hunting (security.microsoft.com)
// Tabla principal: AgentsInfo (reemplaza a AIAgentsInfo desde julio 2026)
AgentsInfo
| summarize arg_max(Timestamp, *) by AgentId
| where LifecycleStatus != "Deleted"
| extend OwnerCount = array_length(Owners),
         McpCount = array_length(McpServers),
         ToolCount = array_length(DeclaredTools),
         HasEntraAgentId = isnotempty(EntraAgentId)
| project Timestamp, AgentName, AgentId, Platform, PublishedStatus, LifecycleStatus,
          Availability, HasEntraAgentId, EntraAgentId, EntraBlueprintId,
          OwnerCount, McpCount, ToolCount, Model, Guardrails
| order by HasEntraAgentId asc, McpCount desc
```

#### Consulta 2 — Rastreo de Invocaciones de Agentes, Inferencias y Ejecución de Herramientas MCP (`CloudAppEvents`) `[Verificado MS Learn]`
Propósito: Auditar y cazar actividad en tiempo de ejecución reportada por la telemetría de observabilidad de Microsoft Agent 365 a través de SDK, Tooling Gateway y servidores MCP.

```kusto
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Tabla principal: CloudAppEvents (telemetría OpenTelemetry de Agent 365)
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType in ("InvokeAgent", "InferenceCall", "ExecuteToolBySDK", "ExecuteToolByGateway", "ExecuteToolByMCPServer")
| extend RawJson = parse_json(tostring(RawEventData))
| extend AgentId = coalesce(tostring(RawJson.AgentId), tostring(RawJson.TargetAgentId), tostring(RawJson.PlatformTargetAgentId)),
         ToolName = tostring(RawJson.ToolName),
         McpServer = tostring(RawJson.McpServerName)
| summarize TotalEvents = count(),
            ToolCalls = countif(ActionType startswith "ExecuteTool"),
            DistinctUsers = dcount(AccountObjectId),
            ToolsUsed = make_set_if(ToolName, isnotempty(ToolName), 20)
            by AgentId, ActionType, McpServer
| order by ToolCalls desc, TotalEvents desc
```

#### Consulta 3 — Correlación de Bloqueos y Auditorías de Real-Time Protection y Prompt Shields (`BehaviorInfo`) `[Verificado MS Learn]`
Propósito: Investigar eventos registrados por reglas de protección en tiempo real de Microsoft Defender (exfiltración de secretos, propagación de contenido malicioso, técnicas de evasión, dominios de correo inseguros y Prompt Shields).

```kusto
// Plataforma: Microsoft Defender XDR Advanced Hunting
// Tablas principales: BehaviorInfo y BehaviorEntities
BehaviorInfo
| where Timestamp > ago(7d)
| where ServiceSource has_any ("Microsoft Defender", "Security for AI", "Agent")
   or ActionType has_any ("AiAgent", "PromptShield", "RealTimeProtection", "Tool")
| join kind=leftouter (
    BehaviorEntities
    | where Timestamp > ago(7d)
    | project BehaviorId, EntityType, EntityRole, AccountUpn, AdditionalFields
) on BehaviorId
| project Timestamp, BehaviorId, Title, Category, Severity, ActionType,
          Description, EntityType, EntityRole, AccountUpn, AdditionalFields
| order by Timestamp desc
```

#### Consulta 4 — Detección de Shadow AI y Tráfico hacia Servicios GenAI No Autorizados en Global Secure Access `[Verificado MS Learn]`
Propósito: Identificar en Microsoft Sentinel / Log Analytics usuarios o agentes en endpoints que generan tráfico hacia plataformas de IA generativa o endpoints externos fuera de la lista corporativa sancionada.

```kusto
// Plataforma: Microsoft Sentinel / Azure Monitor Log Analytics
// Tabla principal: NetworkAccessGenerativeAIInsights (Entra Global Secure Access)
let sanctionedAiServices = dynamic(["copilot.microsoft.com", "m365.cloud.microsoft", "copilot.cloud.microsoft"]);
NetworkAccessGenerativeAIInsights
| where TimeGenerated > ago(7d)
| extend DestinationHost = tolower(tostring(parse_url(DestinationUrl).Host))
| where isnotempty(DestinationHost) and DestinationHost !in (sanctionedAiServices)
| summarize PromptCount = count(),
            UnsanctionedServices = make_set(DestinationHost, 15),
            FirstSeen = min(TimeGenerated),
            LastSeen = max(TimeGenerated)
            by UserPrincipalName
| where PromptCount > 0
| order by PromptCount desc
```

#### Consulta 5 — Búsqueda Forense de Ataques XPIA, Jailbreak y Evaluaciones DLP Diferidas en Auditoría Unificada `[Verificado MS Learn]`
Propósito: Detectar en registros de auditoría exportados (`OfficeActivity` / esquema de auditoría Purview) interacciones con `CopilotInteraction` o `ConnectedAIAppInteraction` donde se marcó `XPIADetected` en recursos accedidos, `JailbreakDetected` en mensajes o diferimiento DLP (`DLPEvaluationDeferred > 0`).

```kusto
// Plataforma: Microsoft Sentinel / Log Analytics (conector Office 365 / Purview Audit)
// Tabla principal: OfficeActivity / AuditLogs de cargas Copilot y ConnectedAIApp
OfficeActivity
| where TimeGenerated > ago(7d)
| where RecordType in ("CopilotInteraction", "ConnectedAIAppInteraction", "AIAppInteraction")
   or OfficeWorkload in ("Copilot", "ConnectedAIApp", "AIApp")
| extend AuditJson = parse_json(AuditData)
| extend AgentId = tostring(AuditJson.AgentId),
         AgentName = tostring(AuditJson.AgentName),
         DlpDeferredMask = toint(AuditJson.DLPEvaluationDeferred),
         DlpDeferredReason = tostring(AuditJson.DLPEvaluationDeferredReason),
         HasXPIA = tostring(AuditJson.AccessedResources) has "\"XPIADetected\":true",
         HasJailbreak = tostring(AuditJson.Messages) has "\"JailbreakDetected\":true"
| where HasXPIA or HasJailbreak or DlpDeferredMask > 0
| project TimeGenerated, UserId, Operation, AgentName, AgentId,
          HasXPIA, HasJailbreak, DlpDeferredMask, DlpDeferredReason
| order by TimeGenerated desc
```

#### Consulta 6 — Inventario de Blueprints, Identidades de Agentes y Agentes en Riesgo vía Microsoft Entra PowerShell y Graph `[Verificado MS Learn]`
Propósito: Auditar programáticamente en Microsoft Entra todos los *Agent Identity Blueprints*, sus identidades derivadas y la colección `riskyAgents` de Entra ID Protection.

```powershell
# Plataforma: Microsoft Entra PowerShell (v1.3+) y Microsoft Graph SDK
Connect-Entra -Scopes 'Application.Read.All', 'IdentityRiskyAgent.Read.All', 'IdentityRiskEvent.Read.All'

# 1. Enumerar Blueprints e identidades de agentes asociadas
$blueprints = Get-EntraAgentIdentityBlueprint -All
foreach ($bp in $blueprints) {
    $identities = Get-EntraAgentIdentity -AgentIdentityBlueprintId $bp.Id
    [PSCustomObject]@{
        BlueprintDisplayName = $bp.DisplayName
        BlueprintId          = $bp.Id
        AgentIdentityCount   = ($identities | Measure-Object).Count
    }
}

# 2. Consultar agentes marcados en riesgo en Microsoft Entra ID Protection
Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/identityProtection/riskyAgents?`$filter=riskLevel eq 'high' or riskLevel eq 'medium'"
```

#### Consulta 7 — Validación Preventiva de Exclusión de Cuentas `agentUser` en Grupos Dinámicos de Usuarios `[Verificado MS Learn]`
Propósito: Verificar mediante la API oficial `evaluateDynamicMembership` que las reglas dinámicas de licenciamiento y acceso de empleados excluyan correctamente las cuentas `agentUser` mediante `user.agentIdentityBlueprintId -eq null`.

```powershell
# Plataforma: Microsoft Graph PowerShell (endpoint evaluateDynamicMembership)
Connect-MgGraph -Scopes 'Group.Read.All', 'User.Read.All'

$candidateRule = '(user.objectId -ne null) -and (user.userType -eq "Member") -and (user.agentIdentityBlueprintId -eq null)'
$body = @{
    memberId       = "<OBJECT-ID-DE-CUENTA-AGENTUSER-DE-PRUEBA>"
    membershipRule = $candidateRule
} | ConvertTo-Json

# Resultado esperado para un agentUser: membershipRuleEvaluationResult = False
Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/groups/evaluateDynamicMembership" `
    -Body $body `
    -ContentType "application/json"
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Subsistema | Indicador de Salud ("Proof of Life") | Método de Verificación Exacto | Frecuencia |
| :--- | :--- | :--- | :--- |
| **Agent Registry & Sync** | Conteo de agentes poblado y sincronización multi-nube sin errores `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > Overview` > verificar tarjetas *Agent registry* y *Registry sync* `[Verificado MS Learn]`. | Diaria `[Decisión / Propuesta Editorial]` |
| **Defender Security for AI** | Toggle `Enable` activo, conector M365 en estado `Connected` y registros recientes (<24h) en `AgentsInfo` `[Verificado MS Learn]`. | `security.microsoft.com > Settings > Security for AI > Get started` + Consulta KQL 1 `[Verificado MS Learn]`. | Diaria `[Decisión / Propuesta Editorial]` |
| **Telemetría SDK / Gateway** | Flujo activo de eventos `InvokeAgent` y `ExecuteToolByGateway` en `CloudAppEvents` `[Verificado MS Learn]`. | Ejecutar Consulta KQL 2 en Advanced Hunting sobre las últimas 24 horas `[Verificado MS Learn]`. | Diaria `[Decisión / Propuesta Editorial]` |
| **Entra Agent ID Lifecycle** | Política `Default Agent Identity Inactivity Lifecycle Policy` en estado `Enabled` con buzón fallback `[Verificado MS Learn]`. | `entra.microsoft.com > ID Governance > Lifecycle Workflows > Lifecycle Policies > Agent ID` `[Verificado MS Learn]`. | Mensual `[Decisión / Propuesta Editorial]` |
| **Purview AI Observability & IRM** | Agentes visibles en `DSPM > AI observability` y política `Risky Agents` activa en IRM `[Verificado MS Learn]`. | `purview.microsoft.com > DSPM > AI observability` e `Insider Risk Management > Policies` `[Verificado MS Learn]`. | Semanal `[Decisión / Propuesta Editorial]` |
| **Shadow AI Endpoint Control** | Dispositivos reportando inventario local en `Agents > Shadow AI` y política `A365 - Block OpenClaw` aplicada `[Verificado MS Learn]`. | `admin.microsoft.com > Agents > Shadow AI > Security policies` e `intune.microsoft.com` `[Verificado MS Learn]`. | Semanal `[Decisión / Propuesta Editorial]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales

> Todos los umbrales numéricos y metas porcentuales constituyen objetivos de referencia consultiva para organizaciones empresariales `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Cobertura de Agentes Gobernados en Agent 365** | `(Agentes gestionados en Agent 365 / Total de agentes detectados incluyendo Unmanaged) * 100` | `>= 98 %` | Mensual | CISO, CIO, AI Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tasa de Agentes con Owner y Sponsor Humano Activo** | `((Total agentes activos - Agents without owners ni sponsor) / Total agentes activos) * 100` | `100 %` (0 agentes huérfanos > 24 h) | Diaria / Semanal | AI Admin, Entra Agent ID Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Cobertura de Identidad Entra Agent ID y Conditional Access** | `(Agentes publicados con EntraAgentId y cubiertos por políticas CA / Total agentes publicados) * 100` | `>= 99 %` | Mensual | Identity Architect, CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tiempo Medio de Contención de Agentes Críticos (MTTC-Agent)** | `Promedio(Hora de Block/Disable efectivo - Hora de detección High Risk en Defender/Entra/Purview)` | `<= 30 minutos` | Diaria / Mensual | SOC Manager, CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tasa de Remediación de Agentes Locales Shadow AI No Autorizados** | `(Endpoints con política Intune de bloqueo aplicada o agente desinstalado / Endpoints con Shadow AI no aprobado) * 100` | `>= 95 %` en `< 7 días` | Semanal | Security Admin, Endpoint Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Cobertura de Servidores MCP tras Tools Gateway y Control Granular** | `(Servidores MCP gobernados con revisión tool-level y Gateway / Total servidores MCP activos) * 100` | `100 %` | Semanal | AI Admin, AppSec | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Índice de Salud Operativa de Herramientas Agénticas** | `(Agentes activos en Single Agent Map con tasa de excepción de herramientas <= 1 % / Total agentes con observabilidad) * 100` | `>= 95 %` | Semanal | CIO, Propietarios de Negocio | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Cumplimiento de Evaluaciones Regulatorias de IA y Cero Sobrescompartición Alta** | `Puntaje en Purview Compliance Manager (AI Assessments) y agentes con riesgo High sin mitigar en DSPM AI Observability` | `>= 90 %` score y `0` agentes High > 7d | Trimestral | GRC, Comité de Ética IA, CISO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de Cinco Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Estadio de Madurez | Caracterización Técnica y Operativa en Microsoft Agent 365 |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Ad-Hoc (Agent Sprawl)** | Proliferación descontrolada de agentes en Copilot Studio, Foundry, nubes externas y escritorios locales; uso de API keys estáticas; cero visibilidad centralizada; ausencia de *Sponsors* humanos y desconocimiento de ataques XPIA o *Shadow AI*. |
| **Nivel 2** | **Descubrimiento Básico** | Visibilidad reactiva en el Agent Registry básico incluido en M365; bloqueo manual esporádico de agentes huérfanos; inicio de inventario en Entra Agent ID sin políticas específicas de Acceso Condicional ni protección runtime en Defender. |
| **Nivel 3** | **Estandarizado y Gobernado** | Licenciamiento **Agent 365 / M365 E7** habilitado; flujo obligatorio de activación con *Default Security Policy Template*; 100 % de nuevos agentes con `EntraAgentId`, `owner` y `sponsor`; política de inactividad 60/90/455 activa; exclusión `user.agentIdentityBlueprintId -eq null` en grupos dinámicos; *DSPM AI Observability* y política `Risky Agents` operativas. |
| **Nivel 4** | **Gestionado Cuantitativamente y Protegido en Runtime** | *Registry Sync* multi-nube (AWS Bedrock, Google Vertex AI, Foundry); reglas personalizadas de bloqueo en **Defender Real-time protection**; **Global Secure Access** filtrando tráfico de agentes; bloqueo automatizado de *Shadow AI* en Intune; pasarelas **Azure AI Gateway / LiteLLM** con control granular por herramienta MCP; caza semanal en `AgentsInfo`, `CloudAppEvents` y `BehaviorInfo`. |
| **Nivel 5** | **Optimizado / Empresa Frontera Resiliente** | Contención casi instantánea coordinada entre Defender, Entra ID Protection y Purview; *AI Red Teaming* semestral sistemático contra **OWASP Agentic Top 10 (`ASI01`–`ASI10`)** y **MITRE ATLAS**; gobierno continuo de ROI por *Agent run-time*; ejecución aislada en **Windows 365 for Agents** y evidencia continua lista para auditoría externa contra NIST CSF 2.0 y NIST AI 600-1. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

### 12.1 Matriz de Trazabilidad NIST CSF 2.0 (CSWP 29 — Seis Funciones) `[Decisión / Propuesta Editorial]`

| Función NIST CSF 2.0 | Subcategoría Oficial | Descripción del Resultado (CSWP 29) | Capacidad Habilitadora en Microsoft Agent 365 | Evidencia Auditable Reproducible |
| :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales sobre privacidad, propiedad intelectual e IA se comprenden y gestionan. | **Purview Compliance Manager (Assessments for AI regulations)** habilitado automáticamente por instancia Agent 365, **Data Lifecycle Management** y opciones de residencia de datos Entra vs. Foundry `[Verificado MS Learn]`. | Reporte trimestral exportado de *Assessments for AI regulations* y configuración documentada de `agent365Config` `[Decisión / Propuesta Editorial]`. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad se establecen, comunican y hacen cumplir. | Modelo RBAC mínimo privilegio (`AI Administrator`, `AI Reader`, `Agent ID Administrator`) y metadatos obligatorios `owner`, `sponsor` y `manager` con traspaso automático en Entra ID Governance `[Verificado MS Learn]`. | Matriz PIM activa, reporte de **Agents without owners = 0** e historial de *Lifecycle Workflows* de sponsors `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.AM-02` | Los inventarios de software, servicios y sistemas mantenidos por la organización se mantienen actualizados. | **Agent Registry** convergente en `admin.microsoft.com`, **Agent Map**, **Registry Sync** (Bedrock, Vertex AI, Foundry), **Shadow AI** (endpoints) y tabla `AgentsInfo` en Defender `[Verificado MS Learn]`. | Exportación CSV fechada del Agent Registry, resultado de Consulta KQL 1 sobre `AgentsInfo` y estado de conectores Registry Sync `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.RA-01` | Las vulnerabilidades en activos y configuraciones erróneas se identifican, validan y registran. | **Defender AI Agent Security Posture Management** (`Assets > AI agents > Security recommendations`), mapa de rutas de exposición y **Purview DSPM AI Observability** `[Verificado MS Learn]`. | Exportación semanal de recomendaciones de postura en Defender y tablero de riesgos de datos en `DSPM > AI observability` `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.AA-01` | Las identidades y credenciales para usuarios, servicios y hardware autorizados son gestionadas por la organización. | **Microsoft Entra Agent ID** (`agentIdentityBlueprint`, `agentIdentity`, `agentUser`), exclusión en grupos dinámicos (`user.agentIdentityBlueprintId -eq null`) y política de inactividad 60/90/455 días `[Verificado MS Learn]`. | Salida de Consulta 6 y Consulta 7 (`evaluateDynamicMembership`) y estado `Enabled` de la política de inactividad `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen en políticas e incorporan mínimo privilegio y segregación. | **Conditional Access para Agentes** (OBO, App-Only, Agent-User), **Access Packages** con expiración, lista negra en plataforma de >50 permisos Graph críticos y apagado granular de herramientas MCP `[Verificado MS Learn]`. | Políticas CA exportadas, campañas trimestrales de *Access Reviews* y capturas de herramientas MCP deshabilitadas `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.DS-01` | La confidencialidad, integridad y disponibilidad de los datos en reposo y en uso están protegidas. | Exigencia de derechos `VIEW` + `EXTRACT` en **Sensitivity Labels** cifradas, **Inline DLP** y políticas DLP sobre instancias de agentes, más filtrado de red SASE en **Global Secure Access** `[Verificado MS Learn]`. | Políticas DLP activas con alcance de agentes, configuración de etiquetas de sensibilidad y logs de GSA `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.CM-03` | Las actividades del personal y el uso de tecnología (incluidos agentes autónomos) se monitorean para hallar eventos adversos. | Telemetría OpenTelemetry de Agent 365 en `CloudAppEvents`, **Entra ID Protection (`riskyAgents`)** y política **`Risky Agents`** en Purview Insider Risk Management `[Verificado MS Learn]`. | Resultados de Consulta KQL 2 (`CloudAppEvents`), reporte `riskyAgents` y cola auditada de alertas IRM `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender actividades asociadas a ciberataques. | Detección cuasi en tiempo real en **Microsoft Defender** (XPIA, jailbreak, fuga de secretos, evasión), correlación en incidentes XDR y banderas `XPIADetected`/`JailbreakDetected` en Purview Audit `[Verificado MS Learn]`. | Incidentes XDR correlacionados con *Prompt evidence collection* y resultados de Consulta KQL 3 y Consulta KQL 5 `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos para evitar la propagación del impacto. | **Defender Real-time protection** (bloqueo en línea de herramientas), acción **Block** en Agent Registry, **Confirm compromise / Disable** en `Risky Agents` y política Intune `A365 - Block OpenClaw` `[Verificado MS Learn]`. | Registros de bloqueo en `BehaviorInfo`, trazas de *Confirm compromise* en Entra y cumplimiento de política Intune `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.AN-03` | Se ejecuta análisis forense para establecer qué ocurrió durante un incidente y su causa raíz. | **Purview Audit** (`CopilotInteraction`, `ConnectedAIAppInteraction`), **Purview eDiscovery** (condición *Copilot activity* y *Legal Hold*) y **Single Agent Map** `[Verificado MS Learn]`. | Casos cerrados/activos en Purview eDiscovery con *Review sets* y líneas de tiempo forenses KQL `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.RP-05` | La integridad de los activos restaurados se verifica, los sistemas se restablecen y se confirma la operación normal. | Ventana de **30 días de retención por soft-delete** y acción **Restore agent** en `admin.microsoft.com`, rotación de credenciales en blueprints y **Confirm safe** en Entra ID Protection `[Verificado MS Learn]`. | Eventos de auditoría de *soft-delete / restore*, validación post-restauración en *Single Agent Map* (excepciones <=1 %) y acta de cierre `[Decisión / Propuesta Editorial]`. |

### 12.2 Alineación Específica a Marcos de Seguridad de IA: NIST AI RMF / AI 600-1, OWASP Top 10 (LLM & Agentic) y MITRE ATLAS `[Decisión / Propuesta Editorial]`

| Riesgo / Técnica de IA | Identificador en Marcos Oficiales | Control Técnico Mitigador en Microsoft Agent 365 |
| :--- | :--- | :--- |
| **Secuestro de Objetivo e Inyección Indirecta de Prompts (XPIA)** | **OWASP Agentic:** `ASI01:2026 Agent Goal Hijack` / **OWASP LLM:** `LLM01:2025 Prompt Injection` / **MITRE ATLAS:** `AML.T0051.000` y `AML.T0051.001` / **NIST AI 600-1:** *Information Security* | Detección XPIA y bloqueo en **Defender Real-time protection**, **Prompt Shields**, bandera `XPIADetected` en Purview Audit y filtrado web/archivos en **Global Secure Access** `[Verificado MS Learn]`. |
| **Abuso de Herramientas y Agencia Excesiva** | **OWASP Agentic:** `ASI02:2026 Tool Misuse & Exploitation` / **OWASP LLM:** `LLM06:2025 Excessive Agency` / **MITRE ATLAS:** `AML.T0040` / **NIST AI RMF:** `MANAGE-2.4` | **Control granular por herramienta individual** en servidores MCP (`Disabled` para escritura/borrado/pagos), **Azure AI Gateway / LiteLLM Guardrails** y bloqueo runtime de *Unsafe email domain* `[Verificado MS Learn]`. |
| **Abuso de Identidad y Escalada de Privilegios Agéntica** | **OWASP Agentic:** `ASI03:2026 Identity & Privilege Abuse` / **MITRE ATT&CK:** `T1078.004`, `T1098.001` / **MITRE ATLAS:** `AML.T0012`, `AML.T0054` (*LLM Jailbreak*) | **Microsoft Entra Agent ID**, bloqueo técnico en plataforma de >50 permisos críticos de Graph, exclusión de `agentUser` en grupos dinámicos, **Conditional Access** y `riskyAgents` `[Verificado MS Learn]`. |
| **Vulnerabilidades en Cadena de Suministro MCP, Skills y Plugins** | **OWASP Agentic:** `ASI04:2026 Agentic Supply Chain Vulnerabilities` / **OWASP LLM:** `LLM03:2025 Supply Chain` / **MITRE ATLAS:** `AML.T0043` (*LLM Plugin Compromise*) / **NIST AI 600-1:** *Value Chain & Component Integration* | Flujo de aprobación obligatoria en `Agents > Tools > Requests`, restricción por categoría de publicador certificado y bloqueo tenant-wide de servidores MCP y plugins dependientes `[Verificado MS Learn]`. |
| **Ejecución Inesperada de Código y Shadow AI Local** | **OWASP Agentic:** `ASI05:2026 Unexpected Code Execution` / **MITRE ATT&CK:** `T1059` | Aislamiento en **Windows 365 for Agents** (Cloud PCs administrados por Intune), descubrimiento en `Agents > Shadow AI` y bloqueo en endpoint vía política Intune `A365 - Block OpenClaw` `[Verificado MS Learn]`. |
| **Envenenamiento de Contexto, Fuga de Datos y Exfiltración de Secretos** | **OWASP Agentic:** `ASI06:2026 Memory & Context Poisoning` / **OWASP LLM:** `LLM02:2025 Sensitive Information Disclosure` & `LLM07:2025` / **MITRE ATLAS:** `AML.T0057`, `AML.T0024` / **NIST AI 600-1:** *Data Privacy* | **Purview DSPM AI Observability**, exigencia de `VIEW` + `EXTRACT` en **Sensitivity Labels**, **Inline DLP**, política `Risky Agents` en IRM y bloqueo **Secret exfiltration** en Defender `[Verificado MS Learn]`. |
| **Comunicación Inter-Agente Insegura, Fallos en Cascada y Rogue Agents** | **OWASP Agentic:** `ASI07:2026 Insecure Inter-Agent Communication`, `ASI08:2026 Cascading Failures`, `ASI09:2026 Human-Agent Trust Exploitation`, `ASI10:2026 Rogue Agents` / **NIST AI RMF:** `GOVERN-1.2`, `MEASURE-2.5` | Autenticación A2A respaldada por **Entra Agent ID**, supervisión humana (*Sponsors*), monitoreo de excepciones >1 % en **Single Agent Map**, **Communication Compliance** y botón global **Block / Disable** `[Verificado MS Learn]`. |

### 12.3 Matriz de Alineación con NIST AI Risk Management Framework (AI RMF 1.0) y Perfil de IA Generativa (NIST AI 600-1) `[Decisión / Propuesta Editorial]`

El perfil transversal **NIST AI 600-1** (*Generative Artificial Intelligence Profile*, complementario a **NIST AI RMF 1.0**) estructura más de 400 acciones sobre las funciones `GOVERN`, `MAP`, `MEASURE` y `MANAGE` para mitigar los riesgos específicos de modelos generativos y agentes autónomos. La siguiente tabla documenta cómo Microsoft Agent 365 operacionaliza cada función:

| Función NIST AI RMF 1.0 / AI 600-1 | Categorías de Riesgo GenAI Cubiertas (NIST AI 600-1) | Implementación Operativa en Microsoft Agent 365 | Artefacto Auditable en el Tenant |
| :--- | :--- | :--- | :--- |
| **GOVERN** (*GV-1.1, GV-1.3, GV-2.1, GV-6.1*) | Gobernanza legal/regulatoria, roles de responsabilidad humana y cadena de valor de terceros (*Value Chain and Component Integration*). | Flujo centralizado de activación en `admin.microsoft.com`, plantillas obligatorias de seguridad, asignación de `owner`/`sponsor` humano y certificación de partners/*Agent Factories* y servidores MCP `[Verificado MS Learn]`. | Evaluaciones activas en **Purview Compliance Manager**, inventario de *Sponsors* y registro de consentimiento MCP `[Decisión / Propuesta Editorial]`. |
| **MAP** (*MP-1.1, MP-3.4, MP-4.1, MP-5.1*) | Contexto de uso previsto, mapeo de interdependencias socio-técnicas, soberanía de datos y exposición de activos sensibles. | Clasificación por canal, plataforma y origen de conocimiento (*Embedded knowledge* vs. *Fine-tuned models* con Copilot Tuning), **Agent Map** multi-clúster y control de residencia Foundry vs. Entra `[Verificado MS Learn]`. | Exportación mensual de **Agent Map**, grafo de exposición en Defender (`Assets > AI agents`) y matriz de residencia `[Decisión / Propuesta Editorial]`. |
| **MEASURE** (*MS-2.5, MS-2.6, MS-2.7, MS-3.2*) | Seguridad de la información, privacidad de datos, confabulación/excepciones operativas y conducta dañina o sesgada. | Telemetría OpenTelemetry en `CloudAppEvents`, tasa de excepciones >1 % en **Single Agent Map**, *AI Red Teaming* semestral, `DSPM > AI observability`, `Risky Agents` en IRM y **Communication Compliance** `[Verificado MS Learn]`. | Tableros de `DSPM > AI observability`, reportes de excepciones en *Single Agent Map* e informes de *AI Red Teaming* `[Decisión / Propuesta Editorial]`. |
| **MANAGE** (*MG-2.2, MG-2.4, MG-3.1, MG-4.1*) | Contención en tiempo real, desactivación de sistemas fuera de límites (*Kill Switch*), respuesta a incidentes y recuperación controlada. | Bloqueo en línea en **Defender Real-time protection** y **Azure AI Gateway / LiteLLM**, apagado granular de herramientas MCP, **Conditional Access / Confirm compromise**, *Block* global, *soft-delete* de 30 días y política de inactividad 60/90/455 días `[Verificado MS Learn]`. | Eventos de bloqueo en `BehaviorInfo`, historial de políticas de inactividad en Entra y bitácoras de playbooks `AH-01` a `AH-05` `[Decisión / Propuesta Editorial]`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Destinatario | Ruta Curricular Oficial Microsoft Learn y Ninja Trainings (Vigente Nov-2026) | Recursos de Comunidad MVP y Laboratorios Prácticos | Certificaciones / Applied Skills Asociadas |
| :--- | :--- | :--- | :--- |
| **AI Administrator / Agent Registry Admin** | Módulo oficial *Get started with Microsoft Agent 365* (`learn.microsoft.com/en-us/training/modules/agent-365-get-started/`, 48 min) + hub *Microsoft Agent 365 documentation* y *AI Skills Navigator for Agent 365* `[Verificado MS Learn]`. | Despliegue en tenant *Frontier* de *Security Policy Templates*, **Agent Map** y pasarelas MCP en `admin.microsoft.com` `[Decisión / Propuesta Editorial]`. | Fundamentos de Administración M365 y Gobierno Copilot / Agent 365 `[Decisión / Propuesta Editorial]`. |
| **Entra Agent ID Admin / Identity Architect** | Documentación oficial *Microsoft Entra Agent ID* (`learn.microsoft.com/en-us/entra/agent-id/`) + edición comunitaria *Microsoft Entra Ninja Training: identidad y acceso para la era de los agentes de IA (2026)* `[Verificado MS Learn]`. | **Merill Fernando** (`merill.net` / `entra.news`, análisis de `user.agentIdentityBlueprintId`), **Maester v2.3.0** (`maester.dev`), **Fabian Bader** (`cloudbrothers.info`), **Thomas Naunheim** y *TechLab: Entra Suite for Frontier Transformation* `[Verificado MS Learn]`. | **Exam SC-300**: *Microsoft Identity and Access Administrator* + Applied Skills de Microsoft Entra `[Verificado MS Learn]`. |
| **Security Admin & SOC L2/L3** | *Enable security for AI agents using Microsoft Defender*, *Protect AI agents in real time* y *Microsoft Security Copilot Ninja Training: hacia el SOC agéntico (2026)* + *Seguridad de agentes de IA en Microsoft Foundry Ninja Training (2026)* `[Verificado MS Learn]`. | Consultas prácticas sobre `AgentsInfo`, `CloudAppEvents` y `BehaviorInfo` + laboratorio **AI Red Teaming Agent** en Foundry y matriz **OWASP FinBot CTF / Agentic Top 10** `[Verificado MS Learn]`. | **Exam SC-200**: *Microsoft Security Operations Analyst* `[Verificado MS Learn]`. |
| **Purview Data Security AI Admin & GRC** | *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365* (`learn.microsoft.com/en-us/purview/ai-agent-365`), *Monitoring agents with Insider Risk Management* y *Audit logs for Copilot and AI applications* `[Verificado MS Learn]`. | Configuración práctica de `DSPM > AI observability`, pruebas de derechos `EXTRACT` en etiquetas cifradas y simulacros de *eDiscovery Copilot activity* `[Decisión / Propuesta Editorial]`. | **Exam SC-401**: *Administering Information Security in Microsoft 365* `[Decisión / Propuesta Editorial]`. |
| **Agent Sponsors / Business Owners** | Guías operativas de patrocinio en `myaccount.microsoft.com` y `myaccess.microsoft.com` (*Maintain agent sponsors and lifecycle* en Entra ID Governance) `[Verificado MS Learn]`. | Taller interno ejecutivo de 60 minutos sobre responsabilidad de patrocinio, revisión trimestral de accesos y respuesta ante alertas DLP `[Decisión / Propuesta Editorial]`. | Certificación interna anual obligatoria de *Accountable AI Sponsor* `[Decisión / Propuesta Editorial]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Técnicas Verificadas contra Microsoft Learn MCP (`2026-11-11`)

| # | Hallazgo Técnico Verificado a Noviembre de 2026 | Impacto en la Guía Operacional | Estado |
| :--- | :--- | :--- | :--- |
| **1** | **Disponibilidad General (GA 1 de mayo de 2026) y Licenciamiento Exacto:** Microsoft Agent 365 alcanzó GA comercial el **1 de mayo de 2026** a **USD $15/usuario/mes** standalone y como componente central de **Microsoft 365 E7: The Frontier Suite (USD $99/usuario/mes)**, operando de forma óptima sobre **Microsoft 365 E5** y cumpliendo controles **FedRAMP High** evaluados al 1 de octubre de 2026. | Se documenta la tabla exacta de capacidades base vs. Agent 365 / M365 E7 sin asumir erróneamente su inclusión gratuita en M365 E5. | `[Verificado MS Learn]` |
| **2** | **Convergencia del Agent Registry y Deprecación de APIs Graph Antiguas:** Desde mayo de 2026, Microsoft convergió el inventario completo de agentes en **Agent 365 (`admin.microsoft.com > Agents > All agents > Registry`)**, deprecando los recursos Graph antiguos (`agentRegistry`, `agentCardManifest`, `agentInstance`, `agentCollection`) y enfocando `entra.microsoft.com` en el gobierno de identidades Agent ID. | Todas las rutinas de inventario y acciones de ciclo de vida apuntan al Microsoft 365 Admin Center y APIs de paquetes Agent 365. | `[Verificado MS Learn]` |
| **3** | **Retiro Definitivo de la Tabla `AIAgentsInfo` el 1 de julio de 2026:** En Advanced Hunting de Microsoft Defender XDR, `AIAgentsInfo` fue sustituida por **`AgentsInfo`** y dejó de ser accesible tras el 1 de julio de 2026; además, `AgentsInfo` almacena snapshots históricos que exigen `summarize arg_max(Timestamp, *) by AgentId`. | Todas las consultas KQL de inventario y postura utilizan exclusivamente `AgentsInfo` con `arg_max`. | `[Verificado MS Learn]` |
| **4** | ** Riesgo en Grupos Dinámicos con `agentUser` (`user.agentIdentityBlueprintId`):** Verificado en documentación de Microsoft y pruebas técnicas de agosto de 2026: las cuentas `agentUser` tienen `userType == "Member"` y coinciden con reglas dinámicas amplias de usuarios humanos, consumiendo licencias y permisos salvo que se añada `-and (user.agentIdentityBlueprintId -eq null)` (nunca `-eq ""`). | Se incorpora la actividad mensual `M-02` y la Consulta 7 con `evaluateDynamicMembership` para blindar los grupos dinámicos del tenant. | `[Verificado MS Learn]` |
| **5** | **Fronteras RBAC Reales entre Portales (Global Admin, AI Admin e IRM):** `AI Administrator` no puede conectar **Azure AI Gateway / LiteLLM** (requiere `Global Administrator`) ni configurar Conditional Access / Access Packages; a la inversa, `Global Administrator` por sí solo no puede ver alertas de **Purview Insider Risk Management** sobre agentes sin el rol `IRM Analyst` o `IRM Investigator` (y las *Administrative Units* no están soportadas en alertas de agentes IRM). | La matriz RBAC (Sección 4) y los procedimientos diarios reflejan con exactitud estas restricciones reales de permisos. | `[Verificado MS Learn]` |
| **6** | **Distinción Crítica en Purview DSPM y Etiquetas de Sensibilidad:** Solo la versión actual de **DSPM (`DSPM > AI observability`)** soporta Agent 365 (*DSPM classic* no lo soporta); además, el contenido recién creado por instancias de Agent 365 no hereda automáticamente las etiquetas de sensibilidad de los archivos origen, y el acceso a ítems cifrados exige conceder explícitamente `VIEW` y `EXTRACT` a la instancia del agente. | Se integran controles compensatorios de etiquetado/DLP y el uso exclusivo de la vista nueva `DSPM > AI observability` en `S-03` y `T-02`. | `[Verificado MS Learn]` |
| **7** | **Work IQ MCP GA, Tools Gateway (Azure AI Gateway / LiteLLM) y Política de Inactividad 60/90/455:** Se verificó que **Work IQ MCP** (10 herramientas genéricas en GA) sustituye para nuevos proyectos a los servidores MCP legacy por app, que `Agents > Settings > Gateways` integra **Azure AI Gateway** y **LiteLLM** en preview, y que la **Default Agent Identity Inactivity Lifecycle Policy** gratuita aplica hitos fijos de 60, 90 y 455 días. | Incorporado en la arquitectura de interoperabilidad, cadencia `S-05`, cadencia `M-04` y pruebas *Proof of Life*. | `[Verificado MS Learn]` |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Definido | Clasificación | Justificación Arquitectónica y Operativa |
| :--- | :--- | :--- | :--- |
| **1** | Metas numéricas de los 8 KPIs (`>= 98 %` cobertura registro, `0` agentes huérfanos >24h, `MTTC <= 30 min`, `>= 95 %` bloqueo Shadow AI en 7d). | `[Decisión / Propuesta Editorial]` | Microsoft Learn documenta las métricas y telemetría base pero no impone SLAs universales; se establecen umbrales exigentes acordes a banca, salud e infraestructura crítica. |
| **2** | Ventanas máximas de activación PIM/JIT (`2 a 4 horas` para roles de configuración, `8 horas` para operadores SOC en turno) y exigencia de doble *Sponsor* humano en producción. | `[Decisión / Propuesta Editorial]` | Traduce la recomendación oficial de mínimo privilegio en parámetros concretos auditables que evitan bloqueos operativos cuando un único patrocinador se ausenta. |
| **3** | Estructura de cadencias operativas (`8` diarias, `7` semanales, `5` mensuales, `2` trimestrales, `1` semestral, `1` anual y `5` playbooks Ad-Hoc). | `[Decisión / Propuesta Editorial]` | Organiza las capacidades de los cinco portales en un modelo de ejecución repetible alineado con guardias SOC 24x7 y ciclos de gobierno trimestrales/anuales. |
| **4** | Modelo de madurez operacional en 5 niveles para la adopción empresarial de agentes IA. | `[Decisión / Propuesta Editorial]` | Permite al CISO y al CAIO diagnosticar la brecha entre experimentación fragmentada (*Agent Sprawl*) y operación gobernada de *Empresa Frontera*. |
| **5** | Mapeo cruzado simultáneo a **NIST CSF 2.0 (CSWP 29)**, **NIST AI RMF 1.0 / AI 600-1**, **OWASP Top 10 for LLM (2025) & Agentic Applications (2026: `ASI01`–`ASI10`)** y **MITRE ATLAS / ATT&CK**. | `[Decisión / Propuesta Editorial]` | Conecta la evidencia técnica nativa de Microsoft Agent 365 con los marcos de auditoría de ciberseguridad general y de seguridad específica de sistemas agénticos exigidos por reguladores en 2026. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn (`[Verificado MS Learn]`)
- **REF-01:** *Microsoft Agent 365 documentation & Overview* — Microsoft Learn (actualizado nov. 2026): `https://learn.microsoft.com/en-us/microsoft-agent-365/overview`
- **REF-02:** *Microsoft Agent 365 - Service Descriptions (Plans and Feature Availability)* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-agent-365/microsoft-agent-365`
- **REF-03:** *Agent Registry, Governance & Lifecycle Actions, and Agent Roles in Microsoft 365 Admin Center* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-registry-overview`
- **REF-04:** *Use Agent Map and Single Agent Map in the Microsoft 365 Admin Center* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-map`
- **REF-05:** *Understand Shadow AI in Microsoft 365 Admin Center* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/microsoft-agent-365/admin/agent-shadow-ai`
- **REF-06:** *Manage Plugins, Skills, MCP Servers, Work IQ MCP, and Tools Gateway in Microsoft 365 Admin Center* — Microsoft Learn (nov. 2026): `https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-tools-gateway`
- **REF-07:** *Microsoft Entra Agent ID Documentation & Microsoft Graph Agent ID APIs* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/entra/agent-id/`
- **REF-08:** *Conditional Access for Agents in Microsoft Entra* — Microsoft Learn (oct. 2026): `https://learn.microsoft.com/en-us/entra/identity/conditional-access/agent-id`
- **REF-09:** *ID Protection for Agents (`riskyAgents`) & Governing Agent Identities (Default Inactivity Policy)* — Microsoft Learn (oct.–nov. 2026): `https://learn.microsoft.com/en-us/entra/id-protection/concept-risky-agents`
- **REF-10:** *Discover AI Agents (`AgentsInfo`), Detect Threats, and Protect AI Agents in Real Time using Microsoft Defender* — Microsoft Learn (nov. 2026): `https://learn.microsoft.com/en-us/defender-xdr/security-for-ai/ai-agent-real-time-protection`
- **REF-11:** *Use Microsoft Purview to Manage Data Security & Compliance for Microsoft Agent 365 & Monitoring Agents with Insider Risk Management (`Risky Agents`)* — Microsoft Learn (ago. 2026): `https://learn.microsoft.com/en-us/purview/ai-agent-365`
- **REF-12:** *Microsoft Agent 365 Integration with Microsoft Foundry (5 Core Pillars & Data Residency)* — Microsoft Learn (ago. 2026): `https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-365-integration`

### 15.2 Blogs Oficiales y Liderazgo Ejecutivo de Microsoft (`[Verificado MS Learn]`)
- **REF-13:** **Charles Lamanna** (EVP, Copilot, Agents, and Platform) — *Microsoft Agent 365: The control plane for AI agents* (Microsoft Copilot Blog, 18 de noviembre de 2025, anuncio Ignite de los 5 pilares): `https://www.microsoft.com/en-us/copilot/blog/2025/11/18/microsoft-agent-365-the-control-plane-for-ai-agents/`
- **REF-14:** **Judson Althoff** (CEO, Microsoft Commercial Business) — *Introducing the First Frontier Suite built on Intelligence + Trust* (The Official Microsoft Blog, 9 de marzo de 2026, anuncio de GA y precios de Agent 365 a $15 y M365 E7 a $99): `https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/`
- **REF-15:** **Vasu Jakkal** (CVP, Microsoft Security) — *Secure agentic AI for your Frontier Transformation* (Microsoft Security Blog, 9 de marzo de 2026): `https://www.microsoft.com/en-us/security/blog/2026/03/09/secure-agentic-ai-for-your-frontier-transformation/`
- **REF-16:** **Jared Spataro** (CMO, Copilot at Work) — *Powering Frontier Transformation with Copilot and agents* (Microsoft Copilot Blog, 9 de marzo de 2026) y **Nirav Shah / Rob Lefferts** — *Microsoft Agent 365, now generally available, expands capabilities and integrations* (Microsoft Security Blog, 1 de mayo de 2026): `https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/`

### 15.3 Comunidad MVP de Seguridad e Identidad
- **REF-17:** **Merill Fernando** — *Microsoft Entra agent users can join your dynamic groups. Here is what to check (`user.agentIdentityBlueprintId`)* (agosto de 2026): `https://merill.net/2026/08/entra-agent-users-dynamic-groups/`

### 15.4 Marcos Normativos Oficiales de Ciberseguridad e Inteligencia Artificial
- **REF-18:** **NIST CSWP 29** — *The NIST Cybersecurity Framework (CSF) 2.0* (National Institute of Standards and Technology, febrero de 2024): `https://doi.org/10.6028/NIST.CSWP.29`
- **REF-19:** **NIST AI 600-1** — *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST, julio de 2024, complemento de NIST AI RMF 1.0): `https://doi.org/10.6028/NIST.AI.600-1`
- **REF-20:** **OWASP GenAI Security Project & MITRE ATLAS** — *OWASP Top 10 for LLM Applications (2025) & OWASP Top 10 for Agentic Applications (2026: ASI01–ASI10)* (`https://genai.owasp.org/initiatives/top-10-for-llm-and-genai/`) y *MITRE ATLAS: Adversarial Threat Landscape for AI Systems* (`https://atlas.mitre.org/`)

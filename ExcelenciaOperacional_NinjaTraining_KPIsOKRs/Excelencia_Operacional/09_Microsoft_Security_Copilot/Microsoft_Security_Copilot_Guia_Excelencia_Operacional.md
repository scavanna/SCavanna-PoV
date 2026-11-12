# Guía Maestra de Excelencia Operacional: Microsoft Security Copilot (IA Generativa y Agéntica para SecOps, Identidad, Endpoints y Datos)

## 1. Portada y Ficha de Control Documental

| Campo de Control | Valor Canónico |
| --- | --- |
| **Identificador del Módulo** | `09_Microsoft_Security_Copilot` |
| **Orden en Repositorio Maestro** | `09` |
| **Slug Canónico** | `Microsoft_Security_Copilot` |
| **Nombre Completo Oficial** | Microsoft Security Copilot (IA Generativa y Agéntica para SecOps, Identidad, Endpoints y Datos) |
| **Categoría Maestra** | `SecOps, XDR y SIEM` |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | `Nuevo desde Microsoft Learn MCP (Nov 2026)` |
| **Relación con Microsoft 365 E5** | `Incluido con dotación base en M365 E5 (2026) + Consumo elástico por SCUs en Azure` `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://securitycopilot.microsoft.com`, `https://security.microsoft.com`, `https://entra.microsoft.com`, `https://intune.microsoft.com`, `https://purview.microsoft.com`, `https://securitystore.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, SOC L1, SOC L2, SOC L3 / Detection Engineer, Threat Hunter, Identity Admin, Endpoint Admin, Data Security / Purview Admin, AI Security Engineer, FinOps, GRC |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST AI RMF 1.0, MITRE ATT&CK Enterprise v18, ISO/IEC 27001:2022, ISO/IEC 42001, Microsoft Responsible AI Standard `[Decisión / Propuesta Editorial]` |

> **Nota de Consolidación y Alcance (Noviembre 2026):** Este módulo establece el modelo canónico de gobierno, operación SecOps/IT, ingeniería de agentes/plugins, control FinOps y auditoría forense para **Microsoft Security Copilot** a corte 11 de noviembre de 2026. Incorpora el cambio estructural anunciado en Ignite 2025 y desplegado entre noviembre de 2025 y junio de 2026 (MC1261596): la **inclusión automática sin costo adicional de 400 Security Compute Units (SCUs) mensuales por cada 1.000 licencias pagas de usuario en Microsoft 365 E5 y Microsoft 365 E7** (hasta 10.000 SCUs/mes mediante *Default Security Copilot Capacity*), su coexistencia con capacidades aprovisionadas y *overage* en Azure, el catálogo oficial de agentes autónomos e interactivos en Defender, Entra, Intune y Purview, la integración con **Microsoft Sentinel MCP Server** y la trazabilidad completa en **Microsoft Purview Unified Audit Log (UAL)** y **DSPM for AI** `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución hacia el SOC Agéntico a Noviembre de 2026

**Microsoft Security Copilot** ha evolucionado desde un asistente conversacional generativo para analistas hacia una plataforma integral de **IA generativa y agéntica** integrada en el flujo diario de operaciones de seguridad (SecOps), identidad, administración de endpoints y protección de datos `[Verificado MS Learn]`. La plataforma combina modelos de lenguaje especializados en seguridad sobre arquitectura Azure OpenAI (`gpt-4.1` en manifiestos de agentes y modelos propios de seguridad de Microsoft) con un sistema de orquestación iterativo de *pre-processing* (*grounding*), ejecución de herramientas/plugins con permisos **On-Behalf-Of (OBO)** del usuario o identidad dedicada **Microsoft Entra Agent ID**, y *post-processing* contextualizado con telemetría organizacional e inteligencia global de amenazas de Microsoft `[Verificado MS Learn]`.

Operativamente, Security Copilot actúa en dos modalidades complementarias: (1) la **experiencia Standalone** en `https://securitycopilot.microsoft.com` para investigaciones transversales multi-nube, ejecución de *Promptbooks*, gestión de agentes/plugins, *Security Store* y gobierno FinOps de capacidad; y (2) las **experiencias Embedded** nativas dentro de Microsoft Defender XDR, Microsoft Sentinel, Microsoft Entra, Microsoft Intune, Microsoft Purview, Microsoft Defender for Cloud, Microsoft Defender Threat Intelligence y Azure Firewall `[Verificado MS Learn]`.

### 2.2 Modelo de Licenciamiento y Capacidad SCU: Inclusión en M365 E5 / E7 vs. Provisioned & Overage en Azure

El hito financiero y operativo más relevante de 2025–2026 es el modelo de **inclusión de capacidad de Security Copilot en Microsoft 365 E5 y Microsoft 365 E7** (*zero-click autoprovisioning*), iniciado el 18 de noviembre de 2025 para clientes existentes y extendido escalonadamente entre el 20 de abril y el 30 de junio de 2026 a todos los tenants comerciales elegibles sin mínimo de licencias `[Verificado MS Learn]`.

| Dimensión de Capacidad y Facturación | Modelo de Inclusión Microsoft 365 E5 y E7 (*Default Security Copilot Capacity*) | Capacidad Aprovisionada en Azure (*Provisioned SCUs*) | Capacidad de Excedente en Azure (*Overage SCUs*) | Estado |
| --- | --- | --- | --- | --- |
| **Elegibilidad y Activación** | Todos los clientes comerciales de **Microsoft 365 E5 y E7** (sin mínimo de usuarios); auto-aprovisionado sin clic (*zero-click*) con un **Default Workspace** vinculado `[Verificado MS Learn]`. | Clientes sin M365 E5/E7 (ej. usuarios exclusivos de Sentinel o M365 E3) o clientes E5/E7 que retienen/añaden capacidad dedicada en Azure `[Verificado MS Learn]`. | Configurable opcionalmente sobre una capacidad aprovisionada en Azure para absorber picos inesperados `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Dotación / Unidad de Medida** | **400 SCUs al mes por cada 1.000 licencias de usuario pagas**, escalando linealmente (ej. 400 asientos = 160 SCUs/mes; 4.000 asientos = 1.600 SCUs/mes) hasta un **tope de 10.000 SCUs/mes** sin cargo adicional `[Verificado MS Learn]`. | Mínimo **1 SCU por hora** configurada por adelantado en bloques fijos de hora reloj (ej. `09:00–10:00`, `10:00–11:00`) `[Verificado MS Learn]`. | Consumo elástico bajo demanda con tope máximo configurable o ilimitado `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Mecánica de Descuento y Rollover** | Deduce exactamente las SCUs consumidas de la bolsa mensual (ej. `3.5 SCUs` reales); **se reinicia cada mes y NO acumula saldo (*no rollover*)** `[Verificado MS Learn]`. | Facturación horaria completa por la capacidad aprovisionada aunque no se consuma; expira al cierre de cada hora reloj sin rollover `[Verificado MS Learn]`. | Se factura con precisión de **un decimal** sobre las unidades exactas consumidas (ej. `3.2 SCUs`), sin redondeo a entero `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Escalamiento ante Agotamiento** | Escalado Pay-As-You-Go a **$6 USD por SCU** adicional (con preaviso oficial de 30 días antes de aplicar throttling sobre excesos) `[Verificado MS Learn]`. | Si no hay *overage* configurado y se alcanza el 100 %, las peticiones se detienen hasta la siguiente hora reloj; ajustes tardan hasta **30 minutos** `[Verificado MS Learn]`. | Al alcanzar el límite combinado (*Provisioned + Overage*), el portal muestra bloqueo temporal hasta la próxima hora `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Cobertura de Escenarios y Sentinel** | Cubre chat, promptbooks, agentes Microsoft/partners (cómputo SCU) y herramientas developer (Agent Builder, MCP, Graph); **clientes E5/E7 que usan Microsoft Sentinel pueden aplicar estas SCUs incluidas en Sentinel** `[Verificado MS Learn]`. | Cubre todas las experiencias GA y Public Preview vinculadas a la capacidad Azure (Private Preview no consume SCUs) `[Verificado MS Learn]`. | Igual cobertura sobre picos de sesiones manuales, promptbooks o agentes automatizados `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Exclusiones Explícitas** | No cubre ingesta/almacenamiento de Sentinel Data Lake, Data Security Investigations no agénticas en Purview, ejecuciones de Azure Logic Apps ni licencias SaaS pagas de agentes de terceros en Security Store `[Verificado MS Learn]`. | Productos subyacentes (Defender, Sentinel, Intune, Entra, Purview, Logic Apps) se licencian por separado `[Verificado MS Learn]`. | Igual exclusión de costos de infraestructura y licencias de productos origen `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

> **Regla Operativa Crítica para Clientes Existentes y Nubes Gubernamentales:** Microsoft Learn indica expresamente que los clientes de M365 E5/E7 que ya tenían capacidad aprovisionada en Azure antes de la inclusión **no deben eliminar su capacidad previa** sin planificación para evitar interrupciones de workspaces existentes `[Verificado MS Learn]`. Asimismo, la documentación estándar de Security Copilot está diseñada para nubes comerciales (no diseñada actualmente para GCC, GCC High, DoD ni Azure Government; cuando clientes GCC adoptan SKU comercial, sus datos de Copilot se almacenan en el Geo US de Azure Public Cloud) `[Verificado MS Learn]`.

### 2.3 Configuración Preseleccionada en el Auto-Aprovisionamiento M365 E5 / E7

Cuando Microsoft habilita automáticamente un tenant elegible de Microsoft 365 E5 o E7, aplica la siguiente línea base que todo CISO y **Security Copilot Owner** debe auditar el día 1 `[Verificado MS Learn]`:
1. **Ubicación de almacenamiento de Customer Data:** Preseleccionada según la geografía de Microsoft Entra (respetando *Microsoft 365 geo override*, *Preferred Data Location* o *Advanced Data Residency - ADR* hacia el geo soportado equivalente); **una vez creado un Workspace, su región de almacenamiento es inmutable** `[Verificado MS Learn]`.
2. **Ubicación de evaluación de prompts (GPU):** Si el almacenamiento del tenant está en la Unión Europea (EU), los prompts se procesan en GPU dentro de **EU**; fuera de EU, se procesan globalmente (`US`, `UK`, `EU`, `ANZ`) optimizando disponibilidad y latencia `[Verificado MS Learn]`.
3. **Preferencias de compartición de Customer Data con Microsoft:** Ambas opciones (*validación de rendimiento con revisión humana* y *entrenamiento/validación de modelos de IA de seguridad de Microsoft*) vienen configuradas en **Off** por defecto en tenants auto-aprovisionados E5/E7 (mientras que en onboarding manual no-E5 vienen en **On** por defecto y deben revisarse explícitamente) `[Verificado MS Learn]`.
4. **Acceso a datos de servicios Microsoft 365 (Purview):** Configurado en **On** por defecto para permitir consultas y triaje sobre alertas DLP, Insider Risk Management, Information Protection, Communication Compliance, DSPM y conjuntos de revisión de eDiscovery `[Verificado MS Learn]`.
5. **Despliegue de Agentes:** Los agentes de Security Copilot **no se activan automáticamente**; requieren configuración explícita de identidad, permisos y disparadores por un administrador autorizado `[Verificado MS Learn]`.

### 2.4 Principios Rectores de Excelencia Operacional

1. **Seguridad y Mínimo Privilegio en nombre del usuario (On-Behalf-Of + Agent ID):** Security Copilot nunca eleva permisos por sí mismo; cada consulta interactiva respeta estrictamente el RBAC del analista autenticado y cada agente autónomo debe operar preferentemente con una identidad dedicada **Microsoft Entra Agent ID** de alcance acotado `[Verificado MS Learn]`.
2. **Supervisión humana obligatoria contra la sobreconfianza (*Human-in-the-Loop & Anti-Overreliance*):** Conforme a la *Application Card* oficial de Microsoft Security Copilot, ninguna conclusión forense, veredicto de triaje o política generada por IA se ejecuta a ciegas en producción sin validación analítica y retroalimentación estructurada `[Verificado MS Learn]`.
3. **Soberanía, privacidad y cero entrenamiento de modelos fundacionales externos:** Los prompts, respuestas y archivos cargados pertenecen a Customer Data, nunca se comparten con OpenAI ni entrenan modelos fundacionales de Azure OpenAI, y mantienen desactivada la captura para revisión humana salvo aprobación expresa de GRC `[Verificado MS Learn]`.
4. **Disciplina FinOps proactiva sobre SCUs (Inclusión E5 + Provisioned + Overage):** Monitorear diariamente el consumo por categoría (`Prompt`, `Promptbook`, `Agent`, `Primitive`) y tipo (`Manual Action`, `Automated Action`) para proteger el presupuesto mensual de 400 SCUs/1.000 usuarios y evitar bloqueos operativos en medio de incidentes críticos `[Verificado MS Learn]`.
5. **Gobierno riguroso de extensibilidad (Plugins, Promptbooks y MCP):** Restringir la publicación de plugins personalizados a nivel tenant a `Owners only` tras validación en ámbito privado, verificando manifiestos YAML/OpenAPI y conexiones **Sentinel MCP Server** contra colisiones de skills e inyección indirecta de prompts (XPIA) `[Verificado MS Learn]`.
6. **Observabilidad y auditoría integral de IA (Purview UAL + DSPM for AI + Sentinel):** Habilitar obligatoriamente el envío de registros a Microsoft Purview Audit (`CopilotInteraction`, `AppIdentity == Copilot.Security.SecurityCopilot`) y **DSPM for AI** para inspeccionar pares prompt/respuesta, banderas `XPIADetected` / `JailbreakDetected` y compartición de sesiones `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional del Ecosistema Microsoft Security Copilot

```
[Superficies de Interacción del Analista y Administradores]
  Standalone Portal (securitycopilot.microsoft.com)  |  Experiencias Embedded (Sidecar / Chat)
  Defender XDR | Sentinel | Entra | Intune | Purview | Defender for Cloud | MDTI | Azure Firewall
                                      |
                                      v
+-----------------------------------------------------------------------------------------------+
|                       MOTOR DE ORQUESTACIÓN MICROSOFT SECURITY COPILOT                        |
|  1. Pre-Processing & Grounding  --->  2. Seguridad/Modelos LLM (Azure OpenAI gpt-4.1 + MSFT)  |
|  3. Post-Processing Contextual  <---  4. Ejecución de Skills / Plugins / Promptbooks / Agents |
|                                                                                               |
|  [Gobierno de Plataforma y Capacidad]                                                         |
|  - Workspaces (Geo Storage inmutable) + GPU Eval Location (US, UK, EU, ANZ / Global)          |
|  - Default Security Copilot Capacity (400 SCU/1K E5-E7, máx 10K/mes) + Azure Provisioned/Over |
|  - RBAC Plataforma (Copilot Owner [mín. 2] / Contributor) + OBO Auth + Entra Agent ID         |
+-----------------------------------------------------------------------------------------------+
         |                                      |                                    |
         v (Catálogo de Agentes IA)             v (Plugins & Protocolo MCP)          v (Auditoría & FinOps)
[Agentes Microsoft & Security Store]   [1P, 3P & Custom Extensibility]      [Purview & Azure Monitor]
- Defender: Alert/Phishing Triage,     - 1P: Defender XDR, Sentinel, NL2KQL - Purview UAL (Audit Standard,
  TI Briefing, Hunting, Analyst,         Entra, Intune, Purview, MDTI/EASM    180d + retención extendida)
  Dynamic Threat Detection             - Sentinel MCP Server (Data Lake &   - Purview DSPM for AI (pares
- Entra: CA Optimization, Identity       Agent Creation en VS Code/Foundry)   Prompt/Response, XPIA/Jailbreak)
  Risk Mgmt, Access Review Agent       - Custom YAML/JSON: AGENT, GPT,      - Usage Monitoring Dashboard
- Intune: Change Review, Offboarding,    KQL, API (OpenAPI 3.0), LogicApp     (90 días, exportación Excel)
  Policy Config, Vuln Remediation
- Purview: DLP & IRM Triage Agents
```

### 3.2 Experiencias Standalone y Embedded Verificadas por Producto

| Superficie / Producto | Ruta / Punto de Acceso | Capacidades Operativas Clave Verificadas | Estado |
| --- | --- | --- | --- |
| **Standalone Portal** | `https://securitycopilot.microsoft.com` | Sesiones multi-plugin, Pinboard, compartición de sesiones de solo lectura en el tenant, librería de **Promptbooks** (*Incident investigation*, *Microsoft User analysis*, *Suspicious script analysis*, *Threat actor profile*, *TI 360 MDTI*, *Vulnerability impact assessment*, *External threat article*), **Agent Library**, **Security Store**, **Owner settings** y **Usage monitoring** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Defender XDR** | `https://security.microsoft.com` (Panel lateral *Copilot* en Incidentes, Hunting y Acciones) | Resumen unificado de incidentes XDR + Sentinel, **Guided Response**, análisis de scripts/códigos y archivos sospechosos, resúmenes de dispositivos e identidades, generación NL2KQL en **Advanced Hunting** y redacción de informes ejecutivos/técnicos (cerrar el panel lateral con `X` no detiene la generación en segundo plano ni altera el consumo SCU) `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Sentinel & Sentinel MCP Server** | `https://security.microsoft.com` + `securitycopilot.microsoft.com > Sources > Microsoft Sentinel` | Investigación sobre incidentes unificados, plugin `Microsoft Sentinel` (con *default workspace* configurable), plugin `Natural language to KQL for Microsoft Sentinel` y **Microsoft Sentinel MCP Server** sobre **Sentinel Data Lake** y creación de agentes en VS Code (`https://sentinel.microsoft.com/mcp/security-copilot-agent-creation`), Copilot Studio y Microsoft Foundry `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Entra** | `https://entra.microsoft.com > Copilot chat` (Sidecar persistente o pantalla completa) | Investigación en lenguaje natural de usuarios riesgosos, aplicaciones riesgosas, registros de inicio de sesión y auditoría, resolución de incidentes de identidad, diseño de **Lifecycle Workflows** y acceso directo a **Agent chat** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Intune** | `https://intune.microsoft.com > Copilot / Agents` | Generación KQL en **Device query**, resumen y detección de conflictos en políticas y Settings Catalog, comparación de configuración entre dispositivos sanos/afectados y troubleshooting guiado `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Purview** | `https://purview.microsoft.com` (DLP, IRM, Comm Compliance, eDiscovery) | Investigación contextual de alertas **DLP**, síntesis de actividades de **Insider Risk Management**, resumen de mensajes en **Communication Compliance** y resumen de documentos en conjuntos de revisión de **eDiscovery** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Defender for Cloud, MDTI & Azure Firewall** | `https://portal.azure.com` y `https://security.microsoft.com` | Resumen, análisis, delegación y remediación de código/recomendaciones en **Defender for Cloud**; enriquecimiento de actores/IOCs en **MDTI**; análisis de top hits y firmas IDPS en **Azure Firewall** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

### 3.3 Catálogo Oficial Verificado de Microsoft Security Copilot Agents (Noviembre 2026)

| Dominio / Portal | Nombre Oficial del Agente | Modelo de Identidad Soportado | Disparador (*Trigger*) | Rol Requerido y Función Operativa Exacta | Estado |
| --- | --- | --- | --- | --- | --- |
| **Microsoft Defender** | **Phishing Triage Agent / Security Alert Triage Agent (Preview)** | `Microsoft Entra Agent ID` o cuenta de usuario existente | Automático al detectarse nueva alerta | Configura `Security Administrator`. Triaje autónomo de correos reportados por usuarios y alertas de colaboración (GA), más alertas de nube e identidad (Preview), emitiendo veredictos razonados y aprendiendo del feedback del analista `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Defender** | **Threat Intelligence Briefing Agent** | `Microsoft Entra Agent ID` o cuenta de usuario existente | Programado por intervalo o manual | Configura `Security Administrator` (+ rol MDE con *Advanced Hunting, Vulnerability Management, Machine Configuration, Device Inventory Read* y acceso Read a *Device Groups* si usa Agent ID). Genera briefings accionables cruzando MDTI, EASM y CVEs internos `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Defender** | **Threat Hunting Assistant** | Identidad del analista autenticado (OBO) | Bajo demanda en Advanced Hunting | Guía sesiones completas de caza en lenguaje natural generando KQL, interpretando resultados y proponiendo pivotes investigativos `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Defender / Sentinel** | **Security Analyst Agent** | Vinculado a la identidad de cada usuario | Bajo demanda en chat o botón *Analyze with Copilot* | Requiere lectura en Defender XDR, Sentinel Log Analytics o **Sentinel Data Lake**; ejecuta detección de anomalías, clustering, scoring de riesgo y pronósticos sin escribir código `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Defender / Sentinel** | **Dynamic Threat Detection Agent** | Servicio backend adaptativo *always-on* | Continuo (*always-on*) | Correlaciona alertas, eventos, anomalías y TI entre Defender y Sentinel para descubrir falsos negativos ocultos, generando alertas dinámicas mapeadas a MITRE ATT&CK `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Entra** | **Conditional Access Optimization Agent** | Crea automáticamente un `Microsoft Entra Agent ID` único | Cada 24 horas o manual | Configura `Security Administrator`; usa `Conditional Access Administrator`. Escanea brechas, solapamientos y usuarios/apps no protegidos, proponiendo políticas en modo *report-only* (`Policy.Create.ConditionalAccessRO`) `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Entra** | **Identity Risk Management Agent (Preview)** | `Microsoft Entra Agent ID` | Cada 24 horas, manual o continuo | Configura `Security Administrator`. Investiga usuarios riesgosos en Entra ID Protection, evalúa impacto potencial y recomienda acciones decisivas de contención `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Entra / Teams** | **Access Review Agent** | Integración Security Copilot + Entra ID Governance | Durante campañas de Access Reviews | Requiere `Identity Governance Admin` + `Lifecycle Workflows Admin` + `Security Copilot Contributor` para supervisión. Guía conversacionalmente a revisores en **Microsoft Teams** destacando inactividad, cambios de pares y anomalías `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Intune** | **Change Review Agent** | RBAC de Intune + Security Copilot | Solicitudes de Multi Admin Approval | Evalúa el impacto potencial de solicitudes de aprobación administrativa en Intune y recomienda acciones fundamentadas `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Intune** | **Device Offboarding Agent** | RBAC de Intune + Microsoft Entra | Análisis bajo demanda / programado | Detecta dispositivos obsoletos o desalineados entre Intune y Entra ID, exigiendo aprobación explícita del administrador antes de retirar cualquier equipo `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Intune** | **Policy Configuration Agent** | RBAC de Intune | Bajo demanda al importar documentos/texto | Traduce guías normativas, baselines o instrucciones en lenguaje llano a configuraciones exactas del **Intune Settings Catalog** y crea el borrador de política `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Intune** | **Vulnerability Remediation Agent** | RBAC de Intune + Defender Vulnerability Mgmt | Continuo / programado | Monitorea vulnerabilidades con telemetría de Defender y prioriza remediaciones en Intune mediante evaluaciones de riesgo impulsadas por IA `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Purview** | **Alert Triage Agent in Data Loss Prevention (Preview)** | Cuenta del administrador que lo activa (**expira cada 90 días**) | Programado o por alerta individual | Visualiza `IRM Analysts/Investigators`; administra `Purview Content Analyst` en `Purview Agent Management`. Clasifica alertas DLP en 4 categorías evaluando sensibilidad, exfiltración y política (exige *evidence collection* en endpoints) `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Purview** | **Triage Agent in Insider Risk Management (Preview)** | Cuenta del administrador que lo activa (**expira cada 90 días**) | Programado o por alerta individual | Mismos roles Purview que DLP Triage Agent. Evalúa riesgo de usuario, archivo y actividad ordenando alertas IRM en 4 categorías priorizadas `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

### 3.4 Arquitectura de Plugins, Manifiestos YAML y Servidor MCP

La extensibilidad técnica de Security Copilot se estructura mediante manifiestos YAML o JSON compuestos por tres claves raíz (`Descriptor`, `SkillGroups`, `AgentDefinitions`) `[Verificado MS Learn]`:
- **Formatos oficiales de `SkillGroups`:** `AGENT` (instrucciones orquestadoras con `ChildSkills`), `GPT` (plantillas de hasta 80.000 caracteres sobre modelo `gpt-4.1`), `KQL` (consultas de hasta 80.000 caracteres apuntando a `Defender`, `Sentinel` o clusters `Kusto` ADX), `API` (especificaciones **OpenAPI 3.0 o 3.0.1**) y `LogicApp` (disparo de flujos en la misma suscripción/tenant) `[Verificado MS Learn]`.
- **Esquemas de autenticación de Plugins soportados:** `None`, `Basic`, `ApiKey`, `ServiceHttp`, `OAuthAuthorizationCodeFlow`, `OAuthClientCredentialsFlow`, `AAD` y `AADDelegated` (evitando `OAuthPasswordGrantFlow` por ser legado no recomendado) `[Verificado MS Learn]`.
- **Prevención de *Skill Collisions*:** Diseñar herramientas consolidadas (ej. un único skill `GetDevices` polimórfico en lugar de tres skills separados) y detallar `DescriptionForModel` (hasta 16.000 caracteres en plugins) separado de `Description` para la interfaz de usuario `[Verificado MS Learn]`.
- **Integración con Model Context Protocol (MCP):** El **Microsoft Sentinel MCP Server** expone colecciones estandarizadas de herramientas de exploración de datos, análisis de entidades, caza y triaje sobre el **Sentinel Data Lake** (requiere rol mínimo `Security Reader`) y creación asistida de agentes en VS Code mediante `https://sentinel.microsoft.com/mcp/security-copilot-agent-creation` `[Verificado MS Learn]`.

### 3.5 Matriz Verificada de Acceso a Datos Microsoft 365 (Purview), Ciclo de Retención y Promptbooks Nativos

De acuerdo con `privacy-data-security.md`, cuando se mantiene activa la opción *Allow Security Copilot to access data from your Microsoft 365 services*, Security Copilot accede exclusivamente a los datos procesados y generados por **Microsoft Purview** conforme a lo configurado por el administrador `[Verificado MS Learn]`:

| Servicio Microsoft Purview Conectado | Datos Exactos Consultados por Security Copilot | Escenario Operativo Habilitado | Estado |
| --- | --- | --- | --- |
| **Data Loss Prevention (DLP)** | Metadatos, contexto de coincidencia de reglas y evidencias asociadas a alertas DLP. | Resumen de alertas DLP y operación del **Alert Triage Agent in DLP** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Microsoft Purview Information Protection (MIP)** | Registros de actividad (*activity logs*) asociados a la aplicación o cambio de etiquetas de sensibilidad. | Correlación de desclasificación o acceso a archivos etiquetados durante investigaciones `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management (IRM)** | Datos de alerta y secuencia de actividades de riesgo asociadas a una política IRM. | Síntesis forense de actividad de riesgo interno y operación del **Triage Agent in IRM** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Communication Compliance** | Contenido capturado dentro de una coincidencia de política de cumplimiento de comunicaciones. | Resumen contextual de mensajes marcados en **Communication Compliance** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **eDiscovery** | Documentos y mensajes contenidos dentro de un conjunto de revisión (*review set*) de una búsqueda eDiscovery. | Resumen asistido de hilos extensos dentro de conjuntos de revisión legales `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Data Security Posture Management (DSPM)** | Eventos de actividad y alertas consolidados provenientes de MIP, DLP e IRM. | Evaluación transversal de postura de seguridad de datos e IA `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

Asimismo, la plataforma aplica reglas estrictas de retención y borrado sobre **Customer Data** (prompts, datos recuperados, respuestas, Pinboard y archivos subidos) que deben integrarse al gobierno documental del SOC `[Verificado MS Learn]`:

| Evento del Ciclo de Vida de Datos en Security Copilot | Plazo Oficial de Retención / Eliminación | Implicación Operativa y Regulatoria | Estado |
| --- | --- | --- | --- |
| **Sesión activa en suscripción vigente** | Retenida mientras la suscripción permanezca activa y la sesión tenga actividad. | Exportar informes ejecutivos cerrados al repositorio formal de casos del SOC `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Inactividad de una sesión > 180 días** | Eliminación automática tras **180 días** sin actividad en la sesión. | No utilizar sesiones de Security Copilot como archivo histórico permanente `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Eliminación de toda la capacidad aprovisionada** | Eliminación definitiva dentro de los **180 días** posteriores a la baja total de capacidad. | Contactar previamente a soporte si se requiere exportación regulatoria `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Solicitud expresa de borrado por el cliente / Opt-out** | Eliminación completada dentro de los **30 días** desde la solicitud en portal o soporte (igual plazo al desactivar *data sharing*). | Habilita respuesta oportuna ante incidentes de exposición interna o solicitudes GDPR/DSR `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Datos capturados bajo *Opt-in* de compartición** | Retenidos máximo **90 días** por el equipo evaluador antes de su borrado (en E5/E7 viene en **Off** por defecto). | Mantener en `Off` por defecto salvo autorización expresa de GRC `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

Finalmente, la librería oficial de **Promptbooks preconstruidos** estandariza flujos repetibles de investigación `[Verificado MS Learn]`:

| Promptbook Preconstruido Oficial | Entrada Requerida (*Input*) | Plugins / Roles Mínimos Requeridos | Salida Estandarizada para el Analista |
| --- | --- | --- | --- |
| **Microsoft Sentinel / Defender XDR incident investigation** | `SENTINEL_INCIDENT_ID` o ID de incidente Defender | Plugin `Microsoft Sentinel` o `Microsoft Defender XDR` + `Sentinel/Defender Reader` | Resumen de alertas, reputación de entidades, dispositivos/usuarios afectados e informe ejecutivo no técnico `[Verificado MS Learn]`. |
| **Microsoft User analysis** | `UPN` del usuario + rango temporal | `Security Reader` (Entra, Intune, Defender) + `IRM Investigator/Analyst` (Purview) | Correlación 360° de inicios de sesión Entra, equipos Intune, anomalías Purview y detecciones Defender `[Verificado MS Learn]`. |
| **Suspicious script analysis** | `SNIPPET` (código PowerShell / CMD) | Capacidad base Security Copilot | Desofuscación funcional paso a paso, indicadores extraídos, mapeo de intención maliciosa y remediación `[Verificado MS Learn]`. |
| **Threat actor profile** | Nombre del actor de amenaza | Plugin `Microsoft Threat Intelligence` | Perfil ejecutivo de TTPs conocidos, herramientas, IOCs asociados y mitigaciones recomendadas `[Verificado MS Learn]`. |
| **Threat Intelligence 360 report based on MDTI article** | Nombre del artículo MDTI | Plugin `Microsoft Threat Intelligence` + telemetría SIEM/XDR | Verificación de exposición interna frente al boletín MDTI y consultas KQL listas para hunting `[Verificado MS Learn]`. |
| **Check impact of an external threat article** | `URL` pública del reporte externo | Plugin `Microsoft Threat Intelligence` + `Public web` | Extracción automática de IOCs del artículo externo, cruce con artículos MDTI y queries KQL `[Verificado MS Learn]`. |
| **Vulnerability impact assessment** | `CVEID` o nombre común de vulnerabilidad | Plugins `Microsoft Threat Intelligence` / `Defender Vulnerability Management` | Estado de divulgación/explotación en campañas reales, impacto técnico y resumen ejecutivo de mitigación `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Los roles propios de **Security Copilot RBAC** (`Security Copilot owner` y `Security Copilot contributor`) **no son roles de Microsoft Entra ID**: se gestionan por Workspace dentro de Security Copilot, solo admiten usuarios o **Role-assignable groups** de Entra ID, y **no conceden por sí mismos acceso a ningún dato de seguridad** `[Verificado MS Learn]`. Adicionalmente, la plataforma fuerza como medida anti-bloqueo la **retención mínima permanente de al menos dos (2) owners** `[Verificado MS Learn]`.

| Rol Oficial / Grupo de Acceso | Plano RBAC | Permisos en Security Copilot y Servicios Subyacentes | Estrategia PIM / Asignación Recomendada | Responsabilidad Operativa y Segregación de Funciones | Estado |
| --- | --- | --- | --- | --- | --- |
| **Security Copilot Owner** | Security Copilot Platform RBAC (por Workspace) | Configurar `Owner settings` (compartición de datos, ubicación GPU, acceso M365, logging a Purview), gestionar asignaciones de roles, restringir plugins preinstalados, aprobar plugins custom para el tenant y ver `Usage monitoring` `[Verificado MS Learn]`. | Asignar vía **Role-assignable group** en Entra gobernado con PIM (máx. 4 h); auditar herencia automática de roles Entra/Purview `[Decisión / Propuesta Editorial]`. | Gobierno de plataforma, privacidad, catálogo de plugins y control de SCUs; mantener mínimo 2 custodios verificados `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Azure Capacity Owner / Contributor + Security Admin** | Azure RBAC + Microsoft Entra RBAC | Aprovisionar, escalar, vincular o eliminar recursos de capacidad SCU (`Provisioned` y `Overage`) en Azure y enlazarlos a Workspaces de Security Copilot `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 2 h, aprobación FinOps/SecOps Lead + MFA resistente al phishing) `[Decisión / Propuesta Editorial]`. | Control presupuestario de capacidad Azure y prevención de borrado accidental e irreversible de capacidad (`Delete the capacity`) `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Security Copilot Contributor (`Recommended Microsoft Security roles`)** | Security Copilot Platform RBAC | Crear sesiones, ejecutar y compartir **Promptbooks**, cargar archivos en sesión propia (por defecto habilitado) e interactuar con experiencias standalone y embedded; **por defecto NO puede subir ni publicar plugins custom** `[Verificado MS Learn]`. | Remover el grupo histórico `Everyone` (acción irreversible y recomendada) y usar `Recommended Microsoft Security roles` o grupos Role-assignable por nivel SOC `[Verificado MS Learn]`. | Operación analítica diaria de triaje, investigación, caza e informes respetando permisos OBO de cada producto `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **SOC L1 / L2 Analyst (Defender Unified RBAC + Sentinel Reader/Responder)** | Defender XDR Unified RBAC + Azure RBAC | Permiso específico *Security Copilot* en rol custom de Defender XDR + `Microsoft Sentinel Reader` / `Responder` para que los plugins de Defender y Sentinel devuelvan incidentes, alertas y tablas KQL en modo OBO `[Verificado MS Learn]`. | Roles operativos de lectura activos; roles de respuesta/remediación elegibles en PIM (8 h por turno) `[Decisión / Propuesta Editorial]`. | Triaje asistido de incidentes unificados, análisis de scripts/archivos, NL2KQL y validación humana de veredictos del Alert Triage Agent `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Security Administrator (Configurador de Agentes Defender / Entra)** | Microsoft Entra RBAC | Requerido explícitamente para configurar y activar el *Security Alert / Phishing Triage Agent*, *Threat Intelligence Briefing Agent*, *Conditional Access Optimization Agent* e *Identity Risk Management Agent* `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 2 h, nunca asignado solo para dar acceso de analista a Copilot) `[Verificado MS Learn]`. | Alta inicial, asignación de `Microsoft Entra Agent ID`, definición de triggers y desactivación de emergencia de agentes `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Endpoint Security Manager / Intune Role con permiso Copilot** | Microsoft Intune RBAC | Consultar inventario, políticas, Device Query y operar *Change Review*, *Device Offboarding*, *Policy Configuration* y *Vulnerability Remediation Agents* en Intune `[Verificado MS Learn]`. | Elegible en PIM (máx. 4 h) con Multi Admin Approval activo para cambios masivos `[Decisión / Propuesta Editorial]`. | Diagnóstico de endpoints, creación asistida de políticas Settings Catalog y aprobación supervisada de bajas de equipos `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Purview Content Analyst (`Purview Agent Management`) + IRM Investigator** | Microsoft Purview RBAC | `Purview Content Analyst` requerido para administrar *DLP Alert Triage Agent* e *IRM Triage Agent*; `IRM Analysts/Investigators` para visualizar triajes y ejecutar el promptbook *Microsoft User analysis* `[Verificado MS Learn]`. | Asignación restringida bajo aprobación de Privacidad/Legal y renovación programada de credenciales de agente cada <90 días `[Verificado MS Learn]`. | Gobierno de agentes de seguridad de datos y auditoría de alertas DLP/IRM sin exponer contenido sensible fuera del equipo autorizado `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Purview Audit Reader & DSPM for AI Administrator** | Microsoft Purview RBAC | Consultar eventos `CopilotInteraction` y operaciones administrativas en Unified Audit Log (UAL) e inspeccionar contenido de pares prompt/respuesta y detecciones XPIA/Jailbreak en **DSPM for AI** `[Verificado MS Learn]`. | Elegible o acotado estrictamente a Auditoría Interna / AI Security Governance `[Decisión / Propuesta Editorial]`. | Supervisión independiente del uso de IA, detección de fugas vía sesiones compartidas e investigación de abusos de prompts `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

> **Advertencia de Seguridad sobre Herencia Automática y Sesiones Compartidas:** (1) Roles como `Billing Administrator`, `Global Administrator`, `Security Administrator`, `Intune Administrator`, `Conditional Access Administrator` y roles de cumplimiento de Entra/Purview heredan automáticamente permisos de `Security Copilot owner` en el workspace por defecto — esta lista debe revisarse y podarse en `Role assignment` `[Verificado MS Learn]`. (2) Al compartir el enlace de una sesión (`Shared session`), cualquier `Copilot contributor` destinatario dentro del mismo tenant puede leer **todos** los prompts y respuestas de esa sesión **sin que Security Copilot reevalúe si el destinatario posee permisos sobre el plugin origen** (ej. Intune o Purview); por tanto, compartir sesiones con datos restringidos requiere disciplina estricta de clasificación `[Verificado MS Learn]`.

---

## 5. Cadencia Operativa Diaria

### D-01: Monitoreo FinOps diario de consumo de SCUs (Inclusión M365 E5/E7, Provisioned y Overage)
- **Objetivo:** Prevenir el agotamiento sorpresivo de la bolsa mensual de SCUs incluidas en M365 E5/E7 o picos no controlados de *Overage SCUs* en Azure `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Home menu > Owner settings > Usage monitoring` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner / FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Seleccionar cada pestaña de capacidad activa (*Default Security Copilot Capacity* de M365 E5/E7 y capacidades Azure aprovisionadas si existen) revisando la curva de las últimas 24 horas `[Verificado MS Learn]`.
  2. Filtrar la tabla de sesiones por `Category` (`Prompt`, `Promptbook`, `Agent`, `Primitive`) y `Type` (`Manual Action` vs. `Automated Action`) para identificar procesos automatizados o Logic Apps con consumo desproporcionado `[Verificado MS Learn]`.
  3. Verificar que el ritmo diario proyectado (`burn rate`) se mantenga alineado al presupuesto mensual (`400 SCUs por cada 1.000 licencias E5/E7`, sin rollover mensual) `[Verificado MS Learn]`.
  4. Si existe una investigación mayor activa y el consumo supera el 85 % del umbral disponible, coordinar con el `Azure Capacity Owner` el ajuste de capacidad al inicio de la hora reloj (recordando que tarda hasta 30 minutos en aplicarse) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación Excel diaria/semanal desde `Usage monitoring > Export` y registro de proyección FinOps `[Verificado MS Learn]`.

### D-02: Supervisión operativa y retroalimentación de veredictos del Phishing / Security Alert Triage Agent
- **Objetivo:** Auditar una muestra representativa de alertas clasificadas autónomamente en Microsoft Defender XDR y retroalimentar al agente para elevar continuamente su precisión `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Security Copilot > Agents > Agents in use > Security Alert Triage Agent / Phishing Triage Agent` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Confirmar que el estado operativo y de autenticación del agente se encuentre activo y procesando nuevas alertas de correo/colaboración, nube e identidad configuradas `[Verificado MS Learn]`.
  2. Revisar la explicación en lenguaje natural (*transparent rationale*) emitida por el agente en los veredictos de verdaderos positivos y falsos positivos de las últimas 24 horas `[Verificado MS Learn]`.
  3. Registrar feedback explícito del analista sobre cualquier desviación detectada para refinar el razonamiento dinámico del agente en el tenant `[Verificado MS Learn]`.
- **Evidencia Auditable:** Métricas de alertas triadas autónomamente y bitácora de feedback analítico en el portal de Microsoft Defender `[Verificado MS Learn]`.

### D-03: Triaje acelerado e investigación guiada de incidentes unificados XDR + Sentinel
- **Objetivo:** Reducir MTTA y MTTR utilizando resúmenes de incidentes, *Guided Response*, análisis de scripts y el promptbook *Incident investigation* con verificación humana obligatoria `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Investigation & response > Incidents` y `https://securitycopilot.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Abrir cada incidente de severidad High/Medium en `security.microsoft.com`, revisar el **Incident summary** y las recomendaciones de **Guided response** generadas por Copilot in Defender `[Verificado MS Learn]`.
  2. Ante comandos ofuscados en PowerShell/CMD o binarios sospechosos, ejecutar **Analyze scripts and codes** / **Analyze files** o el promptbook **Suspicious script analysis** `[Verificado MS Learn]`.
  3. Contrastar siempre las entidades, IOCs y consultas NL2KQL generadas contra las tablas crudas de Advanced Hunting antes de aislar hosts o deshabilitar cuentas (mitigación de *overreliance*) `[Verificado MS Learn]`.
  4. Generar el borrador de cierre y resumen ejecutivo mediante **Create incident reports** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe de incidente validado por analista adjunto al caso en Defender XDR / Sentinel y feedback de calidad registrado (`Looks right` / `Needs improvement`) `[Verificado MS Learn]`.

### D-04: Revisión diaria de hallazgos del Conditional Access Optimization Agent e Identity Risk Management Agent
- **Objetivo:** Evaluar las recomendaciones diarias de cobertura Zero Trust y riesgo de identidad generadas cada 24 horas en Microsoft Entra `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Agents` y `Entra Copilot chat > Agent chat` `[Verificado MS Learn]`.
- **Rol Responsable:** Conditional Access Administrator / Security Administrator / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Revisar la ejecución automática de 24 horas del **Conditional Access Optimization Agent** identificando nuevos usuarios/aplicaciones sin política MFA o políticas redundantes `[Verificado MS Learn]`.
  2. Validar en modo **Report-only** (`Policy.Create.ConditionalAccessRO`) y con la herramienta *What If* cualquier política sugerida antes de promoverla a `On` `[Verificado MS Learn]`.
  3. Inspeccionar las investigaciones priorizadas por el **Identity Risk Management Agent (Preview)** sobre usuarios con riesgo elevado en Entra ID Protection `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de actividad de ambos agentes en Microsoft Entra y cambios de políticas trazados en `AuditLogs` `[Verificado MS Learn]`.

### D-05: Supervisión de colas priorizadas por los Agentes de Triaje en Microsoft Purview (DLP e Insider Risk)
- **Objetivo:** Acelerar la atención de exfiltración de datos sensibles y riesgos internos verificando las cuatro categorías de priorización generadas por IA en Purview `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Data Loss Prevention > Alerts` e `Insider Risk Management > Alerts` `[Verificado MS Learn]`.
- **Rol Responsable:** Purview DLP / Insider Risk Management Analyst & Investigator.
- **Procedimiento Paso a Paso:**
  1. Confirmar que el **Alert Triage Agent in DLP** y el **Triage Agent in Insider Risk Management** ejecutaron sus corridas programadas sin error de expiración de credenciales (vigencia máxima de **90 días**) `[Verificado MS Learn]`.
  2. Atender prioritariamente las alertas ubicadas en la categoría superior de riesgo de sensibilidad, exfiltración y actividad de usuario `[Verificado MS Learn]`.
  3. Utilizar la investigación embebida de Copilot en Purview para resumir actividades correlacionadas y mensajes relevantes antes de escalar a Legal/RR. HH. `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de alertas DLP/IRM triadas y feedback almacenado por los agentes de Purview `[Verificado MS Learn]`.

### D-06: Monitoreo de seguridad sobre interacciones IA (`XPIADetected`, `JailbreakDetected` y eventos Admin)
- **Objetivo:** Detectar intentos de inyección indirecta de prompts (XPIA) desde documentos/artefactos maliciosos analizados por Copilot, intentos de jailbreak o cambios administrativos no autorizados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Audit / DSPM for AI > Activity explorer` y Microsoft Sentinel `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / AI Security Engineer.
- **Procedimiento Paso a Paso:**
  1. Ejecutar consulta diaria sobre registros de auditoría `RecordType == CopilotInteraction` con `AppIdentity == "Copilot.Security.SecurityCopilot"` (y hosts embebidos como `Copilot in Defender`, `Copilot in Intune`) `[Verificado MS Learn]`.
  2. Filtrar eventos donde `AccessedResources` contenga `XPIADetected == true` o donde `Messages` marque `JailbreakDetected == true` `[Verificado MS Learn]`.
  3. Auditar toda operación administrativa (`UpdateTenantSettings`, `CreatePlugin`, `DeletePlugin`, `EnablePromptBook`) contrastándola contra cambios autorizados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Cero alertas XPIA/Jailbreak o cambios de plugins sin investigar en Microsoft Sentinel / Purview Audit `[Verificado MS Learn]`.

### D-07: Verificación de alertas dinámicas del Dynamic Threat Detection Agent y briefings de amenazas
- **Objetivo:** Investigar detecciones adaptativas de falsos negativos generadas entre Defender y Sentinel y distribuir inteligencia diaria priorizada `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Incidents & alerts` y `Security Copilot > Agents > Threat Intelligence Briefing Agent` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / SOC L3.
- **Procedimiento Paso a Paso:**
  1. Revisar cualquier alerta dinámica generada por el **Dynamic Threat Detection Agent**, analizando su explicación en lenguaje natural, técnicas MITRE ATT&CK mapeadas y pasos de remediación `[Verificado MS Learn]`.
  2. Revisar el reporte programado del **Threat Intelligence Briefing Agent**, verificando que el cruce con vulnerabilidades internas de Defender Vulnerability Management no muestre vacíos por permisos de *Device Groups* `[Verificado MS Learn]`.
  3. Convertir los IOCs y TTPs relevantes del briefing en hipótesis activas dentro del **Threat Hunting Assistant** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Briefing diario distribuido al turno SOC y tickets de caza/mitigación creados `[Decisión / Propuesta Editorial]`.

### D-08: Evaluación asistida de solicitudes Multi Admin Approval con el Change Review Agent en Intune
- **Objetivo:** Prevenir impactos operativos o debilitamiento de seguridad en endpoints antes de aprobar cambios administrativos sensibles en Microsoft Intune `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com > Tenant administration > Multi Admin Approval / Agents > Change Review Agent` `[Verificado MS Learn]`.
- **Rol Responsable:** Intune Administrator / Endpoint Security Manager.
- **Procedimiento Paso a Paso:**
  1. Consultar la evaluación de efecto e impacto generada por el **Change Review Agent** sobre las solicitudes pendientes de aprobación dual en Intune `[Verificado MS Learn]`.
  2. Contrastar con Copilot en Intune posibles conflictos con políticas existentes del Settings Catalog antes de otorgar aprobación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Solicitudes de Multi Admin Approval aprobadas/rechazadas con análisis de impacto documentado `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Auditoría semanal de salud de identidades de Agentes (`Entra Agent ID` vs. Cuentas con Expiración a 90 días)
- **Objetivo:** Evitar caídas silenciosas de agentes autónomos por vencimiento de tokens de autenticación y migrar progresivamente hacia identidades dedicadas **Microsoft Entra Agent ID** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Agents`, `https://purview.microsoft.com` y `https://entra.microsoft.com > Entra ID > Agent ID` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner / Security Administrator.
- **Procedimiento Paso a Paso:**
  1. Verificar el estado de conexión y fecha próxima de expiración de todos los agentes en Defender, Entra, Intune y Purview (especialmente los agentes de Purview cuya autenticación bajo cuenta de administrador **expira a los 90 días**) `[Verificado MS Learn]`.
  2. Para agentes creados por Microsoft que admiten **Microsoft Entra Agent ID**, verificar que operen con identidad de agente dedicada en lugar de credenciales personales de un administrador `[Verificado MS Learn]`.
  3. Confirmar que el `Threat Intelligence Briefing Agent` con Agent ID mantenga acceso de lectura sobre todos los nuevos *Device Groups* de producción en Defender for Endpoint `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal de agentes activos con fecha de renovación de credenciales >15 días y 0 agentes detenidos por fallo de autenticación `[Decisión / Propuesta Editorial]`.

### S-02: Gobierno semanal del catálogo de Plugins Preinstalados, Custom Plugins y Security Store
- **Objetivo:** Garantizar que solo permanezcan habilitados plugins validados y que ningún colaborador no autorizado pueda publicar plugins personalizados a toda la organización `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Owner > Plugin settings` y `Manage plugins` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner.
- **Procedimiento Paso a Paso:**
  1. Verificar en `Plugin settings` que la opción *Who can add and manage custom plugins for everyone in the organization?* permanezca en **Owners only** `[Verificado MS Learn]`.
  2. Auditar la sección `Custom` de plugins publicados validando manifiestos YAML/JSON, endpoints OpenAPI 3.0/3.0.1 y esquemas de autenticación (`AAD` / `AADDelegated` / `OAuthAuthorizationCodeFlow`) `[Verificado MS Learn]`.
  3. Revisar que los plugins preinstalados restringidos a `Owners only` no estén degradando involuntariamente experiencias embebidas requeridas por el SOC (ej. `Microsoft Defender XDR` o `Natural Language to KQL`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/registro de configuración de `Plugin settings` e inventario firmado de plugins activos `[Verificado MS Learn]`.

### S-03: Curación y estandarización de la librería corporativa de Promptbooks del SOC
- **Objetivo:** Transformar investigaciones exitosas de la semana en **Promptbooks** reproducibles y depurar prompts obsoletos o ineficientes en consumo de SCUs `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Promptbook library` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Detection Engineer.
- **Procedimiento Paso a Paso:**
  1. Revisar los Promptbooks compartidos con el tenant durante los últimos 7 días, verificando claridad de parámetros de entrada, orden lógico de prompts y ausencia de datos confidenciales hardcodeados `[Verificado MS Learn]`.
  2. Medir en `Usage monitoring` las SCUs promedio consumidas por ejecución de cada Promptbook corporativo, optimizando prompts verbosos `[Verificado MS Learn]`.
  3. Etiquetar y publicar los Promptbooks aprobados para triaje L1/L2 (phishing, compromiso BEC, usuario riesgoso, CVE crítico) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Catálogo versionado de Promptbooks corporativos con costo medio en SCUs documentado `[Decisión / Propuesta Editorial]`.

### S-04: Higiene de endpoints y priorización de parches con Device Offboarding y Vulnerability Remediation Agents
- **Objetivo:** Cerrar brechas de dispositivos fantasma/desalineados entre Intune y Entra ID y acelerar la mitigación de CVEs explotados activamente `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://intune.microsoft.com > Agents > Device Offboarding Agent / Vulnerability Remediation Agent` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Security Manager / Intune Administrator.
- **Procedimiento Paso a Paso:**
  1. Revisar la lista semanal de dispositivos obsoletos o desalineados identificada por el **Device Offboarding Agent** y ejecutar la aprobación administrativa supervisada para su retiro limpio `[Verificado MS Learn]`.
  2. Analizar las priorizaciones de riesgo generadas por el **Vulnerability Remediation Agent** en conjunto con el promptbook **Vulnerability impact assessment** `[Verificado MS Learn]`.
  3. Desplegar políticas de mitigación o actualización validadas con el **Policy Configuration Agent** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de equipos depurados con aprobación humana y planes de remediación CVE ejecutados `[Verificado MS Learn]`.

### S-05: Caza proactiva semanal asistida por Sentinel MCP Server y Security Analyst Agent sobre Data Lake
- **Objetivo:** Ejecutar hipótesis avanzadas de caza de amenazas combinando lenguaje natural y herramientas MCP sobre **Microsoft Sentinel Data Lake** y Defender XDR `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting`, `Security Analyst Agent` y clientes conectados a **Microsoft Sentinel MCP Server** `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / SOC L3.
- **Procedimiento Paso a Paso:**
  1. Ejecutar análisis estadísticos semanales (clustering de conexiones salientes anómalas, anomalías de inicio de sesión, correlación de password spray) mediante el **Security Analyst Agent** y las colecciones de herramientas del **Sentinel MCP Server** `[Verificado MS Learn]`.
  2. Validar que el workspace predeterminado (*default workspace*) del plugin `Microsoft Sentinel` en Security Copilot apunte al workspace primario de producción `[Verificado MS Learn]`.
  3. Promover los hallazgos positivos a reglas analíticas NRT/Scheduled o Custom Detection Rules en el portal de Defender `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro semanal de campañas Hunts ejecutadas y nuevas detecciones promovidas `[Decisión / Propuesta Editorial]`.

### S-06: Auditoría de sesiones compartidas (*Shared Sessions*) y cargas de archivos en DSPM for AI
- **Objetivo:** Prevenir exposición interna no deseada de datos sensibles (Purview/Intune/RR. HH.) derivada del mecanismo de enlaces de sesión compartida en solo lectura `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > DSPM for AI > Activity explorer` y `Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Admin / Security Copilot Owner.
- **Procedimiento Paso a Paso:**
  1. Auditar eventos de compartición de sesiones y carga de archivos (`Upload files`) realizados durante la semana `[Verificado MS Learn]`.
  2. Verificar que sesiones que consultaron plugins sensibles de **Microsoft Purview** (eDiscovery, Insider Risk, Communication Compliance) no hayan sido compartidas con usuarios ajenos a la investigación (dado que la visualización de una sesión compartida no reevalúa el RBAC del plugin origen) `[Verificado MS Learn]`.
  3. Validar en `Owner settings` si el permiso de carga de archivos para `Contributors` debe mantenerse activo o restringirse según política de seguridad de datos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Revisión semanal de actividades en Purview DSPM for AI sin exposiciones laterales de información sensible `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Cierre mensual FinOps de capacidad SCU (400 SCUs/1.000 E5-E7 vs. Provisioned/Overage Azure)
- **Objetivo:** Optimizar la eficiencia financiera del consumo mensual de IA de seguridad, reconciliando el uso real de la bolsa incluida en M365 E5/E7 y ajustando compromisos en Azure `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Usage monitoring` y `https://portal.azure.com > Cost Management + Billing` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner / FinOps Lead / SOC Manager.
- **Procedimiento Paso a Paso:**
  1. Exportar a Excel los últimos 30 días de `Usage monitoring` desglosando consumo por experiencia (`Standalone`, `Embedded`, `Azure Logic Apps`), categoría (`Prompt`, `Promptbook`, `Agent`, `Primitive`), plugin e iniciador `[Verificado MS Learn]`.
  2. Calcular el porcentaje de utilización de la **Default Security Copilot Capacity** (`400 SCUs * [licencias E5-E7 / 1.000]`, máx. `10.000 SCUs/mes`), recordando que las unidades no utilizadas expiran al cierre mensual sin rollover `[Verificado MS Learn]`.
  3. Si el tenant consume regularmente por encima de la dotación incluida, comparar el costo de escalado Pay-As-You-Go ($6 USD/SCU) frente al dimensionamiento de `Provisioned SCUs` + tope de `Overage SCUs` en horas pico del SOC `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe ejecutivo mensual FinOps de costo por incidente investigado y utilización de SCUs `[Decisión / Propuesta Editorial]`.

### M-02: Recertificación mensual de Security Copilot Owners, grupo `Recommended roles` y exclusión de `Everyone`
- **Objetivo:** Asegurar mínimo privilegio estricto en el acceso a la plataforma y auditar los roles que heredan propiedad automática `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Home menu > Role assignment` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner / Identity Governance Admin.
- **Procedimiento Paso a Paso:**
  1. Confirmar que el grupo legado `Everyone` no esté asignado a `Copilot contributor` (y si aún existiera en tenants antiguos, removerlo definitivamente tras asignar `Recommended Microsoft Security roles` o Role-assignable groups dedicados) `[Verificado MS Learn]`.
  2. Auditar la lista de usuarios y roles que heredan **Security Copilot owner** (verificando que haya al menos **2 owners** activos, pero removiendo herencias innecesarias según política de mínimo privilegio) `[Verificado MS Learn]`.
  3. Verificar aplicación de políticas de **Microsoft Entra Conditional Access** para proteger el acceso a servicios de IA y Security Copilot (`Protect AI with Conditional Access policy`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura auditada de `Role assignment` y cumplimiento 100 % MFA resistente al phishing sobre usuarios de Copilot `[Verificado MS Learn]`.

### M-03: Auditoría mensual de Privacidad, Residencia Geográfica, Acceso M365 y Retención Purview Audit
- **Objetivo:** Verificar que ninguna configuración crítica de privacidad o auditoría en `Owner settings` haya sufrido deriva (*configuration drift*) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Owner > Owner settings` y `https://purview.microsoft.com > Audit > Audit retention policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Copilot Owner / GRC & Privacy Officer.
- **Procedimiento Paso a Paso:**
  1. Confirmar en `Owner settings` que las dos casillas de compartición de Customer Data para revisión humana de Microsoft permanezcan en **Off** (salvo autorización escrita de GRC) `[Verificado MS Learn]`.
  2. Verificar la ubicación configurada de evaluación GPU (`EU`, `US`, `UK`, `ANZ` o global) y confirmar que `Logging audit data in Microsoft Purview` esté en **On** `[Verificado MS Learn]`.
  3. Validar en Microsoft Purview que las políticas de retención de auditoría extiendan el período por defecto de **180 días** a >= 365 días para registros `CopilotInteraction` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Checklist mensual de privacidad y retención firmado por Seguridad y Cumplimiento `[Decisión / Propuesta Editorial]`.

### M-04: Evaluación mensual de calidad, precisión y ROI operativo de Agentes y Promptbooks
- **Objetivo:** Medir la reducción real de MTTA/MTTR y auditar la tasa de respuestas marcadas como `Needs improvement` o `Inappropriate` por los analistas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com`, `https://entra.microsoft.com`, `https://intune.microsoft.com`, `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager / Detection Engineering Lead.
- **Procedimiento Paso a Paso:**
  1. Consolidar métricas de desempeño de cada agente desplegado: volumen de alertas triadas, porcentaje de coincidencia con revisión humana L2 y tiempo ahorrado por analista `[Decisión / Propuesta Editorial]`.
  2. Revisar casos donde los analistas reportaron alucinaciones, omisiones o errores KQL (`Needs improvement`) para ajustar instrucciones de agentes custom, descripciones de plugins (`DescriptionForModel`) o plantillas de Promptbooks `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tablero mensual de calidad y precisión de IA en SecOps presentado al CISO `[Decisión / Propuesta Editorial]`.

### M-05: Revisión de seguridad de Agentes Custom, conexiones Logic Apps y herramientas MCP en VS Code / Foundry
- **Objetivo:** Auditar el ciclo de desarrollo seguro de agentes propios y conectores externos asegurando ausencia de credenciales expuestas o *skill collisions* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com > Manage plugins > Custom`, `portal.azure.com > Logic apps` y repositorios de manifiestos YAML `[Verificado MS Learn]`.
- **Rol Responsable:** AI Security Engineer / Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Auditar todos los manifiestos `manifest.yaml` / `plugin.yaml` desplegados en el mes, verificando restricciones de `AgentSingleInstanceConstraint` (`Workspace` o `Tenant`), intervalos `DefaultPeriodSeconds` en `Triggers` y ausencia de esquemas legados como `OAuthPasswordGrantFlow` `[Verificado MS Learn]`.
  2. Revisar configuraciones `mcp.json` y accesos al **Microsoft Sentinel MCP Server** asegurando que solo desarrolladores e ingenieros autorizados con `Security Reader` o superior mantengan sesiones activas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de revisión de código/manifiestos YAML y control de integraciones MCP/Logic Apps `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Renovación preventiva de credenciales de Agentes (<90 días) y revisión de permisos de Agent IDs
- **Objetivo:** Renovar antes del día 75 todas las autenticaciones de agentes atadas a cuentas de administrador (como los agentes de Purview que caducan a los 90 días) y recertificar permisos de **Microsoft Entra Agent IDs** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com`, `https://security.microsoft.com > Security Copilot > Agents` y `https://entra.microsoft.com > ID Governance > Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** Security Administrator / Purview Content Analyst / Identity Governance Admin.
- **Procedimiento Paso a Paso:**
  1. Ejecutar rotación/renovación planificada de la autenticación en *DLP Alert Triage Agent*, *Insider Risk Management Triage Agent* y cualquier agente conectado mediante cuenta de usuario antes de alcanzar su expiración de **90 días** `[Verificado MS Learn]`.
  2. Ejecutar campaña trimestral de Access Reviews sobre los permisos y grupos asignados a cada identidad **Microsoft Entra Agent ID** de Security Copilot `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro trimestral de renovación preventiva sin interrupción de servicio y actas de recertificación de Agent IDs `[Verificado MS Learn]`.

### T-02 (Trimestral): Evaluación de nuevos Agentes y ofertas de Partners en Microsoft Security Store
- **Objetivo:** Incorporar de manera gobernada nuevas capacidades agénticas GA/Preview publicadas por Microsoft o socios certificados en **Security Store** (`https://securitystore.microsoft.com`) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitystore.microsoft.com` y `https://security.microsoft.com > Security Copilot > Security Store` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager / Security Architect / FinOps.
- **Procedimiento Paso a Paso:**
  1. Evaluar trimestralmente novedades del catálogo oficial (verificando requisitos de licencia SaaS de terceros en Security Store y recordando que las capacidades GA y Public Preview consumen SCUs) `[Verificado MS Learn]`.
  2. Ejecutar piloto acotado de 14 días en un workspace o alcance controlado midiendo consumo de SCUs y valor operativo antes de pasar a producción `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Ficha de evaluación arquitectónica, de privacidad y FinOps por cada nuevo agente adoptado `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Ejercicio de AI Red Teaming (XPIA, Jailbreak, Fuga en Shared Sessions y Abuso de Plugins)
- **Objetivo:** Validar empíricamente la resistencia de los flujos del SOC, plugins custom y agentes frente a ataques adversarios dirigidos contra sistemas de IA de seguridad `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Entorno controlado de pruebas en `https://securitycopilot.microsoft.com`, `https://security.microsoft.com` y `https://purview.microsoft.com > DSPM for AI` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Red Team / SOC L3 / AI Security Engineer.
- **Procedimiento Paso a Paso:**
  1. Simular artefactos de prueba benignos que contengan instrucciones ocultas de **Cross Prompt Injection Attack (XPIA)** (ej. en cabeceras de correo de phishing simulado o comentarios de scripts) para verificar que `XPIADetected` se registre en Purview Audit y que el analista/agente no ejecute acciones inducidas `[Verificado MS Learn]`.
  2. Probar controles de detección `JailbreakDetected`, sanitización de entradas en plugins OpenAPI/KQL custom y alertas SIEM ante compartición indebida de sesiones `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral de AI Red Teaming con validación de telemetría en Purview UAL / DSPM for AI y remediación de hallazgos `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión estratégica anual de Arquitectura Agéntica, Acceso Multitenant (GDAP/Lighthouse/B2B) y Cumplimiento RAI
- **Objetivo:** Auditar integralmente el gobierno de Security Copilot frente a NIST CSF 2.0, NIST AI RMF 1.0 y Microsoft Responsible AI, incluyendo modelos multitenant o MSSP `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://securitycopilot.microsoft.com`, `https://entra.microsoft.com` y `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO / GRC Lead / SOC Director.
- **Procedimiento Paso a Paso:**
  1. Auditar todos los accesos multitenant externos (cuentas B2B con *Tenant Switching*, **GDAP** en Partner Center o **Azure Lighthouse**) revocando delegaciones obsoletas `[Verificado MS Learn]`.
  2. Revisar políticas de retención e inactividad (recordando que sesiones inactivas >180 días se eliminan automáticamente) y validar procedimientos de respuesta a solicitudes GDPR/DSR mediante soporte oficial `[Verificado MS Learn]`.
  3. Actualizar el plan anual de capacidad SCU (inclusión M365 E5/E7 vs. crecimiento de agentes autónomos 24x7) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Dictamen anual de Gobierno de IA en Ciberseguridad aprobado por el CISO y Comité de Riesgos `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Respuesta ante Agotamiento o Bloqueo de Capacidad SCU durante un Incidente Mayor (*Major Incident SCU Surge*)
- **Disparador:** Notificación en barra de prompts de proximidad al límite o mensaje de bloqueo al alcanzar el **100 % de capacidad** (*Provisioned + Overage* o agotamiento de bolsa mensual) en medio de una investigación crítica `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://securitycopilot.microsoft.com > Owner settings / Usage monitoring > Change units` o `https://portal.azure.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Identificar en `Usage monitoring` si el pico proviene de ejecuciones automatizadas masivas (`Type == Automated Action`, Logic Apps o agentes no prioritarios) y pausar temporalmente dichos triggers secundarios `[Verificado MS Learn]`.
  2. El `Azure Capacity Owner / Contributor` (con rol `Security Copilot Owner`) ejecuta **Change units** incrementando inmediatamente las `Overage SCUs` o `Provisioned SCUs` (considerando hasta **30 minutos** de propagación) o habilita escalado Pay-As-You-Go ($6 USD/SCU) sobre la capacidad incluida `[Verificado MS Learn]`.
  3. Una vez estabilizado y cerrado el incidente mayor, reducir las `Provisioned SCUs` al inicio de una hora reloj exacta para evitar cargos por bloques horarios dobles `[Verificado MS Learn]`.
- **Evidencia Auditable:** Ticket de emergencia FinOps/SOC y traza de ajuste de unidades en Azure Activity Log `[Verificado MS Learn]`.

### AH-02: Contención ante Detección de Cross-Prompt Injection (XPIA) o Comportamiento Anómalo de un Agente / Plugin Custom
- **Disparador:** Alerta en Purview Audit / Sentinel con `XPIADetected == true` o `JailbreakDetected == true`, o acción/veredicto errático producido por un agente o plugin personalizado `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://securitycopilot.microsoft.com > Agents / Manage plugins` y `https://purview.microsoft.com > DSPM for AI` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Desactivar inmediatamente el toggle del **agente** afectado o eliminar/restringir a `Owners only` el **plugin personalizado** sospechoso (acción de efecto inmediato sobre experiencias standalone y embedded) `[Verificado MS Learn]`.
  2. Si el agente opera con un **Microsoft Entra Agent ID**, deshabilitar su identidad o revocar sus permisos en el centro de administración de Microsoft Entra `[Verificado MS Learn]`.
  3. Extraer en **Microsoft Purview DSPM for AI** (`Activity explorer`) el par completo prompt/respuesta y el recurso origen que contenía el payload XPIA para análisis forense y revertir cualquier cambio o clasificación errónea inducida `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de desactivación inmediata en Purview UAL (`DeletePlugin` / `UpdateTenantSettings`) e informe forense del artefacto XPIA `[Verificado MS Learn]`.

### AH-03: Remediación de Fuga Interna de Datos Sensibles por Compartición Indebida de Sesión (*Shared Session Exposure*)
- **Disparador:** Un analista comparte accidentalmente un enlace de sesión de Security Copilot que contiene datos confidenciales de Purview (DLP/IRM/eDiscovery) o recursos restringidos con destinatarios internos sin autorización de negocio `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://securitycopilot.microsoft.com` (gestión de la sesión por su creador) y `https://purview.microsoft.com > Audit` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Instruir de inmediato al creador original de la sesión para revocar el acceso compartido o eliminar la sesión (recordando que solo el creador controla quién accede al enlace y que el reenvío a terceros por otros usuarios no concede acceso) `[Verificado MS Learn]`.
  2. Si se requiere purga definitiva de Customer Data sensible almacenado en la plataforma, iniciar solicitud formal de eliminación desde el portal o soporte de Security Copilot (eliminación completada dentro de **30 días**) `[Verificado MS Learn]`.
  3. Auditar en Purview UAL todos los usuarios que accedieron a la sesión durante la ventana de exposición y documentar evaluación de impacto de privacidad `[Verificado MS Learn]`.
- **Evidencia Auditable:** Confirmación de eliminación de sesión y bitácora de accesos auditada en Purview UAL `[Verificado MS Learn]`.

### AH-04: Evaluación de Impacto Zero-Day en Menos de 30 Minutos con Promptbooks MDTI y Vulnerability Impact Assessment
- **Disparador:** Divulgación pública de una vulnerabilidad crítica Zero-Day explotada activamente o boletín urgente de un actor de amenazas dirigido al sector `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://securitycopilot.microsoft.com > Promptbook library` e `https://intune.microsoft.com > Agents` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ejecutar el promptbook **Vulnerability impact assessment** ingresando el `CVEID` y el promptbook **Check impact of an external threat article** / **Threat Intelligence 360 report based on MDTI article** `[Verificado MS Learn]`.
  2. Ejecutar las consultas KQL generadas sobre Defender XDR y Microsoft Sentinel para identificar activos expuestos e indicadores de compromiso históricos en el Data Lake `[Verificado MS Learn]`.
  3. Activar el **Vulnerability Remediation Agent** en Intune para priorizar el despliegue de parches o controles compensatorios y generar reporte ejecutivo inmediato para el CISO `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte ejecutivo de exposición Zero-Day generado en <30 minutos y plan de mitigación lanzado en Intune/Defender `[Decisión / Propuesta Editorial]`.

### AH-05: Baja Segura de Capacidad o Desconexión deAcceso a Datos M365 ante Requerimiento Regulatorio
- **Disparador:** Orden regulatoria de soberanía de datos, cambio de arquitectura corporativa o desinversión de un tenant `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://securitycopilot.microsoft.com > Owner settings > Change > Delete the capacity` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Si el requerimiento se limita a impedir consultas sobre datos M365/Purview, desactivar en `Owner settings` la opción *Allow Security Copilot to access data from your Microsoft 365 services* y solicitar purga expresa si se requiere borrado en **30 días** antes de la retención estándar `[Verificado MS Learn]`.
  2. Si se requiere exportación previa al cierre total, contactar a **Security Copilot Support** antes de borrar la capacidad `[Verificado MS Learn]`.
  3. Con rol mínimo `Security Administrator`, ejecutar `Delete the capacity` sabiendo que es una acción permanente e irreversible que elimina todos los Customer Data asociados en un máximo de **180 días** (o 30 días bajo solicitud expresa) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Ticket oficial de soporte Microsoft y acta de baja regulatoria firmada `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Auditoría Purview y Artefactos de Verificación

#### Consulta 1 (KQL — Microsoft Sentinel `OfficeActivity` / CloudAppEvents): Auditoría de interacciones y operaciones administrativas en Security Copilot
Rastrea quién interactúa con Security Copilot, desde qué host embebido o standalone, qué plugins/agentes invoca y qué cambios administrativos ocurren `[Verificado MS Learn]`.

```kql
// Plataforma: Microsoft Sentinel / Defender XDR Advanced Hunting (con ingesta UAL / CloudAppEvents)
// Filtro sobre registros de Microsoft Purview Audit (Workload == Copilot, AppIdentity SecurityCopilot)
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType in ("CopilotInteraction", "UpdateTenantSettings", "CreatePlugin", "DeletePlugin", "EnablePromptBook")
| extend AppIdentity = tostring(RawEventData.AppIdentity),
         AppHost = tostring(RawEventData.AppHost),
         AgentName = tostring(RawEventData.AgentName)
| where AppIdentity has "SecurityCopilot" or AppHost in ("Copilot in Defender", "Copilot in Intune", "Security Copilot")
| summarize TotalEventos = count(), PluginsUsados = make_set(tostring(RawEventData.AISystemPlugin), 10)
    by AccountDisplayName, ActionType, AppHost, AgentName, bin(Timestamp, 1d)
| order by Timestamp desc
```

#### Consulta 2 (KQL — Microsoft Sentinel / Defender XDR): Detección de ataques XPIA (`XPIADetected`) e intentos de `JailbreakDetected` en sesiones de Copilot
Identifica alertas de seguridad sobre el propio uso de IA cuando un recurso analizado intenta inyectar instrucciones ocultas (XPIA) o un usuario ejecuta un prompt de jailbreak `[Verificado MS Learn]`.

```kql
// Plataforma: Microsoft Sentinel / Defender XDR Advanced Hunting
// Inspección de banderas XPIADetected (en AccessedResources) y JailbreakDetected (en Messages)
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType == "CopilotInteraction"
| extend AppIdentity = tostring(RawEventData.AppIdentity)
| where AppIdentity has "SecurityCopilot" or tostring(RawEventData.AppHost) startswith "Copilot in "
| extend Resources = RawEventData.AccessedResources, Msgs = RawEventData.Messages
| mv-expand Resource = Resources
| mv-expand Msg = Msgs
| extend XPIA = tobool(Resource.XPIADetected), Jailbreak = tobool(Msg.JailbreakDetected)
| where XPIA == true or Jailbreak == true
| project Timestamp, AccountDisplayName, AppIdentity, XPIA, Jailbreak,
    ResourceName = tostring(Resource.Name), ResourceId = tostring(Resource.ID)
| order by Timestamp desc
```

#### Consulta 3 (KQL — Azure Monitor `AzureActivity`): Trazabilidad de cambios sobre recursos de Capacidad SCU en Azure
Audita creaciones, escalamientos de unidades `Provisioned`/`Overage` o intentos de eliminación de capacidades de Security Copilot en suscripciones Azure `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AzureActivity (Operaciones sobre capacidades de Security Copilot en Azure)
AzureActivity
| where TimeGenerated > ago(30d)
| where ResourceProviderValue =~ "MICROSOFT.SECURITYCOPILOT" or OperationNameValue has "securityCopilot" or Resource has " capacities"
| where ActivityStatusValue in ("Succeeded", "Failed")
| project TimeGenerated, Caller, OperationNameValue, ActivityStatusValue, SubscriptionId, ResourceGroup, _ResourceId
| order by TimeGenerated desc
```

#### Consulta 4 (KQL — Log Analytics / Sentinel `AuditLogs`): Gobernanza de identidades `Microsoft Entra Agent ID` creadas para Agentes de Security Copilot
Monitorea el alta, modificación de permisos, asignación de credenciales o deshabilitación de identidades de agentes en Microsoft Entra ID `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Seguimiento de identidades de agentes y service principals asociados a Security Copilot)
AuditLogs
| where TimeGenerated > ago(30d)
| where Category in ("ApplicationManagement", "RoleManagement", "DirectoryManagement")
| mv-expand TargetResources
| where tostring(TargetResources.displayName) has_any ("Agent", "Security Copilot", "Conditional Access Optimization", "Triage")
| project TimeGenerated, Category, OperationName, Result,
    InitiatedByUser = coalesce(tostring(InitiatedBy.user.userPrincipalName), tostring(InitiatedBy.app.displayName)),
    TargetName = tostring(TargetResources.displayName), TargetType = tostring(TargetResources.type)
| order by TimeGenerated desc
```

#### Consulta 5 (Exchange Online / Purview Audit PowerShell): Extracción forense directa del Unified Audit Log para `CopilotInteraction`
Script oficial de auditoría para extraer registros de interacciones y administración de Security Copilot directamente desde Microsoft Purview UAL `[Verificado MS Learn]`.

```powershell
# Módulo requerido: ExchangeOnlineManagement (Rol Purview Audit Reader)
Connect-ExchangeOnline -ShowBanner:$false

$Start = (Get-Date).AddDays(-7)
$End   = Get-Date

Search-UnifiedAuditLog -StartDate $Start -EndDate $End -RecordType CopilotInteraction -ResultSize 1000 |
    ForEach-Object {
        $Audit = $_.AuditData | ConvertFrom-Json
        if ($Audit.AppIdentity -like '*SecurityCopilot*' -or $Audit.AppHost -like 'Copilot in *') {
            [PSCustomObject]@{
                CreationTime = $_.CreationDate
                UserIds      = $_.UserIds
                Operation    = $_.Operations
                AppIdentity  = $Audit.AppIdentity
                AppHost      = $Audit.AppHost
                AgentId      = $Audit.AgentId
                AgentName    = $Audit.AgentName
            }
        }
    } | Format-Table -AutoSize
```

#### Consulta 6 (Manifiesto YAML Verificado): Plantilla de Agente Custom con Skills `AGENT`, `GPT` (`gpt-4.1`) y `KQL` (`Sentinel`)
Artefacto declarativo alineado a la especificación oficial de `agent-manifest.md` para auditar y desplegar un agente personalizado sin credenciales embebidas `[Verificado MS Learn]`.

```yaml
Descriptor:
  Name: SecOps.SentinelHighSevTriage
  DisplayName: Sentinel High Severity Triage Helper
  Description: Agente interno gobernado para resumir incidentes High en Sentinel

SkillGroups:
  - Format: KQL
    Skills:
      - Name: FetchRecentHighIncidents
        DisplayName: Fetch Recent High Incidents
        Description: Obtiene los ultimos 10 incidentes de severidad High en Microsoft Sentinel
        Settings:
          Target: Sentinel
          TenantId: '{{TenantId}}'
          SubscriptionId: '{{SubscriptionId}}'
          ResourceGroupName: '{{ResourceGroupName}}'
          WorkspaceName: '{{WorkspaceName}}'
          Template: SecurityIncident | where TimeGenerated > ago(1h) and Severity == 'High' and Status == 'New' | take 10 | project IncidentNumber, Title, Classification
  - Format: AGENT
    Skills:
      - Name: AnalyzeHighIncidentEntrypoint
        Description: Sintetiza contexto prioritario para el analista L1
        Interfaces:
          - Agent
        Inputs:
          - Name: IncidentNumber
            Description: Numero de incidente en Sentinel
            Required: true
        Settings:
          Model: gpt-4.1
          Instructions: |
            Analiza el incidente {{IncidentNumber}}, resume entidades criticas y sugiere tres pasos de verificacion humana sin ejecutar contencion automatica.
        ChildSkills:
          - FetchRecentHighIncidents

AgentDefinitions:
  - Name: SentinelHighSevTriageAgent
    DisplayName: Sentinel High Severity Triage Agent
    Description: Asistente programado cada 15 minutos para pre-triaje de incidentes High
    Publisher: EnterpriseSecOps
    Product: SecurityOperations
    RequiredSkillsets:
      - SecOps.SentinelHighSevTriage
    AgentSingleInstanceConstraint: Workspace
    Triggers:
      - Name: Default
        DefaultPeriodSeconds: 900
        FetchSkill: SecOps.SentinelHighSevTriage.FetchRecentHighIncidents
        ProcessSkill: SecOps.SentinelHighSevTriage.AnalyzeHighIncidentEntrypoint
```

#### Consulta 7 (Microsoft Graph PowerShell): Verificación de licencias elegibles M365 E5 / E7 para calcular la dotación mensual incluida de SCUs
Calcula automáticamente la bolsa mensual esperada (`400 SCUs por cada 1.000 asientos pagos`, con tope de `10.000 SCUs/mes`) en el tenant `[Verificado MS Learn]`.

```powershell
# Módulo requerido: Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "Organization.Read.All"

$EligibleSkus = Get-MgSubscribedSku | Where-Object {
    $_.SkuPartNumber -match "SPE_E5|M365_E5|SPE_E7|M365_E7" -and $_.CapabilityStatus -eq "Enabled"
}
$TotalPaidSeats = ($EligibleSkus.PrepaidUnits.Enabled | Measure-Object -Sum).Sum
$CalculatedSCUs = [Math]::Min(10000, [Math]::Round(($TotalPaidSeats / 1000.0) * 400, 1))

[PSCustomObject]@{
    TotalEligibleE5E7Seats = $TotalPaidSeats
    MonthlyIncludedSCUs    = $CalculatedSCUs
    MonthlyCapApplied      = ($CalculatedSCUs -eq 10000)
}
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Capacidad | Fuente Primaria de Verificación | Condición de Salud ("Proof of Life") | Frecuencia | Estado |
| --- | --- | --- | --- | --- |
| **Capacidad SCU & Inclusión E5/E7** | `securitycopilot.microsoft.com > Owner settings > Usage monitoring` | *Default Security Copilot Capacity* visible y activa, consumo <85 % de cuota proyectada y 0 eventos de bloqueo al 100 %. | Diaria | `[Verificado MS Learn]` |
| **Privacidad y Soberanía** | `securitycopilot.microsoft.com > Owner settings` | Ambas opciones de compartición para revisión humana en `Off`, ubicación GPU conforme a política regional y logging Purview en `On`. | Mensual | `[Verificado MS Learn]` |
| **RBAC de Plataforma** | `securitycopilot.microsoft.com > Role assignment` | Mínimo 2 `Copilot owners` verificados, grupo `Everyone` removido y acceso gobernado por `Recommended roles` o Role-assignable groups. | Mensual | `[Verificado MS Learn]` |
| **Agentes Autónomos Activos** | Portales `Defender`, `Entra`, `Intune`, `Purview > Agents` | Agentes productivos autenticados (preferentemente con `Entra Agent ID`; cuentas Purview renovadas <75 días) y procesando triggers sin error. | Semanal | `[Verificado MS Learn]` |
| **Auditoría UAL & DSPM for AI** | `purview.microsoft.com > Audit` y `DSPM for AI > Activity explorer` | Eventos `CopilotInteraction` fluyendo en tiempo y forma, retención >=365 días y monitoreo activo de `XPIADetected` / `JailbreakDetected`. | Diaria | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales y Ejecutivos

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Clasificación |
| --- | --- | --- | --- | --- | --- | --- |
| **KPI-01** | **Reducción de MTTR en Incidentes Asistidos por Security Copilot** | `((MTTR_SinCopilot - MTTR_ConCopilot) / MTTR_SinCopilot) * 100` sobre incidentes de severidad High/Medium | `>= 30 %` de reducción sostenida | Mensual | CISO, SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Eficiencia de Utilización de la Bolsa Mensual SCU Incluida en M365 E5/E7** | `(SCUs consumidas en el mes sobre Default Capacity / Dotación mensual incluida [400 SCUs por 1.000 E5/E7]) * 100` | `70 % – 92 %` (aprovechamiento óptimo sin throttling inesperado) | Semanal / Mensual | FinOps, Security Copilot Owner | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Concordancia Analítica de Agentes de Triaje (Defender / Purview)** | `(Veredictos de Alert Triage Agents confirmados sin corrección por analistas L2 / Total de veredictos auditados) * 100` | `>= 94 %` | Semanal | SOC Manager, Purview Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Disponibilidad Continua de Autenticación de Agentes Autónomos** | `(Horas operativas reales de agentes activos sin caída por expiración de token/cuenta / Horas programadas del mes) * 100` | `100 %` (0 caídas por expiración de 90 días) | Semanal | Security Administrator, SOC Ops | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Adopción de Microsoft Entra Agent ID en Agentes Soportados** | `(Agentes Microsoft desplegados usando Microsoft Entra Agent ID dedicado / Total de agentes Microsoft desplegados que soportan Agent ID) * 100` | `100 %` | Mensual | Identity Architect, AI Security | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Cobertura de Auditoría Purview UAL y DSPM for AI** | `(Workspaces de Security Copilot con Logging audit data in Microsoft Purview = On + política DSPM for AI activa / Total de Workspaces) * 100` | `100 %` | Mensual | GRC, Data Security Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tiempo de Triaje de Alertas XPIA / Jailbreak sobre Security Copilot** | `Mediana(Timestamp_InicioInvestigacionSOC - Timestamp_EventoXPIAoJailbreakEnAudit)` | `< 30 min` | Diaria | SOC L2, AI Security Engineer | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Tasa de Calidad Percibida en Respuestas y Promptbooks (`Looks Right` Ratio)** | `(Evaluaciones 'Looks right' registradas por analistas / Total de evaluaciones de feedback emitidas en el mes) * 100` | `>= 90 %` | Mensual | SOC L3, Detection Engineering | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Caracterización Operativa en Microsoft Security Copilot |
| --- | --- | --- |
| **Nivel 1** | **Ad-Hoc / Exploratorio** | Tenant auto-aprovisionado con configuración por defecto sin revisar; uso esporádico de prompts libres en portal standalone; sin telemetría DSPM for AI ni control diario de SCUs. |
| **Nivel 2** | **Asistido Básico** | Grupo `Everyone` eliminado, `Owner settings` endurecidos (`Off` en compartición humana, `On` en Purview Audit), analistas L1/L2 usando resúmenes de incidentes y NL2KQL embebidos en Defender XDR. |
| **Nivel 3** | **Estandarizado Multi-Dominio** | Librería corporativa de **Promptbooks** curada, integración activa con **Microsoft Sentinel**, **Entra**, **Intune** y **Purview**, monitoreo FinOps semanal de la dotación de 400 SCUs/1.000 usuarios y validación humana anti-overreliance documentada. |
| **Nivel 4** | **Operación Agéntica Gobernada** | Despliegue en producción de agentes especializados (*Phishing/Alert Triage*, *CA Optimization*, *TI Briefing*, *Intune Change/Vuln*, *Purview DLP/IRM Triage*) autenticados con **Microsoft Entra Agent ID**, renovación preventiva <75 días y detección SIEM de XPIA/Jailbreak. |
| **Nivel 5** | **SOC Agéntico Frontier** | Desarrollo seguro de agentes custom declarativos YAML (`gpt-4.1` + KQL + OpenAPI), uso avanzado de **Microsoft Sentinel MCP Server** sobre Sentinel Data Lake, ejercicios semestrales de **AI Red Teaming** y optimización continua del costo por investigación. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

El siguiente mapeo alinea las capacidades operativas de Microsoft Security Copilot con las **seis funciones** de **NIST CSF 2.0 (CSWP 29)** y tácticas relevantes de **MITRE ATT&CK v18** / **MITRE ATLAS** `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría Oficial | Descripción del Resultado Normativo | Capacidad Habilitadora en Microsoft Security Copilot | Mitigación MITRE ATT&CK / AI | Evidencia Auditable Reproducible |
| --- | --- | --- | --- | --- | --- |
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales —incluyendo privacidad y soberanía de datos— se comprenden y gestionan. | Selección inmutable de región de Workspace, control de ubicación GPU (`EU`, `US`, `UK`, `ANZ`), desactivación de compartición humana (`Off`) y cero entrenamiento de modelos fundacionales externos. | Protección de soberanía y confidencialidad de telemetría SOC | Captura mensual auditada de `Owner settings` y políticas de retención Purview >=365 días. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad se establecen, comunican y aplican. | Modelo RBAC multicapa (`Copilot Owner` [mín. 2], `Copilot Contributor`, remoción de `Everyone`, autenticación **On-Behalf-Of** y restricción de plugins custom a `Owners only`). | `T1078.004` (Valid Accounts: Cloud Accounts) | Registro mensual de `Role assignment` y `Plugin settings` sin acceso excesivo. |
| **IDENTIFY (ID)** | `ID.RA-01` | Las vulnerabilidades en activos y brechas de postura se identifican, validan y registran. | **Vulnerability Remediation Agent** en Intune, **Conditional Access Optimization Agent** en Entra, promptbook *Vulnerability impact assessment* y análisis en Defender for Cloud. | `T1190` (Exploit Public-Facing Application), `T1078` | Reportes de brechas de Acceso Condicional y priorizaciones CVE generadas y cerradas. |
| **IDENTIFY (ID)** | `ID.RA-02` | Se recibe inteligencia sobre amenazas cibernéticas de fuentes compartidas y se contextualiza internamente. | **Threat Intelligence Briefing Agent**, plugins **MDTI** / **Defender EASM** y promptbooks *Threat actor profile* y *TI 360 report based on MDTI article*. | Reconocimiento y correlación proactiva multi-actor | Briefings programados del agente cruzando IOCs externos con exposición real de endpoints. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso y autorizaciones se gestionan aplicando mínimo privilegio y separación de funciones. | Autenticación OBO estricta en todos los plugins 1P, identidades dedicadas **Microsoft Entra Agent ID** para agentes y evaluación previa de cambios con **Change Review Agent** en Intune. | `T1098` (Account Manipulation) | Inventario de identidades `Entra Agent ID` y bitácora de Multi Admin Approval en Intune. |
| **PROTECT (PR)** | `PR.DS-01` | La confidencialidad, integridad y disponibilidad de los datos en reposo están protegidas. | Controles sobre acceso a servicios M365, aislamiento por usuario de archivos cargados (`Upload files`), gobernanza de *Shared sessions* e inspección con **Purview DSPM for AI**. | `T1530` (Data from Cloud Storage) | Políticas activas en Purview DSPM for AI y auditoría semanal de sesiones compartidas. |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender mejor las actividades asociadas. | **Phishing / Security Alert Triage Agent**, **DLP & IRM Triage Agents** en Purview y **Dynamic Threat Detection Agent** descubriendo falsos negativos entre Defender y Sentinel. | `T1566` (Phishing), `T1567` (Exfiltration Over Web Service) | Veredictos explicados en lenguaje natural de agentes de triaje y alertas dinámicas en Defender. |
| **DETECT (DE)** | `DE.CM-09` | El hardware y software de cómputo, entornos de ejecución y plataformas propias (incluyendo IA) se monitorean continuamente. | Auditoría nativa en **Purview Audit (Standard)** (`CopilotInteraction`), detección de `XPIADetected` / `JailbreakDetected` y monitoreo de capacidades SCU en `AzureActivity`. | Defensa contra Prompt Injection (XPIA / Jailbreak) | Reglas analíticas activas en Microsoft Sentinel sobre `CloudAppEvents` y `AzureActivity`. |
| **RESPOND (RS)** | `RS.AN-03` | Se realiza análisis para establecer qué ocurrió durante un incidente y determinar su causa raíz. | Resúmenes de incidentes XDR+Sentinel, análisis de scripts/archivos maliciosos, **Security Analyst Agent** y exploración con **Microsoft Sentinel MCP Server** sobre Data Lake. | `T1059.001` (PowerShell), `T1027` (Obfuscated Files) | Informes forenses de incidentes y sesiones de caza documentadas con validación analítica. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos oportunamente. | **Guided Response** en Defender XDR, **Identity Risk Management Agent** en Entra y playbook `AH-02` de desactivación inmediata de agentes/plugins ante XPIA o anomalía. | `T1078` (Valid Accounts), contención de agentes IA | Trazas de acciones de respuesta guiada aprobadas por humanos y bitácora de contención en UAL. |
| **RESPOND (RS)** | `RS.CO-02` | Las partes interesadas internas y externas son notificadas de los incidentes con contexto claro. | Generación estructurada de informes ejecutivos para audiencias no técnicas mediante **Create incident reports** y los pasos finales de los promptbooks de investigación. | Comunicación ejecutiva de crisis e incidentes | Reportes ejecutivos exportados y validados adjuntos al cierre formal del incidente. |
| **RECOVER (RC)** | `RC.RP-01` | La parte de recuperación del plan de respuesta a incidentes se ejecuta una vez iniciada desde respuesta. | Rehabilitación controlada de políticas con **Policy Configuration Agent**, restauración de capacidad SCU post-pico (`AH-01`) y reincorporación verificada de agentes tras rotación de credenciales. | `T1490` (Inhibit System Recovery) | Registro de restablecimiento de línea base de capacidad SCU, políticas y agentes post-incidente. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta Oficial Microsoft Learn / Credenciales | Recursos Ninja, Comunidad MVP y Práctica Guiada | Cadencia de Reentrenamiento |
| --- | --- | --- | --- |
| **SOC L1 / L2 Analyst** | - *Get started with Microsoft Security Copilot* y *Prompting in Microsoft Security Copilot* `[Verificado MS Learn]`<br>- *Simulaciones interactivas guiadas de Security Copilot* (`learn.microsoft.com/en-us/training/modules/security-copilot-interactive-guides/`, sin consumir SCUs) `[Verificado MS Learn]`<br>- Certificación asociada: **Exam SC-200** (*Microsoft Security Operations Analyst*) `[Verificado MS Learn]` | - *Microsoft Security Copilot Ninja Training: hacia el SOC agéntico (Edición 2026 — L100 a L300)* `[Verificado MS Learn]`<br>- *Microsoft Security Copilot Adoption Hub* (`adoption.microsoft.com/en-us/security-copilot/`) `[Verificado MS Learn]` | Trimestral |
| **SOC L3 / Threat Hunter / AI Security Engineer** | - *Security Copilot Developer documentation*: *Build custom agents*, *Agent manifest (`YAML`)*, *Custom plugins* y *Get started with Microsoft Sentinel MCP server* `[Verificado MS Learn]` | - Nivel L400 del *Security Copilot Ninja Training* (Promptbooks y Plugins avanzados) + librería comunitaria de prompts de Rod Trent (`github.com/rod-trent/Copilot-for-Security`) `[Verificado MS Learn]` | Trimestral |
| **Identity, Endpoint & Data Security Admins** | - Documentación específica de *Microsoft Entra Agents*, *Security Copilot Agents in Intune* y *Microsoft Security Copilot agents in Microsoft Purview* `[Verificado MS Learn]`<br>- Certificaciones **SC-300**, **MD-102** y **SC-401** `[Verificado MS Learn]` | - Laboratorios guiados de *Conditional Access Optimization Agent*, *Policy Configuration Agent* y configuración de *Purview DSPM for AI* `[Verificado MS Learn]` | Semestral |
| **Security Copilot Owner, FinOps & GRC** | - *Learn about Security Copilot for Microsoft 365 E5 and E7 customers*, *Understand Security Compute Units and capacity*, *Privacy and data security* y *Access the Security Copilot audit log* `[Verificado MS Learn]` | - Blog estratégico oficial *The agentic SOC—Rethinking SecOps for the next decade* (Microsoft Security Blog, abr-2026) y marco **NIST AI RMF 1.0** `[Verificado MS Learn]` | Semestral |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Validaciones Técnicas frente a Microsoft Learn (`2026-11-11`)

| # | Área Validada | Hallazgo Técnico Verificado en Microsoft Learn (Corte Noviembre 2026) | Impacto en la Guía Operacional |
| --- | --- | --- | --- |
| **1** | **Inclusión de SCUs en Microsoft 365 E5 y E7 (2025–2026)** | `security-copilot-inclusion.md` (actualizado jun-2026) y `auto-provisioning-security-copilot.md` confirman la dotación incluida de **400 SCUs/mes por cada 1.000 licencias pagas de usuario** (escalado lineal sin mínimo de asientos, hasta **10.000 SCUs/mes**, sin rollover mensual y con escalado futuro Pay-As-You-Go a **$6 USD/SCU**), aplicable también a **Microsoft Sentinel** para clientes E5/E7 `[Verificado MS Learn]`. | Documentado con precisión matemática en Portada, Sección 2.2, `D-01`, `M-01` y Consulta #7. |
| **2** | **Diferencias clave de Privacidad en Auto-Provisioning E5/E7 vs. Manual** | En tenants M365 E5/E7 auto-aprovisionados, las dos opciones de compartición de Customer Data para revisión humana vienen en **Off** por defecto (mientras que en onboarding manual no-E5 vienen en **On** por defecto); además la región de un Workspace es inmutable tras crearse `[Verificado MS Learn]`. | Reflejado en Sección 2.3 y rutina mensual `M-03`. |
| **3** | **Catálogo consolidado de Agentes en Defender, Entra, Intune y Purview** | Verificados los agentes vigentes al `2026-11-11`: en Defender (*Security Alert / Phishing Triage*, *TI Briefing*, *Threat Hunting Assistant*, *Security Analyst*, *Dynamic Threat Detection*); en Entra (*CA Optimization*, *Identity Risk Management Preview*, *Access Review Agent*); en Intune (*Change Review*, *Device Offboarding*, *Policy Configuration*, *Vulnerability Remediation* — página actualizada el mismo `2026-11-11`); en Purview (*DLP Alert Triage* e *IRM Triage* con expiración de autenticación cada **90 días**) `[Verificado MS Learn]`. | Integrado íntegramente en Sección 3.3 y cadencias diarias, semanales y trimestrales (`T-01`). |
| **4** | **Microsoft Sentinel MCP Server y Especificación YAML `gpt-4.1`** | `sentinel-mcp-get-started.md` (sep-2026) y `mcp-get-started.md` confirman el servidor MCP de Sentinel sobre **Sentinel Data Lake** y el endpoint `https://sentinel.microsoft.com/mcp/security-copilot-agent-creation` en VS Code; `agent-manifest.md` confirma los formatos `AGENT`, `GPT` (`gpt-4.1`), `KQL`, `API` (OpenAPI 3.0/3.0.1) y `LogicApp` `[Verificado MS Learn]`. | Documentado en Sección 3.4, `S-05`, `M-05` y Consulta/Artefacto #6. |
| **5** | **Modelo RBAC On-Behalf-Of, Retención de 2 Owners y Riesgo de `Shared Sessions`** | `authentication.md` (jun-2026) confirma la retención forzosa de 2 owners, la recomendación de eliminar `Everyone` (irreversible) en favor de `Recommended Microsoft Security roles` y advierte que visualizar una **Shared session** no reevalúa el RBAC del plugin origen para el destinatario `[Verificado MS Learn]`. | Incorporado en Sección 4, `S-06`, `M-02` y Playbook `AH-03`. |
| **6** | **Facturación exacta de Provisioned vs. Overage SCUs y capacidades Preview** | `security-compute-units-capacity.md` y `manage-usage.md` confirman bloques horarios reloj fijos en `Provisioned SCUs`, cobro con precisión de **un decimal** en `Overage SCUs`, propagación de ajustes en hasta **30 minutos** y cobro activo tanto en capacidades GA como **Public Preview** (solo Private Preview no cobra) `[Verificado MS Learn]`. | Reflejado en Sección 2.2, `D-01`, `T-02` y Playbook `AH-01`. |
| **7** | **Auditoría en Purview Audit (Standard) sin recargo PAYG y banderas XPIA/Jailbreak** | `purview/audit-copilot.md` (ago-2026) y `copilot/security/audit-log.md` confirman que Security Copilot se incluye en **Audit (Standard)** (180 días por defecto, extensible), emite `AppIdentity: Copilot.Security.SecurityCopilot`, registra `XPIADetected` y `JailbreakDetected`, e integra contenido prompt/respuesta vía **Purview DSPM for AI** `[Verificado MS Learn]`. | Reflejado en `D-06`, `M-03`, `SM-01` y Consultas #1, #2 y #5. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Decidido | Clasificación | Justificación Arquitectónica y Consultiva |
| --- | --- | --- | --- |
| **1** | **Umbral preventivo de alerta FinOps al `85 %` de consumo SCU y banda óptima `70 % – 92 %`** | `[Decisión / Propuesta Editorial]` | Dado que las SCUs incluidas en M365 E5/E7 no tienen rollover mensual y que los ajustes de capacidad Azure tardan hasta 30 minutos, operar en `70 %–92 %` maximiza el beneficio pagado sin sufrir bloqueos al 100 % durante incidentes críticos. |
| **2** | **Renovación preventiva al día `< 75` para agentes autenticados con cuenta de usuario** | `[Decisión / Propuesta Editorial]` | Los agentes de triaje en Purview expiran exactamente a los 90 días; fijar una ventana trimestral anticipada (<75 días) erradica interrupciones no planificadas en el triaje DLP/IRM. |
| **3** | **Metas cuantitativas de los 8 KPIs (`>= 30 %` reducción MTTR, `>= 94 %` concordancia de triaje, `< 30 min` respuesta XPIA)** | `[Decisión / Propuesta Editorial]` | Traduce la adopción de IA generativa y agéntica en métricas auditables de eficacia operativa, calidad analítica y seguridad de la propia IA. |
| **4** | **Ejercicio semestral obligatorio de AI Red Teaming (`SM-01`) sobre XPIA, Jailbreak y Shared Sessions** | `[Decisión / Propuesta Editorial]` | Valida empíricamente los controles recomendados en la *Application Card* de Security Copilot frente a adversarios que intentan manipular el razonamiento del SOC mediante artefactos contaminados. |
| **5** | **Modelo de Madurez de 5 niveles y mapeo probatorio a las 6 funciones de NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Proporciona al CISO y a Auditoría Interna una estructura homogénea con los restantes 22 módulos del repositorio maestro. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *What is Microsoft Security Copilot?* (`https://learn.microsoft.com/en-us/copilot/security/microsoft-security-copilot`) — Verificado `2026-11-11`.
- **REF-02:** Microsoft Learn — *Learn about Security Copilot for Microsoft 365 E5 and E7 customers* (`https://learn.microsoft.com/en-us/copilot/security/security-copilot-inclusion`) — Verificado `2026-11-11` (actualizado `2026-06-19`).
- **REF-03:** Microsoft Learn — *Understand how Security Copilot is auto provisioned for eligible Microsoft 365 E5 and E7 customers* (`https://learn.microsoft.com/en-us/copilot/security/auto-provisioning-security-copilot`) — Verificado `2026-11-11` (actualizado `2026-06-18`).
- **REF-04:** Microsoft Learn — *Microsoft Security Copilot Security Compute Units and capacity* (`https://learn.microsoft.com/en-us/copilot/security/security-compute-units-capacity`) — Verificado `2026-11-11` (actualizado `2026-05-01`).
- **REF-05:** Microsoft Learn — *Manage security compute unit usage in Security Copilot* (`https://learn.microsoft.com/en-us/copilot/security/manage-usage`) — Verificado `2026-11-11` (actualizado `2026-08-05`).
- **REF-06:** Microsoft Learn — *Understand authentication and RBAC in Microsoft Security Copilot* (`https://learn.microsoft.com/en-us/copilot/security/authentication`) — Verificado `2026-11-11` (actualizado `2026-06-06`).
- **REF-07:** Microsoft Learn — *Privacy and data security in Microsoft Security Copilot* (`https://learn.microsoft.com/en-us/copilot/security/privacy-data-security`) — Verificado `2026-11-11` (actualizado `2026-07-13`).
- **REF-08:** Microsoft Learn — *Microsoft Security Copilot experiences (Standalone & Embedded)* (`https://learn.microsoft.com/en-us/copilot/security/experiences-security-copilot`) — Verificado `2026-11-11`.
- **REF-09:** Microsoft Learn — *Microsoft Security Copilot agents overview & Discover Agents* (`https://learn.microsoft.com/en-us/copilot/security/agents-overview`) — Verificado `2026-11-11`.
- **REF-10:** Microsoft Learn — *Deploy AI agents in Microsoft Defender XDR* (`https://learn.microsoft.com/en-us/defender-xdr/security-copilot-agents-defender`) — Verificado `2026-11-11` (actualizado `2026-08-07`).
- **REF-11:** Microsoft Learn — *Microsoft Entra Agents & Security Copilot in Microsoft Entra* (`https://learn.microsoft.com/en-us/entra/security-copilot/entra-agents`) — Verificado `2026-11-11` (actualizado `2026-06-15`).
- **REF-12:** Microsoft Learn — *Security Copilot Agents in Microsoft Intune* (`https://learn.microsoft.com/en-us/intune/copilot/agents/`) — Verificado `2026-11-11` (actualizado `2026-11-11`).
- **REF-13:** Microsoft Learn — *Microsoft Security Copilot agents in Microsoft Purview (DLP & IRM Triage)* (`https://learn.microsoft.com/en-us/purview/copilot-in-purview-agents`) — Verificado `2026-11-11`.
- **REF-14:** Microsoft Learn — *Security Copilot with Microsoft Sentinel & Get started with Microsoft Sentinel MCP server* (`https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-mcp-get-started`) — Verificado `2026-11-11` (actualizado `2026-09-23`).
- **REF-15:** Microsoft Learn — *Manage plugins, Use promptbooks & Agent manifest YAML reference* (`https://learn.microsoft.com/en-us/copilot/security/developer/agent-manifest`) — Verificado `2026-11-11` (actualizado `2026-06-04`).
- **REF-16:** Microsoft Learn — *Access the Security Copilot audit log & Audit logs for Copilot and AI applications* (`https://learn.microsoft.com/en-us/copilot/security/audit-log` y `https://learn.microsoft.com/en-us/purview/audit-copilot`) — Verificado `2026-11-11` (actualizado `2026-08-26`).

### Blogs Oficiales, Empleados de Microsoft y Comunidad MVP
- **REF-17:** Microsoft Security Blog — *The agentic SOC—Rethinking SecOps for the next decade* (`https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/`) — Verificado `2026-11-11`.
- **REF-18:** Rod Trent (Microsoft Cloud Security Advocate) — *Security Copilot Prompt & Plugin Community Library* (`https://github.com/rod-trent/Copilot-for-Security`) — Verificado `2026-11-11`.

### Marcos Normativos
- **REF-19:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`) — Verificado `2026-11-11`.

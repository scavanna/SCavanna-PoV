# Guía Maestra de Excelencia Operacional: Microsoft Purview Suite (Arquitectura Integral, Gobierno, DSPM, Seguridad para IA y Compliance Manager)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
|---|---|
| **Identificador del Módulo** | `13_Microsoft_Purview_Suite_Arquitectura_y_Gobierno` |
| **Slug Canónico** | `Microsoft_Purview_Suite_Arquitectura_y_Gobierno` |
| **Nombre Completo** | Microsoft Purview Suite (Arquitectura Integral, Gobierno, DSPM, Seguridad para IA y Compliance Manager) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | 2.0 — Edición Consolidada y Revalidada |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado `MSEOP-MD` (`Version Consolidada 2 20260420`, `version consolidada 1`, `Purview Gral`, series `e01v01`, `e02v01`, `e03v01`) + `Ninja Training Seguridad Microsoft 2026` (`11_Purview_Compliance_Manager` y `12_Purview_DSPM_y_Seguridad_de_datos_para_IA`) + Revalidado Microsoft Learn MCP (Noviembre 2026) |
| **Relación con Microsoft 365 E5** | **Incluido en Microsoft 365 E5** (y comercializado como complemento independiente bajo el nombre vigente **Microsoft Purview Suite**, que reemplazó a *Microsoft 365 E5 Compliance* desde octubre de 2025, complementado por medidores **Pay-As-You-Go** en Azure para fuentes no-M365, IA de terceros y Data Security Investigations) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (Nuevo portal unificado Microsoft Purview — único portal tras el retiro de `compliance.microsoft.com`), `https://security.microsoft.com` (Correlación XDR, Adaptive Protection, Incidentes DLP/IRM y Sentinel), `https://entra.microsoft.com` (Administrative Units, PIM y Conditional Access) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Chief Data Officer (CDO), DPO / Privacy Officer, Data Security Architect, SOC Manager, Data Security Analyst (DLP/IRM/DSI), GRC & Compliance Manager, AI Governance Lead, FinOps Lead, Internal/External Auditors |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), NIST AI RMF 1.0, ISO/IEC 27001:2022, ISO/IEC 42001:2023, Regulación Europea DORA, Directiva NIS2, EU Artificial Intelligence Act (EU AI Act), GDPR y Microsoft Zero Trust (Pilar Data) |

> **Nota de consolidación y rol de módulo paraguas:** En el material histórico de `MSEOP-MD`, el corpus general de Purview abordaba principalmente licenciamiento estratégico y casos de uso ejecutivos sin un modelo operativo SOC/DataSec estructurado por cadencias. Esta guía v2.0 subsana esa brecha estableciendo el **marco maestro de arquitectura, gobierno transversal, gestión de postura de seguridad de datos (DSPM unificado y seguridad para IA / agentes), investigaciones asistidas por IA (Data Security Investigations), gestión continua de cumplimiento normativo (Compliance Manager) y control financiero Pay-As-You-Go**, articulando además la operación coordinada con los ocho módulos especializados subsiguientes del repositorio: **Módulo `14` (Information Protection)**, **Módulo `15` (Data Loss Prevention)**, **Módulo `16` (Data Lifecycle & Records Management)**, **Módulo `17` (Insider Risk Management)**, **Módulo `18` (Communication Compliance)**, **Módulo `19` (Audit Premium)**, **Módulo `20` (eDiscovery Premium)** y **Módulo `21` (Customer Lockbox, Customer Key y M365 PAM)**, así como con el **Módulo `22` (Microsoft Agent 365)** `[Verificado MS Learn]`. Se distinguen estrictamente hechos documentados con `[Verificado MS Learn]` frente a SLAs, metas de KPIs, matrices RACI y criterios consultivos con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 De "E5 Compliance" a Microsoft Purview Suite: Seguridad, Gobierno y Cumplimiento Centrados en el Dato y la IA

En la arquitectura **Zero Trust** de Microsoft, todos los controles de identidad, endpoints, aplicaciones e infraestructura convergen en un único propósito último: **proteger y gobernar los datos organizacionales dondequiera que residan, se muevan o sean procesados por humanos y agentes de IA** `[Verificado MS Learn]`. A noviembre de 2026, **Microsoft Purview** consolida en una sola plataforma (`https://purview.microsoft.com`) tres dominios históricamente aislados `[Verificado MS Learn]`:

1. **Data Security (Seguridad de Datos Proactiva y Adaptativa):** Descubrimiento y evaluación continua de postura mediante la nueva experiencia unificada de **Data Security Posture Management (DSPM)** (con objetivos guiados *Data security objectives*, *AI observability* sobre **Microsoft 365 Copilot**, **Copilot Studio**, **Microsoft Foundry**, **Microsoft Agent 365** y apps GenAI de terceros, y evaluaciones de sobreexposición/*oversharing*), clasificación y cifrado persistente (**Information Protection**), prevención de fuga omnicanal incluyendo red y navegador (**DLP**), detección conductual (**Insider Risk Management** con **Adaptive Protection**) e investigación forense profunda de contenido impulsada por IA generativa (**Data Security Investigations - DSI**) `[Verificado MS Learn]`.
2. **Risk & Compliance (Riesgo Regulatorio, Auditoría y Litigio):** Evaluación automatizada multicloud mediante **Compliance Manager** (más de **360 plantillas regulatorias** incluyendo **NIST CSF 2.0**, **DORA**, **NIS2**, **EU AI Act** e **ISO/IEC 42001**), supervisión ética y de prompts riesgosos (**Communication Compliance**), gobierno de retención y disposición (**Data Lifecycle & Records Management**), trazabilidad forense (**Audit Standard/Premium**), descubrimiento legal unificado (**eDiscovery** moderno tras el retiro de las versiones clásicas en agosto de 2025) y soberanía de acceso/claves (**Customer Lockbox, Customer Key y M365 PAM**) `[Verificado MS Learn]`.
3. **Data Governance (Gobierno del Patrimonio de Datos Multicloud y Fabric):** Catálogo empresarial unificado (**Unified Catalog**), mapa técnico y linaje (**Data Map** con *Live view* sin escaneo previo para Azure y **Microsoft Fabric**), curación de productos de datos y gestión de salud/calidad de datos `[Verificado MS Learn]`.

### 2.2 Rebranding Oficial de Licenciamiento (Octubre 2025+) y Modelo Dual Per-User + Pay-As-You-Go

> **Cambio contractual verificado `[Verificado MS Learn]`:** A partir de octubre de 2025, Microsoft renombró el portafolio *Microsoft 365 E5/F5/G5 Compliance* como **Microsoft Purview Suite** (*Microsoft Purview Suite*, *Microsoft Purview Suite FLW* para Frontline Workers, *Microsoft Purview Suite Gov*, *Microsoft Purview Suite EDU* y *Microsoft Purview Suite for Business Premium* hasta 300 usuarios). Los clientes con **Microsoft 365 E5 / E7 / A5 / G5** incluyen nativamente los derechos por usuario de Microsoft Purview Suite. Complementariamente, Microsoft Purview opera un **modelo híbrido de facturación** donde las licencias por usuario cubren Microsoft 365, endpoints Windows/macOS e interacciones de Microsoft 365 Copilot, mientras que una suscripción de **Azure en modalidad Pay-As-You-Go (PAYG)** habilita cargas no-M365, IA generativa de terceros/agentes y capacidades intensivas de cómputo IA `[Verificado MS Learn]`.

| Modelo / SKU / Medidor | Ámbito Cubierto | Unidad de Medida y Reglas Financieras Verificadas (Noviembre 2026) | Etiqueta |
|---|---|---|---|
| **Microsoft 365 E3** *(Base fundacional)* | M365 Core (Exchange, SharePoint, OneDrive, Teams) | Etiquetas manuales de sensibilidad y retención básica, DLP básico para M365, **Audit (Standard)** con 180 días de retención, eDiscovery básico y **Compliance Manager** con la plantilla incluida *Microsoft Data Protection Baseline*. | `[Verificado MS Learn]` |
| **Microsoft 365 E5 / Microsoft Purview Suite** *(Licencia por usuario)* | M365 + Endpoints Windows/macOS + **Microsoft 365 Copilot** | Auto-etiquetado servicio/cliente, clasificadores entrenables, Endpoint DLP, Browser DLP en Edge for Business, **Adaptive Protection**, **Insider Risk Management**, **Communication Compliance**, Records Management, **Audit (Premium)** (1 año por defecto, hasta 10 años con add-on), eDiscovery avanzado, Customer Lockbox/Customer Key/PAM, **DSPM** sobre M365/M365 Copilot y **3 plantillas regulatorias Premium gratuitas** adicionales en Compliance Manager. | `[Verificado MS Learn]` |
| **Pay-As-You-Go: Seguridad de Datos para Apps y Agentes GenAI no-M365** | Interacciones con apps/agentes IA fuera de M365 Copilot (Foundry, apps SaaS/terceros) | **Microsoft 365 Copilot no genera cargos PAYG** adicionales en usuarios licenciados; las interacciones con IA no-M365 se facturan por mensaje/solicitud (*Data Security for Gen AI*), registros de auditoría procesados, ítems retenidos en DLM y almacenamiento GB/día en eDiscovery. | `[Verificado MS Learn]` |
| **Pay-As-You-Go: Data Security Investigations (DSI)** | Investigaciones profundas de brechas/fugas con IA generativa | No exige licencia empresarial dedicada previa; factura por **GB/mes de datos almacenados** en investigaciones + **DSI Compute Units**. **Advertencia FinOps crítica:** activar *Proactive AI insights* desde DSPM refresca automáticamente la investigación cada **24 horas**, generando consumo continuo mientras permanezca activo. | `[Verificado MS Learn]` |
| **Pay-As-You-Go: Activos Multicloud, Fabric y Network Data Security** | AWS, GCP, Box, Dropbox, Google Drive, Azure SQL/ADLS, Microsoft Fabric y tráfico de red | Protección MIP/DLP sobre fuentes no-M365 facturada por **activo único en alcance/día** (un activo cubierto por múltiples políticas se cuenta **una sola vez**); **IRM** no-M365 por *Data Security Processing Units* (1 unidad = 10.000 actividades); **Network Data Security** por solicitudes salientes; **Communication Compliance** no-M365 por *Text records* (`1 record = 1.000 caracteres`, niveles Standard y Premium). | `[Verificado MS Learn]` |
| **Pay-As-You-Go: Data Governance & Security Copilot** | *Unified Catalog* y agentes de *Security Copilot in Purview* | **Unified Catalog:** activos únicos gobernados/día + *Data Governance Processing Units (DGPU)* (`1 DGPU = 60 minutos` de cómputo para calidad/salud de datos; existe versión gratuita limitada con *Live view* para evaluación). **Security Copilot:** *Security Compute Units (SCUs)* aprovisionadas en bloques horarios más tope de *Overage SCUs*. | `[Verificado MS Learn]` |

### 2.3 Principios Rectores de Arquitectura y Gobierno en Microsoft Purview Suite

1. **Operación unificada orientada a objetivos de seguridad (*Outcome-Driven Data Security*):** Gestionar todo el ciclo desde `https://purview.microsoft.com` organizando el trabajo diario y semanal alrededor de los **Data Security Objectives** de DSPM (prevenir exposición en Copilot/IA, corregir *oversharing*, frenar exfiltración y descubrir datos sensibles) en lugar de operar silos desconectados `[Verificado MS Learn]`.
2. **Defensa convergente entre Seguridad de Datos y SecOps XDR (*Unified Data + Threat Defense*):** Integrar bidireccionalmente alertas de Purview DLP e Insider Risk Management en la cola de incidentes de **Microsoft Defender XDR** (`security.microsoft.com`) y **Adaptive Protection** para elevar controles preventivos automáticamente cuando sube el riesgo conductual o existe un ataque activo `[Verificado MS Learn]`.
3. **Gobernanza segura de IA desde el diseño (*AI-Ready Data Estate & Agent Observability*):** Auditar, clasificar, etiquetar (respetando los derechos de uso `VIEW` y `EXTRACT` en contenido cifrado) y monitorear continuamente interacciones humanas y autónomas en Microsoft 365 Copilot, Copilot Studio, Microsoft Foundry, **Microsoft Agent 365** y apps GenAI de terceros `[Verificado MS Learn]`.
4. **Privacidad por diseño y segregación jurisdiccional (*Privacy-by-Default & Restricted Admin Units*):** Aplicar seudonimización nativa en Insider Risk Management y Communication Compliance, delegar permisos mediante **Role Groups** en Purview acotados a **Administrative Units** de Microsoft Entra ID y **Adaptive Scopes**, y contemplar la ventana de hasta **2 horas de propagación** al activar roles mediante Entra ID PIM for Groups `[Verificado MS Learn]`.
5. **Cumplimiento continuo basado en evidencia viva (*Continuous Compliance Scoring*):** Sustituir auditorías puntuales manuales en hojas de cálculo por evaluaciones continuas en **Compliance Manager**, priorizando acciones preventivas obligatorias (*27 puntos*) y separando controles gestionados por Microsoft, compartidos y del cliente `[Verificado MS Learn]`.
6. **Disciplina FinOps sobre medidores Pay-As-You-Go y SCUs:** Gobernar mediante presupuestos, alertas de consumo en Azure Cost Management y alcance acotado de políticas toda activación de conectores no-M365, *On-demand classification*, *Network Data Security*, *Proactive AI insights* en DSI y *Security Compute Units* `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Mapa Arquitectónico de Microsoft Purview Suite y Articulación con los Módulos `14` a `22`

Este **Módulo 13** gobierna el plano transversal de postura, IA, cumplimiento regulatorio, permisos y costos, orquestando los motores tácticos profundizados en los módulos dedicados del repositorio `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:

| Capa Arquitectónica | Componente en `purview.microsoft.com` | Función en este Módulo 13 vs. Profundización en Módulos Específicos | Ruta Oficial en Portal Unificado | Etiqueta |
|---|---|---|---|---|
| **Plano de Postura y Observabilidad IA** *(Núcleo Módulo 13)* | **Data Security Posture Management (DSPM)** *(versión unificada actual)* | Consolida *Posture*, **Data security objectives**, **AI observability** (incluyendo **Agent 365**), **Asset explorer** (con *Data Security Posture Agent*), *Data risk assessments* (*oversharing*) y *Activity explorer* (`AI activities`). Reemplaza funcionalmente a *DSPM (classic)* y *DSPM for AI (classic)*. | `purview.microsoft.com > Solutions > DSPM` | `[Verificado MS Learn]` |
| **Plano de Investigación con IA** *(Núcleo Módulo 13)* | **Data Security Investigations (DSI)** | Análisis profundo con IA generativa sobre datos comprometidos o exfiltrados: **Vector search** semántico, **Categorization** (Standard/Advanced AI), **Examination** (credenciales, PII, código fuente) y mitigación mediante **Soft Purge / Hard Purge**. | `purview.microsoft.com > Solutions > Data Security Investigations` | `[Verificado MS Learn]` |
| **Plano GRC y Postura Regulatoria** *(Núcleo Módulo 13)* | **Microsoft Purview Compliance Manager** | Gestión continua de cumplimiento multicloud sobre **360+ regulaciones** (NIST CSF 2.0, ISO 27001, DORA, NIS2, EU AI Act), cálculo automático de **Compliance Score** y repositorio de evidencias de controles propios/compartidos. | `purview.microsoft.com > Solutions > Compliance Manager` | `[Verificado MS Learn]` |
| **Plano de Gobierno y Permisos** *(Núcleo Módulo 13)* | **Settings, Role Groups, Administrative Units & Billing** | Administración centralizada de **Role groups**, vinculación con **Administrative Units** de Entra ID, conectores multicloud/Partner (GCP, Snowflake, Databricks), suscripción PAYG y **Unified Catalog / Data Map**. | `purview.microsoft.com > Settings > Roles and scopes / Account` y `Solutions > Unified Catalog` | `[Verificado MS Learn]` |
| **Clasificación y Cifrado** *(-> Módulo 14)* | **Information Protection (MIP)** | Este módulo gobierna cobertura global en DSPM y herencia/derecho `EXTRACT` para IA; el diseño de SITs, clasificadores y cifrado DKE se detalla en `14_Purview_Information_Protection`. | `purview.microsoft.com > Solutions > Information Protection` | `[Verificado MS Learn]` |
| **Prevención de Fuga** *(-> Módulo 15)* | **Data Loss Prevention (DLP)** | Este módulo articula su integración con DSPM, *Adaptive Protection*, navegador Edge/red y Defender XDR; la ingeniería de reglas por ubicación se detalla en `15_Purview_Data_Loss_Prevention`. | `purview.microsoft.com > Solutions > Data Loss Prevention` | `[Verificado MS Learn]` |
| **Ciclo de Vida y Registros** *(-> Módulo 16)* | **Data Lifecycle & Records Management** | Este módulo gobierna retención de interacciones IA/Copilot y alcance jurisdiccional; etiquetas de registro y disposición se detallan en `16_Purview_Data_Lifecycle_y_Records_Management`. | `purview.microsoft.com > Solutions > Data Lifecycle Management / Records Management` | `[Verificado MS Learn]` |
| **Riesgo Interno y Conducta** *(-> Módulos 17 y 18)* | **Insider Risk Management & Communication Compliance** | Este módulo orquesta el bucle *Adaptive Protection*, plantillas *Risky AI usage* / *Prompt shields* y escalamiento a DSI/XDR; operación detallada en `17` y `18`. | `purview.microsoft.com > Solutions > Insider Risk Management / Communication Compliance` | `[Verificado MS Learn]` |
| **Forense, Litigio y Soberanía** *(-> Módulos 19, 20 y 21)* | **Audit, eDiscovery & Lockbox/Key/PAM** | Este módulo gobierna la retención transversal de auditoría, el retiro de eDiscovery clásico (ago-2025) y controles de soberanía detallados en `19`, `20` y `21`. | `purview.microsoft.com > Solutions > Audit / eDiscovery` y `admin.microsoft.com` | `[Verificado MS Learn]` |

### 3.2 Hitos de Plataforma, Retiros de Portales Clásicos y Reglas Técnicas Críticas (2024–2026)

1. **Retiro definitivo del portal clásico `compliance.microsoft.com` (`nov-dic 2024`, MC939918) y del portal clásico de gobernanza `[Verificado MS Learn]`:**
   - Toda operación de seguridad de datos, cumplimiento y gobierno reside exclusivamente en `https://purview.microsoft.com` `[Verificado MS Learn]`.
   - Reubicaciones clave en el nuevo portal: *Classification* pasó a llamarse **Classifiers** dentro de cada solución; *Data Estate Insights* pasó a `Unified Catalog > Health management > Reports`; *Roles and scopes* se centralizó en **Settings**; y *Privacy Risk Management* reside en el portal independiente de **Microsoft Priva** `[Verificado MS Learn]`.
2. **Retiro total de soluciones heredadas de eDiscovery (`2025-08-31`) `[Verificado MS Learn]`:**
   - El 31 de agosto de 2025 Microsoft retiró definitivamente *classic Content Search*, *classic eDiscovery (Standard)* y *classic eDiscovery (Premium)*; la capacidad de *Content Search* ahora opera integrada dentro de la experiencia unificada moderna de **eDiscovery** `[Verificado MS Learn]`.
3. **Evolución de DSPM y DSPM for AI hacia la experiencia unificada de DSPM `[Verificado MS Learn]`:**
   - Las vistas anteriores permanecen accesibles bajo los nombres **DSPM (classic)** y **DSPM for AI (classic)**, pero las nuevas capacidades —incluyendo **Data security objectives**, **Data Security Posture Agent**, integración multicloud vía **Sentinel Data Lake** (GCP, Snowflake, Databricks, Varonis, Cyera, BigID, OneTrust) y la página **AI observability** con soporte nativo para **Microsoft Agent 365**— se entregan exclusivamente en la versión actual de **DSPM** (`Solutions > DSPM`) `[Verificado MS Learn]`.
4. **Reglas técnicas de protección de IA y agentes (`Microsoft 365 Copilot` y `Microsoft Agent 365`) `[Verificado MS Learn]`:**
   - Para que Microsoft 365 Copilot o un agente devuelva contenido protegido con una etiqueta de sensibilidad con cifrado, la identidad o instancia del agente debe poseer explícitamente los derechos de uso **`VIEW` y `EXTRACT`** `[Verificado MS Learn]`.
   - En **Microsoft Agent 365**, los archivos deben compartirse explícitamente con la instancia del agente (las etiquetas configuradas genéricamente para *All users and groups in your organization* o *Any authenticated users* **no** bastan para otorgar descifrado al agente), y el contenido nuevo creado por Agent 365 no hereda automáticamente la etiqueta del archivo fuente `[Verificado MS Learn]`.
5. **Convergencia Purview <-> Microsoft Defender XDR y *Automatic Attack Disruption* `[Verificado MS Learn]`:**
   - Las alertas de **Microsoft Purview DLP** e **Insider Risk Management** se ingieren y correlacionan nativamente en `https://security.microsoft.com`, fusionándose en **Incidentes XDR** junto con señales de endpoint, identidad, correo y SaaS `[Verificado MS Learn]`.
   - Desde un incidente en Defender XDR o un caso en Insider Risk Management, el analista puede lanzar directamente una investigación en **Data Security Investigations (DSI)** para examinar con IA el impacto exacto de los archivos expuestos `[Verificado MS Learn]`.

### 3.3 Flujo Arquitectónico de Señales entre Purview, IA, Entra ID, Defender XDR y Sentinel

```
+---------------------------------------------------------------------------------------+
|                   PATRIMONIO DE DATOS E INTERACCIONES DE IA / AGENTES                 |
|  M365 (EXO/SPO/ODB/Teams) | Endpoints Win/macOS | Fabric/Azure/AWS/GCP | Copilot/A365 |
+-------------------------------------------+-------------------------------------------+
                                            |
                                            v
+---------------------------------------------------------------------------------------+
|                  PORTAL UNIFICADO MICROSOFT PURVIEW (purview.microsoft.com)           |
|  [DSPM: Objectives + AI Observability + Oversharing]   [Compliance Manager: 360+ Regs]|
|  [MIP Labels/EXTRACT] [DLP Omnicanal] [IRM + Adaptive Protection] [Audit + eDiscovery]|
|  [Data Security Investigations (DSI): Vector Search + AI Categorization + Purge]      |
+-------------------+-----------------------------------+-------------------------------+
                    |                                   |
     Niveles Riesgo | Adaptive Protection               | Alertas DLP/IRM + Escalada DSI
    (Elevated/Mod.) | & Admin Units / PIM (2h)          | + OfficeActivity / MIP Logs
                    v                                   v
+-------------------+-------------------+   +-----------+-------------------------------+
|       MICROSOFT ENTRA ID              |   |  MICROSOFT DEFENDER XDR & SENTINEL        |
| - Conditional Access por riesgo IRM   |   | - Correlación en Incidentes Unificados    |
| - Restricted Administrative Units     |   | - Automatic Attack Disruption             |
| - Identidades de Agentes (Agent 365)  |   | - Sentinel Data Lake & E5 Grant (5MB/u/d) |
+---------------------------------------+   +-------------------------------------------+
```

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Modelo de Role Groups en Purview, Propagación PIM (2 Horas) y Administrative Units

La administración de permisos en Microsoft Purview se centraliza en `purview.microsoft.com > Settings > Roles and scopes > Role groups`, complementada por roles de **Microsoft Entra ID** `[Verificado MS Learn]`. Tres reglas técnicas gobiernan el diseño de mínimo privilegio:

1. **Latencia de propagación de Entra ID PIM for Groups (hasta 2 horas) `[Verificado MS Learn]`:** Microsoft Purview soporta asignar membresía mediante grupos de seguridad gobernados Just-In-Time en **Microsoft Entra PIM**, pero documenta oficialmente que **puede tardar hasta 2 horas tras la activación** para que los permisos efectivos se apliquen en Purview. Los playbooks de emergencia deben contemplar esta ventana o disponer de un flujo de respaldo supervisado `[Verificado MS Learn]`.
2. **Delegación jurisdiccional mediante Restricted Administrative Units `[Verificado MS Learn]`:** Purview permite restringir miembros de *Role groups* a **Administrative Units (AU)** de Entra ID en **Data Loss Prevention**, **Insider Risk Management**, **Communication Compliance**, **Data Lifecycle Management**, **Records Management**, **Information Protection**, **Audit** y **eDiscovery**, asegurando que un analista regional (ej. Europa vs. Cono Sur) solo cree políticas e investigue alertas de usuarios pertenecientes a su unidad administrativa `[Verificado MS Learn]`. *(Nota: para ver los role groups de un usuario en la búsqueda global del portal se requiere el rol `Role Management` sin restricción de unidad administrativa)* `[Verificado MS Learn]`.
3. **Separación estricta entre configuración de políticas y visualización de contenido sensible `[Verificado MS Learn]`:** Quien diseña políticas o administra permisos no debe acceder por defecto al texto plano de archivos o prompts en *Content Explorer*, *Activity Explorer* o *Data Security Investigations* salvo rol explícito de revisor aprobado.

| Role Group / Rol Oficial | Plano de Control | Equipo / Persona | Permisos Clave y Restricciones | Estrategia PIM / Administrative Units | Etiqueta |
|---|---|---|---|---|---|
| **Microsoft Purview Compliance Administrator** *(Entra / Purview Role Group)* | Entra ID + Purview | Director GRC / Data Security Lead | Acceso administrativo transversal a configuración de soluciones de cumplimiento, DSPM y Compliance Manager; **no** sustituye permisos exclusivos de eDiscovery Manager, Insider Risk o DSI sin asignación explícita. | **Elegible en Entra ID PIM** (ventana de 4–8 horas considerando hasta 2h de propagación `[Verificado MS Learn]`); prohibido usar *Global Administrator* `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Role Management** *(Purview Role)* | Purview RBAC (`Settings > Roles and scopes`) | Arquitecto de Gobierno de Identidad sobre Purview | Único rol autorizado para crear, modificar y asignar *Role groups* y vincular **Administrative Units** dentro de Microsoft Purview. | **Estrictamente elegible en PIM** con aprobación dual; segregado de analistas operativos de DLP/IRM/DSI `[Decisión / Propuesta Editorial]`. | `[Verificado MS Learn]` |
| **DSPM & Data Security Viewer / Content Explorer List & Content Viewer** | Purview RBAC | Analista de Postura de Datos / AI Governance | Visualización de paneles *Posture*, *Objectives*, *AI observability* e interacción con *Security Copilot in DSPM*; separar estrictamente *List Viewer* (metadatos) de *Content Viewer* (lectura de prompts/archivos reales). | Asignar *List Viewer* acotado por AU para operación diaria y mantener *Content Viewer* **exclusivamente JIT en PIM** con aprobación del DPO `[Decisión / Propuesta Editorial]`. | `[Verificado MS Learn]` |
| **Data Loss Prevention Compliance Management** | Purview RBAC (soporta **Administrative Units**) | Ingeniero de Seguridad de Datos (DLP) | Creación, simulación y ajuste de políticas DLP (M365, Endpoint, Edge Browser, Network, Fabric) e integración con **Adaptive Protection**. | Elegible vía grupo de seguridad PIM y restringido por **Administrative Unit** en organizaciones multinacionales `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management (`Admins` / `Analysts` / `Investigators`)** | Purview RBAC (soporta **Administrative Units**) | Célula de Riesgo Interno + RRHH / Legal | Sub-roles segregados: *Admin* configura políticas/indicadores; *Analyst* realiza triaje seudonimizado; *Investigator* examina casos escalados y dispara investigaciones hacia DSI. | Seudonimización activada por defecto; sub-roles separados en personas distintas para impedir abuso unilateral `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Data Security Investigations (`Admins` / `Investigators` / `Mitigation Admins`)** | Purview RBAC | Equipo CSIRT / Respuesta a Brechas de Datos | Creación de investigaciones, ejecución de *Vector search*, *AI Categorization* y *Examination*, y ejecución segregada de acciones destructivas **Soft Purge / Hard Purge**. | Segregar quien investiga (*Investigator*) de quien ejecuta purgado de datos (*Mitigation*) bajo aprobación formal de Legal/CISO `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`. | `[Verificado MS Learn]` |
| **Compliance Manager (`Admins` / `Assessors` / `Contributors` / `Readers`)** | Purview RBAC | GRC, Dueños de Control TI y Auditores Externos | *Admin* gestiona plantillas regulatorias; *Assessor* valida pruebas y puntaje; *Contributor* carga evidencias técnicas sin alterar plantillas; *Reader* ofrece acceso de solo lectura a auditores. | Asignación nominal por evaluación regulatoria; auditores externos reciben únicamente *Compliance Manager Reader* temporal `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Data Source Administrator / Data Curator** *(Unified Catalog)* | Purview Data Governance RBAC (por *Collections* / Dominios) | Oficina del CDO / Data Stewards | Registro de orígenes multicloud/Fabric, configuración de escaneos en *Data Map*, curación de glosario y gestión de salud en *Unified Catalog*. | Delegado por jerarquía de *Collections* / dominios de negocio y supervisado financieramente por consumo de DGPUs `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

### 4.2 Matriz RACI Transversal del Gobierno de Microsoft Purview Suite `[Decisión / Propuesta Editorial]`

| Dominio Transversal en Microsoft Purview Suite | CISO / Data Security | GRC / Legal / DPO | SOC / Defender XDR | CDO / Data & AI Platform | FinOps / IT Admin |
|---|---|---|---|---|---|
| Arquitectura global de `purview.microsoft.com`, Role Groups y Admin Units | **A / R** | C | I | C | S |
| Operación de **DSPM** (*Data Security Objectives* y remediación de *oversharing*) | **A / R** | C | C | R *(dueños de sitios/datos)* | I |
| Observabilidad y protección de **Copilot, Foundry, Agent 365 y GenAI terceros** | **A / R** | C | C | R *(dueños de agentes)* | I |
| Triaje e integración de alertas DLP / IRM en **Defender XDR** y *Adaptive Protection* | R | C *(en IRM/DPO)* | **A / R** | I | I |
| Activación y ejecución de **Data Security Investigations (DSI)** y *Purge* | **R** | **A** *(autorización legal/Purge)* | C / S | I | C *(costo PAYG)* |
| Evaluaciones regulatorias y **Compliance Score** en **Compliance Manager** | C / R *(controles técnicos)* | **A / R** | C | C | S *(evidencias TI)* |
| Gobierno de medidores **Pay-As-You-Go** (Azure) y capacidad **SCU** | C | I | I | C *(Unified Catalog)* | **A / R** |

---

## 5. Cadencia Operativa Diaria

### D-01 — Revisión del Panel Unificado de DSPM y Avance de Data Security Objectives
- **Objetivo:** Supervisar diariamente el estado de postura de seguridad de datos, anomalías de compartición excesiva (*oversharing*) y exfiltración hacia destinos riesgosos desde la experiencia actual de **DSPM** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > Posture` y `Objectives` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Analyst / SOC L2 `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.RA-05`, `DE.CM-09` / Exfiltration (`TA0010`).
- **Procedimiento:**
  1. Ingresar en `Solutions > DSPM > Posture` (verificando usar la experiencia actual y no *DSPM classic*) y revisar la gráfica de tendencia de 30 días junto con alertas de variación abrupta en exposición de datos sensibles `[Verificado MS Learn]`.
  2. Inspeccionar las tarjetas de **Data security objectives** (*Prevent data exposure in Microsoft 365 Copilot and Microsoft Copilot interactions*, *Prevent oversharing of sensitive data*, *Prevent exfiltration to risky destinations* y *Discover sensitive data*) `[Verificado MS Learn]`.
  3. Revisar mediante **View agent activity** las recomendaciones y triajes generados por el *Data Security Posture Agent* y agentes de triaje de alertas (auditando acciones sugeridas antes de aprobarlas) `[Verificado MS Learn]`.
  4. Si *Proactive AI insights* está habilitado sobre el objetivo de exfiltración, analizar los hallazgos refrescados en las últimas 24 horas por Data Security Investigations `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura o exportación diaria de métricas de *Data security objectives* y registro auditado de acciones de agentes en DSPM `[Verificado MS Learn]`.

### D-02 — Monitoreo Diario de AI Observability: Prompts Sensibles, Apps GenAI y Microsoft Agent 365
- **Objetivo:** Detectar exposición de información confidencial, intentos de *prompt injection* o comportamientos anómalos en interacciones con Microsoft 365 Copilot, agentes corporativos (**Agent 365**, Copilot Studio, Foundry) y sitios GenAI de terceros `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > AI observability` y `Discover > Activity explorer > AI activities` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Analyst / AI Governance Lead `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.AE-02`, `PR.DS-02` / Exfiltration Over Web Service (`T1567`).
- **Procedimiento:**
  1. Abrir `DSPM > AI observability` para revisar el inventario de aplicaciones y agentes IA con actividad reciente, priorizando las instancias de **Microsoft Agent 365** y agentes Copilot Studio clasificados con riesgo elevado por Insider Risk Management `[Verificado MS Learn]`.
  2. Filtrar en `Activity explorer > AI activities` eventos de las últimas 24 horas que involucren tipos de información sensible (SITs), etiquetas `Confidential` / `Highly Confidential` o bloqueos de DLP en navegador/red hacia IA generativa pública `[Verificado MS Learn]`.
  3. Verificar si algún agente fue bloqueado legítimamente por una política DLP e informar al propietario registrado del agente para evitar fallos silenciosos en flujos automatizados de negocio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación filtrada de `AI activities` (metadatos sin exponer texto de prompts salvo elevación JIT autorizada) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### D-03 — Triaje Convergente de Alertas Purview (DLP e Insider Risk) en Incidentes de Microsoft Defender XDR
- **Objetivo:** Correlacionar alertas de fuga de datos y riesgo interno con incidentes de compromiso externo en la cola unificada del SOC para contener ataques híbridos o robo activo de propiedad intelectual `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` + `https://purview.microsoft.com > Solutions > Data Loss Prevention > Alerts` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / SOC L2 + Data Security Analyst `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.AE-03`, `RS.AN-03` / Collection (`TA0009`), Exfiltration (`TA0010`).
- **Procedimiento:**
  1. Filtrar en `security.microsoft.com` incidentes que contengan fuentes de alerta `Microsoft Purview Data Loss Prevention` o `Microsoft Purview Insider Risk Management` `[Verificado MS Learn]`.
  2. Evaluar si el usuario involucrado presenta simultáneamente alertas de robo de credenciales/sesión en Microsoft Entra ID Protection o malware en Defender for Endpoint (distinguiendo actor externo con cuenta comprometida frente a insider real).
  3. Cuando se confirme exfiltración masiva o exposición de activos críticos, escalar directamente desde el incidente XDR hacia una investigación en **Data Security Investigations (DSI)** (`AH-01`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Expediente unificado de incidente en `security.microsoft.com` con clasificación y determinación documentada `[Verificado MS Learn]`.

### D-04 — Supervisión Operativa del Bucle Dinámico de Adaptive Protection (IRM <-> DLP <-> Entra CA)
- **Objetivo:** Verificar que los cambios dinámicos en niveles de riesgo de usuario en Insider Risk Management (`Elevated`, `Moderate`, `Minor`) se estén aplicando sin fallos en políticas DLP y Acceso Condicional `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Analyst `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `PR.AA-05`, `RS.MI-01` / Exfiltration (`TA0010`).
- **Procedimiento:**
  1. Revisar el resumen diario de usuarios asignados actualmente a los perfiles **Elevated risk level**, **Moderate risk level** y **Minor risk level** (manteniendo seudonimización activa) `[Verificado MS Learn]`.
  2. Confirmar que las políticas DLP vinculadas a la condición *Insider risk level for Adaptive Protection is* se encuentren en estado `On` (y no estancadas indefinidamente en modo simulación tras finalizar la calibración inicial) sobre Exchange, Teams y Devices `[Verificado MS Learn]`.
  3. Validar la salud de *Advanced classification scanning and protection* en Endpoint DLP para garantizar efectividad de Adaptive Protection en estaciones Windows y macOS `[Verificado MS Learn]`.
- **Evidencia Auditable:** Panel de estado de `Adaptive protection` y conteo de bloqueos preventivos ejecutados en 24h `[Verificado MS Learn]`.

### D-05 — Auditoría de Cambios Críticos de Configuración y Permisos en Microsoft Purview
- **Objetivo:** Detectar cualquier creación, desactivación o modificación no autorizada de políticas DLP/IRM/Retención, etiquetas de sensibilidad, *Role groups*, *Administrative Units* o investigaciones DSI `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Audit` (o `OfficeActivity` / `CloudAppEvents` en Sentinel y Defender XDR) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / GRC Security Auditor `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-01`, `GV.RR-02` / Impair Defenses (`T1562`).
- **Procedimiento:**
  1. Ejecutar búsqueda sobre operaciones administrativas de las últimas 24 horas en el *Unified Audit Log*: cambios en membresías de `Role groups`, exclusiones en políticas DLP, degradación o borrado de etiquetas MIP, desactivación de retenciones o accesos de lectura a *Content Explorer* / *Data Security Investigations* `[Verificado MS Learn]`.
  2. Contrastar cada cambio administrativo con solicitudes aprobadas en ITSM y activaciones legítimas en Entra ID PIM `[Decisión / Propuesta Editorial]`.
  3. Escalar como incidente grave cualquier acceso administrativo de lectura a contenido sensible sin caso forense o legal respaldatorio `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Consulta diaria guardada sobre `OfficeActivity` / `Audit` conciliada contra tickets de cambio `[Verificado MS Learn]`.

### D-06 — Vigilancia de Salud de Conectores de Datos, Onboarding de Endpoints y Telemetría de Navegador/Red
- **Objetivo:** Garantizar que no existan puntos ciegos de recolección de señales desde estaciones Windows/macOS, Microsoft Edge for Business, extensiones de navegador y conectores no-M365 `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Device onboarding` y `Data connectors` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-09` / Impair Defenses (`T1562`).
- **Procedimiento:**
  1. Verificar en `Settings > Device onboarding` que los dispositivos corporativos Windows y macOS reporten telemetría activa hacia Endpoint DLP e Insider Risk Management `[Verificado MS Learn]`.
  2. Comprobar el estado saludable de conectores de terceros (HR connector para IRM, conectores SaaS/multicloud e integración con **Sentinel Data Lake** cuando aplique en DSPM) `[Verificado MS Learn]`.
  3. Confirmar recepción continua de eventos de uso de IA en navegador (Microsoft Edge for Business y extensión Purview en Chrome/Firefox si aplica) en `Activity explorer` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado `Healthy / Active` de conectores y conteo diario de dispositivos con telemetría Purview activa `[Verificado MS Learn]`.

### D-07 — Control Diario de Consumo FinOps sobre Medidores Pay-As-You-Go, DSI y Capacidad SCU
- **Objetivo:** Prevenir sobrecostos imprevistos en facturación Azure causados por escaneos descontrolados, investigaciones DSI abiertas, *Proactive AI insights* o picos de *Overage SCUs* `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Usage center` + `https://portal.azure.com > Cost Management + Billing` `[Verificado MS Learn]`.
- **Rol Responsable:** FinOps Lead / Purview Platform Administrator `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.RM-02`, `GV.OV-03` / Resource Hijacking / Cost Governance.
- **Procedimiento:**
  1. Revisar alertas de presupuesto diario en Azure Cost Management filtradas por los recursos y medidores de **Microsoft Purview** (activos protegidos/día, *Requests* de red/IA, *Text records*, *Processing units* y almacenamiento/cómputo de **Data Security Investigations**) `[Verificado MS Learn]`.
  2. Verificar qué investigaciones en **DSI** permanecen activas y confirmar si el interruptor de *Proactive AI insights* en DSPM está deliberadamente encendido y presupuestado (dado que refresca e incurre en cargos cada 24 horas) `[Verificado MS Learn]`.
  3. Supervisar la utilización horaria de **Security Compute Units (SCUs)** de Security Copilot en Purview, programando cualquier ajuste de capacidad aprovisionada al inicio exacto de la hora para evitar doble cobro dentro del mismo bloque horario `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tablero diario de consumo PAYG / SCU sin desviaciones sobre el umbral presupuestario aprobado `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01 — Ejecución de Data Risk Assessments y Remediación de Oversharing para Copilot y Agentes
- **Objetivo:** Identificar y corregir semanalmente sitios de SharePoint, equipos de Teams y vínculos `Anyone` / `Organization-wide` con datos sensibles sobreexpuestos que puedan ser indexados y devueltos por Microsoft 365 Copilot o agentes `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > Discover > Data risk assessments` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Engineer + Propietarios de Sitios / CDO `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.RA-05`, `PR.AA-05` / Data from Information Repositories (`T1213`).
- **Procedimiento:**
  1. Revisar los resultados semanales de las evaluaciones predeterminadas y personalizadas de *Data risk assessments* en DSPM, ordenando repositorios por volumen de ítems sensibles y amplitud de permisos de lectura `[Verificado MS Learn]`.
  2. Ejecutar acciones de remediación integradas sobre los sitios de mayor riesgo: revocar vínculos anónimos/organizacionales excesivos, exigir etiquetado de sensibilidad o coordinar controles de acceso restringido en SharePoint Advanced Management `[Verificado MS Learn]`.
  3. Validar que los archivos sensibles cifrados que **no** deban ser resumidos por Copilot ni por agentes carezcan del derecho de uso `EXTRACT` para grupos masivos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal de *Data risk assessments* mostrando reducción neta de sitios con *oversharing* crítico `[Verificado MS Learn]`.

### S-02 — Seguimiento Semanal de Improvement Actions y Variación del Compliance Score en Compliance Manager
- **Objetivo:** Gestionar el flujo semanal de implementación y prueba de controles asignados a equipos técnicos y de negocio en **Microsoft Purview Compliance Manager** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Compliance Manager > Improvement actions` y `Assessments` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC & Compliance Manager + Control Owners `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.OV-03`, `ID.IM-02` / Governance & Assurance.
- **Procedimiento:**
  1. Revisar la variación semanal del **Compliance Score** global (recordando que las acciones actualizan automáticamente su estado técnico dentro de las **24 horas** posteriores al cambio en el tenant) `[Verificado MS Learn]`.
  2. Priorizar el backlog semanal según el peso de riesgo oficial del motor de puntuación: primero acciones **Preventative mandatory (27 puntos)** y **Preventative discretionary (9 puntos)**, seguidas de **Detective / Corrective mandatory (3 puntos)** `[Verificado MS Learn]`.
  3. Verificar que cada acción manual completada por un *Contributor* incluya evidencia documental adjunta antes de que el *Assessor* marque su estado de prueba como `Passed` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación semanal de *Improvement actions* cerradas y evolución del puntaje por evaluación `[Verificado MS Learn]`.

### S-03 — Gobernanza Semanal de Agentes IA (Agent 365, Copilot Studio y Foundry) en Purview
- **Objetivo:** Asegurar que todo nuevo agente desplegado en el tenant cuente con cobertura efectiva de clasificación, etiquetado, DLP, Insider Risk, Communication Compliance y retención `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > AI observability` y `Discover > Apps and agents` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Governance Lead / Data Security Engineer `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.AM-02`, `PR.DS-05` / LLM Prompt Injection / Data Leakage.
- **Procedimiento:**
  1. Conciliar las nuevas instancias detectadas en `DSPM > AI observability` (especialmente **Microsoft Agent 365**) y en `Discover > Apps and agents` (Copilot Studio, Microsoft Foundry, agentes registrados en Entra) `[Verificado MS Learn]`.
  2. Aunque las instancias de **Agent 365** habilitan automáticamente auditoría, clasificación de datos y evaluaciones de regulaciones IA en Compliance Manager al crearse, incluirlas explícitamente (o mediante grupo de seguridad) en políticas de **DLP**, **Insider Risk Management**, **Communication Compliance** y **Data Lifecycle Management** igual que a un usuario `[Verificado MS Learn]`.
  3. Revisar alertas de la plantilla *Risky AI usage* (IRM) y detecciones de *Prompt shields / Protected materials* (Communication Compliance) de la última semana `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal conciliado de agentes IA con verificación de inclusión en políticas Purview `[Verificado MS Learn]`.

### S-04 — Auditoría Semanal de Role Groups, Administrative Units y Activaciones PIM en Purview
- **Objetivo:** Preservar el mínimo privilegio y el aislamiento jurisdiccional entre unidades de negocio en `purview.microsoft.com` `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Roles and scopes > Role groups` + `https://entra.microsoft.com > Administrative units / PIM` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Lead / Purview Role Management Admin `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.RR-02`, `PR.AA-05` / Valid Accounts (`T1078`).
- **Procedimiento:**
  1. Auditar todos los miembros de *Role groups* de alto privilegio (`Organization Management`, `Compliance Administrator`, `Role Management`, `eDiscovery Manager`, `Insider Risk Management`, `Data Security Investigations` y `Content Explorer Content Viewer`) `[Verificado MS Learn]`.
  2. Verificar que los administradores regionales o subsidiarios mantengan correctamente asignadas sus **Restricted Administrative Units** en DLP, IRM, Communication Compliance, DLM, Records, MIP, Audit y eDiscovery `[Verificado MS Learn]`.
  3. Conciliar las activaciones JIT de grupos en Entra ID PIM de los últimos 7 días contra tickets de investigación autorizados `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación semanal de `Role groups`, mapeo de *Administrative Units* y bitácora de activaciones PIM `[Verificado MS Learn]`.

### S-05 — Sintonización Transversal de Ruido Analítico y Falsos Positivos (DLP, IRM y Comm Compliance)
- **Objetivo:** Reducir la fatiga de alertas en el SOC y en los equipos de riesgo calibrando clasificadores, condiciones contextuales y umbrales entre los módulos `14`, `15`, `17` y `18` `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > Reports` y consolas de alertas DLP / IRM / Communication Compliance `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Engineer + SOC L3 Detection Lead `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.AE-07`, `ID.IM-01` / Exfiltration (`TA0010`).
- **Procedimiento:**
  1. Analizar las reglas DLP y políticas IRM con mayor tasa de descarte (*False positive* / *Benign positive*) durante la semana en curso.
  2. Ajustar niveles de confianza de *Sensitive Information Types (SITs)*, diccionarios de proximidad o exclusiones de procesos de servicio documentadas (coordinando la modificación detallada con los propietarios de los Módulos `14`, `15`, `17` y `18`).
  3. Validar toda regla nueva o modificada en modo simulación con *Policy Tips* antes de pasarla a bloqueo productivo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta semanal de tuning con tasa de verdaderos positivos pre y post ajuste `[Decisión / Propuesta Editorial]`.

### S-06 — Revisión Semanal de Investigaciones Abiertas y Ciclo de Vida de Datos en DSI
- **Objetivo:** Controlar el progreso técnico, las autorizaciones legales pendientes y la huella de almacenamiento facturable de las investigaciones abiertas en **Data Security Investigations (DSI)** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Data Security Investigations` `[Verificado MS Learn]`.
- **Rol Responsable:** CSIRT Lead / Data Security Investigator + FinOps `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `RS.AN-03`, `GV.RM-02` / Collection & Exfiltration.
- **Procedimiento:**
  1. Revisar el estado de cada investigación activa en DSI (alcance de datos indexados, categorización IA completada y hallazgos críticos pendientes de mitigación) `[Verificado MS Learn]`.
  2. Cerrar y depurar contenedores de investigaciones concluidas que no requieran preservación legal en **eDiscovery** (Módulo 20), liberando consumo mensual del medidor *Data storage (GB/month)* `[Verificado MS Learn]`.
  3. Auditar en el *Unified Audit Log* todas las consultas y acciones ejecutadas dentro de DSI durante la semana `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario semanal de investigaciones DSI activas/cerradas y reporte de GB retenidos `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01 — Auditoría Mensual de Cobertura de Clasificación, Etiquetado y Protección del Patrimonio de Datos
- **Objetivo:** Medir qué proporción del patrimonio de datos en Microsoft 365, endpoints y nubes conectadas está descubierta, clasificada y protegida por políticas activas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > Asset explorer` y `Reports` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Architect / Propietario Módulo 14 `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.AM-07`, `PR.DS-01` / Data from Cloud Storage (`T1530`).
- **Procedimiento:**
  1. Inspeccionar en `DSPM > Asset explorer` (pestaña *Standard* y pestaña *Agent*) el volumen de activos con información sensible aún sin etiquetar (*Unlabeled sensitive data*) en SharePoint, OneDrive, Exchange y fuentes no-M365 integradas `[Verificado MS Learn]`.
  2. Verificar que las etiquetas de sensibilidad estén habilitadas para archivos de Office en SharePoint y OneDrive (requisito esencial para que Copilot y agentes procesen archivos cifrados más allá de apps locales de escritorio) `[Verificado MS Learn]`.
  3. Derivar brechas de cobertura hacia políticas de auto-etiquetado o campañas de *On-demand classification* acotadas presupuestariamente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de cobertura de etiquetado y reducción de repositorios sensibles sin etiqueta `[Verificado MS Learn]`.

### M-02 — Comité Mensual de Cumplimiento Regulatorio en Compliance Manager (NIST CSF 2.0, DORA, NIS2, EU AI Act)
- **Objetivo:** Evaluar formalmente el estado de cumplimiento frente a los marcos normativos aplicables a la organización y preparar paquetes de evidencia listos para auditoría `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Compliance Manager > Assessments` y `Regulations` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC & Compliance Officer / DPO / CISO `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.OC-03`, `GV.OV-03` / Regulatory Assurance.
- **Procedimiento:**
  1. Revisar el puntaje desglosado entre *Microsoft-managed controls*, *Your controls* y *Shared controls* en la plantilla base **Microsoft Data Protection Baseline** y en las plantillas regulatorias activas (aprovechando las **3 plantillas Premium gratuitas** incluidas en M365 E5 / Purview Suite, ej. **NIST CSF 2.0**, **ISO/IEC 27001:2022**, **EU AI Act**, **DORA** o **NIS2**) `[Verificado MS Learn]`.
  2. Revisar actualizaciones normativas notificadas por Microsoft sobre las plantillas activas y reasignar nuevos controles derivados.
  3. Validar que el equipo legal y el CISO comprendan explícitamente el aviso oficial de Microsoft: el puntaje de Compliance Manager mide progreso de implementación pero **no constituye una garantía jurídica automática de cumplimiento** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte ejecutivo mensual exportado por evaluación regulatoria desde Compliance Manager `[Verificado MS Learn]`.

### M-03 — Conciliación FinOps Mensual de Facturación Pay-As-You-Go de Purview y Dimensionamiento SCU
- **Objetivo:** Auditar la factura mensual de Azure correspondiente a los medidores de consumo de Microsoft Purview y optimizar el alcance de políticas para maximizar retorno sobre riesgo reducido `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://portal.azure.com > Cost Management + Billing` + `https://purview.microsoft.com > Usage center / Unified Catalog` `[Verificado MS Learn]`.
- **Rol Responsable:** FinOps Lead + Data Security Architect + CDO `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `GV.RM-02`, `GV.SC-03` / Financial Governance.
- **Procedimiento:**
  1. Desglosar el cargo mensual por medidor PAYG: activos protegidos en Azure SQL/ADLS/Blob/Fabric/AWS (recordando que todo activo dentro del *scope* de una política cuenta diariamente aunque no dispare condición, pero se cobra una sola vez entre múltiples políticas), *Processing units* de IRM, *Text records* de Communication Compliance, *Requests* de Network Data Security, GB/cómputo de DSI y DGPUs de *Unified Catalog* `[Verificado MS Learn]`.
  2. Ajustar el alcance (*scoping*) de políticas MIP/DLP sobre espacios de trabajo de **Microsoft Fabric** y bases de datos cloud para excluir entornos efímeros de desarrollo/sandbox sin datos reales `[Decisión / Propuesta Editorial]`.
  3. Calibrar la dotación de **Provisioned SCUs** frente a **Overage SCUs** para *Security Copilot in Purview* según patrones reales de uso mensual `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual FinOps de Purview con optimizaciones de alcance aplicadas `[Decisión / Propuesta Editorial]`.

### M-04 — Salud del Mapa de Datos y Gobierno de Activos Críticos en Unified Catalog (Fabric & Multicloud)
- **Objetivo:** Verificar que los activos críticos analíticos en **Microsoft Fabric**, Azure Data Lake/SQL y nubes conectadas mantengan clasificación automática, propietarios asignados y controles de salud en **Unified Catalog** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Unified Catalog > Health management > Reports` y `Data Map` `[Verificado MS Learn]`.
- **Rol Responsable:** CDO Office / Data Governance Administrator `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `ID.AM-07`, `GV.RM-06` / Data from Cloud Storage (`T1530`).
- **Procedimiento:**
  1. Revisar en `Data Map` la salud de escaneos programados, el historial de cambios en **Data Map history** y la visibilidad en tiempo real mediante **Live view** para suscripciones Azure y **Microsoft Fabric** `[Verificado MS Learn]`.
  2. Inspeccionar en `Unified Catalog > Health management > Reports` (evolución del antiguo *Data Estate Insights*) activos huérfanos de curador, productos de datos con baja puntuación de calidad o tablas sensibles sin etiqueta de protección heredada `[Verificado MS Learn]`.
  3. Coordinar con Ingeniería de Seguridad de Datos la aplicación de políticas MIP/DLP sobre workspaces críticos de Fabric/Power BI `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de salud de *Unified Catalog* e historial auditado de `Data Map history` `[Verificado MS Learn]`.

### M-05 — Validación Mensual de Convergencia Purview <-> Defender XDR / Sentinel y Retención de Auditoría
- **Objetivo:** Comprobar la integridad de extremo a extremo del flujo de alertas y logs entre Microsoft Purview, Microsoft Defender XDR y Microsoft Sentinel `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Advanced hunting / Microsoft Sentinel > Data connectors` + `https://purview.microsoft.com > Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 Engineer + Purview Audit Admin `[Decisión / Propuesta Editorial]`.
- **Alineación NIST CSF 2.0 / MITRE:** `DE.CM-01`, `DE.AE-03` / Impair Defenses (`T1562.008`).
- **Procedimiento:**
  1. Verificar en Defender XDR que las alertas de DLP e Insider Risk sigan correlacionándose en incidentes y que las consultas de *Advanced Hunting* devuelvan eventos vigentes de datos e IA (`CloudAppEvents`, `DataSecurityEvents` / `AlertInfo`) `[Verificado MS Learn]`.
  2. Validar en **Microsoft Sentinel** la ingesta gratuita de `OfficeActivity` y el aprovechamiento del **Microsoft 365 E5 Data Grant (hasta 5 MB/usuario/día)** para logs de *Microsoft Purview Information Protection* `[Verificado MS Learn]`.
  3. Auditar las políticas de retención de **Purview Audit (Premium)** (1 año incluido en E5 para usuarios licenciados y políticas de hasta 10 años donde exista requerimiento normativo y add-on) asegurando captura de eventos de Copilot y **Agent 365** (`Módulo 19`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salida mensual de consulta KQL de validación de conectores y políticas de retención de auditoría `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 — Recertificación Trimestral de Privilegios Purview, Administrative Units y Validación de Adaptive Scopes
- **Cadencia:** Trimestral `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Auditar y recertificar la totalidad de miembros en *Role groups* de Purview (especialmente roles con acceso a contenido o purgado), sus **Administrative Units** y la precisión de los **Adaptive Scopes** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Identity governance > Access reviews` + `https://purview.microsoft.com > Settings > Roles and scopes` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Lead + DPO + Purview Role Management Admin `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Ejecutar *Access Reviews* trimestrales sobre los grupos de seguridad asignados a `Role Management`, `Compliance Administrator`, `eDiscovery Manager`, `Insider Risk Management Investigators`, `Data Security Investigations` y `Content Explorer Content Viewer` `[Verificado MS Learn]`.
  2. Verificar que los atributos de directorio de Entra ID (`Department`, `Country`, `CustomAttributes`) que alimentan **Administrative Units** y **Adaptive Scopes** mantengan integridad sin dejar usuarios huérfanos fuera de cobertura de políticas `[Verificado MS Learn]`.
  3. Confirmar en el entorno moderno de **eDiscovery** que no existan casos cerrados reteniendo *holds* innecesarios tras la migración post agosto de 2025 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Actas firmadas de *Access Reviews* y reporte de integridad de *Administrative Units* / *Adaptive Scopes* `[Verificado MS Learn]`.

### T-02 — Evaluación Trimestral de Gobernanza de IA y Regulaciones IA (EU AI Act / NIST AI RMF / ISO 42001)
- **Cadencia:** Trimestral `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Auditar la postura integral frente a normativas emergentes de inteligencia artificial sobre todos los copilotos, agentes (**Agent 365**, Copilot Studio, Foundry) y modelos consumidos por la organización `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Compliance Manager > Assessments` y `Solutions > DSPM > AI observability` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Governance Committee (CISO + CDO + DPO + Legal) `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Evaluar en **Compliance Manager** el avance trimestral de las plantillas regulatorias de IA (**EU Artificial Intelligence Act**, **ISO/IEC 42001:2023**, **NIST AI Risk Management Framework**) incluyendo el inventario automático de instancias de **Agent 365** `[Verificado MS Learn]`.
  2. Revisar el catálogo de sitios GenAI externos detectados por navegador/red, actualizando la clasificación entre aplicaciones IA permitidas con controles DLP inline frente a aplicaciones bloqueadas `[Verificado MS Learn]`.
  3. Verificar políticas de retención y eliminación en **Data Lifecycle Management** específicas para prompts y respuestas de Copilot, agentes y aplicaciones IA conectadas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta trimestral del Comité de Gobernanza de IA y paquete de evaluación exportado de Compliance Manager `[Verificado MS Learn]`.

### SM-01 — Simulacro Semestral de Brecha de Datos y Exfiltración Masiva (Defender XDR + IRM + DSI + Legal)
- **Cadencia:** Semestral `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Ejercitar de extremo a extremo la respuesta coordinada entre SOC, Seguridad de Datos, RRHH, DPO y Legal ante un escenario combinado de robo de credenciales o insider malicioso con fuga de datos críticos.
- **Consola y Ruta:** `https://security.microsoft.com` + `https://purview.microsoft.com > Solutions > Data Security Investigations` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + SOC Manager + CSIRT + DPO / Legal `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Simular sobre datos sintéticos de prueba una exfiltración detectada en Endpoint DLP / Insider Risk correlacionada en **Microsoft Defender XDR**, midiendo el tiempo de elevación automática en **Adaptive Protection** `[Verificado MS Learn]`.
  2. Escalar el incidente hacia **Data Security Investigations (DSI)** en un contenedor de prueba acotado, ejecutando *Vector search*, *AI Categorization* y *Examination* para identificar PII y secretos simulados dentro del plazo legal de notificación (ej. 72h GDPR) `[Verificado MS Learn]`.
  3. Practicar el flujo segregado de autorización legal y ejecución de **Soft Purge** sobre un ítem de prueba, teniendo presente el tiempo de hasta **2 horas de propagación PIM** para roles Purview activados bajo demanda `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral de simulacro de brecha de datos con tiempos medidos y lecciones aprendidas `[Decisión / Propuesta Editorial]`.

### A-01 — Revisión Anual de Taxonomía Maestra de Sensibilidad, Marcos Regulatorios y Soberanía (Módulo 21)
- **Cadencia:** Anual `[Decisión / Propuesta Editorial]`.
- **Objetivo:** Recalibrar anualmente la arquitectura corporativa de clasificación de datos, el portafolio de plantillas en Compliance Manager y los requisitos de soberanía criptográfica y acceso privilegiado.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection / Compliance Manager` + `https://admin.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + CDO + General Counsel + DPO `[Decisión / Propuesta Editorial]`.
- **Procedimiento:**
  1. Revisar anualmente la taxonomía corporativa de etiquetas de sensibilidad, *Sensitive Information Types* personalizados y políticas de retención frente a cambios de negocio, fusiones o nuevas leyes sectoriales.
  2. Revalidar la asignación de las **3 plantillas regulatorias Premium incluidas** en M365 E5 / Purview Suite y licencias adicionales requeridas en Compliance Manager `[Verificado MS Learn]`.
  3. Auditar junto al responsable del **Módulo `21`** el cumplimiento anual de **Customer Lockbox**, rotación/salud de claves en **Customer Key** y políticas de **Microsoft 365 Privileged Access Management** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Documento anual de Arquitectura y Gobierno de Datos firmado por el Comité Ejecutivo `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01 — Playbook DSI-01: Investigación Asistida por IA y Contención ante Brecha o Exfiltración Confirmada
- **Disparador:** Incidente crítico en **Microsoft Defender XDR** con acceso/descarga de repositorios sensibles, caso grave de fuga en **Insider Risk Management** o hallazgo crítico de exfiltración en **DSPM** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents` -> `https://purview.microsoft.com > Solutions > Data Security Investigations` `[Verificado MS Learn]`.
- **Rol Responsable:** CSIRT / Data Security Investigator + Mitigation Admin + DPO / Legal `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Contención inicial convergente:** Aislar endpoints afectados o revocar sesiones en Defender XDR / Entra ID y verificar que el usuario involucrado quede elevado a **Elevated risk level** en **Adaptive Protection** para bloquear compartición externa, copia a USB, impresión y subida a nubes no autorizadas `[Verificado MS Learn]`.
  2. **Apertura acotada en Data Security Investigations (DSI):** Crear la investigación directamente desde el incidente XDR, el caso IRM o el hallazgo DSPM, sumando evidencia del *Unified Audit Log* (*Audit search*) y archivos capturados por *Endpoint DLP evidence collection* tras validar estimación preliminar de volumen PAYG `[Verificado MS Learn]`.
  3. **Análisis profundo con IA generativa:** Ejecutar **Categorization** (*Standard* o *Advanced AI*) para agrupar activos por severidad de riesgo, **Vector search** semántico para hallar documentación relacionada sin depender de palabras clave exactas, y **Examination** para descubrir credenciales expuestas, secretos de red, código fuente o datos personales sujetos a notificación regulatoria `[Verificado MS Learn]`.
  4. **Mitigación y purgado autorizado:** Con aprobación escrita de Legal/CISO y rol segregado de mitigación, ejecutar **Soft Purge** o **Hard Purge** sobre copias indebidas distribuidas internamente, reforzar etiquetas de cifrado y entregar al DPO el inventario exacto de PII afectada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe exportado de hallazgos de *Examination* en DSI, trazas en el *Unified Audit Log* de cada búsqueda/purga y notificación legal documentada `[Verificado MS Learn]`.

### AH-02 — Playbook AI-01: Exposición de Datos Confidenciales o Prompt Injection en Copilot, Foundry o Agent 365
- **Disparador:** Alerta de política *Risky AI usage* (Insider Risk), detección de *Prompt shields* en Communication Compliance, o hallazgo en `DSPM > AI observability` donde un usuario o instancia de **Agent 365** accede/expone información crítica indebidamente `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > DSPM > AI observability` + `Data Loss Prevention` + `eDiscovery` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Governance Lead + Data Security Engineer + SOC L2 `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. **Identificación de alcance:** Inspeccionar en `DSPM > AI observability` y `Activity explorer > AI activities` la identidad humana o el `Agent user ID` de la instancia de **Agent 365** / agente Copilot Studio involucrado, identificando los archivos fuente referenciados y sus etiquetas de sensibilidad `[Verificado MS Learn]`.
  2. **Corte de exposición en origen:** Si la fuga proviene de *oversharing* en SharePoint/OneDrive, restringir permisos del sitio/archivo de inmediato y aplicar etiqueta de sensibilidad con cifrado sin otorgar `VIEW`/`EXTRACT` a la instancia del agente ni a grupos amplios `[Verificado MS Learn]`. Si el agente actúa de forma anómala, suspender la instancia en **Microsoft Agent 365** / Entra ID (`Módulo 22`).
  3. **Búsqueda y eliminación forense de interacciones IA:** Si se volcaron secretos o datos regulados en prompts/respuestas almacenados en buzones, abrir caso en **Purview eDiscovery** usando la condición `Type > Copilot activity` para localizar y purgar selectivamente las interacciones comprometidas conforme al procedimiento oficial `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de auditoría de `Agent 365 activities` / `CopilotInteraction`, ajuste de permisos/etiqueta y acta de purga en eDiscovery `[Verificado MS Learn]`.

### AH-03 — Playbook GOV-01: Incorporación Regulatoria Urgente o Requerimiento de Auditoría Externa
- **Disparador:** Entrada en vigor de una nueva exigencia sectorial, requerimiento de ente regulador (ej. supervisión bancaria DORA, autoridad NIS2 o auditoría de sistemas IA bajo EU AI Act) o due diligence corporativo `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Compliance Manager > Regulations / Assessments` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC & Compliance Manager + Purview Compliance Admin `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. Localizar la plantilla oficial correspondiente entre las más de **360 regulaciones** de **Compliance Manager** (o crear plantilla personalizada si se trata de una norma local específica) verificando disponibilidad de licencias/plantillas Premium en el contador de regulaciones `[Verificado MS Learn]`.
  2. Crear la evaluación (*Assessment*) definiendo los servicios en alcance (Microsoft 365, Azure, multicloud o plantilla universal), aprovechando el reconocimiento automático de *Technical actions* ya implementadas en el tenant para obtener línea base en 24 horas `[Verificado MS Learn]`.
  3. Asignar acciones pendientes con fecha objetivo a dueños técnicos, adjuntar evidencias verificadas y otorgar rol temporal de solo lectura (*Compliance Manager Reader*) al auditor si requiere inspección directa `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete completo de evaluación y matriz de controles exportada desde Compliance Manager `[Verificado MS Learn]`.

### AH-04 — Playbook SEC-01: Abuso de Privilegios Administrativos o Modificación No Autorizada en Purview
- **Disparador:** Detección de desactivación no autorizada de políticas DLP/IRM/Retención, alteración de *Role groups* o *Administrative Units*, o inspección no justificada de documentos en *Content Explorer* / *DSI* `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Users / PIM` + `https://purview.microsoft.com > Settings > Roles and scopes / Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Incident Commander + Role Management Admin + CISO / DPO `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. Revocar sesiones en Microsoft Entra ID, desactivar membresías elegibles/activas en PIM y remover inmediatamente al actor del *Role group* en `Settings > Roles and scopes` `[Verificado MS Learn]`.
  2. Extraer desde `OfficeActivity` / **Audit (Premium)** todas las operaciones realizadas por el administrador durante la ventana de exposición (incluyendo consultas de búsqueda, descargas, cambios de políticas y actividades registradas en *Data Security Investigations activities*) `[Verificado MS Learn]`.
  3. Revertir las políticas alteradas, validar que las retenciones críticas cuenten con **Preservation Lock** cuando aplique (`Módulo 16`) y notificar al DPO si hubo acceso indebido a contenido personal o confidencial `[Verificado MS Learn]`.
- **Evidencia Auditable:** Traza inmutable de `OfficeActivity`, restauración de políticas verificada e informe disciplinario/forense `[Verificado MS Learn]`.

### AH-05 — Playbook FIN-01: Contención de Anomalía Presupuestaria en Medidores Pay-As-You-Go de Purview
- **Disparador:** Alerta de umbral superado (> 80% o pico diario > 200%) en Azure Cost Management sobre medidores de Microsoft Purview `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://portal.azure.com > Cost Management` + `https://purview.microsoft.com > Usage center / Solutions` `[Verificado MS Learn]`.
- **Rol Responsable:** FinOps Lead + Purview Platform Admin `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa:**
  1. Identificar en Azure Cost Management el medidor exacto causante del desvío (ej. política DLP/MIP asignada por error a miles de tablas/workspaces no-M365 o Fabric, bucle de *Proactive AI insights* en DSI, escaneo masivo de *On-demand classification*, alto tráfico en *Network Data Security* o consumo de *Overage SCUs*) `[Verificado MS Learn]`.
  2. Acotar inmediatamente el alcance (*scope*) de la política no-M365 a los contenedores productivos etiquetados como críticos, pausar *Proactive AI insights* si no es requerido 24/7 o ajustar el tope máximo de *Overage SCUs* sin afectar las políticas M365 cubiertas por licencia E5 por usuario `[Verificado MS Learn]`.
  3. Documentar causa raíz y actualizar la lista de verificación previa al despliegue de cualquier política con alcance multicloud o IA externa `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de alerta de presupuesto Azure, ajuste de *scope* aplicado y estabilización del costo diario `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL (Sentinel / Defender XDR) y PowerShell de Auditoría y Gobierno

#### Consulta 1 — Auditoría de Cambios Administrativos en Políticas DLP, Etiquetas, Retención y Role Groups de Purview (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Monitorea en OfficeActivity (ingesta gratuita en Sentinel) cambios críticos en Purview
OfficeActivity
| where TimeGenerated > ago(24h)
| where RecordType in ("ComplianceDLPSharePoint", "ComplianceDLPExchange", "ExchangeAdmin", "SecurityComplianceCenterEOPCmdlet", "MipLabel")
    or Operation has_any ("DlpCompliancePolicy", "DlpComplianceRule", "RetentionCompliancePolicy", "RoleGroup", "AdministrativeUnit", "InsiderRisk", "SensitivityLabel")
| where Operation has_any ("New-", "Set-", "Remove-", "Add-RoleGroupMember", "Remove-RoleGroupMember", "Disable-")
| project TimeGenerated, UserId, Operation, RecordType, ClientIP, ResultStatus, Parameters
| order by TimeGenerated desc
```

#### Consulta 2 — Correlación en Defender XDR de Incidentes que Combinan Alertas Purview (DLP / IRM) con Amenazas Externas (KQL Advanced Hunting) `[Verificado MS Learn]`
```kql
// Identifica usuarios presentes simultáneamente en alertas de Purview (DLP/IRM) y alertas de Identidad/Endpoint
let PurviewAlerts = AlertInfo
    | where Timestamp > ago(7d)
    | where ServiceSource in ("Microsoft Purview Data Loss Prevention", "Microsoft Purview Insider Risk Management", "Microsoft Data Loss Prevention")
    | join kind=inner (AlertEvidence | where EntityType == "User") on AlertId
    | summarize PurviewAlertCount = dcount(AlertId), PurviewTitles = make_set(Title, 5) by AccountUpn;
AlertInfo
| where Timestamp > ago(7d)
| where ServiceSource !in ("Microsoft Purview Data Loss Prevention", "Microsoft Purview Insider Risk Management", "Microsoft Data Loss Prevention")
| join kind=inner (AlertEvidence | where EntityType == "User") on AlertId
| summarize ThreatAlertCount = dcount(AlertId), ThreatSources = make_set(ServiceSource, 5), ThreatTitles = make_set(Title, 5) by AccountUpn
| join kind=inner PurviewAlerts on AccountUpn
| project AccountUpn, PurviewAlertCount, PurviewTitles, ThreatAlertCount, ThreatSources, ThreatTitles
| order by PurviewAlertCount desc, ThreatAlertCount desc
```

#### Consulta 3 — Observabilidad de Interacciones con Microsoft 365 Copilot y Agentes IA en Auditoría (KQL Sentinel / CloudAppEvents) `[Verificado MS Learn]`
```kql
// Rastrea volumen y contexto de interacciones Copilot y agentes registradas en telemetría M365/XDR
CloudAppEvents
| where Timestamp > ago(7d)
| where ActionType has_any ("CopilotInteraction", "Agent", "AIPrompt") or Application has "Copilot"
| summarize TotalInteractions = count(),
            DistinctApps = make_set(Application, 10),
            LastActivityUTC = max(Timestamp)
            by AccountDisplayName, AccountId
| order by TotalInteractions desc
```

#### Consulta 4 — Detección de Compartición Externa o Vínculos Anónimos sobre Sitios Críticos (*Oversharing*) (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Detecta creación de vínculos anónimos (Anyone) o compartición externa en SharePoint y OneDrive
OfficeActivity
| where TimeGenerated > ago(7d)
| where OfficeWorkload in ("SharePoint", "OneDrive")
| where Operation in ("AnonymousLinkCreated", "AnonymousLinkUpdated", "SharingInvitationCreated", "CompanyLinkCreated")
| summarize LinksCreated = count(), SampleUrls = make_set(OfficeObjectId, 5), LastShareUTC = max(TimeGenerated)
    by UserId, Operation, Site_Url
| order by LinksCreated desc
```

#### Consulta 5 — Salud de Ingesta de Microsoft Purview Information Protection (Beneficio E5 Data Grant) (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Verifica eventos de etiquetado, cambio o degradación de sensibilidad en MicrosoftPurviewInformationProtection
MicrosoftPurviewInformationProtection
| where TimeGenerated > ago(7d)
| summarize EventsCount = count(),
            UniqueUsers = dcount(UserId),
            DowngradesOrRemovals = countif(Activity has_any ("Downgrade", "RemoveLabel"))
            by Activity
| order by EventsCount desc
```

#### Consulta 6 — Vigilancia de Búsquedas y Acciones Sensibles en eDiscovery y Data Security Investigations (KQL Sentinel) `[Verificado MS Learn]`
```kql
// Audita quién ejecuta búsquedas de contenido, exportaciones o acciones de Data Security Investigations
OfficeActivity
| where TimeGenerated > ago(7d)
| where Operation has_any ("SearchCreated", "SearchExported", "Preview", "Purge", "Investigation", "ContentExplorer")
| project TimeGenerated, UserId, Operation, RecordType, ClientIP, ObjectId
| order by TimeGenerated desc
```

#### Consulta 7 — Auditoría de Role Groups y Asignación de Administrative Units en Security & Compliance PowerShell `[Verificado MS Learn]`
```powershell
# Conexión al endpoint de Security & Compliance PowerShell (requiere módulo ExchangeOnlineManagement v3+)
Connect-IPPSSession -ShowBanner:$false

$criticalGroups = @(
    "Organization Management",
    "Compliance Administrator",
    "Data Loss Prevention",
    "Insider Risk Management",
    "Insider Risk Management Investigators",
    "eDiscovery Manager",
    "Content Explorer Content Viewer"
)

$auditReport = foreach ($rgName in $criticalGroups) {
    $rg = Get-RoleGroup -Identity $rgName -ErrorAction SilentlyContinue
    if ($rg) {
        $members = Get-RoleGroupMember -Identity $rgName
        [PSCustomObject]@{
            RoleGroup   = $rg.Name
            MemberCount = ($members | Measure-Object).Count
            Members     = ($members.Name -join "; ")
            Description = $rg.Description
        }
    }
}
$auditReport | Export-Csv -Path ".\Purview_RoleGroups_Audit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation -Encoding UTF8
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*) `[Verificado MS Learn]`

| Componente / Integración | Consola y Ruta de Verificación | Criterio Objetivo de Operatividad (*Proof of Life*) |
|---|---|---|
| **Portal Unificado Purview** | `https://purview.microsoft.com > Solutions` | Acceso activo a tarjetas *Data Security*, *Risk & Compliance* y *Data Governance*; sin referencias operativas a `compliance.microsoft.com`. |
| **DSPM Unificado y AI Observability** | `purview.microsoft.com > Solutions > DSPM > Posture / AI observability` | *Data security objectives* poblados y telemetría de últimos 30 días visible para Copilot, agentes y **Agent 365**. |
| **Adaptive Protection Activo** | `purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection` | Niveles de riesgo sincronizando dinámicamente con políticas DLP en modo aplicación (`On`) y Acceso Condicional. |
| **Convergencia con Defender XDR** | `security.microsoft.com > Incidents & alerts > Incidents` | Alertas de Purview DLP e Insider Risk correlacionándose en incidentes XDR con enlace de apertura hacia **DSI**. |
| **Compliance Manager Continuo** | `purview.microsoft.com > Solutions > Compliance Manager > Overview` | *Compliance Score* activo sobre *Microsoft Data Protection Baseline* y las plantillas regulatorias priorizadas con refresco de 24h. |
| **Administrative Units y RBAC** | `purview.microsoft.com > Settings > Roles and scopes > Role groups` | *Role groups* delegados vinculados a *Administrative Units* de Entra ID y sin cuentas *Global Administrator* permanentes. |
| **Gobierno FinOps PAYG / SCU** | `portal.azure.com > Cost Management` + `purview.microsoft.com > Usage center` | Presupuestos y alertas activas sobre medidores PAYG de Purview, almacenamiento DSI y bloques horarios de SCUs. |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operativos, de IA y de Cumplimiento `[Decisión / Propuesta Editorial]`

> **Nota metodológica:** Si bien Microsoft Purview calcula métricas nativas como el *Compliance Score* (con puntajes fijos de 27/9/3/1 puntos por acción) y porcentajes de cobertura en DSPM, **no impone metas porcentuales universales obligatorias**. Los ocho indicadores siguientes constituyen objetivos consultivos recomendados para comités ejecutivos de Seguridad de Datos, IA y GRC `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Medición | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Cobertura de Etiquetado en Repositorios con Datos Sensibles** | `(Activos con SITs detectados que poseen etiqueta de sensibilidad aplicada / Total activos con SITs en DSPM Asset Explorer) * 100` | `>= 90 %` en repositorios críticos M365 y Fabric | Mensual | CISO / CDO | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Reducción de Sitios con Oversharing Crítico Expuestos a IA** | `(Sitios SharePoint/OneDrive con datos sensibles y vínculos Anyone o Org-wide abiertos / Total sitios con datos sensibles) * 100` | `< 2 %` (`0` vínculos `Anyone` en sitios `Highly Confidential`) | Semanal | CISO / AI Governance | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Cobertura de Gobernanza Purview sobre Agentes IA Activos** | `(Instancias activas de Agent 365, Copilot Studio y Foundry incluidas en políticas DLP + IRM + DLM / Total agentes activos en AI observability) * 100` | `100 %` | Semanal | AI Governance Lead / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Compliance Score sobre Controles Gestionados por el Cliente** | `(Puntos obtenidos en Your Controls + Shared Controls / Total puntos posibles del cliente en evaluaciones activas de Compliance Manager) * 100` | `>= 85 %` *(100 % en Preventative mandatory de 27 pts)* | Mensual | GRC / DPO / Directorio | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo Medio de Triaje de Incidentes Convergentes Datos + XDR** | `Promedio(Timestamp primera acción analista - Timestamp creación incidente XDR con alerta DLP/IRM High)` | `<= 30 minutos` (High) / `<= 4 horas` (Medium) | Diaria / Semanal | SOC Manager / CSIRT | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Efectividad del Bucle Dinámico de Adaptive Protection** | `(Políticas DLP de Adaptive Protection en modo Enforcement activo sobre EXO, Teams y Endpoints / Total políticas Adaptive Protection requeridas) * 100` | `100 %` y `>= 98 %` endpoints con onboarding activo | Semanal | Data Security Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Segregación Jurisdiccional y Mínimo Privilegio en Purview RBAC** | `(Administradores regionales con Administrative Units asignadas y revisores Content Viewer bajo PIM JIT / Total administradores elegibles) * 100` | `100 %` (`0` accesos permanentes a contenido plano) | Trimestral | DPO / Internal Audit | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Adherencia Presupuestaria FinOps en Medidores PAYG y SCUs** | `(Gasto mensual real en medidores Azure Purview PAYG + DSI + SCUs / Presupuesto mensual aprobado) * 100` | `<= 100 %` *(desvío no planificado < 10 %)* | Semanal / Mensual | FinOps / CIO / CISO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de Cinco Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Estadio de Madurez | Caracterización en Microsoft Purview Suite |
|---|---|---|
| **Nivel 1** | **Fragmentado / Reactivo** | Uso residual de etiquetas manuales aisladas, políticas DLP solo en modo simulación perpetua, *Global Administrator* compartido, sin visibilidad sobre uso de IA generativa ni integración con el SOC. |
| **Nivel 2** | **Fundacional en M365** | Migración completada a `purview.microsoft.com`, taxonomía inicial MIP desplegada, políticas DLP básicas en Exchange/SharePoint y revisión pasiva del *Data Protection Baseline* en Compliance Manager. |
| **Nivel 3** | **Integrado y Orientado a Postura** | Operación activa de **DSPM** por *Data security objectives*, Endpoint y Browser DLP desplegados, alertas DLP/IRM correlacionadas en **Microsoft Defender XDR**, *Role groups* con PIM y evaluaciones regulatorias prioritarias activas. |
| **Nivel 4** | **Adaptativo y Gobernado para IA** | **Adaptive Protection** aplicando bloqueos dinámicos según riesgo IRM, **AI observability** gobernando Copilot, Copilot Studio, Foundry y **Agent 365** (incluyendo control estricto del derecho `EXTRACT`), **Administrative Units** restringidas y disciplina FinOps sobre PAYG. |
| **Nivel 5** | **Optimizado, Multicloud y Asistido por IA** | **Data Security Investigations (DSI)** integrado en respuesta a brechas con búsqueda vectorial y purga gobernada, cobertura multicloud y **Microsoft Fabric** en *Unified Catalog* / *Sentinel Data Lake*, y cumplimiento continuo automatizado (> 85%) frente a NIST CSF 2.0, DORA, NIS2 y EU AI Act. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota de auditoría:** La siguiente tabla vincula las capacidades arquitectónicas y de gobierno de Microsoft Purview Suite con las **seis funciones de NIST CSF 2.0 (CSWP 29)** y tácticas **MITRE ATT&CK**, definiendo evidencia objetiva reproducible `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría | Resultado de Seguridad (CSWP 29) | Capacidad Habilitadora en Microsoft Purview Suite | Táctica / Técnica MITRE ATT&CK | Evidencia Auditable Reproducible | Etiqueta |
|---|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OC-03` | Requisitos legales, regulatorios y contractuales de protección de datos e IA comprendidos y gestionados. | **Microsoft Purview Compliance Manager** con más de 360 plantillas regulatorias (NIST CSF 2.0, GDPR, DORA, NIS2, EU AI Act, ISO 27001/42001) y cálculo continuo de *Compliance Score*. | Governance & Regulatory Compliance | Evaluaciones exportadas de Compliance Manager con trazabilidad de controles propios, compartidos y de Microsoft (`M-02`). | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Roles, responsabilidades y segregación de deberes establecidos y forzados técnicamente. | **Role groups** en `purview.microsoft.com`, seudonimización en IRM/Comm Compliance, **Restricted Administrative Units** y activación JIT en Entra ID PIM. | Valid Accounts (`T1078`) / Insider Abuse | Exportación PowerShell de `Get-RoleGroup`, mapeo de *Administrative Units* y actas de *Access Reviews* (`T-01`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-07` | Inventarios de datos y metadatos correspondientes mantenidos y clasificados por criticidad. | **DSPM Asset Explorer**, clasificadores SIT/entrenables, **Data Map** (con *Live view* para Azure y Fabric) y **Unified Catalog**. | Data from Cloud Storage (`T1530`) / Repositories (`T1213`) | Reportes mensuales de `DSPM > Asset explorer` y `Unified Catalog > Health management > Reports` (`M-01`, `M-04`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-05` | Amenazas, vulnerabilidades de exposición de datos y riesgos de IA priorizados según impacto. | **DSPM Data Security Objectives**, **AI observability** (incluyendo **Microsoft Agent 365**) y **Data risk assessments** para detección de *oversharing*. | Collection (`TA0009`) | Resultados semanales de `Data risk assessments` e inventario priorizado de agentes en `AI observability` (`S-01`, `S-03`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` | Confidencialidad, integridad y disponibilidad de datos en reposo protegidas. | Etiquetas de sensibilidad con cifrado persistente (incluyendo control explícito de derechos `VIEW` y `EXTRACT` frente a Copilot y Agent 365) y **Customer Key** (`Módulo 21`). | Data from Information Repositories (`T1213`) | Políticas de etiquetado habilitadas en SharePoint/OneDrive y estadísticas en `MicrosoftPurviewInformationProtection`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-02` | Confidencialidad e integridad de datos en tránsito, en uso y en interacciones IA protegidas. | **Purview DLP** omnicanal (M365, Endpoint DLP, Browser DLP en Edge for Business, **Network Data Security** y Fabric) gobernado dinámicamente por **Adaptive Protection**. | Exfiltration Over Web Service (`T1567`) / Removable Media (`T1052`) | Políticas DLP activas vinculadas a niveles de riesgo de `Adaptive protection` (`D-04`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Permisos de acceso a datos gestionados y revocados bajo privilegio mínimo. | Remediación de vínculos anónimos/*oversharing* en DSPM, integración de niveles de riesgo IRM con **Entra Conditional Access** y **Customer Lockbox / PAM** (`Módulo 21`). | Valid Accounts (`T1078`) | Consulta KQL 4 de control de vínculos `AnonymousLinkCreated` y políticas CA basadas en riesgo interno. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-06` | Actividades de proveedores externos, servicios SaaS e IA de terceros monitoreadas. | Telemetría en `Activity explorer > AI activities`, extensión de navegador, **Network Data Security** y conectores multicloud (AWS, GCP, Box, Snowflake). | Exfiltration to Cloud Storage (`T1567.002`) | Registros en `Activity explorer` y detecciones de *Risky AI usage* / *Prompt shields* sobre apps GenAI externas. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-03` | Información de múltiples fuentes correlacionada para detectar incidentes complejos. | Correlación nativa de alertas **Purview DLP** e **Insider Risk Management** dentro de incidentes unificados de **Microsoft Defender XDR** y **Microsoft Sentinel**. | Multi-Stage Collection & Exfiltration (`TA0009`, `TA0010`) | Incidentes correlacionados en `security.microsoft.com` y salida de Consulta KQL 2 (`D-03`). | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.AN-03` | Análisis ejecutado para establecer qué ocurrió durante un incidente y cuál es el impacto en datos. | **Data Security Investigations (DSI)** con **Vector search**, **Categorization** con IA y **Examination** de credenciales, PII y propiedad intelectual junto con **Audit Premium**. | Automated Exfiltration (`T1020`) | Informe de *Examination* exportado desde DSI y trazas de *Audit search* (`AH-01`). | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Incidentes contenidos para prevenir expansión de la fuga o abuso. | Bloqueo automático en **Adaptive Protection**, suspensión de agentes IA riesgosos y mitigación en **DSI** mediante **Soft Purge / Hard Purge**. | Data Staged (`T1074`) / Exfiltration (`TA0010`) | Auditoría en `OfficeActivity` de acciones de purgado aprobadas y elevación de perfil en Adaptive Protection. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-05` | Integridad de activos restaurada y preservación probatoria asegurada tras un incidente. | Retenciones inmutables (**Preservation Lock** en `Módulo 16`), conservación legal en el nuevo **eDiscovery** unificado (`Módulo 20`) y restauración de políticas auditadas (`AH-04`). | Data Destruction (`T1485`) / Defacement | Confirmación de *holds* legales en eDiscovery moderno y actas del simulacro semestral `SM-01`. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Destinatario | Certificaciones y Rutas Oficiales Microsoft Learn (Vigentes Nov-2026) | Recursos Especializados (`Ninja Training 2026` y Blogs Oficiales Microsoft) | Laboratorio Práctico Recomendado |
|---|---|---|---|
| **Data Security Architect & DLP/MIP/IRM Engineers** | Certificación **SC-401** (*Microsoft Certified: Information Security Administrator Associate* — certificación vigente enfocada en seguridad de datos e IA en Purview) `[Verificado MS Learn]`. | **Ninja Training Seguridad Microsoft 2026 — Módulo 12 (`Purview DSPM y Seguridad de datos para IA`)** y Microsoft Security Blog (categoría Microsoft Purview) `[Verificado MS Learn]`. | Configurar *Data security objectives* en DSPM, activar *Adaptive Protection* y probar derechos `EXTRACT` con Copilot y Agent 365. |
| **GRC Manager, DPO & Auditores Internos** | Rutas oficiales *Manage compliance with Microsoft Purview Compliance Manager* y *Administrative Units in Microsoft Purview* en Microsoft Learn `[Verificado MS Learn]`. | **Ninja Training Seguridad Microsoft 2026 — Módulo 11 (`Purview Compliance Manager`)** y guía oficial de cálculo del *Compliance Score* `[Verificado MS Learn]`. | Desplegar evaluación **NIST CSF 2.0** y **EU AI Act**, cargar evidencia de *Shared controls* y validar segregación con *Administrative Units*. |
| **SOC L2 / CSIRT & Data Security Investigators** | Certificación **SC-200** (*Security Operations Analyst Associate*) + documentación oficial de **Data Security Investigations (DSI)** e integración Purview-XDR `[Verificado MS Learn]`. | Serie oficial de arquitectura y demos de *Microsoft Purview Data Security Investigations* y *Microsoft Mechanics: New DSPM* `[Verificado MS Learn]`. | Escalar un incidente XDR con alerta DLP hacia DSI, ejecutar *Vector search* / *Examination* y auditar actividades en `OfficeActivity`. |
| **CDO Office & FinOps Lead** | Rutas *Microsoft Purview Data Governance in the new portal* y *Learn about Microsoft Purview billing models* en Microsoft Learn `[Verificado MS Learn]`. | Calculadoras oficiales de precios Azure para **Microsoft Purview PAYG** y gestión horaria de **Security Compute Units (SCUs)** `[Verificado MS Learn]`. | Configurar *Live view* para Microsoft Fabric en *Unified Catalog* y crear presupuestos/alertas por medidor PAYG en Azure Cost Management. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Incorporadas tras Revalidación en Microsoft Learn MCP (`2026-11-11`)

| # | Estado en Material Previo (`MSEOP-MD`) | Hallazgo Verificado en Microsoft Learn al `2026-11-11` | Corrección Incorporada en esta Guía Definitiva v2.0 |
|---|---|---|---|
| **1** | Denominación comercial *Microsoft 365 E5 Compliance* y referencias operativas al portal clásico `compliance.microsoft.com`. | Desde octubre de 2025 el portafolio se denomina oficialmente **Microsoft Purview Suite** (incluyendo variantes FLW, Gov, EDU y Business Premium), y el portal clásico `compliance.microsoft.com` fue retirado definitivamente a fines de 2024 (MC939918), unificando toda operación en `https://purview.microsoft.com` `[Verificado MS Learn]`. | Se actualizó toda la taxonomía de licenciamiento, navegación y tabla de funciones reubicadas del nuevo portal en Secciones 2.2 y 3.2. |
| **2** | Separación entre vistas aisladas de postura y ausencia de observabilidad específica para agentes autónomos corporativos. | La versión actual de **Data Security Posture Management (DSPM)** (`Solutions > DSPM`) unifica postura tradicional e IA (dejando *DSPM classic* y *DSPM for AI classic* como legados), incorpora **Data security objectives**, el **Data Security Posture Agent** y la página exclusiva **AI observability** con soporte para **Microsoft Agent 365** `[Verificado MS Learn]`. | Se estructuraron las cadencias `D-01`, `D-02`, `S-01` y `S-03` sobre la versión unificada vigente de DSPM y *AI observability*. |
| **3** | Ausencia de una solución nativa con IA generativa para investigar el contenido real afectado en una brecha de datos sin depender únicamente de flujos legales clásicos. | **Microsoft Purview Data Security Investigations (DSI)** provee **Vector search**, **Categorization** con IA, **Examination** de riesgos ocultos y mitigación **Soft/Hard Purge**, integrado con Defender XDR, IRM, DSPM (*Proactive AI insights*), Endpoint DLP y Audit `[Verificado MS Learn]`. | Se integró DSI como pilar arquitectónico, tarea semanal `S-06`, simulacro `SM-01` y playbook central `AH-01`. |
| **4** | Referencias a *Content Search*, *eDiscovery Standard* y *eDiscovery Premium* clásicos como consolas separadas. | Microsoft retiró **todas las experiencias clásicas de eDiscovery el 31 de agosto de 2025**, integrando *Content Search* dentro de la solución moderna unificada de **eDiscovery** (incluyendo búsqueda y purga de `Copilot activity`) `[Verificado MS Learn]`. | Se corrigió en Sección 3.2, `T-01` y playbook `AH-02`, alineando con el Módulo `20`. |
| **5** | Falta de detalle sobre el modelo de facturación por consumo más allá de licencias por usuario M365 E5. | Microsoft Purview opera un modelo dual complementario: licencia por usuario (incluye M365 Copilot sin cargo extra) + **Pay-As-You-Go en Azure** para activos no-M365/Fabric, interacciones GenAI externas, *Network Data Security*, *Text records* (1.000 caracteres), DGPUs (60 min), DSI (con cargo continuo cada 24h si se activa *Proactive AI insights*) y SCUs en bloques horarios `[Verificado MS Learn]`. | Se incorporó matriz financiera detallada en Sección 2.2, control diario `D-07`, conciliación mensual `M-03` y playbook `AH-05`. |
| **6** | Omisión de reglas operativas al combinar Entra ID PIM y Administrative Units con permisos de Purview. | Microsoft Learn documenta que la activación JIT de grupos en **Entra ID PIM puede tardar hasta 2 horas** en hacerse efectiva en Purview, y que **Administrative Units** soportan delegación restringida en DLP, IRM, Communication Compliance, DLM, Records, MIP, Audit y eDiscovery `[Verificado MS Learn]`. | Se documentó la regla de 2 horas de PIM y el alcance exacto de *Administrative Units* en Sección 4.1, `S-04`, `T-01` y `SM-01`. |
| **7** | El corpus previo de Purview Suite en `MSEOP-MD` era únicamente estratégico y carecía de rutinas operativas conectadas con el SOC. | Se articuló un modelo operacional completo de 27 actividades (`Diaria` a `Ad-Hoc`) conectando Purview con **Microsoft Defender XDR** (correlación de incidentes), **Adaptive Protection** (`Elevated`/`Moderate`/`Minor`) y los módulos especializados `14` a `22` `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`. | Transformación en guía maestra operativa y de gobierno transversal cumpliendo el 100% de la especificación v2.0. |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas `[Decisión / Propuesta Editorial]`

| # | Elemento Consultivo / Diseño Editorial | Justificación Arquitectónica y de Gobierno |
|---|---|---|
| **1** | **Diseño de Módulo 13 como plano rector transversal articulado con los Módulos `14` a `22`** | Evita duplicar la ingeniería detallada de reglas MIP/DLP/DLM/IRM/Audit/eDiscovery y provee al CISO, CDO y SOC un único modelo coherente de gobierno, postura IA, permisos y costos. |
| **2** | **Metas cuantitativas en `KPI-01` a `KPI-08` y SLAs de triaje convergente (<= 30 min High)** | Traduce métricas nativas de DSPM, Compliance Manager y Defender XDR en compromisos operativos medibles para el comité de riesgos. |
| **3** | **Separación obligatoria entre *List Viewer* y *Content Viewer* (solo JIT con aprobación DPO) y entre *Investigator* y *Mitigation Admin* en DSI** | Protege la privacidad interna y evita que un único analista lea indiscriminadamente archivos confidenciales o ejecute *Hard Purge* sin control cruzado legal. |
| **4** | **Matriz RACI transversal entre CISO/DataSec, GRC/DPO, SOC/XDR, CDO/AI y FinOps** | Resuelve la tensión habitual en proyectos Purview donde Seguridad, Legal, Datos y Finanzas comparten un mismo portal sin fronteras claras de decisión. |
| **5** | **Mapeo probatorio a 12 subcategorías de las 6 funciones de NIST CSF 2.0 y modelo de madurez de 5 niveles** | Estandariza la presentación de evidencias técnicas de Purview Suite ante auditorías regulatorias y juntas directivas. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn (`[Verificado MS Learn]`)
- **REF-01:** *Learn about the Microsoft Purview portal (`purview.microsoft.com` & relocated features)* — `https://learn.microsoft.com/en-us/purview/purview-portal`
- **REF-02:** *Microsoft Purview service description (Microsoft Purview Suite & licensing matrix)* — `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description`
- **REF-03:** *Learn about Data Security Posture Management (Current unified DSPM, Data security objectives & AI observability)* — `https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about`
- **REF-04:** *Use Microsoft Purview to manage data security & compliance for AI agents* — `https://learn.microsoft.com/en-us/purview/ai-agents`
- **REF-05:** *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365* — `https://learn.microsoft.com/en-us/purview/ai-agent-365`
- **REF-06:** *Learn about Data Security Investigations (AI Vector search, Categorization, Examination & Purge)* — `https://learn.microsoft.com/en-us/purview/data-security-investigations`
- **REF-07:** *Microsoft Purview Compliance Manager overview* — `https://learn.microsoft.com/en-us/purview/compliance-manager`
- **REF-08:** *Compliance Manager scoring (27/9/3/1 point calculation & action types)* — `https://learn.microsoft.com/en-us/purview/compliance-score-calculation`
- **REF-09:** *Compliance Manager regulations list (Included baseline, 3 free E5 premium templates & AI regulations)* — `https://learn.microsoft.com/en-us/purview/compliance-manager-regulations-list`
- **REF-10:** *Learn about Microsoft Purview billing models (Per-user vs. Pay-As-You-Go meters & SCUs)* — `https://learn.microsoft.com/en-us/purview/purview-billing-models`
- **REF-11:** *Permissions in the Microsoft Purview portal (Role groups & 2-hour PIM propagation)* — `https://learn.microsoft.com/en-us/purview/purview-permissions`
- **REF-12:** *Administrative units in Microsoft Purview* — `https://learn.microsoft.com/en-us/purview/purview-admin-units`
- **REF-13:** *Learn about Adaptive Protection in Data Loss Prevention (Insider Risk + DLP integration)* — `https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn`
- **REF-14:** *Alert correlation and incident merging in the Microsoft Defender portal (Purview DLP & IRM integration)* — `https://learn.microsoft.com/en-us/defender-xdr/alerts-incidents-correlation`
- **REF-15:** *Microsoft Purview eDiscovery legacy solutions retirement (August 31, 2025)* — `https://learn.microsoft.com/en-us/purview/edisc-legacy`

### 15.2 Recursos Oficiales de Habilitación Microsoft, Comunidad y Marcos Normativos
- **REF-16:** *Microsoft Certified: Information Security Administrator Associate (Exam SC-401)* — Microsoft Learn (`https://learn.microsoft.com/en-us/credentials/certifications/information-security-administrator/`)
- **REF-17:** *Microsoft Purview Blog — Microsoft Tech Community (Official Product Team Announcements)* — Microsoft (`https://techcommunity.microsoft.com/category/security/blog/microsoftpurviewblog`)
- **REF-18:** *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* — National Institute of Standards and Technology (`https://doi.org/10.6028/NIST.CSWP.29`)
- **REF-19:** *NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0 — NIST AI 100-1)* — National Institute of Standards and Technology (`https://doi.org/10.6028/NIST.AI.100-1`)

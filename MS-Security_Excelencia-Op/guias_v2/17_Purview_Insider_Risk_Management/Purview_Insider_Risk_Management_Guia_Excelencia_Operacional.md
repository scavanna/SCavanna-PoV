# Guía Maestra de Excelencia Operacional: Microsoft Purview Insider Risk Management

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Definición Oficial y Alcance Operativo |
| --- | --- |
| **Identificador del Módulo** | `17_Purview_Insider_Risk_Management` |
| **Slug Canónico** | `Purview_Insider_Risk_Management` |
| **Nombre Completo** | Microsoft Purview Insider Risk Management |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | `Compilado MSEOP-MD + Revalidado Learn` (consolidación depurada de `MSEOP-MD\Purview IRM`, cruce de referentes con *Ninja Training Seguridad Microsoft 2026 — Módulo 07* y revalidación directa contra Microsoft Learn MCP al 11 de noviembre de 2026) |
| **Relación con Microsoft 365 E5** | `Incluido en Microsoft 365 E5` (incluido nativamente en Microsoft 365 E5 / E7 / A5 / G5 / F5 Compliance y Microsoft Purview Suite; indicadores específicos no-M365/IA y el Triage Agent con Security Copilot utilizan medidores Pay-As-You-Go / SCUs; Forensic Evidence opera como add-on opt-in con 20 GB de prueba) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (`Solutions > Insider Risk Management`), `https://security.microsoft.com` (`Incidents & alerts` y `Hunting > Advanced hunting`) y `https://entra.microsoft.com` (`Protection > Conditional Access`) `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, SOC Manager, Analistas e Investigadores de Riesgo Interno (L1/L2/L3), Oficial de Privacidad (DPO), Recursos Humanos (Employee Relations), Asesoría Legal (eDiscovery), Auditoría Interna y Administradores de Purview / Entra ID `[Decisión / Propuesta Editorial]` |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), SEI/CERT *Common Sense Guide to Mitigating Insider Threats* (7th Ed.), ISO/IEC 27001:2022, ISO/IEC 27701, GDPR (Art. 5, 25, 32 y 35 — DPIA / Consejos de Empresa) y leyes regionales de protección de datos laborales `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]` |

> **Nota de Consolidación y Saneamiento Documental (Corte `2026-11-11`):** En la auditoría de las fuentes originales de `MSEOP-MD\Purview IRM` (`0404 - Purview IRM - Bloques - SecOps`, `Version Consolidada (1)` y `Purview IR\Construye una tabla (1)`), se detectó una exportación cruzada de guías genéricas de Microsoft Sentinel, Defender for Office 365 e Intune ajenas al dominio de riesgo interno, además de una imprecisión técnica en `Purview IR` que atribuía el registro de auditoría de IRM al Unified Audit Log general. Todos los bloques genéricos fueron descartados y corregidos contra Microsoft Learn a noviembre de 2026 `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026: Convergencia de Riesgo Humano, Agentes IA y Mitigación Dinámica

A diferencia de las amenazas perimetrales externas, el riesgo interno —malicioso, negligente o derivado de credenciales legítimas comprometidas— opera autenticado dentro del perímetro de confianza. A noviembre de 2026, **Microsoft Purview Insider Risk Management (IRM)** evoluciona desde una herramienta de cumplimiento retrospectivo hacia un motor analítico y preventivo en tiempo casi real que correlaciona señales de Microsoft 365, endpoints Windows y macOS, navegadores (Microsoft Edge y Google Chrome), **Microsoft Defender XDR**, **Microsoft Entra ID**, conectores de Recursos Humanos y acceso físico, e interacciones con **Microsoft 365 Copilot, Copilot Studio, agentes de Microsoft Foundry y sitios de IA generativa de terceros** `[Verificado MS Learn]`.

El diferenciador arquitectónico decisivo de Purview IRM frente a soluciones UEBA o DLP tradicionales reside en cerrar el ciclo completo bajo **Privacidad por Diseño** `[Verificado MS Learn]`:
1. **Línea base sin fricción (*Insider Risk Analytics*):** Permite evaluar riesgos agregados y anónimos en todo el tenant sin crear políticas previas, entregando recomendaciones en tiempo real para calibrar umbrales y evitar fatiga de alertas `[Verificado MS Learn]`.
2. **Detección conductual contextual y agéntica:** Combina detección de secuencias (*Collection → Exfiltration → Obfuscation → Clean-up*), detección de exfiltración acumulada *low-and-slow* a 30 días comparada contra grupos de pares (*Peer Groups* en Entra ID), plantillas dedicadas a **Risky AI usage** y la nueva política predeterminada **Risky Agents (preview)**, acelerando el triaje mediante el **Purview Alert Triage Agent** impulsado por Microsoft Security Copilot `[Verificado MS Learn]`.
3. **Mitigación cerrada en tiempo real (*Adaptive Protection*):** Conecta dinámicamente el nivel de riesgo calculado del usuario (*Elevated*, *Moderate*, *Minor*) con controles preventivos automáticos en **Purview DLP**, **Microsoft Entra Conditional Access** y **Purview Data Lifecycle Management** (preservación automática de 120 días de datos eliminados), manteniendo la productividad intacta para la mayoría de bajo riesgo `[Verificado MS Learn]`.

### 2.2 Matriz Oficial de Licenciamiento, Prerrequisitos y Medidores Complementarios (Corte Noviembre 2026)

El licenciamiento de Insider Risk Management se rige por usuario beneficiado por las políticas o analíticas activas, complementado por medidores específicos para señales no-Microsoft, captura forense visual y cómputo agéntico `[Verificado MS Learn]`:

| Capacidad / Componente | Licencia Base Incluida | Add-ons / Medidores Pay-As-You-Go o Capacidad | Prerrequisitos Técnicos Clave | Estado |
| --- | --- | --- | --- | --- |
| **Motor central IRM, Plantillas base, Analytics, Activity Explorer, Cases y Adaptive Protection** | **Microsoft 365 E5 / E7 / A5 / G5**, **Microsoft 365 F5 Compliance / F5 Security + Compliance**, **Office 365 E5** (según alcance de cargas) o **Microsoft Purview Suite** / add-on *Insider Risk Management* sobre E3 | Sin costo extra para señales nativas M365, Entra ID, Defender y SharePoint/Exchange/Teams | Auditoría habilitada; disponibilidad regional de dependencias Azure en nube comercial (no disponible aún en nubes US Government) | `[Verificado MS Learn]` |
| **Indicadores de apps cloud de terceros (Box, Dropbox, Google Drive) e IA externa / navegador** | Requiere licencia base IRM por usuario | Requiere habilitar facturación **Pay-As-You-Go** en Azure para indicadores específicos no-M365 y **Collection Policies** para apps GenAI externas | Onboarding de dispositivos o extensión de Microsoft Purview en Chrome / señal nativa en Microsoft Edge | `[Verificado MS Learn]` |
| **Monitoreo de uso riesgoso de IA (*Risky AI usage*) y Agentes (*Risky Agents — preview*)** | Incluido para Microsoft 365 Copilot (con licencia Copilot + IRM) y disponible por defecto para agentes elegibles | Pay-As-You-Go para apps GenAI no-M365; alineación futura anunciada hacia M365 E7 / SKU Agent 365 para agentes Foundry/Entra | Agentes creados en Copilot Studio, Microsoft Foundry o SDK P4AI | `[Verificado MS Learn]` |
| **Purview Alert Triage Agent en Insider Risk Management** | Requiere licencia de **Purview Insider Risk Management** | Requiere suscripción Pay-As-You-Go vinculada y aprovisionamiento de **Security Compute Units (SCUs)** de Microsoft Security Copilot (dotación base incluida en M365 E5) | Onboarding a Security Copilot, compartición de datos M365 activa y plug-in Microsoft Purview habilitado; renovación de guardado cada **90 días** | `[Verificado MS Learn]` |
| **Forensic Evidence (captura visual basada en eventos o continua)** | Requiere licencia base IRM | Característica **opt-in add-on**: incluye **20 GB de capacidad de prueba** para clips y compra de capacidad adicional; clips eliminados automáticamente a los **120 días** | Exclusivo **Windows 10/11 Enterprise (y Windows 365) 64-bit** con **Microsoft Purview Client** instalado, GPU integrada DirectX 11+ y doble autorización `Approvers` | `[Verificado MS Learn]` |
| **Adaptive Protection con Entra Conditional Access y DLP** | Requiere licencia IRM + Purview DLP / **Microsoft Entra ID P2** (para políticas de riesgo condicional avanzadas) | Sin medidor adicional | Propagación inicial de hasta 36 horas al activar Adaptive Protection; condición *Insider risk* configurada en CA y DLP | `[Verificado MS Learn]` |

### 2.3 Principios Rectores de Privacidad por Diseño y Alineación Zero Trust

Un programa de riesgo interno fracasa legal o culturalmente si se percibe como vigilancia indiscriminada. Microsoft Purview IRM impone salvaguardas técnicas nativas `[Verificado MS Learn]`:

- **Seudonimización activada por defecto (*Pseudonymization by default*):** La opción `Show anonymized versions of usernames` reemplaza los nombres reales y perfiles organizacionales por pseudónimos aleatorios (ej. `AnonIS8-988`) en alertas, casos y exportaciones CSV para evitar sesgos durante el triaje. **Matices arquitectónicos críticos verificados en Learn:** (1) mientras la anonimización está activa, la vista **Data risk graph** permanece deshabilitada; (2) en el panel del **Alert Triage Agent**, los nombres de usuarios en alertas priorizadas **no se anonimizan**; y (3) al exportar alertas por API hacia SIEM o escalar un caso hacia **Purview eDiscovery**, se exponen los UPN reales para preservar la integridad referencial y legal `[Verificado MS Learn]`.
- **Doble autorización obligatoria y auditoría independiente inalterable:** La captura visual de *Forensic Evidence* está apagada por defecto y exige que un administrador solicite formalmente la captura y un miembro distinto del grupo `Insider Risk Management Approvers` (Legal/RR. HH./Privacidad) la apruebe. Adicionalmente, el **Insider Risk Audit Log** registra de forma automática e indeshabilitable toda acción de administradores, analistas e investigadores durante **180 días** en un sistema de auditoría independiente del Unified Audit Log de Microsoft 365 `[Verificado MS Learn]`.
- **Alineación con los tres principios de Zero Trust:**
  - *Verify Explicitly:* Evalúa continuamente secuencias de riesgo, anomalías acumuladas de 30 días frente a grupos de pares y multiplicadores de impacto (*Risk score boosters*) antes de conceder confianza implícita a una sesión autenticada `[Verificado MS Learn]`.
  - *Use Least Privilege Access:* Segrega estrictamente 6 grupos de roles, restringe alcance regional mediante *Administrative Units*, aísla ejecutivos/proyectos críticos con *Priority User Groups* y ajusta dinámicamente privilegios mediante *Adaptive Protection* `[Verificado MS Learn]`.
  - *Assume Breach:* Correlaciona alertas internas con incidentes de **Microsoft Defender XDR** para acelerar la contención o interrupción de ataques (*attack disruption*) cuando un *insider* actúa maliciosamente o sus credenciales han sido tomadas por un adversario `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional, Conectores de Señales y Catálogo de Plantillas 2026

El motor de Purview IRM ingiere telemetría nativa y externa para evaluar indicadores globales y de política tras ocurrir un evento disparador (*triggering event*) o actividad en alcance `[Verificado MS Learn]`:

1. **Fuentes de Señales e Integración de Endpoints:**
   - **Nativas sin agente adicional:** Registros de actividad de SharePoint Online, OneDrive, Exchange Online, Microsoft Teams, Microsoft Entra ID (eliminación de cuentas, jerarquía organizacional y *Job Titles* para *Peer Groups*), Purview Information Protection (etiquetas de sensibilidad y SITs), Purview DLP, Purview Communication Compliance, **Microsoft Defender for Endpoint** y **Microsoft Defender for Cloud Apps** `[Verificado MS Learn]`.
   - **Endpoints y Navegadores:** Onboarding nativo de **Windows 10/11** y onboarding dedicado de **macOS** para detectar copia a USB, compartición en red, impresión, renombrado/archivado masivo y exfiltración desde **Microsoft Edge** (nativo) y **Google Chrome** (extensión Microsoft Purview Browser) `[Verificado MS Learn]`.
   - **Conectores Externos Críticos:** Conector **HR Data** (importación periódica CSV con `EmailAddress`, `AzureAdId`, `ResignationDate`, `TerminationDate` y eventos de evaluación/cambio de rol para usuarios riesgosos), conector **Physical Badging** (JSON correlacionado con *Priority Physical Assets*), conector de registros médicos electrónicos (**EHR**) e ingesta de indicadores personalizados de terceros (*Bring Your Own Detections*) `[Verificado MS Learn]`.

2. **Catálogo Vigente de Plantillas de Políticas (Corte Noviembre 2026) `[Verificado MS Learn]`:**
   - **Data theft by departing users:** Detecta exfiltración próxima a fechas de renuncia o terminación reportadas por el conector HR o eliminación de cuenta en Entra ID.
   - **Data leaks / Data leaks by priority users / Data leaks by risky users:** Cubren fugas accidentales o deliberadas generales, sobre miembros de *Priority User Groups* (hasta 10.000 usuarios por grupo con revisores restringidos) o usuarios con estresores reportados por HR / Communication Compliance.
   - **Risky AI usage:** Detecta prompts riesgosos (intentos de evasión, ingreso de datos confidenciales/SITs) y respuestas sensibles en **Microsoft 365 Copilot**, **Copilot Studio**, aplicaciones IA empresariales y sitios GenAI públicos.
   - **Risky Agents (preview):** Política activa por defecto en tenants licenciados para monitorear agentes construidos en **Copilot Studio**, **Microsoft Foundry** y **P4AI SDK** (detectando prompts riesgosos, generación de respuestas sensibles, acceso a archivos sensibles de SharePoint y navegación a sitios riesgosos, compartiendo el nivel de riesgo del agente con *DSPM for AI* y el Centro de administración de M365).
   - **Risky browser usage:** Detecta navegación hacia sitios de alto riesgo (malware, phishing, repositorios no autorizados de código/almacenamiento) en Edge y Chrome.
   - **Security policy violations (general, departing, priority, risky users):** Correlaciona alertas de seguridad de **Microsoft Defender for Endpoint** (desactivación de antivirus, instalación de herramientas de evasión o software no autorizado) con el contexto del usuario.
   - **Patient data misuse (preview):** Detecta accesos indebidos o masivos a historiales clínicos mediante señales del conector EHR.

### 3.2 Componentes Operativos, Motores Analíticos y Límites Críticos

| Componente / Motor | Función Operativa Principal | Ruta en Consola | Reglas Técnicas y Restricciones Verificadas (Nov 2026) | Estado |
| --- | --- | --- | --- | --- |
| **Insider Risk Analytics** | Escaneo base gratuito y sin políticas sobre hasta 10 días de logs M365, Exchange, Entra ID y HR para dimensionar riesgos y recomendar umbrales en tiempo real. | `purview.microsoft.com > Solutions > Insider Risk Management > Overview > Run scan` / `Settings > Analytics` | Resultados agregados y anónimos en hasta 48 h; `Show insights at user level` alimenta severidad de usuario hacia DLP, Comm Compliance y Defender XDR. | `[Verificado MS Learn]` |
| **Detección de Secuencias, Acumulación y Boosters** | Identifica cadenas de 2+ fases (*Collection, Exfiltration, Obfuscation, Clean-up*), exfiltración lenta a 30 días frente a *Peer Groups* de Entra ID y amplificadores de puntaje (*Boosters*). | `Insider Risk Management > Policies` y `Settings > Policy indicators` | *Inline alert customization* permite ajustar umbrales desde la alerta; exclusiones globales en `Settings > Intelligent detections`. | `[Verificado MS Learn]` |
| **Alert Triage Agent (Security Copilot in Purview)** | Clasifica automáticamente alertas en *Needs attention*, *Less Urgent* y *Not categorized* según instrucciones en lenguaje natural y resume factores de riesgo (*Summarize with Copilot*). | `purview.microsoft.com > Agents > Explore agents` y conmutador `Triage Agent` en `Alerts` | Consume SCUs; **no anonimiza nombres en su vista**; corre bajo el contexto del último usuario que guardó la configuración (**expira a los 90 días** si no se vuelve a guardar). | `[Verificado MS Learn]` |
| **Workbench de Investigación (Activity Explorer, Cases, Content Explorer)** | Línea de tiempo visual de eventos, notas de cadena de custodia, plantillas de recordatorio educativo (*Notice templates*) e inspección forense de archivos/mensajes. | `Insider Risk Management > Alerts / Cases` | `Data risk graph` requiere desactivar anonimización; `Content Explorer` restringido exclusivamente a `Investigators` (o grupo raíz). | `[Verificado MS Learn]` |
| **Adaptive Protection** | Asigna niveles dinámicos (*Elevated*, *Moderate*, *Minor*) que activan bloqueos o restricciones automáticas en Purview DLP, Entra Conditional Access y retención DLCM de 120 días. | `Insider Risk Management > Adaptive protection` + `entra.microsoft.com > Conditional Access` + `DLP > Policies` | Propagación inicial de hasta 36 horas; crea automáticamente política de etiqueta de retención de 120 días para datos borrados por usuarios *Elevated*. | `[Verificado MS Learn]` |
| **Forensic Evidence** | Captura visual de clips (*Specific activities* ej. 5 min antes / 10 min después, o *All activities*, más clips de *Enhanced Phishing Protection* de SmartScreen) con exclusión de apps/sitios privados. | `Insider Risk Management > Forensic evidence` | **Solo Windows 10/11 Enterprise y Windows 365 (64-bit, GPU integrada DirectX 11+)** con *Microsoft Purview Client* (macOS no soportado para captura visual); doble autorización obligatoria (`Approvers`); clips borrados a los **120 días**; máx. 10 clips por exportación. | `[Verificado MS Learn]` |
| **Insider Risk Audit Log Independiente** | Registro inmutable e indeshabilitable de todas las acciones ejecutadas sobre políticas, casos, alertas, ajustes, usuarios y plantillas por miembros de roles IRM. | Enlace superior derecho `Insider risk audit log` dentro de `Insider Risk Management` | **Independiente del Microsoft 365 Unified Audit Log**; retención fija de **180 días** (se purga permanentemente tras 180 días); exportable a CSV por `Auditors`. | `[Verificado MS Learn]` |
| **Integración Defender XDR, Sentinel y eDiscovery** | Sincronización bidireccional de alertas/incidentes en `security.microsoft.com`, caza KQL en Advanced Hunting, conector SIEM en Sentinel y transferencia legal a eDiscovery. | `Insider Risk Management > Settings > Data sharing` y `security.microsoft.com > Incidents & alerts` | Sincronización de estado/clasificación en <= 30 min; tablas KQL `AlertInfo`, `AlertEvidence`, `DataSecurityBehaviors` y `DataSecurityEvents`; se recomienda migrar de O365 Management API a **Microsoft Graph Security API**. | `[Verificado MS Learn]` |

### 3.3 Integraciones Cruzadas del Ecosistema y Consideraciones Operativas 2026

1. **Correlación Bidireccional con Microsoft Defender XDR (`security.microsoft.com`):** Al activar `Share user risk details with other security solutions` en `Settings > Data sharing`, las alertas de IRM se agrupan en incidentes unificados junto con alertas de Defender for Endpoint, Defender for Identity, Entra ID Protection y Purview DLP, enriqueciendo la página de entidad del usuario con su nivel de riesgo interno para acelerar decisiones de contención o interrupción automática de ataques (*attack disruption*). Los cambios de estado se sincronizan en ambas consolas en menos de 30 minutos (`New / In progress` ↔ `Needs review`; `True positive` ↔ `Confirmed`; `False / Benign positive` ↔ `Dismissed`). *Limitación actual documentada en Learn:* eventos de exfiltración por email, *Risky AI usage* y apps cloud de terceros aún no se proyectan completos en esta vista XDR `[Verificado MS Learn]`.
2. **Integración con Microsoft Sentinel y Precaución en Automatización SOAR:** Se recomienda ingerir alertas mediante el conector oficial **Microsoft Purview Insider Risk Management — Microsoft Sentinel data connector** o **Microsoft Graph Security API** (`SecurityIncident.ReadWrite.All`, `SecurityAlert.ReadWrite.All`, `ThreatHunting.Read.All`). Microsoft Learn advierte que si se ejecutan reglas de automatización en Sentinel sobre incidentes sincronizados desde XDR, los incidentes puros de IRM pueden carecer de payload de alerta anidado y causar fallas en playbooks si no se controla esa condición o se ajusta *Data sharing* `[Verificado MS Learn]`.
3. **Priority User Groups, Information Barriers y Escalamiento a eDiscovery (Premium):** Los *Priority User Groups* permiten aplicar umbrales más sensibles y restringir quién puede ver alertas/casos de miembros VIP o de fusiones y adquisiciones (alineándose con segmentos de **Information Barriers** para evitar conflictos de interés). Cuando un caso confirma dolo o litigio, `Escalate for investigation` transfiere custodios, alertas y notas directamente a un caso de **Purview eDiscovery** para preservación legal (*Hold*) y producción forense `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Gobernanza Multidisciplinaria (Comité Legal + RR. HH. + Privacidad + SecOps) y Segregación Estricta

Operar Insider Risk Management sobre empleados y contratistas exige un **Estatuto de Gobernanza Tripartito** firmado por CISO, Asesoría Legal, Recursos Humanos y el Oficial de Protección de Datos (DPO) —incluyendo consulta a representación sindical o *Works Councils* en jurisdicciones aplicables— antes de pasar políticas a producción `[Decisión / Propuesta Editorial]`. Técnicamente, Microsoft Purview provee **seis grupos de roles nativos** cuya separación impide que quien diseña políticas vea contenido privado o que quien investiga apruebe sus propias capturas forenses; la propagación de cambios en grupos de roles toma hasta **30 minutos** `[Verificado MS Learn]`.

Cuando se aplican **Administrative Units** para restringir analistas o investigadores por país o subsidiaria, los usuarios monitoreados deben agregarse **directamente** a la unidad administrativa (no mediante grupos anidados, cuyas alertas solo verían administradores irrestrictos). Además, los administradores acotados (*Scoped*) no pueden visualizar alertas de `Risky Agents (preview)`, `Data risk graph`, capturas de `Forensic Evidence` ni configurar `Adaptive Protection` o `Priority user groups` `[Verificado MS Learn]`.

### 4.2 Matriz RBAC Oficial de Insider Risk Management y Ecosistema Integrado

| Grupo de Roles / Rol Oficial | Plano RBAC | Permisos Clave Verificados | Estrategia PIM / JIT y Alcance | Responsabilidad Operativa y Segregación (SoD) | Estado |
| --- | --- | --- | --- | --- | --- |
| **Insider Risk Management Admins** | Microsoft Purview RBAC | Configurar políticas, indicadores, conectores, *Analytics*, *Adaptive Protection*, *Priority user groups* y crear solicitudes de *Forensic Evidence*. **Sin acceso a alertas, casos ni Content Explorer.** | Elegible en Entra ID PIM (máx. 4 h JIT con MFA resistente a phishing y ticket aprobado) `[Decisión / Propuesta Editorial]`. | Ingeniería de plataforma y calibración de políticas sin visibilidad sobre investigaciones individuales `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management Analysts** | Microsoft Purview RBAC (+ `Security Reader/Operator` en XDR si opera en Defender) | Acceso e investigación de alertas y casos, *Activity Explorer*, *Analytics insights*, *Notice templates* y pestaña de usuarios en *Adaptive Protection*. **Sin acceso a Content Explorer ni clips forenses.** | Asignación activa (o turno JIT de 8 h) acotada por *Administrative Units* regionales cuando la ley local lo exija `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`. | Triaje Nivel 1 bajo seudonimización, descarte justificado de falsos positivos y escalamiento a caso `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management Investigators** | Microsoft Purview RBAC (+ `Security Operator` para caza KQL en XDR) | Investigación profunda de alertas y casos, acceso exclusivo a **Content Explorer** y visualización de capturas de **Forensic Evidence**, y escalamiento a *eDiscovery*. **Sin permiso para editar políticas.** | Estricto JIT en Entra ID PIM (máx. 4 h) vinculado a ID de caso confirmado `[Decisión / Propuesta Editorial]`. | Investigación Nivel 2/3 para validar sensibilidad real del archivo/mensaje e intención antes de involucrar a RR. HH. o Legal `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management Approvers** | Microsoft Purview RBAC | Único permiso operativo: **aprobar o rechazar solicitudes de captura de Forensic Evidence** para usuarios específicos (sin acceso a alertas, casos, políticas ni clips). | Asignado exclusivamente a representantes designados de **Asesoría Legal, Privacidad (DPO) o Relaciones Laborales (RR. HH.)** fuera de la cadena de mando del SOC `[Verificado MS Learn]`. | Control independiente de doble llave (*dual authorization*) obligatorio antes de grabar actividad visual en endpoints `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management Auditors** | Microsoft Purview RBAC | Único permiso operativo: **visualizar y exportar a CSV el Insider Risk Audit Log** independiente (sin acceso a políticas, alertas ni contenido). | Asignado a Auditoría Interna y Oficialía de Privacidad (DPO) `[Verificado MS Learn]`. | Supervisión independiente anti-abuso ("vigilar a quienes vigilan") exportando mensualmente el log antes de su purga a los 180 días `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Conditional Access Administrator + DLP Compliance Management** | Microsoft Entra ID + Microsoft Purview RBAC | Crear y administrar políticas de Acceso Condicional y políticas DLP que consumen la condición dinámica *Insider risk level* de *Adaptive Protection*. | Elegible JIT en Entra ID PIM (máx. 2 h con cambio aprobado) `[Decisión / Propuesta Editorial]`. | Conectar los niveles *Elevated / Moderate / Minor* con acciones automáticas de bloqueo o restricción de sesión/exfiltración `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Insider Risk Management** (Role Group raíz comodín) | Microsoft Purview RBAC | Concentra todos los permisos anteriores (políticas, casos, Content Explorer, aprobación forense y auditoría). | **Uso operativo diario desaconsejado**; restringido a 1-2 cuentas de resguardo bajo PIM con aprobación dual para evitar el escenario *zero administrator* advertido por Learn `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`. | Continuidad administrativa de emergencia sin romper la segregación ordinaria de funciones `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Verificación Diaria de Salud de Conectores de Señales (HR Data, Physical Badging y Onboarding de Dispositivos)
- **Objetivo:** Asegurar que un silencio de alertas no oculte fallos de importación en los conectores críticos de Recursos Humanos (renuncias/despidos), acceso físico o telemetría de endpoints Windows/macOS `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Data connectors > My connectors` y `Settings > Device onboarding` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` (o monitoreo automatizado de plataforma).
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `Defense Evasion (T1562 — Telemetry Continuity)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar en `My connectors` que el conector **HR** aparezca en estado `Connected` y que `Last import` sea inferior a 24 horas, validando ausencia de errores de formato en `EmailAddress`, `AzureAdId`, `ResignationDate` y `TerminationDate` `[Verificado MS Learn]`.
  2. Si se emplea **Physical badging**, comprobar ausencia de errores de parseo JSON y verificar que el indicador correspondiente siga activo en `Settings > Insider Risk Management > Policy indicators` `[Verificado MS Learn]`.
  3. Revisar el reporte de salud de dispositivos en `Device onboarding` confirmando cobertura activa de endpoints Windows 10/11, macOS y extensión de Chrome `[Verificado MS Learn]`.
  4. Abrir ticket prioritario de remediación ante cualquier desfase de importación superior a 24 horas.
- **Evidencia Auditable:** Registro diario de estado `Connected` y marca temporal de última importación exitosa en conectores HR/Badging `[Verificado MS Learn]`.

### D-02: Triaje Priorizado de Alertas de Severidad Alta y Vista del Purview Alert Triage Agent
- **Objetivo:** Clasificar oportunamente las alertas `Needs review` de alta severidad y las alertas destacadas como `Needs attention` por el agente de Security Copilot manteniendo objetividad bajo seudonimización `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Alerts` (vistas `Standard` y `Triage Agent`) `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Analysts` (Nivel 1).
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.AE-02` / `Exfiltration (TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola de alertas por `Status: Needs review` y `Severity: High`, conmutando también a la vista `Triage Agent` para atender primero la categoría `Needs attention` `[Verificado MS Learn]`.
  2. Tener presente el control de privacidad documentado por Microsoft Learn: en el tablero del `Triage Agent` los nombres de usuario **no aparecen anonimizados** aun cuando `Show anonymized versions of usernames` esté habilitado globalmente, por lo que el acceso al agente debe restringirse a analistas autorizados `[Verificado MS Learn]`.
  3. Utilizar `Summarize with Copilot` para obtener contexto inmediato de evento disparador, factores principales de riesgo y secuencias detectadas `[Verificado MS Learn]`.
  4. Documentar decisión inicial dentro del SLA diario (<= 4 h para *High*): escalar a caso (`Confirm alerts & create case`) o descartar (`Dismiss`) con justificación obligatoria `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Cola de alertas *High* sin pendientes fuera de SLA y notas obligatorias de clasificación registradas `[Decisión / Propuesta Editorial]`.

### D-03: Análisis Contextual de Secuencias y Exfiltración Acumulada en Activity Explorer
- **Objetivo:** Reconstruir la secuencia cronológica de eventos (*Collection → Exfiltration → Obfuscation → Clean-up*) antes de escalar a investigación invasiva de contenido `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Alerts > [Seleccionar Alerta] > Activity explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Analysts` (L1) / `Investigators` (L2).
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.AE-03` / `Collection & Exfiltration (TA0009 / TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar la línea de tiempo y el gráfico de burbujas en `Activity explorer` identificando correlación temporal entre descargas masivas de SharePoint, renombrado/compresión de archivos, copia a USB, impresión o subida a nubes personales `[Verificado MS Learn]`.
  2. Evaluar indicadores de **Cumulative exfiltration detection** (desviación acumulada de 30 días respecto a su *Peer Group* en Entra ID) y multiplicadores activos (*Risk score boosters* como pertenencia a *Priority user group* o historial previo) `[Verificado MS Learn]`.
  3. Revisar metadatos de ruta y extensión de archivos para descartar ruido técnico benigno (ej. sincronizaciones de desarrollo autorizadas) sin abrir el contenido del documento `[Verificado MS Learn]`.
- **Evidencia Auditable:** Notas estructuradas de análisis de secuencia adjuntas al registro de la alerta o caso `[Verificado MS Learn]`.

### D-04: Monitoreo Diario de Alertas de Risky AI Usage y Risky Agents (Preview)
- **Objetivo:** Detectar tempranamente exfiltración de datos confidenciales hacia prompts de IA generativa, intentos de *jailbreak* o comportamientos inseguros de agentes empresariales `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Alerts` (filtro por políticas *Risky AI usage* y *Risky Agents*) `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Analysts` (con perfil irrestricto para alertas de agentes) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-03` / `Exfiltration Over Web Service (T1567)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar alertas generadas por la plantilla **Risky AI usage** (interacciones riesgosas en Microsoft 365 Copilot, Copilot Studio y sitios GenAI externos detectados en Edge/Chrome) y por la política predeterminada **Risky Agents (preview)** (agentes en Copilot Studio, Microsoft Foundry y P4AI SDK) `[Verificado MS Learn]`.
  2. Considerar dos reglas técnicas críticas de `Risky Agents`: (a) los analistas acotados por *Administrative Units* **no pueden ver alertas de agentes**, por lo que esta revisión debe ejecutarla un analista global; y (b) cuando interactúan usuarios invitados (*guest users*), solo se muestran los indicadores de información sensible detectada y no el texto completo del prompt/respuesta `[Verificado MS Learn]`.
  3. Si un agente autónomo accede a datos sensibles fuera de su propósito o sitios riesgosos, coordinar contención inmediata con el propietario del agente en M365 Admin Center / *DSPM for AI* (`AH-05`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro diario de triaje de alertas de usuarios IA y agentes con acciones de mitigación asociadas `[Verificado MS Learn]`.

### D-05: Correlación Diaria en Cola Unificada de Incidentes de Microsoft Defender XDR
- **Objetivo:** Cruzar alertas de riesgo interno con amenazas externas activas (compromiso de credenciales, malware o movimiento lateral) en la consola unificada del SOC `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Incidents & alerts > Incidents` (filtro `Service source: Microsoft Purview Insider Risk Management`) `[Verificado MS Learn]`.
- **Rol Responsable:** Analista SOC L2 (miembro dual de `Security Operator` + `Insider Risk Management Analysts` / `Investigators`) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.AE-02` / `Valid Accounts & Exfiltration (T1078 / TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar en `security.microsoft.com` incidentes y alertas con origen `Microsoft Purview Insider Risk Management` correlacionados automáticamente con Purview DLP, Microsoft Entra ID y Defender for Endpoint `[Verificado MS Learn]`.
  2. Inspeccionar la página de entidad del usuario (*User entity page*) para validar su resumen de riesgo interno y descartar que la exfiltración provenga de una sesión secuestrada (*Account Takeover*) que requiera contención XDR inmediata `[Verificado MS Learn]`.
  3. Clasificar la alerta asegurando consistencia con la tabla oficial de sincronización bidireccional (<= 30 min): `True positive` en Defender equivale a `Confirmed` en Purview; `False / Benign positive` equivale a `Dismissed` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Incidentes unificados en Defender XDR actualizados y sincronizados con Purview IRM `[Verificado MS Learn]`.

### D-06: Supervisión Operativa de Usuarios en Nivel Elevated bajo Adaptive Protection
- **Objetivo:** Auditar los usuarios promovidos dinámicamente al nivel de riesgo *Elevated* verificando la aplicación efectiva de controles restrictivos en DLP, Acceso Condicional y preservación DLCM de 120 días `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Adaptive protection > Insider risk levels` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Analysts` / `Investigators` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.AA-05` / `Exfiltration Prevention (TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar la pestaña de usuarios asignados actualmente a los niveles `Elevated`, `Moderate` y `Minor` en `Adaptive protection` `[Verificado MS Learn]`.
  2. Confirmar que para todo usuario recién ingresado a `Elevated` estén operando sin errores de usuario legítimo las políticas condicionadas en **Purview DLP** (bloqueo de compartición externa/USB) y **Microsoft Entra Conditional Access**, así como la preservación automática de 120 días de datos eliminados `[Verificado MS Learn]`.
  3. Si un analista descarta como falso positivo la alerta que originó el nivel *Elevated*, verificar el restablecimiento del nivel de riesgo para no bloquear indebidamente la operación del empleado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora diaria de usuarios en nivel *Elevated* y verificación de bloqueos preventivos activos `[Verificado MS Learn]`.

### D-07: Verificación Diaria de Privacidad, Seudonimización e Insider Risk Audit Log
- **Objetivo:** Confirmar que la seudonimización global permanezca activa según la política aprobada y auditar cualquier acceso excepcional a contenido o cambios de privacidad `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Insider Risk Management > Privacy` y enlace `Insider risk audit log` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Auditors` (Auditoría Interna / Privacidad) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.PO-02` / `Internal Surveillance Abuse Prevention` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Abrir el **Insider risk audit log** (sistema independiente con retención de 180 días) y filtrar las últimas 24 horas por categoría `Settings`, `Cases` y `Users` `[Verificado MS Learn]`.
  2. Verificar que nadie haya deshabilitado `Show anonymized versions of usernames` sin acta formal firmada por Legal y Privacidad `[Verificado MS Learn]`.
  3. Auditar que todo acceso a casos o visualización de contenido corresponda a investigadores con caso formalmente asignado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Revisión diaria registrada del `Insider risk audit log` sin violaciones de protocolo de privacidad `[Verificado MS Learn]`.

### D-08: Procesamiento de Solicitudes Pendientes de Doble Autorización en Forensic Evidence
- **Objetivo:** Garantizar que toda solicitud urgente de captura visual forense sea evaluada con rigor legal y laboral por un aprobador independiente sin demorar investigaciones críticas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Forensic evidence > Requests` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Approvers` (Legal / DPO / Relaciones Laborales) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RR-02` / `Forensic Collection Governance` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar solicitudes pendientes emitidas por miembros de `Insider Risk Management Admins` para incluir usuarios específicos en políticas de captura visual (*Specific activities* o *All activities*) `[Verificado MS Learn]`.
  2. Validar proporcionalidad legal, ventana temporal de grabación, exclusión de aplicaciones/sitios privados (banca, salud, correo personal) y jurisdicción laboral del empleado antes de aprobar o rechazar `[Verificado MS Learn]`.
  3. Confirmar que toda decisión quede asentada de inmediato en el registro de auditoría independiente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de solicitudes aprobadas/rechazadas por `Approvers` con justificación legal vinculada a caso `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Gestión de Ciclo de Vida de Casos Activos, Cadena de Custodia e Inspección en Content Explorer
- **Objetivo:** Profundizar las investigaciones confirmadas documentando hallazgos objetivos en `Case notes` y validando en `Content explorer` si los archivos exfiltrados contienen información verdaderamente sensible `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Cases` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Investigators` (Nivel 2/3) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.AN-03` / `Exfiltration & Insider Threat Investigation` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar todos los casos abiertos ordenados por antigüedad y severidad, registrando cada avance probatorio en `Case notes` para sostener cadena de custodia `[Verificado MS Learn]`.
  2. Inspeccionar en `Content explorer` (y pestaña `Forensic evidence` cuando exista captura aprobada, recordando que los clips caducan a los **120 días** y se exportan de a máximo 10 clips por lote) la sensibilidad real de los activos involucrados `[Verificado MS Learn]`.
  3. Determinar la vía de resolución: descarte documentado, envío de recordatorio educativo mediante **Notice templates** (para errores inadvertidos, dejando rastro auditable ante reincidencia) o escalamiento formal a Legal/RR. HH. `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora actualizada en `Case notes`, registros de envío de `Notice templates` y tiempos de ciclo controlados `[Verificado MS Learn]`.

### S-02: Revisión de Salud de Políticas (Policy Health Check) y Advertencias No Resueltas
- **Objetivo:** Corregir advertencias técnicas (`Warnings`) y recomendaciones de configuración en políticas activas que degraden la detección `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar la columna `Status` de cada política activa identificando estados `Warnings` o `Recommendations` (complementado por el correo semanal automático de *Unresolved warnings* en `Admin notifications`) `[Verificado MS Learn]`.
  2. Atender fallos típicos: conector HR sin cargas recientes en políticas de usuarios salientes, exceso de usuarios asignados frente a límites de la plantilla o indicadores desactivados globalmente `[Verificado MS Learn]`.
  3. Validar que la política predeterminada `Risky Agents (preview)` y las políticas `Risky AI usage` mantengan activos sus indicadores correspondientes `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/exportación semanal del tablero `Policies` con 100% de políticas productivas en estado `Healthy` `[Verificado MS Learn]`.

### S-03: Calibración de Umbrales (Tuning), Variantes de Indicadores y Grupos de Detección
- **Objetivo:** Reducir falsos positivos y fatiga del SOC ajustando umbrales con base en recomendaciones en tiempo real de *Insider Risk Analytics* y grupos de detección `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Settings > Policy indicators / Intelligent detections` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` (en coordinación con métricas de L1/L2) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.AE-06` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Analizar las alertas descartadas como benignas en la semana e identificar dominios SaaS corporativos legítimos, rutas de archivos temporales o scripts internos ruidosos.
  2. Utilizar **Inline alert customization** o recomendaciones en tiempo real de **Analytics** para ajustar umbrales de volumen diario sin apagar el indicador global `[Verificado MS Learn]`.
  3. Configurar **Detection groups** y variantes de indicadores (*Indicator variants*) para aplicar umbrales diferenciados por rol técnico (ej. desarrolladores o marketing vs. finanzas) y actualizar exclusiones globales en `Intelligent detections` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de cambios de calibración y evolución de tasa de verdaderos positivos `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### S-04: Caza Proactiva Semanal (Threat Hunting KQL) en Microsoft Defender Portal sobre Eventos de Datos
- **Objetivo:** Detectar patrones sutiles de acopio o fuga que aún no hayan superado el puntaje de alerta correlacionando tablas de seguridad de datos con telemetría de endpoint e identidad `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** Threat Hunter / `Insider Risk Management Investigator` + `Security Operator` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.AE-03` / `Collection & Exfiltration (TA0009 / TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar consultas KQL sobre las cuatro tablas integradas en Advanced Hunting: `DataSecurityEvents`, `DataSecurityBehaviors`, `AlertInfo` y `AlertEvidence` `[Verificado MS Learn]`.
  2. Cruzar subidas inusuales a almacenamiento web personal o copias USB en `DataSecurityEvents` contra inicios de sesión riesgosos (`AADSignInEventsBeta`) o ejecución de herramientas de archivo/cifrado en `DeviceProcessEvents`.
  3. Si se descubre una campaña coordinada no cubierta por políticas actuales, abrir investigación formal y proponer ajuste de indicadores a `IRM Admins`.
- **Evidencia Auditable:** Consultas de caza semanal ejecutadas y documentadas con hallazgos o cierre negativo `[Decisión / Propuesta Editorial]`.

### S-05: Sincronización de Priority User Groups y Alineación con Information Barriers
- **Objetivo:** Mantener actualizada la membresía de ejecutivos, administradores críticos, equipos de M&A e investigadores de I+D en *Priority User Groups* preservando confidencialidad estricta `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Insider Risk Management > Priority user groups` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` (irrestricto; no permitido a administradores acotados por AU) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.RA-05` / `High-Impact Insider Mitigation` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Conciliar altas/bajas de proyectos confidenciales (M&A, lanzamientos estratégicos, cuentas privilegiadas Tier-0) actualizando los *Priority user groups* (hasta **10.000 miembros** por grupo; carga manual o CSV) `[Verificado MS Learn]`.
  2. Auditar la lista explícita `Choose who can view this group` confirmando que solo los investigadores designados (y sin conflicto de interés frente a segmentos de **Information Barriers**) puedan ver alertas y casos de dicho grupo `[Verificado MS Learn]`.
  3. Recordar no eliminar nunca un *Priority user group* asignado a una política activa sin reemplazarlo antes, pues deja la política inactiva sin generar alertas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de membresía y permisos de visualización por cada *Priority user group* `[Verificado MS Learn]`.

### S-06: Verificación de Flujos Automatizados SOAR (Power Automate y Conector Microsoft Sentinel)
- **Objetivo:** Comprobar la ejecución saludable de flujos de orquestación con RR. HH./managers y del conector de alertas hacia Microsoft Sentinel `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Insider Risk Management > Power Automate` y `security.microsoft.com > Microsoft Sentinel > Data connectors` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero SOAR / `Insider Risk Management Admins` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.CO-02` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar el historial de ejecuciones de los flujos recomendados de **Power Automate** (solicitud de contexto a RR. HH./manager y registro automático de respuesta en `Case notes`, incluidos sin licencia adicional de Power Automate para funciones estándar) `[Verificado MS Learn]`.
  2. Verificar la ingesta continua del conector **Microsoft Purview Insider Risk Management** en Sentinel y el uso de **Microsoft Graph Security API** `[Verificado MS Learn]`.
  3. Validar que ninguna regla de automatización en Sentinel falle por incidentes IRM sincronizados desde Defender XDR sin payload de alerta anidado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Bitácora semanal sin ejecuciones fallidas en flujos Power Automate y conector Sentinel `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Exportación y Auditoría Independiente del Insider Risk Audit Log (Antes del Límite de 180 Días)
- **Objetivo:** Ejercer supervisión independiente sobre todas las acciones de administradores, analistas, investigadores y aprobadores, preservando evidencia histórica antes del borrado automático a los 180 días `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Insider risk audit log > Export` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Auditors` (Auditoría Interna y DPO) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OV-03` / `Insider Abuse Auditability` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Acceder al **Insider risk audit log** independiente y exportar a CSV la totalidad de eventos del mes cerrado (`Policies`, `Cases`, `Alerts`, `Settings`, `Users`, `Notice templates`) `[Verificado MS Learn]`.
  2. Auditar que no existan búsquedas o aperturas selectivas de casos sobre ejecutivos o pares fuera de asignación formal, ni cambios temporales encubiertos de la opción de anonimización `[Verificado MS Learn]`.
  3. Calcular hash SHA-256 del CSV exportado y custodiarlo en el archivo inmutable de Auditoría Interna (superando así la purga automática nativa a los **180 días**) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Archivo mensual CSV del `Insider risk audit log` + acta de revisión firmada por `Auditors` `[Verificado MS Learn]`.

### M-02: Evaluación Mensual de Insider Risk Analytics y Cobertura de Plantillas (Incluyendo IA y Agentes)
- **Objetivo:** Contrastar los hallazgos agregados de *Insider Risk Analytics* (10 días móviles) frente a las políticas activas para cerrar brechas de cobertura emergentes `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Reports > Analytics` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` + Arquitecto de Seguridad de Datos `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.RA-01` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Analizar los informes consolidados y anónimos de `Reports > Analytics` evaluando porcentajes de actividad exfiltratoria en SharePoint, Exchange externo, cuentas eliminadas de Entra ID, usuarios salientes de HR e interacciones con IA `[Verificado MS Learn]`.
  2. Identificar vectores activos en el tenant que aún carezcan de política dedicada (por ejemplo, activar *Data leaks by risky users*, *Risky browser usage* o afinar *Risky Agents*) `[Verificado MS Learn]`.
  3. Presentar recomendaciones de evolución al Comité de Gobernanza de Riesgo Interno.
- **Evidencia Auditable:** Informe mensual comparativo de *Analytics Insights* vs. matriz de políticas desplegadas `[Verificado MS Learn]`.

### M-03: Revisión de Efectividad de Adaptive Protection (Purview DLP + Entra Conditional Access + DLCM)
- **Objetivo:** Medir cuántas exfiltraciones o accesos riesgosos fueron bloqueados proactivamente por *Adaptive Protection* y calibrar los criterios de transición entre *Minor*, *Moderate* y *Elevated* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `Insider Risk Management > Adaptive protection`, `DLP > Activity explorer` y `entra.microsoft.com > Sign-in logs` `[Verificado MS Learn]`.
- **Rol Responsable:** Arquitecto Zero Trust + `IRM Admins` + `Conditional Access Admin` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-02` / `Exfiltration & Access Mitigation` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Cuantificar usuarios asignados durante el mes a cada nivel de riesgo (*Elevated*, *Moderate*, *Minor*) y revisar las acciones preventivas disparadas automáticamente en reglas DLP y políticas de Acceso Condicional `[Verificado MS Learn]`.
  2. Verificar la creación y operación efectiva de la política automática de etiqueta de retención de **120 días** sobre datos eliminados por usuarios en nivel *Elevated* `[Verificado MS Learn]`.
  3. Ajustar condiciones si algún perfil operativo legítimo experimentó fricción innecesaria en nivel *Moderate*.
- **Evidencia Auditable:** Reporte mensual de efectividad preventiva de *Adaptive Protection* y métricas de incidentes evitados `[Decisión / Propuesta Editorial]`.

### M-04: Renovación Preventiva del Contexto del Triage Agent (Ventana de 90 Días) y Control de SCUs
- **Objetivo:** Evitar la detención silenciosa del *Purview Alert Triage Agent* (cuya autenticación caduca a los **90 días** del último guardado) y optimizar el consumo de *Security Compute Units (SCUs)* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Agents > Explore agents > Insider Risk Management Triage Agent` y herramienta de monitoreo de uso en Security Copilot `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` + `Security Copilot Contributor` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `Agentic Operations Continuity` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar en `Usage monitoring` el consumo mensual de SCUs del agente frente a la dotación incluida en M365 E5 y presupuesto Pay-As-You-Go `[Verificado MS Learn]`.
  2. Refinar las instrucciones personalizadas en lenguaje natural (*Custom instructions*) con base en el feedback mensual de los analistas L1 `[Verificado MS Learn]`.
  3. Re-guardar explícitamente la configuración del agente al menos cada 60 días (renovando de forma proactiva el token de contexto de seguridad antes del vencimiento estricto de **90 días** documentado en Learn) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro mensual de consumo SCU y marca de tiempo de renovación preventiva (< 60 días) del contexto del agente `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### M-05: Auditoría de Grupos de Roles, Administrative Units, Capacidad Forensic Evidence y Reporte al Comité
- **Objetivo:** Auditar mínimo privilegio en los 6 grupos de roles, validar alcance de *Administrative Units*, controlar cuota de almacenamiento de clips forenses y reportar KPIs al Comité Tripartito `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and groups`, `Insider Risk Management > Reports` y `Forensic evidence` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager + DPO + Legal + RR. HH.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OV-01` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar miembros de los 6 grupos de roles verificando que al menos 1 administrador de respaldo permanezca en `Insider Risk Management Admins` (evitando *zero administrator*), que `Approvers` pertenezcan exclusivamente a Legal/RR. HH./Privacidad y que los usuarios en *Administrative Units* estén asignados directamente (no en grupos anidados) `[Verificado MS Learn]`.
  2. Revisar el consumo de almacenamiento de clips en `Forensic evidence` (20 GB de prueba + capacidad contratada) y la expiración automática a los 120 días `[Verificado MS Learn]`.
  3. Exportar datos agregados CSV (preservando anonimización) de `Reports` para presentar el tablero ejecutivo mensual al CISO y al Comité de Riesgo Interno `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual del Comité Tripartito, auditoría RBAC/AU y paquete CSV anonimizado de métricas `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Evaluación de Impacto de Privacidad (DPIA) y Cumplimiento Laboral del Programa IRM
- **Objetivo:** Validar con Privacidad, Legal y Relaciones Laborales que todas las políticas, *Collection Policies*, exclusiones de captura forense y alcances regionales cumplan estrictamente la legislación vigente `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Insider Risk Management` y `Settings > Collection policies` `[Verificado MS Learn]`.
- **Rol Responsable:** DPO + Asesoría Legal Laboral + `IRM Admins`.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OC-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar la configuración de privacidad global, exclusiones de sitios/aplicaciones personales en *Forensic Evidence* y alcances geográficos de *Collection Policies* `[Verificado MS Learn]`.
  2. Revisar las plantillas de notificación educativa (*Notice templates*) asegurando tono constructivo y referencias vigentes a políticas internas de seguridad y uso aceptable de IA `[Verificado MS Learn]`.
  3. Actualizar la Evaluación de Impacto en la Protección de Datos (DPIA) cuando se incorporen nuevos indicadores (ej. agentes IA o conectores físicos) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** DPIA trimestral revisada y firmada por DPO, Legal y RR. HH. `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Prueba End-to-End de Contención Dinámica (Adaptive Protection) y Sincronización XDR/Sentinel
- **Objetivo:** Verificar en entorno controlado con cuentas de prueba que la elevación de riesgo dispare correctamente los bloqueos en DLP y Entra Conditional Access, la preservación de 120 días y la correlación en Defender XDR `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `purview.microsoft.com`, `entra.microsoft.com` y `security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Arquitecto SecOps + Ingeniería Purview y Entra ID.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.AA-05` / `Exfiltration & Access Control Validation` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar secuencia simulada de exfiltración con una identidad sintética dedicada hasta alcanzar nivel `Elevated` en *Adaptive Protection* `[Verificado MS Learn]`.
  2. Comprobar bloqueo efectivo al intentar copiar un archivo sensible a USB/nube personal (DLP), restricción de acceso a app crítica (Entra Conditional Access) y retención automática de 120 días al borrar un documento `[Verificado MS Learn]`.
  3. Verificar aparición del incidente en `security.microsoft.com` y sincronización bidireccional de cierre en menos de 30 minutos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Protocolo trimestral de pruebas técnicas firmadas con capturas y trazas KQL `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Revisión de Lecciones Aprendidas de Casos Cerrados (Práctica SEI/CERT) y Efectividad por Plantilla
- **Objetivo:** Analizar tendencias sistémicas de los últimos 6 meses para transformar incidentes recurrentes en controles preventivos estructurales y mejoras de cultura organizacional `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Reports` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + Líder de Riesgo Interno + RR. HH. + Formación y Concientización.
- **Mapeo NIST CSF 2.0 / MITRE:** `RC.IM-01` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Analizar casos confirmados vs. descartados por departamento, plantilla (*Departing users*, *Priority users*, *Risky AI usage*, *Security policy violations*) y tasa de reincidencia posterior al envío de *Notice templates* `[Verificado MS Learn]`.
  2. Identificar fricciones de negocio que empujen a empleados a usar canales no autorizados o IA sombra (*Shadow AI*) y corregir procesos base.
  3. Retirar indicadores sin valor analítico y recalibrar *Peer Groups* y *Risk score boosters* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral ejecutivo de efectividad, reducción de reincidencia y recalibración de políticas `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Recertificación del Estatuto de Riesgo Interno y Simulacro Conjunto SecOps + Legal + RR. HH.
- **Objetivo:** Recertificar anualmente el marco ético-legal del programa y ejercitar un caso complejo de robo de propiedad intelectual por usuario prioritario saliente hasta su judicialización simulada `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `purview.microsoft.com` (IRM, Forensic Evidence, eDiscovery) y `security.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO, General Counsel, CHRO (Dirección de RR. HH.), DPO y SOC Manager.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RM-01` / `Insider IP Theft Full Lifecycle` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Recertificar el Estatuto de Gobernanza de Riesgo Interno, los acuerdos con representación laboral cuando apliquen y la matriz RACI de los 6 grupos de roles `[Decisión / Propuesta Editorial]`.
  2. Ejecutar simulacro anual completo: señal de renuncia en conector HR → detección de secuencia de acopio y subida a IA/nube personal → contención automática *Adaptive Protection* → solicitud y doble autorización `Approvers` de *Forensic Evidence* → escalamiento encubierto a *Purview eDiscovery* `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Documentar brechas de coordinación o tiempos legales y actualizar playbooks operativos.
- **Evidencia Auditable:** Estatuto anual firmado y reporte ejecutivo de evaluación del simulacro inter-áreas `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Investigación Urgente de Robo de Propiedad Intelectual por Usuario Saliente o VIP
- **Disparador:** Alerta de alta severidad en *Data theft by departing users* o *Data leaks by priority users* con secuencia confirmada de descarga masiva de repositorios críticos y exfiltración hacia USB, correo personal o nube externa `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Cases` y `Adaptive protection` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Investigators` + Comité de Crisis (Legal / RR. HH. / CISO) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MA-02` / `Exfiltration Over Alternative Protocol / USB / Web (TA0010)` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Confirmar la alerta creando un **Caso** formal y verificar que el usuario haya pasado al nivel **Elevated** en *Adaptive Protection* (activando bloqueo inmediato en DLP, restricción en Entra Conditional Access y preservación automática de 120 días de elementos borrados); en caso necesario, contener sesión/dispositivo coordinadamente con el SOC `[Verificado MS Learn]`.
  2. El `Investigator` examina `Activity explorer` y `Content explorer` para inventariar exactamente qué activos de propiedad intelectual o secretos comerciales fueron accedidos/copiados `[Verificado MS Learn]`.
  3. Documentar cada hallazgo con marca horaria en `Case notes` **sin enviar ninguna notificación (*Notice*) al usuario investigado** para no alertarlo ni propiciar destrucción de pruebas externas `[Verificado MS Learn]`.
  4. Convocar mesa reservada con Legal y Relaciones Laborales para decidir revocación anticipada de accesos en ventana de preaviso y ejecutar escalamiento formal a eDiscovery (`AH-03`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Expediente completo del caso en IRM, inventario de archivos comprometidos y acta reservada con Legal/RR. HH. `[Verificado MS Learn]`.

### AH-02: Activación Excepcional de Captura Visual con Forensic Evidence bajo Doble Autorización
- **Disparador:** Investigación activa de alto impacto donde los logs de actividad no bastan para demostrar exfiltración visual o evasión sofisticada en un equipo Windows corporativo `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Forensic evidence` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Admins` (solicitud) + `Insider Risk Management Approvers` (autorización independiente) + `Investigators` (revisión) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.AN-03` / `Automated Collection & Screen Capture Evidence` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Verificar prerrequisitos técnicos del objetivo: equipo **Windows 10/11 Enterprise o Windows 365 (64-bit, GPU integrada DirectX 11+)** incorporado a Purview y con **Microsoft Purview Client** instalado (recordando que macOS no soporta captura visual de *Forensic Evidence*) `[Verificado MS Learn]`.
  2. El `IRM Admin` crea la solicitud formal de captura para el usuario específico eligiendo preferentemente modo **Specific activities** (ej. 5 min antes y 10 min después del indicador de riesgo) y configurando exclusiones estrictas de sitios/apps privadas `[Verificado MS Learn]`.
  3. Un miembro independiente de `Insider Risk Management Approvers` (Legal / DPO / RR. HH.) revisa la base legal y aprueba explícitamente la solicitud (doble autorización obligatoria) `[Verificado MS Learn]`.
  4. El `Investigator` revisa los clips generados en la pestaña `Forensic evidence` y, si se requieren como prueba pericial, exporta los clips relevantes (en lotes de **máximo 10 clips por vez**) antes de su eliminación automática irrevocable a los **120 días** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Solicitud y aprobación dual en `Insider risk audit log` y clips exportados bajo custodia cifrada de Legal `[Verificado MS Learn]`.

### AH-03: Escalamiento Defensible de Caso Confirmado hacia Microsoft Purview eDiscovery (Premium)
- **Disparador:** Confirmación de violación material, fraude, fuga regulatoria o litigio laboral/comercial que exige preservación legal formal (*Legal Hold*), colección forense y revisión por abogados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Cases > [Caso] > Escalate for investigation` `[Verificado MS Learn]`.
- **Rol Responsable:** `Insider Risk Management Investigators` -> Handoff a `eDiscovery Manager` (Asesoría Legal) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.CO-02` / `Legal & Regulatory Response` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Consolidar en `Case notes` el resumen ejecutivo cronológico de evidencias verificadas en `Activity explorer` y `Content explorer` `[Verificado MS Learn]`.
  2. Seleccionar **Escalate for investigation**, asignar denominación codificada al nuevo caso legal y adjuntar instrucciones para Asesoría Legal (asegurando no disparar avisos al custodio en investigaciones reservadas) `[Verificado MS Learn]`.
  3. Confirmar la creación automática del caso vinculado en **Microsoft Purview eDiscovery** (teniendo presente que al exportar/escalar hacia eDiscovery se transfiere la identidad real UPN del custodio para sostener validez jurídica) `[Verificado MS Learn]`.
  4. El equipo Legal aplica de inmediato **eDiscovery Hold** sobre buzón, OneDrive, Teams e interacciones de Copilot del custodio antes de proceder al cierre administrativo del caso en IRM `[Verificado MS Learn]`.
- **Evidencia Auditable:** Vínculo trazable caso IRM -> caso eDiscovery y confirmación de *Legal Hold* activo `[Verificado MS Learn]`.

### AH-04: Respuesta Coordinada SOC ante Compromiso de Cuenta o Insider Activo Correlacionado en Defender XDR
- **Disparador:** Incidente unificado en `security.microsoft.com` que combina una alerta de exfiltración de Purview IRM con alertas de robo de token/credenciales en Entra ID, malware en Defender for Endpoint o movimiento lateral en Defender for Identity `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com > Incidents & alerts` y `entra.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2/L3 (`Security Operator`) + `Insider Risk Management Investigator` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Account Manipulation & Exfiltration (T1098 / TA0010)` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Determinar en minutos mediante telemetría de inicio de sesión (IP, dispositivo, anomalía de token) si se trata de un **adversario externo usando credenciales legítimas** o de un **usuario interno desactivando controles de seguridad** (*Security policy violations*) `[Verificado MS Learn]`.
  2. Ejecutar contención inmediata en **Microsoft Defender XDR** y **Entra ID**: aislamiento de red del endpoint (`Isolate device`), revocación de sesiones/refresh tokens y bloqueo de inicio de sesión.
  3. Utilizar el inventario de `Activity explorer` / `DataSecurityEvents` de IRM para determinar con exactitud qué archivos confidenciales fueron descargados o subidos durante la ventana de compromiso (evaluación precisa de notificación de brecha de datos personales) `[Verificado MS Learn]`.
  4. Sincronizar clasificación `True positive` / `Confirmed` entre ambos portales `[Verificado MS Learn]`.
- **Evidencia Auditable:** Incidente XDR contenido y dictamen de impacto exacto de datos afectados emitido a Privacidad/CISO `[Verificado MS Learn]`.

### AH-05: Contención de Fuga de Datos en Prompts de IA o Comportamiento Anómalo de Agentes (Risky AI / Risky Agents)
- **Disparador:** Alerta crítica de **Risky AI usage** por ingreso masivo de código fuente / PII en sitio GenAI no autorizado, o alerta de **Risky Agents (preview)** por un agente de Copilot Studio / Microsoft Foundry exponiendo datos sensibles o contactando dominios riesgosos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `Insider Risk Management > Alerts`, `DSPM for AI` y `admin.microsoft.com` / Power Platform Admin Center `[Verificado MS Learn]`.
- **Rol Responsable:** `IRM Investigator` + Administrador de Seguridad IA / Agent Admin `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Exfiltration Over Web Service & AI Agent Misuse (T1567)` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Si el evento proviene de un **Agente IA** (`Risky Agents`): suspender o cuarentenar de inmediato el agente en Copilot Studio / Microsoft Foundry / M365 Admin Center, revocar sus credenciales/conectores a SharePoint y auditar los permisos de publicación del creador `[Verificado MS Learn]`.
  2. Si el evento proviene de un **Usuario humano** (`Risky AI usage`): validar si fue negligencia (enviar *Notice template* de uso seguro de IA y reforzar bloqueo inline de navegador con Purview DLP for Endpoint/Browser) o exfiltración deliberada (elevar a `Elevated` en *Adaptive Protection* y abrir caso formal) `[Verificado MS Learn]`.
  3. En caso de exposición de secretos o credenciales en prompts, rotar de inmediato las claves comprometidas y evaluar *Priority Cleanup* si los prompts/respuestas sensibles quedaron distribuidos internamente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de suspensión/remediación del agente o bloqueo DLP en navegador y cierre documentado de la alerta IA `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Microsoft Graph y PowerShell Operativas

#### Consulta 1: Caza de Exfiltración de Archivos Sensibles en Defender XDR Advanced Hunting (`DataSecurityEvents`) `[Verificado MS Learn]`
```kql
// Requiere rol Security Operator + Insider Risk Management Analyst o Investigator
DataSecurityEvents
| where Timestamp > ago(7d)
| where ActionType has_any ("FileCopiedToRemovableMedia", "BrowserUpload", "FileDownloaded", "FilePrinted")
| summarize TotalEventos = count(), ArchivosUnicos = dcount(ObjectName), Destinos = make_set(TargetDomain, 10)
    by AccountUpn, DeviceName, ActionType
| where TotalEventos >= 20
| order by TotalEventos desc
```

#### Consulta 2: Correlación Multi-Dominio de Alertas IRM con Defender y Entra ID en Advanced Hunting (`AlertInfo` + `AlertEvidence`) `[Verificado MS Learn]`
```kql
// Identifica usuarios que combinan alertas de Purview Insider Risk Management con alertas XDR en 14 días
let IrmAlerts = AlertInfo
    | where Timestamp > ago(14d)
    | where ServiceSource == "Microsoft Purview Insider Risk Management"
    | join kind=inner (AlertEvidence | where EntityType == "User") on AlertId
    | project IrmTime = Timestamp, AlertId, IrmTitle = Title, IrmSeverity = Severity, AccountUpn;
AlertInfo
| where Timestamp > ago(14d)
| where ServiceSource != "Microsoft Purview Insider Risk Management"
| join kind=inner (AlertEvidence | where EntityType == "User") on AlertId
| join kind=inner IrmAlerts on AccountUpn
| project AccountUpn, IrmTime, IrmTitle, IrmSeverity, OtherSource = ServiceSource, OtherTitle = Title, OtherSeverity = Severity
| order by IrmTime desc
```

#### Consulta 3: Detección de Comportamientos Anómalos Agregados (`DataSecurityBehaviors`) `[Verificado MS Learn]`
```kql
// Consulta insights conductuales enriquecidos de violaciones a políticas de seguridad de datos en Purview
DataSecurityBehaviors
| where Timestamp > ago(14d)
| summarize Comportamientos = count(), Categorias = make_set(BehaviorType, 10), UltimoEvento = max(Timestamp)
    by AccountUpn
| order by Comportamientos desc
```

#### Consulta 4: Correlación en Microsoft Sentinel de Alertas IRM con Inicios de Sesión Riesgosos en Entra ID (`SecurityAlert` + `SigninLogs`) `[Verificado MS Learn]`
```kql
// Cruza alertas ingeridas por el conector oficial de Insider Risk Management con riesgo de identidad
SecurityAlert
| where TimeGenerated > ago(7d)
| where ProductName has "Insider Risk Management" or ProviderName has "Insider Risk"
| extend EntitiesJson = parse_json(Entities)
| mv-expand EntitiesJson
| where EntitiesJson.Type == "account"
| extend UPN = strcat(tostring(EntitiesJson.Name), "@", tostring(EntitiesJson.UPNSuffix))
| join kind=leftouter (
    SigninLogs
    | where TimeGenerated > ago(7d)
    | where RiskLevelDuringSignIn in ("high", "medium")
    | summarize RiesgosSignIn = count(), IPs = make_set(IPAddress, 5) by UserPrincipalName
) on $left.UPN == $right.UserPrincipalName
| project TimeGenerated, AlertName, AlertSeverity, UPN, RiesgosSignIn, IPs, RemediationSteps
```

#### Consulta 5: Monitoreo en Microsoft Sentinel de Bloqueos de Entra Conditional Access por Adaptive Protection `[Verificado MS Learn]`
```kql
// Verifica activaciones reales de políticas de Acceso Condicional que evalúan la condición Insider risk
SigninLogs
| where TimeGenerated > ago(14d)
| mv-expand CAPolicy = parse_json(ConditionalAccessPolicies)
| where tostring(CAPolicy.displayName) has_any ("InsiderRisk", "AdaptiveProtection")
| where tostring(CAPolicy.result) in ("failure", "reportOnlyFailure", "reportOnlyInterrupted")
| project TimeGenerated, UserPrincipalName, AppDisplayName, IPAddress, PolicyName = tostring(CAPolicy.displayName), Result = tostring(CAPolicy.result)
| order by TimeGenerated desc
```

#### Consulta 6: Extracción de Alertas de Insider Risk Management vía Microsoft Graph Security API (Sustituto Recomendado de O365 Management API) `[Verificado MS Learn]`
```powershell
# Requiere permiso SecurityAlert.Read.All en Microsoft Graph
Connect-MgGraph -Scopes "SecurityAlert.Read.All"

Get-MgSecurityAlertV2 -Filter "serviceSource eq 'microsoftInsiderRiskManagement'" -Top 50 |
    Select-Object Id, Title, Severity, Status, Classification, CreatedDateTime, IncidentId |
    Format-Table -AutoSize
```

#### Consulta 7: Auditoría de Segregación de Funciones en los 6 Role Groups de Insider Risk Management (Security & Compliance PowerShell) `[Verificado MS Learn]`
```powershell
# Verifica que ningún usuario acumule simultáneamente roles incompatibles (ej. Admins + Investigators + Approvers)
Connect-IPPSSession

$irmGroups = @(
    "Insider Risk Management",
    "Insider Risk Management Admins",
    "Insider Risk Management Analysts",
    "Insider Risk Management Investigators",
    "Insider Risk Management Approvers",
    "Insider Risk Management Auditors"
)
foreach ($grp in $irmGroups) {
    $members = Get-RoleGroupMember -Identity $grp -ErrorAction SilentlyContinue
    foreach ($m in $members) {
        [PSCustomObject]@{
            RoleGroup = $grp
            Member    = $m.Name
            Recipient = $m.RecipientTypeDetails
        }
    }
}
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Capacidad Verificada | Consola o Consulta de Comprobación | Resultado Esperado ("Proof of Life") | Estado |
| --- | --- | --- | --- |
| **Privacidad por diseño y seudonimización activa** | `Settings > Insider Risk Management > Privacy` | `Show anonymized versions of usernames` habilitado conforme al estatuto aprobado. | `[Verificado MS Learn]` |
| **Escaneo continuo de Insider Risk Analytics** | `Insider Risk Management > Reports > Analytics` | Reportes agregados actualizados diariamente con ventana móvil de hasta 10 días. | `[Verificado MS Learn]` |
| **Salud del conector HR y políticas activas** | `Settings > Data connectors > My connectors` y `IRM > Policies` | Conector HR en `Connected` (< 24 h) y 100% de políticas en estado `Healthy` (sin `Warnings`). | `[Verificado MS Learn]` |
| **Cobertura de IA y Agentes** | `Insider Risk Management > Policies` | Políticas `Risky AI usage` y `Risky Agents (preview)` habilitadas y generando telemetría. | `[Verificado MS Learn]` |
| **Mitigación cerrada con Adaptive Protection** | `IRM > Adaptive protection > Settings` + políticas DLP y Entra CA | `Adaptive Protection = On` y reglas DLP / Acceso Condicional vinculadas a niveles *Elevated / Moderate / Minor*. | `[Verificado MS Learn]` |
| **Sincronización bidireccional con Defender XDR** | `Settings > Data sharing` + `security.microsoft.com > Advanced hunting` | `Share user risk details = On` y eventos consultables en `DataSecurityEvents` y `AlertInfo`. | `[Verificado MS Learn]` |
| **Auditoría independiente resguardada** | Enlace `Insider risk audit log > Export` | Exportación CSV mensual ejecutada por `Insider Risk Management Auditors` antes del límite de 180 días. | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Ejecutivos y Operativos

> **Nota de Gobernanza:** Los SLAs numéricos y metas porcentuales siguientes representan umbrales consultivos recomendados para comités de seguridad, legal y privacidad `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| --- | --- | --- | --- | --- | --- | --- |
| **KPI-01** | **Tiempo Medio de Triaje de Alertas Críticas (MTTA — High Severity)** | `Promedio(Timestamp primera decisión de analista - Timestamp generación alerta High)` | `<= 4 horas hábiles` (`100% < 24 h`) | Diaria / Semanal | SOC Manager / Líder IRM | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tasa de Verdaderos Positivos por Política (Signal-to-Noise Ratio)** | `(Alertas confirmadas o escaladas a caso / Total de alertas revisadas) × 100` | `>= 65%` tras ajuste con *Analytics* | Semanal / Mensual | `IRM Admins` / Ingeniería Detección | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Disponibilidad y Frescura de Conectores Críticos (HR / Endpoints)** | `(Días con importación HR exitosa < 24 h y cobertura de onboarding >= 95% / Días del mes) × 100` | `>= 99%` | Diaria / Mensual | `IRM Admins` / Plataforma | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Efectividad de Contención Automática (Adaptive Protection)** | `(Intentos de exfiltración o acceso bloqueados automáticamente en usuarios Elevated / Total intentos detectados en usuarios Elevated) × 100` | `>= 95%` sin intervención manual | Mensual | CISO / Arquitecto Zero Trust | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Reducción de Reincidencia Post-Notificación Educativa (Notices)** | `(Usuarios que NO vuelven a generar alerta en 90 días tras recibir Notice template / Total usuarios notificados por error inadvertido) × 100` | `>= 85%` de corrección conductual | Trimestral / Semestral | RR. HH. / Concientización / CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Cumplimiento de Privacidad, SoD y Doble Autorización Forense** | `(Solicitudes Forensic Evidence con aprobación independiente + accesos auditados sin desvíos / Total eventos auditados) × 100` | `100%` (tolerancia cero a abusos) | Diaria / Mensual | DPO / Auditoría Interna / Legal | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tiempo Medio de Escalamiento Legal a Purview eDiscovery** | `Promedio(Timestamp Escalate for investigation - Timestamp confirmación de violación grave en Caso)` | `<= 8 horas` en casos materiales | Mensual | General Counsel / Investigadores L3 | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Continuidad Operativa del Alert Triage Agent y Cobertura IA** | `(Días con Triage Agent activo sin expiración de 90 días + políticas Risky AI / Risky Agents saludables / Días del mes) × 100` | `100%` | Mensual | SOC Manager / Líder Seguridad IA | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de 5 Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Nombre del Nivel | Estado Técnico, Procesal y de Gobernanza |
| --- | --- | --- |
| **Nivel 1** | **Reactivo / Silos Manuales** | Investigaciones ad-hoc mediante búsquedas manuales de logs ante incidentes ya consumados; sin *Insider Risk Analytics*, sin conector HR ni estatuto formal con RR. HH. y Privacidad. |
| **Nivel 2** | **Fundacional con Privacidad por Diseño** | Estatuto tripartito aprobado; seudonimización activa por defecto; segregación básica de grupos de roles; *Insider Risk Analytics* habilitado y primeras políticas *Data leaks* y *Departing users* en producción. |
| **Nivel 3** | **Contextual e Integrado con SecOps** | Conector HR automatizado (< 24 h), onboarding de endpoints Windows/macOS y navegadores Edge/Chrome; *Priority user groups* activos; correlación bidireccional con **Microsoft Defender XDR** y escalamiento fluido hacia **Purview eDiscovery**. |
| **Nivel 4** | **Preventivo Dinámico (Adaptive Protection)** | **Adaptive Protection** cerrado en producción ajustando automáticamente controles en **Purview DLP**, **Entra Conditional Access** y retención DLCM de 120 días; *Forensic Evidence* gobernado con doble llave `Approvers` y caza semanal KQL. |
| **Nivel 5** | **Agéntico y Optimizado Zero Trust** | Gobierno integral de humanos y agentes mediante **Risky AI usage**, **Risky Agents (preview)** conectado a *DSPM for AI* y triaje asistido por **Purview Alert Triage Agent** (Security Copilot); calibración continua por *Peer Groups*, auditoría mensual independiente sellada y simulacros anuales ejecutivos. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

El siguiente mapeo vincula las capacidades de Microsoft Purview Insider Risk Management con las **6 funciones oficiales de NIST CSF 2.0 (CSWP 29)** y tácticas de **MITRE ATT&CK** (`TA0009 Collection`, `TA0010 Exfiltration`, `T1078 Valid Accounts`, `T1562 Impair Defenses`, `T1567 Exfiltration Over Web Service`) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome) | Capacidad Habilitadora en Purview IRM | Evidencia Auditable Reproducible | Etiqueta |
| --- | --- | --- | --- | --- | --- |
| **GOVERN (GV)** | `GV.RM-01` | Los objetivos y estrategia de gestión de riesgos de ciberseguridad e *insider risk* son acordados por el liderazgo. | Estatuto de Gobernanza de Riesgo Interno respaldado por *Insider Risk Analytics* y Comité Tripartito (Legal, RR. HH., Privacidad, CISO). | Acta constitutiva aprobada, DPIA vigente (`T-01`) y reportes ejecutivos mensuales de riesgo interno. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades están definidos y aplicados con separación de funciones. | Segregación estricta en los 6 Role Groups (`Admins`, `Analysts`, `Investigators`, `Approvers`, `Auditors`) y *Administrative Units*. | Salida del script PowerShell de membresías sin conflictos SoD y aprobaciones duales en `Forensic evidence`. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.OV-03` | El desempeño de la gestión de riesgos y el respeto a la privacidad se evalúan y auditan independientemente. | **Insider Risk Audit Log** independiente (180 días) y seudonimización predeterminada (`Show anonymized versions of usernames`). | Exportaciones mensuales CSV del `Insider risk audit log` firmadas por `Insider Risk Management Auditors` (`M-01`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican y registran exposiciones y comportamientos de riesgo en activos, usuarios y agentes. | **Insider Risk Analytics** (escaneo sin políticas de 10 días), *Priority user groups*, *Priority content* y política *Risky Agents (preview)*. | Informes de `Reports > Analytics` y definición documentada de contenido y grupos prioritarios. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos y accesos se gestionan dinámicamente aplicando mínimo privilegio según contexto de riesgo. | **Adaptive Protection** acoplado a **Microsoft Entra Conditional Access** para restringir o bloquear acceso ante nivel *Elevated*. | Políticas activas de Acceso Condicional con condición *Insider risk* y logs de bloqueo en `SigninLogs`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-02` | Se protege la confidencialidad e integridad de los datos en tránsito y frente a canales de exfiltración. | **Adaptive Protection** acoplado a **Purview DLP** bloqueando USB, impresión, correo externo o subida web según nivel *Elevated / Moderate*. | Reglas DLP condicionadas por *Insider risk level* y métricas mensuales `KPI-04`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AT-01` | El personal recibe concientización contextual para reducir errores de seguridad inadvertidos. | Envío automatizado o guiado de **Notice templates** ante fugas accidentales o uso riesgoso de IA. | Plantillas configuradas, historial de avisos enviados en casos y medición de no-reincidencia (`KPI-05`). | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-03` | Las actividades del personal y agentes se monitorean buscando eventos potencialmente adversos respetando la privacidad. | Plantillas *Departing users* (conector HR), *Data leaks*, *Security policy violations* (MDE), *Risky AI usage* y *Risky Agents*. | Tablero `Policies` al 100% en estado `Healthy` y conector HR en `Connected` (`D-01`, `S-02`). | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Los eventos adversos se analizan con contexto multi-fuente e inteligencia artificial para comprender su alcance. | Detección de secuencias, exfiltración acumulada con *Peer Groups*, **Purview Alert Triage Agent** y correlación en **Defender XDR**. | Historial de alertas clasificadas en `Alerts`, vista `Triage Agent` y caza KQL en `DataSecurityEvents`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MA-02` | Los informes de incidentes son triados, validados e investigados con cadena de custodia. | Gestión estructurada en **Cases**, `Activity explorer`, `Content explorer` y clips de **Forensic Evidence** bajo doble autorización. | Expedientes de casos con `Case notes` completas y trazas de autorización dual de clips forenses. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.CO-02` | Las partes interesadas internas (Legal, RR. HH., SOC) son coordinadas de forma segura conforme a procedimientos. | Flujos **Power Automate** hacia RR. HH./managers, conector **Microsoft Sentinel** y transferencia nativa `Escalate for investigation` hacia **Purview eDiscovery**. | Casos escalados exitosamente a Purview eDiscovery con *Legal Hold* activo (`AH-03`). | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-03` | Se asegura la preservación e integridad de evidencias y datos eliminados durante incidentes internos. | Preservación automática de **120 días** en DLCM disparada por *Adaptive Protection* para usuarios *Elevated* y mejoras semestrales `SM-01`. | Directiva automática de retención de 120 días verificada en Purview y actas semestrales de lecciones aprendidas. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Destinatario | Rutas Oficiales Microsoft Learn y Entrenamiento Ninja | Referentes Verificados (Microsoft y Comunidad MVP) | Certificaciones y Marcos Complementarios (Nov 2026) | Estado |
| --- | --- | --- | --- | --- |
| **Ingeniero / Admin de Insider Risk Management** | Ruta oficial SC-401 *Implement and manage Insider Risk Management in Microsoft Purview* (5 módulos); guías de *Adaptive Protection*, *Forensic Evidence* y *Triage Agent*. | **Erin Miyake** (Microsoft PM, Adaptive Protection + Entra CA); **Patrick David** (Microsoft Principal PM, Ninja IRM & Triage Agents); **Sathish Veerapandian** (MVP Security, *EzCloudInfo*). | **Microsoft Certified: Information Security Administrator Associate (Exam SC-401)**. | `[Verificado MS Learn]` |
| **Analista SOC e Investigador Forense (L1/L2/L3)** | Documentación *Investigate insider risk threats in the Microsoft Defender portal*, caza KQL en `DataSecurityEvents` y sesiones del *Virtual Ninja Show* de Defender XDR + IRM. | **Maayan Magenheim**, **Sravan Kumar Mera** y **Michelle Slotwinski** (equipo de producto Microsoft IRM/XDR); **Jorge Castañeda** (MVP Security en español). | **Exam SC-200** (Security Operations Analyst) + **Exam SC-401**. | `[Verificado MS Learn]` |
| **Legal, RR. HH., Privacidad (DPO) y Approvers / Auditors** | Versiones oficiales en español de *Introducción*, *Configuración inicial* (cláusula legal) y *Asignación de permisos* en Microsoft Learn (contrastando siempre contra inglés). | **Nikki Chapple** (MVP) y **Ryan John Murphy** (Microsoft), podcast *All Things M365 Compliance*; archivo oficial de IRM en *Microsoft Security Blog*. | Marco **SEI/CERT Common Sense Guide to Mitigating Insider Threats (7th Ed.)** y capacitación anual del Comité Tripartito. | `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Técnicas Verificadas al `2026-11-11`

| # | Área Auditada | Hallazgo y Corrección Aplicada | Fuente Oficial Verificada |
| --- | --- | --- | --- |
| **1** | **Saneamiento de cruces documentales en `MSEOP-MD\Purview IRM`** | En `0404 - Purview IRM - Bloques - SecOps`, `Version Consolidada (1)` y `Purview IR\Construye una tabla (1)` se habían exportado por error tablas y guías genéricas de Sentinel, Defender for Office 365 e Intune. Se descartaron por completo y se construyeron 28 actividades dedicadas 100% a Purview Insider Risk Management. | Auditoría del repositorio fuente + `SPEC_GUIA_OPERACIONAL.md` `[Decisión / Propuesta Editorial]` |
| **2** | **Corrección crítica sobre la arquitectura del Insider Risk Audit Log** | Un documento fuente (`Purview IR`) afirmaba erróneamente que la auditoría de IRM se consulta en el Unified Audit Log buscando `InsiderRiskManagementCaseAccessed`. Microsoft Learn establece taxativamente que el **Insider Risk Audit Log no está asociado al Microsoft 365 Audit Log**: es un sistema independiente e indeshabilitable, consultable dentro de IRM por `Auditors` y retenido exactamente **180 días**. | `learn.microsoft.com/en-us/purview/insider-risk-management-audit-log` `[Verificado MS Learn]` |
| **3** | **Precisión de soporte de sistema operativo en Forensic Evidence** | Frente a la creencia común de soporte multi-OS para grabación de pantalla, se verificó en Microsoft Learn que mientras macOS soporta onboarding de indicadores de actividad IRM, la captura visual de **Forensic Evidence está soportada exclusivamente en Windows 10/11 Enterprise y Windows 365 (64-bit, GPU integrada DirectX 11+)** con *Microsoft Purview Client*, doble autorización `Approvers` y borrado automático de clips a los **120 días**. | `learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence` `[Verificado MS Learn]` |
| **4** | **Incorporación de Risky Agents (preview) y Purview Alert Triage Agent (2026)** | Se documentó la política predeterminada **Risky Agents (preview)** para agentes en Copilot Studio, Microsoft Foundry y P4AI SDK (compartiendo riesgo con *DSPM for AI* y sin visibilidad para admins acotados por AU), así como el **Alert Triage Agent** en Security Copilot (consumo de SCUs, nombres no anonimizados en su vista y **expiración del contexto a los 90 días** desde el último guardado). | `insider-risk-management-monitoring-agents` y `copilot-in-purview-triage-irm-agent-get-started` `[Verificado MS Learn]` |
| **5** | **Matices exactos de seudonimización (Data Risk Graph, API y eDiscovery)** | Se incorporaron las tres reglas oficiales de `Privacy`: (1) con nombres anonimizados activos no se puede usar `Data risk graph`; (2) el panel del `Triage Agent` muestra nombres sin anonimizar; y (3) exportar vía API SIEM o escalar a `Purview eDiscovery` muestra UPN reales para integridad referencial, mientras que exportar a CSV sí preserva pseudónimos. | `learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy` `[Verificado MS Learn]` |
| **6** | **Adaptive Protection ampliado a DLP, Entra Conditional Access y retención DLCM de 120 días** | Se validó la mitigación triple cerrada de *Adaptive Protection*: bloqueo/restricción dinámica en Purview DLP y **Microsoft Entra Conditional Access** según niveles *Elevated / Moderate / Minor*, más la creación automática de una política de retención de **120 días** para datos eliminados por usuarios en nivel *Elevated*. | `learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection` `[Verificado MS Learn]` |
| **7** | **Integración Defender XDR, Graph Security API y precaución en Sentinel SOAR** | Se documentaron las 4 tablas KQL en Advanced Hunting (`AlertInfo`, `AlertEvidence`, `DataSecurityBehaviors`, `DataSecurityEvents`), la recomendación oficial de migrar de Office 365 Management Activity API hacia **Microsoft Graph Security API** y la precaución en reglas SOAR de Sentinel ante incidentes IRM sin payload de alerta anidado. | `learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender` `[Verificado MS Learn]` |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Definido | Naturaleza | Justificación Arquitectónica y de Gobierno |
| --- | --- | --- | --- |
| **1** | **SLAs operativos (`KPI-01` <= 4 h para alertas High; `KPI-07` <= 8 h para escalamiento legal) y metas porcentuales** | `[Decisión / Propuesta Editorial]` | Microsoft Learn define tiempos de sincronización técnica (ej. <= 30 min entre Purview y Defender, hasta 36 h en Adaptive Protection inicial), pero los SLAs de respuesta humana deben fijarse como estándar de gobierno SOC/Legal. |
| **2** | **Renovación preventiva cada 60 días de la configuración del Purview Alert Triage Agent** | `[Decisión / Propuesta Editorial]` | Dado que el agente deja de ejecutarse automáticamente a los **90 días** del último guardado de configuración, programar su renovación en `M-04` a los 60 días garantiza disponibilidad continua con margen de seguridad de 30 días. |
| **3** | **Exportación mensual sellada (CSV + SHA-256) del Insider Risk Audit Log independiente** | `[Decisión / Propuesta Editorial]` | Como el `Insider risk audit log` elimina permanentemente los registros tras **180 días**, la extracción mensual firmada por `Auditors` asegura trazabilidad anual completa ante auditorías laborales o de protección de datos. |
| **4** | **Restricción del Role Group comodín `Insider Risk Management` a cuentas de resguardo bajo PIM** | `[Decisión / Propuesta Editorial]` | Aunque el grupo existe nativamente, usarlo en el día a día anula la separación entre diseño de políticas, acceso a contenido privado y aprobación forense; se reserva únicamente para evitar el riesgo de *zero administrator*. |
| **5** | **Modelo de madurez de 5 niveles y mapeo probatorio de 12 subcategorías NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Estructura la evolución ética y técnica del programa desde analítica anónima hasta mitigación dinámica Zero Trust y gobierno agéntico auditable. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** *Learn about Insider Risk Management* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management`). Arquitectura general, privacidad por diseño y flujo operativo end-to-end `[Verificado MS Learn]`.
- **REF-02:** *Assign permissions in Insider Risk Management* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-permissions`). Matriz exacta de los 6 grupos de roles nativos y efecto de *Administrative Units* `[Verificado MS Learn]`.
- **REF-03:** *Manage username privacy in Insider Risk Management* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-privacy`). Comportamiento de seudonimización frente a `Data risk graph`, `Triage Agent`, API SIEM y eDiscovery `[Verificado MS Learn]`.
- **REF-04:** *Enable analytics in Insider Risk Management* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-analytics`). Escaneo base sin políticas de hasta 10 días e insights compartidos a nivel usuario `[Verificado MS Learn]`.
- **REF-05:** *Learn about Insider Risk Management policy templates* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-policy-templates`). Catálogo oficial de plantillas (*Departing users*, *Data leaks*, *Risky AI usage*, *Security policy violations*, *Patient data misuse*) `[Verificado MS Learn]`.
- **REF-06:** *Monitoring agents in Insider Risk Management (`Risky Agents` preview)* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-monitoring-agents`). Monitoreo de agentes en Copilot Studio, Microsoft Foundry y P4AI SDK e integración con *DSPM for AI* `[Verificado MS Learn]`.
- **REF-07:** *Get started with the Microsoft Purview Triage Agent in Insider Risk Management* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/copilot-in-purview-triage-irm-agent-get-started`). Requisitos de SCUs, roles y caducidad de contexto a los 90 días `[Verificado MS Learn]`.
- **REF-08:** *Help dynamically mitigate risks with Adaptive Protection* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection`). Niveles *Elevated / Moderate / Minor* integrados con Purview DLP, Entra Conditional Access y retención DLCM de 120 días `[Verificado MS Learn]`.
- **REF-09:** *Learn about Insider Risk Management forensic evidence* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-forensic-evidence`). Requisitos exclusivos Windows 10/11 Enterprise y Windows 365, doble autorización `Approvers` y retención de clips por 120 días `[Verificado MS Learn]`.
- **REF-10:** *Prioritize user groups for Insider Risk Management policies* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-priority-user-groups`). Grupos prioritarios de hasta 10.000 usuarios y restricción granular de revisores `[Verificado MS Learn]`.
- **REF-11:** *Review activities with the Insider Risk Management audit log* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-audit-log`). Independencia respecto al M365 Audit Log, retención de 180 días y exportación CSV `[Verificado MS Learn]`.
- **REF-12:** *Investigate insider risk threats in the Microsoft Defender portal* — Microsoft Learn (`https://learn.microsoft.com/en-us/defender-xdr/irm-investigate-alerts-defender`). Correlación bidireccional XDR, tablas KQL (`DataSecurityEvents`, `DataSecurityBehaviors`), Graph Security API y conector Sentinel `[Verificado MS Learn]`.
- **REF-13:** *Take action on Insider Risk Management cases* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/insider-risk-management-cases`). Gestión de casos, `Case notes`, `Content explorer` y escalamiento nativo a Purview eDiscovery `[Verificado MS Learn]`.

### 15.2 Blogs Oficiales y Empleados de Microsoft
- **REF-14:** Michelle Slotwinski (Microsoft) — *Introducing a unified alert experience for Microsoft Purview Insider Risk Management*, Microsoft Security Blog (`https://techcommunity.microsoft.com/blog/microsoft-security-blog/introducing-a-unified-alert-experience-for-microsoft-purview-insider-risk-manage/4530714`). Evolución 2026 de la experiencia unificada de triaje de alertas `[Verificado MS Learn]`.
- **REF-15:** Nathalia Borges y Patrick David (Microsoft) — *Announcing Alert Triage Agents in Microsoft Purview powered by Security Copilot*, Microsoft Security Blog (`https://techcommunity.microsoft.com/blog/microsoft-security-blog/announcing-alert-triage-agents-in-microsoft-purview-powered-by-security-copilot/4396041`). Arquitectura de agentes de triaje para IRM y DLP `[Verificado MS Learn]`.
- **REF-16:** Maayan Magenheim y Sravan Kumar Mera (Microsoft) — *Defender XDR data security context with Insider Risk Management*, Microsoft Virtual Ninja Training (`https://learn.microsoft.com/en-us/shows/microsoft-sentinel-defender-xdr-virtual-ninja-training/defender-xdrs-data-security-context-with-insider-risk-management`). Integración operativa SOC entre XDR e IRM `[Verificado MS Learn]`.

### 15.3 Referentes de la Comunidad y MVPs de Seguridad
- **REF-17:** Sathish Veerapandian (Microsoft Security MVP) — *EzCloudInfo: Purview Insider Risk Management, Adaptive Protection & Risky Copilot Usage* (`https://ezcloudinfo.com/`). Escenarios prácticos de despliegue, protección adaptativa para el SOC e investigación de uso riesgoso de Microsoft 365 Copilot.
- **REF-18:** Nikki Chapple (Microsoft MVP) — *Purview Data Security & AI Governance Blog* (`https://nikkichapple.com/`) y Jorge Castañeda (Microsoft Security MVP) — *D3FEND Blog* (`https://blog.d3fend.me/`). Prácticas de gobierno Purview, preparación para Copilot y operaciones SecOps en español.

### 15.4 Marcos Normativos y Guías de Referencia de la Industria
- **REF-19:** National Institute of Standards and Technology — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`) y Software Engineering Institute (CMU SEI/CERT) — *Common Sense Guide to Mitigating Insider Threats, Seventh Edition* (`https://www.sei.cmu.edu/library/common-sense-guide-to-mitigating-insider-threats-seventh-edition/`).

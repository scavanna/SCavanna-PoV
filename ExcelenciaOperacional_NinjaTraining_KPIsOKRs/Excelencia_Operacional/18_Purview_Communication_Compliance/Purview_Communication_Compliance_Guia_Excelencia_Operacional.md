# Guía Maestra de Excelencia Operacional: Microsoft Purview Communication Compliance (Riesgo Conductual, Supervisión Regulatoria e Interacciones IA)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Valor Oficial / Definición |
| :--- | :--- |
| **Identificador del Módulo** | `18_Purview_Communication_Compliance` |
| **Slug Canónico** | `Purview_Communication_Compliance` |
| **Nombre Completo** | Microsoft Purview Communication Compliance (Riesgo Conductual, Supervisión Regulatoria e Interacciones IA) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` `[Verificado MS Learn]` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (+ Pay-As-You-Go para fuentes no-M365/IA) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (`Solutions > Communication Compliance`), `https://admin.teams.microsoft.com`, `https://security.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Chief Compliance Officer (CCO), Legal & Regulatory Counsel, Human Resources (Employee Relations), Insider Risk Manager, SOC L2/L3, AI Governance Lead, Purview Compliance Admin |
| **Marcos Normativos Alineados** | NIST CSF 2.0 (`GV, ID, PR, DE, RS, RC`), MITRE ATT&CK v18 / ATLAS, FINRA Rule 3110 / 4530 / 3310 / 2010, SEC Rule 17a-4 / 10b-5, MiFID II, EU AI Act, ISO/IEC 42001, Ley 21.719 (Chile) |

> **Nota de consolidación arquitectónica (Noviembre 2026):** Esta guía operacional incorpora la transición definitiva al portal unificado de Microsoft Purview (`purview.microsoft.com`) tras el retiro del portal clásico a finales de 2024 (`MC939918`), el renombre comercial de *Microsoft 365 E5 Compliance* a **Microsoft Purview Suite** (octubre de 2025), la entrada en vigor de **Policy Match Preservation** configurable (1 mes, 6 meses, 1 año o 7 años desde junio de 2025), la supervisión nativa de prompts y respuestas de **Microsoft 365 Copilot**, **Copilot Studio**, **Microsoft Agent 365** (GA mayo de 2026) y aplicaciones GenAI empresariales como **Anthropic Claude Enterprise** (agosto de 2026) mediante clasificadores basados en LLM (*Prompt Shields*, *Protected material*, *Hate*, *Violence*, *Sexual*, *Self-harm*), así como la facturación complementaria por consumo (*Pay-As-You-Go* por registros de texto de 1.000 caracteres) para cargas no-M365 `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

**Microsoft Purview Communication Compliance** es la solución estratégica de supervisión conductual, cumplimiento regulatorio y seguridad de interacciones con Inteligencia Artificial Generativa dentro de **Microsoft Purview Suite** `[Verificado MS Learn]`. Su propósito operativo es detectar, capturar, contextualizar y remediar mensajes e interacciones potencialmente inapropiadas o ilícitas en canales corporativos internos, externos y agénticos, garantizando **privacidad por diseño (*Privacy by Design*)** mediante seudonimización predeterminada de identidades, segregación estricta de funciones RBAC, opt-in explícito de administradores e inmutabilidad en el registro unificado de auditoría `[Verificado MS Learn]`.

En una arquitectura **Zero Trust** moderna a noviembre de 2026, el perímetro de riesgo ya no se limita al correo electrónico tradicional ni a la exfiltración binaria bloqueada por DLP: abarca amenazas internas precedidas por estresores laborales (*acoso dirigido, amenazas, sabotaje corporativo*), infracciones financieras severas (*manipulación bursátil, colusión regulatoria, lavado de activos, divulgación no autorizada* bajo SEC/FINRA/MiFID II) y riesgos emergentes en **IA Generativa y Agentes Autónomos** (*ataques adversarios de Prompt Injection / Jailbreak, generación de material protegido por derechos de autor y exposición de propiedad intelectual en prompts*) `[Verificado MS Learn]`. Communication Compliance actúa como sensor temprano y mesa de supervisión legal/RR. HH., alimentando indicadores de riesgo conductual hacia **Microsoft Purview Insider Risk Management (IRM)** y escalando evidencia forense directamente hacia casos de **Microsoft Purview eDiscovery (Premium)** `[Verificado MS Learn]`.

### 2.1 Matriz de Licenciamiento, Medidores Pay-As-You-Go y Prerrequisitos

| Componente / Capacidad | Licenciamiento Base / Add-on Requerido | Modelo de Cobro y Alcance Técnico | Estado a Nov-2026 |
| :--- | :--- | :--- | :--- |
| **Canales nativos M365 (Exchange Online, Teams, Viva Engage)** | Microsoft 365 E5 / E7, A5, F5 Compliance, G5; Office 365 E5; **Microsoft Purview Suite** (antes M365 E5 Compliance); o E5 Insider Risk Management add-on | Por usuario supervisado (*per-user licensing*). Sin cargos por consumo adicionales para buzones Exchange Online, chats/canales/transcripciones Teams y Viva Engage en modo nativo. | GA `[Verificado MS Learn]` |
| **Interacciones con Microsoft 365 Copilot y M365 Copilot Chat** | Licencia base de Communication Compliance (M365 E5 / Purview Suite) + licencia de Microsoft 365 Copilot | Incluido **sin cargos Pay-As-You-Go** para interacciones de usuarios con Microsoft 365 Copilot y Microsoft 365 Copilot Chat (`IPM.SkypeTeams.Message.Copilot.*`), incluyendo *Prompt Shields* y *Protected material*. | GA `[Verificado MS Learn]` |
| **Interacciones IA no-M365, Copilot Studio y Enterprise/Other AI Apps** | Suscripción Azure vinculada a **Microsoft Purview Pay-As-You-Go** + licencia base elegible | Facturación por consumo basada en **Text records** (`1 registro de texto = 1.000 caracteres` redondeado hacia arriba; ej. 7.500 caracteres = 8 registros). Aplica tarifa *Premium* al evaluar *Code of conduct* (`Hate, Self-harm, Violence, Sexual`) o *Risky Gen AI* (`Prompt Shields, Protected material`). Cubre Copilot Studio, Fabric Copilot, Security Copilot, Claude Enterprise y apps IA de red/navegador. | GA `[Verificado MS Learn]` |
| **Agentes registrados en Microsoft Agent 365** | Microsoft 365 E7 / Licenciamiento Agent 365 + Microsoft Purview Suite (+ PAYG según origen del agente) | Las instancias de agentes se incluyen en políticas de Communication Compliance igual que un usuario para detectar comunicaciones poco éticas humano-a-agente y agente-a-humano en Teams y correo electrónico. | GA (desde mayo 2026) `[Verificado MS Learn]` |
| **Conectores de terceros (Bloomberg, Slack, Zoom, WhatsApp, SMS)** | Licencia base de Communication Compliance + Conector M365 o partner certificado (ej. TeleMessage, 17a-4, Smarsh) | Ingesta hacia buzones de usuario en Exchange Online; detección entre 24 y 48 horas según frecuencia de importación. *(Nota: conectores nativos de Veritas retirados el 30-jun-2024)*. | GA `[Verificado MS Learn]` |
| **Resumen contextual asistido por IA (Summarize with Copilot)** | **Microsoft Security Copilot** (dotación base de SCUs en M365 E5 o SCUs aprovisionadas en Azure) + rol *Security Copilot Contributor* | Resume mensajes, adjuntos `.docx/.pdf/.txt`, grabaciones y transcripciones de entre 100 y 15.000 palabras en el contexto del clasificador que disparó la alerta. | GA `[Verificado MS Learn]` |

**Prerrequisitos técnicos obligatorios antes de operar `[Verificado MS Learn]`:**
1. **Auditoría unificada habilitada** (`UnifiedAuditLogIngestionEnabled = True` en Exchange Online PowerShell) para registrar toda creación, edición y revisión de políticas (`SupervisionPolicyCreated`, `SupervisionRuleMatch`, `SupervisoryReviewTag`).
2. **Buzones alojados en Exchange Online** tanto para usuarios supervisados (o grupos de distribución para entornos híbridos con almacenamiento en nube de Teams) como obligatoriamente para todos los **Reviewers** asignados a las políticas.
3. **Viva Engage en Native Mode** (usuarios en Entra ID, grupos M365 y archivos en SharePoint) para inspeccionar mensajes privados, conversaciones comunitarias y adjuntos.
4. **Transcripción de reuniones habilitada en Teams Admin Center** si la organización requiere supervisar contenido hablado en reuniones programadas, recurrentes o *Meet Now*.
5. **Suscripción de Azure vinculada a Purview Pay-As-You-Go** antes de activar ubicaciones *Enterprise AI apps*, *Other AI apps* o agentes/Copilots no-M365.

### 2.2 Principios Rectores de Excelencia Operacional

1. **Privacidad por Diseño y Seudonimización Predeterminada (`[Verificado MS Learn]`):** Mantener activa la seudonimización de nombres de usuario (ej. `ANON2340`) para analistas de primer nivel con el fin de eliminar sesgos cognitivos y proteger la intimidad laboral, revelando la identidad real únicamente bajo protocolo documentado de investigación formal con RR. HH. o Legal.
2. **Segregación Inquebrantable entre Administración de Plataforma e Investigación de Contenido (`[Verificado MS Learn]`):** Ningún *Global Administrator* ni miembro de *Communication Compliance Admins* puede leer mensajes ni alertas por defecto; la configuración técnica recae en TI/Cumplimiento Técnico, mientras que el triaje y la remediación recaen exclusivamente en *Analysts* e *Investigators* nombrados explícitamente como *Reviewers* en cada política.
3. **Supervisión Unificada de Comunicaciones Humanas, Agénticas y GenAI (`[Verificado MS Learn]`):** Gobernar bajo un mismo flujo operativo tanto canales tradicionales (Exchange, Teams, Viva Engage, WhatsApp/Bloomberg) como prompts y respuestas de Microsoft 365 Copilot, Copilot Studio, Microsoft Agent 365 y LLMs empresariales frente a *Prompt Shields* y *Protected material*.
4. **Detección Multimodal de Alta Precisión y Reducción de Ruido (`[Verificado MS Learn]`):** Combinar SITs, diccionarios personalizados de hasta 100 KB comprimidos, clasificadores entrenables regulatorios/conductuales, clasificadores de seguridad de contenido LLM (umbral de severidad >= 4), análisis de sentimiento y OCR integrado (100 KB a 4 MB), activando sistemáticamente *Filter email blasts* y *Cross-policy resolution*.
5. **Gobierno Proactivo de Límites de Almacenamiento y Preservación de Evidencia (`[Verificado MS Learn]`):** Monitorear preventivamente el límite duro de **100 GB o 1 millón de mensajes** por buzón de revisión de política (alertas al 80 %, 90 % y 95 %) y alinear el ajuste **Policy Match Preservation** (1 mes, 6 meses, 1 año o 7 años) con los plazos legales sectoriales sin confundirlo con la retención WORM del mensaje original en Data Lifecycle Management.
6. **Orquestación Transversal con Insider Risk Management y eDiscovery Premium (`[Verificado MS Learn]`):** Transformar señales de hostilidad o incumplimiento reiterado (>= 5 mensajes riesgosos en 24 h) en disparadores automáticos de alcance para políticas de fuga de datos en IRM, y escalar incidentes graves con preservación probatoria directa hacia *eDiscovery (Premium)* (hasta 100 mensajes por lote).

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional y Flujo de Procesamiento

A diferencia de Data Loss Prevention (DLP) —que actúa de forma síncrona o cuasi-síncrona para bloquear o advertir sobre exfiltración de datos estructurados en tránsito—, **Communication Compliance** opera como un motor asíncrono de **supervisión profunda post-entrega** `[Verificado MS Learn]`. El motor evalúa señales cada **1 hora** a partir de la hora exacta de creación de la política (`Last policy scan`):
- **Latencia de 1 hora (`[Verificado MS Learn]`):** Cuerpo y metadatos de correo Exchange Online, cuerpo y metadatos de chats/canales Teams, transcripciones de reuniones Teams, mensajes sin adjuntos en Viva Engage y cuerpo de prompts/respuestas de Microsoft 365 Copilot y M365 Copilot Chat.
- **Latencia de hasta 24 horas (`[Verificado MS Learn]`):** Adjuntos de correo Exchange, adjuntos clásicos y *Modern attachments* de OneDrive/SharePoint en Teams (`.docx, .xlsx, .xls, .csv, .pptx, .txt, .pdf`, extraídos automáticamente como `<archivo>.txt`), canales compartidos de Teams y adjuntos de Viva Engage.
- **Latencia de 24 a 48 horas (`[Verificado MS Learn]`):** Escaneo **OCR** de texto impreso o manuscrito en imágenes (`.jpg/.jpeg, .png, .bmp, .tiff` de 100 KB a 4 MB) y datos importados mediante conectores de terceros (Instant Bloomberg, Slack, Zoom, WhatsApp, SMS).

Cuando un mensaje cumple las condiciones (y entra dentro del porcentaje de muestreo configurado, ej. 10 % para supervisión aleatoria FINRA o 100 % para acoso/IA), Communication Compliance guarda una **copia aislada** del mensaje en un buzón de supervisión dedicado (*Review Mailbox*) asociado a la política `[Verificado MS Learn]`. Esta copia permanece disponible durante el periodo definido en **Policy Match Preservation** (por defecto **1 año** desde el 1 de junio de 2025; configurable en 1 mes, 6 meses, 1 año o 7 años) incluso si el usuario abandona la organización y su buzón primario se elimina; por el contrario, eliminar la política destruye permanentemente todas sus copias y alertas asociadas `[Verificado MS Learn]`.

#### Matriz Técnica de Canales Monitoreados, Latencias de Detección y Límites Operativos

| Canal / Ubicación Oficial | Elementos Inspeccionados | Latencia de Detección | Reglas de Alcance y Límites Críticos Verificados |
| :--- | :--- | :--- | :--- |
| **Exchange Online** | Cuerpo, asunto, metadatos y adjuntos soportados por reglas de flujo de correo + imágenes OCR (100 KB–4 MB). | Cuerpo/metadatos: `1 h`<br>Adjuntos y OCR: `24 h` | Canal opcional (ya no obligatorio en políticas nuevas). Máximo **25 adjuntos** evaluados por coincidencia `[Verificado MS Learn]`. |
| **Microsoft Teams (Chats 1:1 / Grupales)** | Mensajes de chat, emojis/imágenes inline, *Modern attachments* de OneDrive/SharePoint (`.docx, .xlsx, .xls, .csv, .pptx, .txt, .pdf`) e imágenes OCR. | Cuerpo/metadatos: `1 h`<br>Adjuntos modernos/OCR: `24 h` | Soporta entornos híbridos de correo asignando un grupo de distribución a usuarios con buzón on-premises y almacenamiento Teams en nube `[Verificado MS Learn]`. |
| **Microsoft Teams (Canales Privados, Públicos y Compartidos)** | Publicaciones en canales estándar, privados y *Shared channels* (internos y externos para usuarios internos en alcance). | Cuerpo: `1 h`<br>Shared channels: `24 h` | Si `Direction = Inbound` y un usuario en alcance pertenece al canal, **todos los mensajes del canal** pueden evaluarse aunque provengan de miembros no incluidos. Canales públicos: **máx. 250 usuarios** en alcance estático y **sin soporte para Adaptive Scopes de usuarios**. *Shared channels* no soportan *Modern attachments* `[Verificado MS Learn]`. |
| **Microsoft Teams (Meeting Transcripts)** | Transcripciones de reuniones programadas (captura todo el contenido hablado aunque se hable desde sala compartida), recurrentes y *Meet now* (hablantes identificados). | `1 h` tras cierre de transcripción | Requiere activar transcripción en Teams Admin Center. Solo evalúa SITs, listas de palabras clave y los **6 clasificadores regulatorios** (ignora clasificadores de conducta laboral). No captura reuniones externas organizadas fuera del tenant `[Verificado MS Learn]`. |
| **Viva Engage** | Mensajes privados, conversaciones comunitarias públicas y archivos adjuntos almacenados en SharePoint. | Cuerpo: `hasta 1 h`<br>Con adjuntos: `hasta 24 h` | Exige **Viva Engage en Native Mode** (usuarios en Entra ID, grupos M365 y archivos en SharePoint). *Report Conversations* viene desactivado por defecto `[Verificado MS Learn]`. |
| **Microsoft Copilot Experiences** | Prompts del usuario y respuestas generadas en Microsoft 365 Copilot y M365 Copilot Chat (`IPM.SkypeTeams.Message.Copilot.*`), así como Copilot Studio. | `1 h` (M365 Copilot) | M365 Copilot incluido sin costo PAYG; Copilot Studio, Fabric Copilot y Security Copilot requieren **Pay-As-You-Go** habilitado. Evalúa prompt y respuesta como entradas separadas `[Verificado MS Learn]`. |
| **Microsoft Agent 365** | Interacciones humano-a-agente y agente-a-humano en Microsoft Teams y correo electrónico. | `1 h` a `24 h` según canal | Las instancias de agentes se agregan al alcance de la política igual que un usuario; visibilidad centralizada en `DSPM > AI observability` `[Verificado MS Learn]`. |
| **Enterprise AI Apps y Other AI Apps** | Prompts y respuestas en apps IA conectadas vía Microsoft Entra / Data Map (ej. Anthropic Claude Enterprise) y apps IA detectadas en navegador/red (catálogo Defender for Cloud Apps). | `1 h` a `24 h` según conector/red | Requiere **Pay-As-You-Go** (medidor *Text records* = 1.000 caracteres). En la cola aparecen con asunto `[AI app]` y remitente *Connected AI app* o *Cloud AI app* `[Verificado MS Learn]`. |
| **Fuentes No-Microsoft (3rd-Party Connectors)** | Instant Bloomberg, ICE Chat, Slack, Zoom, WhatsApp, SMS e ingesta vía partners certificados hacia buzones Exchange Online. | `24 a 48 h` según frecuencia de importación | El conector debe estar aprovisionado previamente en `Data connectors` para aparecer en la sección *Third-Party Sources* del asistente de políticas `[Verificado MS Learn]`. |

#### Catálogo Completo de Clasificadores Integrados (Trainable Classifiers, LLM Content Safety y GenAI)

| Familia de Clasificador | Clasificadores Oficiales | Cobertura / Requisitos de Evaluación | Caso de Uso Normativo / Operativo |
| :--- | :--- | :--- | :--- |
| **Trainable Classifiers — Regulatorios Financieros** | `Customer complaints`, `Gifts & entertainment`, `Money laundering`, `Regulatory collusion`, `Stock manipulation`, `Unauthorized disclosure`, `Corporate sabotage` | Mensajes que cumplan el mínimo de palabras por idioma; soportados también en transcripciones de reuniones de Teams `[Verificado MS Learn]`. | FINRA Rules 3110, 4530, 3310, 2320, 2010, 5270; SEC Rule 10b-5; FCPA; UK Bribery Act; Bank Secrecy Act; NERC CIP `[Verificado MS Learn]`. |
| **Trainable Classifiers — Conducta Empresarial** | `Harassment` (citado como *Targeted harassment* en plantillas), `Threat`, `Profanity`, `Discrimination` (solo inglés) | Multi-idioma (excepto *Discrimination*); usar *Filter email blasts* para evitar falsos positivos en boletines masivos `[Verificado MS Learn]`. | Código de Ética, prevención de acoso laboral y activación automática de *Insider risk trigger* en IRM (>= 5 mensajes en 24 h) `[Verificado MS Learn]`. |
| **Azure AI Content Safety (Basados en LLM)** | `Hate`, `Sexual`, `Violence`, `Self-harm` | Solo M365 Copilot, Teams y Viva Engage; mensajes de `>= 5 palabras` y hasta `10.000 caracteres` (sin adjuntos, OCR ni transcripciones). Genera alerta y columna **Severity** cuando el puntaje es `>= 4` `[Verificado MS Learn]`. | Triaje acelerado de alta precisión para seguridad psicológica, violencia laboral y evaluación automática de *User-reported messages* `[Verificado MS Learn]`. |
| **Clasificadores de Riesgo en IA Generativa** | `Prompt Shield` (ataques de inyección de prompts / *jailbreak*), `Protected material` (texto con copyright/marca en respuestas IA, solo inglés) | Incluidos para M365 Copilot; facturados a tarifa *Premium* por *Text record* en fuentes IA Pay-As-You-Go `[Verificado MS Learn]`. | Defensa frente a *LLM Jailbreak* (`AML.T0051`/`AML.T0054`), cumplimiento de derechos de autor y gobernanza responsable de IA `[Verificado MS Learn]`. |
| **Clasificadores Visuales e Imágenes** | `Adult images`, `Racy images` + **OCR integrado** (texto impreso y manuscrito) | Exchange y Teams; OCR procesa archivos `.jpg/.jpeg, .png, .bmp, .tiff` entre **100 KB y 4 MB** `[Verificado MS Learn]`. | Detección de contenido explícito y evasión de controles textuales mediante capturas de pantalla o fotografías `[Verificado MS Learn]`. |

### 3.2 Componentes y Motores Clave

| Componente / Motor | Función Operativa Detallada | Ruta en Portal Unificado | Integraciones Clave |
| :--- | :--- | :--- | :--- |
| **Motor de Políticas y Plantillas Inteligentes** | Creación y gestión exclusiva vía UI (*PowerShell no soportado para crear/editar políticas*) con 7 plantillas predefinidas (*Conflict of interest, Copilot interactions, Inappropriate content, Inappropriate images, Inappropriate text, Financial regulatory compliance, Sensitive info types*) y constructor lógico `AND / OR / NOT`. | `purview.microsoft.com > Solutions > Communication Compliance > Policies` | Adaptive Scopes, SITs, Diccionarios de palabras clave (100 KB comprimidos) `[Verificado MS Learn]` |
| **Clasificadores Entrenables y Azure AI Content Safety (LLM)** | 11 clasificadores entrenables provistos por Microsoft (*Corporate sabotage, Customer complaints, Discrimination, Gifts & entertainment, Harassment, Money laundering, Profanity, Regulatory collusion, Stock manipulation, Threat, Unauthorized disclosure*) + 4 clasificadores LLM (*Hate, Sexual, Violence, Self-harm* con severidad >= 4 en >= 5 palabras) + 2 clasificadores GenAI (*Prompt Shield*, *Protected material*) + imágenes *Adult/Racy*. | `purview.microsoft.com > Solutions > Communication Compliance > Policies > Conditions` | Azure AI Content Safety, Purview Data Classification `[Verificado MS Learn]` |
| **Inspector de Adjuntos Modernos, OCR y Sentimiento** | Extracción automática a `.txt` de vínculos OneDrive/SharePoint en Teams, OCR propio sobre imágenes de 100 KB a 4 MB, evaluación de sentimiento (*Positive, Negative, Neutral* hasta 5.120 palabras), detección de patrones repetitivos (>= 2 mensajes en 30 días al mismo destinatario) y traducción automática. | `purview.microsoft.com > Communication Compliance > Policies > [Policy] > Pending` | SharePoint Online, OneDrive, Azure AI Vision / Language `[Verificado MS Learn]` |
| **Supervisión de IA Generativa y Agentes (Copilot & Agent 365)** | Inspección separada de prompts y respuestas en M365 Copilot (`[Copilot]`), Copilot Studio, agentes registrados en **Microsoft Agent 365**, apps IA empresariales conectadas vía Entra/Data Map (`[AI app]`, incl. Claude Enterprise) y apps IA de navegador/red. | `purview.microsoft.com > Communication Compliance > Policies` y `DSPM > AI observability` | Microsoft 365 Copilot, Agent 365, Defender for Cloud Apps, Purview PAYG `[Verificado MS Learn]` |
| **Canal de Mensajes Reportados por Usuarios (User-Reported)** | Política del sistema que recibe reportes voluntarios de mensajes inapropiados enviados por empleados desde Microsoft Teams (activo por defecto en TAC) y conversaciones reportadas en Viva Engage (activación manual). | `purview.microsoft.com > Communication Compliance > Policies > User-reported messages` | Teams Admin Center, Viva Engage Admin Center `[Verificado MS Learn]` |
| **Consola de Investigación, Remediación y Copilot Summary** | Vistas *Source, Plain text, Conversation* (hasta 20 mensajes antes/después en Teams), *Translation, User activity*, resumen contextual con **Copilot in Microsoft Purview** (100–15.000 palabras) y acciones: *Resolve* (*Cross-policy resolution*), *Tag as*, *Notify*, *Escalate*, *Remove message in Teams*, *Power Automate* y *Escalate for investigation*. | `purview.microsoft.com > Communication Compliance > Alerts / Policies > Pending` | Microsoft Security Copilot, Microsoft Teams, Power Automate `[Verificado MS Learn]` |
| **Policy Health (Preview), Preservación y Cuotas de Buzón** | Diagnóstico de advertencias críticas (límite de **100 GB o 1M mensajes** por política con alertas al 80/90/95 %) y recomendaciones (*Filter email blasts* y puntos ciegos de alcance), junto con configuración global/por política de **Policy Match Preservation**. | `purview.microsoft.com > Communication Compliance > Policies > Policy health` y `Settings` | Exchange Online Review Mailboxes, Purview DLM `[Verificado MS Learn]` |
| **Puente Nativo hacia Insider Risk Management y eDiscovery Premium** | Creación automática de política *Insider risk trigger* (>= 5 mensajes riesgosos en 24 h activan alcance IRM), compartición bidireccional de severidad de usuario en pestaña *User activity* y apertura directa de casos en eDiscovery (Premium) con hasta 100 mensajes y custodio autocompletado. | `purview.microsoft.com > Solutions > Insider Risk Management / eDiscovery` | Purview Insider Risk Management, Purview eDiscovery (Premium), Defender XDR `[Verificado MS Learn]` |

### 3.3 Hitos y Transiciones Críticas Verificadas (2024–2027)

- **30 de junio de 2024:** Retiro definitivo de todos los conectores nativos de Veritas en Microsoft Purview; las organizaciones financieras deben operar con conectores nativos de Microsoft 365 o partners vigentes (TeleMessage, 17a-4 LLC, Smarsh, Global Relay) `[Verificado MS Learn]`.
- **Noviembre–diciembre de 2024 (`MC939918`):** Retiro del portal de cumplimiento clásico (`compliance.microsoft.com`); toda operación reside en `purview.microsoft.com` `[Verificado MS Learn]`.
- **1 de junio de 2025:** Entrada en vigor obligatoria de **Policy Match Preservation** (1 mes, 6 meses, 1 año por defecto o 7 años), purgando automáticamente copias en Communication Compliance que excedan la antigüedad seleccionada sin afectar los elementos originales del usuario `[Verificado MS Learn]`.
- **1 de octubre de 2025:** Renombre comercial de *Microsoft 365 E5 Compliance* a **Microsoft Purview Suite** `[Verificado MS Learn]`.
- **1 de mayo de 2026:** Disponibilidad general (GA) de **Microsoft 365 E7** y **Microsoft Agent 365**, habilitando gobierno e inclusión de instancias de agentes autónomos en políticas de Communication Compliance y *DSPM > AI observability* `[Verificado MS Learn]`.
- **Julio de 2026:** Soporte para asignaciones con fecha de vencimiento (*time-bound role assignments*) en grupos de roles nativos del portal de Microsoft Purview `[Verificado MS Learn]`.
- **Agosto de 2026:** Incorporación de **Anthropic Claude (Enterprise)** como aplicación IA empresarial soportada por capacidades de seguridad y cumplimiento de Purview, incluyendo Communication Compliance bajo modelo Pay-As-You-Go `[Verificado MS Learn]`.
- **Octubre de 2026 / 15 de octubre de 2027 (`MC1505599`):** GA de la API `AuditLogQuery` de Microsoft Graph y anuncio del retiro de `Search-UnifiedAuditLog` el 15 de octubre de 2027, impactando los scripts de auditoría de supervisión (`SupervisionPolicyCreated`, `SupervisionRuleMatch`, `SupervisoryReviewTag`) `[Verificado MS Learn]`.

### 3.4 Arquitectura de Integraciones Cruzadas del Ecosistema Microsoft

1. **Microsoft Purview Insider Risk Management (IRM) (`[Verificado MS Learn]`):**
   - **Disparador automático de alcance (*Insider risk trigger*):** Al activar la casilla de Communication Compliance dentro de las plantillas *Data leaks by risky users* o *Security policy violations by risky users* en IRM, Purview crea automáticamente la política dedicada `Insider risk trigger - (date)` (o `Risky user in messages - (date)`) con los clasificadores *Threat, Harassment* y *Discrimination*. Cualquier usuario que envíe **5 o más mensajes riesgosos en 24 horas** entra automáticamente en alcance de vigilancia en IRM (latencia de hasta 48 h).
   - **Indicadores nativos en políticas de datos e IA:** IRM consume señales de Communication Compliance (*Sending financial regulatory text*, *Sending inappropriate images/content*, *Sending specific SITs*) y de aplicaciones GenAI (*Prompt Shields* y *Protected material detection* en la plantilla *Risky AI usage*).
   - **Contexto unificado de severidad:** Si se habilita el uso compartido de datos en IRM, la pestaña **User activity** dentro de Communication Compliance muestra el nivel de severidad IRM del usuario, el conteo de actividades riesgosas/inusuales y un enlace directo *Open in insider risk management*.
2. **Microsoft Purview eDiscovery (Premium) (`[Verificado MS Learn]`):**
   - La acción **Escalate for investigation** transfiere hasta **100 coincidencias multi-canal** (Exchange, Teams, Viva Engage, Copilot, conectores de terceros) hacia un nuevo caso de *eDiscovery (Premium)*, poblando automáticamente al usuario investigado como *Custodian* para colocar retenciones legales (*Legal Hold*), ejecutar búsquedas en colecciones y gestionar conjuntos de revisión (*Review Sets*).
3. **Microsoft Purview Data Security Posture Management (DSPM) y Microsoft Agent 365 (`[Verificado MS Learn]`):**
   - Las políticas creadas desde *DSPM for AI* aparecen en la lista de Communication Compliance con el prefijo `DSPM for AI` (o `AI hub`).
   - En la vista actual **DSPM > AI observability**, las detecciones de comportamiento poco ético (*Unethical behavior*) de instancias registradas en **Microsoft Agent 365** se consolidan junto con señales de sobreexposición (*Oversharing*) y exfiltración para priorizar la remediación por propietario del agente.
4. **Microsoft Purview Data Lifecycle Management (DLM) y Records Management (`[Verificado MS Learn]`):**
   - Communication Compliance solo almacena copias operativas sujetas a **Policy Match Preservation** (`1 month` a `7 years`); la conservación probatoria inmutable del elemento original (incluyendo cumplimiento WORM bajo **SEC Rule 17a-4** actualizado desde enero de 2023 con opción de *audit trail* o *Preservation Lock*) recae en políticas de retención de DLM sobre buzones Exchange, mensajes de Teams e interacciones de Copilot/IA.
5. **Microsoft Purview Information Barriers (IB) (`[Verificado MS Learn]`):**
   - Mientras Information Barriers previene de forma preventiva la comunicación no autorizada entre segmentos con conflicto de interés (soportando modos *Legacy*, segmento único y *multi-segment* con hasta 5.000 segmentos y 10 por usuario, SharePoint/OneDrive, contenedores SharePoint Embedded desde sep-2026 y Planner básico), la plantilla **Detect conflict of interest** de Communication Compliance actúa como control detectivo compensatorio auditando comunicaciones internas entre grupos sensibles.
6. **Microsoft Security Copilot y Microsoft Sentinel / Defender XDR (`[Verificado MS Learn]`):**
   - **Copilot in Microsoft Purview** resume conversaciones complejas (100 a 15.000 palabras) directamente en el panel lateral de investigación registrando las respuestas en el historial de Security Copilot.
   - Los eventos administrativos y de coincidencias (`SupervisionPolicyCreated`, `SupervisionPolicyUpdated`, `SupervisionPolicyDeleted`, `SupervisionRuleMatch`, `SupervisoryReviewTag`) fluyen hacia `OfficeActivity` en **Microsoft Sentinel** y `CloudAppEvents` en **Defender XDR** para detección de manipulación de controles o alertas de volumen anómalo.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Microsoft Purview Communication Compliance impone una barrera arquitectónica estricta: **los administradores globales (*Global Administrators*) y los administradores de cumplimiento (*Compliance Administrators* / *Communication Compliance Admins*) pueden configurar políticas, pero tienen bloqueado el acceso a alertas y al contenido de los mensajes** `[Verificado MS Learn]`. Además, para investigar cualquier coincidencia de una política no basta pertenecer al grupo de roles *Analysts* o *Investigators*: la cuenta debe figurar explícitamente en el campo **Reviewers** de esa política específica y poseer un buzón activo en Exchange Online `[Verificado MS Learn]`.

### 4.1 Matriz Oficial de Grupos de Roles y Segregación de Funciones

| Rol / Grupo de Roles | Plano RBAC | Permisos Clave Habilitados | Restricciones de Segregación | Estrategia PIM / JIT y Asignación Recomendada |
| :--- | :--- | :--- | :--- | :--- |
| **Communication Compliance Admins** | Purview Role Group (`purview.microsoft.com > Settings > Roles and scopes > Role groups`) | Configurar políticas, condiciones, conectores, ajustes globales de privacidad (seudonimización, *Policy Match Preservation*, *Cross-policy resolution*), plantillas de notificación y exportar historial de cambios de políticas. | **No puede** ver alertas, abrir mensajes pendientes/resueltos, ver conversaciones ni ejecutar acciones de remediación `[Verificado MS Learn]`. | Asignación con vencimiento (julio 2026) o elegible vía Entra PIM for Groups (máx. 4 h JIT con MFA resistente a phishing y aprobación) `[Decisión / Propuesta Editorial]`. Mantener >= 2 cuentas nominales para evitar escenario *zero-admin* `[Verificado MS Learn]`. |
| **Communication Compliance Analysts** | Purview Role Group + Campo *Reviewers* de la política | Acceder y clasificar alertas de sus políticas asignadas, ver sentimiento e historial, usar *Summarize* con Copilot, etiquetar (*Tag as*), notificar al usuario (*Notify*), escalar a otro revisor (*Escalate*) y resolver (*Resolve*). | **No puede** crear/editar políticas, **no ve** pestañas *Conversation* ni *Translation*, y **no puede** eliminar mensajes en Teams, descargar elementos ni escalar a eDiscovery `[Verificado MS Learn]`. | Grupo operativo base para revisores de RR. HH., supervisores FINRA Serie 24 o Compliance L1 operando con **seudonimización activa**; membresía acotada trimestralmente `[Decisión / Propuesta Editorial]`. |
| **Communication Compliance Investigators** | Purview Role Group + Campo *Reviewers* de la política | Todos los permisos de *Analysts* más remediación avanzada: ver pestañas **Conversation** y **Translation**, **Remove message in Teams**, **Escalate for investigation** (hacia eDiscovery Premium), descargar mensajes/informes `.zip` y ejecutar flujos **Power Automate**. | **No puede** crear, modificar, pausar ni eliminar políticas ni cambiar ajustes globales de privacidad `[Verificado MS Learn]`. | Asignación restringida a investigadores sénior de Legal, Forense Interno y Relaciones Laborales; activación JIT de 8 h o grupo con revisión mensual de accesos `[Decisión / Propuesta Editorial]`. |
| **Communication Compliance Viewers** | Purview Role Group | Acceder a los widgets e informes agregados del panel **Reports** y ver/exportar actualizaciones de configuración de políticas. | **No puede** acceder a alertas individuales, leer contenido de mensajes ni modificar políticas `[Verificado MS Learn]`. | Asignación para Auditoría Interna, Oficiales de Privacidad (DPO), Riesgo Operacional y Comité de Ética `[Decisión / Propuesta Editorial]`. |
| **Communication Compliance (Grupo Todo-en-Uno)** | Purview Role Group | Combina permisos totales de *Admins*, *Analysts*, *Investigators* y *Viewers*. | Rompe la segregación entre quién define el alcance/privacidad y quién lee comunicaciones privadas `[Verificado MS Learn]`. | **Prohibido en producción empresarial** salvo laboratorios aislados; dejar vacío tras configurar los 4 grupos segregados `[Decisión / Propuesta Editorial]`. |
| **Microsoft Entra Compliance Administrator** | Microsoft Entra ID Role | Habilita la visibilidad inicial de la solución en el portal Purview y otorga permisos equivalentes a *Communication Compliance Admins* para el arranque inicial. | Sin acceso a alertas ni lectura de mensajes a menos que se agregue a *Analysts/Investigators* y como *Reviewer* `[Verificado MS Learn]`. | Elegible en **Microsoft Entra PIM** (máx. 2 h JIT, justificación de ticket y MFA FIDO2/Passkey) `[Decisión / Propuesta Editorial]`. |
| **Security Copilot Contributor** | Microsoft Security Copilot RBAC | Permite a *Analysts* e *Investigators* invocar el botón **Summarize** sobre coincidencias de 100 a 15.000 palabras en Purview. | No concede por sí solo acceso a políticas ni mensajes si el usuario carece del rol de Communication Compliance y asignación de *Reviewer* `[Verificado MS Learn]`. | Asignado únicamente a los grupos de seguridad de *Analysts* e *Investigators* autorizados a consumir SCUs `[Decisión / Propuesta Editorial]`. |
| **Audit Reader / Audit Manager** | Purview Role Group + Graph `AuditLogsQuery.Read.All` | Auditar de forma independiente las operaciones `SupervisionPolicyCreated`, `SupervisionPolicyUpdated`, `SupervisionRuleMatch` y `SupervisoryReviewTag` realizadas por administradores y revisores. | Separado del equipo de revisores para garantizar supervisión cruzada (*watch the watchers*) `[Verificado MS Learn]`. | Asignado al equipo de GRC / Privacidad y SOC L2 independiente de los revisores de contenido `[Decisión / Propuesta Editorial]`. |

### 4.2 Unidades Administrativas Restringidas vs. Adaptive Scopes

Para corporaciones multinacionales sujetas a comités de empresa europeos (ej. *Betriebsrat* alemán) o leyes regionales de protección de datos (GDPR, Ley 21.719 de Chile, LFPDPPP de México), Microsoft Purview permite acotar miembros de *Communication Compliance Admins*, *Analysts* e *Investigators* mediante **Administrative Units (AU)** de Microsoft Entra ID `[Verificado MS Learn]`. Al aplicarlas, dichos usuarios pasan a ser *Restricted Administrators* y solo pueden crear políticas o investigar alertas dentro de su unidad administrativa `[Verificado MS Learn]`.

> **Restricción arquitectónica crítica verificada (`[Verificado MS Learn]`):** En Communication Compliance **no es posible combinar Administrative Units con Adaptive Scopes** simultáneamente. Además, los administradores restringidos por AU **no tienen acceso** al panel global **Reports**, a la configuración global de **Settings** (incluidas plantillas de aviso) ni a la exportación directa de registros de auditoría desde la política. La organización debe decidir arquitectónicamente entre segmentación delegada por AU (grupos estáticos/dinámicos Entra) o segmentación dinámica centralizada por *Adaptive Scopes* `[Decisión / Propuesta Editorial]`.

### 4.3 Matriz Detallada de Acciones de Remediación, Límites Técnicos y Permisos Requeridos

| Acción de Remediación | Descripción Operativa y Comportamiento Técnico | Límites y Reglas Oficiales Verificadas | Rol Mínimo Requerido (+ Reviewer) |
| :--- | :--- | :--- | :--- |
| **Resolve / Cross-policy resolution** | Cierra el ítem moviéndolo de *Pending* a *Resolved*. Permite marcar **Item was misclassified** (solo cuando dispara un *trainable classifier* de Microsoft; no disponible aún para clasificadores LLM Content Safety). | **Cross-policy resolution (preview)** viene activado por defecto: al resolver un mensaje se resuelven automáticamente todas sus copias idénticas en otras políticas del tenant `[Verificado MS Learn]`. | `Communication Compliance Analysts` o `Investigators` `[Verificado MS Learn]` |
| **Unresolve** | Revierte uno o varios mensajes desde la pestaña *Resolved* nuevamente hacia *Pending* para permitir acciones adicionales o re-investigación. | Exige comentario auditable; toda transición queda registrada en *History of remediation actions* `[Verificado MS Learn]`. | `Communication Compliance Analysts` o `Investigators` `[Verificado MS Learn]` |
| **Tag as (Estándar y Custom Tags)** | Clasifica el mensaje como `Compliant`, `Noncompliant` o `Questionable`, o aplica etiquetas personalizadas de flujo interno (ej. `Escalated-Legal`). | Máximo **10 etiquetas personalizadas por política** (3 a 64 caracteres, sin caracteres especiales salvo espacios/guiones). Eliminar una etiqueta la borra retroactivamente de ítems previos `[Verificado MS Learn]`. | `Communication Compliance Analysts` o `Investigators` `[Verificado MS Learn]` |
| **Notify (Aviso al Usuario)** | Envía correo electrónico educativo/correctivo al remitente usando una *Notice template* preconfigurada y resuelve automáticamente la coincidencia. | Las plantillas de aviso las crean únicamente *Communication Compliance Admins* en `Settings > Notice templates` `[Verificado MS Learn]`. | `Communication Compliance Analysts` o `Investigators` `[Verificado MS Learn]` |
| **Escalate (a otro Revisor)** | Solicita revisión secundaria por correo electrónico a otro revisor previamente incluido en la lista de *Reviewers* de la misma política. | Solo muestra destinatarios que ya figuren como *Reviewers* en esa política específica `[Verificado MS Learn]`. | `Communication Compliance Analysts` o `Investigators` `[Verificado MS Learn]` |
| **Remove message in Teams** | Bloquea mensajes inapropiados en chats 1:1, grupales o canales de Teams, sustituyéndolos por un *policy tip* visible para remitente y receptores. | Aplica a detecciones ML/clasificadores y *User-reported messages*. No soportado si el denunciante reportó un mensaje previo a su ingreso al chat `[Verificado MS Learn]`. | **Exclusivo de `Communication Compliance Investigators`** (o grupo total `CC`) `[Verificado MS Learn]` |
| **Escalate for investigation (eDiscovery Premium)** | Crea directamente un nuevo caso en **Microsoft Purview eDiscovery (Premium)** precargando automáticamente al usuario como custodio sin requerir permisos adicionales de eDiscovery para abrirlo. | Hasta **100 mensajes por operación** combinando cualquier canal (ej. 50 Teams + 25 Exchange + 25 Viva Engage). **No resuelve ni etiqueta** automáticamente el mensaje en CC `[Verificado MS Learn]`. | **Exclusivo de `Communication Compliance Investigators`** `[Verificado MS Learn]` |
| **Power Automate** | Dispara un flujo automatizado sobre la coincidencia (incluye plantilla integrada *Notify manager when a user has a Communication Compliance alert*). | Requiere licencia de Power Automate para el ejecutor y gobierno DLP de conectores en Power Platform `[Verificado MS Learn]`. | **Exclusivo de `Communication Compliance Investigators`** `[Verificado MS Learn]` |
| **Download / Export files / Message details report** | Descarga directa de mensajes seleccionados o exportación asíncrona para archivo externo y reportes programados. | `Download` directo: máx. **3 MB** (`.zip`). `Export files`: máx. **3 GB** (`1.000 documentos` o `50.000 usuarios`, adjuntos deben seleccionarse manualmente). `Message details report`: hasta **5 programaciones** por política `[Verificado MS Learn]`. | **Exclusivo de `Communication Compliance Investigators`** `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Triaje Priorizado de Cola de Alertas por Severidad LLM y Sentimiento Negativo
- **Objetivo:** Clasificar las alertas generadas en las últimas 24 horas priorizando coincidencias con `Severity >= 4` de clasificadores LLM (*Hate, Violence, Sexual, Self-harm*) y sentimiento *Negative* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Alerts` y `Policies > [Nombre de Política] > Pending` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Analyst / Investigator (Seguridad Conductual / RR. HH. / Compliance).
- **Procedimiento Paso a Paso:**
  1. Acceder a `Communication Compliance > Alerts` para visualizar los últimos 30 días de alertas agrupadas y ordenadas por severidad.
  2. Abrir cada política con elementos en **New pending today** > 0 y ordenar/filtrar en la pestaña **Pending** por columna **Severity** (valores >= 4 generados por clasificadores LLM) y **Sentiment = Negative**.
  3. Verificar si el mensaje muestra la notificación **Pattern detected** (>= 2 mensajes del mismo remitente al mismo destinatario en 30 días), elevando inmediatamente su prioridad operativa.
  4. Para hilos extensos (entre 100 y 15.000 palabras), seleccionar **Summarize** en el panel de **Copilot in Microsoft Purview** para obtener síntesis contextual respecto al clasificador disparado antes de decidir la acción.
- **Evidencia Auditable:** Registro inmutable `SupervisoryReviewTag` en Purview Audit y reducción verificable del contador **New pending today** dentro del SLA interno (< 24 h para severidad alta) `[Decisión / Propuesta Editorial]`.

### D-02: Supervisión de Prompts Adversarios (Prompt Shields) y Fuga de Datos en IA Generativa
- **Objetivo:** Revisar diariamente coincidencias en interacciones con Microsoft 365 Copilot, Copilot Studio, agentes de Agent 365 y aplicaciones IA conectadas/externas por intentos de *Jailbreak* (*Prompt Shield*), *Protected material* o envío de SITs `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política GenAI / Copilot] > Pending` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Investigator / AI Governance Analyst.
- **Procedimiento Paso a Paso:**
  1. Abrir la política basada en la plantilla *Detect Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions* y políticas que cubran *Enterprise AI apps* (ej. Claude Enterprise) y *Other AI apps*.
  2. Identificar en la columna **Subject** el prefijo `[Copilot]` o `[AI app]` y en **Sender/Recipient** si la infracción provino del prompt del usuario o de la respuesta generada por *Copilot / Connected AI app / Cloud AI app*.
  3. Inspeccionar en la barra amarilla superior si el disparo corresponde a **Prompt Shield** (ataque de inyección/jailbreak), **Protected material** (propiedad intelectual de terceros en la respuesta) o un *Sensitive Information Type* corporativo.
  4. Etiquetar como *Noncompliant*, enviar recordatorio pedagógico mediante **Notify** si fue imprudencia del usuario, o escalar a SOC/IRM si evidencia recolección maliciosa o *Prompt Injection* deliberado.
- **Evidencia Auditable:** Historial de remediación del ítem (`View item history`) con comentario técnico y correlación con eventos `CopilotInteraction` (`JailbreakDetected`) en Purview Audit `[Verificado MS Learn]`.

### D-03: Atención y Contención Rápida de Mensajes Reportados por Usuarios en Teams y Viva Engage
- **Objetivo:** Procesar reportes voluntarios enviados por empleados mediante *Report inappropriate content* en Teams y *Report conversation* en Viva Engage, ejecutando remoción inmediata de mensajes tóxicos o abusivos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > User-reported messages > Pending` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Investigator (Relaciones Laborales / Ética).
- **Procedimiento Paso a Paso:**
  1. Ingresar a la política del sistema **User-reported messages** (validando previamente que los revisores sean personal autorizado de RR. HH./Ética y no Global Admins predeterminados).
  2. Revisar la evaluación automática de clasificadores Azure AI Content Safety (*Hate, Self-harm, Sexual, Violence*) y abrir la pestaña **Conversation** (exclusiva de *Investigators*) para inspeccionar hasta 20 mensajes previos y posteriores de contexto.
  3. Si se confirma acoso, amenaza, auto-lesión o difusión de contenido explícito en Teams, ejecutar **Remove message in Teams** para bloquear la visualización del mensaje en el chat/canal y mostrar el *policy tip* institucional.
  4. Etiquetar como *Noncompliant* y documentar el folio del expediente laboral antes de pulsar **Resolve** (recordando que si el mensaje fue enviado antes de que el denunciante entrara al chat, la remoción en Teams no está soportada).
- **Evidencia Auditable:** Traza en `View item history` de la acción `Remove message in Teams` y sustitución verificada del mensaje en el cliente de Teams `[Verificado MS Learn]`.

### D-04: Muestreo Diario de Supervisión Regulatoria Financiera (SEC / FINRA / MiFID II)
- **Objetivo:** Completar la cuota diaria de revisión supervisada (ej. 10 % aleatorio o 100 % dirigido) sobre operadores regulados (*broker-dealers*, banca de inversión) en Exchange, Teams y conectores de terceros (Instant Bloomberg, Zoom, WhatsApp) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política Regulatoria] > Pending` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Analyst / Supervisor Regulatorio (ej. FINRA Series 24).
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola **Pending** por **Item class** (correo, Teams, transcripciones de reuniones, Bloomberg/WhatsApp) y por clasificadores regulatorios (*Stock manipulation, Regulatory collusion, Money laundering, Gifts & entertainment, Unauthorized disclosure, Customer complaints*).
  2. Para transcripciones de reuniones de Teams, revisar la pestaña **Source** y **Plain text** verificando las marcas de tiempo (30 segundos antes y después de la frase marcada) y el audio/grabación si procede de salas compartidas.
  3. Usar la pestaña **Translation** cuando existan comunicaciones multilingües entre mesas globales de negociación.
  4. Clasificar cada elemento con **Tag as** (*Compliant*, *Questionable* o *Noncompliant*) dejando nota obligatoria de supervisión regulatoria y ejecutar **Resolve**.
- **Evidencia Auditable:** Reporte exportable *Items and actions per policy* y *Message details report* demostrando supervisión efectiva ante inspecciones SEC Rule 17a-4 y FINRA Rule 3110 `[Verificado MS Learn]`.

### D-05: Inspección de Adjuntos Modernos Extraídos, Imágenes OCR y Coincidencias Ocultas
- **Objetivo:** Evitar falsos negativos y cierres erróneos revisando archivos vinculados de OneDrive/SharePoint (`.txt` extraídos), capturas de pantalla escaneadas por OCR y metadatos ocultos (HTML/Base64) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política] > Pending > Attachments / Source / Plain text` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Investigator.
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola **Pending** con **Has attachment = Yes** o **File class = attachment**.
  2. Revisar los elementos hijos `.txt` generados por *Modern attachments* de Teams (ej. `PlanEstrategico.docx.txt`) y los elementos hijos de imágenes (`.jpg, .png, .bmp, .tiff` de 100 KB–4 MB) detectados por OCR impreso o manuscrito.
  3. Si un mensaje no muestra resaltado evidente en *Plain text*, aplicar el protocolo de **Hidden matches**: descargar el mensaje (`.zip` < 3 MB) e inspeccionar en texto plano el archivo `.eml` buscando enlaces HTML, atributos `alt` de imágenes, cadenas Base64 o nombres de adjuntos.
  4. Tomar acción de remediación sobre el mensaje padre y sus adjuntos asociados.
- **Evidencia Auditable:** Registro de decisión sobre elementos padre e hijos en el historial de la política `[Verificado MS Learn]`.

### D-06: Verificación de Continuidad de Escaneo Horario (`Messages scanned today` y `Last policy scan`)
- **Objetivo:** Confirmar que todas las políticas activas mantienen su ciclo de evaluación horario y que los conectores de terceros e IA están entregando telemetría sin estancamientos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Revisar en la tabla principal de **Policies** las columnas **Status** (`Active`), **Last policy scan** (debe reflejar ejecución dentro de la última hora UTC) y **Messages scanned today**.
  2. Identificar políticas activas cuyo contador **Messages scanned today** permanezca en `0` de forma anómala durante horas laborales (síntoma de alcance vacío, licencia faltante, Viva Engage fuera de *Native Mode* o caída de conector de terceros).
  3. Verificar que ninguna política se encuentre bloqueada en estados transitorios **Error in pausing**, **Error in resuming** o **Deactivated** por límite de cuota.
- **Evidencia Auditable:** Captura o exportación diaria de *Policy settings and status* (`CSV`) sin políticas degradadas `[Verificado MS Learn]`.

### D-07: Correlación Diaria de Perfil de Riesgo Cruzado en la Pestaña `User activity` (CC + IRM)
- **Objetivo:** Evaluar si los usuarios con coincidencias conductuales o de IA presentan simultáneamente actividades inusuales de exfiltración en Insider Risk Management `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política] > Pending > [Mensaje] > User activity` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Investigator / Insider Risk Investigator.
- **Procedimiento Paso a Paso:**
  1. Para toda coincidencia etiquetada como *Questionable* o *Noncompliant*, abrir la pestaña **User activity** del mensaje.
  2. Revisar el nivel **Insider risk severity** compartido desde IRM, el conteo de *Policy matches / Remediation actions* de los últimos 30 días y el conteo de *Risk activities / Unusual activities* de IRM.
  3. Si el usuario combina lenguaje amenazante/sabotaje o *Jailbreak* en IA con descargas inusuales en SharePoint/OneDrive, seleccionar **Open in insider risk management** (con rol autorizado) o escalar conjuntamente al comité de Insider Threat.
- **Evidencia Auditable:** Nota de correlación documentada en el comentario de etiquetado/escalamiento del caso `[Decisión / Propuesta Editorial]`.

### D-08: Revisión de Salud de Agentes IA en `DSPM > AI observability` y Coincidencias de Agent 365
- **Objetivo:** Supervisar diariamente el comportamiento comunicacional de agentes autónomos registrados en Microsoft Agent 365 y Copilot Studio para detectar respuestas poco éticas o exposición indebida `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > DSPM > AI observability` y `Communication Compliance > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** AI Governance Lead / Communication Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Ingresar a **DSPM > AI observability** (versión actual de DSPM, no *classic*) y revisar los agentes con actividad en los últimos 30 días ordenados por nivel de riesgo de IRM y categoría *Unethical behavior*.
  2. Verificar que toda nueva instancia de agente productivo en **Agent 365** haya sido incorporada en el alcance de las políticas correspondientes de Communication Compliance (tratada como usuario).
  3. Si un agente genera coincidencias *Noncompliant* en interacciones agente-a-humano en Teams o correo, notificar de inmediato al **Agent Owner** registrado en Entra ID para ajustar instrucciones del sistema o pausar el agente.
- **Evidencia Auditable:** Inventario de instancias de agentes cubiertos por políticas de supervisión y ticket de remediación al propietario del agente `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Gobernanza de `Policy Health` (Preview), Reducción de Falsos Positivos y Puntos Ciegos
- **Objetivo:** Atender advertencias de almacenamiento y aplicar recomendaciones semanales de optimización (*Filter email blasts* y *Reduce user scoping blind spots*) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > Policy health` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Revisar los contadores superiores de **Warnings** y **Recommendations** en la página **Policies**.
  2. Abrir cada recomendación de *Potentially reduce false positives by filtering out bulk emails* y habilitar **Filter email blasts** para suprimir boletines, newsletters y envíos masivos, validando los remitentes filtrados en el reporte **Email blast senders**.
  3. Evaluar las recomendaciones de *Reduce user scoping blind spots* (usuarios fuera del alcance estático que cumplen las condiciones de la política) y decidir con Legal/RR. HH. su incorporación al alcance o a un *Adaptive Scope*.
- **Evidencia Auditable:** Exportación semanal de `Export policy updates` y reporte *Email blast senders* en `.csv` `[Verificado MS Learn]`.

### S-02: Retroalimentación de Clasificadores Entrenables y Depuración de Diccionarios Personalizados
- **Objetivo:** Analizar elementos marcados como *Item was misclassified* durante la semana para ajustar condiciones booleanas `AND / OR / NOT`, umbrales de SITs y diccionarios de palabras clave `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política] > Resolved` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin + Lead Analyst (en sesión conjunta sin exposición de PII al Admin).
- **Procedimiento Paso a Paso:**
  1. Filtrar la pestaña **Resolved** y exportar estadísticas agregadas desde `Reports > Items and actions per policy` para medir la tasa de falsos positivos por política.
  2. Para clasificadores entrenables de Microsoft con ruido recurrente, confirmar que los analistas usen *Resolve > Item was misclassified* (enviando muestra a Microsoft solo cuando la política de privacidad corporativa lo autorice; recordar que aún no aplica a clasificadores LLM Content Safety).
  3. Refinar en el **Condition builder** grupos anidados `NOT` (excepciones de dominios de proveedores, firmas legales o disclaimers corporativos) y actualizar diccionarios personalizados cuidando no superar el límite de **100 KB post-compresión** por tenant.
- **Evidencia Auditable:** Registro `SupervisionPolicyUpdated` en el log de auditoría y disminución porcentual de falsos positivos en la semana siguiente `[Verificado MS Learn]`.

### S-03: Monitoreo Preventivo de Cuota de Buzones de Supervisión (100 GB / 1 Millón de Mensajes)
- **Objetivo:** Verificar por PowerShell el tamaño e ítems de cada *Review Mailbox* de política antes de alcanzar los umbrales del 80 %, 90 % o 95 % que provocan la desactivación automática al 100 % `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-SupervisoryReviewPolicyV2` y `Get-MailboxStatistics`) `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin / Exchange Online Admin.
- **Procedimiento Paso a Paso:**
  1. Conectarse a Exchange Online PowerShell con permisos de lectura administrativa y ejecutar el script oficial de inspección de `ReviewMailbox` para listar `ItemCount` y `TotalItemSize` de todas las políticas.
  2. Identificar cualquier política que supere **70 GB** o **700.000 mensajes** (especialmente políticas de revisión al 100 % sobre interacciones GenAI).
  3. Si una política se acerca al 80–90 %, ejecutar preventivamente **Copy policy** con nuevo nombre para garantizar continuidad ininterrumpida de captura, y **pausar/desactivar sin eliminar** la política anterior mientras deban preservarse sus mensajes históricos.
- **Evidencia Auditable:** Salida semanal del comando `Get-MailboxStatistics` archivada en repositorio GRC con umbrales bajo el 80 % `[Verificado MS Learn]`.

### S-04: Conciliación de Casos Escalados a eDiscovery (Premium) e Indicadores de Insider Risk
- **Objetivo:** Asegurar que todos los elementos escalados durante la semana (*Escalate for investigation* y triggers hacia IRM) tengan custodio asignado, retención legal (*hold*) o cierre documentado `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Reports > Escalations by policy` y `Solutions > eDiscovery > Cases` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Investigator + eDiscovery Manager.
- **Procedimiento Paso a Paso:**
  1. Revisar el widget **Escalations by policy** y el informe detallado **Items and actions per policy** (columna *Case created* y *Escalated items*).
  2. Confirmar que cada caso creado en **eDiscovery (Premium)** haya recibido correctamente el paquete de mensajes (hasta 100 mensajes por acción) y que los mensajes originales en la cola de Communication Compliance reciban la etiqueta personalizada `Escalated` y su resolución correspondiente (ya que crear el caso no resuelve ni etiqueta automáticamente el mensaje en CC).
  3. Validar que la política automática *Insider risk trigger* esté enviando señales correctamente a las políticas *Data leaks by risky users* en IRM.
- **Evidencia Auditable:** Tabla de trazabilidad cruzada `Match ID (CC) <-> Case ID (eDiscovery Premium)` `[Verificado MS Learn]`.

### S-05: Control FinOps del Consumo Pay-As-You-Go de Registros de Texto en IA y Fuentes No-M365
- **Objetivo:** Auditar el volumen semanal de *Text records* (unidades de 1.000 caracteres) facturados en Azure por supervisión de apps IA no-M365, Copilot Studio y conectores externos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > Cost Management + Billing` y `https://purview.microsoft.com > Settings > Account and billing` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin + FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Consultar en Azure Cost Management los medidores de facturación de Microsoft Purview Communication Compliance (*Standard* vs. *Premium text records*).
  2. Contrastar el consumo con el porcentaje de revisión (**Review percentage**) de las políticas que incluyen *Enterprise AI apps* y *Other AI apps* (recordando que una política exploratoria al 100 % sin condiciones multiplica tanto el costo PAYG como el llenado del límite de 1M de mensajes).
  3. Ajustar porcentajes de muestreo o acotar condiciones a clasificadores específicos (*Prompt Shields, Protected material*, SITs críticos) una vez concluida la fase de descubrimiento inicial.
- **Evidencia Auditable:** Reporte semanal FinOps de consumo de *Text records* vs. presupuesto mensual aprobado `[Decisión / Propuesta Editorial]`.

### S-06: Auditoría de Envejecimiento de Cola Pendiente (`Pending for (days)`) y Balanceo de Revisores
- **Objetivo:** Detectar cuellos de botella operativos donde coincidencias pendientes superen los 5 días hábiles sin revisión `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Policies > [Política] > Export report` `[Verificado MS Learn]`.
- **Rol Responsable:** Compliance Manager / Communication Compliance Viewer.
- **Procedimiento Paso a Paso:**
  1. Revisar las exportaciones programadas semanales del **Message details report** (máximo 5 programaciones recurrentes por política) e inspeccionar la columna **Pending for (days)** para cada ítem con `Item Status = Pending`.
  2. Identificar revisores ausentes o sobrecargados y reasignar elementos mediante **Escalate** o incorporar revisores suplentes autorizados en la configuración de la política.
- **Evidencia Auditable:** Archivo `.csv` de *Message details report* con el 100 % de ítems dentro del umbral máximo de antigüedad permitido `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Auditoría Independiente de Privacidad sobre Acciones de Revisores y Administradores ("Watch the Watchers")
- **Objetivo:** Auditar todas las operaciones ejecutadas por *Admins*, *Analysts* e *Investigators* en Communication Compliance para detectar accesos indebidos, des-seudonimización no autorizada o modificaciones de políticas sin control de cambios `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` (o API Microsoft Graph `security/auditLog/queries`) y `Communication Compliance > Policies > Export policy updates / Export review activities` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Protection Officer (DPO) / Internal Audit (`Audit Reader`).
- **Procedimiento Paso a Paso:**
  1. Ejecutar una consulta asíncrona en Purview Audit o Microsoft Graph `AuditLogQuery` filtrando por `RecordType = ComplianceSupervisionExchange`, `Discovery` y `AeD`, y operaciones `SupervisionPolicyCreated`, `SupervisionPolicyUpdated`, `SupervisionPolicyDeleted` y `SupervisoryReviewTag`.
  2. Descargar desde cada política crítica los reportes **Export policy updates** y **Export review activities** (`.csv`).
  3. Cotejar cada cambio de política, descarga de mensajes `.zip` o cambio en el ajuste de privacidad de nombres de usuario contra tickets aprobados por Legal/Privacidad.
- **Evidencia Auditable:** Informe mensual de auditoría de privacidad firmado por el DPO sin desviaciones no justificadas `[Verificado MS Learn]`.

### M-02: Certificación Mensual de Membresías RBAC, Revisores de `User-reported messages` y Vencimientos
- **Objetivo:** Garantizar mínimo privilegio verificando los miembros de los 5 grupos de roles de Communication Compliance, fechas de expiración y revisores por política `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and scopes > Role groups` y `Communication Compliance > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin + Identity Governance Admin.
- **Procedimiento Paso a Paso:**
  1. Verificar que el grupo monolítico *Communication Compliance* permanezca vacío (0 miembros) y que existan al menos 2 miembros nominales en *Communication Compliance Admins* para prevenir escenarios *zero-admin*.
  2. Revisar las asignaciones con vencimiento (habilitadas en Purview en julio de 2026) y revocar cuentas de revisores que cambiaron de puesto.
  3. Auditar específicamente la política **User-reported messages** para asegurar que ningún *Global Administrator* figure como revisor residual tras la provisión inicial del tenant.
- **Evidencia Auditable:** Matriz mensual de recertificación RBAC y exportación *Policy settings and status* `[Verificado MS Learn]`.

### M-03: Análisis Ejecutivo de Tendencias de Riesgo Conductual, SITs por Ubicación y Uso de IA
- **Objetivo:** Presentar al Comité de Cumplimiento, RR. HH. y CISO la evolución mensual de incidentes por canal (Exchange, Teams, Viva Engage, Copilot/IA, terceros) y tipos de información sensible expuestos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Communication Compliance > Reports` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Viewer / Chief Compliance Officer.
- **Procedimiento Paso a Paso:**
  1. Exportar a `.csv` (hasta 3 MB por reporte) los informes detallados **Items and actions per location**, **Items and actions per policy** y **Sensitive information type per location (preview)** filtrando por el mes calendario UTC (`00:00:00` a `23:59:59`).
  2. Analizar el desglose de SITs detectados en *Email*, *Teams*, *Microsoft 365 Copilot and Microsoft 365 Copilot Chat*, *Viva Engage* y *Third-party sources*.
  3. Identificar departamentos o canales con incremento en notificaciones (*User notified*) o casos creados (*Case created*) para focalizar campañas de concientización o controles preventivos DLP.
- **Evidencia Auditable:** Paquete mensual de reportes `.csv` y acta del Comité de Ética y Seguridad de Datos `[Verificado MS Learn]`.

### M-04: Validación de Conectores de Terceros, Modo Nativo de Viva Engage y Transcripciones de Teams
- **Objetivo:** Comprobar la integridad de punta a punta de la ingesta de fuentes reguladas no-Microsoft (Bloomberg, Slack, Zoom, WhatsApp) y dependencias de carga M365 `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Data connectors` y `https://admin.teams.microsoft.com > Meetings > Meeting policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin + Messaging/Collaboration Admin.
- **Procedimiento Paso a Paso:**
  1. Verificar el estado saludable de sincronización de todos los **Data connectors** en Purview y confirmar que mensajes sintéticos de prueba en canales regulados generen coincidencias dentro de la ventana esperada de 24–48 horas.
  2. Validar que ninguna política de reuniones en Teams haya deshabilitado accidentalmente **Transcription** para poblaciones sujetas a supervisión de voz/reuniones.
  3. Verificar en Viva Engage Admin Center que **Native Mode** y **Report Conversations** sigan activos y enrutando reportes hacia Communication Compliance.
- **Evidencia Auditable:** Bitácora mensual de pruebas sintéticas (*Proof of Life*) por canal monitoreado `[Decisión / Propuesta Editorial]`.

### M-05: Revisión de Cobertura de `Adaptive Scopes` vs. Límites de Canales Públicos de Teams
- **Objetivo:** Verificar que las consultas dinámicas de atributos de usuario/grupo en *Adaptive Scopes* incluyan correctamente nuevas contrataciones y cambios de rol sin infringir límites conocidos de canales `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and scopes > Adaptive scopes` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Revisar la membresía resuelta de cada *Adaptive Scope* empleado por políticas regulatorias o de alto riesgo (ej. `Department -eq 'Investment Banking'`).
  2. Verificar el límite técnico documentado: **los canales públicos de Teams no tienen cobertura bajo Adaptive Scopes de usuarios** y soportan un máximo de **250 usuarios** en alcances estáticos; para comunidades públicas críticas, asegurar cobertura complementaria mediante alcance explícito de canales o políticas estáticas segmentadas.
- **Evidencia Auditable:** Inventario validado de *Adaptive Scopes* y matriz de cobertura de canales públicos de Teams `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Revisión Legal de `Policy Match Preservation` y Alineación con Data Lifecycle Management
- **Objetivo:** Auditar trimestralmente la configuración global y por política de **Policy Match Preservation** (`1 month`, `6 months`, `1 year` o `7 years`) frente a mandatos regulatorios (SEC 17a-4, FINRA, legislación laboral local) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Communication Compliance > Policy Match Preservation` y `Solutions > Data Lifecycle Management` `[Verificado MS Learn]`.
- **Rol Responsable:** Legal & Regulatory Counsel + Communication Compliance Admin.
- **Procedimiento Paso a Paso:**
  1. Verificar el valor global de **Policy Match Preservation** (por defecto `1 year`) y las excepciones por política personalizada (ej. `7 years` para supervisión financiera regulada, o `6 months` para políticas conductuales donde leyes europeas/latinoamericanas exigen minimización de datos).
  2. Confirmar que los mensajes originales en buzones, Teams y Copilot estén respaldados en paralelo por políticas inmutables (*Preservation Lock* cuando aplique) en **Data Lifecycle Management**, recordando que Communication Compliance solo conserva copias operativas de las coincidencias.
- **Evidencia Auditable:** Dictamen trimestral de retención y preservación firmado por Legal y Cumplimiento `[Verificado MS Learn]`.

### T-02 (Trimestral): Calibración de Plantillas de Notificación (`Notice Templates`), Etiquetas y Flujos Power Automate
- **Objetivo:** Actualizar el tono legal, enlaces a políticas internas e idiomas de las plantillas de advertencia (*Notify*), etiquetas personalizadas (máx. 10 por política) y flujos automatizados de escalamiento `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Communication Compliance > Notice templates` y `make.powerautomate.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Communication Compliance Admin + RR. HH. / Ética Corporativa.
- **Procedimiento Paso a Paso:**
  1. Revisar la efectividad pedagógica de las plantillas de aviso enviadas mediante **Notify** (midiendo la tasa de reincidencia de usuarios notificados en la pestaña *User history*).
  2. Homologar la taxonomía de hasta 10 etiquetas personalizadas (*Custom tags*) entre políticas activas sin eliminar etiquetas históricas en uso (pues borrar una etiqueta la remueve retroactivamente de todos los elementos previos).
  3. Auditar las conexiones y credenciales de los flujos **Power Automate** vinculados a remediación para garantizar que no expongan contenido confidencial fuera del perímetro autorizado.
- **Evidencia Auditable:** Catálogo versionado de plantillas de notificación y flujos Power Automate aprobados `[Verificado MS Learn]`.

### SM-01 (Semestral): Ejercicio *Tabletop* Integrado de Amenaza Interna, Acoso y Exfiltración vía IA
- **Objetivo:** Validar en simulacro práctico de extremo a extremo la coordinación entre Communication Compliance, Insider Risk Management, SOC (Defender XDR/Sentinel), Legal (eDiscovery Premium) y RR. HH. `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` (`Communication Compliance`, `Insider Risk Management`, `eDiscovery`) `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + Chief Compliance Officer + General Counsel + HR Director.
- **Procedimiento Paso a Paso:**
  1. Ejecutar en cuentas de prueba autorizadas un escenario encadenado: envío de >= 5 mensajes con lenguaje amenazante/sabotaje en 24 h (activando *Insider risk trigger*), intento de *Prompt Injection / Jailbreak* en Copilot y compartición de documento confidencial en Teams con captura OCR.
  2. Medir tiempos reales de detección (1 h en texto/Copilot, <= 24–48 h en OCR/IRM trigger), uso de **Remove message in Teams**, correlación en **User activity** y ejecución de **Escalate for investigation** hacia eDiscovery Premium.
  3. Documentar brechas de SLA, permisos faltantes y mejoras al playbook conjunto.
- **Evidencia Auditable:** Informe de resultados del ejercicio semestral con tiempos medidos y plan de acción correctivo `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Evaluación Integral de Impacto en Privacidad (DPIA / PIA), Comités Laborales y Marco Normativo IA
- **Objetivo:** Renovar la legitimación jurídica y ética del programa de supervisión de comunicaciones humanas y agénticas frente a regulaciones internacionales (GDPR, EU AI Act, Ley 21.719 de Chile vigente desde dic-2026, LFPDPPP México, FINRA Rule 3110) `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Compliance Manager` y `Settings > Communication Compliance` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Protection Officer (DPO) + Chief Compliance Officer + CISO.
- **Procedimiento Paso a Paso:**
  1. Auditar la adherencia anual a los cuatro pilares de privacidad de Microsoft Purview: **Pseudonymization** activa por defecto, **RBAC** de mínimo privilegio, **Admin explicit opt-in** documentado por política e integridad de **Audit logs**.
  2. Actualizar las evaluaciones regulatorias de IA (*Assessments for AI regulations*) en **Purview Compliance Manager**, cubriendo Microsoft 365 Copilot, Agent 365 y LLMs empresariales conectados.
  3. Renovar la atestación anual escrita de todos los revisores y las notificaciones de transparencia en el Código de Conducta y políticas de Uso Aceptable de TI/IA de los empleados.
- **Evidencia Auditable:** DPIA anual firmado, registro de atestación de revisores y puntaje actualizado en Compliance Manager `[Verificado MS Learn]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Respuesta de Emergencia ante Amenaza de Violencia, Autolesión o Acoso Severo en Tiempo Real
- **Disparador:** Alerta con `Severity >= 4` en clasificadores LLM *Violence* o *Self-harm*, clasificador *Threat*, o reporte urgente en *User-reported messages* `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Communication Compliance > Policies > [Política] > Pending` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Un *Communication Compliance Investigator* autorizado abre inmediatamente el mensaje, revisa el contexto conversacional (**Conversation** tab, hasta 20 mensajes antes/después) y verifica si existe bandera **Pattern detected**.
  2. Solicita autorización urgente de Legal/RR. HH. para revelar temporalmente la identidad real del usuario si la política opera bajo seudonimización, dejando trazabilidad en el ticket de emergencia.
  3. Ejecuta **Remove message in Teams** si el contenido permanece expuesto en un canal o chat grupal causando daño continuo.
  4. Activa el protocolo corporativo de seguridad física / bienestar laboral con RR. HH. y Seguridad Corporativa, y ejecuta **Escalate for investigation** hacia **eDiscovery (Premium)** seleccionando los mensajes probatorios (máx. 100 por lote) para preservación legal.
- **Evidencia Auditable:** Paquete exportado (`.zip`), caso activo en eDiscovery Premium y registro auditado de remediación `[Verificado MS Learn]`.

### AH-02: Contención e Investigación de *Prompt Injection / Jailbreak* o Exfiltración de IP en Agentes IA / Copilot
- **Disparador:** Detección de clasificador **Prompt Shield** o **Sensitive Information Type** crítico en ubicaciones *Microsoft Copilot experiences*, *Enterprise AI apps* (ej. Claude Enterprise) o instancia de **Microsoft Agent 365** `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Communication Compliance > Policies > Pending`, `DSPM > AI observability` y `Solutions > Audit` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Examinar tanto el elemento del **Prompt** como el de la **Response** en la cola **Pending** para confirmar si el intento de *Jailbreak* logró evadir las salvaguardas del modelo o extraer información restringida.
  2. Consultar en la pestaña **User activity** la severidad del usuario en Insider Risk Management y cruzar en Purview Audit el evento `CopilotInteraction` / `ConnectedAIAppInteraction` para identificar `AccessedResources`, `SensitivityLabelId` y `XPIADetected`.
  3. Si involucra una instancia autónoma de **Agent 365** o Copilot Studio comportándose de forma anómala, coordinar con el propietario del agente y Entra Admin la suspensión temporal del agente en Entra ID / Copilot Studio.
  4. Escalar evidencia a SOC L2/L3 y abrir caso en IRM / eDiscovery Premium si se confirma intención maliciosa.
- **Evidencia Auditable:** Copia preservada del par prompt-respuesta, log `CopilotInteraction` asociado y ticket de incidente SOC `[Verificado MS Learn]`.

### AH-03: Mitigación Inmediata de Política al 90–95 % o Desactivada por Límite de Almacenamiento (100 GB / 1M Mensajes)
- **Disparador:** Notificación automática por correo al alcanzar el 80 %, 90 % o 95 % de la cuota (100 GB o 1.000.000 de mensajes) o alerta crítica en **Policy Health** `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Communication Compliance > Policies` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Seleccionar la política afectada y ejecutar inmediatamente **Copy policy**, asignando un nombre versionado (ej. `FINRA-Supervision-v2-2026Q4`) y optimizando sus condiciones o segmentando la población en dos políticas paralelas.
  2. Verificar que la nueva política entre en estado **Active** y comience a registrar escaneos horarios (`Last policy scan`).
  3. Pausar (**Pause policy**) la política original si aún no llegó al 100 %, o mantenerla en estado **Deactivated** **sin ejecutar Delete** hasta que concluya el ciclo completo de revisión y exportación regulatoria (`Export files` de hasta 3 GB / 1.000 documentos o 50.000 usuarios), evitando pérdida destructiva de evidencia.
- **Evidencia Auditable:** Nueva política activa verificada en `Export policy updates` y respaldo externo `.zip` de la política predecesora `[Verificado MS Learn]`.

### AH-04: Incorporación Urgente de Nueva Aplicación GenAI Empresarial o Conector de Mensajería Externa
- **Disparador:** Despliegue corporativo de un nuevo asistente GenAI (ej. Anthropic Claude Enterprise, nuevo agente en Agent 365) o requerimiento regulatorio sobre nuevo canal de mensajería (WhatsApp / Zoom / Slack) `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Settings > Account and billing`, `Data connectors` y `Communication Compliance > Policies` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Validar que la suscripción Azure de **Pay-As-You-Go** esté activa antes de habilitar ubicaciones IA no-M365, estimando el volumen de *Text records* (1.000 caracteres/registro).
  2. Configurar el registro en Microsoft Entra / conector de Data Map o conector de terceros y esperar la recepción de los primeros ítems de prueba en buzones.
  3. Editar las políticas existentes de Communication Compliance (`Choose locations to detect communications`) marcando **Enterprise AI apps**, **Other AI apps**, la instancia de **Agent 365** o la fuente en **Third-Party Sources**, aplicando inicialmente muestreo controlado y alerta de presupuesto en Azure.
- **Evidencia Auditable:** Coincidencia sintética verificada en la cola **Pending** y alerta de presupuesto FinOps activa `[Verificado MS Learn]`.

### AH-05: Reapertura Auditable de Coincidencias Resueltas por Error (`Unresolve`) ante Requerimiento Legal
- **Disparador:** Auditoría regulatoria o hallazgo posterior que exige re-investigar, re-etiquetar o escalar a eDiscovery mensajes previamente cerrados en la pestaña **Resolved** `[Verificado MS Learn]`.
- **Consola y Ruta:** `purview.microsoft.com > Communication Compliance > Policies > [Política] > Resolved` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Localizar los mensajes requeridos en la pestaña **Resolved** empleando filtros avanzados (**Date** en UTC, **Sender**, **Tags**, **Classifiers**).
  2. Seleccionar los elementos y pulsar **Unresolve** en la barra de comandos, registrando obligatoriamente en **Comment** el número de oficio legal o auditoría que motiva la reapertura.
  3. Pasar a la pestaña **Pending**, verificar el retorno de los mensajes y ejecutar **Escalate for investigation** o exportación formal.
- **Evidencia Auditable:** Traza completa de `Resolve -> Unresolve -> Escalate` en el panel **History of remediation actions** `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, Microsoft Graph y PowerShell

#### Consulta 1: Auditoría de Creación, Modificación y Eliminación de Políticas de Supervisión (Microsoft Sentinel — KQL)
Monitorea en tiempo cuasi-real quién crea, altera o elimina políticas de Communication Compliance (prevención de sabotaje de controles de supervisión) `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Sentinel / Defender Unified SecOps (Tabla: OfficeActivity o CloudAppEvents)
OfficeActivity
| where TimeGenerated > ago(30d)
| where Operation in ("SupervisionPolicyCreated", "SupervisionPolicyUpdated", "SupervisionPolicyDeleted")
| extend AuditDetails = parse_json(AuditData)
| project TimeGenerated, UserId, Operation, PolicyName = tostring(AuditDetails.PolicyName), ClientIP, ResultStatus
| sort by TimeGenerated desc
```

#### Consulta 2: Auditoría de Acciones de Revisión y Etiquetado por Investigadores ("Watch the Watchers" — Microsoft Graph AuditLogQuery v1.0)
Utiliza la API oficial en GA `security/auditLog/queries` (reemplazo recomendado de `Search-UnifiedAuditLog` antes del 15-oct-2027 según `MC1505599`) para auditar toda acción de revisión `[Verificado MS Learn]`.
```powershell
# Plataforma: Microsoft Graph PowerShell SDK (Permiso: AuditLogsQuery.Read.All)
Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "AuditLogsQuery.Read.All"

$params = @{
    "@odata.type"       = "#microsoft.graph.security.auditLogQuery"
    displayName         = "Auditoria-Mensual-Revisores-CC"
    filterStartDateTime = (Get-Date).AddDays(-30).ToUniversalTime().ToString("o")
    filterEndDateTime   = (Get-Date).ToUniversalTime().ToString("o")
    recordTypeFilters   = @("aeD", "discovery", "complianceSupervisionExchange")
    operationFilters    = @("SupervisoryReviewTag", "SupervisionPolicyCreated", "SupervisionPolicyUpdated", "SupervisionPolicyDeleted")
}
$query = Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries" -Body ($params | ConvertTo-Json -Depth 5)
Write-Output "AuditLogQuery ID creado: $($query.id) - Estado inicial: $($query.status)"
```

#### Consulta 3: Verificación Preventiva de Cuota de Almacenamiento de Buzones de Supervisión (Exchange Online PowerShell)
Inspecciona el tamaño e ítems de cada buzón oculto de política (`ReviewMailbox`) frente al límite duro de **100 GB o 1.000.000 de mensajes** `[Verificado MS Learn]`.
```powershell
# Plataforma: Exchange Online PowerShell (Get-SupervisoryReviewPolicyV2 + Get-MailboxStatistics)
Connect-ExchangeOnline -ShowBanner:$false
$policies = Get-SupervisoryReviewPolicyV2 | Sort-Object Name
foreach ($p in $policies) {
    $stats = Get-MailboxStatistics -Identity $p.ReviewMailbox -ErrorAction SilentlyContinue
    [PSCustomObject]@{
        PolicyName    = $p.Name
        Enabled       = $p.Enabled
        ReviewMailbox = $p.ReviewMailbox
        ItemCount     = $stats.ItemCount
        PctItemsLimit = [math]::Round(($stats.ItemCount / 1000000) * 100, 2)
        TotalItemSize = $stats.TotalItemSize.ToString()
    }
}
```

#### Consulta 4: Detección de Tendencias de Coincidencias de Reglas de Supervisión (`SupervisionRuleMatch` — KQL)
Permite al equipo de GRC/SOC correlacionar picos anómalos de infracciones de Communication Compliance sin exponer el cuerpo del mensaje privado `[Verificado MS Learn]`.
```kql
// Plataforma: Microsoft Defender XDR Advanced Hunting (Tabla: CloudAppEvents)
CloudAppEvents
| where Timestamp > ago(14d)
| where ActionType == "SupervisionRuleMatch"
| summarize TotalMatches = count() by bin(Timestamp, 1d), AccountObjectId
| where TotalMatches >= 5
| order by TotalMatches desc
```

#### Consulta 5: Correlación Forense de Intentos de *Jailbreak* en Copilot (`CopilotInteraction` — Microsoft Graph AuditLogQuery)
Complementa las alertas de *Prompt Shield* de Communication Compliance buscando registros `CopilotInteraction` donde `JailbreakDetected` o `XPIADetected` sea `true` `[Verificado MS Learn]`.
```powershell
# Plataforma: Microsoft Graph REST / PowerShell v1.0 (AuditLogQuery sobre CopilotInteraction)
$copilotAuditBody = @{
    "@odata.type"       = "#microsoft.graph.security.auditLogQuery"
    displayName         = "CC-Correlacion-Jailbreak-XPIA-Copilot"
    filterStartDateTime = (Get-Date).AddDays(-7).ToUniversalTime().ToString("o")
    filterEndDateTime   = (Get-Date).ToUniversalTime().ToString("o")
    operationFilters    = @("CopilotInteraction", "ConnectedAIAppInteraction", "AIAppInteraction")
    keywordFilter       = "JailbreakDetected"
}
Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/auditLog/queries" -Body ($copilotAuditBody | ConvertTo-Json)
```

#### Consulta 6: Verificación del Reporte de Usuarios en Microsoft Teams (`Report inappropriate content` — Teams PowerShell)
Confirma que las políticas globales y personalizadas de mensajería en Teams tengan habilitado el reporte de mensajes inapropiados hacia Communication Compliance (módulo Teams >= 4.2.0) `[Verificado MS Learn]`.
```powershell
# Plataforma: Microsoft Teams PowerShell Module (>= 4.2.0)
Connect-MicrosoftTeams
Get-CsTeamsMessagingPolicy | Select-Object Identity, AllowSecurityEndUserReporting
```

#### Consulta 7: Consulta Transicional con `Search-UnifiedAuditLog` para Coincidencias y Etiquetas (Legado vigente hasta 15-oct-2027)
Documentada únicamente para organizaciones en proceso de migración antes del retiro oficial del cmdlet el 15 de octubre de 2027 (`MC1505599`) `[Verificado MS Learn]`.
```powershell
# Plataforma: Exchange Online PowerShell (NOTA: Migrar a Graph AuditLogQuery antes del 15-oct-2027)
$start = (Get-Date).AddDays(-7)
$end   = Get-Date
Search-UnifiedAuditLog -StartDate $start -EndDate $end -RecordType AeD -Operations SupervisoryReviewTag -ResultSize 1000 |
    Select-Object CreationDate, UserIds, Operations, AuditData
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Control Operativo a Verificar | Método / Comando de Verificación | Resultado Esperado ("Proof of Life") | Frecuencia |
| :--- | :--- | :--- | :--- |
| **Aislamiento de Global Admin** | Iniciar sesión con cuenta *Global Admin* sin roles de CC e intentar abrir alertas en `Communication Compliance > Alerts`. | Acceso denegado al contenido de alertas y mensajes pendientes `[Verificado MS Learn]`. | Mensual |
| **Seudonimización Activa** | Revisar `Settings > Communication Compliance > Privacy` con cuenta *Communication Compliance Admins*. | Opción **Show anonymized versions of usernames** activada (`ANONxxxx`) `[Verificado MS Learn]`. | Mensual |
| **Escaneo Horario de Políticas** | Inspeccionar columna **Last policy scan** en `Communication Compliance > Policies`. | Marca temporal UTC inferior a 60–90 minutos en el 100 % de políticas `Active` `[Verificado MS Learn]`. | Diaria |
| **Salud de Cuota de Buzones** | Ejecutar `Get-SupervisoryReviewPolicyV2` + `Get-MailboxStatistics` sobre `ReviewMailbox`. | `TotalItemSize` < 80 GB e `ItemCount` < 800.000 en todas las políticas `[Verificado MS Learn]`. | Semanal |
| **Enrutamiento User-Reported** | Ejecutar `Get-CsTeamsMessagingPolicy` y validar revisores de *User-reported messages*. | `AllowSecurityEndUserReporting = True` y revisores asignados a RR. HH./Ética (cero Global Admins) `[Verificado MS Learn]`. | Mensual |
| **Preservación Configurada** | Verificar `Settings > Communication Compliance > Policy Match Preservation`. | Plazo explícitamente documentado (`1 month`, `6 months`, `1 year` o `7 years`) acorde a matriz legal `[Verificado MS Learn]`. | Trimestral |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales

> **Nota de validación:** Las fórmulas, umbrales y metas numéricas constituyen objetivos de referencia consultiva para operaciones maduras y se etiquetan como `[Decisión / Propuesta Editorial]`.

| ID | Indicador Clave (KPI) | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **SLA de Triaje de Severidad Alta (LLM >= 4 / Amenazas)** | `(Alertas con Severity >= 4 o Threat revisadas en <= 24 h / Total alertas severidad alta) * 100` | `>= 98 %` | Diaria / Semanal | CCO, RR. HH., SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cumplimiento de Cuota de Supervisión Regulatoria** | `(Mensajes resueltos con Tag y comentario dentro del mes / Total coincidencias pendientes del mes en políticas SEC/FINRA) * 100` | `100 %` (0 ítems vencidos > 5 días) | Semanal / Mensual | Chief Compliance Officer, Auditoría | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Precisión de Políticas (True Positive / Actionable Rate)** | `((Ítems marcados Noncompliant + Questionable) / Total ítems resueltos) * 100` | `>= 65 %` (Falsos positivos `<= 35 %`) | Semanal | Communication Compliance Admin, Lead Analyst | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Cobertura de Supervisión sobre Aplicaciones y Agentes IA** | `(Apps GenAI empresariales + instancias Agent 365 activas cubiertas por políticas CC / Total apps e instancias IA en producción) * 100` | `100 %` | Mensual | CISO, AI Governance Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo Medio de Contención de Mensajes Tóxicos en Teams** | `Promedio(Hora de ejecución de Remove message in Teams - Hora de ingreso a User-reported messages)` | `<= 4 horas laborales` | Semanal | RR. HH., Relaciones Laborales | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Salud de Capacidad de Buzones de Supervisión** | `(Políticas activas por debajo del 80 % del límite de 100 GB o 1M mensajes / Total políticas activas) * 100` | `100 %` (0 desactivaciones no planificadas) | Semanal | Communication Compliance Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Índice de Integridad de Segregación RBAC y Privacidad** | `(Políticas sin Global Admins como revisores + Grupo monolítico CC vacío + Seudonimización activa / Total controles verificados) * 100` | `100 %` | Mensual | DPO, Internal Audit, CISO | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Tasa de Efectividad Pedagógica (No-Reincidencia Post-Notify)** | `(Usuarios notificados vía Notify sin nuevas coincidencias Noncompliant en 90 días / Total usuarios notificados) * 100` | `>= 85 %` | Trimestral | CCO, Cultura y Ética, CISO | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Caracterización Operativa en Communication Compliance |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Reactivo** | Sin políticas activas o solo la política por defecto *User-reported messages* atendida esporádicamente por Global Admins; sin supervisión de Copilot ni integración con IRM. |
| **Nivel 2** | **Básico / Repetible** | Políticas creadas desde plantillas estándar para correo y Teams; grupos de roles separados (*Admins* vs. *Investigators*) y seudonimización activa, pero con alto volumen de falsos positivos por newsletters y sin monitoreo de cuotas. |
| **Nivel 3** | **Definido / Proactivo** | Cobertura completa de Exchange, Teams (incluyendo adjuntos modernos y OCR), Viva Engage en modo nativo y Microsoft 365 Copilot (*Prompt Shields* y *Protected material*); *Filter email blasts* activo; *Policy Match Preservation* gobernado y auditoría mensual de revisores. |
| **Nivel 4** | **Gestionado / Integrado** | Supervisión extendida a conectores regulatorios (Bloomberg/WhatsApp) y apps IA empresariales/externas bajo control FinOps PAYG; integración bidireccional activa con **Insider Risk Management** y **eDiscovery (Premium)**; uso sistemático de *Summarize with Copilot* y métricas SLA semanales. |
| **Nivel 5** | **Optimizado / Agéntico** | Gobernanza continua sobre instancias autónomas de **Microsoft Agent 365** desde *DSPM > AI observability*; auditoría programática 100 % migrada a Microsoft Graph `AuditLogQuery`; simulacros semestrales multi-área y DPIA anual automatizado en Compliance Manager. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota metodológica:** El mapeo de capacidades de Communication Compliance hacia resultados de las 6 funciones de **NIST CSF 2.0 (CSWP 29)** constituye una estructura probatoria consultiva etiquetada como `[Decisión / Propuesta Editorial]` apoyada en controles verificados del producto.

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (NIST CSF 2.0) | Capacidad Habilitadora en Communication Compliance | Técnica MITRE ATT&CK / ATLAS | Evidencia Auditable Reproducible |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales (privacidad, supervisión financiera, IA) se comprenden y gestionan. | Plantillas regulatorias SEC/FINRA, **Policy Match Preservation** (hasta 7 años) y **Pseudonymization** por defecto. | N/A (Gobierno Regulatorio) | Configuración exportada de *Policy settings and status* y DPIA anual firmado `[Decisión / Propuesta Editorial]`. |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad y cumplimiento se establecen y hacen cumplir. | Segregación estricta entre `Communication Compliance Admins`, `Analysts`, `Investigators` y `Viewers` + bloqueo por defecto a Global Admin. | `T1078` (Valid Accounts - Abuso de privilegios internos) | Captura de miembros de grupos de roles en Purview y prueba negativa de acceso de Global Admin `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.RA-01` | Se identifican y registran vulnerabilidades y riesgos en activos, incluyendo canales colaborativos y modelos GenAI. | Descubrimiento de riesgos de comportamiento poco ético en agentes y apps IA desde **DSPM > AI observability** y *Policy health* (puntos ciegos). | `AML.T0051` (LLM Prompt Injection) | Reporte mensual de `DSPM > AI observability` e informe *Sensitive information type per location* `[Decisión / Propuesta Editorial]`. |
| **IDENTIFY (ID)** | `ID.IM-02` | Se identifican mejoras a partir de pruebas, ejercicios y revisiones operativas de seguridad. | Flujo de retroalimentación *Item was misclassified*, reporte *Email blast senders* y simulacros semestrales CC + IRM. | N/A (Mejora Continua) | Historial `Export policy updates` y métricas trimestrales de reducción de falsos positivos `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, autorizaciones y derechos se definen y gestionan bajo el principio de mínimo privilegio. | Exigencia dual (Rol *Analyst/Investigator* + inclusión en *Reviewers*), asignaciones con expiración y **Restricted Administrative Units**. | `T1098` (Account Manipulation) | Matriz mensual de recertificación RBAC y logs `SupervisionPolicyUpdated` `[Decisión / Propuesta Editorial]`. |
| **PROTECT (PR)** | `PR.AT-01` | El personal recibe concientización y formación para desempeñar tareas de forma segura y ética. | Acción correctiva **Notify** con plantillas educativas personalizadas (*Notice templates*) ante infracciones leves de código de conducta o uso de IA. | `T1566` / Ingeniería Social e Imprudencia Interna | Conteo de acciones *User notified* en *Items and actions per policy* y KPI de no-reincidencia `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.CM-03` | Las actividades del personal y el uso de tecnología se monitorean para detectar eventos potencialmente adversos. | Escaneo horario de Exchange, Teams (chats, canales, transcripciones, adjuntos modernos, OCR) y Viva Engage con clasificadores entrenables y LLM. | `T1530` / `T1567` (Exfiltración / Sabotaje Interno) | Reporte *Message details report* y eventos `SupervisionRuleMatch` en Purview Audit `[Decisión / Propuesta Editorial]`. |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender actividades asociadas a ataques o riesgos. | Clasificadores **Prompt Shield** (Jailbreak), **Protected material**, análisis de **Sentiment** y correlación **User activity** con IRM. | `AML.T0051` / `AML.T0054` (LLM Jailbreak) | Coincidencias triadas en pestaña *Pending/Resolved* con severidad LLM y contexto Copilot `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.MA-02` | Los reportes de incidentes se clasifican y validan (triaje). | Cola **Alerts**, política **User-reported messages** y síntesis acelerada mediante **Summarize with Copilot in Purview**. | `T1489` / Hostilidad e Impacto Organizacional | Registros `SupervisoryReviewTag` y cumplimiento del SLA en `Pending for (days)` `[Decisión / Propuesta Editorial]`. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes se contienen para evitar la propagación del impacto. | Acción **Remove message in Teams** (sustitución por *policy tip*) y activación automática del alcance de **Insider Risk Management** (>= 5 mensajes/24h). | `T1491` / Difusión Interna de Contenido Dañino | Evidencia en `View item history` de remoción en Teams y alerta disparada en IRM `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.RP-02` | Las acciones de recuperación y preservación probatoria se seleccionan, validan y ejecutan. | Acción **Escalate for investigation** hacia **eDiscovery (Premium)** (hasta 100 mensajes) y comando **Copy policy** ante saturación de cuota de 100 GB. | N/A (Preservación Legal y Continuidad) | Caso creado en eDiscovery Premium y continuidad verificada en nueva política activa `[Decisión / Propuesta Editorial]`. |
| **RECOVER (RC)** | `RC.CO-03` | Las actividades de recuperación y lecciones aprendidas se comunican a las partes interesadas internas y reguladores. | Exportación programada de reportes regulatorios `.csv`, paquetes `.zip` de hasta 3 GB y reapertura auditable mediante **Unresolve**. | N/A (Reporte Regulatorio Post-Incidente) | Paquetes de exportación en pestaña `Exports` y actas de comité ejecutivo `[Decisión / Propuesta Editorial]`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta de Aprendizaje Oficial y Recursos Recomendados (Vigentes a Nov-2026) | Credencial / Validación Práctica |
| :--- | :--- | :--- |
| **Communication Compliance Admin / Purview Architect** | - Módulo MS Learn: *Detect and address communication risks with Microsoft Purview Communication Compliance* `[Verificado MS Learn]`.<br>- Laboratorio guiado: *Implement retention, eDiscovery, and Communication compliance in Microsoft Purview* `[Verificado MS Learn]`.<br>- *Become a Communication Compliance Ninja* (Microsoft Tech Community) complementado con documentación de IA/Agent 365 2026 `[Verificado MS Learn]`. | **Microsoft Applied Skills: APL-5007** (*Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview* — laboratorio práctico de 2 h) `[Verificado MS Learn]`. *(Nota: el examen SC-401 vigente tras SC-400 se enfoca en Information Security Admin y no evalúa en profundidad CC ni IB)*. |
| **Communication Compliance Analyst / Investigator (Legal, RR. HH., FINRA)** | - Guía oficial MS Learn: *Investigate and remediate Communication Compliance alerts* y caso de estudio *Contoso* en español `[Verificado MS Learn]`.<br>- Guía de privacidad: *Microsoft Purview Insider Risk Management and Communication Compliance privacy guide* `[Verificado MS Learn]`.<br>- Entrenamiento interno en uso ético de **Summarize with Copilot in Purview** y cadena de custodia hacia eDiscovery Premium `[Decisión / Propuesta Editorial]`. | Certificación interna anual de privacidad y atestación de revisor + **APL-5007** opcional `[Decisión / Propuesta Editorial]`. |
| **AI Governance Lead / Insider Risk Manager** | - Documentación MS Learn: *Configure a Communication Compliance policy to detect generative AI interactions* y *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365* `[Verificado MS Learn]`.<br>- Integración de indicadores en *Configure policy indicators in Insider Risk Management* `[Verificado MS Learn]`. | **Microsoft Certified: Information Security Administrator Associate (SC-401)** (para postura DSPM/DLP/IRM de IA) + **APL-5007** `[Verificado MS Learn]`. |
| **GRC / DPO / Internal Auditor** | - Documentación MS Learn: *Use Communication Compliance reports and audits* y API Microsoft Graph `security/auditLog/queries` `[Verificado MS Learn]`. | Ejecución trimestral del laboratorio *Watch the Watchers* y verificación negativa de acceso de Global Admin `[Decisión / Propuesta Editorial]`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Verificadas contra Microsoft Learn MCP al `2026-11-11`

| # | Área Técnica | Hallazgo Verificado a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **Portales y Renombre de Suite** | Retiro definitivo del portal clásico a fines de 2024 (`MC939918`) y renombre de *Microsoft 365 E5 Compliance* a **Microsoft Purview Suite** el 1 de octubre de 2025 `[Verificado MS Learn]`. | Todas las rutas operativas apuntan exclusivamente a `purview.microsoft.com` y nomenclatura Purview Suite. |
| **2** | **Preservación Configurable (`Policy Match Preservation`)** | Desde el 1 de junio de 2025 rige el ajuste global y por política de **Policy Match Preservation** (`1 month`, `6 months`, `1 year` por defecto, o `7 years`), eliminando copias antiguas en CC sin borrar el mensaje original del usuario `[Verificado MS Learn]`. | Incorporada revisión trimestral obligatoria (`T-01`) y distinción frente a Data Lifecycle Management. |
| **3** | **Cobertura de IA Generativa, Agent 365 y Claude Enterprise** | Soporte nativo incluido sin PAYG para **Microsoft 365 Copilot / Copilot Chat**, GA de **Microsoft Agent 365** (1 de mayo de 2026) con integración en *DSPM > AI observability*, e incorporación de **Anthropic Claude Enterprise** (agosto de 2026) y apps IA externas bajo **Pay-As-You-Go** (`1 text record = 1.000 caracteres`, redondeado hacia arriba) `[Verificado MS Learn]`. | Documentados flujos diarios `D-02` y `D-08`, control FinOps `S-05` y playbook `AH-02`. |
| **4** | **Clasificadores LLM y Discrepancia de Nombres** | Los clasificadores basados en LLM (*Hate, Sexual, Violence, Self-harm*) evalúan mensajes >= 5 palabras (máx. 10.000 caracteres) en M365 Copilot, Teams y Viva Engage generando columna **Severity** cuando es `>= 4`, además de **Prompt Shield** y **Protected material**. Se documenta que la plantilla cita *Targeted harassment* mientras la tabla de definiciones lista *Harassment* `[Verificado MS Learn]`. | Integrado en triaje diario `D-01` y arquitectura de detección. |
| **5** | **Incompatibilidad Administrative Units + Adaptive Scopes y Límites de Teams** | Microsoft Learn confirma que en Communication Compliance **no pueden usarse Administrative Units junto con Adaptive Scopes**, que las AU bloquean el acceso a *Reports/Settings/Audit export*, y que los canales públicos de Teams no soportan *Adaptive Scopes* de usuarios (y tienen tope de 250 usuarios en alcance estático) `[Verificado MS Learn]`. | Documentado como restricción crítica en Secciones 4.2 y `M-05`. |
| **6** | **Ausencia de PowerShell para Políticas y Retiro deConectores Veritas** | Microsoft Learn establece explícitamente que **PowerShell no está soportado para crear ni gestionar políticas** de Communication Compliance (solo UI; `Get-SupervisoryReviewPolicyV2` se usa solo para lectura de cuotas de buzón) y que todos los conectores de Veritas se retiraron el 30 de junio de 2024 `[Verificado MS Learn]`. | Evitado cualquier cmdlet ficticio de creación de políticas; incluido script real de monitoreo de cuota de 100 GB / 1M mensajes. |
| **7** | **Transición de Auditoría (`MC1505599`) y Expiración de Roles Purview** | En julio de 2026 se añadieron asignaciones con vencimiento en grupos de roles de Purview, y en octubre de 2026 entró en GA la API `AuditLogQuery` de Microsoft Graph anunciándose el retiro de `Search-UnifiedAuditLog` para el **15 de octubre de 2027** `[Verificado MS Learn]`. | Consultas de auditoría de supervisión actualizadas a Microsoft Graph `security/auditLog/queries` en Sección 10. |

### 14.2 Decisiones y Propuestas Editoriales Adoptadas

| # | Elemento Editorial | Clasificación | Justificación Arquitectónica y Operativa |
| :--- | :--- | :--- | :--- |
| **1** | **Prohibición de uso del grupo monolítico `Communication Compliance` en producción** | `[Decisión / Propuesta Editorial]` | Aunque Microsoft ofrece la Opción 1 (un solo grupo) para despliegues simples, en entornos empresariales vulnera la segregación entre quien administra la privacidad y quien lee mensajes privados. |
| **2** | **SLAs operativos (< 24 h severidad alta, <= 4 h remoción Teams, <= 5 días cola regulatoria)** | `[Decisión / Propuesta Editorial]` | Microsoft Learn no impone SLAs humanos universales; se establecen metas exigentes alineadas a inspecciones FINRA Rule 3110 y deber de cuidado laboral. |
| **3** | **Umbral preventivo del 70–80 % en cuota de `ReviewMailbox` para ejecutar `Copy policy`** | `[Decisión / Propuesta Editorial]` | Dado que el sistema desactiva automáticamente la política al llegar a 100 GB o 1M de mensajes (notificando recién al 80/90/95 %), anticipar la copia semanal al 70–80 % evita ventanas ciegas regulatorias. |
| **4** | **Modelo de Madurez de 5 niveles y catálogo de 8 KPIs (`KPI-01` a `KPI-08`)** | `[Decisión / Propuesta Editorial]` | Provee al CISO y al CCO un tablero cuantitativo estandarizado para medir precisión, adopción IA, salud de plataforma y eficacia pedagógica. |
| **5** | **Mapeo probatorio a las 6 funciones de NIST CSF 2.0 y MITRE ATT&CK / ATLAS** | `[Decisión / Propuesta Editorial]` | Conecta los controles nativos de Purview con auditorías externas de ciberseguridad e IA responsable bajo una matriz verificable. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Learn about Communication Compliance*: `https://learn.microsoft.com/en-us/purview/communication-compliance` `[Verificado MS Learn]`
- **REF-02:** Microsoft Learn — *Assign permissions in Communication Compliance (RBAC & Administrative Units)*: `https://learn.microsoft.com/en-us/purview/communication-compliance-permissions` `[Verificado MS Learn]`
- **REF-03:** Microsoft Learn — *Detect channel signals with Communication Compliance (GenAI, Teams, Exchange, Viva Engage, 3rd-party)*: `https://learn.microsoft.com/en-us/purview/communication-compliance-channels` `[Verificado MS Learn]`
- **REF-04:** Microsoft Learn — *Configure a Communication Compliance policy to detect generative AI interactions*: `https://learn.microsoft.com/en-us/purview/communication-compliance-copilot` `[Verificado MS Learn]`
- **REF-05:** Microsoft Learn — *Manage Communication Compliance policies (Templates, LLM Classifiers, OCR, IRM Integration, 100GB/1M Limits)*: `https://learn.microsoft.com/en-us/purview/communication-compliance-policies` `[Verificado MS Learn]`
- **REF-06:** Microsoft Learn — *Investigate and remediate Communication Compliance alerts (Policy Match Preservation, Copilot Summarize, Actions)*: `https://learn.microsoft.com/en-us/purview/communication-compliance-investigate-remediate` `[Verificado MS Learn]`
- **REF-07:** Microsoft Learn — *Use Communication Compliance reports and audits*: `https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits` `[Verificado MS Learn]`
- **REF-08:** Microsoft Learn — *Microsoft Purview Insider Risk Management and Communication Compliance privacy guide*: `https://learn.microsoft.com/en-us/purview/insider-risk-solution-privacy` `[Verificado MS Learn]`
- **REF-09:** Microsoft Learn — *Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365*: `https://learn.microsoft.com/en-us/purview/ai-agent-365` `[Verificado MS Learn]`
- **REF-10:** Microsoft Learn — *How does Microsoft Purview support Agent 365?*: `https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/purview-agent-365` `[Verificado MS Learn]`
- **REF-11:** Microsoft Learn — *Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise)*: `https://learn.microsoft.com/en-us/purview/ai-claude-enterprise` `[Verificado MS Learn]`
- **REF-12:** Microsoft Learn — *Learn about Microsoft Purview billing models (Pay-As-You-Go Text Records)*: `https://learn.microsoft.com/en-us/purview/purview-billing-models` `[Verificado MS Learn]`
- **REF-13:** Microsoft Learn — *Trainable classifier definitions*: `https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions` `[Verificado MS Learn]`
- **REF-14:** Microsoft Learn — *Microsoft Applied Skills: Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview (APL-5007)*: `https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-5007` `[Verificado MS Learn]`

### 15.2 Blogs Oficiales Microsoft, Message Center y Comunidad MVP
- **REF-15:** Microsoft Security Blog — *New Purview Communication Compliance features for Copilot and Insider Risk Management*: `https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-purview-communication-compliance-features-for-copilot-and-insider-risk-manag/4296775` `[Verificado MS Learn]`
- **REF-16:** Microsoft 365 Blog — *Microsoft 365 E7 and Agent 365 are now generally available* (1 de mayo de 2026): `https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295` `[Verificado MS Learn]`
- **REF-17:** Microsoft Security Blog — *Become a Communication Compliance Ninja*: `https://techcommunity.microsoft.com/blog/microsoft-security-blog/become-a-communication-compliance-ninja/3283283` `[Verificado MS Learn]`
- **REF-18:** Microsoft 365 Message Center Archive (Merill Fernando, Microsoft) — *MC1505599: Microsoft Purview Audit AuditLogQuery API GA and Search-UnifiedAuditLog retiring*: `https://mc.merill.net/message/MC1505599` `[Verificado MS Learn]`

### 15.3 Marcos Normativos y Regulatorios
- **REF-19:** NIST — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* y *FINRA Rule 3110 / SEC Rule 17a-4 Compliance Offering*: `https://learn.microsoft.com/en-us/compliance/regulatory/offering-SEC-docs` `[Verificado MS Learn]`

# Guía Maestra de Excelencia Operacional: Microsoft Purview eDiscovery (Experiencia Moderna Unificada y Capacidades Premium en M365 E5)

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Definición Oficial |
| :--- | :--- |
| **Identificador del Módulo** | `20_Purview_eDiscovery_Premium` |
| **Slug Canónico** | `Purview_eDiscovery_Premium` |
| **Nombre Completo** | Microsoft Purview eDiscovery (Experiencia Moderna Unificada y Capacidades Premium en M365 E5) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` `[Verificado MS Learn]` |
| **Origen y Trazabilidad** | Nuevo desde Microsoft Learn MCP (Nov 2026) |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (con facturación Azure Pay-As-You-Go únicamente para almacenamiento en casos de datos de IA no-Microsoft 365 y uso de Graph Export API bajo licencias E3) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (Solutions > eDiscovery), `https://portal.azure.com` (Enterprise Applications / Pay-As-You-Go), `https://developer.microsoft.com/graph/graph-explorer` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, General Counsel / Legal Operations, Data Protection Officer (DPO), Compliance Officer, eDiscovery Administrator, eDiscovery Manager, Insider Risk Lead, Forensics / SecOps L3, Revisores Legales Internos y Externos |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Electronic Discovery Reference Model (EDRM 2.0), MITRE ATT&CK Enterprise v18, ISO/IEC 27001:2022, ISO/IEC 27037, GDPR (Art. 15/17 DSR), SEC Rule 17a-4, Ley 21.719 (Chile), LFPDPPP (México) |

> **Nota de Consolidación Arquitectónica (Noviembre 2026):** Este documento establece el estándar definitivo de excelencia operacional para **Microsoft Purview eDiscovery** tras el hito arquitectónico de modernización ejecutado entre mayo y agosto de 2025 `[Verificado MS Learn]`. El **26 de mayo de 2025** (MC1055528), Microsoft retiró la opción separada de *Content Search* clásico y deshabilitó los parámetros heredados de exportación por PowerShell (`New-ComplianceSearchAction -Export`, `Get-ComplianceSearchAction -Export` y `Set-ComplianceSearchAction -ChangeExportKey`) en Exchange Online `[Verificado MS Learn]`. Posteriormente, el **31 de agosto de 2025**, Microsoft retiró globalmente **todas las experiencias clásicas** (*classic Content Search*, *classic eDiscovery Standard* y *classic eDiscovery Premium*, permaneciendo la documentación legada solo para *21Vianet China*), consolidándolas en una única arquitectura moderna centrada en casos dentro de `https://purview.microsoft.com > Solutions > eDiscovery` `[Verificado MS Learn]`. Toda afirmación técnica oficial se identifica con `[Verificado MS Learn]` y todo umbral operativo, SLA interno, meta de KPI o diseño de gobierno consultivo se identifica con `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución del Descubrimiento Electrónico a Noviembre de 2026

En una arquitectura empresarial moderna impulsada por colaboración ubicua e inteligencia artificial generativa, la capacidad de identificar, preservar, recolectar, procesar, revisar, analizar, censurar y producir Información Almacenada Electrónicamente (*Electronically Stored Information* — ESI) con cadena de custodia defendible ante tribunales y reguladores constituye un pilar crítico de resiliencia jurídica y cibernética `[Decisión / Propuesta Editorial]`.

A noviembre de 2026, **Microsoft Purview eDiscovery** opera como una plataforma unificada en el portal de Microsoft Purview (`https://purview.microsoft.com`), reemplazando la fragmentación histórica de tres consolas separadas (*Content Search*, *Standard* y *Premium*) `[Verificado MS Learn]`. En esta arquitectura:

1. **Modelo centrado en casos (*Case-centric workflow*):** Todos los casos creados en el portal son estructuralmente del tipo unificado; la disponibilidad de capacidades estándar frente a capacidades **Premium** depende de las licencias del tenant/custodios y del interruptor organizacional en `Settings > eDiscovery > General` `[Verificado MS Learn]`. Las búsquedas de contenido rápidas sin caso formal residen ahora dentro de un único caso generado por el sistema denominado **Content search** `[Verificado MS Learn]`.
2. **Indexación avanzada *Just-in-Time* y estadísticas vivas:** A diferencia del flujo clásico que obligaba a reindexar custodios manualmente antes de coleccionar y generaba colecciones inmutables intermedias, la experiencia moderna ejecuta **Advanced indexing** de manera automática durante las búsquedas con alcance de estadísticas, al agregar resultados a un *Review set* o al exportar `[Verificado MS Learn]`.
3. **Cobertura nativa de IA Generativa y Contenedores Modernos:** La solución descubre, preserva y audita interacciones de **Microsoft 365 Copilot**, **Microsoft 365 Copilot Chat (BizChat)**, **Copilot Studio**, notas de **Facilitator** en Teams y aplicaciones de IA conectadas en el buzón del usuario (`IPM.SkypeTeams.Message.Copilot.*`), distingue el tratamiento de **Copilot Memories** (`IPM.Contact`) y **Copilot Pages / Notebooks** (`.page` / `.loop` en contenedores **SharePoint Embedded**), y permite purgar derrames de datos sensibles en IA mediante Microsoft Graph (`purgeData`) `[Verificado MS Learn]`.
4. **Aceleración con IA Defensiva y Analítica Big Data:** Integra **Microsoft Security Copilot** embebido para traducir lenguaje natural a **KeyQL** (*Draft a query with Copilot*), resumir casos completos (*Summarize this case*) y generar resúmenes contextuales de evidencia en *Review sets*, complementado con el nuevo **Advanced review set explorer (preview)** basado en **Kusto Query Language (KQL)** sobre `ReviewSetTable` `[Verificado MS Learn]`.

### 2.2 Matriz de Licenciamiento Oficial y Modelo de Facturación (M365 E5 / Purview Suite / PAYG)

El licenciamiento de capacidades Premium en Microsoft Purview eDiscovery exige licenciar a cada usuario cuyos datos se benefician del servicio (custodios en retención legal, búsqueda avanzada o *Review sets*, y propietarios/miembros de sitios SharePoint o equipos Teams incluidos) `[Verificado MS Learn]`. Los administradores, oficiales de cumplimiento o abogados asignados como miembros de un caso para revisar y analizar datos no requieren licencia E5 por el solo rol de revisor, aunque necesitan licencia base Microsoft 365 E3/E5 y **SharePoint Plan 2 (E3)** para evitar restricciones al exportar contenido de SharePoint `[Verificado MS Learn]`.

| Capacidad / Escenario Operativo | Microsoft 365 E3 / Office 365 E3 | Microsoft 365 E5 / A5 / G5 o Microsoft Purview Suite (antes E5 Compliance) / E5 eDiscovery & Audit | Modelo Pay-As-You-Go (Suscripción Azure Vinculada) |
| :--- | :--- | :--- | :--- |
| **Casos, Búsquedas KeyQL, Estadísticas, Muestras y Exportación estándar** | Incluido `[Verificado MS Learn]` | Incluido `[Verificado MS Learn]` | No aplica para datos M365 `[Verificado MS Learn]` |
| **eDiscovery Holds (infinitos) y Search & Purge de buzón/Teams/IA** | Incluido (requiere licencia elegible; F1/F3 base sin add-on NO cubren ser objetivo de Hold) `[Verificado MS Learn]` | Incluido (habilita Holds basados en consulta KeyQL, acotados por fecha y por custodio) `[Verificado MS Learn]` | No aplica `[Verificado MS Learn]` |
| **Review Sets, Advanced Indexing, OCR de caso, Hilos Teams (12 h) y Cloud Attachments** | No incluido `[Verificado MS Learn]` | Incluido con capacidades Premium habilitadas `[Verificado MS Learn]` | Almacenamiento M365 y M365 Copilot incluido sin cargo PAYG `[Verificado MS Learn]` |
| **Analítica (Near-duplicates, Email threading, Themes), Attorney-Client Privilege, Redacción PDF y KQL Explorer** | No incluido `[Verificado MS Learn]` | Incluido con capacidades Premium habilitadas `[Verificado MS Learn]` | No aplica `[Verificado MS Learn]` |
| **Búsqueda Premium de interacciones de Microsoft 365 Copilot** | No incluido (solo búsqueda/hold/exportación estándar si posee licencia M365 Copilot) `[Verificado MS Learn]` | Incluido al combinar M365 E5 (o M365 E3 + Purview Suite / E5 eDiscovery & Audit) + M365 Copilot `[Verificado MS Learn]` | Almacenamiento de datos M365 AI incluido en suscripción `[Verificado MS Learn]` |
| **Almacenamiento en casos de datos de IA no-Microsoft 365 (`Fabric`, `SecurityCopilot`, `ConnectedAIApp`, `CloudAIApp.SaaS`)** | Requiere PAYG para exportar o conservar en casos `[Verificado MS Learn]` | Búsqueda, Hold y gestión de caso sin cargo; **Add to review set y Exportación** sujetos a medidor diario Azure `[Verificado MS Learn]` | **Obligatorio** (facturación diaria acumulada mientras el caso esté activo o cerrado; cesa al eliminar el caso) `[Verificado MS Learn]` |
| **Microsoft Graph API (`security/cases/ediscoveryCases`)** | Soportado con **Delegated auth** activando facturación PAYG (cobro por GB solo en Export API tras cuota gratuita mensual) `[Verificado MS Learn]` | Soportado con **Delegated auth** y **App-only auth** (operaciones avanzadas sobre *Review sets*, *Tagging* y *Analytics* requieren Premium) `[Verificado MS Learn]` | Obligatorio para uso de API en tenants E3 y para exportar datos IA no-M365 `[Verificado MS Learn]` |
| **Microsoft Security Copilot en eDiscovery (NL2KQL, Resumen de ítems y casos)** | Requiere dotación de SCUs de Security Copilot + capacidades Premium `[Verificado MS Learn]` | Requiere Security Copilot habilitado (M365 E5 incorpora dotación base de SCUs elegibles + aprovisionamiento) `[Verificado MS Learn]` | Consumo de Security Compute Units (SCUs) según plan `[Verificado MS Learn]` |

> **Nota Crítica sobre Buzones Compartidos e Inactivos:** Colocar un buzón compartido (*Shared Mailbox*) en retención de eDiscovery exige **Exchange Online Plan 2** o **Exchange Online Plan 1 + Exchange Online Archiving** `[Verificado MS Learn]`. Los buzones inactivos (*Inactive Mailboxes*, preservados tras borrar el usuario con Hold previo) no consumen licencia activa de uso `[Verificado MS Learn]`.

### 2.3 Principios Rectores y Posicionamiento Zero Trust

1. **Preservación In-Place sin Duplicación Prematura (*Verify Explicitly & Assume Breach*):** Mantener la evidencia inmutable en su ubicación nativa (`Recoverable Items` en Exchange y `Preservation Hold Library` en SharePoint/OneDrive) mediante *Hold policies* verificadas antes de copiar únicamente el subconjunto relevante hacia un *Review set* `[Verificado MS Learn]`.
2. **Aislamiento Estricto por Caso, Frontera Jurisdiccional y Mínimo Privilegio (*Use Least Privilege Access*):** Combinar membresía explícita por caso, segregación entre `eDiscovery Manager` y `eDiscovery Administrator`, **Compliance Boundaries** (`New-ComplianceSecurityFilter`) y **Restricted Administrative Units** para impedir búsquedas globales no autorizadas `[Verificado MS Learn]`.
3. **Integridad Contextual de Colaboración Moderna e IA Generativa:** Recolectar no solo mensajes aislados sino hilos conversacionales completos (+/- 12 horas en Teams, Viva Engage y M365 Copilot), versiones exactas compartidas de *Cloud attachments* y contenedores **SharePoint Embedded** `[Verificado MS Learn]`.
4. **Reducción Defendible de Volumen (*Early Case Assessment & Analytics*):** Aplicar estadísticas previas, deduplicación cercana (*Near-duplicates*), reconstrucción de hilos de correo (*Email threading* con marcador `Is Inclusive`), *Themes* y detección ML de privilegio abogado-cliente antes de revisar o exportar `[Verificado MS Learn]`.
5. **Automatización Soportada vía Microsoft Graph y Cero Scripts Heredados:** Erradicar automatizaciones basadas en parámetros retirados de PowerShell (`-Export`) o autenticación *app-only* no soportada en `Connect-IPPSSession`, estandarizando en `Microsoft.Graph.Security` y `Microsoft Purview eDiscovery API` `[Verificado MS Learn]`.
6. **Trazabilidad Forense y Control FinOps de Datos IA:** Auditar cada vista previa, búsqueda, purga y exportación con dirección IP de cliente en Purview Audit y excluir proactivamente clases `Non M365 AI activity` cuando el mandato legal no requiera datos de IA de terceros sujetos a cobro PAYG `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional alineada al Modelo EDRM 2.0

La arquitectura moderna de Microsoft Purview eDiscovery implementa de extremo a extremo las fases del **Electronic Discovery Reference Model (EDRM)** sin extraer prematuramente los datos fuera del perímetro de seguridad de Microsoft 365 `[Verificado MS Learn]`:

```text
[Eventos Disparadores: Litigio / Regulador / DSR / Escalación Insider Risk Management / Incidente Spillage IA]
                                              │
                                              ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  1. IDENTIFICACIÓN Y MAPEO DE FUENTES (Cases > Data sources)                                             │
│     - Custodios (Buzón Exchange + OneDrive + Contenedores SharePoint Embedded: Loop / Copilot Pages)     │
│     - Fuentes no custodiadas (Sitios SharePoint, M365 Groups, Teams, Canales Privados/Compartidos)       │
└─────────────────────────────────────────────┬────────────────────────────────────────────────────────────┘
                                              │
                     ┌────────────────────────┴────────────────────────┐
                     ▼                                                 ▼
┌─────────────────────────────────────────────┐   ┌────────────────────────────────────────────────────────┐
│  2. PRESERVACIÓN IN-PLACE (Hold policies)   │   │  3. BÚSQUEDA Y EVALUACIÓN (Searches + KeyQL / Copilot) │
│     - Hold infinito o basado en KeyQL/fecha │   │     - Condition Builder / KeyQL / NL2KQL con Copilot   │
│     - Instantánea puntual de grupos         │   │     - Advanced Indexing JIT + Estadísticas y Muestras  │
│     - Monitoreo en Hold Report (preview)    │   │     - Flujo alterno: Search & Purge via Graph API      │
└─────────────────────────────────────────────┘   └────────────────────┬───────────────────────────────────┘
                                                                       │
                                              ┌────────────────────────┴────────────────────────┐
                                              ▼                                                 ▼
                             ┌─────────────────────────────────┐               ┌────────────────────────────────┐
                             │ 4A. EXPORTACIÓN DIRECTA BÚSQUEDA│               │ 4B. REVIEW SETS (Azure Storage │
                             │     - Expiración estricta: 14 d │               │     administrado por Microsoft)│
                             │     - Soporte CMK (preview)     │               │     - OCR, Hilos 12h, Cloud    │
                             └─────────────────────────────────┘               │       Attachments (shared/live)│
                                                                               │     - Decryption RMS / MIP     │
                                                                               └────────────────┬───────────────┘
                                                                                                │
                                                                                                ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  5. REVISIÓN, ANALÍTICA, CENSURA Y PRODUCCIÓN (Review Set Analytics, Explorer KQL & Export)              │
│     - Near-duplicates, Email threading (Is Inclusive), Themes, Attorney-client privilege smart tags      │
│     - Advanced review set explorer (KQL sobre ReviewSetTable) + Resúmenes con Security Copilot           │
│     - Visor Annotate -> Commit redactions ({itemId}_burn.pdf) -> Exportación (descarga <= 30 días / API) │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Componentes Técnicos y Aplicaciones Empresariales Requeridas

Para que los visores nativos, filtros, analítica y exportaciones programáticas operen sin fallos, el tenant debe mantener habilitadas para inicio de sesión (`Enabled for users to sign-in = Yes` en `portal.azure.com > Enterprise Applications`) cuatro aplicaciones empresariales esenciales `[Verificado MS Learn]`:

| Aplicación Empresarial en Microsoft Entra ID | Application (Client) ID Oficial | Función Técnica en eDiscovery |
| :--- | :--- | :--- |
| `Built-in security add-on for on-premises mailboxes` | `00000007-0000-0ff1-ce00-000000000000` | Interacción con servicios de sustrato Exchange Online Protection `[Verificado MS Learn]` |
| `ComplianceWorkbenchApp` | `92876b03-76a3-4da8-ad6a-0511ffdf8647` | Motor de espacio de trabajo, visores y analítica de *Review sets* `[Verificado MS Learn]` |
| `MicrosoftPurviewEDiscovery` | `b26e684c-5068-4120-a679-64a5d2c909d9` | Exportación programática de paquetes y reportes mediante scripts y API (`eDiscovery.Download.Read`) `[Verificado MS Learn]` |
| `Office365Zoom` | `0d38933a-0bbd-41ca-9ebd-28c4b5ba7cb7` | Renderizado de alta fidelidad en visores nativos de documentos `[Verificado MS Learn]` |

### 3.3 Comportamiento Técnico en Cargas Modernas: Cloud Attachments, Teams y Agentes IA

1. **Cloud Attachments (Adjuntos modernos vinculados):**
   - Al activar `Access links (cloud attachments) in messages` al enviar a *Review set* o exportar, eDiscovery extrae enlaces clicables en correos HTML y mensajes de Teams/Copilot (máximo **50 enlaces por mensaje**, longitud de URL <= **2.048 caracteres**, cuerpo <= **100.000 caracteres**; no procesa correos en texto plano, cifrados, carpetas ni cuadernos OneNote completos) `[Verificado MS Learn]`.
   - **Versión compartida vs. versión viva:** Por defecto solo se recolecta la versión actual (*live*). Para preservar y coleccionar la **versión exacta en el instante en que fue compartida**, es obligatorio desplegar previamente en *Data Lifecycle Management* una **etiqueta de retención con auto-aplicación a cloud attachments** en SharePoint y OneDrive `[Verificado MS Learn]`. Con ello, ambas versiones comparten el mismo `GroupID` del mensaje padre `[Verificado MS Learn]`.
   - **Excepción crítica de perímetro:** Si un correo o chat coincide con la búsqueda, el archivo vinculado se recupera como hijo del mensaje incluso si reside fuera de la *Compliance Boundary* de SharePoint/OneDrive del investigador `[Verificado MS Learn]`. En canales compartidos (*Shared Channels*) de Teams, la extracción automática de enlaces no está soportada y debe añadirse manualmente el sitio SharePoint del canal compartido `[Verificado MS Learn]`.
2. **Gobierno Forense de Microsoft 365 Copilot, Copilot Studio, Memories y Pages:**
   - **Prompts y Respuestas:** Se almacenan como elementos individuales en una carpeta oculta del buzón de Exchange Online del usuario con clases `IPM.SkypeTeams.Message.Copilot.<AppName>` (`Word`, `Excel`, `PowerPoint`, `Outlook`, `Teams`, `Loop`, `Whiteboard`, `BizChat`, `Studio.*`, `Security.SecurityCopilot`, `Fabric.*`, `ConnectedAIApp.*`, `CloudAIApp.SaaS.*`) `[Verificado MS Learn]`. El encabezado `From`/`To` refleja el SMTP del usuario y la identidad del principal de servicio de la app Copilot `[Verificado MS Learn]`. Para reconstruir el contexto completo cuando se filtra por palabras clave, debe activarse `Include full conversation for Copilot, Teams and Viva Engage messages` (ventana de **12 horas antes y después**) y `Organize conversations into HTML transcripts` `[Verificado MS Learn]`.
   - **Copilot Memories (`IPM.Contact`):** Se guardan en la subcarpeta oculta `CopilotMemory` de contactos del buzón. **Limitación crítica verificada:** las políticas de retención de Purview y los *eDiscovery Holds* **no preservan actualmente las memorias de Copilot**, y purgar un prompt/respuesta no borra la memoria inferida asociada (debe eliminarse por separado) `[Verificado MS Learn]`.
   - **Copilot Pages y Copilot Notebooks (`.page` / `.loop`):** **No se almacenan en el buzón Exchange**, sino en un contenedor **SharePoint Embedded** propiedad del usuario (identificado bajo la aplicación **Loop**) `[Verificado MS Learn]`. Un Hold aplicado únicamente al buzón del custodio **no protege sus Copilot Pages**: debe agregarse explícitamente la URL del contenedor SharePoint Embedded en el Hold y, al exportar desde el *Review set*, marcar `Convert supported file formats to HTML` para convertir `.page` y `.loop` a HTML legible `[Verificado MS Learn]`.
3. **Descifrado Nativo vs. Límites Criptográficos:**
   - Con capacidades Premium y el rol `RMS Decrypt`, eDiscovery descifra automáticamente correos con *Purview Message Encryption* (sin plantilla de marca personalizada que desvíe al portal externo), adjuntos Office/PDF (requiere `Set-IRMConfiguration -EnablePdfEncryption $true` para PDFs derivados de Office etiquetado) y archivos en SharePoint/OneDrive protegidos con etiquetas de sensibilidad sin expiración de acceso de usuario `[Verificado MS Learn]`.
   - **No soportado para descifrado:** Contenido cifrado con **Double Key Encryption (DKE)**, S/MIME, claves HYOK/RMS on-premises o archivos cifrados anidados dentro de contenedores `.zip` o `.msg` `[Verificado MS Learn]`.
4. **Transición de Notificaciones de Retención Legal (*Hold Notifications* — Hito Agosto 2025):**
   - Con el retiro el **31 de agosto de 2025** de la experiencia clásica de *eDiscovery (Premium)*, el módulo integrado clásico de *Custodian Communications* (Issuance, Re-issuance, Release, Reminders y Escalations) quedó retirado fuera de *21Vianet China* `[Verificado MS Learn]`. En la arquitectura vigente a noviembre de 2026, el motor nativo de Purview ejecuta y audita la retención técnica (*Hold policies* + *Hold report*), mientras que el flujo formal de notificación escrita, recordatorios periódicos y registro de acuse legal del custodio debe instrumentarse mediante flujos gobernados en Power Automate / SharePoint / Approvals conectados a Microsoft Graph (`security/cases/ediscoveryCases/{id}/legalHolds`) o mediante plataformas especializadas de *Legal Hold* integradas vía API `[Decisión / Propuesta Editorial]`.

### 3.4 Matrices Técnicas de Referencia: Clases de IA, Prefijos de Hold y Reglas de Exportación

#### 3.4.1 Tabla Oficial de Almacenamiento, `ItemClass` y Facturación para Datos de Copilot e IA

| Fuente de Aplicación de IA / Artefacto | Ubicación Física de Almacenamiento | Clase de Elemento (`ItemClass`) o Extensión | Cobertura de Hold / Retención | Régimen de Facturación en eDiscovery |
| :--- | :--- | :--- | :--- | :--- |
| **Microsoft 365 Copilot (General)** | Buzón Exchange Online (carpeta oculta) `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.*` `[Verificado MS Learn]` | Soportado por eDiscovery Hold y política Copilot `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Microsoft 365 Copilot Chat (BizChat / Teams / Bing)** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.BizChat` `[Verificado MS Learn]` | Soportado por eDiscovery Hold `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Copilot en Apps Office (Word, Excel, PPT, Outlook, OneNote, Loop, Forms, Whiteboard)** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.<App>` (ej. `.Word`, `.Excel`, `.Outlook`) `[Verificado MS Learn]` | Soportado por eDiscovery Hold `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Microsoft Copilot Studio (Agentes personalizados)** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.Studio.*` `[Verificado MS Learn]` | Soportado por eDiscovery Hold `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Agente Facilitator en Reuniones Teams (Chat e IA Notes)** | Buzón Exchange (asistentes) + OneDrive del iniciador (`Meetings/*.loop`) `[Verificado MS Learn]` | `IPM.SkypeTeams.Message` / `IPM.SkypeTeams.Message.TeamCopilot.AiNotes.Teams` / `.loop` `[Verificado MS Learn]` | Buzón + OneDrive (recolección automática con *cloud attachments*) `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Tareas Asignadas por Agente Facilitator** | Buzón Exchange del usuario asignado `[Verificado MS Learn]` | `IPM.Task` `[Verificado MS Learn]` | Soportado en buzón (retención requiere fecha fin) `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Copilot Personalization & Memory** | Buzón Exchange (subcarpeta oculta `CopilotMemory`) `[Verificado MS Learn]` | `IPM.Contact` `[Verificado MS Learn]` | **NO soportado** por Holds ni políticas de retención; purga independiente `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Copilot Pages y Copilot Notebooks** | Contenedor **SharePoint Embedded** del usuario (etiquetado como **Loop**) `[Verificado MS Learn]` | Archivos `.page` y `.loop` (sin `ItemClass`) `[Verificado MS Learn]` | **NO cubierto por Hold de buzón**; exige URL del contenedor SPE en el Hold `[Verificado MS Learn]` | Incluido en suscripción empresarial `[Verificado MS Learn]` |
| **Copilot in Microsoft Fabric / SQL / BAP** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.Fabric.*`, `.Sql.*`, `.BAP*` `[Verificado MS Learn]` | Soportado por Hold (sin cargo en búsqueda/hold) `[Verificado MS Learn]` | **Pay-As-You-Go** en *Review set* y Exportación `[Verificado MS Learn]` |
| **Microsoft Security Copilot** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.Copilot.Security.SecurityCopilot` `[Verificado MS Learn]` | Soportado por Hold (sin cargo en búsqueda/hold) `[Verificado MS Learn]` | **Pay-As-You-Go** en *Review set* y Exportación `[Verificado MS Learn]` |
| **Microsoft Foundry / Entra Connected AI Apps** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.ConnectedAIApp.AzureAI.<Resource>` / `.Entra.<AppID>` `[Verificado MS Learn]` | Soportado por Hold; gobierno ampliado en M365 E7 y Agent 365 `[Verificado MS Learn]` | **Pay-As-You-Go** en *Review set* y Exportación `[Verificado MS Learn]` |
| **ChatGPT Enterprise y Otras Apps SaaS / Conectores IA** | Buzón Exchange Online `[Verificado MS Learn]` | `IPM.SkypeTeams.Message.ConnectedAIApp.Connector.*` / `IPM.SkypeTeams.Message.CloudAIApp.SaaS.<AppID>` `[Verificado MS Learn]` | Soportado por Hold `[Verificado MS Learn]` | **Pay-As-You-Go** en *Review set* y Exportación `[Verificado MS Learn]` |

#### 3.4.2 Tabla de Diagnóstico Forense de Prefijos `InPlaceHolds` y Mecanismos de Retención

| Prefijo / Propiedad en Exchange y SharePoint | Origen Técnico de la Retención | Consola Oficial para Liberación / Exclusión | Comportamiento post-liberación |
| :--- | :--- | :--- | :--- |
| `UniH<GUID>` | Política de retención de caso eDiscovery (*eDiscovery case hold*) `[Verificado MS Learn]` | `purview.microsoft.com > eDiscovery > Cases > [Caso] > Hold policies` `[Verificado MS Learn]` | Hasta 240 min de propagación + activación automática de `DelayHoldApplied` por 30 días `[Verificado MS Learn]` |
| `cld<GUID>` | Retención asociada a *Cloud attachments* en eDiscovery `[Verificado MS Learn]` | `purview.microsoft.com > eDiscovery > Cases > [Caso] > Hold policies` `[Verificado MS Learn]` | Preserva versiones vinculadas en `Preservation Hold Library` `[Verificado MS Learn]` |
| `mbx<GUID>` | Política de retención de Microsoft Purview con alcance de buzón `[Verificado MS Learn]` | `purview.microsoft.com > Data lifecycle management > Retention policies` (excluir buzón) `[Verificado MS Learn]` | Replicación de exclusión hasta 24 h + posible `DelayHoldApplied` `[Verificado MS Learn]` |
| `skp<GUID>` | Política de retención de Microsoft Teams `[Verificado MS Learn]` | `purview.microsoft.com > Data lifecycle management > Retention policies` (Teams) `[Verificado MS Learn]` | Preserva mensajes en carpeta oculta del sustrato `[Verificado MS Learn]` |
| `grp<GUID>` | Política de retención de Microsoft 365 Groups / Sitios `[Verificado MS Learn]` | `purview.microsoft.com > Data lifecycle management > Retention policies` `[Verificado MS Learn]` | Impide borrado de sitio o librería hasta excluir ubicación `[Verificado MS Learn]` |
| `LitigationHoldEnabled = True` | *Litigation Hold* directo a nivel de buzón Exchange `[Verificado MS Learn]` | Microsoft 365 Admin Center o `Set-Mailbox -LitigationHoldEnabled $false` `[Verificado MS Learn]` | Cubre buzón primario y archivo; activa `DelayHoldApplied` al retirarse `[Verificado MS Learn]` |
| `ComplianceTagHoldApplied = True` |Al menos un ítem en el buzón posee etiqueta de retención con acción de retener `[Verificado MS Learn]` | Revisión/eliminación de etiquetas de retención sobre los ítems afectados `[Verificado MS Learn]` | Impide purga permanente del buzón inactivo mientras persista `[Verificado MS Learn]` |

#### 3.4.3 Comparativa Operativa: Exportación Directa desde Búsqueda vs. Exportación desde Review Set

| Parámetro Técnico | Exportación Directa desde Búsqueda (`Searches > Export`) | Exportación desde Conjunto de Revisión (`Review sets > Export`) |
| :--- | :--- | :--- |
| **Ventana de Expiración y Descarga** | **14 días estrictos**; al día 14 el paquete y sus datos se eliminan irreversiblemente `[Verificado MS Learn]` | El registro perdura toda la vida del caso, pero el contenido debe descargarse dentro de **30 días** `[Verificado MS Learn]` |
| **Cifrado con Customer Key (CMK)** | **Soportado (preview)** si el tenant tiene DEP en estado `PolicyAssigned` vía MDEP `[Verificado MS Learn]` | No aplica CMK al almacenamiento del *Review set* actualmente `[Verificado MS Learn]` |
| **Exportación de Redacciones PDF (`_burn.pdf`)** | No disponible (no existe fase previa de *Annotate* / *Commit redactions*) `[Verificado MS Learn]` | **Soportado** marcando `Export redaction` (reemplaza nativo en archivos individuales; adjunta ambos en hilos Teams/Viva; no compatible con formato PST) `[Verificado MS Learn]` |
| **Conversión de `.loop` y `.page` a HTML** | Exporta copias nativas e informes según configuración de origen `[Verificado MS Learn]` | Opción dedicada **Convert supported file formats to HTML** (desmarcada por defecto) `[Verificado MS Learn]` |
| **Expansión de Familias y Conversaciones** | Hilos HTML, ventana de 12 h Teams/Viva y versiones SharePoint (1, 10, 100, Todas) `[Verificado MS Learn]` | Expansión por `FamilyId` (*Associated family items*) y `ConversationId` (*Associated conversation items*) `[Verificado MS Learn]` |
| **Límites de Partición de Paquetes** | PST: `1 GB`, `2 GB`, `5 GB` (default) o `10 GB`; ZIP: `2 GB`, `10 GB` (default), `20 GB` o `40 GB`; cancelación automática si tarda **> 7 días** `[Verificado MS Learn]` | PST: `1 GB`, `2 GB`, `5 GB` (default) o `10 GB`; ZIP: `2 GB`, `10 GB` (default), `20 GB` o `40 GB` (ZIP >= PST); cancelación si tarda **> 7 días** `[Verificado MS Learn]` |
| **Optimización de Ubicaciones (*Location Optimization*)** | Ejecutar `Generate statistics` antes de exportar limita el procesamiento solo a ubicaciones con coincidencias (`settings.csv`) `[Verificado MS Learn]` | Opera sobre el conjunto estático ya indexado dentro del Azure Storage del *Review set* `[Verificado MS Learn]` |

### 3.5 Integraciones Nativas con el Ecosistema Microsoft

| Solución Integrada | Flujo Operativo de Integración | Valor de Seguridad y Cumplimiento |
| :--- | :--- | :--- |
| **Microsoft Purview Insider Risk Management** | Escalación directa desde un caso de *Insider Risk Management* hacia un nuevo caso de eDiscovery `[Verificado MS Learn]` | Transfiere el contexto de exfiltración o sabotaje interno al equipo jurídico para preservación y revisión probatoria formal `[Verificado MS Learn]` |
| **Microsoft Purview Data Lifecycle Management** | Etiquetas de retención auto-aplicadas a *cloud attachments* y coexistencia con políticas `mbx`/`skp`/`grp` `[Verificado MS Learn]` | Preserva inmutablemente la versión exacta del archivo compartido en el instante del envío `[Verificado MS Learn]` |
| **Microsoft Purview Customer Key (MDEP)** | Cifrado en reposo con claves gestionadas por el cliente (**CMK en preview**) para paquetes de exportación directa `[Verificado MS Learn]` | Extiende la soberanía criptográfica BYOK a los paquetes de exportación generados desde búsquedas `[Verificado MS Learn]` |
| **Microsoft Security Copilot** | Capacidades embebidas en búsquedas (NL2KQL), casos (*Summarize this case*) y *Review sets* (*Summarize item*) `[Verificado MS Learn]` | Acelera drásticamente la formulación de consultas complejas y el triaje documental de contratos, transcripciones y correos `[Verificado MS Learn]` |
| **Microsoft Purview Audit & Microsoft Sentinel** | Registro de actividades eDiscovery (con IP cliente) en `OfficeActivity` / Graph `auditLog` e ingesta SIEM `[Verificado MS Learn]` | Detecta búsquedas abusivas, exportaciones anómalas o modificaciones de permisos por administradores internos `[Decisión / Propuesta Editorial]` |
| **Microsoft Entra ID (Admin Units & B2B Guests)** | Unidades administrativas restringidas en grupos de roles Purview e invitación aprobada de revisores externos B2B `[Verificado MS Learn]` | Asegura segmentación multirregional y colaboración segura con firmas legales externas sin exportar datos `[Verificado MS Learn]` |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Reglas Críticas de Segregación RBAC en eDiscovery

Microsoft Purview gobierna eDiscovery mediante el grupo de roles principal **eDiscovery Manager** (dividido en dos subgrupos: *eDiscovery Manager* y *eDiscovery Administrator*), el grupo **Reviewer** y combinaciones personalizadas de roles unitarios `[Verificado MS Learn]`:

- **Aislamiento entre pares (*eDiscovery Manager*):** Un *eDiscovery Manager* solo puede ver y gestionar los casos que él mismo creó o aquellos a los que fue agregado explícitamente como miembro `[Verificado MS Learn]`. **Ni siquiera el creador de un caso puede remover miembros de un caso** si solo pertenece al subgrupo *eDiscovery Manager* `[Verificado MS Learn]`. Se admiten grupos de seguridad habilitados para correo (*mail-enabled security groups*) en el subgrupo *eDiscovery Manager* (`Add-RoleGroupMember "eDiscoveryManager"`), pero **nunca** en *eDiscovery Administrator* ni como miembros directos de un caso `[Verificado MS Learn]`.
- **Supervisión global restringida (*eDiscovery Administrator*):** Solo usuarios individuales pueden ser designados *eDiscovery Administrator*; pueden ver todos los casos del tenant, configurar ajustes globales (`Settings > eDiscovery`), auto-agregarse a casos huérfanos (por baja del único creador) y remover miembros de casos `[Verificado MS Learn]`.
- **Protección automática contra escalación en casos:** Si se agrega o elimina un rol unitario de un grupo de roles que había sido añadido como miembro de un caso, **Purview remueve automáticamente dicho grupo de roles de todos los casos asociados** para impedir la concesión inadvertida de privilegios adicionales `[Verificado MS Learn]`.
- **Expiración nativa de asignaciones en Purview (Julio 2026):** Aprovechar las asignaciones con fecha de vencimiento en grupos de roles de Microsoft Purview junto con grupos elegibles en **Microsoft Entra PIM** para erradicar privilegios permanentes `[Verificado MS Learn]`.

### 4.2 Matriz Oficial de Roles y Estrategia PIM / JIT

| Rol / Grupo de Roles Oficial | Plano RBAC | Permisos Clave Otorgados | Estrategia de Asignación PIM / JIT Recomendada | Segregación de Funciones (SoD) |
| :--- | :--- | :--- | :--- | :--- |
| **eDiscovery Manager** (Subgrupo) | Purview Portal (`Settings > Role groups`) `[Verificado MS Learn]` | `Case Management`, `Compliance Search`, `Custodian`, `Hold`, `Preview`, `Review`, `Manage review set tags`, `Export`, `RMS Decrypt`, `Communication` (restringido a sus propios casos) `[Verificado MS Learn]` | Elegible vía grupo de seguridad habilitado para correo o asignación temporal por materia legal (máximo 8 h por turno activo) `[Decisión / Propuesta Editorial]` | No puede ver casos ajenos, no puede cambiar ajustes globales ni remover miembros de casos `[Verificado MS Learn]` |
| **eDiscovery Administrator** (Subgrupo) | Purview Portal / PowerShell (`Add-eDiscoveryCaseAdmin`) `[Verificado MS Learn]` | Todos los permisos de *eDiscovery Manager* más visibilidad de **todos los casos**, ajustes globales (`General`, `Analytics`, `Guest users`), reportes globales y remoción de miembros `[Verificado MS Learn]` | **Solo cuentas nominales individuales** (máximo 2-3 custodios senior), activación JIT con aprobación dual y MFA resistente al phishing `[Decisión / Propuesta Editorial]` | Prohibido usar como cuenta operativa diaria de revisión o como principal de servicio de automatización `[Verificado MS Learn]` |
| **Reviewer** (Grupo de roles / Invitados B2B) | Purview Portal / Acceso por caso `[Verificado MS Learn]` | Rol unitario `Review`: acceso de lectura, filtrado, anotación y consulta dentro de los *Review sets* de los casos asignados (sin `Manage review set tags` para invitados) `[Verificado MS Learn]` | Asignación acotada estrictamente a la vigencia del caso; revisión mensual de cuentas B2B externas `[Decisión / Propuesta Editorial]` | Sin capacidad de crear búsquedas in-place, aplicar Holds, gestionar fuentes ni exportar paquetes masivos `[Verificado MS Learn]` |
| **Custom Role Group: Search & Hold Operator** | Purview Portal (`Roles and scopes`) `[Verificado MS Learn]` | Combinación personalizada oficial: `Case Management` + `Compliance Search` + `Custodian` + `Hold` (sin `Preview`, `RMS Decrypt` ni `Export`) `[Verificado MS Learn]` | Activo/Elegible con *Compliance Boundary* regional (`New-ComplianceSecurityFilter`) `[Decisión / Propuesta Editorial]` | Preserva evidencia y ejecuta estimaciones estadísticas sin leer contenido cifrado ni extraer datos del tenant `[Verificado MS Learn]` |
| **Custom Role Group: Production & Export Officer** | Purview Portal (`Roles and scopes`) `[Verificado MS Learn]` | Combinación personalizada oficial: `Case Management` + `Review` + `Export` (con o sin `RMS Decrypt` según autorización legal) `[Verificado MS Learn]` | Elevación JIT bajo ticket de producción legal aprobado por *General Counsel* `[Decisión / Propuesta Editorial]` | Separa a quien revisa y etiqueta documentos de quien descarga paquetes PST/ZIP hacia el exterior `[Decisión / Propuesta Editorial]` |
| **Data Spillage Responder (`Search And Purge`)** | Purview Portal (`Data Investigator` / Custom) `[Verificado MS Learn]` | `Case Management` + `Compliance Search` + `Search And Purge` para ejecutar `purgeData` vía Microsoft Graph sobre correos, Teams o actividad IA `[Verificado MS Learn]` | Estricto JIT (máximo 2 h) con aprobación del CISO y DPO antes de invocar `purgeData` `[Decisión / Propuesta Editorial]` | Prohibido combinar permanentemente con la facultad de apagar *Hold policies* sin control de cuatro ojos `[Decisión / Propuesta Editorial]` |
| **Purview Role Management Admin** | Microsoft Purview / Microsoft Entra ID `[Verificado MS Learn]` | Rol `Role Management` necesario para modificar grupos de roles, asignar *Administrative Units* y aprobar solicitudes de *Guest users* en eDiscovery `[Verificado MS Learn]` | Elegible en Microsoft Entra PIM (máximo 1 h, justificación obligatoria) `[Decisión / Propuesta Editorial]` | No debe ser miembro de casos ni poseer permisos de lectura de evidencia (`Preview` / `Review`) `[Decisión / Propuesta Editorial]` |
| **eDiscovery Graph Automation Service Principal** | Microsoft Entra ID + Purview Service Principal `[Verificado MS Learn]` | Permisos Graph `eDiscovery.Read.All` / `eDiscovery.ReadWrite.All` + `eDiscovery.Download.Read` y membresía en `eDiscoveryManager` (nunca `eDiscovery Administrator`) `[Verificado MS Learn]` | Autenticación exclusiva por certificado alojado en Azure Key Vault; rotación semestral `[Decisión / Propuesta Editorial]` | Restringido a los casos donde el Service Principal sea añadido explícitamente como miembro `[Verificado MS Learn]` |

### 4.3 Desglose Oficial de Roles Unitarios RBAC en Microsoft Purview eDiscovery

Cuando se requiere construir grupos de roles personalizados de mínimo privilegio en `Settings > Roles and scopes > Role groups`, Microsoft Purview expone once roles unitarios específicos para eDiscovery `[Verificado MS Learn]`:

| Rol Unitario RBAC | Capacidad Técnica Exacta Autorizada | Grupos Integrados que lo Incluyen por Defecto |
| :--- | :--- | :--- |
| `Case Management` | Crear, editar, eliminar y administrar acceso a casos; prerrequisito obligatorio antes de ejecutar `Add-eDiscoveryCaseAdmin` `[Verificado MS Learn]` | `eDiscovery Manager`, `Compliance Administrator`, `Organization Management` `[Verificado MS Learn]` |
| `Compliance Search` | Ejecutar búsquedas en Exchange, SharePoint, OneDrive, Teams, M365 Groups y Viva Engage y generar estimaciones estadísticas `[Verificado MS Learn]` | `eDiscovery Manager`, `Compliance Administrator`, `Organization Management` `[Verificado MS Learn]` |
| `Custodian` | Acceder y administrar la pestaña **Data sources** dentro de casos específicos `[Verificado MS Learn]` | `eDiscovery Manager` `[Verificado MS Learn]` |
| `Hold` | Crear, editar, reintentar, apagar y eliminar políticas de retención legal (*Hold policies*) en casos `[Verificado MS Learn]` | `eDiscovery Manager`, `Compliance Administrator`, `Organization Management` `[Verificado MS Learn]` |
| `Preview` | Iniciar acciones de vista previa de muestras de resultados de búsqueda in-place `[Verificado MS Learn]` | `eDiscovery Manager` `[Verificado MS Learn]` |
| `Review` | Acceder a *Review sets*, usar visores (*Source*, *Plain text*, *Annotate*, *Metadata*, *Copilot activity*) y ejecutar filtros/consultas `[Verificado MS Learn]` | `eDiscovery Manager`, `Reviewer` `[Verificado MS Learn]` |
| `Manage review set tags` | Crear jerarquías de etiquetas, *Smart tag groups* y aplicar etiquetas a documentos en *Review sets* (no asignado a *Guest reviewers*) `[Verificado MS Learn]` | `eDiscovery Manager` `[Verificado MS Learn]` |
| `Export` | Exportar resultados de búsquedas o *Review sets* y descargar PDFs individuales desde el visor de revisión `[Verificado MS Learn]` | `eDiscovery Manager` `[Verificado MS Learn]` |
| `RMS Decrypt` | Previsualizar, revisar en *Review sets* y exportar desencriptados correos y archivos protegidos con Azure RMS / etiquetas MIP `[Verificado MS Learn]` | `eDiscovery Manager` (remover en copia personalizada para impedir lectura de cifrados) `[Verificado MS Learn]` |
| `Communication` | Permiso heredado vinculado a flujos de comunicación con custodios `[Verificado MS Learn]` | `eDiscovery Manager` `[Verificado MS Learn]` |
| `Search And Purge` | Eliminar elementos devueltos por una búsqueda (correos, chats Teams o actividad IA vía Graph `purgeData`, máx. 10 ítems/buzón) `[Verificado MS Learn]` | `Organization Management`, `Data Investigator` (NO incluido por defecto en `eDiscovery Manager`) `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Supervisión de Procesos de Larga Duración y Errores en Process Manager
- **Objetivo:** Detectar atascos, cancelaciones por umbral de 7 días o ubicaciones fallidas en búsquedas, cargas a *Review sets*, analítica y exportaciones activas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso Activo] > Process manager` y `eDiscovery > Process report` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Manager / eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Abrir el **Process report** global y los **Process managers** de casos prioritarios marcados como favoritos `[Verificado MS Learn]`.
  2. Filtrar procesos en estado `In progress` (fases *Assessment*, *In progress* o *Catch-up*) y verificar que ninguna exportación supere 5 días de ejecución continua (el servicio cancela automáticamente toda exportación que exceda **7 días**) `[Verificado MS Learn]`.
  3. Identificar búsquedas con ubicaciones fallidas transitorias y ejecutar la acción **Retry failed locations** para reprocesar solo las ubicaciones con error sin reiniciar toda la búsqueda `[Verificado MS Learn]`.
  4. Si una exportación masiva presenta riesgo de timeout, dividir la consulta por rangos de fechas o lotes de custodios `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte `.zip` descargado desde *Process manager* (`Summary.csv`, `Locations.csv`, `Settings.csv`) almacenado en el repositorio del expediente `[Verificado MS Learn]`.

### D-02: Verificación de Aplicación Efectiva de Nuevas Políticas de Retención Legal (Holds)
- **Objetivo:** Confirmar que todo Hold creado en las últimas 24 horas haya transicionado de `In progress` a `On` sin errores por buzón o sitio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Hold policies > [Política] > Details` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Manager / Search & Hold Operator.
- **Procedimiento Paso a Paso:**
  1. Revisar todas las *Hold policies* creadas o editadas hace >= 24 horas (ventana oficial de propagación) `[Verificado MS Learn]`.
  2. Abrir la pestaña **Details** de cada política y verificar que `Hold status` sea `On` en el 100 % de buzones (`Mailbox`) y sitios (`Site`) `[Verificado MS Learn]`.
  3. Ante errores `Distribution group has too many members` (> 1.000 direcciones en motor de hold o > 100 en expansión inicial de lista), `Site inaccessible` (sitio en solo lectura/`NoAccess`) o sitio SharePoint sin título, corregir la causa raíz y ejecutar `Policy actions > Retry policy` `[Verificado MS Learn]`.
  4. Verificar si el custodio utiliza **Copilot Pages** o **Loop** y confirmar que la URL de su contenedor **SharePoint Embedded** esté explícitamente incluida en el Hold `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación CSV de ubicaciones en `Hold policies > Download list` con estado `On` y cero errores `[Verificado MS Learn]`.

### D-03: Triaje de Escalaciones entrantes desde Insider Risk Management y Alertas DLP/IA
- **Objetivo:** Constituir formalmente casos de investigación legal ante escalaciones de riesgo interno o incidentes de fuga de datos en menos de 4 horas hábiles `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Insider Risk Management > Cases` hacia `Solutions > eDiscovery > Cases` `[Verificado MS Learn]`.
- **Rol Responsable:** Insider Risk Lead + eDiscovery Manager.
- **Procedimiento Paso a Paso:**
  1. Validar las escalaciones recibidas desde *Insider Risk Management* o tickets del SOC por derrame de información confidencial en prompts de IA `[Verificado MS Learn]`.
  2. Verificar que el caso creado en eDiscovery tenga asignados exclusivamente los miembros autorizados en `Case settings > Access and permissions` y el número de expediente (*Docket Number*) `[Verificado MS Learn]`.
  3. Mapear en la pestaña **Data sources** al custodio investigado, incluyendo opcionalmente colaboradores frecuentes, manager o grupos propietarios si el mandato legal lo autoriza `[Verificado MS Learn]`.
  4. Activar de inmediato la *Hold policy* preventiva antes de notificar o entrevistar al sujeto `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de creación del caso en Purview Audit y ficha de alcance firmada por Legal/RR.HH. `[Decisión / Propuesta Editorial]`.

### D-04: Control de Ventanas de Caducidad de Paquetes de Exportación (14 y 30 Días)
- **Objetivo:** Evitar la pérdida irreversible de paquetes de exportación directos (caducan a los **14 días**) o de *Review sets* (descarga disponible por **30 días**) y eliminar exportaciones obsoletas con datos sensibles `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Exports` y `Searches` `[Verificado MS Learn]`.
- **Rol Responsable:** Production & Export Officer.
- **Procedimiento Paso a Paso:**
  1. Revisar la pestaña **Exports** de los casos activos e identificar paquetes completados próximos a cumplir 10 días (para exportaciones de búsqueda, que se autodestruyen al día 14) o 25 días (para exportaciones de *Review set*, cuya ventana de descarga vence al día 30) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  2. Descargar los paquetes requeridos hacia el repositorio forense cifrado o ejecutar descarga automatizada vía `Microsoft Purview eDiscovery API` (`exportFileMetadata`) `[Verificado MS Learn]`.
  3. Utilizar la función **Delete search export** sobre exportaciones de búsqueda ya transferidas o innecesarias para minimizar la superficie de exposición de datos sensibles `[Verificado MS Learn]`.
- **Evidencia Auditable:** Hash SHA-256 de los paquetes descargados junto con `Summary.csv` e `Items.csv` `[Decisión / Propuesta Editorial]`.

### D-05: Monitoreo de Actividades Sensibles de eDiscovery en Purview Audit y SIEM
- **Objetivo:** Detectar búsquedas no autorizadas, vistas previas fuera de horario, descargas de PDFs individuales o purgas de datos ejecutadas por cuentas privilegiadas `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit > Search` (o Microsoft Sentinel `OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Compliance Officer.
- **Procedimiento Paso a Paso:**
  1. Consultar eventos diarios bajo el grupo **eDiscovery activities** y **eDiscovery cmdlet activities**, verificando la columna **IP Address** (presente en toda actividad de la experiencia moderna) `[Verificado MS Learn]`.
  2. Auditar específicamente ejecuciones de exportación, descarga individual de PDF en *Review set*, adición de miembros a casos (`Add-eDiscoveryCaseAdmin`) e invocaciones de `purgeData` `[Verificado MS Learn]`.
  3. Correlacionar cada evento con un número de expediente o ticket de cambio válido; escalar como incidente de seguridad cualquier búsqueda sobre buzones VIP/Ejecutivos sin mandato registrado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario de conciliación SIEM / Purview Audit firmado por SecOps `[Decisión / Propuesta Editorial]`.

### D-06: Seguimiento Diario de Acuses de Notificación de Retención Legal (Flujo Complementario)
- **Objetivo:** Garantizar que los custodios sujetos a *Hold* reciban instrucción legal formal y registren su acuse de recibo tras el retiro del módulo clásico de comunicaciones en agosto de 2025 `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Flujo gobernado de Legal Hold (Power Automate / SharePoint List inmutable o plataforma Legal Hold conectada a Graph `legalHolds`) `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** Legal Operations / Paralegal.
- **Procedimiento Paso a Paso:**
  1. Conciliar los nuevos custodios agregados hoy en `Hold policies` contra el registro de avisos legales emitidos (*Issuance notices*) `[Decisión / Propuesta Editorial]`.
  2. Verificar custodios sin acuse tras 5 días hábiles para disparar recordatorios automáticos y escalar al manager directo al día 10 si persiste la falta de respuesta `[Decisión / Propuesta Editorial]`.
  3. Archivar los comprobantes firmados con marca de tiempo UTC dentro del expediente legal del caso `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora de acuses de custodios con timestamp UTC y correlación 1:1 contra `Hold ID` `[Decisión / Propuesta Editorial]`.

### D-07: Supervisión de Solicitudes de Acceso de Revisores Invitados (Guest Users)
- **Objetivo:** Aprobar o rechazar con control estricto las solicitudes pendientes de abogados externos invitados a casos específicos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > eDiscovery > Guest users` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Administrator (con rol `Role Management`).
- **Procedimiento Paso a Paso:**
  1. Revisar solicitudes pendientes en `Settings > eDiscovery > Guest users` verificando nombre completo, correo corporativo, firma legal y justificación documentada `[Verificado MS Learn]`.
  2. Si es la primera vez que el invitado ingresa al tenant, ejecutar el **Paso 1 de aprobación** (creación de cuenta guest en Entra ID, hasta 24 h) y programar el **Paso 2 de aprobación** al caso tras completarse el aprovisionamiento `[Verificado MS Learn]`.
  3. Confirmar que no existan cuentas eliminadas en Entra ID dentro del grupo de roles `Reviewer` (causa oficial de fallo al aprobar invitados) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura de estado en `Settings > eDiscovery > Guest users` y registro en Entra Audit Logs `[Verificado MS Learn]`.

### D-08: Control Diario de Costos Pay-As-You-Go por Datos de IA No-M365 y Graph Export
- **Objetivo:** Evitar cargos inesperados en Azure derivados de incluir inadvertidamente clases de IA no-Microsoft 365 en *Review sets* o exportaciones `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Searches` y `https://portal.azure.com > Cost Management + Billing` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Administrator / FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar las búsquedas en preparación para *Add to review set* o exportación directa y confirmar que, salvo requerimiento explícito del caso, apliquen el filtro `Type > Contains none of > Non M365 AI activity` `[Verificado MS Learn]`.
  2. Revisar la sección *Consumption summary* dentro del archivo `Summary.csv` de los procesos completados en las últimas 24 horas para auditar el volumen exacto en GB de datos IA no-M365 `[Verificado MS Learn]`.
  3. Verificar alertas de presupuesto diario del medidor Purview PAYG en Azure Cost Management `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte `Summary.csv` (*Consumption summary*) y panel de consumo Azure Cost Management `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Auditoría Global del Hold Report (Preview) y Remediación de Políticas Parciales
- **Objetivo:** Conciliar el estado global de todas las políticas de retención legal del tenant considerando el ciclo de sincronización semanal del reporte integrado `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Dashboards > Hold report (preview)` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Acceder a `Hold report (preview)` (que sincroniza estado global cada 3 a 7 días) y descargar el CSV completo mediante **Download report** `[Verificado MS Learn]`.
  2. Filtrar filas con `Policy status` igual a `Applied Partially`, `Released partially` o `Policy failed`, o donde `Rule ID` muestre `Rule not available` `[Verificado MS Learn]`.
  3. Para cada ubicación con `Location error` distinto de `None`, abrir el caso correspondiente, corregir la identidad de buzón/sitio y ejecutar `Retry policy` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Archivo CSV semanal del *Hold report* y registro de remediación de errores `[Verificado MS Learn]`.

### S-02: Sincronización de Fuentes de Datos y Re-expansión de Grupos en Holds Activos
- **Objetivo:** Cerrar la brecha técnica de instantánea puntual (*point-in-time snapshot*) de grupos en Holds y detectar nuevos canales privados o contenedores asociados a custodios `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Data sources` y `Hold policies` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Manager.
- **Procedimiento Paso a Paso:**
  1. En cada caso activo con alta rotación organizacional, ejecutar el control **Sync** en la barra de comandos de fuentes de datos para descubrir nuevos sitios de canales privados de Teams o contenedores asociados `[Verificado MS Learn]`.
  2. Dado que las listas de distribución y grupos M365/Teams en una *Hold policy* capturan su membresía como instantánea estática al crearse, volver a agregar los grupos actualizados (o grupos sombra estáticos sincronizados desde grupos dinámicos Entra) y seleccionar **Apply hold** para re-estampar las ubicaciones `[Verificado MS Learn]`.
  3. Verificar cambios de UPN o renombrado de URLs de OneDrive/SharePoint de custodios y actualizar la política `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de ejecución de `Apply hold` en el *Process manager* de Holds `[Verificado MS Learn]`.

### S-03: Ejecución de Analítica en Review Sets y Validación de Privilegio Abogado-Cliente
- **Objetivo:** Reducir el volumen de revisión humana mediante deduplicación cercana, hilos de correo e identificación asistida por ML de documentos legalmente privilegiados `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Review sets > Manage review set > Run analytics` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Manager / Lead Reviewer.
- **Procedimiento Paso a Paso:**
  1. Verificar en `Case settings > Search & analytics` que estén activos `Near duplicates/email threading`, `Themes`, `Ignore text` (para disclaimers corporativos) y la creación automática de la consulta guardada **For Review** `[Verificado MS Learn]`.
  2. Ejecutar analítica sobre los nuevos lotes incorporados a *Review sets* durante la semana `[Verificado MS Learn]`.
  3. Filtrar por `Is Inclusive = True` o `Has Unique Attachments = True` para priorizar correos inclusivos, y revisar el *Smart tag group* de **Attorney-client privilege** (`AttorneyClientPrivilegeScore`, `HasAttorney`, `IsPrivilege`) para segregar material protegido por secreto profesional antes de cualquier producción `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte del proceso de analítica completado y conteo de documentos etiquetados como `Privileged` / `Non-responsive` `[Verificado MS Learn]`.

### S-04: Evaluación de Ítems Parcialmente Indexados y Remediación de Errores de Procesamiento
- **Objetivo:** Auditar la proporción de elementos parcialmente indexados (~1 % típico por conteo) y remediar archivos protegidos por contraseña en investigaciones críticas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Searches > Statistics` (`Investigate partially indexed items`) `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Manager.
- **Procedimiento Paso a Paso:**
  1. Ejecutar `Generate statistics` marcando `Investigate partially indexed items` en búsquedas de litigios o investigaciones regulatorias de alto impacto `[Verificado MS Learn]`.
  2. Evaluar si se requiere marcar `Perform advanced indexing on partially indexed items` y `Exclude partially indexed items in locations without search hits` al exportar o enviar a *Review set*, recordando que las opciones de tiempo de búsqueda y tiempo de exportación son independientes `[Verificado MS Learn]`.
  3. Identificar archivos con errores de procesamiento (ej. protegidos por contraseña) para ejecutar remediación controlada según protocolo forense `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estadísticas exportadas de ítems parcialmente indexados y `Items.csv` (columna `Added by`: `IndexedQuery`, `UnindexedQuery`, `AdvancedIndex`) `[Verificado MS Learn]`.

### S-05: Revisión de Cierre de Casos, Liberación Controlada de Holds y Purga de Datos PAYG
- **Objetivo:** Liberar retenciones legales concluidas (evitando crecimiento indefinido de `Recoverable Items` y `Preservation Hold Library`) y eliminar casos cerrados con datos IA no-M365 que ya cumplieron su ciclo legal `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases` `[Verificado MS Learn]`.
- **Rol Responsable:** Legal Operations + eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Obtener autorización escrita de *General Counsel* para los asuntos legalmente concluidos en la semana `[Decisión / Propuesta Editorial]`.
  2. Emitir notificación formal de liberación (*Release notice*) a los custodios y ejecutar `Actions > Close case` (verificando que no quede en estado `Closed with errors` por Holds no liberados) `[Verificado MS Learn]`.
  3. Identificar casos cerrados que contengan datos de IA no-Microsoft 365 (los cuales siguen generando cobro diario PAYG mientras el caso exista en estado *Active* o *Closed*) y, si expiró el plazo de preservación probatoria, respaldar reportes y ejecutar `Delete case` para cesar el cargo de almacenamiento `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta de cierre legal firmada y exportación de `Cases > Download list` `[Verificado MS Learn]`.

### S-06: Diagnóstico de Salud de Aplicaciones Empresariales y RBAC (`Diag:edisRBACdiag`)
- **Objetivo:** Prevenir interrupciones operativas por cambios accidentales en políticas de Acceso Condicional, aplicaciones empresariales deshabilitadas o permisos incompletos `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Help (?) > Diag:edisRBACdiag` y `https://portal.azure.com > Enterprise Applications` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Verificar en Microsoft Entra ID que las cuatro aplicaciones (`00000007-...`, `92876b03-...`, `b26e684c-...`, `0d38933a-...`) permanezcan habilitadas para inicio de sesión `[Verificado MS Learn]`.
  2. Ejecutar el diagnóstico integrado `Diag:edisRBACdiag` sobre cuentas operativas que hayan reportado incidencias en búsqueda, vista previa o exportación `[Verificado MS Learn]`.
  3. Validar que ninguna nueva política de Acceso Condicional bloquee flujos de descarga o visores de Office Web en *Review sets* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Resultado de prueba `eDiscovery RBAC Check` sin fallos `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Recertificación de Membresía de eDiscovery Administrators, Managers, Casos y Guests
- **Objetivo:** Garantizar cero deriva de privilegios, auditar casos huérfanos y revocar invitados externos inactivos `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Role groups > eDiscovery Manager`, `Settings > eDiscovery > Guest users` y `https://entra.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO / Purview Role Management Admin + eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Ejecutar `Get-RoleGroupMember -Identity "eDiscoveryManager"` y auditar la lista nominal de *eDiscovery Administrators*, confirmando que no supere el mínimo indispensable (2-3 cuentas) y que no incluya principales de servicio `[Verificado MS Learn]`.
  2. Auditar casos activos cuyo único miembro haya causado baja en la organización; usar un *eDiscovery Administrator* para asignar un nuevo *eDiscovery Manager* responsable y remover al ex-empleado `[Verificado MS Learn]`.
  3. En `Settings > eDiscovery > Guest users`, ejecutar **Remove** sobre abogados externos cuyos casos hayan concluido y limpiar sus cuentas B2B residuales en Microsoft Entra ID `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual de recertificación de accesos y listado exportado de miembros por caso `[Decisión / Propuesta Editorial]`.

### M-02: Actualización de la Lista Oficial de Abogados para Attorney-Client Privilege Detection
- **Objetivo:** Mantener la precisión del atributo `HasAttorney` e `IsPrivilege` frente a altas/bajas del departamento jurídico interno y estudios jurídicos externos de cabecera `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > eDiscovery > Analytics` `[Verificado MS Learn]`.
- **Rol Responsable:** General Counsel Operations + eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Solicitar a Legal Operations el listado actualizado de direcciones SMTP de abogados internos y externos autorizados `[Decisión / Propuesta Editorial]`.
  2. Generar el archivo `.csv` **sin fila de encabezado** (una dirección SMTP por línea) según especificación oficial `[Verificado MS Learn]`.
  3. En `Settings > eDiscovery > Analytics`, verificar que `Attorney-client privilege detection` esté en `On`, cargar el nuevo archivo `.csv` y guardar los cambios `[Verificado MS Learn]`.
- **Evidencia Auditable:** Copia versionada del `AttorneyList_YYYYMM.csv` y evento de configuración en Purview Audit `[Verificado MS Learn]`.

### M-03: Validación de Compliance Boundaries (`ComplianceSecurityFilter`) y Administrative Units
- **Objetivo:** Comprobar técnicamente que los investigadores regionales o por subsidiaria no puedan buscar ni visualizar contenido fuera de su frontera jurisdiccional `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Security & Compliance PowerShell (`Get-ComplianceSecurityFilter`) y `https://purview.microsoft.com > Settings > Roles and scopes` `[Verificado MS Learn]`.
- **Rol Responsable:** Purview Role Management Admin / Compliance Architect.
- **Procedimiento Paso a Paso:**
  1. Listar todos los filtros activos con `Get-ComplianceSecurityFilter` y verificar que ningún grupo de roles asociado sea un "grupo de roles vacío" (configuración ya no soportada; todo grupo con filtro debe tener al menos un rol asignado) `[Verificado MS Learn]`.
  2. Confirmar que los filtros que incluyen reglas SharePoint (`SiteContent_Path`) incluyan explícitamente con operador `-or` el dominio OneDrive (`https://<tenant>-my.sharepoint.com/personal*`) cuando se requiera buscar OneDrive dentro de la agencia `[Verificado MS Learn]`.
  3. Documentar y mitigar la limitación vigente de que las *Compliance Boundaries* no se aplican aún a contenedores **SharePoint Embedded** ni a *Cloud attachments* vinculados desde mensajes dentro del alcance `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salida firmada de `Get-ComplianceSecurityFilter` y prueba sintética cruzada negativa entre agencias `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### M-04: Conciliación de Licenciamiento de Custodios, Shared Mailboxes y Cobertura Cloud Attachments
- **Objetivo:** Asegurar cumplimiento contractual al 100 % en usuarios bajo Hold/Review Set y verificar la salud de la política de auto-etiquetado que preserva versiones compartidas de *Cloud attachments* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.microsoft.com > Billing > Licenses` y `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Label policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Compliance Officer + M365 Licensing Admin.
- **Procedimiento Paso a Paso:**
  1. Cruzar el inventario de ubicaciones activas del *Hold report* contra las licencias asignadas en Entra ID, verificando que ningún usuario F1/F3 sin add-on elegible ni ningún *Shared Mailbox* sin Exchange Online Plan 2 (o Plan 1 + Archiving) figure bajo Hold `[Verificado MS Learn]`.
  2. Confirmar que los custodios en casos con funciones Premium posean Microsoft 365 E5, Purview Suite o E5 eDiscovery & Audit `[Verificado MS Learn]`.
  3. Verificar que la política de auto-aplicación de etiqueta de retención para *cloud attachments* siga activa y procesando sitios SharePoint/OneDrive `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de conciliación de licencias eDiscovery y estado de distribución de política de retención `[Decisión / Propuesta Editorial]`.

### M-05: Higiene del Caso Sistema `Content search` y Plantillas Globales de Etiquetado
- **Objetivo:** Depurar búsquedas históricas heredadas acumuladas en el caso sistema `Content search` y estandarizar las *Tag templates* corporativas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Content Search` y `Settings > eDiscovery > Tag templates` `[Verificado MS Learn]`.
- **Rol Responsable:** eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Revisar los miembros del caso generado por el sistema `Content search` en `Case settings > Access and permissions`, restringiendo el acceso si no todos los *eDiscovery Managers* deben ver búsquedas operativas transversales `[Verificado MS Learn]`.
  2. Eliminar búsquedas obsoletas o de prueba usando la función **Delete search** para mantener higiene operativa `[Verificado MS Learn]`.
  3. Revisar y actualizar en `Settings > eDiscovery > Tag templates` las plantillas reutilizables de revisión (`Responsive`, `Non-Responsive`, `Privileged`, `PII/Redaction Required`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Inventario depurado de búsquedas en `Content search` y catálogo vigente de *Tag templates* `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Simulacro End-to-End de Litigio y Producción Defendible (Incluyendo Copilot y Cloud Attachments)
- **Objetivo:** Validar en un caso controlado de extremo a extremo los tiempos de preservación, recolección de prompts M365 Copilot, captura de versión compartida de *Cloud attachments*, censura PDF (`_burn.pdf`) y exportación auditable `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery` `[Verificado MS Learn]`.
- **Rol Responsable:** Legal Operations + eDiscovery Administrator + SOC L3.
- **Procedimiento Paso a Paso:**
  1. Crear un caso de simulacro sobre cuentas de prueba con interacciones reales de Microsoft 365 Copilot (`IPM.SkypeTeams.Message.Copilot.*`), archivos `.page` en SharePoint Embedded y enlaces compartidos en Teams `[Verificado MS Learn]`.
  2. Ejecutar búsqueda con **Draft a query with Copilot**, cargar resultados a un *Review set* con `Access links (cloud attachments)` e hilos de 12 horas, y ejecutar consultas en **Advanced review set explorer (KQL)** `[Verificado MS Learn]`.
  3. Aplicar una redacción de área en el visor **Annotate**, ejecutar **Commit redactions** para generar `{itemId}_burn.pdf` y exportar marcando `Export redaction` y `Convert supported file formats to HTML`, verificando que el nativo individual sea reemplazado por el PDF censurado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe trimestral de validación EDRM con hashes de paquete exportado y tiempos medidos `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Auditoría de Automatizaciones Microsoft Graph y Certificados de Service Principals
- **Objetivo:** Verificar que todas las integraciones programáticas usen exclusivamente `Microsoft.Graph.Security` (`/v1.0/security/cases/ediscoveryCases`) y `Microsoft Purview eDiscovery API`, con certificados vigentes y mínimo privilegio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://portal.azure.com > App registrations` y registros de Microsoft Graph `[Verificado MS Learn]`.
- **Rol Responsable:** Cloud Security Architect + eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Auditar las aplicaciones registradas con permisos `eDiscovery.Read.All`, `eDiscovery.ReadWrite.All` y `eDiscovery.Download.Read` `[Verificado MS Learn]`.
  2. Confirmar que el Service Principal en Purview pertenezca únicamente a `eDiscoveryManager` y nunca a `eDiscovery Administrator`, y que no existan scripts residuales usando `Connect-IPPSSession` con autenticación *app-only* no soportada `[Verificado MS Learn]`.
  3. Rotar preventivamente certificados próximos a vencer (< 60 días) en Azure Key Vault `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Inventario de *App registrations* eDiscovery y bitácora de llamadas Graph auditadas `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Revisión de Arquitectura de Descifrado, Retención de Buzones Inactivos y Soberanía CMK
- **Objetivo:** Validar el correcto descifrado de etiquetas de sensibilidad MIP (`RMS Decrypt` y `EnablePdfEncryption`), la higiene de `DelayHolds` en buzones inactivos y el estado de CMK para exportaciones directas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-IRMConfiguration`, `Invoke-HoldRemovalAssistant`) y `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Lead + eDiscovery Administrator.
- **Procedimiento Paso a Paso:**
  1. Verificar `Get-IRMConfiguration | fl EnablePdfEncryption` (`$true`) y probar en un *Review set* la visualización de documentos Word/Excel/PDF protegidos con etiquetas de sensibilidad corporativas `[Verificado MS Learn]`.
  2. Auditar buzones inactivos retenidos por antiguos `UniH` o `DelayHoldApplied` usando `Invoke-HoldRemovalAssistant` para depurar aquellos sin obligación legal vigente `[Verificado MS Learn]`.
  3. Si la organización opera con Customer Key (MDEP `PolicyAssigned`), revisar la habilitación de **CMK for direct exports** para proteger paquetes de exportación en reposo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semestral de pruebas criptográficas y depuración de buzones inactivos `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Revisión Ejecutiva del Protocolo Corporativo de Investigaciones Digitales, Privacidad y Retención Legal
- **Objetivo:** Actualizar el manual rector firmado por CISO, *General Counsel*, DPO y RR.HH., alineándolo a cambios regulatorios (GDPR, SEC 17a-4, Ley 21.719 Chile, LFPDPPP México) y novedades de Microsoft Purview `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** Comité Ejecutivo de Gobierno de Datos y `https://purview.microsoft.com > Solutions > Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + General Counsel + DPO.
- **Procedimiento Paso a Paso:**
  1. Evaluar las métricas anuales de desempeño (`KPI-01` a `KPI-08`), hallazgos de auditoría externa y costos acumulados PAYG `[Decisión / Propuesta Editorial]`.
  2. Actualizar las matrices de autorización para búsquedas sobre VIPs, uso de `Search And Purge` en IA generativa y flujos de notificación legal a custodios `[Decisión / Propuesta Editorial]`.
  3. Aprobar el plan anual de formación y recertificación técnica del equipo legal y de cumplimiento (`APL-5007` y `SC-401`) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Política corporativa de eDiscovery vAnual aprobada en directorio y cargada como evidencia en Compliance Manager `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Playbook de Respuesta Rápida ante Derrame de Datos Confidenciales en Prompts/Respuestas de Copilot e IA (`Search & Purge`)
- **Disparador:** Alerta de Purview DLP / DSPM for AI / usuario reportando introducción accidental o maliciosa de secretos industriales, credenciales o datos regulados en Microsoft 365 Copilot, Copilot Studio o apps de IA conectadas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases` + `https://developer.microsoft.com/graph/graph-explorer` (o PowerShell `Invoke-MgGraphRequest` en nubes US Gov) `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Con cuenta miembro de `eDiscovery Manager`, crear un caso dedicado al incidente y una búsqueda acotada al buzón afectado usando la condición `Item class > Copilot activity` (o clase específica como `IPM.SkypeTeams.Message.Copilot.BizChat`), rango horario exacto y palabras clave del derrame `[Verificado MS Learn]`.
  2. Revisar estadísticas (*Top Locations*) y muestra para confirmar que la consulta devuelva **únicamente** los ítems a purgar (límite estricto de **hasta 10 ítems por buzón por ejecución**) `[Verificado MS Learn]`.
  3. Identificar con `Invoke-HoldRemovalAssistant -Identity <UPN>` toda retención o Hold activo sobre el buzón, documentarlos rigurosamente y excluir/suspender temporalmente el Hold (de lo contrario la purga es retenida) `[Verificado MS Learn]`.
  4. Con una cuenta autorizada con el rol `Search And Purge` y permisos Graph `eDiscovery.ReadWrite.All`, obtener `ediscoveryCaseID` y `ediscoverySearchID` e invocar `POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{ediscoveryCaseID}/searches/{ediscoverySearchID}/purgeData` `[Verificado MS Learn]`.
  5. Verificar si el incidente generó una **Copilot Memory** (`IPM.Contact` en `CopilotMemory`) o una **Copilot Page** (`.page` en SharePoint Embedded), eliminándolas por separado dado que borrar el prompt/respuesta no elimina memorias derivadas ni páginas `[Verificado MS Learn]`.
  6. Confirmar que los ítems pasaron a la carpeta oculta `SubstrateHolds` (donde el *timer job* los purga permanentemente en 1 a 7 días) y **reaplicar de inmediato todos los Holds y políticas de retención** documentados en el paso 3 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Código HTTP 202 Accepted de `purgeData`, captura de verificación post-purga y registro en Purview Audit de reaplicación de Holds `[Verificado MS Learn]`.

### AH-02: Playbook de Congelamiento Legal de Emergencia (*Litigation Hold* Inmediato ante Demanda o Investigación Regulatoria)
- **Disparador:** Notificación judicial, requerimiento de ente regulador o investigación de fraude ejecutivo con riesgo inminente de destrucción de evidencia (*spoliation*) `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > Hold policies` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Crear el caso en menos de 1 hora, restringir `Access and permissions` exclusivamente al equipo legal designado y verificar licencias elegibles E5/Purview Suite en todos los custodios objetivo `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  2. En la pestaña **Data sources**, importar los custodios (buzón Exchange, cuenta OneDrive y contenedores **SharePoint Embedded** del usuario para proteger *Copilot Pages* y *Loop*) más los equipos Microsoft Teams (buzón de grupo + sitio SharePoint + sitios de canales privados/compartidos) `[Verificado MS Learn]`.
  3. Crear una **Hold policy** de alcance completo (infinito) sobre dichas ubicaciones y ejecutar **Apply hold** `[Verificado MS Learn]`.
  4. Emitir en paralelo la notificación formal de preservación legal al custodio (salvo orden de investigación silenciosa) y verificar en Exchange PowerShell la presencia del GUID `UniH` en `InPlaceHolds` tras la ventana de propagación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de `Hold policies > Details` en estado `On`, salida de `Get-Mailbox | fl InPlaceHolds` y acuse firmado del custodio `[Verificado MS Learn]`.

### AH-03: Playbook de Respuesta a Solicitudes de Derechos del Titular (DSR — GDPR / Ley 21.719 / LFPDPPP)
- **Disparador:** Solicitud formal de acceso o portabilidad de datos personales presentada por un empleado, ex-empleado o cliente tras la fusión de la antigua herramienta *User Data Search* dentro de eDiscovery `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Crear un caso DSR estandarizado (`DSR-YYYY-NNNN`) asignando solo al equipo de Privacidad/DPO `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  2. Configurar búsqueda usando identificadores exactos del titular, SITs regionales y rango de fechas aplicable; evaluar estadísticas y refinar para minimizar datos de terceros `[Verificado MS Learn]`.
  3. Cargar los resultados pertinentes en un **Review set** para ejecutar *Near-duplicate detection* y utilizar el visor **Annotate** para aplicar **Area redactions** o supresión de texto sobre datos personales de terceras personas involucradas en los mismos documentos `[Verificado MS Learn]`.
  4. Ejecutar **Commit redactions** (`{itemId}_burn.pdf`) y exportar marcando **Export redaction** para entregar únicamente copias censuradas legalmente válidas dentro del plazo legal regulatorio `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete exportado con PDFs censurados (`_burn.pdf`) y `Summary.csv` archivado en el registro de atención de derechos ARCO/DSR `[Verificado MS Learn]`.

### AH-04: Playbook de Recuperación de Caso Huérfano o Revocación de Emergencia de Miembro de Caso
- **Disparador:** Desvinculación abrupta del único *eDiscovery Manager* creador de un caso crítico, o necesidad urgente de retirar a un investigador de un caso sensible `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases > [Caso] > Case settings > Access and permissions` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Activar mediante flujo JIT aprobado una cuenta nominal perteneciente al subgrupo **eDiscovery Administrator** (único rol con visibilidad universal y facultad exclusiva para remover miembros de un caso) `[Verificado MS Learn]`.
  2. Localizar el caso en el dashboard global **Cases**, acceder a `Case settings > Access and permissions` y agregarse temporalmente o agregar al nuevo *eDiscovery Manager* titular `[Verificado MS Learn]`.
  3. Seleccionar **Remove** sobre el usuario desvinculado o revocado y guardar los cambios `[Verificado MS Learn]`.
  4. Desactivar la sesión privilegiada del *eDiscovery Administrator* y auditar el cambio en Purview Audit `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de modificación de membresía del caso en Purview Audit con IP y justificación de cambio `[Verificado MS Learn]`.

### AH-05: Playbook de Diagnóstico y Desbloqueo Forense de Retenciones Fantasma (`Hold Removal Troubleshooting`)
- **Disparador:** Imposibilidad de purgar ítems maliciosos, eliminar un sitio SharePoint/OneDrive o depurar un buzón inactivo pese a haber apagado el Hold visible en el caso `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell / SharePoint Online y `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ejecutar en Exchange Online PowerShell el asistente oficial `Invoke-HoldRemovalAssistant -Identity <UPN o siteUrl>` para inventariar en una sola llamada todas las fuentes de retención activas `[Verificado MS Learn]`.
  2. Inspeccionar `Get-OrganizationConfig | FL InPlaceHolds` y `Get-Mailbox <user> | FL LitigationHoldEnabled,InPlaceHolds,ComplianceTagHoldApplied,DelayHoldApplied,DelayReleaseHoldApplied` `[Verificado MS Learn]`.
  3. Traducir el prefijo identificado a su origen exacto: `UniH` (Hold de caso eDiscovery), `cld` (Cloud attachment hold), `mbx` (política de retención de buzón), `skp` (retención Teams) o `grp` (retención grupo M365) `[Verificado MS Learn]`.
  4. Tener presente que tras retirar un Hold se esperan hasta **240 minutos** de replicación (o hasta 24 h para exclusiones de política `mbx`) y se activa automáticamente un **Delay Hold de 30 días** (`DelayHoldApplied`) que debe gestionarse explícitamente si la eliminación inmediata está autorizada `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salida completa antes y después de `Invoke-HoldRemovalAssistant` adjunta al ticket técnico `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL, KeyQL y Microsoft Graph PowerShell

#### Consulta 1: Detección SIEM de Actividades Críticas de eDiscovery (Exportaciones, Purgas y Cambios de Administración)
- **Plataforma / Tabla:** Microsoft Sentinel / Defender XDR (`OfficeActivity` / `CloudAppEvents`) `[Verificado MS Learn]`.
```kusto
// Audita operaciones críticas en Microsoft Purview eDiscovery moderno (incluyendo IP cliente)
OfficeActivity
| where TimeGenerated > ago(7d)
| where RecordType in ("Discovery", "ComplianceDLPExchange", "ExchangeAdmin")
    or Operation has_any ("eDiscovery", "ComplianceSearch", "CaseHold", "ReviewSet", "PurgeData", "Add-eDiscoveryCaseAdmin", "New-ComplianceSecurityFilter")
| project TimeGenerated, UserId, Operation, ClientIP, ResultStatus, ObjectId, Parameters
| sort by TimeGenerated desc
```

#### Consulta 2: Advanced Review Set Explorer (KQL) — Identificación de Comunicaciones con Destinatarios Externos
- **Plataforma / Tabla:** Purview eDiscovery > Review Set > `Advanced review set explorer (preview)` (`ReviewSetTable`) `[Verificado MS Learn]`.
```kusto
// Extrae ítems del Review Set enviados a dominios externos fuera de la organización
ReviewSetTable
| where isnotempty(Recipients)
| extend Emails = extract_all(@"<([^>]+)>", tostring(Recipients))
| mv-expand Email = Emails
| extend Email = tostring(Email)
| where Email !contains "@contoso.com"
| summarize ExternalRecipients = make_set(Email), ItemCount = count() by ImmutableId, SubjectTitle, Custodian
| sort by ItemCount desc
```

#### Consulta 3: Advanced Review Set Explorer (KQL) — Inventario de Prompts IA, Privilegio Legal y Etiquetas de Sensibilidad
- **Plataforma / Tabla:** Purview eDiscovery > Review Set > `Advanced review set explorer (preview)` (`ReviewSetTable`) `[Verificado MS Learn]`.
```kusto
// Clasifica evidencia en el Review Set por clase de actividad Copilot y detección de privilegio abogado-cliente
ReviewSetTable
| where ItemClass startswith "IPM.SkypeTeams.Message.Copilot" or tostring(IsPrivilege) =~ "true"
| summarize TotalItems = count(), TotalBytes = sum(Size) by ItemClass, tostring(IsPrivilege), tostring(HasAttorney), SensitivityLabel
| sort by TotalItems desc
```

#### Consulta 4: KeyQL — Exclusión FinOps de Datos de IA No-Microsoft 365 Sujetos a Facturación Pay-As-You-Go
- **Plataforma / Tabla:** Purview eDiscovery > Search > `Keyword query language (KeyQL)` `[Verificado MS Learn]`.
```text
(NOT((ItemClass:IPM.SkypeTeams.Message.Copilot.Fabric.*) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.Security.SecurityCopilot) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.BAP*) OR (ItemClass:IPM.SkypeTeams.Message.ConnectedAIApp.*) OR (ItemClass:IPM.SkypeTeams.Message.CloudAIApp.SaaS.*) OR (ItemClass:IPM.SkypeTeams.Message.Copilot.sql.*)))
```

#### Consulta 5: Microsoft Graph PowerShell — Inventario de Casos, Operaciones de Exportación y URLs de Descarga
- **Plataforma / Tabla:** Microsoft Graph PowerShell (`Microsoft.Graph.Security` v1.0) `[Verificado MS Learn]`.
```powershell
# Conecta con identidad delegada o certificado app-only y audita casos y operaciones de exportación
Connect-MgGraph -Scopes "eDiscovery.Read.All"
$cases = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases").value
foreach ($c in $cases) {
    $ops = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/$($c.id)/operations").value
    $exports = $ops | Where-Object { $_.action -in @("exportResult","contentExport") }
    [PSCustomObject]@{
        CaseName    = $c.displayName
        CaseId      = $c.id
        Status      = $c.status
        ExportCount = ($exports | Measure-Object).Count
    }
}
```

#### Consulta 6: Microsoft Graph PowerShell — Ejecución Controlada de `purgeData` para Derrame de Datos en Copilot/IA
- **Plataforma / Tabla:** Microsoft Graph PowerShell (`security/cases/ediscoveryCases/.../purgeData`) `[Verificado MS Learn]`.
```powershell
# Requiere rol 'Search And Purge' en Purview y haber suspendido Holds previamente (máx. 10 ítems/buzón)
Connect-MgGraph -Scopes "eDiscovery.ReadWrite.All"
$caseId   = "00000000-0000-0000-0000-000000000000"
$searchId = "11111111-1111-1111-1111-111111111111"
Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/$caseId/searches/$searchId/purgeData"
```

#### Consulta 7: Exchange Online & Security & Compliance PowerShell — Diagnóstico Integral de Holds y Compliance Boundaries
- **Plataforma / Tabla:** Exchange Online PowerShell / Security & Compliance PowerShell `[Verificado MS Learn]`.
```powershell
# Verifica todas las fuentes de Hold sobre un custodio y lista los filtros de Compliance Boundaries activos
Invoke-HoldRemovalAssistant -Identity "custodio@contoso.com"
Get-Mailbox "custodio@contoso.com" | Format-List LitigationHoldEnabled,InPlaceHolds,ComplianceTagHoldApplied,DelayHoldApplied,DelayReleaseHoldApplied
Get-ComplianceSecurityFilter | Format-Table FilterName,Users,Filters -AutoSize
```

### 10.2 Tabla de Verificación Operativa (*Proof of Life*)

| Componente Verificado | Método de Comprobación Rápida | Estado Esperado ("Proof of Life") |
| :--- | :--- | :--- |
| **Aplicaciones Entra ID Requeridas** | `portal.azure.com > Enterprise Applications` (4 App IDs oficiales) `[Verificado MS Learn]` | Las 4 aplicaciones existen con `Enabled for users to sign-in = Yes` `[Verificado MS Learn]` |
| **Capacidades Premium y Attorney-Client Privilege** | `purview.microsoft.com > Settings > eDiscovery > General / Analytics` `[Verificado MS Learn]` | Capacidades Premium activas y modelo `Attorney-client privilege detection = On` con CSV cargado `[Verificado MS Learn]` |
| **Salud RBAC de Cuentas Investigadoras** | `purview.microsoft.com > Help > Diag:edisRBACdiag` `[Verificado MS Learn]` | Prueba `eDiscovery RBAC Check` superada sin roles faltantes `[Verificado MS Learn]` |
| **Aplicación Efectiva de Holds In-Place** | `Hold policies > Details` + `Get-Mailbox \| fl InPlaceHolds` `[Verificado MS Learn]` | Estado `On` en 100 % de ubicaciones y presencia de prefijo `UniH` / `cld` `[Verificado MS Learn]` |
| **Preservación de Versión Compartida Cloud Attachments** | `Data Lifecycle Management > Label policies` + `Items.csv` (`Is modern attachment = True`) `[Verificado MS Learn]` | Se recolectan tanto la versión viva como la versión compartida bajo el mismo `GroupID` `[Verificado MS Learn]` |
| **Trazabilidad Moderna con IP en Purview Audit** | `Purview > Audit > eDiscovery activities` `[Verificado MS Learn]` | Eventos registrados con dirección IP del cliente poblada en la columna `IP Address` `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs de Excelencia Operacional

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Clasificación |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Efectividad de Aplicación de Holds Legales** | `(Ubicaciones con estado Applied successfully / Total de ubicaciones en Hold policies activas) * 100` | `>= 99.5 %` (remediación < 24 h) | Semanal | General Counsel / Compliance Officer | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tiempo Medio de Congelamiento Probatorio (MTTH)** | `Promedio(Timestamp de Hold en estado On - Timestamp de orden legal formal)` | `<= 4 horas` en casos críticos | Mensual | CISO / General Counsel | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Acuse de Notificación Legal por Custodios** | `(Custodios con acuse firmado registrado / Total de custodios notificados activos) * 100` | `>= 98 %` en <= 10 días hábiles | Semanal | Legal Operations / DPO | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Ratio de Reducción Documental por Analítica (*Culling Rate*)** | `(1 - (Ítems únicos/inclusivos a revisar tras Analytics / Total de ítems ingresados al Review Set)) * 100` | `>= 45 %` en casos > 10.000 ítems | Mensual | General Counsel / FinOps Legal | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo de Contención ante Derrame en IA (`Search & Purge`)** | `Promedio(Timestamp HTTP 202 de purgeData + reaplicación de Holds - Timestamp de detección)` | `<= 2 horas` | Por incidente / Mensual | CISO / SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Cumplimiento de Segregación `eDiscovery Administrator`** | `Conteo de cuentas nominales en subgrupo eDiscovery Administrator` | `<= 3 cuentas` (0 Service Principals) | Mensual | CISO / Auditoría Interna | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Cumplimiento en Plazo de Solicitudes DSR / Regulatorias** | `(Casos DSR y regulatorios producidos con redacción validada dentro del SLA legal / Total casos) * 100` | `100 %` | Mensual | DPO / Comité de Riesgos | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Higiene de Exportaciones y Costo PAYG No Planificado** | `Exportaciones vencidas sin descargar (> 14 d) + Variación no autorizada en gasto PAYG IA no-M365` | `0 exportaciones perdidas` / `<= 5 %` desvío | Mensual | FinOps / eDiscovery Admin | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Observables |
| :--- | :--- | :--- |
| **Nivel 1** | **Inicial / Reactivo** | Uso improvisado del caso `Content search` sin gestión estructurada de casos; exceso de usuarios en `Organization Management` o `eDiscovery Administrator`; sin cobertura de contenedores *SharePoint Embedded* ni exclusión de costos PAYG. |
| **Nivel 2** | **Repetible / Básico** | Creación de casos individuales y aplicación de *Hold policies*, pero sin auto-etiquetado de retención para versiones compartidas de *Cloud attachments*, sin seguimiento formal de acuses de custodios post-agosto 2025 ni validación sistemática del *Hold report*. |
| **Nivel 3** | **Definido / Estandarizado** | Segregación estricta `eDiscovery Manager` vs. `eDiscovery Administrator`, *Compliance Boundaries* activas, uso estándar de *Review sets* con OCR, hilos de 12 h, *Near-duplicates*, *Email threading* y censura PDF confirmada (`_burn.pdf`). |
| **Nivel 4** | **Gestionado / Cuantificado** | Cobertura forense integral de M365 Copilot, Copilot Pages y `Search & Purge` vía Graph; modelo *Attorney-client privilege* entrenado con lista mensual de abogados; consultas avanzadas KQL en *Advanced review set explorer* y monitoreo SIEM de actividades eDiscovery. |
| **Nivel 5** | **Optimizado / Asistido por IA y Código** | Automatización segura mediante `Microsoft.Graph.Security` con certificados en Key Vault, adopción de **Security Copilot** (NL2KQL y resúmenes contextuales), CMK habilitado en exportaciones directas y simulacros trimestrales auditados bajo NIST CSF 2.0. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

| Función NIST CSF 2.0 | Subcategoría Oficial (CSWP 29) | Táctica / Técnica MITRE ATT&CK Relacionada | Capacidad Habilitadora en Microsoft Purview eDiscovery | Evidencia Auditable Reproducible `[Decisión / Propuesta Editorial]` |
| :--- | :--- | :--- | :--- | :--- |
| **GOVERN (GV)** | `GV.OC-03` (Requisitos legales, regulatorios y contractuales comprendidos y gestionados) | N/A (Gobierno normativo) | Gestión centralizada de casos de litigio, auditorías regulatorias y solicitudes DSR en el portal moderno unificado | Inventario exportado `Cases > Download list` con número de expediente y mandato legal asociado |
| **GOVERN (GV)** | `GV.RR-02` (Roles, responsabilidades y autoridades establecidos y aplicados) | `T1078.004` (Valid Accounts: Cloud Accounts) | Segregación entre `eDiscovery Manager`, `eDiscovery Administrator`, `Reviewer` y `Compliance Boundaries` (`New-ComplianceSecurityFilter`) | Salida de `Get-RoleGroupMember`, `Get-ComplianceSecurityFilter` y reporte `Diag:edisRBACdiag` |
| **IDENTIFY (ID)** | `ID.AM-07` (Inventarios de datos y metadatos designados mantenidos) | `T1213` (Data from Information Repositories) | Mapeo unificado de fuentes custodiadas y no custodiadas (Exchange, SharePoint, OneDrive, Teams, Viva Engage y SharePoint Embedded) | Pestaña `Data sources` del caso y reporte `Locations.csv` del *Process manager* |
| **IDENTIFY (ID)** | `ID.RA-05` (Amenazas, vulnerabilidades, probabilidad e impacto usados para priorizar riesgo) | `T1530` (Data from Cloud Storage) | Evaluación temprana con estadísticas de búsqueda, detección de privilegio abogado-cliente (`IsPrivilege`) y **Advanced review set explorer (KQL)** | Reportes `Summary.csv`, `Query Report` y metadatos `AttorneyClientPrivilegeScore` |
| **PROTECT (PR)** | `PR.AA-05` (Permisos de acceso, autorizaciones y derechos gestionados por mínimo privilegio) | `T1098` (Account Manipulation) | Membresía explícita por caso, remoción automática de grupos de roles alterados, *Administrative Units* y aprobación en dos pasos para *Guest users* | Configuración de `Case settings > Access and permissions` y bitácora `Settings > eDiscovery > Guest users` |
| **PROTECT (PR)** | `PR.DS-01` (Confidencialidad, integridad y disponibilidad de datos en reposo protegidas) | `T1485` (Data Destruction) | Preservación inmutable in-place mediante `Hold policies` (`UniH`, `cld`), censura en línea (`_burn.pdf`) y **CMK para exportaciones directas** | `Hold report (preview)`, salida de `Invoke-HoldRemovalAssistant` y paquetes exportados con `Export redaction` |
| **DETECT (DE)** | `DE.CM-03` (Actividades del personal y uso de tecnología monitoreados para detectar eventos adversos) | `T1114.002` (Email Collection: Remote Email Collection) | Auditoría detallada con IP cliente de todas las búsquedas, vistas previas, descargas y cambios de caso en Purview Audit (`OfficeActivity`) | Reglas de detección en Microsoft Sentinel sobre operaciones `eDiscovery` y registros de Purview Audit |
| **DETECT (DE)** | `DE.AE-02` (Eventos potencialmente adversos analizados para comprender actividades asociadas) | `T1567` (Exfiltration Over Web Service) | Correlación de alertas escaladas desde *Insider Risk Management* con comunicaciones Teams (+/- 12 h), *Cloud attachments* y prompts de Copilot | Expediente de caso escalado desde IRM con transcripciones HTML de Teams y *Copilot activity view* |
| **RESPOND (RS)** | `RS.AN-03` (Análisis ejecutado para establecer qué ocurrió durante un incidente y su causa raíz) | `T1005` (Data from Local System / Cloud Repositories) | Reconstrucción forense en *Review sets* con OCR, descifrado MIP (`RMS Decrypt`), *Email threading* y resúmenes asistidos por **Security Copilot** | Conjuntos de revisión etiquetados, notas de investigación y reportes `Items.csv` |
| **RESPOND (RS)** | `RS.MI-01` (Incidentes contenidos) | `T1565` (Data Manipulation / Data Spillage) | Contención y erradicación quirúrgica de derrames de datos sensibles en correos, Teams o actividad IA vía `Search & Purge` (`purgeData`) | Respuesta HTTP 202 del endpoint Graph `purgeData` y verificación post-purga en búsqueda |
| **RECOVER (RC)** | `RC.RP-04` (Funciones críticas del negocio y controles de seguridad restaurados tras acciones correctivas) | `T1490` (Inhibit System Recovery) | Reaplicación verificada de *Hold policies* y políticas de retención inmediatamente después de completar una purga de emergencia en buzón | Registro de auditoría de reaplicación de Hold y estado `On` verificado en `Hold policies > Details` |
| **RECOVER (RC)** | `RC.CO-03` (Actividades de recuperación y resultados comunicados a partes interesadas internas y externas) | N/A (Comunicación post-incidente y regulatoria) | Producción formal defendible de paquetes exportados con reportes íntegros (`Summary.csv`, `Items.csv`, `Export report`) hacia reguladores o tribunales | Paquete de producción firmado criptográficamente y acta de cierre/liberación de caso |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta Oficial Microsoft Learn / Credenciales Vigentes (Nov 2026) | Recursos Ninja Training y Comunidad MVP | Práctica de Laboratorio Exigida `[Decisión / Propuesta Editorial]` |
| :--- | :--- | :--- | :--- |
| **eDiscovery Manager / Investigador Legal** | Módulo *Search for content with Microsoft Purview eDiscovery* + Credencial **Microsoft Applied Skills: Implement retention, eDiscovery, and Communication Compliance in Microsoft Purview (`APL-5007`)** `[Verificado MS Learn]` | **Microsoft Purview eDiscovery Ninja Guide** (`https://aka.ms/ediscoveryninja`) + Guías interactivas CloudGuides de diseño de búsqueda y exportación `[Verificado MS Learn]` | Ejecutar un caso completo con *Condition builder*, KeyQL, *Cloud attachments* y *Review set* con censura `_burn.pdf`. |
| **eDiscovery Administrator / Compliance Architect** | Certificación **Microsoft Certified: Information Security Administrator Associate (`SC-401`)** + Documentación oficial de `Compliance Boundaries`, RBAC y `Hold Removal Assistant` `[Verificado MS Learn]` | Análisis técnicos de transición moderna 2025-2026 por **Tony Redmond** (*Office 365 for IT Pros*) y **Joanne Klein** (retención y versiones compartidas) `[Verificado MS Learn]` | Configurar `New-ComplianceSecurityFilter` para dos agencias, diagnosticar con `Diag:edisRBACdiag` y auditar `Invoke-HoldRemovalAssistant`. |
| **Analista SecOps / Data Spillage Responder** | Guía oficial *Search for and delete AI application data in eDiscovery* + *Use Microsoft Purview APIs for eDiscovery* `[Verificado MS Learn]` | Blog oficial de Ingeniería Microsoft *Collecting Microsoft 365 Copilot Data with Microsoft Purview eDiscovery* (mayo 2026) `[Verificado MS Learn]` | Simular un derrame en Copilot Chat, ejecutar `purgeData` vía Graph en entorno de pruebas y reaplicar Holds verificando `SubstrateHolds`. |
| **Revisor Legal Interno / Externo (Reviewer)** | Guía oficial *Group and view items in a review set* + *Search content with Advanced review set explorer (KQL)* + *Security Copilot in Purview* `[Verificado MS Learn]` | Podcast y briefings *All Things M365 Compliance* (**Nikki Chapple** y **Ryan John Murphy**) sobre flujos EDRM en M365 `[Verificado MS Learn]` | Revisar lotes usando `Is Inclusive`, *Smart tags* de privilegio abogado-cliente, resúmenes de Security Copilot y consultas básicas en `ReviewSetTable`. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Verificadas contra Microsoft Learn MCP (`2026-11-11`)

| # | Área Técnica | Hallazgo Verificado a Corte `2026-11-11` | Impacto en la Guía Operacional |
| :--- | :--- | :--- | :--- |
| **1** | **Retiro de Experiencias Clásicas y Exportación PowerShell (Mayo-Agosto 2025)** | Microsoft deshabilitó los parámetros `-Export` y `-ChangeExportKey` en `New/Get/Set-ComplianceSearchAction` desde el **26 de mayo de 2025** (MC1055528) y retiró todas las experiencias clásicas (*Content Search*, *Standard* y *Premium* clásicas) el **31 de agosto de 2025** `[Verificado MS Learn]`. | Se erradicó toda referencia al portal clásico y a exportaciones PowerShell heredadas, estandarizando en el portal `purview.microsoft.com` y Microsoft Graph API. |
| **2** | **Retiro del Flujo Clásico Integrado de Hold Notifications** | El artículo oficial `ediscovery-create-hold-notification` quedó restringido únicamente a *21Vianet China* tras el retiro del 31-ago-2025; la experiencia moderna conserva *Hold policies* y *Hold report*, sin la pestaña clásica *Communications* `[Verificado MS Learn]`. | Se documentó con transparencia arquitectónica la separación entre la preservación técnica nativa y la orquestación complementaria de avisos/acuses legales. |
| **3** | **Arquitectura Diferenciada de Datos Copilot, Memories y Pages (2026)** | Prompts/respuestas viven en el buzón (`IPM.SkypeTeams.Message.Copilot.*`), pero **Copilot Memories** (`IPM.Contact`) no son retenidas por Holds/políticas de retención y **Copilot Pages** (`.page`) residen en contenedores **SharePoint Embedded** no cubiertos por el Hold de buzón `[Verificado MS Learn]`. | Se incorporaron controles obligatorios en `D-02`, `AH-01` y `AH-02` para incluir URLs SharePoint Embedded y purgar memorias/páginas por separado. |
| **4** | **Nuevo Modelo Híbrido de Facturación PAYG para IA No-M365 y Graph E3** | El almacenamiento en casos activos/cerrados (*Review sets* y exportaciones) de clases `IPM.SkypeTeams.Message.Copilot.Fabric.*`, `SecurityCopilot`, `ConnectedAIApp.*` y `CloudAIApp.SaaS.*` incurre en facturación diaria Azure PAYG hasta eliminar el caso `[Verificado MS Learn]`. | Se añadieron la consulta KeyQL oficial de exclusión, la actividad diaria `D-08` y la depuración semanal `S-05`. |
| **5** | **Advanced Review Set Explorer (KQL) y Redacción Confirmada (`_burn.pdf`)** | Los *Review sets* incorporan en vista previa consultas KQL en tiempo real sobre `ReviewSetTable` y el visor *Annotate* exige ejecutar **Commit redactions** para generar `{itemId}_burn.pdf` y marcar `Export redaction` `[Verificado MS Learn]`. | Se añadieron consultas KQL nativas sobre `ReviewSetTable` en la Sección 10 y procedimientos exactos de censura en `T-01` y `AH-03`. |
| **6** | **Desoporte de Autenticación App-Only en Security & Compliance PowerShell** | Microsoft Learn declara explícitamente como **no soportada** la autenticación *app-only* (CBA) para cmdlets de eDiscovery en `Connect-IPPSSession`, instruyendo migrar automatizaciones a Microsoft Graph `[Verificado MS Learn]`. | Se prohibió el uso de nuevos scripts desatendidos en IPPS para eDiscovery y se estandarizó en `Microsoft.Graph.Security` con Service Principal en `eDiscoveryManager`. |
| **7** | **Renombre de Suite a Microsoft Purview Suite y Retiro Futuro de `Search-UnifiedAuditLog`** | Desde el 1 de octubre de 2025 *M365 E5 Compliance* se denomina **Microsoft Purview Suite**, y en octubre de 2026 (MC1505599) se anunció la GA de Graph `AuditLogQuery` y el retiro de `Search-UnifiedAuditLog` para el 15-oct-2027 `[Verificado MS Learn]`. | Se actualizó la nomenclatura de licenciamiento y se priorizaron consultas KQL/`OfficeActivity` y Microsoft Graph. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Diseñado | Clasificación | Justificación Arquitectónica y de Gobierno |
| :--- | :--- | :--- | :--- |
| **1** | **Flujo Complementario de Notificación y Acuse Legal de Custodios (`D-06`)** | `Propuesta Editorial` | Al haberse retirado en agosto de 2025 el flujo clásico de *Custodian Communications*, las áreas legales requieren un mecanismo auditable (Power Automate/SharePoint + Graph `legalHolds` o solución Legal Hold dedicada) para demostrar diligencia de notificación ante tribunales. |
| **2** | **Tope Máximo de <= 3 Cuentas Nominales en `eDiscovery Administrator` (`KPI-06`)** | `Propuesta Editorial` | Dado que este rol visualiza todos los casos del tenant y puede auto-agregarse a investigaciones confidenciales de directorio o C-Level, limitar su asignación nominal y exigir JIT reduce drásticamente el riesgo de abuso interno. |
| **3** | **SLAs Operativos (`MTTH <= 4 h`, `Search & Purge <= 2 h`, Descarga proactiva al día 10/25)** | `Propuesta Editorial` | Microsoft define límites técnicos (propagación de Hold <= 24 h, expiración de exportación a 14 y 30 días), pero fijar umbrales internos anticipados evita expiraciones accidentales y pérdida de evidencia. |
| **4** | **Exclusión por Defecto de `Non M365 AI activity` salvo Mandato Expreso (`D-08`)** | `Propuesta Editorial` | Previene sobrecostos mensuales acumulativos en Azure PAYG originados por búsquedas amplias de buzón que arrastran telemetría de Fabric Copilot o Security Copilot irrelevante para el litigio. |
| **5** | **Mapeo Probatorio a las 6 Funciones de NIST CSF 2.0 y Modelo de Madurez de 5 Niveles** | `Propuesta Editorial` | Traduce controles técnicos de Purview eDiscovery al lenguaje de auditoría corporativa CSWP 29 para facilitar evaluaciones integradas del CISO y Auditoría Interna. |

---

## 15. Directorio de Referencias Públicas Verificadas

| ID | Título del Recurso | URL Verificada | Tipo de Fuente | Autor / Entidad | Comentario de Verificación (Nov 2026) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REF-01** | Learn about eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc` | Microsoft Learn | Microsoft Corporation | Arquitectura unificada moderna, cambios frente a versión clásica y tabla comparativa Standard vs. Premium (actualizado oct-2026). |
| **REF-02** | Microsoft Purview eDiscovery legacy solutions | `https://learn.microsoft.com/en-us/purview/ediscovery` | Microsoft Learn | Microsoft Corporation | Confirma el retiro global el 31 de agosto de 2025 de *Content Search*, *Standard* y *Premium* clásicos (excepto 21Vianet). |
| **REF-03** | Get started with eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-get-started` | Microsoft Learn | Microsoft Corporation | Prerrequisitos de licencias (incluyendo SharePoint E3), 4 Enterprise Apps obligatorias y configuración inicial. |
| **REF-04** | Assign permissions in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-permissions` | Microsoft Learn | Microsoft Corporation | Matriz oficial de roles RBAC, diferencias `eDiscovery Manager` vs. `Administrator`, `Diag:edisRBACdiag` y desoporte de CBA en IPPS (sep-2026). |
| **REF-05** | Search for and delete AI application data in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-search-copilot-data` | Microsoft Learn | Microsoft Corporation | Tabla oficial de `ItemClass` de Copilot/IA, encabezados `From`/`To`, límite de 10 ítems/buzón y flujo Graph `purgeData` (jun-2026). |
| **REF-06** | Create a search for a case in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-search-query` | Microsoft Learn | Microsoft Corporation | Reglas sintácticas KeyQL, soporte preview de contenedores SharePoint Embedded y *Draft a query with Copilot* (sep-2026). |
| **REF-07** | Create holds in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-hold-create` | Microsoft Learn | Microsoft Corporation | Requisitos de licencia en usuarios objetivo de Hold, instantánea puntual de grupos y preservación en Teams (jun-2026). |
| **REF-08** | Manage hold policies for eDiscovery cases | `https://learn.microsoft.com/en-us/purview/edisc-hold-manage` | Microsoft Learn | Microsoft Corporation | Uso de `Invoke-HoldRemovalAssistant`, prefijos `UniH`/`cld`/`mbx`/`skp`/`grp` y `DelayHoldApplied` (jun-2026). |
| **REF-09** | Use the hold report in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-hold-report` | Microsoft Learn | Microsoft Corporation | Reporte global en preview de políticas de Hold, estados de aplicación y ventana de sincronización de 3 a 7 días. |
| **REF-10** | Cloud attachments in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-cloud-attachments` | Microsoft Learn | Microsoft Corporation | Límites de extracción (50 enlaces, 2.048 chars) y preservación de versión compartida con etiquetas de retención auto-aplicadas. |
| **REF-11** | Group and view items in a review set in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-review-set-view` | Microsoft Learn | Microsoft Corporation | Agrupación por `GroupID`/`ThreadID`, visor *Copilot activity*, censura confirmada (`_burn.pdf`) y resúmenes con Security Copilot (jun-2026). |
| **REF-12** | Search content in a review set with the Advanced review set explorer (preview) | `https://learn.microsoft.com/en-us/purview/edisc-review-set-explorer` | Microsoft Learn | Microsoft Corporation | Consultas KQL en tiempo real sobre `ReviewSetTable`, operadores soportados y límite de 10.000 filas (jun-2026). |
| **REF-13** | Configure analytics settings in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-settings-analytics` | Microsoft Learn | Microsoft Corporation | Configuración del modelo ML `Attorney-client privilege detection`, CSV de abogados y *Smart tag groups* (jun-2026). |
| **REF-14** | Export search results & Export items from a review set in eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-search-export` | Microsoft Learn | Microsoft Corporation | Caducidad de 14 días en búsquedas vs. 30 días en *Review sets*, CMK en preview para exportaciones directas y tamaños PST/ZIP (oct-2026). |
| **REF-15** | Billing in eDiscovery & Use Microsoft Purview APIs for eDiscovery | `https://learn.microsoft.com/en-us/purview/edisc-billing` | Microsoft Learn | Microsoft Corporation | Modelo de cobro PAYG para datos IA no-M365 y Graph Export API en E3, más arquitectura `Microsoft.Graph.Security`. |
| **REF-16** | Collecting Microsoft 365 Copilot Data with Microsoft Purview eDiscovery | `https://techcommunity.microsoft.com/blog/microsoft-security-blog/collecting-microsoft-365-copilot-data-with-microsoft-purview-ediscovery/4516489` | Blog Oficial Microsoft | Microsoft Security Blog | Guía oficial de ingeniería sobre Prompts, Copilot Memories (`IPM.Contact`), Copilot Pages (`.page`) y agente Facilitator (may-2026). |
| **REF-17** | What's New in Microsoft Purview eDiscovery | `https://techcommunity.microsoft.com/blog/microsoft-security-blog/what%E2%80%99s-new-in-microsoft-purview-ediscovery/4441676` | Empleado Microsoft | Aaron Thorp (Microsoft) | Detalla mejoras modernas de reportes (`Added by`, `Summary.csv`), *Create a hold from search* y *Retry failed locations* (ago-2025). |
| **REF-18** | Important Purview eDiscovery Changes Take Effect in May 2025 | `https://office365itpros.com/2025/04/17/purview-ediscovery-may2025/` | MVP Seguridad | Tony Redmond (M365 MVP) | Análisis independiente del retiro de `-Export` en PowerShell (MC1055528, 26-may-2025) y migración al caso `Content Search`. |
| **REF-19** | The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29) & EDRM 2.0 Model | `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf` | Marco Normativo | NIST / EDRM.net | Marco normativo base para el mapeo de controles `GV`, `ID`, `PR`, `DE`, `RS`, `RC` y ciclo de vida probatorio EDRM. |

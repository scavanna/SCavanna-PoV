# Guía Maestra de Excelencia Operacional: Microsoft Purview Information Protection (Sensitivity Labels, Clasificación, Cifrado y Scanner)

## 1. Portada y Ficha de Control Documental

| Campo | Valor |
|---|---|
| **Identificador del Módulo** | `14_Purview_Information_Protection` |
| **Slug Canónico** | `Purview_Information_Protection` |
| **Nombre Completo** | Microsoft Purview Information Protection (Sensitivity Labels, Clasificación, Cifrado y Scanner) |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | Compilado MSEOP-MD (`Purview IP`: `Version Consolidada (1)`, `0404 - Purview IP - Bloques - SecOps`, `MIP Lic VC`, `MIP NIST VC`) + Cruce `Ninja Training 2026 (05_Purview_Information_Protection)` + Revalidado contra Microsoft Learn MCP |
| **Relación con Microsoft 365 E5** | Incluido en Microsoft 365 E5 / Microsoft Purview Suite (capacidades avanzadas de auto-labeling, DKE, EDM, Trainable Classifiers y Dynamic Watermarking; etiquetado manual base en M365 E3) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com`, `https://security.microsoft.com`, `https://admin.microsoft.com`, `https://entra.microsoft.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Data Security Architect, Information Protection Admin, SOC Manager, SOC L1, SOC L2, SOC L3 / Detection Engineer, Collaboration Admin (SharePoint/Teams/Exchange), Data Owners, GRC / Legal & Privacy |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), Arquitectura Zero Trust de Microsoft (Pilar Data), MITRE ATT&CK Enterprise, Microsoft Cloud Security Benchmark (MCSB v2 — Data Protection) |

> **Nota de Consolidación y Trazabilidad (Noviembre 2026):** Este documento consolida y depura en una única guía maestra operativa el corpus local de `MSEOP-MD\Purview IP` (modelo operativo SecOps de actividades recurrentes y ad-hoc, auditoría técnica de los 11 bloques infográficos, matrices de licenciamiento Enterprise/AIP y mapeo probatorio NIST CSF 2.0) junto con la curaduría de `Ninja_Training_Seguridad_Microsoft_2026\05_Purview_Information_Protection`, revalidando cada afirmación técnica contra Microsoft Learn al `2026-11-11`. Se distinguen estrictamente las capacidades, límites, rutas y licencias oficiales mediante `[Verificado MS Learn]` frente a SLAs, umbrales cuantitativos, KPIs, frecuencias y criterios de diseño consultivo mediante `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026

Microsoft Purview Information Protection (antes conocido como Microsoft Information Protection o MIP) constituye el plano fundacional de seguridad centrada en el dato (*data-centric security*) dentro del ecosistema Microsoft `[Verificado MS Learn]`. Su propósito arquitectónico es descubrir, clasificar, etiquetar y proteger la información sensible a lo largo de todo su ciclo de vida —en reposo, en tránsito y en uso— mediante metadatos persistentes (**Sensitivity Labels**) y cifrado basado en identidad (**Azure Rights Management / Azure RMS**), de modo que la protección viaje con el archivo o mensaje incluso fuera del perímetro corporativo `[Verificado MS Learn]`.

A noviembre de 2026, la operación empresarial de Purview Information Protection está marcada por seis transformaciones técnicas verificadas que todo CISO y arquitecto de seguridad debe gobernar:

1. **Adopción del esquema moderno de etiquetas (Label Groups):** Para todos los tenants creados a partir del 1 de octubre de 2025 (y mediante migración irreversible asistida en tenants existentes), los **Label groups** reemplazan la jerarquía clásica de etiquetas padre con subetiquetas. Un grupo de etiquetas solo admite nombre, descripción, color y prioridad, eliminando conflictos de herencia de cifrado o ámbitos dispares `[Verificado MS Learn]`.
2. **Consolidación del etiquetado nativo (Built-in Labeling) y retiro definitivo del add-in clásico AIP:** Tras el retiro del complemento *Azure Information Protection Unified Labeling add-in* para Office (abril de 2024), toda operación de escritorio en Word, Excel, PowerPoint y Outlook se ejecuta exclusivamente sobre el etiquetado integrado nativo en Microsoft 365 Apps, reservándose el **Microsoft Purview Information Protection client** (rama 3.2.x) para etiquetado desde el Explorador de archivos de Windows, visor de archivos protegidos, cmdlets PowerShell locales y el **Information Protection Scanner** en Windows Server `[Verificado MS Learn]`.
3. **Escalamiento del auto-etiquetado en servicio y soporte nativo de PDF:** El techo máximo agregado de procesamiento de políticas de auto-etiquetado del lado del servicio (*service-side auto-labeling*) para SharePoint Online y OneDrive alcanza hasta **500.000 archivos por tenant por día** (con simulaciones de hasta 20.000.000 de archivos coincidentes y hasta 100 políticas por tenant), requiriendo habilitar explícitamente el soporte de etiquetado PDF (`EnableSensitivityLabelforPDF = True`) para no omitir documentos PDF `[Verificado MS Learn]`.
4. **Gobierno de contenedores y modelo Secure by Default:** Las etiquetas de sensibilidad se extienden a contenedores colaborativos (**Microsoft Teams, Microsoft 365 Groups, SharePoint Sites, Loop Workspaces y comunidades de Viva Engage**) para imponer privacidad, bloqueo o control de invitados, vínculos compartidos y restricciones de dispositivos no administrados vía contextos de autenticación de Microsoft Entra Conditional Access, complementadas con etiquetas predeterminadas por biblioteca de documentos en SharePoint `[Verificado MS Learn]`.
5. **Control criptográfico para cargas IA y agentes (Microsoft 365 Copilot y Agent 365):** Microsoft 365 Copilot, Copilot Chat y los agentes respetan tanto los permisos de acceso como las etiquetas de sensibilidad y derechos de uso RMS. Cuando una etiqueta aplica cifrado, Copilot solo procesa y devuelve el contenido si el usuario posee simultáneamente los derechos `VIEW` y `Copy and extract content (EXTRACT)` (o es el *Rights Management issuer/owner*), heredando automáticamente la etiqueta de mayor prioridad en el contenido generado y respetando el bloqueo explícito `BlockContentAnalysisServices` `[Verificado MS Learn]`.
6. **Extensión multicloud y analítica (Microsoft Fabric, Power BI y Purview Data Map):** La misma taxonomía de etiquetas gobierna modelos semánticos, informes, paneles y exportaciones en **Microsoft Fabric / Power BI**, así como columnas SQL y archivos en **Azure Storage (ADLS Gen2 / Azure Files)** y **Amazon S3 / RDS** mediante **Microsoft Purview Data Map** bajo facturación de pago por uso (PAYG) `[Verificado MS Learn]`.

### 2.2 Matriz de Licenciamiento y Prerrequisitos (Corte Noviembre 2026)

Aunque muchas características de Purview operan como servicios a nivel de tenant (*tenant-level services*), los derechos de uso y administración exigen licenciamiento por usuario beneficiado `[Verificado MS Learn]`. Desde octubre de 2025, el add-on *Microsoft 365 E5 Compliance* se comercializa oficialmente en la descripción de servicio como **Microsoft Purview Suite**, y desde el 1 de mayo de 2026 existe **Microsoft 365 E7** junto con **Microsoft Agent 365** para cargas agénticas `[Verificado MS Learn]`.

| Capacidad / Función Operativa | M365 E3 / O365 E3 / EMS E3 | EMS E5 | M365 E5 / O365 E5 / Microsoft Purview Suite (ex E5 Compliance) | M365 E5 Info Protection & Governance / AIP P2 | Notas y Dependencias Críticas |
|---|---|---|---|---|---|
| **Etiquetado manual, predeterminado de política y obligatorio** (Office, Outlook, SharePoint, OneDrive) | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Requiere habilitar integración de etiquetas en SharePoint/OneDrive y coautoría para archivos cifrados `[Verificado MS Learn]`. |
| **Cifrado persistente Azure RMS, User-Defined Permissions (UDP), Do Not Forward / Encrypt-Only** | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | AIP P1 standalone dejó de venderse a nuevos clientes en enero de 2024; AIP P2 requiere licencia base compatible (ej. P1/E3) `[Verificado MS Learn]`. |
| **Information Protection Scanner** (SMB, NFS Preview y SharePoint Server on-premises) | Sí (vía EMS E3 / AIP P1) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí (M365 E5 / Purview Suite) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | En descubrimiento por SITs o aplicación automática por contenido requiere nivel P2 / E5 `[Verificado MS Learn]`. |
| **Auto-labeling en cliente** (Microsoft 365 Apps: recomendación o aplicación automática) | No `[Verificado MS Learn]` | Sí (solo cliente) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Configurado dentro de la propia etiqueta (`Auto-labeling for files and emails`) `[Verificado MS Learn]`. |
| **Auto-labeling en servicio** (SharePoint y OneDrive en reposo; Exchange en tránsito) | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí (Info Prot & Gov; no en AIP P2 puro) `[Verificado MS Learn]` | No etiqueta buzones de Exchange en reposo; techo de hasta 500.000 archivos/día en SPO/OD `[Verificado MS Learn]`. |
| **Clasificadores avanzados: Trainable Classifiers, Exact Data Match (EDM hasta 100M filas), Named Entities** | Parcial (SITs estándar/custom básicos) `[Verificado MS Learn]` | Limitado a cliente `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | EDM soporta hasta 100 millones de filas con refresco diario `[Verificado MS Learn]`. |
| **Etiqueta predeterminada en biblioteca de SharePoint y Dynamic Watermarking** | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Dynamic Watermarking exige etiqueta con cifrado y recomienda `Allow offline access = Never` `[Verificado MS Learn]`. |
| **Etiquetado de reuniones Teams / controles avanzados de reunión** | No `[Verificado MS Learn]` | No `[Verificado MS Learn]` | Sí (opciones avanzadas como marcas de agua en video/E2EE requieren Teams Premium) `[Verificado MS Learn]` | Sí (con Teams Premium donde aplique) `[Verificado MS Learn]` | Protege convocatorias, chat de reunión y opciones de sala de espera/presentadores `[Verificado MS Learn]`. |
| **Double Key Encryption (DKE) y Customer Key** | No `[Verificado MS Learn]` | Sí (DKE vía AIP P2) `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Sí `[Verificado MS Learn]` | Reservado al ~5% de activos ultraconfidenciales con mandato regulatorio estricto `[Verificado MS Learn]`. |
| **Etiquetado en Purview Data Map (SQL, Azure Storage, AWS S3) y clasificación PAYG** | No incluido per-user `[Verificado MS Learn]` | No incluido per-user `[Verificado MS Learn]` | Requiere suscripción Azure Pay-As-You-Go (PAYG) `[Verificado MS Learn]` | Requiere suscripción Azure PAYG `[Verificado MS Learn]` | Aplica etiquetas como metadatos en el Data Map sobre activos no-M365 `[Verificado MS Learn]`. |

### 2.3 Principios Rectores y Alineación Zero Trust (Pilar Data)

1. **Verificar explícitamente mediante clasificación y derechos de uso (`Verify Explicitly`):** Toda decisión de acceso, compartición externa, descarga o procesamiento por IA (Copilot y agentes) evalúa la identidad en Microsoft Entra ID junto con la etiqueta de sensibilidad del activo y los derechos RMS (`VIEW`, `EXTRACT`, `EDIT`, `EXPORT`) `[Verificado MS Learn]`.
2. **Aplicar mínimo privilegio y modelo Secure by Default (`Use Least Privilege`):** Iniciar el programa con una etiqueta predeterminada corporativa (por ejemplo, *Confidencial \ Todos los empleados*), derivar etiquetas desde bibliotecas de sitios críticos y entrenar a los usuarios para gestionar excepciones justificadas en vez de decidir desde cero cuándo proteger `[Verificado MS Learn]`.
3. **Asumir brecha con cifrado persistente e identidad adjunta al dato (`Assume Breach`):** Garantizar que los activos confidenciales conserven cifrado Azure RMS, marcas de agua dinámicas y capacidad de revocación aun si abandonan SharePoint, OneDrive o Exchange hacia almacenamiento externo no gestionado `[Verificado MS Learn]`.
4. **Equilibrar seguridad y razonamiento autorizado sobre los datos (`Reasoning Over Data`):** Preferir cifrado gestionado por Azure RMS o Customer Key sobre DKE para el 95% del patrimonio sensible, permitiendo que indexación, eDiscovery, DLP, antimalware y Microsoft 365 Copilot operen respetando permisos, y confinando DKE exclusivamente al ~5% de "joyas de la corona" reguladas `[Verificado MS Learn]`.
5. **Simular antes de aplicar a escala (`Simulation-First Governance`):** Ninguna política de auto-etiquetado en servicio ni clasificador EDM/entrenable pasa a modo `Turn policy on` sin revisión formal de muestras en modo simulación junto a los dueños de datos `[Verificado MS Learn]`.
6. **Convertir telemetría de datos en operación SOC auditable (`Telemetry-Driven SecOps`):** La telemetría de etiquetado no es un subproducto pasivo; eventos como bajas de nivel, remoción de cifrado y desajustes documento-contenedor deben correlacionarse continuamente con señales de identidad y endpoint generando evidencia repetible `[Decisión / Propuesta Editorial]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Flujo Arquitectónico de Tres Capas

Operativamente, Microsoft Purview Information Protection articula tres planos interdependientes `[Decisión / Propuesta Editorial]`:

- **Capa 1 — Clasificación e Inteligencia del Contenido:** Motor profundo de inspección compuesto por más de 300 **Sensitive Information Types (SITs)** integrados, SITs personalizados (regex, palabras clave, diccionarios, funciones checksum y proximidad), **Named Entities** (nombres de personas, direcciones físicas, condiciones médicas), **Document Fingerprinting** (formularios estandarizados), **Exact Data Match (EDM)** (tablas sensibles hasheadas de hasta 100 millones de filas actualizables a diario) y **Trainable Classifiers** basados en aprendizaje automático `[Verificado MS Learn]`.
- **Capa 2 — Orquestación de Etiquetas y Criptografía Persistente:** Taxonomía en `purview.microsoft.com > Solutions > Information Protection` estructurada en **Label groups** y etiquetas con ámbitos independientes (*Files & other data assets*, *Emails*, *Meetings*, *Groups & sites*), respaldada por **Azure Rights Management (Azure RMS)** para emisión de licencias de publicación y uso (`Use Licenses`), **Dynamic Watermarking**, **User-Defined Permissions (UDP)** y el servicio **Double Key Encryption (DKE)** `[Verificado MS Learn]`.
- **Capa 3 — Superficies de Aplicación, Telemetría y Respuesta SOC:** Etiquetado built-in en Microsoft 365 Apps (Windows, macOS, Web, iOS, Android), SharePoint/OneDrive (incluyendo coautoría cifrada, PDFs y etiquetas predeterminadas de biblioteca), Exchange Online (OME / Advanced Message Encryption y S/MIME), Microsoft Fabric / Power BI, Purview Data Map, **Information Protection Scanner** para repositorios locales y flujo continuo de eventos hacia Unified Audit Log, **Activity Explorer**, **Data Explorer / Content Explorer**, **Microsoft Defender XDR** y **Microsoft Sentinel** `[Verificado MS Learn]`.

### 3.2 Tabla de Componentes Operativos y Rutas Vigentes

| Componente / Motor | Función Operativa Principal | Consola y Ruta Oficial (Nov 2026) | Integraciones Clave | Estado |
|---|---|---|---|---|
| **Sensitivity Labels & Modern Label Groups** | Define la taxonomía corporativa en esquema moderno (grupos sin acciones técnicas + etiquetas con cifrado, marcas visuales, auto-etiquetado en cliente y controles de contenedor). | `purview.microsoft.com > Solutions > Information Protection > Sensitivity labels` | M365 Apps, SharePoint, Teams, Exchange, Fabric/Power BI, Copilot | `[Verificado MS Learn]` |
| **Label Publishing Policies** | Publica etiquetas a usuarios, grupos o Administrative Units con etiqueta predeterminada, etiquetado obligatorio (*mandatory labeling*) y justificación en bajadas (*downgrade*). | `purview.microsoft.com > Solutions > Information Protection > Publishing policies` | Microsoft Entra ID (Groups & Administrative Units) | `[Verificado MS Learn]` |
| **Service-Side Auto-Labeling Engine** | Evalúa y etiqueta archivos en reposo en SharePoint/OneDrive (hasta 500.000 archivos/día agregados; simulación hasta 20M) y correos en tránsito en Exchange, más pestaña *Insights*. | `purview.microsoft.com > Solutions > Information Protection > Auto-labeling` | SharePoint Online, OneDrive, Exchange Online, Purview Data Map | `[Verificado MS Learn]` |
| **Classifiers Suite (SITs, Named Entities, EDM, Trainable)** | Descubre patrones regulatorios, entidades nombradas, coincidencias exactas en bases de hasta 100M de filas (EDM) y categorías documentales por ML. | `purview.microsoft.com > Solutions > Information Protection > Classifiers` | Auto-labeling, Purview DLP, Insider Risk Management, DSPM | `[Verificado MS Learn]` |
| **Azure Rights Management (Azure RMS) & Super User** | Servicio criptográfico cloud que emite licencias de uso, evalúa derechos (`VIEW`, `EXTRACT`, `EXPORT`, `OWNER`), aplica marcas de agua dinámicas y soporta recuperación administrativa. | `purview.microsoft.com > Settings > Information Protection` + Módulo PowerShell `AIPService` | Microsoft Entra ID, eDiscovery, Exchange Online, M365 Copilot | `[Verificado MS Learn]` |
| **Double Key Encryption (DKE) Service** | Arquitectura de doble clave (Azure + servicio DKE bajo custodia exclusiva del cliente on-premises o en nube) para datos sometidos a soberanía criptográfica estricta. | Repositorio oficial DKE Service + `Sensitivity labels > Encryption > Use Double Key Encryption` | Microsoft 365 Apps (Windows), MPIP Client / Scanner / Viewer, MIP SDK 1.7+ | `[Verificado MS Learn]` |
| **Container Labels & Default Library Labels** | Gobierna privacidad, invitados, compartición externa y acceso desde dispositivos no gestionados en Teams/Groups/Sites, y etiqueta por ubicación en bibliotecas SharePoint. | `admin.microsoft.com` / `admin.teams.microsoft.com` / SharePoint Library Settings | Microsoft Entra Conditional Access (Authentication Context), SharePoint, Loop, Viva Engage | `[Verificado MS Learn]` |
| **Information Protection Scanner & MPIP Client** | Servicio Windows Server (cliente MPIP 3.2.x) que inspecciona, clasifica y protege archivos en recursos UNC SMB, NFS (Preview) y SharePoint Server local. | `purview.microsoft.com > Settings > Information Protection > Information protection scanner` | Windows Server, SQL Server, Active Directory / Entra ID | `[Verificado MS Learn]` |
| **Explorers, Posture Reports & Unified SecOps** | Visibilidad de postura (ventana móvil 30 días en preview), Activity Explorer, Content/Data Explorer y correlación de eventos `MicrosoftPurviewInformationProtection` / `CloudAppEvents`. | `purview.microsoft.com > Solutions > Information Protection > Reports / Explorers` y `security.microsoft.com` | Purview Audit, Microsoft Defender XDR, Microsoft Sentinel, Security Copilot | `[Verificado MS Learn]` |

### 3.3 Integraciones Estratégicas y Transiciones 2026–2027

- **Microsoft 365 Copilot, Copilot Chat y Agentes (Agent 365):** Copilot nunca eleva permisos de acceso; adicionalmente verifica derechos de uso sobre elementos cifrados. Si la etiqueta concede `VIEW` pero omite `Copy and extract content (EXTRACT)` (como ocurre en el rol predefinido *Viewer* o *Reviewer* sin extracción), Copilot y los agentes no devuelven ni resumen el contenido a ese usuario (salvo al *Rights Management issuer/owner*, quien conserva siempre todos los derechos) `[Verificado MS Learn]`. Cuando Copilot genera un documento nuevo en Word/Excel/PowerPoint a partir de un archivo etiquetado, hereda automáticamente la etiqueta de mayor prioridad; además, el ajuste avanzado por PowerShell `Set-Label -AdvancedSettings @{BlockContentAnalysisServices="True"}` excluye el archivo del análisis de experiencias conectadas y Copilot `[Verificado MS Learn]`.
- **Retiro de File Policies en Microsoft Defender for Cloud Apps (`2027-01-06`):** Las políticas de archivos de Defender for Cloud Apps que aplicaban etiquetas de sensibilidad en SharePoint, OneDrive o nubes de terceros se retiran definitivamente el **6 de enero de 2027**; las cargas de SharePoint y OneDrive deben migrarse a políticas nativas de *Auto-labeling* o *Purview DLP* mediante el asistente *DLP to Purview migration* `[Verificado MS Learn]`.
- **Microsoft Purview Data Loss Prevention (Módulo 15) e Insider Risk Management (Módulo 17):** Las etiquetas de sensibilidad actúan como condición primaria en reglas DLP (incluyendo Endpoint DLP y la ubicación *Microsoft 365 Copilot and Copilot Chat*) y como indicador de criticidad en perfiles de riesgo de Insider Risk Management (bajadas masivas de nivel o eliminación de etiquetas antes de un cese laboral) `[Verificado MS Learn]`.
- **Microsoft Sentinel y Defender XDR (Módulos 03 y 08):** Los eventos de etiquetado fluyen al Unified Audit Log (`OfficeActivity` / `CloudAppEvents`) y a la tabla `MicrosoftPurviewInformationProtection` en el portal unificado `security.microsoft.com` (recordando el retiro de Sentinel en Azure Portal el 31 de marzo de 2027) `[Verificado MS Learn]`.

### 3.4 Matriz Comparativa de Opciones Criptográficas y Alcance Funcional

| Modalidad Criptográfica en Purview IP | Custodia de Claves | Coautoría Office / Web y Búsqueda M365 | Soporte eDiscovery y Purview DLP | Interacción con Microsoft 365 Copilot | Caso de Uso Arquitectónico Recomendado |
|---|---|---|---|---|---|
| **Azure RMS con clave gestionada por Microsoft (MMK)** | Microsoft (raíz en Azure) `[Verificado MS Learn]` | Completa (con coautoría habilitada) `[Verificado MS Learn]` | Completo (*Reasoning over data*) `[Verificado MS Learn]` | Soportado si el usuario posee `VIEW` + `EXTRACT` `[Verificado MS Learn]` | Estándar recomendado para el ~80-90% de información confidencial corporativa `[Decisión / Propuesta Editorial]`. |
| **Azure RMS Bring Your Own Key (BYOK)** | Cliente genera en HSM y transfiere a Azure Key Vault `[Verificado MS Learn]` | Completa `[Verificado MS Learn]` | Completo `[Verificado MS Learn]` | Soportado con `VIEW` + `EXTRACT` `[Verificado MS Learn]` | Organizaciones que exigen control de ciclo de vida y revocación de la clave raíz del tenant `[Verificado MS Learn]`. |
| **Microsoft Purview Customer Key (DEP)** | Dos claves en Azure Key Vault / Managed HSM del cliente + *Availability key* `[Verificado MS Learn]` | Completa (cifrado de servicio en reposo) `[Verificado MS Learn]` | Completo `[Verificado MS Learn]` | Soportado `[Verificado MS Learn]` | Cumplimiento regulatorio para cifrado raíz en reposo de buzones Exchange y sitios SharePoint/OneDrive `[Verificado MS Learn]`. |
| **User-Defined Permissions (UDP) / Do Not Forward** | Azure RMS (permisos asignados al aplicar) `[Verificado MS Learn]` | Limitada (UDP en Word/Excel/PPT no soporta etiqueta predeterminada estándar de biblioteca) `[Verificado MS Learn]` | Soportado para servicios autorizados `[Verificado MS Learn]` | Evaluado por derechos efectivos del lector `[Verificado MS Learn]` | Compartición ad-hoc con destinatarios específicos externos o comunicaciones reservadas `[Verificado MS Learn]`. |
| **Double Key Encryption (DKE)** | Clave 1 en Azure + Clave 2 en servicio DKE exclusivo del cliente `[Verificado MS Learn]` | **No soportada** (desactiva coautoría, AutoSave y Office Web) `[Verificado MS Learn]` | **No soportado** en reposo en SPO/OD `[Verificado MS Learn]` | **Bloqueado** en reposo y en uso en versiones actuales de Office `[Verificado MS Learn]` | Exclusivamente para el ~5% de secretos críticos con exigencia legal estricta de soberanía de claves `[Verificado MS Learn]`. |

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Microsoft recomienda eliminar asignaciones permanentes de *Global Administrator* y operar mediante grupos de roles específicos en `purview.microsoft.com > Settings > Roles and scopes > Role groups`, soportando delimitación por **Administrative Units** de Microsoft Entra ID y activación Just-in-Time con **Microsoft Entra Privileged Identity Management (PIM) for Groups** `[Verificado MS Learn]`.

| Rol / Role Group Oficial | Plano RBAC | Permisos Clave | Estrategia PIM / JIT Recomendada | Responsabilidad Operativa y Segregación de Funciones | Estado |
|---|---|---|---|---|---|
| **Information Protection Admin** | Purview Portal / Entra ID | Crea, edita y publica Sensitivity Labels, políticas de publicación, políticas de auto-etiquetado, SITs personalizados, EDM y nodos del Scanner. | **Eligible (JIT máx. 4 h)** con MFA phishing-resistant (FIDO2/WHfB), justificación y ticket de cambio aprobado `[Decisión / Propuesta Editorial]`. | Ingeniería de taxonomía, políticas de cifrado y despliegues por oleadas; no debe aprobar sus propios cambios en producción `[Verificado MS Learn]`. |
| **Information Protection Analyst** | Purview Portal | Gestiona alertas relacionadas con protección de información, visualiza reportes y revisa simulaciones sin modificar configuraciones globales de tenant. | **Eligible (JIT 8 h por turno SOC)** con MFA resistente a phishing `[Decisión / Propuesta Editorial]`. | Triaje operativo SOC L1/L2, validación de simulaciones de auto-labeling y análisis de tendencias `[Verificado MS Learn]`. |
| **Information Protection Investigator** | Purview Portal | Investiga actividades y elementos etiquetados/clasificados para responder a incidentes de exposición de datos. | **Eligible (JIT máx. 4 h)** vinculado a número de incidente activo `[Decisión / Propuesta Editorial]`. | Investigación profunda L2/L3 sobre incidentes de degradación de etiquetas o exfiltración `[Verificado MS Learn]`. |
| **Information Protection Reader** | Purview Portal | Acceso de solo lectura a etiquetas, políticas de publicación, políticas de auto-etiquetado e informes de postura. | Asignación activa acotada (o Eligible 8 h) para GRC, Auditoría Interna y Arquitectura `[Decisión / Propuesta Editorial]`. | Verificación independiente de cumplimiento y auditoría sin riesgo de alteración de controles `[Verificado MS Learn]`. |
| **Data Classification Content Viewer** | Purview Portal (Rol sensible) | Permite abrir y leer el contenido real de archivos/correos coincidentes dentro de *Content Explorer / Data Explorer*. | **Eligible estricto (JIT máx. 2 h)** con aprobación dual (Custodio de Privacidad / Legal + SOC Lead) `[Decisión / Propuesta Editorial]`. | Segregado obligatoriamente de los administradores rutinarios para evitar acceso indebido a información confidencial de negocio o PII `[Verificado MS Learn]`. |
| **Data Classification List Viewer** | Purview Portal | Permite listar las ubicaciones, nombres de archivos y conteos en *Content Explorer / Data Explorer* sin abrir el contenido del archivo. | **Eligible (JIT 8 h)** para analistas de postura y dueños de remediación de oversharing `[Decisión / Propuesta Editorial]`. | Habilita inventario y remediación de exposiciones respetando el principio de privacidad por diseño `[Verificado MS Learn]`. |
| **Azure RMS Super User (Grupo dedicado)** | Servicio Azure RMS (`AIPService`) | Concede derecho `OWNER` (control total y descifrado) sobre todo el contenido protegido por Azure RMS del tenant (no aplica a DKE sin acceso a la clave DKE). | **Deshabilitado por defecto** (`Disable-AipServiceSuperUserFeature`); activar solo en emergencia o mediante cuentas de servicio dedicadas a eDiscovery/Scanner auditadas `[Verificado MS Learn]`. | Recuperación ante contingencias legales/criptográficas; toda operación se audita con `Get-AipServiceAdminLog` `[Verificado MS Learn]`. |
| **SharePoint / Teams Administrator** | Microsoft 365 / Entra ID | Habilita integración MIP en SharePoint (`EnableAIPIntegration`), soporte PDF, etiquetas de contenedor en sitios/equipos y contextos de acceso condicional. | **Eligible (JIT máx. 4 h)** coordinado con el equipo de Information Protection `[Decisión / Propuesta Editorial]`. | Gobierno de contenedores colaborativos, bibliotecas críticas y prevención de oversharing previo a Copilot `[Verificado MS Learn]`. |

---

## 5. Cadencia Operativa Diaria

> **Nota Editorial:** La cadencia diaria de 8 actividades (`D-01` a `D-08`) está diseñada como un circuito secuencial donde primero se valida la salud de la telemetría y la integridad administrativa antes de ejecutar triaje y caza proactiva `[Decisión / Propuesta Editorial]`.

### D-01: Verificación de salud de ingesta y telemetría de Information Protection
- **Objetivo:** Confirmar que los eventos del Unified Audit Log, Activity Explorer y las tablas de `security.microsoft.com` (`CloudAppEvents` / `OfficeActivity` / `MicrosoftPurviewInformationProtection`) fluyen sin caída silenciosa antes de iniciar el triaje diario `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Data connectors` y `https://purview.microsoft.com > Solutions > Information Protection > Explorers > Activity explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar en `security.microsoft.com` el estado `Connected` de los conectores de Microsoft 365 y Microsoft Defender XDR `[Verificado MS Learn]`.
  2. Ejecutar consulta rápida de volumen de eventos de etiquetado de las últimas 24 horas y compararla contra el promedio móvil de los últimos 7 días hábiles `[Decisión / Propuesta Editorial]`.
  3. Confirmar en `Activity explorer` que existen registros recientes de `Label applied` / `File read` con latencia normal.
  4. Si se detecta caída superior al 20% en día hábil sin ventana de mantenimiento, abrir ticket prioritario de infraestructura de monitoreo antes de dar por válido cualquier indicador en cero `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro diario del check de ingesta y captura/exportación de volumen de eventos 24h vs. línea base de 7 días (NIST CSF 2.0: `DE.CM-06`) `[Decisión / Propuesta Editorial]`.

### D-02: Auditoría de cambios administrativos del día anterior sobre etiquetas y políticas
- **Objetivo:** Detectar cualquier creación, modificación, despublicación o eliminación no autorizada de etiquetas de sensibilidad, políticas de publicación o políticas de auto-etiquetado `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Audit > Search` (o `Advanced Hunting` en `security.microsoft.com`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / GRC Analyst.
- **Procedimiento Paso a Paso:**
  1. Consultar en Purview Audit las operaciones administrativas de las últimas 24 horas: `New-Label`, `Set-Label`, `Remove-Label`, `New-LabelPolicy`, `Set-LabelPolicy`, `Remove-LabelPolicy`, `New-AutoSensitivityLabelPolicy`, `Set-AutoSensitivityLabelPolicy` `[Verificado MS Learn]`.
  2. Cotejar cada evento detectado contra el registro formal de gestión de cambios (ITSM) y validar la sesión PIM del administrador ejecutor `[Decisión / Propuesta Editorial]`.
  3. Verificar especialmente que ninguna etiqueta con cifrado haya sido eliminada ni que `BlockContentAnalysisServices` o derechos `EXTRACT` hayan sido alterados sin aprobación `[Verificado MS Learn]`.
  4. Ante cualquier cambio huérfano sin ticket aprobado, escalar inmediatamente al playbook `AH-04` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Exportación CSV diaria de operaciones administrativas conciliada 1:1 con folios ITSM (NIST CSF 2.0: `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

### D-03: Triaje de alertas e incidentes relacionados con clasificación y datos sensibles
- **Objetivo:** Clasificar y atender dentro de SLA todas las alertas generadas por políticas de Purview y detecciones correlacionadas en la cola unificada de incidentes `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Investigation & response > Incidents & alerts > Incidents` y `https://purview.microsoft.com > Solutions > Information Protection` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Information Protection Analyst.
- **Procedimiento Paso a Paso:**
  1. Filtrar la cola unificada de incidentes en `security.microsoft.com` por fuentes de Purview / reglas de detección personalizadas sobre degradación de etiquetas `[Verificado MS Learn]`.
  2. Ordenar por severidad (`Critical`, `High`, `Medium`, `Low`) e inspeccionar usuario, activo afectado, etiqueta involucrada y contexto de sesión Entra ID.
  3. Clasificar cada alerta como Verdadero Positivo (VP — escalar a `AH-01`/`AH-02`), Falso Positivo (FP — registrar motivo exacto para tuning semanal `S-01`) o Actividad Benigna Autorizada (BP) `[Decisión / Propuesta Editorial]`.
  4. Documentar timestamps de reconocimiento para cálculo de MTTA `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Bitácora de triaje en cola de incidentes con clasificación VP/FP/BP, analista asignado y marca temporal (NIST CSF 2.0: `DE.AE-02`, MITRE: `Collection / T1005`) `[Decisión / Propuesta Editorial]`.

### D-04: Caza diaria de bajadas de nivel (downgrades) y remoción de etiquetas o cifrado
- **Objetivo:** Identificar usuarios o procesos que reducen la clasificación (`Label changed` hacia menor prioridad) o eliminan etiquetas/protección (`Label removed` / remoción de cifrado RMS), incluso cuando suministran justificación textual `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Explorers > Activity explorer` y `https://security.microsoft.com > Hunting > Advanced hunting` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Information Protection Analyst.
- **Procedimiento Paso a Paso:**
  1. Filtrar `Activity explorer` (últimas 24 horas) por actividades `Label removed` y `Label changed` (sentido downgrade) sobre etiquetas *Highly Confidential* y *Confidential* `[Verificado MS Learn]`.
  2. Revisar el texto de justificación capturado por la política de etiquetas; detectar justificaciones vacías, genéricas ("test", "asdf") o picos de volumen (>5 bajadas por un mismo usuario en 24 h) `[Decisión / Propuesta Editorial]`.
  3. Cruzar usuarios con picos de bajada contra su nivel de riesgo en Insider Risk Management y eventos posteriores de compartición externa o subida web `[Verificado MS Learn]`.
  4. Escalar casos sospechosos a investigación formal (`AH-01`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario de eventos de downgrade/remoción sobre etiquetas críticas y validación de justificaciones (NIST CSF 2.0: `DE.CM-01`, MITRE: `Defense Evasion / T1562`) `[Decisión / Propuesta Editorial]`.

### D-05: Monitoreo y notificación de eventos de oversharing contenedor-documento
- **Objetivo:** Detectar documentos con etiqueta de sensibilidad superior a la etiqueta del sitio de SharePoint o equipo de Teams donde fueron alojados (`FileSensitivityLabelMismatch`) para frenar exposición interna o ante Microsoft 365 Copilot `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Audit > Search` (`FileSensitivityLabelMismatch`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L1 / Collaboration Security Analyst.
- **Procedimiento Paso a Paso:**
  1. Consultar eventos `FileSensitivityLabelMismatch` generados en las últimas 24 horas en SharePoint Online y Microsoft Teams `[Verificado MS Learn]`.
  2. Identificar para cada evento la brecha de sensibilidad (por ejemplo, archivo *Altamente Confidencial* cargado en sitio *Público* o con invitados externos habilitados).
  3. Verificar si el propietario del sitio atendió la notificación automática por correo electrónico o si el archivo permanece expuesto `[Verificado MS Learn]`.
  4. En brechas críticas con acceso de invitados (`Guest`), exigir traslado inmediato del archivo, ajuste de permisos o elevación de la etiqueta del contenedor (`AH-03`) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Registro de eventos `FileSensitivityLabelMismatch` detectados y estado de remediación con dueños de sitios (NIST CSF 2.0: `DE.CM-01`, MITRE: `Exfiltration / T1567`) `[Decisión / Propuesta Editorial]`.

### D-06: Vigilancia de salud operativa de Azure RMS, DKE y accesos denegados a archivos cifrados
- **Objetivo:** Asegurar la disponibilidad continua del plano criptográfico (Azure RMS y endpoints DKE) y detectar patrones anómalos de denegación de acceso a documentos protegidos `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://admin.microsoft.com > Health > Service health`, monitoreo HTTPS del servicio DKE y `Unified Audit Log` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar ausencia de avisos de degradación en Microsoft 365 Service Health para Purview Information Protection / Azure Rights Management y comprobar disponibilidad TLS/latencia del servicio DKE (si está desplegado) `[Verificado MS Learn]`.
  2. Consultar intentos repetidos de acceso denegado a archivos protegidos con RMS agrupados por usuario, IP y documento `[Decisión / Propuesta Editorial]`.
  3. Distinguir errores de permisos legítimos (colaboración B2B mal configurada en Entra Cross-Tenant Access) frente a intentos de lectura no autorizada post-exfiltración o post-revocación `[Verificado MS Learn]`.
  4. Correlacionar usuarios con >5 denegaciones sobre archivos *Highly Confidential* con señales de inicio de sesión riesgoso en Entra ID `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Check diario de salud criptográfica RMS/DKE y resumen de anomalías de acceso denegado investigadas (NIST CSF 2.0: `PR.DS-01`, MITRE: `Collection / T1213`) `[Decisión / Propuesta Editorial]`.

### D-07: Supervisión de interacciones de Microsoft 365 Copilot y agentes con contenido etiquetado
- **Objetivo:** Monitorear el consumo de activos *Confidential* / *Highly Confidential* en prompts y respuestas de Microsoft 365 Copilot, Copilot Chat y agentes, validando herencia de etiquetas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Explorers > Activity explorer` (`Copilot interaction`) y `Solutions > DSPM for AI` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / AI Data Security Analyst.
- **Procedimiento Paso a Paso:**
  1. Filtrar `Activity explorer` por la actividad `Copilot interaction` cruzada con etiquetas de alta sensibilidad en las últimas 24 horas `[Verificado MS Learn]`.
  2. Identificar volúmenes atípicos de extracción/resumen por un mismo usuario o agente sobre bibliotecas financieras, legales o de M&A `[Decisión / Propuesta Editorial]`.
  3. Confirmar que ningún activo marcado con `BlockContentAnalysisServices` o cifrado sin derecho `EXTRACT` aparezca retornado indebidamente `[Verificado MS Learn]`.
  4. Documentar hallazgos de sobreexposición en sitios consumidos por Copilot para alimentar la remediación semanal de contenedores `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte diario de interacciones de IA sobre datos sensibles etiquetados (NIST CSF 2.0: `DE.CM-09`, MITRE: `Collection / T1005`) `[Decisión / Propuesta Editorial]`.

### D-08: Control de SLAs de incidentes de datos abiertos y actualización del tablero diario
- **Objetivo:** Evitar el vencimiento de SLAs en incidentes de exposición de datos activos y cerrar el ciclo de 24 horas con estado RAG consolidado `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents & alerts > Incidents` y Workbook operativo en Microsoft Sentinel `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Shift Lead.
- **Procedimiento Paso a Paso:**
  1. Revisar todos los incidentes abiertos asociados a Information Protection verificando tiempo restante frente al SLA objetivo (ej. Críticos: MTTA <1 h, MTTC <4 h; Altos: MTTA <4 h, MTTC <8 h) `[Decisión / Propuesta Editorial]`.
  2. Escalar de inmediato al SOC Manager y Data Security Lead cualquier expediente con menos del 20% de ventana SLA disponible `[Decisión / Propuesta Editorial]`.
  3. Actualizar el resumen diario RAG (conectores, cambios admin sin ticket, alertas pendientes, bajadas críticas, oversharing y salud RMS) para entrega de turno `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Snapshot diario del tablero operativo RAG y acta de entrega de turno SOC (NIST CSF 2.0: `RS.MA-01`) `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Afinamiento (tuning) de SITs personalizados, EDM y clasificadores entrenables
- **Objetivo:** Reducir falsos positivos y mejorar la precisión de clasificación analizando los descartes documentados durante la operación diaria (`D-03`) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Classifiers` `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin / SOC L3.
- **Procedimiento Paso a Paso:**
  1. Consolidar el registro semanal de falsos positivos por SIT, entidad nombrada, esquema EDM o clasificador entrenable `[Decisión / Propuesta Editorial]`.
  2. Ajustar niveles de confianza (*High/Medium/Low*), proximidad de caracteres, evidencia corroborativa, operadores lógicos `AND` o listas de exclusión en SITs personalizados clonados `[Verificado MS Learn]`.
  3. Verificar que los trabajos programados de refresco y hash de tablas **Exact Data Match (EDM)** se hayan ejecutado sin errores durante la semana `[Verificado MS Learn]`.
  4. Validar los cambios con conjuntos de prueba antes de actualizar políticas en producción `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de cambios de clasificadores y comparativa de precisión pre/post ajuste (NIST CSF 2.0: `ID.IM-03`) `[Decisión / Propuesta Editorial]`.

### S-02: Evaluación de políticas de auto-etiquetado en simulación y pestaña Insights
- **Objetivo:** Auditar la exactitud de políticas en modo simulación antes de activarlas y corregir causas de fallo en políticas activas de auto-etiquetado en servicio `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Auto-labeling` (pestañas *Simulation* e *Insights*) `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin + Data Owners.
- **Procedimiento Paso a Paso:**
  1. Para políticas en `Run policy in simulation mode`, revisar muestras de archivos coincidentes (*Matched items*) junto al dueño de los datos hasta validar una precisión superior al 95% antes de pasar a `Turn policy on` `[Decisión / Propuesta Editorial]`.
  2. Abrir la pestaña **Insights** de cada política activa y registrar la relación de archivos etiquetados vs. fallidos y las tres causas principales de error `[Verificado MS Learn]`.
  3. Verificar que el volumen diario combinado se mantenga holgado respecto al techo técnico de **500.000 archivos/día** en SharePoint y OneDrive `[Verificado MS Learn]`.
  4. Confirmar que el soporte de etiquetado PDF permanezca activo para evitar omisión de archivos `.pdf` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta de validación de muestras firmada por Data Owner y captura semanal de la pestaña *Insights* (NIST CSF 2.0: `PR.DS-01`) `[Decisión / Propuesta Editorial]`.

### S-03: Revisión de tendencias de clasificación, adopción y justificaciones de downgrade
- **Objetivo:** Detectar desvíos de adopción por departamento y patrones recurrentes de bajada de etiqueta que indiquen fricción excesiva o intento de evasión `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Reports` y PowerShell (`Export-ActivityExplorerData`) `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Analyst.
- **Procedimiento Paso a Paso:**
  1. Ejecutar exportación incremental semanal con `Export-ActivityExplorerData` para preservar series históricas más allá de la ventana móvil de 30 días del portal `[Verificado MS Learn]`.
  2. Analizar proporción de etiquetado automático, predeterminado y manual por carga de trabajo (Office, Outlook, SharePoint, OneDrive, Fabric/Power BI).
  3. Agrupar las 10 justificaciones más repetidas en eventos de bajada de etiqueta y proponer ajustes de políticas o micro-capacitación focalizada `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Dataset semanal exportado a repositorio histórico/Power BI e informe de tendencias de clasificación (NIST CSF 2.0: `ID.RA-01`) `[Decisión / Propuesta Editorial]`.

### S-04: Auditoría de sitios SharePoint y equipos Teams sin etiqueta de contenedor o desalineados
- **Objetivo:** Cerrar brechas de gobernanza colaborativa identificando sitios/equipos creados sin etiqueta de contenedor o con desalineación frente a su etiqueta predeterminada de biblioteca (Paso 4 del modelo *Secure by Default*) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://admin.microsoft.com`, SharePoint Admin Center y Microsoft Graph PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** SharePoint / Teams Admin + Information Protection Admin.
- **Procedimiento Paso a Paso:**
  1. Consultar mediante Microsoft Graph / SharePoint PowerShell el inventario de sitios de SharePoint, Microsoft 365 Groups y Teams cuyo atributo `sensitivityLabel` esté vacío `[Verificado MS Learn]`.
  2. Detectar sitios etiquetados como *Confidential / Highly Confidential* que carezcan de etiqueta predeterminada en sus bibliotecas documentales principales o que permitan compartición externa incongruente `[Verificado MS Learn]`.
  3. Notificar a propietarios o aplicar etiquetado administrativo de contenedor según política de gobierno `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Listado semanal de contenedores sin etiqueta y porcentaje de remediación ejecutado (NIST CSF 2.0: `PR.AA-05`) `[Decisión / Propuesta Editorial]`.

### S-05: Supervisión de ciclos y resultados del Information Protection Scanner on-premises
- **Objetivo:** Garantizar que los servidores del **Information Protection Scanner** completen sus ciclos de descubrimiento y protección sobre recursos SMB, NFS (Preview) y SharePoint Server sin nodos detenidos ni errores de credenciales `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Information Protection > Information protection scanner` (Nodes, Content scan jobs) `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin / Hybrid Infrastructure Engineer.
- **Procedimiento Paso a Paso:**
  1. Verificar que todos los nodos del clúster del escáner reporten estado saludable, versión vigente del cliente MPIP (rama 3.2.x) y conectividad con SQL Server y Entra ID `[Verificado MS Learn]`.
  2. Revisar reportes locales (`%localappdata%\Microsoft\MSIP\Scanner\Reports`) y eventos en `Activity explorer` para contabilizar archivos descubiertos, etiquetados, omitidos o bloqueados `[Verificado MS Learn]`.
  3. Incorporar cualquier nuevo file share corporativo detectado por infraestructura en los *Content scan jobs* en modo descubrimiento antes de activar aplicación automática `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reporte de ejecución semanal de *Content scan jobs* y registro de archivos on-premises protegidos (NIST CSF 2.0: `ID.AM-02`) `[Decisión / Propuesta Editorial]`.

### S-06: Auditoría del rol Super User de Azure RMS y accesos a Content/Data Explorer
- **Objetivo:** Controlar estrictamente el uso de capacidades de alto privilegio que permiten inspeccionar o descifrar datos sensibles del tenant `[Verificado MS Learn]`.
- **Consola y Ruta:** PowerShell (`AIPService` / Purview Audit) y `https://entra.microsoft.com > Identity governance > Privileged Identity Management` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / GRC Lead.
- **Procedimiento Paso a Paso:**
  1. Comprobar mediante `Get-AipServiceSuperUserFeature` que la función Super User permanezca `Disabled` salvo ventanas autorizadas o cuentas de servicio estrictamente documentadas `[Verificado MS Learn]`.
  2. Auditar con `Get-AipServiceAdminLog` y Purview Audit toda activación PIM y uso de `Data Classification Content Viewer` durante los últimos 7 días `[Verificado MS Learn]`.
  3. Confirmar que cada visualización de contenido sensible cuente con aprobación dual e identificador de caso válido `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Log semanal de auditoría de Super User y activaciones JIT de `Content Viewer` conciliado contra tickets (NIST CSF 2.0: `PR.AA-05`) `[Decisión / Propuesta Editorial]`.

### S-07: Ajuste de reglas analíticas de correlación en Defender XDR / Microsoft Sentinel
- **Objetivo:** Refinar las detecciones personalizadas que cruzan señales de etiquetas Purview con identidad (Entra ID) y dispositivo (Defender for Endpoint) `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Microsoft Sentinel > Configuration > Analytics` y `Hunting > Custom detection rules` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L3 / Detection Engineer.
- **Procedimiento Paso a Paso:**
  1. Evaluar la tasa de verdaderos positivos y tiempos de generación de las reglas que correlacionan remoción/bajada de etiquetas con inicios de sesión anómalos, dispositivos con riesgo o descargas masivas `[Decisión / Propuesta Editorial]`.
  2. Excluir cuentas de servicio legítimas verificadas (ej. cuenta del Information Protection Scanner) debidamente restringidas por IP/dispositivo `[Verificado MS Learn]`.
  3. Documentar cambios de versión KQL en repositorio de detección como código `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Historial de commits/versiones de reglas analíticas y métrica semanal de precisión de alertas (NIST CSF 2.0: `DE.AE-04`) `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Exportación histórica de postura, cobertura de etiquetado y control FinOps PAYG
- **Objetivo:** Preservar evidencia histórica mensual fuera de la ventana móvil de 30 días de los informes en vista previa y controlar el consumo Pay-As-You-Go en Data Map y clasificación bajo demanda `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Reports`, `Usage center` y `Export-ContentExplorerData` `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin + FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Exportar a PDF los **Posture reports** de Information Protection (distribución de etiquetas, adopción y cobertura de auto-labeling) y ejecutar `Export-ContentExplorerData` por carga de trabajo (Exchange, SharePoint, OneDrive, Teams) `[Verificado MS Learn]`.
  2. Si las etiquetas se extendieron a fuentes no-M365, capturar el informe de etiquetas en *Unified Catalog* (`Health Management > Reports`) `[Verificado MS Learn]`.
  3. Revisar en el **Usage center** de Purview y Azure Cost Management los medidores de facturación PAYG frente al presupuesto mensual asignado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Paquete mensual fechado (PDF + CSV de cobertura por carga de trabajo + conciliación PAYG) almacenado en repositorio inmutable de auditoría (NIST CSF 2.0: `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

### M-02: Pruebas integrales de efectividad de cifrado persistente, Dynamic Watermarking y Copilot
- **Objetivo:** Verificar empíricamente que el cifrado Azure RMS, las marcas de agua dinámicas y las restricciones `VIEW`/`EXTRACT` ante Microsoft 365 Copilot operen sin regresiones en todas las plataformas `[Verificado MS Learn]`.
- **Consola y Ruta:** Entorno de validación con cuentas de prueba licenciadas en Windows, macOS, Web, móvil y Microsoft 365 Copilot `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin / QA Security Engineer.
- **Procedimiento Paso a Paso:**
  1. Descargar fuera del tenant archivos de prueba con etiquetas cifrantes y validar bloqueo de apertura con identidad externa no autorizada `[Verificado MS Learn]`.
  2. Abrir documentos con **Dynamic Watermarking** verificando la inserción dinámica del UPN del lector y la imposibilidad de remoción manual sin derecho `EXPORT` / `OWNER` `[Verificado MS Learn]`.
  3. Ejecutar prompts de prueba en Microsoft 365 Copilot y Copilot Chat comprobando: (a) denegación de retorno en archivos cifrados sin derecho `EXTRACT`, (b) bloqueo en archivos con `BlockContentAnalysisServices="True"`, y (c) herencia automática de la etiqueta más restrictiva en archivos creados `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz mensual de pruebas sintéticas de cifrado, marcas dinámicas y enforcement Copilot con capturas fechadas (NIST CSF 2.0: `PR.DS-01`, `PR.DS-02`) `[Decisión / Propuesta Editorial]`.

### M-03: Revisión de higiene de clientes Office Built-in Labeling, MPIP Client y coautoría
- **Objetivo:** Asegurar que la flota de endpoints mantenga versiones soportadas de Microsoft 365 Apps y del cliente MPIP sin residuos del complemento retirado AIP add-in `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://intune.microsoft.com > Apps` y `https://purview.microsoft.com > Settings > Information Protection > Co-authoring for files with sensitivity labels` `[Verificado MS Learn]`.
- **Rol Responsable:** Endpoint Engineer (Intune) + Information Protection Admin.
- **Procedimiento Paso a Paso:**
  1. Auditar en Microsoft Intune que el 100% de equipos carezca del antiguo *Azure Information Protection Unified Labeling add-in* (retirado) y ejecute versiones de Microsoft 365 Apps compatibles con Dynamic Watermarks, DKE (si aplica) y controles de privacidad de contenido conectado `[Verificado MS Learn]`.
  2. Verificar versiones desplegadas del **Microsoft Purview Information Protection client** (3.2.x) en estaciones que usen el etiquetador de Windows Explorer y en servidores Scanner `[Verificado MS Learn]`.
  3. Confirmar el estado activo de coautoría para archivos cifrados y de integración en Microsoft Fabric / Power BI `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de cumplimiento de versiones de aplicaciones desde Intune (NIST CSF 2.0: `PR.PS-02`) `[Decisión / Propuesta Editorial]`.

### M-04: Progreso de migración desde File Policies de Defender for Cloud Apps (Hito 2027-01-06)
- **Objetivo:** Garantizar la migración completa y el decomiso ordenado de cualquier política de archivos heredada en Defender for Cloud Apps que aplique etiquetas de sensibilidad antes del retiro definitivo del **6 de enero de 2027** `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://security.microsoft.com > Cloud apps > Policies > Policy management > Information protection` y asistente *DLP to Purview migration* `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin + Cloud Security Engineer.
- **Procedimiento Paso a Paso:**
  1. Inventariar las File Policies remanentes en Defender for Cloud Apps clasificadas por la herramienta oficial como `Can migrate`, `Partial migration` o `Cannot migrate` `[Verificado MS Learn]`.
  2. Migrar las políticas de auto-etiquetado de SharePoint y OneDrive hacia políticas nativas de *Service-side auto-labeling* en Purview en modo simulación y validar equivalencia funcional `[Verificado MS Learn]`.
  3. Desactivar las File Policies heredadas una vez confirmada la cobertura en Purview para eliminar evaluaciones duplicadas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Tablero de avance de migración y acta de decomiso de File Policies heredadas (NIST CSF 2.0: `GV.RM-02`) `[Decisión / Propuesta Editorial]`.

### M-05: Revisión ejecutiva de KPIs operacionales (MTTA, MTTC, Cobertura) y comité de datos
- **Objetivo:** Presentar ante el CISO y los Data Owners el desempeño mensual del programa, las señales tempranas de degradación y la priorización de nuevas oleadas `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** Tablero ejecutivo Power BI / Sentinel Workbook + repositorio de evidencias Purview `[Decisión / Propuesta Editorial]`.
- **Rol Responsable:** SOC Manager + Data Security Lead.
- **Procedimiento Paso a Paso:**
  1. Consolidar los 8 KPIs maestros del módulo (`KPI-01` a `KPI-08`) con tendencia trimestral `[Decisión / Propuesta Editorial]`.
  2. Analizar los incidentes de datos del mes, tiempos MTTA/MTTC y casos donde el cifrado persistente evitó exposición material ante terceros `[Decisión / Propuesta Editorial]`.
  3. Revisar novedades mensuales publicadas en *What's new in Microsoft Purview* y anuncios del Message Center para planificar cambios del mes siguiente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Presentación ejecutiva mensual y minuta de decisiones del comité de gobierno de datos (NIST CSF 2.0: `GV.OV-01`) `[Decisión / Propuesta Editorial]`.

### M-06: Conciliación mensual de cambios administrativos, excepciones y cumplimiento RBAC
- **Objetivo:** Certificar ante Control Interno que el 100% de modificaciones a etiquetas, políticas y membresías de grupos de roles ocurridas en el mes contaron con respaldo documental `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Settings > Roles and scopes` y `Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** GRC / Internal Audit Liaison.
- **Procedimiento Paso a Paso:**
  1. Exportar la configuración completa de etiquetas y políticas de publicación mediante la función *Export policy configuration* o PowerShell (`Get-Label`, `Get-LabelPolicy`, `Get-AutoSensitivityLabelPolicy`) `[Verificado MS Learn]`.
  2. Comparar el snapshot actual contra el snapshot del mes anterior (*configuration drift analysis*) `[Decisión / Propuesta Editorial]`.
  3. Revisar la vigencia de exclusiones temporales en políticas de etiquetado obligatorio o auto-labeling y revocar las vencidas `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Snapshot mensual versionado de configuración y matriz de conciliación de cambios al 100% (NIST CSF 2.0: `GV.OV-03`) `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Revisión de taxonomía, esquema moderno Label Groups y compatibilidad de derechos
- **Objetivo:** Validar que la taxonomía (3 a 5 grupos principales recomendados), los derechos de uso (`VIEW`/`EXTRACT`) y el esquema moderno de **Label groups** respondan a nuevos requisitos de negocio, IA y regulaciones regionales `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Sensitivity labels` y `Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Security Architect + Legal & Privacy + Data Owners.
- **Procedimiento Paso a Paso:**
  1. Si el tenant aún mantiene etiquetas padre clásicas, planificar y probar en tenant de preproducción la migración irreversible hacia **Label groups** (`Migrate to the modern label scheme`), resolviendo conflictos de nombres y despublicando subetiquetas residuales innecesarias con los scripts oficiales de PowerShell `[Verificado MS Learn]`.
  2. Auditar con PowerShell todas las etiquetas cifrantes confirmando cuáles otorgan `EXTRACT` (elegibles para Microsoft 365 Copilot y agentes) y cuáles lo restringen deliberadamente `[Verificado MS Learn]`.
  3. Contrastar junto a Legal y Privacidad cambios regulatorios (por ejemplo, Ley 21.719 en Chile vigente desde dic-2026, LFPDPPP en México o GDPR) y actualizar mapeos en Compliance Manager `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta trimestral de revisión de taxonomía y matriz actualizada de derechos RMS vs. IA (NIST CSF 2.0: `GV.OC-01`, `GV.PO-02`) `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Certificación de accesos (Access Reviews) sobre Role Groups de Purview y Super Users
- **Objetivo:** Recertificar mediante revisiones formales quiénes conservan elegibilidad PIM en roles críticos de Information Protection y acceso a claves criptográficas `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Identity governance > Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Admin + CISO Delegate.
- **Procedimiento Paso a Paso:**
  1. Ejecutar campaña trimestral de *Access Reviews* sobre los grupos respaldados en Entra ID para `Information Protection Admins`, `Data Classification Content Viewer`, `Information Protection Investigators` y el grupo de `Azure RMS Super Users` `[Verificado MS Learn]`.
  2. Revocar automáticamente cuentas sin justificación vigente o que hayan cambiado de puesto `[Verificado MS Learn]`.
  3. Verificar cuentas de emergencia (*break-glass*) y custodios de Azure Key Vault / servicio DKE `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte cerrado de campaña *Access Reviews* en Entra ID Governance (NIST CSF 2.0: `PR.AA-05`) `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Simulacro práctico (Tabletop & Live Drill) de contención y revocación criptográfica
- **Objetivo:** Validar en condiciones realistas la velocidad y coordinación entre SOC, Information Protection, Identidad y Legal ante la exfiltración confirmada de documentos confidenciales y la necesidad de recuperación con Super User `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** Entorno controlado en `security.microsoft.com`, `purview.microsoft.com` y PowerShell (`AIPService` / `ExchangeOnlineManagement`) `[Verificado MS Learn]`.
- **Rol Responsable:** SOC Manager + Incident Response Lead + Legal.
- **Procedimiento Paso a Paso:**
  1. Simular un escenario de exfiltración de archivos etiquetados *Highly Confidential* hacia un destino externo combinado con compromiso de credenciales `[Decisión / Propuesta Editorial]`.
  2. Ejecutar cronometradamente revocación de acceso documental / ajuste de permisos RMS, revocación de sesiones en Entra ID y verificación de denegación efectiva (`AH-02`) `[Verificado MS Learn]`.
  3. Ejercitar en paralelo una solicitud autorizada de inspección forense en eDiscovery sobre archivos cifrados validando *reasoning over data* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe post-ejercicio con tiempos medidos, brechas detectadas y plan de mejora (NIST CSF 2.0: `RS.MA-04`, `RC.IM-02`) `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Auditoría criptográfica anual de claves raíz (BYOK, Customer Key y Double Key Encryption)
- **Objetivo:** Auditar la custodia, disponibilidad geográfica, respaldos HSM y procedimientos de rotación o recuperación ante desastres del material criptográfico del tenant `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://portal.azure.com` (Azure Key Vault / Managed HSM), infraestructura del servicio **DKE** y PowerShell `AIPService` `[Verificado MS Learn]`.
- **Rol Responsable:** Lead Enterprise Security Architect + Key Custodian + CISO.
- **Procedimiento Paso a Paso:**
  1. Verificar el estado de la clave raíz del tenant en Azure RMS (`Get-AipServiceKeys`), políticas de acceso RBAC/inmutabilidad en Azure Key Vault / Managed HSM para BYOK y **Customer Key** (`Data Encryption Policies` y *availability key*) `[Verificado MS Learn]`.
  2. Si la organización opera **Double Key Encryption (DKE)**, auditar certificados TLS, alta disponibilidad, respaldos offline de claves privadas y segregación estricta respecto a administradores de Microsoft 365 `[Verificado MS Learn]`.
  3. Validar que nunca se hayan eliminado etiquetas cifrantes históricas necesarias para abrir archivos archivados de largo plazo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Dictamen anual de custodia y resiliencia criptográfica firmado por Key Custodian y CISO (NIST CSF 2.0: `GV.RM-01`, `PR.DS-01`) `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Investigación forense ante remoción o degradación masiva de etiquetas por posible Insider o cuenta comprometida
- **Disparador:** Detección de >= 5 eventos `Label removed` o `Label changed` (downgrade) sobre activos *Confidential / Highly Confidential* por un mismo usuario en < 60 minutos, o alerta correlacionada con inicio de sesión riesgoso / próximo cese laboral `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://security.microsoft.com > Incidents & alerts` + `Advanced hunting` y `https://purview.microsoft.com > Solutions > Information Protection > Explorers > Activity explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Information Protection Investigator.
- **Secuencia Operativa:**
  1. Abrir expediente de incidente en `security.microsoft.com` y ejecutar consulta KQL sobre los últimos 30 días del usuario para reconstruir la línea de tiempo completa (lecturas previas, descargas, cambios de etiqueta, envíos por correo, subidas web o impresiones) `[Verificado MS Learn]`.
  2. Cruzar con `SigninLogs` / `AADUserRiskEvents` en Entra ID para distinguir compromiso externo de identidad (IP anómala, token replay) frente a actor interno autenticado desde su equipo habitual `[Verificado MS Learn]`.
  3. Consultar nivel de riesgo en Insider Risk Management y verificar si los archivos desprotegidos fueron copiados a USB, red o nube personal `[Verificado MS Learn]`.
  4. Si se confirma intención maliciosa o compromiso, activar de inmediato `AH-02` y solicitar preservación legal en Purview eDiscovery `[Verificado MS Learn]`.
- **Evidencia Auditable:** Línea de tiempo forense exportada e informe de triaje vinculado al incidente en Defender XDR (NIST CSF 2.0: `RS.AN-03`, MITRE: `Defense Evasion / T1562`).

### AH-02: Contención criptográfica inmediata (revocación RMS, bloqueo de cuenta y preservación de evidencia)
- **Disparador:** Confirmación de exfiltración o compartición no autorizada de documentos protegidos con Azure RMS o correo cifrado con Advanced Message Encryption `[Verificado MS Learn]`.
- **Consola y Ruta:** PowerShell (`AIPService` / `ExchangeOnlineManagement`), `https://entra.microsoft.com` y `https://purview.microsoft.com > Solutions > eDiscovery` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2/L3 + Information Protection Admin + Identity Admin.
- **Secuencia Operativa:**
  1. Si existe compromiso de cuenta, bloquear inicio de sesión en Microsoft Entra ID y ejecutar revocación inmediata de todos los tokens de actualización activos (`Revoke-MgUserSignInSession`), invalidando la renovación de licencias de uso RMS para nuevos dispositivos `[Verificado MS Learn]`.
  2. Revocar el acceso a documentos rastreados protegidos con RMS (`Set-AipServiceDocumentRevoked`) o revocar correos externos cifrados mediante **Purview Advanced Message Encryption** en el portal de auditoría/OME `[Verificado MS Learn]`.
  3. Tener en cuenta y documentar en la evaluación de impacto la ventana de caché offline de la licencia de uso (`Use License` válida por defecto 30 días salvo etiquetas críticas configuradas con `Allow offline access = Never` o `0-1 días`) `[Verificado MS Learn]`.
  4. Aplicar retención de preservación (*eDiscovery Hold*) sobre el buzón y OneDrive del usuario involucrado para impedir destrucción de evidencia `[Verificado MS Learn]`.
- **Evidencia Auditable:** Comandos/logs de revocación ejecutados, confirmación de revocación de sesión Entra ID y constancia de *Hold* en eDiscovery (NIST CSF 2.0: `RS.MI-01`, MITRE: `Exfiltration / T1567`).

### AH-03: Remediación de urgencia por oversharing crítico en contenedores o exposición en Microsoft 365 Copilot
- **Disparador:** Hallazgo de repositorio SharePoint o equipo Teams con acceso `Everyone except external users` o invitados externos que aloja documentos sensibles sin cifrado o expuestos inadvertidamente en respuestas de Microsoft 365 Copilot `[Verificado MS Learn]`.
- **Consola y Ruta:** SharePoint Admin Center, `https://purview.microsoft.com` y PowerShell (`Microsoft.Online.SharePoint.PowerShell`) `[Verificado MS Learn]`.
- **Rol Responsable:** Collaboration Security Admin + Information Protection Admin.
- **Secuencia Operativa:**
  1. Aplicar de inmediato restricción temporal de acceso al sitio (o activar *Restricted SharePoint Search* / exclusión mientras se sanea el contenedor) y asignar etiqueta de contenedor *Highly Confidential* que bloquee invitados externos y vínculos anónimos `[Verificado MS Learn]`.
  2. Configurar etiqueta predeterminada cifrante en la biblioteca documental afectada y lanzar política focalizada de *Service-side auto-labeling* (o etiquetado por script PowerShell/Graph) para cifrar los archivos existentes en reposo `[Verificado MS Learn]`.
  3. Revocar todos los vínculos compartidos externos activos sobre los elementos comprometidos desde SharePoint/Defender XDR `[Verificado MS Learn]`.
  4. Auditar en `Activity explorer` qué usuarios accedieron o consultaron vía `Copilot interaction` dichos archivos durante la ventana de exposición `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de cambio de etiqueta del contenedor, vínculos revocados y lista auditada de accesos previos (NIST CSF 2.0: `RS.MI-02`, MITRE: `Collection / T1213`).

### AH-04: Reversión de emergencia ante auto-etiquetado erróneo masivo o cambio administrativo no autorizado
- **Disparador:** Activación defectuosa de una política de auto-etiquetado que cifra erróneamente archivos operativos críticos interrumpiendo procesos de negocio, o detección en `D-02` de modificación administrativa sin autorización `[Verificado MS Learn]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Information Protection > Auto-labeling` y Security & Compliance PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Information Protection Admin + SOC Incident Commander.
- **Secuencia Operativa:**
  1. Pausar o devolver de inmediato la política de auto-etiquetado afectada a modo simulación (`Set-AutoSensitivityLabelPolicy -Mode TestWithoutNotifications`) para detener nuevas aplicaciones `[Verificado MS Learn]`.
  2. Si hubo cambio administrativo no autorizado, suspender los privilegios PIM del administrador involucrado, restaurar la configuración exacta desde el snapshot mensual (`M-06`) y abrir investigación de seguridad `[Decisión / Propuesta Editorial]`.
  3. Identificar el lote exacto de archivos afectados mediante `Activity explorer` (`Auto-labeling` / `Policy ID`) y ejecutar remediación controlada de re-etiquetado sin eliminar jamás la etiqueta cifrante del catálogo global `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de desactivación de política, listado de activos restaurados e informe de causa raíz (NIST CSF 2.0: `RC.RP-01`).

### AH-05: Escalamiento regulatorio y extracción de evidencia ante brecha confirmada de datos personales o regulados
- **Disparador:** Incidente confirmado de acceso no autorizado o fuga de datos personales/regulados donde el activo carecía de cifrado efectivo o el actor poseía credenciales válidas de descifrado `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://purview.microsoft.com > Solutions > Audit`, `eDiscovery` y `Data Explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** CISO + DPO / Legal & Privacy + SOC Manager.
- **Secuencia Operativa:**
  1. Cuantificar exactamente el universo de registros y tipos de información sensible comprometidos (SITs, EDM, etiquetas) mediante búsqueda en Purview Audit y eDiscovery `[Verificado MS Learn]`.
  2. Determinar y probar criptográficamente si los archivos extraídos estaban protegidos con cifrado Azure RMS o DKE inaccesible para el atacante (evidencia técnica clave de exención o atenuación regulatoria) `[Verificado MS Learn]`.
  3. Entregar paquete probatorio con cadena de custodia a Legal y al Delegado de Protección de Datos (DPO) dentro de las primeras 24 horas para cumplir ventanas legales de notificación (ej. 72 horas GDPR o plazos locales en MCSA) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Dossier probatorio forense firmado para Legal/Regulador y acta post-mortem con mejoras de control (NIST CSF 2.0: `RS.CO-02`, `RC.CO-03`).

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL y PowerShell Operativas

#### Consulta 1 — Detección de bajadas de nivel (Downgrades) y remoción masiva de etiquetas (Defender XDR — `CloudAppEvents`) `[Verificado MS Learn]`
```kql
// Detecta usuarios con múltiples remociones o bajadas de etiqueta de sensibilidad en 24h
CloudAppEvents
| where Timestamp > ago(24h)
| where ActionType in ("SensitivityLabelRemoved", "SensitivityLabelUpdated", "FileSensitivityLabelChanged")
| extend Raw = parse_json(RawEventData)
| extend LabelEvent = Raw.SensitivityLabelEventData
| extend NewLabelId = tostring(coalesce(LabelEvent.SensitivityLabelId, Raw.SensitivityLabelId))
| extend OldLabelId = tostring(coalesce(LabelEvent.OldSensitivityLabelId, Raw.OldSensitivityLabelId))
| extend Justification = tostring(LabelEvent.JustificationText)
| where ActionType == "SensitivityLabelRemoved" or isnotempty(OldLabelId)
| summarize TotalCambios = count(), Remociones = countif(ActionType == "SensitivityLabelRemoved"),
            ArchivosAfectados = dcount(tostring(Raw.ObjectId)),
            Justificaciones = make_set(Justification, 5)
  by AccountDisplayName, AccountObjectId, IPAddress
| where TotalCambios >= 5 or Remociones >= 3
| order by Remociones desc, TotalCambios desc
```

#### Consulta 2 — Correlación de remoción de etiqueta con inicio de sesión de riesgo en Entra ID (Microsoft Sentinel) `[Verificado MS Learn]`
```kql
// Correlaciona eliminación/cambio de etiqueta en OfficeActivity con sesiones riesgosas en SigninLogs
let Ventana = 24h;
let SesionesRiesgosas = SigninLogs
| where TimeGenerated > ago(Ventana)
| where RiskLevelDuringSignIn in ("high", "medium")
| project UserPrincipalName, SignInTime = TimeGenerated, RiskLevelDuringSignIn, SignInIP = IPAddress, AppDisplayName;
OfficeActivity
| where TimeGenerated > ago(Ventana)
| where Operation in ("SensitivityLabelRemoved", "FileSensitivityLabelRemoved", "RMSProtectionDisabled")
| join kind=inner SesionesRiesgosas on $left.UserId == $right.UserPrincipalName
| where OperationTime >= SignInTime - 1h
| project TimeGenerated, UserId, Operation, OfficeWorkload, SourceFileName, ClientIP, SignInIP, RiskLevelDuringSignIn
| order by TimeGenerated desc
```

#### Consulta 3 — Detección de eventos de Oversharing Documento vs. Contenedor (`OfficeActivity` / Audit) `[Verificado MS Learn]`
```kql
// Identifica cargas o ediciones donde el archivo supera la sensibilidad del sitio SharePoint/Teams
OfficeActivity
| where TimeGenerated > ago(24h)
| where Operation == "FileSensitivityLabelMismatch"
| project TimeGenerated, UserId, OfficeWorkload, Site_Url, SourceFileName, SourceRelativeUrl, ClientIP
| summarize EventosMismatch = count(), Archivos = make_set(SourceFileName, 10) by Site_Url, UserId
| order by EventosMismatch desc
```

#### Consulta 4 — Monitoreo de interacciones de Microsoft 365 Copilot con activos etiquetados (`CloudAppEvents`) `[Verificado MS Learn]`
```kql
// Audita interacciones de M365 Copilot que referencian archivos con etiquetas de sensibilidad
CloudAppEvents
| where Timestamp > ago(24h)
| where ActionType == "CopilotInteraction"
| extend Raw = parse_json(RawEventData)
| mv-expand Resource = Raw.CopilotEventData.AccessedResources
| where isnotempty(Resource.SensitivityLabelId)
| summarize Interacciones = count(), RecursosUnicos = dcount(tostring(Resource.Id)),
            EtiquetasUsadas = make_set(tostring(Resource.SensitivityLabelId), 10)
  by AccountDisplayName, Application
| order by Interacciones desc
```

#### Consulta 5 — Auditoría diaria de cambios administrativos en etiquetas y políticas (`OfficeActivity`) `[Verificado MS Learn]`
```kql
// Captura modificaciones administrativas sobre etiquetas, políticas de publicación y auto-labeling
OfficeActivity
| where TimeGenerated > ago(24h)
| where Operation in ("New-Label", "Set-Label", "Remove-Label", "New-LabelPolicy", "Set-LabelPolicy",
                      "Remove-LabelPolicy", "New-AutoSensitivityLabelPolicy", "Set-AutoSensitivityLabelPolicy")
| project TimeGenerated, UserId, Operation, Parameters, ClientIP
| order by TimeGenerated desc
```

#### Consulta 6 — Exportación histórica automatizada de Activity Explorer y Content Explorer (Security & Compliance PowerShell) `[Verificado MS Learn]`
```powershell
# Conectar a Security & Compliance PowerShell y exportar actividad de etiquetado paginada (>30 días histórico)
Connect-IPPSSession
$End = Get-Date
$Start = $End.AddDays(-7)
$Result = Export-ActivityExplorerData -StartTime $Start -EndTime $End -PageSize 5000 -OutputFormat Json
$AllRecords = @($Result.ResultData)
while (-not $Result.LastPage) {
    $Result = Export-ActivityExplorerData -StartTime $Start -EndTime $End -PageSize 5000 -PageCookie $Result.WaterMark -OutputFormat Json
    $AllRecords += $Result.ResultData
}
$AllRecords | Out-File -FilePath ".\AuditExports\MIP_ActivityExplorer_$($End.ToString('yyyyMMdd')).json" -Encoding utf8
```

#### Consulta 7 — Verificación de configuración de SharePoint Online, PDF Labeling, Super User y derechos `EXTRACT` (PowerShell) `[Verificado MS Learn]`
```powershell
# 1. Validar integración de Sensitivity Labels y soporte PDF en SharePoint Online
Get-SPOTenant | Select-Object EnableAIPIntegration, EnableSensitivityLabelforPDF, DisableDocumentLibraryDefaultLabeling

# 2. Verificar estado del rol Super User en Azure Rights Management
Connect-AipService
Get-AipServiceSuperUserFeature
Get-AipServiceSuperUser

# 3. Inventariar etiquetas con cifrado y bloqueo de análisis de contenido (Copilot)
Get-Label | Where-Object { $_.EncryptionEnabled -eq $true } |
    Select-Object DisplayName, ImmutableId, Priority, EncryptionRightsDefinitions, Settings
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Componente | Señal de "Proof of Life" Verificable | Comando / Superficie de Comprobación | Estado Esperado |
|---|---|---|---|
| **Integración SharePoint + PDF Labeling** | Ambos flags devuelven `True` en el tenant `[Verificado MS Learn]` | `(Get-SPOTenant).EnableAIPIntegration` y `EnableSensitivityLabelforPDF` | `True` / `True` |
| **Coautoría para archivos cifrados** | Opción activada en configuración del tenant `[Verificado MS Learn]` | `purview.microsoft.com > Settings > Information Protection > Co-authoring` | `Enabled` |
| **Auto-labeling en servicio (SPO/OD/EXO)** | Políticas activas procesando sin exceder 500k archivos/día `[Verificado MS Learn]` | `Auto-labeling > Insights tab` | Tasa de fallo < 2% `[Decisión / Propuesta Editorial]` |
| **Azure RMS Super User** | Característica deshabilitada salvo excepción documentada `[Verificado MS Learn]` | `Get-AipServiceSuperUserFeature` | `Disabled` (por defecto) |
| **Information Protection Scanner** | Nodos activos reportando último escaneo exitoso `[Verificado MS Learn]` | `Settings > Information Protection > Scanner > Nodes` | Heartbeat < 24 h `[Decisión / Propuesta Editorial]` |
| **Telemetría en Defender XDR / Sentinel** | Llegada continua de `SensitivityLabelUpdated` / `LabelApplied` `[Verificado MS Learn]` | `CloudAppEvents` / `OfficeActivity` en `security.microsoft.com` | Latencia < 15 min `[Decisión / Propuesta Editorial]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales

> **Nota de Transparencia:** Microsoft proporciona las fuentes de datos (*Posture Reports*, *Insights tab*, *Activity Explorer*, *Content Explorer*, *Usage center* y logs XDR/Sentinel), pero no prescribe metas porcentuales ni SLAs universales. Todas las metas numéricas y frecuencias siguientes constituyen `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
|---|---|---|---|---|---|---|
| **KPI-01** | **Cobertura de Clasificación sobre Datos Sensibles** | `(Elementos etiquetados en SPO/OD/EXO / Total de elementos con SITs detectados) × 100` | `>= 85 %` en tenants M365 E5 (`>= 70 %` en E3) | Mensual | CISO, Data Governance, Reguladores | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tasa de Automatización y Etiquetado por Defecto** | `(Etiquetas aplicadas por Auto-labeling + Default / Total de etiquetas aplicadas) × 100` | `>= 65 %` con tendencia trimestral ascendente | Mensual | Data Security Architect, COO | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Cobertura de Etiquetas de Contenedor en Sitios y Teams** | `(Sitios SharePoint y Teams activos con Container Label / Total de sitios y Teams activos) × 100` | `>= 95 %` (`100 %` en sitios con alcance Copilot) | Semanal | CISO, Collaboration Lead, AI Governance | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Tiempo Medio de Reconocimiento (MTTA — Incidentes Críticos de Datos)** | `Promedio(Timestamp Reconocimiento SOC − Timestamp Generación Alerta)` | `< 60 minutos` (Críticos) / `< 4 horas` (Altos) | Mensual | SOC Manager, Aseguradoras, Auditoría | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Tiempo Medio de Contención Criptográfica (MTTC)** | `Promedio(Timestamp Revocación RMS o Bloqueo Entra − Timestamp Reconocimiento)` | `< 4 horas` (Críticos) / `< 8 horas` (Altos) | Mensual | CISO, SOC Manager | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Éxito de Auto-Labeling en Servicio** | `(Archivos etiquetados exitosamente en pestaña Insights / Total de archivos evaluados para etiquetado) × 100` | `>= 98 %` | Semanal | Information Protection Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tasa de Justificación Válida en Bajadas de Etiqueta (Downgrades)** | `(Eventos de downgrade con justificación de negocio válida / Total de eventos de downgrade auditados) × 100` | `>= 95 %` (`0` remociones masivas sin investigar) | Semanal | SOC L2, Insider Risk Team | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Cumplimiento de Gestión de Cambios Administrativos** | `(Cambios en etiquetas/políticas con ticket ITSM aprobado / Total de cambios en Audit Log) × 100` | `100 %` (tolerancia cero a cambios huérfanos) | Mensual | GRC, Auditoría Interna / Externa | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Características Operativas Verificables |
|---|---|---|
| **Nivel 1** | **Inicial / Reactivo** | Etiquetas creadas sin política global ni cifrado; coexistencia de taxonomías heredadas o add-in AIP obsoleto; sin telemetría integrada al SOC ni visibilidad de datos sensibles en reposo. |
| **Nivel 2** | **Base / Manual Gobernado** | Taxonomía de 3 a 5 niveles publicada en etiquetado nativo (Built-in Office), coautoría y soporte PDF activos en SharePoint/OneDrive, etiquetado manual con justificación en bajadas y revisión reactiva de logs. |
| **Nivel 3** | **Definido / Secure by Default** | Esquema moderno de **Label groups** adoptado; etiqueta predeterminada corporativa activa; etiquetas de contenedor en Teams/SharePoint; auto-etiquetado en cliente activo y auto-labeling en servicio validado por simulación; cadencias diarias/semanales ejecutadas por el SOC. |
| **Nivel 4** | **Gestionado / Cuantitativo e IA-Ready** | Clasificadores avanzados (**EDM** hasta 100M filas, **Trainable Classifiers**, **Named Entities**), **Dynamic Watermarking**, derechos `VIEW`/`EXTRACT` auditados para Microsoft 365 Copilot y agentes, Scanner on-premises cubriendo 100% de file shares críticos y exportación automatizada de KPIs a Power BI/Sentinel. |
| **Nivel 5** | **Optimizado / Defensa Adaptativa Multicloud** | Protección unificada desde M365 hasta **Microsoft Fabric / Power BI** y **Purview Data Map** (SQL, Azure Storage, AWS S3), **DKE / Customer Key** gobernados para activos regulados, contención automatizada vía Playbooks con Managed Identity y evidencia continua mapeada a NIST CSF 2.0. |

### 11.3 Señales de Alerta Temprana de Degradación Operativa `[Decisión / Propuesta Editorial]`

| Señal Anticipatoria | Condición Observada | Riesgo Subyacente | Acción Correctiva Inmediata |
|---|---|---|---|
| **Caída > 20% en eventos diarios de etiquetado** | Reducción abrupta de registros en `OfficeActivity` / `CloudAppEvents` en día hábil normal. | Falla silenciosa de ingesta hacia Sentinel/XDR o despublicación accidental de una política global de etiquetas. | Ejecutar verificación `D-01` y conciliación administrativa `D-02` antes de validar métricas en cero. |
| **Aumento sostenido de Downgrades > 15% semanal** | Crecimiento en cambios hacia etiquetas *Public / General* con justificaciones genéricas. | Fricción excesiva en compartición B2B legítima o evasión deliberada para habilitar extracción externa o IA. | Analizar las 10 justificaciones principales en `S-03` y cazar anomalías por usuario en `D-04`. |
| **Tasa de error > 5% en pestaña Insights de Auto-Labeling** | Incremento de archivos fallidos al aplicar etiquetas en reposo sobre SharePoint/OneDrive. | Archivos bloqueados, PDFs sin soporte habilitado, coautoría desactivada o saturación cercana al techo de 500k/día. | Auditar causas raíz en `S-02` y validar parámetros del tenant en `Consulta 7`. |
| **Proliferación de sitios nuevos sin Container Label** | Sitios SharePoint o Teams creados por autoservicio sin `sensitivityLabel` asignada. | Exposición amplia ante búsqueda interna y Microsoft 365 Copilot (*oversharing*). | Ejecutar barrido Graph `S-04` y exigir etiqueta obligatoria en aprovisionamiento de grupos. |
| **Cero revocaciones ejecutadas pese a incidentes confirmados** | Incidentes de fuga cerrados sin uso de revocación RMS/AME ni corte de sesiones Entra ID. | Brecha de habilitación práctica en el SOC sobre controles activos de contención criptográfica. | Reentrenar al equipo SOC L2/L3 y adelantar ejercicio práctico `SM-01`. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

> **Nota Metodológica:** NIST CSF 2.0 (NIST CSWP 29) define resultados (*outcomes*) agnósticos al fabricante. La siguiente matriz traduce capacidades verificables de Microsoft Purview Information Protection en evidencias objetivas para auditorías internas y regulatorias `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome CSWP 29) | Capacidad Habilitadora en Purview Information Protection | Evidencia Auditable Reproducible y MITRE ATT&CK | Etiqueta |
|---|---|---|---|---|---|
| **GOVERN (GV)** | `GV.OC-01` | La misión organizacional y el contexto de criticidad de la información son comprendidos y comunicados. | Taxonomía corporativa en **Modern Label Groups** con descripciones y *tooltips* visibles en Office, Outlook, Teams y Fabric `[Verificado MS Learn]`. | Exportación de configuración de etiquetas y acta aprobada de taxonomía de datos. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RM-01` | Los objetivos y estrategia de gestión de riesgos son establecidos y acordados por la dirección. | Asociación automática entre nivel de etiqueta y salvaguardas criptográficas (Azure RMS, Customer Key, **Double Key Encryption**) `[Verificado MS Learn]`. | Matriz aprobada de clasificación vs. cifrado y dictamen anual `A-01`. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.OV-03` | El desempeño de la gestión de riesgos cibernéticos es evaluado y revisado para realizar ajustes. | Conciliación diaria/mensual de cambios administrativos (`Set-Label`, `Set-LabelPolicy`) e informes de postura `[Verificado MS Learn]`. | Reporte mensual `M-06` con 100% de cambios conciliados con tickets ITSM. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-02` | Los datos, software y sistemas gestionados por la organización están inventariados. | Descubrimiento continuo con SITs, **EDM (100M filas)**, **Trainable Classifiers**, *Data Explorer* e **Information Protection Scanner** local `[Verificado MS Learn]`. | Exportaciones `Export-ContentExplorerData` y reportes de ciclos del Scanner (`S-05`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-01` | Las vulnerabilidades y exposiciones sobre activos críticos son identificadas y registradas. | Detección de sitios sin etiqueta de contenedor, archivos sensibles sin cifrar y evaluación de riesgo previo a Copilot `[Verificado MS Learn]`. | Inventario Graph semanal de contenedores (`S-04`) y simulaciones de auto-labeling (`S-02`). | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen y gestionan bajo mínimo privilegio. | Derechos granulares Azure RMS (`VIEW`, `EXTRACT`, `PRINT`, `EXPORT`), **Container Labels** con Conditional Access y PIM sobre Role Groups `[Verificado MS Learn]`. | Matriz de derechos `EXTRACT` ante Copilot (`T-01`), campañas *Access Reviews* (`T-02`) y log de Super User (`S-06`) — MITRE `T1078`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` | La confidencialidad, integridad y disponibilidad de los datos en reposo están protegidas. | Cifrado persistente Azure RMS en SharePoint/OneDrive (Office y PDFs), etiquetas predeterminadas de biblioteca, Scanner SMB/SPO Server y DKE `[Verificado MS Learn]`. | Pruebas mensuales de persistencia fuera del perímetro (`M-02`) y estado `EnableSensitivityLabelforPDF = True` — MITRE `T1213`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-02` | La confidencialidad, integridad y disponibilidad de los datos en tránsito y colaboración están protegidas. | Auto-labeling en tránsito en Exchange Online, cifrado OME / Advanced Message Encryption, S/MIME por etiqueta y **Dynamic Watermarking** `[Verificado MS Learn]`. | Evidencia de políticas de correo cifrado y pruebas de marcas de agua dinámicas (`M-02`) — MITRE `T1048`. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-01` | Las redes, servicios y entornos colaborativos se monitorean para detectar eventos potencialmente adversos. | Auditoría continua de `SensitivityLabelRemoved`, downgrades, `FileSensitivityLabelMismatch` y `CopilotInteraction` en XDR/Sentinel `[Verificado MS Learn]`. | Resultados diarios de consultas KQL `D-04`, `D-05` y `D-07` — MITRE `T1562`, `T1005`. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos son analizados para comprender actividades y tácticas asociadas. | Correlación en Microsoft Sentinel / Defender XDR entre degradación de etiquetas, riesgo de identidad Entra ID y alertas de endpoint `[Verificado MS Learn]`. | Reglas analíticas versionadas (`S-07`) y bitácoras de triaje `D-03` — MITRE `T1567`. | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos para evitar la propagación y limitar el impacto sobre los datos. | Revocación de acceso documental RMS / correos AME, ajuste dinámico de permisos de etiqueta y revocación de sesiones Entra ID `[Verificado MS Learn]`. | Registros de ejecución del playbook `AH-02` y métricas MTTC (`KPI-05`). | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.IM-02` | Los planes de recuperación, políticas y procesos operativos se actualizan con lecciones aprendidas. | Continuidad de búsqueda/eDiscovery sobre datos cifrados (*reasoning over data*), reversión controlada `AH-04` y simulacros semestrales `[Verificado MS Learn]`. | Informe del simulacro semestral `SM-01` y actualizaciones de políticas post-incidente. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Destinatario | Nivel | Recursos Oficiales Microsoft Learn y Certificaciones (Nov 2026) | Comunidad Técnica y Ninja Trainings | Competencia Operativa Habilitada |
|---|---|---|---|---|
| **SOC L1 / Analista Junior** | Nivel 1 (Fundamentos) | Ruta oficial *Safeguard sensitive data with Microsoft Purview ninja training scenarios* (`learn.microsoft.com/training/paths/purview-ninja-safeguard-data/`) y fundamentos SC-900 `[Verificado MS Learn]`. | Guía práctica de etiquetas en M365.FM (Mirko Peters, MVP) `[Verificado MS Learn]`. | Ejecución rigurosa de `D-01` a `D-05` (triaje de alertas, lectura de Activity Explorer y detección de oversharing). |
| **Information Protection Admin / Collaboration Admin** | Nivel 2 (Administración) | Certificación oficial **Microsoft Certified: Information Security Administrator Associate (Exam SC-401)** + Credencial aplicada **SC-5003** (*Implement information protection and data loss prevention by using Microsoft Purview*) `[Verificado MS Learn]`. | Serie *Office 365 for IT Pros — MIP Archives* (Tony Redmond, MVP) y guías de diseño conjunto sensibilidad/retención (Joanne Klein, MVP). | Diseño de **Modern Label Groups**, auto-labeling en cliente/servicio, EDM, etiquetas de contenedor, Scanner y migración desde MDCA (`S-01` a `S-05`, `M-01` a `M-04`). |
| **SOC L2/L3 / Detection & IR Engineer** | Nivel 3 (Avanzado SecOps) | Guías de *Advanced Hunting* en Defender XDR (`CloudAppEvents`), conector Purview/M365 en Sentinel y revocación con módulo `AIPService` `[Verificado MS Learn]`. | Laboratorios de detección XDR/Sentinel y Purview en español (Jorge Castañeda, MVP) y videos de *Microsoft Mechanics* (Jeremy Chapman). | Caza avanzada KQL, ajuste de reglas correlacionadas (`S-07`) y ejecución de playbooks de contención y forense (`AH-01` a `AH-04`). |
| **CISO / Data Security Architect / AI Governance** | Nivel 4 (Estrategia y Gobierno) | Modelo oficial *Secure by default with Microsoft Purview* (Pasos 1 a 4), *Data protection for Microsoft 365 Copilot* y *Double Key Encryption* `[Verificado MS Learn]`. | *Purview Lightning Talks* y gobernanza de contenedores/IA (Nikki Chapple, MVP) + resúmenes ejecutivos mensuales (Albert Hoitingh, MVP). | Gobierno del comité mensual (`M-05`), arquitectura Zero Trust para IA/agentes, auditoría anual de claves (`A-01`) y defensa regulatoria ante Directorio. |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Correcciones y Hallazgos Verificados contra Microsoft Learn (`2026-11-11`)

| # | Aspecto Auditado en Material Base (`MSEOP-MD`) | Hallazgo / Estado Vigente a Noviembre de 2026 (`[Verificado MS Learn]`) | Impacto Aplicado en la Guía |
|---|---|---|---|
| **1** | Jerarquía clásica de etiquetas padre y subetiquetas | Desde el **1 de octubre de 2025**, los nuevos tenants usan automáticamente el **Modern label scheme** basado en **Label groups** (que solo admiten nombre, descripción, color y prioridad), con migración irreversible asistida en el portal para tenants previos. | Actualizado en Secciones 2, 3, 8 (`T-01`) y arquitectura JSON. |
| **2** | Referencias heredadas al complemento *AIP Unified Labeling add-in* | El complemento clásico de Office fue retirado definitivamente en abril de 2024; la única vía soportada en Office es el **etiquetado nativo integrado (Built-in)** y el **Microsoft Purview Information Protection client** (3.2.x) para Windows Explorer, Scanner, Viewer y PowerShell. | Incorporado control mensual `M-03` de higiene de versiones en Intune. |
| **3** | Límites de procesamiento en *Service-side auto-labeling* y soporte PDF | Microsoft Learn (`apply-sensitivity-label-automatically`, actualizado el `2026-11-06`) fija el techo máximo agregado en **500.000 archivos etiquetados/día por tenant** en SharePoint y OneDrive (simulación hasta 20M; máx. 100 políticas) y advierte que sin habilitar PDF labeling se omiten los PDFs por completo. | Reflejado en Secciones 2, 3, `S-02` y `10.2`. |
| **4** | Interacción de Microsoft 365 Copilot y agentes con etiquetas y cifrado | Copilot exige derechos `VIEW` y `Copy and extract content (EXTRACT)` para procesar elementos cifrados (excepto al *RMS issuer/owner*), hereda la etiqueta de mayor prioridad en contenido generado y respeta el parámetro PowerShell `BlockContentAnalysisServices`. | Añadida actividad diaria `D-07`, prueba mensual `M-02`, revisión `T-01` y KQL 4. |
| **5** | Etiquetado en apps cloud vía File Policies de Defender for Cloud Apps | Las **File Policies** de Defender for Cloud Apps se retiran el **6 de enero de 2027**; el asistente *DLP to Purview migration* convierte políticas de auto-labeling para SharePoint y OneDrive hacia Purview. | Creada actividad mensual `M-04` de seguimiento de migración y decomiso. |
| **6** | Supuesto conector independiente de Purview IP como única vía hacia Sentinel | El conector dedicado *Microsoft Purview Information Protection* en Sentinel permanece como flujo complementario, mientras que la telemetría operativa primaria de etiquetas y RMS ingresa vía **Unified Audit Log (`OfficeActivity`)** y **`CloudAppEvents`** en el portal unificado `security.microsoft.com` (antes del retiro de Sentinel en Azure Portal el `2027-03-31`). | Corregidas rutas, `D-01` y consultas KQL 1 a 5. |
| **7** | Ventana histórica de reportes nativos y permisos de exploración | Los *Posture reports* de Information Protection operan en vista previa con ventana móvil de **30 días**, exigiendo exportaciones periódicas (`Export-ActivityExplorerData` / `Export-ContentExplorerData`), y segregando `Data Classification List Viewer` de `Data Classification Content Viewer`. | Incorporado en matriz RBAC (Sección 4), `S-03`, `M-01` y Consulta 6. |
| **8** | Nomenclatura de licencias Enterprise Purview e IA agéntica | La descripción oficial del servicio Purview (`2026-11-09`) denomina **Microsoft Purview Suite** a *Microsoft 365 E5 Compliance* (renombre oct-2025) e incorpora soporte para cargas agénticas con **Microsoft 365 E7** y **Agent 365** (GA mayo de 2026). | Actualizada matriz de licenciamiento en Sección 2.2 y JSON. |

### 14.2 Decisiones y Propuestas Editoriales Explícitas

| # | Elemento en la Guía | Clasificación | Justificación Arquitectónica y Operativa |
|---|---|---|---|
| **1** | Estructura de 30 actividades en 7 horizontes (`D`, `S`, `M`, `T`, `SM`, `A`, `AH`) | `[Decisión / Propuesta Editorial]` | Microsoft documenta las herramientas de administración, auditoría y respuesta, pero no prescribe un calendario operativo único para el SOC; esta estructura garantiza control continuo y trazabilidad de auditoría. |
| **2** | Ventanas de SLA (MTTA < 1 h / MTTC < 4 h en incidentes críticos) y umbrales de anomalía (>20% caída de logs, >=5 bajadas/24h) | `[Decisión / Propuesta Editorial]` | Benchmarks consultivos diseñados para contener exposiciones de datos antes de su propagación externa; cada organización debe calibrarlos contra su línea base real. |
| **3** | Metas cuantitativas de los 8 KPIs (`>=85%` cobertura E5, `>=98%` éxito auto-labeling, `100%` cambios con ticket) | `[Decisión / Propuesta Editorial]` | Permiten medir retorno de inversión (ROI) y madurez ante comités ejecutivos y auditores SOC2/ISO/regulatorios sin presentarlos como estándares normativos de Microsoft. |
| **4** | Ventanas horarias de elevación JIT en Entra PIM (2 h para `Content Viewer`, 4 h para `IP Admin`) y aprobación dual | `[Decisión / Propuesta Editorial]` | Materializan el principio de mínimo privilegio y privacidad por diseño sobre roles capaces de alterar políticas globales o leer datos confidenciales. |
| **5** | Modelo de Madurez Operacional de 5 niveles y mapeo probatorio de 12 subcategorías NIST CSF 2.0 | `[Decisión / Propuesta Editorial]` | Traduce los resultados (*outcomes*) de NIST CSWP 29 y la guía *Secure by Default* en una hoja de ruta medible y defendible ante auditoría externa. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Learn about sensitivity labels* (actualizado oct-2026): `https://learn.microsoft.com/en-us/purview/sensitivity-labels`
- **REF-02:** Microsoft Learn — *Migrate parent sensitivity labels to sensitivity label groups (Modern label scheme)*: `https://learn.microsoft.com/en-us/purview/migrate-sensitivity-label-scheme`
- **REF-03:** Microsoft Learn — *Automatically apply a sensitivity label to Microsoft 365 data (500k/day limit & PDF support)* (actualizado 06-nov-2026): `https://learn.microsoft.com/en-us/purview/apply-sensitivity-label-automatically`
- **REF-04:** Microsoft Learn — *Restrict access to content by using sensitivity labels to apply encryption (Azure RMS & Dynamic watermarks)*: `https://learn.microsoft.com/en-us/purview/encryption-sensitivity-labels`
- **REF-05:** Microsoft Learn — *What is Double Key Encryption (DKE)?*: `https://learn.microsoft.com/en-us/purview/double-key-encryption`
- **REF-06:** Microsoft Learn — *Learn about exact data match (EDM) based sensitive information types (100M rows)*: `https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits`
- **REF-07:** Microsoft Learn — *Configure a default sensitivity label for a SharePoint document library*: `https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-default-label`
- **REF-08:** Microsoft Learn — *Use sensitivity labels with Microsoft Teams, Microsoft 365 Groups, and SharePoint sites*: `https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites`
- **REF-09:** Microsoft Learn — *Learn about the Microsoft Purview Information Protection scanner*: `https://learn.microsoft.com/en-us/purview/deploy-scanner`
- **REF-10:** Microsoft Learn — *Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Channel Agent considerations*: `https://learn.microsoft.com/en-us/purview/ai-m365-copilot-considerations`
- **REF-11:** Microsoft Learn — *Introduction to secure by default with Microsoft Purview (Steps 1–4)*: `https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-secure-by-default-intro`
- **REF-12:** Microsoft Learn — *Microsoft Purview service description (Licensing matrix & Purview Suite)* (actualizado 09-nov-2026): `https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description`
- **REF-13:** Microsoft Learn — *Migrate file policies to Microsoft Purview (Retiro 6 de enero de 2027)*: `https://learn.microsoft.com/en-us/defender-cloud-apps/migrate-file-policies-to-purview`
- **REF-14:** Microsoft Learn — *Sensitivity labels in Power BI and Microsoft Fabric* y *Purview Data Map sensitivity labels*: `https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-security-sensitivity-label-overview`

### Blogs Oficiales y Empleados de Microsoft
- **REF-15:** Aashish Ramdas (Microsoft) — *Retirement notification for the Azure Information Protection Unified Labeling add-in for Office*: `https://techcommunity.microsoft.com/blog/microsoft-security-blog/retirement-notification-for-the-azure-information-protection-unified-labeling-ad/3791908`
- **REF-16:** Alym Rayani (Microsoft Security Blog) — *What's new in Microsoft Security (Purview auto-labeling & Data Security updates, 2026)*: `https://www.microsoft.com/en-us/security/blog/2026/08/27/whats-new-in-microsoft-security-august-2026/`

### Comunidad Técnica y MVPs de Seguridad / Microsoft 365
- **REF-17:** Tony Redmond (Microsoft MVP) — *Microsoft Information Protection Archives — Office 365 for IT Pros*: `https://office365itpros.com/category/microsoft-information-protection/`
- **REF-18:** Nikki Chapple (Dual Microsoft MVP, M365 & Security) — *Purview Lightning Talks: Container Sensitivity Labels That Fix Oversharing Fast (2026)*: `https://nikkichapple.com/purview-lightning-talks-microsoft-security-community/`
- **REF-19:** Albert Hoitingh (Microsoft MVP) — *Things to Know About Microsoft Purview (2026 Executive Summaries)*: `https://alberthoitingh.com/2026/09/04/things-to-know-about-microsoft-purview-september-2026/`

### Marcos Normativos y Arquitectónicos
- **REF-20:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)*: `https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`

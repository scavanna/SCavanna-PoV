# Guía Maestra de Excelencia Operacional: Microsoft Purview Data Lifecycle Management y Records Management

## 1. Portada y Ficha de Control Documental

| Atributo Documental | Definición Oficial y Alcance Operativo |
| --- | --- |
| **Identificador del Módulo** | `16_Purview_Data_Lifecycle_y_Records_Management` |
| **Slug Canónico** | `Purview_Data_Lifecycle_y_Records_Management` |
| **Nombre Completo** | Microsoft Purview Data Lifecycle Management y Records Management |
| **Categoría Maestra** | Seguridad de Datos, Cumplimiento y Gobierno (Microsoft Purview) |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | `Compilado MSEOP-MD + Revalidado Learn` (consolidación depurada de `MSEOP-MD\Purview DLCM`, cruce de referentes con *Ninja Training Seguridad Microsoft 2026 — Módulo 09* y revalidación directa en Microsoft Learn MCP al 11 de noviembre de 2026) |
| **Relación con Microsoft 365 E5** | `Incluido en Microsoft 365 E5` (capacidades base estáticas y etiquetas manuales en M365 E3; auto-aplicación, Adaptive Scopes, Cloud Attachments, Auto-Expanding Archiving hasta 3 TB y todo Records Management incluidos en Microsoft 365 E5 / E7 y Microsoft Purview Suite) `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://purview.microsoft.com` (`Solutions > Data Lifecycle Management` y `Solutions > Records Management`), `https://admin.exchange.microsoft.com`, Security & Compliance PowerShell (`Connect-IPPSSession`) y Microsoft Graph Records Management / Audit APIs `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Oficial de Cumplimiento y Privacidad (DPO), Records Manager, Data Governance Lead, SOC Manager, Analistas GRC / Auditoría Interna, Administradores de Microsoft Purview, Exchange Online y SharePoint Online, y Asesoría Legal (eDiscovery) `[Decisión / Propuesta Editorial]` |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), ISO 15489-1:2016 (confirmada 2021), ISO/IEC 27001:2022, ISO/IEC 27701, SEC Rule 17a-4 / FINRA, GDPR / LGPD y marcos regionales de archivos y privacidad (Ley 594 Colombia, LGA y nueva LFPDPPP 2025 México, Ley 21.719 Chile, Ley 25.326 Argentina, Ley 7593 Paraguay) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]` |

> **Nota de Consolidación y Saneamiento Documental (Corte `2026-11-11`):** Durante la auditoría de las fuentes originales en `MSEOP-MD\Purview DLCM` (`0404 - Purview DLCM - Bloques - SecOps` y `Version Consolidada (1)`), se detectó y corrigió una contaminación cruzada donde se habían exportado por error bloques genéricos del SOC transversal centrados en Microsoft Sentinel (triage de incidentes SIEM, playbooks Logic Apps genéricos, ruta generalista L1-L3 y MTTD/MTTR de amenazas de red). Todo bloque ajeno fue descartado y sustituido íntegramente por procedimientos operativos nativos, verificables y auditables de **Microsoft Purview Data Lifecycle Management (DLCM)** y **Microsoft Purview Records Management (RM)** revalidados contra Microsoft Learn al 11 de noviembre de 2026 `[Decisión / Propuesta Editorial]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica a Noviembre de 2026: Reducción de Superficie ROT, Preparación para IA y Resiliencia Legal

En el panorama operativo de ciberseguridad y gobierno corporativo a noviembre de 2026, **Microsoft Purview Data Lifecycle Management** y **Microsoft Purview Records Management** constituyen un control estructural primario de defensa en profundidad sobre el dato, superando ampliamente el enfoque histórico de mero archivo documental `[Decisión / Propuesta Editorial]`. Ambas soluciones gobiernan el ciclo de vida *in-place* —sin duplicar información hacia bóvedas propietarias ni requerir agentes externos de captura— sobre correos electrónicos, sitios documentales, mensajería colaborativa, adjuntos modernos compartidos por vínculo (*cloud attachments*) e interacciones completas de usuarios con **Microsoft 365 Copilot, Copilot Studio, agentes IA empresariales y aplicaciones de IA generativa de terceros** `[Verificado MS Learn]`.

Para un CISO y un Arquitecto de Seguridad, mantener volúmenes crecientes de datos redundantes, obsoletos o triviales (**ROT — Redundant, Obsolete, Trivial**) multiplica tres vectores de riesgo material `[Decisión / Propuesta Editorial]`:
1. **Amplificación del *Oversharing* en Inteligencia Artificial:** Microsoft 365 Copilot, los agentes de Copilot Studio y los agentes empresariales razonan sobre todo el contenido al que el usuario tiene permiso de lectura en Microsoft Graph. Conservar contratos borradores de hace una década, hojas salariales obsoletas o chats antiguos sin purgar amplía exponencialmente la exposición accidental de información sensible en respuestas generadas por IA `[Decisión / Propuesta Editorial]`.
2. **Expansión del Radio de Impacto (*Blast Radius*) ante Exfiltración o Doble Extorsión:** Bajo el principio Zero Trust de *Asumir Brecha*, el único dato inmune al robo por un actor externo o un *insider* saliente es aquel que fue destruido de forma legítima y defendible al vencer su obligación legal o valor de negocio `[Decisión / Propuesta Editorial]`.
3. **Incumplimiento Dual Regulatorio/Privacidad y Deuda de Retención (*Retention Debt*):** Mientras normativas sectoriales (SEC 17a-4, SOX, leyes generales de archivos) exigen inmutabilidad verificable durante plazos estrictos, leyes modernas de protección de datos personales sancionan conservar PII más allá de su finalidad. Adicionalmente, configurar políticas globales de *solo retener* provoca una acumulación indefinida de **Inactive Mailboxes** y cuentas de OneDrive de exempleados que degrada costos de eDiscovery y gobernanza `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

Es indispensable distinguir arquitectónicamente entre **retención (cumplimiento)** y **respaldo / backup (resiliencia operativa)**: Microsoft Purview DLCM garantiza preservación legal y eliminación defensible conforme a normas, mientras que la restauración masiva punto-en-el-tiempo ante desastres operativos o corrupción masiva corresponde a *Microsoft 365 Backup* `[Verificado MS Learn]`.

### 2.2 Matriz Oficial de Licenciamiento: Microsoft 365 E3 vs. Microsoft 365 E5 / Microsoft Purview Suite

La frontera exacta entre licencias base (**Microsoft 365 E3 / Office 365 E3**) y suites avanzadas (**Microsoft 365 E5 / E7**, **Microsoft Purview Suite** —antes denominado *Microsoft Purview E5 Compliance*— o la mini-suite *Information Protection & Governance*) define las capacidades de automatización y escala disponibles en el tenant `[Verificado MS Learn]`:

| Capacidad Técnica | Microsoft 365 E3 / Office 365 E3 | Microsoft 365 E5 / E7 / Microsoft Purview Suite | Modelos Complementarios (Pay-As-You-Go / Add-ons) | Estado |
| --- | --- | --- | --- | --- |
| **Políticas de retención con ámbitos estáticos (*Static Scopes*)** | Incluido para Exchange, SharePoint, OneDrive, Microsoft 365 Groups, Teams (chats y canales) y Viva Engage | Incluido (con capacidad adicional de *Adaptive Policy Scopes*) | Retención de M365 Copilot y Copilot Chat cubierta cuando el usuario cuenta con licencia Microsoft 365 Copilot | `[Verificado MS Learn]` |
| **Etiquetas de retención manuales (estándar, sin declaración de registro)** | Incluido: creación, publicación en políticas de etiquetas y aplicación manual por el usuario en apps | Incluido | N/A | `[Verificado MS Learn]` |
| **Auto-aplicación de etiquetas de retención (*Auto-apply retention labels*)** | No incluido | Incluido mediante SITs, palabras clave / propiedades indexadas (KeyQL), etiquetas de sensibilidad o *Trainable Classifiers* (nota: *Trainable Classifiers* exige M365 E5 / Purview Suite; no está incluido en Office 365 E5 aislado) | N/A | `[Verificado MS Learn]` |
| **Retención automática de *Cloud Attachments*** | No incluido | Incluido: aplica automáticamente etiqueta de retención a la versión exacta del archivo compartido por enlace en Teams, Exchange, Viva Engage y Copilot | N/A | `[Verificado MS Learn]` |
| **Ámbitos de política adaptables (*Adaptive Policy Scopes*)** | No incluido | Incluido: alcance dinámico evaluado diariamente sobre atributos de usuarios Entra ID, sitios SharePoint y grupos Microsoft 365 | N/A | `[Verificado MS Learn]` |
| **Microsoft Purview Records Management integral** | No incluido | Incluido al 100%: *File Plan* (import/export CSV y descriptores), *Records* (bloqueados/desbloqueados), *Regulatory Records*, *Event-based retention*, *Multi-stage Disposition Reviews* (hasta 5 etapas) y *Proof of Disposal* (hasta 7 años) | También disponible sobre E3 vía add-on *Microsoft Purview Suite* o mini-suite *Information Protection & Governance* | `[Verificado MS Learn]` |
| **Archive Mailboxes y Auto-Expanding Archiving** | Buzón de archivo (100 GB); auto-expansión hasta 1,5 TB con Exchange Online Plan 2 | Límite máximo ampliado de **1,5 TB a 3 TB** desde mediados/fines de octubre de 2026 para M365 E5/A5/G5, O365 E5/A5/G5, E7 y Microsoft Purview Suite (exige mantener habilitado el plan de servicio *Records Management*) | Sin costo extra por GB en licencias elegibles; soporta tasa de crecimiento de hasta 1 GB/día | `[Verificado MS Learn]` |
| **Inactive Mailboxes (retención de exempleados)** | Soportado con Exchange Online Plan 2 o archivo/hold elegible aplicado antes de borrar la cuenta | Soportado sin consumir licencia activa tras el borrado del usuario en Entra ID; administración escalable vía *Adaptive Scopes* | N/A | `[Verificado MS Learn]` |
| **Retención de prompts y respuestas en IA empresarial y de terceros** | No incluido para apps IA no-M365 | Soportado para *Microsoft Copilot experiences* (*Security Copilot*, *Copilot in Fabric*, *Copilot Studio*), *Enterprise AI apps* (*Entra-registered*, *ChatGPT Enterprise*, *Microsoft Foundry*) y *Other AI apps* (*ChatGPT*, *Google Gemini*, *DeepSeek*) | Requiere **Collection Policy** con captura de contenido habilitada y facturación **Pay-As-You-Go** en Azure (con alineación futura anunciada hacia M365 E7 / SKU Agent 365 para agentes Foundry/Entra) | `[Verificado MS Learn]` |
| **Microsoft 365 Archive (almacenamiento frío en SharePoint)** | Elegible | Elegible | Medidor **Pay-As-You-Go** en Azure cuando la suma de almacenamiento activo + archivado supera la cuota incluida del tenant | `[Verificado MS Learn]` |

### 2.3 Los 4 Principios Oficiales de Precedencia de Retención y Alineación Zero Trust

Cuando múltiples políticas de retención o una etiqueta de retención coinciden sobre un mismo elemento, Microsoft Purview evalúa un árbol de decisión determinístico. Antes de aplicar los cuatro principios, si el elemento está sujeto a un **eDiscovery Hold** (o a tecnologías legadas como *Litigation Hold* o *In-Place Hold*), **siempre se retiene primero**, salvo que sea objeto de una **Priority Cleanup** aprobada (la cual, a su vez, jamás puede sobrescribir un *Record* ni un *Regulatory Record*) `[Verificado MS Learn]`. Fuera de ese supuesto, rigen en estricto orden secuencial los **cuatro principios oficiales de precedencia de retención** `[Verificado MS Learn]`:

1. **Principio 1 — La retención prevalece sobre la eliminación (*Retention wins over deletion*):** El borrado permanente se suspende siempre que exista cualquier política o etiqueta activa con acción de retener. El usuario puede eliminar el archivo o correo de su bandeja visible, pero una copia íntegra permanece resguardada en `Preservation Hold Library`, `Recoverable Items` o `SubstrateHolds` `[Verificado MS Learn]`.
2. **Principio 2 — El período de retención más largo gana (*Longest retention period wins*):** Entre múltiples reglas de retención, prevalece la fecha efectiva de expiración más lejana calculada para ese elemento concreto (por ejemplo, una retención de 5 años contada desde *última modificación* ganará sobre una de 7 años contada desde *creación* si el documento fue editado en el cuarto año) `[Verificado MS Learn]`.
3. **Principio 3 — Lo explícito prevalece sobre lo implícito en las eliminaciones (*Explicit wins over implicit for deletions*):** Resuelta toda exigencia de retención, una **etiqueta de retención** aplicada a un ítem individual (explícita, sin importar si se aplicó manualmente, por valor predeterminado de biblioteca o por auto-aplicación) gana siempre sobre cualquier **política de retención** a nivel contenedor (implícita), aun cuando la política de contenedor tenga un período de eliminación menor `[Verificado MS Learn]`.
4. **Principio 4 — El período de eliminación más corto gana (*Shortest deletion period wins*):** Si únicamente compiten políticas de eliminación del mismo nivel implícito (por ejemplo, dos directivas de contenedor `Delete-only` en SharePoint sin etiquetas aplicadas), el elemento se elimina de forma permanente al cumplirse el vencimiento más corto `[Verificado MS Learn]`.

Alineación directa con los principios arquitectónicos de **Zero Trust** `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`:
- **Verify Explicitly:** Asignación determinística del ciclo de vida basada en inspección profunda de contenido (SITs, *Trainable Classifiers*, etiquetas de sensibilidad e identificadores `ComplianceAssetID`), eliminando decisiones discrecionales de usuarios finales `[Verificado MS Learn]`.
- **Use Least Privilege Access:** Segregación estricta de grupos de roles en Purview (separando diseño del File Plan, revisión de disposición y aprobación tripartita de *Priority Cleanup*), acotamiento geográfico por *Administrative Units* y fechas de expiración en asignaciones de roles `[Verificado MS Learn]`.
- **Assume Breach:** Minimización continua de datos ROT e historiales efímeros de prompts de IA para acotar drásticamente el volumen exfiltrable, blindaje contra sabotaje administrativo mediante **Preservation Lock** y preservación forense automática de 120 días acoplada a *Adaptive Protection* `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura In-Place por Carga de Trabajo (PHL, Recoverable Items, SubstrateHolds y Copilot/IA)

Microsoft Purview aplica retención y declaración de registros directamente en los contenedores nativos de cada servicio `[Verificado MS Learn]`:

- **SharePoint Online y OneDrive:** Las ediciones o eliminaciones sobre documentos retenidos se copian transparentemente a la **Preservation Hold Library (PHL)** oculta del sitio (computando contra la cuota de almacenamiento de SharePoint). Cuando se comparte un **Cloud Attachment** por enlace en Teams, Outlook, Viva Engage o Copilot bajo una directiva de auto-aplicación de adjuntos en la nube, Purview genera en la PHL una copia inmutable de la versión exacta vigente en el instante en que se compartió el vínculo `[Verificado MS Learn]`. Para migraciones documentales reguladas hacia SharePoint/OneDrive, dado que SharePoint actualiza metadatos al subir el archivo alterando su hash SHA tradicional, la cadena de custodia se valida comparando el hash **QuickXorHash** codificado en Base64 del archivo original contra la propiedad interna `vti_writevalidationtoken` `[Verificado MS Learn]`.
- **Exchange Online, Archive Mailboxes e Inactive Mailboxes:** Los elementos modificados o purgados se retienen en `Recoverable Items` (`Purges`, `Versions`, `DiscoveryHolds`). El buzón de archivo amplía capacidad inicial en 100 GB (110 GB bajo hold) y, al habilitar `AutoExpandingArchive`, aprovisiona almacenamiento auxiliar incremental hasta **3 TB** para licencias elegibles E5 / Purview Suite desde octubre de 2026 (creando subcarpetas automáticas `<Carpeta>_yyyy` con crecimiento máximo soportado de 1 GB/día; si un buzón con archivo auto-expandido se convierte luego en *Inactive Mailbox*, no puede restaurarse como buzón activo y sus datos deben extraerse mediante búsqueda de eDiscovery) `[Verificado MS Learn]`. Al eliminar la cuenta Entra ID de un usuario bajo retención, el buzón pasa a **Inactive Mailbox**; al remover el último hold, Microsoft 365 aplica automáticamente un **Delay Hold de 30 días** antes de la purga física `[Verificado MS Learn]`.
- **Ubicaciones Dedicadas de Microsoft Copilot y Aplicaciones de IA:** Anteriormente agrupadas junto con los chats de Teams, las nuevas políticas de retención separan tres grupos independientes de ubicaciones de IA `[Verificado MS Learn]`:
  1. **Microsoft Copilot experiences:** *Microsoft 365 Copilot* (incluyendo *Copilot Chat*), *Security Copilot*, *Copilot in Fabric* y *Copilot Studio*.
  2. **Enterprise AI apps:** *Entra-registered AI apps*, *ChatGPT Enterprise* y *Microsoft Foundry*.
  3. **Other AI apps:** *ChatGPT*, *Google Gemini*, *Microsoft Copilot (consumer)* y *DeepSeek*.
  Para todas las apps distintas de Microsoft 365 Copilot y Copilot Studio, es prerrequisito activar una **Collection Policy** con la opción de captura de contenido habilitada. Los prompts del usuario y las respuestas completas de la IA se almacenan en una carpeta oculta del buzón Exchange (`UserMailbox`); al vencer la retención o borrarse el historial en la app, un *timer job* (1 a 7 días) mueve los ítems a **SubstrateHolds**, donde permanecen mínimo 1 día antes del purgado definitivo en la siguiente corrida del *timer job* (1 a 7 días), permaneciendo buscables en eDiscovery hasta ese instante final `[Verificado MS Learn]`.

### 3.2 Matriz Oficial de Restricciones: Etiqueta Estándar vs. Record vs. Regulatory Record

La elección entre etiqueta estándar, **Record** (con soporte de bloqueo/desbloqueo en SharePoint y OneDrive mediante *Record Versioning*; en Exchange todo *Record* se comporta siempre como bloqueado) y **Regulatory Record** impone controles técnicos diferenciados `[Verificado MS Learn]`:

| Acción sobre el Elemento | Etiqueta de Retención Estándar | Record — Bloqueado (*Locked*) | Record — Desbloqueado (*Unlocked*, solo SPO/OD) | Regulatory Record (Habilitado con `Set-RegulatoryComplianceUI`) |
| --- | --- | --- | --- | --- |
| **Editar contenido del archivo** | Permitido | **Bloqueado** | Permitido (crea nueva versión; versión previa queda en PHL) | **Bloqueado** |
| **Editar propiedades / renombrar** | Permitido | Permitido por defecto (bloqueable en *Settings > Records Management > Retention Labels*) | Permitido | **Bloqueado** |
| **Eliminar elemento** | Permitido (bloqueable en SPO/OD por ajuste de tenant) | **Bloqueado** | **Bloqueado** | **Bloqueado** |
| **Mover dentro del mismo contenedor** | Permitido | Permitido | Permitido | Permitido |
| **Mover entre contenedores distintos** | Permitido | Permitido solo si nunca fue desbloqueado | **Bloqueado** | **Bloqueado** |
| **Cambiar o quitar la etiqueta** | Permitido | Permitido **solo a administrador del contenedor** | **Bloqueado** | **Bloqueado (ni siquiera Global Admin puede quitarla)** |
| **Auto-aplicación por política** | Soportado | Soportado | Soportado | **No soportado** (solo publicación/aplicación por política de etiquetas) |
| **Acortar período tras guardar etiqueta** | Permitido | Permitido | Permitido | **Bloqueado** (solo puede extenderse) |
| **Sobrescribir con Priority Cleanup** | Permitido (con 3 aprobaciones) | **Bloqueado** | **Bloqueado** | **Bloqueado** |

### 3.3 Componentes Operativos, Límites de Servicio y Transiciones 2026–2027

1. **Límites Estructurales del Tenant (`retention-limits`):** Máximo **1.000 etiquetas de retención** y **10.000 políticas totales** de cumplimiento por tenant (incluyendo hasta 1.800 de Exchange con un máximo recomendado de 25 y soportado de 50 por buzón; 13 políticas SharePoint/OneDrive para todos los sitios o 2.600 con ubicaciones específicas). En ámbitos estáticos con inclusiones/exclusiones explícitas rigen topes estrictos por política: **100 sitios SharePoint**, **100 cuentas OneDrive**, **1.000 buzones Exchange**, **500 grupos M365 / canales Teams** y **1.000 usuarios en Copilot e interacciones IA** —razón arquitectónica decisiva para migrar a **Adaptive Policy Scopes** en organizaciones medianas y grandes `[Verificado MS Learn]`.
2. **Incompatibilidad Actual entre Adaptive Scopes y Preservation Lock:** Microsoft Learn advierte explícitamente que los *Adaptive Policy Scopes* **no soportan Preservation Lock** (`Set-RetentionCompliancePolicy -RestrictiveRetention $true`). Además, para aplicar *Preservation Lock* sobre una política de publicación de etiquetas, dicha política debe contener **únicamente etiquetas que declaren Regulatory Records** `[Verificado MS Learn]`.
3. **Flujos y Límites de Multi-Stage Disposition (`disposition`):** Disponible exclusivamente en etiquetas de retención (nunca en políticas de contenedor); admite hasta **5 etapas secuenciales**, hasta **10 revisores o grupos de seguridad habilitados para correo** (*mail-enabled security groups*; los grupos Microsoft 365 no están soportados) por etapa y **200 revisores por tenant**. Tras el `Approve disposal` de la etapa final, el borrado permanente ocurre en un plazo de **hasta 15 días**; la auto-aprobación opcional admite entre **7 y 365 días** (14 días por defecto); soporta hasta **16.000.000 de ítems** pendientes/aprobados y conserva la **Proof of Disposal hasta por 7 años** `[Verificado MS Learn]`.
4. **Transiciones de APIs 2026–2027:** La automatización de eventos de retención retiró las antiguas APIs REST dedicadas y exige usar **Microsoft Graph Records Management APIs** (`/security/triggers/retentionEvents`, hasta 1.000.000 de eventos por tenant). Asimismo, el cmdlet `Search-UnifiedAuditLog` se retira el **15 de octubre de 2027**, siendo reemplazado por **Microsoft Graph `AuditLogQuery`**, en disponibilidad general desde octubre de 2026 `[Verificado MS Learn]`.

### 3.4 Integraciones Nativas con el Ecosistema de Seguridad Microsoft

- **Purview Information Protection (MIP) y Data Loss Prevention (DLP):** Las etiquetas de sensibilidad publicadas por MIP actúan como condición directa para auto-aplicar etiquetas de retención; DLP complementa la retención impidiendo la exfiltración en tránsito de registros activos `[Verificado MS Learn]`.
- **Purview Insider Risk Management (*Adaptive Protection*):** Cuando IRM eleva a un usuario al nivel *Elevated*, aprovisiona automáticamente una directiva de retención DLCM que preserva durante **120 días** todo archivo o correo borrado por dicho usuario `[Verificado MS Learn]`.
- **Purview DSPM for AI y Microsoft Agent 365:** DLCM reduce la exposición de conocimiento obsoleto indexado por Copilot y gobierna la retención y purga de interacciones de agentes desarrollados en Copilot Studio y Microsoft Foundry `[Verificado MS Learn]`.
- **Purview eDiscovery, Purview Audit y Microsoft Sentinel:** eDiscovery indexa y extrae evidencias desde `PHL`, `Recoverable Items`, `SubstrateHolds` e *Inactive Mailboxes*, mientras que Sentinel correlaciona eventos de alteración de políticas, `Set-RegulatoryComplianceUI` y `Priority Cleanup` en `OfficeActivity` `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

### 4.1 Segregación de Funciones Alineada a ISO 15489-1 y Control Interno

Conforme a **ISO 15489-1:2016** y las prácticas recomendadas por Microsoft Learn, ninguna identidad individual debe concentrar simultáneamente la facultad de diseñar etiquetas, aprobar disposiciones finales y ejecutar limpiezas prioritarias. En particular, **Global Administrator no posee por defecto el rol `Disposition Management`**, y para que el equipo central de Records Management supervise todas las disposiciones pendientes del tenant se debe habilitar un *mail-enabled security group* específico en `Settings > Solution settings > Records Management > Disposition` (o vía `Enable-ComplianceTagStorage` si se requiere reemplazarlo posteriormente) `[Verificado MS Learn]`.

### 4.2 Matriz RBAC Oficial de Microsoft Purview y Exchange Online con Estrategia PIM / JIT

| Rol / Role Group Oficial | Plano RBAC | Permisos Clave | Asignación PIM / JIT y Expiración | Responsabilidad Operativa y Segregación (SoD) | Estado |
| --- | --- | --- | --- | --- | --- |
| **Records Management** (Role Group nativo) | Microsoft Purview RBAC | `Retention Management`, `Disposition Management`, `View-Only Audit Logs`; administra File Plan, descriptores, eventos y etiquetas de registro. | Elegible JIT vía Entra ID PIM (máx. 4 h, MFA FIDO2/resistente a phishing y ticket de cambio aprobado) `[Decisión / Propuesta Editorial]`. | Reservado a Arquitectos / Líderes de Gobierno para cambios aprobados de diseño; no debe emplearse para aprobar disposiciones rutinarias propias `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Retention Manager** (en Role Group personalizado de Ingeniería DLCM) | Microsoft Purview RBAC | Creación y edición de políticas de retención, *Adaptive Scopes*, etiquetas estándar y auto-aplicación **sin** rol `Disposition Management`. | Elegible JIT (máx. 4 h) con justificación documentada `[Decisión / Propuesta Editorial]`. | Despliega políticas técnicas sobre cargas M365 e IA sin poder aprobar destrucción de registros en bandeja de disposición `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Disposition Reviewers** (Role Group personalizado con rol `Disposition Management`) | Microsoft Purview RBAC + Mail-Enabled Security Group | Acceso acotado a `Records Management > Disposition` para ejecutar *Approve disposal*, *Extend*, *Relabel* o *Add reviewers* sobre ítems asignados. | Asignación activa mediante grupos de seguridad habilitados para correo auditados trimestralmente en Entra Access Reviews `[Decisión / Propuesta Editorial]`. | Dueños de datos, Legal y Archivo que validan las etapas 1 a 5 de disposición sin permisos para alterar políticas ni etiquetas `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Content Explorer Content Viewer** | Microsoft Purview RBAC | Visualización del contenido real de correos y documentos en el mini-panel de vista previa durante revisiones de disposición o muestreo de clasificación. | Estricto JIT (máx. 2 h) con aprobación dual de Privacidad y Legal `[Decisión / Propuesta Editorial]`. | Excepcional: los revisores ordinarios deciden mediante metadatos (`Details` / `History`) sin abrir el cuerpo de documentos confidenciales `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Priority Cleanup Admin + Retention Admin + eDiscovery Admin** | Microsoft Purview RBAC | Creación, validación de alcance y **triple aprobación obligatoria** de políticas de *Priority Cleanup* sobre datos bajo retención o hold. | Activación JIT de emergencia ante derrame crítico; exige tres personas distintas en roles separados `[Verificado MS Learn]`. | Control anti-abuso que impide destruir selectivamente evidencia retenida sin autorización mancomunada de Retención, Legal y Seguridad `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **View-Only Retention Management y View-Only Record Management** | Microsoft Purview RBAC | Lectura integral del File Plan, políticas de retención, *Adaptive Scopes* y métricas sin capacidad de escritura. | Permanente para analistas GRC/SOC o asignación con **fecha de expiración automática** (disponible en Purview) para auditores externos `[Verificado MS Learn]`. | Auditoría continua, verificación de postura y extracción segura de indicadores de cumplimiento `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Exchange Administrator** | Microsoft Entra ID + Exchange Online RBAC | Configuración de `Archive Mailboxes`, `AutoExpandingArchive` (hasta 3 TB), `Start-ManagedFolderAssistant`, *Inactive Mailboxes* y remoción controlada de *Delay Holds*. | Elegible en Entra ID PIM (máx. 2 h JIT desde estación PAW) `[Decisión / Propuesta Editorial]`. | Administra la salud del almacenamiento subyacente en Exchange Online sin definir reglas normativas del File Plan `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

---

## 5. Cadencia Operativa Diaria

### D-01: Monitoreo de Estado de Distribución y Errores en Políticas de Retención y Etiquetas
- **Objetivo:** Detectar de inmediato fallos de distribución (`DistributionDetail` en error o estado pendiente prolongado superior a 7 días) en políticas estáticas, adaptables o de auto-aplicación antes de que generen brechas de preservación legal `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Policies > Retention policies` y `Label policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador DLCM (`View-Only Retention Management` para revisión; `Retention Manager` en PIM para remediación).
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `Defense Evasion (T1562 — Impair Defenses)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Acceder a las vistas de `Retention policies` y `Label policies` en el portal de Microsoft Purview y ordenar los registros por la columna `Status`.
  2. Identificar cualquier política cuyo estado sea distinto de `On (Success)`, prestando especial atención a errores de sincronización hacia SharePoint, Exchange o contenedores de Teams/Copilot.
  3. Conectarse a Security & Compliance PowerShell (`Connect-IPPSSession`) y ejecutar `Get-RetentionCompliancePolicy -DistributionDetail | Where-Object {$_.DistributionStatus -ne "Success"}` para aislar la ubicación exacta fallida.
  4. Corregir referencias huérfanas (por ejemplo, sitios eliminados en ámbitos estáticos o topes superados de 100 sitios / 1.000 buzones) y registrar el ticket operativo de remediación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación diaria de estado de distribución sin errores críticos abiertos y registro de remediación asociado `[Decisión / Propuesta Editorial]`.

### D-02: Auditoría Diaria de Cambios Administrativos Críticos en Retención, Registros y Preservation Lock
- **Objetivo:** Verificar que toda creación, modificación, desactivación o bloqueo de políticas de retención, etiquetas del File Plan o habilitación de `Set-RegulatoryComplianceUI` cuente con respaldo formal de gestión de cambios `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` (categoría *Retention policy and retention label activities*) y Microsoft Sentinel (`OfficeActivity`) `[Verificado MS Learn]`.
- **Rol Responsable:** Analista GRC / SOC L2 (`View-Only Audit Logs`).
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `Impact (T1485 — Data Destruction)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Consultar los eventos administrativos de las últimas 24 horas para `New-RetentionCompliancePolicy`, `Set-RetentionCompliancePolicy`, `Remove-RetentionCompliancePolicy`, `Set-ComplianceTag`, `Remove-ComplianceTag` y `Enabled regulatory record option for retention labels` `[Verificado MS Learn]`.
  2. Conciliar cada operación con el número de cambio aprobado por el Comité de Retención y la ventana de activación PIM del administrador ejecutor.
  3. Validar que ninguna política activa haya sufrido acortamiento no autorizado de `RetentionDuration` ni cambio de `Retain` a `Delete-only`.
  4. Ante cualquier cambio no autorizado, activar de inmediato el playbook de incidente crítico `AH-03`.
- **Evidencia Auditable:** Bitácora diaria de conciliación entre registros de Purview Audit / Graph `AuditLogQuery` y tickets ITSM aprobados `[Decisión / Propuesta Editorial]`.

### D-03: Seguimiento de Cola Activa de Revisiones de Disposición Próximas a Vencer o Auto-Aprobarse
- **Objetivo:** Prevenir que expedientes en `Pending dispositions` excedan el SLA interno de revisión o alcancen por inacción el umbral opcional de auto-aprobación (`Auto-approval timeout` de 7 a 365 días, 14 días por defecto) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > Disposition` `[Verificado MS Learn]`.
- **Rol Responsable:** Records Manager (integrante del *mail-enabled security group* administrativo habilitado en `Settings > Solution settings > Records Management > Disposition`) `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RR-02` / `N/A (Gobierno de Disposición Defensible)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar la tarjeta de resumen de `Pending dispositions` en `Records Management > Overview` e ingresar a la vista detallada por etiqueta en `Disposition`.
  2. Filtrar los elementos cuya fecha de expiración supere 10 días hábiles sin acción humana en su etapa actual (etapas 1 a 5) `[Decisión / Propuesta Editorial]`.
  3. Confirmar que los revisores asignados posean el rol `Disposition Management` (recordando que agregar un revisor adicional con `Add reviewers` no le concede permisos RBAC automáticamente) `[Verificado MS Learn]`.
  4. Escalar recordatorio directo al dueño de negocio o activar al revisor suplente si el titular está de licencia.
- **Evidencia Auditable:** Reporte CSV filtrado de `Pending disposition` con 0 elementos vencidos fuera de ventana operativa `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### D-04: Conciliación Diaria de Eventos de Negocio para Retención Basada en Eventos (Event-Driven Retention)
- **Objetivo:** Garantizar que cada evento transaccional originado en RR. HH., ERP o CLM se haya creado sin fallas en Purview con su respectivo `ComplianceAssetID` o consulta KeyQL acotada `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > Events` y telemetría de Microsoft Graph Records Management API `[Verificado MS Learn]`.
- **Rol Responsable:** Records Manager / Ingeniero de Integración GRC.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-01` / `N/A (Integridad de Ciclo de Vida por Eventos)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar el log de ejecución diaria del conector automatizado hacia `/security/triggers/retentionEvents` o cmdlet `New-ComplianceRetentionEvent` `[Verificado MS Learn]`.
  2. Verificar en `Records Management > Events` que ningún evento creado carezca de valor en `Asset ID` o `Keywords` —dado que crear un evento en blanco inicia por accidente el reloj de retención para **todos** los documentos etiquetados con ese `EventType` en todo el tenant `[Verificado MS Learn]`.
  3. Validar para eventos creados hace 7 días (plazo máximo de sincronización de eventos) que el conteo de archivos y correos asociados sea coherente con el expediente origen `[Verificado MS Learn]`.
  4. Si se agregaron documentos nuevos al expediente después de creado el evento original, emitir un nuevo evento con los mismos parámetros para cubrirlos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Salida diaria de `Get-ComplianceRetentionEvent` / Graph API verificada al 100% con `Asset ID` explícito `[Verificado MS Learn]`.

### D-05: Supervisión de Políticas y Ejecuciones Activas de Priority Cleanup
- **Objetivo:** Auditar en tiempo casi real cualquier solicitud, simulación o ejecución de *Priority Cleanup* asegurando que cumpla la regla de triple aprobación y no intente eludir controles de auditoría `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Priority cleanup` y `Solutions > Audit` `[Verificado MS Learn]`.
- **Rol Responsable:** Oficial de Cumplimiento / Analista SOC L2.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Exfiltration & Data Spillage Containment (TA0010)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar en `Priority cleanup` la existencia de directivas creadas, pendientes de aprobación o en ejecución sobre Exchange Online, SharePoint o OneDrive `[Verificado MS Learn]`.
  2. Rastrear en Purview Audit mediante el identificador único de la limpieza las tres aprobaciones obligatorias otorgadas por identidades separadas (*Retention Admin*, *eDiscovery Admin* y *Priority Cleanup Admin*) `[Verificado MS Learn]`.
  3. Verificar que los elementos pendientes de eliminación no correspondan a investigaciones legales activas no informadas.
  4. Archivar la evidencia de finalización una vez completada la purga acelerada.
- **Evidencia Auditable:** Extracto de auditoría por ID de *Priority Cleanup* respaldado por las tres aprobaciones nominales `[Verificado MS Learn]`.

### D-06: Verificación de Conversión a Inactive Mailboxes en Bajas Críticas de Personal (Offboarding)
- **Objetivo:** Evitar pérdida irreversible de correspondencia e interacciones de Teams/Copilot al eliminar cuentas de Microsoft Entra ID, validando la aplicación efectiva del hold de retención antes del borrado `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-Mailbox`, `Get-Mailbox -InactiveMailboxOnly`) y flujo IAM de bajas `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador Exchange Online / Analista IAM.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-11` / `Impact (T1485 — Data Destruction Prevention)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar en el pipeline diario de desvinculación que toda cuenta por eliminar posea `InPlaceHolds` o `ComplianceTagHoldApplied` activo derivado de una política `Retain` o `Retain and then delete` (recordando que políticas `Delete-only` o MRM de Exchange no convierten el buzón en inactivo) `[Verificado MS Learn]`.
  2. Confirmar que ningún operador IAM modifique el `UserPrincipalName` ni elimine el `PrimarySmtpAddress` antes de borrar la cuenta, pues ello impide excluir el buzón inactivo de políticas estáticas en el futuro `[Verificado MS Learn]`.
  3. Comprobar la aparición del buzón en `Get-Mailbox -InactiveMailboxOnly` tras la baja de la cuenta (conservando la ventana de 30 días de recuperación de cuenta *soft-deleted* si fuera una baja errónea) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Log diario automatizado de pre-validación de holds en bajas y listado actualizado de `Inactive Mailboxes` `[Verificado MS Learn]`.

### D-07: Monitoreo de Cuotas Críticas en Recoverable Items y Auto-Expanding Archives (3 TB)
- **Objetivo:** Prevenir interrupción de servicio en buzones bajo retención cuya carpeta `Recoverable Items` se acerque al límite y garantizar la activación oportuna del archivo de expansión automática hasta 3 TB `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://admin.exchange.microsoft.com > Recipients > Mailboxes` y Exchange Online PowerShell `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador Exchange Online.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-11` / `Impact (Availability & Compliance Continuity)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Identificar buzones activos cuyo `TotalDeletedItemSize` supere el 85% de `RecoverableItemsQuota` (100 GB base; 110 GB al habilitar archivo bajo hold) `[Verificado MS Learn]`.
  2. Habilitar `Enable-Mailbox -Archive` y `Enable-Mailbox -AutoExpandingArchive` antes de saturar la cuota primaria (considerando que el aprovisionamiento de áreas auxiliares puede tardar hasta 30 días y soporta un crecimiento máximo de 1 GB/día) `[Verificado MS Learn]`.
  3. Confirmar en buzones de gran volumen que el usuario cuente con licencia E5 / Microsoft Purview Suite y el plan *Records Management* activo para beneficiarse del nuevo techo de **3 TB** vigente desde octubre de 2026 `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte diario automatizado de salud de `Recoverable Items` y estado de `AutoExpandingArchiveEnabled` `[Verificado MS Learn]`.

### D-08: Verificación de Políticas de Retención y Collection Policies para Copilot y Aplicaciones de IA
- **Objetivo:** Asegurar la captura y retención/purga continua de prompts y respuestas de Microsoft 365 Copilot, Copilot Studio, agentes empresariales y apps GenAI externas conforme a la política de gobierno de IA `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Policies > Retention policies` y `Settings > Collection policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador DLCM / Especialista en Gobierno de IA.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RM-03` / `Collection & AI Data Exposure Mitigation` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar que las políticas dedicadas para `Microsoft Copilot experiences`, `Enterprise AI apps` y `Other AI apps` se encuentren habilitadas y en estado `Success` `[Verificado MS Learn]`.
  2. Comprobar en `Settings > Collection policies` que las políticas de ingesta con captura de contenido activa sigan operativas para aplicaciones distintas de M365 Copilot y Copilot Studio `[Verificado MS Learn]`.
  3. Validar que la suscripción Azure vinculada para medidores Pay-As-You-Go de IA no registre errores de cuota o facturación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Estado activo verificado de políticas de retención IA y *Collection Policies* asociadas `[Verificado MS Learn]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Muestreo de Precisión en Políticas de Auto-Aplicación de Etiquetas y Cloud Attachments
- **Objetivo:** Validar mediante muestreo dirigido la exactitud de etiquetas aplicadas automáticamente por SITs, KeyQL, etiquetas de sensibilidad, *Trainable Classifiers* y vínculos de *Cloud Attachments* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Explorers > Content explorer` y `Activity explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** Records Manager / Ingeniero DLCM.
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.AM-07` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Revisar en `Activity explorer` las tendencias semanales de aplicación automática de etiquetas por sitio SharePoint, OneDrive y Exchange.
  2. Evaluar resultados de políticas en modo de simulación antes de promoverlas a producción (esperando hasta 7 días tras ajustes de configuración) `[Verificado MS Learn]`.
  3. Refinar consultas KeyQL o umbrales de confianza de SITs cuando se detecten falsos positivos sobre borradores transitorios, recordando que las políticas de auto-aplicación nunca etiquetan carpetas ni conjuntos de documentos ni soportan *Regulatory Records* `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro semanal de muestreo de calidad de auto-etiquetado (>= 92% de precisión objetivo) `[Decisión / Propuesta Editorial]`.

### S-02: Auditoría de Membresía Dinámica e Higiene de Atributos en Adaptive Policy Scopes
- **Objetivo:** Asegurar que los filtros dinámicos de usuarios Entra ID, sitios SharePoint y grupos Microsoft 365 incluyan sin omisiones a todas las unidades reguladas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and scopes > Adaptive scopes` `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador DLCM.
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.AM-07` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar `Scope details` en cada ámbito adaptable activo (usuarios activos por país/departamento, sitios SharePoint por `RefinableString`, e *Inactive Mailboxes*).
  2. Auditar cuentas o sitios creados recientemente que presenten atributos vacíos (`Department`, `Country`, propiedad administrada de sitio) y por ende escapen de las consultas OPATH/KQL.
  3. Emitir solicitud semanal de normalización de metadatos a los equipos de Entra ID y SharePoint Online.
- **Evidencia Auditable:** Exportación semanal de membresía de *Adaptive Scopes* y tickets de corrección de atributos `[Verificado MS Learn]`.

### S-03: Conducción de Mesas Semanales de Revisión de Disposición Multi-Etapa (Etapas 1 a 5)
- **Objetivo:** Procesar de manera oportuna y documentada los elementos vencidos sujetos a revisión humana antes de su eliminación definitiva `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > Disposition` `[Verificado MS Learn]`.
- **Rol Responsable:** `Disposition Reviewers` + Records Manager.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OC-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Tras el correo semanal de recordatorio enviado por Purview, cada grupo revisor inspecciona las pestañas `Details` e `History` en el mini-panel de `Pending dispositions` `[Verificado MS Learn]`.
  2. Ejecutar la decisión documentada: `Approve disposal` (avanza a la siguiente etapa o, en la etapa final, marca el ítem para eliminación permanente dentro de 15 días), `Extend` (pospone y reiniciará desde la etapa 1 al vencer la prórroga) o `Relabel` `[Verificado MS Learn]`.
  3. Escalar de inmediato a Legal cualquier ítem que deba preservarse por disputa contractual o regulatoria emergente.
- **Evidencia Auditable:** Trazas de auditoría semanales en el grupo *Disposition review activities* con comentarios de los aprobadores `[Verificado MS Learn]`.

### S-04: Control de Consumo en Preservation Hold Libraries y Evaluación de Microsoft 365 Archive
- **Objetivo:** Evitar sobrecostos por agotamiento de cuota en SharePoint Online derivado de `Preservation Hold Library` (PHL) y optimizar el ciclo hacia almacenamiento frío `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** SharePoint Admin Center (`Active sites`) y Azure Cost Management `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador SharePoint + FinOps + DLCM Lead.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RM-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Analizar los sitios con mayor tasa de crecimiento semanal en PHL identificando cargas no humanas (logs, backups locales sincronizados en OneDrive, renderizados CAD/video).
  2. Proponer el paso a **Microsoft 365 Archive** de sitios de proyectos concluidos que aún deban retenerse por años, preservando intactas sus etiquetas y políticas de retención e indexación para eDiscovery `[Verificado MS Learn]`.
  3. Validar el consumo semanal Pay-As-You-Go contra el presupuesto mensual aprobado.
- **Evidencia Auditable:** Informe semanal de top sitios por consumo PHL y estado de archivado en frío `[Decisión / Propuesta Editorial]`.

### S-05: Detección de Intentos Anómalos de Borrado o Remoción de Etiquetas en Records
- **Objetivo:** Identificar posibles acciones de ocultamiento (*Clean-up*) por usuarios maliciosos o errores de administración en contenedores sobre elementos declarados como *Record* `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Audit` y `Activity explorer` `[Verificado MS Learn]`.
- **Rol Responsable:** Analista SOC L2 / Records Manager.
- **Mapeo NIST CSF 2.0 / MITRE:** `DE.CM-09` / `Defense Evasion & Impact (T1070 / T1485)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Filtrar en `Activity explorer` y Purview Audit remociones o cambios de etiquetas de registro efectuados por administradores de sitio/contenedor (único perfil capaz de retirar una etiqueta *Record* bloqueada estándar, nunca un *Regulatory Record*) `[Verificado MS Learn]`.
  2. Comprobar que los ajustes del tenant en `Settings > Solution settings > Records Management > Retention Labels` (*Allow editing of record properties* y *Deletion of items*) no hayan sido alterados `[Verificado MS Learn]`.
  3. Cruzar usuarios con alto volumen de intentos de eliminación bloqueados contra alertas activas de **Purview Insider Risk Management**.
- **Evidencia Auditable:** Reporte semanal de auditoría sobre modificaciones de etiquetas de registro y validación de configuración del tenant `[Verificado MS Learn]`.

### S-06: Verificación de Gobernanza sobre Nuevos Contenedores M365 y Agentes Copilot Studio
- **Objetivo:** Confirmar que todo sitio SharePoint, equipo Teams o agente de Copilot Studio / Foundry dado de alta en la semana quede cubierto por políticas de ciclo de vida `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** SharePoint Admin Center, Power Platform Admin Center y `purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** Ingeniero de Gobierno de Datos.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-01` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Extraer inventario semanal de nuevos sitios, grupos M365 y agentes IA publicados en producción.
  2. Validar que las bibliotecas documentales de procesos regulados reciban su *Default retention label* correspondiente (evitando aplicarla por error en bibliotecas efímeras de trabajo) `[Verificado MS Learn]`.
  3. Verificar que los nuevos agentes empresariales estén alcanzados por la política de retención de `Microsoft Copilot experiences` o `Enterprise AI apps` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Matriz semanal de alta de contenedores y agentes verificada al 100% de cobertura base `[Decisión / Propuesta Editorial]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Exportación, Conciliación y Archivo Firmado de Proof of Disposal
- **Objetivo:** Consolidar evidencia probatoria inalterable de todos los registros destruidos en el mes (por revisión manual o eliminación automática de *Records*), extendiendo la custodia más allá del límite nativo de 7 años `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > Disposition > Disposed items` y Graph `AuditLogQuery` `[Verificado MS Learn]`.
- **Rol Responsable:** Records Manager.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OC-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Seleccionar cada etiqueta de registro en `Records Management > Disposition` y exportar a CSV la vista `Disposed items` acotada al mes vencido (incluyendo tanto ítems revisados como `Records Disposed` sin revisión manual) `[Verificado MS Learn]`.
  2. Extraer vía Microsoft Graph `AuditLogQuery` los registros `Approved disposal` y `Deleted file marked as a record` del mismo período para corroborar integridad cruzada `[Verificado MS Learn]`.
  3. Generar hash SHA-256 del paquete documental y almacenarlo en el repositorio regulado de Auditoría Interna `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Certificados mensuales CSV de `Proof of Disposal` + hashes SHA-256 archivados (12 cierres anuales) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### M-02: Auditoría y Reducción de Deuda de Retención en Inactive Mailboxes y OneDrive
- **Objetivo:** Eliminar la retención perpetua no intencional sobre cuentas de exempleados migrando hacia ámbitos adaptables con expiración definida `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Get-Mailbox -InactiveMailboxOnly`) y `purview.microsoft.com > Adaptive scopes` `[Verificado MS Learn]`.
- **Rol Responsable:** Oficial de Cumplimiento + Administrador Exchange/SharePoint.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.RM-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar el script mensual de inventario de *Inactive Mailboxes* identificando fecha de baja (`WhenSoftDeleted`), holds aplicados y presencia de `DelayHoldApplied` `[Verificado MS Learn]`.
  2. Detectar buzones retenidos exclusivamente por políticas estáticas antiguas `All mailboxes` de *solo retener* o por *eDiscovery case holds* de litigios concluidos `[Verificado MS Learn]`.
  3. Liberar holds cerrados con autorización escrita de Legal y aplicar **Adaptive Policy Scopes** dedicados a buzones inactivos con acción `Retain and then delete` conforme al plazo legal exacto `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de deuda de retención con detalle de buzones inactivos depurados y ahorros de superficie `[Decisión / Propuesta Editorial]`.

### M-03: Medición de Minimización de Datos ROT y Reducción de Superficie para Copilot e IA
- **Objetivo:** Cuantificar la eliminación efectiva de datos redundantes, obsoletos y triviales en sitios expuestos a Microsoft 365 Copilot y en historiales de chats/prompts de IA `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > DSPM for AI` y `Data Lifecycle Management` `[Verificado MS Learn]`.
- **Rol Responsable:** Data Governance Lead + Arquitecto de Seguridad IA.
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.RA-05` / `Collection (TA0009 — AI Oversharing Reduction)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Cruzar los sitios identificados con riesgo de sobreexposición en *DSPM for AI* frente a la aplicación efectiva de políticas de purga de contenido obsoleto no catalogado como registro.
  2. Comprobar mediante búsqueda muestral de eDiscovery que las interacciones vencidas de `Microsoft Copilot experiences`, `Enterprise AI apps` y `Other AI apps` hayan completado su salida de `SubstrateHolds` tras la ventana de procesamiento de *timer jobs* `[Verificado MS Learn]`.
  3. Reportar métricas consolidadas de higiene pre-IA al comité de seguridad y adopción de IA `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Dashboard mensual de reducción de ROT y validación muestral de purga en `SubstrateHolds` `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### M-04: Conciliación de Registros Basados en Eventos sin Asset ID o con Evento Omitido
- **Objetivo:** Evitar que registros vinculados a eventos queden retenidos para siempre por omisión de `ComplianceAssetID` o falta de disparo del evento desde sistemas de negocio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Content search` y `Records Management > Events` `[Verificado MS Learn]`.
- **Rol Responsable:** Records Manager + Dueños de Proceso (RR. HH., Legal, Compras).
- **Mapeo NIST CSF 2.0 / MITRE:** `ID.AM-07` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Buscar en `Content search` documentos etiquetados con etiquetas de tipo `EventAgeInDays` cuya propiedad `ComplianceAssetID` (o propiedad administrada equivalente) esté vacía `[Verificado MS Learn]`.
  2. Conciliar todas las bajas laborales y contratos finalizados del mes contra los registros creados en `Records Management > Events`.
  3. Completar metadatos faltantes y disparar eventos omitidos mediante Microsoft Graph Records Management API `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta mensual de conciliación HRIS/CLM vs. Purview Events sin discrepancias abiertas `[Decisión / Propuesta Editorial]`.

### M-05: Revisión Mensual de Privilegios RBAC, Tope de Revisores y Costos Pay-As-You-Go
- **Objetivo:** Auditar asignaciones privilegiadas en Purview/PIM, controlar el límite máximo de 200 revisores por tenant y revisar facturación Pay-As-You-Go `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Settings > Roles and groups`, Entra PIM y Azure Cost Management `[Verificado MS Learn]`.
- **Rol Responsable:** Analista GRC / FinOps.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.AA-05` / `Privilege Escalation Prevention` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Verificar membresías de `Records Management`, `Retention Management`, `Disposition Management`, `Content Explorer Content Viewer` y roles de `Priority Cleanup`, confirmando expiración automática de accesos temporales `[Verificado MS Learn]`.
  2. Auditar el conteo acumulado de revisores/grupos de disposición frente al límite de **200 por tenant** (consolidando usuarios individuales en *mail-enabled security groups*) `[Verificado MS Learn]`.
  3. Conciliar costos Pay-As-You-Go de retención de apps IA no-M365 y *Microsoft 365 Archive*.
- **Evidencia Auditable:** Reporte mensual de gobierno RBAC/PIM y conciliación FinOps de Purview `[Decisión / Propuesta Editorial]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Revisión Normativa y Racionalización del File Plan
- **Objetivo:** Actualizar el *File Plan* frente a reformas legales o de privacidad regionales manteniendo una taxonomía simplificada (*big-bucket*) fácil de operar y auditar `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > File plan > Export` y `Compliance Manager` `[Verificado MS Learn]`.
- **Rol Responsable:** Comité de Retención (Records Manager, Legal, DPO, CISO).
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OC-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Exportar el `File plan` completo a CSV revisando cada etiqueta, estado, descriptores regulatorios y flujos de disposición `[Verificado MS Learn]`.
  2. Contrastar plazos frente a actualizaciones normativas en *Compliance Manager* y legislación aplicable (ej. Ley 21.719 Chile, nueva LFPDPPP México, Ley 594 Colombia, GDPR, SEC) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Depurar etiquetas inactivas nunca aplicadas y consolidar categorías superpuestas sin superar un catálogo manejable (< 200 tipos de registro recomendados sobre el límite técnico de 1.000) `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** CSV exportado del File Plan versionado y acta de aprobación trimestral del Comité de Retención `[Decisión / Propuesta Editorial]`.

### T-02 (Trimestral): Validación Empírica de los 4 Principios de Precedencia y Cadena de Custodia
- **Objetivo:** Comprobar mediante pruebas controladas el comportamiento exacto de conflictos entre políticas, etiquetas, *eDiscovery Holds*, *Cloud Attachments* y validación de migraciones `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Data Lifecycle Management / Records Management / eDiscovery` `[Verificado MS Learn]`.
- **Rol Responsable:** Arquitecto Purview + Especialista eDiscovery.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-11` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Ejecutar matriz de pruebas sobre ítems sintéticos verificando el flujo oficial de los 4 principios de precedencia en SharePoint, Exchange, Teams y Microsoft 365 Copilot `[Verificado MS Learn]`.
  2. Confirmar que un *eDiscovery Hold* prevalece sobre cualquier acción de eliminación y que *Priority Cleanup* falla de forma segura si se intenta aplicar sobre un *Record* o *Regulatory Record* `[Verificado MS Learn]`.
  3. En proyectos activos de migración hacia SharePoint, auditar la coincidencia del hash QuickXor Base64 contra `vti_writevalidationtoken` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Dossier trimestral de pruebas de precedencia e integridad criptográfica de registros migrados `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Auditoría de Preservation Lock, Regulatory Records y Capacidad del Tenant
- **Objetivo:** Auditar todas las políticas con bloqueo regulatorio irreversible, etiquetas de *Regulatory Record* y márgenes frente a límites de servicio `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Security & Compliance PowerShell (`Get-RetentionCompliancePolicy`, `Get-ComplianceTag`) `[Verificado MS Learn]`.
- **Rol Responsable:** Auditoría Interna + CISO + Oficial de Cumplimiento.
- **Mapeo NIST CSF 2.0 / MITRE:** `PR.DS-01` / `Impact (T1485)` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Auditar cada directiva con `RestrictiveRetention: True` validando su justificación regulatoria vigente y recordando que los *Adaptive Scopes* no admiten *Preservation Lock* `[Verificado MS Learn]`.
  2. Verificar todas las etiquetas con `Regulatory = True` y confirmar que `Set-RegulatoryComplianceUI` permanezca en `$false` fuera de ventanas autorizadas de alta de etiquetas `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Evaluar márgenes frente a topes del tenant: 10.000 políticas totales, 25 políticas recomendadas por buzón y 16 millones de elementos en estados de disposición `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe semestral de auditoría de inmutabilidad y capacidad técnica firmado por Auditoría Interna `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Recertificación Ejecutiva del Programa de Registros (ISO 15489-1) y Simulacro Tabletop
- **Objetivo:** Recertificar anualmente la gobernanza ejecutiva, la Tabla de Retención Documental (TRD), la matriz RACI y la capacidad de respuesta coordinada ante crisis de datos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com` (Records Management, Audit, eDiscovery, Priority Cleanup) `[Verificado MS Learn]`.
- **Rol Responsable:** CISO, General Counsel, DPO y Comité Ejecutivo de Riesgos.
- **Mapeo NIST CSF 2.0 / MITRE:** `RC.IM-01` / `Impact & Exfiltration Readiness` `[Decisión / Propuesta Editorial]`.
- **Procedimiento Paso a Paso:**
  1. Recertificar formalmente la TRD corporativa, la matriz RACI de separación de funciones y los plazos de conservación de interacciones de IA generativa y agentes `[Decisión / Propuesta Editorial]`.
  2. Ejecutar ejercicio *tabletop* anual simulando un derrame masivo de información clasificada bajo retención (ejecución de *Priority Cleanup* con triple aprobación) y un intento de borrado malicioso de políticas por cuenta privilegiada comprometida `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]`.
  3. Consolidar el libro anual de evidencias NIST CSF 2.0 e ISO 15489-1 con los 12 paquetes mensuales de *Proof of Disposal* `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Acta anual del Directorio/Comité de Riesgos, TRD recertificada e informe de lecciones aprendidas del simulacro `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Ejecución de Emergencia de Priority Cleanup ante Derrame de Información Clasificada (Data Spillage)
- **Disparador:** Distribución accidental o maliciosa de credenciales críticas, propiedad intelectual restringida o PII masiva hacia buzones o sitios protegidos por políticas de retención o holds que impiden su purga normal `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Data Lifecycle Management > Priority cleanup` `[Verificado MS Learn]`.
- **Rol Responsable:** Tríada mancomunada: `Retention Admin` + `eDiscovery Admin` + `Priority Cleanup Admin` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Exfiltration & Data Exposure Containment (TA0010)` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Aislar inmediatamente la difusión activa revocando vínculos compartidos o bloqueando el mensaje en Defender for Office 365 / Purview DLP, y construir una consulta KQL exacta que identifique únicamente los archivos o mensajes derramados.
  2. Crear la política de **Priority Cleanup** sobre las ubicaciones afectadas ejecutando obligatoriamente la fase previa de simulación e inspección de coincidencias `[Verificado MS Learn]`.
  3. Comprobar si algún ítem afectado posee etiqueta de **Record** o **Regulatory Record**: por diseño, *Priority Cleanup* **no puede eliminar registros** (si fuese un *Record* estándar no regulatorio y Legal ordena su purga, un administrador del contenedor debe remover primero la etiqueta antes de relanzar la limpieza) `[Verificado MS Learn]`.
  4. Someter la ejecución a las **tres aprobaciones independientes** requeridas desde cuentas distintas con roles segregados `[Verificado MS Learn]`.
  5. Auditar por el ID de la limpieza en Purview Audit / Graph `AuditLogQuery` hasta confirmar la eliminación permanente de todos los ejemplares elegibles `[Verificado MS Learn]`.
- **Evidencia Auditable:** Expediente completo de *Priority Cleanup* con simulación, 3 aprobaciones registradas y log final de purga por ID `[Verificado MS Learn]`.

### AH-02: Suspensión Inmediata de Disposición y Activación de Hold Legal ante Litigio o Investigación Forense
- **Disparador:** Notificación oficial de litigio inminente, auditoría regulatoria compulsiva o escalamiento de caso grave desde Purview Insider Risk Management / SOC `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > eDiscovery > Cases` y `Records Management > Disposition` `[Verificado MS Learn]`.
- **Rol Responsable:** `eDiscovery Manager` (Legal) + `Records Manager` `[Verificado MS Learn]`.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Forensic Evidence Preservation` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Legal abre el caso en Purview eDiscovery y coloca de inmediato un **eDiscovery Hold** sobre los buzones (abarcando `Recoverable Items` y `SubstrateHolds` de Teams/Copilot), sitios SharePoint y cuentas OneDrive de los custodios `[Verificado MS Learn]`.
  2. Por precedencia del *eDiscovery Hold* y el **Principio 1 de retención**, el motor suspende automáticamente toda eliminación permanente en segundo plano `[Verificado MS Learn]`.
  3. El *Records Manager* verifica en `Records Management > Disposition` si existen documentos de dichos custodios en `Pending dispositions` y aplica la acción `Extend` dejando constancia trazable de suspensión por instrucción legal `[Verificado MS Learn]`.
  4. Verificar por PowerShell (`Get-Mailbox | Select InPlaceHolds`) la aplicación efectiva del hold antes de permitir cualquier baja de usuario o reasignación de activos `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de activación de `eDiscovery Hold` en `Success` y bitácora de extensión en `Disposition` `[Verificado MS Learn]`.

### AH-03: Contención y Restauración ante Modificación o Desactivación Maliciosa de Políticas de Retención
- **Disparador:** Detección en SIEM/Audit de desactivación, borrado o reducción de plazos no autorizada sobre políticas de retención o etiquetas de registro por una cuenta administrativa comprometida o maliciosa `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://security.microsoft.com`, `https://entra.microsoft.com` y `https://purview.microsoft.com` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2/L3 + Ingeniero Senior Purview.
- **Mapeo NIST CSF 2.0 / MITRE:** `RS.MI-01` / `Defense Evasion & Impact (T1562 / T1485)` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Contener la identidad atacante en Microsoft Entra ID revocando tokens de sesión continuos (CAE), deshabilitando el usuario y bloqueando elevaciones PIM.
  2. Reaplicar de inmediato la configuración íntegra de la política desde el repositorio versionado del File Plan / backup JSON (aprovechando que los *timer jobs* de 1 a 7 días y el *Delay Hold* automático de 30 días en Exchange impiden la purga física instantánea tras quitar un hold) `[Verificado MS Learn]`.
  3. Evaluar con Legal y CISO la activación irreversible de **Preservation Lock** (`Set-RetentionCompliancePolicy -RestrictiveRetention $true`) sobre las directivas estáticas regulatorias críticas para blindarlas incluso frente a un *Global Administrator* `[Verificado MS Learn]`.
  4. Auditar en `Content Explorer` y `Audit` que ningún registro haya perdido su inmutabilidad durante la ventana de exposición.
- **Evidencia Auditable:** Incidente cerrado en Defender XDR/Sentinel, salida PowerShell de política restaurada y estado `RestrictiveRetention: True` si se aplicó bloqueo `[Verificado MS Learn]`.

### AH-04: Incorporación Masiva de Tablas de Retención por Cambio Regulatorio o Fusión/Adquisición (M&A)
- **Disparador:** Adquisición corporativa con migración documental a Microsoft 365 o promulgación de nueva ley sectorial/privacidad que obliga a desplegar decenas de series nuevas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://purview.microsoft.com > Solutions > Records Management > File plan > Import` `[Verificado MS Learn]`.
- **Rol Responsable:** Arquitecto de Gobierno de Datos + Records Manager + Legal.
- **Mapeo NIST CSF 2.0 / MITRE:** `GV.OC-03` / `N/A` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. Homologar la tabla documental entrante con el File Plan corporativo evitando exceder el límite de **1.000 etiquetas por tenant** `[Verificado MS Learn]`.
  2. Crear previamente en `Records Management > Events > Manage event types` cualquier `EventType` nuevo requerido y, solo si existen series que exijan *Regulatory Records*, ejecutar `Set-RegulatoryComplianceUI -Enabled $true` antes de validar el CSV `[Verificado MS Learn]`.
  3. Importar la plantilla CSV oficial (`LabelName` <= 64 caracteres, `IsRecordLabel`, `Regulatory`, `RetentionAction`, `RetentionDuration`, `RetentionType`, `ReviewerEmail`, descriptores legales) y añadir luego en el portal web las etapas 2 a 5 de revisión multi-etapa `[Verificado MS Learn]`.
  4. Validar la integridad inalterada de los expedientes migrados a SharePoint comparando el QuickXorHash Base64 de origen con la propiedad `vti_writevalidationtoken` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Archivo CSV importado sin errores, configuración multi-etapa completada y certificado de validación `vti_writevalidationtoken` `[Verificado MS Learn]`.

### AH-05: Desbloqueo Operativo de Emergencia por Saturación de Recoverable Items o Preservation Hold Library
- **Disparador:** Interrupción inminente de correo o bloqueo de escritura en sitio SharePoint crítico por alcanzar el 100% de cuota bajo retención `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** Exchange Online PowerShell (`Enable-Mailbox`, `Start-ManagedFolderAssistant`) y SharePoint Admin Center `[Verificado MS Learn]`.
- **Rol Responsable:** Administrador Exchange / SharePoint + Administrador DLCM.
- **Mapeo NIST CSF 2.0 / MITRE:** `RC.RP-03` / `Availability Preservation` `[Decisión / Propuesta Editorial]`.
- **Secuencia Operativa Numerada:**
  1. En Exchange Online: verificar licenciamiento E5 / Purview Suite con plan *Records Management* activo (capacidad hasta **3 TB**), activar archivo y `AutoExpandingArchive`, e invocar `Start-ManagedFolderAssistant -Identity <UPN> -HoldCleanup` `[Verificado MS Learn]`.
  2. Detener cualquier conector o flujo automatizado que inyecte más de **1 GB/día** al buzón afectado `[Verificado MS Learn]`.
  3. En SharePoint Online: ampliar cuota inmediata del sitio para restablecer operación, mover sitios históricos inactivos a *Microsoft 365 Archive* y segregar cargas transaccionales automatizadas hacia contenedores con política de retención ajustada y aprobada por el Comité de Retención `[Verificado MS Learn]`.
- **Evidencia Auditable:** Métricas de cuota normalizadas post-intervención y acta de ajuste arquitectónico sin pérdida de cumplimiento `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas PowerShell, Microsoft Graph y KQL Operativas

#### Consulta 1: Auditoría de Políticas de Retención, Estado de Distribución y Preservation Lock (Security & Compliance PowerShell) `[Verificado MS Learn]`
```powershell
# Requiere ExchangeOnlineManagement y rol View-Only Retention Management o superior
Connect-IPPSSession

Get-RetentionCompliancePolicy -DistributionDetail |
    Select-Object Name, Enabled, Mode, Type, RestrictiveRetention, DistributionStatus,
                  @{N="AdaptiveScopes";E={$_.AdaptiveScopeLocation -join ";"}},
                  WhenChangedUTC |
    Sort-Object RestrictiveRetention -Descending, Name |
    Format-Table -AutoSize
```

#### Consulta 2: Extracción Integral del File Plan, Records, Regulatory Records y Eventos (Security & Compliance PowerShell) `[Verificado MS Learn]`
```powershell
# Exporta el catálogo completo de etiquetas de retención y sus banderas de inmutabilidad
Connect-IPPSSession

Get-ComplianceTag |
    Select-Object Name, Workload, RetentionAction, RetentionDuration, RetentionType,
                  IsRecordLabel, Regulatory, IsRecordUnlockedAsDefault,
                  EventType, ReviewerEmail, AutoApprovalPeriod, WhenCreatedUTC |
    Export-Csv -Path ".\Evidencia_FilePlan_Purview.csv" -NoTypeInformation -Encoding UTF8
```

#### Consulta 3: Cuantificación de Deuda de Retención e Inspección de Holds en Inactive Mailboxes (Exchange Online PowerShell) `[Verificado MS Learn]`
```powershell
# Identifica buzones inactivos, fecha de baja, Delay Holds y holds estáticos o de etiquetas
Connect-ExchangeOnline

Get-Mailbox -InactiveMailboxOnly -ResultSize Unlimited |
    Select-Object DisplayName, UserPrincipalName, PrimarySmtpAddress, WhenSoftDeleted,
                  LitigationHoldEnabled, DelayHoldApplied, DelayReleaseHoldApplied,
                  ComplianceTagHoldApplied, AutoExpandingArchiveEnabled,
                  @{N="InPlaceHolds";E={$_.InPlaceHolds -join ";"}} |
    Export-Csv -Path ".\Auditoria_InactiveMailboxes_RetentionDebt.csv" -NoTypeInformation -Encoding UTF8
```

#### Consulta 4: Monitoreo Preventivo de Recoverable Items y Expansión Automática hasta 3 TB (Exchange Online PowerShell) `[Verificado MS Learn]`
```powershell
# Evalúa saturación de Recoverable Items y activación de AutoExpandingArchive en buzones activos
Connect-ExchangeOnline

Get-Mailbox -ResultSize Unlimited -Filter {RecipientTypeDetails -eq "UserMailbox"} |
    ForEach-Object {
        $stats = Get-MailboxStatistics -Identity $_.UserPrincipalName -ErrorAction SilentlyContinue
        [PSCustomObject]@{
            UPN                     = $_.UserPrincipalName
            ArchiveStatus           = $_.ArchiveStatus
            AutoExpandingArchive    = $_.AutoExpandingArchiveEnabled
            TotalDeletedItemSize    = $stats.TotalDeletedItemSize
            RecoverableItemsWarning = $_.RecoverableItemsWarningQuota
            RecoverableItemsQuota   = $_.RecoverableItemsQuota
        }
    } | Export-Csv -Path ".\Salud_RecoverableItems_AutoExpanding.csv" -NoTypeInformation -Encoding UTF8
```

#### Consulta 5: Disparo Automatizado de Evento de Retención vía Microsoft Graph Records Management API (PowerShell Graph SDK) `[Verificado MS Learn]`
```powershell
# Sustituye las antiguas APIs REST retiradas; dispara retención acotada por ComplianceAssetID
Connect-MgGraph -Scopes "RecordsManagement.ReadWrite.All"

$params = @{
    displayName          = "Fin Contrato Proveedor CRIT-2026-089"
    description          = "Vencimiento contractual validado desde sistema CLM"
    eventQuery           = @{
        "@odata.type" = "#microsoft.graph.security.retentionEventQuery"
        queryType     = "files"
        query         = "ComplianceAssetID:CRIT-2026-089"
    }
    eventTriggerDateTime = "2026-11-11T00:00:00Z"
    retentionEventType   = @{
        "@odata.id"   = "https://graph.microsoft.com/v1.0/security/triggers/retentionEventTypes/<EVENT_TYPE_GUID>"
    }
}
New-MgSecurityTriggerRetentionEvent -BodyParameter $params
```

#### Consulta 6: Auditoría Mensual de Disposición y Cambios de Políticas con Microsoft Graph AuditLogQuery (Sustituto GA de `Search-UnifiedAuditLog`) `[Verificado MS Learn]`
```powershell
# Reemplazo oficial GA desde oct-2026 ante el retiro de Search-UnifiedAuditLog el 15-oct-2027
Connect-MgGraph -Scopes "AuditLogsQuery.Read.All"

$auditQuery = @{
    displayName         = "Auditoria Mensual DLCM y Disposicion"
    filterStartDateTime = (Get-Date).AddDays(-30).ToUniversalTime().ToString("o")
    filterEndDateTime   = (Get-Date).ToUniversalTime().ToString("o")
    operationFilters    = @(
        "Set-RetentionCompliancePolicy",
        "Remove-RetentionCompliancePolicy",
        "Enabled regulatory record option for retention labels",
        "Approved disposal",
        "Deleted file marked as a record"
    )
}
New-MgSecurityAuditLogQuery -BodyParameter $auditQuery
```

#### Consulta 7: Detección KQL en Microsoft Sentinel (`OfficeActivity`) de Alteración de Políticas y Disposición de Registros `[Verificado MS Learn]`
```kql
// Monitorea cambios administrativos sobre retención, Regulatory Records y disposiciones ejecutadas
OfficeActivity
| where TimeGenerated > ago(7d)
| where Operation in~ (
    "New-RetentionCompliancePolicy",
    "Set-RetentionCompliancePolicy",
    "Remove-RetentionCompliancePolicy",
    "Set-ComplianceTag",
    "Remove-ComplianceTag",
    "Enabled regulatory record option for retention labels",
    "Approved disposal",
    "Deleted file marked as a record"
)
| project TimeGenerated, UserId, Operation, OfficeWorkload, ClientIP, Parameters, AuditData
| order by TimeGenerated desc
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Capacidad Verificada | Consola o Comando de Comprobación | Resultado Esperado ("Proof of Life") | Estado |
| --- | --- | --- | --- |
| **Distribución saludable de políticas** | `Get-RetentionCompliancePolicy -DistributionDetail` | `Enabled = True` y `DistributionStatus = Success` en el 100% de las políticas productivas. | `[Verificado MS Learn]` |
| **Gobierno dedicado de Copilot e IA** | `Data Lifecycle Management > Policies > Retention policies` | Políticas independientes activas para `Microsoft Copilot experiences`, `Enterprise AI apps` y `Other AI apps`. | `[Verificado MS Learn]` |
| **Evaluación dinámica de Adaptive Scopes** | `Settings > Roles and scopes > Adaptive scopes > Scope details` | Membresía actualizada diariamente acorde a atributos Entra ID y propiedades SharePoint. | `[Verificado MS Learn]` |
| **Segregación RBAC en Disposition** | `Settings > Roles and groups` y `Records Management > Disposition` | Revisores en *mail-enabled security groups* con rol `Disposition Management` sin acceso de edición al File Plan. | `[Verificado MS Learn]` |
| **Auto-Expanding Archiving hasta 3 TB** | `Get-Mailbox <UPN> \| Select ArchiveStatus, AutoExpandingArchiveEnabled` | `AutoExpandingArchiveEnabled = True` y plan *Records Management* activo en usuarios E5 / Purview Suite. | `[Verificado MS Learn]` |
| **Trazabilidad viva de Proof of Disposal** | `Records Management > Disposition > Disposed items > Export` | Exportación CSV íntegra de registros eliminados con conservación nativa de hasta 7 años. | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Ejecutivos y Operativos

> **Nota de Gobernanza:** Las metas porcentuales y ventanas temporales siguientes constituyen criterios consultivos recomendados para comités ejecutivos de riesgo y retención `[Decisión / Propuesta Editorial]`.

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Etiqueta |
| --- | --- | --- | --- | --- | --- | --- |
| **KPI-01** | **Cobertura de Cargas de Trabajo con Directiva Base (Incluyendo IA)** | `(Cargas M365 y ubicaciones IA activas con política en Success / Total de cargas en uso) × 100` | `100%` | Mensual | CISO / Oficial de Cumplimiento | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Cumplimiento de SLA en Revisiones de Disposición** | `(Ítems en Pending disposition resueltos en <= 20 días hábiles / Total de ítems vencidos en el período) × 100` | `>= 95%` (0 ítems > 30 días) | Semanal / Mensual | Records Manager / Legal | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Completitud de Resguardo Mensual de Proof of Disposal** | `(Meses con paquete CSV Disposed items + Audit firmado con SHA-256 / Meses cerrados) × 100` | `100%` (12/12 meses) | Mensual | Auditoría Interna / GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Precisión en Políticas de Auto-Aplicación de Etiquetas** | `(Muestra auditada de ítems auto-etiquetados correctamente / Muestra total revisada en Content Explorer) × 100` | `>= 92%` | Semanal / Mensual | Records Manager / Data Governance | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Conciliación de Eventos y Asset ID en Retención por Eventos** | `(Eventos de negocio disparados con ComplianceAssetID válido / Total de eventos ocurridos en CLM/HRIS) × 100` | `>= 99%` | Mensual | Records Manager / Dueños de Proceso | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Reducción de Deuda de Retención en Exempleados** | `Variación % trimestral de Inactive Mailboxes y OneDrive retenidos indefinidamente sin mandato legal vigente` | Reducción continua (`0` retenciones perpetuas sin causa) | Mensual / Trimestral | DPO / Oficial de Cumplimiento / FinOps | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Tasa de Minimización de Datos ROT Pre-IA** | `(Volumen TB de datos ROT eliminados defensiblemente por políticas / Volumen ROT elegible identificado) × 100` | `>= 85%` anual en sitios expuestos a Copilot | Mensual | CISO / Líder de Seguridad IA | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Integridad de Cambios Administrativos y Priority Cleanup** | `(Cambios en políticas/etiquetas y limpiezas prioritarias con ticket y triple aprobación / Total detectado en Audit) × 100` | `100%` | Diaria / Mensual | CISO / SOC Manager / Auditoría | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional de 5 Niveles `[Decisión / Propuesta Editorial]`

| Nivel | Nombre del Nivel | Estado Operativo, Técnico y Documental |
| --- | --- | --- |
| **Nivel 1** | **Inicial / Retención Indefinida ("Guardar Todo")** | Ausencia de File Plan o uso de políticas globales estáticas de *solo retener*; uso de *Litigation Hold* legado para bajas; alta acumulación de ROT y superficie crítica de *oversharing* en Microsoft 365 Copilot. |
| **Nivel 2** | **Básico / Estático Manual** | Políticas estáticas por contenedor principal (Exchange, SharePoint, Teams) y etiquetas estándar aplicadas manualmente por el usuario; sin políticas específicas para IA ni revisiones formales de disposición. |
| **Nivel 3** | **Definido / Gobernado E5** | File Plan simplificado e importado con descriptores legales; *Adaptive Policy Scopes* operativos; políticas separadas para `Microsoft Copilot experiences`; declaración de *Records* y revisiones de disposición con segregación RBAC. |
| **Nivel 4** | **Gestionado y Automatizado** | Auto-etiquetado a escala por SITs, KeyQL, etiquetas de sensibilidad, *Trainable Classifiers* y *Cloud Attachments*; retención por eventos automatizada con Microsoft Graph API; resguardo mensual firmado de *Proof of Disposal* y control de deuda de retención. |
| **Nivel 5** | **Optimizado / Zero Trust & AI-Ready** | Minimización continua de ROT integrada con *DSPM for AI*; *Preservation Lock* y *Regulatory Records* auditados semestralmente; preservación forense automática de 120 días acoplada a *Adaptive Protection* (IRM); monitoreo KQL/Graph `AuditLogQuery` en Sentinel y ejercicios anuales con Legal y SOC. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

| Función NIST CSF 2.0 | Subcategoría Oficial | Resultado Esperado (Outcome) | Capacidad Habilitadora en Purview DLCM / RM | Evidencia Auditable Reproducible | Etiqueta |
| --- | --- | --- | --- | --- | --- |
| **GOVERN (GV)** | `GV.OC-03` | Los requisitos legales, regulatorios y contractuales sobre privacidad y registros se comprenden y gestionan. | *File Plan* con descriptores (`AuthorityType`, `CitationName`, `CitationJurisdiction`) y evaluaciones en *Compliance Manager*. | Exportación CSV del `File plan` aprobada por el Comité de Retención con mapeo norma → etiqueta. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad y datos están definidos, comunicados y exigidos. | Separación RBAC entre `Retention Manager`, `Records Management`, grupo `Disposition Management` y tríada de `Priority Cleanup`. | Matriz RACI vigente, exportación de Role Groups con expiración y bitácoras de activación PIM. | `[Decisión / Propuesta Editorial]` |
| **GOVERN (GV)** | `GV.RM-03` | Los riesgos estratégicos de seguridad y privacidad del dato se incorporan a la gestión de riesgos empresariales. | Eliminación sistemática de datos ROT, depuración de *Inactive Mailboxes* y retención acotada de prompts IA. | Reportes mensuales de reducción de ROT y deuda de retención (`KPI-06`, `KPI-07`). | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.AM-07` | Se mantienen inventarios de datos designados y sus metadatos conforme a su criticidad. | Clasificación e inventario mediante `Content Explorer`, SITs, *Trainable Classifiers*, `ComplianceAssetID` y *Adaptive Scopes*. | Exportación de `Get-ComplianceTag` y distribución de registros activos por sitio y buzón en `Content Explorer`. | `[Decisión / Propuesta Editorial]` |
| **IDENTIFY (ID)** | `ID.RA-05` | Las amenazas, vulnerabilidades, probabilidad e impacto guían la priorización del riesgo. | Cruce operativo entre *DSPM for AI* y DLCM para priorizar purga de contenido obsoleto expuesto a Copilot y agentes. | Informe mensual `M-03` de sitios sobreexpuestos remediados con políticas de ciclo de vida. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-01` | Se protegen la confidencialidad, integridad y disponibilidad de los datos en reposo. | Inmutabilidad de *Records* (*Record Versioning*), *Regulatory Records* (`Set-RegulatoryComplianceUI`) y `Preservation Lock` (`T1485`). | Salida PowerShell de políticas con `RestrictiveRetention: True` y validación `vti_writevalidationtoken`. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.DS-11` | Las preservaciones de datos se crean, protegen, mantienen y verifican periódicamente. | Preservación in-place en `Recoverable Items`, `SubstrateHolds`, `Preservation Hold Library`, *Cloud Attachments* y archivo hasta 3 TB. | Protocolos trimestrales `T-02` de búsqueda eDiscovery exitosa sobre elementos eliminados por usuarios bajo retención. | `[Decisión / Propuesta Editorial]` |
| **PROTECT (PR)** | `PR.AA-05` | Los derechos de acceso y autorizaciones respetan mínimo privilegio y separación de funciones. | Elevación JIT en Entra PIM, restricción estricta de `Content Explorer Content Viewer`, *Administrative Units* y triple aprobación en *Priority Cleanup*. | Auditoría mensual `M-05` de membresías RBAC/PIM e intentos administrativos bloqueados. | `[Decisión / Propuesta Editorial]` |
| **DETECT (DE)** | `DE.CM-09` | Los sistemas, servicios y datos se monitorean para detectar acciones o cambios potencialmente adversos. | Registro continuo en Purview Audit / Graph `AuditLogQuery` y reglas analíticas en Microsoft Sentinel sobre `OfficeActivity`. | Consultas mensuales `AuditLogQuery` archivadas e incidentes correlacionados en Sentinel (`D-02`, `S-05`). | `[Decisión / Propuesta Editorial]` |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos para evitar la propagación de exposición o daño material. | Purga acelerada de derrames sensibles mediante **Priority Cleanup** (`TA0010`) y suspensión instantánea por *eDiscovery Hold*. | Expedientes cerrados de `Priority Cleanup` con las 3 aprobaciones nominales y registros de holds legales. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.RP-03` | Se verifica la integridad de los datos preservados o recuperados antes de su uso legal u operativo. | Preservación automática de 120 días disparada por *Adaptive Protection* y extracción íntegra desde `PHL` e *Inactive Mailboxes*. | Evidencia de políticas automáticas de 120 días en usuarios de riesgo *Elevated* y logs de exportación eDiscovery. | `[Decisión / Propuesta Editorial]` |
| **RECOVER (RC)** | `RC.IM-01` | Los procesos de gobierno y recuperación evolucionan a partir de lecciones aprendidas. | Versionado trimestral del *File Plan*, ajuste de *Adaptive Scopes* y mejoras derivadas del simulacro anual `A-01`. | Actas del Comité de Retención e historial versionado de cambios en políticas y etiquetas. | `[Decisión / Propuesta Editorial]` |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Rutas Oficiales Microsoft Learn y Recursos Microsoft | Referentes Verificados (Microsoft y Comunidad MVP) | Certificaciones y Credenciales Vigentes (Nov 2026) | Estado |
| --- | --- | --- | --- | --- |
| **Administrador DLCM y Records Manager** | Ruta oficial *Implement data lifecycle and records management with Microsoft Purview*; guías técnicas de *File Plan*, *Event-driven retention*, *Adaptive scopes* y *Disposition of content*. | **Joanne Klein** (MVP, serie 2026 *Retention Schedule Hot Spots*); **Nikki Chapple** (MVP, guía práctica de Records Management e IA y análisis de *Retention Debt*); **Erica Toelle** y **Roberto Yglesias** (liderazgo de producto Purview DLM/RM). | **Microsoft Certified: Information Security Administrator Associate (Exam SC-401)** + Applied Skill oficial de retención, eDiscovery y Communication Compliance. | `[Verificado MS Learn]` |
| **Analista SOC / Ingeniero SIEM-Purview** | Módulo *Search and investigate with Microsoft Purview Audit*; documentación de Microsoft Graph `AuditLogQuery` y retención de *Copilot & AI apps*. | **Tony Redmond** (MVP, *Microsoft 365 / Microsoft Purview for IT Pros* ed. 2027); **Jorge Castañeda** (MVP Security en español). | **Exam SC-200** (Security Operations Analyst) combinado con **Exam SC-401**. | `[Verificado MS Learn]` |
| **Legal, Privacidad (DPO), Archivo y Revisores** | Documentación oficial en español (*Administración del ciclo de vida de datos* y *Plan de archivos*, contrastando siempre contra la versión en inglés) y plantillas regulatorias de *Compliance Manager*. | Lista oficial *Microsoft Purview* de **Microsoft Security Community** (YouTube) y demostraciones de **Microsoft Mechanics** sobre Copilot y agentes. | Formación interna sobre ISO 15489-1:2016 y habilitación práctica anual en `Disposition` y `Priority Cleanup`. | `[Verificado MS Learn]` `[Decisión / Propuesta Editorial]` |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Correcciones Técnicas Verificadas al `2026-11-11`

| # | Área Auditada | Hallazgo y Corrección Aplicada | Fuente Oficial Verificada |
| --- | --- | --- | --- |
| **1** | **Saneamiento documental de cruces en `MSEOP-MD\Purview DLCM`** | Se identificó que `0404 - Purview DLCM - Bloques - SecOps` y `Version Consolidada (1)` contenían bloques genéricos del SOC transversal centrados en Microsoft Sentinel (20 tareas SIEM, playbooks generales y MTTD/MTTR de red). Se descartó todo material ajeno y se construyeron 28 actividades 100% específicas de Purview DLCM y Records Management. | Auditoría del repositorio origen + `SPEC_GUIA_OPERACIONAL.md` `[Decisión / Propuesta Editorial]` |
| **2** | **Alineación de SKUs a Microsoft Purview Suite y matiz de Trainable Classifiers** | Se actualizó la nomenclatura legada *Purview E5 Compliance / Advanced Data Governance* hacia **Microsoft Purview Suite** (y M365 E5/E7), precisando que *Trainable Classifiers* requiere M365 E5 / Purview Suite y no se incluye en Office 365 E5 aislado. | Microsoft Purview Service Description y `manage-data-governance` `[Verificado MS Learn]` |
| **3** | **Ubicaciones separadas de retención para Copilot y Aplicaciones de IA** | Se incorporó la separación arquitectónica entre `Teams chats` y las tres nuevas categorías de retención IA (`Microsoft Copilot experiences`, `Enterprise AI apps` y `Other AI apps`), su dependencia de *Collection Policies* + Pay-As-You-Go y el flujo técnico en `SubstrateHolds` (con tiempos de purga total de hasta ~16 días en políticas de 1 día). | `learn.microsoft.com/en-us/purview/retention-policies-copilot` `[Verificado MS Learn]` |
| **4** | **Incremento de Auto-Expanding Archiving de 1,5 TB a 3 TB (Octubre 2026)** | Se documentó el despliegue oficial de octubre de 2026 que eleva el límite de archivo de expansión automática de 1,5 TB a **3 TB** para buzones con licencias E5 / Microsoft Purview Suite que mantengan habilitado el plan *Records Management*. | `learn.microsoft.com/en-us/purview/autoexpanding-archiving` `[Verificado MS Learn]` |
| **5** | **Restricciones críticas de Regulatory Records y Preservation Lock** | Se validó que `Set-RegulatoryComplianceUI -Enabled $true` habilita *Regulatory Records* (dejando rastro auditable), que estos **no admiten auto-aplicación**, que **Adaptive Policy Scopes no soportan Preservation Lock**, y que en políticas de etiquetas `-RestrictiveRetention $true` exige únicamente etiquetas de *Regulatory Record*. | `learn.microsoft.com/en-us/purview/declare-records` y `retention-preservation-lock` `[Verificado MS Learn]` |
| **6** | **Parámetros exactos de Multi-Stage Disposition y Proof of Disposal** | Se confirmaron hasta **5 etapas**, máximo 10 revisores o *mail-enabled security groups* por etapa y 200 por tenant (grupos M365 no soportados), borrado en <= 15 días tras aprobación final, auto-aprobación opcional de 7 a 365 días, tope de 16M de ítems y **Proof of Disposal conservada hasta 7 años**. | `learn.microsoft.com/en-us/purview/disposition` y `retention-limits` `[Verificado MS Learn]` |
| **7** | **Triple aprobación en Priority Cleanup y transición Graph AuditLogQuery** | Se incorporó la exigencia de **tres aprobaciones independientes** en *Priority Cleanup* (bloqueada sobre *Records* y *Regulatory Records*), la sustitución de las antiguas APIs REST de eventos por Microsoft Graph Records Management API y la migración desde `Search-UnifiedAuditLog` (retiro el 15-oct-2027) hacia Graph `AuditLogQuery` (GA oct-2026). | `learn.microsoft.com/en-us/purview/records-management` y `event-driven-retention` `[Verificado MS Learn]` |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Definido | Naturaleza | Justificación Arquitectónica y de Gobierno |
| --- | --- | --- | --- |
| **1** | **Metas numéricas de `KPI-01` a `KPI-08` y SLA humano de disposición (<= 20 días hábiles)** | `[Decisión / Propuesta Editorial]` | Microsoft Learn documenta los tiempos del servicio (ej. <= 15 días de purga tras aprobar), pero no fija SLAs organizacionales; establecer <= 20 días evita atrasos crónicos y auto-aprobaciones no revisadas. |
| **2** | **Modelo de madurez operacional de 5 niveles orientado a Zero Trust e IA** | `[Decisión / Propuesta Editorial]` | Ordena la adopción secuencial priorizando primero higiene ROT pre-Copilot y ámbitos dinámicos antes de habilitar controles irreversibles como *Regulatory Records* o *Preservation Lock*. |
| **3** | **Desactivación preventiva de `Set-RegulatoryComplianceUI ($false)` fuera de ventanas de cambio** | `[Decisión / Propuesta Editorial]` | Mitiga el riesgo operativo severo de que un administrador cree y publique por accidente una etiqueta *Regulatory Record* que ni siquiera un Global Admin puede remover después. |
| **4** | **Archivo mensual externo firmado (CSV + SHA-256) de `Disposed items`** | `[Decisión / Propuesta Editorial]` | Extiende la defensa probatoria ante leyes archivísticas o fiscales cuyos plazos de prescripción superan la ventana nativa de 7 años de *Proof of Disposal* en Purview. |
| **5** | **Mapeo de evidencia reproducible sobre 12 subcategorías de las 6 funciones NIST CSF 2.0** | `[Decisión / Propuesta Editorial]` | Convierte telemetría y configuraciones nativas de Purview en artefactos auditables estandarizados bajo CSWP 29. |

---

## 15. Directorio de Referencias Públicas Verificadas

### 15.1 Documentación Oficial Microsoft Learn
- **REF-01:** *Data lifecycle and records management in Microsoft Purview* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/manage-data-governance`). Arquitectura comparativa y solapamiento funcional entre DLCM y Records Management `[Verificado MS Learn]`.
- **REF-02:** *Learn about retention policies and retention labels (The principles of retention)* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/retention`). Definición canónica de los 4 principios oficiales de precedencia de retención `[Verificado MS Learn]`.
- **REF-03:** *Flowchart to determine when an item will be retained or permanently deleted* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/retention-flowchart`). Diagrama lógico determinístico con eDiscovery holds y Priority Cleanup `[Verificado MS Learn]`.
- **REF-04:** *Learn about records management (Compare restrictions & validate migrated records)* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/records-management`). Tabla oficial de restricciones Record vs. Regulatory Record y hash `vti_writevalidationtoken` `[Verificado MS Learn]`.
- **REF-05:** *Declare records by using retention labels (`Set-RegulatoryComplianceUI`)* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/declare-records`). Habilitación por PowerShell y eventos de auditoría de Regulatory Records `[Verificado MS Learn]`.
- **REF-06:** *Disposition of content* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/disposition`). Revisiones de disposición de hasta 5 etapas, permisos, *mail-enabled security groups*, auto-aprobación y exportación CSV `[Verificado MS Learn]`.
- **REF-07:** *Limits for retention policies and retention label policies* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/retention-limits`). Límites por tenant, ámbitos estáticos, revisores y retención de *Proof of Disposition* hasta 7 años `[Verificado MS Learn]`.
- **REF-08:** *Use Preservation Lock to restrict changes to retention policies and retention label policies* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/retention-preservation-lock`). Configuración irreversible `-RestrictiveRetention $true` y exclusión de Adaptive Scopes `[Verificado MS Learn]`.
- **REF-09:** *Use file plan to create and manage retention labels* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/file-plan-manager`). Descriptores normativos y especificación completa de columnas para importación/exportación CSV `[Verificado MS Learn]`.
- **REF-10:** *Start retention when an event occurs (Event-based retention)* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/event-driven-retention`). Relación entre tipos de evento, etiquetas, `ComplianceAssetID` y automatización con Microsoft Graph API `[Verificado MS Learn]`.
- **REF-11:** *Learn about retention for Copilot & AI apps* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/retention-policies-copilot`). Ubicaciones separadas para Microsoft Copilot experiences, Enterprise AI apps y Other AI apps, y flujo en `SubstrateHolds` `[Verificado MS Learn]`.
- **REF-12:** *Adaptive scopes in Microsoft Purview* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes`). Consultas dinámicas por atributos sobre usuarios, sitios SharePoint y grupos M365 `[Verificado MS Learn]`.
- **REF-13:** *Learn about auto-expanding archiving* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/autoexpanding-archiving`). Expansión automática incrementada a 3 TB desde octubre de 2026 para licencias E5 / Purview Suite elegibles `[Verificado MS Learn]`.
- **REF-14:** *Learn about inactive mailboxes* — Microsoft Learn (`https://learn.microsoft.com/en-us/purview/inactive-mailboxes-in-office-365`). Ciclo de vida de buzones de exempleados, Delay Hold de 30 días y precauciones sobre UPN `[Verificado MS Learn]`.

### 15.2 Blogs Oficiales y Empleados de Microsoft
- **REF-15:** Erica Toelle (Microsoft) — *New Microsoft 365 Copilot Data Lifecycle Management options*, Microsoft Security Blog (`https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-m365-copilot-data-lifecycle-management-options/4304636`). Guía oficial del equipo de producto sobre ubicaciones separadas para Copilot `[Verificado MS Learn]`.
- **REF-16:** Roberto Yglesias (Microsoft) — *Announcing general availability of Records Management*, Microsoft Security, Compliance, and Identity Blog (`https://techcommunity.microsoft.com/t5/security-compliance-and-identity/announcing-general-availability-of-records-management/bc-p/1462495/highlight/true`). Arquitectura fundacional de Records Management y disposición defensible en Microsoft 365 `[Verificado MS Learn]`.

### 15.3 Referentes de la Comunidad y MVPs de Seguridad / Microsoft 365
- **REF-17:** Joanne Klein (Microsoft MVP) — *Retention Schedule Hot Spots Blog Series for Purview* (`https://joannecklein.com/category/microsoft-purview/`). Patrones avanzados 2026 para llevar tablas de retención reales al File Plan de Purview.
- **REF-18:** Nikki Chapple (Microsoft MVP) — *Mastering Records Management in Microsoft Purview: A Practical Guide for AI-Ready Governance* (`https://nikkichapple.com/microsoft-purview-records-management-guide/`) y Tony Redmond (Microsoft MVP) — *Compliance Archives, Microsoft 365 for IT Pros* (`https://office365itpros.com/category/compliance/`). Simplificación de series, deuda de retención y automatización PowerShell/Graph.

### 15.4 Marcos Normativos y Estándares Internacionales
- **REF-19:** National Institute of Standards and Technology — *The NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)* (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`) e **ISO 15489-1:2016** *Information and documentation — Records management — Part 1: Concepts and principles* (`https://www.iso.org/standard/62542.html`).

# Guía Maestra de Excelencia Operacional: Microsoft Entra ID Governance (Gobierno de Ciclo de Vida JML, Derechos, Recertificación IA y Agentes)

## 1. Portada y Ficha de Control Documental

| Campo de Control | Valor Canónico |
| --- | --- |
| **Identificador del Módulo** | `02_Microsoft_Entra_ID_Governance` |
| **Orden en Repositorio Maestro** | `02` |
| **Slug Canónico** | `Microsoft_Entra_ID_Governance` |
| **Nombre Completo Oficial** | Microsoft Entra ID Governance (Gobierno de Ciclo de Vida JML, Derechos, Recertificación IA y Agentes) |
| **Categoría Maestra** | `Identidad y Acceso (Microsoft Entra)` |
| **Versión Documental** | `2.0 — Edición Consolidada y Revalidada` |
| **Fecha de Validación Técnica** | `2026-11-11` |
| **Origen y Trazabilidad** | `Nuevo desde Microsoft Learn MCP (Nov 2026)` |
| **Relación con Microsoft 365 E5** | `Complemento / Add-on sobre M365 E5 (Incluido en Microsoft Entra Suite / M365 E7)` `[Verificado MS Learn]` |
| **Portales Principales de Operación** | `https://entra.microsoft.com`, `https://myaccess.microsoft.com`, `https://myaccount.microsoft.com`, `https://portal.azure.com` `[Verificado MS Learn]` |
| **Audiencia Objetivo** | CISO, Identity Architect, Identity Governance Administrator, Lifecycle Workflows Administrator, Privileged Role Administrator, SOC L2/L3, HRIS Integration Lead, Application Owners, GRC & Internal Audit, FinOps |
| **Marcos Normativos Alineados** | NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29), MITRE ATT&CK Enterprise v18, ISO/IEC 27001:2022 (A.5.15–A.5.18), SOX ITGC (Logical Access), Zero Trust Maturity Model (CISA / Microsoft) `[Decisión / Propuesta Editorial]` |

> **Nota de Consolidación y Alcance (Noviembre 2026):** Este módulo establece el estándar operativo para **Microsoft Entra ID Governance** como capa avanzada de Identity Governance and Administration (IGA) sobre el plano base de **Microsoft Entra ID P2** (incluido en Microsoft 365 E5). Incorpora las actualizaciones documentadas en Microsoft Learn hasta noviembre de 2026, incluyendo la distinción contractual exacta frente a Entra ID P2, la inclusión en **Microsoft Entra Suite** y **Microsoft 365 E7 (The Frontier Suite, GA 1 de mayo de 2026)**, la ampliación de **Lifecycle Workflows** a 100 flujos de trabajo y 100 extensiones personalizadas en Logic Apps, el **Access Review Agent** de Microsoft Security Copilot en Entra y Teams, la verificación criptográfica/biométrica con **Verified ID + Face Check** en Access Packages, el modelo de facturación **MAU para Guests B2B** y el gobierno del ciclo de vida de identidades de agentes autónomos mediante **Microsoft Entra Agent ID** y **Microsoft Agent 365** `[Verificado MS Learn]`.

---

## 2. Resumen Ejecutivo y Posicionamiento en Arquitectura Zero Trust / M365 E5

### 2.1 Evolución Estratégica de IGA Cloud-Native a Noviembre de 2026

En una arquitectura Zero Trust moderna, autenticar fuertemente una identidad resulta insuficiente si dicha identidad conserva privilegios acumulados (*privilege creep*), cuentas huérfanas tras una desvinculación laboral o membresías permanentes sin dueño de negocio responsable. **Microsoft Entra ID Governance** resuelve de forma nativa las cuatro preguntas rectoras de gobierno de identidad y auditoría en recursos híbridos y multicloud: (1) qué identidades deben tener acceso a qué recursos, (2) qué están haciendo con ese acceso, (3) si existen controles organizacionales efectivos para administrar dicho acceso y (4) si los auditores pueden verificar objetivamente que los controles operan sin brechas `[Verificado MS Learn]`.

A corte de noviembre de 2026, el gobierno de identidades trasciende a los empleados humanos tradicionales para abarcar cuatro poblaciones críticas bajo un mismo plano de control en `https://entra.microsoft.com`: empleados e internos sincronizados desde sistemas HCM/HRIS, colaboradores externos B2B (**Guests** y **Multi-Tenant Organizations - MTO**), cuentas administrativas privilegiadas y la nueva generación de identidades no humanas y agentes autónomos (**Microsoft Entra Agent ID**) gobernados con patrocinio humano obligatorio (*human sponsor*), *agent identity blueprints* y paquetes de acceso sujetos a expiración `[Verificado MS Learn]`.

### 2.2 Distinción Quirúrgica de Licenciamiento: Entra ID P1 vs. Entra ID P2 (M365 E5) vs. Entra ID Governance, Entra Suite, Agent 365 y M365 E7

Uno de los errores arquitectónicos y presupuestarios más frecuentes en clientes empresariales es asumir que **Microsoft 365 E5** incluye todas las capacidades de **Microsoft Entra ID Governance**. Microsoft Learn establece taxativamente que todas las funciones IGA que ya eran Generally Available (GA) en **Microsoft Entra ID P2** permanecen en P2, pero **ninguna nueva capacidad o función IGA se añade ni se añadirá al SKU Microsoft Entra ID P2** `[Verificado MS Learn]`. Para habilitar las capacidades avanzadas de automatización JML, IA/ML en recertificaciones, Verified ID en paquetes de acceso y descubrimiento de cuentas huérfanas, los clientes de M365 E5 deben adquirir el complemento **Microsoft Entra ID Governance Step Up for Microsoft Entra ID P2** (o **Microsoft Entra Suite Add-on for Microsoft Entra ID P2**, o evolucionar hacia **Microsoft 365 E7**) `[Verificado MS Learn]`.

| Dominio Funcional IGA | Microsoft Entra ID P1 (M365 E3) | Microsoft Entra ID P2 (Incluido en M365 E5 / E5 Security) | Microsoft Entra ID Governance / Step-Up for P2 (y Entra Suite) | Microsoft Agent 365 / Microsoft 365 E7 (Frontier Suite) | Estado |
| --- | --- | --- | --- | --- | --- |
| **HR-Driven Inbound Provisioning** (Workday, SAP SuccessFactors hacia AD y Entra ID) | Incluido | Incluido | Incluido | Incluido en M365 E7 | `[Verificado MS Learn]` |
| **API-Driven Inbound Provisioning** (`/bulkUpload` hacia AD o Entra ID) | Incluido: tope 100K registros/24h (2.000 llamadas) y máx. 2 jobs AD + 2 jobs Entra | Incluido: tope 100K registros/24h (2.000 llamadas) y máx. 2 jobs AD + 2 jobs Entra | Ampliado: **300K registros/24h** (6.000 llamadas) y **máx. 20 jobs AD + 20 jobs Entra** | Ampliado en M365 E7 (300K/24h y 20+20 jobs) | `[Verificado MS Learn]` |
| **Account Discovery** (detección de cuentas locales y huérfanas en apps destino) | No incluido | No incluido | **Exclusivo ID Governance / Entra Suite** | Incluido en M365 E7 | `[Verificado MS Learn]` |
| **Cross-Tenant Sync** (usuarios vs. grupos y Cross-Cloud) | Solo usuarios (misma nube) | Solo usuarios (misma nube) | **Grupos (misma nube) y Cross-Cloud Synchronization** | Incluido en M365 E7 | `[Verificado MS Learn]` |
| **Lifecycle Workflows (LCW)** Joiner-Mover-Leaver y Custom Task Extensions (Logic Apps) | No incluido | No incluido | **Exclusivo ID Governance / Entra Suite** (hasta 100 workflows y 100 custom extensions) | Incluido en M365 E7; **Agent Sponsorship Tasks** en Agent 365 y E7 | `[Verificado MS Learn]` |
| **Entitlement Management (Base vs. Avanzado)** | No incluido | Base: catálogos, paquetes (grupos, Teams, apps, SPO), aprobaciones multietapa, SoD básico (paquetes/grupos incompatibles), My Access | Avanzado: **Auto-assignment policies**, **Verified ID + Face Check**, **Custom Extensions (Logic Apps)**, aprobaciones con **ID Protection / Insider Risk**, **Entra Roles (Preview)**, **SAP IAG (Preview)**, **PIM for Groups elegible en paquetes**, *Mark guest as governed*, solicitud por manager | Añade **Agentes y Service Principals en Access Packages**, permisos API OAuth en paquetes y **Agent Sponsors** como aprobadores | `[Verificado MS Learn]` |
| **Access Reviews (Base vs. ML/IA)** | No incluido | Base: grupos, apps, paquetes y roles PIM; helper de inactividad (>30d) cuando la revisión incluye activos + inactivos | Avanzado: revisiones **solo de usuarios inactivos**, **ML User-to-Group Affiliation** (hasta 600 miembros), **Catalog Access Reviews**, **PIM for Groups AR (Preview)**, **Custom Data Resource AR**, **Inactive Guest Insights** y **Access Review Agent** (con SCUs) | Incluido en M365 E7 (incluye SCUs base de Security Copilot) | `[Verificado MS Learn]` |
| **Privileged Identity Management (PIM)** | No incluido | Incluido: PIM para Entra Roles, Azure Resources, PIM for Groups y Auth Context | Añade **PIM Custom Extensions for Role Activation (Preview)** y Access Reviews avanzados | Incluido en M365 E7 | `[Verificado MS Learn]` |
| **Gobierno de Guests B2B** | No incluido | Funciones base P2 sin cobro adicional | **Facturación MAU en Azure** solo por huéspedes con acciones exclusivas de ID Governance en el mes (`GovernanceLicenseFeatureUsed = True`); exento en MTO | Igual modelo MAU en Azure para externos fuera de MTO | `[Verificado MS Learn]` |

### 2.3 Prerrequisitos Técnicos y Contractuales

1. **Suscripción prerrequisito activa en el tenant:** El SKU **Microsoft Entra ID Governance (User SL)** exige un plan activo con `AAD_PREMIUM` o `AAD_PREMIUM_P2` (ej. Entra ID P1, M365 E3/E5). El SKU **Microsoft Entra ID Governance Step Up for Microsoft Entra ID P2** exige estrictamente un plan activo con `AAD_PREMIUM_P2` (ej. M365 E5, M365 E5 Security, EMS E5). Si el prerrequisito expira, los escenarios gobernados y asignaciones elegibles PIM dejan de operar `[Verificado MS Learn]`.
2. **Cobertura cuantitativa de licencias de miembros:** No es obligatorio asignar técnicamente el *service plan* usuario por usuario para que las funciones operen en el directorio, pero el tenant debe poseer tantas licencias como usuarios miembros estén en el alcance de (o administren) las capacidades de Entra ID Governance `[Verificado MS Learn]`.
3. **Vinculación de suscripción Azure para Guests B2B y Logic Apps:** El gobierno avanzado de usuarios con `userType == "Guest"` exige vincular el tenant a una suscripción y grupo de recursos de Azure desde `ID Governance > Dashboard > Guest governance` con rol `Owner` sobre la suscripción o RG; igualmente, las Custom Extensions y la retención >30 días en Log Analytics/Sentinel requieren suscripción Azure `[Verificado MS Learn]`.
4. **Calidad de atributos autoritativos en HRIS:** Para ejecutar Lifecycle Workflows y recomendaciones ML de afiliación usuario-grupo, los objetos de usuario en Entra ID deben poblar de forma consistente `employeeHireDate`, `employeeLeaveDateTime`, `department`, `employeeType`, `mail` y la referencia jerárquica `manager` `[Verificado MS Learn]`.

### 2.4 Principios Rectores de Excelencia Operacional

1. **Fuente autoritativa única impulsada por RR. HH. (HR-Driven Source of Truth):** Todo alta, cambio de puesto o baja nace en el sistema HCM (Workday, SAP SuccessFactors o API `/bulkUpload`) y fluye sin intervención manual hacia AD/Entra ID `[Verificado MS Learn]`.
2. **Automatización determinista Joiner-Mover-Leaver (Zero-Touch JML):** Orquestar incorporación día-1 con Temporary Access Pass (TAP), reajuste en movilidad interna y revocación integral en bajas mediante Lifecycle Workflows y Azure Logic Apps `[Verificado MS Learn]`.
3. **Acceso empaquetado por rol de negocio, temporal y delegado (Entitlement-by-Design):** Sustituir asignaciones directas ad-hoc por Access Packages gobernados en catálogos delegados a dueños de negocio, exigiendo expiración obligatoria, controles de Separation of Duties y pruebas criptográficas Verified ID en accesos críticos `[Verificado MS Learn]`.
4. **Recertificación inteligente asistida por ML e IA (Anti-Rubber-Stamping):** Erradicar aprobaciones mecánicas combinando señales de inactividad (>30 días), afiliación organizacional ML (*User-to-Group Affiliation*) y el **Access Review Agent** en Microsoft Teams `[Verificado MS Learn]`.
5. **Cero privilegios permanentes (Zero Standing Privileges - ZSP):** Administrar todo rol privilegiado y membresía de grupos críticos como elegible en PIM con activación Just-In-Time (JIT) sujeta a Conditional Access Authentication Context y MFA resistente al phishing `[Verificado MS Learn]`.
6. **Paridad de gobierno para externos B2B e identidades de Agentes IA:** Someter tanto a invitados externos como a identidades **Microsoft Entra Agent ID** a patrocinadores humanos responsables (*sponsors*), transferencia automática de patrocinio ante bajas y expiración automática de derechos `[Verificado MS Learn]`.

---

## 3. Arquitectura Operativa, Componentes Clave e Integraciones del Ecosistema

### 3.1 Arquitectura Funcional de Extremo a Extremo

```
[Sistemas Autoritativos HCM / HRIS]
  Workday | SAP SuccessFactors | HCM Custom via API (/bulkUpload: 300K reg/24h, 20+20 jobs)
                        |
                        v (Inbound Provisioning / Cloud Sync)
+---------------------------------------------------------------------------------------+
|                   PLANO DE CONTROL MICROSOFT ENTRA ID GOVERNANCE                      |
|  1. Lifecycle Workflows (LCW)           2. Entitlement Management (EM)                |
|     - Triggers: Time-based (V1/V2),        - Catalogs (7.500) & Access Packages (20K) |
|       Attribute, Group, Inactivity         - Auto-assignment (15K/pol) & SoD checks   |
|     - 100 Workflows / 25 Tasks /           - Verified ID + Face Check + IDV Partners  |
|       100 Custom Extensions (Logic Apps)   - Custom Extensions (500) + Risk Approvals |
|                                                                                       |
|  3. Access Reviews + IA/ML              4. Privileged Identity Management (PIM)       |
|     - Inactive-only & 30d Sign-in          - Entra Roles, Azure RBAC, PIM for Groups  |
|     - ML User-to-Group Affiliation         - Auth Context + Phishing-Resistant MFA    |
|     - Access Review Agent (Teams/Entra)    - PIM Custom Extensions (Preview)          |
|                                                                                       |
|  5. Agent ID & Guest Governance                                                       |
|     - Agent Blueprints, Agent IDs, Agent Users, Human Sponsors & Sponsor Transfer     |
|     - B2B Guests Governed Lifecycle + MAU Billing + MTO Exemption                     |
+---------------------------------------------------------------------------------------+
          |                             |                               |
          v (Outbound Provisioning)     v (Políticas Zero Trust)        v (Telemetría & SIEM)
[Apps Cloud & On-Premises]    [Ecosistema M365 E5 / E7]       [Azure Monitor / Sentinel]
- SaaS (SCIM 2.0 / SAML)      - Conditional Access & Auth     - AuditLogs (EM, AR, LCW, PIM)
- AD Groups Writeback         - Entra ID Protection           - AADProvisioningLogs
- Apps LDAP / SQL / REST      - Purview Insider Risk Mgmt     - Graph /identityGovernance/*
- SAP Cloud IAG + Account     - Security Copilot SCUs         - Workbooks & Retención >30d
  Discovery (huérfanos)
```

### 3.2 Componentes y Motores Operativos Vigentes (Noviembre 2026)

| Componente Oficial | Función Operativa Principal | Ruta en Portal Oficial | Límites de Servicio y Especificaciones Clave | Estado |
| --- | --- | --- | --- | --- |
| **Inbound HR & API-Driven Provisioning** | Creación, actualización y desactivación automática de identidades en AD on-premises y Entra ID a partir de Workday, SAP SuccessFactors o carga masiva `/bulkUpload`. | `entra.microsoft.com > Entra ID > Enterprise apps > Provisioning` | Hasta **300.000 registros/24h** (6.000 llamadas de 50 registros) y **20 jobs AD + 20 jobs Entra ID** con licencia Entra ID Governance `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Lifecycle Workflows (LCW)** | Automatización de procesos Joiner, Mover y Leaver mediante plantillas, disparadores basados en tiempo/atributo/grupo/inactividad, más de 30 tareas nativas y extensiones Logic Apps. | `entra.microsoft.com > ID Governance > Lifecycle workflows` | Máx. **100 workflows/tenant**, **25 tareas/workflow**, **100 Custom Task Extensions**, `offsetInDays` `-180` a `+180` días, evaluación cada **1–24 h** (defecto 3 h), 5 scopes administrativos/workflow y 10 usuarios on-demand `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Entitlement Management (EM) & My Access** | Agrupación de roles de grupos, Teams, aplicaciones Enterprise, sitios SharePoint Online, roles Entra (Preview), roles SAP IAG (Preview) y permisos API OAuth (Agent 365) en paquetes de acceso delegados. | `entra.microsoft.com > ID Governance > Entitlement management` y `myaccess.microsoft.com` | Máx. **7.500 catálogos**, **20.000 Access Packages**, **25.000 políticas**, **300.000 asignaciones/tenant**, **15.000 asignaciones por auto-assignment policy**, **2.500 Connected Orgs** y **500 Custom Extensions** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Verified ID & Separation of Duties en EM** | Imposición de incompatibilidad unidireccional/bidireccional entre paquetes o grupos de seguridad y exigencia de credenciales verificables W3C + selfie **Face Check** en tiempo real antes de solicitar acceso. | `entra.microsoft.com > ID Governance > Entitlement management > Access packages > Separation of duties / Policies > Requests` | Soporta emisores de **Microsoft Entra Verified ID Network** y socios IDV integrados desde **Microsoft Security Store**; Face Check comparte únicamente el resultado de coincidencia preservando privacidad `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Access Reviews & Access Review Agent** | Campañas periódicas de recertificación de membresías de grupos, aplicaciones, paquetes, catálogos y roles PIM, enriquecidas con ML de afiliación jerárquica y asistente conversacional IA en Teams. | `entra.microsoft.com > ID Governance > Access reviews` y `Agents > Access Review Agent` | Afiliación ML **User-to-Group** soporta grupos internos de hasta **600 usuarios** con atributo `manager`; inactividad se evalúa a **30 días** al inicio de la campaña `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Privileged Identity Management (PIM)** | Elevación Just-In-Time (JIT) con aprobación, justificación, ticket, MFA/Authentication Context y alertas de anomalías sobre roles de Entra ID, recursos Azure y **PIM for Groups**. | `entra.microsoft.com > ID Governance > Privileged Identity Management` | Soporta asignaciones elegibles y activas acotadas en el tiempo, Access Reviews de roles y **Custom Extensions for Role Activation (Preview)** `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Account Discovery & Outbound Provisioning** | Conector SCIM 2.0 y agente de aprovisionamiento para apps SaaS y on-premises (LDAP, SQL, REST/SOAP, SAP) con descubrimiento de cuentas existentes y detección de cuentas huérfanas. | `entra.microsoft.com > Entra ID > Enterprise apps > <App> > Provisioning` | Descubrimiento e inventario de cuentas locales no correlacionadas con Entra ID exclusivo de Entra ID Governance / Entra Suite `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Agent Identity Governance (Entra Agent ID)** | Gobierno de ciclo de vida y acceso para agentes IA mediante *agent identity blueprints*, *agent identities*, *agent users* y patrocinadores humanos responsables. | `entra.microsoft.com > Entra ID > Agent ID` / `myaccess.microsoft.com` / `myaccount.microsoft.com` | Integrado con Microsoft Foundry, Copilot Studio, Azure App Service/Functions, Teams y Agent 365; transferencia automática de sponsor al manager cuando el sponsor sale de la empresa `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

### 3.3 Catálogo Verificado de Tareas Integradas en Lifecycle Workflows y Endpoints Microsoft Graph

Microsoft Learn documenta identificadores inmutables (`taskDefinitionId`) para orquestar flujos Joiner, Mover y Leaver tanto desde el centro de administración como declarativamente mediante Microsoft Graph `[Verificado MS Learn]`:

| Tarea Integrada en Lifecycle Workflows | `taskDefinitionId` Oficial | Categoría JML | Propósito Operativo Clave | Estado |
| --- | --- | --- | --- | --- |
| `Send welcome email to new hire` | `70b29d51-b59a-4773-9280-8841dfd3f2ea` | Joiner | Envía correo de bienvenida personalizable con atributos dinámicos `{{user.displayName}}`. | `[Verificado MS Learn]` |
| `Send onboarding reminder email` | `3C860712-2D37-42A4-928F-5C93935D26A1` | Joiner | Notifica recordatorio previo al ingreso al `manager` poblado del nuevo colaborador. | `[Verificado MS Learn]` |
| `Generate Temporary Access Pass and send via email to user's manager` | `1b555e50-7f65-41d5-b514-5894a026d10d` | Joiner | Emite un TAP de arranque sin contraseña (`{{temporaryAccessPass}}`) para registro FIDO2/Passkey día-1. | `[Verificado MS Learn]` |
| `Request user access package assignment` | `c1ec1e76-f374-4375-aaa6-0bb6bd4c60be` | Joiner, Mover | Solicita y entrega paquetes de acceso base según rol organizacional o cambio de área. | `[Verificado MS Learn]` |
| `Assign licenses to user` | `683c87a4-2ad4-420b-97d4-220d90afcd24` | Joiner, Mover | Asigna SKUs requeridos durante alta o transición de puesto. | `[Verificado MS Learn]` |
| `Add user to groups` / `Add user to teams` | `22085229-5809-45e8-97fd-270d28d66910` / `e440ed8d-25a1-4618-84ce-091ed5be5594` | Joiner, Mover, Leaver | Gestiona membresías en grupos estáticos y equipos Microsoft Teams sin reglas dinámicas por grupo. | `[Verificado MS Learn]` |
| `Update user attributes` | `2c8f4a1b-7d3e-4f9c-8a5b-6e1d2c3f4a5b` | Joiner, Mover, Leaver | Actualiza propiedades estándar, extensiones o Custom Security Attributes durante el ciclo JML. | `[Verificado MS Learn]` |
| `Run a custom task extension` | `4262b724-8dba-4fad-afc3-43fcbb497a0e` | Joiner, Mover, Leaver | Dispara Azure Logic Apps autenticadas con Managed Identity para integrar ITSM, AD o sistemas legacy. | `[Verificado MS Learn]` |
| `Send email to notify manager of user move` | `aab41899-9972-422a-9d97-f626014578b7` | Mover | Alerta al nuevo o anterior gerente ante cambio de `department` o `jobTitle` para validar accesos heredados. | `[Verificado MS Learn]` |
| `Transfer agent identity sponsorships to manager` | `b8f4c3d5-9e7a-4b1c-8f2d-6a5e8b9c7f4a` | Mover, Leaver | Transfiere automáticamente el patrocinio humano de identidades **Microsoft Entra Agent ID** al gerente. | `[Verificado MS Learn]` |
| `Send email to manager / co-sponsors about sponsorship changes` | `b8c4e1f9-3a7d-4b2e-9c5f-8d6a9b1c2e3f` / `ad3b85cd-75b1-43e7-b4b9-0e52faba3944` | Mover, Leaver | Informa a gerentes y co-sponsors sobre transiciones de responsabilidad de invitados o agentes IA. | `[Verificado MS Learn]` |
| `Disable user account` | `1dfdfcc7-52fa-4c2e-bf3a-e3919cc12950` | Leaver | Bloquea el inicio de sesión (`accountEnabled = false`) en Entra ID o híbrido sincronizado. | `[Verificado MS Learn]` |
| `Revoke all refresh tokens for user` | `509589a4-0466-4471-829e-49c5e502bdee` | Mover, Leaver | Invalida tokens de actualización activos e impulsa corte inmediato vía Continuous Access Evaluation (CAE). | `[Verificado MS Learn]` |
| `Cancel all pending access package assignment requests` | `498770d9-bab7-4e4c-b73d-5ded82a1d0b3` | Leaver | Anula solicitudes en tránsito para impedir entregas posteriores a la baja. | `[Verificado MS Learn]` |
| `Remove all access package assignments for user` | `42ae2956-193d-4f39-be06-691b8ac4fa1d` | Mover, Leaver | Revoca de forma centralizada todos los paquetes de acceso asignados al colaborador. | `[Verificado MS Learn]` |
| `Remove users from all groups` / `Remove user from all teams` | `b3a31406-2a15-4c9a-b25b-a658fa5f07fc` / `81f7b200-2816-4b3b-8c5d-dc556f07b024` | Leaver | Limpia la totalidad de membresías residuales de grupos y Teams en una sola operación. | `[Verificado MS Learn]` |
| `Remove all license assignments from user` | `8fa97d28-3e52-4985-b3a9-a1126f9b8b4e` | Leaver | Libera licencias M365/Entra tras ventana legal de retención de buzón/OneDrive. | `[Verificado MS Learn]` |
| `Send email about user inactivity` / `unsponsored guest removal (Preview)` | `92f74cb4-f1b6-4ec0-b766-96210f56edc2` / `a8e4c7f2-9d1b-4a3e-b5c6-8f2e7a9d4c1b` | Leaver | Automatiza avisos previos al bloqueo por inactividad o retiro de invitados externos sin sponsor. | `[Verificado MS Learn]` |
| `Delete user` | `8d18588d-9ad3-4c0f-99d0-ec215f0e3dff` | Leaver | Elimina definitivamente el objeto de usuario tras el período de gracia de retención corporativa. | `[Verificado MS Learn]` |

Asimismo, la automatización como código (*Governance-as-Code*) se apoya en el espacio de nombres `/v1.0/identityGovernance` de Microsoft Graph `[Verificado MS Learn]`:

| Superficie Microsoft Graph API | Endpoint Principal (`https://graph.microsoft.com/v1.0/...`) | Permisos Mínimos de Aplicación / Delegados | Caso de Uso de Automatización y Auditoría |
| --- | --- | --- | --- |
| **Entitlement Management** | `/identityGovernance/entitlementManagement/catalogs`, `/accessPackages`, `/assignmentPolicies`, `/assignments`, `/assignmentRequests` | `EntitlementManagement.Read.All` / `EntitlementManagement.ReadWrite.All` | Respaldo declarativo de catálogos/paquetes, reglas SoD (`incompatibleAccessPackages`) y solicitudes programáticas por agentes IA `[Verificado MS Learn]`. |
| **Access Reviews** | `/identityGovernance/accessReviews/definitions`, `/definitions/{id}/instances/{id}/decisions` | `AccessReview.Read.All` / `AccessReview.ReadWrite.All` | Despliegue estandarizado de campañas trimestrales, extracción de decisiones de revisores y métricas de inactividad `[Verificado MS Learn]`. |
| **Lifecycle Workflows** | `/identityGovernance/lifecycleWorkflows/workflows`, `/customTaskExtensions`, `/workflows/{id}/runs`, `/taskReports` | `LifecycleWorkflows.Read.All` / `LifecycleWorkflows.ReadWrite.All` | Control de versiones de flujos JML, disparo `/activate` bajo demanda y auditoría automatizada de fallos por tarea `[Verificado MS Learn]`. |
| **Privileged Identity Management** | `/roleManagement/directory/roleEligibilityScheduleInstances`, `/roleAssignmentScheduleRequests`, `/identityGovernance/privilegedAccess/group` | `RoleEligibilitySchedule.Read.Directory`, `PrivilegedEligibilitySchedule.Read.AzureADGroup` | Inventario continuo Zero Standing Privileges (ZSP) para roles Entra y **PIM for Groups** `[Verificado MS Learn]`. |
| **Inbound API Provisioning** | `/servicePrincipals/{id}/synchronization/jobs/{jobId}/bulkUpload` | `SynchronizationData-User.Upload` (Application) | Ingesta autoritativa SCIM payload desde sistemas RR. HH. propios (hasta 6.000 llamadas / 300K registros cada 24 h) `[Verificado MS Learn]`. |

### 3.4 Integraciones Cruzadas en el Ecosistema Microsoft Security

- **Microsoft Entra ID Protection y Microsoft Purview Insider Risk Management:** Entitlement Management permite condicionar etapas de aprobación o bloquear solicitudes de Access Packages según el nivel de riesgo de identidad en Entra ID Protection o el nivel de riesgo interno calculado por Purview Insider Risk Management `[Verificado MS Learn]`.
- **Microsoft Entra Conditional Access:** Integración bidireccional mediante (a) **Authentication Context** exigido al activar roles PIM o grupos PIM, (b) **Terms of Use** vinculados a paquetes de acceso y (c) políticas de Acceso Condicional heredadas a escala desde *agent identity blueprints* para agentes IA `[Verificado MS Learn]`.
- **Microsoft Security Copilot:** Creación asistida en lenguaje natural de **Lifecycle Workflows**, investigación contextual en **Entra Copilot chat** y despliegue del **Access Review Agent** (consumiendo la dotación de SCUs incluida en M365 E5/E7 o capacidad Azure) `[Verificado MS Learn]`.
- **Azure Monitor, Log Analytics y Microsoft Sentinel:** Dado que Entra ID retiene eventos de auditoría nativamente solo por **30 días**, la exportación continua de `AuditLogs` y `AADProvisioningLogs` hacia un workspace de Log Analytics / Sentinel (aprovechando el Data Grant de 5 MB/usuario/día de M365 E5 para `AuditLogs` de Entra ID) habilita retención multianual, Workbooks (*Access Package Activity*, *Application role assignment activity*) y correlación SIEM/UEBA `[Verificado MS Learn]`.

---

## 4. Modelo de Gobierno, Roles y Matriz RBAC de Mínimo Privilegio (PIM / JIT)

Microsoft Entra ID Governance aplica delegación granular para separar la administración técnica de plataforma (IT/IAM) de la propiedad funcional de los recursos (dueños de catálogos, gestores de paquetes, aprobadores de negocio y sponsors de invitados/agentes). En particular, Microsoft Learn advierte que **User Administrator** ya no puede crear catálogos ni administrar paquetes en catálogos que no posea; debe emplearse **Identity Governance Administrator** y delegación por catálogo `[Verificado MS Learn]`.

| Rol Oficial (Entra RBAC / Delegación EM) | Plano de Control | Permisos Clave y Alcance | Estrategia PIM / JIT Recomendada | Responsabilidad Operativa y Segregación de Funciones (SoD) | Estado |
| --- | --- | --- | --- | --- | --- |
| **Identity Governance Administrator** | Microsoft Entra RBAC | Crear y gestionar catálogos, Access Packages, políticas EM, Connected Organizations, Access Reviews de grupos/apps y configuración general de ID Governance (no añade grupos ni sitios SPO a catálogos salvo propiedad explícita) `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 4 h, MFA Phishing-Resistant + justificación + ticket ITSM; 0 asignaciones permanentes) `[Decisión / Propuesta Editorial]`. | Gobierno central de arquitectura EM y campañas de recertificación; segregado de Privileged Role Administrator `[Decisión / Propuesta Editorial]`. | `[Verificado MS Learn]` |
| **Lifecycle Workflows Administrator** | Microsoft Entra RBAC | Crear, editar, versionar, programar, ejecutar on-demand y auditar Lifecycle Workflows y Custom Task Extensions (`LifecycleWorkflows.ReadWrite.All`) `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 4 h, aprobación de par IAM Lead para cambios en flujos Leaver productivos) `[Decisión / Propuesta Editorial]`. | Automatización JML, mantenimiento de plantillas, monitoreo de `My Feed` y remediación de tareas fallidas `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Privileged Role Administrator** | Microsoft Entra RBAC | Configurar políticas de PIM para roles Entra y PIM for Groups, administrar asignaciones elegibles/activas y crear Access Reviews sobre roles privilegiados `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 2 h, aprobación dual + Authentication Context `c1` con FIDO2/Passkey + PAW) `[Decisión / Propuesta Editorial]`. | Custodia de Tier-0 y gobierno JIT; prohibido aprobar sus propias solicitudes de elevación `[Decisión / Propuesta Editorial]`. | `[Verificado MS Learn]` |
| **Groups Administrator + Catalog Owner** | Entra RBAC + Rol de Catálogo EM (`ae79f266-...`) | Combinación requerida (cuando no se usa Global Admin ni propiedad individual de cada grupo) para incorporar grupos de seguridad y grupos M365 dentro de un catálogo EM específico `[Verificado MS Learn]`. | `Groups Administrator` **Elegible en PIM** (máx. 2 h); `Catalog owner` asignado a grupo de seguridad gobernado `[Decisión / Propuesta Editorial]`. | Incorporación controlada de grupos corporativos a catálogos departamentales sin exponer `Global Administrator` `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Application Administrator / Cloud App Admin + Catalog Owner** | Entra RBAC + Rol de Catálogo EM | Incorporar aplicaciones Enterprise (`servicePrincipals/appRoleAssignedTo/update`), configurar aprovisionamiento inbound HR/API y outbound SCIM y ejecutar **Account Discovery** `[Verificado MS Learn]`. | **Elegible en PIM** (máx. 4 h, MFA resistente al phishing + registro de cambio) `[Decisión / Propuesta Editorial]`. | Onboarding de aplicaciones al modelo IGA, mapeo de atributos SCIM y conciliación de cuentas huérfanas `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Catalog Creator & Catalog Owner (Negocio)** | Rol Delegado de Entitlement Management (`ba92d953-...` / `ae79f266-...`) | Crear catálogos departamentales propios, añadir recursos de los cuales ya sea propietario y delegar `Access package manager` sin ver catálogos de otras áreas `[Verificado MS Learn]`. | Asignación mediante grupo de seguridad sujeto a Access Review trimestral (no requiere rol de directorio Entra) `[Decisión / Propuesta Editorial]`. | Descentralización segura del gobierno hacia líderes de unidades de negocio (Finanzas, Legal, Ingeniería) `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Access Package Manager & Assignment Manager** | Rol Delegado de Catálogo EM (`7f480852-...` / `e2182095-...`) | `Access package manager`: crear/editar paquetes, políticas y SoD en su catálogo. `Assignment manager`: asignar/remover usuarios y reprocesar entregas sin alterar políticas `[Verificado MS Learn]`. | Asignación acotada por catálogo con expiración semestral y revisión por `Catalog owner` `[Decisión / Propuesta Editorial]`. | Operación diaria de paquetes departamentales y soporte de entregas fallidas sin privilegios globales `[Verificado MS Learn]`. | `[Verificado MS Learn]` |
| **Security Reader / Reports Reader + Log Analytics Reader** | Entra RBAC + Azure RBAC | Lectura de `AuditLogs`, `AADProvisioningLogs`, reportes de Lifecycle Workflows, Workbooks de Entitlement Management y métricas de cumplimiento para SOC y Auditoría Interna `[Verificado MS Learn]`. | Activo acotado o elegible PIM (8 h) para analistas SOC L2/L3 y auditores GRC `[Decisión / Propuesta Editorial]`. | Supervisión independiente, caza de desviaciones IGA y verificación forense sin capacidad de mutación `[Verificado MS Learn]`. | `[Verificado MS Learn]` |

> **Nota sobre Verified ID en Access Packages:** A la fecha de validación, la incorporación inicial de requisitos **Required Verified IDs** en un paquete de acceso documenta como rol prerrequisito `Global Administrator` en el asistente de configuración (con soporte progresivo para `Identity Governance Administrator`, `Catalog owner` y `Access package manager`); por ello, toda alta de emisor Verified ID debe ejecutarse bajo ventana PIM auditada de emergencia/cambio controlado `[Verificado MS Learn]`.

---

## 5. Cadencia Operativa Diaria

### D-01: Supervisión de ejecuciones y fallos de Lifecycle Workflows (Joiner / Mover / Leaver)
- **Objetivo:** Detectar y corregir en menos de 4 horas cualquier fallo en tareas críticas JML (especialmente deshabilitación de cuentas, revocación de refresh tokens y entrega de TAP) `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Lifecycle workflows > Overview (My Feed) / Workflow history` `[Verificado MS Learn]`.
- **Rol Responsable:** Lifecycle Workflows Administrator.
- **Procedimiento Paso a Paso:**
  1. Revisar los indicadores globales de `My Feed`: *Total processed users*, *Processed users with failures* y *Failed tasks* de las últimas 24 horas `[Verificado MS Learn]`.
  2. Filtrar en `Workflow history` la pestaña `Runs` y `Tasks` por estado `Failed`, priorizando flujos de categoría **Leaver** `[Verificado MS Learn]`.
  3. Inspeccionar la razón del error en `Audit logs` (ej. atributo `manager` o `mail` faltante, timeout de Custom Task Extension >3 h o bloqueo de directorio híbrido) `[Verificado MS Learn]`.
  4. Corregir el atributo origen o la Logic App asociada y ejecutar **Run on demand** sobre los usuarios afectados (en lotes de hasta 10 usuarios por ejecución manual) verificando que `Status == Succeeded` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro en `AuditLogs` (`LoggedByService == "Lifecycle Workflows"`, `Category in ("WorkflowManagement", "TaskManagement")`) con cierre de incidencia diaria `[Verificado MS Learn]`.

### D-02: Monitoreo de salud de conectores HR Inbound (Workday / SuccessFactors / API `/bulkUpload`)
- **Objetivo:** Garantizar que las altas, bajas y cambios contractuales desde RR. HH. fluyan sin cuarentenas ni errores de sincronización hacia AD y Entra ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Entra ID > Enterprise apps > <HR Provisioning App> > Provisioning > Provisioning logs` `[Verificado MS Learn]`.
- **Rol Responsable:** Application Administrator (HRIS Integration Lead).
- **Procedimiento Paso a Paso:**
  1. Verificar que el estado del job de aprovisionamiento no se encuentre en **Quarantine** y que el último ciclo haya finalizado dentro del intervalo esperado `[Verificado MS Learn]`.
  2. Filtrar `Provisioning logs` por `Status == Failure` en las últimas 24 horas (colisiones de `userPrincipalName`, DN inválido en AD o reglas de scoping).
  3. Para flujos API-driven, validar el consumo diario respecto a la cuota de **300.000 registros/24h** (6.000 peticiones `/bulkUpload`) `[Verificado MS Learn]`.
  4. Coordinar con RR. HH. la corrección de datos maestros erróneos en el sistema origen (evitando ediciones manuales directas en Entra ID que rompan la precedencia autoritativa) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Eventos en tabla `AADProvisioningLogs` sin errores no gestionados >24 horas `[Verificado MS Learn]`.

### D-03: Resolución de solicitudes de Access Packages en estado `DeliveryFailed` o expirando sin aprobador
- **Objetivo:** Evitar bloqueos operativos de usuarios legítimos y entregas parciales de recursos en paquetes de acceso `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Access packages > Requests` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / Access Package Assignment Manager.
- **Procedimiento Paso a Paso:**
  1. Filtrar la vista global de `Requests` por estados `DeliveryFailed`, `PartiallyDelivered` y `PendingApproval` próximos a vencer `[Verificado MS Learn]`.
  2. Seleccionar las solicitudes con fallo de entrega, inspeccionar la pestaña de errores de recurso (ej. fallo SCIM en app destino o licencia agotada en grupo de licenciamiento) `[Verificado MS Learn]`.
  3. Una vez subsanada la causa raíz en el recurso destino, ejecutar la acción nativa **Reprocess** sobre la asignación afectada `[Verificado MS Learn]`.
  4. Verificar que las políticas con aprobadores ausentes estén enrutando correctamente hacia **Alternate approvers** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Traza en `AuditLogs` (`Category == "EntitlementManagement"`) confirmando estado `Delivered` `[Verificado MS Learn]`.

### D-04: Revisión de alertas de Privileged Identity Management (PIM) y activaciones anómalas Tier-0
- **Objetivo:** Validar diariamente que toda activación de roles críticos (`Global Administrator`, `Privileged Role Administrator`, `Identity Governance Administrator`) responda a tickets autorizados y que no existan alertas PIM activas `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Privileged Identity Management > Microsoft Entra roles > Alerts / Audit history` `[Verificado MS Learn]`.
- **Rol Responsable:** Privileged Role Administrator / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Inspeccionar las **PIM Alerts** integradas (*Roles are being assigned outside of Privileged Identity Management*, *Too many global administrators*, *Roles don't require multifactor authentication for activation*) `[Verificado MS Learn]`.
  2. Revisar el historial de activaciones de las últimas 24 horas contrastando el número de ticket/justificación contra la herramienta ITSM `[Decisión / Propuesta Editorial]`.
  3. Investigar de inmediato con SOC L2 cualquier asignación directa fuera de PIM o activación desde ubicación/dispositivo inusual `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Panel de PIM Alerts en cero hallazgos críticos abiertos y eventos `Category == "RoleManagement"` en `AuditLogs` `[Verificado MS Learn]`.

### D-05: Control de bajas urgentes e inmediatas (*Emergency Leaver Verification*)
- **Objetivo:** Verificar que las desvinculaciones involuntarias o de alto riesgo notificadas en el día hayan completado la revocación de sesiones, tokens y accesos en menos de 15 minutos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Lifecycle workflows > <Emergency Offboarding Workflow> > Run on demand` `[Verificado MS Learn]`.
- **Rol Responsable:** Lifecycle Workflows Administrator / SOC L1-L2.
- **Procedimiento Paso a Paso:**
  1. Confirmar recepción del evento de baja inmediata desde HRIS/Legal o disparo manual de workflow **Real-time employee termination** `[Verificado MS Learn]`.
  2. Verificar la ejecución secuencial exitosa de las tareas integradas: `Disable user account`, `Revoke all refresh tokens for user`, `Cancel all pending access package assignment requests for user`, `Remove all access package assignments for user`, `Remove users from all groups`, `Remove user from all teams` y `Remove all license assignments from user` `[Verificado MS Learn]`.
  3. Si el empleado saliente era sponsor de agentes IA o invitados B2B, confirmar la ejecución de `Transfer agent identity sponsorships to manager` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Historial de usuario en Lifecycle Workflows con 100 % de tareas de revocación completadas y `accountEnabled == false` `[Verificado MS Learn]`.

### D-06: Supervisión de colas de aprobación condicionadas por riesgo (ID Protection / Insider Risk)
- **Objetivo:** Auditar solicitudes de Access Packages escaladas a aprobadores de seguridad debido a riesgo de identidad medio/alto o señal de Insider Risk Management `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://myaccess.microsoft.com > Approvals` y `https://entra.microsoft.com > Protection > Identity Protection > Risky users` `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Identificar solicitudes enrutadas a la etapa de aprobación de riesgo configurada mediante la integración de **Entra ID Protection** o **Purview Insider Risk Management** en Entitlement Management `[Verificado MS Learn]`.
  2. Consultar en **Entra Copilot chat** el resumen de inicios de sesión riesgosos y actividad reciente del solicitante antes de emitir veredicto `[Verificado MS Learn]`.
  3. Denegar la solicitud y disparar remediación de credenciales si se confirma riesgo no mitigado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Decisión registrada con justificación forense en el historial de aprobación de `My Access` y `AuditLogs` `[Verificado MS Learn]`.

### D-07: Verificación de salud de Custom Task Extensions (Azure Logic Apps)
- **Objetivo:** Asegurar cero fallos de autenticación Managed Identity, throttling o timeouts en las Logic Apps invocadas por Lifecycle Workflows, Entitlement Management y PIM `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Lifecycle workflows > Custom extensions` y `https://portal.azure.com > Logic apps > Runs history` `[Verificado MS Learn]`.
- **Rol Responsable:** Lifecycle Workflows Administrator / Platform Engineer.
- **Procedimiento Paso a Paso:**
  1. Revisar en Azure Monitor / Logic Apps las ejecuciones con estado `Failed` o `TimedOut` de las últimas 24 horas `[Verificado MS Learn]`.
  2. Confirmar que el tiempo de ejecución se mantenga muy por debajo del límite `durationBeforeTimeout` (30 minutos a 3 horas) en tareas de tipo *callback* `[Verificado MS Learn]`.
  3. Validar permisos de Managed Identity sobre sistemas externos conectados (ServiceNow, Jira, Active Directory, cmdb) `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Métricas de ejecución de Azure Logic Apps (`Runs Failed == 0`) y eventos `Category == "Other"` en auditoría de LCW `[Verificado MS Learn]`.

### D-08: Monitoreo de asignaciones de privilegios fuera de banda (Direct Role / Group Bypass)
- **Objetivo:** Detectar y revertir en el día cualquier asignación directa de roles de directorio o membresía a grupos críticos realizada eludiendo Access Packages o PIM `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Entra ID > Monitoring & health > Workbooks > Application role assignment activity` / Sentinel Hunting `[Verificado MS Learn]`.
- **Rol Responsable:** SOC L2 / Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Ejecutar consulta KQL diaria sobre `AuditLogs` buscando operaciones `Add member to role` (fuera de PIM) o asignaciones directas a aplicaciones empresariales Tier-1 no originadas por `EntitlementManagement` `[Verificado MS Learn]`.
  2. Contrastar con el workbook oficial *Application role assignment activity* para identificar cambios realizados directamente por administradores globales o de aplicaciones `[Verificado MS Learn]`.
  3. Revertir la asignación directa no autorizada y migrar al usuario al Access Package o rol elegible PIM correspondiente `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Resultado diario de consulta KQL y ticket de remediación de desvío de gobierno `[Decisión / Propuesta Editorial]`.

---

## 6. Cadencia Operativa Semanal

### S-01: Seguimiento de avance de Access Reviews activas y métricas del Access Review Agent
- **Objetivo:** Prevenir el vencimiento de campañas de recertificación sin respuesta de los revisores y supervisar el razonamiento del **Access Review Agent** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Access reviews` y `Agents > Access Review Agent` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Revisar todas las instancias de Access Reviews en estado `In progress` cuya fecha de cierre ocurra en los próximos 7 días `[Verificado MS Learn]`.
  2. Inspeccionar el mapa de actividad y métricas de 30 días del **Access Review Agent**, validando que los revisores estén interactuando con los resúmenes conversacionales en Microsoft Teams `[Verificado MS Learn]`.
  3. Enviar recordatorios dirigidos o activar delegación de revisión (*delegate review tasks*) cuando un revisor se encuentre de licencia o fuera de oficina `[Verificado MS Learn]`.
- **Evidencia Auditable:** Porcentaje de progreso de revisión >80 % previo a las últimas 48 horas de cierre de campaña `[Decisión / Propuesta Editorial]`.

### S-02: Higiene de invitados B2B inactivos y sin patrocinador (*Inactive & Unsponsored Guests*)
- **Objetivo:** Reducir la superficie de exposición externa identificando huéspedes B2B sin inicio de sesión reciente o huérfanos de sponsor interno `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Dashboard > Inactive guest accounts` y `Lifecycle workflows` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Consultar el informe nativo **Inactive guest accounts** (exclusivo de Entra ID Governance) filtrando invitados sin autenticación en los últimos 60/90 días `[Verificado MS Learn]`.
  2. Revisar las ejecuciones de la tarea LCW `Send email about unsponsored guest removal (Preview)` y atestaciones de sponsors pendientes `[Verificado MS Learn]`.
  3. Confirmar que la política de usuarios externos en Entitlement Management bloquee el inicio de sesión y elimine la cuenta invitada tras 30 días sin asignaciones de Access Packages `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte semanal exportado de invitados inactivos remediados y eventos `Guest user disabled/deleted by lifecycle policy` en `AuditLogs` `[Verificado MS Learn]`.

### S-03: Auditoría de excepciones y conflictos en políticas de Separation of Duties (SoD)
- **Objetivo:** Identificar usuarios con asignaciones preexistentes incompatibles (*Additional access*) y auditar cualquier paquete de excepción SoD `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Access packages > <Package> > Separation of duties` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / GRC Analyst.
- **Procedimiento Paso a Paso:**
  1. Revisar en paquetes críticos (ej. *Desarrollo* vs. *Producción*, *Creación de Proveedores* vs. *Aprobación de Pagos*) la columna **Additional access** en la pestaña `Incompatible access packages` `[Verificado MS Learn]`.
  2. Verificar que toda relación de incompatibilidad que deba operar en ambos sentidos esté configurada bidireccionalmente en ambos paquetes (dado que cada regla en Entra EM es unidireccional por diseño) `[Verificado MS Learn]`.
  3. Auditar los miembros de cualquier paquete dedicado a *override* excepcional de SoD validando vigencia temporal y compensación de controles `[Verificado MS Learn]`.
- **Evidencia Auditable:** CSV descargado de `Incompatible assignments` con 0 solapamientos no aprobados `[Verificado MS Learn]`.

### S-04: Conciliación de Account Discovery y cuentas huérfanas en aplicaciones conectadas
- **Objetivo:** Detectar cuentas locales creadas directamente en aplicaciones SaaS/on-premises que carecen de identidad correlacionada o activa en Microsoft Entra ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Entra ID > Enterprise apps > <App> > Provisioning > Account Discovery` `[Verificado MS Learn]`.
- **Rol Responsable:** Application Administrator / Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Ejecutar o revisar los resultados semanales de **Account Discovery** sobre las aplicaciones empresariales críticas conectadas `[Verificado MS Learn]`.
  2. Clasificar las cuentas no correlacionadas (*unmatched/orphan accounts*) distinguiendo cuentas técnicas legítimas documentadas de cuentas residuales de ex-empleados o altas fuera de proceso `[Verificado MS Learn]`.
  3. Deshabilitar/eliminar cuentas huérfanas no justificadas o vincularlas a un Access Package gobernado `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Inventario semanal de cuentas descubiertas vs. cuentas correlacionadas por aplicación `[Verificado MS Learn]`.

### S-05: Gobierno semanal de identidades de Agentes IA (`Microsoft Entra Agent ID`) y Sponsors
- **Objetivo:** Garantizar que el 100 % de las identidades de agentes creadas desde Copilot Studio, Microsoft Foundry, Azure App Service o Agent 365 posean un sponsor humano activo y paquetes con expiración definida `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Entra ID > Agent ID` y `ID Governance > Entitlement management > Access packages` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / AI Governance Lead.
- **Procedimiento Paso a Paso:**
  1. Enumerar los objetos `agent identity blueprint`, `agent identity` y `agent user` dados de alta en los últimos 7 días `[Verificado MS Learn]`.
  2. Confirmar que cada `agent identity` tenga asignado al menos un **sponsor** humano activo y herede políticas de Conditional Access desde su blueprint `[Verificado MS Learn]`.
  3. Revisar solicitudes de Access Packages realizadas programáticamente por agentes o en su nombre por sponsors (incluyendo permisos OAuth de Microsoft Graph o roles Entra) `[Verificado MS Learn]`.
- **Evidencia Auditable:** Listado de identidades de agentes con 0 agentes sin sponsor humano ni permisos permanentes fuera de paquete/blueprint `[Verificado MS Learn]`.

### S-06: Revisión de rechazos y validaciones de Verified ID y Face Check en Access Packages
- **Objetivo:** Detectar intentos fallidos de verificación de identidad o problemas de usabilidad en paquetes de alta seguridad protegidos con Verified ID `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Access packages > Requests` y `Verified ID > Logs` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / SOC L2.
- **Procedimiento Paso a Paso:**
  1. Revisar las solicitudes de paquetes que exigen **Required Verified IDs** y **Require Face Check** `[Verificado MS Learn]`.
  2. Investigar fallos reiterados de coincidencia biométrica (*Face Check*) sobre una misma cuenta corporativa o externa como posible señal de suplantación durante onboarding remoto o elevación de acceso `[Decisión / Propuesta Editorial]`.
  3. Validar disponibilidad y certificados vigentes de los emisores de **Microsoft Entra Verified ID Network** o socios IDV de **Security Store** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registros de presentación de credenciales verificables y escalamiento SOC ante sospecha de fraude de identidad `[Verificado MS Learn]`.

---

## 7. Cadencia Operativa Mensual

### M-01: Reconciliación FinOps de licenciamiento Entra ID Governance, Step-Up P2, Agent 365 y facturación MAU de Guests
- **Objetivo:** Asegurar el cumplimiento contractual de licencias para todos los miembros gobernados y optimizar el gasto mensual por MAU de invitados B2B en Azure `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Billing > Licenses > All products`, `ID Governance > Dashboard > Guest governance` y Azure Cost Management `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / FinOps Analyst.
- **Procedimiento Paso a Paso:**
  1. Comparar el total de asientos activos de `Microsoft Entra ID Governance` / `Step Up for P2` / `Entra Suite` / `M365 E7` (y `Microsoft Agent 365` si aplica) contra el conteo de miembros únicos gobernados y verificar vigencia del prerrequisito `AAD_PREMIUM_P2` `[Verificado MS Learn]`.
  2. Ejecutar consulta KQL mensual en `AuditLogs` filtrando `TargetUserType == "Guest"` y `GovernanceLicenseFeatureUsed == True` para auditar exactamente qué invitados devengaron un cargo MAU en el mes `[Verificado MS Learn]`.
  3. Verificar si existen organizaciones socias recurrentes que deban integrarse como **Multi-Tenant Organization (MTO)** para evitar cobros MAU innecesarios `[Verificado MS Learn]`.
- **Evidencia Auditable:** Informe mensual de conciliación de licencias y desglose de MAU B2B validado con FinOps `[Decisión / Propuesta Editorial]`.

### M-02: Evaluación de efectividad de recomendaciones ML (*User-to-Group Affiliation* e Inactividad) y Access Review Agent
- **Objetivo:** Medir la reducción de *rubber-stamping* (aprobaciones sin revocaciones) y ajustar el alcance de grupos que superan límites de ML `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Access reviews > Review history` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Analizar las campañas cerradas en el mes comparando decisiones del revisor humano frente a las recomendaciones del sistema (`Deny` por inactividad >30 días o baja afiliación organizacional) `[Verificado MS Learn]`.
  2. Identificar grupos de seguridad con más de **600 miembros** (donde **User-to-Group Affiliation** no está soportado) para segmentarlos en grupos funcionales por unidad de negocio o Access Packages `[Verificado MS Learn]`.
  3. Auditar porcentajes de usuarios sin atributo `manager` poblado en el directorio, corrigiéndolos con RR. HH. para maximizar la precisión del grafo de afiliación ML `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte mensual de tasa de adopción de recomendaciones IA/ML y cobertura del atributo `manager` `[Decisión / Propuesta Editorial]`.

### M-03: Optimización de versiones, plantillas y horarios de Lifecycle Workflows
- **Objetivo:** Ajustar ventanas de ejecución (`1–24 h`), reglas de alcance y nuevas versiones de workflows conforme a cambios organizacionales `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Lifecycle workflows > Workflows > Versions / Workflow settings` `[Verificado MS Learn]`.
- **Rol Responsable:** Lifecycle Workflows Administrator.
- **Procedimiento Paso a Paso:**
  1. Revisar el consumo de cuotas del tenant frente a los límites de servicio (**100 workflows**, **25 tareas/workflow**, **100 custom task extensions**) depurando flujos obsoletos `[Verificado MS Learn]`.
  2. Evaluar si el intervalo global programado (por defecto **3 horas**, ajustable a **1 hora**) cumple los SLAs de onboarding y offboarding del negocio `[Verificado MS Learn]`.
  3. Validar migración ordenada desde disparadores `Time based attribute` clásicos hacia comparaciones relativas (`Time based attribute V2`) donde agregue valor operativo `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro de versiones (`Workflow versions`) y documentación de cambios aprobados en CAB `[Verificado MS Learn]`.

### M-04: Revisión mensual de Auto-Assignment Policies y paquetes sugeridos en My Access
- **Objetivo:** Verificar que las reglas dinámicas basadas en atributos asignen y retiren derechos con exactitud y sin aproximarse al límite de 15.000 asignaciones por política `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Access packages > Policies` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Governance Administrator / Catalog Owners.
- **Procedimiento Paso a Paso:**
  1. Auditar todas las **Auto-assignment policies** verificando que el volumen de asignaciones activas por política permanezca holgadamente bajo el tope de **15.000 asignaciones** `[Verificado MS Learn]`.
  2. Confirmar que la opción de remoción automática al dejar de cumplir la condición de atributos esté activada en el 100 % de las políticas automáticas `[Verificado MS Learn]`.
  3. Revisar las sugerencias de paquetes de acceso (*Suggested access packages*) en `My Access` ocultando paquetes técnicos internos que no deban solicitarse manualmente `[Verificado MS Learn]`.
- **Evidencia Auditable:** Exportación de configuración de políticas automáticas y conteo de asignaciones por política `[Verificado MS Learn]`.

### M-05: Verificación de retención y exportación continua de logs IGA hacia Azure Monitor / Microsoft Sentinel
- **Objetivo:** Garantizar cero pérdida de trazabilidad forense superando el límite nativo de 30 días de retención en el portal de Microsoft Entra `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > Entra ID > Monitoring & health > Diagnostic settings / Workbooks > Archived Log Date Range` `[Verificado MS Learn]`.
- **Rol Responsable:** Platform Engineer / Security Reader.
- **Procedimiento Paso a Paso:**
  1. Verificar en `Diagnostic settings` que `AuditLogs` y `ProvisioningLogs` continúen enviándose sin interrupción al workspace de Log Analytics / Microsoft Sentinel `[Verificado MS Learn]`.
  2. Abrir el workbook oficial **Archived Log Date Range** y **Access Package Activity** confirmando continuidad diaria de ingesta y retención alineada a política regulatoria (ej. 365 días en Analytics/Data Lake) `[Verificado MS Learn]`.
  3. Validar que el conector de Entra ID en Sentinel esté aprovechando correctamente el beneficio de Data Grant de 5 MB/usuario/día de M365 E5 para `AuditLogs` `[Verificado MS Learn]`.
- **Evidencia Auditable:** Captura/consulta de `min(TimeGenerated)` y `max(TimeGenerated)` en `AuditLogs` sin huecos de ingesta `[Verificado MS Learn]`.

---

## 8. Cadencias Trimestral, Semestral y Anual

### T-01 (Trimestral): Campaña integral de recertificación de roles privilegiados (PIM), grupos críticos y agentes IA
- **Objetivo:** Ejecutar y cerrar con aplicación automática (*Auto-apply results to resource*) las revisiones trimestrales de todos los roles de directorio Entra, roles de suscripción Azure, **PIM for Groups** y paquetes de **Microsoft Entra Agent ID** `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Privileged Identity Management > Access reviews` y `ID Governance > Access reviews` `[Verificado MS Learn]`.
- **Rol Responsable:** Privileged Role Administrator / Identity Governance Administrator.
- **Procedimiento Paso a Paso:**
  1. Verificar el disparo automático de las campañas trimestrales recurrentes con `If reviewers don't respond == Remove access` y `Auto-apply results to resource == Enabled` `[Verificado MS Learn]`.
  2. Asegurar que ningún administrador revise su propio acceso privilegiado (prohibir *Self-review* en Tier-0/Tier-1) `[Decisión / Propuesta Editorial]`.
  3. Auditar al cierre de la ventana (14 días recomendados) la revocación efectiva de todos los usuarios, invitados y agentes IA denegados o no respondidos `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Reportes PDF/CSV descargados de `Access reviews > History` firmados para cumplimiento SOX / ISO 27001 / NIST CSF 2.0 `[Verificado MS Learn]`.

### T-02 (Trimestral): Incorporación (*Onboarding*) de nuevas aplicaciones de negocio al catálogo gobernado y retiro de asignaciones directas
- **Objetivo:** Expandir progresivamente la cobertura de Entitlement Management y SCIM/Account Discovery sobre el portafolio de aplicaciones SaaS y on-premises `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Catalogs > Resources` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / Application Administrator / Catalog Owners.
- **Procedimiento Paso a Paso:**
  1. Identificar nuevas aplicaciones Enterprise registradas en el trimestre y clasificarlas por criticidad de datos `[Verificado MS Learn]`.
  2. Integrar aprovisionamiento automático (SCIM 2.0, conector on-premises LDAP/SQL/REST o integración **SAP Cloud IAG**) e incorporar sus roles de aplicación en Access Packages con revisión periódica `[Verificado MS Learn]`.
  3. Migrar los usuarios existentes de la aplicación al modelo gobernado revocando asignaciones estáticas previas `[Verificado MS Learn]`.
- **Evidencia Auditable:** Porcentaje actualizado de aplicaciones Tier-1/Tier-2 bajo Entitlement Management `[Decisión / Propuesta Editorial]`.

### SM-01 (Semestral): Revisión arquitectónica de delegación de Catálogos, Connected Organizations y matrices SoD
- **Objetivo:** Recertificar la vigencia de todas las organizaciones externas conectadas B2B, los roles delegados (`Catalog creator`, `Catalog owner`, `Access package manager`) y la matriz corporativa de incompatibilidades SoD `[Verificado MS Learn]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Connected organizations / Settings / Catalogs` `[Verificado MS Learn]`.
- **Rol Responsable:** Identity Architect / CISO / GRC Lead.
- **Procedimiento Paso a Paso:**
  1. Revisar las **Connected organizations** eliminando proveedores cuyos contratos hayan finalizado y auditando sus sponsors internos y externos `[Verificado MS Learn]`.
  2. Ejecutar **Catalog Access Reviews** y validar la lista de usuarios delegados en roles administrativos de Entitlement Management `[Verificado MS Learn]`.
  3. Contrastar con Auditoría Interna y Finanzas la matriz de riesgos de negocio para añadir nuevas reglas bidireccionales de **Separation of Duties** `[Verificado MS Learn]`.
- **Evidencia Auditable:** Acta semestral firmada por IAM, GRC y Compras/Legal con inventario depurado de Connected Organizations y matriz SoD `[Decisión / Propuesta Editorial]`.

### A-01 (Anual): Simulacro integral de resiliencia IGA, caducidad de licencias y auditoría extremo a extremo JML
- **Objetivo:** Validar en entorno de preproducción/piloto los escenarios de fallo catastrófico (interrupción HRIS, fallo de Logic Apps, riesgo de expiración de licencias P2/Governance) y auditar el modelo completo frente a NIST CSF 2.0 `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta Exacta:** `https://entra.microsoft.com > ID Governance` y repositorio IaC (Microsoft Graph PowerShell / Terraform / Maester) `[Verificado MS Learn]`.
- **Rol Responsable:** CISO / Identity Architect / Internal Audit.
- **Procedimiento Paso a Paso:**
  1. Ejecutar pruebas automatizadas de postura con **Maester** y **Zero Trust Assessment** verificando controles de PIM, cuentas de emergencia (*break-glass*), Conditional Access y gobierno de acceso `[Verificado MS Learn]`.
  2. Exportar mediante `Microsoft.Graph.Identity.Governance` el respaldo documental completo de definiciones de workflows, catálogos, paquetes, políticas y configuraciones PIM (mitigando el impacto documentado ante eventual expiración accidental de suscripción, donde las asignaciones elegibles PIM y revisiones activas se eliminan y las asignaciones activas temporales pasan a permanentes) `[Verificado MS Learn]`.
  3. Realizar un muestreo forense anual de 30 altas, 30 movimientos y 30 bajas verificando cumplimiento de SLA minuto a minuto en Log Analytics `[Decisión / Propuesta Editorial]`.
- **Evidencia Auditable:** Informe anual de auditoría IGA, backup JSON de configuraciones Graph y plan de mejora continua aprobado por el CISO `[Decisión / Propuesta Editorial]`.

---

## 9. Operaciones Ad-Hoc y Playbooks de Respuesta a Incidentes / Eventos Críticos

### AH-01: Desvinculación Hostil o Compromiso Confirmado de Identidad Privilegiada / Empleado Crítico
- **Disparador:** Notificación urgente de RR. HH./Legal por despido hostil, alerta crítica de Purview Insider Risk Management o incidente confirmado de robo de sesión/credenciales en Microsoft Defender XDR `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com > ID Governance > Lifecycle workflows` y `Privileged Identity Management` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Ejecutar inmediatamente **Run on demand** del workflow de terminación inmediata sobre el usuario afectado (recordando que `Run on demand` ejecuta las tareas sin evaluar las condiciones de alcance regulares) `[Verificado MS Learn]`.
  2. Confirmar la ejecución instantánea de `Disable user account`, `Revoke all refresh tokens for user`, `Remove all access package assignments for user`, `Cancel all pending access package assignment requests for user` y `Remove users from all groups` `[Verificado MS Learn]`.
  3. En **PIM**, remover cualquier asignación elegible o activa en roles de Entra ID, Azure RBAC y PIM for Groups `[Verificado MS Learn]`.
  4. Si el usuario poseía identidades **Microsoft Entra Agent ID** bajo su patrocinio o propiedad, transferir el patrocinio al manager (`Transfer agent identity sponsorships to manager`) y auditar/deshabilitar los agentes creados por dicho usuario desde `myaccount.microsoft.com` o el centro de administración de Entra `[Verificado MS Learn]`.
- **Evidencia Auditable:** Expediente de incidente en Defender/Sentinel vinculado a los IDs de correlación de `AuditLogs` de LCW, EM y PIM `[Verificado MS Learn]`.

### AH-02: Revocación Masiva de Emergencia de un Agente IA o Clase de Agentes (`Agent Identity Blueprint Kill-Switch`)
- **Disparador:** Comportamiento anómalo, acceso excesivo a datos sensibles o detección de prompt injection/abuso OAuth por parte de una instancia o familia de agentes IA `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Entra ID > Agent ID` y `ID Governance > Entitlement management > Access packages` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Identificar el `agent identity` específico o el `agent identity blueprint` padre involucrado en el incidente `[Verificado MS Learn]`.
  2. Si el fallo afecta a toda una clase de agentes, aplicar bloqueo en Conditional Access o revocar permisos heredables a nivel del **agent identity blueprint** para contener en una sola operación todas las instancias actuales y futuras `[Verificado MS Learn]`.
  3. Remover de inmediato las asignaciones activas de Access Packages del `agent identity` / `agent user` (revocando membresías de grupos, permisos OAuth Graph y roles Entra) `[Verificado MS Learn]`.
  4. Notificar al sponsor humano registrado y registrar lección aprendida antes de cualquier reactivación `[Verificado MS Learn]`.
- **Evidencia Auditable:** Evento de deshabilitación/revocación en `AuditLogs` sobre el objeto de agente y su blueprint `[Verificado MS Learn]`.

### AH-03: Desconexión de Emergencia de Proveedor / Socio Externo Comprometido (*Supply Chain B2B Cutoff*)
- **Disparador:** Brecha de seguridad notificada en un proveedor externo o rescisión contractual inmediata de una **Connected Organization** `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com > ID Governance > Entitlement management > Connected organizations / Access packages` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Localizar la **Connected organization** del proveedor afectado e identificar todos los Access Packages cuyas políticas admiten solicitudes desde dicho dominio/tenant `[Verificado MS Learn]`.
  2. Deshabilitar o eliminar las políticas de solicitud externas para esa organización conectada y remover todas las asignaciones entregadas (`Delivered`) de usuarios pertenecientes a ese proveedor `[Verificado MS Learn]`.
  3. Ejecutar bloqueo de inicio de sesión y revocación de refresh tokens sobre todas las cuentas `Guest` asociadas al dominio externo comprometido `[Verificado MS Learn]`.
  4. Lanzar una Access Review extraordinaria de emergencia sobre cualquier grupo colaborativo M365 o sitio SharePoint donde dicho proveedor haya participado `[Verificado MS Learn]`.
- **Evidencia Auditable:** Cero asignaciones `Delivered` y cero sesiones activas para usuarios del tenant externo afectado `[Verificado MS Learn]`.

### AH-04: Incorporación Masiva por Fusión o Adquisición (M&A) vía MTO y API-Driven Provisioning
- **Disparador:** Integración acelerada de cientos o miles de colaboradores provenientes de una empresa adquirida `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Entra ID > External Identities > Cross-tenant synchronization` y `Enterprise apps > API-driven provisioning` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Configurar relación **Multi-Tenant Organization (MTO)** y **Cross-tenant synchronization** (incluyendo sincronización de grupos habilitada por Entra ID Governance) para evitar cargos MAU de huéspedes entre tenants del mismo grupo empresarial `[Verificado MS Learn]`.
  2. Para empleados que migran directamente al directorio corporativo sin conector Workday/SuccessFactors unificado aún, utilizar **API-driven inbound provisioning** (`/bulkUpload` hasta 300.000 registros/24h) con reglas de mapeo normalizadas `[Verificado MS Learn]`.
  3. Habilitar **Auto-assignment policies** en Entitlement Management basadas en `companyName` / `department` para otorgar acceso día-1 trazable y revocable `[Verificado MS Learn]`.
- **Evidencia Auditable:** Reporte de aprovisionamiento `/bulkUpload` exitoso y asignaciones automáticas auditadas en `AuditLogs` `[Verificado MS Learn]`.

### AH-05: Contención ante Cuarentena o Corrupción Masiva de Datos desde HRIS (*HR Feed Poisoning / Mass Termination Bug*)
- **Disparador:** Error de carga en RR. HH. que marca accidentalmente a cientos de empleados activos con fecha de baja hoy o altera masivamente departamentos `[Decisión / Propuesta Editorial]`.
- **Consola y Ruta:** `https://entra.microsoft.com > Entra ID > Enterprise apps > <HR App> > Provisioning` y `ID Governance > Lifecycle workflows` `[Verificado MS Learn]`.
- **Secuencia Operativa Numerada:**
  1. Pausar de inmediato (`Stop provisioning`) el job de **HR-driven inbound provisioning** y deshabilitar temporalmente el `Schedule` de los Lifecycle Workflows de categoría **Leaver** y **Mover** afectados `[Verificado MS Learn]`.
  2. Auditar en `AADProvisioningLogs` y `Workflow history` la lista exacta de cuentas alcanzadas antes de la pausa `[Verificado MS Learn]`.
  3. Una vez corregido el archivo/tabla en Workday o SuccessFactors, ejecutar workflow de restablecimiento on-demand (`Enable user account`, reasignación de paquetes y licencias) para los usuarios impactados antes de reanudar la programación automática `[Verificado MS Learn]`.
- **Evidencia Auditable:** Registro cronológico de pausa/reanudación en `AuditLogs` y validación 100 % de cuentas restauradas `[Verificado MS Learn]`.

---

## 10. Consultas Técnicas, Telemetría y Verificación de Uso

### 10.1 Catálogo de Consultas KQL y Microsoft Graph PowerShell

#### Consulta 1 (KQL — Log Analytics / Sentinel): Auditoría de modificaciones en políticas de Entitlement Management que omiten aprobación
Detecta cualquier creación o edición de política de asignación de Access Package donde se haya desactivado el requisito de aprobación (`IsApprovalRequiredForAdd == False`) `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Categoría EntitlementManagement)
AuditLogs
| where TimeGenerated > ago(30d)
| where Category == "EntitlementManagement" and Result == "success"
| where AADOperationType in ("CreateEntitlementGrantPolicy", "UpdateEntitlementGrantPolicy")
| mv-expand TargetResources
| where tostring(TargetResources.type) == "AccessPackageAssignmentPolicy"
| extend PolicyId = tostring(TargetResources.id), PolicyName = tostring(TargetResources.displayName)
| mv-expand ModifiedProp = TargetResources.modifiedProperties
| where tostring(ModifiedProp.displayName) == "IsApprovalRequiredForAdd"
    and tostring(ModifiedProp.newValue) has "False"
| project TimeGenerated, OperationName, InitiatedByUser = tostring(InitiatedBy.user.userPrincipalName), PolicyName, PolicyId
| order by TimeGenerated desc
```

#### Consulta 2 (KQL — Log Analytics / Sentinel): Supervisión de fallos en ejecuciones y tareas de Lifecycle Workflows (JML)
Identifica usuarios y tareas específicas con fallos de procesamiento en flujos Joiner, Mover o Leaver `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Servicio Lifecycle Workflows)
AuditLogs
| where TimeGenerated > ago(7d)
| where LoggedByService == "Lifecycle Workflows"
| where Category in ("WorkflowManagement", "TaskManagement", "Other")
| where Result != "success"
| mv-expand TargetResources
| project TimeGenerated, Category, OperationName, Result, ResultReason,
    TargetDisplayName = tostring(TargetResources.displayName),
    TargetId = tostring(TargetResources.id),
    CorrelationId
| order by TimeGenerated desc
```

#### Consulta 3 (KQL — Log Analytics / Sentinel): Control FinOps de eventos facturables MAU para Guests B2B en Entra ID Governance
Enumera los invitados únicos (`userType == Guest`) que utilizaron características exclusivas de Entra ID Governance en los últimos 30 días (`GovernanceLicenseFeatureUsed == True`), permitiendo proyectar con exactitud la factura mensual MAU `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Propiedades adicionales de facturación Guest IGA)
AuditLogs
| where TimeGenerated > ago(30d)
| mv-expand AdditionalDetails
| where tostring(AdditionalDetails.key) == "GovernanceLicenseFeatureUsed"
    and tostring(AdditionalDetails.value) =~ "True"
| mv-expand TargetResources
| extend TargetId = tostring(TargetResources.id), TargetUPN = tostring(TargetResources.userPrincipalName)
| summarize EventosGobernados = count(), Operaciones = make_set(OperationName, 10), PrimeraAccion = min(TimeGenerated)
    by TargetId, TargetUPN
| order by EventosGobernados desc
```

#### Consulta 4 (KQL — Log Analytics / Sentinel): Trazabilidad de resultados y revocaciones en campañas de Access Reviews
Resume decisiones aplicadas, denegaciones y cierres de revisiones de acceso para evidencia de cumplimiento `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Servicio Access Reviews)
AuditLogs
| where TimeGenerated > ago(90d)
| where LoggedByService == "Access Reviews" or Category == "AccessReviews"
| summarize TotalEventos = count(), Exitosos = countif(Result == "success"), Fallidos = countif(Result != "success")
    by OperationName, bin(TimeGenerated, 7d)
| order by TimeGenerated desc
```

#### Consulta 5 (KQL — Log Analytics / Sentinel): Detección de asignaciones privilegiadas permanentes creadas fuera de PIM
Alerta cuando un rol de directorio se asigna directamente de forma permanente eludiendo flujos elegibles de Privileged Identity Management `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AuditLogs (Categoría RoleManagement)
AuditLogs
| where TimeGenerated > ago(7d)
| where Category == "RoleManagement"
| where OperationName has "Add member to role" and OperationName !has "PIM" and LoggedByService != "PIM"
| extend Actor = coalesce(tostring(InitiatedBy.user.userPrincipalName), tostring(InitiatedBy.app.displayName))
| mv-expand TargetResources
| project TimeGenerated, OperationName, Actor, Target = tostring(TargetResources.userPrincipalName), Result
| order by TimeGenerated desc
```

#### Consulta 6 (KQL — Log Analytics / Sentinel): Monitoreo de errores en HR Inbound Provisioning y conectores SCIM
Rastrea fallos de aprovisionamiento entrante desde Workday/SuccessFactors/API o saliente hacia apps SaaS `[Verificado MS Learn]`.

```kql
// Plataforma: Azure Monitor Log Analytics / Microsoft Sentinel
// Tabla: AADProvisioningLogs
AADProvisioningLogs
| where TimeGenerated > ago(24h)
| where ResultType != "Success" and ResultType != "Skipped"
| summarize Fallos = count(), EjemplosError = make_set(ResultDescription, 5)
    by ServicePrincipalName, Action, ResultType
| order by Fallos desc
```

#### Consulta 7 (Microsoft Graph PowerShell): Verificación de conflictos existentes de Separation of Duties entre dos Access Packages
Script oficial basado en `Microsoft.Graph.Identity.Governance` para detectar identidades que ya poseen asignaciones entregadas (`Delivered`) simultáneas en dos paquetes incompatibles `[Verificado MS Learn]`.

```powershell
# Módulo requerido: Microsoft.Graph.Identity.Governance (v2.1.0+)
Connect-MgGraph -Scopes "EntitlementManagement.Read.All"

$PackageProdId = "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
$PackageDevId  = "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"

$AssignProd = @(Get-MgEntitlementManagementAssignment -Filter "accessPackage/id eq '$PackageProdId' and state eq 'Delivered'" -ExpandProperty target -All)
$AssignDev  = @(Get-MgEntitlementManagementAssignment -Filter "accessPackage/id eq '$PackageDevId' and state eq 'Delivered'" -ExpandProperty target -All)

$IndexDev = @{}
foreach ($d in $AssignDev) {
    if ($null -ne $d.Target -and $null -ne $d.Target.Id) { $IndexDev[$d.Target.Id] = $d }
}
foreach ($p in $AssignProd) {
    if ($null -ne $p.Target -and $null -ne $p.Target.Id -and $IndexDev.ContainsKey($p.Target.Id)) {
        [PSCustomObject]@{ TargetId = $p.Target.Id; Email = $p.Target.Email; Conflicto = "Prod + Dev" }
    }
}
```

### 10.2 Tabla de Verificación Operativa ("Proof of Life")

| Control / Capacidad | Fuente Primaria de Verificación | Condición de Salud ("Proof of Life") | Frecuencia | Estado |
| --- | --- | --- | --- | --- |
| **Licencias y Prerrequisito P2** | `entra.microsoft.com > Billing > Licenses > Licensed features` | Plan `Microsoft Entra ID Governance` activo + `AAD_PREMIUM_P2` vigente + suscripción Azure vinculada para Guests. | Mensual | `[Verificado MS Learn]` |
| **Lifecycle Workflows Activos** | `AuditLogs` (`LoggedByService == "Lifecycle Workflows"`) | Eventos regulares de ejecución programada con `Result == "success"` y 0 fallos Leaver >4 h. | Diaria | `[Verificado MS Learn]` |
| **Entitlement Management & SoD** | `AuditLogs` (`Category == "EntitlementManagement"`) + Workbook *Access Package Activity* | Solicitudes en estado `Delivered`, `DeliveryFailed == 0` sin reprocesar y `Additional access == 0` en reglas SoD. | Semanal | `[Verificado MS Learn]` |
| **Access Reviews + ML / Agent** | `ID Governance > Access reviews > History` | 100 % de campañas trimestrales cerradas a tiempo con `Auto-apply` ejecutado y decisión registrada. | Trimestral | `[Verificado MS Learn]` |
| **Retención Extendida en SIEM** | Workbook *Archived Log Date Range* en Log Analytics | Ingesta continua de `AuditLogs` y `AADProvisioningLogs` con retención >= 365 días en Sentinel / Log Analytics. | Mensual | `[Verificado MS Learn]` |

---

## 11. Indicadores Clave de Desempeño (KPIs) y Modelo de Madurez Operacional

### 11.1 Tabla Maestra de KPIs Operacionales y Ejecutivos

| ID | Nombre del KPI | Fórmula de Cálculo | Meta Sugerida | Frecuencia | Audiencia | Clasificación |
| --- | --- | --- | --- | --- | --- | --- |
| **KPI-01** | **SLA de Revocación Integral Leaver (Offboarding Time-to-Revoke)** | `Tiempo entre marca de baja efectiva en HRIS/disparo urgente y finalización exitosa de tareas de deshabilitación + revocación de refresh tokens en LCW` | `< 15 min` (baja urgente) / `< 3 h` (baja programada) | Diaria / Mensual | CISO, SOC Manager, Internal Audit | `[Decisión / Propuesta Editorial]` |
| **KPI-02** | **Tasa de Éxito de Onboarding Día-1 sin Intervención Manual** | `(Altas Joiner procesadas automáticamente con TAP + Access Packages base sin tickets de soporte / Total de altas en el mes) * 100` | `>= 98 %` | Mensual | CIO, Identity Lead, RR. HH. | `[Decisión / Propuesta Editorial]` |
| **KPI-03** | **Tasa de Completitud Efectiva de Access Reviews (No Auto-Default)** | `(Decisiones explícitamente revisadas por humanos asistidos por ML o Access Review Agent antes del cierre / Total de ítems en revisión) * 100` | `>= 95 %` | Trimestral | CISO, GRC, Dueños de Negocio | `[Decisión / Propuesta Editorial]` |
| **KPI-04** | **Índice de Cero Privilegios Permanentes (ZSP Ratio en Roles Críticos)** | `(Asignaciones elegibles en PIM sobre roles Entra críticos / Total de asignaciones elegibles + permanentes excluyendo 2 cuentas break-glass) * 100` | `100 %` | Semanal | CISO, Privileged Role Admin | `[Decisión / Propuesta Editorial]` |
| **KPI-05** | **Cobertura de Aplicaciones Empresariales bajo Entitlement Management** | `(Aplicaciones Tier-1 y Tier-2 gobernadas en Access Packages con aprovisionamiento automático / Total de aplicaciones Tier-1 y Tier-2) * 100` | `>= 90 %` | Trimestral | Identity Architect, GRC | `[Decisión / Propuesta Editorial]` |
| **KPI-06** | **Tasa de Cuentas Huérfanas Remediadas (Account Discovery Hygiene)** | `(Cuentas no correlacionadas detectadas por Account Discovery cerradas o vinculadas en <= 7 días / Total de cuentas no correlacionadas detectadas) * 100` | `>= 99 %` | Semanal | Identity Governance Admin, Audit | `[Decisión / Propuesta Editorial]` |
| **KPI-07** | **Cobertura de Patrocinio Humano en Guests B2B y Agentes IA** | `(Identidades Guest gobernadas + Microsoft Entra Agent IDs con sponsor humano activo y expiración vigente / Total de Guests + Agent IDs) * 100` | `100 %` | Semanal | CISO, AI Governance Lead | `[Decisión / Propuesta Editorial]` |
| **KPI-08** | **Cumplimiento de Separation of Duties (SoD Zero-Conflict Rate)** | `(1 - (Usuarios con asignaciones incompatibles simultáneas no exentas / Total de usuarios con Access Packages)) * 100` | `100 %` | Semanal | GRC, CFO / SOX Compliance | `[Decisión / Propuesta Editorial]` |

### 11.2 Modelo de Madurez Operacional (Niveles 1 a 5) `[Decisión / Propuesta Editorial]`

| Nivel | Estadio | Caracterización Operativa en Microsoft Entra ID Governance |
| --- | --- | --- |
| **Nivel 1** | **Inicial / Ad-Hoc** | Altas y bajas gestionadas por tickets manuales; grupos estáticos sin expiración; roles administrativos permanentes; retención de logs limitada a los 30 días por defecto del portal Entra. |
| **Nivel 2** | **Base P2 (Repetible)** | Uso exclusivo de capacidades base de Entra ID P2: PIM habilitado para Global Admins, primeros Access Packages manuales y Access Reviews anuales básicos sin automatización HRIS ni Lifecycle Workflows. |
| **Nivel 3** | **Definido y Automatizado** | Despliegue de **Entra ID Governance Step-Up**: HR-driven inbound provisioning activo, Lifecycle Workflows JML en producción, delegación por catálogos a unidades de negocio, reglas SoD y exportación continua de `AuditLogs` a Sentinel/Log Analytics. |
| **Nivel 4** | **Gestionado por Riesgo e IA** | **Auto-assignment policies**, **Verified ID + Face Check** en paquetes sensibles, aprobaciones condicionadas por **Entra ID Protection** y **Purview Insider Risk**, **Account Discovery** semanal, recomendaciones ML **User-to-Group Affiliation** y **Access Review Agent** en Teams. |
| **Nivel 5** | **Optimizado y Agéntico (Frontier)** | Gobierno unificado humano + no humano con **Microsoft Entra Agent ID** / **Agent 365**, blueprints con Conditional Access heredado, transferencia automática de sponsors, gestión como código en Graph/IaC con pruebas diarias **Maester** y 0 privilegios permanentes. |

---

## 12. Mapeo de Auditoría a NIST CSF 2.0 y MITRE ATT&CK

El siguiente mapeo vincula capacidades verificadas de Microsoft Entra ID Governance con las **seis funciones** del marco **NIST Cybersecurity Framework (CSF) 2.0 (CSWP 29)** y tácticas de **MITRE ATT&CK v18** `[Decisión / Propuesta Editorial]`.

| Función NIST CSF 2.0 | Subcategoría Oficial | Descripción del Resultado Normativo | Capacidad Habilitadora en Entra ID Governance | Mitigación MITRE ATT&CK | Evidencia Auditable Reproducible |
| --- | --- | --- | --- | --- | --- |
| **GOVERN (GV)** | `GV.RR-02` | Los roles, responsabilidades y autoridades de ciberseguridad están establecidos, comunicados y aplicados. | Delegación granular por catálogos (`Catalog owner`, `Access package manager`), matriz RBAC Entra con PIM y **Separation of Duties (SoD)** en paquetes. | `T1078.004` (Valid Accounts: Cloud Accounts) | Matriz de roles delegados exportada por Graph y reporte de `Incompatible assignments == 0`. |
| **GOVERN (GV)** | `GV.SC-07` | Los riesgos planteados por un proveedor, sus productos y sus servicios se entienden, registran, priorizan, evalúan y monitorean a lo largo de la relación. | Gobierno de **Connected Organizations**, políticas de expiración B2B, *Mark guest as governed*, facturación/trazabilidad MAU y desconexión centralizada de terceros. | `T1199` (Trusted Relationship) | Inventario auditado de Connected Organizations y decisiones de Access Reviews sobre usuarios `Guest`. |
| **IDENTIFY (ID)** | `ID.AM-05` | Los recursos se priorizan según su clasificación, criticidad, valor comercial e impacto en la misión. | Organización de aplicaciones Tier-1/Tier-2, grupos, sitios SPO, roles SAP IAG y permisos API en catálogos segmentados y descubrimiento con **Account Discovery**. | `T1087.004` (Account Discovery: Cloud Account) | Inventario de catálogos EM y reportes semanales de **Account Discovery** sin cuentas huérfanas. |
| **IDENTIFY (ID)** | `ID.RA-01` | Las vulnerabilidades en activos y configuraciones de acceso se identifican, validan y registran. | **Inactive guest insights**, recomendaciones ML **User-to-Group Affiliation**, **Access Review Agent** y pruebas continuas de postura con **Maester**. | `T1098` (Account Manipulation) | Reportes de anomalías de afiliación organizacional e informes automatizados de Maester. |
| **PROTECT (PR)** | `PR.AA-01` | Las identidades y credenciales para usuarios, servicios y hardware autorizados son gestionadas por la organización. | **HR-driven / API-driven inbound provisioning**, **Lifecycle Workflows** (emisión de TAP en Joiner, revocación en Leaver) y **Microsoft Entra Agent ID** con sponsors humanos. | `T1136.003` (Create Account: Cloud Account) | Logs en `AADProvisioningLogs`, `Workflow history` y registro de sponsors de identidades de agentes. |
| **PROTECT (PR)** | `PR.AA-02` | Las identidades son verificadas (*identity proofing*) y vinculadas a credenciales según el contexto de las interacciones. | Requisito obligatorio de **Microsoft Entra Verified ID** (red Entra o socios IDV de Security Store) + verificación biométrica **Face Check** al solicitar Access Packages críticos. | `T1656` (Impersonation) | Política de Access Package con `Required Verified IDs` + `Face Check` activo y trazas de presentación QR. |
| **PROTECT (PR)** | `PR.AA-05` | Los permisos de acceso, derechos y autorizaciones se definen en políticas, se gestionan, aplican y revisan incorporando mínimo privilegio y separación de funciones. | **Entitlement Management**, **PIM** (Zero Standing Privileges), **Access Reviews** periódicos con auto-aplicación y **Auto-assignment policies**. | `T1078` (Valid Accounts), `T1484` (Domain/Tenant Policy Modification) | Historial trimestral de Access Reviews cerradas al 100 % y configuración de roles elegibles PIM. |
| **DETECT (DE)** | `DE.CM-03` | Las actividades del personal y el uso de tecnología se monitorean para encontrar eventos potencialmente adversos. | Alertas nativas de **PIM**, monitoreo de cambios fuera de banda en *Application role assignment activity* y evaluación de riesgo en solicitudes con **ID Protection / Insider Risk**. | `T1098.003` (Additional Cloud Roles) | Consultas KQL programadas en Microsoft Sentinel sobre `AuditLogs` (`EntitlementManagement`, `RoleManagement`). |
| **DETECT (DE)** | `DE.AE-02` | Los eventos potencialmente adversos se analizan para comprender mejor las actividades asociadas. | Correlación en Microsoft Sentinel entre ejecuciones fallidas de **Lifecycle Workflows**, solicitudes de acceso denegadas por riesgo e inicios de sesión sospechosos. | `T1550.001` (Application Access Token) | Incidentes enriquecidos en `security.microsoft.com` correlacionando `AuditLogs` y `SigninLogs`. |
| **RESPOND (RS)** | `RS.MI-01` | Los incidentes son contenidos para evitar la propagación del impacto. | Ejecución **Run on demand** de workflows de terminación inmediata (deshabilitación de cuenta, revocación de refresh tokens, remoción total de paquetes/grupos) y kill-switch de **Agent Blueprints**. | `T1531` (Account Access Removal - defensivo sobre atacante) | Trazas de ejecución en <15 minutos en `AuditLogs` (`LoggedByService == "Lifecycle Workflows"`). |
| **RESPOND (RS)** | `RS.AN-03` | Se realiza análisis forense para establecer qué ocurrió durante un incidente y su causa raíz. | Archivo histórico inmutable >365 días de `AuditLogs` y `AADProvisioningLogs` en Azure Monitor / Sentinel Data Lake reconstruyendo quién solicitó, aprobó y entregó cada derecho. | `T1078.004` (Cloud Accounts) | Workbook *Access Package Activity* y línea de tiempo KQL completa por `TargetId` e `InitiatedBy`. |
| **RECOVER (RC)** | `RC.RP-03` | La integridad de las copias de seguridad y otros activos de restauración se verifica antes de utilizarlos para la recuperación. | Respaldo declarativo de políticas EM, workflows LCW y configuraciones PIM vía Microsoft Graph / **Entra Backup and Recovery** y reaprovisionamiento limpio post-incidente. | `T1490` (Inhibit System Recovery) | Artefactos JSON versionados en Git y validación exitosa de restauración controlada en simulacro anual `A-01`. |

---

## 13. Habilitación y Ruta de Formación por Rol

| Rol Operativo | Ruta Oficial Microsoft Learn / Credenciales | Recursos Avanzados Ninja, Comunidad MVP y Laboratorios Prácticos | Cadencia de Reentrenamiento |
| --- | --- | --- | --- |
| **Identity Governance Administrator & Identity Architect** | - **Exam SC-300:** *Microsoft Identity and Access Administrator* `[Verificado MS Learn]`<br>- Learning Path: *Implement an identity management solution using Microsoft Entra ID* `[Verificado MS Learn]`<br>- Applied Skills: *Get started with identities and access using Microsoft Entra* `[Verificado MS Learn]` | - *TechLab: Entra Suite for Frontier Transformation* (`github.com/microsoft/TechLab-Entra-Suite-for-Frontier-Transformation`) `[Verificado MS Learn]`<br>- Newsletter semanal *Entra.News* (Merill Fernando, Microsoft PM) y automatización de postura con **Maester** (`maester.dev`) `[Verificado MS Learn]` | Trimestral + seguimiento semanal de `entra/fundamentals/whats-new` |
| **Lifecycle Workflows & Provisioning Engineer** | - Módulos Learn de *Plan cloud HR to Microsoft Entra user provisioning*, *Lifecycle Workflows* y *Custom Task Extensions with Azure Logic Apps* `[Verificado MS Learn]` | - Prácticas con el módulo PowerShell `Microsoft.Graph.Identity.Governance` y plantillas de API-driven inbound provisioning (`/bulkUpload`) `[Verificado MS Learn]` | Semestral |
| **Privileged Role Admin & SOC L2/L3** | - Documentación oficial de *Microsoft Entra Privileged Identity Management (PIM)*, *Securing privileged access* y *Security Copilot in Microsoft Entra* `[Verificado MS Learn]` | - Investigación avanzada de bypasses y gobernanza de tokens/roles por MVPs (Fabian Bader — *Cloudbrothers*, Thomas Naunheim — *cloud-architekt.net*, Nathan McNulty) `[Verificado MS Learn]` | Trimestral |
| **Catalog Owners, Managers & Agent Sponsors** | - Guías interactivas de **My Access** (`myaccess.microsoft.com`), delegación de aprobaciones, uso del **Access Review Agent** en Microsoft Teams y administración de agentes en **My Account** (`myaccount.microsoft.com`) `[Verificado MS Learn]` | - Cápsulas internas de 20 minutos enfocadas en prevención de *rubber-stamping*, validación de claims **Verified ID** y responsabilidad del sponsor sobre agentes IA `[Decisión / Propuesta Editorial]` | Semestral |

---

## 14. Registro de Revalidación Técnica (Noviembre 2026) y Decisiones Editoriales

### 14.1 Hallazgos y Validaciones Técnicas frente a Microsoft Learn (`2026-11-11`)

| # | Área Validada | Hallazgo Técnico Verificado en Microsoft Learn (Corte Noviembre 2026) | Impacto en la Guía Operacional |
| --- | --- | --- | --- |
| **1** | **Congelamiento funcional de IGA en Entra ID P2** | `licensing-fundamentals.md` (actualizado oct-2026) confirma que las funciones GA previas en Entra ID P2 se mantienen, pero **no se añadirán nuevas capacidades IGA al SKU P2**; clientes M365 E5 requieren **Step-Up for P2**, **Entra Suite** o **M365 E7** `[Verificado MS Learn]`. | Reflejado en Portada, Sección 2.2 y JSON (`relacionM365E5`). |
| **2** | **Límite real de Lifecycle Workflows (100 vs. 50) y V2 Triggers** | `governance-service-limits.md` y `what-are-lifecycle-workflows.md` confirman la ampliación a **100 workflows por tenant**, **25 tareas/workflow** y **100 custom task extensions** (mientras una sección heredada de `licensing-fundamentals.md` aún cita 50 workflows); además coexisten temporalmente `Time based attribute` y `Time based attribute V2 (Preview)` con comparaciones relativas `[Verificado MS Learn]`. | Documentado el límite autoritativo de 100 workflows y advertida la discrepancia menor de texto en Learn y el comportamiento sin *catch-up* de 3 días en V2 Preview. |
| **3** | **Separación de Funciones (SoD) en P2 vs. Controles Avanzados EM** | La tabla oficial de licencias confirma que `Separation of duties` básico (paquetes y grupos incompatibles, unidireccionales por regla) opera desde P2, mientras **Verified ID + Face Check**, **Auto-assignment policies**, **Custom Extensions**, aprobaciones por **ID Protection / Insider Risk**, **Entra Roles (Preview)** y **SAP IAG (Preview)** exigen Entra ID Governance `[Verificado MS Learn]`. | Precisado quirúrgicamente en la matriz comparativa 2.2 y en las rutinas `S-03` y `S-06`. |
| **4** | **Gobierno de Agentes IA (`Entra Agent ID` + `Agent 365` / `M365 E7`)** | `agent-id-governance-overview.md` (actualizado el `2026-11-07`) introduce el gobierno formal de `agent identity blueprint`, `agent identity` y `agent user` con **human sponsor** obligatorio, transferencia automática al manager en LCW y asignación de Access Packages (licenciado con **Microsoft Agent 365** sobre P1/E3 o **Microsoft 365 E7**, GA el 1 de mayo de 2026) `[Verificado MS Learn]`. | Incorporado en Arquitectura, Cadencia `S-05`, Playbook `AH-02` y KPIs. |
| **5** | **Facturación MAU de Guests B2B y Exención MTO** | `microsoft-entra-id-governance-licensing-for-guest-users.md` (actualizado oct-2026) confirma que los huéspedes solo generan cargo MAU en Azure cuando usan funciones exclusivas de ID Governance (`GovernanceLicenseFeatureUsed == True`), máximo una vez al mes por huésped, y que los invitados provenientes de una **Multi-Tenant Organization (MTO)** quedan exentos del medidor `[Verificado MS Learn]`. | Integrado en `M-01`, `AH-04` y Consulta KQL #3. |
| **6** | **Cambio de permisos de `User Administrator` en Catálogos EM** | `entitlement-management-delegate.md` (actualizado ago-2026) advierte que `User Administrator` ya no puede crear catálogos ni administrar paquetes en catálogos ajenos; se exige migrar hacia `Identity Governance Administrator` y roles delegados por catálogo `[Verificado MS Learn]`. | Incorporado en la matriz RBAC de la Sección 4. |
| **7** | **Cuotas ampliadas de API-Driven Provisioning y límite ML de 600 miembros** | Con Entra ID Governance la cuota `/bulkUpload` sube de 100K a **300K registros/24h** y de 2 a **20 jobs por flujo**; asimismo, las recomendaciones ML **User-to-Group Affiliation** requieren atributo `manager` y soportan grupos de hasta **600 usuarios** `[Verificado MS Learn]`. | Reflejado en `D-02`, `M-02` y Sección 3.2. |

### 14.2 Registro Explícito de Decisiones y Propuestas Editoriales

| # | Elemento Decidido | Clasificación | Justificación Arquitectónica y Consultiva |
| --- | --- | --- | --- |
| **1** | **SLAs numéricos JML (`< 15 min` baja urgente, `< 3 h` baja programada, `< 4 h` remediación de fallos LCW)** | `[Decisión / Propuesta Editorial]` | Microsoft Learn define intervalos técnicos configurables (`1–24 h`, defecto `3 h`) y ejecución `Run on demand`, pero no impone SLAs contractuales internos; se fijan umbrales alineados a prácticas SOC Tier-1 y auditoría SOX/ISO 27001. |
| **2** | **Ventanas máximas de activación PIM (`2 h` para Privileged Role / Groups Admin, `4 h` para Identity Governance / Lifecycle Workflows Admin)** | `[Decisión / Propuesta Editorial]` | Acota la exposición temporal de credenciales administrativas sin generar fricción excesiva en ventanas operativas diarias de gobierno. |
| **3** | **Metas porcentuales de los 8 KPIs (`>= 98 %` onboarding automático, `>= 95 %` decisión explícita en AR, `100 %` ZSP y patrocinio)** | `[Decisión / Propuesta Editorial]` | Proporciona objetivos medibles para tableros ejecutivos del CISO y comités trimestrales de GRC evitando métricas ambiguas. |
| **4** | **Modelo de Madurez Operacional de 5 niveles (Ad-Hoc a Agéntico Frontier)** | `[Decisión / Propuesta Editorial]` | Permite diagnosticar la brecha entre clientes que solo usan P2 básico y organizaciones que gobiernan integralmente humanos, externos B2B y agentes IA. |
| **5** | **Mapeo probatorio cruzado a las 6 funciones de NIST CSF 2.0 y MITRE ATT&CK v18** | `[Decisión / Propuesta Editorial]` | Traduce controles nativos de Entra ID Governance al lenguaje estándar de auditoría externa y defensa informada por amenazas. |

---

## 15. Directorio de Referencias Públicas Verificadas

### Documentación Oficial Microsoft Learn
- **REF-01:** Microsoft Learn — *Microsoft Entra ID Governance overview* (`https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview`) — Verificado `2026-11-11` (actualizado `2026-10-29`).
- **REF-02:** Microsoft Learn — *Microsoft Entra ID Governance licensing fundamentals* (`https://learn.microsoft.com/en-us/entra/id-governance/licensing-fundamentals`) — Verificado `2026-11-11` (actualizado `2026-10-16`).
- **REF-03:** Microsoft Learn — *Microsoft Entra ID Governance licensing for guest users (MAU billing)* (`https://learn.microsoft.com/en-us/entra/id-governance/microsoft-entra-id-governance-licensing-for-guest-users`) — Verificado `2026-11-11` (actualizado `2026-10-06`).
- **REF-04:** Microsoft Learn — *Governing Agent Identities in Microsoft Entra ID Governance* (`https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview`) — Verificado `2026-11-11` (actualizado `2026-11-07`).
- **REF-05:** Microsoft Learn — *What are lifecycle workflows?* (`https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows`) — Verificado `2026-11-11`.
- **REF-06:** Microsoft Learn — *Understanding lifecycle workflows (Triggers V1/V2, Scheduling & Versioning)* (`https://learn.microsoft.com/en-us/entra/id-governance/understanding-lifecycle-workflows`) — Verificado `2026-11-11` (actualizado `2026-08-24`).
- **REF-07:** Microsoft Learn — *Lifecycle Workflows tasks and definitions* (`https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-tasks`) — Verificado `2026-11-11` (actualizado `2026-08-19`).
- **REF-08:** Microsoft Learn — *Microsoft Entra ID Governance service limits* (`https://learn.microsoft.com/en-us/entra/id-governance/governance-service-limits`) — Verificado `2026-11-11` (actualizado `2026-05-18`).
- **REF-09:** Microsoft Learn — *Delegation and roles in entitlement management* (`https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-delegate`) — Verificado `2026-11-11` (actualizado `2026-08-13`).
- **REF-10:** Microsoft Learn — *Configure separation of duties for an access package in entitlement management* (`https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-access-package-incompatible`) — Verificado `2026-11-11`.
- **REF-11:** Microsoft Learn — *Configure Verified ID settings and Face Check for an access package* (`https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-verified-id-settings`) — Verificado `2026-11-11`.
- **REF-12:** Microsoft Learn — *Review recommendations for Access reviews (Inactive users & ML User-to-Group Affiliation)* (`https://learn.microsoft.com/en-us/entra/id-governance/review-recommendations-access-reviews`) — Verificado `2026-11-11`.
- **REF-13:** Microsoft Learn — *Archive & report with Azure Monitor in entitlement management* (`https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-logs-and-reporting`) — Verificado `2026-11-11`.
- **REF-14:** Microsoft Learn — *Auditing Lifecycle Workflows* (`https://learn.microsoft.com/en-us/entra/id-governance/lifecycle-workflow-audits`) — Verificado `2026-11-11`.

### Blogs Oficiales y Empleados de Microsoft
- **REF-15:** Microsoft Entra Blog (Manmeet Bawa, Partner Director PM) — *The Microsoft Entra agent for smarter access governance: Access Review Agent* (`https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-microsoft-entra-agent-for-smarter-access-governance-access-review-agent/4279689`) — Verificado `2026-11-11`.
- **REF-16:** Merill Fernando (Microsoft Principal PM) — *Entra.News & Maester Open-Source Security Testing Framework* (`https://maester.dev/`) — Verificado `2026-11-11`.

### Comunidad MVP de Seguridad e Identidad
- **REF-17:** Fabian Bader (Microsoft Security MVP) — *Cloudbrothers: Entra ID Governance, Conditional Access & Token Protection Research* (`https://cloudbrothers.info/en/`) — Verificado `2026-11-11`.
- **REF-18:** Thomas Naunheim (Microsoft Security MVP) — *Cloud-Architekt: Enterprise Identity Governance, Workload & Privileged Access Architecture* (`https://www.cloud-architekt.net/blog/`) — Verificado `2026-11-11`.

### Marcos Normativos
- **REF-19:** National Institute of Standards and Technology (NIST) — *The NIST Cybersecurity Framework (CSF) 2.0 (NIST CSWP 29)* (`https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf`) — Verificado `2026-11-11`.
